# Plan: Ljungqvist & Sargent ch. 6 solutions (Search and Unemployment)

27 exercises, 6.1-6.27, printed pp. 204-222 (PDF +39).

1. Notebook `Resolucao/ljungqvist_sargent/ls_ch06.ipynb`: helpers (McCall reservation wage by bisection on (6.3.3),
   generic VFI, pgf `save_pdf`), one section per exercise, each number checked by an independent route
   (closed-form equation vs VFI vs policy iteration vs Monte Carlo) with `assert`. Figures `fig/ls06_*.pdf`.
2. `ls_solutions_ch06.tex`: ch03 preamble/boxes; exercises grouped by topic:
   McCall variants (6.1-6.5, 6.7, 6.8, 6.12, 6.13); finite horizon and MPS (6.9, 6.10, 6.20, 6.21);
   time-varying reservation wages (6.14-6.16); quits/firing/promotion/human capital/Markov wages (6.22-6.25);
   effort and externalities (6.6, 6.11, 6.18); computation and bandits (6.19, 6.17); Neal (6.26, 6.27).
3. Misprint to flag: 6.18 law of motion x' = g(x phi) - delta x (read as (1-delta)x + g).
4. pdflatex x2, pdffonts, clean aux; README row for ch. 6 after ch. 5 row.
