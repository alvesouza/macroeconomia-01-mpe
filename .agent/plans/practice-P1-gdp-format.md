# practice-P1-gdp: solutions to the §4 equation/notation/layout format

Goal: rewrite only the `sol` bodies of `Listas/practice-prova01/practice-P1-gdp-block{1,2,3}.tex`
to rules/00_estilo_avaliacao.md §4 (numbered + cited equations, Notation list, one operation per
display), model `Prova/prova-01-solution.tex`. Numbers, statements, rubrics, refs unchanged.

Steps
1. Master + gabarito: add `notacao` environment after `\input{../practice-preamble}`.
2. Q1 states the four identities once as tagged (G1)-(G4) (`q1:G1`..`q1:G4`); later questions cite
   them and say so in their Notation list. Labels `q<N>:...`, unique.
3. Per question: Notation list; each inline arithmetic chain -> display (`align`, `\label` on lines
   cited later, `\nonumber` otherwise); a sentence citing the source before each display. Tables kept.
   Word-only questions (Q5, Q6) get a Notation list only.
4. Build both PDFs with own jobnames (2x each), check logs (no `!`, undefined refs, multiply defined,
   Overfull), pdffonts Type 1, blank PDF has no solution text, run the check script, render 2-3
   answer-key pages to PNG and inspect.
