# NotebookLM Prompts — Macroeconomia I · MPE Insper

Prof. Pedro G. Duarte. **Abra o arquivo → Ctrl+A → Ctrl+C → cole no NotebookLM.**
Slides → campo de criação de slides. Áudio → campo *Customize* do Audio Overview.
Vídeo → campo *Customize* do Video Overview.

Cada arquivo contém **apenas o prompt** — sem cabeçalho, sem metadados. Este README é o
único arquivo com informação sobre os prompts.

> ⚠️ Os campos de slide, áudio e vídeo truncam **em silêncio** por volta de 6.000
> caracteres. Todos os prompts aqui estão abaixo de **5.000**. Antes de editar qualquer um,
> leia [rules/10_notebooklm_prompts.md](../rules/10_notebooklm_prompts.md) e valide com:
> ```
> python .claude/notebooklm-validate.py -v
> ```

## Idioma da saída — não é uniforme

| Tipo | Idioma pedido no prompt |
|---|---|
| **Slides** | **inglês** (lotes até a Lista 3: pt-BR, termos técnicos em inglês entre parênteses) |
| **Vídeo** | **inglês**, rótulos de tela em inglês (lotes até a Lista 3: pt-BR) |
| **Áudio** | **inglês — sempre.** Nunca pedir áudio em português |

Todos os prompts são **escritos em inglês** (o NotebookLM processa melhor); o que muda é o
idioma que eles **pedem de volta**.

---

## Antes de usar: suba as fontes

Faça upload do conteúdo de [`sources/`](sources/) para **um único notebook**, preservando
os nomes — os prompts citam os arquivos pelo nome exato.

| Fonte | Papel |
|---|---|
| `Livro_Pablo_Kurlat_-_A_Course_in_Modern_Macroeconomics_2020...pdf` | **Kurlat (2020)** — piso de toda referência |
| `Livro_Benigno_2015_NewKeynesianEconomics_AS_AD_View.pdf` | **Benigno (2015)** — Aulas 8-9 |
| `Aula_MPE_Macro1_2026_Slides_1.pdf` | Slides da Aula 1 |
| `Aula_MPE_Macro1_SlidesAula2.pdf` | Slides da Aula 2 |
| `Aula_Handout_MPE_Macro1_Aula3_2026.pdf` | **Handout** da Aula 3 (texto corrido) |
| `Aula_MPE_Macro1_SlidesAula4.pdf` | Slides da Aula 4 |
| `Lista_MPE_Macro1_2026_Lista1.pdf` · `Lista2.pdf` · `Lista3.pdf` · `Lista4.pdf` · `Lista5.pdf` | Listas 1-5 |
| `Livro_Kurlat_Cap09_General_Equilibrium.pdf` | **Kurlat cap. 9 isolado** (pp. 165-187) — fonte do lote da Lista 5 |
| `Aula_Slides_Macro1_Aula5.pdf` · `Aula_Slides_Macro1_Aula6.pdf` | Slides das Aulas 5 e 6 |
| `Programa_Macro1_MPE_2026.pdf` | Programa |
| `Livro_Charles_I._Jones_...pdf` · `Livro_..._Romer_...pdf` · `Livro_..._Carlin_David_Soskice_2024...pdf` | Complementares |

**Não subir:** Ljungqvist & Sargent (fora do escopo — puxaria programação dinâmica que não
é cobrada) e `Listas/lista-exam.tex` (template, não material de estudo).

---

## Índice — 70 prompts, em quatro lotes

Quatro recortes coexistem de propósito. O lote **por aula** (40 prompts, Aulas 1-4) segue o programa: cada aula recebe **4 slides + 4 vídeos + 2 áudios**. O lote da **Aula 6** (6 prompts) é **4 vídeos + 2 áudios**, sem slides. Os dois lotes **por mecanismo** — Lista 3 e Lista 5, 12 prompts cada — são **6 slides + 6 vídeos**, um par por mecanismo econômico, atravessando as duas questões da lista. Quem estuda para a aula usa os dois primeiros; quem está resolvendo a lista usa o lote da sua lista.

> ⚠️ **Idioma.** A partir do lote da Aula 6, **todo** prompt pede saída em **inglês** — slides, vídeo e áudio. Os lotes das Aulas 1-4 e da Lista 3 são anteriores a essa regra e ainda pedem pt-BR em slides e vídeo; ficam como estão até serem regerados.

### Aula 1 — Mensuração dos Agregados (Kurlat caps. 1-2)

| Arquivo | Tipo | Cobre | Chars |
|---|---|---|---|
| [slides/aula-01-slides-1-teoria.md](slides/aula-01-slides-1-teoria.md) | Slide | Identidade contábil, valor adicionado, fronteira da produção, PIB × PNB | 4.703 |
| [slides/aula-01-slides-2-mecanica.md](slides/aula-01-slides-2-mecanica.md) | Slide | Nominal × real, Laspeyres/Paasche, encadeamento, deflator, PPP | 4.880 |
| [slides/aula-01-slides-3-exercicios.md](slides/aula-01-slides-3-exercicios.md) | Slide | Kurlat 1.1-1.5, 2.2 + Lista 1 Q1-Q2 | 4.634 |
| [slides/aula-01-slides-4-sintese.md](slides/aula-01-slides-4-sintese.md) | Slide | Além do PIB, IDH, Jones-Klenow, onde mora a ética | 4.890 |
| [video/aula-01-video-1-fluxo-circular.md](video/aula-01-video-1-fluxo-circular.md) | Vídeo | O anel e os três medidores | 4.759 |
| [video/aula-01-video-2-nominal-real.md](video/aula-01-video-2-nominal-real.md) | Vídeo | A bifurcação dos pesos de preço | 4.902 |
| [video/aula-01-video-3-ppp.md](video/aula-01-video-3-ppp.md) | Vídeo | Duas barras: câmbio de mercado × paridade | 4.844 |
| [video/aula-01-video-4-bem-estar.md](video/aula-01-video-4-bem-estar.md) | Vídeo | A tabela que se reordena quando o parâmetro move | 4.675 |
| [audio/aula-01-audio-1-medir-e-escolher.md](audio/aula-01-audio-1-medir-e-escolher.md) | Áudio | Fio: medir é escolher — fronteira e bem-estar | 4.945 |
| [audio/aula-01-audio-2-numero-indice.md](audio/aula-01-audio-2-numero-indice.md) | Áudio | Fio: o problema do número-índice não tem solução neutra | 4.611 |

### Aula 2 — Crescimento e Solow (Kurlat cap. 3, §4.1-4.2)

| Arquivo | Tipo | Cobre | Chars |
|---|---|---|---|
| [slides/aula-02-slides-1-teoria.md](slides/aula-02-slides-1-teoria.md) | Slide | Longo prazo, Malthus, Maddison, fatos de Kaldor, ingredientes do Solow | 4.986 |
| [slides/aula-02-slides-2-mecanica.md](slides/aula-02-slides-2-mecanica.md) | Slide | Equação fundamental, estado estacionário, estabilidade, nível × taxa | 4.924 |
| [slides/aula-02-slides-3-exercicios.md](slides/aula-02-slides-3-exercicios.md) | Slide | Kurlat 3.1-3.3, 4.1-4.2 + Lista 1 Q3-Q4 | 4.911 |
| [slides/aula-02-slides-4-sintese.md](slides/aula-02-slides-4-sintese.md) | Slide | Placar contra os fatos; o que foi assumido e o que foi ganho | 4.950 |
| [video/aula-02-video-1-escala-log.md](video/aula-02-video-1-escala-log.md) | Vídeo | O mesmo dado em escala linear e log | 4.703 |
| [video/aula-02-video-2-malthus.md](video/aula-02-video-2-malthus.md) | Vídeo | Sete séculos de salários reais e o laço malthusiano | 4.691 |
| [video/aula-02-video-3-diagrama-solow.md](video/aula-02-video-3-diagrama-solow.md) | Vídeo | O diagrama montado curva a curva | 4.849 |
| [video/aula-02-video-4-nivel-vs-taxa.md](video/aula-02-video-4-nivel-vs-taxa.md) | Vídeo | Painel duplo: nível sobe, taxa volta a zero | 4.718 |
| [audio/aula-02-audio-1-crescimento-recente.md](audio/aula-02-audio-1-crescimento-recente.md) | Áudio | Fio: crescer é o anormal, não o normal | 4.459 |
| [audio/aula-02-audio-2-nivel-vs-taxa.md](audio/aula-02-audio-2-nivel-vs-taxa.md) | Áudio | Fio: o crescimento entregue é o que foi assumido | 4.833 |

### Aula 3 — Solow e evidências (Kurlat §4.3-4.5, cap. 5)

| Arquivo | Tipo | Cobre | Chars |
|---|---|---|---|
| [slides/aula-03-slides-1-teoria.md](slides/aula-03-slides-1-teoria.md) | Slide | Regra de Ouro, ineficiência dinâmica, mercados de fatores, tecnologia | 4.989 |
| [slides/aula-03-slides-2-mecanica.md](slides/aula-03-slides-2-mecanica.md) | Slide | Calibração, paradoxo dos retornos, eq. (5.4.2), development accounting | 4.985 |
| [slides/aula-03-slides-3-exercicios.md](slides/aula-03-slides-3-exercicios.md) | Slide | Kurlat 4.3, 5.1-5.9 + Lista 2 (Coreias e Gotham) | 4.999 |
| [slides/aula-03-slides-4-sintese.md](slides/aula-03-slides-4-sintese.md) | Slide | O resíduo como ignorância; a Regra de Ouro não é conselho | 5.000 |
| [video/aula-03-video-1-regra-de-ouro.md](video/aula-03-video-1-regra-de-ouro.md) | Vídeo | A corcova do consumo e os dois lados do pico | 4.954 |
| [video/aula-03-video-2-mercados-de-fatores.md](video/aula-03-video-2-mercados-de-fatores.md) | Vídeo | A tangente: salário no intercepto, juro na inclinação | 4.776 |
| [video/aula-03-video-3-previsto-vs-observado.md](video/aula-03-video-3-previsto-vs-observado.md) | Vídeo | Duas barras: o hiato previsto e o observado | 4.449 |
| [video/aula-03-video-4-residuo.md](video/aula-03-video-4-residuo.md) | Vídeo | A barra decomposta e o bloco que sobra | 4.568 |
| [audio/aula-03-audio-1-residuo-ignorancia.md](audio/aula-03-audio-1-residuo-ignorancia.md) | Áudio | Fio: o resíduo é a nossa ignorância | 4.986 |
| [audio/aula-03-audio-2-regra-de-ouro.md](audio/aula-03-audio-2-regra-de-ouro.md) | Áudio | Fio: a Regra de Ouro não é uma recomendação | 4.839 |

### Aula 4 — Consumo e Poupança (Kurlat cap. 6)

| Arquivo | Tipo | Cobre | Chars |
|---|---|---|---|
| [slides/aula-04-slides-1-teoria.md](slides/aula-04-slides-1-teoria.md) | Slide | Keynes, o puzzle, restrição intertemporal, Euler, CRRA | 4.958 |
| [slides/aula-04-slides-2-mecanica.md](slides/aula-04-slides-2-mecanica.md) | Slide | Estáticas comparativas assinadas; σ decide o sinal de ∂c₁/∂r | 4.930 |
| [slides/aula-04-slides-3-exercicios.md](slides/aula-04-slides-3-exercicios.md) | Slide | Kurlat 6.1-6.9 + Lista 3 Q1-Q2 | 4.934 |
| [slides/aula-04-slides-4-sintese.md](slides/aula-04-slides-4-sintese.md) | Slide | Renda permanente, equivalência ricardiana e suas hipóteses | 4.849 |
| [video/aula-04-video-1-puzzle-keynes.md](video/aula-04-video-1-puzzle-keynes.md) | Vídeo | Duas nuvens de dados que se contradizem | 4.716 |
| [video/aula-04-video-2-plano-c1-c2.md](video/aula-04-video-2-plano-c1-c2.md) | Vídeo | O plano (c₁,c₂): reta, curvas, tangência | 4.832 |
| [video/aula-04-video-3-sigma-arbitro.md](video/aula-04-video-3-sigma-arbitro.md) | Vídeo | A rotação do juro e as duas setas opostas | 4.922 |
| [video/aula-04-video-4-ricardo-e-restricao.md](video/aula-04-video-4-ricardo-e-restricao.md) | Vídeo | A reta que não se move, e o bico que a quebra | 4.876 |
| [audio/aula-04-audio-1-consumo-segue-riqueza.md](audio/aula-04-audio-1-consumo-segue-riqueza.md) | Áudio | Fio: consumo segue riqueza, não renda | 4.818 |
| [audio/aula-04-audio-2-timing-do-imposto.md](audio/aula-04-audio-2-timing-do-imposto.md) | Áudio | Fio: o timing do imposto não importa — até que importe | 4.758 |

### Aula 6 — Equilíbrio Geral (Kurlat cap. 9)

Primeiro lote **inteiramente em inglês** — áudio, e agora também o vídeo. Sem slides:
os quatro objetos visuais da aula já esgotam o que ela tem de próprio.

| Arquivo | Tipo | Objeto visual / fio | Chars |
|---|---|---|---|
| [video/aula-06-video-1-tres-agentes.md](video/aula-06-video-1-tres-agentes.md) | Vídeo | Três caixas e quatro mercados; as CPOs colando nos canais até os preços sumirem | 4.952 |
| [video/aula-06-video-2-planejador-e-contradicao.md](video/aula-06-video-2-planejador-e-contradicao.md) | Vídeo | O conjunto factível e o ponto "melhor" que acaba fora dele | 4.961 |
| [video/aula-06-video-3-diagrama-de-fase.md](video/aula-06-video-3-diagrama-de-fase.md) | Vídeo | O diagrama de fase construído do zero até o *saddle path* | 4.984 |
| [video/aula-06-video-4-antecipacao.md](video/aula-06-video-4-antecipacao.md) | Vídeo | As duas curvas deslocando e o consumo saltando antes da notícia se realizar | 4.817 |
| [audio/aula-06-audio-1-precos-fazem-o-planejador.md](audio/aula-06-audio-1-precos-fazem-o-planejador.md) | Áudio | Fio: os preços carregam a informação que o planejador teria | 4.976 |
| [audio/aula-06-audio-2-poupar-menos-e-otimo.md](audio/aula-06-audio-2-poupar-menos-e-otimo.md) | Áudio | Fio: poupar menos que a Regra de Ouro é ótimo, não é falha | 4.944 |

> **Sem slides neste lote.** Cada um dos quatro vídeos já carrega a derivação completa do
> seu objeto; um slide repetiria a álgebra sem acrescentar imagem.

### Lista 3 — por mecanismo econômico (Kurlat cap. 6; Exs. 6.1, 6.5, 6.6)

Recorte **transversal**: cada par slide+vídeo isola um mecanismo e o persegue pelas duas
questões, em vez de seguir a ordem dos itens. Os seis se encadeiam — 1 constrói a máquina,
2 a 4 a diferenciam, 5 e 6 quebram as duas hipóteses que 4 usou.

| Arquivo | Tipo | Mecanismo | Itens | Chars |
|---|---|---|---|---|
| [slides/lista-03-slides-1-riqueza-e-euler.md](slides/lista-03-slides-1-riqueza-e-euler.md) | Slide | RIO, Euler, forma fechada CRRA | Q1(a) | 4.934 |
| [slides/lista-03-slides-2-renda-permanente.md](slides/lista-03-slides-2-renda-permanente.md) | Slide | Propensão a consumir renda futura; Keynes × PIH | Q1(b) | 4.853 |
| [slides/lista-03-slides-3-sigma-arbitro.md](slides/lista-03-slides-3-sigma-arbitro.md) | Slide | σ decide o sinal de ∂c₁/∂r | Q1(c) | 4.891 |
| [slides/lista-03-slides-4-impostos-e-ricardo.md](slides/lista-03-slides-4-impostos-e-ricardo.md) | Slide | Lump-sum como puro efeito-riqueza; equivalência ricardiana | Q1(d,e) | 4.914 |
| [slides/lista-03-slides-5-restricao-de-credito.md](slides/lista-03-slides-5-restricao-de-credito.md) | Slide | KKT, dois regimes, PMgC salta para 1 | Q2(a–c) | 4.978 |
| [slides/lista-03-slides-6-imposto-sobre-poupanca.md](slides/lista-03-slides-6-imposto-sobre-poupanca.md) | Slide | Cunha intertemporal e peso morto a receita igual | Q2(d) | 4.979 |
| [video/lista-03-video-1-riqueza-e-euler.md](video/lista-03-video-1-riqueza-e-euler.md) | Vídeo | O plano (c₁,c₂) montado do zero: dotação, reta, tangência, raio | Q1(a) | 4.803 |
| [video/lista-03-video-2-renda-permanente.md](video/lista-03-video-2-renda-permanente.md) | Vídeo | Deslocamento paralelo e o ótimo deslizando no raio fixo | Q1(b) | 4.408 |
| [video/lista-03-video-3-sigma-arbitro.md](video/lista-03-video-3-sigma-arbitro.md) | Vídeo | Rotação em torno de (W,0) e a derivada cruzando zero | Q1(c) | 4.581 |
| [video/lista-03-video-4-impostos-e-ricardo.md](video/lista-03-video-4-impostos-e-ricardo.md) | Vídeo | A dotação desliza; a reta e a escolha não se movem | Q1(d,e) | 4.678 |
| [video/lista-03-video-5-restricao-de-credito.md](video/lista-03-video-5-restricao-de-credito.md) | Vídeo | A parede vertical e o ótimo empurrado para o canto | Q2(a–c) | 4.719 |
| [video/lista-03-video-6-imposto-sobre-poupanca.md](video/lista-03-video-6-imposto-sobre-poupanca.md) | Vídeo | Transladar × girar a mesma receita, e o ponto na reta errada | Q2(d) | 4.668 |

> **Sem áudio neste lote.** Os dois fios condutores do cap. 6 já estão em
> `aula-04-audio-1` e `aula-04-audio-2`; um terceiro repetiria a tese.


### Lista 5 — por mecanismo econômico (Kurlat cap. 9; Exs. 9.5, 9.7, 9.11, 9.12)

Mesmo recorte **transversal** da Lista 3, agora sobre Equilíbrio Geral, e **inteiramente em
inglês** — slides e vídeo inclusive. As duas questões da lista são imagens espelhadas: a Q1
é o cap. 9 com o **capital congelado**, a Q2 é o cap. 9 com o **trabalho congelado**. Os
seis mecanismos seguem essa cadeia: 1 monta a máquina, 2-3 trabalham a margem de trabalho,
4 é a dobradiça que compara as duas economias, 5-6 trabalham a margem de capital.

| Arquivo | Tipo | Mecanismo | Itens | Chars |
|---|---|---|---|---|
| [slides/lista-05-slides-1-tres-agentes-e-lucro-zero.md](slides/lista-05-slides-1-tres-agentes-e-lucro-zero.md) | Slide | Amputação, lucro zero por Euler, definição de equilíbrio | Q1(a-c) | 4.916 |
| [slides/lista-05-slides-2-preco-que-cancela.md](slides/lista-05-slides-2-preco-que-cancela.md) | Slide | TMS = TMT, equação implícita das horas, unicidade | Q1(d) | 4.919 |
| [slides/lista-05-slides-3-sigma-decide-o-sinal.md](slides/lista-05-slides-3-sigma-decide-o-sinal.md) | Slide | Diferenciação implícita; sinal de 1−σ; renda × substituição | Q1(e) | 4.934 |
| [slides/lista-05-slides-4-juro-sem-ancora.md](slides/lista-05-slides-4-juro-sem-ancora.md) | Slide | Euler nas duas economias; juro sem âncora tecnológica | Q1(d), Q2(a) | 4.797 |
| [slides/lista-05-slides-5-dono-do-capital.md](slides/lista-05-slides-5-dono-do-capital.md) | Slide | Não-arbitragem, linearidade, separação de Fisher | Q2(b,c) | 4.948 |
| [slides/lista-05-slides-6-estado-estacionario-e-regra-de-ouro.md](slides/lista-05-slides-6-estado-estacionario-e-regra-de-ouro.md) | Slide | Estado estacionário, diagrama de fase, K* < K_gr | Q2(d,e) | 4.975 |
| [video/lista-05-video-1-tres-agentes-e-lucro-zero.md](video/lista-05-video-1-tres-agentes-e-lucro-zero.md) | Vídeo | O diagrama de três agentes perdendo peças, uma a uma | Q1(a-c) | 4.330 |
| [video/lista-05-video-2-preco-que-cancela.md](video/lista-05-video-2-preco-que-cancela.md) | Vídeo | Duas equações colidindo até o salário se anular | Q1(d) | 4.572 |
| [video/lista-05-video-3-sigma-decide-o-sinal.md](video/lista-05-video-3-sigma-decide-o-sinal.md) | Vídeo | O dial de σ e o marcador cruzando o zero | Q1(e) | 4.505 |
| [video/lista-05-video-4-juro-sem-ancora.md](video/lista-05-video-4-juro-sem-ancora.md) | Vídeo | Uma equação fixa, o cenário atrás dela sendo trocado | Q1(d), Q2(a) | 4.431 |
| [video/lista-05-video-5-dono-do-capital.md](video/lista-05-video-5-dono-do-capital.md) | Vídeo | Duas colunas convergindo na mesma linha; o lucro reto em zero | Q2(b,c) | 4.532 |
| [video/lista-05-video-6-estado-estacionario-e-regra-de-ouro.md](video/lista-05-video-6-estado-estacionario-e-regra-de-ouro.md) | Vídeo | A corcova do consumo e os dois pontos que nunca coincidem | Q2(d,e) | 4.765 |

> **Sem áudio neste lote.** Os dois fios do cap. 9 já estão em `aula-06-audio-1` e
> `aula-06-audio-2`. Para escutar a lista inteira, o material é outro: as três trilhas em
> [`Leituras/`](../Leituras/), geradas por `/speechify`.

---

## Anatomia

**Slides — 4 por aula, divididos por função.** Cada deck tem um papel e não invade os
outros: *teoria* deriva, *mecânica* calcula e assina derivadas, *exercícios* resolve os
itens do Kurlat e da lista, *síntese* conecta com as outras aulas. Cada um traz uma trava
de escopo explícita e um bloco de Python rodável (exceto teoria e síntese, onde a conta não
é o ponto).

**Vídeos — 4 por aula, um por objeto visual.** Cada vídeo pega **um** gráfico ou diagrama e
o constrói até o fim, em no máximo 6 batidas, cada batida nomeando o que aparece na tela e
cada transição correspondendo a um passo do argumento. Fecha sempre com a **imagem única**
que o aluno deve conseguir redesenhar de memória.

**Lote por mecanismo — 6 pares, um mecanismo cada.** O recorte não é a ordem do enunciado, é a cadeia causal: cada par nomeia um mecanismo, diz de quais itens ele sai, e declara o que pertence aos outros cinco. Os slides derivam e assinam; o vídeo correspondente pega o **único** objeto visual daquele mecanismo e o constrói em seis batidas.

**Áudios — 2 por aula, um fio condutor cada.** Não resumem a aula: desenvolvem **um único
argumento** em no máximo 5 segmentos, dizem explicitamente o que pular, e contêm pelo menos
uma instrução sem equivalente em slide (os dois locutores discordando, autópsia de um erro
comum, motivação histórica).

## Ainda falta

Prompts para as **Aulas 5, 7, 8 e 9** — os slides da Aula 5 já estão em `sources/`; os das
Aulas 7 a 9 ainda não foram disponibilizados, e os prompts citam a fonte pelo nome exato do
arquivo. Quando chegarem, jogue-os em `Aula/`, copie para `sources/` com o prefixo `Aula_`
e rode `/notebooklm`. Falta também o lote por mecanismo das **Listas 4 e 6**.

Cobertura por tema em [Map/cobertura.md](../Map/cobertura.md).
