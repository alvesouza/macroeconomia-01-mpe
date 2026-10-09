# Practice list C (practice-L5-L6) — review fixes, 2026-10-08

Scope: `Listas/practice-L5-L6-block{1,2,3a,3b}.tex` and `-check-b{1,2,3a,3b}.py` only.

1. Q5 aligned to Q6: g >= 0, policy keeps i >= 0, pi* > 0; Q6 gains the nominal bond
   (budget, third FOC, Fisher as no arbitrage); check-b3a draws g >= 0, pi* > 0, admissible mu;
   check-b3b verifies Fisher from the two bond FOCs.
2. Q6(e) statement asks sigma->0, sigma=1, g->0 and a->0 (rubric already grades all four).
3. Q2(a) rubric: quoted conditions capped at 0.5 pt (a third of 1.5).
4. Notation: pi(t)/pi(s) for time paths in Q4(c)-(d); w(i) = W(i)/Y defined in the Q6(d)
   statement (with W(i) and i_T), used in Q5(c), Q6(d)-(e); G, H for the Q4(e) functions;
   kbar = K/h in Q2.
5. Q4 stem: "S_0 is the seigniorage that would hold debt at b_0", "from T on, debt is held at b_T";
   (a) derives S_0 = d + r b_0.
6. MC keys B, A, D, C, A, B (A2 B2 C1 D1). Each item: key, two single-mistake distractors, and one
   combining both, so every feature splits or points to a distractor:
   Q1a c fixed / Y fixed / both; Q1b log Euler / sigma as EIS / net investment + log Euler;
   Q3a forgone interest / triangle / triangle with average balances Y/N;
   Q3b still to come / semi-elasticity 1/a / both; Q5a no growth / inverted beta / both;
   Q5b approximate Fisher / minus r / both. Checks re-derive each and assert it differs from the key.

Done when: `python practice-L5-L6-check.py` passes; both PDFs build with no errors and no
Overfull hbox > 5pt; key 10-15 pages; pdffonts all Type 1; build leftovers deleted.
