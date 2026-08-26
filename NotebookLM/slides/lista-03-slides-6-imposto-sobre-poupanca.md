Build a slide deck in Brazilian Portuguese from the sources below. This is deck 6 of 6 in a set organised by economic mechanism rather than by lecture, and its mechanism is the wedge a tax on the return to saving opens between the private and the social rate of return. Deck 4 established that lump-sum taxes distort nothing and deck 5 removed the credit-market assumption; this deck removes the last one.

Sources. Section 6.2 and exercise 6.6 of "Livro_Pablo_Kurlat_-_A_Course_in_Modern_Macroeconomics_2020_-_libgen.li.pdf" (= KURLAT), question 2 item d of "Lista_MPE_Macro1_2026_Lista3.pdf" (= LISTA3), and "Aula_MPE_Macro1_SlidesAula4.pdf" (= AULA4).

Scope lock. Everything must follow from KURLAT chapter 6 and AULA4. Do not import Bellman equations, dynamic programming, stochastic DSGE or RBC models, the Calvo New-Keynesian Phillips curve, or time-series econometrics. One household, two periods.

Output language: Brazilian Portuguese (pt-BR). Keep established English terms in parentheses at first use, for example "peso morto (deadweight loss)".

THESIS THIS DECK BUILDS TOWARD. Two taxes that raise identical revenue are not equivalent. One shifts the budget line; the other rotates it. Only the second changes the consumption ratio, and only the second leaves the household worse off than it needed to be. Taxes that fall on margins of choice create deadweight loss; taxes on fixed amounts do not.

STRUCTURE. Aim for 22 to 26 slides. Carry three regimes side by side throughout - no tax, lump-sum, tax on returns - in a comparison table updated as each result lands.

BLOCK A - WHAT IS BEING TAXED. State the modified second-period constraint and define the after-tax gross return. Writing the rate as a fraction of interest earned recovers the KURLAT formulation of a tax on interest income, so the two are the same object. The exercise concerns a saver; the asymmetric case is BLOCK J.

BLOCK B - THE NEW FIRST-ORDER CONDITION. Redo the optimisation with the after-tax return in place of the gross rate and display the resulting consumption ratio beside the untaxed one.

BLOCK C - THE PROOF, IN TWO HALVES. First half: from deck 4, lump-sum taxes enter only through lifetime resources and the ratio has no tax term, so its derivative is zero. Second half: the after-tax return is strictly below the gross rate and the mapping is strictly increasing, so the ratio falls. Emphasise that this holds for every positive curvature value, with no exception.

BLOCK D - THE TWO GEOMETRIES. Two diagram slides. The lump-sum tax shifts the line inward with the slope unchanged, so the tangency slides down a fixed ray. The tax on returns rotates the line about the endowment, since a household that neither lends nor borrows pays nothing. Then a slide with both together.

BLOCK E - FIXING THE COMPARISON. Define revenue under the tax on returns as the rate times the saving actually chosen and set the lump-sum amount equal to it. A comparison at unequal revenue proves nothing.

BLOCK F - THE DOMINANCE ARGUMENT. Price the plan chosen under the tax on returns at the market gross rate and show algebraically that it lands exactly on the lump-sum budget line. Conclude on a slide of its own: that plan was affordable under the lump-sum regime and was not chosen, so the lump-sum optimum is strictly better at identical revenue, and the welfare ranking is settled without computing anything.

BLOCK G - THE MARGIN, NAMED. Compare the marginal rate of substitution at each optimum with the rate at which the economy actually transforms present into future consumption. The lump-sum regime leaves them equal; the tax on returns opens a wedge equal to the tax rate. Name the distorted margin as the intertemporal one; the lump-sum tax distorts none.

BLOCK H - MEASURING THE LOSS. Find the lump-sum amount leaving the household exactly as well off as the tax on returns, and report the excess over actual revenue as the deadweight loss, in level and as a share. Use a discount factor of 0,96, a rate of 0,50, curvature of 2 and a tax rate of 0,20.

BLOCK I - THE CLAIM THAT DOES NOT HOLD. Tabulate saving under both regimes for several curvature values, including one where saving rises rather than falls. Explain the two opposing channels and state why the problem set asks about the ratio instead: the ratio is what the Euler equation fixes unambiguously.

BLOCK J - THE KINK, AND WHY LUMP-SUM TAXES ARE RARE. Under the KURLAT version where borrowers pay nothing, the line has two slopes meeting at the endowment, so a household near zero saving may not react. Close with why governments avoid lump-sum taxes: they are regressive by construction, and conditioning on ability to pay creates the very margin that generates the loss.

Include one runnable Python block using numpy only that computes both regimes at equal revenue, prints both consumption ratios and verifies that the distorted plan lies on the lump-sum line. Under twenty-five lines, comments in Portuguese.
