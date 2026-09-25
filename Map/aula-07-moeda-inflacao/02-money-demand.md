---
tags: [aula-07, kurlat-cap-10, baumol-tobin, demanda-por-moeda, velocidade, derivacao]
date: 2026-09-19
---

# 2. Money demand: Baumol–Tobin, derived

**Kurlat §10.4, printed pages 199–204.** Up: [[00-index]] ·
Prev: [[01-money-and-its-supply]] · Next: [[03-equilibrium-and-neutrality]]

> **Companion:** [The Trip to the Bank](companion-baumol-tobin.html) — the two costs trading
> off, the square-root optimum, and both elasticities read straight off the curve.

Money pays no interest and bonds do, so holding money is strictly dominated as an investment.
Any model in which money is held must therefore contain a **friction**, and the whole content of
this section is one specific friction and what it implies.

---

## 2.1 The problem

A household must spend $Y$ over a period, evenly. It holds wealth in bonds earning nominal
interest $i$, and converts bonds to cash on trips to the bank. Each trip costs $F$ in real
resources — time, fees, inconvenience.

Let $n$ be the number of trips. Each trip withdraws $Y/n$, which is then run down to zero before
the next trip. **Average money holdings over the period are therefore half the withdrawal:**

$$\frac{M^d}{P} = \frac{Y}{2n}$$

This is the sawtooth: balances start at $Y/n$, fall linearly to zero, and jump back up. The
average of a linear decline from $x$ to $0$ is $x/2$.

**The two costs.**

- **Transaction cost:** $F\,n$, rising in the number of trips.
- **Forgone interest:** $i\cdot\dfrac{Y}{2n}$, falling in the number of trips.

$$\min_{n}\;\; \mathcal{C}(n)= F n + i\,\frac{Y}{2n}$$

## 2.2 Solving it

$$\frac{d\mathcal C}{dn} = F - \frac{iY}{2n^2} = 0
\qquad\Longrightarrow\qquad
n^2 = \frac{iY}{2F}
\qquad\Longrightarrow\qquad
n^* = \sqrt{\frac{iY}{2F}}$$

Second-order condition: $\mathcal C''(n)=iY/n^3>0$, so it is a minimum. The two cost curves cross
at the optimum — at $n^*$, total transaction cost equals total forgone interest, which is a good
check and a nice fact:

$$Fn^* = \sqrt{\frac{F i Y}{2}} = i\,\frac{Y}{2n^*}$$

Substituting $n^*$ into average balances gives the **Baumol–Tobin money demand**:

$$\frac{M^d}{P} = \frac{Y}{2n^*} = \frac{Y}{2}\sqrt{\frac{2F}{iY}}
\qquad\Longrightarrow\qquad
\boxed{\;\frac{M^d}{P} = \sqrt{\frac{FY}{2i}}\;}$$

Verified against numerical minimisation in `check_money.py`.

## 2.3 The two elasticities, and why they are the point

Take logs of the boxed formula:

$$\ln\frac{M^d}{P} = \tfrac12\ln F + \tfrac12\ln Y - \tfrac12\ln i - \tfrac12\ln 2$$

so

$$\boxed{\;\varepsilon_Y \equiv \frac{\partial\ln(M/P)}{\partial\ln Y}=\frac{1}{2},
\qquad
\varepsilon_i \equiv \frac{\partial\ln(M/P)}{\partial\ln i}=-\frac{1}{2},
\qquad
\varepsilon_F = \frac{1}{2}\;}$$

**The income elasticity is one half, and that is an economic claim, not an algebraic accident.**
A household whose income doubles does **not** double its cash. It goes to the bank more often —
$n^*$ rises with $\sqrt{Y}$ — so cash rises only with the square root. There are **economies of
scale in cash management**.

**Contrast with the Cambridge/quantity-theory formulation**, $M^d/P = kY$, which has
$\varepsilon_Y=1$: money demand proportional to income, no scale economies. The difference is not
a quibble about parameters. One says managing cash has scale economies; the other says it does
not. Which is right is an empirical question, and [[03-equilibrium-and-neutrality]] §3.4 shows
exactly how much a central bank loses by getting it wrong.

**The interest elasticity is negative**, which is the demand-curve property: a higher nominal
rate raises the opportunity cost of holding cash, so people economise on it by trooping to the
bank more often. Note it is $i$ and not $r$ that matters — the opportunity cost of holding a
zero-interest asset is the **nominal** rate, since inflation erodes both money and bonds equally.
This is trap 2 in [[07_moeda_inflacao]] and it returns in the Fisher discussion.

**The $F$ elasticity is where financial innovation enters.** Cash machines, debit cards and
banking on a phone all cut $F$. Since $\varepsilon_F=+1/2$, a falling $F$ **lowers** real money
demand — which is a downward drift in money demand that has nothing to do with income or interest
rates, and which is the standard explanation for why money-demand equations estimated in the
1970s broke down in the 1980s. It is also the reason [[03-equilibrium-and-neutrality]] §3.6 warns
against monetary targeting.

## 2.4 Velocity, as an implication rather than an assumption

Define velocity by the **quantity equation**:

$$M V = P Y \qquad\Longleftrightarrow\qquad V\equiv\frac{PY}{M}$$

**This is a definition, true by construction** — it defines $V$ as whatever makes it hold. It
becomes the *quantity theory* only when you add the assumption that $V$ is constant.

Substitute Baumol–Tobin:

$$V = \frac{Y}{M/P} = \frac{Y}{\sqrt{FY/2i}}
\qquad\Longrightarrow\qquad
\boxed{\;V = \sqrt{\frac{2iY}{F}}\;}$$

**So velocity is not constant.** It rises with the nominal interest rate (people hold less cash,
so each unit turns over faster), rises with income (scale economies again), and falls with the
cost of a trip.

**The pivot to state in an exam:** assuming constant velocity is what converts the quantity
*identity* into the quantity *theory*, and the model just derived says velocity moves whenever
the interest rate moves. So the quantity theory is a good approximation exactly when interest
rates are stable, and a poor one in exactly the episodes — hyperinflations, disinflations — where
people most want to use it.

## 2.5 What the model leaves out

Baumol–Tobin is a model of **transactions** demand only. Two other motives are standard and are
not in it:

- **Precautionary demand** — holding cash against uncertain expenditure, which is the Jensen
  argument of [[05-ricardian-and-constraints]] §5.4 applied to liquidity.
- **Speculative demand** — Keynes's motive, holding money when bond prices are expected to fall.

And the model treats $Y$ as exogenous to the cash decision, ignores the choice between different
liquid assets, and assumes trips are evenly spaced. None of that changes the qualitative results;
all of it means the elasticities are stylised rather than estimates.

> **Contrast: Jones (2020), ch. 8 and Romer (2012), ch. 11.** Jones works with $M^d/P = kY$
> throughout — the Cambridge form — which makes the quantity theory exact and the algebra
> shorter, at the cost of hiding the scale economies. Romer derives money demand from a
> money-in-the-utility-function or cash-in-advance setup, which is more general and more modern
> but yields no closed-form elasticity to test. Kurlat's trip-cost model is the only one of the
> three that *derives* a number you can argue about, which is why it is the one in the syllabus.
> Local files, +25 and +22 page offsets ([[books-index]]).

## 2.6 What to be able to do, cold

1. Set up the trip-cost problem, explain why average balances are $Y/2n$, and derive $n^*$.
2. Reach the square-root formula and verify the second-order condition.
3. Show that at the optimum the two costs are equal.
4. Derive all three elasticities by taking logs, and give the economics of each.
5. State the contrast with the Cambridge form and what is at stake in it.
6. Derive velocity, show it is not constant, and state exactly what converts the quantity
   identity into the quantity theory.
7. Explain how financial innovation shifts money demand, and why that matters for policy.

Practice: Kurlat ch. 10, Exercises 10.3 and 10.4 (p. 204); and Lista 6, question 2, which is the
Baumol–Tobin calibration. Worked in [[Resolucao/lista6_resolucao|lista 6]] — the Kurlat chs. 10–11 solution set has not been written yet and
[[Resolucao/lista6_resolucao|lista 6]].
