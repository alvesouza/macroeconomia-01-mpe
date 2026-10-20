# Plan: practice-P1-gdp, rule 4 (substitution lines)

Rule: `rules/00_estilo_avaliacao.md` §4, item 4. Targets: `Listas/practice-prova01/practice-P1-gdp-block{1,2,3}.tex` (solutions only).

1. For every computation that takes values or expressions from a cited equation or the statement,
   display the receiving equation with the substituted terms in parentheses on its own line, then the
   result on the next line (`align`/`align*`, `\nonumber` on the new lines; labels stay on the result line).
2. Inline numeric results that cite an equation (e.g. "$VA_W=300$ by (G2)") become short displays.
3. Symbolic substitutions (Q3(d): $k_{ss}$ into $y=Ak^\alpha$, $y_{ss}$ into $c_{ss}$) get the
   substituted line before the simplification.
4. No change to statements, numbers, results, tables, rubrics, references.
5. Verify: build blank + answer key (pdflatex x2, own jobnames), log scan, pdffonts, "??", blank PDF has
   no solution text, `practice-P1-gdp-check.py`, view 2 answer-key pages.
