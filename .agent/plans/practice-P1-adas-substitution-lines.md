# practice-P1-adas: rule 4 (every substitution on its own line)

Scope: solutions in `Listas/practice-prova01/practice-P1-adas-block{1,2,3}.tex`. Statements, numbers, results, figures,
rubrics, labels and references unchanged.

1. For each step that substitutes a non-zero expression into an equation and jumps to the simplified result, insert one
   `\nonumber` line with the receiving equation and the substituted expression in parentheses (convert a lone
   `equation` to `align`, label kept on the final line).
2. Where the existing first line already is the substituted equation without parentheses, add the parentheses in place.
3. Not expanded: setting variables to zero ("put di=...=0 in (M)"), numeric plug-ins already displayed with the numbers
   in place, and pure algebraic operations (subtract, collect, divide), which are rule 3, not rule 4.
4. Build blank and answer key twice each with own jobnames; grep logs; pdffonts; no "??"; blank has no solution text;
   run the check script; render 2 answer-key pages.
