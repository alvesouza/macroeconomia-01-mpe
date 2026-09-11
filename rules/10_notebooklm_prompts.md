# Regras para prompts do NotebookLM

Derivadas da auditoria do primeiro lote de prompts (Aula 1 + Kurlat caps. 1-3), agosto de
2026. Substituem o comportamento padrão de `/notebooklm`.

---

## R0 — Sempre perguntar o escopo antes de escrever (regra que precede todas)

**Nunca comece a escrever prompts do NotebookLM sem perguntar.** Mesmo quando o pedido
parece óbvio, mesmo quando o comando já recebeu um diretório como argumento, mesmo quando
já existe um lote anterior no projeto. Pergunte, em **uma única rodada** de perguntas:

1. **Unidade de organização** — um conjunto de prompts corresponde a quê? **Aulas**,
   **capítulos** do livro, **sessões/temas** que atravessam várias aulas, ou **um conjunto
   único** cobrindo tudo. Isso define nome de arquivo, fonte citada e recorte de conteúdo;
   não é inferível com segurança.
2. **Quantos prompts de cada tipo** — contagem separada para **slides**, **áudio** e
   **vídeo**. Zero é resposta válida para um tipo. Não presumir o arranjo
   "2 slides + 1 áudio": aquilo foi a escolha de um lote específico, não um padrão.
3. **Qual conteúdo** — quais aulas, capítulos ou tópicos entram, e o que deve ficar
   deliberadamente de fora.

Só depois disso comece. A única exceção é o usuário dizer explicitamente "usa o padrão" ou
"não pergunta". Se a contagem pedida não dividir igualmente pela unidade escolhida (ex.: 4
prompts de slide para 3 aulas), **declare como vai alocar e siga** — não abra uma segunda
rodada de perguntas.

> **Por que isso é regra e não preferência.** Um prompt de 4.900 caracteres é caro de
> escrever e caríssimo de refazer no recorte errado. Um lote inteiro construído sobre a
> unidade errada é trabalho perdido por completo, e a pergunta que evitaria isso custa uma
> interação.

---

## O diagnóstico

O primeiro lote foi escrito como **lista de cobertura** (uma ementa: "cubra A, B, C..."). Isso
falha porque **as fontes já contêm o conteúdo** — o NotebookLM não precisa que lhe digam o que
está nelas. O que ele precisa é de um **briefing**: que forma a saída deve ter, o que priorizar
e o que deixar de fora.

Medição do `audio/aula-01-audio.md` (5.091 chars, 799 palavras, 9 segmentos):

| Métrica | Valor | Problema |
|---|---|---|
| Minutos por segmento | 3,9-5,0 | Pouco para o que cada bloco pede |
| Segmentos com >3 sub-tópicos | **6 de 9** | "THE THREE METHODS" e "THE HARD CASES" têm **8 cada** |
| Sub-tópico mais espremido | ~33 segundos | 8 itens em ~4,4 min = lista lida em voz alta |
| Numerais no corpo | 26 (14 só no bloco de índices) | Ninguém acompanha 14 números falados |
| Instruções de estilo não verificáveis | 5 | "be honest", "say it plainly", "go slowly"... |

**A causa raiz:** amplitude expulsa profundidade. Pedir 8 sub-tópicos em 4 minutos força
tratamentos de 30 segundos — exatamente o resumo raso que o prompt manda evitar.

---

## As regras

### R1 — Briefing, não ementa
Abra com **uma frase de tese** que toda a saída serve. Depois diga o que priorizar e, de forma
explícita, **o que pular**. Nunca abra com "cubra os seguintes tópicos".

### R2 — Orçamento de profundidade (a regra que mais importa)
- **Áudio:** máximo **5 segmentos**, máximo **3 sub-pontos por segmento**. Se a divisão der
  menos de 5 minutos por segmento, corte segmentos — não encurte a explicação.
- **Slides:** sem limite de tempo, então amplitude é aceitável. Listas de cobertura pertencem
  aqui, não no áudio.

### R3 — Disciplina numérica
- **Áudio:** no máximo **3 numerais por segmento**, e só números que carregam um desfecho
  (58,6% contra 5,9% vale; "0,053 dólares por peso" não). Nunca uma conversão de vários passos
  em voz alta.
- **Slides:** números densos e exatos, sempre.

### R4 — Diga o que omitir
Todo prompt de áudio nomeia **pelo menos dois assuntos a NÃO cobrir**. Sem isso o modelo tenta
cobrir tudo e nivela por baixo.

### R5 — Escopo positivo no áudio, negativo só nos slides
A trava `No Bellman, DSGE, Calvo NKPC` faz sentido em slides, onde o modelo sintetiza e pode
derivar. Em áudio, nomear a técnica proibida arrisca **evocá-la**. Use enquadramento positivo:
> "Mantenha-se no nível da aula enviada; se uma fonte for além, registre em uma frase e siga."

### R6 — Corte instruções de estilo não verificáveis
"be honest", "give credit where due", "say it plainly", "go slowly", "spend real time" gastam
orçamento e não mudam a saída. Substitua por instruções **estruturais**:
> "Enuncie a objeção, depois a melhor réplica, depois o veredito."

### R7 — O áudio precisa justificar existir
Todo prompt de áudio contém **ao menos uma instrução sem equivalente em slide**: os dois
locutores discordando, autópsia de um erro comum, motivação histórica, ou ponte para uma aula
posterior. Sem isso, é um slide lido em voz alta.

### R8 — Declare o idioma da saída (e **nunca peça áudio em português**)
As fontes são em inglês, o curso é em pt-BR. O prompt deve dizer explicitamente em que idioma a
saída deve sair — o padrão do NotebookLM segue as fontes.

| Tipo | Idioma pedido |
|---|---|
| **Slides** | **inglês** |
| **Vídeo** | **inglês**, rótulos de tela em inglês |
| **Áudio** | **inglês — sempre.** Nunca pedir áudio em português, em nenhuma circunstância |

A linha padrão do áudio é:
> `Output language: English, conversational register. Keep the spoken output in English
> throughout, whatever language the uploaded sources are in.`

Isso não é preferência de estilo: é regra fixa do projeto, e **vale para os três tipos**.
Nunca peça saída em português em nenhum prompt. Os lotes das Aulas 1-4 e da Lista 3 foram
escritos antes desta regra e ainda pedem pt-BR em slides e vídeo; ficam como estão até
serem regerados, mas não servem de modelo.

### R9 — Economia de nomes de fonte
Nome completo do arquivo **uma vez**, depois um handle curto (`= KURLAT`). Só cite fontes
realmente usadas: cada nome extra custa ~90 caracteres do orçamento.

### R10 — Orçamento de caracteres
Teto duro **5.000**; alvo **4.400-4.900**. Medido neste projeto: **~6,2 chars/palavra**, logo
**720-780 palavras**. Cabeçalho (título, fontes, escopo, idioma) ≤ 120 palavras.
Validar sempre com `python .claude/notebooklm-validate.py`.

### R11 — Não peça o que a interface controla
A duração do Audio Overview é definida pelo controle da UI (Shorter/Default/Longer), não pelo
prompt. Tratar "35-45 min" como dica, não como especificação — e não gastar orçamento nisso.

> ⚠️ R5 e R11 são **inferências** sobre o comportamento da plataforma, não fatos verificados.
> R1-R4, R6-R10 decorrem da estrutura do próprio texto e são verificáveis.

---

## Regras do vídeo (R12-R16)

O **Video Overview** do NotebookLM gera um vídeo narrado com painéis visuais. Não é slide
(que o leitor percorre no próprio ritmo) nem áudio (que não tem imagem). O erro a evitar é
tratá-lo como um dos dois.

### R12 — Um visual por batida, e o prompt diz qual é
Cada segmento de vídeo nomeia **o que aparece na tela**: um gráfico, um eixo, uma tabela de
duas colunas, uma linha do tempo. Se um segmento não tem visual próprio, ele não é um
segmento de vídeo — vire texto de áudio ou junte ao vizinho.

### R13 — Orçamento de batidas: máximo 6
Mais generoso que o áudio (5), porque a imagem sustenta atenção que a voz sozinha não
sustenta. Ainda assim, **máximo 3 sub-pontos por batida** — a regra R2 vale igual.

### R14 — Números vão na tela, não na narração
Ao contrário do áudio (R3), o vídeo **pode** mostrar tabelas e valores exatos: o
espectador lê. O que a narração faz é **apontar o número que importa**, não recitar a
tabela. Instrução típica:
> "Show the full table on screen; in narration name only the two cells that differ."

### R15 — O movimento tem de significar alguma coisa
Toda transição entre batidas corresponde a **um passo do argumento**, e o prompt diz qual:
uma curva que desloca, um eixo que muda de escala, uma coluna que se acende. Vídeo cuja
transição é só "próximo tópico" deveria ser slide.

### R16 — Fechamento com a imagem única
O último segmento pede **uma imagem que resuma o capítulo inteiro** — o gráfico que a
pessoa deve conseguir redesenhar de memória na prova. Nomeie-o explicitamente.

> R5 (escopo positivo), R6 (sem estilo não verificável), R8 (idioma), R9 (handles de
> fonte) e R10 (orçamento de caracteres) valem para vídeo exatamente como para os demais.
> R11 idem: a duração é controle de UI, não do prompt.

---

## Consequência estrutural: o split muda

O arranjo "2 slides + 1 áudio por capítulo" fazia o áudio cobrir o **capítulo inteiro**, o que
viola R2 automaticamente. Novo arranjo:

| Peça | Papel | Cobertura |
|---|---|---|
| **Slides parte 1** | Teoria e derivação | Metade do capítulo, exaustiva |
| **Slides parte 2** | Mecânica e números | Outra metade, exaustiva |
| **Áudio** | **Um único fio condutor**, fundo | **NÃO** o capítulo inteiro — uma tese, 5 segmentos |
| **Vídeo** | **A geometria do capítulo** | Os 4-6 objetos visuais que a pessoa precisa saber redesenhar |

O áudio deixa de ser resumo e passa a ser **o argumento que amarra o capítulo**. Ex.: para o
cap. 1 do Kurlat, o fio é "por que medir produto é um problema de números-índice, e por que
isso não tem solução livre de arbítrio" — não "tudo que há no capítulo 1".

---

## Checklist antes de salvar

- [ ] **Escopo confirmado com o usuário antes de escrever (R0)**
- [ ] Abre com uma tese em uma frase
- [ ] Áudio: ≤5 segmentos, ≤3 sub-pontos cada, ≤3 numerais por segmento
- [ ] Nomeia ≥2 assuntos a pular (áudio)
- [ ] Escopo em enquadramento positivo (áudio) / trava explícita (slides)
- [ ] Zero instruções de estilo não verificáveis
- [ ] ≥1 instrução sem equivalente em slide (áudio)
- [ ] Idioma da saída declarado — **inglês nos três tipos**, sem exceção
- [ ] Nome de arquivo completo uma vez, depois handle
- [ ] Vídeo: ≤6 batidas, cada uma com **um visual nomeado**, transições que são passos do
      argumento, fechamento com a imagem única
- [ ] 4.400-4.900 chars — rodar o validador
