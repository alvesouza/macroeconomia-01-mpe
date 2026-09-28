# Plan: TTS readings (Listas 5 and 7 topics; correction gaps) and 5 NotebookLM audio prompts

Date: 2026-09-27. Decisions confirmed by the user in one question round:

- Listas 5 and 7 (no corrections supplied): **detailed topic explanations, not solutions**.
  Existing readings follow the book/article page order (`Leituras/lista-05-general-equilibrium-narrated.txt`,
  `Leituras/benigno-2015-adas-narrated.txt`) and walk the solutions. The new scripts are
  concept-first: one part per topic the list tests, built from intuition up, with contrasts to
  earlier lectures, and no item-by-item solution.
- Correction gaps: **one long script organised by gap**, ~60-75 min (~9-11k words at 150 wpm),
  sourced from `Map/avaliacao-listas-1-4.md` and `Map/avaliacao-listas-2-3-6.md`.
- NotebookLM: **5 audio prompts by gap, 0 slides, 0 video**: (1) Aula 5 labour supply, income
  effect through the transfer; (2) search: congestion externality on others, Beveridge shift vs
  movement; (3) PPP and Balassa-Samuelson; (4) conditional convergence + aggregate vs per capita
  (incl. capital dilution on a merger); (5) the writing pattern: answer every object, words
  match the sign, proof then conclusion.

## Files

| Output | Format rules |
|---|---|
| `Leituras/lista-05-topics-explained-narrated.txt` | `.claude/commands/speechify.md` |
| `Leituras/lista-07-topics-explained-narrated.txt` | same |
| `Leituras/correction-gaps-narrated.txt` | same |
| `NotebookLM/audio/gaps-audio-{1..5}-<slug>.md` | `rules/10_notebooklm_prompts.md`, validated by `.claude/notebooklm-validate.py`; no output-language line |

## Verification

- TTS: plain text, no markdown/LaTeX/tables/code; word count reported; every number quoted
  matches the notes (grep spot-checks).
- NotebookLM: validator passes; each prompt under the character budget; sources named by exact
  filename in `NotebookLM/sources/`.
- Index rows: `Map/cobertura.md` (Leituras, NotebookLM), `NotebookLM/README.md`.
