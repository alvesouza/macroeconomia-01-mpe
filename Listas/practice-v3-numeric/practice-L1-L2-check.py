"""Practice list A v3 (Listas 1-2, qualifier level): independent check of every number and derivation.

Run: python practice-L1-L2-check.py   (aborts on the first mismatch).
Each chk() mirrors a value printed in practice-L1-L2.tex; sympy checks the closed forms.
"""
from math import exp, log, sqrt

import sympy as sp
from scipy.optimize import brentq


def chk(name, value, expected, tol=5e-4):
    assert abs(value - expected) <= tol * max(abs(expected), 1e-3), f"{name}: {value} != {expected}"
    print(f"{name:<48} {value:.6f}")


# ===================== Block 1: measurement and welfare =====================
# Q1a CES (eta = 3), base shares (1/2, 1/2), price relatives (1.5, 1)
eta = 3.0
true_col = (0.5 * 1.5 ** (1 - eta) + 0.5) ** (1 / (1 - eta))
lasp = 0.5 * 1.5 + 0.5
chk("A1a true COL (CES)", true_col, 1.176697)
chk("A1a Laspeyres", lasp, 1.25)
chk("A1a Laspeyres bias %", 100 * (lasp / true_col - 1), 6.2291)
chk("A1a Cobb-Douglas bias % (distractor)", 100 * (lasp / sqrt(1.5) - 1), 2.0621)
chk("A1a second-order approx (eta/2) Var(lnR)", eta / 2 * 0.25 * log(1.5) ** 2, 0.061654)
# Q1b Jones-Klenow welfare growth over 30 years (sigma = 1, ubar = 5)
a0, a1, ub = 0.66, 0.76, 5.0
Eln0, Eln1 = 0.0 - 1.2 / 2, 0.45 - 1.0 / 2
lnlam = a1 / a0 * (ub + Eln1) - ub - Eln0
chk("A1b ln lambda over 30 years", lnlam, 1.3)
chk("A1b annual welfare growth %", 100 * lnlam / 30, 4.33333)
chk("A1b life-expectancy part", (a1 / a0 - 1) * (ub + Eln1), 0.75)
# Q1c Paasche above Laspeyres
L = 0.5 * 1.2 + 0.5 * 1.0
P = (0.5 * 1.2 * 1.3 + 0.5 * 1.0) / (0.5 * 1.3 + 0.5 * 1.0)
cov = 0.5 * (1.2 - L) * (1.3 - 1.15) + 0.5 * (1.0 - L) * (1.0 - 1.15)
chk("A1c Laspeyres price", L, 1.1)
chk("A1c Paasche price", P, 1.113043)
chk("A1c Bortkiewicz P/L", 1 + cov / (L * 1.15), P / L)

# Q2 new goods (CES): exact index, power means, Feenstra correction
p, b, x, lam_, U = sp.symbols("p b x lambda U", positive=True)
et = sp.Symbol("eta", positive=True)
# two-variety expenditure minimization, check the exact index formula numerically
from scipy.optimize import minimize
import numpy as np
pp, bb, ee = np.array([2.0, 3.0, 1.5]), np.array([1.0, 1.4, 0.8]), 4.0
def util(xv):
    return np.sum((bb * xv) ** ((ee - 1) / ee)) ** (ee / (ee - 1))
res = minimize(lambda xv: pp @ xv, x0=np.ones(3), constraints={"type": "eq", "fun": lambda xv: util(xv) - 1},
               bounds=[(1e-9, None)] * 3, method="SLSQP", options={"ftol": 1e-12, "maxiter": 500})
P_exact = np.sum((pp / bb) ** (1 - ee)) ** (1 / (1 - ee))
chk("A2a min cost of one util = CES index", res.fun, P_exact, tol=1e-5)
shares = (pp / bb) ** (1 - ee) / np.sum((pp / bb) ** (1 - ee))
chk("A2a expenditure share of variety 1", pp[0] * res.x[0] / res.fun, shares[0], tol=1e-4)
# power-mean representation with current shares: P1/P0 = (sum s1 R^(eta-1))^(1/(eta-1))
s0 = np.array([0.3, 0.5, 0.2]); R = np.array([1.3, 0.9, 1.1]); e2 = 2.5
exact = np.sum(s0 * R ** (1 - e2)) ** (1 / (1 - e2))
s1 = s0 * R ** (1 - e2) / np.sum(s0 * R ** (1 - e2))
assert abs(np.sum(s1 * R ** (e2 - 1)) ** (1 / (e2 - 1)) - exact) < 1e-12
assert np.sum(s0 * R) >= exact >= 1 / np.sum(s1 / R)                 # Laspeyres >= exact >= Paasche
# Feenstra: P_t = P_t^C * lambda_t^(1/(eta-1))
chk("A2d true inflation % (eta=4)", 100 * (1.05 * 0.96 ** (1 / 3) - 1), 3.58088)
chk("A2d overstatement pp (eta=4)", 5 - 100 * (1.05 * 0.96 ** (1 / 3) - 1), 1.41912)
chk("A2d true inflation % (eta=2)", 100 * (1.05 * 0.96 - 1), 0.8)
q = np.array([1.0, 1.0, 1.0]); cont = [0, 1]                           # numeric Feenstra identity
Pfull = np.sum(q[:3] * (pp / bb) ** (1 - ee)) ** (1 / (1 - ee))
PC = np.sum((pp / bb)[cont] ** (1 - ee)) ** (1 / (1 - ee))
lamC = np.sum((pp / bb)[cont] ** (1 - ee)) / np.sum((pp / bb) ** (1 - ee))
chk("A2c Feenstra identity", Pfull, PC * lamC ** (1 / (ee - 1)), tol=1e-10)

# ===================== Block 2: growth =====================
alpha = 0.4
chk("A3a MPK ratio, no human capital", 0.25 ** ((alpha - 1) / alpha), 8.0)
chk("A3a MPK ratio, with human capital", (0.25 / 0.6) ** ((alpha - 1) / alpha), 3.718147)
# Q3b CES golden rule, rho = -1, alpha = 1/2, N = 0.08
k = sp.Symbol("k", positive=True)
f = k / (sp.Rational(1, 2) + sp.Rational(1, 2) * k)
kg = sp.solve(sp.Eq(sp.diff(f, k), sp.Rational(8, 100)), k)
kg = [v for v in kg if v > 0][0]
chk("A3b k_gold", float(kg), 4.0)
chk("A3b saving rate at golden rule", float(sp.Rational(8, 100) * kg / f.subs(k, kg)), 0.2)
chk("A3b capital share at k_gold", float((sp.diff(f, k) * k / f).subs(k, kg)), 0.2)

# Q4 open-economy Solow
al, rs, d, ng, s = 1 / 3, 0.04, 0.05, 0.03, 0.15
N = ng + d
ks = (al / (rs + d)) ** (1 / (1 - al))
ys = ks ** al
wage = (1 - al) * ys
chk("A4 k* (pinned by r*)", ks, 7.127781)
chk("A4 y*", ys, 1.924501)
chk("A4 wage per effective worker", wage, 1.283001)
lam = N - s * (rs + d)
om = s * wage / lam
chk("A4 convergence speed of wealth", lam, 0.0665)
chk("A4 half-life (years)", log(2) / lam, 10.42330)
chk("A4 omega* (wealth)", om, 2.893987)
chk("A4 net foreign assets", om - ks, -4.233794)
chk("A4 foreign-owned share of capital", (ks - om) / ks, 0.593985)
chk("A4 GNI/GDP", (wage + (rs + d) * om) / ys, 0.802007)
chk("A4 creditor threshold s", al * N / (rs + d), 0.296296)
chk("A4 closed-economy speed (1-a)N", (1 - al) * N, 0.053333)
s2 = 0.25
om2 = s2 * wage / (N - s2 * (rs + d))
chk("A4 omega* with s=0.25", om2, 5.578207)
# symbolic: steady state and creditor condition
S_, W_, Y_, A_, R_, N2 = sp.symbols("s w y alpha r N", positive=True)
omega_ss = S_ * (1 - A_) * Y_ / (N2 - S_ * R_)
kstar = A_ * Y_ / R_                                       # (r*+delta) k* = alpha y*
cond = sp.simplify((omega_ss - kstar) * (N2 - S_ * R_) / Y_)
assert sp.simplify(cond - (S_ - A_ * N2 / R_)) == 0       # creditor iff s > alpha N/(r*+delta)
# ---- Q2(d)-(e): deflator bias -> measured growth -> Solow residual; sensitivity
bC = 100 * (1.05 - 1.05 * 0.96 ** (1 / 3))                 # pp per year, eta = 4, 4% new varieties
chk("A2d consumption-deflator bias (pp)", bC, 1.419093)
sC, sI, a3 = 0.8, 0.2, 1 / 3
resid = lambda bI: -(sC * bC + sI * bI) + a3 * bI           # g_A^m - g_A
chk("A2d residual bias, b_I = 0", resid(0.0), -1.135274)
chk("A2d residual bias, b_I = b_C", resid(bC), -0.946062)
chk("A2d residual bias, b_I = 3 b_C", resid(3 * bC), -0.567637)
chk("A2e threshold b_I where the bias vanishes", sC * bC / (a3 - sI), 8.514556)
assert abs(resid(sC * bC / (a3 - sI))) < 1e-12
for et_, n_, val in [(2, .02, 2.1), (2, .04, 4.2), (2, .08, 8.4), (4, .02, 0.704719), (4, .04, 1.419093),
                     (4, .08, 2.878173), (8, .02, 0.302604), (8, .04, 0.610548), (8, .08, 1.243305)]:
    chk(f"A2e inflation bias pp eta={et_} new={n_}", 100 * 1.05 * (1 - (1 - n_) ** (1 / (et_ - 1))), val)
# bias falls with eta and rises with the new-variety share (signs used in A2e)
bias = lambda e_, n_: 1.05 * (1 - (1 - n_) ** (1 / (e_ - 1)))
assert bias(3, .04) > bias(3.1, .04) and bias(3, .05) > bias(3, .04)

# ---- Q4(e): GNI/GDP = (1-alpha) N / Lambda; omega*/k* = s(1-a)(r+d)/(a Lambda)
def open_econ(s_, r_, ng_, a_, d_=0.05):
    N_ = ng_ + d_
    k_ = (a_ / (r_ + d_)) ** (1 / (1 - a_)); y_ = k_ ** a_
    L_ = N_ - s_ * (r_ + d_)
    om_ = s_ * (1 - a_) * y_ / L_
    return om_ / k_, (1 - a_) * N_ / L_, log(2) / L_
for lab, args, wk, gg, hl in [("base", (0.15, 0.04, 0.03, 1 / 3), 0.406015, 0.802005, 10.42327),
                              ("s=.25", (0.25, 0.04, 0.03, 1 / 3), 0.782609, 0.927536, 12.05475),
                              ("r*=.06", (0.15, 0.06, 0.03, 1 / 3), 0.519685, 0.839895, 10.91569),
                              ("n+g=.02", (0.15, 0.04, 0.02, 1 / 3), 0.477876, 0.825959, 12.26805),
                              ("alpha=.4", (0.15, 0.04, 0.03, 0.4), 0.304511, 0.721805, 10.42327)]:
    a_, b_, c_ = open_econ(*args)
    chk(f"A4e omega*/k* {lab}", a_, wk)
    chk(f"A4e GNI/GDP {lab}", b_, gg)
    chk(f"A4e half-life {lab}", c_, hl)
# closed form GNI/GDP = (1-a)N/Lambda, equal to 1 exactly at the creditor threshold
a4, r4, N4 = 1 / 3, 0.04, 0.08
sbar = a4 * N4 / (r4 + 0.05)
assert abs(open_econ(sbar, r4, 0.03, a4)[1] - 1) < 1e-12 and abs(open_econ(sbar, r4, 0.03, a4)[0] - 1) < 1e-12
# phase-line points drawn in the figure (s = 0.15 and 0.25): omega-dot at omega = 0 and the steady states
chk("A4d omega-dot intercept s=.15", 0.15 * wage, 0.192450)
chk("A4d omega-dot intercept s=.25", 0.25 * wage, 0.320750)
print("\nall checks passed")
