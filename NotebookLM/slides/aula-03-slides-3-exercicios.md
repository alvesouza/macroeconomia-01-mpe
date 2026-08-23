Build a slide deck in Brazilian Portuguese from the sources below. This is deck 3 of 4 for this lecture, and its job is worked exercises. Theory was covered in deck 1 and calibration in deck 2; quote their results in one line and use them.

Sources. "Livro_Pablo_Kurlat_-_A_Course_in_Modern_Macroeconomics_2020_-_libgen.li.pdf" (= KURLAT), exercise 4.3 on page 73 and exercises 5.1 to 5.9 on pages 93 to 98. Then both questions of "Lista_MPE_Macro1_2026_Lista2.pdf" (= LISTA2), with "Aula_Handout_MPE_Macro1_Aula3_2026.pdf" (= AULA3) for notation.

Scope lock. Everything must follow from KURLAT sections 4.3 to 4.5 and chapter 5. Do not import Bellman equations, dynamic programming, stochastic DSGE or RBC models, the Calvo New-Keynesian Phillips curve, or time-series econometrics.

Output language: Brazilian Portuguese (pt-BR). Keep established English terms in parentheses at first use.

THESIS THIS DECK BUILDS TOWARD. Question 1 of the problem set is textbook exercise 4.3 with numbers attached, and question 2 is an original problem built on sections 5.3 and 5.4. Together they test the one idea the lecture cares about: that the residual absorbs anything the accountant cannot separate.

STRUCTURE. Aim for 22 to 26 slides, one item per slide where possible: setup, working, boxed answer, one line naming the concept tested. In comparative-static items, draw the diagram and mark the shift before any algebra.

BLOCK A - EXERCISES 5.1 AND 5.2. Work the quantification of the model and the speed of convergence. For 5.2, derive the rate at which the gap to the steady state closes, convert it to a half-life, and say whether that horizon fits the observed persistence of income differences.

BLOCK B - EXERCISES 5.3 AND 5.4. Work 5.3 first: what growth accounting attributes to capital and to technology in a steady state with ongoing technical progress. Bring out the result that anticipates the problem set, that capital accumulation is itself driven by technology, so splitting growth between them is not identifying causes. Then work 5.4 on estimating the capital stock from an initial guess and an investment series, showing how fast the initial error decays.

BLOCK C - EXERCISES 5.5 TO 5.9, RAPIDLY. One slide each: sources of productivity, interest rates, the combined accounting exercise, national accounts and the Golden Rule, disease and productivity. Setup, key step, answer. Flag 5.7 and 5.8 as the likeliest to appear on an assessment, since each spans more than one section.

BLOCK D - EXERCISE 4.3, KOREAN UNIFICATION. This is question 1 of the problem set: work it in the assigned calibrated form, not the book's general one. Two economies share a depreciation rate but differ in capital exponent, productivity level, saving rate and population growth. Item by item: capital per worker and output per person in the initial period for each country; steady-state capital per worker as a function of the parameters, evaluated for both, with what the model predicts about growth in each; then unification, where production uses the southern technology and exponent while pooling both capital stocks and labour forces. Compute the change in output per person for each country separately and identify the source of the gain in each, which differs between the two sides. Close with the bonus item on the unified steady state and whether it lies above or below the current position.

BLOCK E - LISTA2 QUESTION 2, GOTHAM. An original problem, and the deck's most careful treatment. Setup: for every unit of productive capital, firms hold a fixed proportion in security capital, and the agency records both as capital. Four items in order. First, total output as a function of productivity, total capital, labour, the capital exponent and the security ratio, plus the fraction of measured capital held for security and the output lost. Second, the firm's problem, noting it pays the same rental rate on both kinds of capital, and the factor shares an agency would measure, answering explicitly whether crime distorts them. Third, the development accounting exercise of section 5.3 run by an analyst who cannot separate the two capital stocks: the productivity estimate obtained, how it compares with the true value, and whether the exponent is also mismeasured. Fourth, a technology cutting the security requirement, decomposed with the growth accounting equation, showing the entire effect reported as productivity growth while true productivity is unchanged, with the implied annual rate.

BLOCK F - THE PATTERN. Close with a table mapping each LISTA2 item to its textbook origin, and state the finding: the lecturer takes a book exercise, attaches numbers, and adds an original problem stressing the same idea in an unfamiliar setting.

Include one runnable Python block using numpy only that solves the two-country steady states of question 1 and the unified case, printing capital per worker and output per person for each. Under twenty-five lines, with comments in Portuguese.
