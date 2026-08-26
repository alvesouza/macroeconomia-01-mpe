Build a slide deck in Brazilian Portuguese from the sources below. This is deck 3 of 6 in a set organised by economic mechanism rather than by lecture, and its mechanism is the contest between income and substitution effects when the interest rate moves. Deck 1 built the closed form, deck 2 handled future income, deck 4 handles taxes, decks 5 and 6 the frictions.

Sources. Section 6.2 and exercises 6.1 and 6.3 of "Livro_Pablo_Kurlat_-_A_Course_in_Modern_Macroeconomics_2020_-_libgen.li.pdf" (= KURLAT), question 1 item c of "Lista_MPE_Macro1_2026_Lista3.pdf" (= LISTA3), and "Aula_MPE_Macro1_SlidesAula4.pdf" (= AULA4).

Scope lock. Everything must follow from KURLAT chapter 6 and AULA4. Do not import Bellman equations, dynamic programming, stochastic DSGE or RBC models, the Calvo New-Keynesian Phillips curve, or time-series econometrics.

Output language: Brazilian Portuguese (pt-BR). Keep established English terms in parentheses at first use, for example "elasticidade de substituicao intertemporal (elasticity of intertemporal substitution)".

THESIS THIS DECK BUILDS TOWARD. Whether a higher interest rate raises or lowers consumption today is not a fact the model reports; it is a contest that one parameter settles. A student who memorises a direction gets this item wrong. A student who can name the parameter gets every version of it right.

STRUCTURE. Aim for 22 to 26 slides, with the interest-rate derivative pinned as a header once it appears. Each of the two effects gets its own diagram slide before they are combined.

BLOCK A - WHY THE PROBLEM SET ZEROES OUT FUTURE INCOME. State the simplification LISTA3 imposes, with future income and both taxes set to zero. Show that lifetime resources then reduce to initial wealth plus current income, and that their derivative with respect to the interest rate is exactly zero. Put on a slide the reason this matters: the channel by which a higher rate devalues future income is switched off, leaving only the contest over the intertemporal price.

BLOCK B - THE ALGEBRA. Isolate the only term where the rate appears, differentiate it, and assemble the derivative of first-period consumption by the quotient rule. Display the result and factor it so the curvature term stands alone.

BLOCK C - THE SIGN, ISOLATED. On one slide, argue that consumption, the denominator term and the gross rate are all strictly positive, so the sign of the whole expression is the sign of the curvature parameter minus one. Nothing else in the expression can change it.

BLOCK D - THE ELASTICITY FORM. Rewrite the same result as an elasticity with respect to the gross rate, and show it factors into one minus the elasticity of intertemporal substitution, multiplied by the share of lifetime resources allocated to the future.

BLOCK E - THE THREE REGIMES. A table with the curvature parameter in the first column, the elasticity of substitution in the second, the sign of the response in the third, and the winning effect in the fourth. Fill in the case below one, the case at one and the case above one, and give the logarithmic case its own slide as the exact tie, where consumption becomes independent of the rate given lifetime resources.

BLOCK F - THE TWO EFFECTS, DRAWN. Two diagram slides. First, the substitution effect: a compensated line parallel to the new one and tangent to the original indifference curve, with the optimum sliding away from present consumption. Second, the income effect: the move from the compensated line to the actual one, which for a saver expands the feasible set. Then a third slide combining both arrows on one diagram with the net movement as their sum.

BLOCK G - WHY THIS HOUSEHOLD IS NECESSARILY A SAVER. Show that with zero future income the asset position must be positive, so the household is a net creditor and a higher rate is good news for it. State that this fixes the direction of the income effect, and that a borrower would have the opposite one, which is why KURLAT insists on distinguishing the two cases.

BLOCK H - CURVATURE AND THE SHAPE OF THE INDIFFERENCE CURVE. Two panels with the same budget rotation and different curvature, showing that sharply bent curves resist tilting the consumption path, so the substitution movement is short. Connect this to why high curvature means low willingness to substitute.

BLOCK I - CALIBRATION AND THE EMPIRICAL AFTERWORD. With a discount factor of 0,96, a rate of 0,50 and initial resources of 110, tabulate the derivative for curvature values of 0,5, 1 and 2. Close by noting that estimated elasticities of substitution cluster near the tie, which is one reason macro models often adopt the logarithmic case.

Include one runnable Python block using numpy and matplotlib only that plots saving against the interest rate for two curvature values on one chart, so the sign reversal is visible. Under twenty-five lines, comments in Portuguese.
