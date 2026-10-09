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
- **Majority-vote guessing.** If every distractor changes exactly one feature of the key, the
  key is the feature-by-feature majority of the options and can be found without the
  content: at least one distractor per item combines two named mistakes. Check the correct
  letters across the whole list too (every letter used, no repeating pattern), above all
  when different blocks were written separately.
- V/F sem pegadinha = questão fraca; prefira recíprocas e hipóteses que "quebram".
- Solução sem rubrica e sem intuição = incompleta.
- Questão de Solow que não diz se é **por trabalhador** ou **por unidade de eficiência** =
  ambígua. Sempre declarar.

## 8. Graduate level (opt-in for lists and mock exams)

Chosen in `/exam-gen` Step 3 (*Graduate level* depth, *Graduate* math complexity). The
anatomy of §1–§4 stays (blocks, objective + discursive, rubric, intuition, `Ref:`); the bar
moves.

**Scope.** The syllabus does not grow: the exclusions of §7 and `CLAUDE.md` hold (no
Bellman/dynamic programming, no stochastic DSGE/RBC, no Calvo NKPC, no Kurlat ch. 8 or
12–15, no Ljungqvist & Sargent). What rises is the mathematics applied to the course's own
models. In this mode Romer (2012) and the harder Kurlat exercises are the main source of
ideas, and complementary books may raise the level. *Why:* a harder list that changes the
topics trains for an exam the student will not sit.

**Symbolic by default.** Graduate lists and mock exams are posed and solved in parameters
($\alpha,\beta,\sigma,\dots$ with their admissible ranges), without calibrated numbers:
answers are closed forms, conditions, signs, orderings and limits; multiple-choice options
are expressions or conditions; a result with no closed form is characterized (existence,
uniqueness, monotonicity, bounds) and proved. The Brazilian context stays as narrative.
`/exam-gen` asks whether to include numbers; only on an explicit yes do items add calibrated
values, numeric sensitivity tables and numbered axes. *Why:* at this level the skill tested
is deriving and signing results; calibrated numbers move the effort to arithmetic and let a
student who cannot read the model score by computing.

**Questions.**
- Every discursive question starts from **primitives** (preferences, technology,
  constraints, market structure). The student derives what an intermediate list would hand
  over (Euler equation, steady state, AS slope, money demand, Beveridge curve) and then uses it.
- General functional forms come before special cases: CRRA before log, CES before
  Cobb-Douglas, general $u(c,l)$ before a parametric one. Distractors and traps come from
  applying the special case where it fails.
- Each block contains at least one item of each kind: a **proof** ("show that", existence,
  uniqueness, sign of a derivative by implicit differentiation); a **dynamic
  characterization** (linearization around the steady state, eigenvalues, saddle path,
  half-life, stability of a steady state); a **limit or knife-edge case** ($\sigma\to1$,
  $\beta\to1$, elasticity of substitution $\to1$, $\kappa\to0$ or $\infty$); a
  **quantification** in closed form (a second-order welfare cost, a consumption-equivalent
  loss, a multiplier; calibrated numbers only when opted in).
- Objective items need three or more derivation steps or a trap only the general case
  reveals; none is answerable by plugging into a memorized formula.
- **Cross-topic questions.** Every discursive question chains at least two course topics
  that interact inside one model: the result of one is an input of the other (measurement ×
  growth accounting, consumption × equilibrium interest rates, labor supply × taxes ×
  welfare, money × fiscal policy × inflation dynamics, AS–AD × fiscal policy or household
  debt). Name the topics in the question's heading. At least two objective items per block
  also cross topics. *Why:* at this level the exam tests whether a result can be carried from
  one model into another, not whether one model can be reproduced.
- **Integrative questions.** Each graduate list has an integrative block, and each block of a
  graduate mock exam has at least one integrative question: one model in which three or more
  topics from at least two different lectures cross (e.g. Solow transition × welfare
  measurement × discounting; life-cycle saving × labor supply × pension design; growth ×
  equilibrium interest rates × money demand × seigniorage; AS–AD × household debt × fiscal
  transfers × optimal policy). Name the topics in the heading. *Why:* the final exam rewards
  carrying a result through several models; questions that stay inside one topic do not train it.
- **No answer in the statement.** Ask to find, characterize or determine; do not print the
  formula to be proven, except when the result has a name the student should recognize.
- **Parameter analysis in every discursive question**, as the course's lists do ("what
  happens to … if … rises", "for which values of σ …", "as β → 1"): (i) the sign of each
  comparative static, proved by implicit differentiation or a closed form; (ii) a table of
  those signs (results × parameters; $+$, $-$, $0$, or the condition that decides the sign),
  plus a numeric sensitivity table computed by the check script when numbers are opted in;
  (iii) limiting and knife-edge values; (iv) the economic reading of each change.
- **Graphs where the model is read graphically, not in every question.** Each block has at
  least one sub-item that asks the student to draw (phase diagram with loci, arrows and the
  saddle path; AS–AD shifts; Beveridge and job-creation curves; a Laffer curve; a kinked
  budget set; a policy trade-off line), and at most half of the sub-items do. The answer key
  draws it in TikZ/pgfplots from the model's own equations, never a freehand sketch; in
  symbolic mode any admissible parameter values shape the curves, numeric ticks are
  suppressed, and axes, curves and points carry symbolic labels ($k^*$, $y_n$, $\tau^*$).
- Discursive questions have four or five sub-items **a)–e)** (e.g. 3×5 = 15 pts): set up →
  derive → characterize (proof, dynamics, limits) → quantify → parameter analysis.

**Solutions.**
- Rebuild each model from its primitives every time: state the problem, the Lagrangian or
  the substitution used, every FOC (with what the multiplier means), the market-clearing or
  equilibrium condition, then solve. No step is "it can be shown"; second-order or
  sufficiency conditions are noted where they decide the answer.
- Each step says what it uses ("from the household FOC (2) and goods clearing (4)").
- An independent script (`Listas/<list>-check.py`) verifies every result and aborts on a
  mismatch: each closed form with sympy; each claimed sign, limit and ordering (symbolically,
  or at many random admissible parameter draws); each existence claim by root-finding at
  random draws; that every multiple-choice distractor differs from the key; and, with numbers
  opted in, every number, table entry and plotted coordinate. *Why:* long derivations hide
  sign and exponent slips that a reader cannot catch at a glance.
- **Length: 10 to 15 pages of answer key per list**, in the same format (numbered steps,
  intuition, `Ref:`, rubric). If the key has fewer than 10 pages, add questions (integrative
  ones first) until it reaches 10, never pad the prose; above 15, cut questions, never
  steps. A graduate mock exam's key has at least 10 pages. Spend the space on derivations,
  proofs, sign tables and figures. *Why:* a cross-topic question with a parameter analysis
  cannot be solved step by step in one page, and the student studies from the key.

**Rubric.** Score the setup and each derivation step separately. Caps: a special-case
result used in the general case (max. half the item); a result the item asks to derive that
is quoted instead (max. a third); a stability, sign or limit claim without proof (0 for that
line); a parameter analysis that lists signs without proving them or without reading them
economically (max. half the item); a cross-topic question answered inside one model only,
ignoring the link (max. half the item). A requested graph is scored on its own lines: axes
and labels, each locus with its slope, the shift or dynamics (arrows, saddle path, jump), and
the point read off it; a graph contradicting the student's algebra loses the graph points.
