Você vai operar o Google Flow (labs.google/flow) neste navegador para criar as imagens e os vídeos do
episódio "EP 03 — Dia de Maracanã (Vasco x Boca)" do canal "Cleide, a galinha de calça jeans" (TikTok @cleideformosa).
Trabalhe passo a passo e me mostre os resultados para eu aprovar antes de seguir. Tudo o que você precisa
está neste texto; não abra outros links.

REGRA NÚMERO UM: a Cleide tem que ser a mesma galinha em todas as imagens e vídeos. Leia a seção
"Consistência" antes de gerar qualquer coisa.

PASSO 1 — FICHA DA PERSONAGEM (está na seção "Ficha" abaixo)
- No Flow, crie o projeto "Cleide ficha". Modo de IMAGEM, modelo Nano Banana, proporção 9:16, 4 resultados.
- Gere o prompt "1. Frente" copiando exatamente. Me mostre as 4 opções e espere eu escolher.
- Com a frente escolhida anexada como referência, gere "2. Perfil", "3. Três quartos" e "4. Cabeça".
  Me mostre e espere eu escolher cada uma. Baixe como cleide-frente.png, cleide-perfil.png, cleide-34.png, cleide-cabeca.png.
- Antes de me mostrar, confira cada imagem contra os "marcadores de identidade" da seção
  "Consistência" e descarte as que falharem.

PASSO 2 — IMAGENS ÂNCORA (seção "Roteiro")
- Novo projeto no Flow chamado "ep03-maracana". Modo de IMAGEM, Nano Banana, 9:16, 4 resultados.
- Anexe no máximo 3 referências: cleide-frente, cleide-perfil e cleide-cabeca.
- Siga a "Ordem de geração" (a cena mais difícil primeiro). Copie cada prompt exatamente, sem resumir.
- Me mostre as opções de cada cena e espere eu aprovar. Baixe como cena1.png, cena2.png, cena3.png…
- Não pode aparecer escudo, logo, patrocinador nem texto legível. Se aparecer, gere de novo.

PASSO 3 — VÍDEOS
- Modo FRAMES (quadro inicial). NÃO use "Elementos/Ingredientes" para o quadro inicial.
- Modelo Veo 3.1 Fast, 9:16, som ligado. Quadro inicial = a imagem aprovada da cena.
- Copie o prompt de vídeo da cena exatamente. Gere 1 vez e me mostre; só gere de novo se a calça,
  a galinha ou o movimento quebrarem, ou se aparecer logo ou texto.
- Baixe como cena1.mp4, cena2.mp4, cena3.mp4…

PASSO 4 — ENTREGA
- No Google Drive, crie (se não existir) a pasta "Cleide/ep03-maracana" e envie para lá todas as imagens
  e vídeos aprovados, com os nomes acima. Me mande o link da pasta.

REGRAS: nunca use fala nem letra de música; nunca troque o modelo de imagem no meio; se o Flow recusar
um prompt, me avise e sugira a menor mudança possível no texto.

---

# Consistência

**Regra número um do canal: a Cleide é a mesma galinha em todos os vídeos.** O público precisa reconhecê-la em meio segundo. Tudo abaixo é obrigatório, em todo episódio.

### 1. A ficha é a fonte da verdade

- Gere a ficha **uma vez** (prompts em [`prompts.md`](prompts.md)): frente, perfil, 3/4 e um close da cabeça.
- Depois de aprovada, a ficha **nunca mais é refeita**. Os quatro arquivos ficam em `personagem/`:
  `cleide-frente.png`, `cleide-perfil.png`, `cleide-34.png`, `cleide-cabeca.png`.
- **Toda imagem com a Cleide é gerada com a ficha anexada como referência** (2 ou 3 delas, escolhendo os ângulos mais parecidos com a cena). Nunca gere a Cleide só com texto.

### 2. Os marcadores de identidade (conferir em toda imagem)

| Parte | Como tem de ser | Erros comuns que reprovam |
|---|---|---|
| Penas | Carijó: listras finas e regulares preto e branco no corpo todo | Penas lisas, marrons, manchadas, listras grossas |
| Crista | Vermelha, simples (uma fileira de pontas), em pé | Crista dupla, rosa, caída, ausente |
| Barbela | Vermelha, pequena, embaixo do bico | Ausente ou enorme |
| Olho | Âmbar/laranja | Preto, azul |
| Bico e pés | Amarelos | Cinza, preto, rosa |
| Calça | Jeans azul médio desbotado, cinto marrom fino, barra dobrada, joelhos gastos, abertura para o rabo | Jeans escuro, sem cinto, sem barra, vira short, vira macacão, cobre os pés |
| Corpo | Tamanho e proporção de galinha real; corpo na horizontal, nunca em pé como gente | Gigante, humanoide, com mãos |

Se um item falhar, **refaça a imagem antes de gerar o vídeo**. Corrigir imagem é barato; corrigir vídeo é caro e quase nunca funciona.

### 3. Como gerar para não perder a identidade

1. **Mesmo modelo de imagem sempre** (Nano Banana no Flow). Trocar de modelo muda a cara dela. Se um dia mudar de ferramenta, refaça e aprove uma ficha nova nela antes de usar.
2. **Bloco fixo de descrição igual, palavra por palavra**, em todo prompt (já está colado em todos os prompts dos roteiros). Adereço vem **depois** do bloco, nunca no lugar.
3. **Planos médios.** Cleide pequena, ao longe, perde a identidade; close extremo deforma. Ela deve ocupar de 1/4 a 1/2 da altura do quadro.
4. **Vídeo sempre a partir da imagem aprovada** (Flow em **"Frames"**, com a imagem âncora como quadro inicial). Nunca gerar vídeo com a Cleide só por texto. **Não use "Elementos/Ingredientes" para o quadro inicial**: nesse modo o Flow só usa a imagem como inspiração e a Cleide pode mudar.
   - **No máximo 3 referências por cena** (imagens da ficha + cenário). Com mais, a IA mistura quem é quem.
   - **Ações com começo e fim** (o pulinho no skate, a raquetada): técnica A/B em Frames, com a imagem inicial e a **final**. A final tem de ser o estado em que a ação termina, não um passo intermediário.
   - **Gere primeiro a cena mais difícil do episódio** (física, movimento rápido). Se ela não sair, repense a cena antes de gastar crédito no resto.
5. **Clipes curtos (até 8 s).** Quanto mais longo o clipe, mais a personagem "deriva".
6. **Expressão e ação em toda cena:** uma ação de galinha concreta por clipe (cabeça indo e voltando, arrepiar as penas, olhar de lado, bater asas). Personagem parado parece "IA genérica".
7. **Galeria aprovada:** as melhores imagens âncora de cada episódio vão para `personagem/galeria/`. Elas podem ser usadas como referência extra nos próximos episódios (sempre junto com a ficha, nunca no lugar dela).

### 4. Conferência antes de gerar vídeo e antes de postar

- **Imagens:** coloque cada imagem âncora lado a lado com a ficha e passe pela tabela da seção 2.
- **Vídeos:** confira o primeiro quadro, o do meio e o último. Se a calça mudar de cor, o padrão das penas sumir ou a crista mudar no meio do clipe, gere de novo ou corte o trecho.
- O Claude faz essa conferência com o script de comparação:

```bash
python3 .claude/skills/estudio-ia/scripts/comparar.py canais/galinha-de-calca/personagem \
  canais/galinha-de-calca/episodios/ep02-segundo-turno/imagens/*.png \
  canais/galinha-de-calca/episodios/ep02-segundo-turno/clipes/*.mp4
```

Ele monta uma folha com a ficha numa linha e os candidatos (e 3 quadros de cada vídeo) embaixo, para comparar de uma vez.

Origem de várias dessas regras: o estudo do canal do rixardê em [`../APRENDIZADOS-RIXARDE.md`](../APRENDIZADOS-RIXARDE.md).

---

# Ficha

### 1. Frente

```
Ultra-realistic studio photograph, vertical 9:16, full body, camera at the hen's eye level,
soft diffused studio light, plain light-gray seamless background, sharp focus, natural colors.
CHARACTER: Cleide, a real adult Brazilian free-range "carijó" hen with barred black-and-white plumage,
a bright red single comb and wattles, orange-amber eyes, a yellow beak, and scaly yellow legs and feet;
real chicken anatomy and proportions. She wears small, well-fitted, medium-wash faded blue denim jeans
made for a chicken: high waist sitting just below her wings with a thin brown leather belt, the legs
covering her thighs and ending in rolled-up cuffs just above her yellow feet, her tail feathers coming
out through an opening at the back. Visible stitching, slightly worn knees.
Pose: standing on the floor facing the camera, head slightly tilted, looking straight into the lens.
No cartoon, no 3D render look, no human-like body, no text, no logos, no watermark.
```

### 2. Perfil (anexar a frente aprovada)

```
Ultra-realistic studio photograph, vertical 9:16, full body side view (left profile), camera at the
hen's eye level, soft diffused studio light, plain light-gray seamless background, sharp focus.
Same hen and same jeans as the reference image.
CHARACTER: Cleide, a real adult Brazilian free-range "carijó" hen with barred black-and-white plumage,
a bright red single comb and wattles, orange-amber eyes, a yellow beak, and scaly yellow legs and feet;
real chicken anatomy and proportions. She wears small, well-fitted, medium-wash faded blue denim jeans
made for a chicken: high waist sitting just below her wings with a thin brown leather belt, the legs
covering her thighs and ending in rolled-up cuffs just above her yellow feet, her tail feathers coming
out through an opening at the back. Visible stitching, slightly worn knees.
Pose: walking to the left mid-step, one yellow foot lifted, the jeans' back opening and tail feathers
clearly visible, the thin brown belt visible at the waist.
No cartoon, no 3D render look, no human-like body, no text, no logos, no watermark.
```

### 3. Três quartos (anexar a frente aprovada)

```
Ultra-realistic studio photograph, vertical 9:16, full body three-quarter view, camera slightly above
the hen, soft diffused studio light, plain light-gray seamless background, sharp focus.
Same hen and same jeans as the reference image.
CHARACTER: Cleide, a real adult Brazilian free-range "carijó" hen with barred black-and-white plumage,
a bright red single comb and wattles, orange-amber eyes, a yellow beak, and scaly yellow legs and feet;
real chicken anatomy and proportions. She wears small, well-fitted, medium-wash faded blue denim jeans
made for a chicken: high waist sitting just below her wings with a thin brown leather belt, the legs
covering her thighs and ending in rolled-up cuffs just above her yellow feet, her tail feathers coming
out through an opening at the back. Visible stitching, slightly worn knees.
Pose: standing turned three-quarters to the right, head turned back toward the camera with a
sideways chicken glance, showing the stitching and the rolled-up cuffs.
No cartoon, no 3D render look, no human-like body, no text, no logos, no watermark.
```

### 4. Cabeça (anexar a frente aprovada)

Serve para fixar crista, olho, bico e o padrão das penas do pescoço, que são o "rosto" dela.

```
Ultra-realistic studio photograph, vertical 9:16, close-up portrait of the hen's head and neck down to
the top of the jeans waistband, three-quarter angle, camera at eye level, soft diffused studio light,
plain light-gray seamless background, sharp focus on the eye.
Same hen and same jeans as the reference image.
CHARACTER: Cleide, a real adult Brazilian free-range "carijó" hen with barred black-and-white plumage,
a bright red single comb and wattles, orange-amber eyes, a yellow beak, and scaly yellow legs and feet;
real chicken anatomy and proportions. She wears small, well-fitted, medium-wash faded blue denim jeans
made for a chicken: high waist sitting just below her wings with a thin brown leather belt, the legs
covering her thighs and ending in rolled-up cuffs just above her yellow feet, her tail feathers coming
out through an opening at the back. Visible stitching, slightly worn knees.
Pose: head turned slightly toward the camera, one amber eye clearly visible, comb and wattles in full
detail, the barred pattern of the neck feathers sharp, the brown belt just visible at the bottom.
No cartoon, no 3D render look, no human-like body, no text, no logos, no watermark.
```


---

# Roteiro — EP 03 — Dia de Maracanã (Vasco x Boca)

### Regras deste episódio

- **Sem escudo, logo, patrocinador ou texto** na camisa, nas bandeiras ou no estádio. O Vasco é reconhecido pelo preto e branco e pela faixa diagonal.
- **Sem letra de música:** a torcida canta como rugido e batucada, sem palavras entendíveis. Nada de cantar o hino ou cantos com letra (fala e direitos autorais).
- **Nada sobre o Boca:** sem provocação, sem ofensa ao adversário, sem violência, sem sinalizador.
- **Sem fala.**

### Imagens âncora (Nano Banana · 9:16 · anexar `cleide-frente.png`, `cleide-perfil.png` e `cleide-cabeca.png`)

#### Cena 1
```
Amateur smartphone photo, vertical 9:16, handheld by a football fan walking in a crowd, slight motion
blur, imperfect framing, late afternoon golden light, compressed social-media quality, realistic.
CHARACTER: Cleide, a real adult Brazilian free-range "carijó" hen with barred black-and-white plumage,
a bright red single comb and wattles, orange-amber eyes, a yellow beak, and scaly yellow legs and feet;
real chicken anatomy and proportions. She wears small, well-fitted, medium-wash faded blue denim jeans
made for a chicken: high waist sitting just below her wings with a thin brown leather belt, the legs
covering her thighs and ending in rolled-up cuffs just above her yellow feet, her tail feathers coming
out through an opening at the back. Visible stitching, slightly worn knees.
Accessory for this video: a small black football jersey made for a chicken, with a single white diagonal
sash across the chest, worn over the top of her body; no crest, no logos, no sponsor, no number, no text.
The jeans, the brown belt and the rolled-up cuffs remain fully visible below the jersey.
Scene: the crowded access ramp of Maracanã stadium in Rio de Janeiro at the end of the afternoon, the
stadium's white facade and roof structure in the background, hundreds of football fans walking up the
ramp, most wearing plain black or white shirts with a white or black diagonal sash, no crests or logos.
Cleide is walking up the ramp among the fans' legs, confident. A fan in the foreground looks down at her
laughing and pointing.
No logos, no crests, no sponsors, no readable text, no flares, no cartoon, no 3D render look, no
cinematic lighting, no human hands on the hen, the hen never stands upright like a human, no watermark.
```

#### Cena 2
```
Amateur smartphone photo, vertical 9:16, handheld by a fan standing in the stands, slight motion blur,
imperfect framing, stadium floodlights mixed with the last evening light, compressed social-media
quality, realistic.
CHARACTER: Cleide, a real adult Brazilian free-range "carijó" hen with barred black-and-white plumage,
a bright red single comb and wattles, orange-amber eyes, a yellow beak, and scaly yellow legs and feet;
real chicken anatomy and proportions. She wears small, well-fitted, medium-wash faded blue denim jeans
made for a chicken: high waist sitting just below her wings with a thin brown leather belt, the legs
covering her thighs and ending in rolled-up cuffs just above her yellow feet, her tail feathers coming
out through an opening at the back. Visible stitching, slightly worn knees.
Accessory for this video: a small black football jersey made for a chicken, with a single white diagonal
sash across the chest, worn over the top of her body; no crest, no logos, no sponsor, no number, no text.
The jeans, the brown belt and the rolled-up cuffs remain fully visible below the jersey.
Scene: the packed stands of Maracanã stadium at night, a sea of fans in plain black and white shirts
jumping and singing, large plain black-and-white flags waving above them (no crests, no text), the green
pitch and floodlights far below. Cleide is perched on the back of a stadium seat in the middle of the
crowd, wings half open, beak open mid-cluck. The fan next to her is jumping with both arms up.
No logos, no crests, no sponsors, no readable text, no flares, no cartoon, no 3D render look, no
cinematic lighting, no human hands on the hen, the hen never stands upright like a human, no watermark.
```

#### Cena 3
```
Amateur smartphone photo, vertical 9:16, handheld by a fan in the stands, strong motion blur, imperfect
framing, stadium floodlights, compressed social-media quality, realistic.
CHARACTER: Cleide, a real adult Brazilian free-range "carijó" hen with barred black-and-white plumage,
a bright red single comb and wattles, orange-amber eyes, a yellow beak, and scaly yellow legs and feet;
real chicken anatomy and proportions. She wears small, well-fitted, medium-wash faded blue denim jeans
made for a chicken: high waist sitting just below her wings with a thin brown leather belt, the legs
covering her thighs and ending in rolled-up cuffs just above her yellow feet, her tail feathers coming
out through an opening at the back. Visible stitching, slightly worn knees.
Accessory for this video: a small black football jersey made for a chicken, with a single white diagonal
sash across the chest, worn over the top of her body; no crest, no logos, no sponsor, no number, no text.
The jeans, the brown belt and the rolled-up cuffs remain fully visible below the jersey.
Scene: the packed stands of Maracanã stadium at night at the moment the crowd erupts, everyone jumping
with arms up. Cleide is perched on the shoulder of a cheering fan in a plain black shirt, her wings
spread wide, feathers ruffled, the fan's arms raised in celebration on both sides of her.
No logos, no crests, no sponsors, no readable text, no flares, no cartoon, no 3D render look, no
cinematic lighting, the hen never stands upright like a human, no watermark.
```

### Ordem de geração (aprendizado do rixardê: a física difícil primeiro)

1. **Cena 3 primeiro** (ela pulando para o ombro do torcedor na explosão da torcida): é a mais difícil. Se não sair boa em 2 tentativas, troque a ação por ela batendo as asas em cima da cadeira enquanto todo mundo pula, e siga.
2. Depois a cena 2, e por último a cena 1, que é a mais fácil.

**Plano de ligação (opcional, se sobrar crédito):** entre a rampa e a arquibancada, 2 s dela passando por baixo da catraca, filmada pelo torcedor de trás. Deixa o vídeo com cara de sequência, não de clipes soltos.

### Vídeos (Veo · 9:16)

**Modo:** **Frames para vídeo**, com a imagem âncora como quadro inicial; anexe `cleide-perfil.png` como ingrediente, se o Flow permitir. Uma geração por cena; refaça só se a camisa ganhar escudo ou texto, ou se a calça ou a Cleide mudarem.

#### Cena 1 — Frames (quadro inicial: âncora da cena 1)
```
Amateur smartphone video, vertical 9:16, handheld by a fan walking up a crowded stadium ramp, shaky,
imperfect framing, late afternoon golden light, compressed quality, realistic, 8 seconds.
CHARACTER: Cleide, a real adult Brazilian free-range "carijó" hen with barred black-and-white plumage,
a bright red single comb and wattles, orange-amber eyes, a yellow beak, and scaly yellow legs and feet;
real chicken anatomy and proportions. She wears small, well-fitted, medium-wash faded blue denim jeans
made for a chicken: high waist sitting just below her wings with a thin brown leather belt, the legs
covering her thighs and ending in rolled-up cuffs just above her yellow feet, her tail feathers coming
out through an opening at the back. Visible stitching, slightly worn knees.
Accessory for this video: a small black football jersey made for a chicken, with a single white diagonal
sash across the chest; no crest, no logos, no sponsor, no number, no text. The jeans remain fully visible.
Action: 0–4s Cleide walks briskly up the Maracanã access ramp among the fans' legs, head bobbing with
each step. 3–6s a fan in the foreground looks down, laughs and points at her. 5–8s the phone follows her
as she keeps walking up toward the stadium entrance.
Audio: distant samba drums, the crowd singing as a wordless roaring chorus, many footsteps, a soft cluck.
No dialogue, nobody speaks, no song lyrics, no voice-over, no narration, no music track, no subtitles;
only ambient sound, the hen's clucks and wordless reactions. No logos, no crests, no readable text, no
flares. No cartoon, no slow motion, no human hands on the hen, the hen never stands upright like a human.
```

#### Cena 2 — Frames (quadro inicial: âncora da cena 2)
```
Amateur smartphone video, vertical 9:16, handheld by a fan in the stands, shaky and bouncing with the
crowd, imperfect framing, stadium floodlights, compressed quality, realistic, 8 seconds.
CHARACTER: Cleide, a real adult Brazilian free-range "carijó" hen with barred black-and-white plumage,
a bright red single comb and wattles, orange-amber eyes, a yellow beak, and scaly yellow legs and feet;
real chicken anatomy and proportions. She wears small, well-fitted, medium-wash faded blue denim jeans
made for a chicken: high waist sitting just below her wings with a thin brown leather belt, the legs
covering her thighs and ending in rolled-up cuffs just above her yellow feet, her tail feathers coming
out through an opening at the back. Visible stitching, slightly worn knees.
Accessory for this video: a small black football jersey made for a chicken, with a single white diagonal
sash across the chest; no crest, no logos, no sponsor, no number, no text. The jeans remain fully visible.
Action: the crowd jumps in rhythm with the drums while big plain black-and-white flags wave. Perched on
the back of the stadium seat, Cleide flaps her wings and clucks on every beat of the bass drum, bobbing
her head in rhythm. The fan next to her jumps with his arms up, in sync with her.
Audio: the roar of the crowd singing as a wordless chorus, bass drum and snare drums of the fans' band,
rhythmic clucks.
No dialogue, nobody speaks, no song lyrics, no voice-over, no narration, no music track, no subtitles;
only ambient sound, the hen's clucks and wordless reactions. No logos, no crests, no readable text, no
flares. No cartoon, no slow motion, no human hands on the hen, the hen never stands upright like a human.
```

#### Cena 3 — Frames (quadro inicial: âncora da cena 3)
```
Amateur smartphone video, vertical 9:16, handheld by a fan in the stands, very shaky with the crowd's
celebration, imperfect framing, stadium floodlights, compressed quality, realistic, 8 seconds.
CHARACTER: Cleide, a real adult Brazilian free-range "carijó" hen with barred black-and-white plumage,
a bright red single comb and wattles, orange-amber eyes, a yellow beak, and scaly yellow legs and feet;
real chicken anatomy and proportions. She wears small, well-fitted, medium-wash faded blue denim jeans
made for a chicken: high waist sitting just below her wings with a thin brown leather belt, the legs
covering her thighs and ending in rolled-up cuffs just above her yellow feet, her tail feathers coming
out through an opening at the back. Visible stitching, slightly worn knees.
Accessory for this video: a small black football jersey made for a chicken, with a single white diagonal
sash across the chest; no crest, no logos, no sponsor, no number, no text. The jeans remain fully visible.
Action: 0–4s the crowd erupts and everyone jumps; on the fan's shoulder, Cleide spreads her wings wide
and flaps while the fan raises his arms. 4–6s she hops down from his shoulder onto the concrete step.
6–8s she shakes her whole body to fluff her feathers and walks away along the row among the fans' legs.
Audio: a huge eruption of the crowd, clapping, whistles, an excited cluck.
No dialogue, nobody speaks, no song lyrics, no voice-over, no narration, no music track, no subtitles;
only ambient sound, the hen's clucks and wordless reactions. No logos, no crests, no readable text, no
flares. No cartoon, no slow motion, the hen never stands upright like a human.
```
