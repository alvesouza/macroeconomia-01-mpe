"""Romer 1.12 and 1.15 (hardest-parts/romer-1-12.tex, romer-1-15.tex): independent checks.

Run: python check-1-12-1-15.py   (aborts on the first mismatch).
sympy re-derives every closed form of the two fragments, working in logs so that growth-rate
algebra is linear; solve_ivp integrates the levels and recovers the balanced-growth rates, the
elasticity of output with respect to s and the exact speeds of the stock-output ratios.
"""
import math

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp


def chk(name, value, expected, tol=1e-6):
    assert abs(value - expected) <= tol * max(1, abs(expected)), f"{name}: {value} != {expected}"
    print(f"{name:<60} {value:.6f}")


def zero(expr):
    return sp.simplify(expr) == 0


def log_stock(ln_inv, delta, T=600.0):
    """ln X(t) for X' = exp(ln_inv(t, ln X)) - delta X with X(0) = 1, as a function of t."""
    sol = solve_ivp(lambda t, x: np.exp(ln_inv(t, x) - x) - delta, (0.0, T), [0.0],
                    method="DOP853", rtol=1e-12, atol=1e-12, dense_output=True).sol
    return lambda t: float(sol(t)[0])


def bgp_rate(ln_x, T=600.0):
    """Growth rate of exp(ln_x) over the last year of the run, when the path is on its BGP."""
    return ln_x(T) - ln_x(T - 1.0)


# ================================================================== Romer 1.12, symbolic
al, s, n, de, mu, t, z0, g = sp.symbols("alpha s n delta mu t z_0 g", positive=True)
lA, lK, lL, lJt = sp.symbols("lnA lnK lnL lnJtilde", real=True)
phi = al / (1 - al)
assert zero(phi * (1 - al) - al) and zero(1 + phi - 1 / (1 - al))
# (a) Y = (AK)^a L^(1-a), k = K/(A^phi L): y = k^a and Y/K = k^(a-1)
lnY = al * (lA + lK) + (1 - al) * lL
lnk = lK - phi * lA - lL
assert zero(lnY - phi * lA - lL - al * lnk)
assert zero(lnY - lK - (al - 1) * lnk)
# (b) Y = J^a L^(1-a), J = A Jtilde, j = Jtilde/(A^phi L): y = j^a and A Y/J = Y/Jtilde = j^(a-1)
lnYb = al * (lA + lJt) + (1 - al) * lL
lnj = lJt - phi * lA - lL
assert zero(lnYb - phi * lA - lL - al * lnj)
assert zero(lnYb - lJt - (al - 1) * lnj)
# break-even rates: g_k = g_K - phi mu - n;  g_j = g_J - mu - phi mu - n
ma = n + de + phi * mu
m = n + de + mu / (1 - al)
assert zero(n + de + mu + phi * mu - m) and zero(m - ma - mu)
# steady state, (c) elasticity, (d) eigenvalue and speed of y
j = sp.symbols("j", positive=True)
h = s * j**al - m * j
lnjs = (sp.log(s) - sp.log(m)) / (1 - al)                    # ln j* = ln (s/m)^(1/(1-a))
assert zero(sp.log(s) + al * lnjs - (sp.log(m) + lnjs))      # h(j*) = 0
assert zero(s * sp.diff(al * lnjs, s) - al / (1 - al))       # d ln y*/d ln s = a/(1-a)
at_ss = {s: m * j**(1 - al)}                                 # s j*^(a-1) = m
lam = (1 - al) * m
assert zero(sp.diff(h, j).subs(at_ss) + lam)                 # h'(j*) = -(1-a) m
assert zero(lam - ((1 - al) * (n + de) + mu))
ydot = al * j**(al - 1) * h                                  # y = j^a
assert zero((sp.diff(ydot, j) / sp.diff(j**al, j)).subs(at_ss) + lam)
# closed form for z = Jtilde/Y = j^(1-a)
z = s / m + (z0 - s / m) * sp.exp(-(1 - al) * m * t)
assert zero(sp.diff(z, t) - (1 - al) * (s - m * z))
assert zero((1 - al) * j**(-al) * h - (1 - al) * (s - m * j**(1 - al)))
# (e) basic Solow speed (1.31) under Cobb-Douglas, two normalizations
lam_S = lambda gg: (1 - al) * (n + gg + de)
assert zero(lam_S(phi * mu) - (1 - al) * ma)                 # g = phi mu: also the speed in (a)
assert zero(lam - lam_S(phi * mu) - (1 - al) * mu)
assert zero(lam - lam_S(mu) - al * mu)                       # g = mu (solution manual)
cal = {al: sp.Rational(1, 3), n: sp.Rational(1, 100), de: sp.Rational(3, 100),
       mu: sp.Rational(4, 100)}
lam_c, lam_S_c = float(lam.subs(cal)), float(lam_S(phi * mu).subs(cal))
chk("1.12(d) g_Y/L = phi mu, calibration", float((phi * mu).subs(cal)), 0.02)
chk("1.12(d) lambda, calibration", lam_c, 1 / 15)
chk("1.12(d) half-life (years)", math.log(2) / lam_c, 10.4, tol=5e-3)
chk("1.12(e) lambda_S with g = phi mu", lam_S_c, 0.04)
chk("1.12(e) half-life, basic Solow (years)", math.log(2) / lam_S_c, 17.3, tol=5e-3)

# ================================================================== Romer 1.12, numeric
a_, s_, n_, d_, mu_ = 1 / 3, 0.25, 0.01, 0.03, 0.04
ma_, m_ = n_ + d_ + a_ / (1 - a_) * mu_, n_ + d_ + mu_ / (1 - a_)
# (a) K' = s (AK)^a L^(1-a) - delta K with A = e^(mu t), L = e^(n t), K(0) = 1
lnY_a = lambda t, x: a_ * (mu_ * t + x) + (1 - a_) * n_ * t
lnK_ = log_stock(lambda t, x: math.log(s_) + lnY_a(t, x), d_)
chk("1.12(a) g_K on the BGP", bgp_rate(lnK_), n_ + a_ * mu_ / (1 - a_))
chk("1.12(a) g_Y on the BGP", bgp_rate(lambda t: lnY_a(t, lnK_(t))), n_ + a_ * mu_ / (1 - a_))
for tt in (10.0, 40.0):
    w = math.exp(lnK_(tt) - lnY_a(tt, lnK_(tt)))            # K/Y, = 1 at t = 0
    chk(f"1.12(a) K/Y gap decays at (1-a) m_a, t={tt:.0f}", (w - s_ / ma_) / (1 - s_ / ma_),
        math.exp(-(1 - a_) * ma_ * tt))
# (b) J' = s A Y - delta J with Y = J^a L^(1-a), J(0) = 1
lnY_b = lambda t, x: a_ * x + (1 - a_) * n_ * t
lnJ_ = log_stock(lambda t, x: math.log(s_) + mu_ * t + lnY_b(t, x), d_)
chk("1.12(b) g_J on the BGP", bgp_rate(lnJ_), n_ + mu_ / (1 - a_))
chk("1.12(b) g_Y on the BGP", bgp_rate(lambda t: lnY_b(t, lnJ_(t))), n_ + a_ * mu_ / (1 - a_))
for tt in (10.0, 40.0):
    zz = math.exp(lnJ_(tt) - mu_ * tt - lnY_b(tt, lnJ_(tt)))  # Jtilde/Y, = 1 at t = 0
    chk(f"1.12(b,d) Jtilde/Y gap decays at (1-a) m, t={tt:.0f}", (zz - s_ / m_) / (1 - s_ / m_),
        math.exp(-(1 - a_) * m_ * tt))
# (c) raise s by 1%: BGP output rises by a/(1-a) percent
lnJ2 = log_stock(lambda t, x: math.log(1.01 * s_) + mu_ * t + lnY_b(t, x), d_)
chk("1.12(c) elasticity of BGP output w.r.t. s",
    (lnY_b(600.0, lnJ2(600.0)) - lnY_b(600.0, lnJ_(600.0))) / math.log(1.01), a_ / (1 - a_))

# ================================================================== Romer 1.15, symbolic
be, ga, b = sp.symbols("beta gamma b", positive=True)
x = sp.symbols("x", real=True)                               # x = g_K
lab = 1 - al - be - ga


def g_Y(gK, gR, gT, gA, gL):                                 # (1.46)
    return al * gK + be * gR + ga * gT + lab * (gA + gL)


assert zero(g_Y(x, n, n, g, n) - (al * x + (1 - al) * n + lab * g))      # (1.47')
gYt = sp.solve(sp.Eq(x, g_Y(x, n, n, g, n)), x)[0]                       # impose g_K = g_Y
assert zero(gYt - (n + lab / (1 - al) * g))                              # (1.48')
assert zero(gYt - n - lab * g / (1 - al))                                # (1.50)
gY_r = sp.solve(sp.Eq(x, g_Y(x, -b, 0, g, n)), x)[0]                     # text: g_R=-b, g_T=0
assert zero(gY_r - (lab * (n + g) - be * b) / (1 - al))                  # (1.48)
assert zero(gY_r - n - (lab * g - be * b - (be + ga) * n) / (1 - al))    # (1.49)
assert zero((gYt - n) - (gY_r - n) - (be * b + (be + ga) * n) / (1 - al))  # (1.51)
# convergence: g_K = s z - delta with z = Y/K, so d g_K/dt = s z (g_Y - g_K)
zK = sp.symbols("z", positive=True)
gK = s * zK - de
assert zero(s * zK * (g_Y(gK, n, n, g, n) - gK) - (1 - al) * (gK + de) * (gYt - gK))
lam15 = (1 - al) * (n + de) + lab * g
assert zero(sp.diff((1 - al) * (x + de) * (gYt - x), x).subs(x, gYt) + lam15)
assert zero((1 - al) * (gYt + de) - lam15)                   # footnote 23: Y/K > 0 on the BGP
wK = sp.symbols("w", positive=True)                          # w = K/Y, g_K = s/w - delta
gKw = s / wK - de
assert zero(wK * (gKw - g_Y(gKw, n, n, g, n)) - (1 - al) * (s - (gYt + de) * wK))
# Solow in disguise: R^b T^c (AL)^(1-a-b-c) = (A~ L)^(1-a), A~ grows at g~ = (1.50)
lR, lT = sp.symbols("lnR lnT", real=True)
lnAt = (be * (lR - lL) + ga * (lT - lL) + lab * lA) / (1 - al)
assert zero(be * lR + ga * lT + lab * (lA + lL) - (1 - al) * (lnAt + lL))
gt = sum(sp.diff(lnAt, v) * r for v, r in ((lR, n), (lT, n), (lL, n), (lA, g)))
assert zero(gt - (gYt - n))
assert zero((1 - al) * (n + gt + de) - lam15)                # (1.31) with g~

# ================================================================== Romer 1.15, numeric
a_, b_, c_, s_, n_, g_, d_, bb_ = 0.3, 0.1, 0.1, 0.2, 0.01, 0.02, 0.05, 0.005
lab_ = 1 - a_ - b_ - c_
lnY_h = lambda t, x: a_ * x + (b_ + c_) * n_ * t + lab_ * (n_ + g_) * t  # R = T = L = e^(n t)
lnY_r = lambda t, x: a_ * x - b_ * bb_ * t + lab_ * (n_ + g_) * t        # R = e^(-b t), T = 1
lnK_h = log_stock(lambda t, x: math.log(s_) + lnY_h(t, x), d_)
lnK_r = log_stock(lambda t, x: math.log(s_) + lnY_r(t, x), d_)
g150 = bgp_rate(lambda t: lnY_h(t, lnK_h(t))) - n_
g149 = bgp_rate(lambda t: lnY_r(t, lnK_r(t))) - n_
chk("1.15 (1.50) g~_Y/L on the BGP", g150, lab_ * g_ / (1 - a_))
chk("1.15 (1.49) g_Y/L, actual economy", g149, (lab_ * g_ - b_ * bb_ - (b_ + c_) * n_) / (1 - a_))
chk("1.15 (1.51) drag", g150 - g149, (b_ * bb_ + (b_ + c_) * n_) / (1 - a_))
lam_ = (1 - a_) * (n_ + d_) + lab_ * g_
w_star = s_ / (n_ + lab_ * g_ / (1 - a_) + d_)              # K/Y on the BGP
for tt in (10.0, 40.0):
    w = math.exp(lnK_h(tt) - lnY_h(tt, lnK_h(tt)))          # K/Y, = 1 at t = 0
    chk(f"1.15 K/Y gap decays at lambda~, t={tt:.0f}", (w - w_star) / (1 - w_star),
        math.exp(-lam_ * tt))

print("all checks passed")
