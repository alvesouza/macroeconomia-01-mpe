# Tópico 6 — Microfundamentos: Teoria de Equilíbrio Geral

> **Aula 6** — Equilíbrio geral em uma economia de dois períodos; primeiro teorema do
> bem-estar; equilíbrio geral em uma economia de infinitos períodos
> **Kurlat (2020)** — cap. **9**
> **Complementar** — Romer (2012), cap. 2; Williamson, caps. 5 e 11
> **Lista de Exercícios 5**
>
> ⚠️ **Kurlat cap. 8 está fora do escopo** — o programa salta do cap. 7 para o cap. 9.

---

## O que muda em relação às aulas anteriores

Nas Aulas 4-5 os preços ($r$, $w$) eram **dados** ao agente. Aqui eles são **determinados
endogenamente** pelo equilíbrio dos mercados. A pergunta deixa de ser "como o agente
responde a $r$" e passa a ser "qual $r$ torna os planos de todos mutuamente compatíveis".

## Equilíbrio competitivo em dois períodos

**Ingredientes:**
- **Famílias** — maximizam $u(c_1)+\beta u(c_2)$ s.a. a restrição intertemporal, tomando
  $r$ e $w$ como dados. Dotações $y_1, y_2$ (ou trabalho e propriedade das firmas).
- **Firmas** — maximizam lucro; escolhem $K$ e $L$ com $F_K = r+\delta$ e $F_L = w$.
- **Mercados** — bens em cada período, e o mercado de **crédito/ativos**.

### Definição (sempre escreva assim numa prova)

Um **equilíbrio competitivo** é um vetor de alocações $\{c_1, c_2, a, K, L\}$ e um vetor de
preços $\{r, w\}$ tais que:
1. dados os preços, a alocação das famílias resolve o problema de **maximização de
   utilidade** sujeito à restrição orçamentária;
2. dados os preços, a alocação das firmas resolve a **maximização de lucro**;
3. **todos os mercados se equilibram** (*market clearing*).

### Condição de equilíbrio do mercado de crédito

Em economia fechada, sem governo e com agente representativo, a poupança agregada líquida é
zero:

$$a = 0 \quad\Longleftrightarrow\quad c_1 = y_1,\ \ c_2 = y_2$$

Substituindo na equação de Euler, o **juro de equilíbrio** sai como preço que sustenta essa
alocação:

$$\boxed{1+r^* = \frac{u'(y_1)}{\beta\,u'(y_2)}}$$

Com $u = \ln c$: $1+r^* = \dfrac{y_2}{\beta y_1}$.

**Leitura:** o juro real de equilíbrio é alto quando (i) os agentes são impacientes
($\beta$ baixo) ou (ii) a economia está crescendo ($y_2/y_1$ alto) — pois todos querem
tomar emprestado contra o futuro, e o juro precisa subir para desestimulá-los. Não há a quem
tomar emprestado no agregado: **o agente representativo não pode negociar consigo mesmo**.

- Com **produção**, o equilíbrio adiciona $c_1 + K = y_1$ e $c_2 = F(K,L)+(1-\delta)K$, e
  o juro se iguala ao produto marginal líquido: $r^* = F_K - \delta$.
- **Lei de Walras:** com $n$ mercados, se $n-1$ se equilibram, o $n$-ésimo também. Use para
  economizar uma equação.

## Primeiro Teorema do Bem-Estar (1º TBE)

> **Enunciado.** Toda alocação de equilíbrio competitivo é **Pareto-eficiente**.

**Hipóteses que fazem o teorema funcionar:**
1. **Mercados completos** — existe mercado para todo bem relevante (inclusive datado).
2. **Concorrência perfeita** — agentes tomam preços como dados, sem poder de mercado.
3. **Ausência de externalidades** e de bens públicos.
4. **Informação** não assimétrica.
5. Não-saciedade local das preferências.

**Prova (por contradição, esboço):** suponha uma alocação factível que Pareto-domine a de
equilíbrio. Por não-saciedade local, ela custaria estritamente mais aos preços de
equilíbrio para pelo menos um agente e não menos para os demais. Somando as restrições
orçamentárias, o custo agregado excederia a riqueza agregada — contradiz a factibilidade.

**Verificação direta:** o problema do **planejador social** que maximiza
$u(c_1)+\beta u(c_2)$ sujeito só à restrição de recursos tem a **mesma CPO** que o
descentralizado. Alocações coincidem; o preço $r^*$ é o multiplicador de Lagrange da
restrição de recursos.

> **2º TBE** (menção): qualquer alocação Pareto-eficiente pode ser descentralizada como
> equilíbrio competitivo **após transferências lump-sum** — exige adicionalmente
> **convexidade** de preferências e tecnologia.

## Horizonte infinito

$$\max_{\{c_t\}} \sum_{t=0}^{\infty}\beta^t u(c_t)
\quad \text{s.a.} \quad a_{t+1} = (1+r_t)a_t + y_t - c_t$$

- **Condição de No-Ponzi:** $\displaystyle\lim_{T\to\infty}\frac{a_{T+1}}{\prod_{t=0}^{T}(1+r_t)} \ge 0$
  — impede financiar consumo rolando dívida para sempre.
- **Condição de transversalidade** (na solução ótima, vale com igualdade):
  $\lim_{T\to\infty}\beta^T u'(c_T)a_{T+1} = 0$. Euler + transversalidade = suficientes com
  concavidade.
- Em equilíbrio com agente representativo e dotação constante $y$:
  $c_t = y$ e $1+r^* = 1/\beta$ — o juro real iguala a **taxa de preferência
  intertemporal** $\rho$.
- Na versão com produção e crescimento a $g$: $1+r^* = (1+g)^{\sigma}/\beta$, ou
  $r \approx \rho + \sigma g$ — a **regra de Ramsey**, que reaparece na Aula 8 como taxa
  natural de juros.

> É aqui que o curso fecha o círculo aberto na Aula 2: a taxa de poupança que o Solow
> assumia exógena passa a ser **escolhida**, e o estado estacionário resultante satisfaz
> $f'(k^*) = \rho + \delta$ (**regra de ouro modificada**) — com $k^* < k_{ouro}$, ou seja,
> **a economia ótima poupa menos que a Regra de Ouro**, porque a impaciência tem valor.

---

## Padrões de código (Python)

```python
import numpy as np
from scipy.optimize import brentq

BETA, SIGMA = 0.96, 2.0
up = lambda c: c ** (-SIGMA)

# --- juro de equilibrio, dotacao em 2 periodos (a = 0) ---
def r_equilibrio(y1, y2, beta=BETA):
    return up(y1) / (beta * up(y2)) - 1

print(r_equilibrio(100, 105))     # economia crescendo => r alto

# --- com producao: r* = F_K - delta ---
def r_producao(K, L, alpha=1/3, A=1.0, delta=0.1):
    return alpha * A * (K / L) ** (alpha - 1) - delta

# --- planejador vs. descentralizado: devem coincidir ---
def planejador(y1, y2, beta=BETA):
    """max u(c1)+beta u(c2) s.a. c1 + c2/(1+r) <= recursos; sem comercio: c=y."""
    return y1, y2      # com agente representativo e dotacao, a alocacao e a propria dotacao

# --- horizonte infinito: r* = 1/beta - 1 com dotacao constante ---
print(1 / BETA - 1)
```

---

## Armadilhas frequentes

1. **Esquecer o market clearing.** Resolver só a Euler dá a *demanda*, não o equilíbrio.
   Com agente representativo, $a=0$ é o que fecha o modelo.
2. Definir equilíbrio sem listar as três condições (otimalidade das famílias, das firmas,
   e clearing). Numa prova, a definição vale pontos por si.
3. Afirmar o 1º TBE **sem enunciar as hipóteses** — é aí que mora a pegadinha de V/F.
4. Confundir **Pareto-eficiente** com **socialmente desejável** — eficiência nada diz sobre
   distribuição.
5. Inverter os teoremas: o 2º TBE precisa de **convexidade**; o 1º, não.
6. Esquecer a **transversalidade** no horizonte infinito e aceitar trajetórias explosivas
   que satisfazem a Euler.
7. Usar a Regra de Ouro (Aula 3) onde o modelo microfundamentado pede a **regra de ouro
   modificada** $f'(k^*)=\rho+\delta$.
