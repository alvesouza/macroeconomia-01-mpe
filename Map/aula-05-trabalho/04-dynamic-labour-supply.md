---
tags: [aula-05, kurlat-cap-07, substituicao-intertemporal, salario-transitorio, rbc, derivacao]
date: 2026-09-19
---

# 4. Intertemporal substitution of labour

**Kurlat §7.4, printed pages 140–142.** Up: [[00-index]] ·
Prev: [[03-elasticities-and-evidence]] · Next: [[05-search-and-equilibrium]]

The static model says a wage rise has an ambiguous effect on hours. The dynamic model says
something sharper: **it depends on whether the wage rise is temporary or permanent**, and the
temporary case is unambiguous. This is the same transitory-against-permanent logic as
[[04-permanent-income]], applied to a different margin, and recognising that is most of the work.

---

## 4.1 The two-period problem

Extend [[02-static-model]] over two periods, with the household able to borrow and lend at $r$:

$$\max_{c_1,c_2,h_1,h_2}\; u(c_1)-v(h_1)+\beta\left[u(c_2)-v(h_2)\right]$$

$$\text{s.t.}\qquad c_1+\frac{c_2}{1+r} = w_1h_1+\frac{w_2h_2}{1+r}+\pi$$

Note the specification: additively separable in consumption and labour, which as
[[02-static-model]] §2.5 warned is balanced-growth consistent only with log consumption — fine
here, since there is no growth.

Lagrangian with multiplier $\mu$ on the lifetime constraint:

$$\mathcal L = u(c_1)-v(h_1)+\beta\left[u(c_2)-v(h_2)\right]
+\mu\left[w_1h_1+\frac{w_2h_2}{1+r}+\pi-c_1-\frac{c_2}{1+r}\right]$$

Four first-order conditions:

$$u'(c_1)=\mu, \qquad \beta u'(c_2)=\frac{\mu}{1+r}$$
$$v'(h_1)=\mu w_1, \qquad \beta v'(h_2)=\frac{\mu w_2}{1+r}$$

The first pair is the Euler equation of [[02-two-period-problem]] §2.3, unchanged. The second
pair is new, and the ratio of the two labour conditions is the object of this note:

$$\boxed{\;\frac{v'(h_1)}{\beta\,v'(h_2)} = \frac{w_1}{w_2}\,(1+r)
\qquad\Longleftrightarrow\qquad
\frac{v'(h_1)}{v'(h_2)} = \beta(1+r)\frac{w_1}{w_2}\;}$$

**Read it.** The relative marginal disutility of working in the two periods equals the relative
*present-value* wage. The household works more in the period when work pays better, discounting
appropriately. This is the **intertemporal substitution of labour**.

Note that $\mu$ — the marginal utility of wealth — appears in each labour condition separately.
Holding it fixed is exactly the definition of the Frisch elasticity in
[[03-elasticities-and-evidence]] §3.1, so this is where that elasticity does its work.

## 4.2 The closed form, and the elasticity

With $v(h)=\chi h^{1+\eta}/(1+\eta)$, so $v'(h)=\chi h^{\eta}$:

$$\left(\frac{h_1}{h_2}\right)^{\eta}=\beta(1+r)\frac{w_1}{w_2}
\qquad\Longrightarrow\qquad
\boxed{\;\frac{h_1}{h_2}=\left[\beta(1+r)\frac{w_1}{w_2}\right]^{1/\eta}\;}$$

In logs:

$$\ln h_1-\ln h_2 = \frac{1}{\eta}\left[\ln\beta+\ln(1+r)+\ln w_1-\ln w_2\right]
\simeq \frac{1}{\eta}\left[(r-\rho)+\ln\frac{w_1}{w_2}\right]$$

**Three comparative statics, each worth stating.**

1. $\dfrac{\partial\ln(h_1/h_2)}{\partial\ln(w_1/w_2)}=\dfrac{1}{\eta}=\varepsilon^{F}$. The
   relative wage moves relative hours with the **Frisch** elasticity. Exactly the parameter of
   [[03-elasticities-and-evidence]] §3.2.
2. $\dfrac{\partial\ln(h_1/h_2)}{\partial r}=\dfrac{1}{\eta}>0$. **A higher interest rate raises
   current hours.** This is the mechanism that is easy to miss and it is genuinely surprising:
   working today and saving the proceeds is more attractive when the return on saving is high,
   so a rise in $r$ shifts work toward the present. It is the labour-market counterpart of the
   consumption Euler equation, and it is one of the channels through which monetary policy moves
   output in the models of session 8.
3. $\dfrac{\partial\ln(h_1/h_2)}{\partial\ln\beta}=\dfrac{1}{\eta}>0$, so $\beta\downarrow$
   (more impatience) shifts work toward the **future**, not the present — which is the opposite
   of the guess most people make, so it is worth the extra sentence. The *disutility* of future
   work is discounted by $\beta$, so a smaller $\beta$ makes working later cheap in present-value
   utility terms. The impatient household borrows to consume now and repays by working later.
   Note that this is consistent with (2): $\beta$ and $1+r$ enter only through the product
   $\beta(1+r)$, so raising $r$ and raising $\beta$ do the same thing, and $\beta(1+r)=1$ is the
   knife-edge at which hours are equalised across periods — the labour-market twin of the
   perfect-smoothing benchmark in [[02-two-period-problem]] §2.3.

## 4.3 Temporary against permanent wage changes

This is the section's payoff, and it mirrors [[04-permanent-income]] §4.1 exactly.

**A temporary wage rise: $w_1$ up, $w_2$ unchanged.**

- The relative wage $w_1/w_2$ rises, so by §4.2 the household reallocates hours **strongly**
  toward period 1.
- The wealth effect is **small**: lifetime wealth rises only by the extra earnings in one
  period out of a lifetime, and that increment is spread over the whole path.
- **Net: hours rise, and by a lot.** The response is governed by $\varepsilon^{F}$.

**A permanent wage rise: $w_1$ and $w_2$ both up.**

- The relative wage is **unchanged**, so there is no reallocation motive at all.
- The wealth effect is **large** — every period's earnings rose.
- **Net: hours change little, and can fall.** The response is governed by $\varepsilon^{M}$,
  which the log-log benchmark of [[02-static-model]] §2.4 puts at zero.

$$\boxed{\;\text{transitory wage change} \to \varepsilon^{F} \text{ (large)};
\qquad \text{permanent wage change} \to \varepsilon^{M} \text{ (small or zero)}\;}$$

**The consistency check with session 3.** A permanent wage rise is what happens along a balanced
growth path as $A$ grows — and the balanced-growth restriction of [[02-static-model]] §2.5
*requires* hours to be unchanged. So the two statements are the same statement, and the model is
internally consistent: the elasticity that is zero in the long run is large at business-cycle
frequencies, because the two questions are about different experiments.

That is the single most useful sentence in this note. It dissolves the apparent contradiction
between "a century of rising wages with falling hours" and "labour supply is elastic".

## 4.4 Why real-business-cycle models need this, and why it is contested

**The mechanism.** In an RBC model, a temporary positive productivity shock raises the *current*
wage relative to the expected future wage. By §4.3 households substitute work into the present,
so employment rises. That is how the model generates procyclical employment from a technology
shock, without any nominal rigidity, unemployment or involuntary anything.

**The requirement.** Observed employment fluctuations are large relative to observed real wage
fluctuations — the real wage is only mildly procyclical. To get big employment swings from small
wage swings, the mechanism needs a **large Frisch elasticity**, around 2–4.

**The objection.** [[03-elasticities-and-evidence]] §3.3: micro estimates for the intensive
margin are 0.1–0.3, an order of magnitude too small.

**The defence.** The Rogerson indivisible-labour argument of §3.3, reconciliation 1: the
aggregate elasticity is about the extensive margin and can be large even when every individual's
is small. A model with a participation decision and lotteries over employment behaves *as if*
the representative household had a much larger elasticity than any actual household does.

**The residual doubt.** Even granting that, the model attributes recessions to people
*voluntarily choosing* less work because the return has fallen temporarily. Whether that is a
plausible description of unemployment is the substantive objection, and it is why
[[05-search-and-equilibrium]] exists: search models produce unemployment that is not a choice
about hours.

**Scope note.** Kurlat ch. 13 is the RBC chapter and is **outside this course**. This note
records the mechanism because it is the natural use of §4.2 and because the elasticity debate is
examinable, not because the model is.

## 4.5 What this leaves out

The model above has the household choosing hours freely each period at a market wage. It cannot
produce:

- **unemployment** — everyone works their chosen hours at the going wage, so there is no such
  state as "wants to work, cannot find a job";
- **the extensive margin** as a distinct object, since $h$ is continuous;
- **duration** — the flows of [[01-measurement]] §1.3 have no counterpart here.

Those three gaps are exactly what the next note supplies, and they are the reason a course that
has just built a beautiful continuous labour-supply model immediately builds a different one.

## 4.6 What to be able to do, cold

1. Set up the two-period problem and derive all four first-order conditions.
2. Derive the relative-hours condition and its closed form under $v(h)=\chi h^{1+\eta}/(1+\eta)$.
3. Sign the effect of $w_1/w_2$, of $r$ and of $\beta$ on relative hours, and explain the
   interest-rate channel in words.
4. Contrast transitory and permanent wage changes, naming which elasticity governs each.
5. Show that this is consistent with the balanced-growth restriction rather than contradicting it.
6. State the RBC mechanism, the elasticity it requires, the objection, and the
   indivisible-labour defence.

Practice: Kurlat ch. 7, Exercises 7.6 and 7.8 (pp. 149–150). Worked in
[[Resolucao/lista4_resolucao|lista 4]] — the Kurlat ch. 7 solution set has not been written yet; the code lives in `Resolucao/kurlat_ch07_codigo/`.
