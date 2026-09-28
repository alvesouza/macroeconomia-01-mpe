# Plan: Ljungqvist & Sargent ch. 5 solutions

Chapter 5 (LQ dynamic programming) has 14 exercises, printed pp. 145-155 (PDF = printed + 39).

1. Analytical: 5.1 Riccati with cross term; 5.2 (5.2.10)-(5.2.11) = evaluation + improvement, monotone, fixed point = ARE;
   5.5 closed form G(I-bA)^{-1}; 5.6 Lyapunov + trace constant, finiteness |root| < b^{-1/2};
   5.7 second-order difference eq. in p, roots, minimal p0, Laffer; 5.8 LQ + closed form at q=beta (taxes martingale,
   w1,w2 drop out), VAR via Kalman innovations; 5.9 LQ mapping, certainty equivalence, Kalman likelihood, MH posterior;
   5.10 Lyapunov value of prescribed rule, Howard -> Hall PIH; 5.11/5.12 LQ firm, Euler closed form;
   5.13/5.14 PIH, eps>0 regularisation vs eps=0 (P=0 Ponzi vs stabilising solution).
2. Notebook `Resolucao/ljungqvist_sargent/ls_ch05.ipynb`: shared olrp (Riccati iteration, cross term),
   scipy DARE, Howard policy iteration, Lyapunov; one section per exercise; asserts by independent route
   (DARE vs iteration vs PI; closed form vs LQ; Monte Carlo; Kalman loglik vs direct Gaussian density).
   Figures fig/ls05_*.pdf, pdf.fonttype 42. Execute in place.
3. `ls_solutions_ch05.tex` mirroring ch03 preamble/boxes; pdflatex x2; pdffonts; clean aux.
4. Append Chapter 5 row to README (do not touch other rows).
