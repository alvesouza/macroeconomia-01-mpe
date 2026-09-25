---
tags: [benigno, adas, aula-09, multiplicador-fiscal, tabela-1, tabela-2]
date: 2026-09-15
---

# 7. Fiscal multipliers: Table 1 derived, Table 2 reproduced

**Article: §8, equations (22)–(23), Tables 1–2, Figure 10, printed pages 514–516.** Up:
[[00-index]] · Prev: [[06-markup-shocks]] · Next: [[08-liquidity-trap]]

The article writes Table 1 down and moves on. This note derives all six entries, then
reproduces every cell of Table 2 — and the runnable version of that check is
`check_multipliers.py` in this folder, which fails if any formula here is mistyped.

The section's moral, stated once so the algebra has somewhere to go: **judging fiscal
policy by its multiplier on output is misleading, because the object that matters for
welfare is the gap, and the two have different signs for some instruments.**

> **Companion:** [The Multiplier Bench](companion-multipliers.html) — all six multipliers
> recomputed as $lpha$, $\sigma$ and $\eta$ move, with the output multiplier and the gap
> multiplier shown together so the sign disagreement of §7.4 is visible.

---

## 7.1 Setting up

Keep only the fiscal terms of the AD curve (21), setting $i$, $\rho$, $\bar p$ and $p^e$
aside as unaffected by fiscal policy (p. 514):

$$y=g+\bar y_n-\bar g-\sigma\left[p-(\bar\tau_c-\tau_c)\right]$$

Substitute the AS curve (20), $p=\kappa(y-y_n)$ with $p^e$ normalised to zero:

$$y=g+\bar y_n-\bar g-\sigma\kappa(y-y_n)+\sigma(\bar\tau_c-\tau_c)$$

$$y\,(1+\sigma\kappa)=g+\bar y_n-\bar g+\sigma\kappa\,y_n+\sigma(\bar\tau_c-\tau_c)$$

$$y=\frac{g+\bar y_n-\bar g+\sigma\kappa\,y_n+\sigma(\bar\tau_c-\tau_c)}{1+\sigma\kappa}
\tag{$\dagger$}$$

Now the fiscal content of the natural rates. The aggregate mark-up (13) is, to first
order, the sum of its components:

$$\mu\simeq\mu_\theta+\tau_l+\tau_w+\tau_y+\tau_c\;\equiv\;\mu_\theta+\tau+\tau_c,
\qquad \tau\equiv\tau_l+\tau_w+\tau_y$$

(the same for $\bar\mu$). So from (15), keeping only fiscal terms:

$$y_n\big|_{\text{fiscal}}=\frac{\sigma^{-1}g-\tau-\tau_c}{\sigma^{-1}+\eta},
\qquad
\bar y_n\big|_{\text{fiscal}}=\frac{\sigma^{-1}\bar g-\bar\tau-\bar\tau_c}{\sigma^{-1}+\eta}$$

Collapsing $\tau_l,\tau_w,\tau_y$ into a single $\tau$ is legitimate precisely because
they enter only through $\mu$ — the model cannot distinguish them. $\tau_c$ has to be
kept separate because it *also* enters AD directly.

## 7.2 Substituting, term by term

Put both natural rates into $(\dagger)$ and read off coefficients. Write
$D\equiv(\sigma^{-1}+\eta)(1+\sigma\kappa)$, which will be the shared denominator.

**Coefficient on $g$.** Two routes: directly ($+1$) and through $y_n$
($\sigma\kappa\cdot\sigma^{-1}/(\sigma^{-1}+\eta)=\kappa/(\sigma^{-1}+\eta)$). Dividing by
$1+\sigma\kappa$:

$$m_g=\frac{1}{1+\sigma\kappa}+\frac{\kappa}{D}$$

**Coefficient on $\bar g$.** Through $\bar y_n$ ($+\sigma^{-1}/(\sigma^{-1}+\eta)$) and
directly ($-1$):

$$\frac{\sigma^{-1}}{\sigma^{-1}+\eta}-1=\frac{\sigma^{-1}-\sigma^{-1}-\eta}{\sigma^{-1}+\eta}
=-\frac{\eta}{\sigma^{-1}+\eta}
\qquad\Longrightarrow\qquad
m_{\bar g}=\frac{\eta}{D}$$

> **The third confirmation of eq. (15).** This cancellation is the evidence promised in
> [[02-firms-and-as]] §2.4. Benigno's own Table 1 gives
> $m_{\bar g}=\eta/[(\sigma^{-1}+\eta)(1+\kappa\sigma)]$, and that $\eta$ in the numerator
> can only arise from $\sigma^{-1}/(\sigma^{-1}+\eta)-1$. With the mis-transcribed
> coefficient $(\sigma^{-1}-1)$ the same step would give $(1+\eta)/(\sigma^{-1}+\eta)$,
> and Table 2 would not reproduce in any row.

**Coefficient on $\tau$.** Only through $y_n$: $\sigma\kappa\cdot(-1)/(\sigma^{-1}+\eta)$,
so $m_\tau=\kappa\sigma/D$.

**Coefficient on $\bar\tau$.** Only through $\bar y_n$: $-1/(\sigma^{-1}+\eta)$, so
$m_{\bar\tau}=1/D$.

**Coefficient on $\tau_c$.** Through $y_n$ *and* directly through AD:
$-\left[\sigma\kappa/(\sigma^{-1}+\eta)+\sigma\right]/(1+\sigma\kappa)=-\sigma m_g$.

**Coefficient on $\bar\tau_c$.** Through $\bar y_n$ and through AD:

$$\frac{\sigma-\dfrac{1}{\sigma^{-1}+\eta}}{1+\sigma\kappa}
=\frac{\sigma(\sigma^{-1}+\eta)-1}{D}=\frac{\sigma\eta}{D}=\sigma m_{\bar g}$$

Collecting, this is eq. (22) and Table 1:

$$\boxed{\;y=m_g\,g-m_{\bar g}\,\bar g-m_\tau\,\tau-m_{\bar\tau}\,\bar\tau-m_{\tau_c}\,\tau_c+m_{\bar\tau_c}\,\bar\tau_c\;} \tag{22}$$

| | Table 1 formula | Sign in (22) | Why |
|---|---|---|---|
| $m_g$ | $\dfrac{1}{1+\kappa\sigma}+\dfrac{\kappa}{(\sigma^{-1}+\eta)(1+\kappa\sigma)}$ | $+$ | demand **and** supply both expand |
| $m_{\bar g}$ | $\dfrac{\eta}{(\sigma^{-1}+\eta)(1+\kappa\sigma)}$ | $-$ | future spending makes tomorrow poorer: cut consumption today |
| $m_\tau$ | $\dfrac{\kappa\sigma}{(\sigma^{-1}+\eta)(1+\kappa\sigma)}$ | $-$ | AS shifts up, prices rise, real rate rises along AD |
| $m_{\bar\tau}$ | $\dfrac{1}{(\sigma^{-1}+\eta)(1+\kappa\sigma)}$ | $-$ | lower $\bar c_n$ shifts AD down |
| $m_{\tau_c}$ | $\sigma\,m_g$ | $-$ | **both** channels: mark-up shock *and* intertemporal price |
| $m_{\bar\tau_c}$ | $\sigma\,m_{\bar g}$ | $+$ | both channels again, and the intertemporal one wins (see §4.6) |

**"Multipliers" is a courtesy title.** The article says so plainly (p. 515): most of
these "do not have multiplying effects on output in the Keynesian sense". $m_g<1$
always, and it equals one only in the knife-edge $\eta=0$:

$$\eta=0:\quad \kappa=\frac{(1-\alpha)\sigma^{-1}}{\alpha},\quad
m_g=\frac{1}{1+\sigma\kappa}+\frac{\kappa\sigma}{1+\sigma\kappa}=1$$

With $\eta>0$ there is genuine crowding out: $g\uparrow$ raises prices, the real rate
rises, and private consumption falls.

## 7.3 Table 2, reproduced

Computed from the formulas above; run `python Map/benigno/check_multipliers.py` to
regenerate. Printed values from p. 516 in parentheses where rounding differs.

| $\alpha$ | $\sigma$ | $\eta$ | $\kappa$ | $m_g$ | $m_{\bar g}$ | $m_\tau$ | $m_{\bar\tau}$ | $m_{\tau_c}$ | $m_{\bar\tau_c}$ |
|---|---|---|---|---|---|---|---|---|---|
| 0.66 | 0.5 | 0.2 | 1.133 | 0.967 (0.96) | 0.058 | 0.164 | 0.290 | 0.484 | 0.029 |
| 0.75 | 0.5 | 0.2 | 0.733 | 0.976 (0.98) | 0.067 (0.06) | 0.122 | 0.333 | 0.488 | 0.033 |
| 0.66 | 1.0 | 0.2 | 0.618 | 0.936 (0.94) | 0.103 | 0.318 | 0.515 | 0.936 | 0.103 |
| 0.75 | 1.0 | 0.2 | 0.400 | 0.952 | 0.119 | 0.238 | 0.595 | 0.952 | 0.119 |
| 0.66 | 1.0 | 1.0 | 1.030 | 0.746 (0.75) | 0.246 | 0.254 | 0.246 | 0.746 | 0.246 |
| 0.75 | 1.0 | 1.0 | 0.667 | 0.800 | 0.300 | 0.200 | 0.300 | 0.800 | 0.300 |
| 0.66 | 0.5 | 1.0 | 1.545 | 0.855 (0.86) | 0.188 | 0.145 | 0.188 | 0.427 | 0.094 |
| 0.75 | 0.5 | 1.0 | 1.000 | 0.889 (0.88) | 0.222 | 0.111 | 0.222 | 0.444 | 0.111 |

Calibration sources (p. 515): $\alpha=1-1/D$ with price duration $D=3$ quarters for the
United States gives $\alpha\simeq0.66$, with $0.75$ as the high-rigidity experiment;
$\tilde\sigma$ between one half and one; $1/\eta$ near 5 in micro studies but near 1 in
estimated DSGE models (Smets and Wouters, 2003), hence $\eta\in\{0.2,\,1\}$.

**What the numbers say.** Every multiplier is below one. A one-percent-of-GDP rise in
short-run public spending raises output between 0.75% and 0.98%. Short-run tax rises cut
output by 0.11 to 0.32. The consumption-tax multiplier is the one that swings most with
$\sigma$ — around 0.43–0.49 at $\sigma=0.5$, but 0.75–0.95 at $\sigma=1$ — because it is
literally $\sigma\,m_g$: it works through intertemporal substitution, so it inherits the
household's willingness to substitute.

## 7.4 The multipliers on the output gap

Subtract (15) from (22). Coefficient by coefficient, and each cancellation is worth
watching:

$$m_g-\frac{\sigma^{-1}}{\sigma^{-1}+\eta}
=\frac{(\sigma^{-1}+\eta)+\kappa}{D}-\frac{\sigma^{-1}(1+\sigma\kappa)}{D}
=\frac{\sigma^{-1}+\eta+\kappa-\sigma^{-1}-\kappa}{D}=\frac{\eta}{D}=m_{\bar g}$$

$$-m_\tau+\frac{1}{\sigma^{-1}+\eta}=\frac{-\kappa\sigma+(1+\sigma\kappa)}{D}=\frac{1}{D}=m_{\bar\tau}$$

$$-m_{\tau_c}+\frac{1}{\sigma^{-1}+\eta}=\frac{-(1+\sigma\eta+\sigma\kappa)+(1+\sigma\kappa)}{D}
=-\frac{\sigma\eta}{D}=-m_{\bar\tau_c}$$

so that

$$\boxed{\;y-y_n=m_{\bar g}\,(g-\bar g)+m_{\bar\tau}\,(\tau-\bar\tau)-m_{\bar\tau_c}\,(\tau_c-\bar\tau_c)\;} \tag{23}$$

Three results, and all three are examinable:

1. **Permanent fiscal policy does not move the gap.** Every term is a short-minus-long
   difference. Set $g=\bar g$, $\tau=\bar\tau$, $\tau_c=\bar\tau_c$ and the gap is zero,
   whatever the levels. Fiscal policy stabilises only by being *temporary*.
2. **The gap multipliers are the long-run output multipliers.** $m_{\bar g}$,
   $m_{\bar\tau}$, $m_{\bar\tau_c}$ — small numbers. A one-point rise in the
   spending-to-GDP ratio narrows the gap by between 0.06 and 0.30, and at the more
   realistic $\eta=0.2$ by no more than 0.12. Compare $m_g\simeq0.96$ on output: **the
   multiplier on the gap is roughly one eighth of the multiplier on output.**
3. **A consumption-tax cut has the wrong sign.** $\tau_c\downarrow$ raises output
   ($-m_{\tau_c}$ in (22)) but *widens* the gap ($-m_{\bar\tau_c}$ in (23)). Conversely a
   rise in $\tau$ cuts output yet narrows the gap, because it cuts the natural rate by
   more than it cuts output.

## 7.5 The gap against the efficient level

Since $y_n-y_e=-\mu/(\sigma^{-1}+\eta)$ and $\mu\big|_{\text{fiscal}}=\tau+\tau_c$:

$$y-y_e=(y-y_n)-\frac{\tau+\tau_c}{\sigma^{-1}+\eta}$$

Take the $\tau$ terms: $m_{\bar\tau}\tau-\tau/(\sigma^{-1}+\eta)
=\tau\left[1-(1+\kappa\sigma)\right]/D=-\kappa\sigma\tau/D=-m_\tau\tau$. The same
manipulation on $\tau_c$ returns $-m_{\tau_c}$, and $\mu$ contains no $g$, so:

$$\boxed{\;y-y_e=m_{\bar g}\,(g-\bar g)-m_\tau\,\tau-m_{\bar\tau}\,\bar\tau-m_{\tau_c}\,\tau_c+m_{\bar\tau_c}\,\bar\tau_c\;}$$

**Tax multipliers as in (22); spending multipliers as in (23).** The economics: distorting
taxes do not move $y_e$ at all, so their effect on the efficient gap is their full effect
on output; short-run spending moves $y_n$ and $y_e$ by the same amount, so only the
$m_{\bar g}$ part survives.

> **An error in the article.** The prose on p. 515 says this equation "has the same short-
> and long-run public-spending multipliers as Eq. (22) and the same taxation multipliers
> as Eq. (23)". It is the other way round on both counts, as the derivation above shows
> and as the article's own next sentence confirms: "a short-run spending shock moves the
> natural and the efficient level of output, proportionally" — which is precisely why the
> $g$ coefficient must shrink from $m_g$ to $m_{\bar g}$.

## 7.6 The picture: a temporary spending rise (Fig. 10, p. 516)

$g\uparrow$ with $\bar g$ fixed moves **both** curves, the only fiscal instrument
besides $\tau_c$ that does:

- AD shifts up, because $g$ enters (21) directly;
- AS shifts down and right, because $y_n$ rises with $g$ by (15) — the negative wealth
  effect on leisure.

By (23) the gap rises by $m_{\bar g}\,dg>0$, so from an initial zero gap the new
equilibrium $E'$ must lie to the **right of the new natural rate** $y_n'$. Prices rise,
the real rate rises, private consumption is crowded out. The article's summary of $E'$
is worth quoting because it is the whole ambiguity of fiscal stimulus in one line
(p. 516): *"On one hand the economy is overheated by a positive output gap, on the other
hand, private consumption is crowded out."*

To stabilise, raise $i$ and walk AD back to $E''$, where $p=p^e$ and the gap is zero.

**The $\eta=0$ knife-edge** (footnote 10, p. 516): with linear disutility of labour, AS
and AD shift *proportionally*, the new equilibrium lands exactly on $y_n'$, and prices
are stable with no intervention at all. Consistent with $m_{\bar g}=\eta/D=0$ in (23).

## 7.7 The financing caveat

Every number above assumes the government can satisfy (18) by adjusting lump-sum
transfers, so Ricardian equivalence holds. The article flags the alternative (p. 516): if
lump-sum transfers are unavailable, a spending rise must be matched by a distorting tax,
short-run or long-run, and the entries of (22) then have to be combined. A
spending-plus-$\tau$ package, for instance, adds $m_g$ and subtracts $m_\tau$ — still
positive on output, but with the gap effect running through $m_{\bar g}+m_{\bar\tau}$.
This qualification is what makes the long-run fiscal menu of [[08-liquidity-trap]]
attractive: those instruments are sustainable by construction.
