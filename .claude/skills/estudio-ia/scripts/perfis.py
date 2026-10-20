#!/usr/bin/env python3
"""Analisa perfis de referência do TikTok: melhores horários, dias, durações e hashtags.

Para cada perfil, baixa os metadados dos vídeos (sem baixar os vídeos), normaliza as views pelo
próprio perfil (um vídeo "forte" é forte em relação à média daquele perfil, não ao do vizinho) e
compara os 25% melhores com o resto. Método inspirado no rixardê (Apify + GPT), sem precisar de conta.

Uso:
  python3 perfis.py @perfil1 @perfil2 @perfil3 --limite 60 --out canais/<canal>/referencias/perfis.md
  python3 perfis.py @perfil1 --fuso America/Sao_Paulo      # fuso para ler os horários (padrão: Brasília)

Saída: um relatório .md e um .csv com todos os vídeos, ao lado.
"""

from __future__ import annotations

import argparse
import csv
import time
import re
import statistics
import sys
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

try:
    import yt_dlp
except ImportError:
    sys.exit("Falta o yt-dlp (e o curl_cffi para o TikTok). Rode: pip install -r requirements.txt")

DIAS = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
HASHTAG = re.compile(r"#([\wÀ-ÿ]+)")


def coletar(perfil: str, limite: int) -> list[dict]:
    nome = perfil.lstrip("@")
    opts = {"quiet": True, "no_warnings": True, "skip_download": True, "playlistend": limite,
            "ignoreerrors": True}
    info = None
    for tentativa in range(4):  # o TikTok às vezes responde vazio por limite de requisições
        with yt_dlp.YoutubeDL(opts) as y:
            info = y.extract_info(f"https://www.tiktok.com/@{nome}", download=False)
        if info and info.get("entries"):
            break
        time.sleep(30 * (tentativa + 1))
    videos = []
    for e in (info or {}).get("entries") or []:
        if not e or not e.get("timestamp"):
            continue
        desc = e.get("description") or ""
        videos.append({
            "perfil": nome,
            "id": e.get("id"),
            "url": e.get("webpage_url") or f"https://www.tiktok.com/@{nome}/video/{e.get('id')}",
            "timestamp": e["timestamp"],
            "views": e.get("view_count") or 0,
            "likes": e.get("like_count") or 0,
            "comentarios": e.get("comment_count") or 0,
            "compartilhamentos": e.get("repost_count") or 0,
            "duracao": e.get("duration") or 0,
            "hashtags": [h.lower() for h in HASHTAG.findall(desc)],
            "descricao": desc.replace("\n", " ")[:120],
        })
    return videos


def faixa(h: int) -> str:
    return f"{h:02d}h–{(h + 1) % 24:02d}h"


def relatorio(videos: list[dict], fuso: str) -> str:
    tz = ZoneInfo(fuso)
    por_perfil = defaultdict(list)
    for v in videos:
        dt = datetime.fromtimestamp(v["timestamp"], tz)
        v["hora"], v["dia"] = dt.hour, dt.weekday()
        v["data"] = dt.strftime("%Y-%m-%d %H:%M")
        por_perfil[v["perfil"]].append(v)
    # Índice de força: views do vídeo / mediana do perfil.
    for vs in por_perfil.values():
        med = statistics.median([v["views"] for v in vs]) or 1
        for v in vs:
            v["forca"] = v["views"] / med
    todos = sorted(videos, key=lambda v: v["forca"], reverse=True)
    corte = max(1, len(todos) // 4)
    topo, resto = todos[:corte], todos[corte:]

    def taxa(grupo, chave, valor):
        return sum(1 for v in grupo if v[chave] == valor)

    linhas = [f"# Análise de perfis de referência — {date.today().isoformat()}", ""]
    linhas.append(f"- **Perfis:** {', '.join('@' + p for p in por_perfil)}")
    linhas.append(f"- **Vídeos analisados:** {len(videos)} · **topo (25% mais fortes):** {len(topo)}")
    linhas.append(f"- **Fuso dos horários:** {fuso}")
    linhas.append("- **Força** = views do vídeo ÷ mediana de views do próprio perfil (1,0 = vídeo típico do perfil).")
    linhas += ["", "## Perfis", "", "| Perfil | Vídeos | Mediana de views | Melhor vídeo | Duração mediana |", "|---|---|---|---|---|"]
    for p, vs in por_perfil.items():
        melhor = max(vs, key=lambda v: v["views"])
        linhas.append(f"| @{p} | {len(vs)} | {statistics.median([v['views'] for v in vs]):,.0f} | "
                      f"[{melhor['views']:,}]({melhor['url']}) | {statistics.median([v['duracao'] for v in vs]):.0f}s |")

    linhas += ["", "## Horário de postagem", "",
               "Quanto maior a diferença entre a coluna do topo e a de todos, mais aquele horário aparece nos vídeos fortes.", "",
               "| Faixa | % dos vídeos do topo | % de todos os vídeos | Força média |", "|---|---|---|---|"]
    horas = []
    for h in range(24):
        n_topo, n_todos = taxa(topo, "hora", h), taxa(todos, "hora", h)
        if n_todos == 0:
            continue
        forca = statistics.mean([v["forca"] for v in todos if v["hora"] == h])
        horas.append((h, n_topo / len(topo), n_todos / len(todos), forca, n_todos))
    for h, pt, pa, f, _ in sorted(horas, key=lambda x: x[1] - x[2], reverse=True):
        linhas.append(f"| {faixa(h)} | {pt:.0%} | {pa:.0%} | {f:.2f} |")
    candidatas = [x for x in horas if x[4] >= 3]
    if candidatas:
        h = max(candidatas, key=lambda x: (x[1] - x[2], x[3]))[0]
        linhas += ["", f"**Faixa para testar primeiro:** {faixa(h)} (com pelo menos 3 vídeos na amostra). "
                   "É um ponto de partida, não uma lei: confirme com os números do próprio canal."]

    linhas += ["", "## Dia da semana", "", "| Dia | % do topo | % de todos | Força média |", "|---|---|---|---|"]
    for d in range(7):
        n_todos = taxa(todos, "dia", d)
        if n_todos:
            f = statistics.mean([v["forca"] for v in todos if v["dia"] == d])
            linhas.append(f"| {DIAS[d]} | {taxa(topo, 'dia', d) / len(topo):.0%} | {n_todos / len(todos):.0%} | {f:.2f} |")

    def mediana(grupo, chave):
        return statistics.median([v[chave] for v in grupo]) if grupo else 0

    linhas += ["", "## Duração e engajamento", "", "| | Topo | Resto |", "|---|---|---|",
               f"| Duração mediana | {mediana(topo, 'duracao'):.0f}s | {mediana(resto, 'duracao'):.0f}s |"]
    for chave, nome in (("likes", "curtidas"), ("comentarios", "comentários"), ("compartilhamentos", "compartilhamentos")):
        def por_mil(g):
            return statistics.median([1000 * v[chave] / v["views"] for v in g if v["views"]]) if g else 0
        linhas.append(f"| {nome.capitalize()} por mil views | {por_mil(topo):.1f} | {por_mil(resto):.1f} |")

    c_topo = Counter(h for v in topo for h in set(v["hashtags"]))
    c_todos = Counter(h for v in todos for h in set(v["hashtags"]))
    linhas += ["", "## Hashtags", "", "| Hashtag | Aparece no topo | Aparece em todos |", "|---|---|---|"]
    for tag, n in c_topo.most_common(15):
        linhas.append(f"| #{tag} | {n / len(topo):.0%} | {c_todos[tag] / len(todos):.0%} |")
    if not c_topo:
        linhas.append("| _(os vídeos do topo não usam hashtag)_ | | |")

    linhas += ["", "## Os 10 vídeos mais fortes (para modelar)", "", "| Força | Views | Perfil | Postado | Duração | Legenda |", "|---|---|---|---|---|---|"]
    for v in topo[:10]:
        linhas.append(f"| {v['forca']:.1f}× | [{v['views']:,}]({v['url']}) | @{v['perfil']} | {v['data']} | "
                      f"{v['duracao']:.0f}s | {v['descricao'][:60].replace('|', '/')} |")
    linhas += ["", "_Próximo passo: mapear os mais fortes com `video_map.py` e anotar o que eles têm em comum._", ""]
    return "\n".join(linhas)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("perfis", nargs="+", help="@perfil do TikTok (com ou sem @)")
    p.add_argument("--limite", type=int, default=60, help="vídeos mais recentes por perfil")
    p.add_argument("--fuso", default="America/Sao_Paulo")
    p.add_argument("--out", default="perfis.md")
    a = p.parse_args()

    videos = []
    for perfil in a.perfis:
        try:
            vs = coletar(perfil, a.limite)
        except Exception as e:
            print(f"ERRO  {perfil}: {str(e).splitlines()[0][:150]}", file=sys.stderr)
            continue
        print(f"OK    @{perfil.lstrip('@')}: {len(vs)} vídeos")
        videos += vs
    if not videos:
        sys.exit("Nenhum vídeo coletado.")
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(relatorio(videos, a.fuso), encoding="utf-8")
    with out.with_suffix(".csv").open("w", newline="", encoding="utf-8") as f:
        campos = ["perfil", "data", "hora", "dia", "views", "forca", "likes", "comentarios",
                  "compartilhamentos", "duracao", "hashtags", "url", "descricao"]
        w = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore")
        w.writeheader()
        for v in videos:
            w.writerow({**v, "hashtags": " ".join(v["hashtags"]), "forca": f"{v['forca']:.2f}"})
    print(f"OK    {out}  (+ {out.with_suffix('.csv').name})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
