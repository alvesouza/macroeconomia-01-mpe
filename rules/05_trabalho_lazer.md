# Tópico 5 — Microfundamentos: Trabalho e Lazer

> **Aula 5** — Como medimos variáveis do mercado de trabalho; teorias estáticas e
> evidências empíricas; teorias dinâmicas
> **Kurlat (2020)** — cap. **7**
> **Complementar** — Jones (2020), cap. 7; Romer (2012), cap. 11
> **Lista de Exercícios 4**

---

## Medindo o mercado de trabalho

População em idade ativa (PIA) divide-se em **ocupados** ($E$), **desocupados** ($U$) e
**fora da força de trabalho** ($N$). Força de trabalho: $L = E + U$.

$$\text{taxa de desemprego} = \frac{U}{E+U}, \qquad
\text{taxa de participação} = \frac{E+U}{\text{PIA}}, \qquad
\text{razão ocupação/população} = \frac{E}{\text{PIA}}$$

- Fonte no Brasil: **PNAD Contínua** (IBGE).
- **Desalentados** saem da força de trabalho → a taxa de desemprego pode **cair** numa
  recessão. Por isso a razão ocupação/população é informativa em paralelo.
- **Margem extensiva** (quem trabalha) × **margem intensiva** (quantas horas). A maior
  parte do ajuste cíclico agregado vem da extensiva.
- Fatos de longo prazo: queda das horas por trabalhador; alta e depois estabilização da
  participação feminina; queda da participação masculina de idade prima.

## Teoria estática: escolha consumo-lazer

Dotação de tempo $\bar h = \ell + h$ (lazer + trabalho). Salário real $w$, renda não-salarial
$\pi$.

$$\max_{c,\ \ell}\ u(c,\ell) \quad \text{s.a.} \quad c = w(\bar h - \ell) + \pi$$

Reescrevendo como **restrição de tempo cheio**: $c + w\ell = w\bar h + \pi$. O salário é o
**preço do lazer**.

**CPO — a taxa marginal de substituição iguala o salário real:**

$$\boxed{\frac{u_{\ell}(c,\ell)}{u_c(c,\ell)} = w}$$

### Efeito de um aumento de $w$

| Canal | Sobre o lazer | Sobre as horas |
|---|---|---|
| **Substituição** | ↓ | ↑ (lazer ficou caro) |
| **Renda** | ↑ | ↓ (lazer é bem normal) |

Efeito líquido **ambíguo** → a curva de oferta de trabalho pode **dobrar para trás**
(*backward-bending*).

**Caso de referência:** $u(c,\ell) = \ln c + \theta \ln \ell$ dá
$\ell = \dfrac{\theta}{1+\theta}\cdot\dfrac{w\bar h+\pi}{w}$. Se $\pi = 0$, o lazer é
**constante** — renda e substituição se cancelam, e as horas não dependem de $w$. É a
preferência compatível com crescimento equilibrado (horas estáveis apesar de $w$ crescer
secularmente).

- Renda não-salarial $\pi \uparrow$ (herança, transferência, renda do cônjuge) → puro
  **efeito renda** → horas caem. É o teste limpo do modelo.
- **Salário de reserva:** $w^r = \dfrac{u_\ell(\pi,\bar h)}{u_c(\pi,\bar h)}$. Se
  $w < w^r$, solução de canto: não participa. Explica a margem extensiva.

### Evidências

- Elasticidade de oferta de trabalho **pequena** na margem intensiva para homens de idade
  prima; **maior** na extensiva e para segundos provedores.
- Elasticidade **de Frisch** (mantendo a utilidade marginal da riqueza constante) é maior
  que a marshalliana — distinção que importa em modelos dinâmicos.

## Teoria dinâmica

**Substituição intertemporal do trabalho.** Com dois períodos e salários $w_1, w_2$, a
escolha responde ao **salário relativo** $w_1/w_2$ e a $r$:

$$\frac{u_\ell(c_1,\ell_1)}{u_\ell(c_2,\ell_2)} = \frac{w_1}{w_2}\cdot\frac{1}{\beta(1+r)}$$

- Choque salarial **transitório** → forte realocação de horas entre períodos (efeito renda
  desprezível).
- Choque **permanente** → efeito renda grande, resposta de horas pequena.
- Mesma lógica transitório-vs-permanente da Aula 4. É o mecanismo que os modelos de ciclo
  real usam para gerar flutuações de emprego — e a crítica empírica é que ele exige
  elasticidades maiores que as microestimadas.

**Busca e emprego (search).** Desemprego como **fenômeno de fluxo**, não de estoque:
com taxa de separação $\lambda$ e taxa de contratação $f$, o desemprego de estado
estacionário é

$$u^* = \frac{\lambda}{\lambda + f}$$

Salário de reserva na busca: aceita-se a oferta $w$ se $w \ge w^r$; seguro-desemprego mais
generoso eleva $w^r$, eleva a duração do desemprego e pode elevar a qualidade do match.

---

## Padrões de código (Python)

```python
import numpy as np
from scipy.optimize import brentq

THETA = 1.5

# --- oferta de trabalho, u = ln c + theta ln l, dotacao hbar ---
def horas(w, pi=0.0, theta=THETA, hbar=1.0):
    lazer = theta / (1 + theta) * (w * hbar + pi) / w
    return max(hbar - lazer, 0.0)

# --- salario de reserva (canto: h = 0) ---
def salario_reserva(pi, theta=THETA, hbar=1.0):
    """w^r = u_l/u_c avaliado em (c=pi, l=hbar)."""
    return theta * pi / hbar

# --- curva de oferta: verificar se dobra para tras ---
ws = np.linspace(0.5, 5, 100)
h_sem_renda = [horas(w, pi=0) for w in ws]     # constante: efeitos se cancelam
h_com_renda = [horas(w, pi=1) for w in ws]     # crescente

# --- desemprego de estado estacionario (fluxos) ---
u_ss = lambda sep, cont: sep / (sep + cont)
print(u_ss(0.02, 0.25))    # ~7.4%
```

---

## Armadilhas frequentes

1. Escrever a restrição como $c = w h$ e esquecer que $h = \bar h - \ell$ — some a dotação
   de tempo e a intuição do preço do lazer.
2. Afirmar que salário maior sempre aumenta as horas — ignora o efeito renda.
3. Concluir "efeitos se cancelam" com log **sem** checar que $\pi = 0$.
4. Confundir **taxa de desemprego** com **razão ocupação/população** ao interpretar dados.
5. Ignorar desalentados ao comparar taxas de desemprego entre ciclos.
6. Usar a elasticidade marshalliana onde o modelo pede a de **Frisch** (dinâmico).
7. Tratar o desemprego de estado estacionário como estoque fixo em vez de resultado de
   fluxos $\lambda$ e $f$.
