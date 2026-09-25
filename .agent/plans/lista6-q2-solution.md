# Plan — Lista 6, Question 2 (continue the solution) + companion charts

**Scope.** Question 2 (items a, b i–iii, c), 5 points. Replaces the placeholder section at the
end of `Resolucao/lista6_resolucao.tex`. Q1 is already written; do not touch it beyond the
"How to read this document" box (which says Q2 is unanswered) and cross-references.

**Math (all cross-checked symbolically in the text).**
- (a) Log-differentiate $M^S = p\,m^D(Y,i)$ with $i$ constant:
  $\mu = \pi + \eta g \Rightarrow \pi = \mu - \eta g$. State why $i$ constant kills the
  interest term, and that this is the QTM *with* the income elasticity put back in.
- (b) i. Baumol–Tobin $\Rightarrow \eta = 1/2$.
  ii. $\mu = \pi^* + \eta g = 2 + 0.5(3) = 3.5\%$.
  iii. True $\eta = 1$ (Cambridge) $\Rightarrow \pi = 3.5 - 3 = 0.5\%$: undershoot of 1.5 pp,
  i.e. the error is $(\eta_{true}-\eta_{assumed})g$.
- (c) $\ln m^D = \tfrac12\ln Y + \tfrac12\ln F + $ const at constant $i$, so
  $\dot m/m = \tfrac12(g+f)$ and $\pi = \mu - \tfrac12(g+f)$. Cross-check through velocity:
  $\hat V = \tfrac12(g-f)$ and $\pi = \mu + \hat V - g$ gives the same thing.
  $f<0$ is inflationary: cheaper payments technology shrinks the demand for real balances,
  so a fixed $\mu$ supplies money faster than the economy wants to hold it.

**Charts.** New `Resolucao/lista6_codigo/l6_figuras.py`, reusing `estilo_mpl.py` copied from
`lista5_codigo` (pgf backend + lmodern/cmap → no Type 3 fonts), writing into `Resolucao/fig/`:
- `fig_l6q2_eta.pdf` — (i) $\pi$ against $\eta$ at $\mu=3.5\%$, $g=3\%$, marking the
  Baumol–Tobin and Cambridge points and the target line; (ii) the required $\mu(g)$ schedules
  for $\eta=\tfrac12$ and $\eta=1$, with the miss at $g=3\%$ marked.
- `fig_l6q2_trips.pdf` — (i) log paths of $M$, $p$, $m^D$ under $f=0$ vs $f<0$ at fixed $\mu$;
  (ii) $\pi$ against $f$, the line $\mu-\tfrac12(g+f)$.

**Interactive companion.** Already exists — do not rebuild:
`Map/aula-07-moeda-inflacao/companion-baumol-tobin.html` (trips, balances, velocity,
elasticities) and `companion-seigniorage.html`. Link both from the Q2 section.

**Verification.** Numbers ($3.5\%$, $0.5\%$, $\eta$ values) recomputed in the figure script and
printed; `pdflatex` twice; `pdffonts Resolucao/lista6_resolucao.pdf` must show every font as
Type 1 with `uni = yes`.
