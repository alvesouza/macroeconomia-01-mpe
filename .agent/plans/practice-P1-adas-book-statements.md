# practice-P1-adas: reproduce source statements

Rule: `rules/00_estilo_avaliacao.md` §5 "Book questions used in a list or mock exam".
Models: `practice-P1-growth-ge-block1.tex`, `practice-all-topics-block8.tex` / `-block9.tex`.

Sources (text taken from the PDFs):
- Lista 7 (`Listas/MPE_Macro1_2026_Lista7.pdf`, 1 page, English text): Q2 stem + (a) + closing paragraph; Q4 whole.
- Carlin & Soskice (2024) §3.6.1 checklist Q4-Q5, printed p.156 = PDF p.180 (offset +24).
- Benigno (2015): printed page = PDF page + 502. §6.1-6.2 p.512 (PDF 10), §6.3 p.513 (PDF 11),
  §7 pp.513-514 (PDF 11-12), §11 pp.521-523 (PDF 19-21).

Classification:
- Q1 (§6.1-6.2), Q2 (§6.3 + markup analogue): Benigno-built; source line "no exercises; statement ours",
  one quoted sentence, sign reversal / added (b) flagged.
- Q3: Lista 7 Q2(a) verbatim (item (a) only; points label omitted), then Benigno §7 line; sign reversed,
  items (a)-(c) are this list's -> flagged.
- Q4: Lista 7 Q4 verbatim + C&S checklist Q4-5 verbatim + Benigno §11 sentence; items (a)-(c) are this
  list's, answering them in Benigno's notation -> flagged.
- Q5-Q10 (blocks 2-3): created by this list (no book exercise behind them); untouched, as in the models.

Steps: edit block1 headers only (statements before first `\resolespaco`); update master comment line
"cited by section and page only" in both masters. Solutions unchanged.
Verify: pdflatex x2 each master (own jobnames), clean logs, pdffonts Type 1, no "??", blank PDF has no
solution text, check passes, render statement pages, `\needspace` if a source line splits from its text.
