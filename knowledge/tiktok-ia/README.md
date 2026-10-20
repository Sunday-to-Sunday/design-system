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

## Estudos de canal

- **rixardê** (7 vídeos, 20/10/2026): o que aplicar no canal da Cleide em [`canais/galinha-de-calca/APRENDIZADOS-RIXARDE.md`](../../canais/galinha-de-calca/APRENDIZADOS-RIXARDE.md).

## Vídeos analisados

| Data | Vídeo | Canal | Modelo | Nota | Análise |
|---|---|---|---|---|---|
| 2026-10-20 | [faço R$10K/Mês com IA e vou te ensinar de graça](https://youtu.be/7oIW_OZoYJI) | rixardê | `creator-rewards` | 3/5 | [análise](videos/faco-r-10k-mes-com-ia-e-vou-te-ensinar-de-graca-tudo-que-voc-7oIW_OZoYJI.md) |
| 2026-10-20 | [Como ganhar muito dinheiro no TikTok com IA (sem aparecer)](https://youtu.be/oo32igqk9gs) | Projeto Renda Digital | `creator-rewards` (história narrada) | 3/5 | [análise](videos/como-ganhar-muito-dinheiro-no-tiktok-com-ia-sem-aparecer-oo32igqk9gs.md) |
| 2026-10-20 | [Como fazer vídeos virais com IA pra monetizar no TikTok](https://youtu.be/wNmsq0rvJpM) | Yan Pedro | `creator-rewards` (stand-up dublado) | 1/5 | [análise](videos/como-fazer-videos-virais-com-ia-pra-monetizar-no-tiktok-pass-wNmsq0rvJpM.md) |
| 2026-10-20 | [Te ensinando de graça a fazer vídeos bons com IA](https://youtu.be/3VT4ErWf9G4) | rixardê | estudo do canal | — | [transcrição](videos/raw/te-ensinando-de-graca-a-fazer-videos-bons-com-ia-3VT4ErWf9G4.md) · [aprendizados](../../canais/galinha-de-calca/APRENDIZADOS-RIXARDE.md) |
| 2026-10-20 | [Mostrei meus 10+ canais e como começar do zero](https://youtu.be/x7--wpxaWNE) | rixardê | estudo do canal | — | [transcrição](videos/raw/mostrei-meus-10-canais-e-como-comecar-na-internet-do-zero-x7--wpxaWNE.md) · [aprendizados](../../canais/galinha-de-calca/APRENDIZADOS-RIXARDE.md) |
| 2026-10-20 | [Como modelar qualquer vídeo com o Codex](https://youtu.be/nuOLSnE8XAw) | rixardê | estudo do canal | — | [transcrição](videos/raw/como-modelar-qualquer-video-com-o-codex-nuOLSnE8XAw.md) · [aprendizados](../../canais/galinha-de-calca/APRENDIZADOS-RIXARDE.md) |
| 2026-10-20 | [Qual o melhor horário pra postar no TikTok](https://youtu.be/ArU-uklVH_I) | rixardê | estudo do canal | — | [transcrição](videos/raw/qual-o-melhor-horario-pra-postar-no-tiktok-em-qualquer-nicho-ArU-uklVH_I.md) · [aprendizados](../../canais/galinha-de-calca/APRENDIZADOS-RIXARDE.md) |
| 2026-10-20 | [Saturei o nicho de IA?](https://youtu.be/QO9buC-I1oI) | rixardê | estudo do canal | — | [transcrição](videos/raw/saturei-o-nicho-de-ia-QO9buC-I1oI.md) · [aprendizados](../../canais/galinha-de-calca/APRENDIZADOS-RIXARDE.md) |
| 2026-10-20 | [Faça R$1K/mês ou mais (ensaios de foto com IA)](https://youtu.be/Jqr2WcitG-M) | rixardê | estudo do canal | — | [transcrição](videos/raw/faca-r-1k-mes-ou-mais-desse-jeito-que-vou-te-ensinar-Jqr2WcitG-M.md) · [aprendizados](../../canais/galinha-de-calca/APRENDIZADOS-RIXARDE.md) |
