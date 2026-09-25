---
quiz: "Macro I — Aula 8: AD-AS novo-keynesiano, microfundamentos (Benigno §1-5)"
tags:
  ad: "A curva de demanda agregada"
  firma: "Firmas, mark-up e preços rígidos"
  kappa: "A inclinação da oferta agregada"
  natural: "Produto natural e produto eficiente"
  geo: "Geometria do equilíbrio e juro natural"
  trap: "Armadilhas e leitura do modelo"
---

## ad

Q: No modelo de Benigno, por que a curva de demanda agregada é negativamente inclinada no plano produto-nível de preços?
- Porque um nível de preços maior, dado o preço de longo prazo, reduz a inflação esperada e eleva o juro real.
- Porque um nível de preços maior eleva a demanda por moeda e, com o estoque de moeda dado, obriga o juro a subir.
- Porque um nível de preços maior corrói o valor real da dívida nominal das famílias endividadas.
- Porque um nível de preços maior reduz o salário real e leva as firmas a contratar menos trabalhadores.
<!-- YW5zOjA= -->
> A AD é a equação de Euler reescrita. Com $ar p$ dado e $i$ fixado pelo banco central, um $p$ maior significa $(ar p - p)$ menor, logo juro real maior, logo postergação do consumo. A explicação via demanda por moeda é o mecanismo IS-LM, e **não há estoque de moeda nem curva LM neste modelo**.
> Ref: Benigno (2015), §3, eq. (8), p. 506; regras [[08_adas_microfundamentos]]
> Similar: [[benigno/01-household-and-ad]] §1.7

Q: O parâmetro $\sigma$ que aparece na inclinação da AD é igual a quê?
- À elasticidade de substituição intertemporal do consumo, sem nenhum ajuste adicional.
- À elasticidade de substituição intertemporal multiplicada pela participação do consumo no produto.
- Ao inverso da elasticidade de Frisch da oferta de trabalho, como no termo de custo marginal.
- À elasticidade de substituição entre bens diferenciados que determina o mark-up de monopólio.
<!-- YW5zOjE= -->
> $\sigma \equiv \tilde\sigma s_c$. Só a parte de consumo do produto responde ao juro, então um movimento de um ponto no juro real move o **produto** em $\sigma$, não em $\tilde\sigma$. Todo multiplicador da Aula 9 é função de $\sigma$.
> Ref: Benigno (2015), §3, eq. (6) e nota 4, p. 506
> Similar: [[benigno/01-household-and-ad]] §1.4

Q: Um governo anuncia de forma crível que elevará o imposto sobre consumo no período seguinte. Qual o efeito hoje?
- Nenhum, porque impostos futuros não entram na restrição orçamentária intertemporal da família.
- A demanda cai hoje, porque a família antecipa um $ar c_n$ menor e corta o consumo corrente.
- A demanda sobe hoje, porque o termo $(\bar\tau_c-\tau_c)$ ocupa o mesmo lugar da inflação esperada.
- A oferta agregada se desloca para cima, porque o imposto entra no mark-up agregado corrente.
<!-- YW5zOjI= -->
> O que a família substitui é o preço do consumo **inclusive de impostos** entre datas. O termo $(\bar\tau_c-\tau_c)$ está exatamente no slot de $(\bar p - p)$ na eq. (8), então a promessa é expansionista pelo mesmo mecanismo de uma promessa de inflação. É essa equivalência que sustenta o menu de política da armadilha de liquidez.
> Ref: Benigno (2015), §3, eq. (8), p. 506
> Similar: [[benigno/01-household-and-ad]] §1.5

Q: Qual característica da AD novo-keynesiana não tem contrapartida na AD de livro-texto IS-LM?
- Expectativas sobre o futuro distante deslocam a demanda de hoje, via o problema intertemporal único.
- A curva é negativamente inclinada no plano que tem o produto no eixo horizontal e o preço no vertical.
- A política fiscal desloca a curva quando o gasto público corrente aumenta em relação ao consumo privado.
- O banco central consegue mover a curva alterando o instrumento de política monetária de que dispõe.
<!-- YW5zOjA= -->
> As outras três alternativas valem igualmente para as duas curvas. A linha realmente distintiva é a expectativa: $ar y_n$ entra na eq. (8), então notícias sobre produtividade futura, gasto futuro ou mark-up futuro movem a demanda corrente sem que nada real tenha acontecido ainda.
> Ref: Benigno (2015), §3 e §5, Fig. 4, p. 511
> Similar: [[benigno/01-household-and-ad]] §1.6

## firma

Q: De onde vem a forma de mark-up constante do preço ótimo da firma, eq. (11)?
- Da rigidez de preços, que impede a fração $\alpha$ das firmas de reotimizar no curto prazo.
- Da hipótese de retornos constantes de escala na função de produção linear no trabalho.
- Da condição intratemporal da família, que fixa o salário real em termos da desutilidade do trabalho.
- Da elasticidade constante da demanda Dixit-Stiglitz enfrentada por cada produtor diferenciado.
<!-- YW5zOjM= -->
> Elasticidade constante $	heta$ implica mark-up constante $	heta/(	heta-1)$. É isso que torna o modelo tratável. A rigidez determina quem pode aplicar esse preço, não a forma dele; e a condição intratemporal da família é usada depois, para eliminar o salário real.
> Ref: Benigno (2015), §4, eqs. (9) e (11), p. 507
> Similar: [[benigno/02-firms-and-as]] §2.2

Q: O mark-up agregado $\mu$ da eq. (13) reúne poder de monopólio e quatro impostos. Qual a consequência mais importante disso?
- O modelo consegue distinguir choques de oferta verdadeiros de choques puramente tributários.
- O modelo não distingue um choque de OPEC de um aumento de IVA ou de concentração de mercado.
- O mark-up deixa de afetar o produto natural, porque os impostos se cancelam na agregação.
- A política fiscal passa a ser neutra no curto prazo, já que só o nível de $\mu$ importa.
<!-- YW5zOjE= -->
> Os cinco componentes entram multiplicativamente na mesma cunha. Nada no modelo os separa — e é justamente por isso que o "choque de mark-up" da Aula 9 pode ser lido como petróleo, como imposto ou como poder de mercado, com as mesmas consequências de política.
> Ref: Benigno (2015), §4, eq. (13), p. 507
> Similar: [[benigno/02-firms-and-as]] §2.3

Q: Benigno oferece duas justificativas para a rigidez de preços. Qual é a segunda delas?
- Que as firmas enfrentam custos de menu explícitos (e de primeira ordem) nos microdados.
- Que sindicatos impedem o ajuste de salários nominais e portanto de custos marginais.
- Que a mesma álgebra descreve um modelo de informação rígida, com $P^e$ fixado antes do choque.
- Que o banco central fixa diretamente uma fração dos preços por meio de controles administrativos.
<!-- YW5zOjI= -->
> A primeira justificativa é a perda de segunda ordem (Mankiw, 1985): no ótimo a derivada do lucro é zero, então qualquer custo de menu minúsculo racionaliza não mover. A segunda é a releitura como *sticky information*, que é a saída para quem não aceita rigidez literal.
> Ref: Benigno (2015), §4, p. 507
> Similar: [[benigno/02-firms-and-as]] §2.1

Q: Na derivação do produto natural, o que significa a condição de que $\tilde P / P = 1$?
- Que o nível de preços corrente coincide com o nível de preços esperado pelas firmas rígidas.
- Que a fração $\alpha$ de firmas rígidas é igual à fração de firmas que reotimizam livremente.
- Que o mark-up agregado é zero e a economia atinge a alocação que o planejador escolheria.
- Que todas as firmas reotimizam, de modo que o preço desejado coincide com o índice de preços.
<!-- YW5zOjM= -->
> Produto natural é definido como o que prevaleceria com **todos** os preços flexíveis. Aí $P(j)=P$ para todo $j$ e o lado esquerdo da eq. (12) vale um. Note que isso não exige mark-up nulo: o natural ainda carrega a cunha de mark-up, e é por isso que ele difere do eficiente.
> Ref: Benigno (2015), §4.1, eq. (14), p. 508
> Similar: [[benigno/02-firms-and-as]] §2.4

## kappa

Q: A fração $\alpha$ de firmas com preço pré-fixado aumenta. O que acontece com a curva de oferta agregada?
- Fica mais achatada, porque $\alpha$ está no denominador de $\kappa$ e menos preços podem se mover.
- Fica mais inclinada, porque menos firmas absorvem o choque e cada uma precisa mover mais o preço.
- Não muda, porque $\kappa$ depende apenas dos parâmetros de preferência $\sigma$ e $\eta$.
- Fica vertical, porque a economia se aproxima do caso clássico com preços plenamente flexíveis.
<!-- YW5zOjA= -->
> $\kappa=(1-lpha)(\sigma^{-1}+\eta)/lpha$. Com $lpha	o1$, $\kappa	o0$: o produto se move e o nível de preços não. O caso vertical é o oposto, $lpha	o0$. Este é o erro de sinal mais comum do tópico, e o mnemônico é que $lpha$ está embaixo.
> Ref: Benigno (2015), §4.1, eq. (17), p. 508
> Similar: [[benigno/02-firms-and-as]] §2.6

Q: O termo $(\sigma^{-1}+\eta)$ que aparece em $\kappa$ tem qual interpretação econômica?
- Mede a fração de firmas que conseguem reotimizar o preço dentro do período corrente.
- Mede a elasticidade de substituição entre variedades que determina o poder de mercado.
- Mede quanto o custo marginal real sobe quando o produto se afasta do nível natural.
- Mede a sensibilidade da demanda agregada a mudanças no instrumento de política monetária.
<!-- YW5zOjI= -->
> Produzir acima do natural puxa o salário real por dois canais: ao longo da oferta de trabalho ($\eta$) e ao longo da margem de suavização do consumo ($\sigma^{-1}$). A eq. (16) é literalmente a equação de custo marginal, e $\kappa$ é ela multiplicada por $(1-\alpha)/\alpha$.
> Ref: Benigno (2015), §4.1, eq. (16), p. 508
> Similar: [[benigno/02-firms-and-as]] §2.5

Q: A curva de oferta agregada deste modelo sempre passa por qual ponto?
- Pelo ponto cujo preço é $\bar p$ e cujo produto é o produto eficiente $y_e$ do período.
- Pelo ponto cujo preço é $p^e$ e cujo produto é o produto natural $y_n$ do período.
- Pelo ponto em que a demanda agregada cruza o eixo vertical do nível de preços.
- Pelo ponto cujo preço é $p^e$ e cujo produto é o produto efetivamente observado $y$.
<!-- YW5zOjE= -->
> Basta fazer $y=y_n$ na eq. (17): então $p=p^e$. As duas coordenadas são predeterminadas ou reais, e é isso que dá a regra de traçado: recalcule $y_n$ pela eq. (15) e redesenhe a reta de inclinação $\kappa$ pelo novo ponto.
> Ref: Benigno (2015), §5, Figs. 1-2, p. 510
> Similar: [[benigno/02-firms-and-as]] §2.7

Q: Por que a curva (17) **não** é uma curva de Phillips novo-keynesiana?
- Porque foi derivada de concorrência monopolística em vez de concorrência perfeita entre firmas.
- Porque depende do hiato contra o produto eficiente em vez do hiato contra o natural.
- Porque a fração de firmas rígidas é fixa e não sorteada aleatoriamente a cada período.
- Porque relaciona o nível de preços ao hiato, sem termo de inflação futura esperada.
<!-- YW5zOjM= -->
> É a curva de Phillips **novo-clássica**, no nível de preços, que Phelps e Lucas derivaram de informação imperfeita. O próprio artigo diz isso e a nota 7 explica a escolha: a via Calvo acrescentaria termos prospectivos sem mudar nenhum resultado qualitativo. O custo é real e está no §12: o modelo não fala de dinâmica de inflação.
> Ref: Benigno (2015), §4.1 e nota 7, p. 508
> Similar: [[benigno/02-firms-and-as]] §2.8

## natural

Q: Qual é exatamente a diferença entre produto natural e produto eficiente neste modelo?
- O natural supõe preços rígidos e o eficiente supõe preços flexíveis, na mesma economia descentralizada.
- O natural é de curto prazo e o eficiente é o valor para o qual a economia converge no longo prazo.
- O natural é o que o mercado com preços flexíveis produz; o eficiente é o que um planejador escolheria.
- O natural inclui o gasto público na demanda agregada e o eficiente exclui, por não gerar utilidade.
<!-- YW5zOjI= -->
> Ambos supõem preços flexíveis. O que os separa é a cunha $\mu$: o mercado iguala a TMS a $A/(1+\mu)$ e o planejador a iguala a $A$. Daí $y_n-y_e=-\mu/(\sigma^{-1}+\eta)$, e toda a Aula 9 é consequência dessa subtração.
> Ref: Benigno (2015), §4.4, eq. (19), p. 509
> Similar: [[benigno/03-natural-and-efficient]] §3.3

Q: Um choque eleva a produtividade corrente. O que acontece com a diferença $y_n-y_e$?
- Fica inalterada, porque os coeficientes de $a$ em (15) e (19) são idênticos e se cancelam.
- Aumenta, porque $y_n$ responde mais à produtividade corrente do que $y_e$ responde.
- Diminui, porque o planejador consegue explorar a nova tecnologia melhor que o mercado.
- Torna-se positiva, revertendo o sinal da cunha de mark-up que existia antes do choque.
<!-- YW5zOjA= -->
> Produtividade e gasto público movem os dois níveis **exatamente na mesma medida**. Só o mark-up move a diferença. É esse fato que garante a coincidência divina: um instrumento atinge dois alvos porque os alvos não se separaram.
> Ref: Benigno (2015), §4.4, p. 509
> Similar: [[benigno/03-natural-and-efficient]] §3.4

Q: No longo prazo do modelo, qual afirmação é correta sobre neutralidade?
- A moeda é neutra e a política fiscal também, porque ambas só afetam variáveis nominais.
- A moeda não é neutra, porque o nível de preços de longo prazo entra no produto natural.
- Nem a moeda nem a política fiscal têm efeito, porque o produto é fixado pela dotação de fatores.
- A moeda é neutra, mas qualquer aumento de imposto eleva o mark-up e reduz produto e consumo.
<!-- YW5zOjM= -->
> $\bar p$ não aparece em $\bar y_n$ nem em $\bar c_n$: dicotomia clássica. Mas $\bar\mu$ aparece com sinal negativo nos dois, e pela eq. (13) todo imposto é componente de $\bar\mu$. Neutralidade monetária não implica neutralidade fiscal.
> Ref: Benigno (2015), §4.2, p. 508
> Similar: [[benigno/03-natural-and-efficient]] §3.1

Q: Por que o consumo natural de longo prazo $\bar c_n$ merece um nome próprio?
- Porque determina a inclinação $\kappa$ da oferta agregada de curto prazo do período corrente.
- Porque é o único canal pelo qual o futuro alcança o presente, entrando na AD via $\bar y_n$.
- Porque é o alvo de bem-estar contra o qual a política monetária ótima deve ser avaliada.
- Porque fixa a fração de firmas que conseguem reotimizar preços dentro do período corrente.
<!-- YW5zOjE= -->
> Tudo que torna o amanhã mais rico — $\bar a$ maior, $\bar g$ menor, $\bar\mu$ menor — eleva a demanda hoje pelo motivo de suavização. O caso de otimismo do §6.3 é apenas um choque nesse objeto, e o de pessimismo é a largada da armadilha de liquidez.
> Ref: Benigno (2015), §4.2, p. 508
> Similar: [[benigno/03-natural-and-efficient]] §3.1

## geo

Q: Nas Figuras 3 a 5 as duas curvas se cruzam no produto natural com $p=p^e$. O que isso significa?
- Que já se supôs que o banco central fixou o juro nominal exatamente no nível natural.
- Que é uma propriedade do modelo, válida qualquer que seja o instrumento de política escolhido.
- Que o mark-up agregado é necessariamente igual a zero na configuração inicial desenhada.
- Que a fração de firmas rígidas foi calibrada de modo a anular o hiato no ponto inicial.
<!-- YW5zOjA= -->
> O artigo diz isso explicitamente na p. 510: a hipótese "requer fixar o juro nominal e real no nível natural". A âncora da AS é propriedade do modelo; a da AD é uma normalização. Sempre que a figura mostra esse cruzamento, a política ótima já foi suposta.
> Ref: Benigno (2015), §5, p. 510
> Similar: [[benigno/04-equilibrium-geometry]] §4.1

Q: O juro natural $r_n$ contém o termo $\sigma^{-1}(\bar y_n - y_n)$. O que ele diz?
- Que o juro natural sobe quando o mark-up corrente aumenta em relação ao mark-up esperado.
- Que o juro natural depende do nível de tecnologia e não da taxa de crescimento esperada.
- Que o juro natural sobe quando a economia espera ser mais rica amanhã do que é hoje.
- Que o juro natural é constante sempre que o banco central mantém o nível de preços estável.
<!-- YW5zOjI= -->
> Uma economia que espera ficar rica quer tomar emprestado hoje, e é preciso um juro real alto para conter isso. A leitura simétrica é a que importa: perspectivas ruins de longo prazo empurram $r_n$ **para baixo**, possivelmente abaixo de zero — e essa é a origem da armadilha de liquidez.
> Ref: Benigno (2015), §5, p. 511
> Similar: [[benigno/04-equilibrium-geometry]] §4.3

Q: Um choque de produtividade **corrente** desloca a AS mas não a AD. Qual fração do choque aparece no produto?
- A fração inteira, porque o produto sempre acompanha integralmente o produto natural.
- A fração $1/(1+\sigma\kappa)$, que é o complemento da resposta a um choque futuro.
- Nenhuma, porque a demanda agregada não se moveu e ela é quem determina o produto.
- A fração $\sigma\kappa/(1+\sigma\kappa)$, sempre estritamente entre zero e um.
<!-- YW5zOjM= -->
> Da máquina de estática comparativa, $dy/dy_n=\sigma\kappa/(1+\sigma\kappa)$. O resíduo é o hiato, $-dy_n/(1+\sigma\kappa)$, negativo para um choque positivo. É por isso que boa notícia para o produto não é boa notícia para o hiato.
> Ref: Benigno (2015), §5-§6, p. 511
> Similar: [[benigno/04-equilibrium-geometry]] §4.4

Q: Quais dois instrumentos ocupam exatamente o mesmo lugar na curva de demanda agregada?
- O gasto público corrente e o gasto público de longo prazo, com sinais opostos entre si.
- O juro nominal corrente e o nível de preços esperado de longo prazo, com sinais opostos.
- O imposto sobre consumo corrente e a fração de firmas que conseguem reotimizar preços.
- O produto natural corrente e o produto natural de longo prazo, com o mesmo coeficiente.
<!-- YW5zOjE= -->
> $-\sigma\,di$ e $+\sigma\,d\bar p$ entram com o mesmo coeficiente. Cortar o juro em um ponto e elevar o preço de longo prazo em um ponto fazem a mesma coisa com a demanda. Com $i$ travado em zero, só o segundo sobrevive — e é esse o conteúdo inteiro da saída da armadilha.
> Ref: Benigno (2015), §5 e §9, p. 511
> Similar: [[benigno/04-equilibrium-geometry]] §4.4

## trap

Q: Um aluno explica a inclinação da AD dizendo que preços maiores elevam a demanda por moeda e empurram o juro para cima. Qual é o problema?
- Nenhum, é uma forma abreviada e correta do mesmo mecanismo intertemporal do modelo.
- Não existe estoque de moeda nem curva LM no modelo, e o banco central fixa o juro nominal.
- O problema é apenas de ordem, porque o juro sobe antes e não depois do nível de preços.
- O argumento está certo no curto prazo, mas falha quando os preços são plenamente flexíveis.
<!-- YW5zOjE= -->
> Não é um atalho, é outro modelo. Aqui o banco central **fixa** $i$; a demanda cai porque a inflação esperada cai e o juro real sobe. Se a explicação precisa do mercado monetário, ela saiu do artigo.
> Ref: Benigno (2015), §3, p. 506
> Similar: [[benigno/01-household-and-ad]] §1.7

Q: Por que um aumento **permanente** do gasto público não desloca a curva de demanda agregada?
- Porque o gasto público entra na AD apenas pelo produto natural, e não diretamente na equação.
- Porque o gasto público é financiado por impostos lump-sum e vale a equivalência ricardiana.
- Porque o efeito riqueza negativo cancela exatamente o efeito direto sobre a demanda corrente.
- Porque na eq. (8) o gasto entra como a diferença $(g-\bar g)$, que é zero se ambos sobem juntos.
<!-- YW5zOjM= -->
> Só a diferença entre gasto corrente e gasto de longo prazo move a AD. Esse fato isolado é a razão de a política fiscal permanente não alterar o hiato na Aula 9 — todo termo da eq. (23) é uma diferença curto-menos-longo.
> Ref: Benigno (2015), §3, eq. (8), p. 506
> Similar: [[benigno/01-household-and-ad]] §1.4

Q: A economia tem $\mu>0$ em estado estacionário. O que isso implica para o hiato?
- Que o produto natural fica permanentemente abaixo do eficiente, e o hiato é de nível.
- Que o hiato contra o natural e o hiato contra o eficiente coincidem em todos os períodos.
- Que a política monetária consegue eliminar os dois hiatos simultaneamente sem trade-off.
- Que o mark-up deixa de afetar o produto natural, porque é constante ao longo do tempo.
<!-- YW5zOjA= -->
> Com $\mu>0$ a subtração $y_n-y_e=-\mu/(\sigma^{-1}+\eta)$ é negativa e permanente. A nota 21 do artigo é cuidadosa: a função perda quadrática é aproximada em torno de um estado estacionário **eficiente**, e com distorção o alvo relevante pode nem ser $y_e$.
> Ref: Benigno (2015), §4.4 e nota 21, pp. 509 e 522
> Similar: [[benigno/03-natural-and-efficient]] §3.4

Q: Qual é a leitura correta da condição intratemporal $v_l(L)/u_c(C)=W/P$ dentro deste modelo?
- É uma equação do lado da demanda, que determina quanto a família decide consumir hoje.
- É a condição de equilíbrio do mercado de crédito entre poupadores e tomadores de recursos.
- É uma equação do lado da oferta: a firma a usa para escrever custo marginal em função do produto.
- É a definição do juro natural, que iguala poupança desejada a investimento desejado.
<!-- YW5zOjI= -->
> Ela é da família, mas quem a usa é a firma: substituída na eq. (12), elimina o salário real e produz a relação entre preço desejado e produto. Por isso a disposição a trabalhar é o que faz a oferta agregada ter inclinação positiva.
> Ref: Benigno (2015), §3 e §4.1, eqs. (7) e (12), pp. 506-507
> Similar: [[benigno/02-firms-and-as]] §2.3
