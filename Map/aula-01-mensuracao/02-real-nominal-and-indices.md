---
tags: [aula-01, kurlat-cap-01, indices-de-preco, laspeyres, paasche, fisher, derivacao]
date: 2026-09-17
---

# 2. Real GDP and price indices: Laspeyres, Paasche, Fisher, and the bias proved

**Kurlat §1.2, printed pages 22–25.** Up: [[00-index]] · Prev: [[01-three-approaches]] ·
Next: [[03-growth-arithmetic]]

> **Companion:** [The Index Bench](companion-indices.html) — move the two relative prices and
> watch Laspeyres, Paasche and the Fisher chain separate, with the substitution-bias gap read
> out live. It rebuilds Kurlat's Expandia example by default.

The question this note answers: when prices and quantities both move, by how much did output
*really* grow? There is no answer independent of a weighting choice, and the point of the
section is to show precisely how the choices differ and to sign the difference.

---

## 2.1 The problem, stated exactly

Nominal GDP in year $t$ is

$$Y_t^{\text{nom}} \;=\; \sum_i p_{it}\,q_{it}$$

and it moves for two reasons that we want to separate. Kurlat's Example 1.12 (p. 22) is the
easy case: in Kemalchistan every price doubles and every quantity is unchanged, so nominal
GDP doubles and real GDP is flat. It is easy because two special conditions hold:

1. relative quantities do not change;
2. all prices change by the same factor.

When either fails, the decomposition is not unique. Kurlat's Example 1.13 (Expandia, p. 23)
breaks both: wheat goes from 10 tons at \$50 to 11 tons at \$60, and computers from 1 at
\$1,000 to 2 at \$600. Agriculture grew 10%, manufacturing 100%. What is aggregate growth?

## 2.2 Base-year weighting, and why the base matters

Kurlat's equation (1.2.1): real GDP in year $t$ at base-year prices is

$$Y_t^{(0)} \;=\; \sum_i p_{i0}\,q_{it} \tag{1.2.1}$$

**At 2017 prices.** $11\times 50 + 2\times 1000 = 550 + 2000 = 2550$, against a 2017 nominal
of 1500, so growth is

$$g^{I} = \frac{2550}{1500}-1 = 0.70$$

**At 2018 prices.** Revalue 2017 at 2018 prices: $10\times 60 + 1\times 600 = 600+600=1200$,
against a 2018 nominal of 1860:

$$g^{F} = \frac{1860}{1200}-1 = 0.55$$

Seventy per cent against fifty-five. Same data, same arithmetic, different answer, and the
gap is not small.

### Why the early base gives the larger number — the general result

This is the part Kurlat states in one sentence (p. 24) and does not prove: *"Using an earlier
year as the base year gives a higher rate of growth if the sectors that are expanding most are
those whose relative price is falling."* Here is the proof.

Write the two growth factors as quantity indices:

$$1+g^{I} = \underbrace{\frac{\sum_i p_{i0}q_{i1}}{\sum_i p_{i0}q_{i0}}}_{\text{Laspeyres quantity index } Q^{L}},
\qquad
1+g^{F} = \underbrace{\frac{\sum_i p_{i1}q_{i1}}{\sum_i p_{i1}q_{i0}}}_{\text{Paasche quantity index } Q^{P}}$$

Let $s_{i0} = p_{i0}q_{i0}/\sum_j p_{j0}q_{j0}$ be base-period value shares, and define gross
growth factors $\hat q_i = q_{i1}/q_{i0}$ and $\hat p_i = p_{i1}/p_{i0}$. Then

$$Q^{L} = \sum_i s_{i0}\hat q_i , \qquad
Q^{P} = \frac{\sum_i s_{i0}\,\hat p_i\hat q_i}{\sum_i s_{i0}\,\hat p_i}$$

$Q^{L}$ is the plain share-weighted mean of quantity growth; $Q^{P}$ is the same mean
*reweighted* by price growth. Their difference is therefore a covariance. Writing
$\mathbb{E}_s[\cdot]$ for the $s_{i0}$-weighted mean,

$$Q^{P}-Q^{L}
= \frac{\mathbb{E}_s[\hat p\hat q]-\mathbb{E}_s[\hat p]\,\mathbb{E}_s[\hat q]}{\mathbb{E}_s[\hat p]}
= \frac{\operatorname{Cov}_s(\hat p,\hat q)}{\mathbb{E}_s[\hat p]} \tag{2.1}$$

$$\boxed{\;\operatorname{Cov}_s(\hat p,\hat q) < 0 \iff Q^{P} < Q^{L} \iff g^{F} < g^{I}\;}$$

The denominator is positive, so the sign is the sign of the covariance between price growth
and quantity growth across goods. **Demand curves slope down**, so goods whose relative price
falls are the ones whose relative quantity rises, and that covariance is negative in ordinary
data. Hence the early base gives the larger growth number, as in Expandia: computers got
cheaper *and* more numerous, wheat dearer and barely more plentiful.

Check the Expandia numbers against (2.1). Shares $s_{\text{wheat}}=1/3$,
$s_{\text{comp}}=2/3$; $\hat p = (1.2,\,0.6)$, $\hat q=(1.1,\,2.0)$.
$\mathbb{E}_s[\hat p]=0.8$, $\mathbb{E}_s[\hat q]=1.70$, $\mathbb{E}_s[\hat p\hat q]=1.24$,
so $\operatorname{Cov}_s=1.24-1.36=-0.12$ and $Q^P-Q^L = -0.12/0.8 = -0.15$ — exactly the
$0.55-0.70$ gap. Reproduced in `check_measurement.py`.

## 2.3 The Fisher ideal index and chain weighting

Neither base is defensible, so Kurlat's Alternative 3 (p. 24) takes the geometric mean of
the two growth factors and chains it forward:

$$g_t = \left(1+g^{I}_t\right)^{1/2}\left(1+g^{F}_t\right)^{1/2}-1,
\qquad Y_t = Y_{t-1}\left(1+g_t\right) \tag{2.2}$$

This is the **Fisher ideal quantity index**. Three properties make the geometric mean the
right average here, and none of them holds for the arithmetic mean:

1. **It is bracketed.** $\min(Q^L,Q^P)\le \sqrt{Q^LQ^P}\le\max(Q^L,Q^P)$, so the chained
   growth rate always sits between the two base-year answers. Expandia:
   $\sqrt{1.70\times1.55}-1 = 0.6233$, between $0.55$ and $0.70$.
2. **Time reversal.** Running the index backwards inverts it exactly: the Fisher index from
   $0$ to $1$ is the reciprocal of the Fisher index from $1$ to $0$. Laspeyres and Paasche
   each fail this; reversing them swaps one for the other.
3. **The factor-reversal test.** The Fisher *price* index times the Fisher *quantity* index
   equals the nominal value ratio exactly:

$$P^{F}_{t}\cdot Q^{F}_{t} = \frac{\sum_i p_{i1}q_{i1}}{\sum_i p_{i0}q_{i0}}$$

Proof of 3, since it is the one that earns the name "ideal". With
$P^F=\sqrt{P^LP^P}$ and $Q^F=\sqrt{Q^LQ^P}$, and writing $V=\sum p_{i1}q_{i1}/\sum p_{i0}q_{i0}$:

$$P^{L}Q^{P}=\frac{\sum p_{i1}q_{i0}}{\sum p_{i0}q_{i0}}\cdot\frac{\sum p_{i1}q_{i1}}{\sum p_{i1}q_{i0}}=V,
\qquad
P^{P}Q^{L}=\frac{\sum p_{i1}q_{i1}}{\sum p_{i0}q_{i1}}\cdot\frac{\sum p_{i0}q_{i1}}{\sum p_{i0}q_{i0}}=V$$

so $P^FQ^F=\sqrt{P^LQ^P\cdot P^PQ^L}=\sqrt{V^2}=V$. Each cross-product telescopes because the
mismatched sum cancels. That identity is the reason the deflator implied by a Fisher quantity
index is itself a Fisher price index — the accounts stay internally consistent.

**"Chained" means what it says.** Real GDP at any date is $Y_0$ times a product of one-period
Fisher factors, so the level depends on the whole path, not on one base year. The practical
cost: chained real components do **not** add up to chained real GDP. $C+I+G+X-M$ holds in
nominal terms and only approximately in chained real terms, which is why statistical agencies
publish a "residual" line.

## 2.4 The deflator against the CPI

$$\text{GDP deflator}_t = 100\times\frac{Y^{\text{nom}}_t}{Y^{\text{real}}_t}$$

| | GDP deflator | CPI |
|---|---|---|
| Basket | everything **produced** domestically | a **fixed** consumption basket |
| Weighting | current quantities → **Paasche** | base quantities → **Laspeyres** |
| Imports | excluded (they are not domestic output) | included (consumers buy them) |
| Capital goods | included | excluded |
| Revision | revised as data arrive | essentially never revised |

Two consequences worth stating as results rather than as a list.

**(i) An oil shock moves the two indices in opposite directions in an importer.** Imported oil
is in the CPI and not in the deflator; and an importer's deflator actually *falls* when import
prices rise, because imports enter GDP with a minus sign. Kurlat notes the oil-exporter mirror
case at p. 24. The examinable version: in an oil-importing country a spike in crude raises the
CPI and lowers the deflator.

**(ii) The CPI overstates inflation, by the covariance of (2.1).** A Laspeyres price index is
$P^L=\sum_i s_{i0}\hat p_i$: it holds the basket at its base composition and therefore never
lets the consumer substitute away from what became expensive. Running the argument of §2.2 on
prices rather than quantities,

$$P^{P}-P^{L} = \frac{\operatorname{Cov}_s(\hat q,\hat p)}{\mathbb{E}_s[\hat q]} < 0
\qquad\Longrightarrow\qquad P^{L} > P^{F} > P^{P}$$

so **Laspeyres inflation exceeds Fisher inflation exceeds Paasche inflation** whenever demand
slopes down. That ordering is the *substitution bias*, and it is a theorem, not an empirical
regularity — it needs only $\operatorname{Cov}_s(\hat p,\hat q)<0$.

### Sizing it with CES preferences

Take a CES consumer with elasticity of substitution $\varepsilon$ over two goods, facing a
relative price change. Cost-minimising demand gives $\hat q_i \propto \hat p_i^{-\varepsilon}$
for given real consumption, so

$$\operatorname{Cov}_s(\hat p,\hat q)<0 \text{ for } \varepsilon>0,
\qquad \operatorname{Cov}_s = 0 \text{ iff } \varepsilon = 0 \text{ (Leontief)}$$

With Cobb–Douglas ($\varepsilon=1$) and log price changes $\pi_i$ of variance $\operatorname{Var}_s(\pi)$,
a second-order expansion gives the bias

$$\ln P^{L}-\ln P^{F} \;\simeq\; \tfrac{1}{2}\,\varepsilon\,\operatorname{Var}_s(\pi)$$

so the bias grows with both the willingness to substitute and the **dispersion** of price
changes — not with the average inflation rate. A period of high but uniform inflation carries
little substitution bias; a period of moderate inflation with wildly divergent sectoral prices
carries a lot.

**Empirical anchor.** The Boskin Commission (1996) put total US CPI bias at about 1.1
percentage points a year, of which roughly 0.4 was substitution bias and the rest quality
change and new goods. Those last two are *not* covered by the theorem above: they are failures
of the basket to describe the goods, not failures of the weights.

> **Contrast: Jones (2020), ch. 8.** Jones works entirely with the CPI and does not separate
> Laspeyres from Paasche, which lets him move faster but hides the bias result. Where Jones is
> better is the data: his ch. 2 tables give the US deflator and CPI side by side over decades,
> which makes the wedge in (i) visible rather than hypothetical. Local file, +25 page offset
> ([[books-index]]).

## 2.5 Why this note matters later

The inflation rate that appears in the Fisher equation of [[07_moeda_inflacao]] is computed
from one of these indices. If it is a CPI, it carries a positive bias $b$, so measured real
interest $r^{\text{meas}} = i - \pi^{\text{meas}}$ **understates** the true real rate by $b$.
Indexed government bonds, indexed wages and indexed pensions all inherit it, which is why the
Boskin exercise was a fiscal question and not only a statistical one. The same index question
returns in [[08_adas_microfundamentos]], where the price level $p$ of the AS curve is a
Dixit–Stiglitz CES aggregator — that is, exactly the $\varepsilon$-substitution index above,
with $\varepsilon=\theta$.

## 2.6 What to be able to do, cold

1. Compute real GDP at either base, and say which is larger before computing, using (2.1).
2. State and prove the $P^L > P^F > P^P$ ordering.
3. Build a two-period Fisher chain and verify $P^FQ^F=V$.
4. Say what an oil shock does to the CPI and to the deflator of an importer, with the reason.
5. Name the three components of CPI bias and say which one the substitution theorem covers.

Practice: Kurlat ch. 1, Exercise 1.2 (p. 26) — the four-part price/quantity table; and
Exercise 1.3 on chain weighting. Worked in [[Resolucao/kurlat_solutions_ch1-4|ch1-4]].
