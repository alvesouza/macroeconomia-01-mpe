---
quiz: "Macro I — Session 3: Golden Rule, Technology and TFP (hard)"
tags:
  ouro: "Golden Rule"
  fatores: "Factor markets"
  tec: "Technical progress"
  conv: "Convergence"
  ptf: "Growth accounting and TFP"
---

## ouro

Q: In the Solow model with labour-augmenting progress at rate $g$, population growth $n$, depreciation $\delta$ and competitive factor markets, the net return on capital is $r=f'(\tilde k)-\delta$, where $\tilde k=K/(AL)$. What does $r$ equal at the Golden Rule, and what signals dynamic inefficiency?
- $r=n$ at the Golden Rule; the economy over-accumulates when $r<n$, since extra capital then no longer pays for equipping new workers.
- $r=n+g+\delta$ at the Golden Rule; the economy over-accumulates when $r<n+g+\delta$, since capital then fails to cover its own replacement.
- $r=g$ at the Golden Rule; the economy over-accumulates when $r<g$, since capital then earns less than the growth rate of output per worker.
- $r=n+g$ at the Golden Rule; the economy over-accumulates when $r<n+g$, since capital then earns less than the growth rate of aggregate output.
<!-- YW5zOjM= -->
> Maximising $c=f(\tilde k)-(n+g+\delta)\tilde k$ gives $f'(\tilde k_{gold})=n+g+\delta$, so $r=f'-\delta=n+g$. That is the growth rate of aggregate output on the balanced growth path. If $r<n+g$, capital is beyond the Golden Rule, and cutting saving raises consumption at every date. Option B forgets to net out depreciation. Options A and C each drop one component of aggregate growth.
> Ref: Kurlat (2020), §4.3 (pp. 61–63); §4.5 (pp. 69–72); Map [[01-golden-rule]]
> Similar: Kurlat, Exercício 5.6 (p. 96); Exercício 5.8 (p. 97)

Q: Using national accounts, an economist compares gross capital income $r^K K$ with gross investment $I$ in an economy on a balanced growth path, with Cobb-Douglas technology, capital share $\alpha$ and saving rate $s$. Which reading is correct?
- If capital income falls short of investment, the economy saves less than the Golden Rule rate; capital yields more than it absorbs, so more saving is a free lunch.
- If capital income exceeds investment, the economy saves less than the Golden Rule rate; capital yields more than it absorbs, so the economy is dynamically efficient.
- If capital income exceeds investment, the economy saves more than the Golden Rule rate; capital absorbs more than it yields, so the economy is dynamically inefficient.
- If capital income equals investment, the economy is dynamically inefficient, since every unit of capital income is reinvested and none of it is ever consumed.
<!-- YW5zOjE= -->
> With Cobb-Douglas, $r^KK=\alpha Y$ and $I=sY$, so $r^KK>I$ holds exactly when $s<\alpha=s_{gold}$. Capital then pays out more each year than it takes in as new investment, so the economy is below the Golden Rule and dynamically efficient. Raising saving there is *not* a free lunch (A), because it costs consumption today. Equality (D) is precisely the Golden Rule, not an inefficiency. This is the Abel et al. test, which rich economies pass.
> Ref: Kurlat (2020), §4.3 (pp. 61–63); §4.4 (pp. 63–69); cap. 1, §1.1
> Similar: Kurlat, Exercício 5.8 (p. 97); Exercício 5.7 (p. 96)

## fatores

Q: In the decentralised Solow economy, firms with technology $F(K,AL)$ rent capital at $r^K$ and hire labour at $w$ in competitive markets. Why do factor payments exactly exhaust output, and what would change under increasing returns?
- Constant returns make $F$ homogeneous of degree one, so marginal-product payments use up output exactly; under increasing returns they would exceed output and firms would lose money.
- Constant returns make $F$ homogeneous of degree one, so marginal-product payments leave a positive residual profit; under increasing returns that residual would vanish.
- Competition forces zero profit whatever the returns to scale, so payments exhaust output in any case; under increasing returns only the split between factors would change.
- Free entry drives profit to zero whatever the returns to scale, so payments exhaust output in any case; under increasing returns the wage would equal labour's average product.
<!-- YW5zOjA= -->
> Euler's theorem gives $F=F_KK+F_L\,AL$ for $F$ homogeneous of degree one, so $r^KK+wL=Y$ and profit is zero. With increasing returns, $F_KK+F_LAL>F$: paying marginal products would cost more than the output produced, and perfect competition cannot be sustained. Zero profit is a consequence of CRS together with marginal-product pricing. Competition does not deliver it on its own (C, D).
> Ref: Kurlat (2020), §4.4 (pp. 63–69); Map [[02-markets-and-factor-prices]]
> Similar: Kurlat, Exercício 5.6 (p. 96); Exercício 5.7 (p. 96)

Q: Countries $i$ and $US$ share the technology $y=Ak^{\alpha}$, with the same $A$ and competitive factor markets, so the rental rate is $r^K=f'(k)$. Country $i$ has output per worker $y_i$ below the US level $y_{US}$. What does the model predict for $r^K_i/r^K_{US}$?
- $\left(\dfrac{y_{US}}{y_i}\right)^{\alpha/(1-\alpha)}$, which with a capital share near one third is about the square root of the income gap.
- $\left(\dfrac{y_{US}}{y_i}\right)^{1-\alpha}$, which with a capital share near one third is about the income gap to the power two thirds.
- $\left(\dfrac{y_{US}}{y_i}\right)^{(1-\alpha)/\alpha}$, which with a capital share near one third is about the square of the income gap.
- $\left(\dfrac{y_{US}}{y_i}\right)^{1/\alpha}$, which with a capital share near one third is about the cube of the income gap.
<!-- YW5zOjI= -->
> $r^K=\alpha Ak^{\alpha-1}$ and $k=(y/A)^{1/\alpha}$, so $r^K=\alpha A^{1/\alpha}y^{-(1-\alpha)/\alpha}$. With common $A$ the ratio is $(y_{US}/y_i)^{(1-\alpha)/\alpha}$. With $\alpha\approx1/3$, a country ten times poorer would offer about a hundred times the return. Capital does not flow in anything like the volume such returns would attract, which is the Lucas paradox, so the premise of equal $A$ must be wrong. Option A is the elasticity of $y_{ss}$ to $s$, which is a different exponent.
> Ref: Kurlat (2020), cap. 5, §5.2 (pp. 80–83); Map [[04-quantifying-and-convergence]]
> Similar: Kurlat, Exercício 5.1 (p. 93); Exercício 5.6 (p. 96)

## tec

Q: An economy is on the balanced growth path of $Y=K^{\alpha}(AL)^{1-\alpha}$, with labour-augmenting progress at rate $g$. An analyst runs per-worker growth accounting $g_y=g_Z+\alpha\,g_k$, where $Z$ is Hicks-neutral TFP. What does the analyst report?
- TFP growth $g$ and capital deepening zero, since on a balanced growth path capital per worker is constant and all growth is technology.
- TFP growth $(1-\alpha)g$ and capital deepening $\alpha g$, although the capital deepening is itself induced by technical progress.
- TFP growth $\alpha g$ and capital deepening $(1-\alpha)g$, since capital earns a share $\alpha$ and labour-augmenting progress acts through labour.
- TFP growth $(1-\alpha)g$ and capital deepening $\alpha g$, so a fraction $\alpha$ of long-run growth would survive if technical progress stopped.
<!-- YW5zOjE= -->
> Rewriting $Y=K^{\alpha}(AL)^{1-\alpha}$ as $Z K^{\alpha}L^{1-\alpha}$ gives $Z=A^{1-\alpha}$, so $g_Z=(1-\alpha)g$. On the balanced growth path $g_k=g_y=g$, so capital deepening contributes $\alpha g$. That capital is accumulated only *because* $A$ grows: if progress stopped, $k$ would stop growing and all growth would end. Option D reads the accounting as causal. Option A forgets that $k=K/L$ grows at $g$, since only $\tilde k$ is constant.
> Ref: Kurlat (2020), §4.5 (pp. 69–72); cap. 5, §5.4 (pp. 86–90); Map [[03-technological-progress]]
> Similar: Kurlat, Exercício 5.7 (p. 96); Lista 2

Q: In the Solow model with $\tilde y=\tilde k^{\alpha}$, saving rate $s$, population growth $n$ and depreciation $\delta$, the rate of labour-augmenting progress rises permanently from $g$ to $g'>g$. What happens to $\tilde k_{ss}$ and to output per worker?
- $\tilde k_{ss}$ is unchanged because it depends only on $s$, $n$ and $\delta$; output per worker grows at $g'$ from the moment the change occurs.
- $\tilde k_{ss}$ rises because faster progress raises the return on capital; output per worker grows at $g'$ and its level also jumps up on impact.
- $\tilde k_{ss}$ falls because more investment is needed to keep pace with $A$; output per worker still grows at $g$ in the long run, a pure level effect.
- $\tilde k_{ss}$ falls because more investment is needed to keep pace with $A$; output per worker grows at $g'$ in the long run, on a path lower relative to $A$.
<!-- YW5zOjM= -->
> $\tilde k_{ss}=(s/(n+g'+\delta))^{1/(1-\alpha)}$ falls, because the effective replacement rate now includes the faster growth of $A$. Since $y=A\tilde y$, output per worker grows at $g'$ in the long run, but $\tilde y$ settles at a lower level. Unlike a change in $s$, a change in $g$ has a *rate* effect, which is why $g$ is the only lever on long-run growth in this model. Option C treats $g$ like $s$.
> Ref: Kurlat (2020), §4.5 (pp. 69–72); Map [[03-technological-progress]]
> Similar: Kurlat, Exercício 4.4 (p. 73); Lista 2

## conv

Q: In the Solow model with $\tilde y=\tilde k^{\alpha}$, saving rate $s$, population growth $n$, labour-augmenting progress $g$ and depreciation $\delta$, the law of motion is $\dot{\tilde k}=s\tilde k^{\alpha}-(n+g+\delta)\tilde k$. Linearising around the steady state, at what rate $\lambda$ does the gap $\ln\tilde k-\ln\tilde k_{ss}$ close?
- $\lambda=(1-\alpha)(n+g+\delta)$, so a larger capital share slows convergence because diminishing returns set in more gently.
- $\lambda=\alpha\,(n+g+\delta)$, so a larger capital share speeds convergence because capital accumulates out of a larger share of income.
- $\lambda=(1-\alpha)\,s$, so a higher saving rate speeds convergence because more output is diverted to accumulation every period.
- $\lambda=\dfrac{n+g+\delta}{1-\alpha}$, so a larger capital share speeds convergence because the steady state lies further from the start.
<!-- YW5zOjA= -->
> Write $d\ln\tilde k/dt=s\tilde k^{\alpha-1}-(n+g+\delta)$. Its derivative with respect to $\ln\tilde k$ is $-(1-\alpha)s\tilde k^{\alpha-1}$, and at the steady state $s\tilde k_{ss}^{\alpha-1}=n+g+\delta$, so $\lambda=(1-\alpha)(n+g+\delta)$. The saving rate drops out (C) because it is already absorbed into $\tilde k_{ss}$. As $\alpha\to1$, returns stop diminishing and convergence stops.
> Ref: Kurlat (2020), cap. 5, §5.3 (pp. 83–86); Map [[04-quantifying-and-convergence]]
> Similar: Kurlat, Exercício 5.2 (p. 94); Lista 2

Q: Cross-country studies of conditional convergence find that economies close roughly 2% of the gap to their own steady state per year. In the Solow model that rate is $(1-\alpha)(n+g+\delta)$, with $\alpha$ the capital share and $n+g+\delta$ around 6–7% a year. How does the model square with the estimate?
- It already matches: with a capital share near one third the formula gives about 2%, so the narrow-capital model fits the data without modification.
- It predicts convergence that is too slow: matching 2% needs a capital share near zero, so capital must matter much less than income shares suggest.
- It predicts convergence that is too fast: matching 2% needs an effective capital share of two thirds or more, as when human capital is counted as capital.
- It predicts convergence that is too fast: matching 2% needs depreciation near zero, so measured depreciation rates must greatly overstate the true ones.
<!-- YW5zOjI= -->
> With $\alpha\approx1/3$, $\lambda\approx\tfrac23\times6.5\%\approx4\%$ a year, about twice the estimate. Getting $\lambda=2\%$ requires $1-\alpha\approx0.3$, that is, a *broad* capital share near $0.7$. That is what you get when human capital accumulates alongside physical capital (Mankiw–Romer–Weil). Even setting $\delta=0$ (D) leaves $\lambda\approx\tfrac23(n+g)$, which misses because $n$ and $g$ are not zero either. The numbers are the empirical magnitudes quoted by the course, not values to be derived.
> Ref: Kurlat (2020), cap. 5, §5.3 (pp. 83–86); §5.5 (pp. 90–95)
> Similar: Kurlat, Exercício 5.2 (p. 94); Lista 2

## ptf

Q: Two economies have identical aggregate capital, identical labour and identical firm-level technologies. In the first, capital is allocated so that its marginal product is equal across firms; in the second, policy distortions leave marginal products unequal. What does aggregate accounting with $Y=Z K^{\alpha}L^{1-\alpha}$ report?
- Equal TFP in both, because $Z$ is a property of firm technologies and those are identical by assumption; the distortion appears as a lower measured capital share.
- Equal TFP in both, because aggregate inputs are identical and accounting attributes output gaps only to differences in measured inputs, never to the residual.
- Higher TFP in the second, because unequal marginal products mean that some firms earn rents, which national accounts record as extra value added.
- Lower TFP in the second, because the same inputs produce less output; the residual picks up misallocation even though no firm's technology differs.
<!-- YW5zOjM= -->
> Equalising marginal products maximises output for given totals, so the distorted economy produces less from the same $K$ and $L$. Since $Z=Y/(K^{\alpha}L^{1-\alpha})$ is computed as a residual, it is lower there. Measured TFP is therefore not "technology": it absorbs misallocation, institutions, input quality and measurement error. Option B gets the method backwards, since the residual is exactly where unexplained output gaps land.
> Ref: Kurlat (2020), cap. 5, §5.4–§5.5 (pp. 86–95); Map [[05-growth-accounting-and-tfp]]
> Similar: Kurlat, Exercício 5.5 (p. 95); Exercício 5.9 (p. 98)

Q: Development accounting writes $y=A\,k^{\alpha}h^{1-\alpha}$, with human capital per worker $h=e^{\phi S}$, years of schooling $S$ and Mincerian return $\phi$. Compared with an accounting that omits $h$, what happens when schooling is added?
- The share of income gaps attributed to TFP rises, because schooling is higher in poor countries than their income suggests, so $h$ widens the unexplained gap.
- The share attributed to TFP falls, because rich countries have more schooling, but TFP still accounts for the largest part of the gaps between rich and poor countries.
- The share attributed to TFP falls to near zero, because schooling differences are large enough that physical and human capital together explain nearly all of the gaps.
- The share attributed to TFP is unchanged, because $h$ enters with exponent $1-\alpha$ and so only rescales labour, which the accounting already measures per worker.
<!-- YW5zOjE= -->
> Schooling is higher in rich countries, so $h_i/h_{US}<1$, and part of the income ratio that was previously left in $A$ is now explained by $h$. Mincerian returns of about 10% a year per year of schooling are not large enough to close the gap, though, and the robust finding is that TFP remains the largest single factor. Option D misses that $h$ varies across countries, while measuring per worker only removes $L$.
> Ref: Kurlat (2020), cap. 5, §5.4–§5.5 (pp. 86–95); Map [[05-growth-accounting-and-tfp]]
> Similar: Kurlat, Exercício 5.1 (p. 93); Exercício 5.9 (p. 98)
