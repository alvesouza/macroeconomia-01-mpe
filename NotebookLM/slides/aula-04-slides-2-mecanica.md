Build a slide deck in Brazilian Portuguese from the sources below. This is deck 2 of 4 for this lecture, and its job is signed comparative statics and numbers. The model was derived in deck 1; exercises belong to deck 3 and synthesis to deck 4.

Sources. "Aula_MPE_Macro1_SlidesAula4.pdf" (= AULA4) and section 6.2 of "Livro_Pablo_Kurlat_-_A_Course_in_Modern_Macroeconomics_2020_-_libgen.li.pdf" (= KURLAT).

Scope lock. Everything must follow from AULA4 and KURLAT section 6.2. Do not import Bellman equations, dynamic programming, stochastic DSGE or RBC models, the Calvo New-Keynesian Phillips curve, or time-series econometrics.

Output language: Brazilian Portuguese (pt-BR). Keep established English terms in parentheses at first use, e.g. "efeito substituicao (substitution effect)".

THESIS THIS DECK BUILDS TOWARD. Every question the problem set asks is a derivative of the closed-form solution, and each one has a determinate sign except the response to the interest rate, whose sign is decided by the curvature parameter. Knowing which derivatives are unambiguous and which are not is the content of this lecture.

STRUCTURE. Aim for 20 to 24 slides. One derivative per slide: state it, take it, sign it, then read it back in words and mark the movement on the budget diagram. Keep the closed-form solution pinned as a header throughout.

BLOCK A - THE SOLUTION, RESTATED. Open with first-period consumption in closed form as a function of lifetime resources, the discount factor, the interest rate and the curvature parameter. Identify each piece and name the term that carries lifetime resources, since most of the derivatives that follow act through it.

BLOCK B - SECOND-PERIOD INCOME. Differentiate consumption today with respect to income tomorrow. Sign it and give the magnitude, then interpret: a household that expects to be richer later consumes more now, financing it by saving less or borrowing. Frame this as the optimism experiment and show the budget line shifting outward in parallel.

BLOCK C - INITIAL WEALTH. Differentiate with respect to initial assets. Show that wealth and future income enter through the same discounted channel, so the household does not care where its resources come from, only what they are worth today.

BLOCK D - THE DISCOUNT FACTOR. Differentiate with respect to patience. Sign it and interpret the two directions: a more patient household tilts consumption toward the future, so first-period consumption falls and saving rises. Note that this parameter is doing the work that the Keynesian function had no room for.

BLOCK E - THE INTEREST RATE, PART ONE. The longest block; at least five slides. Differentiate first-period consumption with respect to the interest rate and show the sign is not settled by algebra alone. Decompose. Substitution: a higher rate makes future consumption cheaper, so the household postpones, always pushing present consumption down. Income: for a saver, a higher rate means greater lifetime resources, pushing consumption up in both periods. Draw both, with the rotation about the endowment point and the compensated movement shown separately.

BLOCK F - THE INTEREST RATE, PART TWO. Show the curvature parameter deciding the contest. When it is small, the household is willing to move consumption between periods, substitution dominates, and saving rises with the interest rate. When it is large, the household wants a smooth path, income dominates, and saving falls when the interest rate rises. Present the result in a table with the parameter in one column and the sign of the response in the other, and mark the value at which the effects exactly cancel. State that this is the item the problem set asks for and that the expected answer is the condition, not a number.

BLOCK G - BORROWERS AGAINST SAVERS. Repeat the interest-rate experiment for a household that is borrowing rather than saving, and show that the income effect reverses sign because a higher rate makes it poorer. Put savers and borrowers side by side in one table so the asymmetry is explicit.

BLOCK H - TAXES ENTER THROUGH ONE DOOR. Add lump-sum taxes in both periods and show they appear in the solution only through their discounted sum. Compute consumption before and after a change in tax timing that leaves present value unchanged: both levels unmoved, saving absorbing the whole adjustment. Keep this arithmetic; leave interpretation to deck 4.

BLOCK I - CALIBRATION. With plausible parameters, compute the marginal propensity to consume out of a transitory income gain and out of a permanent one. Put the two figures side by side and comment on the gap.

Include one runnable Python block using numpy and matplotlib only that solves the two-period problem across a grid of interest rates for two values of the curvature parameter and plots saving against the rate, so the sign reversal is visible on one chart. Under twenty-five lines, comments in Portuguese.
