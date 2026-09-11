Build a slide deck in English from the sources below. Deck 5 of 6, in a set organised by mechanism rather than by question. Its mechanism is arbitrage: the condition forcing two simultaneously held assets to offer the same return, so stripping one of the three agents of any influence.

Sources. Section 9.3 of "Livro_Kurlat_Cap09_General_Equilibrium.pdf" (= KURLAT9), especially equation 9.3.3, question 2 items b and c of "Lista_MPE_Macro1_2026_Lista5.pdf" (= LISTA5), and "Aula_Slides_Macro1_Aula6.pdf" (= AULA6).

Scope lock. Everything follows from KURLAT9 and AULA6; the investment firm is the frictionless one of section 9.3, and chapter 8 of Kurlat is outside this course. No Bellman equations, dynamic programming, stochastic DSGE or RBC models, Calvo Phillips curve, or time-series econometrics.

Output language: English throughout, whatever language the sources are in. Notation: r for the interest rate, r superscript K for the rental rate.

THESIS. The investment firm's first-order condition looks like it should determine investment and does not. Its problem is linear, so it has no interior optimum; the condition pins down a price, and the quantity comes from market clearing instead. Once that is seen, the irrelevance of ownership is an accounting consequence rather than a surprise.

STRUCTURE. Aim for 22 to 26 slides. Build both ownership arrangements in parallel columns, so the two derivations reach the same boxed line at the same height.

BLOCK A - THE PRODUCTIVE FIRM FIRST. Write the static problem with labour fixed at one and derive the wage as one minus alpha times productivity times capital to the power alpha, and the rental rate as alpha times productivity times capital to the power alpha minus one. One slide on the economics: the wage rises in capital and the rental rate falls in it, both by diminishing returns. Add that profits are zero by deck 1's constant-returns argument.

BLOCK B - ARRANGEMENT ONE, THE HOUSEHOLD OWNS THE CAPITAL. Write the period budget constraint with investment in it and the capital accumulation equation, substitute investment out, and collect the capital terms. Highlight the resulting bracket, the rental rate plus one minus depreciation, and name it the gross return on capital.

BLOCK C - THE INTERTEMPORAL CONDITION FOR CAPITAL. Maximise the discounted sum subject to that constraint and take the first-order condition for next period's capital. Present it beside the bond Euler equation and derive the no-arbitrage condition by comparison, saying why that is legitimate: both assets are held in equilibrium, so different returns would have the household short one and take an unbounded position in the other.

BLOCK D - ARRANGEMENT TWO, THE INVESTMENT FIRM. Write the profit function exactly as equation 9.3.3 has it, discounted rental revenue minus the cost of the goods used to build the capital. Differentiate with respect to investment and stop on the result for a full slide: it is a constant, independent of investment.

BLOCK E - THE THREE CASES. A three-row table: the ratio above one, giving unbounded investment and infinite profit; below one, unbounded disinvestment; exactly one, indifference across every level and profit of exactly zero. Mark the third as the only row consistent with equilibrium, and read off the condition derived in block C.

BLOCK F - THE SUBTLETY MOST ANSWERS MISS. The condition determines a price, not a quantity, so the level of investment is set by goods clearing, which is deck 6. Say explicitly that searching for the investment firm's optimal investment is searching for something that does not exist, and that this is linearity rather than an oversight.

BLOCK G - THREE REASONS OWNERSHIP IS IRRELEVANT. One slide each, and insist on all three because LISTA5 asks for the explanation, not merely the algebra. Both arrangements deliver the same intertemporal price, which merely matches a technological fact. Profits are zero in both, so no surplus is transferred and the lifetime budget set is identical. And consumption possibilities depend only on the resource constraint and that price, neither of which ownership touches.

BLOCK H - WHAT IT IS CALLED, AND WHAT BREAKS IT. Name Fisher separation, from Irving Fisher's The Theory of Interest of 1930, and place Modigliani and Miller beside it. One slide on what breaks it, keeping to what the course has covered: the borrowing constraints of the earlier problem set, and any wedge between the return paid and received. Close on the claim that the investment firm is an accounting device, not an agent with independent influence.

Include one runnable Python block using numpy, under thirty lines, comments in English. Compute the investment firm's profit over a grid of investment levels, show it is identically zero when the arbitrage condition holds and strictly monotone otherwise, and verify both ownership routes return the same interest rate for several parameter draws.
