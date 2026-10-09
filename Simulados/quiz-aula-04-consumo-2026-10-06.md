---
quiz: "Macro I — Session 4: Consumption and Saving (hard)"
tags:
  static: "Static model and the Keynesian function"
  euler: "Two-period problem and the Euler equation"
  ise: "Income and substitution effects"
  pih: "Permanent income"
  ric: "Ricardian equivalence and borrowing constraints"
---

## static

Q: Each household consumes a fixed share $k$ of its permanent income, and measured income is permanent income plus a transitory part uncorrelated with it. Regressing consumption on measured income across households, year by year, in a growing economy, what is found?
- Slopes equal to $k$ and zero intercepts in every year, since the transitory part averages out across households within each year.
- Slopes below $k$ and positive intercepts that rise over time, so each year's APC falls with income while the long-run APC stays at $k$.
- Slopes above $k$ and negative intercepts, since households having a good year spend their windfall, so the APC rises with income.
- Slopes below $k$ and a positive intercept that is the same every year, so the aggregate APC falls over time as the economy gets richer.
<!-- YW5zOjE= -->
> With $C=kY^P$ and $Y=Y^P+e$, the within-year slope is $\operatorname{cov}(C,Y)/\operatorname{var}(Y)=k\lambda$, where $\lambda=\operatorname{var}(Y^P)/\operatorname{var}(Y)<1$. The intercept is $k(1-\lambda)\bar Y^P>0$. High measured income partly means a good year, and a good year is mostly saved. The line passes through $(\bar Y^P,k\bar Y^P)$, so it sits on the long-run ray $C=kY$, and its intercept grows with $\bar Y^P$. That is the Kuznets puzzle solved: the APC falls in the cross-section but is constant in the time series. Option D keeps the Keynesian intercept fixed, so it predicts the rising saving rate that Kuznets did not find. Option A ignores the attenuation from $e$.
> Ref: Kurlat (2020), cap. 6, §6.1 (pp. 103–105); Map [[01-keynesian-and-the-problem]]
> Similar: Kurlat, Exercício 6.1 (p. 123); Lista 3

Q: A function $C=\bar C+\mathrm{mpc}\cdot Y$ is estimated on data where most income changes were temporary tax rebates to households that borrow and lend freely. It is then used to forecast a permanent tax cut. Which assessment is right?
- The forecast is accurate, because $\mathrm{mpc}$ is a structural preference parameter that does not depend on how persistent the income change is.
- The forecast overstates the response, because the estimated $\mathrm{mpc}$ mixes in hand-to-mouth behaviour that a permanent cut does not trigger.
- The forecast is accurate only if the interest rate equals the discount rate, since the transitory and permanent $\mathrm{mpc}$ then coincide at one.
- The forecast understates the response, because the estimated $\mathrm{mpc}$ is the low MPC out of transitory income, not the near-one permanent MPC.
<!-- YW5zOjM= -->
> For unconstrained households, consumption depends on wealth $W$. A temporary rebate raises $W$ by the rebate alone, so its MPC is small. A permanent cut raises $W$ by the present value of the whole stream, and its MPC is near one. A regression on rebate-driven data recovers the small number. This is the Lucas critique applied to the consumption function: the coefficient of a rule depends on the policy regime that generated the data. Option B invents hand-to-mouth households that the stem rules out. Option C is wrong because $r=\rho$ makes the *permanent* MPC exactly one, while the transitory MPC stays well below one.
> Ref: Kurlat (2020), cap. 6, §6.1–§6.2 (pp. 103–105, 115–120); Map [[01-keynesian-and-the-problem]]; [[04-permanent-income]]
> Similar: Kurlat, Exercício 6.1 (p. 123); Exercício 6.6 (p. 125)

## euler

Q: A household maximises $u(c_1)+\beta u(c_2)$ with $u(c)=c^{1-\sigma}/(1-\sigma)$, $\sigma>0$, subject to $c_1+c_2/(1+r)=W$, where $W=y_1+y_2/(1+r)$, $y_t$ is income, $\beta$ the discount factor and $r$ the real rate. What is $c_1$?
- $c_1=\dfrac{W}{1+\beta^{1/\sigma}(1+r)^{\frac{1}{\sigma}-1}}$, so holding $W$ fixed, $r$ drops out of $c_1$ only when $\sigma=1$.
- $c_1=\dfrac{W}{1+\beta^{1/\sigma}(1+r)^{\frac{1}{\sigma}}}$, so holding $W$ fixed, a higher $r$ always lowers $c_1$ for any $\sigma$.
- $c_1=\dfrac{W}{1+\beta^{\sigma}(1+r)^{\sigma-1}}$, so holding $W$ fixed, $r$ drops out of $c_1$ only when $\sigma=1$.
- $c_1=\dfrac{W}{1+\beta^{1/\sigma}(1+r)^{1-\frac{1}{\sigma}}}$, so holding $W$ fixed, a higher $r$ raises $c_1$ when $\sigma<1$.
<!-- YW5zOjA= -->
> The Euler equation is $c_1^{-\sigma}=\beta(1+r)c_2^{-\sigma}$, so $c_2=[\beta(1+r)]^{1/\sigma}c_1$. Substitute into the budget: $c_1+\beta^{1/\sigma}(1+r)^{1/\sigma}c_1/(1+r)=W$, and $(1+r)^{1/\sigma}/(1+r)=(1+r)^{\frac1\sigma-1}$. At $\sigma=1$ the exponent is zero and $c_1=W/(1+\beta)$. Option B forgets to divide $c_2$ by $1+r$ in the budget. Option C uses $\sigma$ where the Euler equation gives $1/\sigma$: it confuses risk aversion with the EIS. Option D flips the sign of the exponent.
> Ref: Kurlat (2020), cap. 6, §6.2 (pp. 105–112); Map [[02-two-period-problem]]
> Similar: Kurlat, Exercício 6.2 (p. 123); Lista 3, Q1

Q: Two households face the same real rate $r$ and discount factor $\beta$, with $\beta(1+r)>1$, borrow and lend freely, and have CRRA utility with coefficients $\sigma_A<\sigma_B$. How do their consumption paths compare?
- Household B's path is steeper, because a higher $\sigma$ means more risk aversion, and a more risk-averse household saves more for the future.
- Both paths have the same slope $\beta(1+r)$, since the Euler equation pins down the ratio of marginal utilities, not the curvature of $u$.
- Household A's path is steeper, because $1/\sigma$ is the elasticity of intertemporal substitution, so A tilts more toward the cheaper future.
- Both paths are flat, because with free borrowing every household smooths consumption perfectly, whatever the value of its $\sigma$.
<!-- YW5zOjI= -->
> The Euler equation gives $c_2/c_1=[\beta(1+r)]^{1/\sigma}$. With $\beta(1+r)>1$ the base exceeds one, so a larger exponent $1/\sigma$ means faster growth. The household with low curvature cares less about an uneven path and tilts more toward the good that the return makes cheap. Option A is the classic confusion of $\sigma$ (risk aversion, which plays no role without risk) with $1/\sigma$ (the EIS). Option B sets the ratio of marginal utilities, not of consumptions. Option D holds only when $\beta(1+r)=1$. The same $1/\sigma$ is the slope parameter of Benigno's AD curve.
> Ref: Kurlat (2020), cap. 6, §6.2 (pp. 105–112); Map [[02-two-period-problem]]; rules [[04_consumo_poupanca]]
> Similar: Kurlat, Exercício 6.3 (p. 124); Lista 3, Q1

## ise

Q: Two-period CRRA problem: $c_1=W/D$, $D=1+\beta^{1/\sigma}(1+r)^{\frac1\sigma-1}$, $W=y_1+y_2/(1+r)$; $\omega\equiv\frac{y_2/(1+r)}{W}$ is future income's share of $W$, $\theta\equiv1-1/D$ is $c_2$'s share. What is $d\ln c_1/d\ln(1+r)$?
- $-\omega-\theta\left(\frac{1}{\sigma}-1\right)$, so a lender's saving can fall as $r$ rises only if $\sigma>1$.
- $-\omega+\theta\left(\frac{1}{\sigma}-1\right)$, so a lender's saving can fall as $r$ rises only if $\sigma<1$.
- $\omega-\theta\left(\frac{1}{\sigma}-1\right)$, so at $\sigma=1$ saving falls as $r$ rises, for every household.
- $-\omega-\theta\left(\sigma-1\right)$, so a lender's saving can fall as $r$ rises only if $\sigma<1$.
<!-- YW5zOjA= -->
> $\ln c_1=\ln W-\ln D$. Since $dW/d(1+r)=-y_2/(1+r)^2$, the wealth elasticity is $-\omega$. Differentiating $D$ with respect to $\ln(1+r)$ gives $(D-1)(\frac1\sigma-1)$, and dividing by $D$ gives $\theta(\frac1\sigma-1)$. Saving moves opposite to $c_1$, so it falls only if the total is positive, which needs $\frac1\sigma-1<0$, i.e. $\sigma>1$. At $\sigma=1$, $c_1$ moves only through human wealth. Option B flips the sign of the fixed-$W$ term. Option C flips the sign of the wealth term (a higher $r$ *lowers* the present value of $y_2$). Option D writes $\sigma$ where $1/\sigma$ belongs.
> Ref: Kurlat (2020), cap. 6, §6.2 (pp. 112–115); Map [[03-income-and-substitution]]
> Similar: Kurlat, Exercício 6.4 (p. 124); Lista 3, Q1

Q: At the current real rate $r$, a two-period household with incomes $y_1,y_2$ and CRRA utility (any $\sigma>0$) happens to choose $c_2=y_2$, neither borrowing nor lending. The rate then rises slightly. What happens to its saving?
- Nothing, because a household with no net trade in future consumption has neither an income nor a substitution effect when $r$ moves.
- It rises, because with no net trade the income effect is zero, leaving only the substitution effect toward the now-cheaper $c_2$.
- It rises only if $\sigma<1$, because the income effect of a higher return dominates whenever the elasticity of substitution is below one.
- It falls, because a higher $r$ lowers the present value of $y_2$, and that loss of human wealth dominates for every value of $\sigma$.
<!-- YW5zOjE= -->
> In endowment form, the income effect of a price change scales with net trade: the term is $(y_2-c_2)\,\partial c_1/\partial W$. With $c_2=y_2$ it vanishes, and the compensated effect, which always moves $c_1$ away from the good that got dearer, is all that is left. The same follows from the elasticity $-\omega-\theta(\frac1\sigma-1)$: with no net trade, $\omega=\theta$, so it reduces to $-\theta/\sigma<0$ for every $\sigma$. Option A drops the substitution effect. Option C applies the lender's ambiguity to a household that is not a lender. Option D counts only the human-wealth term and ignores the offsetting fixed-$W$ term.
> Ref: Kurlat (2020), cap. 6, §6.2 (pp. 112–115); Map [[03-income-and-substitution]]
> Similar: Kurlat, Exercício 6.3 (p. 124); Lista 3, Q1

## pih

Q: A household lives for periods $t=0,\dots,T-1$, borrows and lends freely at $r$, has $\beta(1+r)=1$ so it consumes a flat $c$, and $W\equiv(1+r)a_0+\sum_t y_t/(1+r)^t$. What is the ratio of the $t=0$ MPC out of a rise $\Delta$ in every $y_t$ to the MPC out of a windfall $\Delta$ at $t=0$?
- $\dfrac{1+r}{r}$, independent of $T$, because a permanent rise $\Delta$ is worth $\Delta(1+r)/r$ at any horizon.
- $\dfrac{1-(1+r)^{-T}}{r}$, rising in $T$ toward $1/r$, and equal to $1/(1+r)$ when $T=1$.
- $\dfrac{(1+r)\left[1-(1+r)^{-T}\right]}{r}$, rising in $T$ toward $(1+r)/r$, and equal to one when $T=1$.
- $\dfrac{r}{(1+r)\left[1-(1+r)^{-T}\right]}$, falling in $T$ toward $r/(1+r)$, and equal to one when $T=1$.
<!-- YW5zOjI= -->
> The flat path gives $c\cdot S=W$, with $S=\sum_{t=0}^{T-1}(1+r)^{-t}=\frac{1+r}{r}[1-(1+r)^{-T}]$. A windfall raises $W$ by $\Delta$, so its MPC is $1/S$. A rise in every period raises $W$ by $\Delta S$, so $c$ rises by exactly $\Delta$ and the MPC is one. The ratio is therefore $S$. At $T=1$ both MPCs are one. As $T\to\infty$ the ratio tends to $(1+r)/r$. Option A is that limit stated for every horizon. Option B drops the factor $1+r$, i.e. it discounts the first period. Option D is the transitory MPC itself, the ratio turned upside down.
> Ref: Kurlat (2020), cap. 6, §6.2–§6.3 (pp. 115–120); Map [[04-permanent-income]]
> Similar: Kurlat, Exercício 6.6 (p. 125); Exercício 6.7 (p. 125)

Q: Household data show that consumption rises when a pay raise announced a year in advance is actually paid, not when it is announced. Within the course's framework, which explanation fits?
- Precautionary saving under CRRA utility, because prudence makes consumption drift upward over time even when income is fully anticipated.
- Quadratic utility, because with linear marginal utility households disregard future income until it arrives and consume current resources.
- Strong impatience (a low discount factor), because a household that discounts the future heavily postpones consumption until income arrives.
- A binding borrowing limit, because a household that cannot borrow against the announced raise consumes its current income until it is paid.
<!-- YW5zOjM= -->
> For an unconstrained household, the announcement raises $W$, so consumption jumps at the news and a predictable payment moves nothing. This is the excess-sensitivity failure. A household at $a\ge0$ that wanted to borrow is at a corner with $c_1=y_1$, so its consumption tracks income timing. This is also why measured rebate MPCs of about 0.2–0.4 fit once a share of households is constrained. Option A gives steady drift, not a jump at the payment date. Option B is the case that *produces* the random walk, in which only news moves $c$. Option C gets impatience backwards: it pulls consumption forward, and so increases the desire to borrow.
> Ref: Kurlat (2020), cap. 6, §6.2–§6.3 (pp. 115–122); Map [[04-permanent-income]]; [[05-ricardian-and-constraints]]
> Similar: Kurlat, Exercício 6.5 (p. 124); Exercício 6.7 (p. 125)

## ric

Q: A household with $u(c)=\ln c$ maximises $\ln c_1+\beta\ln c_2$ subject to $c_1+a=y_1$, $c_2=y_2+(1+r)a$ and $a\ge0$, where $y_t>0$ is income, $\beta$ the discount factor and $r$ the real rate. When does the no-borrowing limit bind, and what holds there?
- It binds iff $y_2>\beta(1+r)\,y_1$; then $c_1=y_1$ and $1/c_1>\beta(1+r)/c_2$ holds at the corner.
- It binds iff $y_2>(1+r)\,y_1/\beta$; then $c_1=y_1$ and $1/c_1>\beta(1+r)/c_2$ holds at the corner.
- It binds iff $y_2<\beta(1+r)\,y_1$; then $c_1=y_1$ and $1/c_1<\beta(1+r)/c_2$ holds at the corner.
- It binds iff $y_2>\beta(1+r)\,y_1$; then $c_1=y_1$ and $1/c_1=\beta(1+r)/c_2$ still holds at the corner.
<!-- YW5zOjA= -->
> Without the limit, $c_1=W/(1+\beta)$, so $a=y_1-c_1<0$ iff $y_1(1+\beta)<y_1+y_2/(1+r)$, i.e. $\beta y_1<y_2/(1+r)$, which is $y_2>\beta(1+r)y_1$. Then the corner is $(y_1,y_2)$, and with the multiplier $\mu=u'(c_1)-\beta(1+r)u'(c_2)>0$ the Euler equation holds as a strict inequality. At the corner that is $1/y_1>\beta(1+r)/y_2$, the same condition again. Option D is trap 6: an equality at a binding constraint. Option C reverses both the condition and the inequality. Option B misplaces $\beta$.
> Ref: Kurlat (2020), cap. 6, §6.2 (pp. 120–122); Map [[05-ricardian-and-constraints]]
> Similar: Kurlat, Exercício 6.5 (p. 124); Lista 3, Q1

Q: In a two-period model with lump-sum taxes, households borrowing and lending freely at the government's rate, and a government bound by its intertemporal budget, period-1 spending rises, financed by debt repaid with period-2 taxes. What happens to consumption?
- Nothing, because by Ricardian equivalence the household saves for the whole future tax bill, so debt-financed spending leaves it unaffected.
- Period-1 consumption is unchanged and period-2 consumption falls, because only the later tax cuts disposable income, and only in period 2.
- Both periods' consumption fall, by the same amounts as under tax financing, because lifetime wealth falls by the present value of the spending.
- Both periods' consumption fall, but by less than under tax financing, because debt postpones the burden and the household earns interest meanwhile.
<!-- YW5zOjI= -->
> Substituting the government's budget into the household's gives $c_1+\frac{c_2}{1+r}=y_1+\frac{y_2}{1+r}-G_1-\frac{G_2}{1+r}$. Taxes drop out and spending stays in. A rise in $G_1$ lowers lifetime resources, and the household smooths the loss across both periods. Debt versus taxes is a timing choice, so it changes nothing. Option A is Kurlat's warning on p. 121: Ricardian equivalence makes the *timing* of taxes irrelevant, not spending. Option B has the household ignore a liability it can foresee. Option D forgets that the debt carries interest at the household's own rate, so the tax bill grows by exactly what the household earns.
> Ref: Kurlat (2020), cap. 6, §6.2 (pp. 120–121); Map [[05-ricardian-and-constraints]]
> Similar: Kurlat, Exercício 6.8 (p. 125); Lista 3, Q1
