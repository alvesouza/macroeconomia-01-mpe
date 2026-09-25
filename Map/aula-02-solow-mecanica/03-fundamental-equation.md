---
tags: [aula-02, kurlat-cap-04, equacao-de-solow, tempo-discreto, tempo-continuo, derivacao]
date: 2026-09-18
---

# 3. The fundamental equation, every line shown

**Kurlat §4.2, printed pages 57–59.** Up: [[00-index]] · Prev: [[02-ingredients]] ·
Next: [[04-steady-state-and-stability]]

> **Companion:** [The Solow Diagram](companion-solow.html) — the two curves, the steady state,
> and the exact discrete path overlaid on the continuous approximation so the gap between them
> is visible rather than asserted.

Target: equation (4.2.2). It looks like a definition and it is not — the $(1+n)$ has to be
handled carefully, and the version everybody memorises is an approximation whose error this note
sizes.

---

## 3.1 The per-worker production function

Define $y\equiv Y/L$ and $k\equiv K/L$. Then

$$y = \frac{F(K,L)}{L} \;\overset{\text{CRS}}{=}\; F\!\left(\frac{K}{L},1\right) \;\equiv\; f(k) \tag{4.2.1}$$

Three steps, and Kurlat is explicit that the middle one is the only substantive one. The first
replaces $Y$ using the production function. The second applies Assumption 4.1 with
$\lambda=1/L$. The third is a definition: $f(k)$ is what one worker produces with $k$ units of
capital.

For Cobb–Douglas, $f(k)=k^{\alpha}$, and its derivatives inherit everything from §2.1:
$f'(k)=\alpha k^{\alpha-1}>0$, $f''(k)=\alpha(\alpha-1)k^{\alpha-2}<0$, $f'(0^+)=\infty$,
$f'(\infty)=0$.

## 3.2 The exact law of motion

Now derive how $k$ moves. Kurlat's chain (p. 58), with each step named:

$$\Delta k_{t+1} \equiv k_{t+1}-k_t \qquad\text{(definition)}$$

$$= \frac{K_{t+1}}{L_{t+1}}-k_t \qquad\text{(definition of } k_{t+1})$$

$$= \frac{(1-\delta)K_t+I_t}{L_{t+1}}-k_t \qquad\text{(using 4.1.4)}$$

$$= \frac{(1-\delta)K_t+sY_t}{L_{t+1}}-k_t \qquad\text{(using 4.1.3)}$$

Now the step that has to be done carefully. Multiply and divide by $L_t$ so the numerator can be
written per worker:

$$= \frac{(1-\delta)K_t+sY_t}{L_t}\cdot\frac{L_t}{L_{t+1}}-k_t \qquad\text{(rearranging)}$$

and use Assumption 4.5, $L_{t+1}=(1+n)L_t$, so $L_t/L_{t+1}=1/(1+n)$:

$$\boxed{\;\Delta k_{t+1} = \frac{(1-\delta)k_t+s f(k_t)}{1+n}-k_t\;} \tag{4.2.2, exact}$$

This is the **exact** discrete-time law, and it is what the simulation code in
[[02_crescimento_solow]] implements. Equivalently, in level form:

$$k_{t+1} = \frac{(1-\delta)k_t+s f(k_t)}{1+n}$$

## 3.3 The approximation everyone uses, and its error

Expand the exact form over the common denominator:

$$\Delta k_{t+1} = \frac{(1-\delta)k_t+sf(k_t)-(1+n)k_t}{1+n}
= \frac{sf(k_t)-(\delta+n)k_t}{1+n}$$

so the exact change is the familiar expression **divided by $1+n$**:

$$\boxed{\;\Delta k_{t+1} = \frac{sf(k_t)-(\delta+n)k_t}{1+n}
\;\simeq\; \underbrace{sf(k_t)}_{\text{actual investment}}-\underbrace{(\delta+n)k_t}_{\text{break-even}}\;} \tag{4.2.2}$$

Two things follow, and both matter.

**(i) The approximation is exact about the steady state.** Whatever $n$ is, the two expressions
vanish at the same $k$, because dividing by $1+n>0$ cannot move a zero. So the *steady state of
the approximation is the exact steady state* — the $(1+n)$ affects only the **speed** of
transition, never the destination. This is the reason it is safe to memorise the approximate
form for comparative statics and why trap 2 in [[02_crescimento_solow]] is about dynamics
rather than about $k_{ss}$.

**(ii) The error is exactly a factor $n/(1+n)$ of the change.** Since

$$\Delta k^{\text{approx}} - \Delta k^{\text{exact}}
= \left(sf-(\delta+n)k\right)\left(1-\frac{1}{1+n}\right)
= \frac{n}{1+n}\left(sf-(\delta+n)k\right)$$

with $n=0.01$ the approximation overstates each period's movement by about **1%** of that
movement. Negligible for one period; it accumulates into a visibly faster transition over
decades, which the companion overlays. Quantified in `check_solow.py`.

**Two more traps live in this line**, both from [[02_crescimento_solow]]. Writing the break-even
term as $\delta k$ and dropping $n$ (trap 3) makes the line too flat and $k_{ss}$ too high.
Forgetting the $1+n$ entirely (trap 2) leaves the steady state right and the path wrong.

### Reading the two terms

Kurlat's interpretation of (4.2.2), which is the sentence to be able to say:

- $sf(k_t)$ is **actual investment per worker**: output per worker times the saving rate.
- $(\delta+n)k_t$ is **break-even investment**: what must be invested just to hold $k$ still. Of
  it, $\delta k$ replaces machines that wore out and $nk$ equips the new workers who arrived.

That is why $\delta$ and $n$ appear **together and additively** — they are two reasons the same
stock has to be topped up, and the model cannot tell them apart. A rise in $n$ and a rise in
$\delta$ of the same size are the identical experiment. (This equivalence breaks in session 3,
where technological progress adds $g$ to the same bracket but changes what the variable *means*.)

## 3.4 Continuous time, and the Romer reconciliation

> **Contrast: Romer (2012), ch. 1.** Romer works in continuous time from the start, where the
> derivation is shorter and the $(1+n)$ problem never arises. It is worth doing both, because
> exam questions mix the two conventions.

Start from $k=K/L$ and differentiate with respect to time using the quotient rule:

$$\dot k = \frac{\dot K L - K\dot L}{L^2} = \frac{\dot K}{L}-\frac{K}{L}\frac{\dot L}{L}
= \frac{\dot K}{L}-nk$$

with $n\equiv\dot L/L$. The continuous-time accumulation identity is
$\dot K = I-\delta K = sY-\delta K$, so $\dot K/L = sf(k)-\delta k$ and

$$\boxed{\;\dot k = s f(k)-(\delta+n)k\;}$$

**The approximation of §3.3 is the continuous-time equation exactly.** That is the reconciliation:
what Kurlat presents as an approximation to a difference equation is Romer's differential equation
on the nose, and the $1/(1+n)$ is the entire difference between the two conventions. In the
notation of [[03-growth-arithmetic]] §3.1, the translation is $g\leftrightarrow\ln(1+g)$, and the
discrepancy is second order in $n$.

**Which to use.** Continuous time for anything analytic: the stability proof of
[[04-steady-state-and-stability]], the convergence-speed log-linearisation of session 3, and any
phase diagram. Discrete time for anything you simulate or match to annual data. Say which one you
are in — trap 4 of [[02_crescimento_solow]] is the sibling version of this discipline for
per-worker versus per-efficiency-unit.

## 3.5 The growth rate of $k$, which is what the diagram really shows

Divide the continuous-time equation by $k$:

$$\frac{\dot k}{k} = \frac{s f(k)}{k}-(\delta+n)$$

This is the more useful form for three reasons.

1. **It plots as a decreasing curve against a horizontal line.** $sf(k)/k = sk^{\alpha-1}$ is
   strictly decreasing in $k$ under Cobb–Douglas, so the growth rate of capital per worker falls
   monotonically as the economy accumulates. That single picture *is* conditional convergence.
2. **It is what growth regressions estimate.** The empirical work in session 3 regresses
   $\dot k/k$ (or $\dot y/y$) on the level, and this equation is its theoretical counterpart.
3. **The Cobb–Douglas case gives the growth rate of output free.** Since $y=k^{\alpha}$,
   $\dot y/y = \alpha\,\dot k/k$, so output per worker grows at $\alpha$ times the rate of capital
   per worker — always slower, and the gap is exactly the capital share.

## 3.6 What to be able to do, cold

1. Derive (4.2.2) from (4.1.4) and Assumption 4.5, showing where $L_t/L_{t+1}$ enters.
2. State the exact and approximate laws and say precisely what the $1+n$ does and does not change.
3. Derive the continuous-time version with the quotient rule and identify it with the
   approximation.
4. Name the two components of break-even investment and say why $\delta$ and $n$ are
   interchangeable here.
5. Write $\dot k/k$ and read conditional convergence off it in one sentence.

Practice: Kurlat ch. 4, Exercises 4.3 and 4.4 (pp. 72–73) build and simulate the law of motion.
Worked in [[Resolucao/kurlat_solutions_ch1-4|ch1-4]].
