#!/usr/bin/env python3
"""Monta o prompt para o Claude da extensão do Chrome gerar um episódio no Google Flow.

Junta num arquivo só, pronto para colar, as instruções de operação do Flow, as regras de
consistência, os prompts da ficha (se ela ainda não existir) e as seções de geração do roteiro.
Tudo vai dentro do texto: o Claude do Chrome não precisa abrir links do repositório privado.

Uso:
  python3 prompt_chrome.py canais/<canal>/episodios/epNN-<slug> [--ficha|--sem-ficha] [--drive PASTA]

Saída: <episódio>/PROMPT-CHROME.md
"""

import argparse
import re
import sys
from pathlib import Path

SECOES_ROTEIRO = ("Regras deste episódio", "Imagens âncora", "Ordem de geração", "Vídeos")
OPCIONAIS = ("Regras deste episódio", "Ordem de geração")
SECOES_FICHA = ("1.", "2.", "3.", "4.")
FICHA = ("cleide-frente.png", "cleide-perfil.png", "cleide-34.png", "cleide-cabeca.png")


def secoes(texto, nivel="## "):
    """Divide um markdown em {título: bloco} pelos cabeçalhos do nível dado."""
    blocos, titulo, linhas = {}, None, []
    for linha in texto.splitlines():
        if linha.startswith(nivel):
            if titulo:
                blocos[titulo] = "\n".join(linhas).strip()
            titulo, linhas = linha[len(nivel):].strip(), [linha]
        elif titulo:
            linhas.append(linha)
    if titulo:
        blocos[titulo] = "\n".join(linhas).strip()
    return blocos


def escolher(blocos, prefixos):
    saida = []
    for prefixo in prefixos:
        achados = [b for t, b in blocos.items() if t.startswith(prefixo)]
        if not achados and prefixo not in OPCIONAIS:
            sys.exit(f"Seção que começa com '{prefixo}' não encontrada.")
        saida.extend(achados)
    return saida


def rebaixar(bloco):
    """Desce um nível nos cabeçalhos para caber dentro das seções do prompt."""
    return re.sub(r"^(#+) ", r"#\1 ", bloco, flags=re.M)


def instrucoes(titulo, slug, com_ficha, drive):
    passos = []
    if com_ficha:
        passos.append(f"""PASSO 1 — FICHA DA PERSONAGEM (está na seção "Ficha" abaixo)
- No Flow, crie o projeto "Cleide ficha". Modo de IMAGEM, modelo Nano Banana, proporção 9:16, 4 resultados.
- Gere o prompt "1. Frente" copiando exatamente. Me mostre as 4 opções e espere eu escolher.
- Com a frente escolhida anexada como referência, gere "2. Perfil", "3. Três quartos" e "4. Cabeça".
  Me mostre e espere eu escolher cada uma. Baixe como {", ".join(FICHA)}.
- Antes de me mostrar, confira cada imagem contra os "marcadores de identidade" da seção
  "Consistência" e descarte as que falharem.""")
    n = len(passos) + 1
    passos.append(f"""PASSO {n} — IMAGENS ÂNCORA (seção "Roteiro")
- Novo projeto no Flow chamado "{slug}". Modo de IMAGEM, Nano Banana, 9:16, 4 resultados.
- Anexe no máximo 3 referências: cleide-frente, cleide-perfil e cleide-cabeca.
- Siga a "Ordem de geração" (a cena mais difícil primeiro). Copie cada prompt exatamente, sem resumir.
- Me mostre as opções de cada cena e espere eu aprovar. Baixe como cena1.png, cena2.png, cena3.png…
- Não pode aparecer escudo, logo, patrocinador nem texto legível. Se aparecer, gere de novo.""")
    passos.append(f"""PASSO {n + 1} — VÍDEOS
- Modo FRAMES (quadro inicial). NÃO use "Elementos/Ingredientes" para o quadro inicial.
- Modelo Veo 3.1 Fast, 9:16, som ligado. Quadro inicial = a imagem aprovada da cena.
- Copie o prompt de vídeo da cena exatamente. Gere 1 vez e me mostre; só gere de novo se a calça,
  a galinha ou o movimento quebrarem, ou se aparecer logo ou texto.
- Baixe como cena1.mp4, cena2.mp4, cena3.mp4…""")
    entrega = (f"""PASSO {n + 2} — ENTREGA
- No Google Drive, crie (se não existir) a pasta "{drive}/{slug}" e envie para lá todas as imagens
  e vídeos aprovados, com os nomes acima. Me mande o link da pasta.""" if drive else
               "No fim, me diga onde estão os arquivos baixados.")
    passos.append(entrega)
    return f"""Você vai operar o Google Flow (labs.google/flow) neste navegador para criar as imagens e os vídeos do
episódio "{titulo}" do canal "Cleide, a galinha de calça jeans" (TikTok @cleideformosa).
Trabalhe passo a passo e me mostre os resultados para eu aprovar antes de seguir. Tudo o que você precisa
está neste texto; não abra outros links.

REGRA NÚMERO UM: a Cleide tem que ser a mesma galinha em todas as imagens e vídeos. Leia a seção
"Consistência" antes de gerar qualquer coisa.

{chr(10).join(p + chr(10) for p in passos)}
REGRAS: nunca use fala nem letra de música; nunca troque o modelo de imagem no meio; se o Flow recusar
um prompt, me avise e sugira a menor mudança possível no texto."""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("episodio", type=Path)
    grupo = ap.add_mutually_exclusive_group()
    grupo.add_argument("--ficha", dest="ficha", action="store_true", default=None,
                       help="inclui o passo da ficha da personagem")
    grupo.add_argument("--sem-ficha", dest="ficha", action="store_false",
                       help="pula a ficha (já aprovada)")
    ap.add_argument("--drive", default="Cleide",
                    help='pasta do Google Drive para entregar os arquivos (padrão "Cleide"; "" desliga)')
    args = ap.parse_args()

    ep = args.episodio.resolve()
    roteiro = ep / "roteiro.md"
    canal = ep.parent.parent
    personagem = canal / "personagem"
    for arq in (roteiro, personagem / "CONSISTENCIA.md", personagem / "prompts.md"):
        if not arq.exists():
            sys.exit(f"Arquivo não encontrado: {arq}")

    # Sem escolha explícita, inclui a ficha só se as imagens aprovadas não estiverem no repositório.
    com_ficha = args.ficha
    if com_ficha is None:
        com_ficha = not all((personagem / f).exists() for f in FICHA)

    texto_roteiro = roteiro.read_text(encoding="utf-8")
    titulo = texto_roteiro.splitlines()[0].lstrip("# ").strip()
    partes = [instrucoes(titulo, ep.name, com_ficha, args.drive), "", "---", "",
              "# Consistência", "",
              rebaixar((personagem / "CONSISTENCIA.md").read_text(encoding="utf-8").split("\n", 1)[1].strip())]
    if com_ficha:
        ficha = escolher(secoes((personagem / "prompts.md").read_text(encoding="utf-8")), SECOES_FICHA)
        partes += ["", "---", "", "# Ficha", ""] + [rebaixar(b) + "\n" for b in ficha]
    partes += ["", "---", "", f"# Roteiro — {titulo}", ""]
    partes += [rebaixar(b) + "\n" for b in escolher(secoes(texto_roteiro), SECOES_ROTEIRO)]

    destino = ep / "PROMPT-CHROME.md"
    destino.write_text("\n".join(partes).rstrip() + "\n", encoding="utf-8")
    print(f"OK  {destino}  ({'com' if com_ficha else 'sem'} ficha, {len(destino.read_text()):,} caracteres)")


if __name__ == "__main__":
    main()
