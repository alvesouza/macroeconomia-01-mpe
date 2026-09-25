---
tags: [aula-04, kurlat-cap-06, efeito-renda, efeito-substituicao, slutsky, juros, derivacao]
date: 2026-09-18
---

# 3. Why a higher interest rate has an ambiguous effect on saving

**Kurlat §6.2, printed pages 112–115.** Up: [[00-index]] ·
Prev: [[02-two-period-problem]] · Next: [[04-permanent-income]]

> **Companion:** [Two Periods, One Line](companion-euler.html) — raise $r$ and watch the budget
> line pivot about the endowment, with the Hicksian decomposition drawn as the compensated line.

"Higher interest rates encourage saving" is the single most common false statement in this
material — trap 3 in [[04_consumo_poupanca]]. It is false because a higher interest rate makes a
saver *richer*, and richer households consume more, including today. This note decomposes the
effect exactly and says when each side wins.

---

## 3.1 The two channels

A rise in $r$ does two things to a household that is currently saving.

**Substitution effect.** Future consumption becomes cheaper relative to present consumption —
its price $1/(1+r)$ falls. Substitute toward it: consume less today, **save more**. This
channel always pushes saving up, for savers and borrowers alike, because it is about relative
prices and nothing else.

**Income (wealth) effect.** The household's lifetime wealth changes, and the *sign depends on
which side of the endowment it sits*:

$$W = y_1+\frac{y_2}{1+r} \qquad\Longrightarrow\qquad \frac{\partial W}{\partial r} = -\frac{y_2}{(1+r)^2}<0$$

At first sight $W$ always falls. But $W$ measured this way is not the right welfare object for a
saver, and the correct statement is about the *attainable* consumption bundle. The clean way to
see it: the budget line pivots about the endowment $(y_1,y_2)$, which is always affordable.

- A **lender** ($c_1<y_1$) consumes at a point to the left of the endowment, where the new,
  steeper line lies **above** the old one. Their feasible set has expanded: they are **richer**.
  Being richer, they consume more of both goods, including $c_1$ — which **reduces** saving.
- A **borrower** ($c_1>y_1$) sits to the right of the endowment, where the new line lies
  **below** the old. They are **poorer**, so they cut consumption today — which **increases**
  saving (reduces borrowing).

$$\boxed{\;\text{lender: income effect opposes substitution} \qquad
\text{borrower: income effect reinforces substitution}\;}$$

**Hence:** for a **borrower** the effect of $r$ on saving is unambiguously positive. For a
**lender** it is ambiguous, and which side wins is a quantitative question about $\sigma$.

## 3.2 The decomposition, done exactly

Work with the CRRA closed form from [[02-two-period-problem]] §2.4:

$$c_1 = \frac{W}{D}, \qquad D \equiv 1+\beta^{1/\sigma}(1+r)^{\frac{1}{\sigma}-1},
\qquad W = y_1+\frac{y_2}{1+r}$$

Take logs and differentiate with respect to $\ln(1+r)$:

$$\frac{d\ln c_1}{d\ln(1+r)} = \underbrace{\frac{d\ln W}{d\ln(1+r)}}_{\text{wealth}}
- \underbrace{\frac{d\ln D}{d\ln(1+r)}}_{\text{substitution}}$$

**The wealth term.** $\dfrac{dW}{d(1+r)} = -\dfrac{y_2}{(1+r)^2}$, so

$$\frac{d\ln W}{d\ln(1+r)} = -\frac{y_2/(1+r)}{W} \;\equiv\; -\omega$$

where $\omega\in(0,1)$ is the **share of lifetime wealth coming from future income**. This is
the natural measure of how "back-loaded" the household's income is, and it is exactly the
statistic that decides the sign below.

**The substitution term.**

$$\frac{d\ln D}{d\ln(1+r)}
= \frac{\beta^{1/\sigma}(1+r)^{\frac{1}{\sigma}-1}}{D}\left(\frac{1}{\sigma}-1\right)
= \theta\left(\frac{1}{\sigma}-1\right)$$

where $\theta\equiv 1-1/D\in(0,1)$ is the share of wealth consumed in period 2.

Putting them together:

$$\boxed{\;\frac{d\ln c_1}{d\ln(1+r)} = -\omega-\theta\left(\frac{1}{\sigma}-1\right)\;}$$

and saving is $s_1=y_1-c_1$, so $\dfrac{ds_1}{d\ln(1+r)} = -c_1\dfrac{d\ln c_1}{d\ln(1+r)}$,
whose sign is the *opposite*.

### Reading the formula

**Case $\sigma=1$ (log).** The second term vanishes, and $d\ln c_1/d\ln(1+r)=-\omega$.
Consumption falls, and it falls **only** because the present value of future income fell. Given
$W$, $r$ has no effect at all — the income and substitution effects on the *allocation* cancel
exactly, which is the property noted in [[02-two-period-problem]] §2.4. This is the knife-edge
benchmark, and it is why log utility is the default in this course.

**Case $\sigma<1$ (EIS $>1$).** $\frac{1}{\sigma}-1>0$, so the second term is negative too:
consumption falls by more than the wealth effect alone. **Substitution dominates** and saving
rises with $r$.

**Case $\sigma>1$ (EIS $<1$).** $\frac{1}{\sigma}-1<0$, so the second term is positive and
offsets the wealth term. If $\sigma$ is large enough, $c_1$ **rises** with $r$ and saving
**falls**. The household is so unwilling to tilt its path that a higher return simply makes it
richer and it spends the proceeds.

**A special case worth knowing.** If the household has no second-period income ($y_2=0$, so
$\omega=0$ — a retiree living off assets, or the "cake-eating" case), the wealth term vanishes
and the sign is entirely the substitution term: saving rises with $r$ iff $\sigma<1$. Conversely
if $y_1=0$ the household must borrow and both effects push the same way.

Verified numerically in `check_consumption.py`, which computes the total effect by solving the
problem at two interest rates and checks it against the boxed formula, then splits it into
Hicksian substitution and income components by compensating wealth.

## 3.3 The Slutsky version

For those who prefer the standard consumer-theory apparatus. With the endowment $(y_1,y_2)$
fixed and price $p\equiv 1/(1+r)$ for good 2, the Slutsky equation in endowment form is

$$\frac{\partial c_1}{\partial p} = \underbrace{\left.\frac{\partial c_1}{\partial p}\right|_{\text{comp}}}_{\text{substitution, }>0\text{ for }c_1}
+ \underbrace{\left(y_2-c_2\right)\frac{\partial c_1}{\partial W}}_{\text{endowment income effect}}$$

The second term carries the factor $y_2-c_2$, which is **negative for a lender** (who consumes
more than their period-2 income) and **positive for a borrower**. That factor is the entire
content of §3.1, stated in the general form: the income effect of a price change is
proportional to the household's *net trade* in that good. A household that neither borrows nor
lends has no income effect at all, and for it the substitution effect is the whole story.

## 3.4 The empirical question, and why it is unsettled

The elasticity of saving with respect to the interest rate is one of the most-estimated and
least-agreed numbers in macroeconomics. Estimates of the EIS $1/\sigma$ run from near zero
(Hall, 1988, using aggregate consumption) to around one or above (Attanasio and Weber, using
micro data and correcting for aggregation bias). Standard macro calibrations use $\sigma$
between 1 and 2, which places the economy near or slightly on the "saving falls" side of the
knife-edge.

**Why it matters beyond this session.** The entire effect of monetary policy on demand in
[[08_adas_microfundamentos]] runs through this elasticity: $\sigma$ there is the slope parameter
of the AD curve, and a low EIS means a steep AD curve and a weak interest-rate channel. So the
unsettled empirical question about household saving is the same unsettled question about how
much a central bank can do. It is worth saying that out loud in an exam answer.

## 3.5 The policy corollary

A tax incentive for saving — a tax-exempt retirement account, say — raises the after-tax return
$r$. The analysis above says the effect on national saving is:

- unambiguously positive for **constrained or borrowing** households, who are precisely the
  households least likely to hold such accounts;
- **ambiguous** for lenders, who are precisely the households that do;
- and **zero on the allocation** in the log benchmark.

Add the point that such schemes are typically funded by forgone tax revenue, which is negative
public saving, and the net effect on *national* saving can easily be negative. This is the
standard critique of savings-incentive policy, and it follows from a decomposition rather than
from an opinion.

## 3.6 What to be able to do, cold

1. Name the two channels and give the sign of each for a lender and for a borrower.
2. Explain why the budget line pivots about the endowment, and derive the welfare consequence
   from that geometry alone.
3. Derive $d\ln c_1/d\ln(1+r)=-\omega-\theta(1/\sigma-1)$ and read off all three cases.
4. State why log is the knife-edge, in terms of the allocation rather than the level.
5. Write the Slutsky equation in endowment form and identify the net-trade factor.
6. Give the policy corollary and the reason a saving incentive may lower national saving.

Practice: Kurlat ch. 6, Exercises 6.3 and 6.4 (p. 124). Worked in
[[Resolucao/kurlat_solutions_ch06|ch06]].
