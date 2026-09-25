---
quiz: "Macro I — Lista 7, Part 1/3: foundations (NK vs New Classical vs Keynesian; natural vs efficient output)"
tags:
  schools: "Three generations: NK, New Classical, Keynesian"
  wedge: "Natural vs efficient output"
---

## schools

Q: In both Lucas (1973) and Benigno (2015) the supply curve reads $p-p^e=\kappa(y-y_n)$, where $p$ is the log price level, $p^e$ the expected or pre-set price level, $y$ output and $y_n$ natural output. What changes between the two readings, and what does it imply for a publicly known stabilisation rule?
- In Benigno $p^e$ is a price already posted before the shock by a share $\alpha$ of firms, so a known rule that reacts after posting still moves output.
- In Benigno $p^e$ is the rational forecast of $p$, so any known rule is built into $p^e$ and moves only the price level, exactly as in the New Classical case.
- In Benigno $p^e$ is an adaptive forecast of past prices, so a known rule moves output until expectations catch up with it, as in the original Keynesian model.
- In Benigno $p^e$ is chosen by the central bank each period, so a known rule moves output only through the credibility of the announced price-level target.
<!-- YW5zOjA= -->
> The equation is identical, and Benigno says so (p. 508). What changes is the reading of $p^e$: not a forecast that can be wrong, but a price fixed before the shock by the $\alpha$ firms that cannot reset. A bank that reacts after posting moves output even if its rule is public, which overturns Sargent–Wallace policy ineffectiveness. Option B is the New Classical reading; C is the old Keynesian one; D invents a role for the bank that the model does not give it.
> Ref: Benigno (2015), §4, pp. 507–508; Romer (2012), ch. 6
> Similar: Lista 7, Q1(i); [[benigno/02-firms-and-as]] §2.8

Q: Why does the New-Keynesian model need monopolistic competition for sticky prices to make short-run output demand-determined?
- Because under perfect competition firms earn zero profit, so any demand shock would force exit and push the price level straight back to its flexible-price value.
- Because with price above marginal cost a firm stuck at its pre-set price still gains from each extra unit sold, so it is willing to serve whatever demand arrives.
- Because monopolistic competition makes the demand curve of each firm perfectly elastic, so output responds fully to aggregate demand at the posted price.
- Because the mark-up rises automatically in booms, so firms with pre-set prices can absorb demand shocks without their marginal cost ever changing.
<!-- YW5zOjE= -->
> With $P(j)=(1+\mu)W/A>W/A$, a firm at its pre-set price earns a positive margin on each extra unit, so it serves the demand that shows up. Output is then set by demand in the short run, and that is why shifting AD moves $y$. Monopolistic competition also gives the model an agent whose decision *is* the price. Under perfect competition there is nobody to be sticky. Option C inverts the elasticity: Dixit–Stiglitz demand has finite elasticity $\theta$.
> Ref: Benigno (2015), §4, eqs. (9)–(11), pp. 506–507
> Similar: Lista 7, Q1(ii); [[benigno/02-firms-and-as]] §2.1–2.2

Q: The slope of Benigno's supply curve is $\kappa=(1-\alpha)(\sigma^{-1}+\eta)/\alpha$, where $\alpha$ is the share of firms with pre-set prices, $\sigma$ the output-scaled elasticity of intertemporal substitution and $\eta$ the inverse Frisch elasticity. What happens as $\alpha\to0$, and what does it say about a cut in the nominal rate?
- $\kappa\to0$, AS becomes horizontal, and a cut in the nominal rate moves only output while the price level stays at $p^e$.
- $\kappa\to(\sigma^{-1}+\eta)$, AS keeps a finite slope, and a cut in the nominal rate is split equally between output and the price level.
- $\kappa\to\infty$, AS becomes vertical at $y_n$, and a cut in the nominal rate moves only the price level while output stays at $y_n$.
- $\kappa\to\infty$, AS becomes vertical at $y_e$, and a cut in the nominal rate moves only output toward the efficient level $y_e$.
<!-- YW5zOjI= -->
> With $\alpha$ in the denominator, fewer sticky firms means a steeper curve. At $\alpha\to0$ every firm resets, AS is vertical at the *natural* level, and the classical model returns. From $dy=-\sigma\,di/(1+\sigma\kappa)$, output stops responding. Option D confuses the vertical position: flexible prices deliver $y_n$, not $y_e$, because the mark-up wedge remains.
> Ref: Benigno (2015), eq. (17), p. 508; §5, p. 510
> Similar: [[benigno/02-firms-and-as]] §2.6; [[benigno/04-equilibrium-geometry]] §4.5

Q: Why does the aggregate demand curve slope down in Benigno's model, given that the central bank sets the nominal rate $i$ and the long-run price level $\bar p$ is anchored?
- A higher $p$ lowers real money balances $M/p$, raises the interest rate that clears the money market, and cuts investment spending.
- A higher $p$ lowers the real value of household wealth held in money, so consumption falls through a direct wealth effect on spending.
- A higher $p$ raises money demand at the given $i$, so the central bank must contract the money supply, which lowers spending.
- A higher $p$ lowers expected inflation $\bar p-p$, raises the real rate $i-(\bar p-p)$, and households postpone consumption.
<!-- YW5zOjM= -->
> AD is the log-linear Euler equation, $y=\bar y_n+(g-\bar g)-\sigma[i-(\bar p-p)-(\bar\tau_c-\tau_c)-\rho]$. There is no LM curve and no money stock in it. Option A is the IS–LM Keynes effect and B the Pigou effect; both need money in the model. C gets the regime wrong: with $i$ set, money is supplied elastically and never enters demand.
> Ref: Benigno (2015), §3, eqs. (5)–(8), pp. 505–506; p. 504
> Similar: Lista 7, Q1(iii); [[benigno/01-household-and-ad]]

Q: Which fact is the strongest empirical motivation for putting a *nominal friction* back into a model that keeps rational expectations?
- Inflation and unemployment rose together in the 1970s, which showed that the Phillips curve had no short-run slope at any horizon.
- Announced disinflations still caused deep, long recessions, far longer than misperceptions could last with monthly price data published.
- Money demand became unstable in the 1980s, which made the quantity equation useless and forced central banks to abandon all price targets.
- Real wages are strongly countercyclical in the data, which is exactly what a competitive model with rigid nominal wages predicts.
<!-- YW5zOjE= -->
> The 1970s (option A) motivated rational expectations, not the friction, and it did not show a zero short-run slope. What New Classical misperception cannot explain is large, persistent effects of *announced* policy, for example the Volcker disinflation. A friction that does not rely on anyone being fooled, such as pre-set prices, can. Option C motivates the interest-rate instrument, not the friction. Option D is false: real wages are roughly acyclical, which is evidence *against* the pure nominal-wage story.
> Ref: Benigno (2015), §1–§2, pp. 503–505; Romer (2012), ch. 6
> Similar: Lista 7, Q1(i)

Q: Benigno's welfare loss is $L=\tfrac12(y-y_e)^2+\tfrac{\theta}{2\kappa}(p-p^e)^2$, where $y_e$ is efficient output, $\theta$ the elasticity of substitution between goods and $\kappa$ the AS slope. Why is the output target $y_e$ rather than the natural level $y_n$?
- Because the loss comes from household utility, and the allocation households value most is the planner's $y_e$, not the distorted $y_n$.
- Because $y_n$ is not observable in real time, so a central bank must target the efficient level as a practical proxy that can be measured more reliably.
- Because the natural level moves with every productivity shock, and a target that moves is incompatible with the quadratic form of the welfare loss.
- Because $y_n$ and $y_e$ always coincide in the model, so writing the target as $y_e$ is only a notational choice made for convenience.
<!-- YW5zOjA= -->
> The loss is a second-order approximation to household utility around an efficient steady state. Utility depends on consumption and hours, and the allocation that maximises it is the planner's. So the welfare gap is $y-y_e$. The natural level carries the mark-up wedge, and targeting it would build the distortion into the objective. Option D is false exactly when it matters: a mark-up shock separates the two.
> Ref: Benigno (2015), §11, eq. (33), pp. 521–522
> Similar: Lista 7, Q1(iv), Q4; [[benigno/10-optimal-policy]] §10.1

## wedge

P: A planner maximises $u(C)-v(L)$ subject to $Y=C+G$ and $Y=AL$, with $v(L)=L^{1+\eta}/(1+\eta)$, $u'(C)=C^{-\tilde\sigma^{-1}}$, $\eta$ the inverse Frisch elasticity, $A$ productivity and $G$ public spending. In the decentralised flexible-price economy, firms charge $P=(1+\mu)W/A$ with aggregate mark-up $\mu$. In log-deviations, $\sigma$ is the output-scaled elasticity of intertemporal substitution, $a$ productivity, $g$ public spending, $y_n$ natural output and $y_e$ efficient output.

Q: Which expression gives the gap between natural and efficient output?
- $y_n-y_e=-\mu\,(\sigma^{-1}+\eta)$
- $y_n-y_e=-\mu/(1+\eta)$
- $y_n-y_e=-\mu/(\sigma^{-1}+\eta)$
- $y_n-y_e=-\mu/\sigma^{-1}$
<!-- YW5zOjI= -->
> The planner sets $v'(Y/A)/u'(Y-G)=A$; the market sets the same ratio equal to the real wage $A/(1+\mu)$. The log of the left side is $\eta(y-a)+\sigma^{-1}(y-g)$, with slope $\sigma^{-1}+\eta$ in $y$. The right sides differ by $\mu$, so the solutions differ by $\mu/(\sigma^{-1}+\eta)$, with the market below. The $a$ and $g$ terms are identical in eqs. (15) and (19) and cancel.
> Ref: Benigno (2015), eqs. (14), (15), (19), §4.4, pp. 508–509
> Similar: Lista 7, Q3; [[benigno/03-natural-and-efficient]] §3.4

Q: Which change moves $y_n-y_e$?
- A rise in the payroll tax $\tau_w$, with $a$, $g$ and $\alpha$ held fixed.
- A rise in productivity $a$, with $\mu$, $g$ and $\alpha$ held fixed.
- A rise in public spending $g$, with $\mu$, $a$ and $\alpha$ held fixed.
- A rise in the sticky share $\alpha$, with $\mu$, $a$ and $g$ held fixed.
<!-- YW5zOjA= -->
> Only what enters the market's condition and not the planner's moves the gap. Eq. (13) folds $\tau_w$ into $\mu$, so a payroll tax is a mark-up shock. Productivity and spending enter both problems equally, so they shift $y_n$ and $y_e$ together. The sticky share $\alpha$ enters *neither*: both concepts are flexible-price or planner outcomes, and stickiness only explains why $y$ departs from $y_n$.
> Ref: Benigno (2015), eq. (13), p. 507; §4.4, p. 509
> Similar: Lista 7, Q3; [[benigno/06-markup-shocks]] §6.4

Q: At natural output the household's marginal rate of substitution lies below labour's marginal product by the mark-up wedge. How does the lost surplus, the area between MRS and MRT from $y_n$ to $y_e$, depend on $\mu$?
- $\tfrac12\,\mu^2\,(\sigma^{-1}+\eta)$, rising with the steepness of the MRS curve
- $\mu/(\sigma^{-1}+\eta)$, linear in the wedge like the distance itself
- $\tfrac12\,\mu/(\sigma^{-1}+\eta)$, half the horizontal distance between levels
- $\tfrac12\,\mu^2/(\sigma^{-1}+\eta)$, quadratic in the wedge like the loss
<!-- YW5zOjM= -->
> The triangle has height $\mu$, the gap between MRT and the wage, and base $\mu/(\sigma^{-1}+\eta)$, the horizontal distance. Its area is $\tfrac12\mu^2/(\sigma^{-1}+\eta)=\tfrac12(\sigma^{-1}+\eta)(y_n-y_e)^2$. That is why the welfare loss is quadratic in the efficient gap. A steeper MRS curve shrinks the output shortfall, and so shrinks the triangle, which rules out option A.
> Ref: Benigno (2015), §4.4, p. 509; §11, eq. (33), p. 521
> Similar: Lista 7, Q3; [[benigno/03-natural-and-efficient]] §3.4

P:

Q: In Benigno's loss $L=\tfrac12(y-y_e)^2+\tfrac{\theta}{2\kappa}(p-p^e)^2$, with $\kappa=(1-\alpha)(\sigma^{-1}+\eta)/\alpha$, how does the relative weight on price surprises respond to the sticky share $\alpha$ and to the goods-substitution elasticity $\theta$?
- It falls with $\alpha$ and rises with $\theta$, since more rigidity makes price surprises less frequent while substitutability makes them more costly.
- It rises with $\alpha$ and rises with $\theta$, since more rigidity means more price dispersion per surprise and substitutability punishes dispersion harder.
- It rises with $\alpha$ and falls with $\theta$, since more rigidity means more dispersion while substitutability lets consumers switch away from mispriced goods.
- It is independent of $\alpha$ and rises with $\theta$, since the rigidity term cancels once the weight is divided by the slope of the supply curve.
<!-- YW5zOjE= -->
> The weight is $\theta/\kappa$, and $\kappa$ falls with $\alpha$, so the weight rises with $\alpha$. With few adjusters, a given price-level surprise means a large gap between the adjusters and the frozen firms. And with high $\theta$ consumers shift demand sharply toward the cheap goods, so that dispersion costs more. Benigno, p. 522: "the smaller the fraction [of firms that adjust], the greater the weight to give to price stability". Option C gets the substitution effect backwards.
> Ref: Benigno (2015), §11, eq. (33), p. 522
> Similar: Lista 7, Q4; [[benigno/10-optimal-policy]] §10.1
