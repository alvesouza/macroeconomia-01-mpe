# Plan: practice-all-topics answer key -- §4 rule 4 (every substitution on its own line)

Target: `Listas/practice-prova01/practice-all-topics-block1..9.tex`, `sol` bodies only.

1. Block by block, find each step that substitutes an equation, an expression or numbers into another
   ("substituting/using/plugging (x) into (y)", or silently) and jumps to the simplified result.
2. Insert the receiving equation with the substituted expression in parentheses as its own `\nonumber`
   line (or an `align*` line), one operation per line; `\[...\]` displays become `align*` where a line is added.
   No labels added or removed, so numbering does not change.
3. Untouched: statements, numbers, results, MC keys, figures, rubrics, references.
4. Verify: pdflatex twice for `practice-all-topics.tex` and `practice-all-topics-gabarito.tex` (own jobnames);
   logs free of `!`, undefined / multiply defined refs, Overfull; `pdffonts` all Type 1; no `??` in the text;
   blank PDF has no solution text; `practice-all-topics-check-a.py` and `-check-b.py` pass; render 3 key pages.
