# Tópico 9 — AD-AS Novo-Keynesiano: Análise de Política Econômica

> **Aula 9** — Análise de políticas econômicas através do gráfico AD-AS
> **Benigno (2015)** — **seções 6-12**
> **Complementar** — Carlin & Soskice (2024); Romer (2012), cap. 11
>
> Pré-requisito direto: [Tópico 8](08_adas_microfundamentos.md). Toda a análise aqui é
> **estática comparativa gráfica** sobre as curvas AD (21) e AS (17).

---

## Método (aplicar sempre nesta ordem)

1. **O choque move $y_n$?** Recalcule $y_n$ por (15) e reposicione a AS pelo ponto
   $(p^e, y_n')$.
2. **O choque move a AD?** Só se afetar $i$, $g$, $\tau_c$, $\bar p$ ou o **futuro**
   ($\bar c_n$, via $\bar a$, $\bar g$, $\bar\mu$).
3. **Ache o novo equilíbrio** $E'$ e leia $p$, $y$ e o **hiato** $y - y_n$.
4. **Compare com $y_e$** (19) — é o hiato relevante para bem-estar.
5. **Qual política restaura o ótimo?** Mova a AD com $i$ até o ponto desejado — e diga se
   há **trade-off**.

---

## § 6. Choques de produtividade

| Choque | AS | AD | Resultado sem política | Política ótima |
|---|---|---|---|---|
| **6.1 Transitório** ($a\uparrow$, $\bar a$ igual) | ↓ (desce, $y_n\uparrow$) | não move | $p\downarrow$, $y\uparrow$, mas **hiato negativo** | **Expansionista**: $i\downarrow$ desloca AD até $E''$ — preços estáveis e hiato zero |
| **6.2 Permanente** ($a\uparrow$ e $\bar a\uparrow$) | ↓ | ↑ (sobe: $\bar c_n\uparrow$, suavização) | $E'$ já tem preços estáveis e hiato zero | **Neutra** — $r_n$ não muda, pois $y_n$ e $\bar y_n$ sobem na mesma proporção |
| **6.3 Otimismo** (só $\bar a\uparrow$) | não move | ↑ | $p\uparrow$, $y\uparrow$ **acima** do natural e do eficiente | **Restritiva**: $i\uparrow$ traz a AD de volta a $E$ |

> **A lição da seção 6** (cai em prova): com choques de produtividade **não há trade-off** —
> a política monetária sempre consegue estabilizar preços **e** fechar o hiato ao mesmo
> tempo (*divine coincidence*). Mas **a direção depende da natureza do choque**:
> transitório → **expansionista**; permanente → **neutra**; apenas esperado → **restritiva**.

## § 7. Choques de markup

Aumento temporário de $\mu$ — por poder de monopólio ($\mu_\theta\uparrow$), por tributos
($\tau_w,\tau_l,\tau_y\uparrow$) ou por **preço de insumo inelástico (petróleo)**.

- $y_n \downarrow$ → **AS sobe**. Mas $y_e$ **não se move**.
- Firmas sobem preços; o juro real sobe; famílias poupam mais; demanda e produto caem.
- Resultado: $p\uparrow$ com $y\downarrow$ — **estagflação**.

> **Aqui existe trade-off.** Estabilizar preços exige contrair a AD e afundar mais o produto
> abaixo do eficiente; fechar o hiato eficiente exige aceitar inflação. É a diferença entre
> um choque **eficiente** (produtividade) e um choque **ineficiente** (markup) — a hipótese
> de **salários flexíveis** é o que garante ausência de trade-off no caso anterior.

## § 8. Multiplicadores fiscais

**Em tempos normais:**

| Instrumento | Multiplicador sobre $y$ | Sobre o **hiato** $y-y_n$ |
|---|---|---|
| $g \uparrow$ (gasto público) | positivo, **menor que 1** | positivo e **bem menor** |
| $\tau_c \downarrow$ (corte de imposto) | **positivo** | **negativo** |

Por que o multiplicador do gasto é $<1$: $g\uparrow$ desloca a AD para cima, mas também
eleva $y_n$ (efeito riqueza negativo sobre o lazer, eq. 15) e sobe preços — parte do
estímulo vaza. E o corte de imposto eleva $y$ sem elevar $y_n$ na mesma medida, mas o sinal
sobre o **hiato relevante** se inverte, o que torna a leitura contraintuitiva.

> **Moral:** avaliar política fiscal por multiplicador **sobre o produto** é enganoso.
> O que importa para bem-estar é o hiato contra o **eficiente**.

## § 9. Armadilha de liquidez

O limite inferior sobre a nominal, $i \ge 0$ (ZLB), **trava a AD**: ela não pode ser
deslocada mais para cima por política convencional.

- **Origem** (Krugman, 1998): o juro real de equilíbrio $r_n$ fica **negativo** — por más
  perspectivas de crescimento de longo prazo ($\bar a\downarrow$) ou porque agentes estão
  desalavancando. A AD desce junto com $\bar{AD}$; a economia fica presa abaixo do potencial.
- **Saída:** o instrumento que sobra é a **determinação dos preços de longo prazo $\bar p$**
  — agir sobre **expectativas**. Comprometer-se com $\bar p$ mais alto eleva a inflação
  esperada $(\bar p - p)$, **reduz o juro real** com $i=0$ e desloca a AD para cima.
  Exige **credibilidade** do compromisso.

## § 10. Desalavancagem (Eggertsson & Krugman, 2012)

Dois tipos de agentes — **tomadores** e **poupadores** — com limite de dívida $D$.
Uma queda súbita de $D$ (choque de desalavancagem) força os tomadores a cortar consumo:

- Contração forte da AD → a economia pode **cair na armadilha de liquidez**.
- **A política fiscal fica muito mais potente** — o multiplicador "pode ser bem grande",
  porque não há crowding-out via juros (o juro está travado no piso) e há agentes
  restritos que gastam tudo.
- Surgem os **paradoxos**: da poupança (todos tentam poupar e a renda cai), do trabalho e
  da flexibilidade — medidas que seriam expansionistas em tempos normais viram
  contracionistas, pois derrubam preços esperados e **elevam** o juro real.

## § 11. Política monetária ótima

O modelo microfundado entrega uma função objetivo natural: a **utilidade do consumidor**,
bem aproximada por uma **perda quadrática**

$$\mathcal{L} = (p - p^e)^2 + \lambda\,(y - y_e)^2$$

— desvios de preço não antecipados e hiato contra o **eficiente** (não contra o natural).

- **Choques de produtividade** → $y_n = y_e$ se movem juntos → ambos os termos zeram
  simultaneamente. Basta acompanhar $r_n$: $i = r_n$. **Sem trade-off.**
- **Choques de markup** → $y_n \ne y_e$ → os dois termos não zeram juntos. O ótimo é
  **acomodar parcialmente**, aceitando algum movimento de preços e algum hiato, com o peso
  $\lambda$ determinando a repartição.
- **Interpretação gráfica:** o BC escolhe onde, ao longo da AS deslocada, colocar a AD.
  Sob metas de inflação estritas, escolhe $p=p^e$; sob metas flexíveis, um ponto
  intermediário.

## § 12. Síntese

O modelo entrega, com duas curvas e álgebra de duas equações: não-neutralidade de curto
prazo e neutralidade de longo prazo, resposta ótima a choques reais e de custo, ZLB,
desalavancagem e o caso para metas de inflação — sem recorrer a LM nem a NKPC de Calvo.

---

## Padrões de código (Python)

```python
import numpy as np
import matplotlib.pyplot as plt

SIGMA, ETA, KAPPA, RHO = 1.0, 1.0, 0.5, 0.02
inv = 1 / SIGMA

y_natural  = lambda a=0, g=0, mu=0: ((1 + ETA) * a + (inv - 1) * g - mu) / (inv + ETA)
y_eficiente = lambda a=0, g=0:      ((1 + ETA) * a + (inv - 1) * g) / (inv + ETA)

def equilibrio(i, a=0, g=0, mu=0, a_bar=0, pe=0, p_bar=0):
    """Retorna (y, p, y_n, y_e). a_bar entra via ybar_n (desloca a AD)."""
    yn, ye = y_natural(a, g, mu), y_eficiente(a, g)
    ybar_n = y_natural(a_bar)
    num = p_bar - (ybar_n + g) / SIGMA - (i - RHO) - pe + KAPPA * yn
    y = num / (KAPPA + inv)
    return y, pe + KAPPA * (y - yn), yn, ye

def i_otimo(a=0, g=0, mu=0, a_bar=0):
    """Juro que zera o hiato contra o EFICIENTE mantendo p = pe."""
    from scipy.optimize import brentq
    f = lambda i: equilibrio(i, a, g, mu, a_bar)[0] - y_eficiente(a, g)
    return brentq(f, -5, 5)

# --- a taxonomia da secao 6 ---
for nome, kw in [("transitorio", dict(a=0.05)),
                 ("permanente",  dict(a=0.05, a_bar=0.05)),
                 ("otimismo",    dict(a_bar=0.05))]:
    y, p, yn, ye = equilibrio(i=RHO, **kw)
    print(f"{nome:12s} y={y:+.4f} p={p:+.4f} hiato_n={y-yn:+.4f} "
          f"hiato_e={y-ye:+.4f} i*={i_otimo(**kw):+.4f}")

# --- armadilha de liquidez: i nao pode cair abaixo de zero ---
def equilibrio_zlb(i_desejado, **kw):
    return equilibrio(max(i_desejado, 0.0), **kw)
```

---

## Armadilhas frequentes

1. **Medir o hiato contra $y_n$ quando a questão é de bem-estar.** A referência de
   bem-estar é $y_e$. Com choque de markup os dois divergem — e é exatamente aí que a
   pergunta é feita.
2. Dizer que a política ótima é sempre expansionista diante de choque de produtividade
   positivo. **Depende**: transitório → expansionista; permanente → neutra; otimismo →
   **restritiva**.
3. Deslocar a AS "para cima" e a AD junto num choque **transitório** de produtividade — a
   AD **não se move** (só o $\bar a$ a move).
4. Afirmar que existe trade-off em todo choque. Só há trade-off quando o choque separa
   $y_n$ de $y_e$ — isto é, choques de **markup**.
5. Concluir que corte de imposto sobre consumo melhora o hiato — o multiplicador sobre o
   **hiato** é **negativo** (§8).
6. Tratar a ZLB como se anulasse toda a política monetária. Sobra o canal de
   **expectativas** ($\bar p$).
7. Aplicar as conclusões de tempos normais (multiplicador $<1$) a uma economia em
   desalavancagem — lá o multiplicador é grande.
8. Esquecer que o resultado "sem trade-off" pressupõe **salários flexíveis** (nota 9 do
   artigo).
