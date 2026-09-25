---
tags: [aula-01, kurlat-cap-02, idh, jones-klenow, bem-estar, desigualdade, derivacao]
date: 2026-09-17
---

# 5. Beyond GDP: the HDI, and the Jones–Klenow welfare measure decomposed

**Kurlat §2.1–§2.2, printed pages 31–44.** Up: [[00-index]] ·
Prev: [[04-cross-country-and-ppp]]

> **Companion:** [What Rawls Would Pay](companion-welfare.html) — set consumption, leisure,
> life expectancy and inequality for a country and watch $\lambda$ decompose into its four
> additive log terms, with $\sigma$ on a slider so the inequality penalty can be seen scaling.

Two measures, built on opposite principles. The HDI picks three things that seem to matter and
averages indices of them. Jones and Klenow write down a utility function and ask what compensating
consumption would make a person indifferent. The second is the one worth deriving, because its
decomposition is a genuinely graduate-level result and because every term in it is an object from
later sessions.

---

## 5.1 The HDI, and why its arbitrariness is structural

Three sub-indices, each engineered onto $[0,1]$ by a min–max rescaling (Kurlat, p. 32):

$$I_{\text{life}} = \frac{\text{Life expectancy}-20}{85-20}$$

$$I_{\text{educ}} = \frac{1}{2}\left[\frac{\text{Mean years of schooling, 25-year-olds}}{15}
+ \frac{\text{Expected years of schooling, 5-year-olds}}{18}\right]$$

$$I_{\text{inc}} = \frac{\ln(\text{GNI per capita}) - \ln(100)}{\ln(75{,}000)-\ln(100)}$$

and the index is their geometric mean:

$$\mathrm{HDI} = \left(I_{\text{life}}\,I_{\text{educ}}\,I_{\text{inc}}\right)^{1/3}$$

**Three design choices, each defensible and none derived.**

*The log on income and not on the others.* This is the one choice with an economic argument
behind it: $\ln$ imposes diminishing returns, so a \$1,000 rise matters more at \$2,000 than at
\$60,000. The others are linear, which asserts that a year of life expectancy is worth the same
at 45 as at 80.

*The geometric mean, not arithmetic.* This is not cosmetic. Take logs:

$$\ln \mathrm{HDI} = \tfrac{1}{3}\left(\ln I_{\text{life}}+\ln I_{\text{educ}}+\ln I_{\text{inc}}\right)$$

so the sub-indices are **complements**: the marginal contribution of income rises when health is
high, and any sub-index at zero sends the HDI to zero. An arithmetic mean would make them perfect
substitutes and let a rich, short-lived country buy its way to a high score. The UN switched from
arithmetic to geometric in 2010 for exactly this reason.

*The caps.* GNI is capped at \$75,000, life expectancy at 85. Kurlat's footnote 1 (p. 32) records
the consequence honestly: some countries' GNI exceeds the cap, so their income index is above one.
The bound is a convention, not a fact.

**Why GNI and not GDP.** Because the question is what residents *have*, not what is produced on the
territory — the distinction derived in [[01-three-approaches]] §1.4.

**The empirical punchline.** Kurlat's Figure 2.1.1 (p. 32): the correlation between HDI and GDP per
capita is **0.94**. The index that was built to correct GDP mostly reproduces it. That is not a
failure — it is evidence that income, health and schooling move together across countries — but it
means the HDI adds little information beyond ranking, and it motivates a measure built on theory
rather than on a committee's list. Which is §2.2.

## 5.2 Jones–Klenow: the thought experiment

Kurlat §2.2 (p. 33). Take a random person — Jones and Klenow call him Rawls — behind a **veil of
ignorance**: he will live a year in a country without knowing who in it he will be. Offer him two
options:

- country *Utilia*, whose living standards we want to measure;
- the United States, with everyone's consumption multiplied by $\lambda$.

**Definition.** $\lambda$ is the factor that makes him indifferent. It is an *equivalent variation*,
and it is the welfare measure:

$$u\!\left(\lambda c^{\text{US}}, l^{\text{US}}, a^{\text{US}}\right)
= u\!\left(c^{\text{Utilia}}, l^{\text{Utilia}}, a^{\text{Utilia}}\right) \tag{2.2.2}$$

The utility function, Kurlat's (2.2.1):

$$u(c,l,a) = \mathbb{E}\left[\left(\bar u + \frac{c^{1-\sigma}}{1-\sigma}-\theta(1-l)^2\right)a\right] \tag{2.2.1}$$

with $c$ consumption (random, because he does not know his place in the distribution), $l$ the
leisure share of time, and $a\in\{0,1\}$ an indicator for being alive. Behind the veil he averages
over the $N$ residents:

$$u = \frac{1}{N}\sum_{n=1}^{N}\left(\bar u + \frac{c_n^{1-\sigma}}{1-\sigma}-\theta(1-l)^2\right)a \tag{2.2.3}$$

Four modelling commitments, each of which does work:

1. **Consumption, not output.** Investment and exports do not enter Rawls's year; imports do. So
   the object is $C+G$, not $Y$ — Kurlat's footnote 3 (p. 34) records the assumption that public and
   private consumption give equal utility on average.
2. **$a$ multiplies everything.** The dead get zero, so life expectancy enters as a probability
   weight on the whole bracket, and $\bar u$ — the flow value of being alive at zero consumption —
   becomes a parameter that *must* be pinned down, since it scales how much mortality matters.
3. **$\theta(1-l)^2$** prices work as a convex disutility, so non-market time is valued. This is the
   answer to the Kurlat Example 1.11 problem from [[01-three-approaches]] §1.3(d).
4. **$\sigma$ does double duty.** It is risk aversion behind the veil, and mechanically it becomes
   aversion to inequality, because a spread-out consumption distribution *is* risk from behind the
   veil. That equivalence is the cleverest move in the paper and §5.4 makes it exact.

## 5.3 Risk aversion, concavity, and the warning

Rawls is risk averse if a certain average is preferred to the gamble:

$$u\!\left(\frac{c_{\text{rich}}+c_{\text{poor}}}{2}\right) > \frac{u(c_{\text{rich}})+u(c_{\text{poor}})}{2} \tag{2.2.4}$$

and in general

$$u(\mathbb{E}[c]) > \mathbb{E}[u(c)] \tag{2.2.5}$$

which is **Jensen's inequality**, holding for any strictly concave $u$. Marginal utility is
$u'(c)=c^{-\sigma}$ (2.2.6), positive and decreasing for all $\sigma>0$, and decreasing faster the
larger $\sigma$ is. Two conventions to have straight: at $\sigma=1$ the function
$c^{1-\sigma}/(1-\sigma)$ is undefined but its limit behaviour is $\ln c$ (Kurlat's footnote 6), and
for $\sigma>1$ the level of utility is negative, which means nothing because only comparisons are
interpretable.

> **Kurlat's methodological warning, worth repeating verbatim (p. 35).** *"It's wrong to say people
> dislike risk because their utility function is concave. Instead, one should say: in economic
> models, we describe people's preferences with concave utility functions to capture the fact that
> people dislike risk. Do not put the mathematical cart before the conceptual horse!"* The same
> discipline applies to every functional form in this course — the CRRA of
> [[04_consumo_poupanca]], the Frisch disutility of [[05_trabalho_lazer]], the Dixit–Stiglitz
> aggregator of [[08_adas_microfundamentos]].

**Calibrating $\sigma$.** Estimates run from about 1 to about 10, from portfolio choice (Friend and
Blume, 1975) and from insurance purchases (Szpiro, 1986). Jones and Klenow use $\sigma=1$, at the
low-risk-aversion end — a *conservative* choice, because it minimises the inequality penalty and
therefore understates how much inequality costs.

## 5.4 The decomposition — the result worth knowing

Take $\sigma=1$, so $u = \bar u + \ln c - \theta(1-l)^2$ conditional on being alive, and let $e$ be
the fraction of the age range over which Rawls is alive (Kurlat's construction: age uniform on
$[0,100]$, alive if age is below life expectancy, so $e = \text{LE}/100$). Then

$$u^{j} = e^{j}\left[\bar u + \mathbb{E}\left[\ln c^{j}\right] - \theta\left(1-l^{j}\right)^2\right]$$

Set $u^{\text{US}}(\lambda) = u^{j}$. Scaling US consumption by $\lambda$ adds $\ln\lambda$ inside
the expectation:

$$e^{\text{US}}\left[\bar u + \ln\lambda + \mathbb{E}\ln c^{\text{US}} - \theta(1-l^{\text{US}})^2\right]
= e^{j}\left[\bar u + \mathbb{E}\ln c^{j} - \theta(1-l^{j})^2\right]$$

Now suppose consumption is **lognormal** within each country, $\ln c \sim \mathcal N(\mu,s^2)$, so
that

$$\mathbb{E}\left[\ln c\right] = \ln \mathbb{E}[c] - \tfrac{1}{2}s^2$$

— the mean of the log is the log of the mean minus half the log variance, which is Jensen's
inequality made quantitative. Substituting and solving for $\ln\lambda$, with
$\bar c^{j}=\mathbb{E}[c^{j}]$:

$$\boxed{\;
\ln\lambda \;=\;
\underbrace{\ln\frac{\bar c^{\,j}}{\bar c^{\,\text{US}}}}_{\text{(1) consumption}}
\;-\;\underbrace{\tfrac{1}{2}\left(s_j^2-s_{\text{US}}^2\right)}_{\text{(2) inequality}}
\;-\;\underbrace{\theta\left[(1-l^{j})^2-(1-l^{\text{US}})^2\right]}_{\text{(3) leisure}}
\;+\;\underbrace{\frac{e^{j}-e^{\text{US}}}{e^{\text{US}}}\left[\bar u + \mathbb{E}\ln c^{j}-\theta(1-l^j)^2\right]}_{\text{(4) life expectancy}}
\;}$$

to first order in the mortality difference. **Four additive terms in logs.** Read them:

1. **Consumption.** The only term GDP per capita comes close to capturing, and even here it is
   $C+G$ and not $Y$, so a high-investment country scores below its GDP rank in the one-year
   experiment.
2. **Inequality, priced at exactly half the log variance.** With $\sigma\ne1$ the penalty is
   $-\tfrac{\sigma}{2}s^2$, so it scales linearly in risk aversion. This is the same convexity that
   made the arithmetic mean overstate growth in [[03-growth-arithmetic]] §3.3 — Jensen's inequality
   appearing twice in one session, in two different costumes.
3. **Leisure.** Convex in hours worked, so the marginal hour of work costs more the more you already
   work. This is what makes the France–US comparison of [[04-cross-country-and-ppp]] §4.4 a welfare
   question rather than a productivity question.
4. **Life expectancy**, weighted by the *flow value of a year of life*, which is
   $\bar u$ plus the year's flow utility. This term is empirically the largest single source of
   disagreement with GDP, and it is entirely at the mercy of $\bar u$ — a parameter with no market
   price, recovered from value-of-statistical-life estimates.

**The headline findings.** Western Europe looks considerably better than its GDP suggests — longer
lives, more leisure, less inequality — with $\lambda$ often 20–35% above the GDP ratio. Poor
countries look *worse* than their PPP GDP suggests, because shorter lives and higher inequality
compound the consumption gap. And the cross-country correlation of $\ln\lambda$ with
$\ln(\text{GDP per capita})$ is around 0.95 — the same lesson as the HDI's 0.94, reached from
theory rather than from a list.

## 5.5 Inequality measurement, briefly

The $s^2$ in term (2) is one inequality statistic among several, and the course's vocabulary is:

- **Lorenz curve.** Cumulative income share against cumulative population share, both sorted
  ascending. The 45° line is perfect equality.
- **Gini.** Twice the area between the Lorenz curve and the 45° line; $0$ at equality, $1$ at
  complete concentration. For a lognormal distribution it maps to the log standard deviation
  exactly: $G = 2\Phi(s/\sqrt2)-1$, so $s=0.5\Rightarrow G\simeq0.28$ and $s=1.0\Rightarrow G\simeq0.52$.
  That identity is what lets term (2) be computed from published Gini coefficients.
- **Why the variance of logs and not the Gini in the formula.** Because it is the statistic the
  log utility function actually produces. The Gini enters only as a way to recover $s$.

## 5.6 What to be able to do, cold

1. Write the three HDI sub-indices and say why the aggregation is geometric.
2. State the Kennedy critique (p. 31) and map each item in it to a term in the Jones–Klenow
   function or to a gap that neither measure fixes.
3. Set up (2.2.2) and derive the four-term decomposition with log utility and lognormal
   consumption, showing where the $-\tfrac12 s^2$ comes from.
4. Say how the decomposition changes for general $\sigma$, and which term is most sensitive to
   an unobservable parameter.
5. Explain why both measures correlate around 0.95 with GDP per capita, and why that is
   informative rather than disappointing.

Practice: Kurlat ch. 2, Exercises 2.1–2.4 (pp. 42–43) on the HDI; Exercise 2.10 (p. 44) on the
Rawlsian difference principle as a limit of extreme risk aversion — the cleanest link between
§5.3 and political philosophy. Worked in [[Resolucao/kurlat_solutions_ch1-4|ch1-4]].
