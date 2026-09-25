---
tags: [map, lista, lista-07, benigno, adas, aula-08, aula-09]
date: 2026-09-25
---

# Lista 7: map and analysis

**The list.** [[Listas/MPE_Macro1_2026_Lista7.md|Lista 7]] (PDF `Listas/MPE_Macro1_2026_Lista7.pdf`):
four questions, 10 points. **Solution:** `Resolucao/lista7_resolucao.pdf` (source `.tex`, figures
and numbers in `Resolucao/lista7_codigo/l7_figuras.py`). Up: [[00_indice]] ·
[[exercises-index]] · [[benigno/00-index]].

## What kind of list it is

- **Pure Benigno (2015); no textbook exercise.** It is the first list with no "Based on Kurlat"
  anchor. It covers lectures 8 **and** 9, as [[exercises-index]] predicted after Lista 6 skipped
  Benigno entirely.
- **Conceptual, not computational.** No calibration is given and no number is asked for. The
  marks are for curve, direction, sign and *mechanism*. The solution adds Benigno's own
  calibration only to size the answers.
- **One argument in four steps.** Q1 asks why the model has its ingredients. Q2 uses them: one
  shock on AS, one policy on AD. Q3 isolates the ingredient that makes $y_n\neq y_e$. Q4 prices
  that difference with a loss function.
- **The last question is the most conceptual**, as in every earlier list. Q4 generalises
  Benigno's eq. (33) to free weights $\phi_y,\phi_p$ and a free target $y^\ast$. The half that
  carries the marks is *why* AS is the constraint.

## Question → source → where it is already derived

| Q | Pts | Asks | Benigno (printed pp.) | Derivation note | Companion |
|---|---|---|---|---|---|
| 1 | 3 | NK vs New Classical vs original Keynesian, on 4 dimensions, with evidence and implications | §1–§3 pp. 503–506; §4 p. 507–508 (menu costs, sticky info, NC Phillips curve); §11 pp. 521–522 | [[benigno/00-index]], [[benigno/01-household-and-ad]], [[benigno/02-firms-and-as]] §2.1, §2.8, [[benigno/10-optimal-policy]] §10.1 | — |
| 2a | 1.5 | temporary rise in desired mark-up | §7, Fig. 9, pp. 513–514 | [[benigno/06-markup-shocks]] §6.2 | [Two Shocks](benigno/companion-two-shocks.html) |
| 2b | 1.5 | cut in the nominal rate | §5, Figs. 3–5, pp. 509–511 | [[benigno/04-equilibrium-geometry]] §4.4 | [Two Shocks](benigno/companion-two-shocks.html) |
| 3 | 2 | $y_n$ vs $y_e$; why the mark-up moves only $y_n$ | §4.1–§4.4, eqs. (14), (15), (19), pp. 507–509 | [[benigno/03-natural-and-efficient]] §3.3–§3.5 | [The Wedge](benigno/companion-wedge.html) |
| 4 | 2 | the loss $\phi_y(y-y^\ast)^2+\phi_p(p-p^e)^2$ subject to AS | §11, eqs. (33)–(35), Fig. 14, pp. 521–523 | [[benigno/10-optimal-policy]] §10.1–§10.5 | [The Loss Bowl](benigno/companion-loss-bowl.html) |

Complementary for Q1 only: Romer (2012), ch. 6 (Lucas imperfect information, NK price-setting),
and Carlin & Soskice (2024). Use them for contrast, never to raise the level.

## The answers in one line each

| Q | Core answer | Sized (Benigno's calibration: $\alpha=.66$, $\sigma=.5$, $\eta=.2$, $\kappa=1.133$, $\theta=8$) |
|---|---|---|
| 1 | NK = New-Classical **method** (RE, optimisation) + Keynesian **friction** (pre-set prices). It adds monopolistic competition (someone sets prices, $P>MC$) and an interest-rate instrument (AD is the Euler equation, no LM). Its welfare loss is **derived**, with target $y_e$ | — |
| 2a | AS up/left through $(p^e,y_n')$; AD **still**; $y\downarrow$, $p\uparrow$ (stagflation); $y-y_n>0$ but $y-y_e<0$ | $d\mu=5\%$: $dy_n=-2.27$, $dy=-0.82$, $dp=+1.64$, $y-y_n=+1.45$ |
| 2b | AD up by $\lvert di\rvert$ (right by $\sigma\lvert di\rvert$); AS still; $y\uparrow$, $p\uparrow$ along AS | $di=-1$: $dy=+0.32$, $dp=+0.36$ |
| 3 | Market: $\mathrm{MRS}=A/(1+\mu)$; planner: $\mathrm{MRS}=A$; so $y_n-y_e=-\mu/(\sigma^{-1}+\eta)$. The planner's problem has no $\mu$ in it | $\mu=5\%$: $y_n-y_e=-2.27\%$; lost surplus $\tfrac12\mu^2/(\sigma^{-1}+\eta)=0.057\%$ of output |
| 4 | Convex bowl centred at $(y^\ast,p^e)$. AS is the feasible set because $i$ only moves AD. Targeting rule $\phi_y(y-y^\ast)+\kappa\phi_p(p-p^e)=0$. No trade-off iff $y^\ast=y_n$. Monetary policy cannot move $y_n$ | welfare weights: $1/(1+\theta\kappa)=9.9\%$ into prices; $y^o=-2.05$, $p^o=+0.26$, $i^o=5.84\%$ (vs $r_n=6.55\%$) |

## Traps this list is built to catch

1. **Shifting AD after a *temporary* mark-up shock** (2a). Only AS moves; demand falls *along* AD.
2. **One "output gap"** (2a, 3). Prices respond to $y-y_n$; welfare responds to $y-y_e$.
3. **IS–LM reasoning in 2b** (money supply, liquidity effect). The instrument is $i$; the channel
   is the real rate.
4. **Blaming stickiness for $y_n\neq y_e$** (3). $\alpha$ appears in neither; the wedge is
   market power and taxes.
5. **AD as the constraint in Q4.** AD contains the instrument, so it restricts nothing.
6. **Calling Benigno's AS a NK Phillips curve** (Q1). It is the New-Classical form in the price
   level (fn. 7, p. 508); Calvo is out of scope.

## What the project did for this list

- Solution PDF, 14 pages, three figures, every number printed by the figure script.
- Published (private) copies: [Two Shocks](https://claude.ai/artifact/Hf8KsQYWvTwd6BnyFXP7MZ) ·
  [The Wedge](https://claude.ai/artifact/KUhe4SoMSCrZb5z7afiJ9U) ·
  [The Loss Bowl](https://claude.ai/artifact/5LYyfukdcNiBd3cHXvWH63).
- Three new companions in `benigno/`, each verified against Python at three control vectors.
  "The Three Lines" (`companion-as-ad.html`) still covers the general AS–AD–IT picture.
- No new derivation notes were needed: notes 02, 03, 04, 06 and 10 already had every step.
- NotebookLM: four audio prompts, one thesis per question, `NotebookLM/audio/lista-07-audio-{1..4}-*.md`
  (Lista 7 PDF added to `NotebookLM/sources/`).
- Narration: `Leituras/lista-07-benigno-narrated.txt`, 11,136 words, about 74 minutes at 150 wpm.
- Quiz in three parts, 10 questions each, Hard: `Simulados/quiz-lista-07-part-{1-foundations,2-shocks,3-optimal-policy}-2026-09-25.md`.
