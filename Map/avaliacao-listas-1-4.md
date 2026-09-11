---
tags: [map, macro1, correcao, avaliacao, diagnostico]
date: 2026-09-06
---

# Evaluation of the graded work — Listas 1 and 4

Read from `Listas/correções/Lista+1.pdf` (5 pp.) and `Listas/correções/Lista+04.pdf`
(7 pp.), both **CamScanner scans with no text layer**, read as images. The grader marks in
red pen: **✓** accepted, **✗** rejected, **?** questioned.

Compared throughout against the instructor's own key in `Listas/soluções do instrutor/`
(see [[estilo-do-professor]]) and against the statements in
[[Listas/MPE_Macro1_2026_Lista1|Lista 1]] and [[Listas/MPE_Macro1_2026_Lista4|Lista 4]].

> **On certainty.** The ✓/✗ marks are unambiguous. The *reason* for a ✗ is sometimes
> written and sometimes not. Where I could verify the error independently I say so; where
> the reason is inferred I mark it **(inferred)**.

Back to [[00_indice]] · [[cobertura]]

---

## 1. Scorecard

### Lista 1 — 10 points

| Item | Mark | Answer given | Correct | Verdict |
|---|---|---|---|---|
| 1(a)(i) | ✓ | 56 | 56 | correct |
| 1(a)(ii) | ✓ | 42 | 42 | correct |
| 1(b) value | ✓ | 108 | 108 | correct |
| 1(b) growth | **✗** | 0,6842 | **0,928** | **arithmetic slip** |
| 1(c) value | ✓ | 34 | 34 | correct |
| 1(c) growth | **✗** | 0,3125 | **0,235** | **transcription slip** |
| 1(c) explanation | **✗** | "base year is merely a convention" | substitution bias | **conceptual** |
| 1(d) | ✓ | 2,24 | 2,24 | correct |
| 1(e) value | ✓ | 16 | 16 | correct |
| 1(e) explanation | **✗** | "import/export costs" | non-tradables / Balassa–Samuelson | **conceptual** |
| 2(a) | ✓ | "violência" | — | correct |
| 2(b) | **✗** | migration rich-violent → poor-safe | — | (inferred) |
| 3 | ✓ | Europe/Africa converge, Latin America not | — | correct |
| 4(a) | **✗** | per-capita transition only | + **aggregate** answer | **incomplete** |
| 4(b) | **✗** | *not attempted* | — | **blank** |

**Nine ✓, six ✗.** Every *numerical value* asked for was right. Everything lost was either
a two-second arithmetic slip or an explanation.

### Lista 4 — 10 points

| Item | Mark | Verdict |
|---|---|---|
| 1(a) | ✓✓✓ | correct — Lagrangian route, implicit labour supply, rotation of the budget line all accepted |
| 1(b) math | ✓ | $\partial l^\*/\partial\tau = \dfrac{T}{(1-\tau)^2 w(\gamma l^{\gamma-1}+b)}>0$ — correct |
| 1(b) intuition | **?** | grader queried it — see §3 |
| 2(a) | ✓ | correct |
| 2(b) | **✗** | see §3 |
| 2(c) | ✓✓✓✓✓ | fully correct — $f=\mu\theta^\alpha$, $q=\mu\theta^{\alpha-1}$, $f=q\theta$, both signs |
| 2(d) | **✗** | **wrong agent** — see §3 |
| 2(e) I–II | ✓ | $\partial\ln v/\partial\ln\mu=-1/\alpha<0$ — correct |
| 2(e) III | **✗** | shift vs movement muddled |

---

## 2. The pattern, in one line

> **The algebra is strong. The words are what is costing the marks.**

Of the 11 rejected items across both lists, **8 are verbal** (explanations, intuition,
identifying agents) and only **2 are arithmetic**, with 1 blank. Not one item was lost
because a model was set up wrongly or a derivative was computed wrongly.

That is an unusual and *fixable* profile. It means the marginal hour is worth far more
spent on writing the two sentences after the algebra than on more algebra.

---

## 3. Item-by-item diagnosis of what to fix

### Lista 1, 1(b) — 52/56 mis-cancelled

Written: $\frac{108}{56}-1=\frac{52}{56}=\frac{13}{19}=0{,}6842$.
$52/56$ cancels by 4 to $\mathbf{13/14}=0{,}9286$, not $13/19$. The instructor's key says
$g_y=92{,}8\%$.

**Fix:** when you cancel, check by multiplying back. $13\times4=52$ ✓, $14\times4=56$ ✓.

### Lista 1, 1(c) — wrong denominator carried

Written: $\frac{42}{32}-1$. The value computed two lines above is **34**, not 32.
Correct: $\frac{42}{34}-1=\frac{8}{34}=0{,}235$, i.e. **23,5%**, matching the key.

**Fix:** both slips are of the same species — a number changes between the line where it
is computed and the line where it is used. Circle each intermediate result and copy from
the circle.

### Lista 1, 1(c) explanation — the missing economics ⭐

Written: *"a diferença se dá ao fato da escolha do ano a ser fixado os preços é meramente
uma convenção para ser possível comparar a produção de anos diferentes."*

True, and worth nothing, because it does not say **which direction each convention biases
the answer, or why**.

**What earns the mark.** Prices moved in opposite directions ($p_1: 8\to2$, $p_2: 4\to6$)
and quantities substituted toward the good that got cheaper ($q_1: 5\to12$, $q_2: 4\to3$).
Therefore:

- Valuing **new quantities at old prices** (Laspeyres) prices a large $q_1$ at the old high
  price 8 → **overstates** growth (92,8%).
- Valuing **old quantities at new prices** (Paasche) prices a small $q_1$ at the new low
  price 2 → **understates** growth (23,5%).

That is **substitution bias**, and it is why agencies chain indices (Kurlat ch. 1).

### Lista 1, 1(e) explanation — wrong mechanism ⭐

Written: *"custo de importação e exportação, fazendo os preços não serem um a um."*

That names a friction in **traded** goods — which are exactly the goods where the market
exchange rate works *best*. The mechanism runs the other way.

**What earns the mark.** The market rate prices only what is traded. Most output is
**non-traded** (housing, transport, services, government), and non-traded goods and labour
are systematically cheaper in poorer countries because wages are lower and no arbitrage
forces convergence. Converting at the market rate therefore values non-traded output at a
price nobody there pays and **understates** real production. Hence 2,24 at market rates
against **16** at PPP — a factor of more than 7. This is **Balassa–Samuelson**.

### Lista 1, 4(a) — right transition, missing half the question ⭐

The work shown is correct: $y_1/y_0=2^{-\alpha}$; $k_{ss}=\left(\frac{s}{n+\delta}\right)^{\frac{1}{1-\alpha}}$;
and $\frac{\dot k}{k}=(n+\delta)\left(2^{1-\alpha}-1\right)>0$ — I verified this
independently and it is right.

**What is missing** is that the question asked about **o PIB e o PIB per capita** — two
objects — in **two horizons**. The answer covers per-capita only. The instructor's key adds
the line the answer never reaches:

> $Y_t > Y_{t_0-\varepsilon}$ **pois** $L_t > L_{t_0}$

Total GDP ends up **higher** than before the earthquake, because population kept growing at
$n$ throughout the transition, even though GDP per capita merely returns to where it was.

**Fix:** whenever $n>0$, write two lines, one for $y$ and one for $Y$. This is the single
most-repeated warning in the instructor's key (it recurs in PSET 2 Q1(c) as
*"Not per capita (for S) but still a gain"*).

### Lista 1, 4(b) — blank, 1,5 points

Unattempted. The instructor's key is four lines:
$n\to n' <n \Rightarrow k'_{ss}=\left(\frac{s}{n'+\delta}\right)^{\frac{1}{1-\alpha}}>k_{ss}$,
a second flatter $(n'+\delta)k$ ray on the Solow diagram, a time path rising past the old
steady state, and the note *"higher levels, lower SS growth, higher growth during
convergence."*

**Fix:** 1,5 points for four lines and one diagram. Never leave a Solow comparative static
blank — the diagram alone carries most of the credit.

### Lista 4, 1(b) — correct formula, wrong story ⭐⭐

This is the most interesting mark on either paper. The grader put **✓** on the mathematics
and a large red **?** on the words.

Written: *"quanto menor $\tilde w$, mais barato será o lazer, e reduz o consumo."*

That is the **substitution effect alone** — and with $\ln c$ utility the substitution
effect is *exactly cancelled* by the income effect. Look at the instructor's own boxed
equation:

$$(1-n)^\gamma - b\,n \;=\; \frac{b\,T}{(1-\tau)\,w}$$

**If $T=0$ the right-hand side is zero and neither $\tau$ nor $w$ appears at all.** With log
consumption utility and no transfer, labour supply is completely independent of the wage
and of the tax.

The whole effect works through the **transfer**. $T$ is unearned income: it raises wealth
without changing the price of leisure, which is a pure income effect on hours. Raising
$\tau$ lowers $\tilde w$, which makes the *same* $T$ larger relative to earning capacity,
strengthening that pure income effect.

The submitted derivative already encodes this — $T$ sits in the numerator, so
$\partial l^\*/\partial\tau=0$ when $T=0$. The formula was right and the sentence beneath it
contradicted it. **That mismatch is what the "?" is asking about.**

### Lista 4, 2(b) — Beveridge curve

I verified the submitted algebra independently and **it is correct**:
$v(u)=\left[\frac{s(1-u)}{\mu}\right]^{1/\alpha}u^{-\frac{1-\alpha}{\alpha}}$ matches the
key exactly, and
$\frac{dv}{du}=-\frac{v}{\alpha u}\left[\frac{u}{1-u}+(1-\alpha)\right]<0$ is right.

**(inferred)** The question asked to *"derive the equation that equates job creation and job
destruction"* and to *"explain why it slopes the way it does."* The submitted page jumps
straight to algebra: it never writes $s(1-u)=\mu v^\alpha u^{1-\alpha}$ **as** the
job-creation-equals-job-destruction condition, and it gives the sign of the derivative in
place of an economic explanation. The instructor's key writes the words explicitly:
**"BC → job creation = job destruction."** The graph drawn also carries a "$\mu$ cai"
annotation belonging to part (e).

**Fix:** name the condition in words before solving it; then explain the slope in flow
terms (higher $u$ → more searchers → more matches per vacancy, *and* fewer employed → smaller
inflow; both mean fewer vacancies are needed to balance the flows).

### Lista 4, 2(d) — the externality is on **other people** ⭐⭐

Written: *"a firma toma o $q$ menor, mas o seu prejuízo é infinitesimal, logo ela não
considera essa pequena perda."*

**Wrong agent.** A loss to *itself* would be internalised by definition — that is what
"internalised" means. The content of the word *externality* is that the cost lands on
somebody else.

The instructor's key:

> Congestion externality → the firm posting the vacancy is **better off**, but **others**
> are harmed. Workers also benefit from a higher chance to find a job.

**The full answer.** Posting one extra vacancy raises $\theta$, so $f=\mu\theta^\alpha$ rises
and $q=\mu\theta^{\alpha-1}$ falls. Therefore:
**workers gain** (higher job-finding rate); **other firms lose** (their vacancies are harder
to fill); **the posting firm gains** privately. And $\partial m/\partial V=\alpha q<q$ — the
extra vacancy does *not* produce one extra match, and the shortfall is the friction. The
firm weighs only its own expected profit and internalises neither the congestion it imposes
on rivals nor the benefit it confers on workers.

### Lista 4, 2(e) III — shift vs movement

Written: *"aumenta o número de vagas e desloca a curva de Beveridge, o movimento pela curva
se dá pela variação de $v$ dado a relação de vagas e desemprego."*

The direction is right ($\mu\downarrow \Rightarrow v\uparrow$, consistent with the
correct $\partial\ln v/\partial\ln\mu=-1/\alpha$), but the distinction asked for is not made.

**What earns the mark**, in the key's own words: a fall in $\mu$ is *"a shift in all $v$–$u$
values and possible states, rather than just changing how $\theta$ is split between $u$ and
$v$."* A **movement along** the curve changes tightness at a *given* matching technology; a
**shift** changes the matching technology itself, so every $(u,v)$ pair now yields fewer
matches and the whole set of feasible steady states moves out. An outward shift of the
Beveridge curve is the standard empirical diagnostic of deteriorating matching efficiency,
as opposed to a cyclical movement along it.

---

## 4. Four rules to carry into Lista 5 and the final

1. **Answer every object the question names.** "O PIB e o PIB per capita" is two answers.
   "Which agents gain and which lose" is a list, not a sentence. This alone accounts for
   4 of the 11 rejected items.

2. **Never let the words contradict the formula.** Lista 4 1(b) had the right derivative and
   the wrong story. Before writing the intuition, set every other parameter to its knife-edge
   value and ask what the formula then says. Here: set $T=0$ and the effect vanishes — so the
   story must be about $T$.

3. **An externality is always about somebody else.** If your sentence about an externality
   has the acting agent as the one harmed, it is wrong.

4. **Circle intermediate results and copy from the circle.** Both arithmetic losses on
   Lista 1 were values that changed between the line computing them and the line using them.

---

## 5. Where this feeds

- [[estilo-do-professor]] — what a complete answer looks like to him
- `Leituras/psets-01-04-instructor-solutions-narrated.txt` — his four keys, narrated
- `Leituras/lista-05-general-equilibrium-narrated.txt` — Lista 5, due **08/09/2026**
- [[study-guide]] · [[topics-index]] · [[cobertura]]
