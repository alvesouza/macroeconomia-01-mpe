# Plan: Simulado 5 solutions to the §4 equation/notation/layout format

- Target `Simulados/simulado-05.tex`; model `Prova/prova-01-solution.tex`.
- Preamble: add `notacao` environment (copied from Prova 01) and `\allowdisplaybreaks`.
- Statements: only tags for citation. Q1 Part B: production and law of motion displayed as (S1), (S2).
  Q2: utility, technology, budget displayed as (U), (F), (BC). Q4: existing displays tagged
  (AD), (AS), (YN), (YE); the loss displayed as (LF). Tags (not counter numbers) so the exam and the
  solutions builds show the same labels.
- Solutions: each of the 14 `sol` blocks rewritten: Notation list first (full in the first item of a
  question, new symbols only later), numbered equations with `qXy:` labels, `\eqref` at each step,
  one operation per displayed line. Figures, Intuition, Ref, rubric and Gap text kept verbatim
  (spliced by placeholder from the original file). No number or result changes.
- Method: new blocks in the scratchpad, spliced by a Python script (no sed/heredoc on LaTeX).
- Verify: both PDFs (per-job cut files), logs clean, pdffonts Type 1, exam has no solution text,
  check_simulado_05.py passes, PNG render of 2-3 solution pages.
