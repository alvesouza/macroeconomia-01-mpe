---
tags: [map, simulado, simulado-03, avaliacao, conceitual, solucao]
date: 2026-09-28
---

# Simulado 3: the conceptual mock and its solution

**Exam:** `Simulados/simulado-03-exam.pdf` (source `Simulados/simulado-03.tex`), 9 pages, 100 points.
**Numbers:** every figure quoted in these notes is recomputed by
`Simulados/simulado_codigo/check_simulado_03.py`, which also checks that every link below resolves.
**Figures:** `make_figures.py` in this folder writes `fig/*.svg`.
Up: [[00_indice]] · diagnoses: [[avaliacao-listas-1-4]] · [[avaliacao-listas-2-3-6]] · style:
[[estilo-do-professor]]

---

## What this exam tests, and why it looks the way it does

Five graded lists lost 27 items between them. None was lost on a model set up wrongly. The marks went
at three places ([[avaliacao-listas-2-3-6]] §1):

1. **the last object the question names** (9 items),
2. **the sentence after the formula** (11 items),
3. **the step where the words must agree with the sign** (3 items, the most expensive).

Simulados 1 and 2 were computational. This one is **conceptual**, built to train those three points:

- **Every True/False item needs a justification.** The verdict is worth 1 point and the justification 4.
  A correct verdict with the wrong mechanism scores 1 out of 5.
- **Every discursive item lists the objects to answer** at its end. The rubrics below give points
  per object, so a missing object costs exactly what it cost on the lists.
- **Items ask to explain, draw, sign or say what an observer gets wrong.** Arithmetic appears only
  where a short derivation *is* the explanation.

## Question map

| Q | Block | Topic | Lista anchor | Graded gap it retests | Notes to revise | Companion |
|---|---|---|---|---|---|---|
| [[q1-index-bias-and-deflator\|1]] | I | base-year bias; deflator vs CPI | L1 Q1(b)–(c) | L1 1(c): "the base year is merely a convention" ([[avaliacao-listas-1-4]] §3) | [[aula-01-mensuracao/02-real-nominal-and-indices\|indices]] | [Indices](../aula-01-mensuracao/companion-indices.html) |
| [[q2-brazil-paraguay-denominators\|2]] | I | aggregate vs per capita; PPP; per worker | L1 Q1(d)–(e), Q4(a) | L1 1(e): wrong mechanism for PPP; L1 4(a), L2 1(c): aggregate vs per capita | [[aula-01-mensuracao/04-cross-country-and-ppp\|PPP]] · [[aula-01-mensuracao/03-growth-arithmetic\|growth arithmetic]] | [PPP](../aula-01-mensuracao/companion-ppp.html) |
| [[q3-convergence-and-population\|3]] | II | conditional convergence; a fall in $n$ | L2 Q1(b); L1 Q4(b) | L2 1(b): "divergence"; L1 4(b): blank | [[aula-02-solow-mecanica/05-comparative-statics\|comparative statics]] · [[aula-03-solow-evidencias/04-quantifying-and-convergence\|convergence]] | [Transition](../aula-02-solow-mecanica/companion-transition.html) |
| [[q4-compliance-wedge-as-tfp\|4]] | II | a distortion read as TFP; the Solow transition | L2 Q2(a)–(d) | L2 2(d): blank, the most valuable item on that list | [[aula-03-solow-evidencias/05-growth-accounting-and-tfp\|growth accounting]] | [Hidden wedge](../aula-03-solow-evidencias/companion-hidden-wedge.html) |
| [[q5-labour-tax-and-beveridge\|5]] | III | labour tax with a transfer; Beveridge movement vs shift | L4 Q1(b), Q2(b)–(e) | L4 1(b): right formula, wrong story; L4 2(e) III: shift vs movement | [[aula-05-trabalho/02-static-model\|static labour]] · [[aula-05-trabalho/05-search-and-equilibrium\|search]] | [Labour supply](../aula-05-trabalho/companion-labour-supply.html) · [Flows](../aula-05-trabalho/companion-flows.html) |
| [[q6-euler-ricardo-savings-tax\|6]] | III | Euler and $\sigma$; $r$ in GE; Ricardian equivalence and its breakdown; savings tax | L3 Q1(a),(c),(e), Q2(b),(d); L5 Q1(d) | L3 1(c) and 1(e): words contradict the math; L3 1(a): $a$ never solved; L3 2(b), 2(d) | [[aula-04-consumo/03-income-and-substitution\|income and substitution]] · [[aula-04-consumo/05-ricardian-and-constraints\|Ricardo]] · [[aula-06-equilibrio-geral/01-equilibrium-as-benchmark\|GE]] | [Taxes and limits](../aula-04-consumo/companion-taxes-and-limits.html) · [Frozen capital](../aula-06-equilibrio-geral/companion-frozen-capital.html) |
| [[q7-quantity-equation-and-superneutrality\|7]] | IV | $MV=PY$ as an identity; neutrality vs superneutrality | L6 Q1(a)–(b), Q2 | L6 1(a): "$V$ is a residual" missing; L6 1(b): velocity not interpreted | [[aula-07-moeda-inflacao/02-money-demand\|money demand]] · [[aula-07-moeda-inflacao/03-equilibrium-and-neutrality\|neutrality]] | [Baumol–Tobin](../aula-07-moeda-inflacao/companion-baumol-tobin.html) |
| [[q8-regimes-and-two-shocks\|8]] | IV | $M$ vs $i$ regimes; an efficient shock vs a mark-up shock; AS as the constraint | L6 Q1(c)–(d); L7 Q2–Q4 | L6 1(c): no flexible-price case; L6 1(d): $M$ endogenous not said; Lista 7 traps 1, 2, 5 ([[lista-07]]) | [[benigno/04-equilibrium-geometry\|AS–AD]] · [[benigno/06-markup-shocks\|mark-up]] · [[benigno/10-optimal-policy\|optimal policy]] | [Money regimes](../aula-07-moeda-inflacao/companion-money-regimes.html) · [Two shocks](../benigno/companion-two-shocks.html) · [Loss bowl](../benigno/companion-loss-bowl.html) |

No scenario repeats a list, a textbook exercise or Simulados 1–2 (smartphone boom, German reunification,
debt-financed tax cut, Pix, Brazil–Portugal, "Custo Brasil" capital, agribusiness boom, fuel mark-up).

## The answers in one line each

| Q | Item | Verdict or core answer |
|---|---|---|
| 1 | a | **False.** Year-2 prices give 28.9%, year-1 prices 70.0%: the old prices overweight the good that got cheaper |
| 1 | b | **False.** Imported TVs are in the CPI and not in the deflator, so the CPI rises and the deflator does not |
| 2 | a | Per capita: Paraguay 1.47%, Brazil 1.99%. The headline is wrong: Paraguay is falling behind per person |
| 2 | b | PPP: 16,364 vs 15,000; the ratio falls from 1.50 to 1.09 (Balassa–Samuelson); market rates overstate the gap 1.375 times |
| 2 | c | Per worker: 36,364 vs 30,000, ratio 1.21. Market size, living standards, productivity: three different denominators |
| 3 | a | **False.** Only *conditional* convergence: growth depends on the distance to the country's *own* steady state |
| 3 | b | **False.** Aggregate growth falls 2% → 1%; per capita growth is 0 before and after; $y^*$ rises 8.0% |
| 4 | a | Labour share still $2/3$; $\hat A/A=0.862$; 20% of workers do compliance; the wedge sits in TFP |
| 4 | b | Residual $=1.70\%$ a year, all of it the reform; heavier rules would show as technical regress |
| 4 | c | $y^*$ rises 13.6%: an 8.9% TFP jump plus capital deepening; long-run growth of $y$ back to 0 |
| 5 | a | **False.** With $T=0$ hours are $1/(1+b)$, independent of $\tau$; with $T>0$ hours fall through the transfer |
| 5 | b | **False.** That is a movement *along* the curve to a steeper ray ($\theta\uparrow$); a shift needs $\mu$ or $s$ to change |
| 6 | a | $\sigma=2$: $c_1$ rises 51.00 → 51.24 (income effect). GE: $r=\rho=4.17\%$; with 3% growth, 10.51% |
| 6 | b | Free borrowing: nothing changes except $a$ (+10). With $a\ge-15$: $c_1$ 45 → 51.22; timing matters |
| 6 | c | $c_2/c_1$: 0.9888 (tax) vs 1.008 (lump sum); the savings tax distorts the intertemporal margin; lump sum is better |
| 7 | a | **False.** $V$ is the residual: it fell 0.75%. An identity cannot be refuted |
| 7 | b | **False.** Neutral, not superneutral: $i$ 6% → 12%, real balances −29.3%, velocity +41.4% |
| 8 | a | Set $M$ → $i$ endogenous; set $i$ → $M$ endogenous. Fixed $p$: liquidity effect; flexible $p$: neutrality |
| 8 | b | AS shifts left; $dy=-0.72$, $dp=+1.45$; both gaps $+1.28$; raise $i$ by 4 pp and both close |
| 8 | c | AS is the menu, AD the tool. Optimum $y-y_e=-1.80$, $p-p^e=+0.23$, $di=+3.38$ pp; trade-off because $y_n\ne y_e$ |

## How to use it

1. **Sit it timed: 3 hours, closed book.** Before writing each item, underline its objects and tick them
   at the end (rule 5 of [[avaliacao-listas-2-3-6]] §6).
2. **Only then read the notes, one per question.** Grade yourself with the rubric at the end of each.
   Every note has the same five parts per item: the full derivation with each operation labelled; the
   figure; **"The sentences that earn the mark"**; **"The tempting wrong answer"**; **"Revise"**.
3. **For every item you lost, open the Revise links and the companion**, then rewrite only the two
   sentences after the algebra. Those sentences are where the lists lost their marks.

## Out of scope, deliberately

No Calvo New-Keynesian Phillips curve (the AS used is Benigno's price-level form), no Bellman equations,
no Kurlat ch. 8. The Benigno loss weights come from his eq. (33), as in [[benigno/10-optimal-policy]].
