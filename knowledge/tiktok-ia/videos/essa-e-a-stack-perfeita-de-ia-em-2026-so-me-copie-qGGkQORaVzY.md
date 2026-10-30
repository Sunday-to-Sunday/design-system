# Essa é a stack perfeita de IA em 2026 (só me copie)

> **Veredito:** não é um método de ganhar dinheiro no TikTok, e sim uma forma de organizar o trabalho com IA (memória, skills, time de agentes, ferramentas conectadas). Vale copiar a estrutura para que o canal da Cleide rode com menos explicação a cada sessão.
> **Nota:** 4 · Aplicabilidade 5 · Confiabilidade 3
> **Fonte:** https://youtu.be/qGGkQORaVzY · Felipe Tâmbara · 2026-10-01 · 23:19 · 213.919 views
> **Analisado em:** 2026-10-30

## Resumo
A maioria usa a IA como um chat que começa do zero a cada conversa. A proposta é transformar isso num sistema de 4 camadas, em que cada uma resolve o limite da anterior [00:32]:
1. **Memória:** a IA sabe quem você é.
2. **Habilidades:** sabe como você faz as coisas.
3. **Orquestração:** um time de IAs, não uma só.
4. **Braços:** age dentro das suas ferramentas.

A demonstração é um único prompt, sem nenhuma pergunta de volta, que monta e publica uma página de captura [13:51–21:19].

## Modelo de monetização
- **Tipo:** nenhum para TikTok. É produtividade e infraestrutura.
- **De onde vem o dinheiro (do criador):** a comunidade paga "Core" [21:50]. A skill de segundo cérebro gratuita serve de isca para a comunidade.
- **Requisitos:** Claude Code (ou outro agente com terminal). O Obsidian é opcional [02:09].
- **Investimento inicial:** a assinatura das IAs. O Maestri é grátis para 1 workspace [11:44].
- **Tempo até o primeiro real:** não se aplica. O ganho é tempo por episódio.

## Processo passo a passo
1. **Memória (segundo cérebro)** [01:03–07:23]: uma pasta de arquivos de texto com quem você é, negócios, pessoas, branding (cores, fontes, voz), preços e o que performa ou não. Captura contínua: cada fato novo dito numa conversa vai para a ficha certa [03:12].
2. **Mapa no CLAUDE.md** [05:18–07:00]: o CLAUDE.md carrega em toda sessão e diz **onde** está cada coisa. A IA lê só a pasta de que precisa, em vez de um documento de 3 mil linhas. Isso barateia e acelera.
3. **Skills** [07:37–09:29]: um processo repetido vira um passo a passo (SKILL.md) com referências e exemplos. A skill também diz em que pasta da memória buscar o contexto ("leia X obrigatoriamente antes de montar qualquer cena") [09:06].
4. **Regra dos 3** [10:11]: "Se eu fiz algo três vezes seguidas, vou transformar isso numa skill. E nunca vou fazer a quarta."
5. **Orquestração** [10:51–13:19]: o modelo mais forte planeja, divide e revisa. Modelos médios executam e os baratos fazem as tarefas com passo a passo claro. Isso reparte o custo e os limites entre provedores. O orquestrador também é o juiz: devolve o trabalho que ficou ruim [16:29].
6. **Braços** [15:28–19:45]: ferramentas conectadas por MCP, API ou linha de comando. Basta conectar uma vez e registrar na memória.
7. **Um prompt, as 4 camadas** [20:05]: o pedido curto funciona porque a memória já tem o branding, a skill já sabe o processo e as credenciais já estão conectadas.

### Etapas que o vídeo pulou
- Como manter a memória limpa (ficha duplicada, informação velha). Ele mostra só a captura.
- Segurança: dar à IA acesso ao WhatsApp inteiro e às credenciais do banco de dados é um risco que ele nem menciona.
- Custo real do time de agentes (4 assinaturas).

## Ferramentas
| Ferramenta | Função no processo | Grátis/pago | Para nós |
|---|---|---|---|
| Obsidian | Visualizar a pasta de memória | Grátis | Opcional. O GitHub já mostra os `.md` |
| Claude Code | Agente principal com terminal | Pago | Já usamos (esta sessão) |
| Maestri | Orquestrar vários agentes | Grátis para 1 workspace | Não precisamos agora |
| Codex / Antigravity | Agentes secundários mais baratos | Pago / grátis | Não precisamos agora |
| NotebookLM | Transcrever vídeos e áudios longos | Grátis | Já temos o `yt_extract.py` e o Whisper |
| Zernio | Postar vídeo no TikTok e no Instagram | Pago | Já temos a Metricool conectada |
| Higgsfield | Imagem e vídeo | Pago | Usamos o Google Flow |
| Evolution API | WhatsApp | Não oficial | Evitar: risco de bloqueio do número |
| Wispr Flow | Ditar prompts por voz | Pago | Útil para quem faz tudo pelo celular |
| Supabase, Vercel, n8n, Notion, Fathom | Banco de dados, sites, automação, notas, reuniões | Grátis ou freemium | Fora do escopo do canal |

## Prompts, roteiros e templates
Prompt da demonstração (transcrito de [14:21]): "Crie uma página de captura para a Core com o branding oficial da Core. A página é um formulário rápido para quem quer entrar na Core e pede nome, WhatsApp e cidade. Regras: título forte, formulário em etapas, salve as respostas numa tabela e monte um time no Maestri. Não me pergunte mais nada, só monte."

A versão para nós: "Faz o EP04 da Cleide: [ideia]. Não me pergunte nada." Isso só funciona se a memória e a skill já tiverem tudo.

## Habilidades necessárias
- Organizar arquivos de texto e escrever uma SKILL.md (básico). Já fazemos isso no repositório.
- Orquestrar vários agentes (intermediário). Ainda não precisamos.

## Métricas e metas citadas
- Edição de vídeo: de 24 h com editor pago para 20 min com uma skill [10:11].
- Carrossel modelado de uma referência gringa: mais de 100 mil views [04:47].
- 30 a 50 sites na Vercel sem custo [18:41].

## Alegações vs. evidências
| Alegação | Evidência mostrada | Confiança |
|---|---|---|
| Duas empresas que já renderam mais de R$ 200 mil [00:00] | Nenhuma | Baixa |
| Um prompt monta e publica a página | Mostrada na tela, mas incompleta ("ainda tem tarefas") [21:19] | Média |
| O mapa no CLAUDE.md economiza tokens | Lógica correta: carrega o índice e lê só o arquivo necessário | Alta |
| Edição de vídeo em 20 min, sem pagar nada | Os efeitos do próprio vídeo | Média |

## Riscos e alertas
- **Regras da plataforma:** a Evolution API é uma API de WhatsApp não oficial e pode levar ao bloqueio do número. Não usar no número pessoal.
- **Segurança:** dar à IA as credenciais e o acesso a todas as conversas amplia o estrago se algo der errado. Conectar só o necessário.
- **Viés do criador:** ele vende a comunidade Core. Os números de faturamento são isca.
- **Excesso de ferramenta:** 15 ferramentas para um canal de TikTok é desperdício. Para nós bastam o GitHub (memória e skills), a sessão na nuvem, o Claude no Chrome (Flow), o Google Drive (troca de arquivos) e a Metricool (post).

## Aplicação no canal da Cleide (feito em 2026-10-30)
| Camada | O que já tínhamos | O que foi adicionado |
|---|---|---|
| Memória | `BIBLIA.md`, `CONSISTENCIA.md`, `knowledge/`, roteiros | O mapa do segundo cérebro no `CLAUDE.md` da raiz: toda sessão nova sabe onde está cada coisa sem precisar ser explicada. Também a seção "Memória viva" na BIBLIA, para registrar decisões e resultados no lugar certo |
| Habilidades | `estudio-ia`, `youtube-learn`, `viral-hooks`, `viral-tiktok-content` | A regra dos 3 na `estudio-ia` e o `prompt_chrome.py`. Montar o prompt do Chrome à mão já tinha acontecido; agora ele sai pronto de qualquer roteiro, com todos os textos dentro, sem depender de links do repositório privado |
| Orquestração | Esta sessão (roteiro, edição, post) + o Claude no Chrome (geração no Flow) | O fluxo documentado: a sessão na nuvem faz o pacote e o prompt, o Chrome gera e salva no Drive, e a sessão na nuvem monta e agenda |
| Braços | Metricool (post), Magnific (recusado pelo usuário) | A troca de arquivos pelo Google Drive (pasta "Cleide"), já que esta sessão tem o conector do Drive |

## Plano de teste (7 dias)
- [ ] Dia 1: abrir uma sessão nova e pedir só "faz o próximo episódio da Cleide". Conferir se ela acha a BIBLIA, a CONSISTENCIA e a skill sem explicação.
- [ ] Dia 2–3: gerar o prompt do Chrome com o `prompt_chrome.py`, colar na extensão e salvar os resultados na pasta do Drive.
- [ ] Dia 4–5: a sessão na nuvem baixa do Drive, confere, monta e agenda na Metricool.
- [ ] Dia 6–7: medir o tempo total por episódio e anotar na BIBLIA o que ainda pediu explicação. Cada coisa que precisou ser explicada 3 vezes vira regra ou skill.

## Citações úteis
> "A memória sabe quem você é e a skill sabe como você faz." [07:23]
> "Se eu fiz algo três vezes seguidas, vou transformar isso num estilo. E eu nunca vou fazer a quarta." [10:11]
> "Ele não vai ler literalmente todos os arquivos do meu segundo cérebro." [05:18]
