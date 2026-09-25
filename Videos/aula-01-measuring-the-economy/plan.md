---
tags: [video, aula-01, explainer, plan]
date: 2026-09-17
slug: aula-01-measuring-the-economy
---

# Plan — Aula 1: Measuring the Economy

**Scoping answers (2026-09-17).** Purpose = *first exposure*. Length = **50 minutes**, dense
in derivations, nothing skipped. Math = **textbook derivation** (every line on screen, one
step per line). Examples = calibrated numerical case **+** the course's own exercises (number
and page only) **+** Brazilian data.

House rule deliberately relaxed on the user's explicit instruction: `/explainer` caps a video
at one textbook-depth derivation. This one has **five** (value added, the index covariance,
the Fisher factor-reversal test, Balassa–Samuelson, the Jones–Klenow λ). A 50-minute
first-exposure lecture video is a chain of derivations by construction.

Source of every line: Kurlat (2020) chs. **1–2**, printed pp. 15–44 (offset 0, printed = PDF),
already derived in full at [[Map/aula-01-mensuracao/00-index]]. The video animates those five
notes; it does not add content beyond them.

---

## Thesis

> **Every macroeconomic number is the output of a construction, and every construction is a
> choice. Learning macro measurement is learning which choice was made, and in which direction
> it bends the answer.**

Not "national accounts". The video's job is that each of the five acts ends with a *signed*
statement — the early base gives the larger growth number, Laspeyres overstates inflation,
market rates understate poor countries, the arithmetic mean overstates growth, inequality costs
exactly half the log variance. A sign is a result; a definition is not.

## The cold open, with its clock (0:00–1:30)

On screen, one at a time, three numbers for **Brazil, the same year, the same economy**:

| The US is richer than Brazil by a factor of… | measured 2023 |
|---|---|
| …at the **market exchange rate** | **8.0×** (US\$ 82,587 against US\$ 10,378) |
| …at **PPP** | **3.9×** (US\$ 82,587 against US\$ 21,193) |
| …in **welfare-equivalent consumption** λ, computed in Act V | **≈ 8×** again (λ ≈ 0.12) |

Narration, inside 30 seconds: *"How much richer is the United States than Brazil? Eight times.
Or four times. Or eight times — for a completely different reason. Same year, same two
economies, three answers, and not one of them is a mistake."*

The arc is the video: the exchange rate says eight, PPP halves it to four by taking prices out,
and then pricing inequality and life expectancy **puts it back**. The correction is undone by a
different force, and the viewer has to watch all five acts to see how.

**Measured, not asserted.** Every figure comes from `data/registry.json` (World Bank WDI,
retrieved 2026-09-18, each indicator self-named by its own payload). λ is **computed on screen**
in Act V by `data/check_lambda.py`, not quoted from a paper: σ = 1, the leisure term set to zero
for want of a verified hours series, and ū reported at three values because it has no market
price. All four caveats are said out loud.

No definition is spoken in the first ninety seconds. The three numbers are the hook; the video
is the explanation of why they differ. Motivation criterion satisfied by a concrete
discrepancy, not by an outline.

**Status: data fetched and verified (2026-09-18).** Nine WDI series in `data/`, registry
written, λ cross-checked against a 400,000-draw Monte Carlo. Kurlat's US–Mexico Example 1.14
(p. 25) stays in Act IV as the textbook's own case — the WDI numbers reproduce its structure
(US/Mexico 6.0× at market, 3.3× at PPP against Kurlat's 6.5 and 3.5).

## Colour mapping (one role per colour, whole video)

| Colour | Role | Never |
|---|---|---|
| `BLUE` | the object being measured — the quantity, the curve, the true value | a label |
| `YELLOW` | the **live** line of a derivation; the term currently being moved | decoration |
| `GREY` | `muted` — every derivation line above the live one; background series | a result |
| `RED` | **what breaks**: double counting, the wrong base, substitution bias, the market rate | a correct object |
| `GREEN` | the repaired object: value added, the Fisher chain, the PPP rate, λ | anything provisional |

## Beat sheet

23 beats, ~3,220 s ≈ **53.7 min** of narration at 150 wpm (≈ 8,050 words). Motion `t` stays
0.6–2.0 s; the slack is `hold`. 12–20 steps per beat; derivation beats spend those steps on
lines of algebra.

### Act 0 — the discrepancy

| Beat | On screen | What moves | Narration's job | s | Anchor |
|---|---|---|---|---|---|
| `BeatOpen` | three Brazilian numbers, stacked | each number lands, then the ratio brace between the outer two | pose the discrepancy; promise the resolution; name no definitions | 90 | §1.2 p. 25 |

### Act I — the three approaches (Kurlat §1.1, pp. 15–21)

| Beat | On screen | What moves | Narration's job | s | Anchor |
|---|---|---|---|---|---|
| `BeatFirmIdentity` | derivation stack, one firm | (1.1) written line by line; `Transform` subtracting $M_j$ to reach (1.2) | revenue exhausts into costs and a residual profit — so production = income is an identity, not an estimate. Why depreciation sits on the income side of a *gross* measure | 150 | pp. 15–17 |
| `BeatTelescope` | **wrong first attempt**: fertiliser \$0.80 + lettuce \$1.00 = \$1.80 in `RED` | the \$0.80 is shown twice, then the telescoping sum collapses to $R_n$ in `GREEN` | double counting is not a slogan, it is a telescoping sum; total value added = value of final output | 140 | Ex. 1.2, p. 17 |
| `BeatExpenditure` | $Y=C+I+G+X-M$ built term by term; then Example 1.6's ledger as a real table | the $-M$ arrives *after* $C,I,G,X$, as a correction, not a subtraction of output | why imports carry a minus sign; the \$5 inventory entry that makes 17 = 17; the drawdown sign trap | 150 | Ex. 1.6, p. 19 |
| `BeatConventions` | four-row table, one cell per convention | one row revealed per step, each with its Kurlat example number | transfers ≠ $G$; government valued at cost (so its productivity growth is zero **by construction**); durables vs imputed rent; non-market work excluded | 150 | Ex. 1.7–1.11, pp. 20–22 |
| `BeatGNP` | $\mathrm{GNP}=\mathrm{GDP}+F^{out}-F^{in}$; Ireland's wedge; stock–flow table | the accumulation identity $K_{t+1}=(1-\delta)K_t+I_t$ arrives last, in `BLUE` | territory vs ownership; why the HDI uses GNI; and the one line that becomes the whole of session 2 | 110 | §1.4, p. 21 |

### Act II — real, nominal, and the index problem (Kurlat §1.2, pp. 22–25)

| Beat | On screen | What moves | Narration's job | s | Anchor |
|---|---|---|---|---|---|
| `BeatExpandia` | Expandia's 2×2 price/quantity table, real cells | both base-year computations run side by side to 70% and 55% | the same data give two different growth rates; the gap is 15 points, not noise | 150 | Ex. 1.13, p. 23 |
| `BeatCovariance` | **derivation stack**: $Q^L=\sum s_{i0}\hat q_i$, $Q^P$ reweighted, difference = covariance (2.1) | each line under the last; live line `YELLOW`, above `GREY`; the covariance boxed in `GREEN` | Kurlat states in one sentence what this beat proves: the early base wins **iff** price growth and quantity growth covary negatively — which is what a downward-sloping demand curve says | 170 | p. 24 |
| `BeatFisher` | geometric mean; bracket inequality; the factor-reversal proof $P^LQ^P=P^PQ^L=V$ | the two cross-products telescope on screen, each mismatched sum cancelling | why the *geometric* mean and not the arithmetic one; why "ideal" is earned; and the price of chaining — real components stop adding up | 150 | p. 24 |
| `BeatBias` | the ordering $P^L>P^F>P^P$; then $\ln P^L-\ln P^F\simeq\frac12\varepsilon\operatorname{Var}_s(\pi)$ | the CES demand line substituted into the covariance of the previous beat | substitution bias is a **theorem**, not a regularity; it grows with price *dispersion*, not with the average inflation rate; Boskin's 1.1 points, of which ~0.4 is this | 150 | p. 25 |
| `BeatDeflatorCPI` | deflator-vs-CPI table (real cells) beside a **Brazilian chart**: IPCA against the PIB deflator | the oil-shock arrow moves the two indices in **opposite** directions | one basket is what you produce, the other is what you buy; in an **importer** an oil spike raises the CPI and lowers the deflator - and Brazil, an **exporter**, is the mirror Kurlat names at p. 24: its deflator runs *above* its CPI in every commodity boom (2021: 13.0 against 8.3; 2010: 8.4 against 5.0). The chart shows the wedge instead of asserting it | 150 | p. 24 |

### Act III — growth arithmetic (used all course; Map note 3)

| Beat | On screen | What moves | Narration's job | s | Anchor |
|---|---|---|---|---|---|
| `BeatLogs` | $\tilde g=\ln(1+g)$, series expansion, error table | the $g^2/2$ term boxed; the error column fills row by row | the log rate is exact, the approximation is not; its error is second order; excellent at 2%, useless at hyperinflation — which is why session 7 keeps the exact Fisher equation | 140 | §3.1 |
| `BeatProducts` | $g_{XZ}=g_X+g_Z+g_Xg_Z$; per-capita 3% − 1% = **1.98%** | the cross term appears in `RED`, then shrinks as $g$ falls | products, ratios and powers in logs; the cross term is the price of discrete time; growth accounting previewed as the same identity | 130 | §3.2 |
| `BeatCAGR` | **wrong first attempt**: arithmetic mean of +50% and −50% is zero — and you have 0.75 left | AM–GM inequality written out; CAGR = −13.4% in `GREEN`; then the rule of 70 derived | growth compounds, so only the geometric mean is correct; 70 ÷ growth in per cent = doubling time; 2% is a working lifetime, 7% is a decade | 150 | §3.3–3.4 |
| `BeatLogScale` | log-scale chart, Brazil and the US, `mpl_figure()` | the slope triangle is drawn; then two **parallel** lines are highlighted | slope = growth rate; parallel lines mean a constant *ratio*, i.e. **no convergence**, however small the gap looks — trap 5, and the formal test arrives in session 3 | 120 | §3.5 |

### Act IV — comparing countries (Kurlat §1.2, pp. 25–27)

| Beat | On screen | What moves | Narration's job | s | Anchor |
|---|---|---|---|---|---|
| `BeatPPPproblem` | **wrong first attempt**: divide by 19 pesos, conclude the US is 6.5× richer, in `RED` | the market-rate arrow, then the objection written beneath it | the conversion cannot tell low output from low prices apart | 130 | Ex. 1.14, p. 25 |
| `BeatPPPconstruct` | $\sum p_i^{US}q_i^{for}$; $e^{PPP}$; $\mathcal P=0.54$; the Big Mac as the $N=1$ case | the basket is revalued good by good, at US prices | PPP is the base-year index of Act II with "base year" replaced by "base country" — Laspeyres in space, with the same ambiguity, which is why the PWT is multilateral | 130 | pp. 25–27 |
| `BeatBalassa` | **derivation stack**: $Y_T=A_TL_T$, $Y_N=A_NL_N$, $W=P_TA_T=P_NA_N$ → (4.1) → (4.2) → (4.3) | the division that produces $P_N/P_T=A_T/A_N$ is a `Transform`, not a retype | the relative price of non-tradables is a **pure technology ratio** — no preferences, no demand, no capital. Haircuts are dear in rich countries because barbers are paid factory wages. Two caveats: it is the *ratio* that matters, not poverty; and γ scales it | 170 | §4.3 |
| `BeatDenominator` | $\frac{Y}{\text{Pop}}=\frac{Y}{H}\cdot\frac{H}{E}\cdot\frac{E}{\text{Pop}}$, three factors in three cells | France–US: the per-hour gap closes, the per-person gap does not | getting the denominator wrong turns a statement about leisure into a false statement about productivity — and session 5 models exactly that choice | 110 | §4.4 |

### Act V — beyond GDP (Kurlat §2.1–2.2, pp. 31–44)

| Beat | On screen | What moves | Narration's job | s | Anchor |
|---|---|---|---|---|---|
| `BeatHDI` | the three sub-indices, each min–max rescaled; then the geometric mean, then its log | taking logs turns the product into a sum, and the complementarity is read off | why log on income alone; why geometric and not arithmetic (a zero sends the index to zero; the UN switched in 2010 for this reason); the caps are conventions; **correlation with GDP = 0.94** | 140 | pp. 31–33 |
| `BeatRawls` | the veil of ignorance; $u(c,l,a)$ (2.2.1) built term by term; Jensen's inequality drawn on a concave curve | the chord under the curve, with the gap $u(\mathbb E c)-\mathbb E u(c)$ braced | four modelling commitments, each doing work — consumption not output, $a$ multiplying everything, convex disutility of work, and σ doing double duty as risk aversion **and** inequality aversion. Kurlat's warning quoted: do not put the mathematical cart before the conceptual horse | 160 | pp. 33–35 |
| `BeatLambda` | **derivation stack**: set $u^{US}(\lambda)=u^j$, substitute lognormal $\mathbb E\ln c=\ln\mathbb E c-\frac12 s^2$, solve for $\ln\lambda$ | the four terms separate out of the single line and colour-code as they land | inequality is priced at exactly **half the log variance** — the same Jensen convexity that made the arithmetic mean lie in Act III, in a second costume. Western Europe gains 20–35%; poor countries lose. Correlation with GDP again ≈ 0.95 | 180 | §2.2, pp. 33–40 |

### Closing

| Beat | On screen | What moves | Narration's job | s |
|---|---|---|---|---|
| `BeatClose` | **the ladder**: one Brazilian economy, five numbers — market rate → PPP → per hour → consumption → λ — each step labelled with the construction that produced it | each rung re-lights in the colour of the act that built it | the thesis, said once: the number is the answer to a question, and the question is the construction | 100 |

## The wrong first attempt — one per act, by design

| Act | The plausible move | How it fails | The fix |
|---|---|---|---|
| I | sum every firm's revenue | \$1.80 for \$1 of lettuce | value added telescopes |
| II | pick a base year | 70% or 55%, both defensible | Fisher chain, bracketed |
| III | average the growth rates | +50%, −50%, "zero", and you lost a quarter | geometric mean, AM–GM |
| IV | convert at the market rate | 6.5× becomes 3.5× | PPP, and Balassa–Samuelson says why |
| V | add up what seems to matter | HDI correlates 0.94 with what it corrects | write a utility function and ask for compensation |

## Scope line — what is deliberately left out

- **Kurlat ch. 3 onward.** The rule of 70 appears here as arithmetic; the *Solow* use of it is
  session 2. Growth accounting is previewed in one line and derived in session 3.
- **No stochastic DSGE, no Bellman, no RBC, no time-series econometrics, no Calvo NKPC, no
  Kurlat ch. 8 or chs. 12–15, nothing from Ljungqvist & Sargent** — the project scope lock
  holds inside animations.
- **Chain-linking practice at the statistical agencies** (SNA revisions, BEA methodology) is
  named and dropped; it is not examinable.
- **No exercise statement is ever animated.** Exercises appear as number and page only:
  1.1–1.2 (p. 26), 1.3, 1.4–1.5 (p. 27), 2.1–2.4 (pp. 42–43), 2.10 (p. 44), 3.1–3.2 (pp. 52–53).
- The interactive versions of four of these beats **already exist** as the companion pages in
  `Map/aula-01-mensuracao/`; the video points at them and does not duplicate them.

## Closing image

**One frame: the ladder.** A single vertical scale, Brazil against the US, with five rungs —
market-rate GDP per capita, PPP GDP per capita, output per hour, consumption per head, and λ.
Each rung carries, in one word, the construction that moved it: *convert*, *reweight*,
*re-denominate*, *re-base on consumption*, *price the risk*.

Why this frame is the memorable one: it makes the thesis visible without a sentence. Five
numbers for one country, each higher or lower than the last for a reason the viewer can now
name. A student who redraws that ladder in December has the whole lecture back.

## The novelty line

The slides give the formulas; the textbook gives the examples. Neither ever **signs** the
differences. This video proves, on screen and in order, that the early base gives the larger
number, that Laspeyres exceeds Fisher exceeds Paasche, that the market rate understates poor
countries, that the arithmetic mean of growth rates always overstates, and that inequality
costs half the log variance — and it shows that the second and fifth of those are *the same
inequality of Jensen*, wearing different clothes. That connection is not in Kurlat, not in the
slides, and is the reason to watch rather than read.

## Build order and gates

1. `/lab-data` → the two Brazilian series (IPCA vs PIB deflator; GDP per capita market vs PPP),
   cached with provenance. **Blocking for `BeatOpen`, `BeatDeflatorCPI`, `BeatLogScale`.**
2. `script.md` — the narration, ~8,050 words, spoken-math register.
3. `speechify-tts --script beats.json` — measured durations, `ffprobe`, never estimated.
4. `scenes.py` — 23 scenes, kit only (`Beat`, `Stage`, `table`, `axes_panel`, `mpl_figure`).
5. `layoutcheck` → zero collisions. `beatcheck` → steps, motion share, max `t`.
6. Render all 23 at `-ql`, compile `aula-01-measuring-the-economy-480p.mp4`, **hand it over and
   stop**. The 1080p60 master is not started without a yes.
