# Plan: figures and full derivations across Map/; a conceptual mock exam solved as linked notes

Date: 2026-09-28. Request: (1) more images and graphs in the Map notes, and every step of the
math shown; (2) a mock exam, based on the listas, that tests understanding and the ability to
explain the theory; (3) its solution written in the style of the interconnected notes.

## State found

55 notes in 10 folders (~64k words); only 5 notes embed an image (the gap figures of
2026-09-26). Derivations are mostly stepwise, but not audited end to end.

## Part 1 — notes (one agent per folder, 8 agents)

Folders: aula-01 … aula-07 (aula-06 also owns `derivacoes-cap-09.md` and
`exogenous-capital-lista-05.md`; aula-05 owns `formulario-aula-05.md`), benigno (also updates
the two short indices aula-08, aula-09 with figure links).

Per folder:
- `Map/<folder>/make_figures.py` using the shared `Map/fig/mapstyle.py`; SVGs in
  `Map/<folder>/fig/`. Every number drawn is computed in the script (and asserted against the
  folder's check script where one exists). Target 2-4 figures per note where a picture shows
  the mechanism; none where it would be decoration.
- Embed `![caption](fig/x.svg)` + one-line italic reading of the figure, at the point in the
  text where the reader needs it.
- Audit every derivation; insert missing intermediate steps (no "it can be shown", no
  "rearranging" without the rearranged line). New steps checked with sympy or numerically in
  the folder's check script.
- Additions in English; existing text is not translated or restyled; nothing deleted except
  a step being replaced by its fuller version.

## Part 2 — Simulado 3, conceptual (1 agent)

- `Simulados/simulado-03.tex` → `simulado-03-exam.pdf`. 4 blocks x 25: per block two
  True/False-with-justification items (5 pts each, the mark is in the justification) and one
  discursive question (3 x 5) whose items ask to explain, draw and interpret, predict what an
  observer would wrongly conclude — minimal computation. Every question is anchored in a
  Lista (1-7) theme, and together they cover the graded gaps.
- Solution as linked notes: `Map/simulado-03/00-index.md` + one note per question, figures in
  `Map/simulado-03/fig/`, every math step shown, wiki-links to the derivation notes and
  companions, "the sentences that earn the mark", rubric, and the tempting wrong answer.

## Verification

- Each folder: `make_figures.py` and `check_*.py` run clean; SVGs inspected as PNG renders.
- Simulado 3: exam PDF builds, Type 1 fonts; solution notes' wiki-links resolve to existing
  files (script check).
- Index: `Map/00_indice.md` row for Simulado 3.
