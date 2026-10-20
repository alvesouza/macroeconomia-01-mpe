# Simulado 04: solutions to the §4 equation/notation format

Target: `Simulados/simulado-04.tex` (solutions only). Model: `Prova/prova-01-solution.tex`.
Rule: `rules/00_estilo_avaliacao.md` §4 "Equations, notation and layout".

1. Preamble: copy the `notacao` environment; cut file -> `\jobname.cut` (one per build).
2. Numbering: Q1 solution equations numbered (G1), (G2)... via `\theequation`; Q2 statement
   equations displayed and tagged (1)-(4), counter reset to 4 so Q2/Q3 solutions continue
   (5), (6)...; Q3 statement tagged (AD), (AS), (YN); 3.c statement (LF).
3. Each item: Notation list first (full list in 1.a, 2.a, 2.c, 3.a; new symbols only elsewhere),
   steps rewritten as numbered displays with `\eqref` citations, one operation per line.
   Labels prefixed by item (`q2c:b1`). Steps' text kept short; intuition, refs, rubrics,
   gaps, traps and figures untouched.
4. Build both PDFs twice each, grep logs, pdffonts, check exam PDF text has no solutions,
   run `check_simulado_04.py`, render 2-3 pages to PNG.

## Pass 2: rule 4 (substitution shown in place)

5. Walk every solution; wherever a step substitutes an equation, a value or numbers and jumps
   to the simplified result, insert the line with the substituted expression in parentheses
   (`\nonumber` inside the existing `align`; `equation` -> `align` when a line is added, label
   kept on the last line). Where the cited line already is the in-place form, only add
   parentheses. Statements, numbers, results, figures, rubrics untouched. Rebuild and verify
   as in step 4.
