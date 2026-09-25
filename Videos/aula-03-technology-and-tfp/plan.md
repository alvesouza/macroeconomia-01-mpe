---
tags: [video, aula-03, explainer, plan]
date: 2026-09-21
slug: aula-03-technology-and-tfp
---

# Plan — Aula 3: Technology, and What Solow Cannot Explain

Scoping carried from the set: *first exposure*, ~50 min, **textbook derivation**, examples =
calibrated case + the course's own exercises (number and page only) + Brazilian data. English.

Source: Kurlat (2020) §**4.3–4.5** and ch. **5**, printed pp. 61–100. Derivation layer already
complete at [[Map/aula-03-solow-evidencias/00-index]] (5 notes + `check_growth.py`).

---

## Thesis

> **The model gets repaired and then fails anyway — and the failure is the finding. Solow
> proves the answer is not capital, names what is left, and hands it over unexplained.**

Aula 2 ended with a 3.6× miss. This lecture fixes the growth failure (technology), then spends
its second half proving the level failure is *irreparable* within the model.

## Cold open (0:00–1:30)

Continue the Brazil thread. If Conjecture 5.1 is right — same technology everywhere, income
gaps are capital gaps — then capital is scarce in Brazil, so it must earn more there. How much?

| | |
|---|---|
| Brazilian income per head, vs US | 25.7% |
| Implied rental rate, Brazil vs US | **12.5×** |
| Implied Brazilian interest rate | **138% a year** |

*"Not twelve per cent. A hundred and thirty-eight. And if that were true, every dollar of
capital on earth would already be in Brazil."*

Measured by `data/check_lucas.py`, which also reproduces Kurlat's own Mexico figure (9.4×) as
an assertion, so the machinery is verified against the book before it is pointed anywhere new.

## Beat sheet — 26 beats

Budgets at 150 wpm, rebuilt from measured audio after synthesis (~197 wpm → lands near 47 min).

### Act 0
| Beat | Job | s |
|---|---|---|
| `BeatOpen` | the 138% number; the promise that the model will be repaired and still fail | 90 |

### Act I — the Golden Rule (§4.3, pp. 61–63)
| Beat | Job | s |
|---|---|---|
| `BeatGoldenSetup` | $c_{ss}=f(k)-(\delta+n)k$; why it is cleaner as a choice of $k$ than of $s$ | 110 |
| `BeatGoldenFOC` | **derivation**: $f'(k_{gold})=\delta+n$, second-order condition, Inada for interiority. Read it: the machine must earn its own upkeep | 130 |
| `BeatSGold` | **derivation, two ways**: equate $k$'s → $s_{gold}=\alpha$; then the investment-share argument that explains *why* — save exactly capital's share | 140 |
| `BeatAsymmetry` | above the peak, cutting $s$ raises consumption **immediately and forever** — a Pareto improvement needing no preferences. Below it, some generations lose: a trade-off, not an inefficiency | 150 |
| `BeatDynamicTest` | the observable test: capital income vs investment, 35% against 20% of GDP. Dynamic inefficiency never binds in the data | 110 |

### Act II — markets (§4.4, pp. 63–69)
| Beat | Job | s |
|---|---|---|
| `BeatFirmProblem` | **derivation**: $\max F-r^KK-wL$ → $r^K=f'(k)$, $w=f(k)-kf'(k)$, with the product rule shown | 140 |
| `BeatZeroProfit` | Euler again: $r^Kk+w=f(k)$ exactly. Zero profit is forced, not assumed | 110 |
| `BeatAlphaEquilibrium` | the Cobb–Douglas share is $\alpha$ at **every** $k$, in and out of steady state — which is the empirical argument for the functional form. Plus the CES caveat: $\sigma>1$ and the falling labour share | 140 |
| `BeatInterestRate` | **derivation**: no-arbitrage → $r=f'(k)-\delta$. Golden Rule restated as $r=n$. Poor countries should have high $r$ — the prediction Act IV kills | 130 |

### Act III — technology (§4.5, pp. 69–72)
| Beat | Job | s |
|---|---|---|
| `BeatEfficiencyUnits` | $Y=F(K,AL)$; $\tilde L=AL$; Kurlat's own warning that these are not variables we care about | 110 |
| `BeatTildeLaw` | **derivation**: the law of motion in efficiency units; where $(1+g)(1+n)$ enters; the $ng$ cross term is 0.2% of break-even, so it goes | 150 |
| `BeatBGP` | the growth-rate table, translated back: $\tilde y$ constant, $y$ grows at $g$, aggregates at $n+g$, $K/Y$ and $r$ flat. **Proposition 4.3** | 140 |
| `BeatUzawa` | **derivation sketch**: why technology must be labour-augmenting for a BGP to exist — and the Cobb–Douglas exception where all three forms are the same up to units | 150 |
| `BeatDisappointing` | Kurlat's candour quoted: assumption 4.9 is "rather disappointing". The model explains accumulation completely and growth not at all | 90 |

### Act IV — quantify, and reject (§5.1–5.3, pp. 75–86)
| Beat | Job | s |
|---|---|---|
| `BeatCalibration` | five parameters, each from a separate fact; then the check: $K/Y=s/(\delta+n+g)=3.08$ against a measured 3.2. **The model's best moment** | 140 |
| `BeatConjecture` | Conjecture 5.1 stated as a falsifiable claim. If true, poverty is a capital problem — and capital can be accumulated or imported | 100 |
| `BeatTest1` | **derivation**: eq. (5.3.1) with the Taylor step named; growth falls in $k$, so convergence is predicted. The scatter says no. Two honest qualifications: population weighting (China+India), and within-group convergence (US states, Western Europe) | 160 |
| `BeatSpeed` | **derivation**: log-linearise to $\lambda=(1-\alpha)(\delta+n+g)=4.2\%$, half-life 16 years. Data say 2%. To match, $\alpha$ would have to be **0.69** — twice the accounts' capital share | 140 |
| `BeatTest2` | predicted levels: \$10,000 against an actual \$1,000, and the gap widens the poorer the country | 100 |
| `BeatLucas` | **derivation**: (5.3.4), exponent $(\alpha-1)/\alpha=-1.857$; Kurlat's Mexico 9.4×; then **Brazil 12.5×, 138% a year**. The Lucas paradox needs no capital data at all. Why the exponent is so violent — and that $\alpha=0.7$ would tame it to 1.6× | 160 |

### Act V — what is left (§5.4–5.5, pp. 86–95)
| Beat | Job | s |
|---|---|---|
| `BeatResidual` | **derivation**: total-differentiate → $g_Y=g_A+\alpha g_K+(1-\alpha)g_L$; factor shares enter *because* of Act II. The residual is solved for, never observed | 150 |
| `BeatIgnorance` | what the residual actually contains: utilisation, composition, allocation, institutions, and every error in $\alpha$. Abramovitz: "a measure of our ignorance" | 130 |
| `BeatDevAccounting` | **derivation**: the level decomposition in logs; worked example: capital 28.8%, TFP 71.2% | 130 |
| `BeatKYform` | **derivation**: the $K/Y$ form, and why it is preferred (capital is endogenous; $K/Y$ is not). Capital's share of the log gap falls from 28.8% to **5.2%**. Say which decomposition you used | 140 |
| `BeatHumanCapital` | $h=e^{\phi S}$ justified by Mincer regressions; 4 years against 12 gives $h$ ratio 0.45, contributing 0.59. Real, and far from sufficient. **The exponent trap**: $h^{1-\alpha}$ in one form, $h$ in the other | 140 |
| `BeatClose` | where TFP differences come from — misallocation, institutions, adoption barriers, quality, measurement. The model localises the problem precisely and hands it over | 120 |

## The wrong first attempt

Conjecture 5.1 itself: a coherent, attractive, testable claim that fails three independent
tests. Act IV is built as a trial — hypothesis, three tests, verdict — rather than as a survey.

## Scope line

- **Endogenous growth is out** (Kurlat chs. 12–15, outside the course). Named once in
  `BeatDisappointing` and dropped.
- The Golden Rule stops exactly where preferences would be needed — that is session 4.
- Exercises by number and page only: 4.6–4.8 (pp. 73–74), 4.9–4.10 (p. 74), 4.11–4.12 (p. 74),
  5.1–5.2 (p. 96), 5.3 (p. 97), 5.4 (p. 97), 5.5–5.6 (pp. 98–99).
- Business-cycle uses of TFP are named in one clause (procyclicality) and dropped.

## Closing image

**The bar of the log income gap, split.** One horizontal bar for a poor country against the US,
divided into capital, human capital and TFP — drawn twice, once under each decomposition, so
the TFP block visibly grows from 71% to 95% when you switch to the $K/Y$ form. Underneath, one
line: *the residual is what we cannot explain, and its size depends on a choice you must
declare.*

## Novelty line

Most treatments report "TFP explains most of it" as a fact. This one derives both
decompositions, shows the answer moves by twenty points on a modelling choice, and makes the
student say which one they used. And it runs the Lucas paradox on Brazil rather than on a
textbook country, where it produces an interest rate no one can believe.

## Build order

1. ✅ Data + `check_lucas.py` verified (reproduces Kurlat's 9.4× as an assertion).
2. `script.md` → `beats.json` → **TTS deferred: Speechify credits exhausted 2026-09-21.**
   Durations estimated at 197 wpm meanwhile, flagged `estimated` in the manifest.
3. `scenes.py`, carrying the fixed-grid `Stack` forward from Aula 1.
4. `beatcheck` → render `-ql` → **pull a frame from every derivation beat and look at it**.
