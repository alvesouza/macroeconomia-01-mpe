---
tags: [map, cross-reference, macro1, guia]
date: 2026-08-21
---

# Guia de Estudo

Ordem sugerida, aula a aula. Voltar ao [[00_indice]].

> **Onde você está (2026-08-21):** quatro aulas dadas, Listas 1 e 2 entregues e resolvidas,
> **Lista 3 vence em 24/08**. O bloco vivo é o da **Aula 4**; os blocos 5-9 são preparação.

**Ritmo observado:** uma lista por semana, sempre no domingo (10/08, 17/08, 24/08). Cada
lista é ancorada em **um capítulo** do Kurlat e sai logo após a aula correspondente. Dá
para se antecipar: ao terminar a aula $n$, a lista sobre o capítulo dela chega em dias.

---

## Bloco 1 — Mensuração (Aula 1) · Kurlat caps. 1-2

### Antes da aula
- Ler: **Kurlat §1.1-1.2** (pp. 15-27) e **§2.1-2.2** (pp. 31-40)
- Revisar: [[01_mensuracao_agregados]]

### Depois da aula
- Praticar: Kurlat **1.1** (p. 27), **1.3** (p. 28), **2.2** (p. 41)
- Lista: [[Listas/MPE_Macro1_2026_Lista1|Lista 1, Q1-Q2]] · conferir com
  [[Resolucao/lista1_resolucao|a resolução]]
- NotebookLM: `kurlat-cap01-audio.md`, `kurlat-cap02-audio.md`

### Conexões
- Pré-requisito para: **tudo**. Sem PIB real × nominal não há Solow.
- Volta na Aula 7 disfarçado de **vieses do IPCA** ([[#Bloco 7 — Moeda e Inflação Aula 7 · Kurlat caps 10-11]]).

**O que realmente é cobrado:** não a conta, mas **por que** Laspeyres e Paasche discordam.
Foi o item de maior peso conceitual da Lista 1.

---

## Bloco 2 — Crescimento e Solow (Aula 2) · Kurlat cap. 3 e §4.1-4.2

### Antes da aula
- Ler: **Kurlat §3.1-3.3** (pp. 47-52) e **§4.1-4.2** (pp. 53-61)
- Revisar: [[02_crescimento_solow]]

### Depois da aula
- Rever: [[Aula/MPE_Macro1_SlidesAula2|Slides Aula 2]] — Malthus, Maddison, Clark
- Praticar: Kurlat **3.1** (p. 51), **4.1** (p. 72), **4.2** (p. 72)
- Lista: [[Listas/MPE_Macro1_2026_Lista1|Lista 1, Q3-Q4]]
- Código: `Resolucao/lista1_codigo/q4_solow.py` — simule e veja a transição

### Conexões
- Depende de: [[#Bloco 1 — Mensuração Aula 1 · Kurlat caps 1-2]]
- Pré-requisito para: Blocos 3 e 6

**Trave isto antes de seguir:** **efeito nível × efeito taxa**. Subir $s$ eleva $y^*$ mas
não a taxa de crescimento de longo prazo. Metade dos erros em Solow nasce aqui.

---

## Bloco 3 — Solow e evidências (Aula 3) · Kurlat §4.3-4.5 e cap. 5

### Antes da aula
- Ler: **Kurlat §4.3-4.5** (pp. 61-72) e **cap. 5** (pp. 75-93)
- Revisar: [[03_solow_evidencias]]

### Depois da aula
- Rever: [[Aula/Handout_MPE_Macro1_Aula3_2026(1)|Handout Aula 3]] — é o material mais denso
  do curso até aqui; leia como texto, não como slide
- Praticar: Kurlat **5.1** (p. 93), **5.3** (p. 94), **5.6** (p. 96)
- Avançado: Kurlat **5.7** (p. 96) e **5.8** (p. 97)
- Lista: [[Listas/MPE_Macro1_2026_Lista2|Lista 2]] · [[Resolucao/lista2_resolucao|resolução]]

### Conexões
- Depende de: [[#Bloco 2 — Crescimento e Solow Aula 2 · Kurlat cap 3 e §4 1-4 2]]
- Pré-requisito para: Bloco 9 (choques de produtividade no AD-AS)

**O ponto fino:** o resíduo de Solow é **residual**. A Lista 2 Q2 mostra que uma melhora
puramente **alocativa** — capital que sai da segurança e volta à produção — aparece como
"crescimento da PTF" com a tecnologia literalmente constante.

---

## Bloco 4 — Consumo e poupança (Aula 4) · Kurlat cap. 6 ⏰ **bloco ativo**

### Antes da aula
- Ler: **Kurlat §6.1-6.4** (pp. 103-121)
- Revisar: [[04_consumo_poupanca]]

### Depois da aula
- Rever: [[Aula/MPE_Macro1_SlidesAula4|Slides Aula 4]] — Keynes (1936), o puzzle
  *cross-section* × série temporal, Friedman
- Praticar **nesta ordem** (é o caminho até a Lista 3):
  1. Kurlat **6.1** (p. 121) — é a própria Q1 da lista
  2. Kurlat **6.3** (p. 122) — o item (c) da lista sai daqui
  3. Kurlat **6.5** (p. 123) — é a Q2 da lista
  4. Kurlat **6.6** (p. 123) — o item (d) da Q2 sai daqui
- Lista: [[Listas/MPE_Macro1_2026_Lista3|Lista 3]] — **entrega 24/08/2026**

### Conexões
- Depende de: nada do curso; a máquina é microeconomia de otimização
- Pré-requisito para: Blocos 5, 6, 8 e 9 — **é o conceito mais reutilizado do curso**

**Os dois pontos que decidem a nota:**
1. Em $\partial c_1/\partial r$, **$\sigma$ é o árbitro** entre efeito renda e efeito
   substituição. Não é "só a curvatura".
2. **Equivalência ricardiana**: impostos entram só pelo valor presente
   $\tau_1 + \tau_2/(1+r)$. O *timing* não importa — **desde que** valham as hipóteses. A
   Q2 da lista existe justamente para quebrar uma delas.

---

## Bloco 5 — Trabalho e lazer (Aula 5) · Kurlat cap. 7

### Antes da aula
- Ler: **Kurlat §7.1-7.5** (pp. 127-146)
- Revisar: [[05_trabalho_lazer]]

### Depois da aula
- Praticar: Kurlat **7.1** (p. 146), **7.2** (p. 146), **7.3** (p. 147)
- Avançado: Kurlat **7.5** *Prescott's Calculation* (p. 148) — candidato forte a questão
  grande da Lista 4
- Lista: 4 (a emitir)

### Conexões
- Depende de: [[#Bloco 4 — Consumo e poupança Aula 4 · Kurlat cap 6 ⏰ bloco ativo]] —
  mesma máquina de otimização, outro par de bens
- Pré-requisito para: Bloco 8 (a AS nasce do mercado de trabalho)

**O paralelo que economiza tempo:** transitório × permanente reaparece intacto. Choque
**transitório** de salário move horas muito (Frisch); **permanente** quase não move. É a
renda permanente da Aula 4 com outra roupa.

---

## Bloco 6 — Equilíbrio geral (Aula 6) · Kurlat cap. 9

> ⚠️ **Pular o cap. 8 (Investment)** — está fora do escopo.

### Antes da aula
- Ler: **Kurlat §9.1-9.3** (pp. 165-179)
- Revisar: [[06_equilibrio_geral]]

### Depois da aula
- Praticar: Kurlat **9.1** (p. 179), **9.5** (p. 181), **9.7** (p. 183)
- **Síntese obrigatória:** Kurlat **9.12** *Optimal vs Fixed Savings Rates* (p. 185) —
  fecha o fio que abriu na Aula 2
- Lista: 5 (a emitir)

### Conexões
- Depende de: Blocos 2, 4 e 5
- Pré-requisito para: Bloco 9 (por que existe espaço para política)

**O contraste central do curso:** a Regra de Ouro (Aula 3) maximiza consumo de estado
estacionário e dá $f'(k_{GR})=\delta+n$. O equilíbrio geral dá $f'(k^*)=\rho+\delta$. São
**diferentes**, e o segundo é o **ótimo** — poupar menos que a Regra de Ouro é racional
quando se desconta o futuro.

---

## Bloco 7 — Moeda e Inflação (Aula 7) · Kurlat caps. 10-11

### Antes da aula
- Ler: **Kurlat §10.1-10.4** (pp. 191-202) e **§11.1-11.4** (pp. 205-218)
- Revisar: [[07_moeda_inflacao]]

### Depois da aula
- Praticar: Kurlat **11.2** (p. 218), **10.2** (p. 202), **11.8** (p. 222)
- Avançado: Kurlat **11.6** *Seignorage with High Inflation* (p. 219) — curva de Laffer
- Lista: 6 (a emitir, junto com a Aula 8)

### Conexões
- Depende de: Bloco 1 (índices de preço voltam como vieses do IPCA)
- Pré-requisito para: Bloco 8 — **a dicotomia clássica estabelecida aqui é exatamente o
  que a Aula 8 vai quebrar**

---

## Bloco 8 — AD-AS: microfundamentos (Aula 8) · Benigno §1-5

### Antes da aula
- Ler: **Benigno (2015), §1-5** (pp. 503-511)
- Revisar: [[08_adas_microfundamentos]]
- ⚠️ Declarar a notação: onde o Benigno divergir do Kurlat, diga qual está usando

### Depois da aula
- Reproduzir à mão: **Figs. 1-5**. Não há exercícios de fim de seção — a prática *é*
  redesenhar os gráficos e saber o que desloca cada curva
- Equações a ter na ponta: **(21)** AD · **(17)/(20)** AS · **(15)** $y_n$ · **(19)** $y_e$
- Lista: 6 (a emitir)

### Conexões
- Depende de: Blocos 4, 5, 6 e 7 — **converge tudo**
- Pré-requisito para: Bloco 9

**Não confunda:** $y_n$ (natural, preços flexíveis **com** markup) × $y_e$ (eficiente, do
planejador). A distância entre eles é **distorção estrutural**, não ciclo. Estabilizar em
torno de $y_n$ não é atingir $y_e$ — e é daí que sai metade da discussão da Aula 9.

---

## Bloco 9 — AD-AS: política (Aula 9) · Benigno §6-12

### Antes da aula
- Ler: **Benigno (2015), §6-12** (pp. 511-523)
- Revisar: [[09_adas_politica]]

### Depois da aula
- Trabalhar cada figura como um exercício: Fig. 6 (choque transitório), Fig. 7
  (permanente), Fig. 8 (otimismo), Fig. 9 (markup/estagflação)
- Derivar o sinal do multiplicador fiscal (§8) e o argumento do ZLB (§9)
- Lista: 7 (provável — confirmar)

### Conexões
- Depende de: **todo o curso**
- É o material mais provável de virar questão de síntese na avaliação final

**A questão que eu esperaria na prova:** contrastar choque de produtividade **transitório**
e **permanente** — as respostas do juro real natural têm **sinais diferentes**, e a razão é
o mecanismo de renda permanente da Aula 4 operando dentro da AD.

---

## Roteiro de revisão para a avaliação final (65% da nota)

Não revise aula por aula. Revise pelos **sete fios** de [[topics-index]]:

1. **Equação de Euler** (4 → 6 → 8)
2. **Transitório × permanente** (4 → 5 → 9)
3. **Efeito renda × substituição** (4 → 5)
4. **Taxa de poupança**: exógena → Regra de Ouro → escolhida (2 → 3 → 6)
5. **Neutralidade da moeda**: vale → quebra → volta a valer (7 → 8 → 9)
6. **Eficiência de Pareto** (3 → 6 → 9)
7. **PTF** (1 → 3 → 9)

Cada fio atravessa três aulas e é exatamente o formato de questão contextualizada descrito
em [[00_estilo_avaliacao]]. Quem só sabe cada aula isolada responde metade.
