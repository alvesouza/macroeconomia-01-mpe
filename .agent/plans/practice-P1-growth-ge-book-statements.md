# practice-P1-growth-ge: reproduce book statements

User request overrides the project rule "Nunca reproduzir enunciado de exercício" for this list.

Scope: Q1-Q7 (blocks 1-2) are book-based; Q8-Q10 are created, untouched. Block 3 untouched.

1. Each book-based `\questao` header: points + `\textit{Source: ...}` line (full citation, pages, "reproduced
   verbatim", note when items are partial/changed) + existing "What this trains".
2. Verbatim statement after the header, before `\resolespaco` (blank list) / `sol` (key): enumerate with (a)...
   Text taken from the PDFs (Kurlat printed page = PDF page; Jones p.129 = PDF 154; Romer p.97 = PDF 119).
3. List-added parts under `\textit{Added parts (not in the book):}`: Q2 (b)-(d), Q6 (f), Q7 (c). Romer keeps
   "Harder, contrast".
4. Masters (blank and key): replace "Book exercises are cited by number and page only" sentence.
5. Solutions unchanged. Verify: pdflatex x2 each master (own jobnames), clean logs, pdffonts Type 1, no "??",
   blank PDF has no solution text, check script passes, visual check of statement pages.
