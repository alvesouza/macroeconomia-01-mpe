---
tags: [map, aula-01, mensuracao, derivacoes, kurlat]
date: 2026-09-17
---

# Aula 1 — Measuring the macroeconomic aggregates, derived

**Source.** Kurlat (2020), chapters **1** and **2**, printed pages 15–44. Complementary:
Jones (2020) ch. 2; Romer (2012) ch. 1 for the growth arithmetic; Jones & Klenow (2016),
which Kurlat §2.2 reproduces.

**Why this directory exists.** [[01_mensuracao_agregados]] states the results — the three
approaches, the index formulas, the PPP correction, the HDI. It does not derive them, and
three of them have real content underneath: why Laspeyres and Paasche bracket the truth,
why non-tradables are systematically cheap in poor countries, and why a welfare measure
that respects risk aversion penalises inequality by exactly half the log variance. Those
derivations are here, in full.

---

## Reading order

| # | Note | Kurlat | What it settles |
|---|---|---|---|
| 1 | [[01-three-approaches]] | §1.1, pp. 15–21 | Why production = income = expenditure is a theorem about value added, not a convention. Depreciation, imputation, transfers, inventories |
| 2 | [[02-real-nominal-and-indices]] | §1.2, pp. 22–25 | Laspeyres, Paasche, Fisher and the chain. The substitution-bias inequality proved, not asserted |
| 3 | [[03-growth-arithmetic]] | used throughout | The log approximation with its error term; CAGR; the rule of 70; why a log scale reads slopes as rates |
| 4 | [[04-cross-country-and-ppp]] | §1.2, pp. 25–27 | The PPP exchange rate defined; Balassa–Samuelson derived from a two-sector model |
| 5 | [[05-beyond-gdp]] | §2.1–§2.2, pp. 31–44 | HDI algebra and its arbitrariness; the Jones–Klenow λ decomposed into four additive terms |

Runnable check: `check_measurement.py` in this folder. It rebuilds Kurlat's Expandia
example both ways, verifies the Fisher chain sits between them, proves the Laspeyres ≥
Paasche ordering numerically on random data, and reproduces the λ decomposition against a
brute-force expected-utility calculation.

## Interactive companions

Four pages in this folder. They share `../companion.css`, need no build step and no network.

| Companion | Drives | Note |
|---|---|---|
| [The Index Bench](companion-indices.html) | Laspeyres, Paasche and Fisher separating as the covariance changes sign | [[02-real-nominal-and-indices]] |
| [Reading a Log Scale](companion-growth.html) | the same two economies on linear and log axes; doubling times; the AM–GM shortfall | [[03-growth-arithmetic]] |
| [Two Countries, Two Baskets](companion-ppp.html) | Balassa–Samuelson: the price level as $(A_T/A_N)^{\gamma}$, and the PPP uplift it implies | [[04-cross-country-and-ppp]] |
| [What Rawls Would Pay](companion-welfare.html) | $\ln\lambda$ as a waterfall of its four terms, with $\sigma$ scaling the inequality penalty | [[05-beyond-gdp]] |

---

## Notation, once

| Symbol | Meaning |
|---|---|
| $p_{it}$, $q_{it}$ | price and quantity of good $i$ in year $t$; year $0$ is the base |
| $Y_t^{\text{nom}}=\sum_i p_{it}q_{it}$ | nominal GDP |
| $Y_t^{(0)}=\sum_i p_{i0}q_{it}$ | real GDP at base-year prices (Kurlat eq. 1.2.1) |
| $g^{I}_t,\;g^{F}_t$ | growth at initial-year and final-year prices |
| $\lambda$ | Jones–Klenow equivalent variation: the factor by which US consumption must be scaled to match country $i$ |
| $\sigma$ | coefficient of relative risk aversion; also governs the inequality penalty |

**One caution that propagates through the whole course.** Kurlat's lower-case growth
rates are *net* rates ($Y_{t}=Y_{t-1}(1+g)$), while from [[04_consumo_poupanca]] onward
lower-case letters become log-deviations. They agree to first order and differ at second
order; [[03-growth-arithmetic]] gives the size of the disagreement.

## What this session is really about

Every later session measures something. The Solow model of [[02_crescimento_solow]] is a
statement about $Y/L$; the consumption theory of [[04_consumo_poupanca]] is a statement
about $C$; the inflation of [[07_moeda_inflacao]] is a statement about a price index built
exactly as in [[02-real-nominal-and-indices]]. If the index is a Laspeyres, the inflation
rate carries substitution bias, and the real interest rate computed from it inherits the
bias with the opposite sign. That link is made explicit in [[07_moeda_inflacao]].

## Out of scope, deliberately

Kurlat ch. 8 (investment) and chs. 12–15 are outside this course. National-accounts
institutional detail beyond what the exercises need (SNA revisions, chain-linking
practice at the BEA) is not examinable. No exercise statement is reproduced anywhere in
this directory — exercises are cited by number and page only.
