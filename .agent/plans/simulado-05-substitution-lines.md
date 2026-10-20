# Simulado 05 — apply rule 4 (explicit substitution lines)

Target: `Simulados/simulado-05.tex`, solutions only (`rules/00_estilo_avaliacao.md` §4, rule 4).

1. For every step that substitutes an equation, an earlier value, or numbers, insert the receiving
   equation with the substituted expression in parentheses as its own `\nonumber` line, before the
   simplification. Where the existing first line already is the substitution, add the parentheses in place.
2. No change to statements, numbers, results, figures, rubrics, labels or references.
3. Rebuild both jobs twice; check logs (errors, undefined refs, multiply defined labels, overfull boxes),
   `pdffonts`, "??" in text, no solution text in the exam PDF; run `check_simulado_05.py`.
