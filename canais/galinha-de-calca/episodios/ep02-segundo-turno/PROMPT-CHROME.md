Você vai operar o Google Flow (labs.google/flow) neste navegador para criar as imagens e os vídeos do
episódio "EP 02 — Segundo turno" do canal "Cleide, a galinha de calça jeans" (TikTok @cleideformosa).
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
- Novo projeto no Flow chamado "ep02-segundo-turno". Modo de IMAGEM, Nano Banana, 9:16, 4 resultados.
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
- No Google Drive, crie (se não existir) a pasta "Cleide/ep02-segundo-turno" e envie para lá todas as imagens
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

# Roteiro — EP 02 — Segundo turno

### Regras deste episódio (não negociáveis)

- **Zero política:** nenhum candidato, partido, número, cor de campanha, adesivo, bandeira, camiseta com mensagem. Figurantes com roupas neutras (branco, cinza, bege, azul-claro, jeans). Evitar vermelho e verde e amarelo predominantes.
- **A tela da urna nunca aparece.** A cabine esconde tudo; só se ouvem os bipes.
- **A câmera fica na sala, nunca dentro da cabine.** Vemos a Cleide entrar no espaço de votação e sair, mas a divisória de papelão sempre esconde a urna.
- **O processo aparece certo:** ela passa pelo mesário e entrega um documento antes de votar. Nada que sugira fraude ou que "qualquer um vota".
- **Sem fala.**
- **Informação verdadeira na legenda** (data do segundo turno e documento com foto).

### Imagens âncora (Nano Banana · 9:16 · anexar `cleide-frente.png` e `cleide-perfil.png`)

#### Cena 1
```
Amateur smartphone photo, vertical 9:16, handheld by someone standing in a queue, slight motion blur,
imperfect framing, morning daylight coming through windows mixed with fluorescent light, compressed
social-media quality, realistic.
CHARACTER: Cleide, a real adult Brazilian free-range "carijó" hen with barred black-and-white plumage,
a bright red single comb and wattles, orange-amber eyes, a yellow beak, and scaly yellow legs and feet;
real chicken anatomy and proportions. She wears small, well-fitted, medium-wash faded blue denim jeans
made for a chicken: high waist sitting just below her wings with a thin brown leather belt, the legs
covering her thighs and ending in rolled-up cuffs just above her yellow feet, her tail feathers coming
out through an opening at the back. Visible stitching, slightly worn knees.
Scene: the corridor of a Brazilian public school on election day: half-tiled walls painted light green
and white, a row of classroom doors with plain white paper sheets taped on them (no readable text),
a ceiling fan, a queue of ordinary adult voters of different ages standing along the wall, all wearing
plain neutral everyday clothes in white, grey, beige, light blue and denim. Cleide is walking down the
middle of the corridor next to the queue, toward an open classroom door. An older woman in the queue
looks down at her, covering a smile.
No political symbols, no campaign colors, no stickers, no flags, no numbers, no candidates, no logos,
no readable text. No cartoon, no 3D render look, no cinematic lighting, no human hands on the hen, the
hen never stands upright like a human, no watermark.
```

#### Cena 2
```
Amateur smartphone photo, vertical 9:16, taken from the back of a classroom by someone standing near
the pushed-aside desks, slight motion blur, imperfect framing, fluorescent light, compressed
social-media quality, realistic.
CHARACTER: Cleide, a real adult Brazilian free-range "carijó" hen with barred black-and-white plumage,
a bright red single comb and wattles, orange-amber eyes, a yellow beak, and scaly yellow legs and feet;
real chicken anatomy and proportions. She wears small, well-fitted, medium-wash faded blue denim jeans
made for a chicken: high waist sitting just below her wings with a thin brown leather belt, the legs
covering her thighs and ending in rolled-up cuffs just above her yellow feet, her tail feathers coming
out through an opening at the back. Visible stitching, slightly worn knees.
Scene: a Brazilian public school classroom set up as a polling station: student desks pushed against
the wall, a simple table where two poll workers in plain neutral clothes sit with printed lists and
papers (no readable text), and further away a standard grey cardboard voting booth partition standing
on a small table, its open side facing away from the camera. Cleide is standing on top of the poll
workers' table; a small blank card lies on the table in front of her beak. The female poll worker looks
at the card with a calm, professional expression.
No political symbols, no campaign colors, no stickers, no flags, no numbers, no candidates, no visible
voting machine screen, no logos, no readable text. No cartoon, no 3D render look, no cinematic lighting,
no human hands on the hen, the hen never stands upright like a human, no watermark.
```

#### Cena 3
```
Amateur smartphone photo, vertical 9:16, taken inside the classroom from the side of the voting booth,
a few meters away, slight motion blur, imperfect framing, fluorescent light, compressed social-media
quality, realistic.
CHARACTER: Cleide, a real adult Brazilian free-range "carijó" hen with barred black-and-white plumage,
a bright red single comb and wattles, orange-amber eyes, a yellow beak, and scaly yellow legs and feet;
real chicken anatomy and proportions. She wears small, well-fitted, medium-wash faded blue denim jeans
made for a chicken: high waist sitting just below her wings with a thin brown leather belt, the legs
covering her thighs and ending in rolled-up cuffs just above her yellow feet, her tail feathers coming
out through an opening at the back. Visible stitching, slightly worn knees.
Scene: the same Brazilian public school classroom used as a polling station. Cleide is standing on the
small table behind the grey cardboard voting booth partition, seen from the side: her body, jeans and
tail feathers are visible, her head is lowered toward the inside of the booth, and the partition
completely hides whatever is inside it. In the background, the poll workers' table with two staff
members in plain neutral clothes and the open classroom door.
No political symbols, no campaign colors, no stickers, no flags, no numbers, no candidates, no visible
voting machine or screen, no logos, no readable text. No cartoon, no 3D render look, no cinematic
lighting, no human hands on the hen, the hen never stands upright like a human, no watermark.
```

### Vídeos (Veo · 9:16)

**Modo:** **Frames para vídeo**, com a âncora como quadro inicial; anexe `cleide-perfil.png` como ingrediente, se o Flow permitir. Se o Flow recusar por política (tema eleitoral), tire as palavras "election" e "polling station" e descreva só "a classroom with a cardboard booth and a table with two staff members"; a cena continua igual.

#### Cena 1 — Frames (quadro inicial: âncora da cena 1)
```
Amateur smartphone video, vertical 9:16, handheld by someone standing in a queue, slight shake,
imperfect framing, quick clumsy zoom, morning daylight mixed with fluorescent light, compressed quality,
realistic, 8 seconds.
CHARACTER: Cleide, a real adult Brazilian free-range "carijó" hen with barred black-and-white plumage,
a bright red single comb and wattles, orange-amber eyes, a yellow beak, and scaly yellow legs and feet;
real chicken anatomy and proportions. She wears small, well-fitted, medium-wash faded blue denim jeans
made for a chicken: high waist sitting just below her wings with a thin brown leather belt, the legs
covering her thighs and ending in rolled-up cuffs just above her yellow feet, her tail feathers coming
out through an opening at the back. Visible stitching, slightly worn knees.
Action: 0–4s Cleide walks briskly down the school corridor next to the queue of voters, head bobbing
with each step; people look down and step back slightly. 3–5s the older woman covers her mouth to hide
a laugh. 4–6s Cleide turns and walks in through the open classroom door. The phone turns to follow her.
Audio: footsteps on the tiled floor, a ceiling fan, the queue's background chatter as an unintelligible
murmur, a soft cluck.
No dialogue, nobody speaks, no voice-over, no narration, no music, no subtitles; only ambient sound, the
hen's clucks and wordless reactions. No political symbols, no campaign colors, no stickers, no flags, no
numbers, no readable text. No cartoon, no slow motion, no human hands on the hen, the hen never stands
upright like a human.
```

#### Cena 2 — Frames (quadro inicial: âncora da cena 2)
```
Amateur smartphone video, vertical 9:16, filmed from the back of the classroom, slight shake, imperfect
framing, fluorescent light, compressed quality, realistic, 8 seconds.
CHARACTER: Cleide, a real adult Brazilian free-range "carijó" hen with barred black-and-white plumage,
a bright red single comb and wattles, orange-amber eyes, a yellow beak, and scaly yellow legs and feet;
real chicken anatomy and proportions. She wears small, well-fitted, medium-wash faded blue denim jeans
made for a chicken: high waist sitting just below her wings with a thin brown leather belt, the legs
covering her thighs and ending in rolled-up cuffs just above her yellow feet, her tail feathers coming
out through an opening at the back. Visible stitching, slightly worn knees.
Action: 0–2s on top of the poll workers' table, Cleide nudges the small blank card toward the female
poll worker with her beak. 2–4s the poll worker glances at the card, checks her printed list and gives a
small calm nod. 4–6s Cleide hops down from the table. 6–8s she walks across the classroom floor toward
the grey cardboard voting booth.
Audio: ceiling fan, paper rustling, the corridor's chatter as an unintelligible murmur, a soft cluck.
No dialogue, nobody speaks, no voice-over, no narration, no music, no subtitles; only ambient sound and
wordless reactions. No political symbols, no campaign colors, no stickers, no flags, no numbers, no
readable text. No cartoon, no slow motion, no human hands on the hen, the hen never stands upright like a
human.
```

#### Cena 3 — Frames (quadro inicial: âncora da cena 3)
```
Amateur smartphone video, vertical 9:16, filmed inside the classroom from the side of the voting booth,
slight shake, imperfect framing, the phone swings to follow the hen at the end, fluorescent light,
compressed quality, realistic, 8 seconds.
CHARACTER: Cleide, a real adult Brazilian free-range "carijó" hen with barred black-and-white plumage,
a bright red single comb and wattles, orange-amber eyes, a yellow beak, and scaly yellow legs and feet;
real chicken anatomy and proportions. She wears small, well-fitted, medium-wash faded blue denim jeans
made for a chicken: high waist sitting just below her wings with a thin brown leather belt, the legs
covering her thighs and ending in rolled-up cuffs just above her yellow feet, her tail feathers coming
out through an opening at the back. Visible stitching, slightly worn knees.
Action: 0–3s behind the grey cardboard partition, Cleide pecks a few times at something inside the
booth that the partition hides; short electronic key beeps. 3–4s one long electronic confirmation beep.
4–6s Cleide steps out from behind the partition flapping her wings and does two small excited hops.
6–8s she runs past the poll workers' table, where the female poll worker laughs, and out through the
open classroom door.
Audio: short electronic key beeps, one long final electronic beep, wings flapping, quick little
footsteps, a wordless laugh, an excited cluck.
No dialogue, nobody speaks, no voice-over, no narration, no music, no subtitles; only ambient sound, the
hen's clucks and wordless reactions. The voting machine and its screen are never visible: the cardboard
partition hides them at all times. No political symbols, no campaign colors, no stickers, no flags, no
numbers, no readable text. No cartoon, no slow motion, no human hands on the hen, the hen never stands
upright like a human.
```
