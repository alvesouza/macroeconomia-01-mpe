# Plan: practice-all-topics blocks 1-5 solutions to the §4 equation/notation/layout format

Target: `Listas/practice-prova01/practice-all-topics-block1..5.tex` (Q1-Q15). Model: `Prova/prova-01-solution.tex`.
Blocks 6-9, the master and the gabarito copy belong to another agent; not touched here.

1. Edit only `sol` bodies (one Edit per `sol`): open with `\begin{notacao}` (one item for MC); number every
   equation a later step uses, labels `bBqN:name` (global question number), cite with `\eqref`;
   statement equations restated in the first solution of the question with their own labels;
   `\passo{title}{lead sentence}` then the display outside the argument; `align*` for uncited steps.
2. Untouched: statements, points, numbers, MC keys, rubrics, refs, tables, the pgfplots figure of Q5(b).
3. Verify: `python practice-all-topics-check-a.py`; scratch wrapper `_fmt-a.tex` (blocks 1-5, `\solucoestrue`),
   pdflatex twice with `-jobname=_fmt-a`; logs free of `!`, undefined/multiply defined refs, Overfull;
   render 2-3 pages to PNG in the scratchpad; delete `_fmt-a*`.
