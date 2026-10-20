# Comece aqui (para qualquer sessão do Claude)

Canal: **Cleide, a galinha de calça jeans** · TikTok `@cleideformosa` · vídeos gerados com IA, sem fala.
Repositório: `Sunday-to-Sunday/design-system`, branch `claude/youtube-video-analysis-tool-gzxalw`.

Leia nesta ordem:
1. [`BIBLIA.md`](BIBLIA.md): quem é a Cleide, as três regras (ação absurda, câmera de celular real, corpo de galinha), sem fala.
2. [`personagem/CONSISTENCIA.md`](personagem/CONSISTENCIA.md): **regra número um, a Cleide é igual em todos os vídeos.**
3. [`personagem/prompts.md`](personagem/prompts.md): prompts da ficha, prontos para colar.
4. O roteiro do episódio da vez em `episodios/`.

## Próximos passos (em ordem)

1. **Ficha da Cleide no Google Flow** (modo imagem, Nano Banana, 9:16, 4 resultados): gerar frente → aprovar → perfil, 3/4 e cabeça com a frente anexada. Salvar em `personagem/`. Conferir cada uma contra a tabela de `CONSISTENCIA.md`.
2. **EP03 — Dia de Maracanã** (postar **terça 20/10, 18h–19h**, antes de Vasco x Boca às 21h30): [roteiro](episodios/ep03-maracana/roteiro.md). Mesma sequência: imagens âncora com a ficha anexada → conferir → vídeos em "Frames para vídeo".
3. **EP02 — Segundo turno** (postar **sábado 24/10, 18h–20h**): imagens âncora das cenas 1, 2 e 3 com a ficha anexada (seção "Imagens âncora" do [roteiro](episodios/ep02-segundo-turno/roteiro.md)) → conferir → vídeos em "Frames para vídeo", Veo 3.1 Fast, imagem âncora como quadro inicial (seção "Vídeos").
4. Salvar como `episodios/ep02-segundo-turno/imagens/cena1.png…` e `clipes/cena1.mp4…`.
5. **Montagem:** `python3 .claude/skills/estudio-ia/scripts/montar.py canais/galinha-de-calca/episodios/ep02-segundo-turno/edicao.yaml` (ou mandar os clipes para a sessão do Claude na nuvem, que monta).
6. **Conferência:** `python3 .claude/skills/estudio-ia/scripts/comparar.py canais/galinha-de-calca/personagem <imagens e clipes>`.
7. **TikTok:** conta pessoal `@cleideformosa` (nunca comercial), conectar na Metricool e agendar com o rótulo "conteúdo gerado por IA" ligado.

Depois, o EP01 (skate) segue o mesmo caminho.
