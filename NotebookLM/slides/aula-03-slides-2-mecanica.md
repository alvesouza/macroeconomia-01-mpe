Build a slide deck in Brazilian Portuguese from the sources below. This is deck 2 of 4 for this lecture, and its job is calibration and accounting. The Golden Rule, factor markets and technological progress were derived in deck 1; exercises belong to deck 3 and synthesis to deck 4.

Sources. "Aula_Handout_MPE_Macro1_Aula3_2026.pdf" (= AULA3) and chapter 5 of "Livro_Pablo_Kurlat_-_A_Course_in_Modern_Macroeconomics_2020_-_libgen.li.pdf" (= KURLAT).

Scope lock. Everything must follow from AULA3 and KURLAT chapter 5. Do not import Bellman equations, dynamic programming, stochastic DSGE or RBC models, the Calvo New-Keynesian Phillips curve, or time-series econometrics.

Output language: Brazilian Portuguese (pt-BR). Keep established English terms in parentheses at first use, e.g. "residuo de Solow (Solow residual)".

THESIS THIS DECK BUILDS TOWARD. When the model is given real numbers and asked how much of the gap between rich and poor countries capital can explain, it answers with a fraction far too small. The remainder is given a name and a symbol, and this deck is careful about what that name does and does not mean.

STRUCTURE. Aim for 20 to 24 slides. Every quantity is computed on the slide with the arithmetic visible. Every decomposition appears as a table with one column per term.

BLOCK A - PUTTING NUMBERS ON THE PARAMETERS. Assemble the calibration: capital share from factor income data, a depreciation rate, a population growth rate, and observed investment rates for a rich and a poor country. Give the source and plausible range for each, so the student sees which numbers are solid and which are conventions.

BLOCK B - THE MODEL'S PREDICTION. Use the closed-form steady state to compute the ratio of output per worker between the two countries implied by their investment rates alone. Show the computation. Then place the observed ratio beside it in the same table. The predicted gap is small and the observed gap is large, and the slide should let that contrast stand without commentary before the next block explains it.

BLOCK C - THE RETURNS PUZZLE. Treat the failure as a test, not a nuisance. If the whole gap were capital scarcity, compute the marginal product of capital the model implies for the poor country and show that number. Then state the implication: capital should flood there, and it does not. Name the puzzle and give one paragraph on candidate explanations, without settling it.

BLOCK D - GROWTH ACCOUNTING, DERIVED. Start from the production function, take logarithms, differentiate with respect to time, and obtain the decomposition of output growth into a capital term weighted by the capital share, a labour term weighted by the labour share, and a residual. Present the final equation with the exact numbering KURLAT uses, so the student can cite it in an exam answer. Then work a full numerical example in a table with one column per term and a row per period.

BLOCK E - WHAT THE RESIDUAL IS. Give this a full slide because it is the conceptual core. The residual is defined by subtraction, so it contains everything that is not measured factor accumulation: genuine technological change, the efficiency with which resources are allocated across firms, institutional quality, unmeasured inputs such as human capital or capital utilisation, and measurement error in the inputs themselves. Present that list as a table with a column stating how each item would show up.

BLOCK F - DEVELOPMENT ACCOUNTING. Distinguish it from growth accounting explicitly and early, since the two are routinely confused. Growth accounting decomposes change over time within one country; development accounting decomposes differences in levels across countries at a point in time. Set up the second decomposition, compute it for a pair of countries, and give the standard finding for what fraction of cross-country income variation is attributed to productivity rather than to factors.

BLOCK G - MEASURING THE CAPITAL STOCK. Work through how capital is actually estimated, since the residual inherits every error made here: guess an initial stock, measure investment, iterate the accumulation identity. Show numerically how fast an incorrect initial guess decays. This is the mechanism behind one of the chapter's exercises, and it shows that the inputs to the residual are themselves constructed.

BLOCK H - SOURCES OF PRODUCTIVITY DIFFERENCES. Present the candidates from KURLAT section 5.5 and, for each, state what evidence bears on it: human capital quality, misallocation of resources across firms, barriers to adopting existing technology, and institutions. Rank them by how much of the gap each is estimated to carry, and flag that the estimates are contested.

Include one runnable Python block using numpy and pandas only that takes series of output, capital and labour, performs the growth accounting decomposition, and returns each contribution and the residual as a dataframe. Under twenty-five lines, with comments in Portuguese.
