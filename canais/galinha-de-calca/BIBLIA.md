# BIBLIA — Galinha de Calça Jeans

> Documento-mestre do canal. Itens marcados com **[decidir]** esperam uma escolha sua.

## 1. Premissa

**A Cleide é uma influenciadora que nunca gravou um vídeo.** Ela é uma galinha caipira de calça jeans que vive situações absurdas (anda de skate, joga beach tennis, surfa, faz trilha) e alguém por perto sempre filma com o celular. Ela nunca fala, nunca posa, nunca olha para a câmera pedindo like: ela só vive. Quem faz o papel de "influenciadora" é a legenda.

## 2. As três regras

1. **A ação é absurda.** Galinha andando de skate, sacando no beach tennis, remando no stand up. É isso que para o dedo na tela.
2. **A câmera é real.** Todo vídeo parece gravado com celular por alguém que estava ali: vertical, treme, faz zoom torto, perde o foco, corta a cabeça das pessoas, tem gente passando na frente. Nada de luz de cinema, câmera lenta ou movimento perfeito. É o contraste entre o absurdo e o "vídeo de celular comum" que gera a dúvida e a graça (o mesmo motor do #skateondog).
3. **O corpo é de galinha.** Ela faz coisas impossíveis, mas com o corpo de galinha: equilibra com as asas abertas, segura com os pés, rebate com o bico, a asa ou o peito, pula com bater de asas. Nunca mãos, nunca de pé feito gente, nunca gesto humano. Quanto mais "galinha" o jeito de fazer, mais engraçado e mais crível.

**Sem fala.** Ninguém fala no vídeo. O som é o ambiente (rodas do skate no concreto, mar, a bolinha na raquete), o cacarejo dela e reações sem palavras (risada, "uuuh", assobio, aplauso). Murmúrio de fundo sem palavras entendíveis pode.

## 3. Por que pode funcionar

- **Formato provado:** o #skateondog faz milhões de views com um animal real fazendo uma coisa impossível, filmado de forma simples, sem uma palavra.
- **A dúvida "é real?"** puxa comentário e compartilhamento, os sinais que mais empurram vídeo no TikTok.
- **A camada de influenciadora** dá personalidade sem precisar de fala: a legenda e o texto na tela são escritos como se ela postasse ("treino de terça ✨", "não tô pronta pra segunda").
- **Brasilidade:** beach tennis, futevôlei, praia, pista de skate pública, bloco de Carnaval. Esportes e lugares que o público daqui reconhece.
- **Pauta infinita:** cada esporte, passeio ou trend vira episódio.

## 4. Personagem

**Nome:** Cleide.

### Bloco fixo (copiar igual em todo prompt)

```
CHARACTER: Cleide, a real adult Brazilian free-range "carijó" hen with barred black-and-white plumage,
a bright red single comb and wattles, orange-amber eyes, a yellow beak, and scaly yellow legs and feet;
real chicken anatomy and proportions. She wears small, well-fitted, medium-wash faded blue denim jeans
made for a chicken: high waist sitting just below her wings with a thin brown leather belt, the legs
covering her thighs and ending in rolled-up cuffs just above her yellow feet, her tail feathers coming
out through an opening at the back. Visible stitching, slightly worn knees.
```

### Nunca muda
- Plumagem carijó, crista vermelha, pés amarelos.
- **A mesma calça jeans em todo vídeo**: azul médio desbotada, barra dobrada, cinto marrom fino. É a marca registrada dela; mesmo surfando ou na academia, é de calça jeans.
- Corpo e movimentos de galinha.

### Adereços (um ou dois por vídeo, quando combinar com a situação)
Óculos escuros, viseira de beach tennis, boné, capacete de skate, colete salva-vidas, pulseira de neon de festa, número de corrida preso na calça, colar havaiano, fitinha do Bonfim. Descreva no prompt **depois** do bloco fixo: `Accessory for this video: small black sunglasses sitting on her beak.` Nunca troca nem cobre a calça.

### Personalidade (só pelo comportamento)
Confiante, despachada, indiferente ao espanto alheio. Faz a manobra como quem faz isso todo dia e segue a vida. O humor é ela levar a sério algo que não devia conseguir fazer.

### Ficha de referência e consistência (gerar primeiro)
Prompts em [`personagem/prompts.md`](personagem/prompts.md). Salve as aprovadas como `cleide-frente.png`, `cleide-perfil.png`, `cleide-34.png` e `cleide-cabeca.png`.

**A Cleide tem de ser idêntica em todos os vídeos.** O protocolo obrigatório está em [`personagem/CONSISTENCIA.md`](personagem/CONSISTENCIA.md): a ficha nunca é refeita, toda imagem é gerada com a ficha anexada, o vídeo sempre parte de uma imagem aprovada, e tudo passa pela conferência lado a lado antes de virar vídeo e antes de ir ao ar.

## 5. A câmera (o que faz parecer real)

Todo prompt de imagem e de vídeo começa com um destes blocos:

**Celular de quem está perto (padrão):**
```
Amateur smartphone video, vertical 9:16, handheld by a bystander, slight shake, imperfect framing,
quick clumsy digital zoom, focus hunting for a moment, natural daylight, compressed social-media quality,
realistic.
```

**Celular de quem está acompanhando (seguindo a ação):**
```
Amateur smartphone video, vertical 9:16, the person filming runs or walks alongside to follow the action,
bouncy shaky footage, subject sometimes partly out of frame, natural daylight, compressed quality, realistic.
```

Proibidos em todo prompt de imagem: `no cartoon, no 3D render look, no cinematic lighting, no slow motion, no human hands on the hen, the hen never stands upright like a human, no readable text, no logos, no watermark`.
Proibidos em todo prompt de vídeo: os de cima + `no dialogue, nobody speaks, no voice-over, no narration, no music, no subtitles; only ambient sound, the hen's clucks and wordless reactions (laughs, cheers, whistles)`.

## 6. Formatos

### A. Flagra absurdo — 8 a 15 s (crescer)
Uma ação, um ou dois clipes.
- **0–1 s:** ela já está fazendo a coisa absurda (no skate, na quadra). Nada de preparação.
- **Meio:** a ação dá certo de um jeito galinha (equilibra batendo as asas, rebate com o peito).
- **Final:** ela termina, desce, sacode as penas e vai embora como se nada fosse. Corte seco: o vídeo recomeça sozinho.
- **Texto na tela:** voz de influenciadora, até 5 palavras ("treino de terça ✨").

### B. Montagem — 12 a 20 s, 8 a 14 planos de 1 a 1,5 s (estilo #skateondog)
Um esporte ou um dia, vários ângulos curtos no ritmo de um som da biblioteca do TikTok. De cada geração usa-se o melhor segundo.

### C. "Um dia comigo" — 60 a 90 s (monetizar)
O "vlog" da influenciadora sem fala: 8 a 10 situações absurdas de um mesmo dia (acorda, academia, beach tennis, açaí, skate no fim de tarde, festa), cada uma com uma linha de texto em voz de influenciadora e um carimbo de hora. Dois re-ganchos visuais (por volta de 25 s e de 60 s): a situação mais absurda do dia e o fechamento dela dormindo empoleirada de calça.

### Assinatura de final
Ela sacode as penas depois da ação e sai andando, sem olhar para a câmera.

## 7. Banco de ideias

Marque `[x]` quando virar episódio. Entre parênteses, o adereço sugerido.

**Esportes**
- [x] Skate na pista pública, descendo a rampa → **EP01**
- [ ] Beach tennis na praia, sacando e rebatendo com a asa (óculos escuros + viseira)
- [ ] Futevôlei: ela rebate de peito e de bico por cima da rede (óculos escuros)
- [ ] Stand up paddle na lagoa, equilibrando na prancha (colete salva-vidas)
- [ ] Surfando uma marolinha em Saquarema (nenhum: só a calça molhada)
- [ ] Corrida de rua com número de peito preso na calça
- [ ] Patins na orla, de asas abertas
- [ ] Slackline no parque
- [ ] Academia: no leg press, empurrando com os pés
- [ ] Bicicleta: na garupa e depois "pedalando" com os pés
- [ ] Tirolesa, presa no equipamento, cacarejando
- [ ] Parapente duplo com um instrutor (só o instrutor aparece, de costas)
- [ ] Bodyboard numa onda pequena
- [ ] Kart, de capacete, numa curva

**Rolês**
- [ ] No pedalinho de cisne do lago
- [ ] Montanha-russa do parque, com as penas voando
- [ ] Na garupa de um motoboy, de capacete
- [ ] Show de forró, dançando no meio do salão
- [ ] Bloco de Carnaval, em cima do ombro de um folião (colar havaiano)
- [ ] Na fila do açaí, depois bicando a granola de cima
- [ ] Pescando no píer, segurando a vara com os pés
- [ ] Sessão de fotos no pôr do sol do Arpoador (óculos escuros)
- [ ] No cinema, no meio da fileira, com o balde de pipoca

**Trends e datas**
- [ ] São João: pulando a fogueira cenográfica e dançando quadrilha
- [ ] Copa: torcendo no telão da praça (fitinha verde e amarela)
- [ ] Ano Novo na praia, pulando as sete ondas
- [x] Futebol: chega ao Maracanã e faz a festa na arquibancada com a torcida do Vasco → **EP03**
- [ ] Depois da eleição: "detox" no stand up paddle de óculos escuros ("desinstalei o grupo da família")
- [x] Eleição: entra na sala de votação, passa pelo mesário, vota atrás da cabine e sai comemorando → **EP02**

## 8. Identidade do perfil

- **@:** `@cleideformosa` (parecia livre no TikTok em 20/10/2026; `@galinhadecalca` já existe).
- **Nome no perfil:** "Cleide 👖🐔 influencer"
- **Bio:** "influenciadora que nunca gravou um vídeo • sempre de calça jeans • vídeos feitos com IA"
- **Legendas:** em primeira pessoa, como se ela postasse: curtas, com um emoji ("hoje o treino foi pesado 🛹").
- **Marca d'água:** o @ pequeno e transparente, duas vezes no vídeo.

## 9. Plano de publicação

| Fase | Meta | O que postar | Frequência |
|---|---|---|---|
| 1. Teste (semanas 1–2) | Descobrir quais esportes e situações prendem mais | Flagras de 8–15 s, variando | 1–2 por dia |
| 2. Crescer | 10 mil seguidores | Repetir os que reteram + montagens + trends | 1–2 por dia |
| 3. Monetizar | Programa de recompensas (10 mil seguidores, 100 mil views em 30 dias, vídeos acima de 1 min, conta pessoal) | "Um dia comigo" (60–90 s) 3–4 por semana + flagras | diário |

**Métricas para decidir:** % que assistiu até o fim (meta acima de 100% nos flagras curtos, por causa do loop), compartilhamentos, comentários "é real?" e pedidos de esporte ("faz ela no surf").

## 10. Regras

- **Rótulo "conteúdo gerado por IA" sempre ativado.** O vídeo tem aspecto real; o rótulo é obrigatório e a graça continua.
- Nunca afirmar que é real. Resposta padrão aos "é real?": `treino todo dia 💅`.
- Nada de a Cleide se machucar, cair feio ou correr perigo real: tombos, se houver, são leves, e ela levanta e sai andando.
- Trilha só da biblioteca do TikTok/CapCut.
- Sem marcas, logos ou pessoas reconhecíveis.
- Guardar a pasta de cada episódio (prova de originalidade).
- **Futebol:** sem escudo, logo ou patrocinador (o time se reconhece pelas cores), sem letra de canto de torcida, sem provocar o adversário, sem violência ou sinalizador.
- **Datas cívicas e eleições:** zero política (nenhum candidato, partido, número, cor de campanha, adesivo), processo mostrado do jeito certo, nada que sugira fraude, informação verdadeira na legenda.

## 11. Episódios

| EP | Título | Formato | Adereço | Status | Views 48h | Conclusão | Pacote |
|---|---|---|---|---|---|---|---|
| 01 | Skate | Flagra absurdo | — | roteiro pronto | — | — | [roteiro](episodios/ep01-skate/roteiro.md) |
| 03 | Dia de Maracanã — Vasco x Boca (postar ter. 20/10, 18h–19h) | Flagra absurdo (data) | camisa preta com faixa branca | roteiro pronto | — | — | [roteiro](episodios/ep03-maracana/roteiro.md) |
| 02 | Segundo turno (postar sáb. 24/10) | Flagra absurdo (data) | — | roteiro pronto | — | — | [roteiro](episodios/ep02-segundo-turno/roteiro.md) |

**Arquivados:** "A faixa" e "A feira" (`episodios/_arquivo/`) eram da fase "só plausível" e ficaram reais demais. "O provador" foi descartado antes, por depender de fala.

## 12. Rotina de garimpo e teste

- **A conta @cleideformosa só assiste ao nicho** (animais fazendo coisas impossíveis, IA realista, humor de flagra), para o algoritmo aprender e mostrar referências. Salvar 5 links por dia em `referencias/garimpo.md`.
- **Toda semana:** rodar `perfis.py` nos 3 a 5 perfis de referência (horário, dia, duração, hashtags e os vídeos mais fortes para modelar).
- **Teste honesto de 10 vídeos** antes de mudar o formato. Se nenhum passar de ~10 mil views e a retenção estiver baixa, mudar primeiro o formato (lugares, esportes, câmera); depois, o personagem.
- Aprendizados completos do estudo do rixardê: [`APRENDIZADOS-RIXARDE.md`](APRENDIZADOS-RIXARDE.md).

## 13. Referências modeladas

| Referência | Formato | O que aproveitar | Mapa |
|---|---|---|---|
| #skateondog (compilação) | Montagem rápida | Animal fazendo algo impossível, sem fala, câmera de gênero reconhecível, 1 corte/s, final com o animal | [mapa](referencias/skate-on-dog-compilacao/mapa.md) |
