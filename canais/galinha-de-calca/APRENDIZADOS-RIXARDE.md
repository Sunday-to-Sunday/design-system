# O que o canal do rixardê ensina para a Cleide dar certo

> Estudo dos 7 vídeos do canal [@rixardead](https://www.youtube.com/@rixardead) (cerca de 4h30, transcrições completas em `knowledge/tiktok-ia/videos/raw/`), feito em 20/10/2026.
> Quem é: criador brasileiro que vive de canais de IA no TikTok (programa de recompensas). Personagem de maior sucesso: o "Britinho", com 11 milhões de views em 5 a 6 dias e 6 milhões no primeiro vídeo.
> Os horários `[mm:ss]` apontam para o trecho exato de cada vídeo.

Vídeos estudados:
- **A** = [Te ensinando de graça a fazer vídeos bons com IA](https://youtu.be/3VT4ErWf9G4) (168 mil views)
- **B** = [Mostrei meus 10+ canais e como começar do zero](https://youtu.be/x7--wpxaWNE)
- **C** = [Faço R$10K/mês com IA](https://youtu.be/7oIW_OZoYJI) (876 mil views; [análise completa](../../knowledge/tiktok-ia/videos/faco-r-10k-mes-com-ia-e-vou-te-ensinar-de-graca-tudo-que-voc-7oIW_OZoYJI.md))
- **D** = [Como modelar qualquer vídeo com o Codex](https://youtu.be/nuOLSnE8XAw)
- **E** = [Qual o melhor horário pra postar no TikTok](https://youtu.be/ArU-uklVH_I)
- **F** = [Saturei o nicho de IA?](https://youtu.be/QO9buC-I1oI)
- **G** = [Faça R$1K/mês ou mais (ensaios de foto com IA)](https://youtu.be/Jqr2WcitG-M)

## Os 10 aprendizados que mudam o nosso jogo

### 1. O sucesso vem de juntar um formato que já funciona com uma virada própria
O Britinho nasceu de juntar dois formatos que já funcionavam: o humor bizarro do brain rot e os diálogos das novelinhas. Saiu algo que ninguém fazia [A 05:12–06:44]. Ele repete isso em tudo: "duas coisas podem acontecer" com anime deu 117 mil views [B 20:15]; o formato do "gordão que oferece itens" virou versão com personagens de anime [B 36:21]. "Tudo que vocês pegarem, coloquem a cara de vocês. O que tem aqui que faz eu assistir este e não o do outro?" [B 37:23].
**Para a Cleide:** já estamos fazendo isso, com o formato do #skateondog (animal fazendo algo impossível, câmera simples), mais a camada de influenciadora e o Brasil (Maracanã, feira, eleição). **Manter.** E cada episódio de data ou tendência (o EP03 com o Vasco) segue a mesma lógica dele: formato fixo com o assunto do dia.

### 2. Qualidade antes de quantidade
"Independente do nicho, o que importa mesmo é ser um conteúdo legal, um vídeo que as pessoas tenham vontade de assistir" [B 02:36]. Ele dificilmente sacrifica qualidade por frequência [B 29:38]. Quem copia de qualquer jeito ("criança de 10 anos fazendo") não sustenta [C 47:08].
**Para a Cleide:** melhor 1 vídeo por dia caprichado do que 3 apressados. O checklist de consistência e o "teste do é real?" são o nosso padrão de qualidade.

### 3. Consistência do personagem é o que sustenta o canal
Ele largou um canal de Roblox **com 350 mil views no 4º vídeo** porque a IA não mantinha o personagem igual, e isso "quebrava a imersão" [B 32:12–33:46]. O primeiro passo de qualquer vídeo dele é gerar os personagens de corpo inteiro, em fundo neutro, como referência [A 12:38–13:40]; em todo prompt de cena ele manda usar **exatamente** essa referência [A 20:57–22:00].
**Para a Cleide:** confirma o nosso protocolo (`personagem/CONSISTENCIA.md`). Duas regras novas que entraram nele por causa disso:
- **No Flow, use "Frames" (quadro inicial), não "Elementos/Ingredientes"**, quando quiser que o vídeo comece exatamente na imagem aprovada; em "Elementos" o Flow só usa a imagem como inspiração [A 33:07].
- **No máximo 3 referências por cena**; com mais, a IA confunde quem é quem e quem faz o quê [A 21:28].

### 4. Física e movimento complexo são o ponto fraco da IA: teste antes
Uma cena de um relógio girando levou **mais de 1 hora** de tentativas [B 34:16–35:18]; a primeira cena de bebês sendo separados levou mais de 1 hora e muitos créditos [C 1:42:03–1:44:41].
**Para a Cleide:** skate, beach tennis e futevôlei são exatamente esse tipo de movimento. Por isso:
- gerar **primeiro a cena mais difícil** do episódio, antes de gastar crédito no resto;
- para ações com começo e fim definidos (o pulinho no skate, a raquetada), usar a **técnica A/B**: imagem inicial e imagem **final** no modo Frames. A imagem B tem de ser o **estado final** da ação, não uma continuação [A 34:42];
- se a ação sair estranha no meio, **cortar na edição** antes do defeito [A 42:30];
- preferir ações em que o corpo dela se move pouco e o objeto faz o trabalho (o skate rola, a bola vem até ela).

### 5. Personagem vivo: expressão e ação em toda cena
"Foquem bastante nas expressões, nas ações dos personagens, pro vídeo não parecer morto, não parecer IA genérica" [B 46:04].
**Para a Cleide:** em todo prompt de vídeo, uma ação de galinha concreta (cabeça indo e voltando, arrepiar as penas, olhar de lado, bater asas). Já está nos roteiros; continuar sempre.

### 6. Cenas de apoio fazem parecer série, não clipe solto
"Quanto mais cenas de apoio e de continuidade, mais volumoso e melhor fica o vídeo"; uma cena de transição liga a anterior à próxima [A 37:15–38:48].
**Para a Cleide:** nos episódios com mudança de lugar, um plano curto de ligação. No EP03, por exemplo, ela passando pela catraca entre a rampa e a arquibancada. Entra como opcional nos próximos roteiros (e é obrigatório no formato longo "Um dia comigo").

### 7. Edição que dá ritmo
O que ele faz em todo vídeo [A 39:20–49:51; C 1:48–2:13]:
- aproximação lenta nas cenas paradas → **já está no `montar.py`** (opção `zoom: 1.06` por clipe);
- acelerar trechos lentos;
- transição rápida só entre lugares muito diferentes;
- normalizar o volume (já está no `montar.py`);
- um filtro de cor leve;
- legenda com fonte chamativa no meio da tela, quando houver fala (não é o nosso caso).

**Música:** ele cria trilhas próprias no **Suno** para não ter problema de direitos [A 46:43]. Boa opção para a Cleide ter um "tema" próprio.

### 8. Garimpo diário com uma conta dedicada
- Toda conta dele **só consome conteúdo do próprio nicho**, para o algoritmo entregar mais do mesmo [B 09:23–09:53].
- Ele navega com "olhar de produtor": vê um vídeo bom, abre o perfil, olha a média de views e salva [B 08:20–08:51].
- Usa o bloco de notas como "reservatório cerebral" de links e o Notion para organizar [B 10:24, 48:11].

**Para a Cleide:**
- usar a própria conta @cleideformosa só para assistir conteúdo de animais fazendo coisas impossíveis, IA realista e humor de flagra;
- salvar 5 links por dia em `referencias/garimpo.md`;
- uma vez por semana, rodar a análise de perfis (item 9).

### 9. Horário e hashtags por dados, não por palpite
Ele raspa os perfis de referência (Apify) e pede ao GPT os horários e as hashtags dos vídeos mais fortes. No exemplo dele, a faixa vencedora foi **das 9h às 10h** para vídeos de novelinha de fruta [E 08:49–09:52]. Mas ele mesmo diz que "não é ciência exata": já viu vídeo das 2h da manhã estourar [E 00:00–00:31].
**Para a Cleide:** criei o `perfis.py`, que faz isso sem conta no Apify:

```bash
python3 .claude/skills/estudio-ia/scripts/perfis.py @perfil1 @perfil2 @perfil3 --out canais/galinha-de-calca/referencias/perfis.md
```

Ele baixa só os metadados dos vídeos de cada perfil e compara os 25% mais fortes com o resto. Os vídeos fortes são medidos em relação à média do próprio perfil. O relatório mostra horário, dia, duração, engajamento, hashtags e os 10 vídeos mais fortes para modelar. Falta **escolher 3 a 5 perfis de referência** (animais realistas fazendo coisas absurdas, de preferência brasileiros).

### 10. Não se apegar: 10 vídeos sem resultado, muda
"Postou uns 10 vídeos, sentiu que teve qualidade, mas não tá bombando? Arquiva, sem dó" [B 17:43]. "No TikTok não tenha medo de mudar o conteúdo; o que importa é o vídeo ser legal e a pessoa ficar no vídeo" [B 20:46]. E nicho saturado não existe: o que é original cria público fiel [F 01:00–03:36].
**Para a Cleide:** combinar um teste honesto de **10 vídeos**. Se depois deles nenhum passar de ~10 mil views e a retenção estiver baixa, a primeira mudança é de formato (outros esportes e lugares, outra câmera); a segunda, de personagem. Até lá, não mudar a cada vídeo.

## Proteções que ele aprendeu apanhando

- **Nunca copiar quadro a quadro.** O primeiro vídeo do Britinho foi desmonetizado para sempre por ter sido modelado print a print de outro vídeo [B 43:30–44:00]. Modelar é copiar a estrutura e trocar todo o resto.
- **Guardar tudo** (imagens, clipes, projeto de edição): foi o que ele usou como prova para recuperar vídeos derrubados por "conteúdo não original" [B 44:00–44:30; C 2:15:53]. Já está no checklist de cada episódio.
- **Mais de uma conta monetizada.** O TikTok desmonetizou a conta dele 5 dias antes do pagamento; ele saiu do programa para garantir o saldo e ficou um mês sem postar [A 06:44–07:46; B 44:30]. Para nós: quando a Cleide monetizar, pensar numa segunda conta com outro formato.
- **Conteúdo "perturbador" derruba vídeo** [C 2:15:22]. A Cleide é leve por natureza; manter assim.

## O que ignoramos (e por quê)

- **Contas de Flow, Grok e GPT compradas em sites de revenda (GGMax, GameMarket)** e o **truque do teste grátis com cartão de 24 horas**: aparecem em quase todos os vídeos, inclusive como "patrocinador" [A 02:05; B 05:43; D descrição; E 01:22; F 04:24]. Violam os termos das ferramentas ou são fraude de cobrança; você usa a sua assinatura oficial do Flow.
- **Perfis apelativos e falsos** para crescer rápido [B 19:44, C 23:15]: ele mesmo diz que não gosta e que funciona pior.
- **Copiar vídeos de canais gringos e só dublar** [B 27:30]: ele fez e se arrependeu (público infantil, nada original).

## Sobre ferramentas (o que ele viu, o que vimos)

- Para ele, o **Grok** era o melhor gerador de vídeo, mas ficou caro e limitado; hoje ele usa o **Flow** (Nano Banana para imagens e o modelo de vídeo mais barato do Flow) [C 14:59–16:00; A 32:07].
- Ele criticou o **Magnific**: modelos ruins para fala em português, e o Kling 2.5 não gera som [B 05:43–06:44]. Bate com o que medimos no seu Magnific. Mas, como **a Cleide não fala**, um vídeo sem som (Kling 2.5: 325 créditos por 5 s em 1080p) mais o som ambiente colocado na edição pode ser uma alternativa barata ao Flow. Vale um teste.
- O "mapeamento de vídeo" dele (skill no Codex) faz o mesmo que o nosso `video_map.py`: storyboard, imagens âncora, transcrição e horário de postagem [D 06:42–08:16].

## Uma ideia de renda extra que ele mostrou (fora do canal)

Vender **ensaios de fotos com IA** para um público mais velho, com anúncio no Facebook e atendimento pelo WhatsApp: R$ 14,90 por 3 fotos e R$ 39,90 por 10. No primeiro dia, R$ 12 de anúncio voltaram R$ 200 [G 06:43, 10:51, 30:11]. Ele pede para tratar bem os clientes, porque são memórias das pessoas [G 11:54]. Não tem relação com a Cleide, mas usa as mesmas ferramentas (Flow com Nano Banana). Fica registrado para o futuro.

## O que mudou no projeto por causa deste estudo

- [x] `personagem/CONSISTENCIA.md`: modo Frames (não Elementos), no máximo 3 referências por cena, cena difícil gerada primeiro, imagem B como estado final.
- [x] `montar.py`: opção `zoom` (aproximação lenta) por clipe.
- [x] `perfis.py`: análise de horários, dias, duração e hashtags dos perfis de referência.
- [x] `yt_extract.py`: passa a preferir o áudio original em português quando o vídeo tem dublagem automática.
- [ ] **Você:** escolher 3 a 5 perfis de referência do TikTok para rodar o `perfis.py`.
- [ ] **Você:** usar a conta @cleideformosa só para consumir o nicho.
- [ ] Combinar o teste de 10 vídeos antes de mudar o formato.
