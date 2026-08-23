---
tags: [map, macro1, cobertura, status]
date: 2026-08-21
---

# Cobertura — o que existe e o que falta

Estado do material em **2026-08-21**. Voltar ao [[00_indice]].

| Aula | Regras | Material | Lista | Resolução | Resumo | Quiz | NotebookLM |
|---|---|---|---|---|---|---|---|
| **1** — Mensuração | ✅ | ✅ Slides 1 | ✅ L1 | ✅ | ⬜ | ⬜ | ✅ |
| **2** — Crescimento e Solow | ✅ | ✅ Slides 2 | ✅ L1 | ✅ | ⬜ | ⬜ | ✅ |
| **3** — Solow e evidências | ✅ | ✅ Handout 3 | ✅ L2 | ✅ | ⬜ | ⬜ | ✅ |
| **4** — Consumo e poupança | ✅ | ✅ Slides 4 | ✅ L3 | ⏳ **entrega 24/08** | ⬜ | ⬜ | ✅ |
| **5** — Trabalho e lazer | ✅ | ⬜ | ⬜ L4 | — | ⬜ | ⬜ | ⬜ |
| **6** — Equilíbrio geral | ✅ | ⬜ | ⬜ L5 | — | ⬜ | ⬜ | ⬜ |
| **7** — Moeda e inflação | ✅ | ⬜ | ⬜ L6 | — | ⬜ | ⬜ | ⬜ |
| **8** — AD-AS microfund. | ✅ | ⬜ | ⬜ L6 | — | ⬜ | ⬜ | ⬜ |
| **9** — AD-AS política | ✅ | ⬜ | ⬜ L7? | — | ⬜ | ⬜ | ⬜ |

✅ pronto · ⏳ em aberto com prazo · ⬜ falta · — não se aplica ainda

**O curso está na metade.** Quatro aulas dadas, três listas emitidas, duas resolvidas.
A Lista 3 vence em **24/08/2026** — é o item com prazo mais próximo.

---

## Materiais por diretório

### `Aula/` — 4 de 9 aulas

| Arquivo | Aula | MD? |
|---|---|---|
| `MPE_Macro1_2026_Slides_1.pdf` | 1 — Mensuração | ✅ (em `Livros/`) |
| `MPE_Macro1_SlidesAula2.pdf` | 2 — *Economic Growth* | ✅ |
| `Handout_MPE_Macro1_Aula3_2026(1).pdf` | 3 — Solow, Regra de Ouro, PTF | ✅ |
| `MPE_Macro1_SlidesAula4.pdf` | 4 — *Microfoundations I: Consumption and Saving* | ✅ |

> A Aula 3 veio como **handout** (texto corrido), não como slides — é o material mais
> denso até agora, 42 KB de MD contra ~20 KB dos slides.

### `Listas/` — 3 de 7

| Arquivo | Lista | Entrega | MD? |
|---|---|---|---|
| `MPE_Macro1_2026_Lista1.pdf` | 1 (10 pts) | 10/08/2026 | ✅ |
| `MPE_Macro1_2026_Lista2.pdf` | 2 (10 pts) | 17/08/2026 | ✅ |
| `MPE_Macro1_2026_Lista3.pdf` | 3 | **24/08/2026** | ✅ |
| `lista-exam.tex` | template LaTeX (`\ifsolucoes`) | — | — |

### `Resolucao/`

| Arquivo | O que é |
|---|---|
| `lista1_resolucao.tex` / `.pdf` | Resolução da Lista 1 |
| `lista1_codigo/` | `q1_pib.py`, `q3_convergencia.py`, `q3_figura.py`, `q4_solow.py`, `estilo_mpl.py` |
| `lista2_resolucao.tex` / `.pdf` | Resolução da Lista 2 |
| `lista2_codigo/` | `l2q1_coreia.py`, `l2q2_gotham.py`, `l2_figuras.py`, `estilo_mpl.py` |
| `kurlat_solutions_ch1-4.tex` / `.pdf` | Soluções dos exercícios do Kurlat, caps. 1-4 |
| `fig/` | 5 figuras PDF (Solow, trajetórias, convergência, crime) |

### `Pedro/Soluções/Lista 1/`

`lista-1-questao-3.ipynb` + `.pdf`, `pwt110.xlsx` (Penn World Table 11.0), `q03.png` —
trabalho próprio sobre a Q3 (convergência) da Lista 1.

### `NotebookLM/`

`README.md` + `sources/` (16 PDFs prontos para upload) + **40 prompts** em `slides/` (16),
`video/` (16) e `audio/` (8) — 10 por aula, para as Aulas 1 a 4. Ver [[00_indice]].

### Livros convertidos para MD — todos

| Obra | MD | Tamanho |
|---|---|---|
| Kurlat (2020) | ✅ | 901 KB |
| Benigno (2015) | ✅ | 93 KB |
| Jones (2020) | ✅ | 1.828 KB |
| Romer (2012) | ✅ | 1.970 KB |
| Romer — manual de soluções | ✅ | 1.215 KB |
| Carlin & Soskice (2024) | ✅ | 2.999 KB |
| Jones — manual do instrutor (2016) | ✅ | 739 KB |
| Williamson — manual de soluções (2014) | ✅ | 319 KB |
| Ljungqvist & Sargent (2018) | ✅ (⚠️ fora do escopo) | 4.296 KB |
| Programa | ✅ | 5 KB |

---

## Conteúdo das listas emitidas

### Lista 1 — 10 pontos · entrega 10/08/2026

| # | Pts | Base | Kurlat | O que pede |
|---|---|---|---|---|
| 1 | 3 (0,6/item) | cap. 1 | ≈ **1.2** | (a) PIB nominal 2024/2025 · (b) PIB real a preços de 2024 e crescimento · (c) PIB real a preços de 2025 — **explicar a diferença** (Laspeyres × Paasche) · (d) PIB colombiano a câmbio de mercado · (e) a **PPP**, e explicar a diferença |
| 2 | 2 | cap. 2 | = **2.2** (p. 41) | Exercício do livro, atribuído pelo número |
| 3 | 2 | cap. 3 | = **3.3** (p. 52) | Exercício do livro, atribuído pelo número |
| 4 | 3 (1,5/item) | cap. 4 | ≈ **4.1** + **4.2** | Solow em estado estacionário, terremoto destrói **metade do capital**: (a) curto e longo prazo sobre PIB e PIB per capita · (b) idem, com $n$ **caindo pela metade** por emigração |

### Lista 2 — 10 pontos · entrega 17/08/2026

| # | Pts | Base | Kurlat | O que pede |
|---|---|---|---|---|
| 1 | 4 | cap. 4 | = **4.3** *Korean Unification* | Coreias do Norte e do Sul como economias de Solow com $\alpha$ e $A$ **diferentes** ($\alpha_N=0{,}25$, $A_N=4$; $\alpha_S=0{,}5$, $A_S=5$; $s_S=0{,}30$, $n_S=0{,}01$; $s_N=0{,}16$, $n_N=0{,}03$; $\delta=0{,}05$). (a) $k_0$ e $y_0$ · (b) $k^*$ como função dos parâmetros · (c) **unificação** com a tecnologia do Sul — de onde vem o ganho? · (d) bônus: Coreia unificada |
| 2 | 6 | cap. 5 | autoral, sobre §5.3-5.4 | "Gotham": para cada unidade de capital produtivo, as firmas investem $\phi$ em segurança, e o estatístico **não separa os dois**. (a) produto em função de $A,K,L,\alpha,\phi$ · (b) problema da firma e **shares** medidos · (c) *development accounting* — que $\tilde{A}$ o analista obtém? · (d) WayneTech corta $\phi$ para $\phi/4$: usar a eq. **(5.4.2)** e mostrar que o efeito inteiro é reportado como **crescimento da PTF**, com $A$ constante |

### Lista 3 — entrega **24/08/2026** ⏰

| # | Pts | Base | Kurlat | O que pede |
|---|---|---|---|---|
| 1 | 5 | cap. 6 | = **6.1** (+ item de **6.3**) | Problema de 2 períodos com impostos e riqueza inicial, $u(c)=c^{1-\sigma}/(1-\sigma)$. (a) $c_1,c_2,a$ em forma fechada · (b) $c_1/y_1$ vs. $y_2$ (otimismo) · (c) $\partial c_1/\partial r$ e **o papel de $\sigma$** (renda × substituição) · (d) efeito da tributação · (e) só o **valor presente** $\tau_1+\tau_2/(1+r)$ importa → **equivalência ricardiana** |
| 2 | — | cap. 6 | = **6.5** (+ item de **6.6**) | Variante com **restrição de crédito** $a \ge -b$. (a) o que a restrição significa, o que é $b$ · (b) dois exemplos em que ela morde · (c) resolver nos **dois casos** (ativa e inativa) · (d) imposto sobre o **retorno da poupança** vs. *lump-sum* de mesma receita — qual margem cada um distorce |

> **Padrão confirmado nas três listas** — usar em `/exam-gen`, detalhado em [[exercises-index]]:
> 1. Cada lista anuncia seu capítulo ("Based on Kurlat (2020, Cap. N)").
> 2. Metade dos itens é exercício do livro (pelo número ou recalibrado); a outra metade é
>    **autoral e recontextualizada** — Brasil × Colômbia, Coreia, Gotham.
> 3. **O último item de cada questão é o mais conceitual** e vale a maior parte do
>    julgamento: Laspeyres × Paasche, origem do ganho da unificação, resíduo de Solow como
>    má alocação, equivalência ricardiana, qual margem o imposto distorce.

---

## Lacunas conhecidas

- **Materiais das Aulas 5-9** ainda não disponibilizados.
- **Listas 4-7** ainda não emitidas. A atribuição da Lista 7 à Aula 9 é inferência — o
  programa anuncia 7 listas mas só mapeia até a 6.
- **Resolução da Lista 3** pendente (entrega 24/08).
- `Simulados/` **vazio** — nenhum quiz gerado. O ecossistema de quiz está pronto
  (`quiz.html`, `.claude/quiz-validate.py` atualizados em 2026-08-21).
- `Monitoria/`, `Prova/`, `Design/` vazios.
- Nenhum **resumo** (`/summarize`) gerado para nenhuma aula.
- Prompts do NotebookLM só para as **Aulas 1-4** — as demais dependem do material ser
  divulgado, já que cada prompt cita a fonte pelo nome exato do arquivo.

## Próximos passos sugeridos

```bash
/solution Listas/MPE_Macro1_2026_Lista3.md   # prazo 24/08 - prioridade
/quiz-gen Aula/ 20                           # primeiro quiz: Aulas 1-4
/summarize Aula/                             # resumos das 4 aulas dadas
/exercise-plan "consumo e poupanca"          # treino para a Lista 3
```

Quando novos slides e listas chegarem: jogue em `Aula/` e `Listas/`, rode `/convert` e
depois `/study-map .` para atualizar este quadro.
