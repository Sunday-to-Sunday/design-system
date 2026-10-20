#!/usr/bin/env python3
"""Extrai metadados, capítulos e transcrição de vídeos do YouTube.

Uso:
  # Um ou mais vídeos -> gera um .md por vídeo pronto para análise
  python3 yt_extract.py video URL_OU_ID [URL_OU_ID ...] --out DIR

  # Descobrir vídeos sobre um tema (ordenados por visualizações)
  python3 yt_extract.py search "ganhar dinheiro com ia tiktok" --limit 15

  # Listar os vídeos mais recentes de um canal ou playlist
  python3 yt_extract.py list https://www.youtube.com/@canal/videos --limit 20

Dependências: pip install -r requirements.txt
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

try:
    import yt_dlp
except ImportError:
    sys.exit("Falta o yt-dlp. Rode: pip install -r requirements.txt")

try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    YouTubeTranscriptApi = None

# Ordem de preferência das legendas: português primeiro, depois inglês e espanhol.
LANGS = ["pt-BR", "pt", "pt-PT", "en", "en-US", "en-GB", "es", "es-419"]

ID_RE = re.compile(r"(?:v=|youtu\.be/|shorts/|embed/|live/)([A-Za-z0-9_-]{11})")


def video_id(ref: str) -> str:
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", ref):
        return ref
    m = ID_RE.search(ref)
    if not m:
        raise ValueError(f"Não reconheci um ID de vídeo em: {ref}")
    return m.group(1)


def slugify(text: str, max_len: int = 60) -> str:
    text = text.lower()
    text = re.sub(r"[àáâãä]", "a", text)
    text = re.sub(r"[èéêë]", "e", text)
    text = re.sub(r"[ìíîï]", "i", text)
    text = re.sub(r"[òóôõö]", "o", text)
    text = re.sub(r"[ùúûü]", "u", text)
    text = text.replace("ç", "c")
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text[:max_len].rstrip("-") or "video"


def ts(seconds: float) -> str:
    s = int(seconds)
    h, rem = divmod(s, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


COOKIES: str | None = None


def ydl(extra: dict | None = None) -> yt_dlp.YoutubeDL:
    opts = {"quiet": True, "no_warnings": True, "skip_download": True, "logger": _SilentLogger()}
    if COOKIES:
        opts["cookiefile"] = COOKIES
    opts.update(extra or {})
    return yt_dlp.YoutubeDL(opts)


class _SilentLogger:
    def debug(self, msg): pass
    def info(self, msg): pass
    def warning(self, msg): pass
    def error(self, msg): pass


def fetch_metadata(vid: str) -> dict:
    """Metadados completos via yt-dlp; se o YouTube bloquear, cai para o oEmbed (só título e canal)."""
    url = f"https://www.youtube.com/watch?v={vid}"
    try:
        with ydl() as y:
            info = y.extract_info(url, download=False)
    except Exception as e:
        # O cliente do player embutido costuma escapar do "confirme que não é um robô" em IPs de nuvem.
        # Ele não traz formatos de vídeo, mas traz descrição, números e legendas, que é o que importa aqui.
        try:
            with ydl({
                "ignore_no_formats_error": True,
                "extractor_args": {"youtube": {"player_client": ["web_embedded"]}},
            }) as y:
                info = y.extract_info(url, download=False)
        except Exception:
            return fetch_oembed(vid, reason=str(e).splitlines()[0])
    upload = info.get("upload_date")
    return {
        "id": vid,
        "url": f"https://www.youtube.com/watch?v={vid}",
        "title": info.get("title"),
        "channel": info.get("channel") or info.get("uploader"),
        "channel_url": info.get("channel_url"),
        "subscribers": info.get("channel_follower_count"),
        "upload_date": datetime.strptime(upload, "%Y%m%d").date().isoformat() if upload else None,
        "duration": info.get("duration"),
        "views": info.get("view_count"),
        "likes": info.get("like_count"),
        "comments": info.get("comment_count"),
        "language": info.get("language"),
        "tags": info.get("tags") or [],
        "description": info.get("description") or "",
        "chapters": [
            {"start": c.get("start_time", 0), "title": c.get("title", "")}
            for c in (info.get("chapters") or [])
        ],
        "_subtitles": info.get("subtitles") or {},
        "_auto_captions": info.get("automatic_captions") or {},
        "_partial": None,
    }


def fetch_oembed(vid: str, reason: str) -> dict:
    import urllib.parse
    import urllib.request

    url = f"https://www.youtube.com/watch?v={vid}"
    with urllib.request.urlopen(
        "https://www.youtube.com/oembed?format=json&url=" + urllib.parse.quote(url), timeout=30
    ) as r:
        data = json.load(r)
    return {
        "id": vid, "url": url, "title": data.get("title"),
        "channel": data.get("author_name"), "channel_url": data.get("author_url"),
        "subscribers": None, "upload_date": None, "duration": None, "views": None,
        "likes": None, "comments": None, "language": None, "tags": [], "description": "",
        "chapters": [], "_subtitles": {}, "_auto_captions": {},
        "_partial": reason,
    }


def transcript_via_api(vid: str) -> tuple[list[dict], str] | None:
    if YouTubeTranscriptApi is None:
        return None
    api = YouTubeTranscriptApi()
    try:
        listing = api.list(vid)
    except Exception:
        return None
    available = list(listing)
    if not available:
        return None
    # Prefere legenda manual no idioma preferido, depois automática, depois qualquer uma.
    ranked = sorted(
        available,
        key=lambda t: (
            LANGS.index(t.language_code) if t.language_code in LANGS else len(LANGS),
            t.is_generated,
        ),
    )
    chosen = ranked[0]
    try:
        fetched = chosen.fetch()
    except Exception:
        return None
    label = f"{chosen.language_code}{' (automática)' if chosen.is_generated else ''}"
    return [{"start": s.start, "text": s.text} for s in fetched.snippets], label


def transcript_via_ytdlp(meta: dict) -> tuple[list[dict], str] | None:
    """Fallback: baixa a faixa json3 que o yt-dlp já listou nos metadados."""
    import time
    import urllib.request

    spoken = meta.get("language")
    auto_keys = meta["_auto_captions"].keys()
    # Nas legendas automáticas, "<idioma>-orig" é o reconhecimento de fala original;
    # as demais chaves são traduções de máquina, então só aceitamos os idiomas preferidos.
    auto_order = (
        ([f"{spoken}-orig", spoken] if spoken else [])
        + [k for k in auto_keys if k.endswith("-orig")]
        + LANGS
    )
    manual_order = LANGS + list(meta["_subtitles"].keys())

    for source, order, auto in (
        (meta["_subtitles"], manual_order, False),
        (meta["_auto_captions"], auto_order, True),
    ):
        tried = set()
        for lang in order:
            if lang in tried:
                continue
            tried.add(lang)
            tracks = source.get(lang) or []
            track = next((t for t in tracks if t.get("ext") == "json3"), None)
            if not track:
                continue
            data = None
            for attempt in range(3):  # o endpoint de legendas costuma responder 429 de vez em quando
                try:
                    with urllib.request.urlopen(track["url"], timeout=30) as r:
                        data = json.load(r)
                    break
                except Exception:
                    time.sleep(2 * (attempt + 1))
            if data is None:
                continue
            lang = lang.removesuffix("-orig")
            lines = []
            for ev in data.get("events", []):
                text = "".join(seg.get("utf8", "") for seg in ev.get("segs") or []).strip()
                if text:
                    lines.append({"start": ev.get("tStartMs", 0) / 1000, "text": text})
            if lines:
                return lines, f"{lang}{' (automática)' if auto else ''}"
    return None


def transcript_from_file(path: Path) -> tuple[list[dict], str]:
    """Transcrição colada pelo usuário (ex.: "Mostrar transcrição" do YouTube), com ou sem timestamps."""
    lines, current = [], 0.0
    stamp = re.compile(r"^\s*\[?(\d{1,2}(?::\d{2}){1,2})\]?\s*(.*)$")
    for raw in path.read_text(encoding="utf-8").splitlines():
        m = stamp.match(raw)
        if m:
            parts = [int(x) for x in m.group(1).split(":")]
            current = float(sum(v * 60**i for i, v in enumerate(reversed(parts))))
            raw = m.group(2)
        if raw.strip():
            lines.append({"start": current, "text": raw.strip()})
    return lines, f"arquivo {path.name}"


def group_paragraphs(lines: list[dict], window: float = 30.0) -> list[tuple[float, str]]:
    """Junta as falas em blocos de ~30s com timestamp, mais fácil de ler e citar."""
    paras: list[tuple[float, str]] = []
    start, buf = None, []
    for ln in lines:
        text = ln["text"].replace("\n", " ").strip()
        if not text:
            continue
        if start is None:
            start = ln["start"]
        if ln["start"] - start >= window and buf:
            paras.append((start, " ".join(buf)))
            start, buf = ln["start"], []
        buf.append(text)
    if buf:
        paras.append((start or 0, " ".join(buf)))
    return paras


def fmt_num(n) -> str:
    return f"{n:,}".replace(",", ".") if isinstance(n, int) else "—"


def render_markdown(meta: dict, transcript: tuple[list[dict], str] | None) -> str:
    out = [f"# {meta['title']}", ""]
    out += [
        f"- **URL:** {meta['url']}",
        f"- **Canal:** {meta['channel']} ({fmt_num(meta['subscribers'])} inscritos) — {meta['channel_url']}",
        f"- **Publicado em:** {meta['upload_date'] or '—'}",
        f"- **Duração:** {ts(meta['duration']) if meta['duration'] else '—'}",
        f"- **Views / likes / comentários:** {fmt_num(meta['views'])} / {fmt_num(meta['likes'])} / {fmt_num(meta['comments'])}",
        f"- **Extraído em:** {datetime.now().date().isoformat()}",
    ]
    if meta["_partial"]:
        out.append(
            "- **Atenção:** metadados parciais (o YouTube bloqueou o yt-dlp: "
            f"{meta['_partial'][:120]}). Rode com `--cookies cookies.txt` para obter "
            "descrição, capítulos e números."
        )
    if meta["tags"]:
        out.append(f"- **Tags:** {', '.join(meta['tags'][:20])}")
    out += ["", "## Descrição", "", meta["description"].strip() or "_(sem descrição)_", ""]
    if meta["chapters"]:
        out += ["## Capítulos", ""]
        out += [f"- [{ts(c['start'])}] {c['title']}" for c in meta["chapters"]]
        out.append("")
    out.append("## Transcrição")
    out.append("")
    if transcript:
        lines, label = transcript
        out += [f"_Idioma da legenda: {label}_", ""]
        out += [f"**[{ts(start)}]** {text}" for start, text in group_paragraphs(lines)]
    else:
        out.append(
            "_Transcrição indisponível (vídeo sem legendas ou bloqueado). "
            "Analise só pelos metadados ou peça ao usuário um vídeo alternativo._"
        )
    out.append("")
    return "\n".join(out)


def cmd_video(args) -> int:
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    failures = 0
    for ref in args.refs:
        try:
            vid = video_id(ref)
            meta = fetch_metadata(vid)
        except Exception as e:
            print(f"ERRO  {ref}: {e}", file=sys.stderr)
            failures += 1
            continue
        if args.transcript:
            transcript = transcript_from_file(Path(args.transcript))
        else:
            transcript = transcript_via_api(vid) or transcript_via_ytdlp(meta)
        path = out_dir / f"{slugify(meta['title'])}-{vid}.md"
        path.write_text(render_markdown(meta, transcript), encoding="utf-8")
        status = transcript[1] if transcript else "SEM TRANSCRIÇÃO"
        if meta["_partial"]:
            status += ", metadados parciais"
        print(f"OK    {path}  [{status}]")
    return 1 if failures == len(args.refs) else 0


def print_entries(entries: list[dict], sort_by_views: bool) -> None:
    if sort_by_views:
        entries = sorted(entries, key=lambda e: e.get("view_count") or 0, reverse=True)
    for e in entries:
        dur = ts(e["duration"]) if e.get("duration") else "--:--"
        print(
            f"{fmt_num(e.get('view_count')):>13} views | {dur:>8} | "
            f"{(e.get('channel') or e.get('uploader') or '?')[:28]:<28} | "
            f"{e.get('title')} | https://youtu.be/{e.get('id')}"
        )


def cmd_search(args) -> int:
    with ydl({"extract_flat": True}) as y:
        info = y.extract_info(f"ytsearch{args.limit}:{args.query}", download=False)
    print_entries(info.get("entries") or [], sort_by_views=True)
    return 0


def cmd_list(args) -> int:
    with ydl({"extract_flat": True, "playlistend": args.limit}) as y:
        info = y.extract_info(args.url, download=False)
    print_entries(info.get("entries") or [], sort_by_views=args.by_views)
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--cookies", help="cookies.txt (formato Netscape) para contornar o bloqueio anti-bot")
    sub = p.add_subparsers(dest="cmd", required=True)

    v = sub.add_parser("video", help="extrai metadados + transcrição de um ou mais vídeos")
    v.add_argument("refs", nargs="+", help="URLs ou IDs de vídeos")
    v.add_argument("--out", default="knowledge/tiktok-ia/videos/raw", help="pasta de saída")
    v.add_argument("--transcript", help="usa uma transcrição salva em arquivo (quando o YouTube bloquear)")
    v.set_defaults(func=cmd_video)

    s = sub.add_parser("search", help="busca vídeos no YouTube por tema")
    s.add_argument("query")
    s.add_argument("--limit", type=int, default=15)
    s.set_defaults(func=cmd_search)

    ls = sub.add_parser("list", help="lista vídeos de um canal ou playlist")
    ls.add_argument("url")
    ls.add_argument("--limit", type=int, default=20)
    ls.add_argument("--by-views", action="store_true", help="ordena por visualizações")
    ls.set_defaults(func=cmd_list)

    args = p.parse_args()
    global COOKIES
    COOKIES = args.cookies
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
