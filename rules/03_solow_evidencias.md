# Tópico 3 — Crescimento Econômico: Solow (cont.) e Evidências

> **Aula 3** — Regra de Ouro; progresso tecnológico; quantificando o Modelo de Solow;
> contabilidade do crescimento e diferenças de produtividade total dos fatores
> **Kurlat (2020)** — seções **4.3-4.5** e cap. **5**
> **Complementar** — Jones (2020), caps. 4-6; Romer (2012), cap. 1
> **Lista de Exercícios 2**

---

## Regra de Ouro do estoque de capital

Escolhe-se $s$ para **maximizar o consumo de estado estacionário**:

$$\max_{s}\ c^*(s) = f(k^*(s)) - (n+\delta)k^*(s)$$

Condição de primeira ordem:

$$\boxed{f'(k_{ouro}) = n + \delta}$$

Com Cobb-Douglas, $\alpha k^{\alpha-1} = n+\delta$ implica $s_{ouro} = \alpha$: **a taxa de
poupança da Regra de Ouro iguala a participação do capital na renda**.

- $k^* > k_{ouro}$ → **ineficiência dinâmica**: reduzir $s$ eleva o consumo *hoje e
  sempre*. Pareto-melhora inequívoca.
- $k^* < k_{ouro}$ → chegar à Regra de Ouro exige **sacrificar consumo hoje** por mais
  consumo depois — há um trade-off intertemporal genuíno, e o Solow (sem preferências) não
  consegue dizer se compensa. Este gap é a motivação para os microfundamentos da Aula 4.

## Progresso tecnológico

Tecnologia **aumentadora de trabalho** (*labor-augmenting* / Harrod-neutra):

$$Y_t = F(K_t, A_t L_t), \qquad A_{t+1} = (1+g)A_t$$

> Só a forma Harrod-neutra é compatível com uma **senda de crescimento equilibrado**
> (*balanced growth path*) com $K/Y$ constante e função de produção geral. Com
> Cobb-Douglas as três formas (Hicks, Harrod, Solow-neutra) são intercambiáveis.

**Variáveis por unidade de eficiência:** $\tilde k \equiv \dfrac{K}{AL}$,
$\tilde y \equiv \dfrac{Y}{AL}$.

$$\dot{\tilde k} = s f(\tilde k) - (n+g+\delta)\tilde k
\quad\Longrightarrow\quad
\tilde k^* = \left(\frac{s}{n+g+\delta}\right)^{\frac{1}{1-\alpha}}$$

### Taxas de crescimento na senda equilibrada

| Variável | Taxa |
|---|---|
| $\tilde k,\ \tilde y,\ \tilde c$ | 0 |
| $k = K/L,\ y = Y/L,\ c$ | $g$ |
| $K,\ Y,\ C,\ L$ | $n+g$ (exceto $L$, que cresce a $n$) |
| $K/Y$, participações, $r$ | constantes |

> O crescimento de longo prazo do produto **per capita** é $g$ — determinado
> **exogenamente**. O Solow explica a acumulação de capital, mas *não* explica o
> crescimento; ele o assume. Este é o resultado mais importante da Aula 3.

Regra de Ouro com tecnologia: $f'(\tilde k_{ouro}) = n + g + \delta$.

## Quantificando o Solow

Duas perguntas empíricas:

1. **O Solow dá conta das diferenças de renda entre países?** Com $\alpha \approx 1/3$, as
   diferenças observadas de $s$ e $n$ geram diferenças de $y^*$ **muito menores** que as
   observadas. Elasticidade de $y^*$ a $s$ é $\alpha/(1-\alpha) \approx 0{,}5$.
2. **E os retornos do capital?** Se toda a diferença fosse capital, o PMgK em países pobres
   seria absurdamente alto e o capital fluiria para lá — o **paradoxo de Lucas**.

Conclusão: o resíduo — a **PTF** — faz o trabalho pesado.

## Contabilidade do crescimento

Diferenciando $Y = A K^{\alpha} L^{1-\alpha}$ (com $A$ neutra à la Hicks):

$$\underbrace{g_Y}_{\text{produto}} = \underbrace{g_A}_{\text{resíduo de Solow}}
+\ \alpha\, g_K + (1-\alpha)\, g_L$$

Por trabalhador: $g_y = g_A + \alpha\, g_k$.

**Resíduo de Solow:** $g_A = g_Y - \alpha g_K - (1-\alpha)g_L$ — medido por diferença,
"medida da nossa ignorância".

Decomposição de **níveis** (development accounting):

$$y = A\,k^{\alpha} \quad\Longrightarrow\quad
\frac{y_i}{y_{US}} = \frac{A_i}{A_{US}}\left(\frac{k_i}{k_{US}}\right)^{\alpha}$$

Com capital humano: $Y = A K^{\alpha}(hL)^{1-\alpha}$, $h$ estimado por retornos
mincerianos da escolaridade.

- $\alpha$ é calibrado pela **participação do capital na renda** ($\approx 1/3$), não
  estimado por regressão.
- Resultado robusto na literatura: a **PTF** explica a maior parte das diferenças de renda
  entre países; capital físico e humano explicam a menor parte.

---

## Padrões de código (Python)

```python
import numpy as np
import pandas as pd

ALPHA = 1/3

# --- Regra de Ouro ---
def k_ouro(n, g, delta, alpha=ALPHA):
    """f'(k) = n + g + delta  =>  alpha * k^(alpha-1) = n+g+delta"""
    return (alpha / (n + g + delta)) ** (1 / (1 - alpha))

s_ouro = ALPHA          # com Cobb-Douglas, s_ouro = alpha

def consumo_ss(s, n, g, delta, alpha=ALPHA):
    k = (s / (n + g + delta)) ** (1 / (1 - alpha))
    return k**alpha - (n + g + delta) * k

# --- contabilidade do crescimento ---
def residuo_solow(gY, gK, gL, alpha=ALPHA):
    return gY - alpha * gK - (1 - alpha) * gL

# --- development accounting: decompor y_i / y_US ---
def decompor(y_rel, k_rel, alpha=ALPHA):
    """Retorna (contribuicao_capital, contribuicao_PTF) em razões."""
    contrib_k = k_rel ** alpha
    return contrib_k, y_rel / contrib_k
```

---

## Armadilhas frequentes

1. **Confundir $s^*$ com $s_{ouro}$.** Toda taxa de poupança gera *um* estado estacionário;
   só uma maximiza o consumo.
2. Concluir que estar abaixo da Regra de Ouro é ineficiente — **não é**. Só o excesso de
   capital ($k^*>k_{ouro}$) é ineficiência dinâmica.
3. Misturar $k = K/L$ com $\tilde k = K/AL$ no mesmo exercício.
4. Dizer que $\tilde y$ cresce a $g$ na senda equilibrada — ela é **constante**; quem
   cresce a $g$ é $y$.
5. Esquecer o $g$ na reta de reposição $(n+g+\delta)\tilde k$.
6. Estimar $\alpha$ por regressão em vez de calibrar pela participação na renda.
7. Ler o resíduo de Solow como "progresso técnico" puro — ele agrega tudo que não foi
   medido (instituições, alocação, qualidade dos insumos, erro de medida).
