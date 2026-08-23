# Tópico 8 — Modelo AD-AS Novo-Keynesiano: Microfundamentos

> **Aula 8** — Microfundamentos das curvas de demanda (AD) e oferta (AS) agregadas;
> equilíbrios de curto e longo prazos
> **Benigno (2015)** — **seções 1-5** (*Research in Economics* 69: 503-524)
> **Complementar** — Carlin & Soskice (2024); Romer (2012), cap. 6
> **Lista de Exercícios 6**
>
> ⚠️ Referenciar por **seção** (1-12) e equação numerada, não por capítulo.

---

## O modelo em uma frase

Um modelo novo-keynesiano de **dois períodos** — curto prazo e longo prazo — com
**concorrência monopolística** e **rigidez de preços** no curto prazo, resolvido
graficamente no plano **(nível de preços $p$, produto $y$)**. Tudo em log-desvios do estado
estacionário; letras minúsculas são logs.

## Ingredientes

- **Famílias** maximizam $u(C)-v(L)+\beta\{u(\bar C)-v(\bar L)\}$ sujeito à restrição
  orçamentária **intertemporal**. (Barra = longo prazo.)
- **Firmas** — muitos produtores de bens diferenciados, com demanda
  $Y(j) = (P(j)/P)^{-\theta}(C+G)$ e tecnologia linear $Y(j)=AL(j)$.
- **Rigidez:** no curto prazo, uma fração $\alpha$ das firmas mantém o preço fixo em $P^e$
  (fixado antes dos choques) e atende à demanda; a fração $1-\alpha$ otimiza. **No longo
  prazo todas ajustam.**
- Utilidade isoelástica: $\tilde\sigma$ = EIS no consumo; $\eta$ = inverso da elasticidade
  de Frisch, com $v(L)=L^{1+\eta}/(1+\eta)$.

## A curva AD

Da equação de Euler $u_c(C) = \beta(1+i)\frac{P}{\bar P}u_c(\bar C) $, log-linearizada, e de
$y = s_c c + g$:

$$\boxed{y = \bar y_n + (g-\bar g) - \sigma\left[\,i - (\bar p - p) - (\bar\tau_c - \tau_c) - \rho\,\right]} \tag{21}$$

com $\sigma \equiv \tilde\sigma s_c$ e $\rho \equiv -\ln\beta$.

**Por que a AD é decrescente — e por que o motivo é *diferente* do IS-LM.**
Dado $\bar p$, um $p$ maior hoje reduz a inflação esperada $(\bar p - p)$, **eleva o juro
real** $r = i - (\bar p - p)$, induz mais poupança e derruba o consumo corrente. É um
canal **intertemporal**. No AD-AS de livro-texto a inclinação vem da demanda por moeda
(preços altos → demanda por liquidez → juros sobem). Aqui **não há curva LM**: o
instrumento de política é a **taxa de juros nominal $i$**, não a oferta de moeda.

### O que desloca a AD para cima (↑)

| Curto prazo | Longo prazo (expectativas) |
|---|---|
| $i \downarrow$ (política monetária expansionista) | $\bar p \uparrow$ (preços futuros mais altos) |
| $\tau_c \downarrow$ (imposto sobre consumo hoje) | $\bar c_n \uparrow$ — por $\bar a \uparrow$, $\bar g \downarrow$, $\bar\mu_\theta \downarrow$, $\bar\tau_{y,w,l} \downarrow$, $\bar\tau_c \uparrow$ |
| $g \uparrow$ (gasto público hoje) | |

> A dependência de $\bar c_n$ é o coração do modelo: **expectativas sobre o futuro deslocam
> a demanda hoje**, pelo motivo de suavização de consumo.

## A curva AS

Firmas que ajustam praticam **markup sobre custo marginal**: $P(j)=(1+\tilde\mu)W/A$. Com
$p = \alpha p^e + (1-\alpha)\tilde p$, chega-se a

$$\boxed{p - p^e = \kappa\,(y - y_n)} \tag{17, 20}$$

uma "curva de Phillips novo-clássica": **desvios não antecipados de preço** respondem ao
**hiato do produto**.

- **Positivamente inclinada.** Mais produto → mais custo marginal real → firmas flexíveis
  sobem preços.
- **Inclinação $\kappa$.** Depende da fração $\alpha$ de firmas com preço rígido: **quanto
  maior $\alpha$, menor $\kappa$, mais horizontal a AS** — atividade se move muito e preços
  pouco.
- **Truque gráfico essencial:** a AS **sempre passa pelo ponto $(p^e,\ y_n)$**. Para
  deslocá-la, ache o novo $y_n$ e trace a curva pelo novo par.

## Produto natural × produto eficiente

**Natural** ($y_n$) — o que prevaleceria com **preços flexíveis**:

$$y_n = \frac{1+\eta}{\sigma^{-1}+\eta}\,a + \frac{\sigma^{-1}-1}{\sigma^{-1}+\eta}\,g - \frac{1}{\sigma^{-1}+\eta}\,\mu \tag{15}$$

**Eficiente** ($y_e$) — o que um planejador escolheria maximizando $u(C)-v(L)$ s.a.
$Y=C+G$ e $Y=AL$:

$$y_e = \frac{1+\eta}{\sigma^{-1}+\eta}\,a + \frac{\sigma^{-1}-1}{\sigma^{-1}+\eta}\,g \tag{19}$$

$$\Longrightarrow\quad \boxed{y_n - y_e = -\frac{\mu}{\sigma^{-1}+\eta}}$$

> **Este é o resultado que organiza a Aula 9.** Produtividade $a$ e gasto público $g$
> deslocam natural e eficiente **na mesma proporção**. O **markup $\mu$** desloca só o
> natural — é a única fonte de **ineficiência**, e por isso a única que gera **trade-off**
> para a política monetária.

O markup agregado combina poder de monopólio e tributos:
$1+\mu = (1+\mu_\theta)\dfrac{(1+\tau_w)(1+\tau_c)}{(1-\tau_y)(1-\tau_l)}$, com
$\mu_\theta = \dfrac{\theta}{\theta-1}-1$.

## Equilíbrio de curto e de longo prazo

**Curto prazo:** intersecção de AD (21) e AS (17) determina $(p, y)$ **simultaneamente**.
Política monetária **não é neutra** — $i$ move $y$ real, por causa da rigidez.

**Longo prazo:** todas as firmas ajustam, $y = y_n$, a **curva de Phillips é vertical** e
vale a **dicotomia clássica**. Política monetária determina apenas $\bar p$ (é **neutra**);
política fiscal **não** é neutra — impostos elevam o markup e reduzem produto e consumo.

**Juro real natural** — o $i$ que entrega simultaneamente $y=y_n$ e $p=p^e$:

$$r_n = \rho + \sigma^{-1}(\bar y_n - y_n) + \sigma^{-1}(g - \bar g) + (\bar\tau_c - \tau_c)$$

Fixar $i = r_n$ é a referência de política do modelo inteiro.

---

## Padrões de código (Python)

```python
import numpy as np
import matplotlib.pyplot as plt

# --- parametros ---
SIGMA, ETA, KAPPA, RHO = 1.0, 1.0, 0.5, 0.02

def y_natural(a=0.0, g=0.0, mu=0.0, sigma=SIGMA, eta=ETA):
    inv = 1 / sigma
    return ((1 + eta) * a + (inv - 1) * g - mu) / (inv + eta)

def y_eficiente(a=0.0, g=0.0, sigma=SIGMA, eta=ETA):
    inv = 1 / sigma
    return ((1 + eta) * a + (inv - 1) * g) / (inv + eta)

# --- curvas ---
AS = lambda y, pe, yn: pe + KAPPA * (y - yn)          # p = pe + kappa (y - yn)
def AD(y, i, ybar_n, p_bar=0.0, g=0.0, gbar=0.0, dtau_c=0.0):
    """Inverte (21) para p em funcao de y."""
    return p_bar - (ybar_n + (g - gbar) - y) / SIGMA - (i - dtau_c - RHO)

# --- equilibrio de curto prazo: AS = AD ---
def equilibrio(i, a=0.0, g=0.0, mu=0.0, pe=0.0, p_bar=0.0, ybar_n=0.0):
    yn = y_natural(a, g, mu)
    # pe + k(y-yn) = p_bar - (ybar_n + g - y)/sigma - (i - RHO)
    num = p_bar - ybar_n / SIGMA - g / SIGMA - (i - RHO) - pe + KAPPA * yn
    y = num / (KAPPA + 1 / SIGMA)
    return y, AS(y, pe, yn), yn

def juro_natural(yn, ybar_n=0.0, g=0.0, gbar=0.0):
    return RHO + (ybar_n - yn) / SIGMA + (g - gbar) / SIGMA

y_eq, p_eq, yn = equilibrio(i=RHO, a=0.05)     # choque de produtividade transitorio
print(f"y={y_eq:.4f}  p={p_eq:.4f}  yn={yn:.4f}  hiato={y_eq-yn:.4f}")
```

---

## Armadilhas frequentes

1. **Trazer a LM.** Não existe curva LM aqui — o BC fixa $i$.
2. Justificar a inclinação da AD pelo canal de demanda por moeda (raciocínio IS-LM). O
   canal correto é **intertemporal**, via juro real e inflação esperada.
3. Confundir **eixo vertical = nível de preços $p$** com inflação $\pi$. É nível.
4. Esquecer que a AS passa por $(p^e, y_n)$ — sem essa âncora, os deslocamentos saem
   errados.
5. **Confundir $y_n$ com $y_e$.** Só coincidem quando $\mu$ não se move. Todo o Tópico 9
   depende dessa distinção.
6. Dizer que "mais rigidez torna a AS mais inclinada" — é o contrário: $\alpha\uparrow$
   ⇒ $\kappa\downarrow$ ⇒ AS **mais plana**.
7. Aplicar neutralidade monetária no **curto prazo** — ela vale só no longo.
8. ⚠️ **Não** substituir a AS deste modelo pela NKPC de Calvo
   ($\pi_t = \kappa x_t + \beta E_t\pi_{t+1}$). O próprio Benigno (nota 7) diz que essa
   complicação está fora do escopo pedagógico.
