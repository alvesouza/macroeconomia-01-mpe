Build a slide deck in Brazilian Portuguese from the sources below. This is deck 2 of 4 for this lecture, and its job is the mechanics of the model and the numbers. The historical argument and the Kaldor facts were covered in deck 1; exercises belong to deck 3 and synthesis to deck 4.

Sources. "Aula_MPE_Macro1_SlidesAula2.pdf" (= AULA2) and sections 4.1 and 4.2 of "Livro_Pablo_Kurlat_-_A_Course_in_Modern_Macroeconomics_2020_-_libgen.li.pdf" (= KURLAT).

Scope lock. Everything must follow from AULA2 and KURLAT sections 4.1 and 4.2. The Golden Rule, factor markets and technological progress belong to the next lecture and must not appear. Do not import Bellman equations, dynamic programming, stochastic DSGE or RBC models, the Calvo New-Keynesian Phillips curve, or time-series econometrics.

Output language: Brazilian Portuguese (pt-BR). Keep established English terms in parentheses at first use, e.g. "estado estacionario (steady state)".

THESIS THIS DECK BUILDS TOWARD. The model has exactly one moving part, the capital stock per worker, and everything else is a consequence. Once its law of motion is written, the steady state, the stability, and the sharp distinction between a level effect and a growth effect all follow without further assumptions.

STRUCTURE. Aim for 20 to 24 slides. Every result is derived on the slide, then signed, then read back in words. Every diagram is drawn before it is used.

BLOCK A - REDUCING TO PER-WORKER TERMS. Use constant returns to scale to write output per worker as a function of capital per worker alone, showing the division step rather than quoting the result. Then plot it and mark what the Inada conditions impose at each end: infinite slope at the origin, slope going to zero as capital grows without bound.

BLOCK B - THE LAW OF MOTION. Derive the equation of motion for capital per worker step by step. Begin with the aggregate accumulation identity, substitute the saving rule, divide by the labour force, and handle the population growth term carefully, since this is where algebra errors concentrate. Present the final expression in the exact form AULA2 uses. Then read it back in words: capital per worker rises when investment per worker exceeds what is needed to replace depreciation and equip new workers.

BLOCK C - THE DIAGRAM. Draw the standard picture with capital per worker on the horizontal axis, the saving curve rising and flattening, and effective depreciation as a straight line through the origin. Explain the shape of each curve from the assumptions in block A rather than from familiarity. Mark the intersection and define the steady state as the capital stock at which the two are equal.

BLOCK D - EXISTENCE, UNIQUENESS, STABILITY. Prove each rather than reading them off the picture. Existence and uniqueness follow from the Inada conditions and the curvature of the production function: one curve starts above the other and ends below it, crossing once. Stability follows from the sign of the gap on either side. Draw arrows showing motion from below and above the steady state, with the corresponding time paths.

BLOCK E - SOLVING WITH COBB-DOUGLAS. Specialise the production function and solve for steady-state capital per worker in closed form as a function of the saving rate, depreciation, population growth and the exponent. Then obtain steady-state output per worker. Keep this closed form visible for the rest of the deck, since it is the expression every exercise uses.

BLOCK F - COMPARATIVE STATICS, ONE PARAMETER AT A TIME. Take the derivative of steady-state output per worker with respect to the saving rate, then population growth, then depreciation. For each, give the sign, show the shift on the diagram, and state the economics in one sentence. Give population growth extra room: it moves the effective depreciation line, not the saving curve, and students frequently shift the wrong one.

BLOCK G - LEVEL AGAINST RATE. The most tested distinction in the chapter; give it at least four slides. Raise the saving rate permanently and show the new steady state: higher output per worker, long-run growth still zero. Plot the transition in two panels, level and growth rate, so the growth rate visibly jumps, decays and returns to zero. State the conclusion as a boxed result: raising saving buys a permanently higher level and only a temporary period of faster growth.

BLOCK H - CALIBRATION. Put plausible values on the parameters, compute the implied steady state, and compute how long the economy takes to close a stated fraction of the gap. Present the half-life as one figure and compare it with a human career.

Include one runnable Python block using numpy and matplotlib only that iterates the law of motion from an arbitrary initial capital stock, plots capital per worker and the growth rate of output per worker against time, and marks the steady state. Under twenty-five lines, with comments in Portuguese.
