# Kurlat ch. 7, 10-11 solutions + Ljungqvist & Sargent solutions

## Kurlat (in scope)
1. **Ch. 7** — write `Resolucao/kurlat_solutions_ch07.tex` (7.1-7.7) against the existing,
   verified `kurlat_ch07_codigo/` and `fig/fig_k7_*`. Same preamble/boxes as `kurlat_solutions_ch09.tex`.
   Any exercise not covered by `ch07_numerico.py` (7.4) gets a check added.
2. **Chs. 10-11** — `kurlat_ch10-11_codigo/` (`ch10_11_numerico.py` asserting every formula by an
   independent route, `ch10_11_figuras.py` with pgf backend) + `kurlat_solutions_ch10-11.tex`
   (10.1-10.5, 11.1-11.9). Cagan demand (11.6) is in scope.
3. Compile with pdflatex; `pdffonts` must show Type 1 only. Update `Map/cobertura.md` table.

## Ljungqvist & Sargent (outside course scope — user request overrides)
Scope (user, 2026-09-27): **every chapter, in order**, starting at ch. 2, two chapters per batch.
Per chapter N: `Resolucao/ljungqvist_sargent/ls_solutions_chNN.tex` (Kurlat box style,
analytical) + `ls_chNN.ipynb` for computational exercises (executed, outputs saved).
The `.md` conversion garbles math — read exercise statements from the PDF pages.
Progress ledger: `Resolucao/ljungqvist_sargent/README.md` (chapter, exercises, status).

## Verification
- `python ch0N_numerico.py` exits 0; notebooks run end to end (`jupyter nbconvert --execute`).
- PDFs compile with no undefined refs; fonts Type 1.
