# Guia do Google Flow para o estúdio

Recursos do Flow confirmados em outubro de 2026 (Veo 3.1 + Nano Banana). O Flow muda rápido: se a tela do usuário mostrar outros nomes ou opções, siga a tela e atualize este guia.

| Recurso | Para quê | Quando usar |
|---|---|---|
| **Imagem (Nano Banana)** | Gerar e editar imagens; aceita imagens de referência | Ficha do personagem e imagens âncora |
| **Ingredientes para vídeo** | Vídeo a partir de até 3 imagens de referência (personagem, objeto, estilo) | Padrão do canal: personagem consistente em cenas novas |
| **Frames para vídeo** | Vídeo que liga uma imagem inicial a uma final | Quando o começo e o fim da ação precisam ser exatos (técnica A/B) |
| **Texto para vídeo** | Vídeo só com o prompt | Planos de ambiente sem o personagem |
| **Estender (Extend)** | Continua um clipe a partir do último quadro | Cenas que precisam durar mais de 8 s sem corte |
| **Áudio** | Som ambiente, efeitos e falas geradas junto com o vídeo | Sempre; descreva o som no prompt |

Os clipes têm cerca de 8 s. O acesso a alguns modos depende do plano (Pro × Ultra) e do modelo (Veo 3.1 Fast × Quality); confirme na tela do usuário.

## Estrutura de prompt de imagem (Nano Banana)

```
[Estilo/meio] Ultra-realistic smartphone photo, vertical 9:16, natural light, slight motion blur, no text.
[Personagem — bloco fixo da BIBLIA, igual sempre]
[Ação/pose] what the character is doing, body orientation, where she looks.
[Cenário] specific Brazilian place, time of day, props, background people and what they do.
[Câmera] shot size (wide/medium/close), angle (eye level, low angle), lens feel (24mm phone), framing.
[Luz/clima] golden hour / overcast / fluorescent market light.
[Proibidos] no cartoon, no 3D render look, no anthropomorphic human body, no human hands on the chicken, no text, no watermark.
```

## Estrutura de prompt de vídeo (Veo)

```
Mode: Ingredients (refs: character front, character 3/4, [scene image])   ← diga ao usuário quais imagens anexar
[Plano] Handheld smartphone footage, vertical 9:16, 8 seconds, realistic.
[Personagem — bloco fixo da BIBLIA]
[Ação em ordem] 0–3s: ... 3–6s: ... 6–8s: ...
[Câmera] how the phone moves (follows her, slight shake, zooms in at the end).
[Áudio] ambient sound, chicken clucks, background chatter; dialogue: a man off-camera says in Brazilian Portuguese: "..."
[Proibidos] the chicken does not talk, no subtitles, no music, no text on screen, natural chicken movement (pecking, head bobbing, quick steps).
```

- **Falas:** escreva a frase exata entre aspas, diga quem fala e em que idioma. Uma ou duas falas curtas por clipe.
- **Sem música no Flow:** a trilha entra no CapCut, para poder trocar sem regenerar.
- **Sem texto gerado:** legendas e títulos vão no CapCut; texto gerado sai com erro.

## Personagem consistente

1. Gere a ficha: frente, perfil e 3/4 de corpo inteiro, fundo cinza-claro liso, a mesma luz de estúdio suave. Peça 4 variações e escolha uma por ângulo.
2. Crie a imagem âncora de cada cena no Nano Banana **anexando a ficha** como referência.
3. No vídeo, use **Ingredientes** com 2 imagens da ficha + a âncora da cena, ou **Frames** com a âncora como quadro inicial.
4. Se a calça ou as penas "derivarem" (mudar cor, comprimento, virar shorts), refaça a âncora antes de gastar crédito em vídeo.

## Realismo

- Peça "smartphone footage" ou "amateur phone video" + "handheld": vídeo de celular parece flagrante real e esconde imperfeições.
- Animais reais se mexem de jeito próprio: descreva os movimentos de galinha (cabeça indo e voltando, ciscar, passos rápidos, arrepiar as penas) e proíba gestos humanos.
- Pessoas ao fundo reagindo de verdade (rindo, filmando com o celular, apontando) vendem a cena.
- Evite close extremo no rosto do animal vestido; planos médios escondem as costuras da calça.

## Quando o Flow recusa o prompt

Tire o gatilho provável e reescreva: crianças pequenas em situações de risco, violência ou animal se machucando, nudez (mesmo de bicho, "naked" pode disparar), marcas e logos registrados, pessoas famosas. Gerações recusadas não gastam crédito.

## Custo em créditos

Planeje com uma ou duas gerações por cena. Gere as imagens até ficarem certas (custam pouco ou nada) e **só depois** gaste crédito no vídeo.
