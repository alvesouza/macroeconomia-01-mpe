---
tags: [map, aula-04, consumo, poupanca, euler, renda-permanente, derivacoes]
date: 2026-09-18
---

# Aula 4 — Consumption and saving, microfounded

**Source.** Kurlat (2020), chapter **6**, printed pages 103–126. Complementary: Romer (2012)
ch. 8 for the formal permanent-income and random-walk results; Williamson chs. 4 and 9 for the
two-period diagram worked at length.

**Why this directory exists.** Sessions 2 and 3 ran on Assumption 4.7: households save a fixed
fraction $s$ of income, because someone said so. Every comparative static in those sessions is
therefore conditional on a behavioural rule with no justification. This session replaces the
rule with a decision, and the first thing that happens is that $s$ stops being a number and
becomes a *function* — of the interest rate, of impatience, of the whole expected path of
income, and of whether the household can borrow.

The single result to carry out of this session: **consumption responds to wealth, not to
current income.** Everything else is a corollary or an exception to it.

---

## Reading order

| # | Note | Kurlat | What it settles |
|---|---|---|---|
| 1 | [[01-keynesian-and-the-problem]] | §6.1, pp. 103–105 | The Keynesian consumption function, the three facts that break it, and what a microfoundation has to deliver |
| 2 | [[02-two-period-problem]] | §6.2, pp. 105–112 | The intertemporal budget constraint; the Euler equation derived three ways; closed forms for log and CRRA; the geometry |
| 3 | [[03-income-and-substitution]] | §6.2, pp. 112–115 | Why a higher interest rate has an ambiguous effect on saving, decomposed exactly; why log is the knife-edge; savers against borrowers |
| 4 | [[04-permanent-income]] | §6.2–§6.3, pp. 115–120 | Transitory against permanent income; the marginal propensity to consume derived; the infinite-horizon annuity formula; the random walk |
| 5 | [[05-ricardian-and-constraints]] | §6.2–§6.4, pp. 120–126 | Ricardian equivalence with all five assumptions named; credit constraints and the return of current income; precautionary saving; the behavioural alternatives |

Runnable check: `check_consumption.py`. It solves the two-period problem numerically and
against the closed forms, verifies the Euler equation holds at the optimum and fails off it,
decomposes the interest-rate effect into income and substitution terms by compensated
demand, reproduces the transitory-against-permanent MPC contrast, confirms Ricardian
equivalence numerically and then breaks it by imposing a borrowing limit, and checks that the
constrained Euler holds as an inequality.

## Interactive companions

| Companion | Drives | Note |
|---|---|---|
| [Two Periods, One Line](companion-euler.html) | the budget line rotating about the endowment as $r$ moves, with indifference curves, the Euler condition and the saver/borrower switch | [[02-two-period-problem]] · [[03-income-and-substitution]] |
| [Wealth, Not Income](companion-pih.html) | transitory against permanent shocks, the MPC out of each, the horizon effect, and a borrowing limit that switches the household back to hand-to-mouth | [[04-permanent-income]] · [[05-ricardian-and-constraints]] |
| [Taxes, Timing and the Limit](companion-taxes-and-limits.html) | Lista 3 on one page: the Ricardian swap (neutral, then broken by a binding $a\ge-b$), a tax on the return to saving against an equal-revenue lump sum, and the sign of $\partial c_1/\partial r$ against $\sigma$ | [[05-ricardian-and-constraints]] · [[03-income-and-substitution]] |

---

## Notation, once

| Symbol | Meaning | Note |
|---|---|---|
| $c_1,c_2$ | consumption in the two periods | choice variables |
| $y_1,y_2$ | income, taken as given | endowment |
| $a$ | assets carried from period 1 to 2 | $a<0$ is borrowing |
| $r$ | real interest rate | the relative price of $c_1$ in terms of $c_2$ |
| $\beta=\dfrac{1}{1+\rho}$ | discount **factor**; $\rho$ is the discount **rate** | trap 2 in [[04_consumo_poupanca]] |
| $W = y_1+\dfrac{y_2}{1+r}$ | lifetime wealth | the only thing consumption depends on |
| $\sigma$ | coefficient of relative risk aversion | CRRA curvature |
| $1/\sigma$ | **elasticity of intertemporal substitution** | trap 4: these are reciprocals, not synonyms |

**The three objects that must not be confused**, and that this directory keeps apart
throughout: the discount factor $\beta$ against the discount rate $\rho$; risk aversion
$\sigma$ against the EIS $1/\sigma$; and the *level* of income against its *present value*.

## Where this session feeds

- $s$ as a function of $r$ is exactly what [[06_equilibrio_geral]] needs to close the model:
  once households choose saving and firms choose capital, the interest rate is determined in
  equilibrium instead of being read off the production function.
- The Euler equation derived here is, verbatim, equation (3) of Benigno (2015) and therefore
  the aggregate demand curve of [[08_adas_microfundamentos]]. The New-Keynesian AD curve *is*
  the object built in [[02-two-period-problem]] §2.3.
- Ricardian equivalence is assumed throughout Benigno §3–§9 and broken in §10; the assumptions
  that do the work are listed in [[05-ricardian-and-constraints]] §5.2 and the one that fails
  in the deleveraging model is named there.

## Out of scope

Kurlat ch. 8 (investment and present values) is outside this course, so the asset-pricing
extensions are not developed. Stochastic dynamic programming, Bellman equations and the full
Hall random-walk econometrics are out; the random-walk result appears in
[[04-permanent-income]] §4.5 as a stated consequence with its intuition, not as a derivation.
