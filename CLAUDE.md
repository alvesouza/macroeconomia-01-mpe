<!-- TIER-0, orçamento 900 tokens. Bloco GERADO: edite rules/core.md e rode tools/sync_rules.py -->

# Macroeconomia I — MPE Insper (2026/T3)

Livro-texto **Kurlat (2020)**; **Benigno (2015)** nas Aulas 8-9. Programa, bibliografia,
avaliação, estrutura: [rules/11_curso_programa.md](rules/11_curso_programa.md) · [Map/](Map/00_indice.md).

<!-- GENERATED:tier0:start -->
### Non-negotiable

1. Escalate retrieval in this order and stop at the first rung that answers the
   question: **graph query → symbol lookup → structural search → ripgrep → file slice
   → whole file**.

2. Do not switch the main-loop model mid-session. Delegate to a subagent instead.

3. Write the plan to `.agent/plans/<slug>.md` before implementing any non-trivial
   change, then implement against it.

4. Report only outcomes observed in tool output. Failing tests are quoted, not
   summarized away. Skipped steps are stated.

5. Never read secrets into context: `.env`, key material, credential stores, tokens.
   Reference them by name.

6. Memory-safety, point-in-time, and idempotency gates do not relax under deadline.

### Prefer

7. Persist findings to `.agent/notes/<topic>.md` rather than re-deriving them.

8. Reuse before writing. If you write new code anyway, say what you found and why it
   did not fit.

9. Match the surrounding code. `.agent/conventions.md` outranks this repo's style
   preferences; correctness rules never yield.

10. Doc comments on public functions: purpose, parameter meaning, failures, calling
    context. Inline comments state constraints the code cannot express, never narration.

### Avoid

11. Making the diff larger than the change. Refactor inside the change's own context;
    outside it, ask (`codebase-work.md`).

12. Abstractions, defensive branches for impossible states, and speculative generality.

13. Claiming completion when part of the task is unfinished. Do the rest; if truly
    blocked, state plainly what is missing and why.

14. Re-deriving facts already established in the session.

Rationale and verification commands for each rule: `rules/core.md`
<!-- GENERATED:tier0:end -->

## Escopo — não extrapolar

Restrito a **Kurlat caps. 1-7, 9-11** e **Benigno (2015)**. Fora: Kurlat cap. 8 e caps. 12-15;
DSGE estocástico, Bellman e programação dinâmica, RBC estocástico, econometria de séries
temporais, NKPC de Calvo log-linearizada. Ljungqvist & Sargent está em `Livros/` e **não** é do
curso. A demanda de Cagan **está** no escopo (exercício 11.6). Complementar serve para intuição
e contraste, nunca para elevar o nível. **Nunca reproduzir enunciado de exercício**: número + página.

## Formato

pt-BR (termo técnico em inglês entre parênteses na 1ª vez). LaTeX `$...$`; nunca `$` solto
para moeda. **Python**, sem R. Notação de Kurlat.

## Irmãos e segredos

`../Video explainer` (kit de vídeo) · `../Efficient Token` (governança: pacotes em `rules/`,
`tools/`, `.claude/hooks/`). Chaves em `.env`, não versionado; nunca ler segredo para o contexto.
