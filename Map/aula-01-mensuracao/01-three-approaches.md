---
tags: [aula-01, kurlat-cap-01, contabilidade-nacional, valor-adicionado, derivacao]
date: 2026-09-17
---

# 1. The three approaches, and why they are the same number

**Kurlat §1.1, printed pages 15–21.** Up: [[00-index]] · Next: [[02-real-nominal-and-indices]]
· Rules: [[01_mensuracao_agregados]]

The claim to establish: production, income and expenditure are not three estimates of the
same thing that happen to agree. They are the same sum, regrouped. Once that is proved,
every accounting question in the exercise set is a question about which group a transaction
falls into.

---

## 1.1 The firm-level identity

Take firm $j$ in period $t$. Let $R_j$ be its sales revenue, $M_j$ the value of
intermediate inputs it purchases from other firms, $W_j L_j$ its wage bill, $\Pi_j$ its
profit, $D_j$ its depreciation, $T_j$ indirect taxes net of subsidies, and $I^{\text{nt}}_j$
its interest payments and rents. Accounting requires revenue to exhaust into costs, factor
payments and residual profit:

$$R_j \;=\; M_j + W_j L_j + I^{\text{nt}}_j + D_j + T_j + \Pi_j \tag{1.1}$$

Define **value added** as revenue net of purchased intermediates:

$$\mathrm{VA}_j \;\equiv\; R_j - M_j \;=\; \underbrace{W_j L_j + I^{\text{nt}}_j + D_j + T_j + \Pi_j}_{\text{payments to factors and government}} \tag{1.2}$$

Equation (1.2) *is* the equality of the production and income approaches, at the level of
one firm. Nothing has been assumed; it follows from profit being defined as the residual.
Sum over firms:

$$\boxed{\;\sum_j \mathrm{VA}_j \;=\; \sum_j\left(W_jL_j + I^{\text{nt}}_j + D_j + T_j + \Pi_j\right)\;}$$

The left side is GDP by production; the right side is GDP by income. Kurlat's income column
in Table 1.1 (p. 16) lists exactly these five items, which is why **depreciation appears as
a form of income** — an entry his own footnote 1 calls odd. It is not income accruing to
anybody. It is there because GDP is *gross*: the production measure never subtracted
depreciation, so the income measure must add it back for (1.2) to hold. Net domestic
product subtracts it from both sides.

### Why value added and not revenue

Kurlat's Example 1.2 (p. 17): a fertiliser plant sells for \$0.80 to a farmer who sells
lettuce for \$1. Summing revenues gives \$1.80, and the \$0.80 of fertiliser is counted
twice — once as itself, once inside the lettuce. Value added is \$0.80 and \$0.20, summing
to \$1, the value of the only good that left the production system.

Formally, in a chain of $n$ stages with $M_{j} = R_{j-1}$ the sum telescopes:

$$\sum_{j=1}^{n}\left(R_j - R_{j-1}\right) = R_n - R_0 = R_n \qquad (R_0 = 0)$$

**Total value added equals the value of final output.** The telescoping is the theorem; the
"avoid double counting" slogan is its consequence.

## 1.2 Expenditure, and the closing identity

Every unit of final output is bought by somebody, and the buyer is a household, a firm
accumulating capital, the government, or a foreigner. Writing $C$, $I$, $G$, $X$ for those
four and $M$ for imported goods that appear inside them:

$$Y \;=\; C + I + G + X - M \tag{1.1.1}$$

The $-M$ is not a claim that imports reduce output. It is a correction: $C$, $I$, $G$ and
$X$ are measured at purchaser prices and therefore already contain imported content, which
was not produced domestically. Subtracting $M$ removes exactly that content.

Kurlat's Example 1.6 (p. 19) is the test case and worth working, because it is the one
students get wrong. A manufacturer imports \$10 of components, uses half in a \$20 car, and
stores the rest; a gardener exports \$2 of lettuce. Then:

$$\underbrace{(20-5)}_{\text{car VA}} + \underbrace{2}_{\text{lettuce}} = 17,
\qquad
\underbrace{20}_{C} + \underbrace{5}_{I\,(\text{inventories})} + \underbrace{2}_{X} - \underbrace{10}_{M} = 17$$

The unused \$5 of components is an **inventory investment**. Without that entry the
expenditure side would read $20+2-10=12 \ne 17$. Inventories exist in the accounts precisely
to keep (1.1.1) true when production and use are not synchronised.

> **Sign trap.** An inventory *drawdown* is negative investment. Kurlat states this at p. 18:
> when Dunder Mifflin finally sells the stored paper, the sale adds to $C$ and the inventory
> change subtracts an equal amount, so GDP in the year of sale is unaffected by the sale of
> goods produced earlier. GDP records the year of *production*.

## 1.3 The four conventions that decide every exercise

Each of these is a choice, not a theorem, and each one is where an exam question lives.

**(a) Transfers are not government purchases.** Kurlat Example 1.8 (p. 20): a \$20,000
pension changes no entry in any of the three columns. The government hands over purchasing
power; nothing is produced. Only $G$ that buys goods and services enters (1.1.1). This is
trap 3 in [[01_mensuracao_agregados]] and it recurs in the fiscal-policy discussion of
[[09_adas_politica]], where the lump-sum transfer $T$ plays exactly this role: it moves
resources without moving output.

**(b) Government output is valued at cost.** Kurlat Example 1.7 (p. 20): a kindergarten
teacher paid \$85,000 and a free concert costing \$85,000 contribute identically, even
though one is attended by a class and the other by four people. There is no market price, so
input cost is used as the value of output. The consequence is that **government productivity
growth is zero by construction** in the accounts — a measurement artefact that matters for
the TFP numbers in [[03-growth-arithmetic]] and in session 3.

**(c) Durables are consumed at purchase; housing is not.** Kurlat Example 1.5 (p. 18). A
television bought for \$500 is \$500 of consumption in the year of purchase and nothing
thereafter. A house is investment when built, and then generates an *imputed* flow of
housing services every year, valued at the rent an equivalent house would fetch. The
inconsistency is deliberate and Kurlat justifies it on two grounds: housing is large (imputed
owner-occupier rent is nearly 8% of US GDP, p. 21) and long-lived, and without the imputation
measured GDP would fall whenever a renter bought their home.

**(d) Non-market production is excluded.** Kurlat Example 1.11 (p. 22): two neighbours who
pay each other \$25 generate \$50 of GDP; the same two people doing their own chores generate
zero. This is the single largest conceptual gap between GDP and welfare, and it is exactly
what the leisure term in the Jones–Klenow measure of [[05-beyond-gdp]] is built to price.

## 1.4 GDP against GNP, derived

GDP is defined by **territory**, GNP (now GNI) by **ownership of factors**. Let $F^{\text{in}}$
be factor income earned domestically by non-residents and $F^{\text{out}}$ factor income
earned abroad by residents. Then

$$\mathrm{GNP} = \mathrm{GDP} + F^{\text{out}} - F^{\text{in}}$$

The gap is large exactly where foreign ownership is large. Ireland is the standard case:
profits of foreign-owned firms are produced in Ireland (in GDP) and accrue abroad (out of
GNP), so Irish GNP runs roughly 15–20% below GDP. The HDI uses **GNP** per capita for
precisely this reason — see [[05-beyond-gdp]] §5.1 and Kurlat's footnote 1 on p. 32.

## 1.5 The stock–flow discipline

| Stock (a level, at a date) | Flow (a rate, over a period) |
|---|---|
| capital $K_t$ | investment $I_t$ |
| wealth | saving |
| government debt $B_t$ | deficit $B_t - B_{t-1}$ |
| money supply $M_t$ | money growth $\dot M/M$ |

Linked by an accumulation identity, which is the entire engine of session 2:

$$K_{t+1} = (1-\delta)K_t + I_t$$

Depreciation is the flow that converts a stock into a smaller stock, which is why Kurlat
flags at p. 21 that it "plays an important role in the theory of economic growth that we'll
study in Chapter 4". The $\delta K$ term in the Solow equation of
[[02_crescimento_solow]] is the same $D_j$ that appears in (1.2).

## 1.6 Contrast: Jones (2020), ch. 2

Jones builds the same identity but sets it up as a **circular flow** between households and
firms rather than as a telescoping sum over production stages. The two are equivalent, and
the difference is pedagogical rather than substantive, but Jones's presentation makes one
thing visible that Kurlat's does not: in the circular flow, the income approach and the
expenditure approach are the two directions of the *same* set of arrows, so their equality is
a conservation law rather than a coincidence. Jones's ch. 2 also carries the cleaner
international dataset; his growth-facts tables are the ones used in
[[02-real-nominal-and-indices]] and in session 2. Cite Jones by the **local 2020 file**, with
the +25 page offset recorded in [[books-index]].

## 1.7 What to be able to do, cold

1. Given any transaction, place it in all three columns and check that the three totals move
   by the same amount.
2. Say why the value-added sum telescopes, in one line.
3. Explain why depreciation appears on the income side of a *gross* measure.
4. Give the imputation conventions and the reason for each.
5. Compute GNP from GDP and a factor-income account.

Practice: Kurlat ch. 1, Exercises 1.1 and 1.2 (p. 26); ch. 2, Exercise 2.10 (p. 44) for the
Rawlsian difference principle, which connects to [[05-beyond-gdp]]. Worked in
[[Resolucao/kurlat_solutions_ch1-4|ch1-4]].
