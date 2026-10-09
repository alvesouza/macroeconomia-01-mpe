---
quiz: "Macro I — Session 1: Measuring the Aggregates (hard)"
tags:
  cn: "National accounts"
  idx: "Real, nominal and price indices"
  ppp: "Cross-country comparisons and PPP"
  grow: "Growth arithmetic"
  bem: "Beyond GDP"
---

## cn

Q: A carmaker produces a car in year $t$ but sells it to a household in year $t+1$, at an unchanged price. How does each year's GDP record the car?
- Year $t$ records nothing because no transaction occurred; year $t+1$ records the full price as consumption, since GDP measures sales of final goods.
- Year $t$ records the price as inventory investment; year $t+1$ records consumption and an equal fall in inventories, so year-$t+1$ GDP is unchanged.
- Year $t$ records the price as inventory investment; year $t+1$ records it again as consumption, since a sale to a household is always final demand.
- Year $t$ records the price as intermediate consumption of the firm; year $t+1$ records consumption, so the car is counted once but in the year of sale.
<!-- YW5zOjE= -->
> GDP measures production in the period, not sales. The unsold car is produced in $t$, so it enters $I$ as a change in inventories. In $t+1$ the household's purchase adds to $C$, but inventories fall by the same amount, so $\Delta I$ is negative and year-$t+1$ GDP does not change. Option C counts the car twice. Option A dates the output by when it was sold. Option D treats a finished good as an input.
> Ref: Kurlat (2020), cap. 1, §1.1 (pp. 15–21); rules [[01_mensuracao_agregados]]
> Similar: Kurlat, Exercício 2.4 (p. 41); Lista 1, Q1

Q: Government services such as public schooling have no market price, so national accounts value their output at the cost of the inputs used. Which consequence follows?
- Measured government output overstates true output in every year, because wages of public employees include rents that a market price would strip out.
- Government value added is zero by construction, since output and input costs cancel, so public services enter GDP only through purchases from private firms.
- Measured productivity growth in the public sector tracks private-sector productivity growth, because public wages are benchmarked against private ones.
- Measured productivity growth in the public sector is about zero by construction, so any true efficiency gain there stays invisible in real GDP.
<!-- YW5zOjM= -->
> If output is valued at what the inputs cost, then real output is deflated input. Output per unit of input is fixed by the method, so a teacher who learns to teach twice as well shows up as no extra output. Value added is not zero: it equals the compensation of public employees plus the consumption of fixed capital, so B is wrong. Option A asserts a bias in one direction, and nothing in the method fixes its sign. Option C mixes up wages with output.
> Ref: Kurlat (2020), cap. 1, §1.1 (pp. 15–21); cap. 2, §2.1 (pp. 31–35)
> Similar: Kurlat, Exercício 2.3 (p. 41); Exercício 2.4 (p. 41)

## idx

Q: Real GDP is computed at the fixed prices of a base year $b$. One sector's relative price falls steadily while its quantity grows much faster than the rest of the economy. How does measured real growth in a recent year depend on how far back $b$ lies?
- The older the base year, the higher measured growth, because the booming sector is weighted at its old high price; rebasing revises recent growth down.
- The older the base year, the lower measured growth, because the booming sector is weighted at its old high price; rebasing revises recent growth up.
- Measured growth does not depend on the base year, because relative prices cancel when the same prices weigh both years of the growth rate.
- The older the base year, the higher measured growth, because accumulated inflation since $b$ inflates real output; rebasing removes that inflation.
<!-- YW5zOjA= -->
> At fixed base prices, each good's weight in measured growth is proportional to $p_{ib}q_{it}$. The further back $b$ lies, the higher the booming good's relative price, and so the larger its weight. Because that good is also the fastest-growing one, aggregate growth comes out higher. When the base is moved to a recent year, the good's weight drops to its current low price and recent growth is revised down. This is the computer-price episode, and it is why statistical offices chain-weight. Prices do not cancel (C), because they weight goods whose growth rates differ. Option D mixes up real and nominal: base prices are held fixed, so no inflation enters.
> Ref: Kurlat (2020), cap. 1, §1.2 (pp. 22–25); Map [[02-real-nominal-and-indices]]
> Similar: Kurlat, Exercício 1.3 (p. 28); Exercício 1.5 (p. 29)

Q: A country exports a commodity it does not consume. Its world price rises, while every quantity produced and every domestic consumer price stays unchanged. What happens?
- Real GDP at base-year prices rises with the export price, the GDP deflator is unchanged, and the CPI rises as exporters pass the gain to consumers.
- Real GDP at base-year prices is unchanged, the GDP deflator is unchanged, and the CPI rises because imports now cost more in units of the export good.
- Real GDP at base-year prices is unchanged, the GDP deflator rises, and the CPI is unchanged, though each unit exported now buys more imports.
- Real GDP at base-year prices is unchanged, the GDP deflator and the CPI both rise, and real income falls because the price level is now higher.
<!-- YW5zOjI= -->
> Real GDP holds prices at the base year, so with unchanged quantities it does not move. Nominal GDP rises with the export price. The deflator is nominal over real, and it covers everything produced at home, exports included, so it rises. The CPI prices only the consumption basket, and by assumption the commodity is not in it and no consumer price moved. The terms of trade have improved, so real *income* (command over imports) rises even though real *output* does not. Option D has the welfare effect the wrong way round.
> Ref: Kurlat (2020), cap. 1, §1.2 (pp. 22–27); rules [[01_mensuracao_agregados]]
> Similar: Kurlat, Exercício 1.5 (p. 29); Lista 1

Q: Suppose the CPI overstates true cost-of-living inflation by $b>0$ per year, through substitution, quality and new-goods bias. Nominal wages grow at rate $g_W$ and true inflation is $\pi$. What does deflating wages by the CPI report, and what follows?
- Measured real wage growth is $g_W - \pi + b$, so the bias makes real wages look better than they are and overstates welfare gains over time.
- Measured real wage growth is $g_W - \pi - b$, so a bias of a fraction of a point compounds into a large understatement of real-wage gains over decades.
- Measured real wage growth is $(g_W - \pi)(1-b)$, so the bias scales real gains down proportionally but can never change their sign.
- Measured real wage growth is $g_W - \pi - b$, but the error cancels over long horizons because substitution bias reverses once relative prices revert.
<!-- YW5zOjE= -->
> Measured inflation is $\pi+b$, and the growth rate of a ratio is approximately the difference of the growth rates, so measured real wage growth is $g_W-(\pi+b)$. The level error compounds, reaching a factor of about $e^{-bT}$ after $T$ years. Even a small $b$ therefore turns a modest rise in real wages into apparent stagnation. The bias does not reverse (D): substitution bias exists because a fixed-weight index ignores substitution, whichever way relative prices move.
> Ref: Kurlat (2020), cap. 1, §1.2 (pp. 22–25); Map [[03-growth-arithmetic]]
> Similar: Kurlat, Exercício 1.3 (p. 28); Lista 1

## ppp

Q: Two countries, $i$ and $US$, each produce a tradable and a non-tradable good using labour only: one worker makes $A_T$ units of tradables or $A_N$ units of non-tradables. Labour moves freely across sectors within a country but not across countries, and arbitrage equalises the tradable price across countries. The price level is $P = P_T^{1-\gamma}P_N^{\gamma}$, where $\gamma\in(0,1)$ is the expenditure share on non-tradables. What is $P^i/P^{US}$?
- $\left(\dfrac{A_T^i/A_N^i}{A_T^{US}/A_N^{US}}\right)^{1-\gamma}$, so the gap grows with the share of tradables in the basket.
- $\left(\dfrac{A_N^i/A_T^i}{A_N^{US}/A_T^{US}}\right)^{\gamma}$, so a relatively productive non-tradable sector means a high price level.
- $\left(\dfrac{A_T^i}{A_T^{US}}\right)^{\gamma}$, so only tradable productivity matters, since it alone pins down the wage.
- $\left(\dfrac{A_T^i/A_N^i}{A_T^{US}/A_N^{US}}\right)^{\gamma}$, so a large productivity edge in tradables means a high price level.
<!-- YW5zOjM= -->
> Within each country, mobile labour equalises the wage across sectors: $w = P_T A_T = P_N A_N$, which gives $P_N = P_T\,A_T/A_N$. Then $P = P_T^{1-\gamma}(P_T A_T/A_N)^{\gamma} = P_T\,(A_T/A_N)^{\gamma}$, and since $P_T$ is common across countries it cancels in the ratio. The tradable sector sets the wage, the wage sets the price of non-tradables, and so a country with a large edge in tradables has expensive services. This is Balassa–Samuelson, and it is why market exchange rates understate poor countries' real income. Option C would be right only if $A_N$ were equal across countries.
> Ref: Kurlat (2020), cap. 1, §1.2 (pp. 25–27); Map [[04-cross-country-and-ppp]]
> Similar: Kurlat, Exercício 1.5 (p. 29); Lista 1

## grow

Q: Output per person grows by a fraction $x\in(0,1)$ in odd years and falls by the same fraction $x$ in even years. Starting from $Y_0$, what is output after $2T$ years, and how does that compare with the average annual growth rate?
- $Y_0(1-x^2)^T$, below $Y_0$, although the arithmetic average of the annual growth rates is exactly zero.
- $Y_0$, unchanged, because rises and falls of equal size cancel, consistent with an average growth rate of zero.
- $Y_0(1-x)^{2T}$, below $Y_0$, because each fall applies to a larger base than the rise that preceded it.
- $Y_0(1+x^2)^T$, above $Y_0$, because compounding magnifies the gains so that rises outweigh equal falls.
<!-- YW5zOjA= -->
> Each pair of years multiplies output by $(1+x)(1-x)=1-x^2<1$, so after $T$ pairs output is $Y_0(1-x^2)^T$. The arithmetic mean of the rates is $0$, but the geometric mean is $(1-x^2)^{1/2}-1<0$, and the geometric mean is what governs levels (AM ≥ GM). This is why average growth is measured by the CAGR and not by averaging annual rates. Option C applies the fall twice per pair.
> Ref: Kurlat (2020), cap. 1 (growth arithmetic, used throughout); Map [[03-growth-arithmetic]]
> Similar: Kurlat, Exercício 3.1 (p. 51); Lista 1

## bem

Q: Let $HDI=(I\cdot E\cdot H)^{1/3}$, with income index $I=\frac{\ln y-\ln y_{min}}{\ln y_{max}-\ln y_{min}}$, health index $H=\frac{LE-LE_{min}}{LE_{max}-LE_{min}}$, education index $E$, income per capita $y$ and life expectancy $LE$. Holding HDI and $E$ fixed, how much income $dy$ is worth one extra year of life expectancy?
- $\dfrac{dy}{dLE}=\dfrac{y}{LE-LE_{min}}$, so the implicit value of a life-year rises in proportion to income.
- $\dfrac{dy}{dLE}=\dfrac{\ln y-\ln y_{min}}{y\,(LE-LE_{min})}$, so the implicit value of a life-year falls with income.
- $\dfrac{dy}{dLE}=\dfrac{y\,(\ln y-\ln y_{min})}{LE-LE_{min}}$, so a life-year's implicit value rises faster than income.
- $\dfrac{dy}{dLE}=\dfrac{y\,(LE-LE_{min})}{\ln y-\ln y_{min}}$, so the implicit value of a life-year rises with income.
<!-- YW5zOjI= -->
> $\ln HDI=\tfrac13(\ln I+\ln E+\ln H)$. Then $\partial\ln HDI/\partial LE = \frac{1}{3H(LE_{max}-LE_{min})} = \frac{1}{3(LE-LE_{min})}$ and $\partial \ln HDI/\partial y = \frac{1}{3I\,y(\ln y_{max}-\ln y_{min})}=\frac{1}{3y(\ln y-\ln y_{min})}$. Their ratio is the marginal rate of substitution in C. Because the income term carries both $y$ and $\ln y$, the HDI implicitly values a year of life in a rich country at many times its value in a poor one. That is a known critique of the index's arbitrary functional form. Option D inverts the ratio.
> Ref: Kurlat (2020), cap. 2, §2.1 (pp. 31–35); Map [[05-beyond-gdp]]
> Similar: Kurlat, Exercício 2.1 (p. 40); Exercício 2.5 (p. 41)

Q: In the Jones–Klenow welfare measure, flow utility is CRRA with coefficient of relative risk aversion $\sigma$, and consumption within a country is log-normal with log-variance $v$. Countries $i$ and $US$ share mean consumption and every other welfare component, with log-variances $v_i$ and $v_{US}$. What is the inequality term in $\ln\lambda$, where $\lambda$ scales US consumption to match welfare in country $i$?
- $-\tfrac{\sigma}{2}(v_i-v_{US})$, so more risk aversion makes the same dispersion gap cost more.
- $-\tfrac{1}{2\sigma}(v_i-v_{US})$, so more risk aversion makes the same dispersion gap cost less.
- $-\tfrac{1}{2}(v_i-v_{US})$, so risk aversion has no effect on what the dispersion gap costs.
- $-\sigma\,(v_i-v_{US})$, so more risk aversion makes the same dispersion gap cost more.
<!-- YW5zOjA= -->
> If $\ln c\sim N(\mu,v)$, then $E[c^{1-\sigma}]=e^{(1-\sigma)\mu+(1-\sigma)^2v/2}$, so the certainty-equivalent consumption satisfies $\ln c^{CE}=\mu+(1-\sigma)v/2$. Mean consumption satisfies $\ln E[c]=\mu+v/2$, so $\ln c^{CE}-\ln E[c]=-\sigma v/2$. Taking the difference between the two countries gives A. With log utility ($\sigma=1$) the penalty is exactly half the log variance. Option C is that special case wrongly generalised, and D drops the $1/2$ from the log-normal moment.
> Ref: Kurlat (2020), cap. 2, §2.2 (pp. 35–40); Map [[05-beyond-gdp]]
> Similar: Kurlat, Exercício 2.8 (p. 42); Exercício 2.10 (p. 43)

Q: France has GDP per capita well below the US level, yet its Jones–Klenow welfare measure $\lambda$ comes much closer to the US. Which combination of components closes most of that gap?
- A higher consumption share of GDP and a more favourable PPP correction, which together raise French consumption per person above the US level.
- Longer life expectancy, more leisure and lower consumption inequality, which together offset most of the lower consumption per person.
- Higher measured investment and a larger public sector, which raise future consumption and are counted by the measure as present welfare.
- Longer working hours and lower consumption inequality, which together offset most of the lower consumption per person in France.
<!-- YW5zOjE= -->
> $\ln\lambda$ splits additively into life expectancy, consumption, leisure and inequality. France loses on consumption, but it gains on all three of the others: people live longer, work fewer hours, and consumption is less dispersed. Option D gets the hours wrong, since longer work *lowers* welfare. Option C counts investment, which the measure leaves out because only consumption and leisure enter utility. French consumption per person is below the US level, so A is false.
> Ref: Kurlat (2020), cap. 2, §2.2 (pp. 35–40); Map [[05-beyond-gdp]]
> Similar: Kurlat, Exercício 2.9 (p. 43); Exercício 2.1 (p. 40)
