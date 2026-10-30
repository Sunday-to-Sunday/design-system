Você vai operar o Google Flow (labs.google/flow) neste navegador para criar as imagens e os vídeos do
episódio "EP 01 — Skate" do canal "Cleide, a galinha de calça jeans" (TikTok @cleideformosa).
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
- Novo projeto no Flow chamado "ep01-skate". Modo de IMAGEM, Nano Banana, 9:16, 4 resultados.
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
- No Google Drive, crie (se não existir) a pasta "Cleide/ep01-skate" e envie para lá todas as imagens
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

# Roteiro — EP 01 — Skate

### Imagens âncora (Nano Banana · 9:16 · anexar `cleide-frente.png` e `cleide-perfil.png`)

#### Cena 1
```
Amateur smartphone photo, vertical 9:16, handheld, slight motion blur, imperfect framing, late
afternoon golden sunlight, compressed social-media quality, realistic.
CHARACTER: Cleide, a real adult Brazilian free-range "carijó" hen with barred black-and-white plumage,
a bright red single comb and wattles, orange-amber eyes, a yellow beak, and scaly yellow legs and feet;
real chicken anatomy and proportions. She wears small, well-fitted, medium-wash faded blue denim jeans
made for a chicken: high waist sitting just below her wings with a thin brown leather belt, the legs
covering her thighs and ending in rolled-up cuffs just above her yellow feet, her tail feathers coming
out through an opening at the back. Visible stitching, slightly worn knees.
Scene: a public concrete skatepark in a Brazilian city: grey concrete ramps and banks with graffiti,
a few palm trees, a metal fence, apartment buildings in the background. Cleide is standing on a
skateboard at the top edge of a small concrete ramp, about to drop in, her yellow feet gripping the
board, wings slightly open for balance. At the side of the park two teenage skaters have stopped and
are watching, one holding his skateboard. Far in the background a dog on a leash sits next to its
owner, staring at the hen.
Camera at about 1 meter high, a few meters away, slightly tilted.
No cartoon, no 3D render look, no cinematic lighting, no human hands on the hen, the hen never stands
upright like a human, no readable text, no logos, no watermark.
```

#### Cena 2
```
Amateur smartphone photo, vertical 9:16, handheld, slight motion blur, imperfect framing, late
afternoon golden sunlight, compressed social-media quality, realistic.
CHARACTER: Cleide, a real adult Brazilian free-range "carijó" hen with barred black-and-white plumage,
a bright red single comb and wattles, orange-amber eyes, a yellow beak, and scaly yellow legs and feet;
real chicken anatomy and proportions. She wears small, well-fitted, medium-wash faded blue denim jeans
made for a chicken: high waist sitting just below her wings with a thin brown leather belt, the legs
covering her thighs and ending in rolled-up cuffs just above her yellow feet, her tail feathers coming
out through an opening at the back. Visible stitching, slightly worn knees.
Scene: the same Brazilian public concrete skatepark. Cleide is on the skateboard rolling toward a low
concrete kicker ramp, wings half open, body leaning forward, the jeans and rolled-up cuffs clearly
visible. A concrete bench and a backpack on the ground at the right edge of the frame. The two teenage
skaters in the background are holding up their phones, filming.
Camera at about 1 meter high, a few meters away, static.
No cartoon, no 3D render look, no cinematic lighting, no human hands on the hen, the hen never stands
upright like a human, no readable text, no logos, no watermark.
```

### Ordem de geração (aprendizado do rixardê: a física difícil primeiro)

1. **Cena 2 primeiro** (o pulinho com a prancha subindo e ela caindo de volta em cima): é a física mais difícil. Se depois de 2 tentativas a prancha ou a galinha "derreterem", use a técnica A/B: gere uma segunda imagem com ela **já pousada** no skate depois do pulo e use as duas em Frames (início e fim). Se ainda assim não sair, tire o pulinho e mantenha só ela rolando até parar e descendo.
2. Depois a cena 1.

### Vídeos (Veo · 9:16)

**Modo:** **Frames para vídeo**, com a âncora como quadro inicial; anexe também `cleide-perfil.png` como ingrediente, se o Flow permitir, para segurar a calça. Gere 2 vezes a cena 1 (é a mais difícil) e 1 vez a cena 2.

#### Cena 1 — Frames (quadro inicial: âncora da cena 1)
```
Amateur smartphone video, vertical 9:16, the person filming walks backward to follow the action,
bouncy shaky footage, subject sometimes partly out of frame, late afternoon golden sunlight, compressed
quality, realistic, 8 seconds.
CHARACTER: Cleide, a real adult Brazilian free-range "carijó" hen with barred black-and-white plumage,
a bright red single comb and wattles, orange-amber eyes, a yellow beak, and scaly yellow legs and feet;
real chicken anatomy and proportions. She wears small, well-fitted, medium-wash faded blue denim jeans
made for a chicken: high waist sitting just below her wings with a thin brown leather belt, the legs
covering her thighs and ending in rolled-up cuffs just above her yellow feet, her tail feathers coming
out through an opening at the back. Visible stitching, slightly worn knees.
Action: 0–2s Cleide tips the skateboard over the edge of the small concrete ramp and drops in, wings
opening for balance. 2–5s she rolls smoothly down and across the flat ground of the skatepark toward
the camera, her head bobbing slightly, feathers ruffling in the wind, feet gripping the board. 5–8s she
rolls past the two teenage skaters, who step back surprised; in the background the leashed dog stares.
Audio: skateboard wheels rolling on concrete, the click of the board crossing concrete joints, a
teenager's wordless "uuuuh", a short laugh, distant city sounds.
No dialogue, nobody speaks, no voice-over, no narration, no music, no subtitles; only ambient sound, the
hen's clucks and wordless reactions. No cartoon, no slow motion, no human hands on the hen, the hen never
stands upright like a human; she balances like a real chicken, using her wings.
```

#### Cena 2 — Frames (quadro inicial: âncora da cena 2)
```
Amateur smartphone video, vertical 9:16, handheld by a bystander, slight shake, imperfect framing,
quick clumsy digital zoom at the end, late afternoon golden sunlight, compressed quality, realistic,
8 seconds.
CHARACTER: Cleide, a real adult Brazilian free-range "carijó" hen with barred black-and-white plumage,
a bright red single comb and wattles, orange-amber eyes, a yellow beak, and scaly yellow legs and feet;
real chicken anatomy and proportions. She wears small, well-fitted, medium-wash faded blue denim jeans
made for a chicken: high waist sitting just below her wings with a thin brown leather belt, the legs
covering her thighs and ending in rolled-up cuffs just above her yellow feet, her tail feathers coming
out through an opening at the back. Visible stitching, slightly worn knees.
Action: 0–2s Cleide rolls up the low concrete kicker ramp. 2–3s she does a small hop with a quick flap
of her wings, the skateboard lifts slightly off the ground and she lands back on it. 3–5s she rolls to a
stop near the concrete bench. 5–7s she hops off the board onto the ground, shakes her whole body to fluff
her feathers, and walks away out of frame with quick chicken steps. 5–8s the empty skateboard keeps
rolling slowly on its own.
Audio: wheels on concrete, the clack of the board landing, a whistle and short applause from the
teenagers, one cluck from the hen.
No dialogue, nobody speaks, no voice-over, no narration, no music, no subtitles; only ambient sound, the
hen's clucks and wordless reactions. No cartoon, no slow motion, no human hands on the hen, the hen never
stands upright like a human.
```
