# Plan: practice-P1-growth-ge solutions to the §4 equation/notation/layout format

Target: `Listas/practice-prova01/practice-P1-growth-ge*.tex`. Model: `Prova/prova-01-solution.tex`.

1. Master and gabarito: add `notacao` environment after `\input{../practice-preamble}` (not in the shared preamble).
2. Rewrite only the `sol` bodies, block by block (Q1-Q4, Q5-Q8, Q9-Q10):
   - open each with `\begin{notacao}`; define new symbols where they first appear;
   - number every equation a later step uses, labels `qN:name`, cite with `\eqref`;
   - displays (`align`, `\nonumber` on intermediate lines) instead of inline chains, one operation per line;
   - `\passo{title}{lead sentence}` followed by the display outside the macro argument.
3. Untouched: statements, points, numbers, rubric substance, refs, tables, every pgfplots `coordinates {...}` list
   (the check parses them by position, so no new `coordinates` lists may be added before or between them).
4. Build blank + gabarito with own jobnames (twice each); grep logs for `!`, undefined/multiply defined, Overfull;
   `pdffonts`; blank PDF text has no solution text; run the check; render 2-3 answer-key pages to PNG.

## Addendum: rule 4 (substitution shown in place)

5. In every `sol` body, wherever a step substitutes (x) into (y) and jumps to the simplified result, insert the
   receiving equation with the substituted expression in parentheses as its own `\nonumber` line (convert `\[...\]`
   or single `equation` to `align`/`align*` where needed); numeric evaluations show the numbers in place first.
   No statement, number, result, label, rubric, ref or `coordinates` list changes. Rebuild and verify as in step 4.
