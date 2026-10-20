"""Verify every closed form and figure coordinate in prova-01-solution.tex.

Aborts on the first mismatch. Run from Prova/: python prova-01-solution-check.py
"""
import random

import sympy as sp


def zero(expr):
    """True if expr simplifies to 0, else if it vanishes at 20 random admissible points (all in (0,1))."""
    if sp.simplify(expr) == 0:
        return True
    for _ in range(20):
        val = expr.subs({x: random.uniform(0.05, 0.95) for x in expr.free_symbols})
        if abs(complex(sp.N(val))) > 1e-9:
            return False
    return True

s, sg, n, d, A, b, a0, r, w, Pi = sp.symbols(
    "s sigma n delta A beta a0 r w Pi", positive=True)
k = sp.symbols("k", positive=True)

# Q1: three approaches agree.
assert 600 + (1000 - 600) == 1000
assert 600 + (1000 - 600 - 100) + 100 == 1000
assert 600 + 300 + (100 + 100) == 1000 + 100 == 1100

# 2.a: steady state of (1+n)k' = (1-d)k + sAk^sg.
kss = (s * A / (n + d)) ** (1 / (1 - sg))
assert zero((1 - d) * kss + s * A * kss**sg - (1 + n) * kss)

# 2.b: argmax of c_SS = (1-s) A kss^sg is s = sigma (FOC and SOC).
lnc = sp.log(1 - s) + sg / (1 - sg) * sp.log(s)
assert sp.solve(sp.diff(lnc, s), s) == [sg]
assert zero(sp.diff(lnc, s, 2).subs(s, sg) + 1 / (1 - sg) ** 2 + 1 / ((1 - sg) * sg))
kgr = sp.solve(sg * A * k ** (sg - 1) - (n + d), k)[0]
assert zero((n + d) * kgr / (A * kgr**sg) - sg)

# 2.d: Euler + budget give c1 = W/(1+beta).
c1, c2 = sp.symbols("c1 c2", positive=True)
W = a0 + w * A + Pi
sol = sp.solve([c2 - b * (1 + r) * c1, c1 + c2 / (1 + r) - W], [c1, c2], dict=True)[0]
assert zero(sol[c1] - W / (1 + b))
assert zero(W - sol[c1] - b * W / (1 + b))

# 2.e: wage + profit = output; steady state with a0 = 0; slope there = sigma.
wA = (1 - sg) * A * k**sg
assert zero(wA + (A * k**sg - wA) - A * k**sg)
keq = (b * A / (1 + b)) ** (1 / (1 - sg))
phi = b / (1 + b) * A * k**sg
assert zero(phi.subs(k, keq) - keq)
assert zero(sp.diff(phi, k).subs(k, keq) - sg)

# Figure 1 coordinates (A=1, sigma=0.4, beta=0.5, a0=0.15).
kk = 1.0
for _ in range(500):
    kk = (0.15 + kk**0.4) / 3
assert abs(kk - 0.2376) < 5e-5
assert abs((1 / 3) ** (1 / 0.6) - 0.1602) < 5e-5

# Q3: AD/AS solution and policy.
S, kap, eta, i, ybar, ynat, pe, pbar, ye, ph = sp.symbols(
    "sigma kappa eta i ybar y_n p_e pbar y_e phi", real=True)
y, p = sp.symbols("y p", real=True)
eqs = [y - (ybar - S * (i - (pbar - p))), p - pe - kap * (y - ynat)]
yp = sp.solve(eqs, [y, p], dict=True)[0]
assert zero(sp.diff(yp[y], ybar) - 1 / (1 + S * kap))
assert zero(sp.diff(yp[p], ybar) - kap / (1 + S * kap))
dybar = -1 / (1 / S + eta)
di = sp.solve(sp.diff(yp[y], ybar) * dybar + sp.diff(yp[y], i) * sp.Symbol("x"), sp.Symbol("x"))[0]
assert zero(di + 1 / (1 + S * eta))

# 3.c: targeting rule from dL/dy = 0 along AS; i* moves one-for-one with ybar/sigma, free of phi.
L = (y - ye) ** 2 / 2 + ph / (2 * kap) * (kap * (y - ynat)) ** 2
ystar = sp.solve(sp.diff(L, y), y)[0]
assert zero(ystar - (ye + ph * kap * ynat) / (1 + ph * kap))
pstar = pe + kap * (ystar - ynat)
assert zero((ystar - ye) + ph * (pstar - pe))
istar = sp.solve(ystar - (ybar - S * (i - (pbar - pstar))), i)[0]
assert zero(sp.diff(istar, ybar) - 1 / S)
assert sp.diff(sp.diff(istar, ybar), ph) == 0

# Figures 2-3 coordinates (kappa=0.5, sigma=1, phi=2, y_n=0, y_e=1, shift 0.6).
num = {kap: 0.5, ph: 2, ynat: 0, ye: 1, pe: 0}
assert abs(float(ystar.subs(num)) - 0.5) < 1e-12 and abs(float(pstar.subs(num)) - 0.25) < 1e-12
assert abs(0.5 - 0.6 / 1.5 - 0.1) < 1e-12 and abs(-0.6 / 1.5 + 0.4) < 1e-12
Lo = 0.5 * 0.25 + 2 / (2 * 0.5) * 0.25**2
assert abs((2 * Lo) ** 0.5 - 0.7071) < 1e-4 and abs((2 * Lo * 0.5 / 2) ** 0.5 - 0.3536) < 1e-4

print("prova-01-solution: all checks passed")
