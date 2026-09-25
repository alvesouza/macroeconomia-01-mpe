---
tags: [benigno, adas, aula-09, choques-de-produtividade, divine-coincidence]
date: 2026-09-15
---

# 5. Productivity shocks: three cases, three different policies

**Article: §6, §6.1–§6.3, Figures 6–8, printed pages 511–513.** Up: [[00-index]] ·
Prev: [[04-equilibrium-geometry]] · Next: [[06-markup-shocks]] ·
Rules: [[09_adas_politica]]

The article's own summary of this section (p. 513) is the examinable sentence:
*"Regardless of the properties of the shock — temporary, permanent or expected —
monetary policy can always move interest rates to stabilize prices and the output gap
simultaneously. But the direction of the movement depends on the nature of the shock."*
Everything below is that sentence, derived.

Throughout, the starting point is Fig. 5: $p=p^e=\bar p$, $y=y_n=y_e$, $i=r_n$, $\mu=0$.
From (15) and (19), a productivity change moves both real anchors by the same amount:

$$dy_n=dy_e=\frac{1+\eta}{\sigma^{-1}+\eta}\,da,\qquad d\bar y_n=\frac{1+\eta}{\sigma^{-1}+\eta}\,d\bar a$$

---

## 5.1 Temporary gain: $a\uparrow$, $\bar a$ unchanged (§6.1, Fig. 6)

**Curves.** $y_n$ rises, so AS shifts **down and right** through the new anchor
$(p^e,y_n')$. AD does not move: current productivity appears nowhere in (21).

**Equilibrium.** From the machine in [[04-equilibrium-geometry]] §4.4, with
$d\bar y_n=di=d\bar p=0$:

$$dy=\frac{\sigma\kappa}{1+\sigma\kappa}\,dy_n>0,\qquad
d(y-y_n)=-\frac{dy_n}{1+\sigma\kappa}<0,\qquad
dp=-\frac{\kappa\,dy_n}{1+\sigma\kappa}<0$$

Read the three together, because the combination is counter-intuitive and it is what the
question will ask about: **output rises, prices fall, and the output gap is negative.**
Good news for output is not good news for the gap. Sticky prices are the reason: only
$1-\alpha$ of firms cut their prices, so the real-rate fall is too small to pull demand
up by the full $dy_n$.

The mechanism in the article's words (p. 512): higher $A$ lowers real marginal cost, the
adjusting firms cut prices, that raises expected inflation $(\bar p-p)$ and lowers the
real rate, which stimulates consumption — but not enough.

**Welfare.** $y_e$ moved by the same $dy_n$, so $y-y_e=-dy_n/(1+\sigma\kappa)<0$ too.
The economy is inefficiently *small* even while it grows.

**Optimal policy.** Set $d(y-y_n)=0$ in the machine:

$$-dy_n-\sigma\,di=0\quad\Longrightarrow\quad \boxed{di=-\frac{dy_n}{\sigma}<0}$$

An **expansionary** cut. Cross-check against the natural rate: $r_n$ contains
$\sigma^{-1}(\bar y_n-y_n)$, so $dr_n=-\sigma^{-1}dy_n<0$ — the natural real rate has
fallen and the policy rate must follow it down, which is the same number. At that rate,
$dy=dy_n$ and $dp=0$: point $E''$ in Fig. 6, with stable prices and a closed gap.

## 5.2 Permanent gain: $a\uparrow$ and $\bar a\uparrow$ (§6.2, Fig. 7)

**Curves.** AS shifts down as before. Now AD shifts **up too**, because
$\bar y_n$ rises: the household expects to be richer and, to smooth, raises consumption
today.

**Equilibrium.** Put $d\bar y_n=dy_n$ in the machine:

$$d(y-y_n)=\frac{dy_n-dy_n}{1+\sigma\kappa}=0,\qquad dp=0,\qquad dy=dy_n$$

The two shifts are exactly the right size relative to one another — AD moves up by
precisely the amount that makes the new AS cross it at the new natural rate. No policy
intervention, no price movement, no gap. Fig. 7 draws this as $E\to E'$ with nothing else
happening.

**Why exactly?** Because $dr_n=\sigma^{-1}(d\bar y_n-dy_n)=0$. The natural real rate is
a function of expected *growth*, and a permanent level shift in productivity leaves
growth unchanged. Holding $i$ fixed is therefore already optimal: monetary policy should
be **neutral**.

That is a general lesson worth extracting: what monetary policy tracks is not the level
of technology but the **gap between future and current** natural output. A shock that
raises both equally is invisible to it.

## 5.3 Optimism about the future: $\bar a\uparrow$ only (§6.3, Fig. 8)

Read as either a genuine future improvement or a belief about one — the model cannot
tell them apart, which is itself the point. The mirror case, pessimism, runs the same
algebra with the sign flipped and is the starting gun for [[08-liquidity-trap]].

**Curves.** AS does **not** move: current productivity is unchanged, so $y_n$ is
unchanged. AD shifts up, through $\bar y_n$.

**Equilibrium.** With $dy_n=0$:

$$dy=d(y-y_n)=\frac{d\bar y_n}{1+\sigma\kappa}>0,\qquad
dp=\frac{\kappa\,d\bar y_n}{1+\sigma\kappa}>0$$

Output and prices both rise, and the whole of the output response *is* a gap: output is
above natural **and** above efficient, since $y_e$ did not move either. The economy is
overheating on the strength of a forecast.

**Optimal policy.** Set the gap to zero: $d\bar y_n-\sigma\,di=0$, so

$$\boxed{di=\frac{d\bar y_n}{\sigma}>0}$$

**Restrictive** — and the same number as $dr_n=+\sigma^{-1}d\bar y_n$. Fig. 8: raising
$i$ walks AD back down to $E$.

## 5.4 The three cases in one table

| Case | $dy_n$ | $d\bar y_n$ | AS | AD | Gap without policy | $dp$ | $dr_n$ | Optimal $di$ |
|---|---|---|---|---|---|---|---|---|
| §6.1 temporary | $+$ | $0$ | down | still | **negative** | $-$ | $-\sigma^{-1}dy_n$ | **cut** |
| §6.2 permanent | $+$ | $+$ (equal) | down | up | zero | $0$ | $0$ | **nothing** |
| §6.3 expected | $0$ | $+$ | still | up | **positive** | $+$ | $+\sigma^{-1}d\bar y_n$ | **raise** |

Three shocks to the same variable, three different signs for the policy response. Any
answer of the form "positive productivity shock ⇒ expansionary policy" is wrong two
times out of three. The rule that is always right: **move $i$ to the new $r_n$**.

## 5.5 Why there is no trade-off here — stated precisely

The loss function derived in [[10-optimal-policy]] penalises two things, $(p-p^e)^2$ and
$(y-y_e)^2$. By (17), $p-p^e=\kappa(y-y_n)$. So both terms vanish at the same time if
and only if $y$ can be made equal to $y_n$ **and** to $y_e$ simultaneously — that is, iff

$$y_n=y_e \iff \mu \text{ unchanged}$$

Productivity shocks do not touch $\mu$, and by §3.4 they move $y_n$ and $y_e$ by the same
amount. One instrument, $i$, therefore hits two targets. This is the **divine
coincidence**, and here it is not a coincidence at all but a consequence of the shock
being *efficient*.

Two conditions sit underneath it, and both are worth naming because exam questions live
in them:

1. **Wage flexibility.** Footnote 9 (p. 513): "An important assumption here is that of
   wage flexibility. Trade-offs will occur with sticky wages." With sticky wages a
   productivity shock moves the efficient allocation without letting the real wage get
   there, and the coincidence breaks.
2. **An efficient steady state.** The loss function is an approximation around
   $\mu=0$ (footnote 21, p. 522). With a distorted steady state the welfare-relevant
   target is no longer $y_e$ and the clean result weakens.
