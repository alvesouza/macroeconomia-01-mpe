# Plan: Romer 8.13 and 8.15 solutions for hardest-solutions.tex

Scope: two LaTeX fragments + one check script, inputs of `Listas/hardest-solutions.tex`
(already lists `\input{hardest-parts/romer-8-13}` and `romer-8-15`). English (global rule).

1. `Listas/hardest-parts/romer-8-13.tex` — macros of `Listas/hardest-preamble.tex`.
   (a) perturbation -> external-habit Euler ratio; equilibrium log-linear growth equation;
   cases theta=1 (b=0) and theta>1 (0<b<1). (b) full marginal utility M_t (habit cost),
   Euler M_t = (1+r)/(1+rho) M_{t+1}; growth form; linearization with rho=r=0 ->
   g_{t+2}-g_{t+1} = g_{t+1}-g_t; exact relation X_t^{1-theta} = mu R_t for the sign.
2. `Listas/hardest-parts/romer-8-15.tex` — commitment, naive, sophisticated plans (log);
   time inconsistency + commitment value; proof for any proportional date-2 rule;
   CRRA: c1 = W/(1+[delta A(s)]^{1/sigma}), sign via concavity/convexity of A.
3. `Listas/hardest-parts/check-8-13-8-15.py` — sympy/numeric asserts for every claim.
4. Compile each fragment through a temp wrapper outside the repo (pdflatex x2), fix errors
   and overfull boxes > 5pt, delete the temp folder. No Bellman, no stochastic models.
