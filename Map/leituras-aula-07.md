---
tags: [map, macro1, aula-07, moeda, inflacao, leitura, lista-06]
date: 2026-09-12
---

# Reading plan — Lecture 7, Money and Inflation

#map/leituras

Lecture 7 is where the course states the **classical dichotomy**: money fixes the price level,
real variables are fixed by real forces. This file is the reading route for it — which pages of
Kurlat to read, in which order, what the lecture adds that the book does not have, and which
pages each item of **Lista 6** actually needs. Back to [[00_indice]].

> **Pages.** Kurlat's offset is **0**, so printed page = PDF page ([[books-index]]). If you do
> not want to open the 320-page book, the two chapters were cut out as a standalone file:
> [`Leituras/Kurlat_cap10-11_Money_and_Inflation.pdf`](../Leituras/Kurlat_cap10-11_Money_and_Inflation.pdf)
> — printed pp. **189–222**, 34 pages, with a `.md` beside it. It is also staged for upload as
> `NotebookLM/sources/Livro_Kurlat_Cap10-11_Money_and_Inflation.pdf`.

---

## 1. The core reading — Kurlat, chapters 10 and 11

Part IV opens on p. **189**. The examinable text runs **191–218**; the exercises to **222**.

| § | Title | Pages | pp. | What it gives you | Lista 6 |
|---|---|---|---|---|---|
| **10** | **Money** | **191** | | | |
| 10.1 | What is Money? | 191–192 | 2 | The three functions; why *medium of exchange* is the one that defines money; double coincidence of wants; M0 → M2 and why there is no unique measure | — |
| 10.2 | The Supply of Money | 192–194 | 2 | Monetary base vs broader aggregates; the bank's role in creating deposits | Q1(d) |
| 10.3 | Changing the Supply of Money | 194–199 | 5 | Open-market operations, the discount window, reserve requirements — the longest section in ch. 10, and the one the slides compress hardest | Q1(c,d) |
| 10.4 | The Demand for Money | 199–202 | 3 | **Baumol-Tobin** derived properly: the trip-cost trade-off, $N^*$, and $\frac{M}{p}=\sqrt{\frac{YF}{2i}}$ with its elasticities $+\tfrac12$ in $Y$ and $-\tfrac12$ in $i$ | **Q1(b), Q2(b,c)** |
| — | *Exercises 10.x* | 202–203 | 2 | Five exercises | |
| **11** | **The Price Level and Inflation** | **205** | | | |
| 11.1 | Measurement | 205–208 | 3 | The index-number problem again (it is lecture 1's problem wearing new clothes); GDP deflator vs CPI and what each weights | — |
| 11.2 | Equilibrium | 208–215 | **7** | The money market as an equilibrium condition; neutrality; the steady states; **where $\pi=\mu-\eta g$ comes from**. The heart of the lecture | **Q1(a,c,d), Q2(a,b)** |
| 11.3 | Seignorage | 215–217 | 2 | The inflation tax, its **base** $M/p$, and why the base shrinks as inflation rises | — |
| 11.4 | The Cost of Inflation | 217–218 | 2 | Shoe-leather out of Baumol-Tobin, the **Friedman rule** ($i=0$, so $\pi=-r$), menu costs, relative-price uncertainty, bank seigniorage | — |
| — | *Exercises 11.x* | 218–222 | 5 | Nine exercises | |

**28 pages of text, 7 of exercises.** §11.2 is a seventh of the reading and most of the exam risk.

## 2. Reading order — four sittings

| # | Pages | pp. | After this sitting you can… |
|---|---|---|---|
| 1 | 191–202 | 12 | …say what counts as money, explain why the multiplier is not a constant, and **derive Baumol-Tobin from the trip-cost problem** rather than quoting the square root |
| 2 | 205–215 | 11 | …derive $\pi = \mu - \eta g$ by differentiating the equilibrium condition, and say what each of the three steady states assumes |
| 3 | 215–218 | 4 | …explain who pays the inflation tax, why its base erodes, and why the Friedman rule demands deflation |
| 4 | 202–203, 218–222 | 7 | …do the exercises, starting with the five starred in §5 below |

Sitting 2 is the one to protect. If time runs out, read 208–215 twice and skip 11.1 — the
index-number material is already covered by lecture 1 and [[01_mensuracao_agregados]].

## 3. Lecture vs book — what each has that the other does not

The slides are [`Aula/MPE_Macro1_SlidesAula7_2026.pdf`](../Aula/MPE_Macro1_SlidesAula7_2026.pdf)
(22 pages, 8 sections). A converted `.md` sits beside it, but **markitdown scrambles the
two-column algebra — read the PDF for any derivation.**

**Only in the lecture.** This is what cannot be learned from the book alone:

| Slide content | Why it matters |
|---|---|
| The **commercial bank balance sheet**, and why banks hold reserves (unexpected withdrawals; regulation) | Makes the multiplier a behavioural result, not an identity |
| The multiplier **breaking at a zero interest rate** or when reserves earn interest, with the **US late-2008** episode | The reason "base up ⇒ money up" failed in practice; a natural exam question |
| **Keynes (1936, ch. 15)** and the three motives — transactions, precautionary, speculative | Names the taxonomy the book does not dwell on |
| Two **worked index examples**: wheat/computers (deflator ≈ 73, $\pi\approx-27\%$) and Ferrari/caviar/champagne (CPI 100 → 110, $\pi=10\%$) | The arithmetic you are expected to reproduce |
| The **Usuria** example: 11% nominal, 2% expected inflation, ≈ 8.8% real | Fisher exactly vs approximately |
| **Three steady states** laid out explicitly, with the time-differentiation that yields $\pi=\mu-\eta g$ | This *is* Lista 6 Q2(a) |
| Two comparative statics: a **one-time jump in $M^S$** (p jumps proportionally) and a **one-time rise in $\mu$** | The second is the subtle one — see the trap in §6 |
| The **government budget constraint**, slide eq. (6), framing seigniorage as a loan never repaid | Connects money creation to fiscal policy |

**Only in the book.** §10.3's full treatment of the instruments (5 pages the slides compress to
a few lines), the formal algebra of §11.2 and §11.3, the 14 end-of-chapter exercises, and the
**Cagan money demand**, which appears only as exercise 11.6 and on no slide.

**Notation.** The slides write money demand $m^D(Y,i)$; [[07_moeda_inflacao]] writes $L(Y,i)$.
Same object. Follow Kurlat's $m^D(Y,i)$ in anything you hand in, and say so if you use the other.

## 4. The 14 end-of-chapter exercises

★ = bears directly on Lista 6. **Pages and levels are taken from [[exercises-index]]**, which
is the authority `/exercise-plan` reads; the pages there were re-measured against the PDF for
this file and agree exactly.

| # | Title | p. | Subtopic | Level |
|---|---|---|---|---|
| 10.1 | Central Bank Instruments | 202 | Money supply, instruments | foundational |
| 10.2 | Pickpockets | 202 | Currency ratio, multiplier | exam |
| 10.3 | Interest on Reserves | 202 | Multiplier, zero lower bound | exam |
| ★ 10.4 | ATMs | 203 | Baumol-Tobin comparative statics in $F$ | exam |
| ★ 10.5 | Going to the Bank | 203 | Baumol-Tobin, velocity | advanced |
| ★ 11.1 | The Elasticity of Money Demand | 218 | $\eta$ under Baumol-Tobin | exam |
| ★ 11.2 | The Quantity Theory | 218 | Constant velocity, what it implies | foundational |
| 11.3 | Seignorage with Zero Inflation and Growth | 219 | Seigniorage, growth (uses 11.1) | exam |
| 11.4 | Growth in the Money Supply | 219 | Money growth → inflation | exam |
| ★ 11.5 | Inflation Targeting | 219 | Hitting a target; a shock to $r$ | exam |
| 11.6 | Seignorage with High Inflation | 219 | **Cagan** demand, inflation Laffer curve | advanced |
| 11.7 | Bank Seignorage | 221 | Seigniorage earned by banks | advanced |
| 11.8 | Real Interest Rates | 222 | Fisher, ex-ante vs ex-post | exam |
| 11.9 | Money among Prisoners of War | 222 | Synthesis of chs. 10–11 | foundational |

Do the five starred ones before the lista. Then **11.6**, which is the only place the course
meets the Cagan function and the Laffer logic in algebra.

## 5. Lista 6, item by item

[`Listas/MPE_Macro1_2026_Lista6.pdf`](../Listas/MPE_Macro1_2026_Lista6.pdf) — 2 pages, 2
questions, 5 points each, both *"Based on Kurlat (2020, Cap. 10 e 11)"*.

| Item | Asks | Read first | The trap |
|---|---|---|---|
| Q1(a) | Why $MV=PY$ is an accounting identity, not a theory of money demand; whether it says $M$ *causes* $p$, $Y$ or $V$ | 11.2 (208–215) | Answering "money causes inflation". As an identity it is **empty** — it becomes a theory only on the added assumptions that $V$ is stable and $Y$ is real-side determined. Name the assumptions |
| Q1(b) | What Baumol-Tobin implies for money demand **and velocity** | 10.4 (199–202) | Stopping at $\sqrt{YF/2i}$. Invert it: $V = PY/M = \sqrt{2iY/F}$ — velocity **rises with $i$** and is not a constant, which is exactly what the QTM assumed away |
| Q1(c) | With $p=\bar p$ fixed, how $Y$ and $i$ must move after a rise in $M^S$; is there a clear mechanism; what changes under flexible prices | 11.2 (208–215) | Asserting the classical result in a fixed-price world. With $p$ stuck, $i$ must fall and/or $Y$ rise — and the honest answer is that ch. 11 has **no mechanism** for that; it is lecture 8's job. Say so |
| Q1(d) | Reading the equilibrium when the CB sets $M$ versus when it sets $i$ | 10.2–10.3, 11.2 | Treating the two as alternatives with the same content. Fix $i$ and the quantity of money becomes **endogenous** — the same equation read in the opposite direction |
| Q2(a) | Derive $\pi = \mu - \eta g$ from the equilibrium condition | 11.2 + slides §6 | Asserting it. Differentiate $M^S = p\,m^D(Y,i)$ with respect to time, divide through, and use constant $i$ to kill the interest term |
| Q2(b)(i) | $\eta$ under Baumol-Tobin | 10.4, ex. 11.1 | $\eta = \tfrac12$ — the income elasticity of $\sqrt{YF/2i}$, not 1 |
| Q2(b)(ii) | The money growth rate for $\pi^*=2\%$, $g=3\%$ | — | $\mu = \pi^* + \eta g = 2 + \tfrac12(3) = \mathbf{3.5\%}$ |
| Q2(b)(iii) | Realised inflation if demand is really Cambridge, $\eta=1$ | — | $\pi = 3.5 - 1(3) = \mathbf{0.5\%}$ — the bank **undershoots by 1.5 pp**. Getting $\eta$ wrong biases inflation downward, and the sign of the error is the point |
| Q2(c) | With $\dot F/F = f < 0$, show $\pi = \mu - \tfrac12(g+f)$, and why falling $F$ is inflationary | 10.4 + ex. 10.4 | Log-differentiate $m^D=\sqrt{YF/2i}$ at constant $i$: $\hat m = \tfrac12(g+f)$, so $\pi = \mu - \tfrac12(g+f)$. Cheaper bank trips mean people **hold less real money**; demand grows more slowly, so a fixed $\mu$ is now too loose and $\pi$ rises |

**Q2(c) is the last item, and by the professor's pattern the last item is the most conceptual —
the second half of it (the *why*) is where the marks are**, not the log-differentiation.

> **Due date.** The PDF prints *"Data de entrega: 21/09/2025"*. The year is almost certainly a
> typo for **2026**: the course runs in 2026 and Lista 5 was due 08/09/2026. Cited verbatim here;
> confirm with the professor rather than assuming.

> ⚠️ **The maps' prediction was half wrong.** [[exercises-index]] and [[aulas-x-bibliografia]]
> predicted Lista 6 = Kurlat 10–11 **+ Benigno §1–5** (lectures 7 *and* 8), naming exercises
> 11.2, 11.6 and 10.4. The chapter anchor and the spirit of 11.2/10.4 hit; **11.6 (Cagan) did
> not appear, and there is no Benigno content at all.** So the AD-AS material must fall to
> **Lista 7**, which now carries lectures 8–9.

## 6. Complementary reading

Page numbers below are **printed**; add the offset from [[books-index]] for the PDF page.

| Source | Where | Printed | PDF | Use it for | Caution |
|---|---|---|---|---|---|
| **Jones (2020)**, ch. 8 *Inflation* | §8.2 Quantity Theory (216), §8.4 Costs (225), §8.5 Fiscal Causes / Inflation Tax (228), §8.6 The Great Inflation of the 1970s (232) | **211–239** | 236–264 | The best complement for this lecture: more graphical, real US data, and a fiscal story for high inflation that Kurlat only gestures at | Verified against the local 2020 file |
| **Romer (2012, 4th ed.)**, ch. 11 *Inflation and Monetary Policy* | — | **513–583** | 535–605 | Rigour on seigniorage, the inflation tax and dynamic inconsistency | **Much of it is past this course** — read for intuition only, and do not import its models |
| **Jones (2020)**, ch. 12 | §12.3 The Phillips Curve (326) | 317+ | 342+ | — | ⚠️ `rules/07` lists Jones ch. 12 under lecture 7. It is **Phillips-curve material: lectures 8–9**, not 7 |
| **Carlin & Soskice (2024)** | monetary policy / inflation targeting | — | — | Contrast with Benigno in lectures 8–9 | **Chapter numbers not verified** for the local 2024 edition; little of it serves lecture 7 |
| **Williamson**, solutions manual (2014) | — | — | — | — | ⚠️ `rules/07` cites "Williamson, cap. 12". **Only the solutions manual is in the project — the textbook is not**, and the chapter mapping is unverified. Do not rely on it |

## 7. Proposed additions to [[07_moeda_inflacao]] — **not applied**

`rules/07_moeda_inflacao.md` was **not modified**. It is already strong on this topic; these are
the gaps this reading turned up, for a later decision:

1. **The elasticity form of the inflation equation.** The rules file gives the QTM in growth
   rates, $g_M + g_V = \pi + g_Y$, but not $\pi = \mu - \eta g$ — which is the form the lecture
   derives and the form **both parts of Lista 6 Q2** are written in.
2. **$\eta$ as the bridge.** State explicitly that Baumol-Tobin implies $\eta=\tfrac12$ and the
   Cambridge equation implies $\eta=1$, and that the choice shifts required money growth by
   $\tfrac12 g$ — the whole content of Q2(b).
3. **Velocity as an implication, not an assumption.** Baumol-Tobin gives $V=\sqrt{2iY/F}$; the
   rules file derives money demand but never inverts it, which is Q1(b).
4. **The $\mu \to \mu'$ experiment.** A permanent rise in money growth raises $i$, which lowers
   $m^D$, so $p$ must **jump at the announcement** on top of growing faster afterwards. The
   slides make this explicit; the rules file's trap list does not.
5. **Shoe-leather with the formula.** The slides give total trip cost $\sqrt{(r+\pi)YF/2}$, slide
   eq. (7) — a concrete hook for the Friedman rule the rules file states only verbally.

## 8. Scope guard

- The course **stops at Kurlat ch. 11.** Chapters 12–15 (business cycles, RBC, New Keynesian,
  policy) are **not examinable**, even though ch. 12 begins on p. 223, immediately after this
  reading. Do not wander in.
- Kurlat **ch. 8 (Investment) is out of scope** throughout the course.
- **Cagan money demand is in scope** — it is Kurlat exercise 11.6. It is the one piece of
  "advanced" machinery the chapter legitimately introduces.
- Nothing from Ljungqvist & Sargent; no stochastic DSGE, no dynamic programming, no
  time-series econometrics; no log-linearised Calvo NKPC.
- **Where this lecture sits.** It is the first half of the second thread named in [[00_indice]]:
  *money is neutral, but only in the long run.* Lecture 7 establishes the dichotomy; lectures
  8–9 break it at short horizons with sticky prices and recover it at long ones. Q1(c) is the
  seam — it asks what happens when $p$ cannot move, and the honest answer is "chapter 11 has no
  answer; that is lecture 8".

---

**Listen instead:** the whole lecture is narrated in
[`Leituras/aula-07-money-and-inflation-narrated.txt`](../Leituras/aula-07-money-and-inflation-narrated.txt)
— 21,180 words, about 141 minutes at 150 words per minute, covering both chapters, the slides
and Lista 6, with a spoken formula sheet and a self-test. NotebookLM prompts for this lecture
(4 slide decks + 3 audio threads) are in [`NotebookLM/`](../NotebookLM/README.md).

**See also:** [[07_moeda_inflacao]] · [[books-index]] · [[exercises-index]] ·
[[aulas-x-bibliografia]] · [[cobertura]] · [[00_indice]]
