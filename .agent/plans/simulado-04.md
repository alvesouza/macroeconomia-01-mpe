# Plan: Simulado 4 (mirror of the real Prova 01 format)

- Files: `Simulados/simulado-04.tex` (exam/solutions toggle as simulado-01/02, jobname builds),
  `simulado-04-exam.pdf`, `simulado-04-solutions.pdf`, `Simulados/simulado_codigo/check_simulado_04.py` (sympy asserts).
- Format: 10 points. Q1 1.5 (a/b/c 0.5), Q2 5.5 (a-e 1.0, f 0.5), Q3 3.0 (a/b/c 1.0). Symbolic in Q2-Q3.
- Q1 coffee farm + roastery: (a) imports, three approaches = 800; (b) unsold output -> inventory
  investment, GDP 800, next-year sale nets to zero; (c) government: wages 120, imported medicines 30,
  transfers 50, tax 200 -> GDP 920.
- Q2 Solow with labour-augmenting A (g) and n: (a) stationary k~=K/(AL), ratio, k~_SS, BGP rates;
  (b) s_GR = alpha, f'(k~)= (1+g)(1+n)-(1-delta), c per worker at every date.
  Two-period GE with leisure in both periods, household owns firm that owns K1 (full depreciation),
  borrows K2 from household: (c) budget constraint with Pi1, Pi2; (d) FOCs c1,c2,L1,L2,a1, c1=H/((1+b)(1+g));
  (e) firm FOCs, Pi1=alpha Y1, Pi2=0, s*=ab/(1+ab), L1, L2, map k^2(k^1) with 45-degree diagram;
  (f) relation to Solow (delta=1, n=0, s endogenous, s* < s_GR).
- Q3 Benigno: (a) news of higher abar -> AD right, gaps; (b) price stability -> raise i by Gamma dabar/sigma,
  divine coincidence, observer angle; (c) news + temporary IPI (tau_y) markup shock, loss
  1/2(y-ye)^2+phi/(2kappa)(p-pe)^2: targeting rule, decomposition of i*, news part independent of phi.
- Verify: run check script, compile both PDFs twice, pdffonts all Type 1.
