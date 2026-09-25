# Plan — derivation layer for all nine sessions

Goal: one directory per session, `Map/aula-NN-<slug>/`, holding math-dense interconnected
notes that show every undergraduate and graduate step. Precedent and density target:
`Map/benigno/` (10 notes, every Lagrangian and log-linearisation in full) and
`Map/derivacoes-cap-09.md`.

Scoping answers (2026-09-17): layout = `Map/aula-01..09/`; depth = 5-8 notes per session at
Benigno density plus a runnable check script per session; complementary books enter as
(a) contrast boxes where they differ from Kurlat, (b) derivations Kurlat omits, (c) data and
calibration magnitudes with source and page. Language = English (global rule outranks the
project pt-BR default; the `Map/benigno/` set already follows it).

## Division of labour between layers

| Layer | File | Role |
|---|---|---|
| Statements | `rules/01..09` | results, traps, formulas — loaded as agent context, stays compact |
| Derivations | `Map/aula-NN-*/` | this plan — every step, never loaded wholesale |
| Solutions | `Resolucao/` | the textbook exercises worked |

Rule: a derivation note never restates a whole rules file; it links `[[0N_slug]]` and derives.
No exercise statement is ever reproduced — number and page only (project scope lock).

## Directories and contents

| Dir | Aula | Source | Notes |
|---|---|---|---|
| `aula-01-mensuracao` | 1 | Kurlat 1-2 | GDP three ways; real vs nominal and index theory; price indices and bias; cross-country comparison (PPP); welfare beyond GDP |
| `aula-02-solow-mecanica` | 2 | Kurlat 3, 4.1-4.2 | growth facts and the Kaldor list; the Solow ODE/difference equation; steady state and stability; comparative statics; **Romer contrast**: continuous time |
| `aula-03-solow-evidencias` | 3 | Kurlat 4.3-4.5, 5 | Golden Rule; labour-augmenting progress and the balanced path; convergence speed by log-linearisation (**Romer**); growth accounting and TFP (**Jones**); the evidence chapter |
| `aula-04-consumo` | 4 | Kurlat 6 | two-period problem; Euler and the EIS; permanent income and annuity value; Ricardian equivalence; borrowing constraints; uncertainty and precaution |
| `aula-05-trabalho` | 5 | Kurlat 7 | measurement identities; static consumption-leisure; income vs substitution and the balanced-growth restriction; Frisch vs Marshallian elasticities; search and the Beveridge curve |
| `aula-06-equilibrio-geral` | 6 | Kurlat 9 | absorbs and links `derivacoes-cap-09.md`; two-period GE; infinite horizon; First Welfare Theorem; phase diagram |
| `aula-07-moeda-inflacao` | 7 | Kurlat 10-11 | money demand (Baumol-Tobin); equilibrium and neutrality; Fisher; steady states and the elasticity; seigniorage and the inflation tax; **Jones cap. 8** and **Romer cap. 11** contrasts |
| `aula-08-adas-micro` | 8 | Benigno 1-5 | index note only; links `benigno/01..04` |
| `aula-09-adas-politica` | 9 | Benigno 6-12 | index note only; links `benigno/05..10` |

Each directory: `00-index.md` (reading order table, notation, what the session settles) plus the
numbered notes, plus `check_<topic>.py` asserting the session's closed forms against an
independent numerical path, in the style of `Map/benigno/check_multipliers.py`.

## Order

aula-01 -> 02 -> 03 -> 04 -> 05 -> 06 -> 07 -> 08/09 index notes -> `Map/00_indice.md` rows.

Sessions are delivered one at a time; each is complete and verified before the next starts.

## Status — COMPLETE (2026-09-20)

| Dir | Notes | Companions | Check script |
|---|---|---|---|
| `aula-01-mensuracao` | 5 | 4 | `check_measurement.py` PASS |
| `aula-02-solow-mecanica` | 5 | 2 | `check_solow.py` PASS |
| `aula-03-solow-evidencias` | 5 | 2 | `check_growth.py` PASS |
| `aula-04-consumo` | 5 | 2 | `check_consumption.py` PASS |
| `aula-05-trabalho` | 5 | 2 | `check_labour.py` PASS |
| `aula-06-equilibrio-geral` | 2 + links to `derivacoes-cap-09` | 1 | `check_ge.py` PASS |
| `aula-07-moeda-inflacao` | 4 | 2 | `check_money.py` PASS |
| `aula-08-adas-micro` | routing note -> `benigno/` | (4 in `benigno/`) | `check_multipliers.py` PASS |
| `aula-09-adas-politica` | routing note -> `benigno/` | (shared) | `check_multipliers.py` PASS |

Totals: 33 new derivation notes, 15 companions, 7 new check scripts, all 8 passing.
`Map/companion.css` promoted to `Map/` and shared by every companion.

Carried-over quizzes are done: `Simulados/quiz-aula-08-microfundamentos-2026-09-19.md` and
`Simulados/quiz-aula-09-politica-2026-09-19.md`, both PASS `.claude/quiz-validate.py`.

### Claims corrected while writing, because a check failed

1. **Substitution bias** is a statement about the sign of $\operatorname{Cov}_s(\hat p,\hat q)$,
   not about "demand slopes down" — with idiosyncratic demand shifts the Laspeyres-Paasche
   ordering reverses. `check_measurement.py` now verifies the criterion in both directions.
2. **Development accounting**: the $K/Y$ form takes $h^{1}$, not $h^{1-\alpha}$. Fixing that
   moved the TFP share from 51% to 60% — the Hall-Jones number. Note 05 of aula-03 now states
   both decompositions and says the answer moves ten points on the choice.
3. **Intertemporal labour supply**: more impatience shifts work toward the **future**, not the
   present, because future disutility is discounted by beta. Note 04 of aula-05 corrected.
4. **Velocity** rises when trips get cheaper; my test asserted the opposite sign.
5. **The transitory MPC** is the annuity factor, which equals $1/T$ only as $r\to0$; at
   $r=4\%$, $T=40$ it is 0.049, nearly twice $1/T$. Note 04 of aula-04 corrected.
6. The exact discrete Solow law has break-even $\delta+n+g+ng$, so its steady state sits 0.35%
   below the continuous-time closed form.

## Carried over from the Benigno set — CLOSED

Everything in `.agent/plans/benigno-2015-explainer-set.md` is done: the ten derivation notes,
`check_multipliers.py`, the narration (`Leituras/benigno-2015-adas-narrated.txt`), the seven
NotebookLM prompts (87/87 pass), the `rules/08` eq. (15)/(19) coefficient fix, the
`Map/00_indice.md` row, and the two quizzes above.
