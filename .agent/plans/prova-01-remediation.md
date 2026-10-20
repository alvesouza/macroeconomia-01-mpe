# Plan: Prova 01 remediation + all-topics list + mock exams

Date: 2026-10-16. Decisions confirmed by the user in one question round:
NotebookLM = **5 audio prompts, one per error cluster**, 0 slides, 0 video · lists =
**LaTeX PDF + gabarito PDF** in the practice-list style · **~8-10 exercises per topic** ·
TTS = **one script per topic**. Follow-up request: then **one practice list covering every
course topic**, then **mock exams** (defaulting to 2, Prova-01 format).

Reference for every agent: `Prova/prova-01-error-analysis.md` (diagnosis + correct solutions,
five error clusters).

## Outputs

| # | Output | Owner |
|---|---|---|
| 1 | `Listas/practice-prova01/practice-P1-gdp.tex` (+ blocks, check.py, PDF, gabarito PDF) | agent |
| 2 | `Listas/practice-prova01/practice-P1-growth-ge.tex` (same) | agent |
| 3 | `Listas/practice-prova01/practice-P1-adas.tex` (same) | agent |
| 4 | `Leituras/prova-01-{gdp,growth-ge,adas}-narrated.txt` | 3 agents |
| 5 | `NotebookLM/audio/prova-01-audio-{1..5}-<slug>.md` | agent |
| 6 | `Listas/practice-prova01/practice-all-topics.tex` (blocks Aulas 1-5 and 6-9) | 2 agents + main loop assembles |
| 7 | `Simulados/simulado-04.tex`, `simulado-05.tex` (exam + solutions PDFs, check script) | 2 agents |

## List design (per topic)

Order: Kurlat/book exercises at exam level first (cited **by number + page only**, never
reproducing statements), then harder book items, then conceptual items, then 2-3 **created**
items written in full at the end (same level or harder). Solutions in the gabarito; when a
book has an answer (instructor PSETs in `Listas/soluções do instrutor/`, Jones instructor
manual, Williamson solution manual, Romer solution manual), the solution is checked against it
and the source cited. Every numeric/symbolic result verified by a `check.py` (sympy).
Preamble: `\input{../practice-preamble}`. Fonts: lmodern+cmap, `pdffonts` all Type 1.

## Verification

- Each list: check.py passes; both PDFs compile; pdffonts Type 1.
- NotebookLM: `python .claude/notebooklm-validate.py` passes; no output-language line.
- TTS: plain text, no markdown/LaTeX; word count reported.
- Index rows: `Map/cobertura.md`, `NotebookLM/README.md`.

## Revision 2026-10-17: solution format rule

User asked that every solution (1) number equations and cite them at each step, (2) open with a
Notation list, (3) keep one operation per displayed line. Codified in
`rules/00_estilo_avaliacao.md` §4 (+ global estilo-avaliacao/macro-1, solution.md,
book-solutions.md). Model: `Prova/prova-01-solution.tex` (rewritten). Rewrite the `sol` parts of:
practice-P1-gdp, practice-P1-growth-ge, practice-P1-adas, practice-all-topics (blocks 1-5, 6-9),
simulado-04, simulado-05. Statements, results and points unchanged; check scripts still pass;
PDFs rebuilt; pdffonts Type 1.
