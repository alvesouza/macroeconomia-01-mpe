# Plan — Benigno (2015) full explainer set

Source: `Livros/Benigno_2015_NewKeynesianEconomics_AS_AD_View.md` (Research in Economics
69: 503-524). Already summarised at rule level in `rules/08_adas_microfundamentos.md`
(sections 1-5) and `rules/09_adas_politica.md` (sections 6-12). This set is the
**derivation layer** those two files point to. Precedent: `Map/derivacoes-cap-09.md`.

Scoping answers (2026-09-15): NotebookLM unit = Aula 8 / Aula 9; counts = 4 slides +
3 audio + 0 video; quiz = 2 files (microfoundations / policy); language = English
(global rule outranks the project pt-BR default).

## Deliverables

1. `Map/benigno/00-index.md` .. `09-optimal-policy.md` — 10 wiki-linked notes, every
   step of algebra shown, undergrad and grad level, one equation numbering shared with
   the article. Plus `check_multipliers.py`: asserts Table 1 formulas reproduce all 8
   rows of Table 2 and both deleveraging multipliers (1.29 / 1.62 / 2.75).
2. `Leituras/benigno-2015-adas-narrated.txt` — TTS script, math spoken in words, no
   tables, no symbols read out. Follows `Leituras/aula-07-money-and-inflation-narrated.txt`.
3. NotebookLM prompts, validated by `.claude/notebooklm-validate.py`:
   - slides: `aula-08-slides-{1-derivation,2-geometry}`, `aula-09-slides-{1-shocks-and-multipliers,2-trap-and-optimal-policy}`
   - audio: `aula-08-audio-1-the-missing-lm-curve`, `aula-09-audio-1-divine-coincidence-and-its-limit`, `aula-09-audio-2-the-multiplier-is-not-the-point`
   - 3 audio over 2 units allocates 1 to Aula 8 and 2 to Aula 9: sections 6-12 carry the
     two arguments that need two hosts (the coincidence and its failure; output vs gap).
4. `Simulados/quiz-aula-08-microfundamentos-2026-09-15.md` and
   `Simulados/quiz-aula-09-politica-2026-09-15.md`, validated by `.claude/quiz-validate.py`.
5. Link from `Map/00_indice.md`; correct the transcription error found in the rules files.

## Finding to fix (verified three ways)

`rules/08` and `rules/09` carry the public-spending coefficient in y_n (eq. 15) and y_e
(eq. 19) as `(sigma^-1 - 1)/(sigma^-1 + eta)`. It is `sigma^-1/(sigma^-1 + eta)`:
  - log-linearising (14) directly gives it;
  - Benigno's own text says output rises one-to-one with g when eta = 0, which the
    printed coefficient contradicts and this one satisfies;
  - Table 1's m_gbar = eta/((sigma^-1+eta)(1+kappa*sigma)) only follows from this one,
    and Table 2 then reproduces to two decimals in all 8 rows.
The `(sigma^-1 - 1)` form is an OCR artefact of `sigma^(-1)` in the source markdown.
Fix: formula and the two Python snippets in both rules files.

## Order

notes -> check script (run it) -> narration -> NotebookLM (validate) -> quizzes
(validate) -> index and rules fixes.
