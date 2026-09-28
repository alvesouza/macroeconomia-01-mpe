---
tags: [map, aula-03, solow, regra-de-ouro, ptf, contabilidade-do-crescimento, derivacoes]
date: 2026-09-18
---

# Aula 3 — Golden Rule, technology, and what the Solow model cannot explain

**Source.** Kurlat (2020), sections **4.3–4.5** and chapter **5**, printed pages 61–100.
Complementary: Jones (2020) chs. 4–6 for development accounting and the data; Romer (2012)
ch. 1 for the formal convergence-speed log-linearisation, which Kurlat does by Taylor
approximation instead.

**Why this directory exists.** Session 2 built a model that fails its own first target: it
predicts zero long-run growth in output per worker. This session repairs that, and then
turns the repaired model on the data and watches it fail a second time — this time
irreparably, which is the honest result and the one worth understanding. Kurlat's chapter 5
is an unusually direct piece of model-testing for a textbook, and the notes here keep every
number he uses.

---

## Reading order

| # | Note | Kurlat | What it settles |
|---|---|---|---|
| 1 | [[01-golden-rule]] | §4.3, pp. 61–63 | $f'(k_{gold})=\delta+n$ derived; $s_{gold}=\alpha$; why being *below* the Golden Rule is not inefficient and being above it is |
| 2 | [[02-markets-and-factor-prices]] | §4.4, pp. 63–69 | The decentralised economy: $w$, $r^K$, $r=r^K-\delta$; zero profit from CRS; $\alpha$ as an equilibrium object rather than a label |
| 3 | [[03-technological-progress]] | §4.5, pp. 69–72 | Assumption 4.9 and efficiency units; the balanced growth path; why technology must be **labour-augmenting**, with the Uzawa argument |
| 4 | [[04-quantifying-and-convergence]] | §5.1–§5.3, pp. 75–86 | Kurlat's calibration; Conjecture 5.1 stated and rejected three ways; eq. (5.3.4) and the Lucas paradox; the convergence speed derived properly |
| 5 | [[05-growth-accounting-and-tfp]] | §5.4–§5.5, pp. 86–95 | The Solow residual as a *definition*; growth accounting against development accounting; human capital; where TFP differences come from |

Runnable check: `check_growth.py`. It verifies the Golden Rule in closed form and by
numerical maximisation, confirms that factor payments exhaust output, reproduces Kurlat's
Mexico–US rental-rate ratio of 9.4 and his \$10,000-against-\$1,000 prediction failure,
derives the convergence half-life two independent ways, and decomposes a synthetic
cross-country panel into capital and TFP contributions.

## Interactive companions

| Companion | Drives | Note |
|---|---|---|
| [The Golden Rule](companion-golden-rule.html) | $c_{ss}(s)$ as a hump; the dynamically inefficient region shaded; the consumption path of a move to $s_{gold}$ from either side | [[01-golden-rule]] |
| [Whose Fault Is the Gap?](companion-development.html) | a country's income ratio split into capital and TFP, with the implied rental rate and the Lucas-paradox magnitude | [[04-quantifying-and-convergence]] · [[05-growth-accounting-and-tfp]] |
| [Security Capital Looks Like Bad Luck](companion-hidden-wedge.html) | Lista 2 Q2 (Gotham): $\hat A/A=(1+\theta)^{-\alpha}$ against $\theta$; a fall in $\theta$ reported as TFP growth $\alpha\ln[(1+\theta)/(1+\theta')]/T$ while $g_K$, $g_L$ drop out | [[05-growth-accounting-and-tfp]] |

---

## Notation, once

The single most common error in this session is mixing the two rescalings. Keep them apart:

| Symbol | Definition | Grows at, on a BGP |
|---|---|---|
| $k = K/L$ | capital per **worker** | $g$ |
| $\tilde k = K/(AL)$ | capital per **efficiency unit** | $0$ |
| $y = Y/L$ | output per worker | $g$ |
| $\tilde y = Y/(AL)$ | output per efficiency unit | $0$ |
| $K$, $Y$, $C$ | aggregates | $n+g$ |
| $L$ | labour | $n$ |
| $K/Y$, factor shares, $r$ | ratios | $0$ |

Kurlat writes $\tilde L \equiv AL$ for efficiency units of labour and derives everything in
those units. Trap 3 and trap 4 in [[03_solow_evidencias]] are both about this table.

**Kurlat's calibration (§5.2, p. 77)**, used throughout this directory and in the companions:

$$\alpha = 0.35,\qquad g = 0.015,\qquad n = 0.01,\qquad \delta = 0.04,\qquad s = 0.20$$

with $\alpha$ read off the 0.65 labour share, $g$ off the 1.5% US growth rate since 1800,
$n$ off US population growth since 1950, $\delta$ from BEA estimates (0.02 buildings, 0.15
equipment, 0.30 computers, blended to 0.04), and $s$ matched to the recent US **investment**
rate — Kurlat notes the US saving rate is a little lower, because the economy is not closed
and runs a trade deficit.

## The two results this session exists to deliver

1. **Long-run growth in output per worker equals $g$, and $g$ is exogenous.** The Solow model
   explains capital accumulation and then *assumes* the thing it was built to explain. Kurlat
   is candid about this: Assumption 4.9 is "rather disappointing" and the questions of why
   technology advances and what sets its pace are left aside.
2. **Capital cannot explain cross-country income differences.** Conjecture 5.1 — same
   technology everywhere, differences are capital — is rejected by convergence patterns, by
   the level of predicted output, and by implied rates of return. What is left is TFP, and TFP
   is a residual, not an explanation.

Out of scope here: endogenous growth (Kurlat chs. 12–15 are outside the course), and
anything requiring an optimising saver — the Golden Rule of [[01-golden-rule]] deliberately
stops where preferences would be needed, which is exactly where [[04_consumo_poupanca]]
picks up.
