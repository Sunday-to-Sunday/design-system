# Base de conhecimento — Ganhar dinheiro com IA no TikTok

Gerada e mantida pela skill [`youtube-learn`](../../.claude/skills/youtube-learn/SKILL.md). Para alimentar, peça ao Claude algo como:

- "Analisa esse vídeo: https://youtu.be/…"
- "Busca vídeos sobre TikTok Shop com IA e analisa os 3 melhores"
- "Compara os métodos de canal dark que já estudamos"

## Estrutura

- `videos/raw/` — extração bruta (metadados + transcrição com timestamps)
- `videos/` — análise de cada vídeo (processo, ferramentas, riscos, plano de teste)
- `playbooks/` — métodos consolidados a partir de vários vídeos

## Modelos de monetização estudados

### `creator-rewards` — Novelinhas / humor com IA para o programa de recompensas
Animações curtas de IA (frutas, bichos, objetos antropomórficos) que seguem **formatos que se repetem** ("Divisão", "Caga ouro", "Duas cabeças"…), adaptados com personagens, diálogos e bordões próprios. O fluxo é: garimpar o feed → biblioteca de formatos → mapear as imagens âncora → personagens isolados → cenas → imagem para vídeo (técnica A/B, multishot) → CapCut → postar. Vídeos com mais de 1 minuto quando a conta estiver monetizada.
- Fontes: [rixardê — faço R$10K/Mês com IA](videos/faco-r-10k-mes-com-ia-e-vou-te-ensinar-de-graca-tudo-que-voc-7oIW_OZoYJI.md)
- Fica de fora: contas de ferramentas revendidas, golpes de teste grátis, perfis falsos que fingem ser pessoas reais e compra de contas do TikTok.

### `creator-rewards` — História curta narrada ("canal dark")
Episódios históricos dramáticos de cerca de 1 minuto, com narração grave, imagens de IA animadas, design de som forte e um estilo visual fixo num "prompt mestre". Passa de 1 minuto naturalmente.
- Fontes: [Projeto Renda Digital](videos/como-ganhar-muito-dinheiro-no-tiktok-com-ia-sem-aparecer-oo32igqk9gs.md)
- Aplicado no canal [`canais/um-dia-em`](../../canais/um-dia-em/BIBLIA.md), em versão sem narração e em primeira pessoa.

### Evitar — Dublar áudio de outra pessoa
Animar personagens sobre cortes virais de comediantes: conteúdo não original e violação de direitos. [Análise](videos/como-fazer-videos-virais-com-ia-pra-monetizar-no-tiktok-pass-wNmsq0rvJpM.md).

## Vídeos analisados

| Data | Vídeo | Canal | Modelo | Nota | Análise |
|---|---|---|---|---|---|
| 2026-10-20 | [faço R$10K/Mês com IA e vou te ensinar de graça](https://youtu.be/7oIW_OZoYJI) | rixardê | `creator-rewards` | 3/5 | [análise](videos/faco-r-10k-mes-com-ia-e-vou-te-ensinar-de-graca-tudo-que-voc-7oIW_OZoYJI.md) |
| 2026-10-20 | [Como ganhar muito dinheiro no TikTok com IA (sem aparecer)](https://youtu.be/oo32igqk9gs) | Projeto Renda Digital | `creator-rewards` (história narrada) | 3/5 | [análise](videos/como-ganhar-muito-dinheiro-no-tiktok-com-ia-sem-aparecer-oo32igqk9gs.md) |
| 2026-10-20 | [Como fazer vídeos virais com IA pra monetizar no TikTok](https://youtu.be/wNmsq0rvJpM) | Yan Pedro | `creator-rewards` (stand-up dublado) | 1/5 | [análise](videos/como-fazer-videos-virais-com-ia-pra-monetizar-no-tiktok-pass-wNmsq0rvJpM.md) |
