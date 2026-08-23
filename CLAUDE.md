# Macroeconomia I — MPE Insper (2026, 3º trimestre)

Projeto de estudo da disciplina **Macroeconomia I** do Mestrado Profissional em Economia
do Insper.

| | |
|---|---|
| **Professor** | Pedro G. Duarte (pedro.duarte@insper.edu.br) |
| **Monitor** | Frederico Marco Pereira Gomes — "Fred" (fredericompg@al.insper.edu.br) |
| **Instituição** | Insper Instituto de Ensino e Pesquisa — Mestrado Profissional em Economia |
| **Período** | 2026, 3º trimestre |
| **Bibliografia básica** | Kurlat, Pablo (2020). *A Course in Modern Macroeconomics* |
| **Artigo obrigatório** | Benigno, Pierpaolo (2015). "New-Keynesian economics: An AS–AD view" |

---

## Escopo do curso

A disciplina cobre **cinco grandes temas**, em 9 aulas:

1. Mensuração de agregados macroeconômicos e suas limitações
2. Crescimento econômico de longo prazo
3. Fundamentos microeconômicos: consumo/poupança, lazer/trabalho e equilíbrio geral
4. Moeda e inflação
5. Modelo de demanda e oferta agregadas (AD-AS) para análise de política econômica

Ênfase em **modelos microfundamentados** e na "forma de pensar" da macroeconomia moderna.

### ⚠️ NÃO extrapolar

Todo conteúdo gerado neste projeto — resumos, soluções, quizzes, listas, prompts —
deve ficar **restrito ao escopo acima**. Especificamente:

- **Não** usar modelos, técnicas ou notação que não apareçam em Kurlat (caps. 1-7, 9-11)
  ou em Benigno (2015).
- **Kurlat cap. 8 está FORA do escopo** — o programa salta do cap. 7 (Trabalho e Lazer)
  direto para o cap. 9 (Equilíbrio Geral).
- **Não** introduzir DSGE estocástico, métodos recursivos, programação dinâmica,
  Bellman, RBC estocástico ou econometria de séries temporais. O
  Ljungqvist & Sargent está na pasta `Livros/` mas **não** faz parte do curso.
- **Não** trazer a curva de Phillips novo-keynesiana em forma canônica log-linearizada
  (NKPC de Calvo) — o curso usa a apresentação **AS-AD gráfica** do Benigno.
- Quando um livro complementar for mais rigoroso que o Kurlat, use-o para **intuição e
  contraste**, nunca para elevar o nível técnico exigido.

---

## Conteúdo programático: aula × bibliografia

| Aula | Tópico | Livro principal | Lista | Regras |
|---|---|---|---|---|
| **1** | Mensuração dos Agregados Macroeconômicos | Kurlat, caps. **1-2** | Lista 1 | [01](rules/01_mensuracao_agregados.md) |
| **2** | Crescimento: Fatos Básicos e Modelo de Solow | Kurlat, cap. **3** e **4.1-4.2** | Lista 1 | [02](rules/02_crescimento_solow.md) |
| **3** | Crescimento: Solow (cont.) e Evidências | Kurlat, caps. **4.3-4.5** e **5** | Lista 2 | [03](rules/03_solow_evidencias.md) |
| **4** | Microfundamentos: Consumo e Poupança | Kurlat, cap. **6** | Lista 3 | [04](rules/04_consumo_poupanca.md) |
| **5** | Microfundamentos: Trabalho e Lazer | Kurlat, cap. **7** | Lista 4 | [05](rules/05_trabalho_lazer.md) |
| **6** | Microfundamentos: Teoria de Equilíbrio Geral | Kurlat, cap. **9** | Lista 5 | [06](rules/06_equilibrio_geral.md) |
| **7** | Mercado Monetário e Inflação | Kurlat, caps. **10** e **11** | Lista 6 | [07](rules/07_moeda_inflacao.md) |
| **8** | Modelo AD-AS novo-keynesiano | Benigno (2015), **seções 1-5** | Lista 6 | [08](rules/08_adas_microfundamentos.md) |
| **9** | AD-AS: análise de política econômica | Benigno (2015), **seções 6-12** | — | [09](rules/09_adas_politica.md) |

> **Listas.** O programa anuncia **7 listas** no trimestre, mas mapeia explicitamente
> apenas as Listas 1 a 6. A Lista 7 provavelmente cobre as Aulas 8-9 (Benigno) — confirmar
> com o professor. Só a **Lista 1** está em `Listas/` até agora.

### Avaliação

| Componente | Peso |
|---|---|
| Média aritmética das **5 melhores** notas nas 7 listas | 35% |
| **Avaliação final** | 65% |

O estilo das listas e da avaliação final está especificado em
[rules/00_estilo_avaliacao.md](rules/00_estilo_avaliacao.md) — fonte única de verdade para
`/exam-gen` e `/exam-grade`.

---

## Bibliografia

### Básica (piso de toda referência)

| Arquivo em `Livros/` | Obra | Uso |
|---|---|---|
| `Pablo Kurlat - A Course in Modern Macroeconomics (2020)...pdf` | **Kurlat (2020)** | **Livro-texto do curso.** Toda questão, solução e resumo deve ancorar aqui primeiro (capítulo + seção). |
| `Benigno_2015_NewKeynesianEconomics_AS_AD_View.pdf` | **Benigno (2015)**, *Research in Economics* 69: 503-524 | Aulas 8-9. Referência por **seção** (1-12), não por capítulo. |
| `Programa_Macro1_MPE_2026.pdf` | Programa da disciplina | Escopo, avaliação, cronograma. |

Kurlat online: https://sites.google.com/view/pkurlat/a-course-in-modern-macroeconomics

### Complementar

| Arquivo em `Livros/` | Obra | Uso |
|---|---|---|
| `Charles I. Jones - Macroeconomics (2020)...pdf` | **Jones (2020)**, 5ª ed. | Intuição e dados de crescimento (Aulas 2-3); exposição mais gráfica. |
| `Macroeconomics Instructor&_039_s Manual{Charles I. Jones}(2016)...pdf` | Manual do instrutor do Jones | Exercícios resolvidos — ⚠️ edição de **2016**, não casa com o texto de 2020. |
| `(...) David Romer-Advanced Macroeconomics, 4th edition (2012).pdf` | **Romer (2012)**, 4ª ed. | Rigor formal em Solow e crescimento. |
| `David Romer - Advanced Macroeconomics Solution Manual.pdf` | Manual de soluções do Romer | Soluções — checar contra a edição do texto. |
| `Macrkeconomics_ Institutions, Instability, and Inequality{Carlin, Soskice}(2024)...pdf` | **Carlin & Soskice (2024)** | Modelo AD-AS/3 equações — contraste com o Benigno (Aulas 8-9). |
| `Stephen D. Williamson - Instructor's Solution Manual (2014)...pdf` | Manual de soluções do Williamson | ⚠️ **Só o manual de soluções** — o livro-texto não está no projeto. |
| `Lars Ljungqvist, Thomas J. Sargent - Recursive Macroeconomic Theory (2018)...pdf` | Ljungqvist & Sargent (2018) | ⚠️ **Fora do escopo.** Não citado no programa. Não usar como base de exercícios ou soluções. |

### ⚠️ Divergências de edição (importante para páginas)

O programa cita edições que **não** são as que estão em `Livros/`. Ao gerar linhas `Ref:`
com página, use sempre a edição **do arquivo local** e diga qual é:

| Obra | Programa cita | Arquivo local |
|---|---|---|
| Carlin & Soskice | 2006, *Imperfections, Institutions and Policies* | **2024**, *Institutions, Instability, and Inequality* |
| Romer | 5ª ed. (2018) | **4ª ed. (2012)** |
| Williamson | 6ª ed. (2017) | manual de soluções de **2014** |

Jones (2020, 5ª ed.) é o único complementar em que edição citada e arquivo local coincidem.

---

## Idioma e formato

- **Idioma de saída:** Português (Brasil). Termos técnicos consagrados em inglês podem
  ficar em inglês entre parênteses na primeira ocorrência (ex.: "estado estacionário
  (*steady state*)").
- **Matemática:** LaTeX. Inline `$...$`, display `$$...$$`. Nunca usar `$` solto para
  moeda — escreva "120 reais" ou "R\$ 120" escapado.
- **Código:** **Python** (numpy/pandas/matplotlib). Usado para simulações de Solow,
  contabilidade do crescimento, calibração e gráficos. Sem R.
- **Notação:** seguir Kurlat. Onde o Benigno divergir, declarar a notação usada no início
  da solução.

---

## Índice de regras

| Arquivo | Cobre |
|---|---|
| [rules/00_estilo_avaliacao.md](rules/00_estilo_avaliacao.md) | Estilo de listas, simulados e correção (taxonomia, rubrica, LaTeX) |
| [rules/01_mensuracao_agregados.md](rules/01_mensuracao_agregados.md) | Contabilidade nacional, PIB, comparações, desenvolvimento humano |
| [rules/02_crescimento_solow.md](rules/02_crescimento_solow.md) | Fatos do crescimento, mecânica do Modelo de Solow |
| [rules/03_solow_evidencias.md](rules/03_solow_evidencias.md) | Regra de Ouro, progresso tecnológico, contabilidade do crescimento, PTF |
| [rules/04_consumo_poupanca.md](rules/04_consumo_poupanca.md) | Consumo estático e intertemporal, restrição orçamentária |
| [rules/05_trabalho_lazer.md](rules/05_trabalho_lazer.md) | Mercado de trabalho, oferta de trabalho estática e dinâmica |
| [rules/06_equilibrio_geral.md](rules/06_equilibrio_geral.md) | EG em 2 períodos e infinitos períodos, 1º teorema do bem-estar |
| [rules/07_moeda_inflacao.md](rules/07_moeda_inflacao.md) | Moeda, oferta e demanda por moeda, inflação e seus custos |
| [rules/08_adas_microfundamentos.md](rules/08_adas_microfundamentos.md) | Microfundamentos das curvas AD e AS, equilíbrios de curto e longo prazo |
| [rules/09_adas_politica.md](rules/09_adas_politica.md) | Análise gráfica de políticas no AD-AS novo-keynesiano |

---

## Estrutura do projeto

| Diretório | Conteúdo |
|---|---|
| `Aula/` | Slides e materiais das 9 aulas |
| `Listas/` | Listas de exercícios (PDF) + `lista-exam.tex` (template LaTeX) |
| `Livros/` | Livro-texto, artigo do Benigno, complementares, programa |
| `Monitoria/` | Materiais de monitoria (Fred) |
| `Prova/` | Avaliação final e provas anteriores |
| `Simulados/` | Quizzes em MD, consumidos por `quiz.html` |
| `Resolucao/` | Soluções geradas por `/solution`, `/exam-gen`, `/exam-grade` |
| `rules/` | Regras por tópico (este índice) |
| `Map/` | Mapas de referência cruzada (Obsidian) |
| `NotebookLM/` | Prompts de slides/áudio + `sources/` para upload |
| `Design/` | Material visual auxiliar |
