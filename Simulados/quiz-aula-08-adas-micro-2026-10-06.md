---
quiz: "Macro I — Session 8: New-Keynesian AD-AS Microfoundations (hard)"
tags:
  hh: "Household and AD"
  firm: "Firms and AS"
  nat: "Natural vs efficient output"
  geo: "Short- vs long-run equilibrium geometry"
---

## hh

Q: In Benigno's two-period New-Keynesian model the household faces one intertemporal budget constraint with a lump-sum transfer $T$. The government pays a larger lump-sum transfer now and levies a lump-sum tax of equal present value in the long-run period. What happens to the AD curve?
- It shifts right, because current disposable income rises and households spend part of it, as a Keynesian consumption function would predict.
- It does not move, because only the present value of lump-sum transfers enters the budget, and the Euler equation pins current consumption.
- It shifts left, because households foresee the long-run tax, so long-run natural consumption falls and pulls current demand down with it.
- It does not move, but the AS curve shifts left, because the larger current transfer makes households richer today and so they supply less labour.
<!-- YW5zOjE= -->
> With a single intertemporal constraint, the timing of lump-sum transfers changes nothing the household chooses; only their present value matters, and here it is unchanged. Current consumption comes from the Euler equation, $c=\bar c-\tilde\sigma[i-(\bar p-p)-\rho]$, where $\bar c$ is long-run natural consumption, set by $\bar a$, $\bar g$ and $\bar\mu$. A lump-sum tax is not in $\bar\mu$, so $\bar c_n$ does not move (C is wrong), and $T$ appears nowhere in AD. Option A uses a current-income consumption function, which this model does not have. Option D gets the wealth effect wrong: the present value of wealth is unchanged, and $T$ does not enter $y_n$. Ricardian equivalence holds until borrowers and savers are split.
> Ref: Benigno (2015), §3, eqs. (1)–(6) (pp. 505–506); §4.3, eq. (18) (pp. 508–509); Map [[01-household-and-ad]]
> Similar: Lista 7, Q1

Q: In Benigno's model the AD curve slopes down with slope $-1/\sigma$ because the central bank holds the nominal rate $i$ fixed while the current price level $p$ varies. Suppose that instead the bank raises $i$ by more than one point for each point by which $p$ exceeds its pre-set level. What happens to AD?
- It becomes flatter: a rise in $p$ now raises the real rate more than one-for-one, so demand falls more; the slope is partly a policy choice.
- It becomes steeper: the rule offsets part of the fall in expected inflation, so the real rate moves by less than before and demand responds less to $p$.
- It is unchanged: the household reacts only to expected inflation $(\bar p-p)$, which depends on prices and not on how the bank sets the rate $i$.
- It becomes vertical: the rule fixes the real rate whatever $p$ does, so current output no longer depends on the price level and only AS sets $p$.
<!-- YW5zOjA= -->
> AD comes from the Euler equation, $y=\bar y_n+(g-\bar g)-\sigma[i-(\bar p-p)-\rho]$, and the household responds to the real rate $r=i-(\bar p-p)$. If $i$ is fixed, $dr=dp$. If $i$ rises with $p$, $dr$ is larger than $dp$, so output falls by more for a given price rise and AD is flatter. The slope $-1/\sigma$ is therefore an assumption about policy (fixed $i$), not a property of preferences alone. B has the direction backwards. A vertical AD (D) would require $i$ to *fall* one-for-one with $p$, which keeps $r$ fixed. C forgets that $i$ sits in the same bracket as $p$.
> Ref: Benigno (2015), §3, eqs. (3)–(8) (pp. 505–506); §5, eq. (21) (pp. 509–510); Map [[01-household-and-ad]]
> Similar: Lista 7, Q1

## firm

Q: In Benigno's model a share $\alpha\in(0,1)$ of firms keeps the pre-set log price $p^e$ and the rest reset to $\tilde p$, so the log price level is $p=\alpha p^e+(1-\alpha)\tilde p$. The AS curve is $p-p^e=\kappa(y-y_n)$ with $\kappa=(1-\alpha)(\sigma^{-1}+\eta)/\alpha$, where $y$ is output, $y_n$ natural output, $\sigma$ the output-scaled intertemporal elasticity and $\eta$ the inverse Frisch elasticity. What is $\tilde p-p^e$?
- $\dfrac{\sigma^{-1}+\eta}{1-\alpha}(y-y_n)$, so resetting firms move further from $p^e$ as more firms reset.
- $\dfrac{(1-\alpha)(\sigma^{-1}+\eta)}{\alpha}(y-y_n)$, so resetting firms move exactly as much as the price level.
- $\dfrac{\sigma^{-1}+\eta}{\alpha}(y-y_n)$, so resetting firms move further from $p^e$ as fewer firms get to reset.
- $\dfrac{\alpha(\sigma^{-1}+\eta)}{1-\alpha}(y-y_n)$, so resetting firms move further from $p^e$ as more firms are stuck.
<!-- YW5zOjI= -->
> From the index, $p-p^e=(1-\alpha)(\tilde p-p^e)$, so $\tilde p-p^e=(p-p^e)/(1-\alpha)=\kappa(y-y_n)/(1-\alpha)=(\sigma^{-1}+\eta)(y-y_n)/\alpha$. A check: $\tilde p-p=(\tilde p-p^e)-(p-p^e)=(\sigma^{-1}+\eta)(y-y_n)\,[1/\alpha-(1-\alpha)/\alpha]=(\sigma^{-1}+\eta)(y-y_n)$, which is eq. (16), the marginal-cost equation. As $\alpha\to1$ the few firms that reset move a great deal, but they carry almost no weight, so $p$ hardly moves. Option B is $p-p^e$, the aggregate, not the resetters' price. Options A and D invert the weight.
> Ref: Benigno (2015), §4.1, eqs. (16)–(17) (pp. 507–508); Map [[02-firms-and-as]]
> Similar: Lista 7, Q2

Q: Benigno's aggregate mark-up is $1+\mu=\frac{\theta}{\theta-1}\frac{(1+\tau_w)(1+\tau_c)}{(1-\tau_y)(1-\tau_l)}$, which combines payroll, consumption, sales and labour-income taxes. Which current tax moves both the AS anchor and the position of the AD curve?
- The labour-income tax $\tau_l$, because it cuts the after-tax wage and so lowers both labour supply and the income households spend today.
- The sales tax $\tau_y$, because it raises the price buyers pay for every variety and so lowers the quantity of goods demanded today.
- None of them: taxes sit only in the mark-up $\mu$, so every current tax shifts AS through $y_n$ and leaves the AD curve where it was.
- The consumption tax $\tau_c$, because it is in the mark-up and also in the tax-inclusive real rate behind the Euler equation.
<!-- YW5zOjM= -->
> All four taxes enter $\mu$, so all four move $y_n$ and therefore the AS anchor $(p^e,y_n)$. Only $\tau_c$ is also in the Euler equation. What the household substitutes across dates is the tax-inclusive price of consumption, so AD contains $(\bar\tau_c-\tau_c)$ in the same slot as expected inflation. A current cut in $\tau_c$ therefore lowers $\mu$ (AS moves right) and makes consumption today cheap relative to tomorrow (AD moves right). Option A assumes a current-income consumption function. Option B confuses a tax paid by the firm out of revenue with the demand curve for varieties, and $\tau_y$ is not in the AD curve. Option C misses the Euler channel.
> Ref: Benigno (2015), §3, eqs. (7)–(8) (p. 506); §4, eqs. (12)–(13) (p. 507); Map [[02-firms-and-as]]
> Similar: Lista 7, Q2

Q: In Benigno's model a share of firms keeps its pre-set price and serves whatever demand arrives, while wages and the other prices adjust. An AD expansion pushes output beyond its natural level. What happens to a stuck firm's mark-up, and why does it keep producing?
- Its mark-up shrinks, since the real wage rises with output, but it still serves demand because its price stays above marginal cost.
- Its mark-up is unchanged, because its wage bill was fixed with its price, so it meets the extra demand at a constant marginal cost.
- Its mark-up widens, because its fixed price is now cheap relative to the index and more demand lets it earn a larger profit per unit.
- Its mark-up shrinks to zero at once, so it rations its customers and all output above the natural level comes from the resetting firms.
<!-- YW5zOjA= -->
> Marginal cost is $W/A$. Above $y_n$, the household's intratemporal condition $v_l(L)/u_c(C)=W/P$ requires a higher real wage, because labour is higher ($\eta$) and so is consumption ($\sigma^{-1}$). The stuck firm's price $P^e$ is fixed, so $P^e/(W/A)$ falls. Under monopolistic competition price starts above marginal cost by the factor $\theta/(\theta-1)$, so a small demand shock still leaves selling profitable. That is why output becomes demand-determined. Only wages are flexible in the model, so B is wrong. C confuses higher volume with a higher margin per unit. D ignores the initial mark-up, which is the cushion that makes rationing unnecessary.
> Ref: Benigno (2015), §4, eqs. (9)–(12) (pp. 506–507); §4.1, eq. (16) (p. 508); Map [[02-firms-and-as]]
> Similar: Lista 7, Q1

## nat

Q: In Benigno's model the efficient level of output is $y_e=\frac{1+\eta}{\sigma^{-1}+\eta}a+\frac{\sigma^{-1}}{\sigma^{-1}+\eta}g$, where $a$ is log productivity, $g$ public spending scaled by output, $\sigma$ the output-scaled intertemporal elasticity and $\eta$ the inverse Frisch elasticity. With technology $Y=AL$, what is the response of efficient log hours, $\partial l_e/\partial a$?
- $\dfrac{1+\eta}{\sigma^{-1}+\eta}$, so efficient hours always rise with productivity, by less than one-for-one.
- $\dfrac{1-\sigma^{-1}}{\sigma^{-1}+\eta}$, so efficient hours rise with productivity only when $\sigma$ exceeds one.
- $\dfrac{\sigma^{-1}-1}{\sigma^{-1}+\eta}$, so efficient hours rise with productivity only when $\sigma$ is below one.
- $\dfrac{1-\sigma^{-1}}{1+\eta}$, so efficient hours rise with productivity only when $\sigma$ exceeds one.
<!-- YW5zOjE= -->
> Since $Y=AL$, $l_e=y_e-a$, so $\partial l_e/\partial a=\frac{1+\eta}{\sigma^{-1}+\eta}-1=\frac{1+\eta-\sigma^{-1}-\eta}{\sigma^{-1}+\eta}=\frac{1-\sigma^{-1}}{\sigma^{-1}+\eta}$. Higher productivity raises the return to work (substitution) and also makes the household richer (income, whose strength is $\sigma^{-1}$ through the curvature of $u$). Hours rise only if substitution dominates, $\sigma>1$. Natural output has the same $a$ coefficient, so natural hours respond identically: the mark-up does not change this answer. Option A is $\partial y_e/\partial a$, the output response. C flips the sign. D uses the wrong denominator.
> Ref: Benigno (2015), §4.4, eq. (19) (p. 509); §4.1, eq. (15) (p. 508); Map [[03-natural-and-efficient]]
> Similar: Lista 7, Q3

Q: In Benigno's model the long-run mark-up $\bar\mu>0$ leaves long-run natural output below its efficient level. Which instrument can close that long-run gap?
- A higher long-run price level $\bar p$, because a higher expected price level lowers the real rate and lifts demand toward the efficient level of output.
- Higher long-run public spending $\bar g$, because it raises long-run natural output and so narrows the distance to the efficient level of output.
- A long-run production subsidy that sets $1+\bar\mu=1$, financed by lump-sum taxes, because only the wedge separates natural from efficient output.
- No instrument, because the gap comes from the substitution elasticity $\theta$, a preference parameter, so no decentralised economy reaches it.
<!-- YW5zOjI= -->
> In the long run $\bar y_n-\bar y_e=-\bar\mu/(\sigma^{-1}+\eta)$, and $\bar\mu$ collects $\theta/(\theta-1)$ and the four long-run taxes. A subsidy such as $\bar\tau_y=-1/(\theta-1)$ gives $(1+\bar\mu_\theta)/(1-\bar\tau_y)=1$, which removes the wedge. Lump-sum $T$ in the government constraint (18) pays for it without creating a new distortion. $\bar p$ is the long-run monetary instrument, and money is neutral in the long run, so $\bar p$ does not appear in $\bar y_n$ (A). $\bar g$ moves $\bar y_n$ and $\bar y_e$ by the same coefficient $\sigma^{-1}/(\sigma^{-1}+\eta)$, so the gap is unchanged (B). D treats a market-power wedge as if it were a technological limit.
> Ref: Benigno (2015), §4.2–§4.4, eqs. (13), (18)–(19) (pp. 508–509); Map [[03-natural-and-efficient]]
> Similar: Lista 7, Q3

## geo

Q: In Benigno's model, with AS $p-p^e=\kappa(y-y_n)$ and AD $y=\bar y_n-\sigma[i-(\bar p-p)-\rho]$, where $\bar y_n=\frac{1+\eta}{\sigma^{-1}+\eta}\bar a+\dots$ is long-run natural output, $\bar a$ long-run productivity and $i$, $\bar p$ fixed, what is $dp/d\bar a$?
- $-\dfrac{\kappa(1+\eta)}{(\sigma^{-1}+\eta)(1+\sigma\kappa)}$
- $\dfrac{(1+\eta)}{(\sigma^{-1}+\eta)(1+\sigma\kappa)}$
- $\dfrac{\sigma\kappa(1+\eta)}{(\sigma^{-1}+\eta)(1+\sigma\kappa)}$
- $\dfrac{\kappa(1+\eta)}{(\sigma^{-1}+\eta)(1+\sigma\kappa)}$
<!-- YW5zOjM= -->
> A future productivity gain leaves $y_n$ (and so AS) unchanged and shifts AD right by $d\bar y_n$, through consumption smoothing. Substituting AS into AD gives $y-y_n=[\bar y_n-y_n-\sigma(i-\rho-\bar p+p^e)]/(1+\sigma\kappa)$, so $d(y-y_n)=d\bar y_n/(1+\sigma\kappa)$ and $dp=\kappa\,d(y-y_n)$. With $d\bar y_n=\frac{1+\eta}{\sigma^{-1}+\eta}d\bar a$, the result is $dp/d\bar a=\kappa(1+\eta)/[(\sigma^{-1}+\eta)(1+\sigma\kappa)]>0$. Good news about supply that arrives tomorrow raises prices today, because today it is only a demand shock. Option A borrows the sign of a current supply shock. B is $dy/d\bar a$. C confuses the price response with the output share of a current supply shock.
> Ref: Benigno (2015), §5, eqs. (20)–(21) (pp. 509–511); §4.2 (p. 508); Map [[04-equilibrium-geometry]]
> Similar: Lista 7, Q2

Q: In Benigno's model the current consumption tax $\tau_c$ enters the aggregate mark-up one-for-one, so $dy_n=-d\tau_c/(\sigma^{-1}+\eta)$, and it enters AD as $y=\bar y_n-\sigma[i-(\bar p-p)-(\bar\tau_c-\tau_c)-\rho]$. With AS $p-p^e=\kappa(y-y_n)$, $\kappa=(1-\alpha)(\sigma^{-1}+\eta)/\alpha$, and $i$, $\bar p$, $\bar\tau_c$ fixed, what is $dy/d\tau_c$?
- $-\dfrac{\sigma}{\alpha(1+\sigma\kappa)}$
- $-\dfrac{\sigma}{1+\sigma\kappa}$
- $-\dfrac{(1-\alpha)\sigma}{\alpha(1+\sigma\kappa)}$
- $-\dfrac{\sigma}{\alpha}$
<!-- YW5zOjA= -->
> Equilibrium output is $y=[\bar y_n+\sigma\kappa y_n-\sigma(i-\rho-(\bar\tau_c-\tau_c)-\bar p+p^e)]/(1+\sigma\kappa)$. So $dy=[\sigma\kappa\,dy_n-\sigma\,d\tau_c]/(1+\sigma\kappa)$. The supply channel gives $\sigma\kappa\,dy_n=-\sigma\frac{\kappa}{\sigma^{-1}+\eta}d\tau_c=-\sigma\frac{1-\alpha}{\alpha}d\tau_c$. Adding the demand channel $-\sigma\,d\tau_c$ gives $-\sigma[(1-\alpha)/\alpha+1]=-\sigma/\alpha$, so $dy/d\tau_c=-\sigma/[\alpha(1+\sigma\kappa)]$. A cut in $\tau_c$ moves both curves right, so output rises on both counts. Option B keeps only the demand channel and C only the supply channel. D drops the price feedback, which is the denominator $1+\sigma\kappa$.
> Ref: Benigno (2015), §5, eqs. (20)–(21) (pp. 509–511); §4, eq. (13) (p. 507); Map [[04-equilibrium-geometry]]
> Similar: Lista 7, Q2

Q: In Benigno's two-period model every firm resets its price in the long-run period. How are long-run output $\bar y$ and the long-run price level $\bar p$ determined?
- Both are set where a long-run AD curve, drawn at the long-run nominal rate, crosses a vertical long-run AS curve, so both depend on monetary policy.
- $\bar y$ equals natural output, set by $\bar a$, $\bar g$ and $\bar\mu$, and $\bar p$ is chosen by the central bank, its only long-run role.
- $\bar y$ equals natural output, set by $\bar a$, $\bar g$ and $\bar\mu$, and $\bar p$ must equal $p^e$, since rational firms anticipate it.
- $\bar y$ is set by long-run demand, since output is demand-determined, and $\bar p$ adjusts until long-run demand matches long-run supply.
<!-- YW5zOjE= -->
> With all prices flexible the classical dichotomy holds: $\bar y=\bar y_n$ from the real side, and $\bar p$ appears nowhere in it. The model has no third period, so no long-run Euler equation (no long-run AD) pins $\bar p$. Benigno lets monetary policy choose it, and $\bar p$ then feeds back into today's AD through expected inflation $(\bar p-p)$. Option A invents a long-run demand curve. C confuses $\bar p$ with the pre-set short-run price $p^e$: they coincide only when policy chooses that, which Benigno assumes in his initial equilibrium. D applies the short-run, sticky-price logic to a period where prices are flexible.
> Ref: Benigno (2015), §4.2–§4.3 (p. 508); §5 (pp. 509–511); Map [[03-natural-and-efficient]]
> Similar: Lista 7, Q1
