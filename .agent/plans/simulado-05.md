# Plan: Simulado 5 (whole course, real-exam format)

- Source `Simulados/simulado-05.tex`; PDFs by jobname (`-exam`, `-solutions` via `\withsolutions`),
  preamble copied from `simulado-02.tex` (lmodern + cmap after fontenc). English.
- Format of Prova 01: 10 points, 4 long questions, narrative scenario, items a-d.
- Q1 (2.0) Measurement + Solow. (a) coffee chain: imports, inventories, government at cost; three
  approaches = 580; inventory drawdown next year; "unsold / free school" claim. (b) Solow per worker,
  alpha=1/3, s 0.15 -> s_GR; carry exponent; c impact -21.6%, c* +16.9%; time paths.
- Q2 (2.5) Labour-leisure in GE (Kurlat 7, 9): Y=AK^a L^(1-a), u=ln c+psi ln(1-L), psi=1/3,
  tau=25% on labour income. Planner = CE at tau=0 (L=2/3). Rebate L=0.6, waste L=9/14;
  substitution vs income effect; alpha=0 knife edge; consumption-equivalent welfare loss.
- Q3 (2.5) Money (Kurlat 10-11): Baumol-Tobin from primitives (Y=60000, F=25, i=12% -> N=12,
  m=2500); pi=mu-eta g with eta=1/2; Real-style credible cut mu 11%->5%: m jumps sqrt2, p jumps
  down or remonetisation 41.4%; seigniorage mu*m and its split; no Laffer peak under BT vs Cagan
  semi-log peak 1/a; shoe-leather cost sqrt(iFY/2); Friedman rule.
- Q4 (3.0) Benigno: sigma=eta=1, kappa=0.5, rho=2%, L=1/2(y-ye)^2+phi/(2kappa)(p-pe)^2.
  Markup +4: optimum y*=-4/3, p*=1/3 at phi=4, i*=3%; sign(phi-sigma); limits. ZLB: ybar_n -4,
  r_n=-2%, outcome y=-4/3, p=-2/3; forward guidance pbar=+2; g at ZLB: m_g=5/6, gap 1/3, g=4;
  vs optimal unconstrained policy multiplier omega_g=1/2.
- Check `Simulados/simulado_codigo/check_simulado_05.py` (sympy) asserts every number and closed
  form, prints plot coordinates. Compile twice each; pdffonts.
