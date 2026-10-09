# Building the practice lists (Listas/practice-*.tex)

- `comment.sty` (MiKTeX v3.8) writes every included `sol` body to `comment.cut` in the
  working directory, so two pdflatex runs in the same folder overwrite each other's
  solutions. Run builds one at a time, or give each job its own cut file:
  `pdflatex -jobname=<job> "\AtBeginDocument{\def\DefaultCutFileName{\def\CommentCutFile{<job>.cut}}}\input{<file>.tex}"`.
  Overriding `\CommentCutFile` alone does nothing: the package resets it through
  `\DefaultCutFileName` at every `sol` environment. The log shows
  "Straight input of <job>.cut" when the override works.
- The shared preamble now sets that per-job cut file itself, and `\bloco`/`\questao` start with
  `\par`, so `\input`-ed block files need no blank line between them (without it, a heading
  ran into the last line of the previous block).
- Answer key: copy the list with its `\solucoesfalse` line flipped to `\solucoestrue`,
  compile twice, rename the PDF to `<list>-gabarito.pdf` (`/exam-gen` Step 6).
- Background agents writing large single files stalled ("no progress for 600s"); one block
  per agent, one file of at most ~250 lines per Write, finished reliably.
