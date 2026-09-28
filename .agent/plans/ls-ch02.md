# Plan: Ljungqvist & Sargent ch. 2 solutions

Chapter 2 has 30 exercises (2.1-2.30, printed pp. 85-104 = PDF pp. 124-143; offset +39).

1. Notebook `Resolucao/ljungqvist_sargent/ls_ch02.ipynb`, built by a script from a list of cells: one section
   per exercise; every numerical answer cross-checked by an independent route with `assert`
   (closed form vs recursion / truncated sum / simulation / DARE / joint-Gaussian brute force).
   Figures saved via `savefig(backend="pgf")` with lmodern+cmap -> `fig/ls02_*.pdf` (Type 1 fonts).
2. Execute with `jupyter nbconvert --execute --inplace`.
3. `ls_solutions_ch02.tex`: ch09 preamble/boxes verbatim, header/title adapted; grouped by topic
   (Markov chains; linear stochastic difference equations; Kalman filter; spectra; permanent income; LQ/Howard).
   Flag statement typos found (2.27e signs, 2.29 eq. (2) ordering).
4. pdflatex x2, pdffonts (no Type 3), delete aux/log/out/toc.
5. README ledger row (append if exists).
