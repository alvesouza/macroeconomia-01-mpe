---
tags: [map, aula-05, trabalho, lazer, oferta-de-trabalho, busca, derivacoes]
date: 2026-09-18
---

# Aula 5 — Labour and leisure, derived

**Source.** Kurlat (2020), chapter **7**, printed pages 127–150. Complementary: Jones (2020)
ch. 7 for the long-run participation facts; Romer (2012) ch. 11 for the search-and-matching
treatment and the formal elasticity definitions.

**Why this directory exists.** Sessions 2 and 3 assumed everybody works and the labour force
equals the population (Assumption 4.5 in [[02-ingredients]]). Session 4 microfounded the saving
decision and left labour alone. This session microfounds the other half: how much people work,
whether they work at all, and why the answer to "does a higher wage raise hours?" is *it
depends*, with a precise statement of what it depends on.

There are two separate questions here and the chapter answers both, which is why the notes
split the way they do. The **intensive** margin — hours per worker — is a consumption–leisure
choice. The **extensive** margin — who works at all — is a participation decision with a corner
solution, and the fact that most cyclical variation in hours happens on the extensive margin is
what makes the static model insufficient on its own.

---

## Reading order

| # | Note | Kurlat | What it settles |
|---|---|---|---|
| 1 | [[01-measurement]] | §7.1, pp. 127–131 | The three stocks and the flows between them; why the unemployment rate can fall in a recession; the Beveridge curve; which margin carries the cycle |
| 2 | [[02-static-model]] | §7.2, pp. 131–137 | The full-income constraint; MRS $=w$; income against substitution on hours; why log-log preferences are forced by balanced growth; the reservation wage |
| 3 | [[03-elasticities-and-evidence]] | §7.3, pp. 137–140 | Marshallian, Hicksian and Frisch elasticities defined and ordered; the micro evidence; Prescott's Europe–US calculation and the elasticity it implies |
| 4 | [[04-dynamic-labour-supply]] | §7.4, pp. 140–142 | Intertemporal substitution of labour; transitory against permanent wage changes; why this is the mechanism real-business-cycle models need, and why it is contested |
| 5 | [[05-search-and-equilibrium]] | §7.5, pp. 142–150 | Unemployment as a flow equilibrium; $u^*=\lambda/(\lambda+f)$ derived; the matching function; reservation wages in search; what unemployment insurance does |

Runnable check: `check_labour.py`. It verifies the static first-order condition against
numerical optimisation, confirms that log-log preferences make hours independent of the wage
and that no other CRRA pair does, computes all three elasticities and checks the Slutsky
ordering, reproduces the steady-state unemployment formula against a simulated flow model,
and reproduces Prescott's implied elasticity.

Figures: `make_figures.py` writes every `fig/*.svg` embedded in the notes and asserts each
labelled number before drawing it.

## Interactive companions

| Companion | Drives | Note |
|---|---|---|
| [The Backward Bend](companion-labour-supply.html) | the labour supply curve bending back as non-wage income and preferences move, with the reservation wage marking where participation stops | [[02-static-model]] · [[03-elasticities-and-evidence]] |
| [Unemployment Is a Flow](companion-flows.html) | $u^*=\lambda/(\lambda+f)$ as a stock settling between two flows, with the Beveridge curve traced out as matching efficiency moves | [[05-search-and-equilibrium]] |

---

## Notation, once

| Symbol | Meaning |
|---|---|
| $\bar h$ | time endowment; $\bar h=\ell+h$ splits it into leisure and work |
| $\ell$, $h$ | leisure, hours worked |
| $w$ | real wage — and, crucially, **the price of leisure** |
| $\pi$ | non-wage income (transfers, spousal income, asset income) |
| $E$, $U$, $N$ | employed, unemployed, out of the labour force |
| $L=E+U$ | labour force |
| $\lambda$ | separation rate (job destruction) |
| $f$ | job-finding rate |
| $\eta$ | inverse Frisch elasticity — the same $\eta$ as in [[08_adas_microfundamentos]] |

**The one-line summary.** The household's intratemporal condition

$$\frac{u_\ell(c,\ell)}{u_c(c,\ell)} = w$$

says the marginal rate of substitution between leisure and consumption equals the real wage.
That single equation is the labour supply curve, the object that makes the AS curve slope up in
[[02-firms-and-as]], and the equation that Benigno divides by the firm's mark-up condition to
eliminate the real wage. It is the most reused first-order condition in the course after the
Euler equation.

## Where this session feeds

- The **AS curve** of [[08_adas_microfundamentos]] is built by combining this condition with
  mark-up pricing. The parameter $\eta$ there is the inverse Frisch elasticity defined in
  [[03-elasticities-and-evidence]] §3.2, and the dispute over its value recorded there is
  exactly the dispute that makes $\kappa$ uncertain in session 8.
- The **general equilibrium** of [[06_equilibrio_geral]] needs labour supply and labour demand
  to clear a market; this session supplies the first.
- The three-factor decomposition of output per person in
  [[04-cross-country-and-ppp]] §4.4 — output per hour, hours per worker, employment rate — is
  finally given a model here, and the France–US comparison becomes answerable.

## Out of scope

Human capital and schooling decisions (that is the Mincer material of
[[05-growth-accounting-and-tfp]] §5.4, used there as measurement rather than as a choice);
wage bargaining and union models; the full Diamond–Mortensen–Pissarides equilibrium with
free-entry vacancy creation, of which [[05-search-and-equilibrium]] carries only the flow
accounting and the matching function.
