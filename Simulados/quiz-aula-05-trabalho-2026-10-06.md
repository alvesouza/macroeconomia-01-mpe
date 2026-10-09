---
quiz: "Macro I — Session 5: Labour and Leisure (hard)"
tags:
  meas: "Measurement and flows"
  stat: "Static labour supply"
  elast: "Elasticities and evidence (Frisch, Prescott)"
  dyn: "Dynamic labour supply"
  search: "Search and flow equilibrium"
---

## meas

Q: Over one year a country's participation rate rises, its unemployment rate rises, and its employment-to-population ratio also rises. Which reading is coherent?
- The data are inconsistent, since the employment ratio equals participation times one minus the unemployment rate, so it cannot rise when unemployment does.
- Many people entered the labour force; most found jobs, but entrants still searching lift the unemployment rate, which here signals a stronger market.
- Job losers are leaving for inactivity, which lifts participation and unemployment together, so the market is weakening despite the higher employment ratio.
- Employed workers are moving into unemployment while new entrants take their jobs, so the rise in unemployment reflects only higher separation rates.
<!-- YW5zOjE= -->
> The employment-to-population ratio is $E/\text{PIA}=\frac{E+U}{\text{PIA}}\cdot\frac{E}{E+U}$, participation times $(1-u)$. If participation rises by more than $1-u$ falls, the ratio rises together with $u$, so A is wrong. The coherent story is an inflow of encouraged entrants: most of them get jobs, so employment per person rises, and the ones still searching count as unemployed. This is the mirror image of the discouraged-worker case, and it is why $u$ alone is a poor gauge of labour-market strength. Option C contradicts itself, because people who move to inactivity *lower* participation. Option D cannot explain the rise in participation.
> Ref: Kurlat (2020), cap. 7, §7.1 (pp. 127–131); Map [[01-measurement]]
> Similar: Kurlat, Exercício 7.1 (p. 146); Exercício 7.4 (p. 147); Lista 4

## stat

Q: A household maximises $\ln c+\theta\ln\ell$ subject to $c=w(\bar h-\ell)+\pi$, where $c$ is consumption, $\ell$ leisure, $\bar h$ the time endowment, $w$ the real wage, $\pi>0$ non-wage income and $\theta>0$ the leisure weight. At an interior optimum, what is the uncompensated wage elasticity of hours $h=\bar h-\ell$?
- $\dfrac{\theta\pi}{w\bar h+\theta\pi}$, positive and below one, so hours respond least for workers who are close to the participation threshold.
- $\dfrac{w\bar h}{w\bar h-\theta\pi}$, above one at every wage, so hours always respond more than proportionally to the wage at any interior optimum.
- $-\dfrac{\theta\pi}{w\bar h-\theta\pi}$, negative, so non-wage income makes the labour supply curve bend backward as the wage approaches the threshold.
- $\dfrac{\theta\pi}{w\bar h-\theta\pi}$, positive and unbounded as $w$ falls toward $\theta\pi/\bar h$, the reservation wage at which participation stops.
<!-- YW5zOjM= -->
> Leisure is $\ell=\frac{\theta}{1+\theta}\cdot\frac{w\bar h+\pi}{w}$, so $h=\bar h-\ell=\frac{w\bar h-\theta\pi}{(1+\theta)w}$. Then $\frac{d\ln h}{d\ln w}=\frac{w\bar h}{w\bar h-\theta\pi}-1=\frac{\theta\pi}{w\bar h-\theta\pi}$. Option B forgets the $-1$ that comes from the $w$ in the denominator. The elasticity is positive because $\pi$ does not scale with the wage, so the income effect is weaker than the substitution effect. With $\pi=0$ it is exactly zero. Interior hours need $w\bar h>\theta\pi$, that is $w>w^r=\theta\pi/\bar h$, and the elasticity explodes as $w\to w^r$: near the participation corner, a small wage change makes a large proportional change in hours. Option A has the sign inside the denominator wrong, which reverses that conclusion.
> Ref: Kurlat (2020), cap. 7, §7.2 (pp. 131–137); Map [[02-static-model]]
> Similar: Kurlat, Exercício 7.2 (p. 147); Lista 4, Q1(a)

Q: A growth model uses $u(c,h)=\frac{c^{1-\sigma}}{1-\sigma}-v(h)$ with $\sigma>1$, $v$ increasing and convex, $c$ consumption and $h$ hours, while the real wage $w$ grows forever at a constant rate. What happens to hours along the growth path?
- Hours trend toward zero, because with $\sigma>1$ the income effect of each permanent wage rise outweighs the substitution effect.
- Hours rise without bound, because with $\sigma>1$ consumption utility is more curved, so the substitution effect of each permanent wage rise dominates.
- Hours stay constant, because additive separability between consumption and hours is enough to make the income and substitution effects cancel.
- Hours stay constant only if $v$ is isoelastic, $v(h)=\chi h^{1+\eta}/(1+\eta)$, since the wage then enters the first-order condition multiplicatively.
<!-- YW5zOjA= -->
> The intratemporal condition is $v'(h)=w\,c^{-\sigma}$. If hours were constant, $c$ would grow with $w$, so the right side would scale as $w^{1-\sigma}$. With $\sigma>1$ that tends to zero, which forces $v'(h)$, and so $h$, down over time. Hours decline toward zero. Only $\sigma=1$, that is $\ln c+v(\cdot)$, or a multiplicative form $\frac{c^{1-\sigma}}{1-\sigma}v(\ell)$, keeps hours constant as wages grow (King–Plosser–Rebelo). Additive separability alone is not enough (C), and the shape of $v$ cannot rescue it (D). Benigno can use this form because his model has two periods and no growth.
> Ref: Kurlat (2020), cap. 7, §7.2 (pp. 131–137); Map [[02-static-model]]
> Similar: Kurlat, Exercício 7.5 (p. 148); Lista 4, Q1

## elast

Q: Two economies share preferences $\ln c-\chi\frac{h^{1+\eta}}{1+\eta}$ and the real wage $w$, where $c$ is consumption, $h$ hours and $\chi,\eta>0$. Economy $i\in\{EU,US\}$ taxes labour income at rate $\tau_i$ and rebates all revenue as a lump sum $T_i$, so $c=(1-\tau_i)wh+T_i$ with $T_i=\tau_i wh$ in equilibrium. What is $h_{EU}/h_{US}$?
- $\left(\dfrac{1-\tau_{EU}}{1-\tau_{US}}\right)^{1/\eta}$, so the hours gap equals the Frisch elasticity $1/\eta$ applied to the net-of-tax gap.
- $\left(\dfrac{1-\tau_{US}}{1-\tau_{EU}}\right)^{1/(1+\eta)}$, so the higher-tax economy works more, because its lump-sum transfer is larger.
- $\left(\dfrac{1-\tau_{EU}}{1-\tau_{US}}\right)^{1/(1+\eta)}$, so hours never fall proportionally more than the net-of-tax rate does.
- $\left(\dfrac{1-\tau_{EU}}{1-\tau_{US}}\right)^{\eta/(1+\eta)}$, so a smaller Frisch elasticity makes the hours gap between them wider.
<!-- YW5zOjI= -->
> The first-order condition is $\chi h^{\eta}=(1-\tau)w/c$. Multiply by $h$: $\chi h^{1+\eta}=(1-\tau)wh/c$. With full rebate, $c=(1-\tau)wh+\tau wh=wh$, so $\chi h^{1+\eta}=1-\tau$. Dividing the two economies cancels $\chi$ and gives C. The exponent is $\frac{1}{1+\eta}=\frac{\varepsilon^F}{1+\varepsilon^F}<1$, not $1/\eta$ (A): multiplying by $h$ adds one to the power, because the rebate ties consumption to hours. So matching a large hours gap with taxes needs a very large Frisch elasticity, which is the core of the critique of Prescott. Option D runs the wrong way, since a smaller elasticity (larger $\eta$) shrinks the gap.
> Ref: Kurlat (2020), cap. 7, §7.3 (pp. 137–140); Map [[03-elasticities-and-evidence]]
> Similar: Kurlat, Exercício 7.5 (p. 148); Lista 4, Q1(b)

Q: In two economies every household has the same small intensive-margin hours elasticity. In one, many households have reservation wages close to the market wage; in the other, reservation wages lie far from it. How do aggregate hours respond to a small transitory wage change?
- Identically in both, because the aggregate elasticity is the average of individual elasticities, and those are equal across the two by assumption.
- Much more in the first, because participation is a discrete choice, so the aggregate response depends on how many households sit near the threshold.
- Much more in the second, because households far from their reservation wage have more room to adjust their hours on the intensive margin.
- Identically in both, because a transitory change leaves lifetime wealth almost unchanged, so reservation wages and participation do not move.
<!-- YW5zOjE= -->
> At the corner, a household works only if $w>w^r$. A small wage change does nothing to households far from the threshold, but it moves into or out of work everyone close to it. The aggregate elasticity therefore reflects the *density* of households near $w^r$, not the average individual elasticity (A). This is the Rogerson indivisible-labour argument, and it is the main reconciliation of small micro estimates with the large aggregate elasticity that macro models need. It also fits the fact that the extensive margin carries most cyclical hours. Option D confuses wealth with the price of current time: a transitory wage rise does make working now more attractive.
> Ref: Kurlat (2020), cap. 7, §7.3 (pp. 137–140); §7.2 (pp. 131–137); Map [[03-elasticities-and-evidence]]
> Similar: Kurlat, Exercício 7.6 (p. 149); Lista 4

Q: Suppose Prescott is right that higher effective labour taxes, rebated lump-sum, explain why Europeans work fewer hours than Americans. What follows for comparing European and US welfare?
- The welfare gap equals the GDP-per-person gap, since the taxes are rebated, so households keep the resources they would have had anyway.
- Europeans are better off than GDP suggests, and their allocation is efficient, because they freely choose leisure at the after-tax wage.
- The welfare gap exceeds the GDP-per-person gap, because the taxes destroy output and also force leisure on households who would rather work.
- The GDP gap overstates the welfare gap, as extra leisure is valued, yet European hours remain inefficiently low, driven by a tax wedge.
<!-- YW5zOjM= -->
> If hours are lower because after-tax leisure is cheap, Europeans are buying leisure that GDP does not count. A welfare measure with a leisure term, such as Jones–Klenow, closes part of the gap. But the price they respond to is distorted: the rebate removes the income effect and leaves the wedge between the marginal product and the after-tax wage in place, so there is a deadweight loss. That is why B is wrong to call the allocation efficient. Option A ignores leisure. Option C gets the direction wrong, since hours are chosen, not forced, and leisure has value.
> Ref: Kurlat (2020), cap. 7, §7.3 (pp. 137–140); cap. 2, §2.2 (pp. 35–40); Map [[03-elasticities-and-evidence]]
> Similar: Kurlat, Exercício 7.5 (p. 148); Exercício 2.9 (p. 43)

## dyn

Q: A household maximises $\ln c_1-\chi\frac{h_1^{1+\eta}}{1+\eta}+\beta\left[\ln c_2-\chi\frac{h_2^{1+\eta}}{1+\eta}\right]$ subject to $c_1+\frac{c_2}{1+r}=w_1h_1+\frac{w_2h_2}{1+r}$, where $c_t$, $h_t$, $w_t$ are consumption, hours and the real wage in period $t$, $\beta\in(0,1)$ the discount factor, $r$ the real interest rate and $\chi,\eta>0$. What is $h_1/h_2$, and where does a lower $\beta$ shift work?
- $\left[\beta(1+r)\dfrac{w_1}{w_2}\right]^{1/\eta}$, so a more impatient household shifts work toward period 2 and borrows to consume now.
- $\left[\beta(1+r)\dfrac{w_1}{w_2}\right]^{1/\eta}$, so a more impatient household shifts work toward period 1, as it discounts future pay.
- $\left[\dfrac{w_1}{\beta(1+r)w_2}\right]^{1/\eta}$, so a more impatient household shifts work toward period 1 and saves the extra pay.
- $\left[\beta(1+r)\dfrac{w_1}{w_2}\right]^{\eta}$, so a more impatient household shifts work toward period 2 and borrows to consume now.
<!-- YW5zOjA= -->
> With multiplier $\mu$ on the budget, the labour conditions are $\chi h_1^{\eta}=\mu w_1$ and $\beta\chi h_2^{\eta}=\mu w_2/(1+r)$. Dividing gives $(h_1/h_2)^{\eta}=\beta(1+r)\,w_1/w_2$, and taking the power $1/\eta$ gives A. A lower $\beta$ lowers $h_1/h_2$: the disutility of future work is discounted more, so working later is cheap in utility terms, and the impatient household consumes now and pays by working later. Option B has the right formula but the wrong reading. Option C inverts $\beta(1+r)$. Option D uses $\eta$ where the relative-wage elasticity should be the Frisch $1/\eta$. By the same product, a higher $r$ raises current hours.
> Ref: Kurlat (2020), cap. 7, §7.4 (pp. 140–142); Map [[04-dynamic-labour-supply]]
> Similar: Kurlat, Exercício 7.6 (p. 149); Exercício 7.8 (p. 150)

Q: Over a century real wages rose several-fold while hours per worker changed comparatively little, yet business-cycle models need hours to respond strongly to wages. How can one model with $\ln c$ utility and no non-wage income deliver both?
- Secular wage growth was anticipated while cyclical changes are surprises, and in an optimising model only unanticipated wage changes move hours.
- The secular rise came from capital deepening and the cyclical moves from TFP, and in an optimising model only TFP-driven wage changes move hours.
- The secular rise is permanent, so the Marshallian elasticity (zero here) applies; cyclical moves are transitory, so the larger Frisch elasticity applies.
- The secular rise is permanent, so the Frisch elasticity (zero here) applies; cyclical moves are transitory, so the larger Marshallian elasticity applies.
<!-- YW5zOjI= -->
> When every period's wage is scaled by $k$, consumption scales by $k$ and hours do not change: the income and substitution effects cancel, so the Marshallian elasticity is zero. This is the balanced-growth restriction. A transitory rise changes the relative wage $w_1/w_2$ while barely moving lifetime wealth, so hours reallocate with the Frisch elasticity. The two facts are about different experiments, not a contradiction. Option D swaps the elasticities, and the Frisch one is the larger. Option A is wrong because a fully anticipated transitory wage rise also moves hours in the two-period model. The empirical objection is that the Frisch elasticity the cycle requires exceeds micro estimates.
> Ref: Kurlat (2020), cap. 7, §7.4 (pp. 140–142); §7.2 (pp. 131–137); Map [[04-dynamic-labour-supply]]
> Similar: Kurlat, Exercício 7.6 (p. 149); Exercício 7.8 (p. 150)

## search

Q: In a labour force of fixed size, $u_t$ is the unemployment rate; each period a fraction $\lambda$ of the employed lose their jobs and a fraction $f$ of the unemployed find one, with $0<\lambda+f<1$ and $u^*=\lambda/(\lambda+f)$. How does the gap $u_t-u^*$ evolve?
- $u_{t+1}-u^*=(1-f)(u_t-u^*)$, so convergence speed depends only on the job-finding rate and not at all on the separation rate.
- $u_{t+1}-u^*=(1-\lambda-f)(u_t-u^*)$, so at equal $u^*$ an economy with larger gross flows returns to its steady state faster.
- $u_{t+1}-u^*=(\lambda+f)(u_t-u^*)$, so at equal $u^*$ an economy with larger gross flows returns to its steady state more slowly.
- $u_{t+1}-u^*=(1-\lambda)(u_t-u^*)$, so convergence speed depends only on the separation rate and not at all on the job-finding rate.
<!-- YW5zOjE= -->
> The law of motion is $u_{t+1}=u_t+\lambda(1-u_t)-fu_t=\lambda+(1-\lambda-f)u_t$. Subtract $u^*=\lambda+(1-\lambda-f)u^*$, which is the same equation at the fixed point, and B follows. Each period a share $\lambda+f$ of the gap closes, so separations speed up convergence as much as hiring does. Options A and D each drop one flow. Two economies with the same $u^*$ but tripled flows differ both in spell length ($1/f$) and in how fast a shock to unemployment dies out. Option C inverts the persistence factor.
> Ref: Kurlat (2020), cap. 7, §7.5 (pp. 142–150); §7.1 (pp. 127–131); Map [[05-search-and-equilibrium]]
> Similar: Kurlat, Exercício 7.7 (p. 150); Lista 4, Q2

Q: More generous unemployment benefits lengthen unemployment spells. Suppose much of that response comes from workers with no savings and no access to credit. What does this imply for the case for benefits?
- It strengthens it, because those workers were taking the first offer out of need, so their longer search is partly efficient rather than moral hazard.
- It weakens it, because constrained workers respond most to benefits, so their longer spells are the purest form of moral hazard in the search model.
- It is irrelevant, because whatever the reason, a higher benefit raises the reservation wage, lowers the finding rate and raises steady-state unemployment.
- It strengthens it, because constrained workers have reservation wages unaffected by benefits, so benefits insure them without raising unemployment at all.
<!-- YW5zOjA= -->
> A worker who cannot borrow accepts a poor offer because search is unaffordable, not because it is unattractive. Benefits relax that constraint, so this part of the duration response moves the worker toward the search an unconstrained worker would choose. It is a liquidity effect, not a distortion, and it often comes with better matches. Option C treats every rise in $u^*$ as a cost, which skips the welfare question. Option D contradicts the premise, since these workers' spells do lengthen. The optimal benefit is interior: it trades the moral-hazard part of the duration response against insurance and liquidity value.
> Ref: Kurlat (2020), cap. 7, §7.5 (pp. 142–150); Map [[05-search-and-equilibrium]]
> Similar: Kurlat, Exercício 7.8 (p. 150); Lista 4, Q2
