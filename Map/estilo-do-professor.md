---
tags: [map, macro1, estilo, professor, correcao, avaliacao]
date: 2026-09-06
---

# The instructor's solution style — evidence from PSETs 1–4

Built from the four handwritten solution sets in `Listas/soluções do instrutor/`
(`pset 1.pdf`, `PSET 2.pdf`, `PSET 3 (1).pdf`, `PSET 4 (2).pdf`), which are **scans with
no text layer** — they were read as images.

This is the only direct evidence of the **grading function** for the final (65% of the
grade). Every other source teaches the economics; these show what he counts as a finished
answer. Feeds `/solution`, `/exam-gen`, `/exam-grade` and the `kurlat_solutions_*` series.

Back to [[00_indice]] · listening version:
`Leituras/psets-01-04-instructor-solutions-narrated.txt`

---

## 1. The six structural habits

| # | Habit | Evidence |
|---|---|---|
| **1** | **The final answer is isolated and marked** — highlighted, boxed, or double-slashed | Every numerical result and every closed form, in all four sets, without exception |
| **2** | **Causation runs through arrow chains, not prose** | PSET 1 Q4: `CP: K↓ → k↓ → y e Y↓`; `LP: K→Kss então y→y` |
| **3** | **Diagrams come in pairs** — mechanism panel + time path directly beneath | PSET 1 Q4(a) and (b); PSET 4 Q2(b) and (e) |
| **4** | **Traps are flagged in the margin** in lighter pen, prefixed `#` | 21 such notes across the four sets — see §4 |
| **5** | **Structural objects get named** with an underbrace | PSET 2: `(1+θ)^{-α}` underbraced "**wedge**"; PSET 4: "**destruição**" / "**criação**" |
| **6** | **Sign first, interpret second** — never interpret an unsigned derivative | PSET 3(c): isolates and highlights `(σ-1)/σ` → "Determines sign of ∂c₁/∂r" |

**He is not looking for paragraphs.** PSET 1 is 3 handwritten pages for 10 points, two of
them mostly diagrams. PSET 4 is 5 pages for 10 points. Length is not the signal.

---

## 2. The solution method he actually uses

### Two-period household problems: substitution, not Lagrange

PSET 3 Q1(a), verbatim structure — **he never writes a Lagrangian**:

1. Solve the period-1 constraint for assets: $a = a_0 + y_1 - \tau_1 - c_1$
2. Substitute into the period-2 constraint → $c_2$ as a function of $c_1$ alone
3. Substitute into the objective → **unconstrained** problem in $c_1$
4. Differentiate once, chain rule → Euler equation

> ⚠️ The student's own Lista 4 answer used a Lagrangian and it was accepted. But the
> substitution route is faster under time pressure and is what his own key shows.

**The denominator to memorise** — it appears in every part of PSET 3 and will reappear:

$$D \;\equiv\; 1 + \beta^{1/\sigma}(1+r)^{\frac{1}{\sigma}-1}$$

$$c_1=\frac{a_0+y_1-\tau_1+\frac{y_2-\tau_2}{1+r}}{D},\qquad
c_2=\frac{y_2-\tau_2+(1+r)(a_0+y_1-\tau_1)}{D}$$

Numerator = lifetime wealth in present value. Denominator = how it splits across periods.

### Implicit answers are acceptable

PSET 4 Q1(a) stops at $(1-n)^\gamma - bn = \dfrac{bT}{(1-\tau)w}$ and **does not solve for
$n$**. When no closed form exists, characterise and move on. Do not burn time inverting.

### Growth accounting is written with the residual decomposed

PSET 2 Q2(d): $g_Y=\alpha g_K+(1-\alpha)g_L+\underbrace{g_{\text{Solow}}}_{\text{TFP}+\Delta\theta}$
— he underbraces the residual and writes *what is inside it*.

---

## 3. Numbers and conventions

- **Decimal comma** throughout (`7,113`, `0,016667`, `92,8%`) — Brazilian convention.
- **2–4 significant figures**, no more. `82,16`, `393,62`, `0,96 p.p./year`.
- Mixes **Portuguese and English** freely: `CP`/`LP` (curto/longo prazo), `SS`, `BC`.
- Percentages given as **percentage points per year** where that is the natural unit.
- Writes $\tilde k$ for per-efficiency-unit and $k$ for per-worker without always saying which.

---

## 4. Every margin warning, and what it means

| Set | His note | What it protects against |
|---|---|---|
| 1 | "#Mesmo para y" | Drawing two identical time paths; $y$ is monotone in $k$ |
| 1 | "#Higher levels, lower SS growth, higher growth during convergence" | Collapsing three distinct objects into one |
| 1 | "$Y_t>Y_{t_0-\varepsilon}$ pois $L_t>L_{t_0}$" | **Aggregate ≠ per capita** when $n>0$ |
| 2 | "Careful with chosen base!" | Asymmetry of proportional change: −12,64% vs +14,47% |
| 2 | "capital gets dilluted at uni" | Per-worker capital falls mechanically on merger |
| 2 | "Not per capita (for S) but still a gain" | Which welfare statement you are making |
| 2 | "Workers also affected" | A capital wedge hits wages too — factors are complements |
| 2 | "$\hat A$ gets distorted…; $\hat\alpha=\alpha$ since $rk/Y$ is directly observable" | Normal factor shares ≠ no distortion |
| 3 | "Determines sign of $\partial c_1/\partial r$" | Asserting a direction you have not signed |
| 3 | "≠0 due to savings!" | The asset market transmits taxes across periods |
| 3 | "#Saving extra to pay future taxes" | The Ricardian mechanism in five words |
| 3 | "PV of taxes" | Prove RE by showing taxes enter only via $\tau_1+\tau_2/(1+r)$ |
| 3 | "#Just multiplied by $\frac{1+r}{1+r}$ what we had before" | Presenting a rescaling as a new derivation |
| 3 | "Natural debt limit (implicit)" | A limit exists even with no explicit rule |
| 3 | "Same revenue → both affordable → lump-sum welfare improving → Euler equation" | The whole DWL argument, compressed |
| 4 | "#Consumption-leisure tradeoff" | Naming the FOC |
| 4 | "Income and substitution effects + $l\leftrightarrow n$ connection" | Answer in **hours**, not leisure |
| 4 | "$\mu$ → Match efficiency → increases inflow U→E" | Define by the flow it governs |
| 4 | "BC → job creation = job destruction" | Name the economics of the SS condition |
| 4 | "#Matches increase **less**… vacancies to employment is not 1:1 → **friction**" | $\partial m/\partial V=\alpha q<q$ |
| 4 | "#Congestion externality → firm posting is better off, but **others** are harmed. Workers also benefit" | The externality lands on **others**, never on itself |
| 4 | "Shift in all $v$–$u$ values… rather than just changing how $\theta$ is split" | Shift of vs movement along |

---

## 5. ⚠️ One notation discrepancy to handle carefully

In PSET 3(c) his margin reads **"#σ { Intertemporal elasticity of substitution"**.

Strictly — and in Kurlat's own text — $\sigma$ is the **coefficient of relative risk
aversion / curvature**, and $1/\sigma$ is the **elasticity of intertemporal substitution**.
His note is loose shorthand.

**Defensive tactic:** state both once, explicitly, in any answer where $\sigma$ appears:

> "$\sigma$ is the curvature of $u$; $1/\sigma$ is the elasticity of intertemporal
> substitution."

Then no reader can mark you wrong under either convention. See the trap list in
[[topics-index#Tópico Consumo intertemporal Euler]].

---

## 6. The recurring high-value question type

In **three of four** sets, the item carrying the most weight is a **measurement or
attribution** question, not a modelling question:

| Set | Item | The question underneath |
|---|---|---|
| 1 | Q1(c), Q1(e) | Why do two *correct* measurements disagree? (base-year bias; PPP) |
| 2 | Q2(c), Q2(d) | Why does a pure distortion show up as *productivity*? |
| 4 | Q2(d) | Who bears a cost that no price registers? |

**Pattern:** build the model correctly, then ask what a competent observer with ordinary
data would *wrongly conclude*. Expect this structure on the final.

---

## 7. Checklist to apply to every future solution

Use this on `kurlat_solutions_ch07`, the Lista 5 resolution, and the final.

- [ ] Every final answer **boxed or highlighted**, findable without reading the working
- [ ] Every derivative **signed**; ambiguous ones have the deciding factor isolated
- [ ] Structural terms **named** (wedge, congestion externality, natural debt limit, MRS = MRT)
- [ ] Where population/labour force moves: **aggregate and per-capita answered separately**
- [ ] Short-run/long-run questions get **two panels** (mechanism + time path)
- [ ] Budget line under a wage tax **rotates about the no-work point**, never shifts parallel
- [ ] Implicit characterisations left implicit when no closed form exists
- [ ] Percentage changes state **which base** is in the denominator
- [ ] $\sigma$ vs $1/\sigma$ disambiguated in one explicit sentence
- [ ] The "what would an observer wrongly conclude" angle addressed where the question invites it
