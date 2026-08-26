Build a slide deck in Brazilian Portuguese from the sources below. This is deck 2 of 6 in a set organised by economic mechanism rather than by lecture, and its mechanism is the propensity to consume out of future income. Deck 1 built the closed form; the interest-rate contest is deck 3, taxes are deck 4, and the two frictions are decks 5 and 6.

Sources. Sections 6.1 and 6.2 and exercises 6.1 and 6.4 of "Livro_Pablo_Kurlat_-_A_Course_in_Modern_Macroeconomics_2020_-_libgen.li.pdf" (= KURLAT), question 1 item b of "Lista_MPE_Macro1_2026_Lista3.pdf" (= LISTA3), and "Aula_MPE_Macro1_SlidesAula4.pdf" (= AULA4).

Scope lock. Everything must follow from KURLAT chapter 6 and AULA4. Do not import Bellman equations, dynamic programming, stochastic DSGE or RBC models, the Calvo New-Keynesian Phillips curve, or time-series econometrics.

Output language: Brazilian Portuguese (pt-BR). Keep established English terms in parentheses at first use, for example "hipotese da renda permanente (permanent income hypothesis)".

THESIS THIS DECK BUILDS TOWARD. The model's sharpest empirical claim is that news about tomorrow moves spending today, with no change in today's income, today's wealth or the interest rate. That single derivative separates this theory from the Keynesian consumption function, and it is testable.

STRUCTURE. Aim for 20 to 24 slides. Keep the closed form for first-period consumption pinned as a header. Every claim gets both an algebraic slide and a diagram slide, and the diagrams reuse the plane built in deck 1.

BLOCK A - THE RIVAL HYPOTHESIS FIRST. Present the Keynesian function from KURLAT section 6.1: consumption as an intercept plus a fraction of current income. State plainly what it predicts when only expected future income changes, which is nothing, and put that prediction on a slide by itself so the contrast later is unmistakable.

BLOCK B - THE DERIVATIVE. Differentiate first-period consumption with respect to second-period income. Show that future income enters only inside the lifetime-resources term and only after discounting, so the derivative is the marginal propensity to consume out of wealth divided by the gross rate. Sign it and bound it strictly between zero and one.

BLOCK C - THE COMPARISON THAT MATTERS. On its own slide, put the derivative with respect to current income beside the derivative with respect to future income, and form their ratio. Show that the ratio is exactly the discount factor on one period, so the two differ by nothing except timing. State the consequence: there is no intrinsic preference for current income in this model, only for present value.

BLOCK D - LINEARITY. Show that under CRRA preferences the consumption function is linear in lifetime resources, so both propensities are constants that do not depend on the level of income. Name the source, homotheticity, and note that decks 5 and 6 break it.

BLOCK E - AND SAVING. Differentiate the asset position with respect to future income and show it is the negative of the consumption derivative. State the result in words: a household that expects to be richer later saves less now, or borrows. Put the two derivatives side by side in a table so the offset is visible.

BLOCK F - OPTIMISM, DEFINED. Translate the LISTA3 phrase about households suddenly becoming optimistic into the only object in the model that can carry it, which is an upward revision of second-period income. Show the budget line shifting outward in parallel and the tangency sliding up the ray from the origin, so both consumptions rise and the endowment point moves without the slope changing.

BLOCK G - TRANSITORY AGAINST PERMANENT. Compute the response of consumption and of saving to a one-period income gain and to a gain in both periods of equal size. Tabulate both, and show that saving absorbs almost the whole transitory gain while the permanent gain passes into consumption nearly one for one. Name this the central testable prediction of the chapter.

BLOCK H - WHAT THE DATA WOULD LOOK LIKE. Following KURLAT exercise 6.4, sketch two households with different income profiles and show that a cross-section of first-period data alone would look Keynesian even though neither household is Keynesian. State the identification lesson: current income and lifetime resources are correlated, so the coefficient on current income is not the propensity it appears to be.

BLOCK I - CALIBRATION. With a discount factor of 0,96, a rate of 0,50 and curvature of 2, compute both propensities and the ratio between them, and show the effect on consumption and saving of a revision of future income of ten units.

Include one runnable Python block using numpy and matplotlib only that plots first-period consumption against future income for two curvature values, marking both slopes on the chart. Under twenty-five lines, comments in Portuguese.
