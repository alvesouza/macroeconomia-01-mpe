# Lista 6 — Question 1(d)

> How do we interpret the money market equilibrium if we assume Central Banks control the
> money supply? What if they control the nominal interest rate instead?

Answered using only what items (a)–(c) established: the identity $MV = PY$, the
Baumol–Tobin demand, and the equilibrium condition $M^S = p\,m^D(Y,i)$. **No IS–LM, and no
aggregate-demand channel** — everything below is a statement about the money market alone.

A LaTeX treatment of the same item, with the money-market diagram, is in
`Resolucao/lista6_resolucao.tex`, item (d). This note is the diagram-free version.

---

## 1. The answer is a counting argument

Equation (2) is **one equation**:

$$M^S = p\,m^D(Y,i)$$

It contains four objects: $M^S$, $p$, $Y$, $i$. Take $p$ and $Y$ as given from outside — the
short-run assumption of item (c). That leaves **two** unknowns, $M^S$ and $i$, and **one**
equation.

So exactly one of them can be set from outside; the other is whatever makes the equation
hold. **That choice is the monetary policy regime.** Nothing else in this item does any work.

---

## 2. Regime A — the bank fixes the quantity

Set $M^S = \bar M$. The equation becomes

$$\bar M = p\,m^D(Y,i) \qquad\Longrightarrow\qquad i \ \text{adjusts}$$

The nominal interest rate is **endogenous**. The central bank does not choose it. It is the
price that clears the market, exactly as a price clears any market in which the quantity is
fixed.

**The mechanism, from Baumol–Tobin.** Item (b) gave

$$m^D = \sqrt{\frac{FY}{2i}}, \qquad n^\star = \sqrt{\frac{iY}{2F}}$$

If the bank supplies less money than people wish to hold at the prevailing rate, the shortage
bids $i$ up. A higher $i$ raises the opportunity cost of an idle balance, so each household
makes **more trips to the bank and holds a smaller average balance**, until desired holdings
equal $\bar M/p$.

The adjustment is a change in household transaction behaviour — trips — not a movement along
any aggregate demand schedule.

---

## 3. Regime B — the bank fixes the price

Set $i = \bar\imath$. Then $m^D(Y,\bar\imath)$ is a number, and the equation becomes

$$M^S = p\,m^D(Y,\bar\imath) \qquad\Longrightarrow\qquad M^S \ \text{adjusts}$$

The **money supply is now endogenous**. Having announced a rate, the bank is obliged to supply
whatever quantity is demanded at it — buying securities when the public wants more money,
selling when it wants less. Its balance sheet is the residual.

This is how essentially every modern central bank operates: it announces a rate, not a
quantity of money.

---

## 4. Why both instruments cannot be used at once

Fixing $\bar M$ **and** $\bar\imath$ imposes two conditions on one equation. Generically there
is no solution: the pair chosen simply will not satisfy it. You would have to guess in advance
the exact $\bar M$ that clears at $\bar\imath$, which requires knowing $m^D$ perfectly.

So treating "the money supply" as an exogenous policy instrument is a **modelling choice**,
not a fact about central banks.

The two regimes are equivalent **only under perfect knowledge of $m^D$**. They come apart the
moment money demand shifts.

---

## 5. Same shock, different symptom

Take the falling transaction cost from question 2(c), $\dot F/F = f < 0$ — financial
innovation making a trip to the bank cheaper. Since $m^D = \sqrt{FY/2i}$, demand **falls at
every interest rate**.

| Regime | What is fixed | What moves | What you observe |
|---|---|---|---|
| A | $\bar M$ | $i$ **falls**, to make holding money attractive again | a moving interest rate |
| B | $\bar\imath$ | $M^S$ **contracts**, to defend the rate | a moving money stock |

The underlying event is identical. Which variable moves is a property of the regime, not of
the economy — which is the practical content of this item.

---

## 6. Back to item (a)

Item (a) established that $MV = PY$ is an accounting identity and therefore causally silent.
Combining it with Baumol–Tobin removes velocity's freedom:

$$V = \frac{Y}{m^D} = \sqrt{\frac{2iY}{F}}$$

- Under **Regime A**: $i$ moves, so $V$ moves. Fixing $M$ does **not** fix $PY$ — which is
  precisely why item (a)'s identity could not be read as a quantity theory.
- Under **Regime B**: $i$ is pinned, so $V$ is pinned (given $Y$ and $F$), and $M$ moves
  one-for-one with $PY$. Here $p$ and $Y$ cause $M$, not the reverse.

The identity is the same in both. The theory of $m^D$ is what tells you which letter absorbs
the shock.

---

## 7. Consequence for question 2

Question 2 derives $\pi = \mu - \eta g$ and then asks the bank to *choose* $\mu$. That is
coherent only under **Regime A**. Under a rate rule there is no $\mu$ to select: $\mu$ is
whatever defending $\bar\imath$ happens to require, and inflation is pinned by the rule and by
expectations instead.

Worth stating explicitly if question 2 asks you to interpret the result.

---

## Summary answer

The equilibrium condition is one equation in two policy-relevant unknowns, so it determines
exactly one of them.

- **Bank controls $M$:** the quantity is exogenous and the interest rate is the endogenous
  market-clearing price. Households adjust through the frequency of bank trips.
- **Bank controls $i$:** the rate is exogenous and the money stock is endogenous and
  demand-determined. The bank accommodates whatever quantity is demanded.

Both cannot be chosen at once, and the two regimes differ observationally as soon as money
demand shifts.
