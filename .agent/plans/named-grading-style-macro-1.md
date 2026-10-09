# Named grading style "macro 1"

Goal: make `rules/00_estilo_avaliacao.md` a reusable, named grading style that other courses
can request.

1. Copy `rules/00_estilo_avaliacao.md` verbatim to
   `~/.claude/commands/templates/styles/macro-1.md` (verbatim, so a re-sync is a plain `cp`
   and drift is a `cmp`).
2. `/exam-gen` and `/exam-grade`: accept a style name in `$ARGUMENTS`; a named style outranks
   the project's `rules/00_estilo_avaliacao.md`; keep its grading rules, rebind its course
   bindings (bibliography, block table, scope exclusions, examples, template path) to the
   current course.
3. `/setup-study`: ask for the grading style in Step 1; in Step 5 copy the named style into
   `rules/00_estilo_avaliacao.md` instead of the generic template, rebound to the new course.
4. Edit the local copies, then copy them over the global ones so both stay byte-identical.

Verify: `cmp` local vs global for the three commands; `cmp` rules/00 vs styles/macro-1.md.
