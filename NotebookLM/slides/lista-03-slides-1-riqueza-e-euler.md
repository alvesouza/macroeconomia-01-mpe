Build a slide deck in Brazilian Portuguese from the sources below. This is deck 1 of 6 in a set organised by economic mechanism rather than by lecture, and it covers the machinery that the other five all reuse: how two period-by-period constraints collapse into one, and what the first-order condition pins down. The comparative statics belong to decks 2, 3 and 4; the two market frictions belong to decks 5 and 6.

Sources. Section 6.2 and exercise 6.1 of "Livro_Pablo_Kurlat_-_A_Course_in_Modern_Macroeconomics_2020_-_libgen.li.pdf" (= KURLAT), question 1 of "Lista_MPE_Macro1_2026_Lista3.pdf" (= LISTA3), and "Aula_MPE_Macro1_SlidesAula4.pdf" (= AULA4).

Scope lock. Everything must follow from KURLAT chapter 6 and AULA4. Do not import Bellman equations, dynamic programming, stochastic DSGE or RBC models, the Calvo New-Keynesian Phillips curve, or time-series econometrics.

Output language: Brazilian Portuguese (pt-BR). Keep established English terms in parentheses at first use, for example "restricao orcamentaria intertemporal (intertemporal budget constraint)".

THESIS THIS DECK BUILDS TOWARD. The whole problem set is one object differentiated five times. Build that object correctly and every later item is a derivative; build it wrong and no later item can be recovered. Two things carry the entire construction: the present-value budget constraint, which says where resources come from, and the Euler equation, which says how they are split.

STRUCTURE. Aim for 22 to 26 slides. Derive on the board rather than announcing results: each algebraic step gets its own slide, with the line before it visible at the top. Pin the final closed form as a running header from the moment it appears.

BLOCK A - THE PRIMITIVES. State the problem exactly as LISTA3 question 1 poses it: preferences additively separable across two periods with a discount factor strictly between zero and one, two flow constraints, initial wealth, taxes in both periods, and a single real rate at which the household may borrow or lend freely. One slide per object, saying what each one is and what sign it can take.

BLOCK B - COLLAPSING THE CONSTRAINTS. Show that the asset variable appears in both flow constraints, isolate it in the second, substitute into the first, and watch it disappear. Present the resulting constraint and name it. Two readings on separate slides: the price of future consumption is the inverse of the gross rate, and income enters only in present value, never period by period.

BLOCK C - WHERE EACH TERM SITS. Build the lifetime-resources term piece by piece: initial wealth, first-period income net of tax, and second-period income net of tax discounted once. State that taxes and initial wealth are additive here, and flag that this additivity is what decks 4 and 5 will exploit and then break.

BLOCK D - THE FIRST-ORDER CONDITION. Set up the Lagrangian, take both derivatives, eliminate the multiplier, and display the Euler equation. Give the marginal reading in words: the utility given up by saving one more unit today equals the discounted utility gained tomorrow. Show that concavity of utility plus convexity of the budget set makes this condition sufficient, so the interior solution is unique.

BLOCK E - PUTTING THE FUNCTIONAL FORM IN. Take marginal utility for the CRRA family, note it is the same expression in the logarithmic case, and rearrange the Euler equation into the ratio of second- to first-period consumption. Emphasise on its own slide that this ratio depends only on patience, the interest rate and curvature, and on no income or tax term whatsoever.

BLOCK F - CLOSING THE SOLUTION. Substitute the ratio back into the budget constraint, solve, and display closed forms for both consumptions and for saving. Show that the KURLAT formula in section 6.2 is this expression with wealth and taxes set to zero. Give saving as the difference between disposable resources today and consumption today, and rewrite it so that the term multiplying future income is visible, since deck 5 will read its sign.

BLOCK G - TWO SANITY CHECKS. Slide one: set curvature to one and recover the logarithmic solution, noting that consumption then stops depending on the interest rate given lifetime resources. Slide two: set the product of the discount factor and the gross rate to one and show that consumption is perfectly flat, for any curvature.

BLOCK H - A CALIBRATION THAT CLOSES IN ROUND NUMBERS. Choose a discount factor of 0,96, a rate of 0,50 and curvature of 2, so the denominator term equals 0,8 and the consumption ratio equals 1,2 exactly. Tabulate lifetime resources, both consumptions and saving, and verify the second-period flow constraint on screen.

Include one runnable Python block using numpy only that computes the closed form, then confirms it against a direct numerical maximisation over the asset choice and prints the Euler residual. Under twenty-five lines, comments in Portuguese.
