Build a slide deck in English from the sources below. This is deck 1 of 6 in a set organised by economic mechanism rather than by question. Its mechanism is the accounting that closes the model: constant returns, competitive pricing, and the definition of equilibrium that first-order conditions alone do not give. Decks 2 and 3 work the labour margin, decks 4 to 6 the capital margin.

Sources. Section 9.1 of "Livro_Kurlat_Cap09_General_Equilibrium.pdf" (= KURLAT9), question 1 items a to c of "Lista_MPE_Macro1_2026_Lista5.pdf" (= LISTA5), and "Aula_Slides_Macro1_Aula6.pdf" (= AULA6).

Scope lock. Everything follows from KURLAT9 and AULA6. Chapter 8 of Kurlat is outside this course. No Bellman equations, dynamic programming, stochastic DSGE or RBC models, Calvo New-Keynesian Phillips curve, or time-series econometrics.

Output language: English throughout, whatever language the sources are in. Notation: r for the interest rate, r superscript K for the rental rate of capital.

THESIS. LISTA5 question 1 is chapter 9 with capital frozen, and the freeze removes three lines a student who knows the book too well will write anyway. What survives is a model where zero profit is an identity rather than a condition, and where "define the equilibrium" means three blocks, not one.

STRUCTURE. Aim for 22 to 26 slides. Carry a running box listing what this economy has that Kurlat's has, and what it does not.

BLOCK A - THE AMPUTATION. Three removals relative to section 9.1, one slide each. No investment firm, so the third agent does not exist and equation 9.1.11 has no analogue. No capital accumulation, so equation 9.1.5 becomes the line that capital equals K bar in both periods, depreciation zero. No storage, so goods clearing carries no investment term, and mark that third one as what every later result descends from.

BLOCK B - THE HOUSEHOLD. Write the objective with the forms LISTA5 specifies, power utility in consumption and logarithmic utility in leisure, then the present-value budget constraint with all four wealth terms. Give a full slide to the contrast with equation 9.1.1: Kurlat's household holds the bracket one plus the rental rate minus depreciation, which includes the principal because capital can be sold into a used-capital market. Here it can only be rented, so the terms are rentals in both periods and no depreciation term appears. Show both constraints side by side, differing term highlighted.

BLOCK C - THE FIRM, STATIC BY CONSTRUCTION. Write the period-by-period problem and explain why it has no discount factor: it rents everything and carries nothing between dates. That licenses two one-period problems instead of one two-period problem.

BLOCK D - ZERO PROFIT AS AN IDENTITY. Three labelled steps. Homogeneity of degree one from exponents summing to one; Euler's theorem for homogeneous functions; direct verification for Cobb-Douglas, the marginal product of capital being alpha times output over capital and that of labour one minus alpha times output over labour. Impose the firm's conditions and show factor payments exhaust revenue. Close with two claims: this is an identity from constant returns plus competitive pricing, not an imposed condition, and it is scale that delivers it rather than alpha. Add a slide showing profit dropping out of the budget constraint, leaving wealth as labour income plus rental income.

BLOCK E - THE FOUR FIRST-ORDER CONDITIONS. Attach a multiplier, write one condition per choice variable, take two ratios, show the multiplier cancelling twice. Present the survivors as a two-column table: the intratemporal condition, equation 9.1.7, and the Euler equation, 9.1.8, each in general and explicit form. Name which margin each describes, since LISTA5 asks for that identification. Close the block by fixing a convention on its own slide: sigma is the curvature of utility and the coefficient of relative risk aversion, one over sigma the elasticity of intertemporal substitution, and deck 3 turns on it.

BLOCK F - THE DEFINITION OF COMPETITIVE EQUILIBRIUM. Three numbered blocks: household optimality, firm optimality, market clearing. List the allocation and the price system as two explicit sets, and write the three clearing conditions for goods, labour and capital in each period.

BLOCK G - THE THREE WAYS TO LOSE THE MARKS. Writing only first-order conditions, which gives demand and not equilibrium. Writing an investment term in goods clearing. Omitting the credit market, where net lending is zero, which follows by Walras's law and must hold anyway because the representative agent cannot trade with itself.

Include one runnable Python block using numpy, under twenty-five lines, comments in English. Verify Euler's theorem numerically for Cobb-Douglas, confirm factor payments exhaust output at the firm's optimum for several parameter draws, and print the residual profit to show it is zero to machine precision.
