Build a slide deck in Brazilian Portuguese from the sources below. This is deck 2 of 4 for this lecture, and its job is mechanics and numbers. The accounting identity and the production boundary were derived in deck 1; do not re-derive them. Exercises belong to deck 3 and synthesis to deck 4.

Sources. "Aula_MPE_Macro1_2026_Slides_1.pdf" (= AULA1) and chapter 1, section 1.2, of "Livro_Pablo_Kurlat_-_A_Course_in_Modern_Macroeconomics_2020_-_libgen.li.pdf" (= KURLAT).

Scope lock. Everything must follow from AULA1 and KURLAT section 1.2. Do not import Bellman equations, dynamic programming, stochastic DSGE or RBC models, the Calvo New-Keynesian Phillips curve, or time-series econometrics.

Output language: Brazilian Portuguese (pt-BR). Keep established English terms in parentheses at first use, e.g. "paridade do poder de compra (purchasing power parity)".

THESIS THIS DECK BUILDS TOWARD. Comparing output across time or across countries requires a set of prices, and there is no neutral set. Every index is a correct answer to a specific question, and the arithmetic here exists to show which question each one answers.

STRUCTURE. Aim for 18 to 22 slides. Every quantity gets computed on a running numerical example that stays visible; nothing is merely defined. Numbers are exact and appear on the slide.

BLOCK A - THE RUNNING EXAMPLE. Build a two-good, two-year table of prices and quantities, choosing values where one good becomes markedly cheaper and its quantity rises substantially, so the effects later in the deck are large enough to see. Pin this table as a header on every computational slide that follows. Compute nominal output in both years as the baseline.

BLOCK B - REAL OUTPUT COMPUTED TWICE. Compute real output in the later year valued at earlier-year prices, and the growth rate it implies. Then compute real output in the earlier year valued at later-year prices, and its implied growth rate. Put both growth rates on a single slide, side by side, in large type, and name them Laspeyres and Paasche. State explicitly that both computations are correct and that they answer different questions.

BLOCK C - THE MECHANISM BEHIND THE GAP. Show the substitution numerically. Identify the good whose relative price fell, show its quantity rising, and compute its expenditure share in each year. Then show how a weight taken from the year in which that good was still expensive gives it more influence than its current importance warrants. Derive the general direction as a proposition, then immediately construct a second numerical example where the ordering reverses, so the direction is understood as a tendency rather than a law.

BLOCK D - CHAINING, STEP BY STEP. Extend the example to a third year. Compute the year-on-year growth rates using each year's own prices as weights, then compound them into a chained index. Put the chained series next to both fixed-base series in one table. State the honest summary: chaining removes the dependence on a single arbitrary base year, but it makes a weighting choice every period rather than no choice at all. Note the practical cost, that chained levels stop being additive across components, and show a small case where the components fail to sum.

BLOCK E - THE DEFLATOR. Define it as the ratio of nominal to real output and compute it on the running example under each of the three real measures, producing three different deflator paths. Then contrast it with a fixed-basket consumer price index across three concrete dimensions in a three-row table: which basket, how often the weights update, and how imported goods are treated. Give one concrete circumstance under which the two indices move in opposite directions.

BLOCK F - ACROSS COUNTRIES, THE ARITHMETIC. Take one country's output in its own currency. Convert it at the market exchange rate. Then build a purchasing power parity conversion from a small basket of goods with prices in both countries, showing the implied parity rate and how it differs from the market rate. Compute the country's output both ways and put the two figures side by side.

BLOCK G - WHY THE WEDGE HAS A SIGN. Explain the mechanism with a two-column table of a traded good and a non-traded service priced in a rich and a poor country. Show that the traded good's prices are close and the service's are far apart. Derive the conclusion: because non-traded goods are cheaper where productivity is lower, market exchange rates systematically understate real income in poorer countries. Give the typical order of magnitude of the correction for a middle-income country.

Include one runnable Python block using numpy and pandas only that takes a price-quantity table and returns nominal output, both fixed-base real series, the chained index and the implied deflator, printing them as a single dataframe. Keep it under twenty-five lines with comments in Portuguese.
