---
tags: [aula-01, aritmetica-do-crescimento, log, regra-do-70, derivacao]
date: 2026-09-17
---

# 3. Growth arithmetic, with the error terms

**Used throughout Kurlat; formalised here.** Up: [[00-index]] ·
Prev: [[02-real-nominal-and-indices]] · Next: [[04-cross-country-and-ppp]]

> **Companion:** [Reading a Log Scale](companion-growth.html) — the same series on linear and
> log axes side by side, with the rule-of-70 doubling times marked and the log-approximation
> error plotted against $g$.

Every result in sessions 2 and 3 is stated as a growth rate, and half the mistakes in them are
arithmetic rather than economic. This note derives the five facts that get used without
comment for the rest of the course, and says how big the approximation error is in each.

---

## 3.1 Net rates, gross factors, and logs

Three ways to say the same thing:

$$Y_{t} = Y_{t-1}(1+g_t) \quad\Longleftrightarrow\quad
\frac{Y_t}{Y_{t-1}} = 1+g_t \quad\Longleftrightarrow\quad
\ln Y_t - \ln Y_{t-1} = \ln(1+g_t)$$

Define the **log growth rate** $\tilde g_t \equiv \ln Y_t - \ln Y_{t-1}$. The relation between
the two is exact:

$$\tilde g = \ln(1+g), \qquad g = e^{\tilde g}-1$$

Expanding the logarithm gives the approximation and, more usefully, its error:

$$\tilde g = g - \frac{g^2}{2} + \frac{g^3}{3} - \cdots
\qquad\Longrightarrow\qquad
\boxed{\;g - \tilde g \;\simeq\; \frac{g^2}{2}\;}$$

| $g$ | $\tilde g=\ln(1+g)$ | error $g-\tilde g$ | relative error |
|---|---|---|---|
| 0.01 | 0.00995 | 0.00005 | 0.5% |
| 0.05 | 0.04879 | 0.00121 | 2.4% |
| 0.10 | 0.09531 | 0.00469 | 4.7% |
| 0.50 | 0.40546 | 0.09454 | 18.9% |
| 2.00 | 1.09861 | 0.90139 | 45.1% |

**The rule to carry.** The log approximation is excellent for quarterly and annual growth in
developed economies, tolerable for a decade of Chinese growth, and useless for hyperinflation —
which is exactly why [[07_moeda_inflacao]] insists on the *exact* Fisher equation when
inflation is large, and why the Cagan money demand of Kurlat Exercise 11.6 is written in logs
from the start.

## 3.2 Products, ratios and powers

For any differentiable $X_t,Z_t>0$, differentiate $\ln(XZ) = \ln X + \ln Z$ with respect to $t$:

$$\frac{\dot{(XZ)}}{XZ} = \frac{\dot X}{X}+\frac{\dot Z}{Z}
\qquad\Longrightarrow\qquad g_{XZ} = g_X+g_Z \quad\text{(exactly, in continuous time)}$$

$$g_{X/Z} = g_X-g_Z, \qquad g_{X^{a}} = a\,g_X$$

In **discrete** time these hold only approximately, and the error is again second order:

$$(1+g_X)(1+g_Z) = 1+g_X+g_Z+g_Xg_Z
\qquad\Longrightarrow\qquad g_{XZ} = g_X+g_Z+\underbrace{g_Xg_Z}_{\text{cross term}}$$

Two uses that recur:

- **Per capita growth.** $g_{Y/L} \simeq g_Y - g_L$. With $g_Y=3\%$ and $g_L=1\%$, per capita
  growth is 1.98%, not 2.00%. The cross term is $-0.0003$.
- **Growth accounting.** $Y=AK^{\alpha}L^{1-\alpha}$ gives
  $g_Y = g_A + \alpha g_K + (1-\alpha)g_L$ exactly in continuous time. This is the identity
  that session 3 turns into the Solow residual; see [[03_solow_evidencias]].

## 3.3 Compounding, CAGR, and why arithmetic means lie

Iterating $Y_t=Y_{t-1}(1+g)$ from $0$ to $T$:

$$Y_T = Y_0(1+g)^T
\qquad\text{(discrete)},\qquad
Y_t = Y_0e^{\tilde g t}\qquad\text{(continuous)}$$

Given a series, the constant rate that reproduces its endpoints is the **compound annual growth
rate**:

$$\mathrm{CAGR} = \left(\frac{Y_T}{Y_0}\right)^{1/T}-1$$

This is a *geometric* mean of the annual gross factors, and it is the only mean that is
correct, because growth compounds multiplicatively. By the AM–GM inequality,

$$\left(\prod_{t=1}^{T}(1+g_t)\right)^{1/T} \;\le\; \frac{1}{T}\sum_{t=1}^{T}(1+g_t)$$

with equality only if every $g_t$ is identical. So **the arithmetic mean of growth rates always
overstates realised growth**, and the gap widens with volatility. Concretely: $+50\%$ then
$-50\%$ has arithmetic mean $0$ and leaves you with $0.75$ of what you started with; the CAGR
is $-13.4\%$. This is trap 4 in [[01_mensuracao_agregados]], and it is the same convexity that
makes the inequality penalty appear in [[05-beyond-gdp]].

## 3.4 The rule of 70

Set $Y_T/Y_0=2$ and solve:

$$(1+g)^T = 2 \;\Longrightarrow\; T = \frac{\ln 2}{\ln(1+g)} \simeq \frac{0.693}{g}
= \frac{69.3}{100g}$$

so doubling time in years is about $70$ divided by the growth rate in per cent. Seventy rather
than 69.3 because it divides cleanly and because the log approximation error pushes the true
answer slightly up.

| growth | rule of 70 | exact $\ln 2/\ln(1+g)$ |
|---|---|---|
| 1% | 70.0 | 69.7 |
| 2% | 35.0 | 35.0 |
| 5% | 14.0 | 14.2 |
| 7% | 10.0 | 10.2 |
| 10% | 7.0 | 7.3 |

**What it is for.** It converts growth-rate differences into the only currency that matters for
the Solow model: time. A country growing at 2% doubles income per head in 35 years, once a
working lifetime. At 7% it doubles in a decade — three and a half doublings, a factor of eleven,
in the same lifetime. That comparison is the whole motivation for Kurlat ch. 3, and the
"very long run" section (§3.1, p. 47) is the observation that for most of human history the
relevant growth rate was near zero, so doubling time exceeded recorded history.

## 3.5 Reading a log scale, and the trap

Plot $\ln Y_t$ against $t$. Then

$$\frac{d\ln Y}{dt} = \frac{\dot Y}{Y} = \tilde g$$

so **the slope of a log-scale plot is the growth rate**, and a straight line is constant
*proportional* growth — not constant absolute growth. Three readings follow:

1. A straight line on a log plot is exponential growth on a linear plot.
2. Two parallel lines are two economies growing at the same rate; the vertical gap between them
   is the constant log difference, i.e. the constant *ratio* of incomes. Parallel lines mean
   **no convergence**, however close they look.
3. A line that flattens is growth slowing, even while the level keeps rising.

Trap 5 in [[01_mensuracao_agregados]] is the confusion of (2) and (3): a chart on which poor
countries' lines run parallel to rich ones shows a permanent income ratio, and reading it as
"catching up" because the absolute gap in logs looks small is an error. Session 3 turns this
into the formal convergence test; see [[03_solow_evidencias]].

> **Contrast: Romer (2012), ch. 1.** Romer works in continuous time from the first page, so
> every one of the identities in §3.2 holds exactly for him and the cross terms never appear.
> Kurlat works in discrete time, which is closer to data and to the exercises, at the price of
> second-order residuals. The two are reconciled by noting $\tilde g$ *is* Romer's growth rate:
> translate a Kurlat difference equation into Romer's ODE by replacing $g$ with $\ln(1+g)$ and
> the statements coincide. This matters in session 2, where the Solow steady state is derived
> both ways — [[02_crescimento_solow]].

## 3.6 What to be able to do, cold

1. Convert between net rates, gross factors and log rates, and state the error size.
2. Decompose the growth of a product, a ratio and a power.
3. Explain why the CAGR and never the arithmetic mean, and give the AM–GM reason.
4. Use the rule of 70 in both directions.
5. Read levels, rates and convergence off a log-scale chart without confusing them.

Practice: Kurlat ch. 3, Exercises 3.1 and 3.2 (pp. 52–53). Worked in
[[Resolucao/kurlat_solutions_ch1-4|ch1-4]].
