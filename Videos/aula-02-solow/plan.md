---
tags: [video, aula-02, explainer, plan]
date: 2026-09-20
slug: aula-02-solow
---

# Plan — Aula 2: Growth Facts and the Mechanics of Solow

**Scoping answers carried from the set (2026-09-17).** Purpose *first exposure*; length
**~50 min**, nothing skipped; math **textbook derivation**, every line on screen; examples
*calibrated case + the course's own exercises (number and page only) + Brazilian data*.
Narration **English** per the global rule.

Source: Kurlat (2020) ch. **3** and §**4.1–4.2**, printed pp. 47–61 (offset 0). The derivation
layer already exists in full at [[Map/aula-02-solow-mecanica/00-index]] — five notes that prove
existence, uniqueness and global stability rather than asserting them, plus `check_solow.py`.
This video animates those notes; it adds no content beyond them.

---

## Thesis

> **Diminishing returns is the entire model. It is why the economy converges, it is why saving
> more can never raise growth forever — and it is why capital accumulation cannot explain why
> Brazil is poor.**

One assumption (4.3) does all three jobs. The video's job is to make the viewer feel that
single fact three times, in three different costumes, and then watch it fail against data.

## The cold open, with its clock (0:00–1:30)

Two numbers, then a third that breaks them.

| | |
|---|---|
| Brazil, gross capital formation, 2000–2023 average | **18.3% of GDP** |
| United States, same measure, same years | **21.3% of GDP** |
| Brazilian income per head, 2023, as a share of American | **25.7%** |

*"Brazil invests eighteen per cent of what it produces. The United States invests
twenty-one. Three points apart. And Americans are four times richer. By the end of this video
you will be able to put those two investment rates into the most famous model in
macroeconomics, turn the handle, and watch it tell you — with a straight face — that Brazil
should be ninety-two per cent as rich as the United States."*

No definition inside the first ninety seconds. The hook is a discrepancy the viewer cannot
yet resolve, and the resolution is the whole of session 3.

**Measured, not asserted.** `data/check_solow_brazil.py`, World Bank WDI, fetched 2026-09-20:
observed ratio 0.257; predicted from saving rates alone 0.926; predicted from *s* and
*(n+δ)* together 0.920; unexplained factor **3.58×**. For saving alone to close the gap,
Brazil would have to invest **1.4%** of GDP — the script asserts that absurdity rather than
stating it.

## Colour mapping (unchanged from Aula 1 — the set shares one palette)

| Colour | Role |
|---|---|
| `BLUE` | the object being measured: the production function, $k$, the data |
| `YELLOW` | the live derivation line; the object of attention |
| `GREY` | muted: lines already past; background series |
| `RED` | what breaks: the wrong first attempt, the model's failure |
| `GREEN` | the repaired object: the result that survives |

## Beat sheet — 26 beats

Budgets are written at 150 wpm and **rebuilt from measured audio** after synthesis, as in
Aula 1 (`george` speaks at ~197 wpm, so the video lands near 47 min).

### Act 0 — the discrepancy

| Beat | On screen | Narration's job | s |
|---|---|---|---|
| `BeatOpen` | the three numbers, one at a time | pose the gap; promise the model will get it wrong | 90 |

### Act I — the facts a growth model has to hit (ch. 3, pp. 47–51)

| Beat | On screen | Narration's job | s | Anchor |
|---|---|---|---|---|
| `BeatVeryLongRun` | the UK series on a log scale; the \$400 subsistence line | growth is a recent phenomenon; what orders countries today is the **date of take-off**, not the rate after it | 110 | §3.1, p. 47 |
| `BeatKaldor` | facts 1–3 as a real table, one row per step, with the US magnitudes | 1.5% a year and 27× over 216 years; $K/Y=3.2$; labour share 65%, falling ~3pp after 2000. And the proprietors'-income problem that makes the last one hard to measure | 150 | §3.2, pp. 48–50 |
| `BeatFactFour` | **derivation**: divide capital income by the capital stock, then divide top and bottom by GDP | fact 4 is not independent — it is facts 2 and 3 divided by each other. $r=(1-\text{labour share})/(K/Y)=11\%$ gross, ~6% net of depreciation | 130 | p. 50 |
| `BeatScatter` | growth since 1960 against initial income, **WDI, all countries**, Brazil and the US marked | rich countries cluster; poor countries scatter enormously. Absolute convergence **fails**; conditional convergence survives | 130 | §3.3, p. 51 |

### Act II — the ingredients, and what each one buys (§4.1, pp. 53–57)

| Beat | On screen | Narration's job | s | Anchor |
|---|---|---|---|---|
| `BeatCRS` | assumptions 4.1–4.4 as a table, one row per reveal | CRS is replication and it is what lets the model close in one variable; diminishing returns is the engine; **Inada does not follow from diminishing returns**, and the two buy different things | 140 | pp. 53–55 |
| `BeatCobbDouglas` | **derivation**: verify CRS, $F_K>0$, $F_{KK}<0$, Inada, for $K^\alpha L^{1-\alpha}$ | Kurlat says "easy to verify" and leaves it; we verify it, four lines, because the Inada check is where $\alpha<1$ earns its keep | 150 | (4.1.2), p. 55 |
| `BeatEuler` | **derivation**: differentiate $F(\lambda K,\lambda L)=\lambda F$ at $\lambda=1$ | Euler's theorem: factor payments exhaust output exactly, so competitive factors leave zero profit — and $\alpha$ *is* the capital income share, which is why the 0.65 labour share of Act I hands us $\alpha\simeq0.35$ | 140 | p. 55 |
| `BeatSavingRate` | assumptions 4.5–4.8; then the $S=I$ algebra **with** a government | $S=I$ needs a closed economy, **not** $G=0$ — the tax term cancels (footnote 2, p. 56). $s$ exogenous is the assumption the rest of the course dismantles | 130 | pp. 55–57 |

### Act III — the fundamental equation (§4.2, pp. 57–59)

| Beat | On screen | Narration's job | s | Anchor |
|---|---|---|---|---|
| `BeatPerWorker` | $y=F(K,L)/L = F(k,1)\equiv f(k)$, three steps | only the middle step is substantive: it is CRS with $\lambda=1/L$ | 110 | (4.2.1) |
| `BeatLawOfMotion` | **derivation, 7 lines**: from $\Delta k$ to (4.2.2) exact | the step everyone fumbles is multiplying and dividing by $L_t$ so $L_t/L_{t+1}=1/(1+n)$ | 170 | p. 58 |
| `BeatApproximation` | collect over the common denominator; the familiar form appears **divided by $1+n$** | the $(1+n)$ changes the **speed**, never the destination — dividing by a positive number cannot move a zero. Error is exactly $n/(1+n)$ of each period's move | 140 | (4.2.2) |
| `BeatContinuous` | **derivation**: quotient rule on $k=K/L$ | what Kurlat calls an approximation *is* Romer's differential equation exactly. Say which convention you are in | 130 | Romer ch. 1 |
| `BeatGrowthRate` | $\dot k/k = sf(k)/k-(\delta+n)$: a falling curve against a flat line | this single picture **is** conditional convergence; and $\dot y/y=\alpha\dot k/k$, so output always grows slower than capital, by exactly the capital share | 120 | §3.5 |

### Act IV — the steady state (§4.2, pp. 59–61)

| Beat | On screen | Narration's job | s | Anchor |
|---|---|---|---|---|
| `BeatDiagram` | the Solow diagram **built**: axes → $f(k)$ → $sf(k)$ → $(\delta+n)k$ → the crossing | break-even investment is two things added: $\delta k$ replaces what wore out, $nk$ equips the workers who arrived. That is why $n$ and $\delta$ enter identically | 140 | p. 59 |
| `BeatClosedForm` | **derivation**: solve $sk^\alpha=(\delta+n)k$ | read the exponents rather than memorise them: $1/(1-\alpha)=1.5$ on capital, $\alpha/(1-\alpha)=0.5$ on output. **Output responds less than capital, because of diminishing returns** | 140 | §4.1 |
| `BeatExistence` | **derivation**: $\phi(k)/k$, its two Inada limits, the intermediate value theorem | existence is *exactly* the two Inada conditions | 150 | §4.2 |
| `BeatUniqueness` | **derivation**: $f(k)/k$ strictly falling, via chord-above-tangent | uniqueness is *exactly* diminishing returns. Two assumptions, two halves of one theorem | 140 | §4.2 |
| `BeatAK` | **wrong first attempt**: $f(k)=ak$ — the line and the line never cross | drop assumption 4.3 and there is no steady state at all: growth forever, or collapse. The $AK$ model, and proof that "level not rate" is a *consequence* of diminishing returns and nothing more | 130 | §4.2 |
| `BeatStability` | monotone arrows on the diagram; then $G'(k_{ss})<1$ | the picture is not a proof; here is the proof. Convergence at $\lambda=(1-\alpha)(\delta+n)=4\%$ a year — a **half-life of 17 years** | 150 | §4.3 |

### Act V — level against rate, and the failure (§4.2 + the data)

| Beat | On screen | Narration's job | s | Anchor |
|---|---|---|---|---|
| `BeatCompStatics` | implicit differentiation; the signed table | all three are **level** effects; the long-run growth column is zero in every row. $n$ and $\delta$ are literally the same parameter here | 140 | §5.1 |
| `BeatTransition` | $s$ rises: $k$ cannot jump, $y$ does not jump, $c$ falls **discretely**, $\dot k$ jumps up | growth spikes and decays at $\lambda$; the level is permanently higher. The area under the growth spike **is** the level gain | 160 | §5.2 |
| `BeatNumbers` | $s:0.20\to0.25$ with $\alpha=1/3$, $\delta=0.05$, $n=0.01$ | +11.8% output per worker, peak growth ~0.5% a year, most of it gone within a generation. That is what "save more" buys | 130 | §5.2 |
| `BeatConsumption` | **derivation**: $dc_{ss}/ds$ and its criterion | more saving raises long-run consumption **iff** $f'(k_{ss})>\delta+n$. A model with no optimising agent has produced a welfare criterion — and that inequality is the Golden Rule, which is session 3 | 120 | §5.4 |
| `BeatBrazil` | **the failure**: 18.3 vs 21.3 into the closed form → 0.92, against an observed 0.257 | the elasticity is 0.5, so a 14% saving gap buys a 7% income gap. To explain the real gap Brazil would need to invest **1.4%** of GDP. The model is out by a factor of 3.6 | 160 | §4.1, §5.5 |
| `BeatClose` | the closing image | what must carry the weight instead, and what session 3 has to do | 110 |

## The wrong first attempt

| Where | The plausible move | How it fails |
|---|---|---|
| Act IV | assume a production function without diminishing returns | $AK$: the two lines never cross, no steady state exists |
| Act V | explain Brazil's income with Brazil's saving rate | predicts 92% of US income; the truth is 26% |

Act V's is the video's real one, and it is aimed at the exam's most expensive error (trap 1 in
`rules/02`): **a level effect is not a rate effect.**

## Scope line

- **Session 3 owns**: the Golden Rule, technological progress and the balanced growth path,
  growth accounting and TFP, the convergence-speed regression, factor markets as an
  equilibrium result. Each is named here and handed forward, never developed.
- The project scope lock holds: no stochastic DSGE, no Bellman, no RBC, no time-series
  econometrics, no Kurlat ch. 8 or chs. 12–15, nothing from Ljungqvist & Sargent.
- **No exercise statement is animated.** Cited by number and page only: 3.1–3.3 (pp. 51–52),
  4.1–4.2 (p. 72), 4.3–4.4, 4.5 *Malthus*, 4.6–4.7 (pp. 72–73), 5.4 (p. 100).
- Malthus (Ex. 4.5) is named as the model of "the other 99% of human history" and dropped.

## Closing image

**The Solow diagram with the failure drawn on it.** The two curves, the crossing at $k_{ss}$
— and beside it, two dots: where the model puts Brazil (92% of the US) and where Brazil
actually is (26%). The gap between those dots is labelled once: **everything session 3 is
about**.

Why it is the memorable frame: the canonical diagram every student can already draw, with the
one thing it *cannot* do drawn next to it. A student who redraws that has both the mechanism
and its limit.

## The novelty line

Every treatment draws the diagram. Almost none of them *proves* that the crossing exists
(Inada), that it is unique (concavity), and that the economy gets there without overshooting
— nor shows that these are three separate assumptions doing three separate jobs. And almost
none runs the model's own elasticity against real numbers for the student's own country and
reports that it misses by 3.6×. This video does both, and the second is what makes session 3
feel necessary rather than merely next.

## Build order

1. ✅ Data fetched: 3 WDI indicators, all countries, registry + `check_solow_brazil.py` verified.
2. `script.md` → `beats.json` → TTS (expect repeated passes: the API allows 1 request at a time).
3. `scenes.py` using the **fixed-grid `Stack`** from Aula 1 — carry that file forward, it is
   the fix for the overlapping-lines defect.
4. `beatcheck` (min 12 steps a beat), render at `-ql`, **pull a frame from every derivation
   beat and look at it**, compile, hand over the draft.
