---
tags: [aula-02, kurlat-cap-03, fatos-de-kaldor, crescimento, dados]
date: 2026-09-18
---

# 1. The facts a growth model has to hit

**Kurlat ch. 3, printed pages 47–51.** Up: [[00-index]] · Next: [[02-ingredients]] ·
Rules: [[02_crescimento_solow]]

A model is judged by the regularities it reproduces. This note states them with the numbers
attached, and proves the one that is not independent.

---

## 1.1 The very long run (§3.1, p. 47)

Following Maddison (2001) and Bolt et al. (2018), GDP per capita can be pushed back centuries
using indirect evidence — skeletal heights, livestock counts, crop yields, iron output — once
you anchor it with the observation that any society that did not starve was above subsistence,
which is on the order of **\$400 a year at current prices**, close to today's extreme-poverty
line.

Two facts emerge from the UK series, and they frame the whole of growth theory:

1. Even before 1800 UK GDP per capita was **above subsistence and growing slowly**. Kurlat
   flags that this is contested — some economic historians read the pre-industrial series as
   stagnant and near subsistence.
2. Something in the 19th century **accelerated** the growth rate. This is the Industrial
   Revolution, and Kurlat is careful to say there is no settled answer as to what caused it or
   why it happened in the UK first.

Other countries went through the same transition at different dates, from levels not far above
subsistence. The **date of take-off**, not the rate afterwards, is what orders countries today —
a point worth carrying into the convergence discussion of [[05-comparative-statics]] §5.5.

> **Why the charts are in log scale**, from Kurlat's footnote 1 (p. 47): a log scale converts
> proportional differences into absolute ones, so the vertical distance from 1,000 to 2,000
> equals that from 10,000 to 20,000; constant proportional growth is a straight line and its
> slope is the growth rate. That is the machinery of [[03-growth-arithmetic]] §3.5, and the
> companion [Reading a Log Scale](../aula-01-mensuracao/companion-growth.html) drives it.

## 1.2 The Kaldor facts (§3.2, pp. 48–51)

Kaldor (1957) called them *remarkable historical constancies*. Kurlat states four and checks
them on US data. Note that his list is shorter and in a different order from the six in
[[02_crescimento_solow]]; the rules file follows the conventional textbook list, this note
follows the book.

**Fact 1. The growth rate of GDP per capita is constant.**
A straight line on a log plot fits the US from 1800 to 2016 well. The rate is about **1.5% per
year**, and compounded over 216 years it makes GDP per capita about **27 times higher**.

Check that internal consistency, because it is a good use of [[03-growth-arithmetic]]:
$1.015^{216} = e^{216\ln 1.015} = e^{216\times0.014889} = e^{3.216} \simeq 24.9$. The book's
27 implies $\ln 27/216 = 0.01526$, so 1.53% — the two statements agree to the rounding. Verified
in `check_solow.py`.

**Fact 2. The capital–output ratio is constant.**
$K/Y$ has stayed near **3.2** in the US. Kurlat notes the measurement problem: the capital
stock is hard to observe and is usually built by cumulating investment net of depreciation —
the perpetual-inventory method, which Exercise 5.4 (p. 100) asks you to think through. That
method is just the accumulation identity (4.1.4) of [[02-ingredients]] run forward from a
guess, which is why the same $\delta$ appears in the data construction and in the model.

Read $K/Y=3.2$ as: the total capital the US has accumulated is what the economy produces in
3.2 years.

**Fact 3. The labour and capital shares of GDP are constant.**
Splitting income into labour (wages) and capital (corporate profits, rents, interest,
depreciation), the US labour share sat very stably at about **65%** until roughly 2000, and has
since fallen by about **3 percentage points**.

The measurement wrinkle Kurlat raises is real and worth knowing: **proprietors' income** is
ambiguous — is a small business owner's income a return to their labour or to their
investment? The common fix is to exclude it entirely, which implicitly assumes the labour–capital
split inside the proprietor sector matches the rest of the economy. Kurlat calls this "not
entirely satisfactory", and it is one reason estimates of the labour share differ across papers.

**Fact 4. The average rate of return on capital is constant.**
And here is the one that is not an independent fact. Kurlat proves it (p. 50), and the proof is
two lines:

$$\text{Return on capital} \;\equiv\; \frac{\text{Capital income}}{\text{Capital stock}}
\;=\; \frac{\dfrac{\text{Capital income}}{\text{GDP}}}{\dfrac{\text{Capital stock}}{\text{GDP}}}$$

Divide numerator and denominator by GDP. The numerator is the capital income **share**, constant
by Fact 3. The denominator is $K/Y$, constant by Fact 2. A ratio of two constants is constant.

$$\boxed{\;r = \frac{1-\text{labour share}}{K/Y}\;}$$

Put the US numbers in: $(1-0.65)/3.2 = 0.109$, so a **gross** return near 11%. Kurlat's
footnote 3 is the necessary caveat: this is gross of depreciation, because the capital income
measure includes depreciation. Net of a depreciation rate $\delta$, the return is
$r_{\text{net}} = r - \delta$, so with $\delta\simeq0.05$ the net return is about **6%** — which
is the number that should appear in any calibration, and the one that reappears as the real
interest rate in [[06_equilibrio_geral]].

Kurlat states Fact 4 separately anyway, because the time path of the return on capital is what
many growth theories are really about, so it is useful to keep in view even though it carries
no independent information.

### What the four facts jointly force on a model

They are not four unrelated targets. Taken together they say the economy travels along a
**balanced growth path**: $Y$, $K$ and $C$ all grow at the same constant rate, $K/Y$ is flat,
factor shares are flat, and $r$ is flat. That is a strong restriction, and session 3 shows it is
satisfied only by **labour-augmenting** technical progress — the Uzawa theorem result, which is
why $A$ multiplies $L$ and not $K$ in [[03_solow_evidencias]].

## 1.3 Growth across countries (§3.3, p. 51)

Kurlat's Figure 3.3.1 plots growth since 1960 against initial income. The pattern is asymmetric
and it is the pattern the model must explain:

- **Initially-rich countries** grow at rates close to one another, near the middle of the
  overall range. Low variance.
- **Initially-poor countries** show enormous variance. South Korea and Botswana grew fast enough
  to close much of the gap; Congo and Madagascar grew slowly or negatively and fell further
  behind.

Two readings, and only the second survives:

1. *Absolute convergence*, the claim that poor countries grow faster, **fails** in the world
   sample. The scatter is a cloud, not a downward line.
2. *Conditional convergence*, the claim that each country converges to **its own** steady state
   and grows faster the further below it sits, is consistent with this picture, because poor
   countries differ enormously in $s$, $n$ and institutions and therefore in $k_{ss}$.

The distinction is trap 6 in [[02_crescimento_solow]], and the formal test — a growth regression
with $s$ and $n$ on the right-hand side — is derived in session 3.

> **Contrast: Jones (2020), chs. 3–5.** Jones organises the same facts around the *ratio* of a
> country's income to US income and the distribution of that ratio over time, which makes the
> lack of absolute convergence visually obvious and shows the distribution's shape — not
> collapsing to a point, and possibly bimodal. Kurlat's growth-against-initial-income scatter is
> the standard regression picture; Jones's is the distribution picture. They answer different
> questions and both belong in an exam answer about convergence. Local 2020 file, +25 page offset
> ([[books-index]]).

## 1.4 What to be able to do, cold

1. State the four facts as Kurlat states them, with the US magnitudes: 1.5% and 27×, $K/Y=3.2$,
   labour share 65% falling ~3pp after 2000.
2. Derive Fact 4 from Facts 2 and 3 in two lines, and give the gross and net return numbers.
3. Say why proprietors' income makes the labour share hard to measure, and what the usual fix
   assumes.
4. Describe the cross-country scatter and say precisely which convergence claim it refutes.
5. Explain what a log scale does and read a growth rate off one.

Practice: Kurlat ch. 3, Exercises 3.1 *The Past is a Foreign Country* (p. 51), 3.2 *The Kaldor
Facts in Other Countries* (p. 52), 3.3 *Within-Region Convergence* (p. 52). All three are data
exercises against the Maddison and PWT databases; [[lab-data]] can fetch both offline. Worked in
[[Resolucao/kurlat_solutions_ch1-4|ch1-4]].
