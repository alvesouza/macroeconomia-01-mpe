# Tópico 2 — Crescimento Econômico: Fatos Básicos e Modelo de Solow

> **Aula 2** — Fatos do crescimento de longo prazo; crescimento comparado de países;
> ingredientes e mecânica básica do Modelo de Solow
> **Kurlat (2020)** — cap. **3** e seções **4.1-4.2**
> **Complementar** — Jones (2020), caps. 3-5; Romer (2012), cap. 1
> **Lista de Exercícios 1**

---

## Fatos estilizados do crescimento

**Fatos de Kaldor** (economias desenvolvidas, horizonte longo):
1. $Y/L$ cresce a taxa aproximadamente constante.
2. $K/L$ cresce a taxa aproximadamente constante.
3. A razão $K/Y$ é aproximadamente constante.
4. A taxa de retorno do capital $r$ é aproximadamente constante.
5. As **participações de capital e trabalho** na renda são aproximadamente constantes.
6. As taxas de crescimento **diferem** muito entre países.

Fatos entre países:
- Dispersão enorme de renda per capita (razão de ~30-50× entre os extremos).
- **Sem convergência absoluta** na amostra mundial; há **convergência condicional**.
- "Milagres" e "desastres" de crescimento — mudanças de posição relativa são possíveis.

## Ingredientes do modelo de Solow

**Função de produção** com retornos constantes de escala (CRS), produtividade marginal
positiva e decrescente, e condições de Inada:

$$Y_t = F(K_t, A_t L_t), \qquad \text{Cobb-Douglas: } Y_t = K_t^{\alpha}(A_t L_t)^{1-\alpha}$$

**Leis de movimento** (versão básica, $A$ constante):

$$K_{t+1} = (1-\delta)K_t + I_t, \qquad I_t = sY_t, \qquad L_{t+1} = (1+n)L_t$$

- $s$ — taxa de poupança/investimento, **exógena e constante** (esta é a hipótese central,
  e é o que será microfundamentado a partir da Aula 4).
- $\delta$ — depreciação; $n$ — crescimento populacional.
- Economia **fechada e sem governo**: $S = I$.

## Forma intensiva

Com CRS, divida por $L$: $k \equiv K/L$, $y \equiv Y/L$, $y = f(k) = k^{\alpha}$.

**Equação fundamental de Solow** (tempo discreto):

$$k_{t+1} = \frac{(1-\delta)k_t + s f(k_t)}{1+n}$$

Aproximação em tempo contínuo (a mais usada em prova):

$$\dot{k} = s f(k) - (n+\delta)k$$

- $sf(k)$ — **investimento efetivo** por trabalhador.
- $(n+\delta)k$ — **investimento de reposição** (*break-even*): repõe a depreciação e
  equipa os novos trabalhadores.

## Estado estacionário

$\dot k = 0 \Rightarrow s f(k^*) = (n+\delta)k^*$. Com Cobb-Douglas:

$$k^* = \left(\frac{s}{n+\delta}\right)^{\frac{1}{1-\alpha}}, \qquad
y^* = \left(\frac{s}{n+\delta}\right)^{\frac{\alpha}{1-\alpha}}, \qquad
c^* = (1-s)y^*$$

**Estabilidade:** o estado estacionário é globalmente estável (para $k>0$). Se $k<k^*$,
$\dot k>0$; se $k>k^*$, $\dot k<0$. As condições de Inada garantem existência e unicidade.

### Estática comparativa

| Choque | $k^*$ | $y^*$ | crescimento de $y$ no LP |
|---|---|---|---|
| $s \uparrow$ | ↑ | ↑ | **0** (só efeito de nível) |
| $n \uparrow$ | ↓ | ↓ | **0** |
| $\delta \uparrow$ | ↓ | ↓ | **0** |

> **O resultado central da Aula 2:** no Solow básico **não há crescimento de longo prazo de
> $y$**. Aumentar a poupança gera crescimento apenas na **transição** — um efeito de nível,
> não de taxa. Crescimento sustentado exige progresso tecnológico (Aula 3).

## Convergência

- **Absoluta** — países pobres crescem mais rápido. Falha na amostra mundial.
- **Condicional** — controlando por $s$, $n$, $\delta$, cada país converge ao **seu**
  $k^*$; quanto mais longe do próprio estado estacionário, mais rápido cresce.
- A velocidade de convergência decorre da **produtividade marginal decrescente** do
  capital.

---

## Padrões de código (Python)

```python
import numpy as np
import matplotlib.pyplot as plt

ALPHA, S, DELTA, N = 1/3, 0.25, 0.05, 0.01
f = lambda k: k ** ALPHA

def k_estrela(s=S, n=N, delta=DELTA, alpha=ALPHA):
    return (s / (n + delta)) ** (1 / (1 - alpha))

def trajetoria(k0, T=200, s=S, n=N, delta=DELTA):
    """Tempo discreto: k_{t+1} = [(1-delta)k_t + s f(k_t)] / (1+n)."""
    k = np.empty(T + 1)
    k[0] = k0
    for t in range(T):
        k[t + 1] = ((1 - delta) * k[t] + s * f(k[t])) / (1 + n)
    return k

# --- diagrama de Solow ---
k = np.linspace(0.01, 1.5 * k_estrela(), 400)
fig, ax = plt.subplots()
ax.plot(k, S * f(k), label=r"$s\,f(k)$")
ax.plot(k, (N + DELTA) * k, label=r"$(n+\delta)k$")
ax.axvline(k_estrela(), ls=":", color="gray")
ax.set_xlabel("$k$"); ax.set_ylabel("por trabalhador"); ax.legend()
```

---

## Armadilhas frequentes

1. **Confundir efeito de nível com efeito de taxa.** $s\uparrow$ eleva $y^*$, não $g_y$
   de longo prazo. Este é o erro #1 em prova.
2. Esquecer o $(1+n)$ no denominador da versão em tempo discreto.
3. Escrever a reta de reposição como $\delta k$, omitindo $n$.
4. Não declarar se $k$ é **por trabalhador** ou **por unidade de eficiência** (Aula 3).
5. Tratar $s$ como escolha ótima — no Solow ela é **exógena** por hipótese.
6. Confundir convergência **absoluta** com **condicional** ao ler evidência empírica.
