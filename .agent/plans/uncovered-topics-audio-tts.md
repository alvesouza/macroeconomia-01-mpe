# Plan: NotebookLM audio + TTS for the topics Prova 01 did not test

Date: 2026-10-21. Scope confirmed with the user in one round:
**6 NotebookLM audio prompts, one per uncovered cluster, 0 slides, 0 video**; **one long TTS script**
(~90-120 min); content = all four groups below.

Prova 01 tested: GDP three approaches, Solow + golden rule, two-period household/equilibrium,
Benigno long-run-markup news + optimal policy (see `Prova/prova-01-error-analysis.md`).

## Clusters (one audio prompt each; the TTS has one part per cluster)

1. Measurement: price indices (Laspeyres, Paasche, chained), real vs nominal, PPP vs market rate
   and Balassa-Samuelson, beyond GDP (HDI, Jones-Klenow welfare). Kurlat chs. 1-2.
2. Growth evidence: growth and development accounting, the Solow residual/TFP, absolute vs
   conditional convergence. Kurlat chs. 3, 5.
3. Consumption: income vs substitution with CRRA (sign of dc1/dr), Ricardian equivalence and when
   it fails (credit constraints), permanent income and the MPC. Kurlat ch. 6.
4. Labour and general equilibrium: labour supply with income/substitution, taxes and transfers,
   Frisch vs Marshallian, search and the Beveridge curve; First Welfare Theorem, when it fails
   (distortionary taxes), infinite horizon and the modified golden rule. Kurlat chs. 7, 9.
5. Money and inflation: aggregates and the multiplier, Baumol-Tobin, quantity theory as identity vs
   theory, pi = mu - eta g, Fisher, seigniorage and Cagan's Laffer curve. Kurlat chs. 10-11.
6. Benigno beyond Prova 01: current productivity and markup shocks, when the divine coincidence
   fails and phi vs sigma, fiscal multiplier, ZLB and forward guidance, NK vs New Classical vs
   Keynesian. Benigno 2015 §1-12.

## Outputs

| Output | Rules |
|---|---|
| `NotebookLM/audio/uncovered-audio-{1..6}-<slug>.md` | `rules/10_notebooklm_prompts.md`; validator; no language line; rows in `NotebookLM/README.md` |
| `Leituras/uncovered-topics-narrated.txt` | `.claude/commands/speechify.md`; plain text; written in two halves (clusters 1-3, 4-6) and joined |

Avoid repeating existing material: `NotebookLM/audio/aula-*`, `gaps-audio-*`, `lista-0*`,
`Leituras/aula-07-money-and-inflation-narrated.txt`, `lista-0*-narrated.txt`. Angle: exam-style
reasoning (what a question asks, the trap, the sentence that earns the mark).

## Verification

Validator passes for all 6; TTS format check per speechify; word count reported; index rows in
`Map/cobertura.md` and `NotebookLM/README.md`.
