---
tags: [map, aula-07, moeda, inflacao, baumol-tobin, senhoriagem, derivacoes]
date: 2026-09-19
---

# Aula 7 — Money and inflation, derived

**Source.** Kurlat (2020), chapters **10** and **11**, printed pages 191–222.
Complementary: Jones (2020) ch. 8 *Inflation* (pp. 211–239) — the best complement for this
session; Romer (2012) ch. 11 *Inflation and Monetary Policy* (pp. 513–583) for the formal
seigniorage and hyperinflation material.

**Why this directory exists.** [[07_moeda_inflacao]] states the results and
[[leituras-aula-07]] routes the reading page by page. Neither derives the Baumol–Tobin
square root, neither proves that the interest-elasticity of money demand is exactly $-1/2$ from
that model, and neither shows *why* the inflation Laffer curve has a peak. Those are the three
derivations here, plus the one that matters most for the exam: the decomposition

$$\pi = \mu_M - \varepsilon_{Y}\,g_Y$$

and everything that follows from getting $\varepsilon_Y$ wrong.

---

## Reading order

| # | Note | Kurlat | What it settles |
|---|---|---|---|
| 1 | [[01-money-and-its-supply]] | §10.1–§10.3, pp. 191–199 | What makes money money; the four aggregates; the multiplier derived from two ratios; how open-market operations work |
| 2 | [[02-money-demand]] | §10.4, pp. 199–204 | Baumol–Tobin from the trip-cost problem; the square-root formula; both elasticities derived, not asserted; velocity as an implication |
| 3 | [[03-equilibrium-and-neutrality]] | §11.1–§11.2, pp. 205–215 | Price indices and Fisher; the three steady states; neutrality against superneutrality; the inflation-targeting error formula |
| 4 | [[04-seigniorage-and-costs]] | §11.3–§11.4, pp. 215–222 | The inflation tax and its base; the Laffer peak derived; Cagan demand; the costs of inflation, sorted by whether they need surprise |

Runnable check: `check_money.py`. It solves the Baumol–Tobin problem numerically and against
the closed form, confirms both elasticities to machine precision, verifies the money multiplier
against a simulated deposit-expansion chain, reproduces Kurlat's deflator and CPI arithmetic and
his Fisher example, checks the steady-state inflation decomposition and the policy-error formula,
and locates the Laffer peak at $1/a$ for Cagan demand both analytically and numerically.

## Interactive companions

| Companion | Drives | Note |
|---|---|---|
| [The Trip to the Bank](companion-baumol-tobin.html) | the two costs trading off, the square-root optimum, and both elasticities read off the same curve | [[02-money-demand]] |
| [The Inflation Tax](companion-seigniorage.html) | revenue as rate times base, the base eroding faster than the rate rises, and the Laffer peak at $1/a$ | [[04-seigniorage-and-costs]] |

---

## Notation, once

| Symbol | Meaning |
|---|---|
| $M$ | nominal money stock; $M/P$ real balances |
| $i$, $r$ | nominal and real interest rates |
| $\pi$ | inflation; $\mu_M \equiv \dot M/M$ money growth |
| $F$ | the fixed cost of a trip to the bank (Baumol–Tobin) |
| $V$ | velocity, $PY/M$ |
| $\varepsilon_Y$, $\varepsilon_i$ | income and interest elasticities of money demand |
| $a$ | semi-elasticity of Cagan money demand, $L=e^{-a\pi}$ |

**Two conventions that cause errors.** Kurlat's $\eta$ in this chapter is the **income
elasticity of money demand** — not the inverse Frisch elasticity of [[05_trabalho_lazer]] and
[[08_adas_microfundamentos]], which is a completely different object that happens to share the
letter. This directory writes $\varepsilon_Y$ to keep them apart. And $\mu_M$ here is money
growth, not the mark-up $\mu$ of session 8.

## The spine of the session

1. **Money is held despite being dominated in return.** Any interest-bearing asset beats
   currency, so a model in which money is valued needs a *friction*. Baumol–Tobin supplies one:
   converting bonds to cash costs $F$ per trip.
2. **That friction pins down money demand**, and its functional form determines the two
   elasticities that everything else runs on.
3. **In equilibrium the price level is whatever clears the money market**, and with output and
   the real rate set by real forces, money is **neutral** — the classical dichotomy of
   [[01-equilibrium-as-benchmark]] §1.3, now with a price level attached.
4. **Neutrality is not superneutrality.** A one-off change in $M$ is fully neutral; a change in
   the *growth rate* of $M$ changes the nominal rate, which changes desired real balances, which
   changes real resources spent on trips to the bank. That asymmetry is the whole of
   [[03-equilibrium-and-neutrality]] §3.5.
5. **Inflation is a tax**, and like any tax it erodes its own base, which is why the revenue
   curve has a peak.

## Where this session sits

This is the **last session of the classical block**. Everything up to here has flexible prices
and money that does not matter for real variables. Sessions 8 and 9 break that by freezing a
fraction of prices, at which point money becomes non-neutral in the short run and a
stabilisation problem appears.

The bridge is explicit: [[08_adas_microfundamentos]] has **no money in it at all** — the central
bank sets $i$ directly and there is no LM curve. So the money-demand apparatus built here is
*not* used there, and understanding why is worth a paragraph in any exam answer. The reason
Benigno can drop it is that once the central bank sets the interest rate, the money stock becomes
whatever is needed to clear the money market at that rate, and money demand becomes a residual
that never feeds back. See [[01-household-and-ad]] §1.7 for the trap this creates.

## Out of scope

Kurlat forward-references chapter 14 (sticky prices and monetary non-neutrality) and chapter 15
(the zero lower bound); **both are outside this course** and their content is covered instead by
Benigno (2015) in sessions 8 and 9. Where Kurlat points forward, this directory stops and says
so. The money multiplier is covered as accounting, not as a theory of banking.

Support material already in the project: the full narrated reading is
[[Leituras/aula-07-money-and-inflation-narrated.txt|the class 7 narration]], and the page-by-page
reading route is [[leituras-aula-07]].
