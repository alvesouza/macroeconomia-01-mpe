---
tags: [map, benigno, adas, new-keynesian, derivacoes, aula-08, aula-09]
date: 2026-09-15
---

# Benigno (2015) — the whole article, derived

**Source.** Pierpaolo Benigno, "New-Keynesian economics: an AS–AD view", *Research in
Economics* 69 (2015), printed pages 503–524. Twelve sections, 35 numbered equations,
two tables, fourteen figures. This note set derives **every one of them**, with no step
left to the reader.

**Why it exists.** [[08_adas_microfundamentos]] and [[09_adas_politica]] state the
results and the traps; they do not derive them. The article itself skips steps on
purpose — it says so in §1: *"Readers not interested in technicalities can skip Sections
3 and 4."* In a graduate course you are exactly the reader who cannot skip them. So each
note below takes one block of the article and shows the algebra in full: the Lagrangian,
the first-order conditions, every log-linearisation, every substitution.

**What is new here relative to the article.** Benigno argues graphically. Wherever he
draws a curve shifting, these notes also solve the two-equation system in closed form,
so each figure becomes a signed and sized statement. Three examples, all derived below:
a temporary productivity gain opens a gap of exactly $-\Delta y_n/(1+\sigma\kappa)$; the
optimal response to a mark-up shock lets exactly a fraction $1/(1+\theta\kappa)$ of it
through to prices; the deleveraging multiplier of 2.75 in §10 follows from three
parameters you can check.

---

## Reading order

| # | Note | Article | What it settles |
|---|---|---|---|
| 1 | [[01-household-and-ad]] | §3, eqs. (1)–(8), pp. 505–506 | Euler equation → the AD curve. Why it slopes down for a reason that is **not** the IS-LM reason |
| 2 | [[02-firms-and-as]] | §4, §4.1, eqs. (9)–(17), pp. 506–508 | Dixit–Stiglitz demand, mark-up pricing, the natural rate, and $p-p^e=\kappa(y-y_n)$ |
| 3 | [[03-natural-and-efficient]] | §4.2–§4.4, eqs. (18)–(19), pp. 508–509 | The planner's problem, $y_n-y_e=-\mu/(\sigma^{-1}+\eta)$, classical dichotomy |
| 4 | [[04-equilibrium-geometry]] | §5, eqs. (20)–(21), Figs. 1–5, pp. 509–511 | Closed-form equilibrium, slopes, anchor points, the natural real rate $r_n$ |
| 5 | [[05-productivity-shocks]] | §6, Figs. 6–8, pp. 511–513 | The three cases — temporary, permanent, expected — each signed and sized |
| 6 | [[06-markup-shocks]] | §7, Fig. 9, pp. 513–514 | Stagflation, and the first genuine trade-off in the model |
| 7 | [[07-fiscal-multipliers]] | §8, eqs. (22)–(23), Tables 1–2, Fig. 10, pp. 514–516 | Table 1 derived line by line; Table 2 reproduced; output vs. gap vs. efficient gap |
| 8 | [[08-liquidity-trap]] | §9, Figs. 11–12, pp. 516–518 | The $\mathrm{AD}_0$ locus, why $r_n<0$ traps the economy, the expectations exit |
| 9 | [[09-deleveraging]] | §10, eqs. (24)–(32), Fig. 13, pp. 518–521 | Borrowers and savers, the Fisher channel, an **upward-sloping AD**, multipliers above one |
| 10 | [[10-optimal-policy]] | §11, eqs. (33)–(35), Fig. 14, pp. 521–522 | Second-order welfare loss, the IT line, the targeting rule |
| 11 | [[11-three-schools-and-market-clearing]] | §1–§4, §11, pp. 503–508 (fn. 7), 521–522 | **Lista 7 Q1**: what market clearing means; original Keynesian vs New Classical vs New Keynesian, each derived (IS–LM, policy ineffectiveness, NK stabilisation) and compared on the four dimensions |

Runnable check: `check_multipliers.py` in this folder reproduces Table 2 and the three
deleveraging multipliers from the Table 1 formulas. It fails loudly if any formula in
[[07-fiscal-multipliers]] or [[09-deleveraging]] is mistyped. It also checks, with sympy,
every intermediate algebra step written out in notes 1–10.

Figures: `make_figures.py` in this folder draws every `fig/fig_b*.svg` embedded in the
notes from the same closed forms, asserting each labelled number before drawing it.

## Interactive companions

Seven pages in this folder, each driving the algebra of a note from live controls. Open them
in a browser; they share `../companion.css` and need no build step and no network.

| Companion | Drives | Note |
|---|---|---|
| [The Three Lines](companion-as-ad.html) | AS, AD and the IT line together; both gaps read out separately as a shock moves | [[04-equilibrium-geometry]] · [[05-productivity-shocks]] · [[06-markup-shocks]] · [[10-optimal-policy]] |
| [The Multiplier Bench](companion-multipliers.html) | all six Table 1 multipliers as $\alpha,\sigma,\eta$ move; output against gap, side by side | [[07-fiscal-multipliers]] |
| [The Floor Under Demand](companion-zlb.html) | the $\mathrm{AD}_0$ locus, a negative $r_n$, and the $\bar p$ exit | [[08-liquidity-trap]] |
| [When Demand Slopes Up](companion-deleveraging.html) | $\varpi$ crossing zero as debt rises; the three paradoxes reverse on screen | [[09-deleveraging]] |
| [Two Shocks](companion-two-shocks.html) | Lista 7 Q2: a temporary mark-up rise (AS) and a rate cut (AD), side by side, with both gaps | [[06-markup-shocks]] · [[04-equilibrium-geometry]] |
| [The Wedge](companion-wedge.html) | Lista 7 Q3: MRS against MRT and the market wage; $y_n-y_e=-\mu/(\sigma^{-1}+\eta)$ and the lost-surplus triangle | [[03-natural-and-efficient]] |
| [The Loss Bowl](companion-loss-bowl.html) | Lista 7 Q4: iso-loss ellipses tangent to AS for free $\phi_y,\phi_p,y^\ast$; the targeting rule and the share into prices | [[10-optimal-policy]] |


---

## Notation, once

Lower-case letters are **log-deviations from the steady state**, not logs of levels. The
definitions in footnote 4 (p. 506) matter, because two of them are scaled by output and
not by their own steady state:

$$y \equiv \frac{Y-\tilde Y}{\tilde Y},\qquad c \equiv \frac{C-\tilde C}{\tilde C},\qquad
g \equiv \frac{G-\tilde G}{\tilde Y},\qquad s_c \equiv \frac{\tilde C}{\tilde Y}$$

so that the resource constraint $Y=C+G$ aggregates as $y=s_c c+g$ and **not** as
$y=c+g$. Everything downstream — the definition of $\sigma$, every multiplier — carries
that $s_c$.

| Symbol | Meaning | Where it enters |
|---|---|---|
| $\bar x$ | long-run (second-period) value of $x$ | everywhere |
| $\tilde\sigma$ | intertemporal elasticity of substitution in consumption | $u(C)=C^{1-\tilde\sigma^{-1}}/(1-\tilde\sigma^{-1})$ |
| $\sigma \equiv \tilde\sigma s_c$ | EIS **scaled to output** — the AD slope parameter | (6), (21) |
| $\rho \equiv -\ln\beta$ | rate of time preference | (4) |
| $\eta$ | inverse Frisch elasticity of labour supply | $v(L)=L^{1+\eta}/(1+\eta)$ |
| $\theta>1$ | elasticity of substitution across goods | (9), and the IT slope |
| $\mu_\theta \equiv \theta/(\theta-1)-1$ | pure monopoly mark-up | (13) |
| $\mu$ | **aggregate** mark-up: monopoly power and taxes together | (13) |
| $\alpha\in(0,1)$ | fraction of firms with pre-set prices $P^e$ | §4 |
| $\kappa \equiv (1-\alpha)(\sigma^{-1}+\eta)/\alpha$ | AS slope | (17) |
| $y_n$, $y_e$ | natural and efficient output | (15), (19) |
| $\tau_c,\tau_l,\tau_w,\tau_y$ | taxes on consumption, labour income, labour cost, sales | (13), (18) |

**The one-line summary of the whole model.** Two equations,

$$\underbrace{y = \bar y_n + (g-\bar g) - \sigma\left[i-(\bar p - p)-(\bar\tau_c-\tau_c)-\rho\right]}_{\text{AD, from the Euler equation}}
\qquad
\underbrace{p - p^e = \kappa\,(y-y_n)}_{\text{AS, from mark-up pricing under sticky prices}}$$

in two unknowns $(p,y)$, plus a third line, $(y-y_e)+\theta(p-p^e)=0$, that says what
the central bank should want. Sections 6 through 10 are comparative statics on those
three lines and nothing else.

## Where the article is wrong, or the transcription is

Two flags, both resolved in the notes rather than hidden:

1. **Eq. (15) and (19), the coefficient on $g$.** The project markdown of the article
   renders it as $(\sigma^{-1}-1)/(\sigma^{-1}+\eta)$ — an OCR artefact of
   $\sigma^{-1}$. The correct coefficient is $\sigma^{-1}/(\sigma^{-1}+\eta)$; three
   independent confirmations are in [[02-firms-and-as]] and [[07-fiscal-multipliers]].
2. **The gap against the efficient level, p. 515.** The prose claims that equation has
   "the same short- and long-run public-spending multipliers as Eq. (22)". It cannot:
   spending moves $y_e$, so the coefficient is $m_{\bar g}$, not $m_g$. Derived in
   [[07-fiscal-multipliers]].

## Out of scope, deliberately

The article's footnote 7 (p. 508) rules out the forward-looking Calvo Phillips curve as
beyond its pedagogical scope, and the course follows it. Nothing in these notes uses
$\pi_t=\kappa x_t+\beta E_t\pi_{t+1}$, dynamic programming, or stochastic DSGE. The AS
equation here is a **New-Classical** Phillips curve in the price *level*, and the model
has exactly two periods.
