# Prompt para o Claude no Chrome (gerar no Google Flow)

Cole o bloco abaixo no painel do Claude na extensão do Chrome, com o Google Flow (labs.google/flow) aberto e logado. Troque `EP03` e o link do roteiro quando for outro episódio.

```
Você vai operar o Google Flow (labs.google/flow) neste navegador para criar as imagens e os vídeos de um
episódio do canal "Cleide, a galinha de calça jeans" (TikTok @cleideformosa). Trabalhe passo a passo e
me mostre os resultados para eu aprovar antes de seguir.

Leia primeiro estes arquivos no GitHub (estou logado):
1. Regras de consistência (obrigatórias):
   https://github.com/Sunday-to-Sunday/design-system/blob/claude/youtube-video-analysis-tool-gzxalw/canais/galinha-de-calca/personagem/CONSISTENCIA.md
2. Prompts da ficha da personagem:
   https://github.com/Sunday-to-Sunday/design-system/blob/claude/youtube-video-analysis-tool-gzxalw/canais/galinha-de-calca/personagem/prompts.md
3. Roteiro do episódio (seções "Ordem de geração", "Imagens âncora" e "Vídeos"):
   https://github.com/Sunday-to-Sunday/design-system/blob/claude/youtube-video-analysis-tool-gzxalw/canais/galinha-de-calca/episodios/ep03-maracana/roteiro.md

Passo 1 — Ficha (só se ainda não existir a ficha aprovada):
- No Flow, crie um projeto "Cleide ficha". Modo de IMAGEM, modelo Nano Banana, proporção 9:16, 4 resultados.
- Gere o prompt "1. Frente" copiando exatamente do prompts.md. Me mostre as 4 e espere eu escolher.
- Com a frente escolhida anexada como referência, gere "2. Perfil", "3. Três quartos" e "4. Cabeça".
  Me mostre e espere eu escolher cada uma. Baixe as escolhidas como cleide-frente.png, cleide-perfil.png,
  cleide-34.png e cleide-cabeca.png.
- Antes de me mostrar, confira cada imagem contra a tabela "marcadores de identidade" do CONSISTENCIA.md
  (penas carijó, crista vermelha simples, olho âmbar, bico e pés amarelos, calça jeans azul desbotada
  com cinto marrom e barra dobrada). Descarte as que falharem.

Passo 2 — Imagens âncora do episódio:
- Novo projeto com o nome do episódio. Modo de IMAGEM, Nano Banana, 9:16, 4 resultados.
- Anexe no máximo 3 referências: cleide-frente, cleide-perfil e cleide-cabeca.
- Siga a "Ordem de geração" do roteiro (a cena mais difícil primeiro). Copie cada prompt exatamente.
- Me mostre as opções de cada cena e espere eu aprovar. Baixe como cena1.png, cena2.png, cena3.png.
- Não pode aparecer escudo, logo, patrocinador nem texto legível. Se aparecer, gere de novo.

Passo 3 — Vídeos:
- Modo FRAMES (quadro inicial). NÃO use "Elementos/Ingredientes" para o quadro inicial.
- Modelo Veo 3.1 Fast, 9:16, som ligado. Quadro inicial = a imagem aprovada da cena.
- Copie o prompt de vídeo da cena exatamente do roteiro. Gere 1 vez; me mostre; só gere de novo se a
  calça, a galinha ou o movimento quebrarem, ou se aparecer logo/texto.
- Baixe como cena1.mp4, cena2.mp4, cena3.mp4.

Regras: nunca use fala nem letra de música; nunca troque o modelo de imagem no meio; se o Flow recusar
um prompt, me avise e sugira a menor mudança possível no texto.
No fim, me diga onde estão os arquivos baixados.
```

Depois, mande os arquivos (`cleide-*.png`, `cena*.png` e `cena*.mp4`) para a sessão do Claude na nuvem (anexando no chat ou por uma pasta do Google Drive). Ela confere a consistência, monta o vídeo final com o `montar.py` e prepara o post.
