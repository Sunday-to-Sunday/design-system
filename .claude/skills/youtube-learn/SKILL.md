---
name: youtube-learn
description: Analisa vídeos do YouTube para extrair habilidades, processos e playbooks acionáveis, com foco em formas de ganhar dinheiro com IA no TikTok. Use sempre que o usuário colar um link do YouTube, pedir para "analisar", "estudar", "resumir" ou "aprender com" um vídeo/canal/playlist, quiser descobrir vídeos sobre um tema (ex.: "TikTok Shop com IA", "canal dark", "UGC com IA"), comparar métodos de vários vídeos, ou consultar o que já aprendemos na base de conhecimento.
---

# YouTube Learn — vídeos viram playbooks

Objetivo: transformar vídeos do YouTube em **processos replicáveis** (passo a passo, ferramentas, custos, métricas) e separar o que é método real do que é promessa de guru. O foco padrão é **ganhar dinheiro com IA no TikTok**; para outros temas, use o mesmo fluxo e adapte a lente.

Tudo o que for analisado fica salvo em `knowledge/tiktok-ia/` para virar uma base de conhecimento cumulativa.

## Ferramenta

`.claude/skills/youtube-learn/scripts/yt_extract.py` (Python 3). Na primeira vez:

```bash
pip install -r .claude/skills/youtube-learn/scripts/requirements.txt
```

| Comando | Para quê |
|---|---|
| `python3 .claude/skills/youtube-learn/scripts/yt_extract.py video URL [URL ...]` | Metadados, descrição, capítulos e transcrição com timestamps → um `.md` por vídeo em `knowledge/tiktok-ia/videos/raw/` |
| `... search "termo" --limit 15` | Descobre vídeos sobre um tema, ordenados por views |
| `... list URL_DO_CANAL/videos --limit 20 [--by-views]` | Lista vídeos de um canal ou playlist |
| `... --cookies cookies.txt video URL` | Quando o YouTube pedir "confirme que não é um robô" |
| `... video URL --transcript arquivo.txt` | Usa uma transcrição colada pelo usuário quando o download for bloqueado |

Se a saída disser `SEM TRANSCRIÇÃO`, o YouTube bloqueou o IP (comum em servidores na nuvem). Tente de novo uma vez após ~1 min; se persistir, peça ao usuário para abrir o vídeo, clicar em **"…" → Mostrar transcrição**, copiar e colar o texto, salve num arquivo e rode com `--transcript`. Nunca invente o conteúdo de um vídeo que você não conseguiu ler.

## Fluxo

### 1. Coletar
- Link(s) informado(s) → rode `video`.
- Tema sem links → rode `search` com 2–3 variações em PT e EN (ex.: `"ganhar dinheiro com ia tiktok"`, `"tiktok shop afiliado ia"`, `"ai faceless tiktok monetization"`), mostre a lista ao usuário e sugira os 3–5 mais promissores (views altas, recentes, canais com histórico, títulos que prometem um processo e não só resultado). Pergunte antes de processar muitos.
- Canal → `list --by-views` e escolha os vídeos mais vistos/relevantes.

### 2. Ler a transcrição inteira
Leia o `.md` gerado do começo ao fim. Não resuma pela descrição ou pelo título: o método costuma estar no meio do vídeo e o pitch de venda no começo e no fim.

### 3. Analisar
Preencha o modelo em `references/analysis-template.md`, aplicando a lente de `references/tiktok-ia-lens.md`. Regras:
- **Cite timestamps** `[mm:ss]` para cada passo e afirmação importante, para poder conferir no vídeo.
- **Separe fato de alegação.** "Ganhei R$ 20 mil/mês" é alegação; "o programa exige 10 mil seguidores" é fato verificável. Marque o que precisa ser checado.
- **Explicite o implícito.** Se o vídeo pula etapas ("aí é só postar"), liste o que falta e como resolver.
- **Identifique como o criador ganha dinheiro com o próprio vídeo** (curso, afiliado de ferramenta, mentoria). Isso explica vieses.
- **Cheque as regras atuais do TikTok** quando o método depender delas (elegibilidade, conteúdo de IA, conteúdo reaproveitado). Se tiver busca na web, confirme; se não, sinalize como "verificar".
- Escreva em português, direto, em formato de checklist que dê para executar.

### 4. Salvar
- Análise: `knowledge/tiktok-ia/videos/<slug>.md` (mesmo slug do arquivo em `raw/`).
- Atualize o índice `knowledge/tiktok-ia/README.md`: uma linha na tabela de vídeos analisados e, se surgir um modelo de monetização novo, adicione-o à seção de modelos.
- Se 2+ vídeos descrevem o mesmo método, crie ou atualize um playbook consolidado em `knowledge/tiktok-ia/playbooks/<metodo>.md` juntando os melhores passos de cada um, com as fontes.

### 5. Responder
Mostre ao usuário: veredito em 1 frase, nota de 1 a 5 (aplicabilidade × confiabilidade), o processo em passos, primeiros 3 passos para testar esta semana e os alertas. Indique o caminho dos arquivos salvos.

## Comparar vários vídeos
Quando analisar mais de um vídeo sobre o mesmo tema, termine com uma tabela comparativa (método, investimento inicial, tempo até primeiro R$, dependência de regras da plataforma, nota) e uma recomendação de por onde começar.

## Consultar a base
Se o usuário perguntar "o que já sabemos sobre X", leia `knowledge/tiktok-ia/README.md` e os arquivos ligados antes de buscar vídeos novos.
