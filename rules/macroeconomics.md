---
id: macroeconomics
title: Applied macroeconomics
tier: 2
applyTo: "**/{macro,nowcast,forecast,var,svar,business_cycle,monetary,fiscal}/**, **/*{Nowcast,Macro,VAR,Phillips,Taylor}*"
skills: [econ]
owner: quant-team
---

Macro used for forecasting, positioning, and policy analysis. The binding constraints
are not theoretical elegance but **data vintage, identification, and the fact that
nearly every aggregate relationship is simultaneous**.

## Non-negotiable

1. **Evaluate forecasts on the data available at the time — vintage data, never the
   latest release.**
   *Why:* revisions to GDP, payrolls, and industrial production are large, systematic,
   and correlated with the cycle. A model backtested on final data is being scored on
   information nobody had, and the result does not survive contact with live use.
   *Check:* the backtest reads an as-of snapshot (ALFRED/real-time database), not a
   current download. This is `quant-research#1` applied to macro.

2. **Name the identification scheme for any shock.** Recursive ordering, sign
   restrictions, external/narrative instrument, or high-frequency identification around
   announcements.
   *Why:* macro aggregates are simultaneous by construction — policy responds to the
   economy while the economy responds to policy. An impulse response without an
   identification argument is a correlation drawn with confidence bands.

3. **Separate accounting identities from behavioural claims.** `Y = C + I + G + NX` is
   true by construction and explains nothing.
   *Why:* identities cannot be violated, so a conclusion derived from one alone is a
   restatement. Most bad macro reasoning is an identity worn as a theory.

4. **Distinguish level effects from growth effects, and transitory from permanent
   shifts.**
   *Why:* the two have different policy implications and different persistence, and
   conflating them inverts the conclusion — a saving-rate change moves the level of
   income per capita, not its long-run growth rate.

5. **Treat the output gap, potential output, NAIRU, and `r*` as estimates with wide
   uncertainty, not as data.**
   *Why:* real-time output-gap estimates are revised by amounts comparable to the gap
   itself. Any signal built on one inherits that error, and the revision is correlated
   with the cycle you are trying to trade.

6. **State the expectations assumption, and check whether it survives the policy you
   are evaluating.**
   *Why:* the Lucas critique — a reduced-form relationship estimated under one regime
   shifts when the regime changes, because expectations do. A policy recommendation
   from a reduced form assumes away the thing being tested.

7. **Nominal and real are never mixed.** State the deflator, the base period, and
   whether cross-country figures are market-rate or PPP.

## Prefer

8. **A random-walk or AR(1) benchmark for every forecast claim.** Most macro series are
   near-unit-root, and beating the naive benchmark out of sample is the entire test.
   Report the ratio, not the level of fit.

9. **Local projections over VAR** for impulse responses when you care about horizon
   robustness — fewer parametric restrictions, less error compounding at long horizons,
   at the cost of efficiency.

10. **Factor models** (dynamic factor, FAVAR) when you have many correlated series.
    Macro data is highly collinear; a handful of factors usually carries most of the
    signal and avoids arbitrary variable selection.

11. **Mixed-frequency methods** (MIDAS, bridge equations, state-space nowcasting) rather
    than aggregating high-frequency data down. Aggregation discards the timeliness that
    made the series useful.

12. **Decompose nominal rates before using them**: real rate, expected inflation, and
    term premium move for different reasons and have different implications. The same
    applies to breakevens (expectations plus liquidity and inflation-risk premia).

13. **State dependence in multipliers and transmission.** Fiscal multipliers, policy
    pass-through, and correlations are regime-dependent — slack, the effective lower
    bound, and balance-sheet conditions all change the answer.

14. **Report forecast uncertainty**, and evaluate the whole predictive distribution
    (CRPS, coverage) when the tails matter — which for positioning they always do.

## Avoid

15. **The HP filter for the output gap or the cycle.** It has a severe end-point problem
    exactly where you need it (the present), induces spurious dynamics, and its
    predictions have no basis in the underlying process. Use Hamilton's regression
    filter, a production-function estimate, or a band-pass filter with the end-point
    treatment stated.

16. **Treating the Solow residual as technology.** It absorbs measurement error, factor
    utilization, markups, and reallocation. It is a residual, which is a measure of what
    the model does not explain.

17. **Inferring causality from aggregate time-series correlation.** Simultaneity is the
    default, not the exception.

18. **A representative agent where heterogeneity is the mechanism.** The distribution of
    liquidity, credit constraints, and marginal propensities to consume is exactly what
    determines fiscal multipliers and transmission.

19. **Extrapolating a short-run Phillips-curve trade-off.** The relationship is unstable
    across regimes and flattens or steepens with the anchoring of expectations; a
    coefficient estimated on one sample does not transport.

20. **Ignoring the intertemporal government budget constraint.** Deficits today are
    taxes, inflation, or default later; a model silent on which is incomplete.

21. **Seasonally adjusting data that is already adjusted**, and comparing across
    definitional breaks (methodology changes, rebasing, reclassification) without
    splicing.

**Reference:** `rules/references/macroeconomics.md` — real-time data and revisions,
shock identification methods compared, forecasting and nowcasting toolkit with
benchmarks, cycle measurement and filter choice, policy rules and `r*`, macro-to-asset
transmission, growth accounting caveats.
Load it when implementing; the rules above stand on their own.
