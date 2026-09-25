---
quiz: "Macro I — Lista 7, Part 2/3: AS–AD shocks (temporary mark-up rise, nominal-rate cut, both gaps)"
tags:
  markup: "Temporary mark-up shock"
  ratecut: "Nominal-rate cut"
  synthesis: "Comparing shocks and horizons"
---

## markup

P: Benigno's two-period model. AS: $p-p^e=\kappa(y-y_n)$. AD: $y=\bar y_n-\sigma[i-(\bar p-p)-\rho]$, with $g=\bar g$ and no tax changes. Here $p$ is the log price level, $p^e$ the pre-set price, $y$ output, $y_n$ natural output, $\bar y_n$ long-run natural output, $\bar p=p^e$ the anchored long-run price level, $i$ the nominal rate, $\rho$ time preference, $\sigma$ the output-scaled intertemporal elasticity, $\eta$ the inverse Frisch elasticity, $\alpha$ the sticky share and $\kappa=(1-\alpha)(\sigma^{-1}+\eta)/\alpha$. Natural output is $y_n=[(1+\eta)a+\sigma^{-1}g-\mu]/(\sigma^{-1}+\eta)$. The economy starts at $y=y_n=y_e=0$, $p=p^e$, $i=\rho$, and the mark-up $\mu$ rises temporarily by $d\mu>0$; the central bank leaves $i$ unchanged.

Q: What is the change in output $dy$?
- $dy=-\dfrac{d\mu}{\sigma^{-1}+\eta}$
- $dy=-\dfrac{\sigma}{1+\sigma\kappa}\cdot\dfrac{d\mu}{\sigma^{-1}+\eta}$
- $dy=-\dfrac{\sigma\kappa}{1+\sigma\kappa}\cdot\dfrac{d\mu}{\sigma^{-1}+\eta}$
- $dy=-\dfrac{\kappa}{1+\sigma\kappa}\cdot\dfrac{d\mu}{\sigma^{-1}+\eta}$
<!-- YW5zOjI= -->
> $dy_n=-d\mu/(\sigma^{-1}+\eta)$, and with AD fixed a current supply shock passes through by $\sigma\kappa/(1+\sigma\kappa)\in(0,1)$. Option A is full pass-through, which would need flexible prices. Option D is the price response, $dp=-\kappa\,dy_n/(1+\sigma\kappa)$, not the output response, and B is missing the $\kappa$. Output falls by less than capacity because the frozen firms keep serving demand at $p^e$.
> Ref: Benigno (2015), §7, Fig. 9, p. 513; closed form of §5
> Similar: Lista 7, Q2(a); [[benigno/06-markup-shocks]] §6.2

Q: What are the signs of the two output gaps at the new equilibrium, where $y_e$ is efficient output and is unaffected by $\mu$?
- $y-y_n>0$ and $y-y_e<0$: above the new natural level, hence rising prices, and below the efficient level, hence lost welfare.
- $y-y_n<0$ and $y-y_e<0$: below both levels, since output fell and both targets are measured against the unchanged pre-shock output.
- $y-y_n>0$ and $y-y_e>0$: above both levels, since prices are rising and rising prices always signal an overheating economy.
- $y-y_n<0$ and $y-y_e>0$: below natural output, which fell by less, and above efficient output, which fell by more than output.
<!-- YW5zOjA= -->
> $d(y-y_n)=-dy_n/(1+\sigma\kappa)>0$, because output falls by less than $y_n$. And $d(y-y_e)=dy<0$, because $y_e$ does not move. By the AS curve, prices move only with $y-y_n$, which explains the inflation; welfare responds to $y-y_e$. Reporting one "output gap" here loses the question.
> Ref: Benigno (2015), §7, p. 513; §4.4, p. 509
> Similar: Lista 7, Q2(a) and Q3; [[benigno/06-markup-shocks]] §6.2

Q: By how much does the AS curve shift vertically, at a given output level?
- By $d\mu$, since each adjusting firm raises its own price by the full rise in the desired mark-up.
- By $\tfrac{\alpha}{1-\alpha}\,d\mu$, since the sticky firms carry the aggregate price level with them.
- By $\kappa\,d\mu$, since the AS slope converts a mark-up change directly into a price change.
- By $\tfrac{1-\alpha}{\alpha}\,d\mu$, since adjusters raise their relative price and the index follows.
<!-- YW5zOjM= -->
> At given $y$, $dp=-\kappa\,dy_n=\kappa\,d\mu/(\sigma^{-1}+\eta)=\tfrac{1-\alpha}{\alpha}d\mu$. Aggregation gives $\tilde p-p=\tfrac{\alpha}{1-\alpha}(p-p^e)$: the adjusters raise their price *relative to the index* by $d\mu$, and since the index rises with them, the aggregate shift is scaled by $(1-\alpha)/\alpha$. Option C forgets to divide by $(\sigma^{-1}+\eta)$.
> Ref: Benigno (2015), eqs. (16)–(17), p. 508
> Similar: [[benigno/02-firms-and-as]] §2.5

P:

Q: Why does the AD curve not move after a *temporary* rise in the mark-up $\mu$, and what would change if the rise were permanent (both $\mu$ and the long-run $\bar\mu$ rise)?
- AD depends on $\mu$ only through the current real rate, which the bank holds fixed; a permanent rise would also leave AD in place for that reason.
- $\mu$ is absent from the AD equation and $\bar y_n$ is unchanged; a permanent rise lowers $\bar y_n$, so AD would also shift down.
- AD is the Euler equation, which only depends on the nominal rate; a permanent rise would shift AD up because firms expect higher prices.
- AD shifts only with fiscal variables; a permanent mark-up rise is equivalent to a permanent tax cut and would shift AD to the right.
<!-- YW5zOjE= -->
> AD is $y=\bar y_n+(g-\bar g)-\sigma[\cdot]$. A current mark-up is not in it, and a temporary shock leaves $\bar\mu$, hence $\bar y_n$, untouched. A permanent rise lowers $\bar y_n$, so households expect to be poorer and consume less today, and AD shifts down. Then $d\bar y_n=dy_n$ makes $d(y-y_n)=0$ and $dp=0$, with output down by the full $dy_n$.
> Ref: Benigno (2015), §7, p. 513 ("leaving other analyses to the reader")
> Similar: [[benigno/06-markup-shocks]] §6.5

## ratecut

P: Benigno's model with AS $p-p^e=\kappa(y-y_n)$ and AD $y=\bar y_n-\sigma[i-(\bar p-p)-\rho]$, where $\kappa=(1-\alpha)(\sigma^{-1}+\eta)/\alpha$ is the AS slope, $\alpha$ the sticky share, $\sigma$ the output-scaled intertemporal elasticity, $\bar p=p^e$ anchored, and $y_n$, $y_e$ and $\bar y_n$ unaffected by monetary policy. The economy starts at $i=r_n$, the natural real rate, with $y=y_n=y_e$ and $p=p^e$. The central bank cuts the nominal rate by $di<0$.

Q: What are the changes in output and the price level?
- $dy=-\dfrac{\sigma}{1+\sigma\kappa}\,di$ and $dp=\kappa\,dy$
- $dy=-\sigma\,di$ and $dp=\kappa\,dy$
- $dy=-\dfrac{1}{1+\sigma\kappa}\,di$ and $dp=\kappa\,dy$
- $dy=-\dfrac{\sigma\kappa}{1+\sigma\kappa}\,di$ and $dp=dy/\kappa$
<!-- YW5zOjA= -->
> From the closed form $y-y_n=\tfrac{\sigma}{1+\sigma\kappa}[r_n-i+(\bar p-p^e)]$ with $r_n$ unchanged. Option B, $-\sigma\,di$, is the *horizontal shift* of AD, and it would be the output response only if the price level stayed put. The price level rises along AS, raising the real rate back up, so output moves by the smaller amount $\sigma/(1+\sigma\kappa)$.
> Ref: Benigno (2015), §5, Figs. 3–5, pp. 509–511
> Similar: Lista 7, Q2(b); [[benigno/04-equilibrium-geometry]] §4.4

Q: Which sequence correctly describes the transmission of the cut?
- The cut raises the money supply, the LM curve shifts right, the interest rate that clears the money market falls, and investment rises until output catches up.
- The cut lowers the long-run price level, households expect deflation, the real rate falls, consumption rises, and firms cut prices to meet the new demand.
- The cut lowers the real rate with long-run prices anchored, households bring consumption forward, sticky firms serve it, and adjusters raise prices.
- The cut raises expected inflation directly, the Phillips curve shifts up, firms raise all prices at once, and output rises only because real wages fall.
<!-- YW5zOjI= -->
> The model has no money market and no LM curve (option A). Monetary policy leaves $\bar p$ anchored (option B inverts this), and $p^e$ is predetermined, so AS does not shift (option D). The channel is the Euler equation: a lower real rate raises current demand. The $\alpha$ sticky firms serve it at $p^e$. Higher hours raise the wage households require, so the $1-\alpha$ adjusters raise prices, which partly offsets the fall in the real rate.
> Ref: Benigno (2015), §3, pp. 505–506; p. 504
> Similar: Lista 7, Q2(b)

P:

Q: With AS slope $\kappa=(1-\alpha)(\sigma^{-1}+\eta)/\alpha$ and a nominal-rate cut $di<0$ starting from $i=r_n$, what does a higher sticky share $\alpha$ do to the effects of the cut?
- More of the cut goes into prices and less into output, because more rigid prices steepen the AS curve and raise the slope $\kappa$.
- More of the cut goes into output and less into prices, because more rigid prices flatten the AS curve and lower the slope $\kappa$.
- The split between output and prices is unchanged, because $\alpha$ enters both the output and the price responses in the same proportion.
- Both output and prices respond more, because a higher $\alpha$ also raises the elasticity of demand to the real rate through $\sigma$.
<!-- YW5zOjE= -->
> $\alpha$ is in the denominator of $\kappa$, so $\partial\kappa/\partial\alpha<0$. With a flatter AS, $dy=-\sigma\,di/(1+\sigma\kappa)$ is larger and $dp=\kappa\,dy$ is smaller. The most common error on this material is option A, saying more rigidity steepens AS. Option D is wrong because $\sigma$ is a preference parameter and does not depend on $\alpha$.
> Ref: Benigno (2015), eq. (17), p. 508
> Similar: [[benigno/02-firms-and-as]] §2.6

## synthesis

P: Benigno's model: AS $p-p^e=\kappa(y-y_n)$, AD $y=\bar y_n-\sigma[i-(\bar p-p)-\rho]$ with $\bar p=p^e$, natural real rate $r_n=\rho+\sigma^{-1}(\bar y_n-y_n)$, and $y-y_n=\tfrac{\sigma}{1+\sigma\kappa}(r_n-i)$. Here $\sigma$ is the output-scaled intertemporal elasticity and $\kappa$ the AS slope. A temporary mark-up rise lowers $y_n$ by $dy_n<0$ and leaves $\bar y_n$ and efficient output $y_e$ unchanged. The economy started at $i=\rho$.

Q: What change in the nominal rate keeps the price level at $p=p^e$ after the shock?
- $di=\kappa\,dy_n$, a cut, which moves AD out until output returns to the efficient level $y_e$.
- $di=0$, since the price level is pinned by $p^e$ and returns to it without any policy response.
- $di=-\dfrac{dy_n}{\sigma(1+\sigma\kappa)}$, a small rise that offsets only the direct price effect of the shock.
- $di=-\dfrac{dy_n}{\sigma}$, a rise that moves $i$ up to the new natural rate $r_n$ and closes $y-y_n$.
<!-- YW5zOjM= -->
> $p=p^e$ requires $y=y_n$, which requires $i=r_n$. Since $dr_n=-dy_n/\sigma>0$, the bank must *raise* the rate by exactly that amount. Output then falls all the way to $y_n'$, the deepest contraction. Option A is the opposite policy: holding $y=y_e$ needs a cut and accepts the largest price rise. The two targets need moves of opposite sign, and that is the trade-off.
> Ref: Benigno (2015), §7, Fig. 9, pp. 513–514
> Similar: Lista 7, Q2(a) and Q4; [[benigno/06-markup-shocks]] §6.3

Q: If instead both the mark-up and its long-run value rise permanently by the same amount ($dy_n=d\bar y_n<0$), what happens with the nominal rate held at $\rho$?
- $r_n$ does not change, so $y-y_n$ and $p-p^e$ stay at zero, output falls by the full $dy_n$, and no rate can close the efficient gap.
- $r_n$ rises by $-dy_n/\sigma$, so the gap turns positive and prices rise, exactly as in the temporary case, with a larger fall in output.
- $r_n$ does not change, so $y-y_n$ and $p-p^e$ stay at zero, output is unchanged, and the permanent mark-up affects only the long-run price level.
- $r_n$ falls by $dy_n/\sigma$, so the gap turns negative and prices fall, which the bank should offset with a cut to hold the price level at $p^e$.
<!-- YW5zOjA= -->
> $dr_n=\sigma^{-1}(d\bar y_n-dy_n)=0$. AD shifts down exactly as much as AS shifts left, so the new crossing is at $y_n'$ with $p=p^e$. The gap against natural output is zero, but the welfare gap $y-y_e=dy_n$ is permanent. It is a supply-side problem, not a stabilisation problem, and no interest rate can close it. Option C forgets that output does fall.
> Ref: Benigno (2015), §7, p. 513
> Similar: [[benigno/06-markup-shocks]] §6.5

P:

Q: A temporary productivity gain and a temporary mark-up fall both shift the AS curve down and to the right in Benigno's model. What distinguishes them for monetary policy?
- Nothing: both raise natural output by the same mechanism, so one nominal rate stabilises prices and welfare at once in either case.
- The productivity gain also shifts AD, because it raises expected long-run income, while the mark-up fall leaves AD in place.
- The productivity gain moves $y_n$ and $y_e$ together, so there is no trade-off; the mark-up fall moves only $y_n$, so a trade-off exists.
- The mark-up fall moves $y_n$ and $y_e$ together, so there is no trade-off; the productivity gain moves only $y_n$, so a trade-off exists.
<!-- YW5zOjI= -->
> Both shift AS through the anchor $(p^e,y_n')$. But $a$ enters the planner's problem while $\mu$ does not, so $dy_e=dy_n$ for productivity and $dy_e=0$ for the mark-up. A trade-off exists if and only if the shock moves $y_n-y_e$, which happens if and only if it moves $\mu$. Option B describes a *permanent* or expected productivity shock, not a temporary one. Option D swaps the two.
> Ref: Benigno (2015), §6.1 and §7, pp. 511–514; §4.4, p. 509
> Similar: Lista 7, Q3; [[benigno/06-markup-shocks]] §6.4
