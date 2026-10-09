---
quiz: "Macro I — Session 6: General Equilibrium (hard)"
tags:
  rate: "Two-period GE and the interest rate"
  fwt: "First welfare theorem and the planner"
  saddle: "Infinite-horizon dynamics and the saddle path"
  mgr: "Steady state and the modified Golden Rule"
  shock: "Shocks on the phase diagram"
---

## rate

Q: A two-period endowment economy has one representative household with utility $u(c_1)+\beta u(c_2)$, $u(c)=c^{1-\sigma}/(1-\sigma)$, discount factor $\beta\in(0,1)$, curvature $\sigma>0$, and endowments $y_1,y_2$ of the single good. What is the equilibrium gross real interest rate $1+r^*$?
- $1+r^*=\frac{1}{\beta}\left(\frac{y_2}{y_1}\right)^{1/\sigma}$, so a household with a low elasticity of substitution needs a small rate change to accept $c_t=y_t$
- $1+r^*=\frac{1}{\beta}\left(\frac{y_2}{y_1}\right)^{\sigma}$, so a household that dislikes uneven consumption needs a large rate change to accept $c_t=y_t$
- $1+r^*=\frac{1}{\beta}\left(\frac{y_1}{y_2}\right)^{\sigma}$, so faster endowment growth lowers the rate as the household wants to save more of the future
- $1+r^*=\beta\left(\frac{y_2}{y_1}\right)^{\sigma}$, so a more patient household with a higher $\beta$ needs a higher rate before it accepts $c_t=y_t$
<!-- YW5zOjE= -->
> Market clearing with a representative household forces $a=0$, so $c_1=y_1$ and $c_2=y_2$. The Euler equation $c_1^{-\sigma}=\beta(1+r)c_2^{-\sigma}$ then reads $1+r^*=\frac{1}{\beta}(y_2/y_1)^{\sigma}$. Here the rate is the price that makes the household content to consume its endowment. A higher $\sigma$ means the household dislikes uneven consumption more, so a given amount of growth needs a larger rate to stop it borrowing against the future. Option A puts the elasticity $1/\sigma$ where the curvature $\sigma$ belongs. Option C has growth working the wrong way. Option D multiplies by $\beta$ where it should divide, so the role of patience comes out reversed.
> Ref: Kurlat (2020), cap. 9, §9.1 (pp. 165–168); cap. 6, §6.3; rules [[06_equilibrio_geral]]
> Similar: Kurlat, Exercício 9.5 (p. 181); Lista 5, Q1(d)

Q: In a two-period endowment economy with a single representative household, a change in preferences makes every household more patient. What adjusts in equilibrium?
- Aggregate saving rises, because each household now wants to save more at the old rate, and the real interest rate falls to make room for the extra saving
- The real interest rate is unchanged, because it is pinned by technology, and consumption shifts from period 1 to period 2 as households lend to each other
- The real interest rate rises, because more patient households demand a higher return on the extra wealth they now want to carry into period 2
- The real interest rate falls until desired saving is zero again, while consumption in both periods and aggregate saving stay exactly as they were
<!-- YW5zOjM= -->
> A representative household has no one to lend to. Whatever its preferences, aggregate net saving is zero and it consumes its endowment in each period. A rise in patience therefore cannot move quantities. It moves the price instead: the rate falls until the household no longer wants to save at all. Option A is the partial-equilibrium answer, where the rate is given and the household saves more. Option B treats the rate as set by technology, but an endowment economy has no technology that could fix it. Option C gets the sign wrong, because extra patience makes lending more attractive, which lowers the rate rather than raising it.
> Ref: Kurlat (2020), cap. 9, §9.1 (pp. 165–168); Map [[01-equilibrium-as-benchmark]]
> Similar: Kurlat, Exercício 9.5 (p. 181); Exercício 9.2 (p. 179)

Q: A two-period economy has a representative household with utility $\ln c_1+\beta\ln c_2$ ($\beta\in(0,1)$), labour fixed at one, output $F(K)=AK^{\alpha}$ ($A>0$, $\alpha\in(0,1)$), and capital $K_2$ built from period-1 goods that is used up in period 2. Let $W_1$ be the period-1 resources, output plus undepreciated initial capital. Which equilibrium $K_2$ follows?
- $K_2=\frac{\alpha\beta}{1+\alpha\beta}W_1$, since equating the marginal rate of substitution to $F_K(K_2)$ gives $c_1=K_2/(\alpha\beta)$
- $K_2=\frac{\beta}{1+\beta}W_1$, since a log household saves the same share of its wealth whatever the interest rate the technology produces
- $K_2=\frac{\alpha\beta}{1+\beta}W_1$, since a log household saves the share $\beta/(1+\beta)$ and only the share $\alpha$ of output is paid to capital
- $K_2=\frac{\alpha}{1+\alpha}W_1$, since the equilibrium interest rate offsets impatience exactly, so $\beta$ drops out once prices have cancelled
<!-- YW5zOjA= -->
> The prices cancel to $\frac{u'(c_1)}{\beta u'(c_2)}=F_K(K_2)$, here $\frac{c_2}{\beta c_1}=\alpha AK_2^{\alpha-1}$. With $c_2=AK_2^{\alpha}$ the left side is $\frac{AK_2^{\alpha}}{\beta c_1}$, so $c_1=K_2/(\alpha\beta)$ and $A$ cancels. The resource constraint $c_1+K_2=W_1$ then gives $K_2(1+\frac{1}{\alpha\beta})=W_1$, which is option A. Option B is the endowment-economy rule for saving out of wealth. It ignores that period-2 consumption is $AK_2^{\alpha}$ and not $(1+r)K_2$, because the wage bill in period 2 is part of the household's income. Option C splices two partial rules together. Option D drops impatience, which still matters: it is the reason the household does not invest up to the point where $F_K=1$.
> Ref: Kurlat (2020), cap. 9, §9.1–9.2 (pp. 165–172); Map [[derivacoes-cap-09]]
> Similar: Kurlat, Exercício 9.2 (p. 179); Lista 5, Q1

## fwt

Q: A student writes every first-order condition of the two-period production economy, then adds market clearing for goods in both periods, labour in both periods and credit. There is one equation too many, and nothing fixes the level of prices. Which reading is correct?
- The extra equation shows the model is overdetermined, so the investment firm must be dropped; the price level is then pinned by the goods market
- Every budget constraint binds, so one clearing condition follows from the others by Walras' law; only relative prices such as $w_t$ and $1+r$ are determined
- One clearing condition is redundant because the planner's constraints replace it; the price level is pinned by the First Welfare Theorem
- Every budget constraint binds, so the credit market clears by assumption; the price level is fixed by normalising the period-1 wage to one
<!-- YW5zOjI= -->
> Summing the binding budget constraints shows that the value of aggregate excess demand is zero at any price vector. So once all but one market clear, the last one must clear too, and one equation is redundant. Every budget constraint is also homogeneous of degree zero in nominal prices. The model therefore fixes $w_t$ in goods and the rate $1+r$, but not the price level. That is the classical dichotomy, and it is why money has to be added before the price level can be determined. Option A takes the redundancy for an inconsistency. Option C confuses the planner, which is a device for the proof, with an equation of the decentralised model. Option D has the right count, but normalising a price picks a numéraire, and that is not a theory of the price level.
> Ref: Kurlat (2020), cap. 9, §9.1 (pp. 165–168); Map [[01-equilibrium-as-benchmark]]
> Similar: Kurlat, Exercício 9.5 (p. 181); Exercício 9.2 (p. 179)

Q: A government taxes the rental income of capital at rate $\tau\in(0,1)$ and rebates the revenue lump-sum to the household, in an economy that otherwise meets every assumption of the First Welfare Theorem. Which statement is correct?
- The arbitrage condition becomes $1+r=(1-\tau)F_K$, so the marginal rate of substitution falls short of $F_K$; investment is too low, and a planner could do better
- The arbitrage condition becomes $1+r=(1-\tau)F_K$, but the rebate hands the revenue back, so the household's wealth and the allocation match the planner's
- The arbitrage condition becomes $1+r=F_K/(1-\tau)$, so the marginal rate of substitution exceeds $F_K$; investment is too high and a planner could do better
- The arbitrage condition is unchanged at $1+r=F_K$, because the tax falls on rental income only; it redistributes but leaves the allocation Pareto optimal
<!-- YW5zOjA= -->
> The investment firm now keeps $(1-\tau)r^K$ per unit, so zero profit requires $1+r=(1-\tau)F_K$. Combined with the Euler equation this gives $\frac{u'(c_1)}{\beta u'(c_2)}=(1-\tau)F_K(K_2)$, while the planner sets the marginal rate of substitution equal to $F_K$ itself. The wedge makes the household value future goods below what the technology can deliver, so it invests too little. The rebate restores income, but it does nothing at the margin, because the household takes the transfer as given. This is the same logic that made a rebated wage tax distortionary. Option B confuses a wealth effect with a marginal one. Option C puts the wedge on the wrong side. Option D forgets that rental income is exactly the return the arbitrage condition prices.
> Ref: Kurlat (2020), cap. 9, §9.2 (pp. 168–172); Map [[derivacoes-cap-09]]
> Similar: Kurlat, Exercício 9.6 (p. 182); Exercício 9.1 (p. 179)

## saddle

Q: A neoclassical growth economy, with fixed labour and a household that maximises discounted utility, starts with capital below its steady state. The household picks initial consumption slightly below the saddle-path level. What happens, and what rules the path out?
- Capital rises and consumption falls at once, and the path converges to a steady state with more capital than the optimal one; the No-Ponzi condition rules it out
- Capital falls while consumption rises, until capital runs out in finite time; the path breaks the resource constraint and is never feasible
- Capital and consumption both rise and the path reaches the same steady state, only more slowly, so it is optimal too; transversality does not bind
- Both rise at first, then consumption turns down once capital passes its steady state and capital heads past the Golden Rule; transversality rules it out
<!-- YW5zOjM= -->
> Below the saddle path and to the left of the vertical locus, both $K$ and $c$ rise. But $c$ rises too slowly, so the path crosses the vertical line before it reaches the steady state. From then on $F_K-\delta<\frac{1}{\beta}-1$, consumption falls, and capital keeps piling up past the Golden Rule. That path is feasible in every period, but the household is accumulating capital it never consumes, so $\beta^t u'(c_t)K_{t+1}$ does not go to zero. Transversality is what rules it out. Option B describes a start *above* the saddle path. Option A misplaces the dynamics and names the wrong condition, since No-Ponzi bounds debt and not assets. Option C overlooks that only the knife-edge path reaches the steady state.
> Ref: Kurlat (2020), cap. 9, §9.3 (pp. 172–179); Map [[02-dynamics-and-saddle-path]]
> Similar: Kurlat, Exercício 9.9 (p. 184); Lista 5, Q2

Q: Two neoclassical growth economies are identical, with fixed labour and capital starting below the steady state, except that households in one have a higher intertemporal elasticity of substitution $1/\sigma$. How do their outcomes compare?
- The steady-state capital stock is higher where $1/\sigma$ is higher, because those households are more willing to postpone consumption to build up capital
- Steady-state capital and consumption are the same, but where $1/\sigma$ is higher saving reacts more to the gap $F_K-\delta-\rho$, so convergence is faster
- Steady-state capital and consumption are the same, and the transition is the same too, because $\sigma$ cancels whenever the Euler equation is linearised
- The steady state is the same, but where $1/\sigma$ is higher households smooth consumption more strongly, so they save less and convergence is slower
<!-- YW5zOjE= -->
> At the steady state $c_{t+1}/c_t=1$, and raising 1 to the power $1/\sigma$ still gives 1. So the vertical locus $F_K(K_{ss})=\rho+\delta$ does not depend on $\sigma$, and the hump-shaped locus contains no preference parameter at all. The steady state is the same in both economies. Along the transition, consumption growth is $[\beta(1+F_K-\delta)]^{1/\sigma}$, which reacts more to a given capital gap when $1/\sigma$ is high. Households then accept a steeper consumption path, save more early on and converge faster. Option A treats $1/\sigma$ as patience, but patience is $\rho$. Option D mixes up willingness to substitute over time with a desire to smooth, which is $\sigma$ itself. Option C is wrong because $\sigma$ drops out only at the fixed point, not along the path.
> Ref: Kurlat (2020), cap. 9, §9.3 (pp. 172–179); Map [[02-dynamics-and-saddle-path]]; Map [[derivacoes-cap-09]]
> Similar: Kurlat, Exercício 9.12 (p. 185); Lista 5, Q2

## mgr

Q: In the neoclassical growth model with fixed labour, output $F(K,1)$, depreciation rate $\delta$ and discount factor $\beta\in(0,1)$, the locus where capital is constant is $c=F(K,1)-\delta K$. What is its slope at the steady state $K_{ss}$?
- $\frac{1}{\beta}-1+\delta$, which is positive, so the steady state sits on the rising side of the locus and to the left of its peak
- $1-\beta$, which is positive, so the steady state sits on the rising side of the locus and to the left of its peak at the Golden Rule
- $\frac{1}{\beta}-1$, which is positive, so the steady state sits on the rising side of the locus and to the left of its Golden Rule peak
- $\delta-\frac{1}{\beta}+1$, which is negative, so the steady state sits on the falling side of the locus and to the right of its peak
<!-- YW5zOjI= -->
> The slope of the locus is $F_K(K,1)-\delta$. At the steady state the consumption Euler equation imposes $F_K(K_{ss},1)=\frac{1}{\beta}-1+\delta$, so the slope is $\frac{1}{\beta}-1=\rho>0$. A positive slope means the steady state lies on the rising side of the hump, below the Golden Rule, where the slope is zero. That is the modified Golden Rule seen as a slope. Option A is the marginal product itself, with $\delta$ left in. Option B is a common approximation of $\rho$, but it is not equal to it. Option D gets the sign wrong and would put the economy in the dynamically inefficient region.
> Ref: Kurlat (2020), cap. 9, §9.3 (pp. 172–179); cap. 4, §4.3; Map [[02-dynamics-and-saddle-path]]
> Similar: Kurlat, Exercício 9.12 (p. 185); Lista 5, Q2

Q: In the neoclassical growth model with fixed labour, output $AK^{\alpha}$ ($A>0$, $\alpha\in(0,1)$), depreciation rate $\delta$ and discount factor $\beta\in(0,1)$, what is the ratio of the steady-state capital stock $K_{ss}$ to the Golden Rule stock $K_{gr}$?
- $\frac{K_{ss}}{K_{gr}}=\left[\frac{\frac{1}{\beta}-1+\delta}{\delta}\right]^{\frac{1}{1-\alpha}}$, larger than one, rising as households become less patient
- $\frac{K_{ss}}{K_{gr}}=\left[\frac{\delta}{\frac{1}{\beta}-1+\delta}\right]^{\frac{1}{1-\alpha}}$, below one, independent of $A$, tending to one as $\beta\to1$
- $\frac{K_{ss}}{K_{gr}}=\left[\frac{\delta}{\frac{1}{\beta}-1+\delta}\right]^{\frac{1}{\alpha}}$, below one, independent of $A$, tending to one as $\beta\to1$
- $\frac{K_{ss}}{K_{gr}}=\left[\frac{\alpha\delta}{\frac{1}{\beta}-1+\delta}\right]^{\frac{1}{1-\alpha}}$, below one, independent of $A$, tending to $\alpha$ as $\beta\to1$
<!-- YW5zOjE= -->
> The Golden Rule sets $\alpha AK_{gr}^{\alpha-1}=\delta$, and the steady state sets $\alpha AK_{ss}^{\alpha-1}=\frac{1}{\beta}-1+\delta$. Dividing the second by the first cancels $\alpha A$ and gives $(K_{ss}/K_{gr})^{\alpha-1}=\frac{1/\beta-1+\delta}{\delta}$. Raising both sides to $\frac{1}{\alpha-1}$ inverts the ratio and leaves option B. The gap between the two stocks is impatience, and nothing else: it closes as $\beta\to1$. Option A forgets that the exponent $\alpha-1$ is negative, so the ratio is not inverted. Option C uses the wrong exponent. Option D keeps an $\alpha$ that cancels, because both conditions share the factor $\alpha A$.
> Ref: Kurlat (2020), cap. 9, §9.3 (pp. 172–179); cap. 4, §4.3; Map [[derivacoes-cap-09]]
> Similar: Kurlat, Exercício 9.12 (p. 185); Lista 5, Q2

## shock

Q: A neoclassical growth economy with fixed labour sits at its steady state when a one-time disaster destroys part of its capital stock, with preferences and technology unchanged. What happens to consumption and to the real interest rate?
- Consumption drops onto the unchanged saddle path at the lower capital stock; the rate jumps above $\rho$ and falls back as capital is rebuilt
- Consumption stays at its old level to smooth the shock; the rate is unchanged at $\rho$, because in this model it is pinned by $\beta$ alone
- Consumption drops onto a new saddle path that leads to a lower steady state; the rate stays above $\rho$ for good, because capital stays scarce
- Consumption drops onto the unchanged saddle path at the lower capital stock; the rate falls below $\rho$, because output and saving demand fall
<!-- YW5zOjA= -->
> Neither locus moves, because no parameter has changed. Only the state variable has jumped. Capital is predetermined and consumption is free, so consumption jumps onto the old saddle path at the lower $K$. The path slopes upward, so consumption falls. With less capital, $F_K-\delta$ exceeds $\rho$, the rate rises, and the Euler equation then delivers rising consumption while capital is rebuilt. This is the Solow transition with saving chosen rather than assumed. Option B treats the rate as fixed by $\beta$ at every date, but that holds only at the steady state. Option C moves the steady state, which only a change in a parameter could do. Option D has the scarcity effect backwards.
> Ref: Kurlat (2020), cap. 9, §9.3 (pp. 172–179); Map [[02-dynamics-and-saddle-path]]
> Similar: Kurlat, Exercício 9.9 (p. 184); Exercício 9.8 (p. 183)
