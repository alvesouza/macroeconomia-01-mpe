Build a slide deck in Brazilian Portuguese from the sources below. This is deck 4 of 6 in a set organised by economic mechanism rather than by lecture, and its mechanism is lump-sum taxation as a pure wealth effect, carried through to the equivalence result. Decks 5 and 6 dismantle the two assumptions this deck relies on.

Sources. Section 6.2 and exercise 6.1 of "Livro_Pablo_Kurlat_-_A_Course_in_Modern_Macroeconomics_2020_-_libgen.li.pdf" (= KURLAT), with attention to the caveat page in that section, question 1 items d and e of "Lista_MPE_Macro1_2026_Lista3.pdf" (= LISTA3), and "Aula_MPE_Macro1_SlidesAula4.pdf" (= AULA4).

Scope lock. Everything must follow from KURLAT chapter 6 and AULA4. Do not import Bellman equations, dynamic programming, stochastic DSGE or RBC models, the Calvo New-Keynesian Phillips curve, or time-series econometrics.

Output language: Brazilian Portuguese (pt-BR). Keep established English terms in parentheses at first use, for example "equivalencia ricardiana (Ricardian equivalence)".

THESIS THIS DECK BUILDS TOWARD. A lump-sum tax has exactly one job in this model: it moves lifetime resources. It touches no price, so it distorts no margin, and the consumption ratio is invariant to it. Push that observation one step and the timing of taxes stops mattering altogether, with private saving absorbing the entire adjustment.

STRUCTURE. Aim for 22 to 26 slides. Keep the closed form pinned as a header. Every derivative gets its sign stated, then read back in words, then marked on the budget diagram.

BLOCK A - THE OBSERVATION THAT SAVES MOST OF THE WORK. Before differentiating anything, show that both taxes appear in the solution only inside lifetime resources, and that the consumption ratio contains no tax term. Conclude on that slide alone that a lump-sum tax must shift the budget line inward in parallel, without rotating it.

BLOCK B - SIX DERIVATIVES IN ONE TABLE. Build a table with three rows for present consumption, future consumption and saving, and two columns for a tax today and a tax tomorrow. Fill each cell, then devote one slide per row to reading it back.

BLOCK C - CONSUMPTION FALLS, BUT NOT ONE FOR ONE. Show that a tax of one unit today reduces present consumption by the marginal propensity to consume, which is strictly below one. State the mechanism: the household smooths, and the instrument it smooths with is saving.

BLOCK D - THE SIGN THAT REVERSES. Give the effect of a future tax on saving and show it is positive. Explain that the household saves today in order to pay tomorrow, while still consuming less today because it is poorer. Put this beside the effect of a present tax on saving, which is negative, and note that this is the only sign in the table that flips.

BLOCK E - THE RATIO BETWEEN THE TWO TAXES. Show that the response to a tax today is exactly the gross rate times the response to a tax tomorrow, and state why: in present value the tax today simply is larger by that factor.

BLOCK F - ONLY PRESENT VALUE ENTERS. Rewrite lifetime resources splitting off the discounted sum of the two taxes, and show both consumptions depend on that sum alone. Emphasise on its own slide that this argument never uses the CRRA form and holds for any concave utility, because taxes reach the problem only through the budget constraint.

BLOCK G - THE EXPERIMENT. Cut the present tax by one unit and raise the future tax by the gross rate. Verify on screen that the present value of taxes is unchanged, then report the three results: both consumptions unmoved, saving up by exactly one. Verify the result a second way through the second-period flow constraint, so the arithmetic closes twice.

BLOCK H - WHAT MOVES AND WHAT DOES NOT. Diagram slide: the budget line stays fixed while the endowment point slides along it, and the tangency does not move. Show that the distance between endowment and tangency, which is saving, is the only thing that changed. Add the national-accounting reading: public saving down one, private saving up one, national saving unchanged.

BLOCK I - THE FOUR ASSUMPTIONS. A table listing lump-sum taxes, absence of credit constraints, a common interest rate for government and household, and the taxpayer being alive to pay. Against each, name what breaks it. Mark the first two as decks 5 and 6.

BLOCK J - WHAT THE RESULT DOES NOT SAY. Following the caveat in KURLAT section 6.2, state the misreading explicitly and correct it: the level and composition of government spending still matter, and so does the type of tax. The claim is only about the timing of lump-sum taxes at constant present value.

Include one runnable Python block using numpy only that computes both consumptions and saving before and after the tax swap for several curvature values and prints the differences, showing zeros in the consumption columns and one in the saving column. Under twenty-five lines, comments in Portuguese.
