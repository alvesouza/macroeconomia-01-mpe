# Plan — Lista 7: map, full solution, three companions

**Scope.** Lista 7 (4 questions, 10 points), entirely Benigno (2015) — Aulas 8–9. No Kurlat
exercise. User choices (2026-09-25): all three companions, Benigno's calibration, LaTeX PDF like
Lista 6, companions local + published as Artifacts.

## Map (question → source)

| Q | Pts | Benigno | Notes already derived | Companion |
|---|---|---|---|---|
| 1 NK vs NC vs Keynesian | 3 | §1–§3 pp. 503–506, §4 p. 507–508 (menu costs, sticky info, NC Phillips curve), §11 p. 521–522 | 00-index, 01, 02 §2.8, 10 §10.1 | — (conceptual) |
| 2a temporary markup ↑ | 1.5 | §7, Fig. 9, pp. 513–514 | 06 §6.2 | `companion-two-shocks.html` |
| 2b nominal rate ↓ | 1.5 | §5 Fig. 4, p. 511; §4.3 | 04 §4.4 | same page, right panel |
| 3 y_n vs y_e | 2 | §4.2–§4.4, eqs. (14), (15), (19), pp. 508–509 | 03 §3.3–3.5 | `companion-wedge.html` |
| 4 loss + AS | 2 | §11, eqs. (33)–(35), Fig. 14, pp. 521–523 | 10 §10.1–10.5 | `companion-loss-bowl.html` |

## Math to state and verify (Benigno calibration α=.66, σ=.5, η=.2, θ=8 ⇒ κ=1.1333)

- 2a, dμ=+5%: dy_n=−dμ/(σ⁻¹+η); dy=σκ/(1+σκ)·dy_n; dp=−κ dy_n/(1+σκ); gaps opposite sign.
- 2b, di=−1pp: AD shifts up by 1pp in p (right by σ·1pp); dy=−σdi/(1+σκ), dp=κ dy; y_n,y_e fixed.
- 3: log MRS = η(y−a)+σ⁻¹(y−g); planner MRS=a, market MRS=a−μ ⇒ y_n−y_e=−μ/(σ⁻¹+η);
  deadweight triangle ½μ²/(σ⁻¹+η).
- 4: substitute AS ⇒ y^o=(φy y*+φpκ² y_n)/(φy+φpκ²); p−p^e=κφy(y*−y_n)/(φy+φpκ²);
  targeting rule φy(y−y*)+φpκ(p−p^e)=0; min loss φyφpκ²(y*−y_n)²/(φy+φpκ²);
  Benigno mapping φy=½, φp=θ/(2κ), y*=y_e ⇒ rule (34), share 1/(1+θκ); implementing rate
  i=r_n−(1+σκ)(y^o−y_n)/σ.

## Files

1. `Listas/MPE_Macro1_2026_Lista7.md` — clean transcription (the PDF is short; no markitdown table mess).
2. `Resolucao/lista7_codigo/l7_figuras.py` (+ copied `estilo_mpl.py`): prints every number above,
   writes `Resolucao/fig/fig_l7q2_shocks.pdf`, `fig_l7q3_wedge.pdf`, `fig_l7q4_loss.pdf`.
3. `Resolucao/lista7_resolucao.tex` → `.pdf`, Lista 6 preamble and box styles.
4. `Map/benigno/companion-{two-shocks,wedge,loss-bowl}.html`, linking `../companion.css`;
   artifact copies with the CSS inlined, built in the scratchpad.
5. `Map/lista-07.md` routing note; update `Map/exercises-index.md` forecast row and
   `Map/benigno/00-index.md` companion table.

## Verification

- Python numbers printed; companions checked against them at 3 control vectors each (node).
- `pdflatex` ×2; `pdffonts` all Type 1, uni=yes.

## Addendum (2026-09-25): short version in the instructor's style

User asked for a second Lista 7 solution "based on" `Listas/soluções do instrutor/PSET 6.pdf`.
That PDF is the instructor's Lista 6 solution (money), so it supplies the **format only**:
answer-first, arrow chains, one or two lines per step, key result highlighted/boxed, derivation
only where the answer depends on it. Content = the long solution, unchanged numbers.
Output: `Resolucao/lista7_resolucao_curta.tex/.pdf`, reusing `fig/fig_l7q2_shocks.pdf` (Q2 asks
for diagrams). Target 3-4 pages. Verify: pdflatex x2, pdffonts Type 1 + uni.
