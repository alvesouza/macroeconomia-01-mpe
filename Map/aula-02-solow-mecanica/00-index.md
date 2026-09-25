---
tags: [map, aula-02, solow, crescimento, derivacoes, kurlat]
date: 2026-09-18
---

# Aula 2 — Growth facts and the mechanics of Solow, derived

**Source.** Kurlat (2020), chapter **3** and sections **4.1–4.2**, printed pages 47–61.
Complementary: Jones (2020) chs. 3–5 for data and intuition; Romer (2012) ch. 1 for the
continuous-time treatment and the formal stability argument.

**Why this directory exists.** [[02_crescimento_solow]] states the model and its traps. It
does not derive the fundamental equation from the accumulation identity, does not prove that
the steady state is unique and globally stable, and does not show *where* the Inada
conditions are actually used. Those three gaps are the content of this directory, because
they are exactly what separates "I can draw the Solow diagram" from "I can be asked anything
about it".

---

## Reading order

| # | Note | Kurlat | What it settles |
|---|---|---|---|
| 1 | [[01-growth-facts]] | ch. 3, pp. 47–51 | The four Kaldor facts with the US numbers; why fact 4 is implied by facts 2 and 3; the cross-country dispersion the model must explain |
| 2 | [[02-ingredients]] | §4.1, pp. 53–57 | Assumptions 4.1–4.8, each with the job it does. Why CRS is what makes per-worker form legal, and what Inada buys that diminishing returns does not |
| 3 | [[03-fundamental-equation]] | §4.2, pp. 57–59 | Equation (4.2.2) derived line by line from (4.1.4); the exact discrete law against the textbook approximation; the continuous-time version reconciled with Romer |
| 4 | [[04-steady-state-and-stability]] | §4.2, pp. 59–61 | $k_{ss}$ in closed form; existence and uniqueness from Inada; global stability proved, not asserted |
| 5 | [[05-comparative-statics]] | §4.2, pp. 59–61 | Level against rate, the exam's most expensive confusion, with the transition path computed |

Runnable check: `check_solow.py`. It verifies the closed-form steady state against a
simulated path, checks that the exact and approximate laws of motion agree to first order
and quantifies where they part, confirms global stability from a grid of initial conditions,
and reproduces the US Kaldor magnitudes from the model's own restrictions.

## Interactive companions

| Companion | Drives | Note |
|---|---|---|
| [The Solow Diagram](companion-solow.html) | $sf(k)$ against $(n+\delta)k$, the steady state moving as the parameters move, with the exact discrete path overlaid | [[03-fundamental-equation]] · [[04-steady-state-and-stability]] |
| [Level, Not Rate](companion-transition.html) | a permanent rise in $s$: growth spikes, then dies; the level is permanently higher and the long-run growth rate is unchanged | [[05-comparative-statics]] |

---

## Notation, once

Kurlat writes the steady state $k_{ss}$; most other sources write $k^*$. They are the same
object and this directory uses $k_{ss}$ to stay with the book.

| Symbol | Meaning | First appears |
|---|---|---|
| $K_t,\;L_t,\;Y_t$ | aggregate capital, labour, output | (4.1.1) |
| $k\equiv K/L$, $y\equiv Y/L$ | per worker — and in this chapter per capita too, since everybody works | (4.2.1) |
| $f(k)\equiv F(k,1)$ | the per-worker production function | (4.2.1) |
| $s$ | saving rate, **exogenous and constant** | Assumption 4.7 |
| $\delta$ | depreciation rate | Assumption 4.8 |
| $n$ | population growth rate | Assumption 4.5 |
| $\alpha$ | capital share in Cobb–Douglas; shown in [[02-ingredients]] to *be* the capital income share | (4.1.2) |

**The one-line summary of the whole session.** Capital per worker obeys

$$\Delta k_{t+1} \;=\; \underbrace{s f(k_t)}_{\text{actual investment}} \;-\; \underbrace{(\delta+n)k_t}_{\text{break-even investment}}$$

and because $f$ is concave with $f'(0)=\infty$ and $f'(\infty)=0$, that difference is
positive for small $k$, negative for large $k$, and zero at exactly one point. Everything
else in sessions 2 and 3 is a consequence of those two sentences.

## What this session cannot do, and says so

The basic Solow model has **no long-run growth in output per worker**. At $k_{ss}$ both $k$
and $y$ are constant, so a model built to explain Kaldor fact 1 — constant positive growth of
GDP per capita — fails at it. That failure is deliberate and it is the entire motivation for
[[03_solow_evidencias]], where labour-augmenting technical progress is introduced precisely
to repair it. Saying "saving more raises the growth rate" is not a small slip here; it is a
claim the model explicitly denies.

Also out of scope in this session: the Golden Rule, factor markets and the $\alpha$
interpretation as an equilibrium result, technological progress, growth accounting and the
convergence-speed regression. All of those are session 3.
