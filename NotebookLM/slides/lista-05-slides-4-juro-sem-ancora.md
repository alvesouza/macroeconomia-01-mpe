Build a slide deck in English from the sources below. This is deck 4 of 6 in a set organised by economic mechanism rather than by question. Its mechanism is the interest rate: what determines it, and how completely that changes once the economy can move goods through time. It is the hinge of the set, the only deck that puts the two questions side by side.

Sources. Sections 9.1 and 9.3 of "Livro_Kurlat_Cap09_General_Equilibrium.pdf" (= KURLAT9), question 1 item d and question 2 item a of "Lista_MPE_Macro1_2026_Lista5.pdf" (= LISTA5), and "Aula_Slides_Macro1_Aula6.pdf" (= AULA6).

Scope lock. Everything follows from KURLAT9 and AULA6. Chapter 8 of Kurlat is outside this course. No Bellman equations, dynamic programming, stochastic DSGE or RBC models, Calvo New-Keynesian Phillips curve, or time-series econometrics.

Output language: English throughout, whatever language the sources are in. Notation: r for the interest rate, r superscript K for the rental rate, rho for one over beta minus one.

THESIS. The Euler equation is the same in both halves of the problem set but means two different things, because what stands on the other side of it differs. When nothing can be stored, production fixes the consumption path and the interest rate is whatever makes the household content with a path it cannot alter. When capital can be accumulated, the same equation becomes a constraint on technology.

STRUCTURE. Aim for 22 to 26 slides. Run a two-column comparison throughout, headed frozen capital and accumulable capital, adding one row per result.

BLOCK A - THE EULER EQUATION, TWICE. Derive it by the ratio of two first-order conditions, then again by a perturbation moving a small amount of consumption between adjacent dates. Give the power-utility form, the consumption ratio equal to the bracket beta times one plus the interest rate, raised to one over sigma. One slide on why the second derivation earns its place: it shows the equation is a no-arbitrage condition on the household's own plan rather than an algebraic by-product.

BLOCK B - THE FROZEN-CAPITAL CASE. Impose goods clearing period by period, so consumption equals output at each date, and derive the rate as one over beta times the output ratio raised to the power sigma. Show explicitly that the marginal product of capital appears nowhere.

BLOCK C - WHY THAT IS NOT AN OVERSIGHT. There is no technology for moving goods between dates, so the rate cannot equal a rate of transformation, because no such rate exists. The quantity side is already determined, so the price carries no allocative work: here the interest rate reports, it does not allocate.

BLOCK D - THE COLLAPSE TO PURE IMPATIENCE. Equal productivity across periods gives equal hours, hence equal consumption, hence one plus the rate equal to one over beta. Give the number for beta equal to 0.96 and state the principle: with nothing to trade and no growth, the rate equals impatience exactly.

BLOCK E - THE INFINITE-HORIZON HOUSEHOLD. Write the discounted-sum objective, the flow budget constraint in every period, and the initial asset position given by the initial capital stock. Then a dedicated slide on the No-Ponzi condition: state it as a limit and explain why the problem is not well posed without it, namely that debt could be rolled over forever to finance unbounded consumption.

BLOCK F - WHAT MAKES CONSUMPTION GROW. Consumption rises if and only if beta times one plus the rate exceeds one, that is, if and only if the rate exceeds rho. Present three cases on one slide, rising, flat and falling paths, with the position of the rate relative to rho in each.

BLOCK G - WHAT SIGMA DOES AND DOES NOT DO. Sigma enters only through the exponent one over sigma, the elasticity of intertemporal substitution, so it governs how steeply the path tilts for a given gap between the rate and rho. Then the negative half: sigma affects how fast the economy travels, never where it arrives, because setting the consumption ratio to one raises the bracket to a power and one raised to any power is one.

BLOCK H - THE TWO ECONOMIES SIDE BY SIDE. Complete the comparison. Rows for what pins the consumption path, what pins the interest rate, whether the marginal product of capital appears, and what happens when productivity rises. Highlight the single row where the columns give opposite answers, and close on the statement that preferences determine the interest rate and technology determines the quantity of capital.

Include one runnable Python block using numpy, under twenty-five lines, comments in English. Simulate consumption paths under the Euler equation for three values of the rate relative to rho and three values of sigma, print the growth factor in each case, and assert it equals one for every sigma when the rate equals rho.
