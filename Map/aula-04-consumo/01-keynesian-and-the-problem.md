---
tags: [aula-04, kurlat-cap-06, keynes, funcao-consumo, puzzle-de-kuznets]
date: 2026-09-18
---

# 1. The Keynesian consumption function, and the three facts that break it

**Kurlat §6.1, printed pages 103–105.** Up: [[00-index]] ·
Next: [[02-two-period-problem]] · Rules: [[04_consumo_poupanca]]

Before building the intertemporal model it is worth being precise about what is wrong with the
thing it replaces. The Keynesian consumption function is not stupid; it fits one kind of data
very well and fails three specific tests, and the intertemporal model was built to pass exactly
those three.

---

## 1.1 The function

Keynes (1936) proposed that consumption depends on current disposable income:

$$C = \bar C + \mathrm{mpc}\cdot Y, \qquad 0<\mathrm{mpc}<1,\ \ \bar C>0$$

with two properties Keynes called "psychological law":

- the **marginal** propensity to consume is between zero and one — people spend part of extra
  income and save the rest;
- the **average** propensity to consume, $C/Y = \bar C/Y + \mathrm{mpc}$, **falls** as income
  rises, because the constant $\bar C$ is spread over a larger base.

This is the consumption function behind the Keynesian cross and the textbook multiplier
$1/(1-\mathrm{mpc})$, and the reason the multiplier exceeds one. It is also, note, a *rule*
rather than a decision — the same methodological status as Assumption 4.7 in
[[02-ingredients]].

## 1.2 Fact 1 — cross-section against time series (the Kuznets puzzle)

**In a cross-section of households** the function fits well: richer households do save a larger
share of income. The APC falls with income, exactly as predicted.

**In long-run time series** it fails. Kuznets (1946) found that the US aggregate saving rate was
roughly **constant** from the 1870s to the 1940s, over a period in which real income per head
rose several-fold. If the APC fell with income as the cross-section implies, the saving rate
should have climbed steadily. It did not.

So the same function cannot describe both. Something distinguishes "having a high income this
year" from "being a high-income economy".

**What the intertemporal model says.** Consumption depends on lifetime wealth, so a household
whose income is temporarily above its own average consumes a smaller share of it. In a
cross-section, high-income households are disproportionately households having a *good year*, so
they save more — the cross-sectional pattern is a composition effect, not a preference. In the
long run, when everybody's permanent income rises together, the ratio is unchanged. Both facts,
one model. That is Friedman's (1957) permanent income hypothesis and it is derived in
[[04-permanent-income]].

## 1.3 Fact 2 — consumption is smoother than income

Aggregate consumption is markedly less volatile than aggregate income over the business cycle;
the standard deviation of consumption growth is roughly half to two-thirds that of output
growth, and non-durable consumption is smoother still.

A function $C=\bar C+\mathrm{mpc}\cdot Y$ with $\mathrm{mpc}$ near the observed cross-sectional
value of 0.7–0.9 predicts consumption almost as volatile as income. It has no mechanism for
smoothing, because it has no borrowing, no saving motive and no future in it.

**What the intertemporal model says.** A concave utility function makes households dislike
uneven consumption paths, and access to borrowing and lending lets them do something about it.
Smoothing is the *first-order prediction* of the model rather than a puzzle for it, and its
strength is governed by the curvature $\sigma$. This is derived in [[02-two-period-problem]] §2.4.

## 1.4 Fact 3 — announcements move consumption before income moves

A pre-announced, temporary tax rebate moves consumption at the date it is **announced**, not at
the date the cash arrives; and a tax change known to be temporary moves consumption much less
than one believed permanent. Neither is possible in a function of current income.

**What the intertemporal model says.** Consumption is a function of $W$, the present value of
the whole income path, so anything that changes expectations changes consumption today. This is
also the property that makes the AD curve of [[08_adas_microfundamentos]] shift on news about
the long run — the row in the shift table that IS-LM has no counterpart for.

## 1.5 What a microfoundation has to deliver

Kurlat's programme for the chapter, and the checklist to hold the next four notes against:

1. A consumption function that depends on **wealth**, so that transitory and permanent income
   have different effects — [[04-permanent-income]].
2. **Smoothing** as a consequence of preferences, with a parameter governing how strong it is —
   [[02-two-period-problem]].
3. A prediction for how saving responds to the **interest rate**, including the possibility that
   it responds ambiguously — [[03-income-and-substitution]].
4. An account of **when the old function is right after all**: households that cannot borrow
   consume their current income, and for them the Keynesian function is exactly correct —
   [[05-ricardian-and-constraints]] §5.3.

Point 4 is the one worth emphasising, because it is easy to leave a lecture on this material
believing the Keynesian function was simply wrong. It was not. It is the special case of the
correct model that applies to constrained households, and since a substantial share of
households in every economy is constrained, it remains empirically relevant. The intertemporal
model tells you *which* households it applies to, which the original could not.

## 1.6 The methodological point

This session is the first time in the course that a behavioural rule is replaced by an
optimisation problem, and the gain is worth naming explicitly, because it repeats for labour
supply in [[05_trabalho_lazer]] and for pricing in [[08_adas_microfundamentos]]:

- **Comparative statics become meaningful.** With a rule, "what happens if $r$ rises" has no
  answer — the rule does not mention $r$. With a decision, it has an answer, and possibly an
  ambiguous one that the model can decompose.
- **Welfare becomes computable.** A utility function can be evaluated; a rule cannot. This is
  what lets the Golden Rule question of [[01-golden-rule]] §1.4 finally be settled.
- **Policy invariance.** A rule estimated under one policy regime need not survive a change of
  regime — the Lucas critique. A preference parameter is meant to.

## 1.7 What to be able to do, cold

1. Write the Keynesian consumption function and state its two properties.
2. State the Kuznets puzzle precisely — which data the function fits and which it does not.
3. Give the three empirical failures and say, for each, what mechanism the intertemporal model
   supplies.
4. Explain in what sense the Keynesian function survives as a special case.
5. Give the three methodological arguments for microfoundations.

Practice: Kurlat ch. 6, Exercise 6.1 (p. 123). Worked in
[[Resolucao/kurlat_solutions_ch06|ch06]].
