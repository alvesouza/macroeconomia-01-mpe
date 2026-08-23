# Tópico 7 — Mercado Monetário e Inflação

> **Aula 7** — O que é moeda e como medi-la; a oferta de moeda; teorias de demanda por
> moeda; inflação, medida e custos
> **Kurlat (2020)** — caps. **10** e **11**
> **Complementar** — Jones (2020), caps. 8 e 12; Romer (2012), cap. 11; Williamson, cap. 12
> **Lista de Exercícios 6**

---

## O que é moeda

Três funções: **meio de troca**, **unidade de conta**, **reserva de valor**. A primeira é a
que a distingue — moeda resolve o problema da **dupla coincidência de desejos**.

**Agregados monetários** (do mais líquido ao menos):

| Agregado | Composição (aprox.) |
|---|---|
| **M0 / base monetária** | papel-moeda em poder do público + reservas bancárias |
| **M1** | papel-moeda em poder do público + depósitos à vista |
| **M2** | M1 + depósitos de poupança + títulos privados |
| **M3, M4** | agregados progressivamente menos líquidos (quotas de fundos, títulos públicos) |

No Brasil a série é publicada pelo **Banco Central**.

## Oferta de moeda

**Multiplicador monetário.** Com razão reservas/depósitos $rr$ e razão papel-moeda/depósitos
$cr$:

$$M = m \cdot B, \qquad \boxed{m = \frac{1+cr}{rr+cr}}$$

- $B$ (base) é controlada pelo BC via operações de mercado aberto, redesconto e compulsório.
- $m > 1$ porque bancos operam com **reservas fracionárias**.
- $m$ **não é constante**: cai quando bancos acumulam reservas em excesso ou o público
  retém mais papel-moeda (crises).
- Na prática moderna, o BC opera fixando a **taxa de juros** (Selic) e deixa a quantidade
  de moeda endógena.

## Demanda por moeda

**Teoria quantitativa (TQM).** Equação de trocas — uma **identidade**:

$$MV = PY$$

Vira **teoria** ao supor $V$ estável e $Y$ determinado pelo lado real. Em taxas de
crescimento:

$$\boxed{g_M + g_V = \pi + g_Y}$$

Com $g_V \approx 0$: $\pi \approx g_M - g_Y$. Base da tese de que **"inflação é sempre e em
todo lugar um fenômeno monetário"** — no longo prazo.

**Cambridge / demanda por saldos reais:**

$$\frac{M^d}{P} = L(Y, i), \qquad L_Y > 0,\ \ L_i < 0$$

- $Y$ → **motivo transação**; $i$ → **custo de oportunidade** de reter moeda.
- **Baumol-Tobin** (demanda por estoques): com custo fixo $F$ por saque,
  $$\frac{M^d}{P} = \sqrt{\frac{FY}{2i}}$$
  Elasticidade-renda $=1/2$ e elasticidade-juro $=-1/2$ — economias de escala na gestão de
  caixa.

## Dicotomia clássica e neutralidade

- **Dicotomia clássica:** variáveis reais são determinadas por fatores reais; a moeda fixa
  só o **nível de preços**.
- **Neutralidade da moeda:** mudança de **nível** de $M$ muda $P$ proporcionalmente, sem
  efeito real. Vale no longo prazo (com preços flexíveis).
- **Superneutralidade:** mudança na **taxa de crescimento** de $M$ não afeta variáveis
  reais. Mais forte, e falha na presença de custos de manter encaixes.

**Equação de Fisher:** $i = r + \pi^e$ (exata: $1+i = (1+r)(1+\pi^e)$).
**Efeito de Fisher:** no longo prazo, $\pi\uparrow$ passa integralmente para $i$, com $r$
inalterado.

## Inflação: medida e custos

**Medida:** IPCA (índice oficial de metas no Brasil, IBGE), INPC, IGP-M; deflator do PIB
(ver [Tópico 1](01_mensuracao_agregados.md)). Vieses de Laspeyres: substituição, qualidade,
novos bens, ponto de venda.

**Custos da inflação antecipada:**
- **Custo de sola de sapato** (*shoe-leather*) — economizar encaixes reais é custoso.
- **Custo de menu** — remarcar preços.
- **Distorções tributárias** — o imposto incide sobre ganhos *nominais*.
- **Confusão da unidade de conta** — contabilidade e contratos ficam ruidosos.

**Custos da inflação não antecipada:**
- **Redistribuição arbitrária** entre credores e devedores (a inflação surpresa favorece o
  devedor).
- **Dispersão de preços relativos** → má alocação.
- Incerteza inflacionária eleva prêmios de risco.

**Senhoriagem e imposto inflacionário:**

$$\text{senhoriagem} = \frac{\Delta M}{P}, \qquad
\text{imposto inflacionário} = \pi \cdot \frac{M}{P}$$

A base do imposto é o encaixe real $M/P$, que **encolhe** quando $\pi$ sobe → existe uma
**curva de Laffer da inflação**: acima de certo ponto, mais inflação arrecada menos.
Hiperinflações são o caso-limite, tipicamente originadas em déficits fiscais monetizados.

**Regra de Friedman:** a inflação ótima faz $i = 0$, ou seja $\pi = -r$ — elimina o custo de
oportunidade de reter moeda (deflação moderada). Contrasta com metas de inflação positivas
na prática (viés de medida, rigidez nominal para baixo, espaço para política monetária).

---

## Padrões de código (Python)

```python
import numpy as np

# --- multiplicador monetario ---
def multiplicador(rr, cr):
    return (1 + cr) / (rr + cr)

print(multiplicador(rr=0.10, cr=0.30))    # ~3.25

# --- TQM em taxas de crescimento ---
def inflacao_tqm(gM, gY, gV=0.0):
    return gM + gV - gY

# --- Fisher (exata e aproximada) ---
fisher_exata = lambda r, pi_e: (1 + r) * (1 + pi_e) - 1
fisher_aprox = lambda r, pi_e: r + pi_e

# --- Baumol-Tobin ---
def baumol_tobin(F, Y, i):
    return np.sqrt(F * Y / (2 * i))

# --- curva de Laffer da inflacao, com L = exp(-a*pi) ---
def receita_inflacionaria(pi, a=5.0):
    return pi * np.exp(-a * pi)

grid = np.linspace(0.001, 1.0, 500)
pi_otimo = grid[np.argmax([receita_inflacionaria(p) for p in grid])]
print(f"pico da Laffer: {pi_otimo:.1%}")   # = 1/a
```

---

## Armadilhas frequentes

1. Tratar $MV=PY$ como **teoria** sem declarar as hipóteses ($V$ estável, $Y$ exógeno) —
   como identidade ela é vazia.
2. Confundir **base monetária** com **M1**, ou nível de $M$ com taxa de crescimento de $M$.
3. Confundir **neutralidade** com **superneutralidade** (item clássico de V/F).
4. Usar a Fisher aproximada em regime de inflação alta, onde o termo cruzado importa.
5. Somar senhoriagem e imposto inflacionário como se fossem coisas distintas e aditivas.
6. Concluir que mais inflação sempre arrecada mais — ignora a erosão da base (Laffer).
7. Aplicar a neutralidade no **curto prazo** — é exatamente o que a Aula 8 vai negar.
8. Confundir **inflação** (variação do nível de preços) com **nível de preços alto**.
