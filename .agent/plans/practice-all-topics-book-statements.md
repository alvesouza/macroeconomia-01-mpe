# practice-all-topics: reproduce book statements

Rule: `rules/00_estilo_avaliacao.md` §5 "Book questions used in a list or mock exam".

Book-based questions: B1 Kurlat 1.3 (pp.28-29), B2 Kurlat 4.2 (pp.72-73), B3 Kurlat 5.4 (pp.94-95),
B4 Kurlat 6.4 (pp.122-123), B5 Kurlat 7.3 (pp.147-148), B6 Kurlat 9.11 (p.185), B7 Kurlat 11.6
(pp.219-221, items (a)-(j) of (a)-(u)); B8 Benigno §4.1-4.4 (pp.507-509), B9 Benigno §8 (pp.514-516).

1. Kurlat headers: points + `\textit{Source: ... --- reproduced verbatim ...}`; verbatim stem and items from
   the PDF (printed page = PDF page) before `\resolespaco`. List instructions that were in the old header
   move under `\textit{Added parts (not in the book):}` (or "Added to the book's items").
   Cross-references to other exercises/equations get a bracketed note marked as ours.
2. Benigno headers: `\textit{Source: built on Benigno ... the statement below is ours.}` + one quoted
   sentence with page (PDF page = printed - 502). Items unchanged.
3. Solutions, MC keys, checks unchanged.
4. Verify: pdflatex x2 per master (own jobnames), clean logs, pdffonts Type 1, no "??", blank PDF has no
   solution text, both checks pass, Fructus table in PDF text matches check-a data, visual check.
