---
tags: [video, aula-04, explainer, plan]
date: 2026-09-22
slug: aula-04-consumption
---

# Plan — Aula 4: Consumption and Saving, Microfounded

Scoping carried from the set: *first exposure*, ~50 min, **textbook derivation**, calibrated
case + course exercises (number and page only) + Brazilian data. English.

Source: Kurlat (2020) ch. **6**, printed pp. 103–126. Derivation layer complete at
[[Map/aula-04-consumo/00-index]] (5 notes + `check_consumption.py`).

---

## Thesis

> **Consumption responds to wealth, not to current income — and every apparent exception is
> the model telling you which household you are looking at.**

Sessions 2 and 3 ran on Assumption 4.7: households save a fixed fraction $s$ because somebody
said so. This session replaces the rule with a decision, and $s$ stops being a number and
becomes a function — of the interest rate, of impatience, of the whole expected income path,
and of whether the household can borrow at all.

## Cold open (0:00–1:30)

The same household, the same preferences, two windfalls.

| A windfall of R\$ 1,000… | consumed now |
|---|---|
| …that arrives once and never again | **51%** |
| …that arrives every year from now on | **100%** |

*"One household. One utility function. Two marginal propensities to consume, differing by a
factor of two. No consumption function of current income can produce that — it has one MPC by
construction."*

Then the twist that sets up Act V: for a household that **cannot borrow**, both numbers become
100%, and the old Keynesian function is exactly right again.

Computed in `data/check_consumption.py` (copied from `Map/aula-04-consumo/`, which already
verifies every closed form in this lecture).

## Beat sheet — 26 beats

### Act 0
| Beat | Job | s |
|---|---|---|
| `BeatOpen` | the two MPCs; the promise that one model delivers both, and says when the old one is right | 90 |

### Act I — what has to be replaced (§6.1, pp. 103–105)
| Beat | Job | s |
|---|---|---|
| `BeatKeynes` | $C=\bar C+\text{mpc}\cdot Y$; the two "psychological law" properties; that it is a **rule**, with the same status as Assumption 4.7 | 110 |
| `BeatKuznets` | the puzzle: the function fits the cross-section and fails the long-run time series. Kuznets' constant saving rate over decades of rising income | 130 |
| `BeatThreeFacts` | consumption is smoother than income; announcements move consumption **before** cash arrives. Neither is possible in a function of current income | 130 |
| `BeatMethod` | why microfoundations: comparative statics become meaningful, welfare becomes computable, and parameters survive policy changes (Lucas) | 110 |

### Act II — the two-period problem (§6.2, pp. 105–112)
| Beat | Job | s |
|---|---|---|
| `BeatPreferences` | $u(c_1)+\beta u(c_2)$; what separability, concavity and geometric discounting each buy — and $\beta$ is a **factor**, $\rho$ a **rate** | 130 |
| `BeatBudget` | **derivation**: two period constraints → the intertemporal constraint. Three readings: $1/(1+r)$ is a price; $W$ is all that matters; the endowment is **always** on the line | 140 |
| `BeatEuler` | **derivation, three routes**: substitution, Lagrangian, and the perturbation argument — eat one unit less today, invest it, and at an optimum the trade is a wash | 160 |
| `BeatSmoothing` | $\beta(1+r)=1 \iff r=\rho \Rightarrow c_1=c_2$: perfect smoothing regardless of how uneven income is. Above and below, the path tilts | 120 |
| `BeatClosedForms` | **derivation**: log gives $c_1=W/(1+\beta)$ — $r$ enters *only* through $W$. Then CRRA, and check it nests log | 150 |
| `BeatEIS` | why $1/\sigma$ is the elasticity of intertemporal substitution and $\sigma$ is risk aversion — **reciprocals by construction**, which is a CRRA artefact, not a law | 120 |

### Act III — the interest rate (§6.2, pp. 112–115)
| Beat | Job | s |
|---|---|---|
| `BeatPivot` | the line pivots **about the endowment**, so a lender gets richer and a borrower poorer. The geometry does the work before any algebra | 130 |
| `BeatDecomposition` | **derivation**: $d\ln c_1/d\ln(1+r) = -\omega - \theta(1/\sigma - 1)$, with $\omega$ the share of wealth that is future income | 160 |
| `BeatThreeCases` | $\sigma=1$ knife-edge (allocation unaffected); $\sigma<1$ saving rises; $\sigma>1$ saving **falls**. "Higher rates encourage saving" is simply not a theorem | 130 |
| `BeatPolicyCorollary` | a savings tax break helps most the households least likely to use it, is ambiguous for those who do, and is funded by public dissaving — so national saving can fall | 120 |

### Act IV — permanent income (§6.2–6.3, pp. 115–120)
| Beat | Job | s |
|---|---|---|
| `BeatTwoMPCs` | **derivation**: transitory $\Delta W=\Delta$ vs permanent $\Delta W = \Delta(2+r)/(1+r)$; the 0.51 and 1.00; and the check that the permanent MPC is exactly 1 when $r=\rho$ | 150 |
| `BeatHorizon` | why the transitory MPC is not tiny here: the lifetime **is** two periods. Generalise to $T$ and the MPC scales like $1/T$ | 120 |
| `BeatKuznetsResolved` | the cross-section is a composition effect — high-income households are disproportionately having a *good year*. Both facts, one model | 130 |
| `BeatRandomWalk` | consumption should move only on **news**; the excess-sensitivity puzzle stated as the empirical challenge, not derived | 110 |

### Act V — where it breaks (§6.2–6.4, pp. 120–126)
| Beat | Job | s |
|---|---|---|
| `BeatTaxes` | **derivation**: taxes enter only through their present value; add the government's own constraint and $T$ **vanishes**, leaving $G$ | 140 |
| `BeatRicardian` | the mechanism concretely: cut $T_1$ by $\Delta$, borrow, repay $(1+r)\Delta$ — private saving rises exactly $\Delta$, national saving unchanged. A deficit-financed tax cut is a forced loan | 150 |
| `BeatFiveAssumptions` | the five assumptions, each a way it fails. And Kurlat's warning: it says **nothing** about changing $G$ — only about the *timing of taxes* | 140 |
| `BeatConstraints` | $a\ge0$ binds → $c_1=y_1$, hand-to-mouth, and the **Euler becomes an inequality** (the Kuhn–Tucker trap). MPC jumps to 1; Ricardian equivalence fails; the Keynesian function is exactly right for these households | 160 |
| `BeatTwoTypes` | a fraction $\chi$ unconstrained, $1-\chi$ constrained; aggregate MPC $\approx \chi r/(1+r) + (1-\chi) \approx 0.33$ — right in the estimated range. This two-type structure **is** session 9's deleveraging model | 130 |
| `BeatPrecaution` | uncertainty raises saving if $u'''>0$, by Jensen on the Euler equation — the third appearance of Jensen in this course | 110 |
| `BeatClose` | the closing image; and the handover: $s(r)$ is exactly what session 6 needs to close the model, and this Euler equation **is** Benigno's equation (3) | 110 |

## The wrong first attempt

"Higher interest rates encourage saving." Stated, then decomposed, then shown to be false for
exactly the households that do most of the saving. It is trap 3 in `rules/04`.

## Scope line

- Kurlat ch. 8 (investment, present values) is outside the course — no asset-pricing extensions.
- No stochastic dynamic programming, no Bellman, no Hall random-walk econometrics: the
  random-walk result is **stated with its intuition**, never derived.
- Exercises by number and page only: 6.1 (p. 123), 6.2–6.3 (pp. 123–124), 6.4 (p. 124),
  6.5 (p. 124).

## Closing image

**The budget line with two points marked on it.** The endowment, and the optimum — with the
horizontal gap between them labelled *saving*. Then a vertical wall dropped at $c_1=y_1$: the
borrowing limit. The optimum slides back onto the endowment, saving collapses to zero, and the
MPC label flips from 0.51 to 1.00.

One picture that contains the whole session: the household that can trade across time, and the
one that cannot.

## Novelty line

Most courses present permanent income and then, separately, credit constraints as a caveat.
This video derives them as **the same diagram** — the constraint is a wall on the line already
drawn — and shows the MPC jumping on screen when the wall arrives. It also decomposes the
interest-rate effect exactly, rather than waving at "income and substitution effects", and
names the one parameter that decides the sign.

## Build order

1. Copy `check_consumption.py` from the Map directory; it already verifies every closed form.
2. `script.md` → `beats.json` → **TTS deferred (credits exhausted)**; durations estimated at
   197 wpm and flagged.
3. `scenes.py` with the fixed-grid `Stack`.
4. `beatcheck` → render `-ql` → inspect a frame from every derivation beat.
