---
tags: [aula-03, kurlat-cap-05, contabilidade-do-crescimento, residuo-de-solow, ptf, capital-humano]
date: 2026-09-18
---

# 5. Growth accounting, development accounting, and what TFP is

**Kurlat §5.4–§5.5, printed pages 86–95.** Up: [[00-index]] ·
Prev: [[04-quantifying-and-convergence]]

> **Companion:** [Whose Fault Is the Gap?](companion-development.html) — decompose a country's
> income ratio into capital, human capital and TFP, and watch how much the answer moves when
> $\alpha$ moves.

Two decompositions that look identical and answer different questions. Growth accounting
decomposes a country's change **over time**; development accounting decomposes the gap between
two countries **at a point in time**. Confusing them is common and the algebra does not stop
you, so this note keeps them apart deliberately.

---

## 5.1 The method

Kurlat's three steps (p. 86):

1. Measure how much capital and labour changed.
2. Work out how much output change *should* follow. This is the step where theory does the work.
3. Attribute everything left over to productivity.

Start from a production function with technology as a **separate argument**, so that no
particular form of technical progress is imposed:

$$Y_t = F(K_t, L_t, A_t) \tag{5.4.1}$$

Kurlat is explicit (p. 86) that the labour-augmenting case $F(K,AL)$ is a special case of
(5.4.1), and that he wants to allow other forms. This is legitimate here because the exercise
will assume Cobb–Douglas, under which the forms are interchangeable up to units
([[03-technological-progress]] §3.4).

## 5.2 The growth-accounting identity, derived

Totally differentiate (5.4.1) with respect to time:

$$\dot Y = F_K\dot K + F_L\dot L + F_A\dot A$$

Divide by $Y$ and multiply and divide each term to create growth rates:

$$\frac{\dot Y}{Y} = \underbrace{\frac{F_KK}{Y}}_{\text{capital share}}\frac{\dot K}{K}
+ \underbrace{\frac{F_LL}{Y}}_{\text{labour share}}\frac{\dot L}{L}
+ \underbrace{\frac{F_AA}{Y}\frac{\dot A}{A}}_{\text{residual}}$$

The two elasticities are the factor **shares**, by [[02-markets-and-factor-prices]] §2.1 — this
is where competitive factor markets enter, and it is the whole reason the decomposition can be
implemented with national-accounts data rather than with an estimated production function. With
Cobb–Douglas they are $\alpha$ and $1-\alpha$:

$$\boxed{\;g_Y = g_A + \alpha\,g_K + (1-\alpha)\,g_L\;}$$

and in per-worker terms, subtracting $g_L$ from both sides and using $g_y=g_Y-g_L$,
$g_k=g_K-g_L$:

$$\boxed{\;g_y = g_A + \alpha\,g_k\;}$$

**The Solow residual** is what this is solved for:

$$g_A = g_Y - \alpha g_K - (1-\alpha)g_L$$

It is measured **by difference**. Nothing about $A$ is observed; it is defined as whatever makes
the identity hold. Abramovitz's phrase, which Kurlat echoes, is that it is *"a measure of our
ignorance"*.

### What the residual actually contains

Trap 7 in [[03_solow_evidencias]], and the single most important caveat in this session. $g_A$
absorbs, indiscriminately:

- genuine technical progress;
- **mismeasured inputs** — capital utilisation over the cycle, labour effort, quality change in
  machines;
- **composition** — a shift of workers from low- to high-productivity sectors raises measured
  TFP without anything becoming more productive;
- **allocative efficiency** — the same inputs distributed better across firms;
- **institutions, distortions, misallocation**;
- and any error in $\alpha$, $g_K$ or $g_L$.

Two consequences. First, TFP is strongly **procyclical** in the data, which is implausible as
technology and is mostly unmeasured utilisation — a point that matters for the business-cycle
chapters this course excludes but that should still be said. Second, and more important here:
calling the residual "technology" in a cross-country comparison is a decision, not a finding.

## 5.3 Development accounting — the level decomposition

A different question: not why a country grew, but why it is richer than another **now**. Take
levels rather than growth rates, with $y=Ak^{\alpha}$:

$$\frac{y_i}{y_{US}} = \frac{A_i}{A_{US}}\left(\frac{k_i}{k_{US}}\right)^{\alpha}$$

In logs, which is how it is reported:

$$\underbrace{\ln\frac{y_i}{y_{US}}}_{\text{observed gap}}
= \underbrace{\alpha\ln\frac{k_i}{k_{US}}}_{\text{capital's contribution}}
+ \underbrace{\ln\frac{A_i}{A_{US}}}_{\text{TFP, the residual}}$$

**Worked example.** A country with $y_i/y_{US}=0.10$ and $k_i/k_{US}=0.15$, at $\alpha=0.35$:

$$\text{capital contributes } 0.15^{0.35}=0.515,
\qquad \text{TFP must supply } \frac{0.10}{0.515}=0.194$$

So capital explains a factor of about 2 of the 10-fold gap and TFP a factor of 5. In log terms,
capital accounts for $\ln 0.515/\ln 0.10 = 28.8\%$ and TFP for 71.2%. Computed in
`check_growth.py`.

### A better decomposition: the capital–output ratio form

There is a well-known problem with the form above. Capital is *endogenous*: a country with high
TFP invests more and therefore has more capital, so attributing that capital to "capital" gives
TFP too little credit. Rewrite using $K/Y$ instead of $K/L$. From $y=Ak^{\alpha}$,

$$y = A^{\frac{1}{1-\alpha}}\left(\frac{K}{Y}\right)^{\frac{\alpha}{1-\alpha}}$$

*Derivation.* $y=Ak^{\alpha}=A(K/L)^{\alpha}=A(K/Y)^{\alpha}(Y/L)^{\alpha}=A(K/Y)^{\alpha}y^{\alpha}$,
so $y^{1-\alpha}=A(K/Y)^{\alpha}$ and raise both sides to $1/(1-\alpha)$. ∎

This is preferable because $K/Y$ is constant along a balanced growth path and does **not**
respond to TFP in the long run ([[03-technological-progress]] §3.3), so the two terms are closer
to independent. The exponent on the capital term rises to $\alpha/(1-\alpha)=0.54$, but it is
applied to a ratio that varies far less across countries than $k$ does — capital–output ratios
are broadly similar everywhere, capital–labour ratios are not. The net effect is that the $K/Y$
form attributes **more** to TFP. With $K_i/Y_i$ at 0.8 of the US ratio and the same
$y_i/y_{US}=0.10$, capital now accounts for only **5.2%** of the log gap instead of 28.8%.

## 5.4 Human capital

The natural objection: labour is not homogeneous, and a US worker has far more schooling than a
worker in a poor country. Put it in:

$$Y = AK^{\alpha}(hL)^{1-\alpha}$$

where $h$ is human capital per worker. **How $h$ is measured** is the part worth knowing,
because it is not arbitrary: it uses **Mincer** wage regressions. The empirical regularity is
that log wages rise roughly linearly in years of schooling,

$$\ln w = \text{const} + \phi\,S$$

with a return $\phi$ of about 6–10% per year of schooling. Since competitive labour markets pay
the marginal product, that return *is* the productivity gain, so

$$h = e^{\phi S}$$

with $\phi$ often taken piecewise (higher for the first four years, lower later), following Hall
and Jones (1999) and Klenow and Rodríguez-Clare (1997).

**What it buys.** A country with 4 years of schooling against the US 12, at $\phi=0.10$:

$$\frac{h_i}{h_{US}} = e^{0.10(4-12)} = e^{-0.8} = 0.45$$

and its contribution to the income ratio is $0.45^{1-\alpha}=0.45^{0.65}=0.60$. So human capital
explains a factor of 1.7 out of the tenfold gap — real but far from sufficient.

**Careful with the exponent on $h$.** In the $K/L$ form, $y=Ak^{\alpha}h^{1-\alpha}$, so human
capital enters as $h^{1-\alpha}$. In the $K/Y$ form the algebra of §5.3 gives

$$y = A^{\frac{1}{1-\alpha}}\left(\frac{K}{Y}\right)^{\frac{\alpha}{1-\alpha}}h$$

so $h$ enters with exponent **one**. Carrying $h^{1-\alpha}$ into the $K/Y$ decomposition is a
common slip and it understates human capital by a third.

**Putting the pieces together, with the numbers above.** In the $K/L$ form, physical and human
capital jointly account for **51%** of the log gap — roughly half and half with TFP. In the
preferred $K/Y$ form they account for **40%**, leaving TFP **60%**. Both are computed in
`check_growth.py`, and the second is the Hall and Jones (1999) figure; Klenow and
Rodríguez-Clare (1997) report 50–60% depending on specification.

The honest summary is therefore not "capital explains less than half" under every accounting.
It is that **under the decomposition whose two terms are closest to independent, TFP carries the
majority** — and that the answer moves by ten percentage points on a modelling choice a careless
reader would not notice. Say which decomposition you used.

## 5.5 Where do TFP differences come from? (§5.5)

Kurlat's §5.5 asks the question the residual forces. The candidate answers, none of which the
model delivers:

- **Misallocation.** The same technology used badly. If capital and labour are distributed
  across firms in a way that does not equate marginal products, aggregate TFP falls even with
  identical firm-level technology. Hsieh and Klenow (2009) estimate that moving China and India
  to US allocative efficiency would raise their TFP by 30–60%.
- **Institutions.** Property rights, contract enforcement, corruption — the Hall and Jones
  "social infrastructure", and Acemoglu–Johnson–Robinson's colonial-origins instrument.
- **Barriers to technology adoption.** Knowledge is non-rival and should diffuse; something
  stops it. Parente and Prescott.
- **Human capital quality** rather than quantity — years of schooling are not learning, and test
  scores across countries differ far more than enrolment does.
- **Measurement.** Some of the residual is not real.

The intellectually honest position, and the one to write in an exam: *the Solow model localises
the problem precisely and then hands it over.* It proves that the answer is not capital, which
is a genuine and non-obvious result, and it names the remaining object without explaining it.

> **Contrast: Jones (2020), chs. 4–6.** Jones runs the same development-accounting exercise and
> reports it as a bar chart of contributions country by country, which makes the TFP share
> visible at a glance and is the better format for an exam answer. He also carries the human
> capital construction in more detail than Kurlat, including the piecewise Mincer returns. Where
> Kurlat is stronger is the *rejection* argument of [[04-quantifying-and-convergence]] — Jones
> does not state the capital hypothesis as a falsifiable conjecture and test it three ways. Use
> Kurlat for the logic, Jones for the numbers. Local 2020 file, +25 offset ([[books-index]]).

## 5.6 Growth accounting against development accounting, kept apart

| | Growth accounting | Development accounting |
|---|---|---|
| Question | why did **this country** grow? | why is **this country** poorer? |
| Data | one country, many dates | many countries, one date |
| Object | growth rates $g_Y,g_K,g_L$ | levels $y_i/y_{US}$, $k_i/k_{US}$ |
| Residual | $g_A$, TFP **growth** | $A_i/A_{US}$, TFP **level** |
| Typical finding | for the US, TFP growth is about half of output-per-worker growth; for the East Asian miracles, capital dominated | TFP explains most of cross-country variation |

The East Asian result (Young, 1995; Krugman's "myth of Asia's miracle") is the best illustration
that the two answers can differ: Singapore's growth was almost entirely factor accumulation,
with a TFP residual near zero, while its **level** of TFP is high. Fast growth from accumulation
and a high productivity level are different facts, and only keeping the two accountings apart
lets you say both.

## 5.7 What to be able to do, cold

1. Derive $g_Y=g_A+\alpha g_K+(1-\alpha)g_L$ by total differentiation, naming where factor
   shares come from.
2. Compute a Solow residual from data and list at least four things it contains besides
   technology.
3. Run a development-accounting decomposition in logs and report the capital and TFP shares.
4. Derive the $K/Y$ form and say why it is preferred.
5. Explain how $h=e^{\phi S}$ is justified by Mincer regressions, and compute a human-capital
   contribution.
6. State the headline finding and the East Asian counterpoint.

Practice: Kurlat ch. 5, Exercises 5.3 *Causes of Growth and Growth Accounting* (p. 97), 5.5 and
5.6 on TFP differences (pp. 98–99). Worked in [[Resolucao/kurlat_solutions_ch05|ch05]].
