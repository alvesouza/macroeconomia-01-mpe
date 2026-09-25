---
tags: [aula-05, kurlat-cap-07, elasticidades, frisch, prescott, evidencia]
date: 2026-09-19
---

# 3. Three elasticities, and the number macroeconomics cannot agree on

**Kurlat §7.3, printed pages 137–140.** Up: [[00-index]] · Prev: [[02-static-model]] ·
Next: [[04-dynamic-labour-supply]]

> **Companion:** [The Backward Bend](companion-labour-supply.html) — the three elasticities read
> off the same supply curve at the same point, so the ordering between them is visible.

"The labour supply elasticity" is three different numbers and most disagreements in this
literature are about which one is being quoted. This note defines all three, orders them, and
then works Prescott's Europe–US calculation, which is the highest-stakes application of the
distinction in the course.

---

## 3.1 The three elasticities

All three measure $d\ln h/d\ln w$; they differ in **what is held fixed**.

**Marshallian (uncompensated).** Hold non-wage income $\pi$ fixed and let the household's
welfare change:

$$\varepsilon^{M}=\left.\frac{\partial \ln h}{\partial \ln w}\right|_{\pi}$$

This contains both the substitution and the income effect, so it is the ambiguous one of
[[02-static-model]] §2.3 and can be **negative** (the backward bend).

**Hicksian (compensated).** Hold **utility** fixed by adjusting $\pi$:

$$\varepsilon^{H}=\left.\frac{\partial \ln h}{\partial \ln w}\right|_{\bar u}$$

Pure substitution effect, so $\varepsilon^{H}>0$ always — the compensated labour supply curve
slopes up, no exceptions.

**Frisch.** Hold the **marginal utility of wealth** $\mu$ fixed:

$$\varepsilon^{F}=\left.\frac{\partial \ln h}{\partial \ln w}\right|_{\mu}$$

This is the relevant one in a dynamic model where a household with a given lifetime wealth
reallocates hours across periods in response to a *temporary* wage change. It is the elasticity
of [[04-dynamic-labour-supply]], and the one that appears as $1/\eta$ in Benigno.

### The ordering, and why

$$\boxed{\;\varepsilon^{F} \;\ge\; \varepsilon^{H} \;\ge\; \varepsilon^{M}\;}$$

The first inequality: holding $\mu$ fixed is a *weaker* constraint than holding utility fixed,
because the household is additionally allowed to move resources across periods. More margins of
adjustment means a larger response.

The second is the **Slutsky decomposition** applied to labour supply:

$$\underbrace{\varepsilon^{M}}_{\text{uncompensated}}
= \underbrace{\varepsilon^{H}}_{\text{substitution}}
+ \underbrace{\frac{wh}{c}\,\varepsilon_{\pi}}_{\text{income}}$$

where $\varepsilon_{\pi}=\partial\ln h/\partial\ln \pi<0$ is the (negative) income elasticity —
leisure is a normal good — weighted by the share of earnings in consumption. So
$\varepsilon^{M}\le\varepsilon^{H}$, with equality only if the income effect is zero.

**The log-log case pins the arithmetic.** From [[02-static-model]] §2.4 with $\pi=0$, hours are
constant, so $\varepsilon^{M}=0$ exactly. And the Hicksian elasticity is then exactly the
income-effect term with the sign flipped. That is the cleanest illustration that
$\varepsilon^{M}=0$ does **not** mean "labour supply does not respond" — it means two responses
cancelled. Checked in `check_labour.py`.

## 3.2 The Frisch elasticity and $\eta$

Take the balanced-growth-consistent specification with $v(h)=\chi\,h^{1+\eta}/(1+\eta)$, so the
marginal disutility of work is $v'(h)=\chi h^{\eta}$. The intratemporal condition with the
marginal utility of wealth $\mu$ held fixed is

$$\chi h^{\eta}=\mu w \qquad\Longrightarrow\qquad \ln h = \frac{1}{\eta}\left[\ln\mu+\ln w-\ln\chi\right]$$

$$\boxed{\;\varepsilon^{F}=\frac{d\ln h}{d\ln w}\bigg|_{\mu}=\frac{1}{\eta}\;}$$

**$\eta$ is the inverse Frisch elasticity.** This is exactly the $\eta$ of
[[02-firms-and-as]] §2.3 and of Benigno's $v(L)=L^{1+\eta}/(1+\eta)$. So the parameter that
determines how steep the aggregate supply curve is in session 8 is *this* elasticity, and the
dispute below is therefore a dispute about the slope of the Phillips curve.

## 3.3 What the evidence says

The estimates split cleanly by margin and by group, which is the substance of Kurlat §7.3.

| Group / margin | Frisch elasticity | Source type |
|---|---|---|
| Prime-age men, **intensive** margin | 0.1 – 0.3 | micro panel, hours regressions |
| Married women, secondary earners | 0.5 – 1.0+ | micro, includes participation |
| **Extensive** margin, all | 0.2 – 0.4 | participation responses |
| Aggregate, implied by macro models | 2 – 4 | calibration to match cycles |

**The conflict is real and unresolved.** Micro studies of prime-age men find a very small
elasticity — those men work full-time whatever the wage. Macro models need a large one to
generate observed employment fluctuations from plausible productivity shocks.

**Three reconciliations, all partly right:**

1. **Aggregation over the extensive margin.** §1.5 and [[02-static-model]] §2.6: participation
   is a discrete choice, so the aggregate elasticity is the density of households near their
   reservation wage, not the average individual elasticity. Everyone can have a small individual
   elasticity while the aggregate is large. This is the Rogerson (1988) indivisible-labour
   argument, and it is the main modern answer.
2. **Whose elasticity.** Prime-age men are the least responsive group and the most studied.
   Weighting by the groups that actually move at the margin — secondary earners, the young, the
   near-retired — raises the aggregate number.
3. **Which elasticity.** Micro hours regressions typically identify something closer to the
   Marshallian or Hicksian elasticity; macro models need the Frisch. By §3.1 the Frisch is the
   largest of the three, so part of the gap is definitional rather than substantive.

Kurlat's own note (p. 139) is that estimates from micro studies are "quite a bit lower" than the
value Prescott's calculation requires, "though there is some debate as to how to translate" one
into the other. That translation problem is §3.1.

## 3.4 Prescott's calculation

Prescott (2004), which Kurlat presents at pp. 137–139 and sets as Exercise 7.5 (p. 148).

**The fact.** In the early 1970s, hours worked per person of working age were similar in the US
and in continental Europe. By the 1990s Americans worked roughly **50% more hours** than the
French or the Germans.

**The hypothesis.** The difference is not culture or preferences. It is the **effective marginal
tax rate on labour income** — income tax plus payroll tax plus consumption tax, which all drive
the same wedge between the wage a firm pays and the consumption a worker gets. European
effective rates are far higher.

**The mechanism.** In the static model of [[02-static-model]], a tax $\tau$ makes the relevant
price of leisure $(1-\tau)w$. With a log-log specification and $\pi=0$ hours would be unaffected
(the cancellation of §2.4), so Prescott needs a specification where the substitution effect
dominates — which means a **Frisch elasticity around 1 or higher**.

**The arithmetic, in the form to reproduce.** With $u=\ln c-\chi h^{1+\eta}/(1+\eta)$ and a
government that returns revenue lump-sum, the first-order condition gives

$$\chi h^{1+\eta} = (1-\tau)\frac{wh}{c}$$

and with the consumption share of after-tax income fixed, hours satisfy

$$\frac{h_{\text{EU}}}{h_{\text{US}}}=\left(\frac{1-\tau_{\text{EU}}}{1-\tau_{\text{US}}}\right)^{1/\eta}$$

**Put the numbers in.** Prescott's effective marginal rates are roughly
$\tau_{\text{US}}=0.40$ and $\tau_{\text{EU}}=0.60$. Then

$$\frac{1-\tau_{\text{EU}}}{1-\tau_{\text{US}}}=\frac{0.40}{0.60}=0.667$$

and to deliver $h_{\text{EU}}/h_{\text{US}}=1/1.5=0.667$ requires $1/\eta = 1$, i.e.

$$\boxed{\;\varepsilon^{F}=\frac{1}{\eta}\simeq 1\;}$$

An elasticity of about **one** — well above the 0.1–0.3 that micro studies of prime-age men
report, and around the upper end of what the participation literature finds. Computed in
`check_labour.py`, which also shows how the required elasticity moves with the assumed tax gap.

**Why this matters and why it is contested.** Kurlat records (p. 139) that there is no consensus
on whether Prescott is right. The argument has enormous stakes: if true, a large part of the
Europe–US income-per-person gap of [[04-cross-country-and-ppp]] §4.4 is a *chosen* response to
taxation rather than a productivity failure, and European hours are not a welfare loss but a
purchase of leisure. If the elasticity is really 0.2, taxes explain a fifth of the gap and
something else explains the rest — unionisation, statutory hours, vacation mandates, or
preferences after all.

**The honest position for an exam:** the calculation is a clean identification of what the data
require of the elasticity. Whether that requirement is met is the empirical question, and it is
the same question as §3.3.

## 3.5 The welfare reading, which is the point

Suppose Prescott is right. Then Europeans work less because leisure is *cheap* for them in
after-tax terms, and they are choosing it. Measured GDP per person is lower; utility need not
be. This is precisely the correction that the leisure term in the Jones–Klenow welfare measure
of [[05-beyond-gdp]] §5.4 applies — and it is why that term is one of the largest in the European
decomposition.

So the three sessions connect: [[04-cross-country-and-ppp]] observed the hours gap,
[[05-beyond-gdp]] priced it in welfare terms, and this note supplies the mechanism that
generates it. Being able to run that chain is a good answer to almost any question about
Europe–US comparisons.

## 3.6 What to be able to do, cold

1. Define all three elasticities by what is held fixed, and state the ordering with the reason.
2. Write the Slutsky decomposition for labour supply and identify the income-effect weight.
3. Derive $\varepsilon^{F}=1/\eta$ from $v(h)=\chi h^{1+\eta}/(1+\eta)$.
4. Quote the evidence by margin and group, and give the three reconciliations of the micro–macro
   gap.
5. Reproduce Prescott's calculation and back out the implied elasticity.
6. State the welfare implication and connect it to the Jones–Klenow leisure term.

Practice: Kurlat ch. 7, Exercise 7.5 *Prescott's Calculation* (p. 148) — parts (b) and (c) ask
for exactly the implied elasticity computed above; and Exercise 7.6 (p. 149). Worked in
[[Resolucao/lista4_resolucao|lista 4]] — the Kurlat ch. 7 solution set has not been written yet; the code lives in `Resolucao/kurlat_ch07_codigo/`.
