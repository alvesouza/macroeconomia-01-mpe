---
tags: [prova, correction, macro1]
date: 2026-10-16
---

# Prova 01 — error analysis and correct solutions

Source: the nine photos in `Prova/Prova 01/`. Score read from the grader's marks:
**Q1 1.0/1.5 · Q2 3.1/5.5 · Q3 0.5/3.0 · total ≈ 4.6/10.**

Full step-by-step solution with figures and rubric: `prova-01-solution.pdf` (source
`prova-01-solution.tex`, checked by `prova-01-solution-check.py`).

| Item | Pts | Got | Error type | One-line diagnosis |
|---|---|---|---|---|
| 1.a | 0.5 | 0.5 | — | Correct (final-goods GDP = 1000) |
| 1.b | 0.5 | 0.3 | Incomplete | Number right, but the item asked for **three approaches** (product, income, expenditure); only one was given |
| 1.c | 0.5 | 0.2 | **Conceptual** + incomplete | 1100 right, but the extra 100 was attributed to "wages and **consumption**". It is **investment** (own-account software = gross fixed capital formation). No three approaches |
| 2.a | 1.0 | 1.0 | — | Correct: $k_{SS}=\left(\frac{sA}{n+\delta}\right)^{1/(1-\sigma)}$ |
| 2.b | 1.0 | 0.3 | **Algebra** | $c_{SS}=(1-s)A\,k_{SS}^{\sigma}$, but the substitution dropped the $\sigma$: wrote $(\cdot)^{1/(1-\sigma)}$ instead of $(\cdot)^{\sigma/(1-\sigma)}$, so got $s=1/(2-\sigma)$ instead of $s_{GR}=\sigma$ |
| 2.c | 1.0 | 0.9 | Incomplete | Budget constraint omits **firm profits** $\Pi_1$ (household owns the firm); interpretation "consumption adjusted by r" is loose — it is a present-value statement |
| 2.d | 1.0 | 0.8 | Incomplete | Euler and $c_1$ right, but **no FOC for $L_1$** ("todas as variáveis de sua escolha") |
| 2.e | 1.0 | 0.0 | **Conceptual** | Saving rate not derived from the optimum (it is $\beta/(1+\beta)$); no market clearing $K_2=a_1$; wrong $k_2(k_1)$ map; diagram without a valid steady state |
| 2.f | 0.5 | 0.1 | **Conceptual** | "Solow with $\delta=1$, $n=0$" is half the answer. The point: the saving rate is **endogenous** ($\beta/(1+\beta)$, from preferences), and compare it with $s_{GR}=\sigma$ |
| 3.a | 1.0 | 0.2 | **Conceptual** | Shifted **AS** via current $\mu$; the item is about the **long-run** markup $\bar\mu$, which moves $\bar y$ and hence **AD**. Inconsistent sign story ("p↑ y↓" in AD) |
| 3.b | 1.0 | 0.1 | **Conceptual (sign)** | Said *raise* the rate. A fall in AD with prices falling calls for a **cut** in $i$; no discussion of the cost |
| 3.c | 1.0 | ~0.2 | Method + conceptual | Did not use $dL/dy=0$ along AS; differentiated in $i$ and then used a $y_e$ that contained $\mu$; concluded the response depends on $\phi$ vs $\sigma$ — it does not |

## The five error clusters (each becomes one NotebookLM audio)

1. **GDP: three approaches must each be computed and must agree.** Value added (product),
   factor incomes (income), final uses $C+I+G+NX$ (expenditure). Intermediate vs final;
   zero-price services are not in GDP; own-account software is investment.
2. **Golden rule algebra: carry the exponent.** $c=(1-s)f(k)$ with $f(k)=Ak^\sigma$, so
   $c_{SS}\propto(1-s)s^{\sigma/(1-\sigma)}$. Cross-check with $f'(k_{GR})=n+\delta$. Sanity
   test at a knife edge: $\sigma\to0\Rightarrow s_{GR}\to0$; the wrong answer gives $1/2$.
3. **The household problem: list every choice variable and every income source.**
   $c_1,c_2,a_1,L_1$; labour income **and** profits; a choice with no utility cost (labour
   here) is a corner solution, and saying so *is* the FOC.
4. **From one household to the economy.** Market clearing $K_2=a_1$ turns the saving rule
   into a law of motion $k_2=\phi(k_1)$; draw it against the 45° line. Relation to Solow:
   same law of motion with $\delta=1$, $n=0$, but $s=\beta/(1+\beta)$ **is chosen**, and it
   need not equal $s_{GR}=\sigma$.
5. **Benigno: which bar moves which curve, and the sign of policy.** $\bar\mu\to\bar y\to$ AD;
   $\mu\to y_n\to$ AS. A pure AD shock has no trade-off (divine coincidence): cut $i$. Optimal
   policy = minimise the loss **along AS** ($dL/dy=0$); the response to $\bar\mu$ news does
   not depend on $\phi$.

---

## Correct solutions

### Q1 — GDP (Kurlat cap. 1; Aula 1)

Notation: A = input firm, B = final-goods firm, N = social network.

**1.a.** Product: $VA_A=600$, $VA_B=1000-600=400$, GDP $=1000$. Income: factor incomes of A
(600) and B (400). Expenditure: $C=1000$. All three give **1000**. Counting $600+1000$ would
double-count the input.

**1.b.** Advertising is a service **bought by a firm**, so it is an **intermediate input**
of B. The service users get for free has price zero and is not a market transaction.

| Approach | A | B | N | GDP |
|---|---|---|---|---|
| Product (VA) | 600 | $1000-600-100=300$ | 100 | **1000** |
| Income | 600 | 300 (B's profit falls by 100) | 100 | **1000** |
| Expenditure | — | — | — | $C=1000$ → **1000** |

Comparison with 1.a: GDP is unchanged. Only the **distribution** of income moves (100 from B
to N). The welfare from the free service is real but not measured (a "Beyond GDP" point,
Kurlat cap. 2).

**1.c.** N uses its 100 to pay workers who build software for N's own use. Software is a
durable productive asset, so it is **gross fixed capital formation** (investment in
intellectual property), valued at cost.

| Approach | A | B | N | GDP |
|---|---|---|---|---|
| Product (VA) | 600 | 300 | ads 100 + software 100 = 200 | **1100** |
| Income | 600 | 300 | wages 100 + operating surplus 100 | **1100** |
| Expenditure | — | — | — | $C=1000$, $I=100$ → **1100** |

GDP rises by 100 because a new **final** good (an investment good) was produced. It is not
consumption: by the statement nothing else changes, so $C$ stays 1000. If the software were
expensed as an intermediate cost, GDP would stay at 1000. Capitalising software is the
modern national-accounts convention.

### Q2 — Solow, golden rule, two-period equilibrium (Kurlat caps. 4-6, 9)

**2.a.** $y_t=Ak_t^\sigma$; $(1+n)k_{t+1}=(1-\delta)k_t+sAk_t^\sigma$, so
$\frac{k_{t+1}}{k_t}=\frac{1-\delta+sAk_t^{\sigma-1}}{1+n}$. Setting $k_{t+1}=k_t$:
$$k_{SS}=\left(\frac{sA}{n+\delta}\right)^{\frac1{1-\sigma}}.$$

**2.b.** $c_{SS}=(1-s)Ak_{SS}^{\sigma}=(1-s)A\left(\frac{sA}{n+\delta}\right)^{\frac{\sigma}{1-\sigma}}$.
$$\ln c_{SS}=\text{const}+\ln(1-s)+\tfrac{\sigma}{1-\sigma}\ln s
\;\Rightarrow\; -\frac1{1-s}+\frac{\sigma}{(1-\sigma)s}=0
\;\Rightarrow\;\sigma(1-s)=(1-\sigma)s\;\Rightarrow\;\boxed{s_{GR}=\sigma}.$$
SOC: $-\frac1{(1-s)^2}-\frac{\sigma}{(1-\sigma)s^2}<0$. Cross-check: $\max_k Ak^\sigma-(n+\delta)k$
gives $\sigma Ak^{\sigma-1}=n+\delta$ (MPK = $n+\delta$). Then
$s=(n+\delta)k/(Ak^\sigma)=\sigma$. **Golden-rule saving = capital share.**

**2.c.** Household (owns the firm; $\bar L=1$ time endowment). Period 1:
$c_1+a_1=a_0+w_1AL_1+\Pi_1$. Period 2 (retired): $c_2=(1+r)a_1$. Eliminating $a_1$:
$$c_1+\frac{c_2}{1+r}=a_0+w_1AL_1+\Pi_1 .$$
Reading: the **present value** of lifetime consumption equals initial wealth plus the
present value of income (labour and profits). Leaving wealth unspent at the end is never
optimal ($u'>0$), so the constraint binds.

**2.d.**
$\mathcal L=\ln c_1+\beta\ln c_2+\lambda\big[a_0+w_1AL_1+\Pi_1-c_1-\tfrac{c_2}{1+r}\big]+\nu(1-L_1)$.

- $c_1$: $1/c_1=\lambda$.
- $c_2$: $\beta/c_2=\lambda/(1+r)$.
- $L_1$: $\lambda w_1A-\nu=0\Rightarrow\nu=w_1A/c_1>0\Rightarrow L_1=1$. Work carries no
  disutility, so the household supplies its whole endowment (corner solution).
- Euler: $c_2=\beta(1+r)c_1$.

Hence
$$c_1=\frac{a_0+w_1A+\Pi_1}{1+\beta},\quad c_2=\frac{\beta(1+r)}{1+\beta}(a_0+w_1A+\Pi_1),\quad a_1=\frac{\beta}{1+\beta}(a_0+w_1A+\Pi_1).$$
Interpretation: with log utility the household consumes a fraction $1/(1+\beta)$ of
lifetime wealth. $c_1$ does not depend on $r$ because all resources arrive in period 1, so
the income and substitution effects cancel. More patience (higher $\beta$) means a lower
$c_1$ and more saving.

**2.e.** Saving rate $=a_1/(\text{resources})=\boxed{\beta/(1+\beta)}$, constant. Firm,
competitive: $w_1A=(1-\sigma)AK_1^\sigma L_1^{-\sigma}$, so $w_1A=(1-\sigma)Ak_1^\sigma$ at
$L_1=1$. Profit is the capital share, $\Pi_1=\sigma Ak_1^\sigma$ (the initial stock belongs to
the household's firm and depreciates fully). Then labour income plus profit equals $Y_1$.
The only asset is capital, so **market clearing** gives $K_2=a_1$:
$$k_2=\frac{\beta}{1+\beta}\big(a_0+Ak_1^\sigma\big).$$
Diagram: a concave curve with intercept $\beta a_0/(1+\beta)$, slope falling to 0. It
crosses the 45° line exactly once, and that crossing is $k_{SS}$; it is stable, since the
slope there is below 1. Repeating the economy with $a_0$ as a one-off (or $a_0=0$ for later
cohorts):
$$k_{SS}=\left(\frac{\beta A}{1+\beta}\right)^{\frac1{1-\sigma}}.$$
*Reading note.* The statement does not say who owns $K_1$. In the overlapping-generations
reading (the young save only wages; the old consume the capital income), the map is
$k_2=\frac{\beta}{1+\beta}(1-\sigma)Ak_1^\sigma$ (Diamond, Romer cap. 2). The diagram and
the logic are the same.

**2.f.** The law of motion is Solow's equation (2) with $\delta=1$ (full depreciation) and
$n=0$: $k_{SS}$ above is eq. 9 with $s=\beta/(1+\beta)$. The difference that matters is
that Solow **assumes** $s$, while here $s$ **comes from optimisation**: patience pins it
down, and log utility makes it constant and independent of $r$. That microfounds Solow's
fixed saving rate (Kurlat ex. 9.12). Against 2.b, the equilibrium saving rate equals the
golden rule only if $\beta/(1+\beta)=\sigma$. The competitive equilibrium does not maximise
steady-state consumption. If $\beta/(1+\beta)>\sigma$ it over-accumulates
($k_{SS}>k_{GR}$, dynamic inefficiency is possible with finite lives).

### Q3 — Benigno (2015) AS-AD (Aulas 8-9)

AD in $(y,p)$: $y=\bar y+(g-\bar g)-\sigma i+\sigma\bar p-\sigma p-\sigma\ln\beta$ (slope
$-1/\sigma$). AS: $p=p^e+\kappa(y-y_n)$. The long-run output is
$\bar y=\frac{1+\eta}{\sigma^{-1}+\eta}\bar a+\frac{\sigma^{-1}}{\sigma^{-1}+\eta}\bar g-\frac{1}{\sigma^{-1}+\eta}\bar\mu$.

**3.a.** Initial point $E_0$: AD$_0$ ∩ AS at $(y_n,p^e)$. News of a higher **long-run**
markup lowers $\bar y$ by $d\bar\mu/(\sigma^{-1}+\eta)$. Households expect lower permanent
income and cut consumption today (Euler), so **AD shifts left**. $y_n$ depends on the
**current** $\mu$, which has not moved, so **AS stays put**. Solving:
$dy=\frac{d\bar y}{1+\sigma\kappa}<0$ and $dp=\frac{\kappa\,d\bar y}{1+\sigma\kappa}<0$.
The output gap $y-y_n<0$ opens: a demand-driven recession. Flexible-price firms cut prices;
preset-price firms keep $p^e$ and produce what is demanded.

**3.b.** Price stability means keeping $p=p^e$. On AS that requires $y=y_n$, so AD must be
moved back: **cut** $i$ by $\frac{d\bar y}{\sigma}=-\frac{d\bar\mu}{\sigma(\sigma^{-1}+\eta)}$.
Raising $i$ would deepen the recession and the fall in prices. Cost: none in terms of the
gap $y-y_n$, because a pure demand shock carries no trade-off (the divine coincidence). What
remains is not curable by monetary policy: $y_n<y_e$ (the markup wedge), and $\bar y$ is
lower for good. Caveat: if $i$ is near zero, the cut may be infeasible (ZLB, §9).

**3.c.** Use AS to write $p-p^e=\kappa(y-y_n)$ inside the loss:
$L=\tfrac12(y-y_e)^2+\tfrac{\phi\kappa}{2}(y-y_n)^2$. The CB controls AD through $i$, so it
picks the point on AS: $dL/dy=0$:
$$(y-y_e)+\phi\kappa(y-y_n)=0\iff\boxed{(y-y_e)+\phi(p-p^e)=0},\qquad y^\ast=\frac{y_e+\phi\kappa y_n}{1+\phi\kappa},\ p^\ast=p^e+\kappa(y^\ast-y_n).$$
The rate that delivers it comes from AD:
$i^\ast=\frac{\bar y+g-\bar g-y^\ast}{\sigma}+\bar p-p^\ast-\ln\beta$. News of a higher $\bar\mu$
moves neither $y_e$ nor $y_n$, so $(y^\ast,p^\ast)$ does not move. The CB fully offsets the
AD shift, $di^\ast=d\bar y/\sigma<0$, **for any $\phi$**. Role of $\phi$: it fixes where on
AS the economy sits. With $\phi\to\infty$ it sits at $(y_n,p^e)$ (strict price stability);
with $\phi=0$ at $y_e$, with $p>p^e$. Graph: the loss ellipse is tangent to AS at $O$; AD
shifts left and the cut brings it back through $O$.
