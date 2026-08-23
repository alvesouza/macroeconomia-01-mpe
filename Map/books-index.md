---
tags: [map, cross-reference, macro1, registro, study-pack]
date: 2026-08-21
---

# Índice de Livros — sumário e mapeamento de páginas

#map/books

Usado por `/study-pack` (extrai páginas de PDF) e pelas linhas `Ref:` de gabaritos e
resumos. Voltar ao [[00_indice]].

> Para os **exercícios** — número, página, subtópico e nível, um por linha — veja
> [[exercises-index]]. Este arquivo mapeia **seções**; aquele mapeia **exercícios**.

> **Offset** = `página_no_PDF − página_impressa`. Para extrair a página impressa $p$ de um
> PDF, use `p + offset`. Offsets medidos automaticamente contra os rodapés dos próprios
> arquivos em `Livros/`.

## Offsets

| Sigla | Obra | Arquivo em `Livros/` | Págs PDF | Offset |
|---|---|---|---|---|
| **KUR** | Kurlat (2020) | `Pablo Kurlat - A Course in Modern Macroeconomics (2020) - libgen.li.pdf` | 320 | **0** |
| **BEN** | Benigno (2015) | `Benigno_2015_NewKeynesianEconomics_AS_AD_View.pdf` | 22 | **−502** |
| **JON** | Jones (2020, 5ª ed.) | `Charles I. Jones - Macroeconomics (2020...).pdf` | 657 | **+25** |
| **ROM** | Romer (2012, 4ª ed.) | `(The Mcgraw-Hill...) David Romer-Advanced Macroeconomics, 4th edition...pdf` | 738 | **+22** |
| **C&S** | Carlin & Soskice (2024) | `Macrkeconomics_ Institutions, Instability, and Inequality{...}.pdf` | 969 | **+24** |

- **Kurlat: offset 0** — página impressa = página do PDF. Conveniente.
- **Benigno** é artigo de periódico, paginado 503-524: `pdf = impressa − 502`
  (p. 503 → PDF 1; p. 524 → PDF 22).
- Manuais de soluções (Romer, Jones 2016, Williamson 2014) não têm offset medido — são
  usados por número de exercício, não por página.

---

## Kurlat (2020) — sumário com páginas

Páginas impressas = páginas do PDF.

### Parte I — GDP and Living Standards (p. 13)

| Cap./Seção | Título | Pág. | Aula |
|---|---|---|---|
| **1** | **GDP** | **15** | [[01_mensuracao_agregados]] |
| 1.1 | GDP Accounting | 15 | 1 |
| 1.2 | Making Comparisons | 22 | 1 |
| — | *Exercises 1.x* | **27** | 1 |
| **2** | **Beyond GDP** | **31** | [[01_mensuracao_agregados]] |
| 2.1 | The Human Development Index | 31 | 1 |
| 2.2 | Beyond GDP | 33 | 1 |
| — | *Exercises 2.x* | **40** | 1 |

### Parte II — Economic Growth (p. 45)

| Cap./Seção | Título | Pág. | Aula |
|---|---|---|---|
| **3** | **Basic Facts about Economic Growth** | **47** | [[02_crescimento_solow]] |
| 3.1 | The Very Long Run | 47 | 2 |
| 3.2 | The Kaldor Facts | 48 | 2 |
| 3.3 | Growth Across Countries | 51 | 2 |
| — | *Exercises 3.x* | **51** | 2 |
| **4** | **The Solow Growth Model** | **53** | [[02_crescimento_solow]] / [[03_solow_evidencias]] |
| 4.1 | Ingredients of the Model | 53 | **2** |
| 4.2 | Mechanics | 57 | **2** |
| 4.3 | The Golden Rule | 61 | **3** |
| 4.4 | Markets | 63 | **3** |
| 4.5 | Technological Progress | 69 | **3** |
| — | *Exercises 4.x* | **72** | 2-3 |
| **5** | **Theory and Evidence** | **75** | [[03_solow_evidencias]] |
| 5.1 | The Kaldor Facts Again | 75 | 3 |
| 5.2 | Putting Numbers on the Model | 77 | 3 |
| 5.3 | The Capital Accumulation Hypothesis | 80 | 3 |
| 5.4 | Growth Accounting | 86 | 3 |
| 5.5 | TFP Differences | 89 | 3 |
| — | *Exercises 5.x* | **93** | 3 |

> ⚠️ **O cap. 4 é dividido entre duas aulas.** Aula 2 = §4.1-4.2; Aula 3 = §4.3-4.5.

### Parte III — Microeconomic Foundations (p. 101)

| Cap./Seção | Título | Pág. | Aula |
|---|---|---|---|
| **6** | **Consumption and Saving** | **103** | [[04_consumo_poupanca]] |
| 6.1 | Keynesian | 103 | 4 |
| 6.2 | Two Period Model | 105 | 4 |
| 6.3 | Many periods | 117 | 4 |
| 6.4 | Behavioral Theories | 120 | 4 |
| — | *Exercises 6.x* | **121** | 4 |
| **7** | **Labor and Leisure** | **127** | [[05_trabalho_lazer]] |
| 7.1 | Measuring the Labor Market | 127 | 5 |
| 7.2 | Static Model | 131 | 5 |
| 7.3 | Evidence | 137 | 5 |
| 7.4 | A Dynamic Model | 140 | 5 |
| 7.5 | Equilibrium in the Labor Market | 142 | 5 |
| — | *Exercises 7.x* | **146** | 5 |
| ~~**8**~~ | ~~**Investment**~~ | ~~151~~ | ⚠️ **FORA DO ESCOPO** |
| **9** | **General Equilibrium** | **165** | [[06_equilibrio_geral]] |
| 9.1 | Two-Period Economy | 165 | 6 |
| 9.2 | First Welfare Theorem | 168 | 6 |
| 9.3 | Infinite-Period Economy | 172 | 6 |
| — | *Exercises 9.x* | **179** | 6 |

### Parte IV — Money and Inflation (p. 189)

| Cap./Seção | Título | Pág. | Aula |
|---|---|---|---|
| **10** | **Money** | **191** | [[07_moeda_inflacao]] |
| 10.1 | What is Money? | 191 | 7 |
| 10.2 | The Supply of Money | 192 | 7 |
| 10.3 | Changing the Supply of Money | 194 | 7 |
| 10.4 | The Demand for Money | 199 | 7 |
| — | *Exercises 10.x* | **202** | 7 |
| **11** | **The Price Level and Inflation** | **205** | [[07_moeda_inflacao]] |
| 11.1 | Measurement | 205 | 7 |
| 11.2 | Equilibrium | 208 | 7 |
| 11.3 | Seignorage | 215 | 7 |
| 11.4 | The Cost of Inflation | 217 | 7 |
| — | *Exercises 11.x* | **218** | 7 |

### Capítulos 12-15 — fora do escopo

O livro continua até o cap. 15 (exercícios nas pp. 237, 258, 285, 310). **Nada disso é
cobrado.** O programa termina no cap. 11, e as Aulas 8-9 usam o Benigno.

---

## Benigno (2015) — seções

Artigo, pp. 503-524. `pdf = impressa − 502`.

| Seção | Título | Pág. impressa | Pág. PDF | Aula |
|---|---|---|---|---|
| 1 | Introduction | 503 | 1 | 8 |
| 2 | Background literature | 504 | 2 | 8 |
| 3 | **Aggregate demand** | 505 | 3 | **8** |
| 4 | **Aggregate supply** | 506 | 4 | **8** |
| 4.1 | The short run | 507 | 5 | 8 |
| 4.2 | The long run | 508 | 6 | 8 |
| 4.3 | Policies | 508 | 6 | 8 |
| 4.4 | The efficient level of output | 508 | 6 | 8 |
| 5 | **The AS-AD model** | 509 | 7 | **8** |
| 6 | **Productivity shocks** | 511 | 9 | **9** |
| 6.1 | A temporary productivity shock | 512 | 10 | 9 |
| 6.2 | A permanent productivity shock | 512 | 10 | 9 |
| 6.3 | Optimism or pessimism on future productivity | 513 | 11 | 9 |
| 7 | **Mark-up shocks** | 513 | 11 | **9** |
| 8 | **Fiscal multipliers** | 514 | 12 | **9** |
| 9 | **Liquidity trap** | 517 | 15 | **9** |
| 10 | **The economics of debt deleveraging** | 519 | 17 | **9** |
| 11 | **Optimal monetary policy** | 521 | 19 | **9** |
| 12 | Conclusion | 523 | 21 | 9 |

**Equações-chave para citar:**

| Eq. | O que é |
|---|---|
| (3)-(5) | Equação de Euler → base da AD |
| (6), (8), **(21)** | **Curva AD** log-linear |
| (15) | **Produto natural** $y_n$ |
| **(17), (20)** | **Curva AS** — $p-p^e=\kappa(y-y_n)$ |
| (19) | **Produto eficiente** $y_e$ |
| (13) | Markup agregado $\mu$ com tributos |

**Figuras** (úteis para reproduzir em TikZ): Fig. 1-2 (AS), Fig. 3-4 (AD e deslocamentos),
Fig. 5 (equilíbrio $E$), Fig. 6 (choque transitório), Fig. 7 (permanente), Fig. 8
(otimismo), Fig. 9 (markup / estagflação).

---

## Materiais do curso convertidos para MD

Além dos livros, o material do professor também está em MD (convertido com `/convert`),
o que permite citar aula e lista por conteúdo:

| Arquivo MD | O que é |
|---|---|
| `Aula/MPE_Macro1_SlidesAula2.md` | Aula 2 — *Economic Growth* |
| `Aula/Handout_MPE_Macro1_Aula3_2026(1).md` | Aula 3 — handout (texto corrido, 42 KB) |
| `Aula/MPE_Macro1_SlidesAula4.md` | Aula 4 — *Microfoundations I: Consumption and Saving* |
| `Livros/MPE_Macro1_2026_Slides_1.md` | Aula 1 — Mensuração |
| `Listas/MPE_Macro1_2026_Lista1.md` · `Lista2.md` · `Lista3.md` | Listas 1-3 |
| `Livros/Programa_Macro1_MPE_2026.md` | Programa da disciplina |

> ⚠️ A conversão de PDF de slides embaralha tabelas e fórmulas (é *markitdown* sobre um
> layout de duas colunas). Serve para **localizar** um tópico e citar a aula; para ler a
> derivação, volte ao PDF.

---

## Como usar com os comandos

```bash
# extrai as paginas de Solow (Kurlat 53-72) num PDF unico
/study-pack Resolucao/remediacao-solow.md

# plano de exercicios apontando itens reais
/exercise-plan "Solow e contabilidade do crescimento"
#   -> ex.: "Kurlat, Exercício 4.3 (p. 72)"; "Kurlat, Exercício 5.2 (p. 93)"

# linha Ref: num gabarito
#   Ref: Kurlat (2020), cap. 4, §4.3 (p. 61)
#   Ref: Benigno (2015), §6.1 e Fig. 6 (p. 512)
```
