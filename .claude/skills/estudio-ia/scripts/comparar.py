#!/usr/bin/env python3
"""Folha de comparação de consistência: a ficha do personagem em cima, os candidatos embaixo.

Uso:
  python3 comparar.py PASTA_DA_FICHA candidato1.png candidato2.mp4 ... [--out comparacao.jpg]

Imagens entram como estão; de cada vídeo saem 3 quadros (início, meio e fim), porque o personagem
costuma "derivar" ao longo do clipe. Cada quadro recebe um rótulo com o nome do arquivo.
"""

from __future__ import annotations

import argparse
import math
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

IMG = {".png", ".jpg", ".jpeg", ".webp"}
VID = {".mp4", ".mov", ".webm"}
CW, CH = 300, 534  # célula ~9:16 (altura par: o ffmpeg arredonda ímpar e o tile quebra)


def run(cmd):
    subprocess.run(cmd, check=True, capture_output=True)


def duracao(p: Path) -> float:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                         capture_output=True, text=True).stdout.strip()
    return float(out or 0)


def celula(src: Path, rotulo: str, dest: Path, ss: float | None = None):
    rot = rotulo.replace("'", "").replace(":", " ")[:28]
    vf = (f"scale={CW}:{CH}:force_original_aspect_ratio=decrease,pad={CW}:{CH}:(ow-iw)/2:(oh-ih)/2:0x222222,"
          f"drawtext=text='{rot}':x=6:y=h-30:fontsize=18:fontcolor=white:box=1:boxcolor=black@0.6:boxborderw=4,"
          f"format=rgb24")  # mesmo formato em todas as células, senão o tile reinicia no meio
    cmd = ["ffmpeg", "-v", "error", "-y"] + (["-ss", f"{ss:.2f}"] if ss is not None else []) + \
          ["-i", str(src), "-frames:v", "1", "-vf", vf, str(dest)]
    run(cmd)


def grade(celulas: list[Path], dest: Path, cols: int):
    rows = math.ceil(len(celulas) / cols)
    tmp = dest.parent / f".{dest.stem}"
    tmp.mkdir(exist_ok=True)
    for i, c in enumerate(celulas):
        shutil.copy(c, tmp / f"{i:03d}.png")
    run(["ffmpeg", "-v", "error", "-y", "-framerate", "1", "-i", str(tmp / "%03d.png"),
         "-vf", f"tile={cols}x{rows}:padding=6:color=0x111111", "-frames:v", "1", str(dest)])
    shutil.rmtree(tmp)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("ficha", help="pasta com as imagens de referência do personagem")
    p.add_argument("candidatos", nargs="+")
    p.add_argument("--out", default="comparacao.jpg")
    a = p.parse_args()

    ficha = sorted(f for f in Path(a.ficha).iterdir() if f.suffix.lower() in IMG)
    if not ficha:
        sys.exit(f"Nenhuma imagem de ficha em {a.ficha}")
    work = Path(tempfile.mkdtemp(prefix="comparar-"))
    try:
        topo = []
        for i, f in enumerate(ficha):
            d = work / f"f{i}.png"
            celula(f, "FICHA " + f.stem, d)
            topo.append(d)
        cand = []
        for j, c in enumerate(map(Path, a.candidatos)):
            if c.suffix.lower() in IMG:
                d = work / f"c{j}.png"
                celula(c, c.stem, d)
                cand.append(d)
            elif c.suffix.lower() in VID:
                dur = duracao(c)
                for k, t in enumerate([0.2, dur / 2, max(0.2, dur - 0.3)]):
                    d = work / f"c{j}_{k}.png"
                    celula(c, f"{c.stem} {t:.1f}s", d, ss=t)
                    cand.append(d)
        cols = max(len(topo), min(6, len(cand)) or 1)
        # completa a linha da ficha com células vazias para os candidatos começarem na linha de baixo
        vazio = work / "vazio.png"
        run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"color=c=0x111111:s={CW}x{CH}",
             "-frames:v", "1", "-vf", "format=rgb24", str(vazio)])
        linha_ficha = topo + [vazio] * (cols - len(topo))
        out = Path(a.out).resolve()
        grade(linha_ficha + cand, out, cols)
        print(f"OK  {out}  [{len(topo)} da ficha, {len(cand)} quadros de candidatos]")
    finally:
        shutil.rmtree(work, ignore_errors=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
