"""Practice list C v4, Block 3, Question 5 (objective items a-d): verifies every closed form with sympy,
every claimed sign, limit and ordering at random admissible draws, and that each multiple-choice distractor
differs from the key. Aborts on the first mismatch.

Run from Listas/: python practice-L5-L6-check-b3a.py  (also run by practice-L5-L6-check.py)
"""
import math
import random

import sympy as sp

random.seed(20261007)
N = 400  # random admissible draws per sign / distractor check

sig, beta, a, kappa, r, mu, pis, c, P = sp.symbols("sigma beta a kappa r mu pi_star c P", positive=True)
G = sp.symbols("G", positive=True)  # G = 1+g > 0
i, x, R, I = sp.symbols("i x R I", real=True)


def zero(expr, what):
    assert sp.simplify(expr) == 0, f"{what}: residual {sp.simplify(expr)}"


def draw():
    """One admissible draw (the ranges of Question 6): sigma>0, 0<beta<1, g>=0, beta(1+g)^(1-sigma)<1,
    a, kappa, r > 0, pi*>0, and mu above the Friedman bound 1+mu = beta(1+g)^(1-sigma), so i >= 0."""
    while True:
        d = {sig: random.uniform(0.1, 6), beta: random.uniform(0.3, 0.999), G: random.uniform(1.0, 1.15),
             a: random.uniform(0.05, 20), kappa: random.uniform(0.01, 2), r: random.uniform(1e-3, 0.5),
             pis: random.uniform(1e-3, 2)}
        lo = d[beta] * d[G] ** (1 - d[sig])
        if lo < 1:
            d[mu] = random.uniform(lo - 1, lo + 2)
            return d


def num(expr, d):
    return float(expr.subs(d))


# ---------------------------------------------------------------- a) GE x money (sigma = 1, inflation target)
euler = sp.solve(sp.Eq(c ** -sig, beta * (1 + R) * (G * c) ** -sig), R)
assert len(euler) == 1
one_r = 1 + euler[0]
zero(one_r - G ** sig / beta, "a) Euler + goods clearing: 1+r = (1+g)^sigma/beta")
zero(one_r.subs(sig, 1) - G / beta, "a) log case: 1+r = (1+g)/beta")
# Fisher from the two bond FOCs: real one gives beta*(c_{t+1}/c_t)^-sigma = 1/(1+r); nominal one adds P_t/P_{t+1}.
ratio = 1 / one_r  # beta * u'(c_{t+1})/u'(c_t)
Pn = P * (1 + pis)  # P_{t+1}
fisher = sp.solve(sp.Eq(c ** -sig / P, (1 + I) * ratio * c ** -sig / Pn), I)
zero(1 + fisher[0] - one_r * (1 + pis), "a) exact Fisher from the bond FOCs")
key_a = (G * (1 + pis) / beta - 1)
zero(one_r.subs(sig, 1) * (1 + pis) - 1 - key_a, "a) key i = (1+g)(1+pi*)/beta - 1")
# money growth that delivers the target at constant i: M = kappa e^{-ai} P Y
M_t = kappa * sp.exp(-a * x) * P * c
M_t1 = kappa * sp.exp(-a * x) * Pn * (G * c)
zero(M_t1 / M_t - G * (1 + pis), "a) M grows at (1+g)(1+pi*) - 1")
opts_a = {"A": key_a, "B": beta * (1 + pis) - 1, "C": (1 + pis) / beta - 1, "D": beta * G * (1 + pis) - 1}
zero(opts_a["C"] - key_a.subs(G, 1), "a) C = key with g = 0 (no-growth real rate)")
inv = sp.solve(sp.Eq(beta / c, (1 + R) / (G * c)), R)  # beta u'(c_t) = (1+r) u'(c_{t+1}), log utility
zero(opts_a["D"] - ((1 + inv[0]) * (1 + pis) - 1), "a) D = inverted discount factor")
zero(opts_a["B"] - ((1 + inv[0]).subs(G, 1) * (1 + pis) - 1), "a) B = no growth and inverted discount factor")
for _ in range(N):
    d = draw()
    k = num(key_a, d)
    for L in "BCD":
        assert abs(num(opts_a[L], d) - k) > 1e-9, f"a) distractor {L} equals the key at {d}"

# ---------------------------------------------------------------- b) seigniorage x interest rates (g = 0)
pi_b = sp.solve(sp.Eq(1 + mu, (1 + x) * 1), x)[0]  # constant M/(PY), Y constant: 1+mu = (1+pi)(1+g), g = 0
zero(pi_b - mu, "b) pi = mu when g = 0")
zero(one_r.subs(G, 1) - 1 / beta, "b) 1+r = 1/beta when g = 0")
i_b = (1 + r) * (1 + mu) - 1
zero(sp.diff(i_b, mu) - (1 + r), "b) di/dmu = 1+r")
M0 = sp.symbols("M0", positive=True)
zero(((1 + mu) * M0 - M0) / P / (M0 / (P * kappa * sp.exp(-a * i_b))) - mu * kappa * sp.exp(-a * i_b),
     "b) S/Y = mu * kappa e^{-ai}")
S = mu * kappa * sp.exp(-a * i_b)
lnS = sp.log(mu) + sp.log(kappa) - a * i_b
zero(sp.expand_log(sp.log(S), force=True) - lnS, "b) ln(S/Y)")
foc = sp.diff(lnS, mu)
zero(foc - (1 / mu - a * (1 + r)), "b) FOC")
roots = sp.solve(foc, mu)
mu_star = 1 / (a * (1 + r))
assert len(roots) == 1, roots
zero(roots[0] - mu_star, "b) mu* = 1/(a(1+r))")
zero(sp.diff(lnS, mu, 2) + 1 / mu ** 2, "b) SOC: d2 lnS/dmu2 = -1/mu^2")
zero(sp.diff(S, mu, 2).subs(mu, mu_star) + S.subs(mu, mu_star) / mu_star ** 2, "b) S''(mu*) = -S/mu*^2")
assert sp.limit(S, mu, 0, "+") == 0 and sp.limit(S, mu, sp.oo) == 0, "b) Laffer limits"
zero(mu * sp.diff(sp.log(kappa * sp.exp(-a * i_b)), mu) + a * (1 + r) * mu, "b) base elasticity -a(1+r)mu")
zero((mu * sp.diff(sp.log(kappa * sp.exp(-a * i_b)), mu)).subs(mu, mu_star) + 1, "b) unit elasticity at mu*")
approx = sp.solve(sp.diff(sp.log(mu) - a * (r + mu), mu), mu)
opts_b = {"A": 1 / a, "B": mu_star, "C": 1 / a - r, "D": mu_star - r}
zero(approx[0] - opts_b["A"], "b) A from the approximate Fisher equation")
zero(opts_b["A"] / mu_star - (1 + r), "b) A overstates mu* by the factor 1+r")
zero(opts_b["D"] - (roots[0] - r), "b) D = the key's root minus r")
zero(opts_b["C"] - (approx[0] - r), "b) C = both mistakes: the approximate-Fisher root minus r")
S_f = sp.lambdify((mu, a, kappa, r), S, "math")
for _ in range(N):
    d = draw()
    k = num(mu_star, d)
    assert k > 0
    for L in "ACD":
        assert abs(num(opts_b[L], d) - k) > 1e-9, f"b) distractor {L} equals the key at {d}"
    s_star = S_f(k, d[a], d[kappa], d[r])
    for m in (k * f for f in (0.01, 0.2, 0.5, 0.9, 0.99, 1.01, 1.1, 2, 5, 50)):
        assert S_f(m, d[a], d[kappa], d[r]) < s_star, "b) mu* is not the global maximum"

# ---------------------------------------------------------------- c) GE x money x welfare
assert sp.diff(one_r, mu) == 0, "c) r does not depend on mu"
pi_c = sp.solve(sp.Eq(1 + mu, (1 + x) * G), x)[0]  # constant M/(PY): 1+mu = (1+pi)(1+g)
one_i = sp.powsimp(one_r * (1 + pi_c))
zero(sp.powsimp(one_i - G ** (sig - 1) * (1 + mu) / beta, force=True), "c) 1+i = (1+g)^(sigma-1)(1+mu)/beta")
di_dmu = sp.diff(one_i, mu)
zero(sp.powsimp(di_dmu - G ** (sig - 1) / beta, force=True), "c) di/dmu")
m_mu = kappa * sp.exp(-a * (one_i - 1))
zero(sp.diff(m_mu, mu) + a * m_mu * di_dmu, "c) dm/dmu = -a m di/dmu")
m_x = kappa * sp.exp(-a * x)
W = sp.integrate(m_x, (x, 0, i)) - i * m_x.subs(x, i)
W_closed = kappa / a * (1 - (1 + a * i) * sp.exp(-a * i))
zero(W - W_closed, "c) Bailey area closed form")
zero(sp.diff(W_closed, i) - a * kappa * i * sp.exp(-a * i), "c) W'(i)")
zero(sp.diff(W_closed, i) + i * sp.diff(m_x, x).subs(x, i), "c) W'(i) = -i m'(i)")
assert W_closed.subs(i, 0) == 0, "c) W(0) = 0"
fr = sp.solve(sp.Eq(G ** (sig - 1) * (1 + mu) / beta, 1), mu)
zero(sp.powsimp(fr[0] - (beta * G ** (1 - sig) - 1), force=True), "c) Friedman rule 1+mu = beta(1+g)^(1-sigma)")
checked = 0
while checked < N:
    d = draw()
    if num(one_i, d) <= 1:  # drawn mu keeps i >= 0; W > 0 needs i > 0 (i = 0 is the Friedman rule)
        continue
    checked += 1
    assert num(di_dmu, d) > 0, "c) di/dmu > 0"
    assert num(sp.diff(m_mu, mu), d) < 0, "c) dm/dmu < 0"
    iv = num(one_i, d) - 1
    assert num(W_closed, {**d, i: iv}) > 0 and num(sp.diff(W_closed, i), {**d, i: iv}) > 0, "c) W > 0, W' > 0"
    assert math.exp(d[a] * iv) > 1 + d[a] * iv, "c) e^{ai} > 1 + ai"

# ---------------------------------------------------------------- d) growth x money
lnG = sp.symbols("lnG", real=True)
el = lambda e: sp.simplify(sp.diff(sp.expand_log(sp.log(e.subs(G, sp.exp(lnG))), force=True), lnG))
zero(el(one_i) - (sig - 1), "d) d ln(1+i)/d ln(1+g) = sigma - 1")
zero(el(one_r) - sig, "d) real-rate channel: +sigma")
zero(el(1 + pi_c) + 1, "d) inflation channel: -1")
zero(el(one_r * (1 + pis)) - sig, "d) inflation targeting: elasticity sigma")
zero(sp.diff(one_i.subs(sig, 1), G), "d) log case: i independent of g")
di_dG = sp.diff(one_i, G)
for _ in range(N):
    d = draw()
    s = d[sig]
    v = num(di_dG, d)
    assert (v > 0) == (s > 1) and (v < 0) == (s < 1), f"d) sign of di/dg at sigma={s}"
    assert num(sp.diff(1 + pi_c, G), d) < 0 and num(sp.diff(one_r, G), d) > 0, "d) channel signs"
    assert num(sp.diff(one_r * (1 + pis), G), d) > 0, "d) inflation targeting: i rises with g"

print("practice-L5-L6-check-b3a.py: all checks passed")
