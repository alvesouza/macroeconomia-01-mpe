# Plan: Ljungqvist & Sargent ch. 11 solutions

Chapter 11 (Fiscal Policies in a Growth Model) has 20 exercises, printed pp. 449-470 (PDF = printed + 39).

1. Analytical, grouped:
   - 11.1, 11.2, 11.4: tax reforms and a capital levy (consumption tax vs lump sum vs capital tax;
     levy at T=0 is lump sum, at T=10 it is a one-time capital tax with a Laffer curve).
   - 11.3: investment-specific productivity psi_t (relative price of capital 1/psi_t).
   - 11.5-11.8, 11.13: planner/steady state (modified golden rule, small open economy, linear utility).
   - 11.9: linear utility, finite horizon (corner solutions, linprog check).
   - 11.10-11.12, 11.15-11.17: reading paths/yield curves; consistent fiscal stories.
   - 11.14: CE with g and a revenue-neutral capital tax (fixed point on tau_k).
   - 11.18: habit/durability; FOCs, steady state, algorithm (Newton on the path; stable-subspace check).
   - 11.19-11.20: Big K / little k at given prices; elastic labour, foreseen tau_n.
2. Notebook `Resolucao/ljungqvist_sargent/ls_ch11.ipynb`: shared toolkit (policy arrays g, tau_c,
   tau_k, psi, levy; Newton path solver on (11.6.3); shooting of 11.6.3 by bisection on c_0;
   linearisation (11.10.8) with numeric H derivatives; welfare and prices (11.6.8)). Independent routes:
   Newton vs shooting vs linear approximation; lambda_2 root vs corrected (11.10.16); VFI vs closed form
   (11.13); household problem at equilibrium prices vs aggregate path (11.19); elastic-labour Newton vs
   shooting (11.20); habit Newton vs stable-subspace linearisation (11.18). LQ toolkit of ch05/07 not
   needed (no LQ problem). Benchmark parameters of section 11.9 (alpha=.33, delta=.2, beta=.95,
   gamma=2, g=.2, f=k^alpha) where the book gives none; B=3 in 11.20. Figures fig/ls11_*.pdf.
3. `ls_solutions_ch11.tex` (ch08 preamble/boxes, full statements), pdflatex x2, pdffonts, clean aux.
4. README: Chapter 11 row after Chapter 10.
