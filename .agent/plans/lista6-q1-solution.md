# Plan — Lista 6, Question 1 (solution document)

**Scope.** Question 1 only (items a–d), 5 points, "Based on Kurlat (2020, Cap. 10 e 11)".
Question 2 is *not* in scope for this pass; the document reserves a marked placeholder for it.

**Source of truth already established in the repo** (do not re-derive):
- `Map/leituras-aula-07.md` §5 — item-by-item map of Lista 6, with the trap for each item.
- `rules/07_moeda_inflacao.md` — Baumol-Tobin $m^D=\sqrt{YF/(2i)}$, elasticities $+\tfrac12$,
  $-\tfrac12$; classical dichotomy; neutrality vs superneutrality; Fisher.
- Kurlat §10.2–10.4 (pp. 192–202) and §11.2 (pp. 208–215).

**Output.** `Resolucao/lista6_resolucao.tex` → `.pdf`, mirroring `lista5_resolucao.tex`:
same preamble (lmodern + cmap, mandatory), same tcolorbox styles (theory / question / plan /
trap / rubric), same `\passo`, `\intuicao`, `\resp` macros, English, blue highlighted answers.

**Content per item**
- (a) $MV=PY$ holds by *definition of $V$* ($V\equiv PY/M$), so it is one equation in four
  unknowns and has zero causal content. It becomes the QTM only on three added assumptions
  ($V$ stable / exogenous, $Y$ real-side determined, $M$ policy-controlled). Answer to the
  causal sub-question: it says nothing — the identity is satisfied by *any* split of a change
  in $M$ across $p$, $Y$, $V$.
- (b) Invert Baumol-Tobin: $V = PY/M = \sqrt{2iY/F}$. Velocity is *not* a constant: it rises
  with $i$ (elasticity $+\tfrac12$) and with $Y$ ($+\tfrac12$), and falls with $F$
  ($-\tfrac12$). Income elasticity of money demand $\tfrac12 < 1$ ⇒ scale economies in cash
  management ⇒ $V$ trends up with growth. Derive $N^*$ and the average balance so the square
  root is built, not quoted.
- (c) With $p=\bar p$: $M^S/\bar p$ jumps, so real balances demanded must rise, so $i$ falls
  and/or $Y$ rises. Two honest points: (i) ch. 11 supplies *no* mechanism by which a lower $i$
  raises $Y$ — that is lecture 8's job (sticky prices, AD); (ii) with flexible $p$ the
  classical dichotomy holds, $Y$ and $i$ are pinned by the real block and $p$ jumps
  proportionally — money is neutral.
- (d) Same equation, two readings. $M$ fixed ⇒ $i$ is the endogenous price that clears the
  market. $i$ fixed ⇒ the CB must supply whatever $M$ the demand curve calls for; money
  becomes endogenous. Note the horizontal-supply picture, the real-world practice (Selic), and
  that the two are equivalent only under perfect information about $m^D$ — they differ once
  money demand shifts (a shock to $F$, a payments innovation).

**Verification.** No numerical claims in Q1 beyond the elasticities $\tfrac12$/$-\tfrac12$,
which are checked symbolically in the text. Compile with `pdflatex` twice; then `pdffonts`
must show every font as Type 1 with `uni = yes` (global LaTeX rule).
