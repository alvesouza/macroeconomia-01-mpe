# practice-P1-adas: solutions to the §4 equation/notation/layout format

Scope: `Listas/practice-prova01/practice-P1-adas*.tex`. Solutions only; statements, points, results, figures unchanged.

1. Master + gabarito: add `notacao` env after `\input{../practice-preamble}`; turn the notation-box equations into one
   `align` with `\tag`s (AD), (AS), (YN), (YB), (YE), (LF) (same content, one per line).
2. Q1(a) builds the machine: differentiated AD/AS `q1:dAD`, `q1:dAS`, `q1:dy`, (M) `q1:M`. Later questions cite these.
   Q4 labels `q4:ystar`, `q4:dys`, `q4:dps`, `q4:di0`, `q4:di`, `q4:ddi` are cited by Q3(c), Q9, Q10.
3. Each question's first `sol` opens with a full Notation list; later items list only new symbols.
4. Displays outside `\passo` arguments; one operation per line, a sentence between displays.
5. Build both PDFs twice, grep logs, pdffonts, blank PDF free of solution text, run the check, render 2-3 pages.
