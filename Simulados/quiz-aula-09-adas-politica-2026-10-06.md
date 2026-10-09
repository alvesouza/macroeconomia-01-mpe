---
quiz: "Macro I — Session 9: AD-AS Policy Analysis (hard)"
tags:
  prod: "Productivity shocks"
  markup: "Markup shocks"
  fiscal: "Fiscal multipliers"
  zlb: "Liquidity trap / ZLB"
  delev: "Deleveraging"
  opt: "Optimal policy"
---

## prod

Q: In Benigno's AS-AD model, current productivity $a$ rises by $da$ and long-run productivity $\bar a$ by $\lambda\,da$ ($0\le\lambda\le1$); natural output in each period moves by $\frac{1+\eta}{\sigma^{-1}+\eta}$ times that period's productivity change, the natural real rate is $r_n=\rho+\sigma^{-1}(\bar y_n-y_n)$, $\sigma$ is the output-scaled intertemporal elasticity and $\eta$ the inverse Frisch elasticity. Which change in the nominal rate $i$ keeps $p=p^e$ and closes the gap?
- $di=-\dfrac{(1-\lambda)(1+\eta)}{\sigma^{-1}+\eta}\,da$
- $di=+\dfrac{(1-\lambda)(1+\eta)}{1+\sigma\eta}\,da$
- $di=-\dfrac{(1-\lambda)(1+\eta)}{1+\sigma\eta}\,da$
- $di=-\dfrac{(1-\lambda)(1+\eta)}{\sigma(1+\sigma\eta)}\,da$
<!-- YW5zOjI= -->
> The rule that never fails is to move $i$ to the new $r_n$. Here $dy_n=k\,da$ and $d\bar y_n=\lambda k\,da$ with $k=(1+\eta)/(\sigma^{-1}+\eta)$, so $dr_n=\sigma^{-1}(\lambda-1)k\,da$. Since $\sigma^{-1}/(\sigma^{-1}+\eta)=1/(1+\sigma\eta)$ (multiply top and bottom by $\sigma$), $di=-(1-\lambda)(1+\eta)\,da/(1+\sigma\eta)$. The two endpoints check it: $\lambda=0$ is the temporary case, a cut of $dy_n/\sigma$; $\lambda=1$ is the permanent case, no move at all. Option A leaves out the $\sigma^{-1}$ that turns a change in expected growth into a change in the real rate. Option B has the sign the wrong way round: a gain that is expected to fade lowers $r_n$. Option D divides by $\sigma$ a second time.
> Ref: Benigno (2015), §6.1–§6.2 (pp. 511–513), eq. (15); Map [[05-productivity-shocks]]
> Similar: Lista 7, Q2(b); [[benigno/04-equilibrium-geometry]] §4.3

Q: An economy sits at nominal rate $i=0$ with natural real rate $r_n=0$, long-run price level $\bar p$ equal to the preset level $p^e$, and output at natural $y_n$; a temporary productivity gain then raises $y_n$, long-run natural output unchanged, with AD slope $-1/\sigma$ and AS slope $\kappa>0$. What follows?
- Output rises by less than $y_n$, prices fall and the gap stays negative; with no room to cut $i$, closing it takes a promise of $\bar p-p^e=\sigma^{-1}dy_n$.
- Output falls and prices fall, because cheaper goods raise the real burden of debt; this is the paradox of toil, which holds whenever $i$ sits at zero.
- Output rises one-for-one with $y_n$ and $p$ stays at $p^e$, since the shock keeps $y_n=y_e$ and the divine coincidence holds at any nominal rate.
- Output rises by less than $y_n$, prices fall and the gap stays negative; with no room to cut $i$, closing it takes a promise of $\bar p-p^e=\sigma\,dy_n$.
<!-- YW5zOjA= -->
> AD does not move, because current productivity is not in it, while AS shifts down. So the gap opens at $-dy_n/(1+\sigma\kappa)$ and prices fall. The natural rate falls to $r_n'=-\sigma^{-1}dy_n<0$, and the cut that would normally fix this is blocked by the floor. At $i=0$ the gap is $\frac{\sigma}{1+\sigma\kappa}[r_n'+(\bar p-p^e)]$, so closing it takes $\bar p-p^e=-r_n'=\sigma^{-1}dy_n$. Option D inverts that factor. Option C is wrong because the divine coincidence says one instrument *can* reach both targets; at the floor that instrument is gone. Option B borrows the paradox of toil, which needs an upward-sloping AD (debt, with $\bar p$ tied to $p$), not just a zero rate. With AD sloping down, output still rises.
> Ref: Benigno (2015), §6.1 (pp. 511–512); §9 (pp. 516–518); Map [[05-productivity-shocks]]; [[08-liquidity-trap]]
> Similar: [[benigno/08-liquidity-trap]] §8.2–§8.4

## markup

Q: In Benigno's model, two temporary tax rises raise the aggregate mark-up $\mu$ by the same amount: one on payroll ($\tau_w$), one on consumption ($\tau_c$, which also enters AD through the term $\bar\tau_c-\tau_c$). With the nominal rate $i$ and long-run price level $\bar p$ held, and $\eta$ the inverse Frisch elasticity, how do outcomes compare?
- Both taxes shift only AS, and by the same amount, so both produce the same stagflation: the same fall in output and the same rise in $p$ relative to $p^e$.
- The consumption tax also shifts AD up, as households buy before prices climb further, so output falls by less and $p$ rises by more than under the payroll tax.
- The consumption tax shifts only AD, being paid by households rather than firms, so it lowers output and $p$ while leaving natural output $y_n$ unchanged.
- The consumption tax also shifts AD down, so output falls by more than under the payroll tax, and $p$ does not rise: it falls, or stays put if $\eta=0$.
<!-- YW5zOjM= -->
> Both taxes raise $\mu$ by the same amount, so the AS shift is identical. $\tau_c$ also sits in the AD bracket in the slot of expected inflation: a tax that is high now and lower later makes current consumption dearer, and AD shifts down. On output, $m_{\tau_c}-m_\tau=\sigma m_g-\kappa\sigma/D=(1+\sigma\eta)/D>0$, so the consumption tax costs more output. On prices, $dp=\kappa\,d(y-y_n)$. By (23) the payroll tax opens a positive gap ($+m_{\bar\tau}$), so $p$ rises. The consumption tax gives $-m_{\bar\tau_c}=-\sigma\eta/D\le0$, so $p$ falls, and is unchanged at $\eta=0$. Option A misses the AD channel. Option B gets its direction wrong. Option C drops the mark-up channel, which is still there.
> Ref: Benigno (2015), §7 (p. 513); §8 (pp. 514–515), eqs. (13), (22)–(23); Map [[06-markup-shocks]]
> Similar: Lista 7, Q2(a); [[benigno/07-fiscal-multipliers]] §7.4

## fiscal

Q: In Benigno's model, a temporary spending rise $dg$ is financed by an equal temporary rise $d\tau=dg$ in the sales/payroll tax $\tau$ (a mark-up component), long-run instruments fixed; with $D\equiv(\sigma^{-1}+\eta)(1+\sigma\kappa)$, $\sigma$ the output-scaled intertemporal elasticity, $\eta$ the inverse Frisch elasticity and $\kappa$ the AS slope, what is the change in the gap $y-y_n$?
- $d(y-y_n)=\dfrac{\eta-\sigma\kappa}{D}\,dg$
- $d(y-y_n)=\dfrac{1+\eta}{D}\,dg$
- $d(y-y_n)=\dfrac{\eta-1}{D}\,dg$
- $d(y-y_n)=\dfrac{\sigma^{-1}+\eta}{D}\,dg$
<!-- YW5zOjE= -->
> Use (23), $y-y_n=m_{\bar g}(g-\bar g)+m_{\bar\tau}(\tau-\bar\tau)-\dots$, with $m_{\bar g}=\eta/D$ and $m_{\bar\tau}=1/D$. Both terms push the same way, so $d(y-y_n)=(1+\eta)\,dg/D$. As a direct check, $dy_n=(\sigma^{-1}-1)dg/(\sigma^{-1}+\eta)$ and $dy=(dg+\sigma\kappa\,dy_n)/(1+\sigma\kappa)$, which give the same result. The tax lowers $y_n$ by more than it lowers $y$, so it *adds* to the gap that drives prices. Option A is the gap against **efficient** output, $m_{\bar g}-m_\tau$: taxes do not move $y_e$, so there the tax enters with its full output multiplier. At the calibration that gap is negative, while the price-relevant gap is positive. Option C flips the sign of the tax term. Option D is the pure demand push $dg/(1+\sigma\kappa)$, with both supply channels dropped.
> Ref: Benigno (2015), §8 (pp. 514–516), eqs. (22)–(23), Table 1; Map [[07-fiscal-multipliers]]
> Similar: [[benigno/07-fiscal-multipliers]] §7.5 and §7.7

Q: In Benigno's model with linear disutility of labour (inverse Frisch elasticity $\eta=0$) and lump-sum financing, the government raises spending $g$ temporarily while the nominal rate $i$ is held. What happens?
- Output rises by more than $dg$, because with labour supply perfectly elastic nothing crowds out private consumption and part of the extra income is spent again.
- Output rises by $dg$, but $p$ rises and the real rate climbs, so private consumption falls and the gap against natural output opens by the full $dg$.
- Output rises by exactly $dg$, consumption is unchanged, and $p$ and both output gaps stay put, so the central bank has nothing it needs to offset.
- Output is unchanged, because with $\eta=0$ the AS curve is flat and the wealth effect on labour supply exactly cancels the stimulus to demand.
<!-- YW5zOjI= -->
> With $\eta=0$, $\partial y_n/\partial g=\sigma^{-1}/\sigma^{-1}=1$. The negative wealth effect makes households work exactly enough extra to produce the new spending, so AS shifts right by $dg$. AD shifts right by the same $dg$. In Table 1, $m_g=1$ and $m_{\bar g}=\eta/D=0$, so output rises one-for-one, the gap against natural output (23) and against efficient output are both unchanged, and $p=p^e$ (footnote 10). Since $y=s_c c+g$ and $dy=dg$, consumption does not move. A multiplier of one, then, with no stabilisation value at all. Option A needs a consumption function the model does not have. Option B has the gap opening by $dg$, but gap-opening happens only when $\eta>0$, and then by $m_{\bar g}\,dg$. Option D is wrong because $\kappa=(1-\alpha)\sigma^{-1}/\alpha>0$ even at $\eta=0$.
> Ref: Benigno (2015), §4.2 (p. 508); §8 (pp. 515–516), fn. 10, Table 1; Map [[07-fiscal-multipliers]]
> Similar: [[benigno/03-natural-and-efficient]] §3.1

## zlb

Q: An economy sits at nominal rate $i=0$ with natural rate $r_n=0$ (gap closed) when a temporary mark-up shock hits; the bank minimises $\tfrac12(y-y_e)^2+\tfrac{\phi}{2\kappa}(p-p^e)^2$, with $\phi$ its weight on prices, $y_e$ efficient output, $\kappa$ the AS slope and $\sigma$ the AD parameter (slope $-1/\sigma$). When does the zero bound keep it from its optimum?
- Only when $\phi<\sigma$: such a bank wants $i$ below its no-policy level, which the floor forbids, while a bank with $\phi>\sigma$ wants a rise and is unconstrained.
- Only when $\phi>\sigma$: such a bank wants to cut $i$ to offset the fall in output, which the floor forbids, while a bank with $\phi<\sigma$ wants a rise and is unconstrained.
- For every $\phi$, since stagflation puts output below $y_e$, so every optimum involves some cut in $i$ to raise output, and the floor forbids any cut.
- For no $\phi$, since the shock raises $p$, and a higher $p$ lowers the real rate at $i=0$, so demand recovers by itself and $i$ never needs to move.
<!-- YW5zOjA= -->
> With no policy, a share $1/(1+\sigma\kappa)$ of the shock reaches prices. At the optimum the share is $1/(1+\phi\kappa)$. The bank raises $i$ iff it wants less into prices than doing nothing delivers, i.e. iff $\phi>\sigma$, and cuts iff $\phi<\sigma$. So the floor binds only for a dove. The welfare-based weight is $\phi=\theta\approx8\gg\sigma$, so a welfare-maximising bank is unaffected: its optimal move is a rise. Option B swaps the two mandates. Option C forgets that a cut also raises the price surprise, so a hawk prefers a rise despite the lower output. Option D has the sign of the real rate wrong: with $\bar p$ fixed, a higher $p$ lowers expected inflation $\bar p-p$ and *raises* the real rate.
> Ref: Benigno (2015), §9 (p. 517); §11 (p. 522), eq. (35), fn. 24; Map [[08-liquidity-trap]]; [[10-optimal-policy]]
> Similar: Lista 7, Q4; [[benigno/10-optimal-policy]] §10.5

Q: Starting from $i=r_n=\rho>0$, with natural real rate $r_n=\rho+\sigma^{-1}(\bar y_n-y_n)$, $\rho$ the time-preference rate, $\sigma$ the output-scaled intertemporal elasticity and $y_n,\bar y_n$ current and long-run natural output, which productivity decline can push the economy into a liquidity trap?
- Any of them, if large enough: lower productivity lowers natural output, depresses demand along with it, and so drives $r_n$ below zero in every case.
- A temporary fall in current productivity, if large enough, since $y_n$ falls today and a deep current slump is what leaves an economy stuck at the zero bound.
- A permanent fall in current and long-run productivity, if large enough, since $y_n$ and $\bar y_n$ both fall, so the drop in $r_n$ is twice the temporary one.
- Only an expected fall in long-run productivity, if $\sigma^{-1}d\bar y_n<-\rho$; a temporary current fall raises $r_n$, and a permanent one leaves $r_n$ unchanged.
<!-- YW5zOjM= -->
> A trap means $r_n<0$, so what matters is the sign of $dr_n=\sigma^{-1}(d\bar y_n-dy_n)$. A temporary current fall ($dy_n<0$, $d\bar y_n=0$) *raises* $r_n$: households expect to be richer later than now, want to borrow, and the real rate must rise to stop them, so the right response is a rate rise. A permanent fall moves both terms equally, so $dr_n=0$, as in the neutral permanent case. Only pessimism ($d\bar y_n<0$ alone) lowers $r_n$, and it pushes it below zero once $\sigma^{-1}d\bar y_n<-\rho$. This is Krugman's poor-growth-prospects origin, the optimism case run backwards. Option C adds the two shifts when they cancel. Option B confuses a low level of output with a low natural real rate.
> Ref: Benigno (2015), §6.1–§6.3 (pp. 511–513); §9 (p. 517), Fig. 12; Map [[08-liquidity-trap]]
> Similar: [[benigno/04-equilibrium-geometry]] §4.3; [[benigno/05-productivity-shocks]] §5.4

## delev

Q: In Benigno's deleveraging model savers are a share $\chi$, initial debt is $d_0$ (share of output), long-run inflation is tied to zero ($\bar p=p$) and the nominal rate is fixed, so AD reduces to $y=\text{const}+\frac{1-\chi}{\chi}[\hat d+d_0(p-p^e)]$, with $\hat d$ the change in the debt limit; AS is $p-p^e=\kappa(y-y_n)$ with $y_n$ fixed. In a stable equilibrium, what is $dy/d\hat d$?
- $\dfrac{dy}{d\hat d}=\dfrac{1-\chi}{\chi+(1-\chi)d_0\kappa}$
- $\dfrac{dy}{d\hat d}=\dfrac{1-\chi}{\chi-(1-\chi)d_0\kappa}$
- $\dfrac{dy}{d\hat d}=\dfrac{1-\chi}{1-(1-\chi)d_0\kappa}$
- $\dfrac{dy}{d\hat d}=\dfrac{\chi}{\chi-(1-\chi)d_0\kappa}$
<!-- YW5zOjE= -->
> Substitute $dp=\kappa\,dy$ into AD: $dy=\frac{1-\chi}{\chi}(d\hat d+d_0\kappa\,dy)$. Multiply by $\chi$ and collect the $dy$ terms: $[\chi-(1-\chi)d_0\kappa]\,dy=(1-\chi)\,d\hat d$. Stability (footnote 19) requires AD, slope $\chi/[(1-\chi)d_0]$, to be steeper than AS, slope $\kappa$, which makes the denominator positive. A deleveraging shock $d\hat d<0$ then lowers output by more than its direct effect $(1-\chi)d\hat d/\chi$. The response *grows* with $\kappa$: more price flexibility means a larger fall in prices, a heavier real debt burden and a deeper slump. That is the paradox of flexibility. Option A has the Fisher feedback with the wrong sign, which would make flexibility a cushion. Option C drops the division by $\chi$. Option D puts the savers' share in the numerator, but only borrowers respond to the limit.
> Ref: Benigno (2015), §10 (pp. 519–521), eqs. (31)–(32), Fig. 13, fn. 19; Map [[09-deleveraging]]
> Similar: [[benigno/09-deleveraging]] §9.4–§9.6

## opt

Q: A temporary mark-up rise $d\mu>0$ hits Benigno's AS-AD economy at $i=r_n$, $\bar p=p^e$; the bank enforces $(y-y_e)+\phi(p-p^e)=0$, with $\phi$ its price weight, $y_e$ efficient output, $\kappa$ the AS slope, $\sigma$ the AD parameter (slope $-1/\sigma$) and $\eta$ the inverse Frisch elasticity. By how much does it move the nominal rate $i$?
- $di=\dfrac{\kappa(\phi-\sigma)}{(1+\sigma\eta)(1+\sigma\kappa)}\,d\mu$
- $di=\dfrac{\kappa(\sigma-\phi)}{(1+\sigma\eta)(1+\phi\kappa)}\,d\mu$
- $di=\dfrac{\kappa(\phi-\sigma)}{(1+\sigma\eta)(1+\phi\kappa)}\,d\mu$
- $di=\dfrac{(\phi-\sigma)}{(\sigma^{-1}+\eta)(1+\phi\kappa)}\,d\mu$
<!-- YW5zOjI= -->
> Solving AS together with the targeting rule gives $dy=\phi\kappa\,dy_n/(1+\phi\kappa)$ and $dp=-\kappa\,dy_n/(1+\phi\kappa)$, where $dy_n=-d\mu/(\sigma^{-1}+\eta)$. Along AD with $\bar p$ fixed, $dy=-\sigma\,di-\sigma\,dp$, so $di=-(dy+\sigma\,dp)/\sigma=-\kappa(\phi-\sigma)dy_n/[\sigma(1+\phi\kappa)]$. Substituting $dy_n$ and using $\sigma(\sigma^{-1}+\eta)=1+\sigma\eta$ gives option C. The sign confirms the mandate result: a rise iff $\phi>\sigma$. At the article's calibration ($\phi=\theta=8$, $\kappa\approx1.13$, $\sigma=0.5$, $\eta=0.2$, $dy_n=-1$) it is about 1.69 points, less than the 2 points strict price stability would need. Option A puts the no-policy denominator $1+\sigma\kappa$ where the optimum's $1+\phi\kappa$ belongs. Option B flips the sign. Option D loses $\kappa$ and one factor of $\sigma$.
> Ref: Benigno (2015), §11 (pp. 521–523), eqs. (34)–(35), Fig. 14; Map [[10-optimal-policy]]
> Similar: Lista 7, Q4; [[benigno/10-optimal-policy]] §10.4

Q: Two central banks follow targeting rules $(y-y_e)+\phi(p-p^e)=0$ with different price weights $\phi$, one hawkish and one dovish, with $y_e$ efficient output and $\sigma$ the AD parameter (slope $-1/\sigma$); each faces optimism that raises expected long-run natural output $\bar y_n$ and nothing else. How do their optimal responses compare?
- Identically: both raise $i$ by $\sigma^{-1}d\bar y_n$ and return to $p=p^e$ and $y=y_e$, since neither AS nor the targeting line moves at all.
- The hawk raises $i$ by $\sigma^{-1}d\bar y_n$ to hold $p=p^e$, while the dove raises it by less, accepting some overheating to keep output nearer the higher $y_e$.
- The hawk raises $i$ to hold $p=p^e$, while the dove cuts $i$, since the shock separates natural from efficient output and the mandate sets the sign of the response.
- Neither moves $i$, since the shock raises $\bar y_n$ only and leaves $y_n$ and $y_e$ unchanged, so the targeting rule is already satisfied at the old rate.
<!-- YW5zOjA= -->
> Optimism moves AD up and nothing else: $y_n$ and $y_e$ are current-period objects and do not move. AS still passes through $(p^e,y_n)$ and every targeting line still passes through $(p^e,y_e)=(p^e,y_n)$, so all lines meet at the original point, where the loss is zero whatever $\phi$ is. Each bank raises $i$ by $d\bar y_n/\sigma$, which is exactly $dr_n$, and walks AD back. The weight $\phi$ only sets the slope of the targeting line around $(p^e,y_e)$, and that matters only when the shock pulls AS's anchor away from $y_e$, i.e. a mark-up shock. Option D forgets that AD has moved: holding $i$ leaves output and prices above target. Option B wrongly has $y_e$ rising. Option C carries the mark-up logic over to a shock that creates no trade-off.
> Ref: Benigno (2015), §6.3 (pp. 512–513); §11 (p. 522), eq. (34); Map [[10-optimal-policy]]
> Similar: [[benigno/10-optimal-policy]] §10.3; [[benigno/05-productivity-shocks]] §5.3
