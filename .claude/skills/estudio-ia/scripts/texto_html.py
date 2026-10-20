"""Renderiza o texto da tela como página HTML gravada quadro a quadro (fundo transparente).

Vantagens sobre o drawtext do ffmpeg: emoji colorido, fonte da web e animação de entrada e saída.
Precisa do Playwright (pip install playwright) e de um Chromium; usa o do sistema se houver.
"""

from __future__ import annotations

import asyncio
import html
import os
import shutil
from pathlib import Path

W, H, FPS = 1080, 1920, 30

CHROMIUMS = [
    os.environ.get("CHROMIUM_PATH", ""),
    "/opt/pw-browsers/chromium",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
]

TOPO = {"topo": "300px", "centro": "calc(50% - 60px)", "baixo": "1450px"}

PAGINA = """<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0;width:{w}px;height:{h}px;background:transparent;overflow:hidden}}
#t{{position:absolute;top:{top};left:60px;right:60px;text-align:center;
   font:800 {tam}px Inter, "Helvetica Neue", Arial, "Noto Color Emoji", "Apple Color Emoji", sans-serif;
   color:#fff;-webkit-text-stroke:{traco}px #000;paint-order:stroke fill;
   text-shadow:0 6px 18px rgba(0,0,0,.45);line-height:1.15}}
</style></head><body><div id="t">{texto}</div>
<script>
const DUR={dur};
function render(t){{
  const el=document.getElementById('t');
  const entra = t<0.25 ? 0.6+0.55*(t/0.25) : (t<0.4 ? 1.15-0.15*((t-0.25)/0.15) : 1);
  const sai = t>DUR-0.3 ? Math.max(0,(DUR-t)/0.3) : 1;
  el.style.transform='scale('+entra+')';
  el.style.opacity=Math.min(1, t/0.12)*sai;
}}
render(0);
</script></body></html>"""


def disponivel() -> str | None:
    try:
        import playwright  # noqa: F401
    except ImportError:
        return None
    for c in CHROMIUMS:
        if c and Path(c).exists():
            return c
    return None


def renderizar(texto: str, duracao: float, posicao: str, tamanho: int, destino: Path, chromium: str) -> Path:
    """Grava os quadros PNG de um texto animado em destino/ e devolve o padrão %04d.png."""
    from playwright.async_api import async_playwright

    if destino.exists():
        shutil.rmtree(destino)
    destino.mkdir(parents=True)
    pagina = destino / "texto.html"
    pagina.write_text(PAGINA.format(
        w=W, h=H, top=TOPO.get(posicao, TOPO["topo"]), tam=int(tamanho * 1.1),
        traco=max(2, int(tamanho / 22)), texto=html.escape(texto), dur=duracao,
    ), encoding="utf-8")

    async def gravar():
        async with async_playwright() as p:
            nav = await p.chromium.launch(executable_path=chromium)
            pg = await nav.new_page(viewport={"width": W, "height": H})
            await pg.goto(pagina.as_uri())
            await pg.wait_for_timeout(300)  # fontes carregadas
            for i in range(max(1, round(duracao * FPS))):
                await pg.evaluate(f"render({i / FPS})")
                await pg.screenshot(path=str(destino / f"{i:04d}.png"), omit_background=True)
            await nav.close()

    asyncio.run(gravar())
    return destino / "%04d.png"
