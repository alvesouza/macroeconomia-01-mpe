# Tópico 1 — Mensuração dos Agregados Macroeconômicos

> **Aula 1** — Princípios da contabilidade nacional; medindo produto, dispêndio e renda;
> comparações entre países e ao longo do tempo; além do produto, o desenvolvimento humano
> **Kurlat (2020)** — caps. **1-2**
> **Complementar** — Jones (2020), caps. 2 e 8 (dados e comparações internacionais)
> **Lista de Exercícios 1**

---

## As três óticas do PIB

Identidade fundamental: **produto = dispêndio = renda**.

$$Y = C + I + G + (X - M)$$

- **Produção** — soma do **valor adicionado** de cada setor (evita dupla contagem).
- **Dispêndio** — soma dos gastos finais (a identidade acima).
- **Renda** — salários + lucros + juros + aluguéis + impostos indiretos − subsídios.

Pontos de atenção:
- **Bens finais × intermediários**; variação de estoques entra em $I$.
- **PIB × PNB (RNB)** — território × propriedade dos fatores.
- **Estoque × fluxo** — capital é estoque, investimento é fluxo.
- O que **fica de fora**: produção doméstica não remunerada, economia informal,
  externalidades, depreciação (PIB é *bruto*; PIL é líquido).

## Nominal, real e índices de preço

$$\text{Deflator do PIB}_t = \frac{\text{PIB nominal}_t}{\text{PIB real}_t}\times 100$$

| | Deflator do PIB | Índice de preços ao consumidor (IPC/IPCA) |
|---|---|---|
| Cesta | todos os bens **produzidos** internamente | cesta **fixa** de consumo |
| Tipo | Paasche (peso corrente) | Laspeyres (peso da base) |
| Importados | exclui | inclui |
| Viés | — | viés de substituição, de qualidade, de novos bens |

Taxa de inflação: $\pi_t = \dfrac{P_t - P_{t-1}}{P_{t-1}}$.

**Encadeamento (chain weighting)** — resolve a dependência do ano-base ao usar preços
médios de anos adjacentes.

## Comparações entre países

- Converter a **PPP** (paridade do poder de compra), não a câmbio de mercado — bens
  não-comercializáveis são sistematicamente mais baratos em países pobres
  (efeito **Balassa-Samuelson**).
- Fonte usual: **Penn World Table**.
- PIB **per capita** ≠ PIB **por trabalhador** ≠ PIB **por hora trabalhada**.

## Além do produto

- **IDH** — renda, educação, expectativa de vida (média geométrica dos subíndices).
- Limitações do PIB como medida de bem-estar: distribuição, lazer, saúde, meio ambiente.
- Medidas de desigualdade: curva de Lorenz, **índice de Gini**.

## Aritmética de crescimento (usada o curso inteiro)

- Crescimento em log: $g \approx \ln Y_t - \ln Y_{t-1}$ (bom para $g$ pequeno).
- Composição: $Y_T = Y_0 (1+g)^T$; em tempo contínuo $Y_t = Y_0 e^{gt}$.
- **Regra do 70**: tempo para dobrar $\approx 70/(100g)$ anos.
- Produto de variáveis: $g_{XY} \approx g_X + g_Y$; razão: $g_{X/Y} \approx g_X - g_Y$.

---

## Padrões de código (Python)

```python
import numpy as np
import pandas as pd

# --- PIB real com ano-base fixo vs. deflator ---
def pib_real(qtd: pd.DataFrame, precos_base: pd.Series) -> pd.Series:
    """qtd: linhas = anos, colunas = bens. precos_base: preços do ano-base."""
    return qtd.mul(precos_base, axis=1).sum(axis=1)

def deflator(qtd: pd.DataFrame, precos: pd.DataFrame, precos_base: pd.Series) -> pd.Series:
    nominal = (qtd * precos).sum(axis=1)
    return 100 * nominal / pib_real(qtd, precos_base)

# --- taxa de crescimento média (geométrica, não aritmética) ---
def cagr(serie: pd.Series) -> float:
    n = len(serie) - 1
    return (serie.iloc[-1] / serie.iloc[0]) ** (1 / n) - 1

# --- regra do 70 ---
tempo_para_dobrar = lambda g: np.log(2) / np.log(1 + g)
```

---

## Armadilhas frequentes

1. Somar produção bruta em vez de valor adicionado (dupla contagem).
2. Comparar PIB nominal entre anos ou países sem deflacionar / sem PPP.
3. Tratar transferências (aposentadorias, seguro-desemprego) como parte de $G$.
4. Usar média **aritmética** de taxas de crescimento em vez de geométrica.
5. Confundir *nível* e *taxa de crescimento* na leitura de um gráfico em escala log.
