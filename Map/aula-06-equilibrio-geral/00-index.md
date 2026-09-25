---
tags: [map, aula-06, equilibrio-geral, tbe, derivacoes, kurlat]
date: 2026-09-19
---

# Aula 6 — General equilibrium

**Source.** Kurlat (2020), chapter **9**, printed pages 165–190.

**Read this first.** The equation-by-equation derivation of this chapter already exists and is
complete: [[derivacoes-cap-09]] walks all **33 numbered equations** of Kurlat ch. 9 — where each
one comes from, which assumption enters, what cancels, who proposed it and what the trap is. It
is the primary document for this session and nothing here repeats it.

This directory adds the three things that file does not carry: the two **organising ideas**
stated separately from the equation walk, a **runnable check** of the chapter's closed forms,
and an **interactive phase diagram**.

---

## Reading order

| # | What | Where |
|---|---|---|
| 1 | The 33 equations, one by one | **[[derivacoes-cap-09]]** — Parts 0 to VI |
| 2 | What competitive equilibrium buys, and why the prices cancel | [[01-equilibrium-as-benchmark]] |
| 3 | The infinite-horizon dynamics, the saddle path, and why it is not Solow | [[02-dynamics-and-saddle-path]] |

If you are short of time, the ordering that works is: Part 0 of [[derivacoes-cap-09]] for the
map, then [[01-equilibrium-as-benchmark]] for the idea, then Parts I–III of
[[derivacoes-cap-09]] for the algebra, then [[02-dynamics-and-saddle-path]].

Runnable check: `check_ge.py`. It verifies that the five first-order conditions collapse to the
two the planner would have written, solves the planner's problem numerically and confirms the
allocations coincide, checks Walras' law on a perturbed price vector, reproduces the
steady-state conditions, and confirms that the saddle path is the only non-explosive trajectory.

## Interactive companion

| Companion | Drives |
|---|---|
| [The Saddle Path](companion-phase-diagram.html) | the $\dot k=0$ and $\dot c=0$ loci, the two unstable arms, and the knife-edge trajectory that the transversality condition selects — with the Golden Rule marked for comparison |

---

## What this session is for

Sessions 2 and 3 had a mechanical saving rate. Session 4 gave the household a saving decision
but took the interest rate as given. Session 5 gave it a labour decision but took the wage as
given. **Nothing so far has determined a price.**

This session closes that. Households choose, firms choose, and prices adjust until every market
clears simultaneously. The interest rate stops being a parameter and becomes an equilibrium
object — which is the prerequisite for every policy question in sessions 7 to 9, because a
policy that moves a price is meaningless in a model where prices are exogenous.

The chapter's architecture, in the sentence [[derivacoes-cap-09]] Part 0 uses: *three independent
optimisation problems are set up, five first-order conditions containing prices are extracted,
the conditions are combined until the prices **cancel**, and what survives is proved to be
exactly what an omniscient planner would have written without ever seeing a price.*

## The two results, and where they are broken later

**1. The price system aggregates information no one has.** The decentralised economy reaches the
planner's allocation without anyone computing it. This is the First Welfare Theorem, proved in
[[derivacoes-cap-09]] Part III via the two inequalities (9.2.2) and (9.2.3).

**2. It is a benchmark, not a description.** The theorem needs complete markets, price-taking,
no externalities and no distortions. Every later session violates one of them on purpose:

| Session | What is broken | Consequence |
|---|---|---|
| [[07_moeda_inflacao]] | money is held despite being dominated in return | the model needs a friction to explain money at all |
| [[08_adas_microfundamentos]] | **price-taking** — firms have market power, mark-up $\mu>0$ | natural output falls below efficient output; see [[03-natural-and-efficient]] §3.4 |
| [[08_adas_microfundamentos]] | prices cannot adjust for a fraction $\alpha$ of firms | the allocation is not even the flexible-price one |
| [[09_adas_politica]] | trade-offs and a role for stabilisation policy | the whole of Aula 9 exists because the theorem fails |

**Read the sessions in that order and the course has a spine:** build the frictionless benchmark,
prove it is efficient, then introduce exactly one friction at a time and watch a policy problem
appear. Without session 6 the mark-up in session 8 is a parameter; with it, the mark-up is the
measure of how far the economy sits from an allocation that has been *proved* optimal.

## Where the algebra reappears

The Euler equation (9.1.8) and the intratemporal condition (9.1.7) of this chapter are, with
different notation, equations (3) and (7) of Benigno (2015) — see [[01-household-and-ad]] §1.2.
The firm's first-order conditions (9.1.9)–(9.1.10) are the factor-price conditions of
[[02-markets-and-factor-prices]] §2.1. And the arbitrage condition (9.1.11) is
$r=r^{K}-\delta$ from §2.4 of that note. Nothing in session 8 is new machinery; it is this
chapter with a mark-up wedge and a fraction of prices held fixed.

## Out of scope

Kurlat ch. 8 (investment, present values and risk) is outside this course, so the investment
firm of (9.1.2) is taken as given rather than motivated from asset pricing. The Second Welfare
Theorem, incomplete markets, and overlapping generations are not covered.
