# Macroeconomia I — MPE Insper (2026, 3º trimestre)

Projeto de estudo da disciplina **Macroeconomia I** do Mestrado Profissional em Economia
do Insper — Prof. Pedro G. Duarte, monitor Frederico "Fred" Gomes.

**Livro-texto:** Kurlat (2020), *A Course in Modern Macroeconomics*
**Artigo obrigatório:** Benigno (2015), "New-Keynesian economics: An AS–AD view"

O escopo, o mapa aula × capítulo e as regras de conteúdo estão em
[CLAUDE.md](CLAUDE.md) — leia antes de gerar qualquer material.

---

## Estrutura do projeto

| Diretório | Para quê |
|---|---|
| [Aula/](Aula/) | Slides e materiais das 9 aulas |
| [Listas/](Listas/) | Listas de exercícios + `lista-exam.tex` (template LaTeX de lista/gabarito) |
| [Livros/](Livros/) | Kurlat, Benigno, complementares e o programa da disciplina |
| [Monitoria/](Monitoria/) | Materiais de monitoria |
| [Prova/](Prova/) | Avaliação final e provas anteriores |
| [Simulados/](Simulados/) | Quizzes em Markdown, consumidos pelo `quiz.html` |
| [Resolucao/](Resolucao/) | Soluções geradas (`/solution`, `/exam-gen`, `/exam-grade`) |
| [rules/](rules/) | Regras por tópico: fórmulas, armadilhas, padrões de código |
| [Map/](Map/) | Mapas de referência cruzada (wiki-links para Obsidian) |
| [NotebookLM/](NotebookLM/) | Prompts de slides/áudio + `sources/` prontos para upload |
| [Design/](Design/) | Material visual auxiliar |
| `.claude/commands/` | Cópias locais dos comandos — edite à vontade |

---

## Comandos disponíveis

### Preparar material

```bash
/convert Aula/                    # converte slides PDF para Markdown
/convert Livros/                  # converte livros (demorado — já rodado no setup)
/summarize Aula/                  # resumo estruturado de todas as aulas
/list-exercises Listas/           # extrai todos os enunciados das listas
/study-map .                      # (re)gera os mapas de referência cruzada em Map/
```

### Estudar e praticar

```bash
/solution Listas/MPE_Macro1_2026_Lista1.md      # resolve uma lista, passo a passo
/exercise-plan "Solow, contabilidade do crescimento"
                                  # plano de exercícios REAIS dos livros (número + página),
                                  # ponderado por subtópico e nível — não reproduz enunciados

/book-solutions "Kurlat cap. 6"   # soluções no estilo tcolorbox (LaTeX)
/study-pack Resolucao/remediacao-XX.md
                                  # monta um PDF único com as páginas recomendadas
```

### Avaliação (estilo MPE)

```bash
/exam-gen "Aulas 2-3: crescimento e Solow"
                                  # gera lista/simulado + gabarito + rubrica em LaTeX.
                                  # Pergunta antes: profundidade, temas tangenciais,
                                  # complexidade matemática.

/exam-grade Listas/lista-02.tex minha-resolucao.md
                                  # corrige sua resolução contra a rubrica, com tetos por
                                  # erro conceitual e referência aos livros
```

O estilo (taxonomia de questões, contextualização brasileira, rubrica, LaTeX) está
especificado em [rules/00_estilo_avaliacao.md](rules/00_estilo_avaliacao.md).

### Quizzes

```bash
/quiz-gen Simulados/ --tema "moeda e inflação"   # gera quiz em MD
/quiz-analyze <cole o JSON de resultados>        # análise de erros + quiz de reforço
```

### NotebookLM

```bash
/notebooklm Aula/                 # gera prompts de slides e áudio para cada aula
```

---

## Como rodar os quizzes

O `quiz.html` precisa ser servido por HTTP (ele lê os `.md` do `Simulados/` via `fetch`).

```bash
cd "d:\Documents\Git\Github\Macroeconomia 01 - MPE"
python -m http.server
```

Depois abra <http://localhost:8000/quiz.html> e escolha o arquivo de quiz.

Ao final, use **Exportar** para salvar o JSON de resultados e passe-o para
`/quiz-analyze`. O player também exporta uma versão **standalone** do quiz (arquivo único,
sem servidor).

> Antes de publicar um quiz novo, o `/quiz-gen` roda `.claude/quiz-validate.py`
> automaticamente — ele checa integridade de parsing e padrões anti-chute (alternativa
> correta sistematicamente mais longa, etc.).

---

## Navegar no Obsidian

Abra a **pasta raiz do projeto** como vault. Os arquivos em [Map/](Map/) usam wiki-links
`[[...]]` e tags, ligando aula → capítulo do livro → exercício → quiz. O grafo do Obsidian
mostra a estrutura do curso e revela quais tópicos estão sem cobertura.

---

## Fluxo NotebookLM

1. **Suba as fontes.** Todo o conteúdo de [NotebookLM/sources/](NotebookLM/sources/) já está
   achatado e prefixado por categoria (`Aula_`, `Lista_`, `Livro_`, `Monitoria_`, `Prova_`).
   Faça upload em massa para um único notebook, **preservando os nomes** — os prompts citam
   os arquivos pelo nome exato.
2. **Gere os prompts.** `/notebooklm Aula/`
3. **Use.** Abra o arquivo de prompt → `Ctrl+A` → `Ctrl+C` → cole no NotebookLM
   (slides → campo de criação de slides; áudio → campo *Customize* do Audio Overview).

> ⚠️ Os campos do NotebookLM truncam **em silêncio** por volta de 6.000 caracteres. Mantenha
> cada prompt abaixo de 5.000. Para conferir:
> ```powershell
> Get-ChildItem NotebookLM\slides,NotebookLM\audio -Filter *.md |
>   ForEach-Object { "{0,5}  {1}" -f (Get-Content $_.FullName -Raw).Length, $_.Name }
> ```

---

## Fluxo de estudo sugerido

1. Antes da aula — leia o capítulo do Kurlat correspondente ([CLAUDE.md](CLAUDE.md)) e o
   arquivo de `rules/` do tópico.
2. Depois da aula — `/summarize` do slide, e `/quiz-gen` para autoavaliação rápida.
3. Lista de exercícios — resolva primeiro; depois `/solution` para conferir o método.
4. Erros recorrentes — `/quiz-analyze` gera a remediação, e `/study-pack` monta o PDF com
   exatamente as páginas a reler.
5. Antes da avaliação final — `/exam-gen` com os 4 blocos, resolva sem consulta, e
   `/exam-grade` para a correção com rubrica.
