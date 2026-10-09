"""Practice list B v4, Block 3a (Question 5, objective items): checks every closed form, sign,
limit, ordering and multiple-choice distractor printed in practice-L3-L4-block3a.tex.

Run from Listas/: python practice-L3-L4-check-b3a.py   (aborts on the first mismatch).
Closed forms are checked with sympy; signs and orderings at random admissible draws.
"""
import math
import random

import sympy as sp
from scipy.optimize import brentq

rng = random.Random(20261007)
DRAWS = 300


def zero(expr, name):
    """Assert that the sympy expression `expr` simplifies to zero; `name` labels a failure."""
    res = sp.simplify(expr)
    assert res == 0, f"{name}: residual {res}"


def differ(key, options, name, tol=1e-9):
    """Assert that each distractor value in `options` (label -> value) differs from `key`."""
    for label, val in options.items():
        assert abs(val - key) > tol, f"{name}: distractor {label} equals the key"


# ---------- (a) debt-financed transfer, share lam of households at the borrowing limit ----------
y1, y2, T, b, r, lam, beta, sig = sp.symbols("y1 y2 T b r lambda beta sigma", positive=True)
zero(y1 + T + (y2 - (1 + r) * T) / (1 + r) - (y1 + y2 / (1 + r)), "a: PV of resources")
zero(sp.diff(y1 + T + b, T) - 1, "a: constrained c1 = y1 + T + b")
zero(lam * T + (1 - lam) * 0 - lam * T, "a: aggregate = lam T")
# binding condition u'(c1) > beta(1+r) u'(c2) with CRRA u: the left side falls, the right rises in T
d_lhs = sp.lambdify((y1, T, b, sig), sp.diff((y1 + T + b) ** (-sig), T))
d_rhs = sp.lambdify((y2, T, b, r, beta, sig),
                    sp.diff(beta * (1 + r) * (y2 - (1 + r) * (T + b)) ** (-sig), T))


def c1_crra(y_1, y_2, tau1, tau2, r_, b_, beta_, sig_):
    """Period-1 consumption of a CRRA household whose savings satisfy a >= -b_.

    Returns (c1, binds): binds is True when the unconstrained optimum would borrow more than b_.
    """
    wealth = y_1 - tau1 + (y_2 - tau2) / (1 + r_)
    g = (beta_ * (1 + r_)) ** (1 / sig_)            # c2 / c1 from the Euler equation
    c1_free = wealth / (1 + g / (1 + r_))
    cap = y_1 - tau1 + b_                           # c1 when a = -b_
    return min(c1_free, cap), c1_free > cap


n = 0
while n < DRAWS:
    p = (rng.uniform(0, 0.1), rng.uniform(0, 0.3), rng.uniform(0.8, 0.99), rng.uniform(0.5, 4))
    T_, lam_ = rng.uniform(0.01, 0.2), rng.uniform(0.05, 0.95)
    yc = (rng.uniform(0.1, 0.6), rng.uniform(1.5, 3.0))     # constrained type: poor now
    yu = (rng.uniform(1.0, 2.0), rng.uniform(0.3, 1.0))     # unconstrained type
    tax = (-T_, (1 + p[0]) * T_)                            # transfer now, (1+r)T of taxes later
    c_b, bind_cb = c1_crra(*yc, 0, 0, *p)
    c_a, bind_ca = c1_crra(*yc, *tax, *p)
    u_b, bind_ub = c1_crra(*yu, 0, 0, *p)
    u_a, bind_ua = c1_crra(*yu, *tax, *p)
    if not (bind_cb and bind_ca and not bind_ub and not bind_ua):
        continue
    assert abs(u_a - u_b) < 1e-12, "a: unconstrained c1 moved"
    assert abs(c_a - c_b - T_) < 1e-12, "a: constrained c1 did not rise by T"
    key = lam_ * T_
    assert abs(lam_ * (c_a - c_b) + (1 - lam_) * (u_a - u_b) - key) < 1e-12, "a: aggregate"
    differ(key, {"A": T_, "B": (1 - lam_) * T_, "C": 0.0}, "a")
    assert d_lhs(yc[0], T_, p[1], p[3]) < 0 < d_rhs(yc[1], T_, p[1], p[0], p[2], p[3]), "a: slopes"
    n += 1

# ---------- (b) Jones-Klenow consumption equivalent with ln c - theta h^2 ----------
c0, c1, h0, h1, th, Lam = sp.symbols("c0 c1 h0 h1 theta Lambda", positive=True)
sol = sp.solve(sp.Eq(sp.log(Lam * c0) - th * h0**2, sp.log(c1) - th * h1**2), Lam)
assert len(sol) == 1, "b: Lambda not unique"
key_b = sp.log(c1 / c0) + th * (h0**2 - h1**2)
zero(sp.expand_log(sp.log(sol[0]) - key_b, force=True), "b: ln Lambda")
dist_b = {"A": sp.log(c1 / c0), "C": sp.log(c1 / c0) + th * (h0 - h1),     # key is B
          "D": sp.log(c1 / c0) - th * (h0 - h1)}                            # levels and the sign flipped
syms_b = (c0, c1, h0, h1, th)
f_key = sp.lambdify(syms_b, key_b)
f_dist = {k: sp.lambdify(syms_b, v) for k, v in dist_b.items()}
for _ in range(DRAWS):
    x = (rng.uniform(0.5, 2), rng.uniform(0.5, 2), rng.uniform(0.05, 0.95),
         rng.uniform(0.05, 0.95), rng.uniform(0.1, 5))
    kv = f_key(*x)
    differ(kv, {k: f(*x) for k, f in f_dist.items()}, "b")
    assert (kv < math.log(x[1] / x[0])) == (x[3] > x[2]), "b: Lambda < c1/c0 iff h1 > h0"
# general CRRA: Lambda^(1-sigma) = (c1/c0)^(1-sigma) + (1-sigma) theta (h0^2 - h1^2) c0^(sigma-1)
X = (c1 / c0) ** (1 - sig) + (1 - sig) * th * (h0**2 - h1**2) * c0 ** (sig - 1)
resid = X * c0 ** (1 - sig) - c1 ** (1 - sig) - (1 - sig) * th * (h0**2 - h1**2)  # (1-sig) x welfare gap
zero(sp.powsimp(sp.expand_power_base(sp.expand(resid), force=True), force=True), "b: CRRA Lambda")
lim = sp.limit(sp.log(X) / (1 - sig), sig, 1)
zero(sp.expand_log(lim - key_b, force=True), "b: limit sigma -> 1")

# ---------- (c) news of a permanent future wage rise, separable ln c - v(h) ----------
eta, w, k, psi, eps = sp.symbols("eta w k psi epsilon", positive=True)
h_t = (eta * w * k / psi) ** eps                  # v(h) = psi h^(1+1/eps)/(1+1/eps), k = [beta(1+r)]^-t
zero(sp.powsimp(psi * h_t ** (1 / eps), force=True) - eta * w * k, "c: FOC v'(h) = eta w k")
zero(sp.diff(w * h_t, w) - (1 + eps) * h_t, "c: d(w h)/dw = (1+eps) h > 0")
zero(sp.diff(h_t, eta) - eps * h_t / eta, "c: dh/deta = eps h/eta > 0")


def labor_plan(w_path, a0, beta_, r_, psi_, eps_):
    """Solve max sum beta^t [ln c_t - v(h_t)] s.t. the lifetime budget; return (h_0, c_0)."""
    def phi(x):                                   # budget surplus at eta = exp(x); increasing in x
        e = math.exp(x)
        tot = a0
        for t, wt in enumerate(w_path):
            kt = (beta_ * (1 + r_)) ** (-t)
            tot += (wt * (e * wt * kt / psi_) ** eps_ - 1 / (e * kt)) / (1 + r_) ** t
        return tot
    e = math.exp(brentq(phi, -60, 60, xtol=1e-14))
    return (e * w_path[0] / psi_) ** eps_, 1 / e


for _ in range(DRAWS):
    N = rng.randint(1, 6)
    wp = [rng.uniform(0.5, 2) for _ in range(N + 1)]
    q_ = (rng.uniform(-0.3, 1), rng.uniform(0.85, 0.99), rng.uniform(0, 0.1),
          rng.uniform(0.5, 3), rng.uniform(0.2, 2))
    g = rng.uniform(0.02, 0.5)
    h_old, c_old = labor_plan(wp, *q_)
    h_new, c_new = labor_plan([wp[0]] + [wt * (1 + g) for wt in wp[1:]], *q_)
    assert h_new < h_old and c_new > c_old, "c: h0 must fall and c0 rise"

# ---------- (d) search: benefits and tightness ----------
wg, VE, VU, VF, z, y, kap, s, q, tht, phg = sp.symbols(
    "w V_E V_U V_F z y kappa s q theta phi", positive=True)
asset = [r * VE - (wg + s * (VU - VE)), r * VU - (z + tht * q * (VE - VU))]
s0 = sp.solve(asset + [VE - VU], [wg, VE, VU], dict=True)
assert len(s0) == 1, "d: phi = 0 system"
zero(s0[0][wg] - z, "d: w = z at phi = 0")
vf = sp.solve(r * VF - (y - z - s * VF), VF)[0]
zero(q * vf - (y - z) * q / (r + s), "d: free entry (y-z) q/(r+s) = kappa")
sg = sp.solve(asset + [(1 - phg) * (VE - VU) - phg * VF], [wg, VE, VU], dict=True)[0]
w_fe = sg[wg].subs(VF, kap / q)                  # wage with free entry V_F = kappa/q
jc = (r * VF - (y - w_fe - s * VF)).subs(VF, kap / q)
zero(jc * (1 - phg) * q - (kap * (r + s + phg * tht * q) - (1 - phg) * (y - z) * q), "d: job creation")
zero((1 - phg) * (y - z) * q - kap * (r + s + phg * tht * q)
     - q * ((1 - phg) * (y - z) - kap * ((r + s) / q + phg * tht)), "d: JC divided by q")
Q = sp.Function("q")
F = (y - z) * Q(tht) - kap * (r + s)
zero(-sp.diff(F, z) / sp.diff(F, tht) - Q(tht) / ((y - z) * sp.diff(Q(tht), tht)), "d: dtheta/dz")
S, Am, xi = sp.symbols("S A_m xi", positive=True)    # S = y - z > 0; q = A_m theta^(-xi) as in Q3(b)
th_cf = (Am * S / (kap * (r + s))) ** (1 / xi)
zero(S * Am * th_cf ** (-xi) - kap * (r + s), "d: closed-form theta, q = A_m theta^(-xi)")
zero(sp.diff(sp.expand_log(sp.log(th_cf.subs(S, y - z)), force=True), z)
     + 1 / (xi * (y - z)), "d: dln theta/dz")


def theta_eq(y_, z_, kap_, r_, s_, am_, xi_, ph_):
    """Steady-state tightness from (1-phi)(y-z) = kappa[(r+s) theta^xi/A_m + phi theta]."""
    G = lambda t: (1 - ph_) * (y_ - z_) - kap_ * ((r_ + s_) * t ** xi_ / am_ + ph_ * t)
    hi = 1.0
    while G(hi) > 0:
        hi *= 2
    return brentq(G, 1e-300, hi, xtol=1e-300, rtol=1e-14)


for i in range(DRAWS):
    y_ = rng.uniform(0.5, 2)
    par = (y_, rng.uniform(0, 0.95 * y_), rng.uniform(0.01, 1), rng.uniform(0, 0.1),
           rng.uniform(0.01, 0.5), rng.uniform(0.2, 2), rng.uniform(0.1, 0.9))
    ph_ = 0.0 if i % 3 == 0 else rng.uniform(0, 0.95)
    t0 = theta_eq(*par, ph_)
    dz = 1e-4 * (par[0] - par[1])
    t1 = theta_eq(par[0], par[1] + dz, *par[2:], ph_)
    assert t1 < t0, "d: theta must fall with z"
    # unemployment s/(s+f) rises iff f = A_m theta^(1-xi) falls (compared on f: u can round to 1)
    assert par[5] * t1 ** (1 - par[6]) < par[5] * t0 ** (1 - par[6]), "d: job finding must fall with z"
    if ph_ == 0.0:
        cf = (par[5] * (par[0] - par[1]) / (par[2] * (par[3] + par[4]))) ** (1 / par[6])
        assert abs(t0 / cf - 1) < 1e-9, "d: root vs closed form"

print("practice-L3-L4-check-b3a: all checks passed")
