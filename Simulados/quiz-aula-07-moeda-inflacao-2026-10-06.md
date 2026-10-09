---
quiz: "Macro I — Session 7: Money and Inflation (hard)"
tags:
  sup: "Money and its supply"
  dem: "Money demand"
  eq: "Equilibrium and neutrality"
  seig: "Seigniorage and the inflation tax"
  cost: "Costs of inflation"
---

## sup

Q: The public holds currency $C=cD$ and banks hold reserves $R=\theta D$, where $D$ is demand deposits, $c>0$ and $0<\theta<1$; the base is $B=C+R$ and $M_1=C+D$. If the currency ratio rises by $dc$, by what proportion $dB/B$ must the base change to keep $M_1$ constant?
- $\dfrac{dB}{B}=\dfrac{1-\theta}{(1+c)(c+\theta)}\,dc$, an expansion, because currency held by the public leaks out of the deposit chain.
- $\dfrac{dB}{B}=\dfrac{\theta-1}{(1+c)(c+\theta)}\,dc$, a contraction, because currency held by the public is itself a part of $M_1$.
- $\dfrac{dB}{B}=\dfrac{1-\theta}{(c+\theta)^{2}}\,dc$, an expansion, because currency held by the public leaks out of the deposit chain.
- $\dfrac{dB}{B}=\dfrac{1+c}{(c+\theta)^{2}}\,dc$, an expansion, because each unit of currency must be matched by new reserves.
<!-- YW5zOjA= -->
> Dividing the two identities by $D$ gives $M_1=\frac{1+c}{c+\theta}B$. In logs, $d\ln M_1=\big[\frac{1}{1+c}-\frac{1}{c+\theta}\big]dc+\frac{dB}{B}$, and the bracket is $\frac{(c+\theta)-(1+c)}{(1+c)(c+\theta)}=\frac{\theta-1}{(1+c)(c+\theta)}<0$. Setting $d\ln M_1=0$ gives A. A rise in $c$ lowers the multiplier when $\theta<1$, because a unit moved from deposits to currency stops being re-lent, so the base must expand. B has the sign flipped. C is $-\partial m/\partial c$, a change in the *level* of the multiplier, not the proportional change that offsets it. D confuses the multiplier's numerator with its derivative.
> Ref: Kurlat (2020), cap. 10, §10.2–10.3 (pp. 192–199); Map [[01-money-and-its-supply]]
> Similar: Kurlat, Exercício 10.2 (p. 202); Lista 6

Q: After 2008 the US monetary base grew several-fold while M1 grew far less, and banks were paid interest on reserves. What does the identity $M_1/B=(1+c)/(c+\theta)$, with $c$ the currency-deposit ratio and $\theta$ the reserve-deposit ratio, say about this episode?
- The identity failed in that episode, since it holds only while banks keep reserves at the legal minimum $\theta$, so a model of bank lending must replace it.
- The currency ratio $c$ must have jumped, since a rise in $c$ is the only way for the multiplier to fall while the base expands this much.
- The reserve ratio $\theta$ rose as banks chose to hold paid excess reserves, so the multiplier fell and $B$ stopped pinning down $M_1$.
- The multiplier stayed constant, and $M_1$ grew less only because the new base reached the public with a long lag through new bank loans.
<!-- YW5zOjI= -->
> The multiplier is an accounting identity given $c$ and $\theta$, so it cannot fail (A); what fails is reading it as a mechanism with $\theta$ held fixed. Once reserves earn interest, holding them is a choice, $\theta$ rises endogenously, and $\partial m/\partial\theta=-(1+c)/(c+\theta)^2<0$ makes the multiplier collapse, at times below one. A rise in $c$ would also lower $m$, but it is not the only route and it was not the main one (B). D contradicts the observed fall in $M_1/B$, which is the multiplier itself. This is why modern central banks set an interest rate and let the money stock be endogenous.
> Ref: Kurlat (2020), cap. 10, §10.3 (pp. 194–199); Map [[01-money-and-its-supply]]
> Similar: Kurlat, Exercício 10.3 (p. 202); Exercício 10.1 (p. 202)

## dem

Q: In the Baumol–Tobin model a household spends real income $Y$ evenly, bonds pay nominal rate $i$, each trip to the bank costs $F$, and real money demand is $\sqrt{FY/(2i)}$. If trips cost time, so $F=\phi Y$ with $\phi>0$ fixed, money grows at rate $\mu$, output at rate $g$, and $i$ is constant, what is steady-state inflation $\pi$?
- $\pi=\mu-\tfrac12 g$, since the income elasticity of money demand stays at $\tfrac12$ whatever the trip cost is.
- $\pi=\mu-g$, since a time cost of trips raises the income elasticity of money demand to exactly $1$.
- $\pi=\mu-2g$, since a time cost of trips raises the income elasticity of money demand to exactly $2$.
- $\pi=\mu-\tfrac32 g$, since the income elasticity is $\tfrac12$ through $Y$ plus a further $1$ through $F$.
<!-- YW5zOjE= -->
> Substituting $F=\phi Y$ gives $M/P=\sqrt{\phi Y^2/(2i)}=Y\sqrt{\phi/(2i)}$, so the income elasticity is $1$: the Cambridge form $M/P=kY$ comes back. Log-differentiating $M=P\cdot L(Y,i)$ at constant $i$ gives $\mu=\pi+\eta g$ with $\eta=1$, hence $\pi=\mu-g$. The economies of scale in cash management disappear because a richer household's time is worth proportionally more, so it makes no extra trips. A ignores that $F$ moves with $Y$. D adds the full $1$ for $F$, but money demand has elasticity $\tfrac12$ with respect to $F$, so $F=\phi Y$ adds only $\tfrac12$.
> Ref: Kurlat (2020), cap. 10, §10.4 (pp. 199–202); cap. 11, §11.2 (pp. 208–215); Map [[02-money-demand]]
> Similar: Kurlat, Exercício 11.1 (p. 218); Exercício 10.4 (p. 203); Lista 6

Q: In the Baumol–Tobin model velocity is $V=\sqrt{2iY/F}$, where $i$ is the nominal rate, $Y$ real income and $F$ the real cost of a trip to the bank. When is the quantity theory, $MV=PY$ with $V$ held constant, a poor guide to inflation?
- In fast-growing economies with stable inflation, since $V$ rises with $Y$ and $MV=PY$ stops holding as an identity once $V$ moves.
- In stable, low-inflation periods, since small movements in $i$ then dominate $V$, while large swings in $i$ cancel out over a cycle.
- Only when $F$ changes, since $i$ enters $V$ under a square root, so its movements are too damped to matter in practice.
- In hyperinflations and disinflations, since $i$ then moves a lot and $V$ moves with it, exactly when people most want the theory.
<!-- YW5zOjM= -->
> $MV=PY$ defines $V$, so it holds by construction (A is wrong on that count). It becomes a theory only by adding that $V$ is constant, and the model says $V$ rises with $i$. When inflation and hence $i=r+\pi$ swing widely, in hyperinflations and stabilisations, velocity swings too, and money growth stops mapping one-for-one into inflation. When $i$ is stable the constant-velocity approximation is good (B inverts this). A square root damps the response of $V$ but does not remove it: tripling $i$ raises $V$ by a factor of $\sqrt3$ (C).
> Ref: Kurlat (2020), cap. 10, §10.4 (pp. 199–202); cap. 11, §11.2 (pp. 208–215); Map [[02-money-demand]]
> Similar: Kurlat, Exercício 11.2 (p. 218); Lista 6

## eq

Q: Real money demand is $M/P=L\,e^{-a\pi}$, with $L>0$ fixed and $a>0$; prices are flexible and output is constant, so in steady state $\pi=\mu$, the money growth rate. A permanent rise in $\mu$ from $\mu_0$ to $\mu_1>\mu_0$ is announced and believed at once, with $M$ unchanged at that instant. What is $P_{\text{after}}/P_{\text{before}}$ at the announcement?
- $e^{a(\mu_1-\mu_0)}$, a discrete upward jump in the price level, after which $P$ grows at the new rate $\mu_1$.
- $e^{-a(\mu_1-\mu_0)}$, a discrete downward jump in the price level, after which $P$ grows at the new rate $\mu_1$.
- $(\mu_1/\mu_0)^{a}$, a discrete upward jump in the price level, after which $P$ grows at the new rate $\mu_1$.
- $1$, with no jump since $M$ has not moved at that instant; only the growth rate of $P$ changes to $\mu_1$.
<!-- YW5zOjA= -->
> At the instant of the announcement $M$ is fixed, and $P=M/(Le^{-a\pi})$, so $P_{\text{after}}/P_{\text{before}}=e^{-a\mu_0}/e^{-a\mu_1}=e^{a(\mu_1-\mu_0)}>1$. Higher expected inflation raises the cost of holding money, so desired real balances fall, and with $M$ fixed the only way to cut $M/P$ is a jump in $P$. D is the common mistake of changing only the slope of $\ln P$. B gets the direction of the jump wrong. C treats the semi-log form as a log-log form. With Baumol–Tobin demand, the same logic gives a jump of $\sqrt{i_1/i_0}$.
> Ref: Kurlat (2020), cap. 11, §11.2 (pp. 208–215); Map [[03-equilibrium-and-neutrality]]
> Similar: Kurlat, Exercício 11.4 (p. 219); Exercício 11.6 (p. 219)

Q: An economy has flexible prices and Baumol–Tobin money demand $M/P=\sqrt{FY/(2i)}$, where $F$ is the real cost per trip to the bank. Compare a permanent rise in the money growth rate with a one-off doubling of the money stock. Which statement is correct?
- Both are neutral: each changes only nominal variables, because the real rate $r$ and output are pinned down by real forces in either case.
- The doubling lowers the real rate $r$ by adding liquidity, while faster growth only raises inflation and leaves every real variable unchanged.
- The doubling is neutral, but faster growth raises $i$, lowers real balances and raises real resources spent on trips, so superneutrality fails.
- Faster growth is neutral, but the doubling raises real balances $M/P$ for good, so real money holdings rise and spending on trips falls.
<!-- YW5zOjI= -->
> A one-off doubling of $M$ doubles $P$ and leaves $M/P$, $r$ and $Y$ unchanged: money is neutral. A higher growth rate raises $\pi$ and therefore $i=r+\pi$, which lowers desired real balances and raises the number of trips $n^*=\sqrt{iY/(2F)}$. Each trip uses $F$ of real resources. So money is neutral in levels but not in growth rates. A misses that $r$ fixed does not mean $i$ is fixed. B and D reverse the roles: with flexible prices the level of $M$ cannot move $r$ or $M/P$.
> Ref: Kurlat (2020), cap. 11, §11.2 (pp. 208–215); §11.4 (pp. 217–218); Map [[03-equilibrium-and-neutrality]]
> Similar: Kurlat, Exercício 11.4 (p. 219); Lista 6

## seig

Q: Real money demand is $M/P=kYe^{-a\pi}$, with $k,a>0$; output $Y$ grows at rate $g$, money at rate $\mu$, and in steady state $\pi=\mu-g$. Seigniorage is $S=\dot M/P$. Which money growth rate $\mu^*$ maximises $S/Y$, and what is inflation $\pi^*$ there?
- $\mu^*=1/a$ and $\pi^*=1/a$, since the base erodes at rate $a$ per point whatever the growth rate of output.
- $\mu^*=1/a+g$ and $\pi^*=1/a$, since the peak of the inflation Laffer curve always sits at inflation $1/a$.
- $\mu^*=1/a-g$ and $\pi^*=1/a-2g$, since output growth lowers the money growth needed to collect revenue.
- $\mu^*=1/a$ and $\pi^*=1/a-g$, since growth raises the base without moving the peak in money growth.
<!-- YW5zOjM= -->
> $S=\frac{\dot M}{M}\cdot\frac{M}{P}=\mu kYe^{-a(\mu-g)}$, so $S/Y=ke^{ag}\,\mu e^{-a\mu}$. The factor $ke^{ag}$ does not depend on $\mu$, and $\frac{d}{d\mu}(\mu e^{-a\mu})=e^{-a\mu}(1-a\mu)=0$ gives $\mu^*=1/a$, so $\pi^*=1/a-g$. The tax is levied on money growth, not on inflation. Growth lets the government collect revenue $(\pi+g)M/P$ even at zero inflation, because the demand for real balances grows. B keeps the zero-growth result $\pi^{\max}=1/a$, but the rate being taxed is $\mu$, not $\pi$. A is inconsistent with $\pi=\mu-g$.
> Ref: Kurlat (2020), cap. 11, §11.3 (pp. 215–217); Map [[04-seigniorage-and-costs]]
> Similar: Kurlat, Exercício 11.6 (p. 219); Exercício 11.3 (p. 219)

Q: A credible stabilisation ends a high inflation: inflation drops at once to a low steady rate, and the public rebuilds its real money balances over the following months. What happens to the inflation tax $\pi M/P$ and to seigniorage $\dot M/P$ while balances are rebuilt?
- Both fall to low values together, since in every period seigniorage $\dot M/P$ and the inflation tax $\pi M/P$ are one and the same object.
- The inflation tax is low, but seigniorage $\dot M/P$ can stay high for a while, as new money meets the rising demand for real balances.
- Seigniorage $\dot M/P$ falls to zero, since any new money would reignite inflation, while the inflation tax rises as the base is rebuilt.
- Both rise above their pre-stabilisation values, since the economy has moved to the rising left side of the Laffer curve in $\pi$.
<!-- YW5zOjE= -->
> Differentiating $M/P$ gives $\dot M/P=\frac{d}{dt}(M/P)+\pi\,\frac{M}{P}$. Seigniorage equals the inflation tax only when real balances are constant, which is the steady state. While the public is remonetising, $\frac{d}{dt}(M/P)>0$, so the government can issue money that people willingly absorb without it raising prices. Inflation-tax revenue is low because $\pi$ is low (A merges the two concepts; D invents a rise). C is wrong because money issued to meet a rise in demand does not push up prices.
> Ref: Kurlat (2020), cap. 11, §11.3 (pp. 215–217); Map [[04-seigniorage-and-costs]]
> Similar: Kurlat, Exercício 11.3 (p. 219); Exercício 11.6 (p. 219)

## cost

Q: Inflation is steady, high and fully anticipated; every wage, loan, pension and tax rule is indexed to the price level, and posting new prices costs nothing, while currency still pays a zero nominal return. Which cost of inflation survives?
- Shoe-leather costs, since the nominal rate $i=r+\pi$ stays high and people spend real resources economising on currency that cannot be indexed.
- Redistribution from creditors to debtors, since debtors repay in currency whose real value has fallen, whatever indexing of $i$ is in place.
- None at all, since with full anticipation and indexing money is superneutral and the inflation rate $\pi$ is a pure change of units.
- Tax distortions, since nominal capital gains still rise with $\pi$ and are taxed in full even after every bracket has been indexed.
<!-- YW5zOjA= -->
> Indexing removes every cost that runs through nominal contracts, and anticipation removes the redistribution that needs a surprise (B). The stem rules out menu costs and indexes the tax rules (D). Currency, however, cannot be indexed: it pays zero, so the cost of holding it is $i=r+\pi$, which is high. People economise on balances and spend $Fn^*$ of real resources on trips to the bank. This is the failure of superneutrality, so C is wrong. Only the Friedman rule $i=0$ removes this cost.
> Ref: Kurlat (2020), cap. 11, §11.4 (pp. 217–218); Map [[04-seigniorage-and-costs]]
> Similar: Kurlat, Exercício 11.4 (p. 219); Exercício 10.4 (p. 203)

Q: The Friedman rule sets the nominal rate $i$ to zero, so with a real rate $r>0$ the Fisher equation gives steady inflation $\pi=-r$. Why does it target deflation rather than zero inflation, and what is the main modern objection?
- Deflation transfers wealth to money holders, who are poorer on average; the objection is that surprise deflation raises the real debt burden $r$.
- Zero inflation still leaves menu costs that only deflation at rate $r$ removes; the objection is that the CPI overstates true inflation $\pi$.
- At $\pi=0$ the cost of holding money is still $i=r>0$ although money is free to make; the objection is that $i=0$ leaves no room to cut rates.
- At $\pi=0$ seigniorage $\pi M/P$ is still positive and distorting; the objection is that deflation at $r$ needs a money stock shrinking forever.
<!-- YW5zOjI= -->
> The private cost of holding money is the nominal rate, while the social cost of creating it is zero. Efficiency equates the two, so $i=0$. At zero inflation $i=r>0$, and people still waste resources economising on cash. By Fisher, $i=0$ means $\pi=-r$ (exactly, $-r/(1+r)$). The modern objection is that a permanent $i=0$ puts the economy at the zero lower bound with no room to cut. Measurement bias and downward wage rigidity are further reasons why central banks target about 2%. B is wrong because menu costs rise with any nonzero inflation, deflation included. D is wrong because the inflation tax is zero at $\pi=0$. A rests on a redistribution story the rule does not use.
> Ref: Kurlat (2020), cap. 11, §11.4 (pp. 217–218); Map [[04-seigniorage-and-costs]]
> Similar: Kurlat, Exercício 11.5 (p. 219); Exercício 11.4 (p. 219)
