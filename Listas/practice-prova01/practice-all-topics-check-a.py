"""All-topics practice list, Blocks 1-5 (practice-all-topics-block1..5.tex): checks every number.

Run: python practice-all-topics-check-a.py   (aborts on the first failed assert).
Numbers are checked with exact fractions where the solution states a fraction and to the
printed rounding otherwise; the golden-rule algebra of Block 3 is checked with sympy; each
multiple-choice key is recomputed and the distractor values are asserted to differ from it.
"""
import math
from fractions import Fraction as F

import sympy as sp


def close(x, y, tol=5e-4):
    """Assert that x agrees with the printed value y to the printed rounding."""
    assert abs(x - y) <= tol, (x, y)


# ---------------------------------------------------------------- Block 1
# Q1: Kurlat Ex. 1.3 (Fructus data, p. 28): year, qA, pA, qB, pB, qC, pC
FRUCTUS = """2000 100 40 50 30 200 20
2001 103 39 47 35 206 20
2002 107 39 47 38 213 19
2003 109 39 45 38 215 18
2004 112 40 46 41 224 18
2005 112 39 46 39 227 17
2006 114 40 47 36 237 16
2007 115 40 46 42 249 16
2008 119 40 43 44 255 16
2009 118 42 40 46 262 15
2010 116 43 41 44 268 15
2011 118 42 40 50 280 15
2012 117 42 41 50 289 15
2013 119 43 40 53 290 14
2014 120 44 40 56 297 13
2015 125 45 41 59 308 13
2016 128 45 38 66 320 13
2017 129 46 38 61 330 13
2018 131 47 37 64 344 13
2019 136 47 37 61 353 13
2020 143 47 34 61 361 12"""
rows = [list(map(int, ln.split())) for ln in FRUCTUS.splitlines()]
qs = [(r[1], r[3], r[5]) for r in rows]
ps = [(r[2], r[4], r[6]) for r in rows]


def dot(u, v):
    """Value of quantities v at prices u."""
    return sum(x * y for x, y in zip(u, v))


base = [dot(ps[0], q) for q in qs]
chain = [base[0]]
for t in range(1, 21):
    gI = dot(ps[t - 1], qs[t]) / dot(ps[t - 1], qs[t - 1])
    gF = dot(ps[t], qs[t]) / dot(ps[t], qs[t - 1])
    chain.append(chain[-1] * (gI * gF) ** 0.5)       # Kurlat's geometric average
assert (base[0], base[1]) == (9_500, 9_650)
assert dot(ps[1], qs[1]) == 9_782 and dot(ps[1], qs[0]) == 9_650
close(9_650 / 9_500 - 1, 0.01579, 5e-6)
close(9_782 / 9_650 - 1, 0.01368, 5e-6)
close((9_650 / 9_500 * 9_782 / 9_650) ** 0.5 - 1, 0.01473, 5e-6)
close(chain[1], 9_639.97, 5e-3)
for t, yb, yc in ((5, 10_400, 10_341.8), (10, 11_230, 10_950.0), (15, 12_390, 11_922.8), (20, 13_960, 12_976.2)):
    assert base[t] == yb, (t, base[t])
    close(chain[t], yc, 0.05)
close((base[20] / base[0]) ** (1 / 20) - 1, 0.0194, 5e-5)
close((chain[20] / chain[0]) ** (1 / 20) - 1, 0.0157, 5e-5)
gap = [b - c for b, c in zip(base, chain)]
assert all(g1 >= g0 for g0, g1 in zip(gap, gap[1:])), gap   # the gap widens every year
assert (qs[20][2], ps[20][2], qs[20][1], ps[20][1]) == (361, 12, 34, 61)

# Q2: created economy
VA = dict(F=500, P=700 - 300 - 100 - 40, N=40 + 60, G=120)
wages = dict(F=250, P=180, N=30 + 60, G=120)
profit = dict(F=250, P=80, N=10)
for f in ("F", "P", "N"):
    assert VA[f] == wages[f] + profit[f], f
GDP = sum(VA.values())
C, I, G, X, M = 650, 50 + 60, 120, 200, 100
assert GDP == C + I + G + X - M == sum(wages.values()) + sum(profit.values()) == 980
assert GDP - 60 == 920                    # software expensed as an intermediate input of N
assert GDP + 80 == 1060                   # wrong: Bolsa Familia transfer counted in G
assert GDP - 30 == 950                    # GNI: 30 of F's profit paid to a foreign owner
assert 500 + 700 + 100 + 120 == 1420      # wrong: gross output summed (double counting)
nominal2 = 650 * 1.10 + 50 * 1.10 + 60 + 120 * 1.05 + 200 * 1.20 - 100 * 1.50
close(nominal2, 1046, 1e-9)
defl = nominal2 / 980
prod2 = (360 + 240) + (770 - 360 - 150 - 40) + 100 + 126   # production side, 2026
assert prod2 == 1046 and 715 + 55 == 770
assert 70 + 6 + 40 - 50 == 66 and 980 + 66 == 1046
close(defl, 1.0673, 1e-4)                 # GDP deflator +6.73%
cpi = 1.10                                # consumers buy only food (the app is free)
assert cpi - 1 > defl - 1

# Q3 (MC, key C): PPP
y_brl, e_mkt, e_ppp, y_us = 60_000, 5.0, 2.5, 85_000
assert y_brl / e_mkt == 12_000 and y_brl / e_ppp == 24_000
close(y_brl / e_mkt / y_us, 0.1412)
close(y_brl / e_ppp / y_us, 0.2824)
assert y_brl * e_ppp == 150_000           # distractor D
close(y_brl * e_ppp / y_us, 1.76, 5e-3)

# ---------------------------------------------------------------- Block 2
# Q4: Kurlat Ex. 4.2 (Black Death), alpha = 1/3, L -> 2L/3, K fixed
a = 1 / 3
close((2 / 3) ** (1 - a), 0.763)          # Y
close((3 / 2) ** a, 1.145)                # y and w
close((3 / 2) ** (a - 1), 0.763)          # r^K = MPK

# Q5: created Solow, A = 1, alpha = 1/3, s = 0.2, n = 0.02, delta = 0.08
s, n, d = 0.2, 0.02, 0.08
kss = (s / (n + d)) ** (1 / (1 - a))
yss = kss ** a
close(kss, 2.8284)
close(yss, 1.4142)
close((1 - s) * yss, 1.1314)
assert abs(s * kss ** a - (n + d) * kss) < 1e-12           # break-even holds exactly
s2 = 0.25
k2, y2 = (s2 / (n + d)) ** 1.5, (s2 / (n + d)) ** 0.5
close(k2, 3.9528)
close(y2, 1.5811)
close(y2 / yss - 1, 0.1180)
close(0.5 * math.log(1.25), 0.1116)
close(kss ** (a - 1), 0.5, 1e-12)
gk = ((1 - d) + s2 * kss ** (a - 1)) / (1 + n) - 1
close(gk, 0.0245)
close((1 + gk) ** a - 1, 0.0081)
close((1 - s2) * yss, 1.0607)             # c on impact, below 1.1314
close((1 - s2) * y2, 1.1859)              # new steady-state c, above 1.1314
# (c) convergence: Piaui at k*/8
kpi = kss / 8
close(kpi ** (a - 1), 2.0, 1e-12)
close(kpi ** a, 0.7071)
g_pi = ((1 - d) + s * kpi ** (a - 1)) / (1 + n) - 1
close(g_pi, 0.2941)
close((1 + g_pi) ** a - 1, 0.0897)
g_pi_low = ((1 - d) + 0.1 * kpi ** (a - 1)) / (1 + n) - 1
close(g_pi_low, 0.0980)
close((1 + g_pi_low) ** a - 1, 0.0317)
close((0.1 / (n + d)) ** 0.5, 1.0, 1e-12)               # own steady state y* = 1
close(1 / yss, 0.7071)
close(kpi ** a / yss, 0.5, 1e-12)
close(s * yss, 0.2828)
close(kpi, 0.3536)

# Q6 (MC, key A): n from 1% to 2%; with s/(n+d) the level falls, growth of Y rises
assert (s / (0.02 + d)) < (s / (0.01 + d))

# ---------------------------------------------------------------- Block 3
# Q7: Kurlat Ex. 5.4
close(0.2 / 0.1, 2.0, 1e-12)
for t, r in ((5, 0.7048), (10, 0.8257), (50, 0.9974)):
    K = 2.0
    est = 1.0
    for _ in range(t):
        est = 0.9 * est + 0.2
    close(est, 2 - 0.9 ** t, 1e-12)
    close(est / K, r)
    close(est, {5: 1.4095, 10: 1.6513, 50: 1.9948}[t])
    close(0.9 ** t, {5: 0.5905, 10: 0.3487, 50: 0.0052}[t])
close(0.2 / 0.05 / 2, 2.0, 1e-12)
close(2 ** -0.35, 0.7846)

# Q8: created golden rule, per efficiency unit, n + g + delta = 0.08, alpha = 1/3
S, al = sp.symbols("s alpha", positive=True)
lnc = sp.log(1 - S) + al / (1 - al) * sp.log(S)
sgr = sp.solve(sp.diff(lnc, S), S)
assert sgr == [al], sgr
soc = sp.diff(lnc, S, 2).subs(S, al)
assert sp.simplify(soc + 1 / (al * (1 - al) ** 2)) == 0   # SOC = -1/(alpha(1-alpha)^2) < 0
wrong = sp.solve(sp.diff(sp.log(1 - S) + sp.log(S) / (1 - al), S), S)
assert sp.simplify(wrong[0] - 1 / (2 - al)) == 0          # dropped-exponent answer
assert sp.limit(wrong[0], al, 0) == sp.Rational(1, 2)
x = 0.08


def ct(s_):
    """Steady-state consumption per efficiency unit at saving rate s_."""
    return (1 - s_) * (s_ / x) ** 0.5


close(ct(0.18), 1.23)
close(ct(1 / 3), 1.3608)
close(ct(0.45), 1.3044)
close((0.18 / x) ** 1.5, 3.375)
close((1 / 3 / x) ** 1.5, 8.5052)
close((0.45 / x) ** 1.5, 13.3409)
for s_, r in ((0.18, 0.0981), (1 / 3, 0.03), (0.45, 0.0093)):
    close(a * x / s_ - 0.05, r)
    close(a * x / s_ - 0.05 - 0.03, x * (a / s_ - 1), 1e-12)
close(ct(1 / 3) / ct(0.18), 1.106)
close((1 / 3 / x) ** 0.5, 2.0412)
close(a * x / 0.18, 0.1481)
yt_old = (0.45 / x) ** 0.5
close(yt_old, 2.3717)
close(0.55 * yt_old, 1.3044)
close((2 / 3) * yt_old, 1.5811)

# Q9 (MC, key D): growth accounting, alpha = 0.4
gY, gK, gL = 3.2, 4.4, 1.8
res = gY - 0.4 * gK - 0.6 * gL
close(res, 0.36, 1e-12)
close(gY - gL, 1.4, 1e-12)
close((gY - gL) - 0.4 * (gK - gL), 0.36, 1e-12)
close(res / (gY - gL), 0.257)
close(res / gY, 0.1125)                   # distractor: share of output growth
close(gY - 0.6 * gK - 0.4 * gL, -0.16, 1e-12)
close(-0.16 / gY, -0.05)
close(gY - 0.4 * gK, 1.44, 1e-12)
close(1.44 / gY, 0.45)
close(gY - 0.6 * gK, 0.56, 1e-12)
close(0.56 / (gY - gL), 0.4)

# ---------------------------------------------------------------- Block 4
# Q10: Kurlat Ex. 6.4, beta = 1, r = 0 -> c1 = c2 = (y1 + y2)/2
A_, B_ = (2, 4), (6, 4)
cA, cB = sum(A_) / 2, sum(B_) / 2
assert (cA, cB) == (3, 5)
slope = (cB - cA) / (B_[0] - A_[0])
assert slope == 0.5 and cA - slope * A_[0] == 2
ys, cs = [2, 6, 4, 4], [3, 5, 3, 5]
my, mc = sum(ys) / 4, sum(cs) / 4
cov = sum((u - my) * (v - mc) for u, v in zip(ys, cs)) / 4
var = sum((u - my) ** 2 for u in ys) / 4
assert (cov / var, mc - cov / var * my) == (0.5, 2.0)
assert (my, mc, cov, var) == (4, 4, 1, 2)
close(3 / 2, 1.5, 0)
close(5 / 6, 0.83, 5e-3)

# Q11: created two-period problem, log utility, beta = 0.6, 1 + r = 2
beta, R = F(3, 5), 2
W = 10 + 40 + 10 - 10 + F(90 - 10, R)
assert W == 90
c1 = W / (1 + beta)
assert c1 == F(225, 4)                    # 56.25
c2 = beta * R * c1
assert c2 == F(135, 2)                    # 67.5
a1 = 50 - c1
assert a1 == F(-25, 4)
assert c2 == 80 + R * a1
# Ricardian: tau1 = 0, tau2 = 30
W2 = 10 + 40 + 10 - 0 + F(90 - 30, R)
assert W2 == W and 60 - c1 == F(15, 4)
# credit constraint a >= 0 before the cut
assert F(1, 50) > beta * R / 80           # 0.02 > 0.015: Euler holds as an inequality
assert F(1, 50) == F(2, 100) and beta * R / 80 == F(3, 200)
assert F(1, 50) - beta * R / 80 == F(1, 200)                  # mu = 0.005
assert beta * R == F(6, 5) and W / (1 + beta) == F(90) / F(8, 5)
assert 2 ** (1 / 30) - 1 > 0.0225 and 2 ** (1 / 30) - 1 < 0.0235  # about 2.3% a year
assert (c1 - 50) / 10 == F(5, 8)          # MPC out of the tax cut

# Q12 (MC, key B): y2 = 0, d c1/dr has the sign of (sigma - 1)/sigma
sg, bt, rr, y1 = sp.symbols("sigma beta r y1", positive=True)
c1s = y1 / (1 + bt ** (1 / sg) * (1 + rr) ** (1 / sg - 1))
dc = sp.diff(c1s, rr)
for sv in (0.5, 2.0, 1.0):
    val = dc.subs({sg: sv, bt: 0.9, rr: 0.05, y1: 1})
    if sv > 1:
        assert val > 0
    elif sv < 1:
        assert val < 0
    else:
        assert abs(float(val)) < 1e-12

# ---------------------------------------------------------------- Block 5
# Q13: Kurlat Ex. 7.3, tau_c = tau/(1 - tau) and equal revenue
for tau in (0.1, 0.3, 0.5):
    tc = tau / (1 - tau)
    close(1 / (1 + tc), 1 - tau, 1e-12)
    h, w = 0.4, 1.3
    c = w * (1 - tau) * h
    close(tc * c, tau * w * h, 1e-12)
close(0.3 / 0.7, 0.4286)

# Q14: created labour supply, u = ln c + theta ln l, theta = 1.5, w(1 - tau) = 0.7, T = 0.1
th, wt, T = F(3, 2), F(7, 10), F(1, 10)
lsr = th * (wt + T) / ((1 + th) * wt)
assert lsr == F(24, 35)                   # 0.6857
h = 1 - lsr
assert h == F(11, 35)                     # 0.3143
assert h == 1 / (1 + th) - th * T / ((1 + th) * wt)
assert h == (1 - th * T / wt) / (1 + th)  # PSET 4 Q1(a) with gamma = 1, b = theta
c = wt * h + T
assert c == F(8, 25)                      # 0.32
assert th * c / wt == lsr                 # FOC theta/l = w~/c
assert th * T == F(3, 20)                 # reservation wage 0.15
eM = th * T / ((1 + th) * wt * h)
assert eM == F(3, 11)                     # 0.2727
eF = lsr / h
assert eF == F(24, 11)                    # 2.1818
hT2 = 1 / (1 + th) - th * F(2, 10) / ((1 + th) * wt)
assert hT2 == F(8, 35)                    # 0.2286
close(float(hT2 - h), -0.0857)
assert th * F(2, 10) == F(3, 10)          # reservation wage with T = 0.2
h_tau = 1 / (1 + th) - th * T / ((1 + th) * F(6, 10))
assert h_tau == F(3, 10)
close(float(h_tau - h), -0.0143)

# Q15 (MC, key E): Kurlat one-period DMP, m = A V^(1/2) U^(1/2), U = 0.1, A = 1
U = 0.1
for S_chi, V, Up in ((0.4, 0.016, 0.06), (0.3, 0.009, 0.07)):
    Vv = U * S_chi ** 2
    close(Vv, V, 1e-12)
    m = (Vv * U) ** 0.5
    close(m / Vv * S_chi, 1.0, 1e-12)     # free entry: q (1-mu)(y-b) = chi
    close(U - m, Up, 1e-12)

close(U * 0.5 ** 2, 0.025, 1e-12)        # distractor A (surplus up)
close(0.016 * 0.3 / 0.4, 0.012, 1e-12)    # distractor C (V proportional to S)
close(0.3 / 1.75, 0.1714)
close(float(F(24, 35)), 0.6857)
close(float(F(11, 35)), 0.3143)
close(float(F(8, 35)), 0.2286)
close(float(F(24, 11)), 2.18, 5e-3)
close(float(F(3, 11)), 0.27, 5e-3)
assert F(5, 2) * F(7, 10) * F(11, 35) == F(11, 20)          # 0.55
assert F(3, 2) * F(8, 10) / (F(5, 2) * F(7, 10)) == F(24, 35)

print("practice-all-topics-check-a: all assertions passed")
