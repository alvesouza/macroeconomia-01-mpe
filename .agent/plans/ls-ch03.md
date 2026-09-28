# Plan: Ljungqvist & Sargent ch. 3 solutions

Chapter 3 has a single exercise (3.1, Howard's policy iteration on stochastic Brock-Mirman, p. 114).

1. Derive J_h in closed form for k'=h*A k^a theta (two routes: series; undetermined coefficients).
2. Improvement step: coefficient on ln k is a/(1-ab) independent of h0 -> h1 = ab; h2 = h1; Bellman check -> optimal.
3. Contrast: VFI from v0=0 gives h_j = ab(1-(ab)^j)/(1-(ab)^{j+1}).
4. Notebook `Resolucao/ljungqvist_sargent/ls_ch03.ipynb`: closed form vs recursion/MC; numerical improvement
   step (Gauss-Hermite + minimize_scalar); discretised model VFI vs PFI; asserts. Figures fig/ls03_*.pdf (pdf.fonttype 42).
5. `ls_solutions_ch03.tex` with ch09 preamble/boxes; pdflatex x2; pdffonts; clean aux.
6. README ledger row (append if exists).
