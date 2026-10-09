"""Block 1 of practice-L3-L4 (symbolic): checks every result of practice-L3-L4-block1.tex.

Q1: finite-horizon CRRA share, endowment-economy rate, kinked budget set, binding
borrowing limit. Q2: present bias with CRRA (plans, Jensen ordering, value of
commitment x and its expansion, equilibrium rates with sophisticated and naive
households, parameter signs and limits). Closed forms with sympy; signs, orderings
and existence claims at random admissible draws; brute-force optimization as an
independent path. Run from Listas/: python practice-L3-L4-check-b1.py
"""
import mpmath as mp
import numpy as np
import sympy as sp
from scipy.optimize import brentq, minimize, minimize_scalar

rng = np.random.default_rng(20261007)
N = 200
mp.mp.dps = 50
be, s, r, gam, T, g, y1 = sp.symbols("beta sigma r gamma T g y1", positive=True)
om, W, c, d, e, b1 = sp.symbols("omega W c delta epsilon b1", positive=True)
HALF = sp.Rational(1, 2)


def u(x, sg):
    """CRRA utility of consumption x (log at sg == 1); works on floats and mpf."""
    if sg == 1:
        return mp.log(x) if isinstance(x, mp.mpf) else np.log(x)
    return x ** (1 - sg) / (1 - sg)


def argmax(f, lo, hi):
    """Maximizer of the scalar function f on (lo, hi)."""
    return minimize_scalar(lambda z: -f(z), bounds=(lo, hi), method="bounded",
                           options={"xatol": 1e-13}).x


def sig():
    """Random admissible sigma, log-uniform on (0.15, 8), away from 1."""
    while True:
        v = float(np.exp(rng.uniform(np.log(0.15), np.log(8.0))))
        if abs(v - 1) > 0.03:
            return v


def logzero(a, b):
    """True if log(a) - log(b) simplifies to 0 (positive symbols, logs expanded)."""
    return sp.simplify(sp.expand_log(sp.log(a) - sp.log(b), force=True)) == 0


def zero(expr):
    """True if expr simplifies to 0 for positive symbols (power bases expanded)."""
    expr = sp.powsimp(sp.expand_power_base(expr, force=True), force=True)
    return sp.simplify(expr) == 0


# ---------------- Q1(a): finite-horizon share c0/W ----------------
t = sp.Symbol("t", integer=True, nonnegative=True)
geo = sp.summation(gam ** t, (t, 0, T))
geo = geo.args[-1][0] if isinstance(geo, sp.Piecewise) else geo
assert sp.simplify(geo - (1 - gam ** (T + 1)) / (1 - gam)) == 0, "Q1a geometric sum"
assert sp.simplify(sp.limit((1 - gam) / (1 - gam ** (T + 1)), gam, 1) - 1 / (T + 1)) == 0
g_key = be ** (1 / s) * (1 + r) ** (1 / s - 1)
assert logzero((be * (1 + r)) ** (1 / s) / (1 + r), g_key), "Q1a gamma"
assert sp.simplify(g_key.subs(s, 1) - be) == 0, "Q1a: C = key B at sigma = 1"
assert logzero(g_key.subs(r, 1 / be - 1), be), "Q1a: C = key B when beta(1+r) = 1"
assert logzero(g_key.subs(s, 1 / s), be ** s * (1 + r) ** (s - 1)), "Q1a: A = key with sigma for 1/sigma"
assert logzero(((be * (1 + r)) ** (1 / s)).subs(s, 1 / s), (be * (1 + r)) ** s), \
    "Q1a: D = gamma without budget discounting, and sigma for 1/sigma"
share = lambda gm, n: (1 - gm) / (1 - gm ** (n + 1))
for i in range(N):
    sg, bt, rr, n = sig(), rng.uniform(0.3, 0.99), rng.uniform(0.001, 0.3), int(rng.integers(1, 61))
    gk = bt ** (1 / sg) * (1 + rr) ** (1 / sg - 1)
    c0 = share(gk, n)
    path = c0 * (bt * (1 + rr)) ** (np.arange(n + 1) / sg)
    assert abs(np.sum(path / (1 + rr) ** np.arange(n + 1)) - 1) < 1e-9, "Q1a budget"
    assert np.allclose(path[:-1] ** -sg, bt * (1 + rr) * path[1:] ** -sg, rtol=1e-9)
    for gd in (bt ** sg * (1 + rr) ** (sg - 1), bt, (bt * (1 + rr)) ** sg):     # A, C, D
        assert abs(share(gd, n) / c0 - 1) > 1e-6, "Q1a distractor equals key"
    if i < 40:                                   # brute force, short horizons
        sgb, nb = rng.uniform(0.4, 3.0), int(rng.integers(1, 4))
        disc = (1 + rr) ** -np.arange(nb + 1)
        obj = lambda cv: -np.sum(bt ** np.arange(nb + 1) * u(cv, sgb))
        res = minimize(obj, np.full(nb + 1, 1 / disc.sum()), method="SLSQP",
                       bounds=[(1e-9, None)] * (nb + 1),
                       constraints={"type": "eq", "fun": lambda cv: cv @ disc - 1},
                       options={"ftol": 1e-15, "maxiter": 1000})
        gb = bt ** (1 / sgb) * (1 + rr) ** (1 / sgb - 1)
        assert res.success and abs(res.x[0] - share(gb, nb)) < 1e-5, "Q1a brute force"

# ---------------- Q1(b): endowment-economy rate ----------------
r_key = (1 + g) ** s / be - 1
assert logzero(y1 ** -s, be * (1 + r_key) * ((1 + g) * y1) ** -s), "Q1b Euler at c_t = y_t"
assert sp.simplify(r_key.subs(s, 1) - ((1 + g) / be - 1)) == 0, "Q1b: A = key D at sigma = 1"
assert sp.simplify(r_key.subs(g, 0) - (1 / be - 1)) == 0, "Q1b: B = key D at g = 0"
assert sp.simplify(r_key.subs({s: 1 / s, be: 1}) - ((1 + g) ** (1 / s) - 1)) == 0, \
    "Q1b: C = key with sigma for 1/sigma and beta = 1"
for _ in range(N):
    sg, bt, gg, ya = sig(), rng.uniform(0.3, 0.99), rng.uniform(0.01, 0.5), rng.uniform(0.5, 2)
    rk = (1 + gg) ** sg / bt - 1
    a = argmax(lambda z: u(ya - z, sg) + bt * u((1 + gg) * ya + (1 + rk) * z, sg),
               -0.9 * (1 + gg) * ya / (1 + rk), 0.9 * ya)
    assert abs(a) < 1e-6 * ya, "Q1b: zero saving at the key rate"
    for rd in ((1 + gg) / bt - 1, 1 / bt - 1, (1 + gg) ** (1 / sg) - 1):        # A, B, C
        assert abs(rd - rk) > 1e-9, "Q1b distractor equals key"


# ---------------- Q1(c): kinked budget set (False) ----------------
def kinked_saving(ya, yb, bt, sg, rs, rb):
    """Optimal saving (borrowing if < 0) with deposit rate rs and loan rate rb."""
    f_s = lambda z: u(ya - z, sg) + bt * u(yb + (1 + rs) * z, sg)
    f_b = lambda z: u(ya - z, sg) + bt * u(yb + (1 + rb) * z, sg)
    a_s, a_b = argmax(f_s, 0, ya * (1 - 1e-9)), argmax(f_b, -yb / (1 + rb) * (1 - 1e-9), 0)
    return a_s if f_s(a_s) >= f_b(a_b) else a_b


for _ in range(N):
    sg, bt, ya, yb = sig(), rng.uniform(0.5, 0.99), rng.uniform(0.5, 2), rng.uniform(0.5, 2)
    m = ya ** -sg / (bt * yb ** -sg)
    rs, rb = m * rng.uniform(0.5, 0.98) - 1, m * rng.uniform(1.02, 1.5) - 1
    fs = lambda z: u(ya - z, sg) + bt * u(yb + (1 + rs) * z, sg)
    h = 1e-6                                     # f'(0) = beta u'(y2)(1 + rs - m)
    fp = (fs(h) - fs(-h)) / (2 * h)
    assert abs(fp - bt * yb ** -sg * (1 + rs - m)) < 1e-6 * (1 + ya ** -sg), "Q1c f'(0)"
    assert fp < 0 and abs(kinked_saving(ya, yb, bt, sg, rs, rb)) < 1e-6, "Q1c kink"
    small = rs + rng.uniform(0.05, 0.95) * (m - 1 - rs)
    assert abs(kinked_saving(ya, yb, bt, sg, small, rb)) < 1e-6, "Q1c small rise"
    big = m * rng.uniform(1.02, 1.3) - 1
    assert kinked_saving(ya, yb, bt, sg, big, max(rb, big + 0.1)) > 1e-6, "Q1c big rise"

# ---------------- Q1(d): binding limit, debt-financed tax cut (False) ----------------
for _ in range(N):
    sg, bt, rr = sig(), rng.uniform(0.5, 0.99), rng.uniform(0.0, 0.2)
    ya, yb, ta, tb = rng.uniform(0.2, 0.6), rng.uniform(1.5, 3), rng.uniform(0, 0.1), rng.uniform(0, 0.3)
    pv = ya - ta + (yb - tb) / (1 + rr)
    c1u = pv / (1 + bt ** (1 / sg) * (1 + rr) ** (1 / sg - 1))   # unconstrained c1; the cut leaves pv alone
    assert c1u > ya - ta
    bb = rng.uniform(0.05, 0.9) * (c1u - ya + ta)                  # the limit binds before the cut
    dbar = c1u - (ya - ta + bb)
    for dl in (rng.uniform(0.05, 0.95) * dbar, rng.uniform(1.05, 3) * dbar):   # below, then above Delta_bar
        c1 = []
        for t1, t2 in ((ta, tb), (ta - dl, tb + (1 + rr) * dl)):
            lo = max(-bb, -(yb - t2) / (1 + rr) * (1 - 1e-9))      # keeps c2 > 0 on the search interval
            a = argmax(lambda z: u(ya - t1 - z, sg) + bt * u(yb - t2 + (1 + rr) * z, sg), lo, ya - t1 - 1e-9)
            c1.append(ya - t1 - a)
        assert abs(c1[0] - (ya - ta + bb)) < 1e-6, "Q1d limit binds before the cut"
        assert abs(c1[1] - c1[0] - min(dl, dbar)) < 1e-6, "Q1d dc1 = min(Delta, Delta_bar)"
    assert dl - (c1[1] - c1[0]) > 0.04 * dbar, "Q1d False: a cut above Delta_bar is partly saved"


# ---------------- Q2 closed forms ----------------
def plans(bt, sg, w0=1.0):
    """Commitment, naive and sophisticated plans (c0, c1, c2) at r = 0."""
    o = bt ** (1 / sg)
    lam = (1 + o) ** (1 - 1 / sg) * (bt + o) ** (1 / sg)
    com = tuple(w0 / (1 + 2 * o) * v for v in (1, o, o))
    w1 = 2 * o * w0 / (1 + 2 * o)
    nai = (com[0], w1 / (1 + o), o * w1 / (1 + o))
    w1 = lam * w0 / (1 + lam)
    sop = (w0 / (1 + lam), w1 / (1 + o), o * w1 / (1 + o))
    return com, nai, sop, lam, o


def U0(p, bt, sg):
    """Self 0's utility of plan p."""
    return u(p[0], sg) + bt * (u(p[1], sg) + u(p[2], sg))


def x_gen(bt, sg):
    """Value of commitment, closed form for sigma != 1 (floats or mpf)."""
    o = bt ** (1 / sg)
    lam = (1 + o) ** (1 - 1 / sg) * (bt + o) ** (1 / sg)
    return 1 - ((1 + lam) / (1 + 2 * o)) ** (sg / (1 - sg))


x_log = lambda bt: 1 - (4 * bt / (1 + bt) ** 2) ** (bt / (1 + 2 * bt))
A = lambda z, sg: z ** (1 - sg) + (1 - z) ** (1 - sg)

# Q2(a): FOCs and the Lambda identity, symbolically (beta = omega^sigma)
assert zero(c ** -s - om ** s * (om * c) ** -s), "Q2a self 1 / commitment FOC"
kk = 1 / (1 + om)
assert zero(om ** s * A(kk, s) - (1 + om) ** (s - 1) * (om ** s + om)), "Q2a Lambda"
lam_s = (1 + om) ** (1 - 1 / s) * (om ** s + om) ** (1 / s)
assert zero(om ** s * A(kk, s) * (lam_s * W / (1 + lam_s)) ** -s - (W / (1 + lam_s)) ** -s)
assert sp.simplify(lam_s.subs(s, 1) - 2 * om) == 0, "Q2a log: Lambda = 2 beta"
w1n = W - W / (1 + 2 * om)
assert sp.simplify(w1n - 2 * om * W / (1 + 2 * om)) == 0, "Q2a naive W1"
assert sp.simplify((w1n / (1 + om)) / (om * W / (1 + 2 * om)) - 2 / (1 + om)) == 0
assert sp.simplify((om * w1n / (1 + om)) / (om * W / (1 + 2 * om)) - 2 * om / (1 + om)) == 0
for _ in range(N):
    sg, bt = sig(), rng.uniform(0.05, 0.98)
    com, nai, sop, lam, o = plans(bt, sg)
    k1 = argmax(lambda z: u(z, sg) + bt * u(1 - z, sg), 1e-12, 1 - 1e-12)
    assert abs(k1 - 1 / (1 + o)) < 1e-6 and 0.5 < k1 < 1, "Q2a self 1 share"
    c0b = argmax(lambda z: u(z, sg) + bt * (u(k1 * (1 - z), sg) + u((1 - k1) * (1 - z), sg)),
                 1e-12, 1 - 1e-12)
    assert abs(c0b - sop[0]) < 1e-6, "Q2a sophisticated c0 (brute force)"
    assert abs((bt * A(1 / (1 + o), sg)) ** (1 / sg) - lam) < 1e-9 * lam, "Q2a Lambda"
    assert abs(sum(sop) - 1) < 1e-12 and abs(sum(nai) - 1) < 1e-12
    assert nai[1] > com[1] and nai[2] < com[2], "Q2a plan revision"
    # Q2(b): ordering and the effective return
    assert (sop[0] < nai[0]) == (sg > 1) and abs(sop[0] - nai[0]) > 1e-12, "Q2b ordering"
    assert (A(1 / (1 + o), sg) > 2 ** sg) == (sg > 1), "Q2b Jensen"
    R = (A(1 / (1 + o), sg) / 2 ** sg) ** (1 / (1 - sg))
    assert R < 1, "Q2b effective return"
    c0R = argmax(lambda z: u(z, sg) + bt * 2 ** sg * u(R * (1 - z), sg), 1e-12, 1 - 1e-12)
    assert abs(c0R - sop[0]) < 1e-6, "Q2b naive self with return R"
assert sp.simplify(A(HALF, s) - 2 ** s) == 0, "Q2b A(1/2)"
assert sp.simplify(sp.diff(c ** (1 - s), c, 2) - s * (s - 1) * c ** (-s - 1)) == 0
for bt in (0.2, 0.5, 0.9):
    _, nai, sop, _, _ = plans(bt, 1)
    assert abs(sop[0] - nai[0]) < 1e-15, "Q2b log: equal c0"

# Q2(c): lemma, values, x, bounds, W-independence, log, sigma -> 1, beta -> 1
for _ in range(N):
    sg, wt = sig(), rng.uniform(0.1, 3, 3)
    S = np.sum(wt ** (1 / sg))
    cj = wt ** (1 / sg) / S
    assert abs(cj.sum() - 1) < 1e-12 and np.ptp(wt * cj ** -sg) < 1e-9 * np.mean(wt * cj ** -sg)
    assert abs(np.sum(wt * u(cj, sg)) - S ** sg / (1 - sg)) < 1e-9 * S ** sg / abs(1 - sg)
for _ in range(N):
    sg, bt, w0 = sig(), rng.uniform(0.05, 0.98), rng.uniform(0.3, 5)
    com, nai, sop, lam, o = plans(bt, sg, w0)
    vc = lambda wl: U0(plans(bt, sg, wl)[0], bt, sg)
    assert abs(vc(w0) - w0 ** (1 - sg) * (1 + 2 * o) ** sg / (1 - sg)) < 1e-9 * abs(vc(w0))
    vs = U0(sop, bt, sg)
    assert abs(vs - w0 ** (1 - sg) * (1 + lam) ** sg / (1 - sg)) < 1e-9 * abs(vs), "Q2c V_S"
    f = lambda z: vc((1 - z) * w0) - vs
    assert f(0) > 0 and f(1 - 1e-12) < 0, "Q2c existence of x"
    grid = np.linspace(0, 1 - 1e-6, 60)
    assert np.all(np.diff([f(z) for z in grid]) < 0), "Q2c uniqueness of x"
    xr = brentq(f, 0, 1 - 1e-12, xtol=1e-15)
    xk = x_gen(bt, sg)
    assert 0 < xk < 1 and abs(xr - xk) < 1e-8, "Q2c closed form for x"
    w2 = 3.7 * w0
    vs2 = U0(plans(bt, sg, w2)[2], bt, sg)
    xr2 = brentq(lambda z: vc((1 - z) * w2) - vs2, 0, 1 - 1e-12, xtol=1e-15)
    assert abs(xr2 - xr) < 1e-8, "Q2c x independent of W"
    assert U0(nai, bt, sg) < vs, "Q2c naive loss larger"
    # log case
    com, nai, sop, _, _ = plans(bt, 1, w0)
    assert abs(U0(nai, bt, 1) - U0(sop, bt, 1)) < 1e-12, "Q2c log: V_N = V_S"
    gap = U0(com, bt, 1) - U0(sop, bt, 1)
    assert abs(gap - bt * np.log((1 + bt) ** 2 / (4 * bt))) < 1e-12, "Q2c v_C - v_S"
    xl = brentq(lambda z: U0(plans(bt, 1, (1 - z) * w0)[0], bt, 1) - U0(sop, bt, 1),
                0, 1 - 1e-12, xtol=1e-15)
    assert abs(xl - x_log(bt)) < 1e-9, "Q2c log formula"
    bm = mp.mpf(bt)
    assert abs(x_gen(bm, 1 + mp.mpf("1e-12")) - x_log(bm)) < 1e-9, "Q2c sigma -> 1"
xg_half = x_gen(HALF, s)
assert sp.simplify(sp.limit(xg_half, s, 1) - x_log(HALF)) == 0, "Q2c sigma -> 1 (sympy)"
ratio = sp.series(A(HALF + d, s) / 2 ** s, d, 0, 4).removeO()
assert all(sp.simplify(ratio.coeff(d, i) - v) == 0
           for i, v in ((0, 1), (1, 0), (2, 2 * s * (s - 1)), (3, 0))), "Q2c A expansion"
mu_ser = sp.series((1 + 2 * s * (s - 1) * d ** 2) ** (1 / s), d, 0, 4).removeO()
assert sp.simplify(mu_ser - 1 - 2 * (s - 1) * d ** 2) == 0, "Q2c mu expansion"
lnx = sp.series(s / (1 - s) * sp.log(1 + 2 * om * 2 * (s - 1) * d ** 2 / (1 + 2 * om)),
                d, 0, 3).removeO()
assert sp.simplify(lnx + 4 * s * om / (1 + 2 * om) * d ** 2) == 0, "Q2c ln(1-x)"
om_e = (1 - e) ** (1 / s)
assert sp.simplify(sp.series(om_e, e, 0, 2).removeO() - (1 - e / s)) == 0, "Q2c omega"
dl_e = (1 - om_e) / (2 * (1 + om_e))
assert sp.simplify(sp.series(dl_e, e, 0, 2).removeO() - e / (4 * s)) == 0, "Q2c delta"
for sv in (HALF, 2, 3):
    assert sp.limit(x_gen(be, sv) / (1 - be) ** 2, be, 1) == 1 / (12 * sp.S(sv)), "Q2c order"
assert sp.limit(x_log(be) / (1 - be) ** 2, be, 1) == sp.Rational(1, 12), "Q2c log order"
for _ in range(N):
    sg, ep = sig(), mp.mpf("1e-5")
    assert abs(x_gen(1 - ep, mp.mpf(sg)) * 12 * sg / ep ** 2 - 1) < 1e-3, "Q2c 1/(12 sigma)"

# ---------------- Q2(d): equilibrium rates, sophisticated households ----------------
r01, r12, yv = sp.Rational(1, 1) * (1 + be) / (2 * be) - 1, 1 / be - 1, sp.Symbol("y", positive=True)
up = lambda z: z ** -s
assert sp.simplify(up(yv) - be * (1 + r12) * up(yv)) == 0, "Q2d r12"
assert sp.simplify(up(yv) - (1 + r01) * 2 * be / (1 + be) * up((1 + be) * yv / (1 + be))) == 0
assert sp.simplify(r01 - (1 - be) / (2 * be)) == 0 and sp.simplify(r12 - 2 * r01) == 0


def self1(w1, bt, sg, R):
    """Self 1's (c1, c2) from its Euler equation and budget c1 + c2/R = w1."""
    c1v = w1 / (1 + bt ** (1 / sg) * R ** (1 / sg - 1))
    return c1v, (bt * R) ** (1 / sg) * c1v


for _ in range(N):
    sg, bt, yy = sig(), rng.uniform(0.2, 0.98), rng.uniform(0.5, 2)
    R01, R12 = (1 + bt) / (2 * bt), 1 / bt
    wq = (1 + bt) * yy                           # W1 when nobody saved at date 0
    c1b = argmax(lambda z: u(z, sg) + bt * u(R12 * (wq - z), sg), 1e-9, wq - 1e-9)
    assert abs(c1b - yy) < 1e-6 and abs(self1(wq, bt, sg, R12)[0] - yy) < 1e-12, "Q2d self 1"
    tot = lambda z: u(z, sg) + bt * sum(u(v, sg) for v in self1(R01 * (yy - z) + wq, bt, sg, R12))
    assert abs(argmax(tot, 0.2 * yy, 1.8 * yy) - yy) < 1e-6, "Q2d self 0 clears at r01"
    xs = rng.uniform(0.3, 1)                     # plotted curves = closed forms
    assert abs(1 / xs - 1 - (1 - xs) / xs) < 1e-12 and abs((1 - xs) / (2 * xs) - (1 / xs - 1) / 2) < 1e-12

# ---------------- Q2(e): signs, limits, naive economy ----------------
assert sp.simplify(sp.diff(r01, be) + 1 / (2 * be ** 2)) == 0, "Q2e dr01/dbeta"
assert sp.simplify(sp.diff(r12, be) + 1 / be ** 2) == 0, "Q2e dr12/dbeta"
assert sp.diff(r01, s) == 0 and sp.diff(r12, s) == 0, "Q2e no sigma"
assert sp.limit(r01, be, 1) == 0 and sp.limit(r12, be, 1) == 0, "Q2e rates at beta = 1"
assert sp.limit(r01, be, 0, "+") == sp.oo and sp.limit(r12, be, 0, "+") == sp.oo
for sv in (HALF, 2):                             # x -> 0 at the ends (sympy)
    assert sp.limit(x_gen(be, sv), be, 1) == 0 and sp.limit(x_gen(be, sv), be, 0, "+") == 0
assert sp.limit(x_log(be), be, 0, "+") == 0 and sp.limit(x_log(be), be, 1) == 0
assert sp.limit(x_gen(HALF, s), s, sp.oo) == 0 and sp.limit(x_gen(HALF, s), s, 0, "+") == 0
assert logzero(lam_s, om * (1 + om) ** (1 - 1 / s) * (1 + om / om ** s) ** (1 / s)), "Q2e Lambda rewrite"
for _ in range(50):                              # x -> 0 at the ends (random draws)
    sg, bt = mp.mpf(sig()), mp.mpf(rng.uniform(0.05, 0.98))
    assert 0 <= x_gen(mp.mpf("1e-1000"), sg) < 1e-4 and x_gen(1 - mp.mpf("1e-8"), sg) < 1e-14
    assert 0 <= x_gen(bt, mp.mpf("1e-3")) < 1e-6 and 0 <= x_gen(bt, mp.mpf("1e7")) < 1e-6
    assert 0 < x_gen(bt, sg) < 1 and 0 < x_log(bt) < 1, "Q2e x inside (0, 1)"
    om_s = bt ** (1 / mp.mpf("1e-2"))            # sigma -> 0 bound on Lambda, in logs:
    # ln(Lambda/omega) <= omega/(beta sigma); comparing levels is below 50-digit precision once omega < 1e-48
    ln_lam = (1 - 100) * mp.log1p(om_s) + 100 * mp.log1p(om_s / bt)
    assert ln_lam <= om_s / (bt * mp.mpf("1e-2")), "Q2e Lambda bound"
for _ in range(N):                               # signs near beta = 1
    sg, ep, hh = mp.mpf(sig()), mp.mpf("1e-3"), mp.mpf("1e-12")
    dxb = (x_gen(1 - ep + hh, sg) - x_gen(1 - ep - hh, sg)) / (2 * hh)
    dxs = (x_gen(1 - ep, sg + hh) - x_gen(1 - ep, sg - hh)) / (2 * hh)
    assert dxb < 0 and abs(dxb / (-ep / (6 * sg)) - 1) < 0.05, "Q2e dx/dbeta near 1"
    assert dxs < 0 and abs(dxs / (-ep ** 2 / (12 * sg ** 2)) - 1) < 0.05, "Q2e dx/dsigma"
for i in range(N):                               # naive economy
    sg, bt, yy = sig(), rng.uniform(0.2, 0.98), rng.uniform(0.5, 2)
    p = 1 - 1 / sg
    R01n, R12 = (1 + bt) ** sg / (1 + bt ** p) ** sg / bt, 1 / bt
    R01s = (1 + bt) / (2 * bt)
    assert np.sign(R01n - R01s) == np.sign(sg - 1), "Q2e sign(r01N - r01S)"
    assert np.sign(((1 + bt) / 2) ** p - (1 + bt ** p) / 2) == np.sign(p), "Q2e Jensen z^p"
    if i < 40:                                   # brute force: believed plan, then c0 = y
        wq = (1 + bt) * yy

        def believed(w1):
            """Value self 0 expects from W1: max u(c1) + u(c2), c1 + beta c2 = w1."""
            c1v = argmax(lambda z: u(z, sg) + u((w1 - z) / bt, sg), 1e-9 * w1, w1 * (1 - 1e-9))
            return u(c1v, sg) + u((w1 - c1v) / bt, sg), c1v

        assert abs(believed(wq)[1] - wq / (1 + bt ** p)) < 1e-6, "Q2e planned c1"
        c0n = argmax(lambda z: u(z, sg) + bt * believed(R01n * (yy - z) + wq)[0],
                     0.5 * yy, 1.5 * yy)
        assert abs(c0n - yy) < 1e-5, "Q2e naive self 0 clears at r01N"
assert sp.simplify(((1 + be) / (1 + be ** 0)) ** 1 / be - (1 + be) / (2 * be)) == 0

print("practice-L3-L4-check-b1.py: all checks passed")
