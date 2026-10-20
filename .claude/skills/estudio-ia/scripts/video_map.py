#!/usr/bin/env python3
"""Mapeia um vídeo de referência (TikTok, YouTube Shorts, Instagram, arquivo local) para modelagem.

Gera numa pasta:
  video.mp4           o vídeo baixado
  frames/cena-NN.jpg  um quadro do meio de cada cena (candidatas a imagem âncora)
  contato.jpg         folha de contato com todas as cenas numeradas, para ver de uma vez
  mapa.md             metadados + tabela de cenas com tempo, duração e falas de cada trecho

Uso:
  python3 video_map.py URL_OU_ARQUIVO --out referencias/<nome>
  python3 video_map.py URL --out DIR --threshold 0.25   # mais sensível a cortes
  python3 video_map.py URL --out DIR --no-transcribe    # pula a transcrição (mais rápido)

Dependências: pip install -r requirements.txt  (e ffmpeg instalado no sistema)
"""

from __future__ import annotations

import argparse
import json
import math
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path


def run(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, check=True, capture_output=True, text=kw.pop("text", True), **kw)


def ts(seconds: float) -> str:
    m, s = divmod(seconds, 60)
    return f"{int(m):02d}:{s:04.1f}"


def download(src: str, out: Path) -> tuple[Path, dict]:
    local = Path(src)
    if local.exists():
        dest = out / ("video" + local.suffix)
        shutil.copy(local, dest)
        return dest, {"title": local.stem, "url": str(local)}
    try:
        import yt_dlp
    except ImportError:
        sys.exit("Falta o yt-dlp. Rode: pip install -r requirements.txt")
    opts = {
        "quiet": True,
        "no_warnings": True,
        "noprogress": True,
        "outtmpl": str(out / "video.%(ext)s"),
        "format": "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]/bv*+ba/b",
        "merge_output_format": "mp4",
    }
    with yt_dlp.YoutubeDL(opts) as y:
        info = y.extract_info(src, download=True)
    path = next(out.glob("video.*"))
    meta = {
        "title": info.get("title") or info.get("description", "")[:80],
        "url": info.get("webpage_url") or src,
        "uploader": info.get("uploader") or info.get("channel"),
        "upload_date": info.get("upload_date"),
        "views": info.get("view_count"),
        "likes": info.get("like_count"),
        "comments": info.get("comment_count"),
        "description": info.get("description") or "",
    }
    return path, meta


def probe(path: Path) -> dict:
    out = run([
        "ffprobe", "-v", "error", "-select_streams", "v:0",
        "-show_entries", "stream=width,height,r_frame_rate:format=duration",
        "-of", "json", str(path),
    ]).stdout
    data = json.loads(out)
    st = data["streams"][0]
    num, den = st["r_frame_rate"].split("/")
    return {
        "duration": float(data["format"]["duration"]),
        "width": st["width"],
        "height": st["height"],
        "fps": round(float(num) / float(den), 2),
    }


def detect_cuts(path: Path, threshold: float, min_len: float) -> list[float]:
    proc = subprocess.run(
        ["ffmpeg", "-hide_banner", "-i", str(path), "-vf", f"select='gt(scene,{threshold})',showinfo",
         "-vsync", "vfr", "-f", "null", "-"],
        capture_output=True, text=True,
    )
    cuts, last = [], 0.0
    for m in re.finditer(r"pts_time:([0-9.]+)", proc.stderr):
        t = float(m.group(1))
        if t - last >= min_len:  # ignora flashes e cortes muito colados
            cuts.append(t)
            last = t
    return cuts


def extract_frames(path: Path, scenes: list[tuple[float, float]], frames_dir: Path) -> list[Path]:
    frames_dir.mkdir(exist_ok=True)
    paths = []
    for i, (start, end) in enumerate(scenes, 1):
        # Um pouco depois do início: pega a "imagem âncora" antes da animação andar muito.
        t = start + min(0.4, (end - start) * 0.25)
        dest = frames_dir / f"cena-{i:02d}.jpg"
        run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.3f}", "-i", str(path),
             "-frames:v", "1", "-q:v", "3", "-vf", "scale=540:-2", str(dest)])
        paths.append(dest)
    return paths


def contact_sheet(frames: list[Path], dest: Path) -> None:
    """Numera cada quadro e junta tudo numa grade (o filtro tile completa a grade sozinho)."""
    cols = 5 if len(frames) > 8 else 4
    rows = math.ceil(len(frames) / cols)
    tmp = dest.parent / ".contato"
    tmp.mkdir(exist_ok=True)
    for i, f in enumerate(frames, 1):
        run(["ffmpeg", "-v", "error", "-y", "-i", str(f), "-vf",
             f"scale=270:480:force_original_aspect_ratio=decrease,pad=270:480:(ow-iw)/2:(oh-ih)/2,"
             f"drawtext=text='{i}':x=10:y=10:fontsize=34:fontcolor=white:box=1:boxcolor=black@0.65:boxborderw=8",
             str(tmp / f"{i:03d}.jpg")])
    run(["ffmpeg", "-v", "error", "-y", "-framerate", "1", "-i", str(tmp / "%03d.jpg"),
         "-vf", f"tile={cols}x{rows}:padding=4:color=black", "-frames:v", "1", "-q:v", "3", str(dest)])
    shutil.rmtree(tmp)


def transcribe(path: Path, model_size: str) -> tuple[list[dict], str] | None:
    try:
        import numpy as np
        from faster_whisper import WhisperModel
    except ImportError:
        print("faster-whisper não instalado: pulando transcrição", file=sys.stderr)
        return None
    # Decodifica com o ffmpeg em vez do PyAV do faster-whisper, que quebra com algumas versões.
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(path), "-ac", "1", "-ar", "16000", "-f", "f32le", "-"],
        capture_output=True, check=True,
    ).stdout
    if not raw:
        return None
    audio = np.frombuffer(raw, np.float32)
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    segments, info = model.transcribe(audio, vad_filter=True)
    return [{"start": s.start, "end": s.end, "text": s.text.strip()} for s in segments], info.language


def render(meta: dict, info: dict, scenes, frames, transcript, out: Path) -> str:
    lines = [f"# Mapa — {meta.get('title') or 'vídeo de referência'}", ""]
    lines += [
        f"- **Fonte:** {meta.get('url')}",
        f"- **Perfil:** {meta.get('uploader') or '—'}",
        f"- **Views / likes / comentários:** {meta.get('views') or '—'} / {meta.get('likes') or '—'} / {meta.get('comments') or '—'}",
        f"- **Duração:** {info['duration']:.1f}s · {info['width']}x{info['height']} · {info['fps']} fps",
        f"- **Cenas detectadas:** {len(scenes)} (corte médio a cada {info['duration'] / max(len(scenes), 1):.1f}s)",
        f"- **Mapeado em:** {date.today().isoformat()}",
    ]
    if meta.get("description"):
        lines += ["", "## Legenda do post", "", meta["description"].strip()]
    lines += ["", "## Folha de contato", "", "![contato](contato.jpg)", "", "## Cenas", ""]
    lines += ["| # | Início | Duração | Quadro | Fala / áudio neste trecho |", "|---|---|---|---|---|"]
    for i, ((start, end), frame) in enumerate(zip(scenes, frames), 1):
        said = ""
        if transcript:
            said = " ".join(
                s["text"] for s in transcript[0] if s["start"] < end and s["end"] > start
            ).replace("|", "/")
        lines.append(f"| {i} | {ts(start)} | {end - start:.1f}s | ![]({frame.relative_to(out)}) | {said or '—'} |")
    lines += ["", "## Transcrição completa", ""]
    if transcript:
        lines.append(f"_Idioma detectado: {transcript[1]} (Whisper, pode ter erros)_")
        lines.append("")
        lines += [f"**[{ts(s['start'])}]** {s['text']}" for s in transcript[0]]
    else:
        lines.append("_Sem transcrição (vídeo sem fala ou transcrição desativada)._")
    lines += [
        "",
        "## Storyboard de imagens âncora",
        "",
        "_A preencher pelo Claude depois de olhar os quadros: junte cortes que são só movimento da mesma "
        "imagem âncora, descreva cada âncora (enquadramento, ação, câmera, luz) e anote o que acontece na animação._",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("src", help="URL (TikTok, Shorts, Reels…) ou caminho de um arquivo de vídeo")
    p.add_argument("--out", required=True, help="pasta de saída")
    p.add_argument("--threshold", type=float, default=0.3, help="sensibilidade de corte (0.2 = mais cortes)")
    p.add_argument("--min-scene", type=float, default=0.6, help="duração mínima de uma cena, em segundos")
    p.add_argument("--whisper", default="small", help="modelo do Whisper: tiny, base, small, medium")
    p.add_argument("--no-transcribe", action="store_true")
    args = p.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    video, meta = download(args.src, out)
    info = probe(video)
    cuts = detect_cuts(video, args.threshold, args.min_scene)
    bounds = [0.0, *cuts, info["duration"]]
    scenes = [(a, b) for a, b in zip(bounds, bounds[1:]) if b - a > 0.05]
    frames = extract_frames(video, scenes, out / "frames")
    try:
        contact_sheet(frames, out / "contato.jpg")
    except subprocess.CalledProcessError as e:
        print(f"aviso: não consegui montar a folha de contato ({e.stderr[:200]})", file=sys.stderr)
    transcript = None if args.no_transcribe else transcribe(video, args.whisper)
    (out / "mapa.md").write_text(render(meta, info, scenes, frames, transcript, out), encoding="utf-8")
    print(f"OK  {out}/mapa.md  [{len(scenes)} cenas, {info['duration']:.0f}s, "
          f"{'com' if transcript else 'sem'} transcrição]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
