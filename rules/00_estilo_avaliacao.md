# Estilo de Avaliação (MPE) — regras de listas, simulados e correção

Especificação do estilo das avaliações de **Macroeconomia I (MPE Insper)**. É a fonte única
de verdade para os comandos `/exam-gen` (gerar lista + gabarito) e `/exam-grade` (corrigir a
resolução do aluno). Casada com o template `Listas/lista-exam.tex`.

## 1. Estrutura do documento

- Organização em **blocos temáticos** (1 a 4). Cada bloco mapeia a um conjunto de aulas e
  vale um total de pontos (no simulado completo: 4 blocos × 25 = 100 pts; numa lista
  temática, use 1–2 blocos).
- Cada bloco tem, tipicamente, **duas questões**:
  - **Questão objetiva** (10 pts): itens **a) e b)** de múltipla escolha (3 pts cada, 4–5
    alternativas, sem penalização por erro) + itens **c) e d)** de **Verdadeiro/Falso**
    (2 pts cada).
  - **Questão discursiva** (15 pts): um enunciado-mãe contextualizado + sub-itens **a), b),
    c)** (5 pts cada), com espaço "Resolução:".
- Numa **lista de exercícios** o tamanho é flexível (o aluno escolhe o escopo); mantenha a
  mesma anatomia de questões.

### Regra de V/F (sempre na capa/instruções)
Nota dos itens V/F $=\max\{0,\ \text{acertos}-\text{erros}/2\}\times$ valor do item. Itens
em branco não contam como erro.

### Blocos naturais em Macro I

| Bloco | Aulas | Tema |
|---|---|---|
| I | 1 | Mensuração e contabilidade nacional |
| II | 2-3 | Crescimento de longo prazo e Solow |
| III | 4-6 | Microfundamentos (consumo, trabalho, equilíbrio geral) |
| IV | 7-9 | Moeda, inflação e AD-AS novo-keynesiano |

## 2. Taxonomia das questões

- **Múltipla escolha (a, b):** aplicação direta de fórmula ou identificação de conceito.
  4–5 alternativas. Distratores plausíveis e do **mesmo comprimento** da correta
  (anti-chute), refletindo erros comuns de macro:
  - confundir **nominal × real**, **estoque × fluxo**, **nível × taxa de crescimento**;
  - confundir **PIB × PNB**, **deflator × IPC**, **valor adicionado × produção bruta**;
  - errar o sinal do efeito renda × substituição na oferta de trabalho;
  - confundir **poupança de estado estacionário × Regra de Ouro**;
  - atribuir a Solow crescimento de longo prazo de $y$ **sem** progresso tecnológico;
  - tratar deslocamento **ao longo** da curva AD/AS como deslocamento **da** curva.
- **Verdadeiro/Falso (c, d):** testam **recíprocas falsas** e armadilhas conceituais
  (ex.: "poupança maior eleva o $k^*$" é V; "poupança maior eleva o crescimento de longo
  prazo de $y$" é F; "toda alocação de equilíbrio competitivo é Pareto-eficiente" precisa
  das hipóteses do 1º TBE). Uma afirmação por item, sem ambiguidade.
- **Discursiva (a, b, c):** progressão crescente — montar o problema (restrições, agentes,
  hipóteses) → resolver/derivar (CPO, estado estacionário, equilíbrio) → interpretar
  (estática comparativa, bem-estar, política). Cada sub-item testa um aspecto distinto do
  mesmo cenário.

## 3. Contextualização (marca do estilo)

- **Toda** questão é ancorada em um cenário macro **brasileiro plausível e atual**:
  instituição, indicador ou episódio real — IBGE (Contas Nacionais, PNAD Contínua, SNIPC),
  Banco Central (Copom, Focus, Selic, agregados monetários M1-M4), IPEA, Tesouro Nacional,
  IPCA/INPC/IGP-M, PIB per capita comparado (PPP, Penn World Table), PNAD (taxa de
  participação, desemprego), reforma da previdência, regime de metas de inflação. O
  contexto é casca; o núcleo é o modelo do curso.
- Parâmetros numéricos **escolhidos para dar respostas fechadas limpas** (Cobb-Douglas com
  $\alpha=1/3$, $\delta=0{,}1$, elasticidades unitárias, log-utilidade). Declare "valores
  ilustrativos" quando convém.
- Não confundir realismo institucional com extrapolação teórica: **só modelos do curso**
  (ver `CLAUDE.md`, seção "NÃO extrapolar").

## 4. Formato da solução (gabarito)

- **Objetivas:** `Gabarito: X` + 1–3 linhas justificando (conta ou conceito).
- **Discursivas:** sequência numerada **"Passo — título. texto."** (montagem → derivação →
  resultado → verificação). Inclua:
  - **Intuição econômica.** parágrafo curto com o "porquê".
  - **Ref:** âncora bibliográfica (capítulo + seção, e página quando o `Map/` tiver).
  - **Rubrica de correção.** distribuição de pontos por passo, com:
    - **Tetos por erro conceitual** (ex.: "confundir taxa de poupança da Regra de Ouro com
      a que maximiza $k^*$ → máx. 2 pts no sub-item"; "usar $\Delta k = sf(k)$ sem
      depreciação → máx. 1 pt").
    - **Penalidades leves** por erro aritmético com método correto ($-1$ pt).
    - **Não-cumulatividade:** tetos conceituais prevalecem sobre penalidades leves (não se
      somam).
  - **Risco residual** (opcional): pegadinha comum / ambiguidade do enunciado a evitar.
- **Gráficos.** Em Macro I muita coisa se resolve no diagrama (Solow, AD-AS, restrição
  intertemporal). A rubrica deve pontuar **eixos rotulados, curvas nomeadas e direção do
  deslocamento** separadamente da conclusão verbal.

## 5. Uso da bibliografia (obrigatório)

Ancore conteúdo e referências nos livros do curso, via `Map/` e `rules/` quando existirem:

- **Kurlat (2020)** — **piso** (capítulo/seção em toda questão).
- **Benigno (2015)** — piso das Aulas 8-9; referenciar por **seção** (1-12).
- **Jones (2020, 5ª ed.)** — intuição, dados e exposição gráfica de crescimento.
- **Romer (2012, 4ª ed.)** — rigor formal adicional / derivações.
- **Carlin & Soskice (2024)** — contraste institucional no AD-AS.

⚠️ Ver `CLAUDE.md` → "Divergências de edição": o programa cita edições diferentes das que
estão em `Livros/`. Cite sempre a edição **local** e diga qual é.

⚠️ **Ljungqvist & Sargent está fora do escopo** — nunca usar como fonte de exercícios.

Formule questões **originais** a partir do entendimento dos conceitos; nunca copie ou
parafraseie exercícios do livro. Use o `Map/` para pesos por tópico e para páginas nas
linhas `Ref:`.

## 6. Convenções LaTeX

- Template: `Listas/lista-exam.tex`. Um único `.tex` com `\ifsolucoes`:
  - `\solucoesfalse` → **lista em branco** (espaço para resolver).
  - `\solucoestrue` → **gabarito + rubrica** (mesmo arquivo).
- Macros: `\bloco`, `\questao`, `\alternativas`, `\gabarito`, `\resolespaco`, `\passo`,
  `\intuicao`, `\refbib`, `\rubrica`; blocos de solução dentro do ambiente `sol` (excluído
  na lista em branco via pacote `comment`).
- **Regra global de PDF copiável:** preâmbulo já traz `\usepackage{lmodern}` e
  `\usepackage{cmap}` após `fontenc`. Compilar com `pdflatex` (2×) e verificar `pdffonts`
  (tudo **Type 1**, nunca Type 3).
- Matemática em `$...$`/`$$...$$`. Nunca usar `$` solto para moeda (escreva "120 reais").
- Gráficos em **TikZ/pgfplots** (Solow, AD-AS) — nunca imagem rasterizada.

## 7. Anti-padrões

- Não extrapolar o conteúdo do curso (checar `CLAUDE.md`). Em especial: nada de Bellman,
  DSGE estocástico, NKPC de Calvo log-linearizada ou Kurlat cap. 8.
- **Anti-chute de formatação:** a correta não pode ser sistematicamente a mais longa, nem a
  única com parênteses/fórmula/exemplo. Escreva os distratores no mesmo nível de detalhe e
  no mesmo estilo da correta (parênteses, hedges, símbolos, unidades) — às vezes mais
  longos, às vezes mais curtos. A única coisa que distingue a correta é ser verdadeira,
  nunca o formato. Distribua a posição da correta (não fixar A).
- V/F sem pegadinha = questão fraca; prefira recíprocas e hipóteses que "quebram".
- Solução sem rubrica e sem intuição = incompleta.
- Questão de Solow que não diz se é **por trabalhador** ou **por unidade de eficiência** =
  ambígua. Sempre declarar.
