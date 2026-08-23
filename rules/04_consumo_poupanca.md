# Tópico 4 — Microfundamentos: Consumo e Poupança

> **Aula 4** — Determinantes da decisão de consumo e poupança em um modelo estático;
> e em um modelo intertemporal
> **Kurlat (2020)** — cap. **6**
> **Complementar** — Romer (2012), cap. 8; Williamson, caps. 4 e 9
> **Lista de Exercícios 3**

---

## Por que microfundamentar

No Solow, $s$ é exógena. Aqui ela vira **resultado de escolha ótima** de um consumidor que
maximiza utilidade sujeito a uma restrição orçamentária. Isso permite (i) fazer estática
comparativa com fundamento, (ii) avaliar bem-estar, (iii) prever como a poupança responde a
juros, impostos e expectativas.

## Modelo de dois períodos

**Preferências:** $U(c_1, c_2) = u(c_1) + \beta u(c_2)$, com $u' > 0$, $u'' < 0$ e
$\beta = \dfrac{1}{1+\rho} \in (0,1)$ o fator de desconto ($\rho$ = taxa de preferência
intertemporal).

**Restrições período a período:**
$$c_1 + a = y_1, \qquad c_2 = y_2 + (1+r)a$$

**Restrição orçamentária intertemporal (RIO)** — elimine $a$:

$$\boxed{c_1 + \frac{c_2}{1+r} = y_1 + \frac{y_2}{1+r} \equiv W}$$

O preço relativo do consumo futuro é $\dfrac{1}{1+r}$. $W$ é a **riqueza da vida toda**.

**Problema e solução.** $\max u(c_1)+\beta u(c_2)$ s.a. RIO. A CPO é a **equação de Euler**:

$$\boxed{u'(c_1) = \beta(1+r)\,u'(c_2)}$$

Interpretação: na margem, o custo de utilidade de poupar uma unidade hoje iguala o
benefício descontado de consumi-la amanhã. Se $\beta(1+r) = 1$, então $c_1 = c_2$ —
**suavização perfeita**.

### Caso log e CRRA

| Utilidade | Euler | Solução |
|---|---|---|
| $u(c)=\ln c$ | $\dfrac{c_2}{c_1} = \beta(1+r)$ | $c_1 = \dfrac{W}{1+\beta}$, $\ c_2=\dfrac{\beta(1+r)W}{1+\beta}$ |
| $u(c)=\dfrac{c^{1-\sigma}-1}{1-\sigma}$ | $\dfrac{c_2}{c_1} = [\beta(1+r)]^{1/\sigma}$ | $c_1 = \dfrac{W}{1+\beta^{1/\sigma}(1+r)^{(1/\sigma)-1}}$ |

$\sigma$ = coeficiente de aversão relativa ao risco; $1/\sigma$ = **elasticidade de
substituição intertemporal (EIS)**.

> Com **log** ($\sigma=1$), efeitos renda e substituição de $r$ se cancelam exatamente:
> $c_1$ **não depende de $r$** dada a riqueza. É o caso-referência da aula.

### Efeito de um aumento de $r$ sobre a poupança

| Canal | Direção sobre $s_1$ | Por quê |
|---|---|---|
| **Substituição** | ↑ | consumo futuro ficou mais barato |
| **Renda** | ↓ (se **poupador**) | o poupador ficou mais rico |
| **Renda** | ↑ (se **tomador**) | o devedor ficou mais pobre |

Efeito líquido **ambíguo** para um poupador; depende de $\sigma$. Para $\sigma<1$
(EIS > 1), domina a substituição.

## Estática comparativa essencial

- **$y_1 \uparrow$ transitório** — $W$ sobe pouco; consumo sobe pouco em ambos os períodos;
  **poupança sobe muito**.
- **$y_1$ e $y_2 \uparrow$ permanente** — $W$ sobe muito; consumo sobe quase 1-a-1;
  **poupança quase não muda**.
- Este contraste é a **Hipótese da Renda Permanente**: o consumo responde a mudanças de
  *riqueza*, não de renda corrente. Testável e o coração da aula.

## Extensões

- **Restrição de crédito** ($a \ge 0$): se a solução irrestrita pedia $a<0$, a restrição
  binds e $c_1 = y_1$ — o consumidor volta a ser "mão-a-boca" e a **sensibilidade à renda
  corrente reaparece**.
- **Horizonte infinito:** $\max \sum_{t=0}^{\infty}\beta^t u(c_t)$ s.a.
  $\sum_t \dfrac{c_t}{(1+r)^t} = \sum_t \dfrac{y_t}{(1+r)^t} + (1+r)a_0$, com a condição de
  **No-Ponzi**. Euler vale entre quaisquer dois períodos consecutivos.
- **Equivalência ricardiana:** se o governo corta impostos hoje e os eleva no futuro com o
  mesmo valor presente, $W$ não muda e $c$ não muda — a poupança privada sobe exatamente o
  tanto que a pública caiu. Depende de horizonte infinito, ausência de restrição de
  crédito e impostos *lump-sum*.

---

## Padrões de código (Python)

```python
import numpy as np
from scipy.optimize import brentq

BETA, R = 0.96, 0.04

def riqueza(y1, y2, r=R):
    return y1 + y2 / (1 + r)

# --- solução fechada CRRA (sigma=1 => log) ---
def consumo_otimo(y1, y2, r=R, beta=BETA, sigma=1.0):
    W = riqueza(y1, y2, r)
    razao = (beta * (1 + r)) ** (1 / sigma)       # c2/c1
    c1 = W / (1 + razao / (1 + r))
    return c1, razao * c1

def poupanca(y1, y2, **kw):
    c1, _ = consumo_otimo(y1, y2, **kw)
    return y1 - c1

# --- verificar a Euler numericamente ---
def euler_residuo(c1, c2, r=R, beta=BETA, sigma=1.0):
    up = lambda c: c ** (-sigma)
    return up(c1) - beta * (1 + r) * up(c2)

# --- transitório vs. permanente ---
base = poupanca(100, 100)
print("choque transitorio:", poupanca(110, 100) - base)   # poupança sobe muito
print("choque permanente :", poupanca(110, 110) - base)   # poupança quase não muda
```

---

## Armadilhas frequentes

1. Escrever a RIO descontando $c_2$ por $(1+r)$ em vez de dividir — inverter o desconto.
2. Confundir **fator** de desconto $\beta$ com **taxa** $\rho$.
3. Afirmar que $r\uparrow$ sempre eleva a poupança — ignora o efeito renda.
4. Tratar $1/\sigma$ (EIS) como se fosse $\sigma$ (aversão ao risco).
5. Aplicar a equivalência ricardiana sem checar as hipóteses (crédito, horizonte, tipo de
   imposto).
6. Esquecer que, com restrição de crédito ativa, a Euler vale como **desigualdade**
   ($u'(c_1) > \beta(1+r)u'(c_2)$), não igualdade.
