# macroeconomics — reference

Loaded on demand from `rules/macroeconomics.md`. Rules live there; this is the detail
needed to implement them.

## 1. Real-time data and revisions

The single most common way a macro backtest lies to you.

| Series | Revision behaviour |
|---|---|
| GDP (advance → second → third → annual → benchmark) | Large; sign of quarterly growth can flip |
| Payrolls | Two revisions plus annual benchmark; birth-death model matters at turning points |
| Industrial production | Revised for years |
| CPI | Index level never revised; seasonal factors are |
| Surveys (PMI, sentiment) | Rarely revised — part of why they are useful for nowcasting |

Revisions are **not** noise: they are correlated with the cycle, because early estimates
lean on incomplete source data that under-samples exactly the firms that fail or surge.

```python
# Correct: as-of vintage
df = fred.get_series_asof("GDPC1", asof="2019-03-15")
# Wrong: today's view of 2019
df = fred.get_series("GDPC1").loc[:"2019-03-15"]
```

Build the panel as a **vintage triangle** — rows = reference period, columns = release
date — and slice by release date, never by reference period alone.

## 2. Identifying shocks

| Scheme | Idea | Cost |
|---|---|---|
| **Recursive (Cholesky)** | Ordering imposes which variables react contemporaneously | Ordering is an untestable assumption; results often flip when reordered |
| **Sign restrictions** | Impose the sign of responses implied by theory | Set-identified, not point-identified — report the whole set, not the median |
| **External instrument / proxy SVAR** | Use a narrative or exogenous series as instrument for the shock | Needs a genuinely exogenous, relevant instrument |
| **High-frequency identification** | Asset price moves in a tight window around a scheduled announcement | Cleanest available for monetary shocks; needs intraday data; contaminated by the information effect |
| **Narrative** | Historical documents establish exogeneity | Labour-intensive; few observations |
| **Heteroskedasticity-based** | Identification from variance shifts across regimes | Requires a credible regime break |

The **information effect** is the trap in high-frequency identification: a hawkish
surprise may signal that the central bank sees strong growth, so yields and equities can
both rise. Separate policy from information using the co-movement of rates and equities,
or an instrument purged of the growth signal.

**Local projections** for impulse responses:

```
y_{t+h} - y_{t-1} = α_h + β_h · shock_t + Γ_h · controls_t + ε_{t+h}     one regression per h
```

`β_h` traces the IRF directly. Advantages: no error compounding over horizons, easy
state dependence (interact the shock with a regime indicator), easy non-linearity.
Cost: less efficient than a VAR, and serially correlated residuals require HAC or
Driscoll-Kraay standard errors.

Use a VAR when you need the full system and a consistent covariance structure; use LP
when you care most about a specific horizon or state dependence.

## 3. Forecasting and nowcasting

**Always report against a benchmark.** For most macro series the honest benchmark is a
random walk or a low-order AR:

```
relative RMSE = RMSE_model / RMSE_benchmark        < 1 is the only claim worth making
Diebold-Mariano test for whether the difference is significant
```

| Method | Use when |
|---|---|
| AR / ARIMA | Baseline; often hard to beat at short horizons |
| **Dynamic factor model** | Many correlated indicators; extracts a few common factors |
| **FAVAR** | Factors plus a policy variable, for shock analysis with a wide information set |
| **MIDAS / bridge equations** | Predictors at higher frequency than the target |
| **State-space nowcast (Kalman)** | Ragged-edge data, mixed frequencies, continuous updating as releases arrive |
| BVAR with Minnesota prior | Many variables, short sample — shrinkage prevents overfitting |
| Forecast combination | Almost always beats any single model; equal weights are a strong default |

**Ragged edge** is the defining nowcasting problem: on any given day, different series
have different last-observation dates. A state-space model handles it natively; ad-hoc
alignment discards the newest information, which is the information you wanted.

Evaluate the distribution, not just the point: CRPS, PIT histograms for calibration, and
interval coverage. A point forecast with no uncertainty is not usable for sizing.

## 4. Cycle measurement

Trend-cycle decomposition is a modelling choice with large consequences.

| Filter | Problem |
|---|---|
| **HP** | Severe end-point instability; induces spurious cycles even in a random walk; the smoothing parameter is arbitrary. **Do not use for real-time gaps.** |
| **Hamilton regression** | `y_{t+h}` on `y_t … y_{t-3}`; no end-point problem, no spurious dynamics, simple. The recommended default |
| Baxter-King / Christiano-Fitzgerald | Band-pass; BK loses observations at both ends, CF is one-sided-capable |
| Beveridge-Nelson | Model-based permanent/transitory split; depends on the ARIMA specification |
| Production function | Structural, interpretable, but requires estimating potential inputs and TFP |
| Unobserved components / multivariate | Uses a Phillips curve or Okun relation to pin the gap |

Whatever you choose, **report the real-time (one-sided) estimate**, not the full-sample
smoothed one, whenever the use case is real-time.

Okun's law as a cross-check: `Δu ≈ -β(g - g*)`, `β` around 0.5 for the US. Large
divergence between the unemployment-implied gap and the output-implied gap is a signal
that one of them is mismeasured.

## 5. Policy rules and the natural rate

A Taylor-type rule is most useful as a **forecasting and communication benchmark**,
not as a description of what a committee will do:

```
i_t = r*_t + π_t + φ_π(π_t − π*) + φ_x x_t          φ_π > 0  ⟹  Taylor principle
```

The **Taylor principle**: the nominal rate must move more than one-for-one with
inflation, so the *real* rate rises. Otherwise policy is accommodative when it looks
tight, and equilibria become indeterminate.

`r*` is unobservable and estimated with wide error (Laubach-Williams, Holston-Laubach-
Williams). Two consequences: policy stance should be judged over a *range* of `r*`, and
a strategy conditioned on a point estimate is conditioned on a residual.

At the **effective lower bound** the rule cannot bind. Transmission then runs through
forward guidance, asset purchases, and the exchange rate, and the usual relationships
change sign or magnitude — a model estimated across an ELB period without allowing for
it is misspecified.

## 6. Macro to asset prices

Decompose before you interpret.

```
nominal yield  =  expected average real rate  +  expected inflation
                  + term premium + inflation risk premium + liquidity
breakeven      =  expected inflation + inflation risk premium − TIPS liquidity premium
```

A breakeven move is not an expectations move until the premia are accounted for.

| Channel | Reads through |
|---|---|
| Growth surprises | Cyclicals vs defensives; credit spreads; curve steepening |
| Inflation surprises | Breakevens, front-end rates, real assets |
| Policy surprises | Front-end rates, curve shape, dollar |
| Term premium | Long end, duration risk, equity discount rates |
| Global dollar cycle | EM assets, commodities, cross-border credit |

**Surprises, not levels.** Markets price the expectation; only the deviation from
consensus moves prices. Build the surprise as `(actual − consensus) / historical
std(surprise)` so it is comparable across releases, and use a consensus vintage that was
available before the release.

UIP fails at short horizons — high-rate currencies tend to appreciate rather than
depreciate, which is the carry trade. Treat the failure as a fact to be modelled (risk
premium, convenience yield), not as an anomaly to be assumed away.

## 7. Growth, in the parts that change decisions

The mechanics of Solow rarely enter applied work. Three implications do:

- **Level vs growth.** Changes in saving rates, tax rates, or capital deepening move the
  *level* of income per worker. Only technology growth moves the long-run growth rate.
  This is where forecasts most often go wrong by an order of magnitude.
- **Convergence is conditional and slow.** Roughly 2%/year toward a country's *own*
  steady state — a ~35-year half-life. Unconditional catch-up is not a fact.
- **Development accounting.** Factor accumulation explains well under half of
  cross-country income differences; the productivity residual dominates. That residual
  is exactly the thing measured worst.

Growth accounting: `ΔA/A = ΔY/Y − α·ΔK/K − (1−α)·ΔL/L`, with `α` from the capital income
share under competitive pricing. The residual is not technology — see rule 16.

## 8. Diagnostic questions for any macro claim

- Is this an identity or a behavioural claim?
- Which data vintage, and would it have been available then?
- What identifies the shock?
- Level effect or growth effect; transitory or permanent?
- Is the gap/`r*`/NAIRU an estimate being treated as data?
- Does the relationship survive the regime change being proposed?
- What is the naive benchmark, and does this beat it out of sample?
