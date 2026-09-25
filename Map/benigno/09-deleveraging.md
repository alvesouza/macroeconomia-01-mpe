---
tags: [benigno, adas, aula-09, desalavancagem, eggertsson-krugman, efeito-fisher]
date: 2026-09-15
---

# 9. Debt deleveraging: an AD curve that can slope up

**Article: §10, equations (24)–(32), Figure 13, printed pages 518–521.** Up:
[[00-index]] · Prev: [[08-liquidity-trap]] · Next: [[10-optimal-policy]]

The model of Eggertsson and Krugman (2012), compressed into the same two-curve diagram.
Everything here follows from one change: **some households are at a borrowing limit, so
their Euler equation does not hold.** The consequences are an AD curve with a new slope,
three paradoxes, and multipliers above one.

> **Companion:** [When Demand Slopes Up](companion-deleveraging.html) — raise initial debt past
> the inversion threshold and watch AD rotate through vertical; the paradox of toil then shows
> as a favourable AS shift moving output the wrong way.

---

## 9.1 Two types

Fraction $\chi$ are **savers**, $1-\chi$ are **borrowers**, each maximising

$$u(C_j)-v(L_j)+\beta_j\left\{u(\bar C_j)-v(\bar L_j)\right\},\qquad j=b,s \tag{24}$$

with $\beta_b<\beta_s$: borrowers are more impatient, which is why they borrow at all.
Flow budget constraints, with $B_j>0$ denoting **debt**:

$$B_j=(1+i_0)B_{0,j}+PC_j-W_jL_j-\Pi_j+T_j \tag{25}$$

$$B_{2,j}=(1+i)B_j+\bar P\bar C_j-\bar W_j\bar L_j-\bar\Pi_j+\bar T_j \tag{26}$$

Note these are *flow* constraints, one per period, not a single lifetime constraint as in
[[01-household-and-ad]]. That is forced: with a borrowing limit the two periods can no
longer be collapsed. And profits $\Pi_j$ are now separated from taxes $T_j$ — the
distribution of both across types will matter.

The debt limit, a safe-debt threshold that applies in each period:

$$\frac{(1+r)B_j}{P}\le D \tag{27}$$

**The shock of interest is a fall in $D$ from $D_0$.** The article is candid that it is
unmodelled: "For reasons not modelled here, borrowers suddenly realize that they have to
reduce their debt exposure."

Assume borrowers start constrained (they are impatient) and stay constrained through the
deleveraging. Then **their Euler equation is replaced by (27) holding with equality**:
their consumption is whatever the budget constraint allows given the maximum debt they
may carry. This is the single modelling step that drives the section.

## 9.2 Two tricks that keep it tractable

**Cobb–Douglas labour.** $Y=AL$ with $L=L_s^{\chi}L_b^{1-\chi}$, and a matching wage index
$W=W_s^{\chi}W_b^{1-\chi}$, so that each type's compensation moves with total compensation,
$W_jL_j=WL$ (p. 519). Consequence, used later: labour income and profits together exhaust
output, $W_jL_j+\Pi_j=PY$.

**Exponential utility.** $u(C_j)=1-\exp(-zC_j)$, $z>0$. This is the assumption that makes
aggregation work, and it is worth seeing why. Take the intratemporal condition for each
type,

$$\frac{v_l(L_j)}{u_c(C_j)}=\frac{W_j}{P} \tag{28}$$

and average with weights $\chi$ and $1-\chi$. With $u_c(C_j)=z\exp(-zC_j)$, the marginal
utilities multiply into the *sum* of consumptions rather than a messy average:

$$\frac{L^{\eta}}{\exp\left[-z\left(\chi C_s+(1-\chi)C_b\right)\right]}=\frac{W}{P} \tag{29}$$

Only **aggregate** consumption appears. That is why, using $Y=AL$,
$Y=\chi C_s+(1-\chi)C_b+G$ and long-run mark-up pricing $P=(1+\mu_\theta)W/A$:

$$\frac{(Y_n/A)^{\eta}}{\exp\left[-z(Y_n-G)\right]}=\frac{A}{1+\mu_\theta}$$

which log-linearises into **exactly eq. (15) again**, with
$\tilde\sigma\equiv1/(z\tilde Y)$. So:

> The natural level of output is **independent of the distribution of wealth**, and the
> short-run AS curve is unchanged, still $p-p^e=\kappa(y-y_n)$.

All the action is on the demand side. (With isoelastic utility this would fail, and the
model would not fit on one diagram.)

## 9.3 The new AD curve

Savers are unconstrained, so their Euler equation survives — in **levels**, because
exponential utility makes the relevant object the level of consumption, not its log:

$$\bar C_s=C_s-\tilde\sigma\left[i-(\bar p-p)-\rho\right] \tag{30}$$

Take the resource constraint in both periods, difference them, and substitute (30):

$$y=g+\left(\bar y_n-\bar g\right)-\chi\tilde\sigma\left[i-(\bar p-p)-\rho\right]
+\left(1-\chi\right)\frac{C_b-\bar C_b}{\tilde Y} \tag{31}$$

Two changes from (21), and both matter:

- the interest-rate term is scaled by $\chi$ — **only savers respond to the real rate**,
  so the conventional monetary channel is weaker the more borrowers there are;
- a new shifter appears: the borrowers' consumption *profile* $C_b-\bar C_b$. If
  deleveraging forces them to cut today relative to tomorrow, aggregate demand falls for
  reasons no interest rate authorised.

Now solve for $C_b$. With (27) binding in both periods, (25) and (26) give

$$C_b=-\frac{(1+i_0)P_0D_0}{(1+r_0)P}+\frac{D}{1+r}+Y-T_b,
\qquad
\bar C_b=-\frac{(1+i)PD}{(1+r)\bar P}+\frac{\bar D}{1+\bar r}+\bar Y-\bar T_b$$

using $W_jL_j+\Pi_j=PY$. Read the first: a borrower's consumption is income, minus the
real value of inherited debt service, plus what it is newly allowed to borrow, minus
taxes. Approximate both around the initial debt position, substitute into (31), and the
short-run AD curve takes its final form:

$$\boxed{\;y=y_n-\varphi\left[i-(\bar p_n-p)-\rho\right]
+\frac{1}{\chi}\Big[(g-\bar g)-(1-\chi)(\tau_b-\bar\tau_b)\Big]
+\frac{(1-\chi)}{\chi}\Big[\hat d+d_0\left(p-p^e\right)\Big]\;} \tag{32}$$

$$\varphi\equiv\frac{\sigma\chi+(1-\chi)d_0\beta}{\chi}\;\ge0,\qquad
d_0\equiv\frac{D_0}{\tilde Y},\quad
\tau_b\equiv\frac{T_b-\tilde T_b}{\tilde Y},\quad
\hat d\equiv\frac{D-D_0}{\tilde Y}$$

## 9.4 The slope: two new channels, and the Fisher effect wins

Differentiate (32) with respect to $p$. The interest term contributes $-\varphi$; the new
debt term contributes $+(1-\chi)d_0/\chi$:

$$\frac{dy}{dp}=-\varphi+\frac{(1-\chi)d_0}{\chi}
=-\sigma-\frac{(1-\chi)d_0\beta}{\chi}+\frac{(1-\chi)d_0}{\chi}
=-\underbrace{\left[\sigma-\frac{d_0(1-\beta)(1-\chi)}{\chi}\right]}_{\textstyle \equiv\,\varpi}$$

$$\boxed{\;\frac{dy}{dp}=-\varpi,\qquad
\left.\frac{dp}{dy}\right|_{AD}=-\frac{1}{\varpi}\;}$$

The two channels inside $\varpi$, both running through the borrowers:

| Channel | Direction | Mechanism |
|---|---|---|
| **Borrowing limit** | flattens AD | $p\uparrow$ raises the real rate, so $D/(1+r)$ — what may be safely borrowed today — falls; borrowers consume less |
| **Fisher effect** | steepens AD | $p\uparrow$ cuts the *real value of inherited nominal debt* $P_0D_0/P$; borrowers consume more |

The Fisher channel dominates, because $d_0(1-\beta)(1-\chi)/\chi>0$, which makes
$\varpi<\sigma$ and so $|-1/\varpi|>|-1/\sigma|$: **for given $\sigma$, debt-constrained
agents make AD steeper.** And the term can be large enough to flip the sign entirely:

$$\varpi<0 \iff d_0>\frac{\sigma\chi}{(1-\beta)(1-\chi)}$$

i.e. **AD slopes upward when initial debt $d_0$ is high or the saver share $\chi$ is
low.** Under the Eggertsson–Krugman assumption that inflation between short and long run
is tied to zero — so the $(\bar p-p)$ channel is switched off and only Fisher survives —
the slope is positive unambiguously. That is what Fig. 13 (p. 521) draws, with the caveat
of footnote 19: AS must be flatter than AD for the equilibrium to be stable.

**In this regime lower prices are contractionary.** They raise the real burden of
nominal debt, cut borrowers' consumption, and cut output.

## 9.5 Deleveraging and the three paradoxes

A deleveraging shock is $\hat d<0$ in (32): a **left shift** of AD. Output and prices
fall, and the fall can be deep enough to put the economy in the liquidity trap of
[[08-liquidity-trap]], where cutting $i$ to zero is not enough to return to $E$.

Once AD slopes up, three things that are expansionary in normal times reverse sign:

1. **Paradox of thrift.** Borrowers save more to pay down debt; aggregate demand and
   income fall; realised saving ends up *lower*. The Keynesian paradox, recovered in a
   microfounded model.
2. **Paradox of toil.** A downward shift of AS — from a temporary productivity gain, a
   lower mark-up, or a *tax cut that should encourage work* — is **contractionary** here.
   Along an upward-sloping AD, pushing prices down destroys borrower consumption faster
   than cheaper output creates demand.
3. **Paradox of flexibility.** *More* price flexibility — a steeper AS, i.e. larger
   $\kappa$ — produces a **larger** output contraction, because it delivers a larger fall
   in prices and so a larger increase in the real debt burden.

> **The escape clause, footnote 20 (p. 520), and it is worth knowing.** If the long-run
> price level is well anchored *irrespective of* short-run prices, AD must be drawn
> downward-sloping for a given future price level — and then **the paradoxes of toil and
> flexibility disappear.** The paradoxes are not properties of debt alone; they need the
> expectation channel to be switched off. A central bank with a credible long-run price
> level target is therefore doing paradox prevention.

## 9.6 Policy: a stronger exit and a real multiplier

**Monetary.** The §8 exit — commit to a higher long-run price level — works here
*reinforced*, because the coefficient $\varphi$ in (32) exceeds $\sigma$. Raising $\bar p$
lowers the real rate, which raises savers' consumption **and** relieves borrowers, whose
debt service falls. Two beneficiaries instead of one.

**Fiscal.** Two structural changes:

- **Ricardian equivalence fails.** $\tau_b$ — lump-sum transfers *to the borrowers* —
  appears in (32). Who is taxed now matters, and so does how spending is financed, because
  a euro taken from a constrained agent is a euro of lost consumption while a euro taken
  from a saver is largely absorbed by saving.
- **The multiplier exceeds one**, which §8's Table 2 ruled out by construction. With
  long-run prices well anchored, the multiplier on short-run government spending is

$$\boxed{\;\frac{\dfrac{1}{\chi}+\dfrac{\varpi\kappa}{1+\sigma\eta}}{1+\varpi\kappa}\;}$$

and when long-run inflation is instead tied to zero,

$$\boxed{\;\frac{1-\dfrac{d_0(1-\chi)\kappa}{1+\sigma\eta}}{\chi-d_0(1-\chi)\kappa}\;}$$

Evaluated at the article's calibration — $\alpha=0.66$, $\sigma=0.5$, $\eta=0.2$,
$d_0=1.2$ (debt at 120% of GDP) — and reproduced in `check_multipliers.py`:

| Case | Borrowers $1-\chi$ | Multiplier |
|---|---|---|
| Anchored long-run prices | $1/3$ | **1.29** |
| Anchored long-run prices | $1/2$ | **1.62** |
| Zero long-run inflation | $1/3$ | **2.75** |

Why so big. In normal times the spending multiplier is held below one by two leaks:
prices rise, the real rate rises, and private consumption is crowded out. In the trap the
nominal rate cannot rise, and a share $1-\chi$ of households is constrained and spends
every euro of income. Both leaks are plugged. In the zero-inflation case the denominator
$\chi-d_0(1-\chi)\kappa$ is small and shrinking in $d_0$ — the multiplier grows with the
debt stock, and the formula is explosive near $\chi=d_0(1-\chi)\kappa$, which is the same
condition as an AD curve steeper than AS: exactly where footnote 19 says the equilibrium
stops being stable. Numbers from that region should not be quoted.

## 9.7 The one-paragraph summary

Put a borrowing constraint on a third of households and three things change and one does
not. The AS curve does not change at all, thanks to exponential utility. The AD curve
gets steeper, possibly upward-sloping, because prices now move the real value of nominal
debt. Deleveraging becomes an autonomous demand shock that no interest rate authorised.
And fiscal policy, weak and sub-unitary in normal times, becomes the powerful instrument
of the textbook Keynesian story — for a reason the textbook does not give: the agents who
receive the spending cannot smooth it.
