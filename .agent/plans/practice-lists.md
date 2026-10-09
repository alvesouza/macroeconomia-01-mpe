# Practice lists A–D and the hardest-exercises list — state as of 2026-10-07

## History
- v1 (exam standard) → `Listas/practice-intermediate/`.
- v2 (graduate) → `Listas/practice-v2-graduate/`. User: "still too simple".
- v3 (qualifier level, current) → `Listas/practice-L*.tex`, built to style guide §8 as extended
  on 2026-10-07: cross-topic discursive questions, no answer in the statement, a parameter
  analysis (proved signs, sensitivity table, limits, reading) in every discursive question,
  graphs in some sub-items (≥1 per block), five sub-items, answer key ≤ 15 pages.

## v3 content
- A: CES/new-goods price index → deflator bias → Solow residual; open-economy Solow (GNI/GDP =
  (1−α)N/Λ, creditor threshold s̄ = α(n+g+δ)/(r*+δ)).
- B: present bias with CRRA (Jensen ordering, value of commitment) + equilibrium interest rates
  with present-biased households; Prescott tax–transfer model (Laffer peak, welfare cost,
  four elasticities, α analysis).
- C: Ramsey with hours and a labor tax (implicit h(K,c) Jacobian, overshooting of hours);
  unpleasant monetarist arithmetic (S₂ = S₁ + (1+r)^T(S₀−S₁), T*, forward-looking Cagan).
- D: Benigno from primitives + taxes in the markup + oil shock diagram + rigidity analysis;
  optimal policy, ZLB, deleveraging (anchored vs constant inflation, stability bound).

## v4: symbolic conversion (user decision 2026-10-07)
- Rule: graduate lists and mock exams are symbolic by default; `/exam-gen` asks before using
  numbers (style guide §8 "Symbolic by default", exam-gen Step 3 second question).
- Numeric v3 archived (copy) in `Listas/practice-v3-numeric/`.
- Each list (A–D) converted whole, Blocks 1–3: symbols with admissible ranges; closed forms,
  conditions, signs, limits; MC options as expressions; proved sign tables replace numeric
  sensitivity tables; graphs without numeric ticks; one check script per list (sympy +
  random admissible draws). Lists split into `practice-LX-block{1,2,3a,3b}.tex` inputs.
- Done when: both PDFs build, keys 10–15 pages, Type 1 fonts, checks pass.
- Status 2026-10-08: done. Written by 16 agents (one per block piece), then one read-only
  review and one fix pass per list (fix notes in `.agent/plans/practice-L*-review-fixes.md`).
  All four: checks pass (sympy + random admissible draws, MC letters asserted), keys 15 pages,
  blank lists 7–8 pages, no overfull boxes, Type 1 only, no calibrated numbers.
  MC keys: A CADCBB, B BDCADB, C BADCAB, D DBADBC.

## Block 3 (integrative, added because each key was 7 pages; rule: 10–15 pages)
Files `Listas/practice-L*-block3a.tex` (Q5 objective), `-block3b.tex` (Q6 discursive),
`-block3-check.py`; `\input` before `\end{document}`.
- A: Hsieh–Klenow PPP investment prices; dynamic-efficiency test; Solow saving reform
  0.20→0.25 (exact Bernoulli path, CE welfare x(ρ), threshold ρ*, marginal threshold
  f'(k*)−N = modified golden rule).
- B: hand-to-mouth transfer; Jones–Klenow leisure; pension design (funded / Bismarck /
  Beveridge PAYG): ω = 1−τ(r−n)/(1+r), hours, saving → Solow, CE losses, r table.
- C: r(g,σ,β) in an endowment economy; i under money-growth vs inflation targeting (σ>1
  condition); seigniorage peak μ*; Bailey cost vs Friedman rule; σ×g table.
- D: pandemic in the borrower–saver AS–AD (supply + pessimism + deleveraging); transfer
  multiplier 1/[χ(1+ϖκ)]; policy mix vs targeting rule; χ, d₀, κ table.

## Hardest textbook exercises
- Plan: `Listas/pratica-hardest.md` (30: 16 Kurlat advanced + 14 Romer; weights by final-exam
  blocks). Solutions: Romer in `Listas/hardest-solutions.pdf` (fragments + checks in
  `Listas/hardest-parts/`); Kurlat in `Resolucao/kurlat_solutions_*.pdf` (pages in the plan).
- Romer solution manual typo found: 11.22(c) sign (π̇ᵉ > 0 outside [g₁, g₂]).

## Verification
- `Listas/practice-L*-check.py` (relative tolerance 5e-4, floor 1e-3) and
  `Listas/hardest-parts/check-*.py`: all pass.
