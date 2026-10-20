---
name: estudio-ia
description: Estúdio de produção de vídeos com IA para TikTok usando o Google Flow (Nano Banana para imagens, Veo para vídeo). Use quando o usuário quiser criar ou evoluir a ideia de um canal, desenhar um personagem consistente, modelar um vídeo de referência (link do TikTok, Shorts ou Reels), escrever roteiro, gerar prompts de imagem âncora e de imagem para vídeo, montar o pacote de um episódio, planejar a edição no CapCut ou a legenda do post. Também quando ele disser "próximo episódio", "modela esse vídeo", "faz os prompts", "galinha de calça" ou mandar um link de vídeo curto para usar de referência.
---

# Estúdio IA — da ideia ao vídeo no Flow

O Claude faz tudo o que não exige clicar no Flow: ideia, personagem, mapeamento de referências, roteiro, prompts, edição e legenda. O usuário cola os prompts no Google Flow, gera, escolhe e devolve os resultados (print ou arquivo) para o Claude revisar e corrigir.

Cada canal mora em `canais/<canal>/`:

```
canais/<canal>/
  BIBLIA.md              conceito, personagem, formatos, regras, banco de ideias
  personagem/            prompts da ficha do personagem + imagens de referência aprovadas
  referencias/<nome>/    vídeos modelados (saída do video_map.py + storyboard)
  episodios/epNN-<slug>/ pacote de cada episódio (roteiro.md + imagens/ + clipes/)
```

Leia sempre a `BIBLIA.md` do canal antes de escrever qualquer coisa. Ela é a fonte da verdade sobre o personagem e o tom.

## Ferramentas

```bash
pip install -r .claude/skills/estudio-ia/scripts/requirements.txt   # primeira vez (precisa do ffmpeg)
python3 .claude/skills/estudio-ia/scripts/video_map.py URL --out canais/<canal>/referencias/<nome>
```

```bash
python3 .claude/skills/estudio-ia/scripts/montar.py canais/<canal>/episodios/epNN-<slug>/edicao.yaml [--previa]
```

O `montar.py` substitui a edição no CapCut: lê o `edicao.yaml` do episódio (clipes, cortes, velocidade, enquadramento, texto na tela, marca d'água, trilha) e exporta o `final.mp4` em 1080x1920, 30 fps, H.264, com volume normalizado a -14 LUFS. Todo pacote de episódio deve vir com o `edicao.yaml` ao lado do `roteiro.md`. O texto da tela é renderizado em HTML pelo `texto_html.py` (emoji colorido e animação de entrada e saída) quando há Playwright e um Chromium; sem eles, cai no texto simples do ffmpeg, que não mostra emoji. Depois de montar, extraia 3 ou 4 quadros com o ffmpeg e olhe (ferramenta Read) antes de entregar.

O `video_map.py` baixa o vídeo (TikTok, Shorts, Reels ou arquivo local), detecta os cortes, salva um quadro por cena, monta a `contato.jpg` numerada e transcreve as falas com o Whisper local. O resultado fica em `mapa.md`.

Se o download falhar, peça ao usuário para baixar o vídeo e mandar o arquivo; o script também aceita caminho local.

## Fluxos

### A. Ideia do canal → `BIBLIA.md`
1. Entenda o personagem e o objetivo (monetizar pelo programa de recompensas exige vídeos com mais de 1 minuto, 10 mil seguidores e 100 mil views em 30 dias; ver `knowledge/tiktok-ia/`).
2. Defina: premissa em 1 frase, ficha visual do personagem (descritores fixos), personalidade, o que **nunca** muda, 2–3 formatos que se repetem (um curto para crescer e um com mais de 1 minuto para monetizar), banco de pelo menos 30 ideias, regras de tom e de segurança.
3. Use o modelo em `references/biblia-template.md`.

### B. Personagem consistente (obrigatório)
Se o canal tiver um `personagem/CONSISTENCIA.md`, ele manda: siga-o em todo episódio. Use `scripts/comparar.py PASTA_DA_FICHA imagens... clipes...` para montar a folha ficha × candidatos e olhe antes de aprovar qualquer imagem ou vídeo.

1. Escreva prompts para a **ficha do personagem** no Nano Banana: frente, perfil e 3/4, corpo inteiro, fundo neutro, mesma luz (`references/flow-guia.md`, seção Personagem).
2. O usuário gera, escolhe e salva as aprovadas em `canais/<canal>/personagem/`. Essas imagens viram os **ingredientes** de todos os vídeos.
3. Congele na BIBLIA o bloco de descrição do personagem e repita-o **igual, palavra por palavra**, em todo prompt.

### C. Modelar uma referência
1. Rode o `video_map.py`.
2. **Olhe a `contato.jpg` e os quadros** (ferramenta Read) e leia o `mapa.md`.
3. Preencha a seção "Storyboard de imagens âncora" do `mapa.md`:
   - junte os cortes que são só movimento da mesma imagem;
   - descreva cada âncora: enquadramento, ação, câmera, luz, som;
   - anote o gancho (0–2 s), o ritmo, a virada e o final.
4. Extraia **o que faz o vídeo funcionar** (estrutura, gancho, ritmo) e o que é só superfície. Modelar é copiar a estrutura e trocar todo o resto: personagem, cenário, piada, falas. Nunca reproduza o vídeo dos outros quadro a quadro.

### D. Pacote do episódio → `episodios/epNN-<slug>/roteiro.md`
Use `references/episodio-template.md`. O pacote tem:
1. Ideia, formato, duração-alvo, referência modelada (se houver).
2. Roteiro cena a cena, com o tempo de cada uma (clipes de ~8 s).
3. **Prompts de imagem âncora** (Nano Banana), um por cena, independentes entre si.
4. **Prompts de vídeo** (Veo), um por cena, dizendo o modo do Flow (Ingredientes, Frames ou Texto), a ação, a câmera, o áudio e as falas.
5. Plano de edição no CapCut, texto na tela, legenda do post, hashtags e checklist de publicação (inclusive o **rótulo de conteúdo de IA**).
6. **Checagem de viralização** (`references/viralizacao.md`): as 8 checagens em tabela. Se uma falhar, reescreva antes de entregar. Para o gancho use a skill `viral-hooks` (gere de 3 a 6 opções de tipos diferentes e escolha); para o tamanho, a meta de conclusão e o vídeo longo, use a `viral-tiktok-content` (inclusive `assets/long-tiktok-template.md` nos vídeos de 60 s ou mais).

Antes de escrever, use a skill **creative-director** (quando disponível) para testar a ideia: ela diz o que é a cena em uma frase? A calça/o personagem é o assunto, ou aparece de passagem? Tem exatamente uma virada? Mate a ideia fraca cedo e diga ao usuário por quê.

### E. Revisão (loop de correção)
Quando o usuário mandar prints ou clipes gerados:
- compare com o roteiro e com a ficha do personagem (calça, cor das penas, crista, proporção);
- diga exatamente o que está errado e devolva o **prompt corrigido**, completo;
- se o Flow recusar um prompt por política, reescreva tirando o gatilho provável e explique a troca.

## Regras de produção

- **Prompts em inglês.** O Veo segue melhor instruções em inglês. Se o canal tiver fala, escreva as falas em português do Brasil entre aspas, com "Brazilian Portuguese" explícito. Se o canal for **sem fala** (veja a BIBLIA), todo prompt de vídeo termina com `No dialogue, nobody speaks, no voice-over, no music, no subtitles, background voices only as an unintelligible murmur`, e o checklist do post manda ouvir com fone e cortar qualquer palavra que o Veo tenha colocado.
- **Cada prompt é independente:** nada de "como na cena anterior". Repita personagem, cenário, luz e estilo em todos.
- **9:16 vertical** em tudo.
- **Uma ação principal por clipe de 8 s.** Ação demais vira bagunça.
- Mantenha a lista de descritores visuais fixos do personagem e a "lista de proibidos" da BIBLIA em todo prompt.
- Se houver fala, escreva você mesmo, curta e natural; diálogo genérico é o que entrega vídeo feito por IA.
- Se o canal quer parecer real, rode o "teste do é real?" da BIBLIA em todo episódio: o personagem só faz o que faria na vida real, a câmera é de gente comum (celular, câmera de segurança, câmera de carro) e nada é bonito demais.
- Antes de entregar, confira: o vídeo final passa de 1 minuto? (só quando a conta já estiver monetizando) Tem gancho nos 2 primeiros segundos? Tem o rótulo de IA no checklist?
- Atualize o banco de ideias e a lista de episódios da BIBLIA a cada episódio produzido, anotando o que funcionou quando o usuário trouxer números.
