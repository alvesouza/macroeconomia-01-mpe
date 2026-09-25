---
tags: [benigno, adas, aula-09, armadilha-de-liquidez, zlb, expectativas]
date: 2026-09-15
---

# 8. The liquidity trap: the $\mathrm{AD}_0$ locus and the way out

**Article: §9, Figures 11–12, printed pages 516–518.** Up: [[00-index]] ·
Prev: [[07-fiscal-multipliers]] · Next: [[09-deleveraging]]

Two claims to establish. First, a zero bound on the nominal rate puts a *ceiling* on the
AD curve, and the model says exactly where it is. Second, even with the conventional
instrument exhausted, the model still has an instrument — and it is visible in the
algebra of [[04-equilibrium-geometry]] as the slot that $i$ and $\bar p$ share.

> **Companion:** [The Floor Under Demand](companion-zlb.html) — push long-run natural output
> down until the natural rate goes negative and the zero-rate ceiling binds, then buy the gap
> back with the long-run price level alone.

---

## 8.1 Why there is a bound at all

In a model with no money, why can't $i$ be $-5\%$? The article's answer (p. 517): because
otherwise agents could borrow to run infinite consumption. Footnote 11 is more careful
and worth reading, because it undercuts the naive story: in a genuinely cashless economy
money pays the same rate as bonds and there is no zero bound; the bound is the
*remuneration of money*, and it is zero only because currency pays zero and retains its
store-of-value function. So:

$$i\ge 0$$

and a **liquidity trap** is the state $i=0$ in which conventional monetary policy has run
out of its standard tool.

## 8.2 The $\mathrm{AD}_0$ locus

Put $i=0$ in the AD curve (21):

$$\boxed{\;\mathrm{AD}_0:\qquad y=\bar y_n+(g-\bar g)+\sigma\left[(\bar p-p)+(\bar\tau_c-\tau_c)+\rho\right]\;}$$

Same slope $-1/\sigma$, the highest position the AD curve can occupy for given
$\bar p$, $g$ and taxes. Every expansionary interest-rate move shifts AD up *towards*
$\mathrm{AD}_0$ and can never go past it (Fig. 11, p. 518).

Using the closed form of [[04-equilibrium-geometry]] with $i=0$:

$$\left.y-y_n\right|_{i=0}=\frac{\sigma}{1+\sigma\kappa}\Big[r_n+(\bar p-p^e)\Big]$$

**Read that as the diagnostic.** With long-run prices anchored at $p^e$ — the standard
assumption of a credible, non-committal central bank — the best attainable gap is
$\sigma r_n/(1+\sigma\kappa)$. Hence:

$$r_n\ge0\;\Longrightarrow\;\text{the gap can be closed};\qquad
\boxed{r_n<0\;\Longrightarrow\;\text{the economy is stuck below potential}}$$

The trap is not fundamentally about the interest rate. It is about the **natural real
rate being negative**, and the nominal floor then preventing the actual real rate from
reaching it.

## 8.3 Where a negative $r_n$ comes from

$$r_n=\rho+\sigma^{-1}\left(\bar y_n-y_n\right)+\sigma^{-1}(g-\bar g)+(\bar\tau_c-\tau_c)$$

The dominant term is the second. Following Krugman (1998), the two sources the article
names (p. 517):

- **Poor long-run growth prospects**: $\bar y_n$ low relative to $y_n$, i.e. pessimism —
  which is exactly §6.3 run in reverse. Note the symmetry: optimism about the future
  required a *restrictive* response; pessimism deep enough requires an expansionary one
  the floor forbids.
- **Forced deleveraging**: some agents must cut spending regardless of the interest rate,
  which is [[09-deleveraging]].

Fig. 12 (p. 518) draws it: AD falls *and* $\mathrm{AD}_0$ falls with it, since both
contain $\bar y_n$. Cutting $i$ to zero reaches $E'$ at best, where — in the article's
words — "the real interest rate is too high, household consumption too low and the
economy still in a slump with output far below potential".

## 8.4 The exit: the instrument that is left

From [[04-equilibrium-geometry]] §4.4, $-\sigma\,di$ and $+\sigma\,d\bar p$ occupy the
**same slot**. So when $di$ is unavailable, use $d\bar p$. Solving for the commitment
that closes the gap at $i=0$:

$$\boxed{\;\bar p-p^e=-r_n\;}$$

A promise to deliver a long-run price level higher by exactly the absolute value of the
natural real rate. The mechanism, stated carefully: raising $\bar p$ raises expected
inflation $(\bar p-p)$, which lowers the **real** rate at an unchanged zero nominal rate,
which raises consumption. Both AD and $\mathrm{AD}_0$ shift up, and $E''$ in Fig. 12
becomes reachable.

Three things this exit needs, none of them algebraic:

1. **Credibility.** It is a promise about a future the central bank will be tempted to
   renege on once the trap is over. This is why the literature (Eggertsson and Woodford,
   2003) treats it as a commitment problem and not a choice of instrument.
2. **A transmission story.** The article names quantitative easing (p. 517): expand the
   balance sheet and inject liquidity until the price level turns, since the price index
   is the value of money in terms of goods. And it lists Bernanke's (2002) five
   instruments: expand the scale and menu of asset purchases; commit to zero rates for a
   long period; announce and enforce yield ceilings on long maturities with unlimited
   purchases; offer fixed-term loans to banks at near-zero rates against a wide
   collateral set; buy foreign debt.
3. **A substitute, if prices will not move.** By [[01-household-and-ad]] §1.5,
   $(\bar\tau_c-\tau_c)$ sits in the same bracket as $(\bar p-p)$. A pre-announced path
   of *rising consumption taxes* is an expected-inflation policy run by the treasury.

## 8.5 Fiscal policy in the trap: which instrument, and why not the obvious one

Apply (22) and (23) from [[07-fiscal-multipliers]]. Two desiderata — raise output and
narrow the gap — and the two lists nearly coincide:

| Instrument | Raises $y$? (22) | Narrows the gap? (23) |
|---|---|---|
| $g\uparrow$ | yes | yes |
| $\bar g\downarrow$ | yes | yes |
| $\tau\downarrow$ (sales/payroll, now) | **yes** | **no — widens it** |
| $\bar\tau\downarrow$ (sales/payroll, later) | yes | yes |
| $\tau_c\downarrow$ (consumption tax now) | yes | yes |
| $\bar\tau_c\uparrow$ (consumption tax later) | yes | yes |

**One policy fails the pair: a current cut in sales and payroll taxes.** It raises output
while worsening the gap, because it raises the natural rate by more than it raises
output. The article says it "should be avoided" (p. 517), and footnote 14 notes that
Eggertsson (2011), in a fully dynamic model, finds the tax-cut multiplier turning
*negative* once the rate hits zero while the spending multiplier rises above one.

Among the survivors, the article's preference is the surprising one: **long-run
instruments beat short-run ones** (pp. 517–518). Three reasons, each mapping onto a curve:

1. **$g\uparrow$ pushes prices down; $\bar g\downarrow$ does not.** A short-run spending
   rise also shifts AS down (it raises $y_n$), which holds prices down. In a slump with
   deflation, downward nominal wage rigidity and nominal debt, lower prices worsen balance
   sheets — the theme of [[09-deleveraging]]. A cut in *future* spending moves AD only.
2. **Composition.** $g\uparrow$ crowds out private consumption; $\bar g\downarrow$ raises
   it, by raising $\bar c_n$. In a slump driven by a consumption collapse, that is the
   margin one wants to move.
3. **Sustainability.** A short-run stimulus only works if it is not permanent (by (23),
   permanent fiscal policy has no gap effect at all), and if lump-sum financing is
   unavailable it must be paid for with future taxes — and higher future taxes are among
   the *most* contractionary items in (22).

The resulting recommendation: a package of **future** fiscal actions with expansionary
effects on current consumption — cut future taxes, cut future spending, raise future
consumption taxes — all of which shift AD up, none of which push prices down, and all of
which respect the government's budget constraint.

## 8.6 The IS-LM comparison, made precise

The traditional Keynesian version has the LM curve flat at the left, so shifts in IS move
income without moving the interest rate, and monetary expansion is absorbed without
effect. The conclusion drawn from it is that **fiscal policy is the only effective
instrument** in a trap.

This model reaches a different conclusion from the same starting point. The nominal rate
is stuck, but demand depends on the *real* rate, and the real rate depends on an
expectation the central bank can still act on. So monetary policy is not out of the game;
it has changed instrument, from $i$ to $\bar p$. And fiscal policy, when used, is best
used through expectations too — which is the same insight wearing a different hat.
