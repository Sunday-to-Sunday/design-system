# Protocolo de consistência da Cleide

**Regra número um do canal: a Cleide é a mesma galinha em todos os vídeos.** O público precisa reconhecê-la em meio segundo. Tudo abaixo é obrigatório, em todo episódio.

## 1. A ficha é a fonte da verdade

- Gere a ficha **uma vez** (prompts em [`prompts.md`](prompts.md)): frente, perfil, 3/4 e um close da cabeça.
- Depois de aprovada, a ficha **nunca mais é refeita**. Os quatro arquivos ficam em `personagem/`:
  `cleide-frente.png`, `cleide-perfil.png`, `cleide-34.png`, `cleide-cabeca.png`.
- **Toda imagem com a Cleide é gerada com a ficha anexada como referência** (2 ou 3 delas, escolhendo os ângulos mais parecidos com a cena). Nunca gere a Cleide só com texto.

## 2. Os marcadores de identidade (conferir em toda imagem)

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

## 3. Como gerar para não perder a identidade

1. **Mesmo modelo de imagem sempre** (Nano Banana no Flow). Trocar de modelo muda a cara dela. Se um dia mudar de ferramenta, refaça e aprove uma ficha nova nela antes de usar.
2. **Bloco fixo de descrição igual, palavra por palavra**, em todo prompt (já está colado em todos os prompts dos roteiros). Adereço vem **depois** do bloco, nunca no lugar.
3. **Planos médios.** Cleide pequena, ao longe, perde a identidade; close extremo deforma. Ela deve ocupar de 1/4 a 1/2 da altura do quadro.
4. **Vídeo sempre a partir da imagem aprovada** (Flow em "Frames para vídeo", com a imagem âncora como quadro inicial). Nunca gerar vídeo com a Cleide só por texto.
5. **Clipes curtos (até 8 s).** Quanto mais longo o clipe, mais a personagem "deriva".
6. **Galeria aprovada:** as melhores imagens âncora de cada episódio vão para `personagem/galeria/`. Elas podem ser usadas como referência extra nos próximos episódios (sempre junto com a ficha, nunca no lugar dela).

## 4. Conferência antes de gerar vídeo e antes de postar

- **Imagens:** coloque cada imagem âncora lado a lado com a ficha e passe pela tabela da seção 2.
- **Vídeos:** confira o primeiro quadro, o do meio e o último. Se a calça mudar de cor, o padrão das penas sumir ou a crista mudar no meio do clipe, gere de novo ou corte o trecho.
- O Claude faz essa conferência com o script de comparação:

```bash
python3 .claude/skills/estudio-ia/scripts/comparar.py canais/galinha-de-calca/personagem \
  canais/galinha-de-calca/episodios/ep02-segundo-turno/imagens/*.png \
  canais/galinha-de-calca/episodios/ep02-segundo-turno/clipes/*.mp4
```

Ele monta uma folha com a ficha numa linha e os candidatos (e 3 quadros de cada vídeo) embaixo, para comparar de uma vez.
