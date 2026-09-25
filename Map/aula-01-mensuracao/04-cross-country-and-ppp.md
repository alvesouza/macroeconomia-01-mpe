---
tags: [aula-01, kurlat-cap-01, ppp, balassa-samuelson, comparacoes-internacionais, derivacao]
date: 2026-09-17
---

# 4. Comparing countries: PPP, and Balassa–Samuelson derived

**Kurlat §1.2, printed pages 25–27.** Up: [[00-index]] ·
Prev: [[03-growth-arithmetic]] · Next: [[05-beyond-gdp]]

> **Companion:** [Two Countries, Two Baskets](companion-ppp.html) — set relative productivity
> in tradables and non-tradables and watch the market exchange rate, the PPP rate and the
> measured income ratio separate. The Balassa–Samuelson prediction is drawn as the line the
> data should sit on.

The section makes one measurement point and raises one theoretical question it does not answer.
The measurement point is that market exchange rates are the wrong converter. The question is
*why* they are systematically wrong in one direction, and that is Balassa–Samuelson, derived
here in full because it is the reason the correction is large and predictable rather than noise.

---

## 4.1 The problem

Kurlat's Example 1.14 (p. 25): US GDP is \$20.5tn with 327m people; Mexican GDP is 23.5tn pesos
with 127m people. Per capita: \$62,700 and 185,000 pesos. The numbers are not comparable
because the units differ.

**Market-rate conversion.** At 19 pesos to the dollar, Mexican GDP per capita is
$185{,}000/19 \simeq \$9{,}700$, so measured US income is 6.5 times Mexican income.

**The objection.** A dollar converted into pesos buys more in Mexico than it buys in the US.
Low measured GDP at market rates may mean low output, or it may mean low prices. The
conversion cannot tell the two apart.

## 4.2 The PPP construction

Value the foreign country's quantities at *US* prices:

$$\mathrm{GDP}^{\text{PPP}}_{\text{foreign}} \;=\; \sum_{i=1}^{N} p^{\text{US}}_i\, q^{\,i}_{\text{foreign}}$$

This is the base-year index of [[02-real-nominal-and-indices]] with "base year" replaced by
"base country": exactly Laspeyres-in-space if the US basket is the reference. It inherits the
same weighting ambiguity — valuing at Mexican prices instead gives a different answer, and the
Penn World Table's multilateral (Geary–Khamis, and now Gini–Éltetö–Köves–Szulc) methods exist
precisely to impose transitivity across many countries at once, so that the US–Mexico ratio
does not depend on whether you route the comparison through Canada.

At PPP, Mexican GDP per capita is about \$18,000, roughly twice the market-rate figure. So the
true income ratio is about 3.5, not 6.5. **Nearly half of the measured income gap between the
US and Mexico at market rates is a price-level difference, not an output difference.**

### The PPP exchange rate, defined

Kurlat defines it as the rate that would reconcile the two conversions:

$$e^{\text{PPP}} \;\equiv\; \frac{\mathrm{GDP}^{\text{PPP}} \text{ (in dollars)}}{\mathrm{GDP}\text{ (in local currency)}}$$

Define the **price level of the country relative to the US** as the ratio of the market rate to
the PPP rate:

$$\mathcal{P} \;\equiv\; \frac{e^{\text{PPP}}}{e^{\text{market}}}$$

$\mathcal{P}<1$ means goods are cheaper there than in the US. For Mexico,
$e^{\text{market}} = 1/19 = 0.0526$ dollars per peso and $e^{\text{PPP}} = 18{,}000/185{,}000
= 0.0973$, so $\mathcal{P} = 0.54$: the Mexican price level is a little over half the US level.

**The Big Mac index** is the same construction with $N=1$:

$$e^{\text{BigMac}} = \frac{\text{price of a Big Mac in the US (dollars)}}
{\text{price of a Big Mac abroad (local currency)}}$$

Its virtue is that the good is standardised; its defect, as Kurlat's footnote 2 says, is that
the price includes the restaurant's location, rent and wages — which are exactly the
non-tradable components that the next section shows are the source of the whole phenomenon. So
the Big Mac index is not a flawed measure of tradable-goods parity: it is an unintentionally
good measure of the overall price level, for the same reason.

## 4.3 Why poor countries are cheap: Balassa–Samuelson, derived

The empirical regularity is not that prices are randomly different. It is that $\mathcal{P}$
rises monotonically with income per head. Here is the model that produces it.

**Setup.** Two sectors, tradables $T$ and non-tradables $N$, one mobile factor (labour), linear
technology:

$$Y_T = A_T L_T, \qquad Y_N = A_N L_N$$

**Assumption 1 (law of one price in tradables).** Tradables are arbitraged, so their price is
the same everywhere once converted at the market rate. Normalise the world tradable price to
one and measure everything in that unit: $P_T = 1$ in every country.

**Assumption 2 (labour mobility across sectors).** Competitive firms pay the value of the
marginal product, and workers move until wages are equalised:

$$W = P_T A_T = P_N A_N$$

**Step 1 — the relative price of non-tradables.** Divide:

$$\boxed{\;\frac{P_N}{P_T} = \frac{A_T}{A_N}\;} \tag{4.1}$$

This is the whole mechanism in one line, and notice what it does *not* contain: no preferences,
no demand, no capital. The relative price of non-tradables is a pure technology ratio. A country
that is very productive at making tradables must pay high wages in tradables; those wages are
paid to haircutters and bus drivers too, whose productivity has not risen; so haircuts are
expensive there.

**Step 2 — the aggregate price level.** Let consumption be Cobb–Douglas with a share
$\gamma$ on non-tradables. The consumer price index is the geometric average

$$P = P_T^{1-\gamma}P_N^{\gamma} = \left(\frac{P_N}{P_T}\right)^{\gamma}
= \left(\frac{A_T}{A_N}\right)^{\gamma} \tag{4.2}$$

using $P_T=1$. Taking logs, the price level of country $j$ relative to the US:

$$\ln \mathcal{P}_j = \gamma\left[\left(\ln A_{T,j}-\ln A_{T,\text{US}}\right)
-\left(\ln A_{N,j}-\ln A_{N,\text{US}}\right)\right] \tag{4.3}$$

**Step 3 — the empirical prediction.** The productivity gap between rich and poor countries is
much larger in tradables (manufacturing, agriculture with modern inputs) than in non-tradables
(haircuts, domestic service, construction). Formally, assume
$\ln A_{T,j}-\ln A_{T,\text{US}} < \ln A_{N,j}-\ln A_{N,\text{US}} < 0$ for a poor country $j$.
Then the bracket in (4.3) is negative, so $\mathcal{P}_j<1$:

$$\boxed{\;\text{poorer country} \;\Longrightarrow\; \text{lower price level}
\;\Longrightarrow\; \text{market-rate GDP understates real GDP}\;}$$

and the understatement is *larger* the poorer the country. That is why the PPP correction
raised Mexico by a factor of about 1.9 and would raise India by more.

**Step 4 — the sign of the bias in growth comparisons.** Differentiating (4.3) along a growth
path, a country whose tradable productivity is catching up fast experiences **real exchange
rate appreciation** — its price level rises toward the US level. So a fast-growing economy's
GDP measured at market rates grows faster than its GDP at constant PPP, because part of the
market-rate growth is the price level catching up, not output. This is a standard source of
overstated growth figures for China in the 2000s.

### Two things the derivation shows that the slogan does not

1. **It is about the *ratio* of sectoral productivities, not about being poor.** A country that
   is uniformly unproductive in both sectors has $A_T/A_N$ unchanged and no price-level effect
   at all, however poor it is. Poverty per se predicts nothing; asymmetric productivity does.
2. **$\gamma$ scales it.** A country whose consumption basket is mostly tradable goods shows
   little effect. This is why the PPP correction is smaller for small open economies with high
   import shares than for large continental ones at the same income.

## 4.4 Which denominator: three different "per" measures

$$\underbrace{\frac{Y}{\text{Population}}}_{\text{living standards}}
\;\ne\;
\underbrace{\frac{Y}{\text{Employment}}}_{\text{productivity per worker}}
\;\ne\;
\underbrace{\frac{Y}{\text{Hours}}}_{\text{productivity per hour}}$$

They are linked by an identity worth memorising, because session 5 takes it apart:

$$\frac{Y}{\text{Pop}} = \underbrace{\frac{Y}{H}}_{\text{output per hour}}
\times \underbrace{\frac{H}{E}}_{\text{hours per worker}}
\times \underbrace{\frac{E}{\text{Pop}}}_{\text{employment rate}}$$

The classic application: France's output **per hour** is close to the US level, while its output
**per person** is roughly 25–30% lower. The whole gap is in the last two factors — shorter hours
and lower participation. Whether that is a welfare loss or a preference for leisure is exactly
the question [[05-beyond-gdp]] prices and that [[05_trabalho_lazer]] models. Getting the
denominator wrong turns a statement about leisure into a false statement about productivity.

## 4.5 Sources, and their disagreements

| Source | Builds | Caution |
|---|---|---|
| **Penn World Table** | multilateral PPP, real GDP at constant prices, capital stocks, hours | versions differ materially; always cite the version number |
| World Bank / ICP | the PPP benchmark rounds themselves | benchmark years are revised; the 2011 and 2017 rounds moved China's level noticeably |
| Maddison Project | very long-run historical series | pre-1900 numbers are reconstructions, not measurements |

Kurlat uses PWT; Jones (2020) uses it too, which is why their growth facts agree. Sessions 2
and 3 quote PWT-based numbers throughout — see [[02_crescimento_solow]].

## 4.6 What to be able to do, cold

1. Convert GDP at market rates and at PPP and say which is larger for a poor country, and why.
2. Define the PPP exchange rate and the relative price level, and compute both from data.
3. Derive (4.1) from wage equalisation and the law of one price, in three lines.
4. Give the two conditions under which Balassa–Samuelson predicts *no* price-level gap.
5. Decompose output per person into the three factors and use it on the France–US comparison.

Practice: Kurlat ch. 1, Exercise 1.4 (p. 27) on PPP and market rates; Exercise 1.5 on the
Big Mac index. Worked in [[Resolucao/kurlat_solutions_ch1-4|ch1-4]].
