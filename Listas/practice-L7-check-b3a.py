"""Practice list D v4, Block 3, Question 5 (practice-L7-block3a.tex): every closed form, sign, limit and distractor.

Run from Listas/: python practice-L7-check-b3a.py   (aborts on the first mismatch).
kappa is treated as a free positive slope: (1-alpha)(1/sigma+eta)/alpha covers all of (0, inf) as alpha runs over (0, 1).
"""
import random

import sympy as sp

random.seed(20261007)
N = 400
sg, et, rho, k, gm = sp.symbols("sigma eta rho kappa gamma", positive=True)
chi, beta, d0 = sp.symbols("chi beta d_0", positive=True)
y, p, pe, a, mu, g, gb, i, pbar, yn, ybn, dpbar = sp.symbols("y p p^e a mu g gbar i pbar y_n ybar_n dpbar", real=True)


def zero(expr, what):
    assert sp.simplify(expr) == 0, f"{what}: {sp.simplify(expr)} != 0"


def asad(ybn_, yn_, i_, pbar_, pe_=0):
    """AS (20) p - p^e = kappa (y - y_n) and AD (21) with g = gbar and no taxes; returns (y, p)."""
    s = sp.solve([sp.Eq(p - pe_, k * (y - yn_)), sp.Eq(y, ybn_ - sg * (i_ - (pbar_ - p) - rho))], [y, p], dict=True)[0]
    return s[y], s[p]


def draw():
    """One random admissible draw: sigma, eta, rho, kappa, gamma > 0."""
    return {sg: random.uniform(0.05, 5), et: random.uniform(0.01, 5), rho: random.uniform(0.001, 0.1),
            k: random.uniform(0.01, 10), gm: random.uniform(0.05, 3)}


_CACHE = {}


def ev(expr, v):
    """Numeric value of expr at the draw v; each expression is lambdified once."""
    expr = sp.sympify(expr)
    if expr not in _CACHE:
        syms = sorted(expr.free_symbols, key=str)
        _CACHE[expr] = (syms, sp.lambdify(syms, expr, "math"))
    syms, f = _CACHE[expr]
    return f(*(v[s] for s in syms))


def differs(e1, e2, extra):
    """Two expressions differ at N random admissible draws (extra() adds the item's own variables)."""
    for _ in range(N):
        v = {**draw(), **extra()}
        assert abs(ev(e1, v) - ev(e2, v)) > 1e-9, (e1, e2, v)


# ----------------------------------------------------------------- (a) credible rise in the long-run price level
y1, p1 = asad(ybn, yn, i, pbar + dpbar, pe)
y0, p0 = asad(ybn, yn, i, pbar, pe)
dy, dp = sp.simplify(y1 - y0), sp.simplify(p1 - p0)
key_a = sg / (1 + sg * k) * dpbar
zero(dy - key_a, "(a) dy")
zero(dp - sg * k / (1 + sg * k) * dpbar, "(a) dp")
zero(dy - sg * (dpbar - dp), "(a) AD in differences")
assert sp.limit(dy, k, 0) == sg * dpbar                      # A is the rigid-price limit
assert sp.limit(dy, k, sp.oo) == 0 and sp.limit(dp, k, sp.oo) == dpbar
for _ in range(N):                                           # dy > 0 and 0 < dp < dpbar
    v = {**draw(), dpbar: random.uniform(1e-3, 1)}
    assert ev(dy, v) > 0 and 0 < ev(dp, v) < v[dpbar]
for dis in (sg * dpbar, dpbar, sg * k / (1 + sg * k) * dpbar):
    differs(dis, key_a, lambda: {dpbar: random.uniform(1e-3, 1)})

# ----------------------------------------------------------------- (b) permanent productivity rise
gap_flex = et * (y - a) + (y - g) / sg - a + mu                # p~ - p = (w - p) - a + mu, l = y - a
yn_gen = sp.solve(sp.Eq(gap_flex, 0), y)[0]
zero(yn_gen - ((1 + et) * a + g / sg - mu) / (1 / sg + et), "(b) y_n, eq. (15)")
Y = yn_gen.subs({g: 0, mu: 0})
zero(gap_flex.subs({g: 0, mu: 0}) - ((1 / sg + et) * y - (1 + et) * a), "(b) p~ - p at g = mu = 0")
zero(Y - (1 + et) * a / (1 / sg + et), "(b) key y_n")
rn_b = rho + (Y - Y) / sg                                    # abar = a  ->  ybar_n = y_n
zero(rn_b - rho, "(b) r_n unchanged")
yb, pb = asad(Y, Y, rho, 0)
zero(yb - Y, "(b) y = y_n")
zero(pb, "(b) p = p^e")
AD21 = ybn - sg * (i - (pbar - p) - rho)
zero(AD21.subs({ybn: Y, i: rho, pbar: 0, p: 0}) - Y, "(b) shifted AD passes through (y_n, p^e)")
zero((pe + k * (0 - Y)) - (pe - k * Y), "(b) A: price read off the new AS at the old output")
zero((pe + k * (y - Y)) - (pe + k * y) + k * Y, "(b) B: downward AS shift is kappa y_n")
zero(Y - a - (1 - 1 / sg) * a / (1 / sg + et), "(b) y_n - a")
zero((Y - a).subs(sg, 1), "(b) D holds only at sigma = 1")
key_b = (Y, sp.Integer(0))
for dis in ((sp.Integer(0), -k * Y), (Y, -k * Y), (a, sp.Integer(0))):
    for _ in range(N):
        v = {**draw(), a: random.uniform(1e-3, 0.5)}
        dist = abs(ev(dis[0] - key_b[0], v)) + abs(ev(dis[1] - key_b[1], v))
        assert dist > 1e-9, (dis, v)

# ----------------------------------------------------------------- (c) debt-financed transfers
B = sp.Symbol("B", positive=True)
zero(B - (1 + i) * B / (1 + i), "(c) PV of a debt-financed transfer")
tb, tbb, dhat, pnb = sp.symbols("tau_b taubar_b dhat pbar_n", real=True)
phi = (sg * chi + (1 - chi) * d0 * beta) / chi                 # Benigno's definition
zero(phi - (sg + (1 - chi) * d0 * beta / chi), "(c) phi rewritten")
AD32 = (ybn - phi * (i - (pnb - p) - rho) + (g - gb) / chi - (1 - chi) / chi * (tb - tbb)
        + (1 - chi) / chi * (dhat + d0 * (p - pe)))
varpi = sg - d0 * (1 - beta) * (1 - chi) / chi
zero(sp.diff(AD32, p) + varpi, "(c) dy/dp = -varpi")
zero(phi - (1 - chi) * d0 / chi - varpi, "(c) varpi = phi - (1-chi) d0/chi")
s32 = sp.solve([sp.Eq(y, AD32), sp.Eq(p - pe, k * (y - yn))], [y, p], dict=True)[0]
dtb, dtbb = sp.symbols("dtau_b dtaubar_b", real=True)
Delta = -(dtb - dtbb)
zero(sp.diff(AD32, tb) * dtb + sp.diff(AD32, tbb) * dtbb - (1 - chi) / chi * Delta, "(c) AD shift (1-chi)/chi Delta")
dyc = sp.diff(s32[y], tb) * dtb + sp.diff(s32[y], tbb) * dtbb
zero(dyc - (1 - chi) * Delta / (chi * (1 + varpi * k)), "(c) dy = (1-chi) Delta/[chi(1+varpi kappa)]")
stable = 0
while stable < N:                                             # draws with varpi >= 0: stability is automatic
    v = {**draw(), chi: random.uniform(0.01, 0.99), beta: random.uniform(0.5, 0.999), d0: random.uniform(0, 20),
         dtb: -random.uniform(1e-3, 1), dtbb: random.choice([0, random.uniform(1e-3, 1)])}
    if ev(varpi, v) < 0:
        continue
    assert ev(1 + varpi * k, v) > 0
    assert ev(Delta, v) > 0 and ev(dyc, v) > 0
    stable += 1
stable = 0
while stable < N:                                             # any stable draw, varpi < 0 included
    v = {**draw(), chi: random.uniform(0.01, 0.99), beta: random.uniform(0.01, 0.999), d0: random.uniform(0, 50),
         dtb: -random.uniform(1e-3, 1), dtbb: random.choice([0, random.uniform(1e-3, 1)])}
    if ev(1 + varpi * k, v) <= 1e-6:
        continue
    assert ev(dyc, v) > 0
    stable += 1

# ----------------------------------------------------------------- (d) oil shock, Okun's law
yg, pg = asad(ybn, yn, i, pbar, pe)
rn = rho + (ybn - yn) / sg
zero(yg - yn - sg / (1 + sg * k) * (rn - i + pbar - pe), "(d) general gap formula")
gap_d = sp.simplify((yg - yn).subs({i: rho, pbar: pe}))
y_d = sp.simplify(yg.subs({i: rho, pbar: pe}))
zero(gap_d - sg / (1 + sg * k) * (rn - rho), "(d) gap via r_n")
zero(gap_d - (ybn - yn) / (1 + sg * k), "(d) gap")
zero(y_d - (sg * k * yn + ybn) / (1 + sg * k), "(d) output")
zero(y_d.subs(ybn, 0) - sg * k / (1 + sg * k) * yn, "(d) output at ybar_n = 0")
zero(gap_d.subs(ybn, yn), "(d) permanent shock: zero gap")
yn_oil = ((1 + et) * a - mu) / (1 / sg + et)
for _ in range(N):
    v = {**draw(), a: -random.uniform(1e-3, 0.5), mu: random.uniform(1e-3, 0.5)}
    ynv = ev(yn_oil, v)
    w = {**v, yn: ynv, ybn: 0}
    assert ynv < 0 and ev(rn - rho, w) > 0
    assert ev(gap_d, w) > 0 and ev(-gm * gap_d, w) < 0
    assert ynv < ev(y_d, w) < 0
for _ in range(N):                                            # general conditions: sign(u - u_n), sign(y)
    v = {**draw(), yn: random.uniform(-1, 1), ybn: random.uniform(-1, 1)}
    u_gap = ev(-gm * gap_d, v)
    assert (u_gap < 0) == (v[ybn] > v[yn])
    assert (ev(y_d, v) < 0) == (ev(sg * k * yn + ybn, v) < 0)

print("practice-L7-check-b3a: all checks passed")
