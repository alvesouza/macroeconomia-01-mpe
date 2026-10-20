# practice-P1-gdp: reproduce book statements

Rule: `rules/00_estilo_avaliacao.md` §5 "Book questions used in a list or mock exam". Same format as
`practice-P1-growth-ge-book-statements.md`.

Scope: block 1 Q1 (Kurlat 1.1, p.27), Q2 (Jones ch.2 Ex.2 p.39, Ex.3 pp.39-40); block 2 Q3 (Kurlat 5.8,
pp.97-98), Q4 (Kurlat 5.7, pp.96-97), Q6 (Kurlat 1.4 p.29, Kurlat 2.4 p.41, Jones ch.2 Ex.9 p.41).
Q5 and block 3 are created questions, untouched.

1. Each book-based `\questao` header: points + `\textit{Source: ...}` line (author, year, title, exercise number
   and name, pages, "reproduced verbatim", partial/changed notes). Existing "What this trains" kept.
2. Verbatim statement after it, before `\resolespaco`. Text from the PDFs (Kurlat printed = PDF page;
   Jones ch.2 printed 39 = PDF 64, offset 25, verified). Book `$` amounts typeset as `\$` (verbatim wins over
   the "no loose $" rule; it is escaped, not math).
3. Added parts marked: Q6's "Answer each in words" instruction.
4. Masters (blank and key): replace "Book exercises are cited by number and page only..." sentence.
5. Solutions unchanged. Verify: pdflatex x2 each master (own jobnames), clean logs, pdffonts Type 1, no "??",
   blank PDF has no solution text, check script passes, visual check of statement pages.
