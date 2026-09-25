---
tags: [map, aula-08, adas, novo-keynesiano, benigno, derivacoes]
date: 2026-09-19
---

# Aula 8 — New-Keynesian AS–AD: microfoundations

**Source.** Benigno (2015), *New-Keynesian economics: an AS–AD view*, **sections 1–5**,
printed pages 503–511.

**Read this first.** The full derivation already exists: [[benigno/00-index|the Benigno
derivation set]] carries all 35 equations of the article, every Lagrangian, every
log-linearisation and every closed form. This page is a routing note — it says which of those
notes belong to this class, in what order, and what each one settles.

---

## Reading order for this class

| # | Note | Article | What it settles |
|---|---|---|---|
| 1 | [[benigno/01-household-and-ad]] | §3, eqs. (1)–(8) | The Euler equation becomes the AD curve. Why it slopes down for a reason that is **not** the IS-LM reason |
| 2 | [[benigno/02-firms-and-as]] | §4, §4.1, eqs. (9)–(17) | Dixit–Stiglitz demand, mark-up pricing, the natural rate, and $p-p^e=\kappa(y-y_n)$ with $\kappa$ derived |
| 3 | [[benigno/03-natural-and-efficient]] | §4.2–§4.4, eqs. (18)–(19) | The planner's problem and the subtraction $y_n-y_e=-\mu/(\sigma^{-1}+\eta)$ that organises all of Aula 9 |
| 4 | [[benigno/04-equilibrium-geometry]] | §5, eqs. (20)–(21), Figs. 1–5 | Closed-form equilibrium, both slopes, the anchor points, and the natural real rate $r_n$ |

Companions: [The Three Lines](benigno/companion-as-ad.html) drives notes 3 and 4.

Runnable check: `benigno/check_multipliers.py` (it covers the whole article, including the
Aula 9 material).

Rules file: [[08_adas_microfundamentos]]. Narration:
[[Leituras/benigno-2015-adas-narrated.txt|the Benigno narration]], parts one to five.

NotebookLM prompts for this class: `aula-08-slides-1-derivation`,
`aula-08-slides-2-geometry`, `aula-08-audio-1-the-missing-lm-curve`.

---

## Why this class is the hinge of the course

Sessions 2 to 7 built a classical economy: prices flexible, money neutral, the allocation
efficient by the First Welfare Theorem of [[01-equilibrium-as-benchmark]] §1.4. Nothing in it
gives a central bank anything to do.

This class breaks that benchmark in exactly **two** places, and the discipline of knowing which
two is most of the value:

1. **Monopolistic competition.** Firms face downward-sloping demand and charge a mark-up $\mu$
   over marginal cost. This breaks the *price-taking* assumption of the welfare theorem, and it
   drives a permanent wedge between natural and efficient output.
2. **Sticky prices.** A fraction $\alpha$ of firms cannot reset prices when a shock arrives. This
   means the economy does not even reach its own flexible-price allocation in the short run.

Everything else — the household, the Euler equation, the intratemporal condition, the production
function — is **unchanged** from earlier sessions. That is worth saying explicitly, because the
article's notation makes it look like new machinery when it is not:

| Benigno's object | Where you already met it |
|---|---|
| Euler equation (3), (4) | [[02-two-period-problem]] §2.3 and §2.4 |
| Intratemporal condition (7) | [[02-static-model]] §2.2 |
| $\eta$, inverse Frisch elasticity | [[03-elasticities-and-evidence]] §3.2 |
| $\tilde\sigma$, the EIS | [[02-two-period-problem]] §2.4 |
| Mark-up pricing (11) | new — this is friction 1 |
| Sticky fraction $\alpha$ | new — this is friction 2 |
| The planner's problem (19) | [[01-equilibrium-as-benchmark]] §1.4, now as a benchmark to fall short of |

## The three things to be able to do after this class

1. **Derive the AD curve from the Euler equation** and explain why it slopes down without
   mentioning money. The trap is in [[benigno/01-household-and-ad]] §1.7, and it is the single
   most common error on this material: this model has **no LM curve and no money stock**, which
   is exactly why session 7's money-demand apparatus is not used here.
2. **Derive $\kappa$** rather than asserting it, and get the comparative statics the right way
   round — $\alpha$ is in the *denominator*, so more rigidity means a **flatter** AS curve.
3. **Subtract $y_e$ from $y_n$** and read off the criterion that organises the next class: a
   policy trade-off exists if and only if the shock moves $\mu$.

## Correction carried in the notes

The project's markdown extraction of the article renders the public-spending coefficient in
eqs. (15) and (19) as $(\sigma^{-1}-1)/(\sigma^{-1}+\eta)$. It is $\sigma^{-1}/(\sigma^{-1}+\eta)$;
the $(\sigma^{-1}-1)$ form is an OCR artefact. Three independent confirmations are given in
[[benigno/02-firms-and-as]] §2.4, and [[08_adas_microfundamentos]] has been corrected.

## Scope

Sections 6–12 of the article are [[aula-09-adas-politica/00-index|Aula 9]]. Kurlat ch. 14, which
covers similar ground with IS-LM, is **outside this course**. Nothing here uses a forward-looking
Calvo Phillips curve — footnote 7 of the article explains why, and [[benigno/02-firms-and-as]]
§2.8 records the cost of that choice.
