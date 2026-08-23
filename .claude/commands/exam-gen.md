---
description: Gera uma lista de exercícios (ou simulado) no estilo da Avaliação Final do MPE — questões objetivas + discursivas contextualizadas — com gabarito e rubrica, em LaTeX (um único .tex com toggle lista/gabarito). Pergunta profundidade, temas tangenciais e complexidade antes de gerar.
argument-hint: <conteúdo/tópicos a testar> [nº de questões]
allowed-tools: Read Grep Glob Bash PowerShell Write Edit AskUserQuestion
---

Gera uma lista de exercícios no estilo de avaliação do MPE a partir de `$ARGUMENTS` (o conteúdo que o aluno quer testar).

Estilo, taxonomia, formato de solução, rubrica e regras LaTeX: siga **`~/.claude/commands/templates/estilo-avaliacao.md`** (cópia local em `rules/00_estilo_avaliacao.md` quando existir). Template LaTeX: **`~/.claude/commands/templates/lista-exam.tex`**.

## Passo 1 — Escopo

Interprete `$ARGUMENTS`: tópicos/aulas/arquivos a cobrir e nº de questões (padrão: 1 bloco objetivo + 1 discursivo por tema; ou o que o aluno pedir). Se vago, infira do `CLAUDE.md`.

## Passo 2 — Contexto e bibliografia

1. Leia `CLAUDE.md` (escopo do curso, restrição "não extrapolar", bibliografia).
2. Leia `rules/` (fórmulas, definições) e **`Map/`** (cross-references: pesos por tópico, páginas dos livros para as linhas `Ref:`, exercícios similares).
3. Use os **livros** (N&S piso; J-R rigor; ZaE narrativa; MWG cross-check) para garantir correção e referências. Formule questões **originais** — nunca copie exercícios.
4. Identifique tópicos **adjacentes** ao escopo (via `Map/`) para oferecer como temas tangenciais no Passo 3.

## Passo 3 — Avalie a matematizabilidade e pergunte ao aluno

**Primeiro** avalie se o conteúdo é **matematizável** (tem fórmulas, derivações, cálculo numérico — ex.: Slutsky, UMP/EMP, Pigou, Arrow-Debreu) ou é **predominantemente conceitual** (ex.: intuições de Coase, tipologia de assimetria, estabilidade em matching). Isso decide se a pergunta de complexidade matemática aparece.

Faça **uma** chamada AskUserQuestion com as perguntas abaixo (adapte as opções ao escopo; pule qualquer uma já respondida em `$ARGUMENTS`):

1. **Profundidade** — quão a fundo abordar o tema?
   - *Revisão rápida* (conceitos centrais, aplicação direta)
   - *Padrão de prova* (recomendado — montar→resolver→interpretar)
   - *Aprofundado* (inclui provas/derivações e casos-limite, estilo J-R/MWG)
2. **Temas tangenciais** — incluir tópicos adjacentes? (multiSelect, opções vindas do `Map/`; ex.: para Slutsky → elasticidades, bem-estar CV/EV, Giffen). Inclua a opção "Só o tema principal".
3. **Complexidade matemática** — **somente se o conteúdo for matematizável**:
   - *Leve* (plug-and-play, números limpos)
   - *Média* (recomendado — multi-passo, dualidade)
   - *Pesada* (derivações, integrais de bem-estar, prova/limite)

   Se o conteúdo for **predominantemente conceitual**, substitua esta pergunta por **Ênfase quantitativa**: *100% conceitual* / *Maioria conceitual com 1–2 itens quantitativos* / *Equilibrado* — e não force matemática onde o tema não pede.
4. **Formato** — *Completo* (objetivas + discursivas) / *Só objetivas* (MC + V/F) / *Só discursivas*.

Se o conteúdo misturar partes matematizáveis e conceituais, você pode oferecer a complexidade matemática referida apenas à parte quantitativa.

## Passo 4 — Projete a lista

Conforme o estilo: blocos temáticos; em cada bloco, questão objetiva (a,b MC 3 pts; c,d V/F 2 pts) e/ou discursiva (a,b,c × 5 pts). Calibre pela complexidade escolhida. Distribua a posição da alternativa correta (não fixar A). V/F deve testar recíprocas/armadilhas. Contextualize cada questão num cenário brasileiro plausível, com parâmetros que dão resposta fechada limpa.

## Passo 5 — Escreva o `.tex`

Copie o template e preencha o corpo com as questões e as soluções:
```bash
mkdir -p Listas && cp ~/.claude/commands/templates/lista-exam.tex "Listas/lista-<tema>.tex"
```
- Defina `\listatema`. Remova o exemplo do template.
- Cada questão usa as macros (`\bloco`, `\questao`, `\alternativas`, `\gabarito`, `\resolespaco`) e cada solução vai dentro de `\begin{sol}...\end{sol}` com `\passo`, `\intuicao`, `\refbib` e `\rubrica` (com tetos conceituais + penalidades leves + não-cumulatividade).
- Deixe o toggle em `\solucoesfalse` (a lista em branco é o default).

## Passo 6 — Compile e verifique

Compile os **dois** PDFs a partir do mesmo fonte (regra global lmodern+cmap):
```bash
cd Listas
pdflatex -interaction=nonstopmode -halt-on-error "lista-<tema>.tex"   # 2x -> lista em branco
# gabarito: flip do toggle só para compilar, depois restaure \solucoesfalse
python3 - <<'PY'
import re
f="lista-<tema>.tex"; s=open(f,encoding="utf-8").read()
g=re.sub(r'(?m)^\\solucoesfalse\b','\\\\solucoestrue',s)
open("_gab.tex","w",encoding="utf-8").write(g.replace('lista-<tema>','lista-<tema>-gabarito'))
PY
pdflatex -interaction=nonstopmode -halt-on-error _gab.tex   # 2x
mv _gab.pdf "lista-<tema>-gabarito.pdf"; rm -f _gab.* *.aux *.log
```
Verifique: `pdffonts lista-<tema>.pdf` — tudo **Type 1**, zero Type 3. Sem erros de compilação.

O aluno edita o `.tex` e, para ver o gabarito, troca `\solucoesfalse`→`\solucoestrue` e recompila.

## Passo 7 — Relatório

Mostre: nº de questões (objetivas/discursivas) por bloco; complexidade e temas escolhidos; arquivos gerados (`lista-<tema>.tex`, `.pdf` em branco, `-gabarito.pdf`); contagem de páginas; como resolver e depois rodar `/exam-grade Listas/lista-<tema>.tex` para corrigir a própria resolução.
