---
tags: [aula-07, kurlat-cap-11, senhoriagem, imposto-inflacionario, cagan, laffer, custos-da-inflacao]
date: 2026-09-19
---

# 4. Seigniorage, the inflation Laffer curve, and the costs of inflation

**Kurlat §11.3–§11.4, printed pages 215–222.** Up: [[00-index]] ·
Prev: [[03-equilibrium-and-neutrality]]

> **Companion:** [The Inflation Tax](companion-seigniorage.html) — revenue as rate times base,
> with the base eroding faster than the rate rises past the peak.

Printing money is a way of raising revenue, and like every tax it has a base that shrinks when
the rate rises. This note derives where the peak is, and then sorts the costs of inflation by the
one criterion that matters: whether they require the inflation to be a *surprise*.

---

## 4.1 Seigniorage and the inflation tax

**Seigniorage** is the real revenue from creating money:

$$S = \frac{\dot M}{P} = \frac{\dot M}{M}\cdot\frac{M}{P} = \mu_M\cdot\frac{M}{P}$$

In a steady state with constant real balances and $\pi=\mu_M$ (from
[[03-equilibrium-and-neutrality]] §3.4, with $g_Y=0$):

$$\boxed{\;S = \underbrace{\pi}_{\text{the tax rate}}\times\underbrace{\frac{M}{P}}_{\text{the tax base}}\;}$$

**This is a tax**, and naming its parts correctly is most of the work:

- **Who pays:** holders of money, through the erosion of the real value of their balances.
- **The rate:** the inflation rate, since that is the proportional loss per period.
- **The base:** real money balances.
- **Why it is collected without legislation:** it requires no vote, no collection apparatus and
  no compliance. That is why it is the revenue source of last resort for states that have lost
  access to ordinary taxation and to borrowing — which is the standard empirical account of
  hyperinflations.

**The distinction worth a sentence.** *Seigniorage* is the flow revenue from new money creation.
The *inflation tax* is the erosion of existing balances. In a steady state they coincide; out of
steady state they do not, because real balances are changing.

## 4.2 Cagan money demand and the Laffer peak

To find the revenue-maximising inflation rate, the base has to respond to the rate. Cagan (1956)
proposed the semi-log form, which is the standard tool for high inflation:

$$\frac{M}{P} = L\,e^{-a\pi}, \qquad a>0$$

$a$ is the **semi-elasticity**: a one-point rise in inflation cuts real balances by $a$ per cent.
Note this is a semi-elasticity, not an elasticity — the log of balances is linear in the *level*
of inflation, which is what makes it tractable at rates where ordinary elasticities break down.

**Seigniorage as a function of the rate:**

$$S(\pi) = \pi\,L\,e^{-a\pi}$$

Maximise:

$$\frac{dS}{d\pi} = L\,e^{-a\pi}\left(1-a\pi\right) = 0
\qquad\Longrightarrow\qquad
\boxed{\;\pi^{\max} = \frac{1}{a}\;}$$

Second-order condition: $S''(\pi^{\max}) = -aLe^{-1}<0$, a maximum. And the revenue at the peak is

$$S(\pi^{\max}) = \frac{L}{a}e^{-1} \simeq \frac{0.368\,L}{a}$$

Both verified analytically and by numerical maximisation in `check_money.py`.

**Reading the condition.** At the peak, the elasticity of the base with respect to the rate is
exactly $-1$: $\dfrac{d\ln(M/P)}{d\ln\pi} = -a\pi = -1$. That is the general Laffer condition and
it is worth stating in that form, because it is the same condition for any tax.

**Below the peak**, raising inflation raises revenue: the rate effect dominates. **Above it**,
raising inflation *lowers* revenue, because people flee money faster than the rate rises. This is
trap 6 in [[07_moeda_inflacao]] — concluding that more inflation always raises more revenue.

**The dynamic trap that produces hyperinflation.** A government needing revenue above $S(1/a)$
cannot get it at any inflation rate. If it keeps raising money growth anyway, the public keeps
economising on balances, the base keeps shrinking, revenue keeps falling, and the government
raises money growth further. That is a divergent feedback loop, and it is the standard account of
why hyperinflations accelerate rather than settling. Note also that $a$ itself rises as people
learn to economise, which pulls the peak down over time — so a rate that raised revenue last year
may not this year.

**Calibration.** Cagan's estimates for the European hyperinflations put $a$ in the range implying
peak monthly inflation of 10–50%. At $a=3$ (annual), the peak is at $\pi=33\%$ a year, and
seigniorage there is about $0.37\times L/3$ — typically a few per cent of GDP. **A few per cent
of GDP is the realistic ceiling**, which is why seigniorage cannot finance a large deficit and
why attempts to make it do so end in the loop above.

## 4.3 The costs of inflation, sorted properly

The useful sort is by whether the inflation is **anticipated**.

### Costs of anticipated inflation

**Shoe-leather costs.** Higher $\pi$ raises $i$, which lowers desired real balances and raises
the number of trips to the bank — $n^*$ from [[02-money-demand]] §2.2. Those trips consume real
resources, $Fn^*$. This is exactly the failure of superneutrality derived in
[[03-equilibrium-and-neutrality]] §3.6, now given its name and its welfare interpretation.

**Menu costs.** Changing posted prices is costly, and higher inflation means changing them more
often.

**Relative-price distortion.** If prices are changed at staggered dates, higher inflation means
larger dispersion of relative prices among firms whose costs have not actually diverged. This is
a misallocation cost and it is precisely the object that the welfare loss function of
[[10-optimal-policy]] §10.1 prices — the $\theta/\kappa$ weight there *is* this cost.

**Tax distortions.** Nominal tax systems interact badly with inflation: capital gains are taxed on
nominal gains, depreciation allowances are set in historical cost, and bracket thresholds drift.
These are usually the largest measured costs of moderate inflation.

**Unit-of-account erosion.** Prices become worse signals, and beyond some rate contracts shorten
and the currency stops being used for long-horizon calculations.

### Costs of unanticipated inflation

**Arbitrary redistribution.** Unexpected inflation transfers wealth from nominal creditors to
nominal debtors, as §3.3 showed. The government, typically the largest nominal debtor, gains.
This is not a deadweight loss — it is a transfer — but it is an arbitrary one, and the
*anticipation* of it raises risk premia on nominal debt, which is a real cost.

**Noise in relative prices.** When the aggregate price level is volatile, an individual price
change is hard to read as a relative-price signal or as inflation. That is the Lucas (1973)
imperfect-information mechanism named in [[00-index]] of the Benigno set and in
[[02-firms-and-as]] §2.8.

### Why not target zero, then?

Three arguments for a small positive target, all standard and all worth naming:

1. **Measurement bias.** CPI inflation overstates true inflation by roughly a point
   ([[02-real-nominal-and-indices]] §2.4), so a measured 2% may be a true 1%.
2. **Downward nominal wage rigidity.** Some inflation lets real wages fall without nominal cuts,
   which greases relative-wage adjustment.
3. **Room above the zero lower bound.** A higher inflation target means a higher average nominal
   rate, which leaves more space to cut before hitting zero. This is the argument that connects
   directly to [[08-liquidity-trap]] §8.2 — an economy with a higher $\pi$ target has a smaller
   chance of $r_n<0$ binding.

### And the Friedman rule, in the other direction

The opportunity cost of holding money is $i$, but the social cost of producing money is zero. So
the efficient policy sets $i=0$, which by Fisher means $\pi=-r$ — **steady deflation at the real
interest rate**. That eliminates shoe-leather costs entirely.

Kurlat notes the tension plainly, and it is a good closing observation: the Friedman rule says
target deflation, and every actual central bank targets 2% inflation. The three arguments above
are why the theory loses. It is also worth noting that at $i=0$ the economy is permanently at the
zero lower bound of [[08-liquidity-trap]], which is the modern objection the older literature did
not have.

## 4.4 What to be able to do, cold

1. Define seigniorage, identify the rate, the base and who pays, and distinguish it from the
   inflation tax.
2. State Cagan demand, derive $\pi^{\max}=1/a$ with the second-order condition, and give the
   revenue at the peak.
3. State the Laffer condition as a unit elasticity of the base.
4. Explain the hyperinflation feedback loop and why $a$ rising makes it worse.
5. Sort the costs of inflation by whether they require surprise, and give at least three in each
   group.
6. Give the three arguments for a positive target and the Friedman-rule argument against, and say
   why the latter loses.

Practice: Kurlat ch. 11, Exercises 11.4–11.6 (pp. 221–222). **Exercise 11.6 is the Cagan demand
exercise and is explicitly in scope** for this course. Worked in
[[Resolucao/lista6_resolucao|lista 6]] — the Kurlat chs. 10–11 solution set has not been written yet. Narration: parts eight through eleven of
[[Leituras/aula-07-money-and-inflation-narrated.txt|the class 7 narration]].
