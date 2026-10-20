#!/usr/bin/env python3
"""Monta o vídeo final de um episódio a partir de um edicao.yaml (substitui a edição no CapCut).

Faz: corta e junta os clipes, ajusta a velocidade, encaixa tudo em 1080x1920 (preenchendo ou com
faixas pretas), escreve o texto na tela e a marca d'água nos momentos pedidos, normaliza o volume
para o padrão das redes (-14 LUFS), mistura uma trilha opcional e exporta em H.264, 30 fps.

Uso:
  python3 montar.py canais/<canal>/episodios/epNN-<slug>/edicao.yaml
  python3 montar.py edicao.yaml --previa      # exporta rápido, em baixa qualidade, para conferir

Exemplo de edicao.yaml (caminhos relativos à pasta do yaml):

  saida: final.mp4
  clipes:
    - arquivo: clipes/cena1.mp4
      inicio: 0        # segundos (opcional)
      fim: 6           # segundos (opcional)
      velocidade: 1.0  # opcional
      modo: preencher  # preencher (corta as bordas) | caber (faixas pretas, ex.: dashcam 16:9)
      volume_db: 0     # opcional, ajuste do som deste clipe
      zoom: 1.06       # opcional, aproximação lenta até 106% no fim do clipe (bom para cenas paradas)
  textos:
    - texto: "eu domingo:"
      inicio: 0
      fim: 3
      posicao: topo    # topo | centro | baixo
      tamanho: 64      # opcional
  marca_dagua:
    texto: "@galinhadecalca"
    momentos: [[2, 5], [10, 13]]
  audio:
    normalizar: true
    trilha: null       # caminho de um mp3/m4a da biblioteca, opcional
    trilha_db: -20

Texto da tela: se o Playwright e um Chromium estiverem instalados, cada texto é renderizado em HTML
(emoji colorido + animação de entrada e saída, via texto_html.py). Sem eles, cai no drawtext do
ffmpeg, que não mostra emoji. Para forçar o modo simples: `estilo: simples` no texto.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import texto_html  # noqa: E402

try:
    import yaml
except ImportError:
    sys.exit("Falta o PyYAML. Rode: pip install pyyaml")

W, H, FPS = 1080, 1920, 30
FONTES = [
    "/usr/share/fonts/opentype/inter/Inter-Bold.otf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",  # macOS
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]
EMOJI = re.compile("[\U0001F000-\U0001FAFF☀-➿️‍]")


def fonte_padrao() -> str:
    for f in FONTES:
        if Path(f).exists():
            return f
    sys.exit("Nenhuma fonte encontrada; informe 'fonte:' no edicao.yaml.")


def duracao_de(path: Path) -> float:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                         capture_output=True, text=True).stdout.strip()
    return float(out or 0)


def tem_audio(path: Path) -> bool:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=index",
         "-of", "csv=p=0", str(path)],
        capture_output=True, text=True,
    ).stdout.strip()
    return bool(out)


def atempo(v: float) -> str:
    """O atempo do ffmpeg aceita de 0,5 a 2 por estágio: encadeia quando preciso."""
    parts = []
    while v > 2.0:
        parts.append("atempo=2.0")
        v /= 2.0
    while v < 0.5:
        parts.append("atempo=0.5")
        v /= 0.5
    parts.append(f"atempo={v:.4f}")
    return ",".join(parts)


def y_pos(posicao: str) -> str:
    return {"topo": "h*0.16", "centro": "(h-text_h)/2", "baixo": "h*0.78"}.get(posicao, "h*0.16")


def montar(spec_path: Path, previa: bool) -> Path:
    base = spec_path.parent
    spec = yaml.safe_load(spec_path.read_text(encoding="utf-8"))
    fonte = spec.get("fonte") or fonte_padrao()
    clipes = spec.get("clipes") or []
    if not clipes:
        sys.exit("edicao.yaml sem clipes.")

    tmp = Path(tempfile.mkdtemp(prefix="montar-"))
    inputs: list[str] = []
    filtros: list[str] = []
    duracao_total = 0.0

    for i, c in enumerate(clipes):
        arq = (base / c["arquivo"]).resolve()
        if not arq.exists():
            sys.exit(f"Clipe não encontrado: {arq}")
        ini = float(c.get("inicio", 0))
        fim = c.get("fim")
        vel = float(c.get("velocidade", 1.0))
        trim_args = ["-ss", f"{ini}"] + (["-to", f"{float(fim)}"] if fim is not None else [])
        inputs += [*trim_args, "-i", str(arq)]

        if c.get("modo", "preencher") == "caber":
            enquadra = (f"scale={W}:{H}:force_original_aspect_ratio=decrease,"
                        f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:black")
        else:
            enquadra = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}"
        zoom = float(c.get("zoom", 1.0))
        if zoom > 1.0:
            # Aproximação lenta ao longo do clipe (dica de edição do rixardê para cenas paradas).
            dur_clip = (float(fim) if fim is not None else duracao_de(arq)) - ini
            enquadra += (f",scale=w='trunc({W}*(1+({zoom}-1)*t/{dur_clip:.3f})/2)*2':h=-2:eval=frame,"
                         f"crop={W}:{H}")
        filtros.append(f"[{i}:v]{enquadra},setsar=1,fps={FPS},setpts=(PTS-STARTPTS)/{vel}[v{i}]")

        vol = float(c.get("volume_db", 0))
        if tem_audio(arq):
            filtros.append(
                f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo,asetpts=PTS-STARTPTS,"
                f"{atempo(vel)},volume={vol}dB[a{i}]"
            )
        else:
            # Clipe mudo: gera silêncio com a mesma duração para o concat não quebrar.
            dur = float(subprocess.run(
                ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(arq)],
                capture_output=True, text=True).stdout.strip())
            seg = ((float(fim) if fim is not None else dur) - ini) / vel
            filtros.append(f"anullsrc=r=48000:cl=stereo,atrim=0:{seg:.3f}[a{i}]")
        duracao_total += ((float(fim) if fim is not None else 1e9) - ini) / vel

    n = len(clipes)
    filtros.append("".join(f"[v{i}][a{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=1[vcat][acat]")

    # Textos: em HTML (emoji + animação) quando possível; senão drawtext do ffmpeg.
    chromium = texto_html.disponivel()
    ultimo = "vcat"
    textos_simples = []
    k_in = n
    for j, t in enumerate(spec.get("textos") or []):
        ini_t, fim_t = float(t.get("inicio", 0)), float(t.get("fim", 3))
        if chromium and t.get("estilo", "animado") != "simples":
            padrao = texto_html.renderizar(t["texto"], fim_t - ini_t, t.get("posicao", "topo"),
                                           int(t.get("tamanho", 64)), tmp / f"html{j}", chromium)
            inputs += ["-framerate", str(FPS), "-i", str(padrao)]
            filtros.append(f"[{k_in}:v]setpts=PTS-STARTPTS+{ini_t}/TB[ov{j}]")
            filtros.append(f"[{ultimo}][ov{j}]overlay=0:0:eof_action=pass[vt{j}]")
            ultimo = f"vt{j}"
            k_in += 1
        else:
            textos_simples.append(t)

    # Texto simples e marca d'água (via textfile=, que evita os problemas de escape do drawtext).
    desenhos = []
    for j, t in enumerate(textos_simples):
        texto = EMOJI.sub("", t["texto"]).strip()
        if texto != t["texto"].strip():
            print(f"aviso: emoji removido do texto da tela: {t['texto']!r}", file=sys.stderr)
        tf = tmp / f"texto{j}.txt"
        tf.write_text(texto, encoding="utf-8")
        tam = int(t.get("tamanho", 64))
        desenhos.append(
            f"drawtext=fontfile='{fonte}':textfile='{tf}':fontsize={tam}:fontcolor=white:"
            f"borderw=4:bordercolor=black@0.85:x=(w-text_w)/2:y={y_pos(t.get('posicao', 'topo'))}:"
            f"enable='between(t,{float(t.get('inicio', 0))},{float(t.get('fim', 3))})'"
        )
    md = spec.get("marca_dagua")
    if md and md.get("texto"):
        tf = tmp / "marca.txt"
        tf.write_text(md["texto"], encoding="utf-8")
        for a, b in md.get("momentos") or [[0, 9999]]:
            desenhos.append(
                f"drawtext=fontfile='{fonte}':textfile='{tf}':fontsize=38:fontcolor=white@0.45:"
                f"borderw=2:bordercolor=black@0.35:x=w-text_w-48:y=h*0.86:"
                f"enable='between(t,{float(a)},{float(b)})'"
            )
    if desenhos:
        filtros.append(f"[{ultimo}]{','.join(desenhos)}[vout]")
        ultimo = "vout"

    # Áudio: trilha opcional + normalização.
    audio = spec.get("audio") or {}
    a_final = "acat"
    trilha = audio.get("trilha")
    if trilha:
        tr = (base / trilha).resolve()
        inputs += ["-stream_loop", "-1", "-i", str(tr)]
        filtros.append(f"[{k_in}:a]aresample=48000,aformat=channel_layouts=stereo,"
                       f"volume={float(audio.get('trilha_db', -20))}dB[trilha]")
        filtros.append("[acat][trilha]amix=inputs=2:duration=first:dropout_transition=0[amix]")
        a_final = "amix"
    if audio.get("normalizar", True):
        filtros.append(f"[{a_final}]loudnorm=I=-14:TP=-1.5:LRA=11[aout]")
        a_final = "aout"

    saida = (base / spec.get("saida", "final.mp4")).resolve()
    if previa:
        saida = saida.with_name(saida.stem + "-previa.mp4")
    qualidade = (["-preset", "veryfast", "-crf", "30"] if previa else ["-preset", "medium", "-crf", "18"])
    cmd = [
        "ffmpeg", "-v", "error", "-y", *inputs,
        "-filter_complex", ";".join(filtros),
        "-map", f"[{ultimo}]", "-map", f"[{a_final}]",
        "-c:v", "libx264", *qualidade, "-pix_fmt", "yuv420p", "-r", str(FPS),
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
        "-movflags", "+faststart", str(saida),
    ]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        print("Falhou. Grafo de filtros usado:\n" + ";\n".join(filtros), file=sys.stderr)
        raise
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return saida


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("spec", help="caminho do edicao.yaml")
    p.add_argument("--previa", action="store_true", help="exporta rápido, em baixa qualidade")
    args = p.parse_args()
    saida = montar(Path(args.spec), args.previa)
    info = json.loads(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=width,height,codec_name",
         "-of", "json", str(saida)], capture_output=True, text=True).stdout)
    v = next(s for s in info["streams"] if s.get("width"))
    print(f"OK  {saida}  [{v['width']}x{v['height']}, {float(info['format']['duration']):.1f}s]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
