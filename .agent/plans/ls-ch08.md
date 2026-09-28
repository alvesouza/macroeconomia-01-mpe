# Plan: Ljungqvist & Sargent ch. 8 solutions

Chapter 8 (Equilibrium with Complete Markets) has 28 exercises, printed pp. 304-330 (PDF = printed + 39).

1. Analytical, grouped: 8.1-8.3 planner/decentralisation (family economics, representative consumer v_theta);
   8.4-8.7, 8.20, 8.24-8.26, 8.28 Markov pricing: q_t^0 = beta^t pi_t u'(c_t)/u'(c_0), one-step kernel
   Q_ij = beta P_ij u'(c_j)/u'(c_i), Q_h = Q^h, natural debt limits A = (I-Q)^{-1} y;
   8.5, 8.9, 8.10, 8.13, 8.27 no-aggregate-risk / corner economies (linear vs log consumers);
   8.8 tax smoothing (W'(R)=mu => constant R; Arrow position B(g) = R/(1-beta) - v(g));
   8.11-8.12 equivalent martingale measure / Harrison-Kreps; 8.14 Weill (CRRA shares, default option);
   8.15-8.19, 8.22, 8.23 heterogeneous beliefs (likelihood-ratio weights, entropy drift, recursive Pareto);
   8.21 entropy >= 0 via m log m >= m-1.
2. Notebook `Resolucao/ljungqvist_sargent/ls_ch08.ipynb`: small shared Markov toolkit (kernel, h-step kernel,
   debt limits, Perron recovery). The ch05/07 LQ toolkit does not apply (no LQ problem in ch. 8); not copied.
   Independent routes: closed forms vs brute-force history enumeration / truncated AD sums / scipy optimisation /
   budget checks; recovery by Perron root vs quadratic in beta; recursive Pareto by truncated binomial sums vs FOCs.
   Figures fig/ls08_*.pdf (pdf.fonttype=42).
3. `ls_solutions_ch08.tex` (ch07 preamble/boxes, full statements), pdflatex x2, pdffonts, clean aux.
4. README: Chapter 8 row after Chapter 7.
Parameters chosen where the book gives none are stated in the PDF next to their use.
