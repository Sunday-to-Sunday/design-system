@AGENTS.md

# Mapa do segundo cérebro (canais de vídeo com IA)

Além do app Next.js, este repositório guarda a memória e as skills dos canais de TikTok com IA. Leia só a pasta de que o pedido precisa; não varra tudo.

| Pedido | Onde ler primeiro |
|---|---|
| Qualquer coisa da Cleide ("galinha", "próximo episódio", "@cleideformosa") | `canais/galinha-de-calca/COMECE-AQUI.md` → `BIBLIA.md` → `personagem/CONSISTENCIA.md` (regra número um: a Cleide é igual em todo vídeo) |
| Escrever um episódio | skill `estudio-ia`, roteiro anterior em `canais/galinha-de-calca/episodios/` como modelo |
| Gerar no Google Flow | `python3 .claude/skills/estudio-ia/scripts/prompt_chrome.py <pasta do episódio>` → o usuário cola o `PROMPT-CHROME.md` no Claude do Chrome |
| Montar o vídeo final | `montar.py` com o `edicao.yaml` do episódio; conferir com `comparar.py` |
| Analisar um vídeo do YouTube | skill `youtube-learn`; base em `knowledge/tiktok-ia/README.md` |
| Resultados, decisões, o que funcionou | `canais/galinha-de-calca/BIBLIA.md`, seções 11 (Episódios) e 14 (Memória viva) |

Ferramentas conectadas (braços): Google Flow pelo Claude do Chrome (geração), Google Drive pasta `Cleide/<episódio>` (troca de arquivos entre o Chrome e a nuvem), Metricool blogId 7433701 (agendar post, sempre com `isAigc: true`). O usuário não quer o Magnific.

Regras fixas: vídeos sem fala; nada partidário; sem escudos, logos ou letras de música; rótulo de IA sempre; conta pessoal no TikTok.

Captura contínua: decisão nova do usuário ou número de um post vai para a seção 14 da BIBLIA na mesma hora. Processo repetido 3 vezes vira script ou skill.
