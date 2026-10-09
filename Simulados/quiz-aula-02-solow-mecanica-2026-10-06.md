---
quiz: "Macro I — Session 2: Growth Facts and Solow Mechanics (hard)"
tags:
  fatos: "Growth facts"
  solow: "Solow mechanics"
---

## fatos

Q: In a competitive economy with $Y=K^{\alpha}(AL)^{1-\alpha}$, depreciation $\delta$ and net return on capital $r$, which pair of Kaldor facts is enough to make $r$ constant?
- A constant growth rate of capital per worker together with a constant labour share, since $r$ equals the growth rate of capital per worker plus depreciation.
- A constant labour share together with a constant growth rate of output per worker, since $r$ is the residual left after labour is paid its share.
- A constant capital share together with a constant capital–output ratio, since the rental rate equals $lpha$ over the capital–output ratio.
- A constant capital–output ratio together with a constant growth rate of output per worker, since $r$ equals that growth rate plus depreciation.
<!-- YW5zOjI= -->
> With competitive markets, $r^K=\partial Y/\partial K=\alpha Y/K$, so $r=\alpha/(K/Y)-\delta$. Once the capital share and $K/Y$ are constant, $r$ is constant too. The fact about the return on capital therefore adds no information beyond the facts about shares and $K/Y$. None of the other options gives the correct formula for the return.
> Ref: Kurlat (2020), cap. 3 (pp. 47–51); §4.4 (pp. 63–69); Map [[01-growth-facts]]
> Similar: Kurlat, Exercício 3.2 (p. 52); Exercício 5.6 (p. 96)

Q: The Kaldor facts include constant factor shares. Does matching that fact require a Cobb-Douglas production function?
- Not on a balanced growth path: with labour-augmenting progress $K/(AL)$ is constant, so every CRS function yields constant shares; Cobb-Douglas matters only off that path.
- Yes in all cases: only Cobb-Douglas has a unit elasticity of substitution, and any other CRS function makes shares drift while capital per worker keeps rising along the path.
- Not on a balanced growth path: with capital-augmenting progress $AK/L$ is constant, so any CRS function gives constant shares; Cobb-Douglas is needed only for constant shares off that path.
- Yes in all cases: constant shares require that the capital share equal the saving rate, a restriction that holds only when output is Cobb-Douglas with exponent $s$.
<!-- YW5zOjA= -->
> With CRS, the capital share $\frac{\tilde k f'(\tilde k)}{f(\tilde k)}$ depends only on $\tilde k=K/(AL)$, and that ratio is constant on a balanced growth path. Shares are therefore constant for *any* CRS technology. What drifts with non-unit substitution elasticity is $K/L$, but shares do not depend on it. Option C picks the wrong form of progress: capital-augmenting progress cannot sustain a balanced growth path except under Cobb-Douglas (Uzawa). Cobb-Douglas earns its keep elsewhere, because it keeps shares constant across countries and along transitions, which is exactly where the data also show stable shares.
> Ref: Kurlat (2020), cap. 3 (pp. 47–51); §4.5 (pp. 69–72); Map [[01-growth-facts]]
> Similar: Kurlat, Exercício 3.2 (p. 52); Lista 1

Q: US income per capita in the late nineteenth century was close to that of many of today's poor countries, and it has grown at a roughly constant rate since. What does this pattern imply for reading today's cross-country income gaps?
- Today's poor countries must be on a lower long-run growth path, since no country reaches rich levels without first matching the nineteenth-century US saving rate.
- Cross-country gaps are mainly measurement error from PPP conversion, since a steady growth rate cannot on its own produce gaps of thirty or fifty to one.
- Today's gaps must narrow on their own within a generation, because diminishing returns guarantee that poor countries grow faster than the US once did.
- Modest growth-rate differences sustained over a century or more are enough to open today's gaps, so the question is why growth started at different times and rates.
<!-- YW5zOjM= -->
> At about 2% a year for 150 years, income grows by a factor of roughly $e^{3}\approx 20$, which is the order of today's rich–poor ratios. The gaps are what you get when growth starts at different dates and runs at different rates. That is why the course asks what determines growth, and does not stop at what determines levels at a point in time. Option C assumes absolute convergence, which the world sample rejects. Option B dismisses gaps that survive PPP correction.
> Ref: Kurlat (2020), cap. 3 (pp. 47–51); Map [[01-growth-facts]]
> Similar: Kurlat, Exercício 3.1 (p. 51); Lista 1

## solow

Q: In the Solow model with a general CRS per-worker production function $f(k)$, saving rate $s$, population growth $n$ and depreciation $\delta$, let $\varepsilon \equiv k f'(k)/f(k)$ be the elasticity of output to capital at the steady state $k_{ss}$. What is $d\ln k_{ss}/d\ln s$?
- $\dfrac{\varepsilon}{1-\varepsilon}$, which reduces to $\alpha/(1-\alpha)$ when the technology is Cobb-Douglas $k^{\alpha}$.
- $\dfrac{1}{1-\varepsilon}$, which reduces to $1/(1-\alpha)$ when the technology is Cobb-Douglas $k^{\alpha}$.
- $1-\varepsilon$, which reduces to $1-\alpha$ when the technology is Cobb-Douglas $k^{\alpha}$.
- $\dfrac{1}{\varepsilon}$, which reduces to $1/\alpha$ when the technology is Cobb-Douglas $k^{\alpha}$.
<!-- YW5zOjE= -->
> The steady state solves $s f(k_{ss})=(n+\delta)k_{ss}$. Taking logs and differentiating gives $d\ln s+\varepsilon\,d\ln k_{ss}=d\ln k_{ss}$, so $d\ln k_{ss}/d\ln s=1/(1-\varepsilon)$. Option A is the elasticity of $y_{ss}$, obtained by multiplying by $\varepsilon$, so it answers a different question. The closer $\varepsilon$ is to one, the weaker diminishing returns are and the more capital responds to saving.
> Ref: Kurlat (2020), §4.2 (pp. 57–61); Map [[05-comparative-statics]]
> Similar: Kurlat, Exercício 4.1 (p. 72); Exercício 5.1 (p. 93)

Q: In the Solow model with $y=k^{\alpha}$, saving rate $s$, population growth $n$ and depreciation $\delta$, steady-state consumption per worker is $c_{ss}=(1-s)y_{ss}$. What is $d\ln c_{ss}/d\ln s$, and when is it positive?
- $\dfrac{\alpha}{1-\alpha}+\dfrac{s}{1-s}$, positive for every $s$, so higher saving always raises steady-state consumption per worker.
- $\dfrac{1}{1-\alpha}-\dfrac{s}{1-s}$, positive whenever $s<1/(2-\alpha)$, so the consumption-maximising rate exceeds the capital share.
- $\dfrac{\alpha}{1-\alpha}-\dfrac{s}{1-s}$, positive whenever $s<\alpha$, so the consumption-maximising saving rate is the capital share.
- $\dfrac{\alpha}{1-\alpha}-s$, positive whenever $s<\alpha/(1-\alpha)$, so the consumption-maximising rate exceeds the capital share.
<!-- YW5zOjI= -->
> $y_{ss}=(s/(n+\delta))^{\alpha/(1-\alpha)}$, so $\ln c_{ss}=\ln(1-s)+\frac{\alpha}{1-\alpha}\ln s+\text{const}$. Differentiating with respect to $\ln s$ gives $\frac{\alpha}{1-\alpha}-\frac{s}{1-s}$. The function $x/(1-x)$ is increasing, so the expression is positive exactly when $s<\alpha$, which is the Golden Rule $s_{gold}=\alpha$ reached from comparative statics alone. Option B uses the elasticity of $k_{ss}$ where the elasticity of $y_{ss}$ belongs. Option D differentiates $\ln(1-s)$ incorrectly.
> Ref: Kurlat (2020), §4.2 (pp. 57–61); §4.3 (pp. 61–63)
> Similar: Kurlat, Exercício 5.8 (p. 97); Lista 1

Q: A Solow economy has saving rate $s$, population growth $n$, depreciation $\delta$ and a per-worker production function with $f'(k)>0$, $f''(k)<0$ and $f'(0)=\infty$, but $\lim_{k\to\infty}f'(k)=b>0$. What happens if $s\,b>n+\delta$?
- No steady state with positive capital exists: $k$ grows without bound and its growth rate tends to $sb-(n+\delta)$, so saving affects long-run growth.
- A unique steady state still exists, because diminishing returns alone ensure that $sf(k)$ eventually falls below $(n+\delta)k$ as capital accumulates.
- Two steady states exist, a stable one at low $k$ and an unstable one at high $k$, so where the economy ends up depends on its initial capital.
- No steady state with positive capital exists: $k$ falls to zero from any start, because replacement investment eventually outruns actual investment.
<!-- YW5zOjA= -->
> The growth rate of capital is $\dot k/k=s f(k)/k-(n+\delta)$. By L'Hôpital, $f(k)/k\to b$, and since $f$ is concave, $f(k)/k$ falls toward $b$ from above. With $sb>n+\delta$ the growth rate stays positive forever and tends to $sb-(n+\delta)$, which is the AK model in the limit. Diminishing returns alone (B) are not enough: the second Inada condition, $f'(\infty)=0$, is what forces the $sf(k)$ curve to cross the replacement line. Saving then has a *rate* effect, not just a level effect.
> Ref: Kurlat (2020), §4.1 (pp. 53–57); §4.2 (pp. 57–61); Map [[02-ingredients]]
> Similar: Kurlat, Exercício 4.4 (p. 73); Lista 1

Q: The Solow model is written per worker, $y=f(k)$ with $f(k)\equiv F(k,1)$, $k=K/L$ and $y=Y/L$. Which assumption on $F(K,L)$ makes that rewriting legitimate, and what would break without it?
- Diminishing marginal returns to capital; without them, output per worker would still depend only on $k$, but no steady state would exist.
- The Inada conditions; without them, output per worker would depend on the size of the labour force, so large countries would be richer.
- A constant saving rate; without it, output per worker would depend on how saving varies with income, so $f$ would shift as $k$ rises.
- Constant returns to scale; without them, output per worker would depend on the size of the labour force as well as on capital per worker.
<!-- YW5zOjM= -->
> $F(K,L)/L=F(K/L,1)$ is the definition of homogeneity of degree one. Under increasing returns, $Y/L$ rises with $L$ at given $K/L$, so the economy's scale would matter. CRS is therefore what lets one equation in $k$ stand in for the whole economy. Inada conditions (B) deliver existence of the steady state, not the per-worker form. Saving behaviour (C) concerns accumulation and has nothing to do with the shape of $F$.
> Ref: Kurlat (2020), §4.1 (pp. 53–57); Map [[02-ingredients]]
> Similar: Kurlat, Exercício 4.1 (p. 72); Lista 1

Q: In the Solow model without technical progress, population growth rises permanently from $n$ to $n'>n$. Comparing the new steady state with the old one, what happens to output per worker and to aggregate output?
- Output per worker is unchanged in the long run because $n$ enters the steady state only through the level of $L$; aggregate output grows faster, at $n'$.
- Output per worker is permanently lower because capital is spread over more workers; aggregate output grows permanently faster, at $n'$ instead of $n$.
- Output per worker is permanently lower because capital is spread over more workers; aggregate output grows at $n'$ only during the transition, then at $n$.
- Output per worker is permanently higher because a larger labour force raises the return on capital; aggregate output grows at $n'$ in the long run.
<!-- YW5zOjE= -->
> The replacement line $(n'+\delta)k$ is steeper, so $k_{ss}=(s/(n'+\delta))^{1/(1-\alpha)}$ falls and $y_{ss}$ falls with it. This is a level effect. In the new steady state $k$ and $y$ are constant while $L$ grows at $n'$, so $K$ and $Y$ grow at $n'$ for ever. Option C mixes up the growth rate of the aggregate with that of the per-worker variables. Option A forgets that $n$ appears in the break-even investment term.
> Ref: Kurlat (2020), §4.2 (pp. 57–61); Map [[05-comparative-statics]]
> Similar: Kurlat, Exercício 4.1 (p. 72); Lista 1

Q: A Solow economy with $y=k^{\alpha}$, population growth $n$ and depreciation $\delta$ sits at its steady state under saving rate $s$. The saving rate rises permanently to $s'>s$. Using $\dot k = s f(k) - (n+\delta)k$, what is the growth rate of output per worker immediately after the change?
- $(n+\delta)\dfrac{s'-s}{s}$, the same as the growth rate of capital per worker, since output and capital move together on impact.
- $\alpha\,(s'-s)$, proportional to the change in the saving rate alone, since $n$ and $\delta$ do not shift on impact.
- $\alpha\,(n+\delta)\dfrac{s'-s}{s}$, a fraction $\alpha$ of the growth rate of capital per worker, and it decays toward zero.
- $\alpha\,(n+\delta)\dfrac{s'-s}{s'}$, a fraction $\alpha$ of the growth rate of capital per worker, and it decays toward zero.
<!-- YW5zOjI= -->
> At the old steady state $f(k_{ss})/k_{ss}=(n+\delta)/s$. On impact, $\dot k/k=s'(n+\delta)/s-(n+\delta)=(n+\delta)(s'-s)/s$. Since $y=k^{\alpha}$, $g_y=\alpha\,g_k$. Growth then falls back to zero as $k$ approaches the new steady state: the level effect shows up as a temporary burst of growth. Option D evaluates $f(k)/k$ at the new steady state when it should use the old one. Option A forgets the elasticity $\alpha$.
> Ref: Kurlat (2020), §4.2 (pp. 57–61); Map [[05-comparative-statics]]
> Similar: Kurlat, Exercício 4.1 (p. 72); Exercício 5.2 (p. 94)

Q: In the Solow model with $y=A k^{\alpha}$, saving rate $s$, population growth $n$ and depreciation $\delta$, what is the elasticity of steady-state output per worker $y_{ss}$ to a permanent change in productivity $A$, and why?
- $\dfrac{1}{1-\alpha}$: higher $A$ raises output directly and, through saving out of it, induces more capital, which raises output again.
- $1$: higher $A$ scales output one for one, while capital per worker is set by $s/(n+\delta)$ alone and does not respond to productivity.
- $\dfrac{\alpha}{1-\alpha}$: higher $A$ acts only through the extra capital it induces, since in the steady state output is pinned down by capital.
- $\dfrac{1}{\alpha}$: higher $A$ raises output directly and, since capital earns a share $\alpha$ of income, the induced capital multiplies that effect.
<!-- YW5zOjA= -->
> $sAk^{\alpha}=(n+\delta)k$ gives $k_{ss}=(sA/(n+\delta))^{1/(1-\alpha)}$, and then $y_{ss}=Ak_{ss}^{\alpha}=A^{1/(1-\alpha)}(s/(n+\delta))^{\alpha/(1-\alpha)}$. The direct effect has elasticity $1$ and the induced capital adds $\alpha/(1-\alpha)$. This multiplier is why, in development accounting, part of what looks like a capital gap is really a TFP gap at work. Option C leaves out the direct effect, and option B leaves out the induced capital.
> Ref: Kurlat (2020), §4.2 (pp. 57–61); cap. 5, §5.1 (pp. 75–80)
> Similar: Kurlat, Exercício 5.1 (p. 93); Lista 1
