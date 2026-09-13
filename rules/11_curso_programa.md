# Programa, bibliografia e estrutura — detalhe

> **Tier 2.** Carregado sob demanda, não a cada turno. O `CLAUDE.md` guarda só o contrato:
> identidade, trava de escopo, idioma, projetos irmãos e ponteiros. O detalhe está aqui e,
> mais completo ainda, em [`Map/`](../Map/00_indice.md).

## Conteúdo programático: aula × bibliografia

| Aula | Tópico | Livro principal | Lista | Regras |
|---|---|---|---|---|
| **1** | Mensuração dos Agregados Macroeconômicos | Kurlat, caps. **1-2** | Lista 1 | [01](01_mensuracao_agregados.md) |
| **2** | Crescimento: Fatos Básicos e Modelo de Solow | Kurlat, cap. **3** e **4.1-4.2** | Lista 1 | [02](02_crescimento_solow.md) |
| **3** | Crescimento: Solow (cont.) e Evidências | Kurlat, caps. **4.3-4.5** e **5** | Lista 2 | [03](03_solow_evidencias.md) |
| **4** | Microfundamentos: Consumo e Poupança | Kurlat, cap. **6** | Lista 3 | [04](04_consumo_poupanca.md) |
| **5** | Microfundamentos: Trabalho e Lazer | Kurlat, cap. **7** | Lista 4 | [05](05_trabalho_lazer.md) |
| **6** | Microfundamentos: Teoria de Equilíbrio Geral | Kurlat, cap. **9** | Lista 5 | [06](06_equilibrio_geral.md) |
| **7** | Mercado Monetário e Inflação | Kurlat, caps. **10** e **11** | Lista 6 | [07](07_moeda_inflacao.md) |
| **8** | Modelo AD-AS novo-keynesiano | Benigno (2015), **seções 1-5** | Lista 7 ⚠️ | [08](08_adas_microfundamentos.md) |
| **9** | AD-AS: análise de política econômica | Benigno (2015), **seções 6-12** | — | [09](09_adas_politica.md) |

> **Listas.** O programa anuncia **7 listas**; as **Listas 1 a 6 já foram emitidas**.
>
> ⚠️ **A Lista 6 saiu sem Benigno** (12/09/2026): é "Based on Kurlat (2020, Cap. 10 e 11)" e
> nada mais, cobrindo **só a Aula 7**. Logo a **Lista 7** tem de carregar as Aulas 8 **e** 9
> (Benigno §1-12), ou o AD-AS fica sem lista — confirmar com o professor. Detalhe em
> [Map/leituras-aula-07.md](../Map/leituras-aula-07.md).

### Avaliação

| Componente | Peso |
|---|---|
| Média aritmética das **5 melhores** notas nas 7 listas | 35% |
| **Avaliação final** | 65% |

Estilo de listas e da avaliação: [rules/00_estilo_avaliacao.md](00_estilo_avaliacao.md).

## Bibliografia

### Básica

| Arquivo em `Livros/` | Obra | Uso |
|---|---|---|
| `Pablo Kurlat - A Course in Modern Macroeconomics (2020)...pdf` | **Kurlat (2020)** | **Livro-texto.** Toda questão, solução e resumo ancora aqui primeiro (capítulo + seção). |
| `Benigno_2015_NewKeynesianEconomics_AS_AD_View.pdf` | **Benigno (2015)**, *Research in Economics* 69: 503-524 | Aulas 8-9. Referência por **seção** (1-12). |
| `Programa_Macro1_MPE_2026.pdf` | Programa | Escopo, avaliação, cronograma. |

Kurlat online: https://sites.google.com/view/pkurlat/a-course-in-modern-macroeconomics

### Complementar

| Obra | Uso |
|---|---|
| **Jones (2020)**, 5ª ed. | Intuição e dados de crescimento (Aulas 2-3); cap. 8 *Inflation* (pp. 211-239) é o melhor complemento da Aula 7 |
| Manual do instrutor do Jones | Exercícios resolvidos — ⚠️ edição de **2016**, não casa com o texto de 2020 |
| **Romer (2012)**, 4ª ed. | Rigor formal em Solow; cap. 11 *Inflation and Monetary Policy* (pp. 513-583) |
| Manual de soluções do Romer | Soluções — checar contra a edição do texto |
| **Carlin & Soskice (2024)** | AD-AS/3 equações — contraste com o Benigno (Aulas 8-9) |
| Williamson — manual de soluções (2014) | ⚠️ **Só o manual** — o livro-texto não está no projeto |
| Ljungqvist & Sargent (2018) | ⚠️ **Fora do escopo.** Não usar como base de exercícios ou soluções |

### ⚠️ Divergências de edição (importante para páginas)

Ao gerar linhas `Ref:` com página, use sempre a edição **do arquivo local** e diga qual é.
Offsets medidos em [Map/books-index.md](../Map/books-index.md): Kurlat **0**, Benigno **−502**,
Jones **+25**, Romer **+22**, Carlin & Soskice **+24**.

| Obra | Programa cita | Arquivo local |
|---|---|---|
| Carlin & Soskice | 2006, *Imperfections, Institutions and Policies* | **2024**, *Institutions, Instability, and Inequality* |
| Romer | 5ª ed. (2018) | **4ª ed. (2012)** |
| Williamson | 6ª ed. (2017) | manual de soluções de **2014** |

## Índice de regras de conteúdo

| Arquivo | Cobre |
|---|---|
| [00_estilo_avaliacao.md](00_estilo_avaliacao.md) | Estilo de listas, simulados e correção |
| [01_mensuracao_agregados.md](01_mensuracao_agregados.md) | Contabilidade nacional, PIB, comparações, IDH |
| [02_crescimento_solow.md](02_crescimento_solow.md) | Fatos do crescimento, mecânica do Solow |
| [03_solow_evidencias.md](03_solow_evidencias.md) | Regra de Ouro, progresso tecnológico, PTF |
| [04_consumo_poupanca.md](04_consumo_poupanca.md) | Consumo estático e intertemporal |
| [05_trabalho_lazer.md](05_trabalho_lazer.md) | Mercado de trabalho, oferta de trabalho |
| [06_equilibrio_geral.md](06_equilibrio_geral.md) | EG em 2 e infinitos períodos, 1º TBE |
| [07_moeda_inflacao.md](07_moeda_inflacao.md) | Moeda, demanda por moeda, inflação e custos |
| [08_adas_microfundamentos.md](08_adas_microfundamentos.md) | Microfundamentos de AD e AS |
| [09_adas_politica.md](09_adas_politica.md) | Política no AD-AS novo-keynesiano |
| [10_notebooklm_prompts.md](10_notebooklm_prompts.md) | Regras dos prompts do NotebookLM (R0: sempre perguntar escopo) |

> Os pacotes de governança (`core`, `context`, `codebase-work`, `model-routing`,
> `lang-python`, `macroeconomics`) vieram do **Efficient Token** e estão listados em
> [INDEX.md](INDEX.md). São outra coisa: governam **como o agente trabalha**, não o conteúdo.

## Estrutura do projeto

| Diretório | Conteúdo |
|---|---|
| `Aula/` | Slides e materiais das 9 aulas |
| `Listas/` | Listas de exercícios (PDF) + `lista-exam.tex` |
| `Livros/` | Livro-texto, Benigno, complementares, programa |
| `Monitoria/` · `Prova/` | Monitoria (Fred); avaliação final e provas anteriores |
| `Simulados/` | Quizzes em MD, consumidos por `quiz.html` |
| `Resolucao/` | Soluções geradas (`/solution`, `/exam-gen`, `/exam-grade`) |
| `Leituras/` | Extratos de capítulo (PDF + MD) e roteiros narrados (`/speechify`) |
| `Notebooks/` | Projetos Jupyter (`/lab`) — um subdiretório por projeto |
| `Videos/` | Vídeos animados (`/explainer`) — um subdiretório por vídeo |
| `rules/` | Regras de conteúdo (acima) + pacotes de governança |
| `Map/` | Mapas de referência cruzada (Obsidian) |
| `NotebookLM/` | Prompts de slides/áudio/vídeo + `sources/` |
| `.agent/` | `plans/` e `notes/` — plano antes de mudança não trivial, achados persistidos |
| `tools/` | `sync_rules.py`, `token_report.py` e afins (do Efficient Token) |

> `Notebooks/` e `Videos/` nascem no primeiro uso. Artefatos pesados (cache, render, áudio)
> estão no `.gitignore`; versiona-se código, plano e proveniência.
