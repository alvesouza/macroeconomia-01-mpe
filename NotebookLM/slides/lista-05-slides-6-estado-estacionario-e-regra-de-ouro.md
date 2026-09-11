Build a slide deck in English from the sources below. Deck 6 of 6, organised by mechanism rather than by question. Its mechanism is the division of labour between preferences and technology at rest: impatience fixes the rate, capital moves until technology agrees.

Sources. Section 9.3, equation 9.3.17 and exercises 9.11 and 9.12 of "Livro_Kurlat_Cap09_General_Equilibrium.pdf" (= KURLAT9), question 2 items d and e of "Lista_MPE_Macro1_2026_Lista5.pdf" (= LISTA5), "Aula_Slides_Macro1_Aula6.pdf" (= AULA6).

Scope lock. Everything follows from KURLAT9 and AULA6, the phase diagram treated graphically. Chapter 8 of Kurlat is outside this course. No Bellman equations, dynamic programming, stochastic DSGE or RBC models, or Calvo curve.

Output language: English throughout, whatever the sources are in.

THESIS. The competitive economy rests holding strictly less capital than the level maximising the consumption it enjoys there, and that shortfall is not a failure. It is the exact measure of impatience, and it costs far less consumption than the capital gap suggests.

STRUCTURE. Aim for 26 to 30 slides. From block C keep one diagram per slide, capital on the horizontal axis, adding one object at a time.

BLOCK A - THE RESOURCE CONSTRAINT. Combine goods clearing at fixed labour with capital accumulation, substitute investment out, and obtain next period's capital as what survives depreciation plus output minus consumption. Give the sentence form beside the algebra, and say that with the Euler equation this is a pair of difference equations, after which all is geometry.

BLOCK B - THE STEADY STATE AND THE CLOSED FORMS. Constant consumption forces beta times one plus the rate to equal one; arbitrage gives the rate as the rental rate minus depreciation; the firm's condition gives the rental rate as the marginal product of capital; equate to obtain equation 9.3.17. Mark which substitution used preferences and which technology, then solve for the capital stock under Cobb-Douglas and for consumption as output minus replacement investment.

BLOCK C - THE PUNCHLINE. The steady-state rate is one over beta minus one and nothing else, not productivity, not alpha, not depreciation. Two moves: a constant path requires the reward for waiting to offset impatience exactly, which is purely preferences; technology then sets the quantity, capital rising until the net marginal product meets that rate. Close on the sentence that preferences determine the rate and technology the capital stock.

BLOCK D - THE PHASE DIAGRAM. One object per slide: the vertical locus for constant consumption, with a slide on why it is vertical, namely that consumption does not enter the steady-state condition at all; the concave hump for constant capital; their intersection; the four regions; the saddle path; and the state variable that cannot jump against the jump variable that must.

BLOCK E - THE NUMBERS. Table with productivity 1, alpha 0.35, depreciation 0.08, rows for beta 0.900, 0.960, 0.990, 0.999. Capital 2.537, 5.082, 8.066, 9.502. Consumption 1.182, 1.360, 1.431, 1.439. Rates 11.11, 4.17, 1.01 and 0.10 per cent. In the notes: ten points of patience triple capital while consumption moves about 21 per cent.

BLOCK F - THE GOLDEN RULE AND THE COMPARISON. Maximise steady-state consumption over capital, obtain the condition that the marginal product equals depreciation, and compute 9.685 with consumption 1.439. Then a slide with the two conditions on consecutive lines, the extra term marked; argue the inequality from its positivity plus the monotonicity of the marginal product, and place both points on the hump, flat at its peak.

BLOCK G - WHY AN EFFICIENT ECONOMY STOPS SHORT. Three slides. Reject the premise in the word enough: the Golden Rule is about one point, ignoring when consumption arrives. State what the household maximises, a discounted sum over the path, and the transition reaching it would need. Under-accumulation is the optimum, the Golden Rule a benchmark.

BLOCK H - THE CONTRAST, THE LIMIT AND THE FLATNESS. Bring in Solow with an exogenous saving rate, where capital can exceed the Golden Rule so consumption could rise in every period by saving less, impossible once the rate is chosen. As beta approaches one the steady-state condition converges to the Golden Rule condition. Then the flatness: at beta 0.999 capital is 1.9 per cent short but consumption only 0.006 per cent, and at beta 0.96 capital is half while consumption is 5.5 per cent below. Explain by second-order loss at a maximum, connect to exercise 9.12, page 185, and close on the line that the distance to the Golden Rule is impatience, measured.

Include one runnable Python block using numpy, under thirty lines, comments in English. Compute the steady state and Golden Rule in closed form, confirm the Golden Rule is the argmax of steady-state consumption on a grid, confirm the steady state lies below it for every beta below one, and print both shortfalls.
