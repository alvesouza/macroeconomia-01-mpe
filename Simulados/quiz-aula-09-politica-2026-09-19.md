---
quiz: "Macro I — Aula 9: AD-AS novo-keynesiano, política econômica (Benigno §6-12)"
tags:
  prod: "Choques de produtividade e coincidência divina"
  markup: "Choques de mark-up e o trade-off"
  fiscal: "Multiplicadores fiscais"
  zlb: "Armadilha de liquidez"
  delev: "Desalavancagem e efeito Fisher"
  otima: "Política monetária ótima"
---

## prod

Q: Um ganho de produtividade **temporário** atinge a economia e o banco central não reage. O que acontece?
- O produto sobe, os preços caem e o hiato contra o natural fica $\textbf{negativo}$.
- O produto sobe, os preços sobem e o hiato contra o natural fica $\textbf{positivo}$.
- O produto fica inalterado, porque a curva de demanda agregada $\textbf{não}$ se desloca.
- O produto sobe, os preços caem e o hiato contra o natural permanece $\textbf{nulo}$.
<!-- YW5zOjA= -->
> A AS desloca-se para baixo e a AD não se move. Da máquina: $dy=\sigma\kappa\,dy_n/(1+\sigma\kappa)>0$, $dp<0$ e $d(y-y_n)=-dy_n/(1+\sigma\kappa)<0$. Boa notícia para o produto não é boa notícia para o hiato: só $(1-\alpha)$ das firmas corta preços, e a queda do juro real é insuficiente.
> Ref: Benigno (2015), §6.1, Fig. 6, p. 512; regras [[09_adas_politica]]
> Similar: [[benigno/05-productivity-shocks]] §5.1

Q: Por que um ganho de produtividade **permanente** não exige nenhuma resposta de política?
- Porque o produto natural $y_n$ não se move quando o choque é permanente em vez de temporário.
- Porque o juro natural $r_n$ depende do crescimento esperado, que um choque de nível não altera.
- Porque a curva de oferta agregada $\textbf{AS}$ é vertical no longo prazo, por construção.
- Porque o mark-up $\mu$ absorve integralmente o choque e mantém o hiato de bem-estar fechado.
<!-- YW5zOjE= -->
> $dr_n=\sigma^{-1}(d\bar y_n-dy_n)=0$ quando os dois sobem igualmente. A AD sobe exatamente o quanto faz a nova AS cruzá-la no novo natural: hiato zero, preço inalterado. A lição geral é que a política monetária não persegue o **nível** de tecnologia, e sim a diferença entre o natural futuro e o corrente.
> Ref: Benigno (2015), §6.2, Fig. 7, p. 513
> Similar: [[benigno/05-productivity-shocks]] §5.2

Q: A economia fica otimista sobre a produtividade futura, sem que nada mude hoje. Qual a política ótima?
- Cortar o juro nominal, porque o produto corrente ainda não subiu e há folga a explorar.
- Manter o juro, porque apenas a produtividade futura mudou e o natural corrente é o mesmo.
- Elevar o juro, porque a demanda subiu sem que a capacidade corrente tenha se movido.
- Elevar o gasto público, porque só a política fiscal alcança expectativas sobre o futuro.
<!-- YW5zOjI= -->
> A AS não se move e a AD sobe. Toda a resposta do produto **é** hiato, positivo contra o natural e contra o eficiente: a economia superaquece com base numa previsão. Política ótima $di=d\bar y_n/\sigma>0$, que é exatamente $dr_n$.
> Ref: Benigno (2015), §6.3, Fig. 8, p. 513
> Similar: [[benigno/05-productivity-shocks]] §5.3

Q: Qual enunciado sobre a coincidência divina é correto?
- Ela vale porque produtividade e gasto movem $y_n$ e $y_e$ na mesma medida, sem tocar $\mu$.
- Ela vale sempre que o banco central adota metas de inflação, qualquer que seja o choque.
- Ela é uma coincidência numérica que depende da calibração escolhida para $\alpha$ e $\theta$.
- Ela vale porque a curva de oferta agregada passa pelo ponto $(p^e, y_e)$ por construção.
<!-- YW5zOjA= -->
> Não é coincidência: é consequência de o choque ser **eficiente**. Duas condições a sustentam e ambas são examináveis — flexibilidade salarial (nota 9) e um estado estacionário eficiente (nota 21). Com salários rígidos, um choque de produtividade move a alocação eficiente sem deixar o salário real chegar lá.
> Ref: Benigno (2015), §6 e notas 9 e 21, pp. 513 e 522
> Similar: [[benigno/05-productivity-shocks]] §5.5

## markup

Q: Um choque de mark-up positivo atinge a economia. O que acontece com os **dois** hiatos?
- Ambos ficam negativos, porque o produto cai abaixo dos dois níveis de referência.
- Ambos ficam positivos, porque $y_n$ cai mais do que o produto efetivamente observado.
- O hiato contra o natural fica negativo e o hiato contra o eficiente fica positivo.
- O hiato contra o natural fica positivo e o hiato contra o eficiente fica negativo.
<!-- YW5zOjM= -->
> $y_n$ cai e $y_e$ não se move. O produto fica **acima** do natural, e é por isso que os preços sobem — pela eq. (17) só esse hiato move preços. E fica **abaixo** do eficiente, e é por isso que o bem-estar cai. Quem reporta "o hiato do produto" já errou a questão.
> Ref: Benigno (2015), §7, Fig. 9, p. 513
> Similar: [[benigno/06-markup-shocks]] §6.2

Q: Depois de um choque de mark-up, o banco central quer estabilizar os preços. O que precisa fazer?
- Cortar o juro, e o resultado é a maior alta de preços entre as três opções disponíveis.
- Elevar o juro, e o resultado é a contração mais profunda entre as três opções disponíveis.
- Manter o juro, e o resultado é o ponto intermediário entre estabilizar preços e produto.
- Elevar o gasto público, porque a política monetária isolada não alcança o nível de preços.
<!-- YW5zOjE= -->
> Estabilizar preços exige fechar o hiato contra o **natural**, que caiu: $di=-dy_n/\sigma>0$. O produto cai então o $dy_n$ inteiro — mais fundo do que se nada fosse feito. Entregar produto eficiente exigiria o oposto, um corte, com a maior alta de preços. É esse sinal oposto que torna o trade-off genuíno.
> Ref: Benigno (2015), §7, Fig. 9, p. 514
> Similar: [[benigno/06-markup-shocks]] §6.3

Q: Qual é o teste geral para saber se um choque cria um trade-off de política?
- Basta verificar se o choque desloca a curva $\textbf{AS}$ em vez da curva de demanda.
- Basta verificar se o choque é temporário, já que só choques permanentes criam trade-off.
- Basta verificar se o choque move o mark-up $\mu$, único termo em $y_n-y_e$.
- Basta verificar se o choque afeta o produto corrente e o produto futuro de forma desigual.
<!-- YW5zOjI= -->
> $y_n-y_e=-\mu/(\sigma^{-1}+\eta)$. Só $\mu$ aparece. Produtividade e gasto deslocam a AS sem criar trade-off, então o critério da alternativa sobre deslocar a AS é insuficiente. Impostos distorcivos, poder de mercado e petróleo movem $\mu$ e criam trade-off.
> Ref: Benigno (2015), §7, p. 514
> Similar: [[benigno/06-markup-shocks]] §6.4

Q: Uma alta **permanente** do mark-up (corrente e de longo prazo) produz o quê?
- Hiato positivo contra o natural e alta de preços, exigindo aperto monetário imediato.
- Hiato negativo e deflação, porque a AD cai mais do que a $\textbf{AS}$ se desloca.
- Nenhum efeito real, porque o mark-up é neutro quando muda de forma permanente e crível.
- Hiato nulo e preços estáveis, com o produto caindo $dy_n$ e perda de bem-estar permanente.
<!-- YW5zOjM= -->
> A AS sobe e a AD **também** cai, porque $\bar y_n$ cai com $\bar\mu$. Como $d\bar y_n=dy_n$, a máquina dá hiato zero e preço inalterado. Mas o hiato de bem-estar é $dy_n<0$ e permanente, e nenhum juro o fecha: é problema de oferta, não de estabilização.
> Ref: Benigno (2015), §7, p. 513
> Similar: [[benigno/06-markup-shocks]] §6.5

## fiscal

Q: O multiplicador do gasto público corrente sobre o **produto** é próximo de 0,96, mas sobre o **hiato** é cerca de 0,06. Por quê?
- Porque o gasto público eleva o produto natural quase tanto quanto eleva o produto efetivo.
- Porque o gasto público é financiado por impostos distorcivos que anulam parte do estímulo.
- Porque a curva de oferta agregada é vertical no horizonte relevante para a política fiscal.
- Porque o multiplicador sobre o hiato ignora o efeito do gasto sobre o consumo privado.
<!-- YW5zOjA= -->
> Gasto público é efeito riqueza negativo: a família fica mais pobre, tira menos lazer e trabalha mais, então $y_n$ sobe junto. Quase todo o ganho de produto é acompanhado por alta de capacidade, e só o resíduo — proporcional a $\eta$ — vira hiato. Daí $m_{\bar g}=\eta/D$.
> Ref: Benigno (2015), §8, eqs. (22)-(23), Tabela 2, p. 516
> Similar: [[benigno/07-fiscal-multipliers]] §7.4

Q: Qual instrumento fiscal eleva o produto e ao mesmo tempo **alarga** o hiato?
- Um aumento do gasto público corrente financiado com transferências lump-sum.
- Um corte no imposto sobre vendas e folha de longo prazo, anunciado de forma crível.
- Um corte no imposto sobre consumo corrente, com o imposto futuro mantido constante.
- Um aumento do imposto sobre consumo futuro, com o imposto corrente inalterado.
<!-- YW5zOjI= -->
> Na eq. (22) $\tau_c$ entra com $-m_{\tau_c}$, então cortá-lo eleva o produto; na eq. (23) entra com $-m_{\bar\tau_c}$, então cortá-lo alarga o hiato. O corte eleva o natural mais do que eleva o produto. O mesmo vale para um corte corrente em $\tau$, que o artigo diz que "deve ser evitado" na armadilha.
> Ref: Benigno (2015), §8-§9, eqs. (22)-(23), pp. 515-517
> Similar: [[benigno/07-fiscal-multipliers]] §7.4

Q: Por que uma expansão fiscal **permanente** não altera o hiato do produto?
- Porque a equivalência ricardiana (com impostos lump-sum) anula todo efeito fiscal real.
- Porque todo termo da eq. (23) é uma diferença entre valor corrente e valor de longo prazo.
- Porque o gasto permanente é integralmente compensado por queda do consumo privado.
- Porque o banco central reage automaticamente para manter o hiato fechado o tempo todo.
<!-- YW5zOjE= -->
> $y-y_n = m_{\bar g}(g-\bar g)+m_{\bar\tau}(\tau-\bar\tau)-m_{\bar\tau_c}(\tau_c-\bar\tau_c)$. Iguale corrente e longo prazo e tudo zera, quaisquer que sejam os níveis. A política fiscal estabiliza **sendo temporária**. Isso não é equivalência ricardiana: um aumento de $G$ tem efeitos reais, só não sobre o hiato.
> Ref: Benigno (2015), §8, eq. (23), p. 515
> Similar: [[benigno/07-fiscal-multipliers]] §7.4

Q: Sobre o hiato contra o produto **eficiente**, qual afirmação é correta?
- Ele carrega os multiplicadores de gasto da eq. (22) e os de imposto da eq. (23).
- Ele coincide com o hiato contra o natural sempre que a política fiscal é lump-sum.
- Ele não depende de impostos distorcivos, porque estes não afetam o produto eficiente.
- Ele carrega os multiplicadores de imposto da eq. (22) e os de gasto da eq. (23).
<!-- YW5zOjM= -->
> Impostos distorcivos não movem $y_e$, então o efeito deles sobre o hiato eficiente é o efeito **inteiro** sobre o produto — multiplicadores da (22). Gasto corrente move $y_n$ e $y_e$ igualmente, então sobra só a parte pequena — multiplicadores da (23). O texto do artigo na p. 515 afirma o contrário e está errado; a frase seguinte dele confirma a correção.
> Ref: Benigno (2015), §8, p. 515
> Similar: [[benigno/07-fiscal-multipliers]] §7.5

## zlb

Q: Qual é a definição precisa de armadilha de liquidez neste modelo?
- O estado em que o juro nominal $i$ chega a zero, qualquer que seja o juro natural $r_n$.
- O estado em que a demanda agregada é horizontal e a política fiscal perde toda a eficácia.
- O estado em que o juro natural $r_n$ é negativo e o piso nominal impede fechar o hiato.
- O estado em que a inflação esperada é negativa e a deflação se torna autorrealizável.
<!-- YW5zOjI= -->
> Com preços de longo prazo ancorados, o melhor hiato alcançável é $\sigma r_n/(1+\sigma\kappa)$. Se $r_n\ge0$ o hiato fecha; se $r_n<0$ a economia fica presa. A armadilha não é sobre o juro nominal, é sobre o **natural** — e reformular assim é o que torna a saída óbvia.
> Ref: Benigno (2015), §9, Fig. 11, p. 517
> Similar: [[benigno/08-liquidity-trap]] §8.2

Q: Com $i=0$, qual compromisso fecha exatamente o hiato do produto?
- Elevar o preço de longo prazo em $\bar p-p^e=-r_n$, isto é, o módulo do juro natural.
- Elevar o gasto público corrente até o produto atingir o natural $y_n$ do período.
- Reduzir o imposto sobre vendas e folha corrente até anular a cunha de mark-up agregada.
- Fixar uma meta de nível de preços corrente, deixando o preço de longo prazo inalterado.
<!-- YW5zOjA= -->
> $-\sigma\,di$ e $+\sigma\,d\bar p$ ocupam o mesmo slot na AD. Travado o primeiro, use o segundo. O mecanismo, enunciado com cuidado: $\bar p$ maior eleva a inflação esperada, que reduz o juro **real** com o nominal parado em zero, que eleva o consumo. Exige credibilidade, porque é promessa sobre um futuro em que o banco quererá voltar atrás.
> Ref: Benigno (2015), §9, Fig. 12, p. 518
> Similar: [[benigno/08-liquidity-trap]] §8.4

Q: Por que Benigno prefere instrumentos fiscais de **longo prazo** dentro da armadilha?
- Porque instrumentos de longo prazo têm multiplicadores maiores sobre o produto corrente.
- Porque só eles respeitam a equivalência ricardiana e por isso não distorcem o consumo.
- Porque o banco central não consegue observar em tempo real o gasto público corrente.
- Porque o gasto corrente empurra os preços para baixo e agrava balanços com dívida nominal.
<!-- YW5zOjM= -->
> Três razões, cada uma mapeada numa curva: o gasto corrente também desloca a AS (eleva $y_n$) e segura preços, o que numa deflação piora balanços; ele expulsa consumo privado enquanto cortar gasto futuro o eleva; e estímulo corrente precisa ser temporário e pago depois com impostos contracionistas.
> Ref: Benigno (2015), §9, pp. 517-518
> Similar: [[benigno/08-liquidity-trap]] §8.5

Q: Em que a conclusão deste modelo difere da leitura IS-LM tradicional da armadilha?
- Não difere: em ambos apenas a política fiscal tem eficácia quando o juro atinge o piso.
- Aqui a política monetária muda de instrumento, do juro nominal para o preço de longo prazo.
- Aqui a política fiscal é totalmente ineficaz, porque vale a equivalência ricardiana estrita.
- Aqui o piso do juro nominal não existe, porque a economia modelada é inteiramente sem moeda.
<!-- YW5zOjE= -->
> A demanda depende do juro **real**, e o real depende de uma expectativa sobre a qual o banco ainda pode agir. A nota 11 é mais cuidadosa sobre o piso: numa economia genuinamente sem moeda não haveria bound algum, e ele existe só porque o papel-moeda rende zero e guarda valor.
> Ref: Benigno (2015), §9 e nota 11, p. 517
> Similar: [[benigno/08-liquidity-trap]] §8.6

## delev

Q: Com uma fração de famílias no limite de endividamento, por que a curva de demanda agregada pode ficar **positivamente** inclinada?
- Porque preços maiores reduzem o valor real da dívida nominal herdada e liberam consumo.
- Porque os tomadores deixam de responder ao juro e a curva perde o canal intertemporal.
- Porque a oferta agregada também muda de sinal quando há famílias restritas ao crédito.
- Porque o produto natural passa a depender da distribuição de riqueza entre os dois tipos.
<!-- YW5zOjA= -->
> O efeito Fisher. A inclinação é $-1/\varpi$ com $\varpi=\sigma-d_0(1-\beta)(1-\chi)/\chi$, e $\varpi$ vira negativo quando a dívida inicial é alta ou a fração de poupadores é baixa. Note que a AS **não** muda: a utilidade exponencial mantém o natural independente da distribuição.
> Ref: Benigno (2015), §10, eq. (32), Fig. 13, pp. 519-521
> Similar: [[benigno/09-deleveraging]] §9.4

Q: O que é o "paradoxo do esforço" (*paradox of toil*) neste modelo?
- Que mais famílias trabalhando eleva o desemprego de equilíbrio por congestão de matching.
- Que poupar mais no agregado reduz a poupança efetivamente realizada pelas famílias.
- Que um choque favorável de oferta, que empurra preços para baixo, contrai a economia.
- Que preços mais flexíveis aprofundam a contração em vez de acelerar o ajuste automático.
<!-- YW5zOjI= -->
> Com a AD positivamente inclinada, deslocar a AS para baixo derruba os preços, o que destrói consumo dos tomadores mais rápido do que o produto barato cria demanda. As outras duas descrições existem no modelo, mas são os paradoxos da poupança e da flexibilidade.
> Ref: Benigno (2015), §10, p. 520
> Similar: [[benigno/09-deleveraging]] §9.5

Q: Qual hipótese faz os paradoxos do esforço e da flexibilidade **desaparecerem**?
- Que a fração de tomadores seja inferior a um terço da população de famílias.
- Que a dívida inicial esteja abaixo de cem por cento do produto de estado estacionário.
- Que o banco central consiga levar o juro nominal a valores negativos sem restrição.
- Que o nível de preços de longo prazo esteja ancorado, seja qual for o preço corrente.
<!-- YW5zOjM= -->
> Nota 20, p. 520. Se $\bar p$ está ancorado seja qual for $p$, a AD volta a ser desenhada com inclinação negativa para um preço futuro dado, e os dois paradoxos somem. Eles não são propriedade da dívida sozinha: precisam que o canal de expectativas esteja desligado.
> Ref: Benigno (2015), §10, nota 20, p. 520
> Similar: [[benigno/09-deleveraging]] §9.5

Q: Por que o multiplicador do gasto público excede um na desalavancagem, se era menor que um na Tabela 2?
- Porque a oferta agregada se torna horizontal e o produto passa a ser determinado pela demanda.
- Porque os dois vazamentos usuais — alta do juro real e suavização — deixam de operar.
- Porque o produto natural deixa de responder ao gasto público quando há restrição de crédito.
- Porque a equivalência ricardiana passa a valer e as transferências deixam de ser neutras.
<!-- YW5zOjE= -->
> Em tempos normais o multiplicador fica abaixo de um porque preços sobem, o juro real sobe e o consumo privado é expulso; e porque toda família suaviza. Na armadilha o nominal não pode subir e uma fração $1-\chi$ gasta cada unidade recebida. Os dois vazamentos são tapados. Note que a equivalência ricardiana **falha** aqui, não passa a valer.
> Ref: Benigno (2015), §10, p. 521
> Similar: [[benigno/09-deleveraging]] §9.6

## otima

Q: A função perda da eq. (33) mede o hiato do produto contra qual referência, e por quê?
- Contra o produto natural, porque é esse hiato que move o nível de preços na oferta agregada.
- Contra o produto eficiente, porque famílias se importam com consumo e lazer, não com custo marginal.
- Contra o produto de longo prazo, porque a aproximação é tomada em torno do estado estacionário.
- Contra o produto observado no período anterior, porque a perda é definida em termos de variações.
<!-- YW5zOjE= -->
> A perda vem de uma aproximação de segunda ordem da utilidade da família. Quem consome e trabalha é a família, e o que ela perde é distância do que um planejador escolheria. O hiato contra o natural aparece, sim, mas dentro do termo de preços, via $p-p^e=\kappa(y-y_n)$.
> Ref: Benigno (2015), §11, eq. (33), p. 521
> Similar: [[benigno/10-optimal-policy]] §10.1

Q: Na função perda, o peso sobre a estabilidade de preços é $\theta/\kappa$. Mais rigidez de preços implica o quê?
- Menos peso sobre preços, porque com poucos ajustando o nível de preços quase não se move.
- Peso inalterado, porque $\theta$ e $\kappa$ se movem na mesma direção e se cancelam.
- Menos peso sobre preços, porque a política monetária perde tração sobre o nível de preços.
- Mais peso sobre preços, porque uma surpresa gera maior dispersão entre firmas idênticas.
<!-- YW5zOjM= -->
> $\alpha$ maior significa $\kappa$ menor e portanto $\theta/\kappa$ maior. Com poucas firmas ajustando, uma dada surpresa de preços implica **grande dispersão** de preços relativos entre firmas idênticas, e é a dispersão que destrói bem-estar. O artigo diz exatamente isso na p. 522.
> Ref: Benigno (2015), §11, p. 522
> Similar: [[benigno/10-optimal-policy]] §10.1

Q: Por que Benigno prefere uma regra de **meta** a uma regra de **instrumento** do tipo Taylor?
- Porque os coeficientes ótimos de uma regra de instrumento dependem do processo de choques.
- Porque a regra de instrumento é impossível de implementar com dados em tempo real.
- Porque a regra de meta dispensa qualquer hipótese sobre as preferências do banco central.
- Porque a regra de instrumento viola a condição de transversalidade do problema da família.
<!-- YW5zOjA= -->
> A objeção do artigo não é que não se possa fazer: é que "seria fortuito se essa política fosse ótima em todas as circunstâncias". Reotimizar os coeficientes a cada processo de choque significa que já não há regra. A regra de meta $(y-y_e)+\theta(p-p^e)=0$ sequer menciona o choque.
> Ref: Benigno (2015), §11, eq. (34), p. 522
> Similar: [[benigno/10-optimal-policy]] §10.2

Q: A política ótima deixa passar para os preços que fração de um choque de mark-up?
- A fração $\theta\kappa/(1+\theta\kappa)$, que na calibração do artigo é cerca de nove décimos.
- A fração inteira, porque a política ótima sempre prioriza o produto sobre os preços.
- A fração $1/(1+\theta\kappa)$, que na calibração do artigo é cerca de um décimo.
- Nenhuma fração, porque a regra de meta implica estabilidade estrita do nível de preços.
<!-- YW5zOjI= -->
> Com $\theta=8$ e $\kappa\simeq1{,}13$, $\theta\kappa\simeq9{,}1$, então cerca de 10% vai para preços e 90% é absorvido como perda de produto. Um banco central baseado em bem-estar fica **próximo**, mas não idêntico, a um metas-de-inflação estrito. E um banco com reta de meta mais inclinada deveria **cortar** após o mesmo choque.
> Ref: Benigno (2015), §11, Fig. 14, nota 24, pp. 522-523
> Similar: [[benigno/10-optimal-policy]] §10.4
