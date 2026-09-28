# Plan: diagnose Listas 2, 3, 6; close companion gaps; two mock exams

Date: 2026-09-26. Request: analyse the graded lists and the NotebookLM audio prompts to find
knowledge gaps, build mock exams from all seven lists with detailed solutions, build the
missing interactive companions, link them in the notes, add figures to the notes.

## Inputs already established

- Listas 1 and 4 were diagnosed in `Map/avaliacao-listas-1-4.md`. New scans, not yet read by
  the project: `Listas/correções/Lista+2+Macro.pdf`, `Lista+03+Macro.pdf`,
  `Lista+06+-+Pedro+Alves.pdf` (no text layer, read as images on 2026-09-26).
- The 23 NotebookLM audio files are **prompts**, not transcripts. "Evaluating the audio" means
  checking which diagnosed gap each prompt's thesis covers, and which gap none covers.
- Exam format: `rules/00_estilo_avaliacao.md` + template `Listas/lista-exam.tex`
  (4 blocks x 25 pts; each block = objective Q (2 MC x 3 + 2 T/F x 2) + discursive Q (3 x 5)).
- Output language English (global rule outranks the project's pt-BR); the professor's lists
  are in English anyway.

## Deliverables

1. `Map/avaliacao-listas-2-3-6.md`: scorecard and item-by-item diagnosis of the three new
   corrections, a consolidated gap table over Listas 1-4, 6 (Lista 5 and 7 not graded yet),
   and an audio-coverage column: gap -> which audio prompt addresses it, or none.
2. `Map/fig/*.svg` + `Map/fig/gap_figures.py`: one figure per major gap, embedded in the
   diagnosis note and in the derivation note where that topic lives.
3. Five companions, one per list question that has none:
   | Companion | List item | Folder | Linked from note |
   |---|---|---|---|
   | companion-unification.html | L2 Q1 (Korea) | aula-02-solow-mecanica | 05-comparative-statics.md |
   | companion-hidden-wedge.html | L2 Q2 (Gotham) | aula-03-solow-evidencias | 05-growth-accounting-and-tfp.md |
   | companion-taxes-and-limits.html | L3 Q1(d-e), Q2 | aula-04-consumo | 05-ricardian-and-constraints.md |
   | companion-frozen-capital.html | L5 Q1 | aula-06-equilibrio-geral | 01-equilibrium-as-benchmark.md |
   | companion-money-regimes.html | L6 Q1(c-d) | aula-07-moeda-inflacao | 03-equilibrium-and-neutrality.md |
   Each follows its sibling companions (shared `Map/companion.css`), is checked against a
   Python script at three control vectors, and is linked from its folder `00-index.md`.
4. Two mock exams, `Simulados/simulado-01.tex`, `simulado-02.tex`, each covering all four
   blocks, questions chosen so that every diagnosed gap is tested at least once across the
   pair. Each compiles to a blank exam and a solution+rubric PDF. Solutions keep every
   derivation step and arithmetic line; each question names the gap it targets. Numbers
   verified by `Simulados/simulado_codigo/check_simulado_0{1,2}.py`, which asserts.
5. Index updates: `Map/00_indice.md`, `Map/cobertura.md` rows for the new files.

## Verification

- Companion checks: each script prints the three control vectors and exits non-zero on mismatch.
- `pdflatex` twice per mock; `pdffonts` shows only Type 1 fonts.
- Gap figures: script runs clean, SVGs open.

## Delegation

Five companion agents and two mock-exam agents in parallel; the diagnosis note, the figures
and the index updates are done in the main loop.
