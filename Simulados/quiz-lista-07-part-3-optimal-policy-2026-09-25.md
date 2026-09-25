---
quiz: "Macro I — Lista 7, Part 3/3: optimal policy (the loss, the AS constraint, the targeting rule)"
tags:
  solve: "Solving the constrained loss"
  meaning: "Reading the loss and the constraint"
  limits: "What the constraint forbids"
---

## solve

P: A central bank chooses output $y$ and the log price level $p$ to minimise $\mathcal L=\phi_y(y-y^*)^2+\phi_p(p-p^e)^2$, with $\phi_y,\phi_p>0$, output target $y^*$ and pre-set price $p^e$. It is subject to the AS curve $p-p^e=\kappa(y-y_n)$, where $\kappa>0$ is the AS slope and $y_n$ natural output.

Q: Which condition characterises the optimum (the targeting rule)?
- $\phi_y(y-y^*)+\phi_p(p-p^e)=0$
- $\phi_y(y-y^*)+\kappa\,\phi_p(p-p^e)=0$
- $\kappa\,\phi_y(y-y^*)+\phi_p(p-p^e)=0$
- $\phi_y(y-y^*)-\kappa\,\phi_p(p-p^e)=0$
<!-- YW5zOjE= -->
> The Lagrangian first-order conditions are $2\phi_y(y-y^*)-\lambda\kappa=0$ and $2\phi_p(p-p^e)+\lambda=0$. Eliminating $\lambda$ gives $\phi_y(y-y^*)=-\kappa\phi_p(p-p^e)$. Geometrically it is the tangency of an iso-loss ellipse with the AS line: the marginal rate of substitution between the targets equals the transformation rate $\kappa$. Option D has the wrong sign, and it would put the optimum where both gaps share a sign.
> Ref: Benigno (2015), §11, eq. (34), p. 522
> Similar: Lista 7, Q4; [[benigno/10-optimal-policy]] §10.2

Q: What is optimal output?
- $y^o=\dfrac{\phi_y\,y^*+\phi_p\kappa\,y_n}{\phi_y+\phi_p\kappa}$
- $y^o=\dfrac{\phi_p\kappa^2\,y^*+\phi_y\,y_n}{\phi_y+\phi_p\kappa^2}$
- $y^o=\dfrac{\phi_y\,y^*+\phi_p\,y_n}{\phi_y+\phi_p}$
- $y^o=\dfrac{\phi_y\,y^*+\phi_p\kappa^2\,y_n}{\phi_y+\phi_p\kappa^2}$
<!-- YW5zOjM= -->
> Substitute AS into the loss: $\mathcal L=\phi_y(y-y^*)^2+\phi_p\kappa^2(y-y_n)^2$. The minimiser is the weighted average with weights $\phi_y$ on the target and $\phi_p\kappa^2$ on $y_n$. The price weight enters squared in $\kappa$ because a unit of output gap costs $\kappa$ units of price surprise, and the surprise is squared. Option B swaps the weights, which would make a hawkish bank stay closer to $y^*$.
> Ref: Benigno (2015), §11, pp. 522–523
> Similar: Lista 7, Q4

Q: What is the minimum loss at the optimum?
- $\mathcal L^o=\dfrac{\phi_y\phi_p\kappa^2}{\phi_y+\phi_p\kappa^2}\,(y^*-y_n)^2$
- $\mathcal L^o=\dfrac{\phi_y\phi_p\kappa}{\phi_y+\phi_p\kappa}\,(y^*-y_n)^2$
- $\mathcal L^o=\dfrac{\phi_y+\phi_p\kappa^2}{\phi_y\phi_p\kappa^2}\,(y^*-y_n)^2$
- $\mathcal L^o=\dfrac{\phi_y\phi_p\kappa^2}{\phi_y+\phi_p\kappa^2}\,(y^*-y_n)$
<!-- YW5zOjA= -->
> For $\min_y\,a(y-A)^2+b(y-B)^2$ the value is $\tfrac{ab}{a+b}(A-B)^2$. Here $a=\phi_y$, $b=\phi_p\kappa^2$, $A=y^*$ and $B=y_n$. The loss is zero if and only if $y^*=y_n$, which is the whole content of the divine coincidence. Option D drops the square and would give a negative loss when $y^*<y_n$.
> Ref: Benigno (2015), §11, p. 522
> Similar: Lista 7, Q4

P:

Q: With Benigno's welfare weights $\phi_y=\tfrac12$, $\phi_p=\theta/(2\kappa)$ and target $y^*=y_e$, where $\theta$ is the goods-substitution elasticity, $\kappa$ the AS slope and $y_e$ efficient output, what fraction of a mark-up shock does the optimal policy let into prices, relative to strict output stabilisation?
- $\kappa/(1+\theta\kappa)$
- $\theta\kappa/(1+\theta\kappa)$
- $1/(1+\theta\kappa)$
- $1/(1+\kappa)$
<!-- YW5zOjI= -->
> The share into prices is $\phi_y/(\phi_y+\phi_p\kappa^2)=\tfrac12/(\tfrac12+\tfrac{\theta\kappa}{2})=1/(1+\theta\kappa)$. The rest, $\theta\kappa/(1+\theta\kappa)$ (option B), is absorbed as lost output. Under Benigno's calibration, with $\theta=8$ and $\kappa\approx1.13$, about one tenth of the shock reaches prices. The targeting rule becomes his eq. (34), $(y-y_e)+\theta(p-p^e)=0$.
> Ref: Benigno (2015), eqs. (33)–(34), p. 522; fn. 24; calibration p. 515
> Similar: Lista 7, Q4; [[benigno/10-optimal-policy]] §10.4

## meaning

Q: A central bank sets only the nominal rate $i$, which appears in the AD curve $y=\bar y_n-\sigma[i-(\bar p-p)-\rho]$ but not in the AS curve $p-p^e=\kappa(y-y_n)$. Why is its loss minimised subject to AS rather than to AD?
- Because AD is only a long-run relation, while AS holds in the short run, when the loss is evaluated and the rate can move.
- Because AS is derived from optimising firms and AD from an identity, so only AS carries economic content that restricts the bank.
- Because both curves restrict the bank, but AS binds first since its slope $\kappa$ is steeper than the AD slope $-1/\sigma$.
- Because AD contains the free instrument, so any point on AS is reachable by some rate, and AS is the one relation policy cannot shift.
<!-- YW5zOjM= -->
> Moving $i$ slides AD along AS, so the feasible set is exactly the AS line: an opportunity frontier, as a budget line is for a consumer. AD restricts nothing, because for any target point there is a rate that puts AD through it; it only tells the bank which rate implements its choice. AD is not an identity (option B); it is the Euler equation.
> Ref: Benigno (2015), §11, pp. 521–522
> Similar: Lista 7, Q4

Q: The loss $\mathcal L=\phi_y(y-y^*)^2+\phi_p(p-p^e)^2$ is convex and symmetric in both gaps. What does that imply for a central bank facing a shock that separates $y_n$ from $y^*$?
- It hits the target with the larger weight exactly and leaves all of the adjustment to the other variable.
- It spreads the miss across both targets, since the marginal loss is small near each target and grows fast.
- It accepts a boom above $y^*$ more readily than a recession below it, because the loss is steeper on the left.
- It chooses whichever corner, strict price or strict output stability, gives the smaller total loss.
<!-- YW5zOjE= -->
> With quadratic losses the marginal cost of a deviation is zero at the target and rises linearly. So the first units of miss on each target are almost free, and the optimum is interior, a tangency, never a corner unless one weight is infinite. Symmetry rules out option C: booms and recessions of equal size cost the same. The bank stabilises around $y^*$; it does not push output up.
> Ref: Benigno (2015), §11, p. 522
> Similar: Lista 7, Q4

Q: Why is the price term in the welfare-based loss the surprise $p-p^e$ rather than the price level $p$ itself?
- Because only unanticipated price movements separate the firms that adjusted from those stuck at $p^e$, and that dispersion is what costs welfare.
- Because the central bank cannot control the level of $p$ at all, so the only price variable it can be held accountable for is the surprise.
- Because an anticipated price level raises the real interest rate one for one, which is already penalised by the output term of the loss.
- Because $p^e$ is the inflation target announced by the bank, so the term measures the bank's credibility and not a welfare cost.
<!-- YW5zOjA= -->
> With a share $\alpha$ of prices frozen at $p^e$, a surprise creates relative-price dispersion across otherwise identical goods, so consumers' purchases are inefficiently spread. An anticipated price level is set by every firm alike, creates no dispersion, and costs nothing in this model. Option D misreads $p^e$: it is pre-set by firms, not announced by the bank.
> Ref: Benigno (2015), §11, eq. (33), p. 522
> Similar: [[benigno/10-optimal-policy]] §10.1

Q: In Benigno's $(y,p)$ diagram, the targeting line $(y-y_e)+\phi(p-p^e)=0$ has slope $-1/\phi$, where $\phi$ is the mandate's weight on prices, and AD has slope $-1/\sigma$. After a mark-up rise, relative to doing nothing, which bank cuts the nominal rate?
- A bank with $\phi>\sigma$, whose targeting line is flatter than AD, since it wants output back toward $y_e$ first.
- A bank with $\phi=\theta$, the welfare weight, since households always prefer output stability after a cost shock.
- A bank with $\phi<\sigma$, whose targeting line is steeper than AD, since it leans toward output.
- No bank at all, since a mark-up shock raises the natural rate and every mandate therefore requires a higher rate.
<!-- YW5zOjI= -->
> Doing nothing puts the economy at the AS–AD crossing. If the targeting line is steeper than AD (a dove), its intersection with the new AS lies to the right of that point, so AD must move out and the rate is cut. A hawk, with a flatter line, sits left of it and raises the rate. Benigno, p. 522: the sign of the optimal response to a cost-push shock is a property of the mandate, not of the economy. Under the welfare weight, $\theta=8>\sigma$, so the bank raises the rate.
> Ref: Benigno (2015), §11, eq. (35), Fig. 14, pp. 522–523; fn. 24
> Similar: Lista 7, Q4; [[benigno/10-optimal-policy]] §10.4–10.5

## limits

Q: For which shock is the loss-minimising outcome exactly $y=y^*=y_e$ and $p=p^e$, with zero loss, where $y_e$ is efficient output and $y_n$ natural output?
- A temporary rise in the mark-up, because the bank can raise the rate until output and prices both return to their targets.
- A temporary rise in productivity, because it moves both levels together, so AS passes through the bliss point.
- A permanent rise in the mark-up, because the long-run shift in AD offsets the shift in AS and leaves the bliss point on AS.
- A rise in the payroll tax, because the bank can offset the tax wedge through the real rate and restore efficient output.
<!-- YW5zOjE= -->
> Zero loss requires $y^*=y_n$ after the shock, so AS must pass through $(y_e,p^e)$. Productivity (and spending) moves both levels equally; the bank sets $i=r_n$ and hits both targets: the divine coincidence. Every mark-up shock, including a payroll tax (option D) and a permanent rise (option C), moves $y_n$ but not $y_e$. A permanent one gives zero price gap but a permanent efficient gap, which no rate can close.
> Ref: Benigno (2015), §6.1 and §11, pp. 511–512, 522
> Similar: Lista 7, Q3–Q4; [[benigno/05-productivity-shocks]]

Q: A central bank with loss $\phi_y(y-y^*)^2+\phi_p(p-p^e)^2$ sets $y^*$ permanently above natural output $y_n$, and firms set $p^e$ rationally before each period. What happens on average?
- Output settles permanently between $y_n$ and $y^*$, with a constant positive price surprise that firms learn to accept every period.
- Output reaches $y^*$ on average, because the bank moves the nominal rate after $p^e$ is set, so firms can never offset its policy.
- Output stays at $y^*$ only while the bank is credible, after which the AS curve itself shifts right toward the efficient level.
- Output equals $y_n$ on average, because firms build any systematic surprise into $p^e$, so only unforeseen shocks move output.
<!-- YW5zOjM= -->
> With rational pre-set prices, surprises average zero: $E[p-p^e]=0$, and by AS, $E[y-y_n]=0$. A bank that wants output above $y_n$ every period tries to surprise every period, and price-setters anticipate it. That is the time-inconsistency logic of Kydland–Prescott and Barro–Gordon. It is why Benigno approximates welfare around an efficient steady state, where $y_n=y_e$ absent shocks (fn. 21, p. 522). Option B confuses reacting to *shocks* with systematically exploiting AS.
> Ref: Benigno (2015), §11, fn. 21, p. 522
> Similar: Lista 7, Q4; [[benigno/10-optimal-policy]] §10.5
