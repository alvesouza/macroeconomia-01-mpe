# Plan: Ljungqvist & Sargent ch. 7 solutions

Chapter 7 (Recursive Competitive Equilibrium: I) has 7 exercises, printed pp. 244-248 (PDF = printed + 39).

1. Analytical: 7.1 competitive firm (Bellman, regulator with x=[y,Y,1], u=y'-y; undetermined coefficients give
   h1=1, h2, h0 in closed form; actual law nh0+(1+nh2)Y; Euler (7.2.7)); 7.2 REE fixed point H=M(H) (quadratic in H1
   = planner's characteristic equation), test pairs (i)-(iii), iterative algorithm with damping; 7.3 planner regulator,
   s = (iii); 7.4 monopoly regulator (A1 -> 2A1 in Euler); 7.5 duopoly MPE definition, Bellman, nnash;
   7.6 Phelps-Pollak/Laibson MPE by backward induction, commitment Bellman; log/Cobb-Douglas closed form;
   7.7 equilibrium search: Bellman with aggregate U, reservation wage, phi(U)=1-F(wbar(U)), RCE definition.
2. Notebook `Resolucao/ljungqvist_sargent/ls_ch07.ipynb`: reuse ch05 toolkit (olrp/dare/evaluate/howard) verbatim,
   add nnash (coupled Riccati). Asserts by independent route: olrp vs undetermined coefficients vs Euler residual;
   REE via quadratic vs planner LQ vs damped iteration on M; nnash vs best-response iteration with olrp;
   7.6 grid backward induction vs closed form; 7.7 grid RCE vs scalar steady-state root. Figures fig/ls07_*.pdf.
3. `ls_solutions_ch07.tex` (ch03 preamble/boxes, full statements), pdflatex x2, pdffonts, clean aux.
4. README: Chapter 7 row after Chapter 6 (concurrent agent) / Chapter 5.
