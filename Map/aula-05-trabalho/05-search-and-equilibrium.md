---
tags: [aula-05, kurlat-cap-07, busca, matching, beveridge, seguro-desemprego, derivacao]
date: 2026-09-19
---

# 5. Search: unemployment as a flow equilibrium

**Kurlat §7.5, printed pages 142–150.** Up: [[00-index]] ·
Prev: [[04-dynamic-labour-supply]]

> **Companion:** [Unemployment Is a Flow](companion-flows.html) — the unemployment stock
> settling where the two flows balance, with the Beveridge curve traced as matching efficiency
> and separations move.

The models so far have no unemployment in them: everyone works their chosen hours at the going
wage. This note builds the minimum apparatus that produces unemployment as an equilibrium
object rather than as a failure.

---

## 5.1 The flow accounting

Two states, employed $E$ and unemployed $U$, with a fixed labour force $L=E+U$ normalised to one
so that $u=U/L$ is the unemployment rate.

- **Separation rate $\lambda$:** the fraction of the employed who lose their job each period.
  Flow out of employment: $\lambda E = \lambda(1-u)$.
- **Job-finding rate $f$:** the fraction of the unemployed who find a job each period. Flow out
  of unemployment: $f U = f u$.

The law of motion:

$$u_{t+1}-u_t = \underbrace{\lambda(1-u_t)}_{\text{inflow}}-\underbrace{f u_t}_{\text{outflow}}$$

**Steady state.** Set the change to zero:

$$\lambda(1-u^*) = f u^*
\;\Longrightarrow\;
\lambda = u^*(\lambda+f)
\;\Longrightarrow\;
\boxed{\;u^* = \frac{\lambda}{\lambda+f}\;}$$

**Stability.** The map is $u_{t+1}=u_t+\lambda-(\lambda+f)u_t = \lambda+\left[1-(\lambda+f)\right]u_t$,
a linear difference equation with slope $1-(\lambda+f)$. Since $\lambda+f\in(0,2)$ for sensible
rates, $|1-(\lambda+f)|<1$ and the steady state is globally stable, with deviations decaying at
rate $\lambda+f$ per period. Verified in `check_labour.py` against a simulated path.

**Half-life.** Deviations decay with half-life $\ln 2/(\lambda+f)$. With monthly US values
$\lambda\simeq0.034$ and $f\simeq0.43$, that is $\ln2/0.464\simeq1.5$ months — the unemployment
rate reverts to its flow-implied level very fast. So persistent high unemployment means
persistently changed **flows**, not slow adjustment of the stock.

## 5.2 What the formula says

**It depends only on the ratio.** Write $u^*=\dfrac{1}{1+f/\lambda}$. Only $f/\lambda$ matters.

**Average duration of an unemployment spell is $1/f$.** If the exit probability each month is
$f$, the expected number of months to exit is $1/f$. So:

$$u^* = \frac{\lambda}{\lambda+f} = \frac{\lambda\cdot(1/f)}{1+\lambda/f}\approx \lambda\times\text{duration}
\quad\text{for small }\lambda/f$$

**Unemployment is the separation rate times the duration of a spell.** That decomposition is the
most useful thing in this note, because the two factors are separately measurable and separately
meaningful.

**The US–Europe comparison, made precise.** Take two economies with the same $u^*=8\%$:

| | $\lambda$ (monthly) | $f$ (monthly) | duration $1/f$ |
|---|---|---|---|
| "US-style" | 0.035 | 0.40 | 2.5 months |
| "Europe-style" | 0.009 | 0.10 | 10 months |

Identical unemployment rates; a completely different experience. In the first, many people are
briefly unemployed; in the second, few people are unemployed for a long time. Long-term
unemployment carries skill depreciation, detachment and much larger welfare costs — so the same
headline number describes two different social problems. This is the point flagged in
[[01-measurement]] §1.3, now with the algebra behind it. Both rows are computed in
`check_labour.py`.

**Corollary for policy.** A policy that reduces separations ($\lambda\downarrow$) and one that
raises finding ($f\uparrow$) both reduce $u^*$, but the first raises duration for those who do
become unemployed while the second cuts it. Employment protection legislation does the first;
active labour market policy aims at the second.

## 5.3 The matching function

Where does $f$ come from? Hiring requires an unemployed worker and a vacancy to find each other,
which takes time and resources. Model it with a **matching function**:

$$M = A_m\,U^{\xi}V^{1-\xi}, \qquad \xi\in(0,1)$$

with $A_m$ matching efficiency. It is Cobb–Douglas and CRS by the same convenience and for the
same reasons as the production function of [[02-ingredients]] — and note the conceptual move:
matching is treated as a *production process* whose inputs are searchers and vacancies.

Define **market tightness** $\theta\equiv V/U$ — vacancies per unemployed worker. Then

$$f = \frac{M}{U}=A_m\left(\frac{V}{U}\right)^{1-\xi}=A_m\theta^{1-\xi},
\qquad
q = \frac{M}{V}=A_m\theta^{-\xi}$$

where $q$ is the rate at which a **vacancy** is filled. Two immediate properties:

- $f$ is **increasing** in tightness: when vacancies are plentiful relative to searchers,
  workers find jobs fast.
- $q$ is **decreasing** in tightness: the same conditions make it hard for firms to fill posts.

**This is a congestion externality and it is the reason the model is not trivial.** One more
unemployed worker makes it easier for firms to hire (raising $q$) and harder for other workers
to find work (lowering $f$). Neither effect is internalised by the searcher, so the
decentralised outcome is not generally efficient — the Hosios condition states exactly when it
is, and that is beyond this course.

### The Beveridge curve, derived

Combine the steady-state condition with the matching function:

$$u^* = \frac{\lambda}{\lambda+A_m\theta^{1-\xi}}, \qquad \theta=\frac{v}{u}$$

Substituting $\theta=v/u$ and rearranging gives a **downward-sloping** relation between $v$ and
$u$: higher vacancies raise tightness, raise $f$, and lower $u$. That is the Beveridge curve of
[[01-measurement]] §1.4, now derived rather than observed.

And the shift result: an **outward** shift — more $u$ at the same $v$ — requires $\lambda$ up or
$A_m$ down. So a Beveridge curve that moves out is diagnostic of *either* more churn *or* worse
matching, and distinguishing the two requires separation data. Verified numerically.

## 5.4 Reservation wages in search

The unemployed worker receives job offers drawn from a wage distribution $F(w)$ and must decide
whether to accept. With unemployment benefit $b$ per period, discount factor $\beta$, and jobs
that last forever once taken, the value of unemployment $V^U$ and of employment $V^E(w)$ satisfy

$$V^{E}(w) = \frac{w}{1-\beta}, \qquad
V^{U} = b+\beta\,\mathbb{E}\!\left[\max\left\{V^{E}(w'),\,V^{U}\right\}\right]$$

The worker accepts iff $V^{E}(w)\ge V^{U}$, and since $V^{E}$ is strictly increasing in $w$
there is a **reservation wage** $w^{r}$ defined by

$$\boxed{\;\frac{w^{r}}{1-\beta} = V^{U}\;}$$

Accept any offer above it, reject any below. Note that this is a *different* reservation wage
from the participation threshold of [[02-static-model]] §2.6: that one compares work with
leisure, this one compares accepting now with waiting for a better offer. Both are corner
conditions, and they are often confused.

**Comparative statics, all examinable:**

- $b\uparrow$ raises $V^{U}$, hence raises $w^{r}$: **more generous unemployment insurance makes
  workers choosier**, so they reject more offers, $f$ falls, and by §5.1 both duration and $u^*$
  rise.
- Greater **dispersion** of the wage offer distribution raises $w^{r}$: the option value of
  continuing to search is higher when there is more to gain from a lucky draw.
- $\beta\uparrow$ (more patience) raises $w^{r}$.

## 5.5 Unemployment insurance: the trade-off, stated properly

The naive reading of §5.4 is that unemployment insurance is bad because it raises unemployment.
The model says something more careful, and this is the examinable version.

**The cost.** Higher $b$ raises $w^r$, lowers $f$, raises duration and raises $u^*$. This is a
real distortion — a **moral hazard** effect, and it is measured: the elasticity of unemployment
duration with respect to benefit generosity is around 0.5 in the empirical literature.

**Three benefits, all in the model.**

1. **Insurance.** Job loss is a large uninsurable risk, and by the concavity of
   [[02-two-period-problem]] §2.1 a risk-averse worker values smoothing consumption across it
   highly. This is the Baily–Chetty logic: the optimal replacement rate balances the moral hazard
   elasticity against the consumption drop at job loss.
2. **Match quality.** A worker who can afford to reject a bad offer takes a better job.
   Higher $w^r$ means higher accepted wages and potentially longer, more productive matches. The
   empirical evidence here is mixed but the mechanism is in the model.
3. **Liquidity rather than moral hazard.** Part of the duration response is a *liquidity* effect
   — a constrained household ([[05-ricardian-and-constraints]] §5.3) takes the first offer because
   it cannot afford to search, not because search is unattractive. Benefits relax that constraint,
   and that portion of the response is efficient rather than distortionary.

**The conclusion to write:** the optimal level of unemployment insurance is interior, not zero,
and the model identifies exactly which elasticity has to be measured to find it.

## 5.6 What search adds that §7.2–§7.4 could not

| Question | Static / dynamic supply | Search |
|---|---|---|
| Why is anyone unemployed? | nobody is | matching takes time |
| Why do spells have duration? | no concept of it | $1/f$ |
| What does a recession do? | hours fall voluntarily | $\lambda$ rises and $f$ falls |
| Is unemployment inefficient? | question does not arise | yes, through congestion externalities |
| Does the wage clear the market? | yes, by construction | no — matches are bilateral |

The last row is the deepest difference. In the competitive model a wage clears the labour market
instantly. Once matching is bilateral and takes time, there is a *surplus* to be split in each
match, no single market-clearing wage, and the division is a bargaining problem — which is where
the full Diamond–Mortensen–Pissarides model goes, and where this course stops.

## 5.7 What to be able to do, cold

1. Write the law of motion, derive $u^*=\lambda/(\lambda+f)$ and prove it is globally stable.
2. Decompose unemployment into separation rate times duration, and use it on a US–Europe
   comparison.
3. Define the matching function and tightness, derive $f$ and $q$, and say why the externality
   matters.
4. Derive the Beveridge curve from the steady state and the matching function, and say what a
   shift means.
5. Define the search reservation wage, distinguish it from the participation reservation wage,
   and sign the effect of $b$ on $w^r$, $f$, duration and $u^*$.
6. State the unemployment-insurance trade-off with all three benefits, not just the cost.

Practice: Kurlat ch. 7, Exercises 7.7 *The Beveridge Curve* (p. 150) and 7.8 (p. 150). Worked in
[[Resolucao/lista4_resolucao|lista 4]] — the Kurlat ch. 7 solution set has not been written yet; the code lives in `Resolucao/kurlat_ch07_codigo/`.
