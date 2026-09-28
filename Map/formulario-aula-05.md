---
tags: [map, formulario, macro1, trabalho-lazer, dmp, aula-05]
date: 2026-08-30
---

# Formulário — Aula 5: Trabalho e Lazer

**Kurlat (2020), cap. 7** · [[05_trabalho_lazer|regras do tópico]] ·
[[Listas/MPE_Macro1_2026_Lista4|Lista 4]] · [[Resolucao/lista4_resolucao|resolução]] ·
volta ao [[00_indice]]

Dois níveis no mesmo arquivo. O **Nível 1** é cola de prova: só equações, agrupadas por
bloco, sem comentário. O **Nível 2** é a mesma lista anotada — de onde cada fórmula vem,
quando usar e qual é a armadilha. Use o 1 na véspera e o 2 no estudo.

---
---

# NÍVEL 1 — Cola

## A. Medindo o mercado de trabalho — §7.1

$$\text{PIA} = E + U + N, \qquad L = E + U$$

$$u = \frac{U}{E+U}, \qquad
\text{particip.} = \frac{E+U}{\text{PIA}}, \qquad
\frac{\text{ocup.}}{\text{pop.}} = \frac{E}{\text{PIA}}$$

$$v = \frac{V}{L}, \qquad \theta = \frac{V}{U}$$

## B. Escolha estática consumo-lazer — §7.2

$$\bar h = \ell + n, \qquad \widetilde w \equiv (1-\tau)w$$

$$c = \widetilde w\,n + T
\qquad\Longleftrightarrow\qquad
\underbrace{c + \widetilde w\,\ell}_{\text{gasto}} = \underbrace{\widetilde w\,\bar h + T}_{M}$$

$$\boxed{\ \mathrm{TMS} = \frac{u_\ell}{u_c} = \widetilde w\ }$$

**Caso da Lista 4** — $U = \ln c + b\,\dfrac{\ell^{1-\gamma}}{1-\gamma}$, $b,\gamma>0$:

$$b\,c\,\ell^{-\gamma} = \widetilde w
\qquad\Longrightarrow\qquad
\boxed{\ \ell^{\gamma} + b\,\ell = b\,\bar h + \frac{b\,T}{\widetilde w}\ }, \qquad n = \bar h - \ell$$

| Caso | Solução | Oferta |
|---|---|---|
| $T = 0$, qualquer $\gamma$ | $\ell^{\gamma} + b\ell = b\bar h$ | **vertical** |
| $\gamma = 1$, qualquer $T$ | $\ell = \dfrac{b}{1+b}\left(\bar h + \dfrac{T}{\widetilde w}\right)$ | crescente se $T>0$ |
| Orç. equilibrado $T=\tau w n$ | $(1-\tau)\ell^{\gamma} + b\ell = b\bar h$; se $\gamma=1$, $\ell = \dfrac{b}{b+1-\tau}$ | crescente |

**Caso log-log geral do Kurlat** — $u = \ln c + \theta\ln \ell$, renda não-salarial $\pi$:

$$\ell = \frac{\theta}{1+\theta}\cdot\frac{w\bar h + \pi}{w}$$

**Salário de reserva** (canto $\ell = \bar h$, isto é, $n=0$):

$$w^{r} = \frac{u_\ell(T,\bar h)}{u_c(T,\bar h)}\cdot\frac{1}{1-\tau}
= \frac{b\,T\,\bar h^{-\gamma}}{1-\tau}
\qquad\text{participa} \iff w > w^{r}$$

**Estática comparativa**

$$\frac{\partial \ell}{\partial \tau}
 = \frac{b\,T}{w(1-\tau)^{2}\left(\gamma\ell^{\gamma-1}+b\right)} \ge 0,
\qquad
\boxed{\ \frac{\partial n}{\partial \tau}
 = -\frac{b\,T}{w(1-\tau)^{2}\left(\gamma\ell^{\gamma-1}+b\right)} \le 0\ }$$

$$= 0 \iff T = 0$$

$$\frac{\partial \ell}{\partial \widetilde w}
 = \frac{-b\,T}{\widetilde w^{\,2}\left(\gamma\ell^{\gamma-1}+b\right)} \le 0,
\qquad
\frac{d\ln n}{d\tau} = -\frac{\varepsilon}{1-\tau}$$

**Elasticidades**

$$\varepsilon \equiv \frac{\partial n}{\partial \widetilde w}\frac{\widetilde w}{n}
= \frac{\ell^{\gamma} - b\,n}{n\left(\gamma\ell^{\gamma-1}+b\right)}
\qquad\text{(Marshall, não compensada)}$$

$$\boxed{\ \varepsilon^{F}
= \frac{\partial n}{\partial \widetilde w}\frac{\widetilde w}{n}\bigg|_{c}
= \frac{1}{\gamma}\cdot\frac{\ell}{n} = \frac{\ell}{\gamma(\bar h-\ell)}\ }
\qquad\text{(Frisch, } c \text{ constante)}$$

**Decomposição de um aumento de $\widetilde w$**

| Canal | $\ell$ | $n$ |
|---|---|---|
| Substituição (lazer encarece) | ↓ | ↑ |
| Renda (lazer é bem normal) | ↑ | ↓ |
| **Líquido com $\ln c$ e $T=0$** | **0** | **0** |
| **Líquido com $\ln c$ e $T>0$** | ↓ | ↑ |

## C. Oferta de trabalho dinâmica — §7.4

$$\frac{u_\ell(c_1,\ell_1)}{u_\ell(c_2,\ell_2)}
= \beta(1+r)\,\frac{w_1}{w_2}$$

Choque **transitório** de salário → horas respondem muito (Frisch).
Choque **permanente** → horas quase não respondem (efeito renda cancela).

## D. Busca — modelo DMP — §7.5

$$m(V,U) = \mu\,V^{\alpha}U^{1-\alpha}, \qquad \alpha\in(0,1),\ \mu>0,\ \text{CRS}$$

$$\boxed{\ E_{t+1} = \underbrace{(1-s)E_t}_{\text{sobrevivem}}
 + \underbrace{\mu V_t^{\alpha}U_t^{1-\alpha}}_{\text{criação}},
\qquad U_t = L - E_t\ }$$

$$e_{t+1} = (1-s)e_t + \mu v_t^{\alpha}u_t^{1-\alpha}$$

**Taxas** (dependem só de $\theta$, graças aos retornos constantes):

$$\boxed{\ f \equiv \frac{m}{U} = \mu\theta^{\alpha}, \qquad
q \equiv \frac{m}{V} = \mu\theta^{\alpha-1}, \qquad
f = \theta q\ }$$

$$\varepsilon_{f,\theta} = \alpha > 0, \qquad
\varepsilon_{q,\theta} = -(1-\alpha) < 0, \qquad
\alpha + (1-\alpha) = 1$$

Durações esperadas: desemprego $1/f$; vaga $1/q$.

**Estado estacionário** — criação $=$ destruição:

$$sE = m(V,U)
\quad\Longleftrightarrow\quad
\boxed{\ s(1-u) = \mu v^{\alpha}u^{1-\alpha} = f\,u\ }
\quad\Longrightarrow\quad
\boxed{\ u^{\ast} = \frac{s}{s+f} = \frac{s}{s+\mu\theta^{\alpha}}\ }$$

**Curva de Beveridge**

$$\boxed{\ v(u) = \left[\frac{s(1-u)}{\mu}\right]^{1/\alpha}
 u^{-\frac{1-\alpha}{\alpha}}\ }$$

$$\frac{dv}{du} = -\frac{v}{\alpha u}\left[\frac{u}{1-u} + 1-\alpha\right] < 0,
\qquad
\frac{d\ln v}{d\ln u} = -\frac{1}{\alpha}\left[\frac{u}{1-u} + 1-\alpha\right]$$

$$\frac{\partial \ln v}{\partial \ln \mu}\bigg|_{u} = -\frac{1}{\alpha},
\qquad
\frac{\partial \ln v}{\partial \ln s}\bigg|_{u} = +\frac{1}{\alpha}$$

**Externalidade da vaga**

$$\frac{\partial m}{\partial V} = \alpha\,\frac{m}{V} = \underbrace{\alpha q}_{\text{marginal, social}}
\;<\; \underbrace{q}_{\text{médio, privado}},
\qquad \text{cunha} = (1-\alpha)q$$

## E. Geometria — o que gira, o que desloca

| Objeto | Muda o quê | Efeito |
|---|---|---|
| $\tau$ ou $w$, plano $(\ell,c)$ | inclinação $-\widetilde w$ | **gira** a reta em torno de $(\bar h,\,T)$ |
| $T$, plano $(\ell,c)$ | intercepto | **translada** a reta |
| $\theta$, plano $(u,v)$ | variável endógena | **move ao longo** da Beveridge |
| $\mu$ ou $s$, plano $(u,v)$ | parâmetro de fluxo | **desloca** a Beveridge |

![Slutsky decomposition with log-log preferences](aula-05-trabalho/fig/fig_slutsky_loglog.svg)
*$\ln c+1.5\ln\ell$ with no non-wage income ($T=\pi=0$): the wage doubles, substitution (A→B)
cuts leisure to 0.455, income (B→C) restores 0.60. Vertical supply.*

![Beveridge curve: movement along versus shift](aula-05-trabalho/fig/fig_beveridge_along_vs_shift.svg)
*Drawn in the notes' notation: $A_m=\mu$, $\lambda=s$, $1-\xi=\alpha$. Along the curve $\theta=v/u$
changes (rays from the origin). A lower $A_m$ moves the whole curve out.*

## F. Calibrações de referência

| Bloco | Parâmetros | Resultado |
|---|---|---|
| Prescott, EUA (Kurlat Ex. 7.5) | $b=1{,}54$, $\gamma=1$, $\bar h=w=1$, $\tau=0{,}34$, $T=0{,}102$ | $\ell=0{,}700$, $n=0{,}300$, $\varepsilon^F=2{,}33$ |
| Prescott, Europa | $\tau=0{,}53$, $T=0{,}124$ | $\ell=0{,}766$, $n=0{,}234$ — **22,1% menos** horas |
| DMP mensal (EUA) | $s=0{,}02$, $\alpha=0{,}5$, $\mu=0{,}30/\sqrt{0{,}7}$ | $f=0{,}30$, $q=0{,}43$, $\theta=0{,}7$, $u^{\ast}=6{,}25\%$, $v=4{,}4\%$ |

> Estimativas empíricas da elasticidade de Frisch: **0,4 a 1** (Kurlat, Ex. 7.5(l)).
> O modelo de Prescott precisa de 2,33 — é a crítica padrão.

---
---

# NÍVEL 2 — Anotado

## B. Escolha estática consumo-lazer

| Fórmula | De onde vem | Quando usar | Armadilha |
|---|---|---|---|
| $c + \widetilde w\ell = \widetilde w\bar h + T$ | substituir $n = \bar h-\ell$ em $c=\widetilde w n+T$ | **sempre comece por aqui** — transforma a decisão em escolha entre dois bens com preços $1$ e $\widetilde w$ | escrever $c = wn$ e perder a dotação de tempo; usar $w$ em vez de $\widetilde w$ como preço do lazer |
| $\mathrm{TMS} = u_\ell/u_c = \widetilde w$ | dividir as duas CPOs do lagrangiano, eliminando $\lambda$ | é a única equação de comportamento do domicílio | vale para **qualquer** $u(c,\ell)$; não decore a versão específica |
| $b\,c\,\ell^{-\gamma} = \widetilde w$ | a TMS acima com $U=\ln c + b\ell^{1-\gamma}/(1-\gamma)$ | Lista 4, Q1 | $u_c = 1/c$ vem do $\ln$, não do termo do lazer |
| $\ell^{\gamma}+b\ell = b\bar h + bT/\widetilde w$ | isolar $c$ na CPO e substituir na restrição | dá $\ell$ e portanto $n$ | não tem forma fechada em $\gamma$ — e **não precisa ter**: o lado esquerdo é estritamente crescente, então a raiz é única |
| $\ell^\gamma + b\ell = b\bar h$ (caso $T=0$) | mesma equação com $T=0$ | mostrar que a oferta é **vertical** | vale para todo $\gamma$ — quem manda no cancelamento é o $\ln(c)$, não a curvatura do lazer |
| $\ell = \frac{b}{b+1-\tau}$ | orçamento equilibrado $T=\tau w n$, com $\gamma=1$ | quando o governo devolve toda a receita | aqui $\partial n/\partial\tau<0$ **sempre** — o rebate mata o efeito renda |
| $w^r = bT\bar h^{-\gamma}/(1-\tau)$ | TMS avaliada em $(c,\ell)=(T,\bar h)$ | margem extensiva, quem participa | com $T=0$, $w^r=0$: participa-se a qualquer salário |
| $\varepsilon^F = \ell/(\gamma n)$ | CPO com $c$ **fixo**: $\ell = (bc/\widetilde w)^{1/\gamma}$ | comparar com estimativas empíricas | não confundir com $\varepsilon$ marshalliana; o fator $\ell/n$ é grande porque se trabalha pouco do dia |

### As três derivações que valem a pena refazer à mão

**1. Por que a oferta é vertical com $T=0$.** Substitua a restrição na utilidade:
$$\widetilde U(\ell) = \ln\big[\widetilde w(\bar h-\ell)\big] + b\frac{\ell^{1-\gamma}}{1-\gamma}
= \underbrace{\ln\widetilde w}_{\text{constante em }\ell} + \ln(\bar h-\ell) + b\frac{\ell^{1-\gamma}}{1-\gamma}$$
O salário entra **aditivamente**: desloca o nível da utilidade, não o $\arg\max$. Nenhuma
conta é necessária.

**2. Por que $T$ quebra o empate.** A renda de tempo cheio é $M = \widetilde w\bar h + T$.
Se $T=0$, $M$ é **proporcional** a $\widetilde w$ — e com $\ln c$ a proporcionalidade faz
os dois efeitos terem magnitude idêntica. Se $T>0$, $M$ cai **menos** que
proporcionalmente quando $\widetilde w$ cai: o efeito renda enfraquece e a substituição
sobra.

**3. Unicidade.** $\Phi(\ell)=\ell^\gamma+b\ell$ tem $\Phi'=\gamma\ell^{\gamma-1}+b>0$; e
$\widetilde U''(\ell) = -\widetilde w^2/[\,\cdot\,]^2 - b\gamma\ell^{-\gamma-1}<0$. Problema
estritamente côncavo, CPO suficiente. Como $\widetilde U'\to+\infty$ quando $\ell\to0^+$,
**nunca** se escolhe lazer zero.

## D. Modelo DMP

| Fórmula | De onde vem | Quando usar | Armadilha |
|---|---|---|---|
| $E_{t+1}=(1-s)E_t+m(V_t,U_t)$ | contabilidade: estoque $+$ entra $-$ sai | é o modelo inteiro; não há otimização aqui | é $sE_t$, não $sE_{t+1}$ — a separação incide sobre quem **estava** empregado |
| $\mu$ | escalar que multiplica $m$ | eficiência do **encontro**, a "PTF do matching" | não é produtividade do trabalho; e é **adimensional**, porque $m$ tem CRS |
| $f=\mu\theta^{\alpha}$, $q=\mu\theta^{\alpha-1}$ | dividir $m$ por $U$ e por $V$, usando CRS | tudo do item (c) em diante | o expoente de $q$ é **negativo**: mercado apertado enche a vaga mais devagar |
| $f=\theta q$ | $\frac{m}{U}=\frac{m}{V}\cdot\frac{V}{U}$ | provar em uma linha | é **identidade contábil**, vale para qualquer $m$; provar por substituição funciona mas esconde isso |
| $s(1-u)=f\,u$ | $E_{t+1}=E_t$, dividido por $L$ e por $u$ | a condição criação $=$ destruição | esquecer de dividir por $L$ ao passar de níveis para taxas |
| $u^{\ast} = s/(s+f)$ | isolar $u$ acima | desemprego de estado estacionário | é **razão entre fluxos**, não estoque fixo; duas economias com mesmo $u$ podem ter durações muito diferentes |
| $v(u)=[s(1-u)/\mu]^{1/\alpha}u^{-\frac{1-\alpha}{\alpha}}$ | isolar $v$ em $s(1-u)=\mu v^\alpha u^{1-\alpha}$ | curva de Beveridge | é um **lugar geométrico**, não uma relação causal; sozinha não determina o equilíbrio |
| $\partial m/\partial V=\alpha q$ | derivar $m$ em $V$ | medir a externalidade de congestão | a firma espera $q$ (produto **médio**) e gera $\alpha q$ (**marginal**); a cunha $(1-\alpha)q$ são encontros tirados das outras firmas |

### Por que a Beveridge é decrescente — duas forças, mesmo sentido

Parta de $s(1-u) = \mu v^{\alpha}u^{1-\alpha}$ e suba $u$ com $v$ fixo:

1. **Esquerda cai** — com mais desempregados há menos gente empregada, logo menos
   separações a repor. A *necessidade* de contratar diminui.
2. **Direita sobe** — com mais gente procurando, o mesmo estoque de vagas gera mais
   encontros. A *capacidade* de contratar aumenta.

Necessidade menor e capacidade maior: as duas pedem **menos vagas**. Daí $dv/du<0$.

### Deslocamento × movimento — a distinção mais cobrada

| | Movimento **ao longo** | **Deslocamento** da curva |
|---|---|---|
| O que muda | $\theta$ — variável **endógena** | $\mu$ ou $s$ — **parâmetros** |
| Origem | demanda por trabalho: lucratividade, produtividade, expectativas | atrito estrutural: descasamento, busca menos intensa, seguro-desemprego mais generoso |
| Leitura | a economia desliza sobre curva fixa: expansão no canto superior esquerdo, recessão no inferior direito | a mesma taxa de vagas passa a conviver com mais desemprego, em qualquer ponto |

Em uma frase: **$\theta$ move a economia sobre a curva; $\mu$ e $s$ movem a curva debaixo
da economia.**

### Duas ressalvas que separam resposta boa de resposta completa

1. **Um deslocamento observado não identifica a causa.** $\mu\downarrow$ e $s\uparrow$
   deslocam a curva para fora do mesmo jeito ($\mp 1/\alpha$). Distinguir exige dados de
   **fluxo**, não de estoque.
2. **A direção líquida da ineficiência em 2(d) é ambígua.** Congestão empurra para excesso
   de vagas; *thick market* empurra para escassez. Qual domina depende da divisão do
   excedente, que o enunciado não dá. Diga que há ineficiência, não em que sentido.

---

## Armadilhas do tópico inteiro

Consolidadas de [[05_trabalho_lazer]] e da [[Resolucao/lista4_resolucao|resolução da Lista 4]]:

1. Escrever $c = wn$ e esquecer $n=\bar h-\ell$ — some a dotação e a intuição do preço do lazer.
2. Afirmar que salário maior sempre aumenta horas — ignora o efeito renda.
3. Concluir "os efeitos se cancelam" com log **sem** checar que $T=0$ (ou $\pi=0$).
4. Confundir **taxa de desemprego** com **razão ocupação/população** ao ler dados.
5. Ignorar desalentados: numa recessão a taxa de desemprego pode **cair** porque gente sai
   da força de trabalho.
6. Usar a elasticidade marshalliana onde o modelo pede a de **Frisch**.
7. Tratar o desemprego de estado estacionário como estoque fixo, e não como resultado dos
   fluxos $s$ e $f$.
8. Trocar deslocamento por movimento ao longo da Beveridge.

## Onde cada bloco aparece

| Bloco | Kurlat | Lista 4 | Exercícios do livro |
|---|---|---|---|
| Medição | §7.1, pp. 127-131 | contexto | — |
| Estática consumo-lazer | §7.2, pp. 131-137 | **Q1(a)** | 7.1, 7.2, 7.3, 7.6 |
| Renda × substituição | §7.2, pp. 134-137 | **Q1(b)** | 7.5(c) |
| Evidências de elasticidade | §7.3, pp. 137-140 | Q1, discussão | 7.5(j)-(l) |
| Dinâmica / Frisch | §7.4, p. 140 | — | 7.5 |
| Busca e DMP | §7.5, pp. 142-146 | **Q2(a)-(e)** | **7.7** |

> Ver a progressão completa em [[topics-index#Tópico Trabalho e lazer estático]] e
> [[topics-index#Tópico Oferta de trabalho dinâmica Frisch e search]].
