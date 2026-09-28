# Plan: Ljungqvist & Sargent ch. 9 solutions

Chapter 9 (Overlapping Generations) has 13 exercises, printed pp. 366-378 (PDF = printed + 39).
All are analytical; the notebook holds numerical sanity checks of every key result.

1. Analytical (tex): 9.1 CRRA saving function, stationary/nonstationary monetary equilibria,
   limit return (w2/w1)^gamma; 9.2 within-generation lenders/borrowers, p_t = p* + c(w1/w2)^t,
   no Pareto ranking; 9.3 Lucas tree kills all monetary equilibria, unique tree equilibrium R>1;
   9.4 growth, R = n; 9.5 growth + all monetary equilibria, Pareto ranking; 9.6 Kareken-Wallace
   (constant e, indeterminacy under real deficits, determinacy with nominal anchors);
   9.7 credit controls (no monetary eq. at R=1; borrowing limit gives 1+r=1/2 and q=8/y);
   9.8 inside money / real bills; 9.9 social security crowds out money (tau<y/2);
   9.10 seigniorage (linear dynamics in 1/m, Laffer max z*=sqrt(N1 a/N2 b));
   9.11 unpleasant arithmetic (h(R)=D+(R2-1)B, good side of Laffer curve);
   9.12 Grandmont-Hall (p=pbar, r=0 unique); 9.13 Bryant-Keynes-Wallace (root product w2/w1,
   forced saving replicates and then attains golden rule).
2. Notebook `Resolucao/ljungqvist_sargent/ls_ch09.ipynb`: one section per exercise; saving
   functions by numerical optimisation vs closed forms; recursions vs closed-form price paths;
   brentq roots vs quadratic formulas; utility comparisons. Figures fig/ls09_*.pdf (fonttype 42).
3. `ls_solutions_ch09.tex` (ch07 preamble/boxes, full statements), pdflatex x2, pdffonts, clean aux.
4. README: Chapter 9 row after Chapter 8 (concurrent agent) / Chapter 7.
