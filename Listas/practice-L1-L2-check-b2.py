"""Practice list A v4, Block 2 (Questions 3-4, symbolic): independent check of every closed form,
sign, limit, ordering, existence claim and distractor in practice-L1-L2-block2.tex.

Run from Listas/: python practice-L1-L2-check-b2.py   (aborts on the first failed assertion).
Identities: sympy (the difference simplifies to 0, or the expanded logs of two products of
powers agree). Signs, orderings and existence: DRAWS random admissible draws, fixed seed.
"""
import math

import numpy as np
import sympy as sp
from scipy.optimize import brentq

rng = np.random.default_rng(20261007)
DRAWS = 300


def same(e1, e2):
    """True when e1 - e2 simplifies to zero."""
    return sp.simplify(e1 - e2) == 0


def same_log(e1, e2):
    """True when two positive products of powers agree (their expanded logs coincide)."""
    d = sp.expand_log(sp.log(e1), force=True) - sp.expand_log(sp.log(e2), force=True)
    return sp.simplify(d) == 0


def u(lo, hi):
    """One uniform draw on (lo, hi)."""
    return float(rng.uniform(lo, hi))


def differ(a, b):
    """True when two numbers differ beyond rounding."""
    return abs(a - b) > 1e-7 * max(1.0, abs(a), abs(b))


# ===== Q3(a): MPK ratio from observables, Y = A K^a (hL)^(1-a), common A =====
al, A, h, y, L, K = sp.symbols("alpha A h y L K", positive=True)
phi, chi = sp.symbols("phi chi", positive=True)
Y = A * K**al * (h * L)**(1 - al)
assert same_log(sp.diff(Y, K), al * Y / K)                        # MPK = alpha y/k
k_of_y = (y / (A * h**(1 - al)))**(1 / al)                         # k that produces y
assert same_log(A * k_of_y**al * h**(1 - al), y)
mpk_obs = sp.diff(Y, K).subs(K, k_of_y * L)
assert same_log(mpk_obs, al * A**(1 / al) * (y / h)**(-(1 - al) / al))


def mpk(yy, hh, tfp=A):
    """MPK in terms of output and human capital per worker (closed economy)."""
    return al * tfp**(1 / al) * (yy / hh)**(-(1 - al) / al)


key_a = (chi / phi)**((1 - al) / al)
assert same_log(mpk(phi * y, chi * h) / mpk(y, h), key_a)
opts_a = {"A": (1 / phi)**((1 - al) / al), "B": (chi / phi)**(1 - al),
          "C": (1 / phi)**(1 - al), "D": key_a}
assert same_log(key_a.subs(chi, 1), opts_a["A"])                  # A: no human capital
assert same_log((phi / chi)**(al - 1), opts_a["B"])               # B: y/h in place of k/h
assert same_log(opts_a["B"].subs(chi, 1), opts_a["C"])            # C: both mistakes
assert key_a.subs(chi, phi) == 1                                  # ratio -> 1 as chi -> phi
assert same(sp.diff(sp.log(chi / phi) * (1 - al) / al, al), -sp.log(chi / phi) / al**2)
fa = {key: sp.lambdify((al, phi, chi), e) for key, e in opts_a.items()}
for _ in range(DRAWS):
    a_, c_ = u(0.05, 0.95), u(0.05, 0.99)
    p_ = u(0.01, 0.999 * c_)
    v = {key: f(a_, p_, c_) for key, f in fa.items()}
    assert v["A"] > max(v["C"], v["D"]) and min(v["C"], v["D"]) > v["B"] > 1, (a_, p_, c_, v)
    assert differ(v["C"], v["D"]), (a_, p_, c_, v)

# ===== Q3(b): CES Golden-Rule saving rate =====
k, N = sp.symbols("k N", positive=True)
psi = sp.Symbol("psi", real=True)                                 # psi < 1, psi != 0
f = A * (al * k**psi + 1 - al)**(1 / psi)
fp = sp.diff(f, k)
assert same_log(fp, al * A**psi * (f / k)**(1 - psi))             # f' = a A^psi (f/k)^(1-psi)
sig = 1 / (1 - psi)
fk_gr = (N / (al * A**psi))**(1 / (1 - psi))                      # f/k where f' = N
key_b = (al * A**psi)**(1 / (1 - psi)) * N**(-psi / (1 - psi))
assert same_log(N / fk_gr, key_b)                                 # s = N k / f
assert same_log(key_b, al**sig * (A / N)**(sig - 1))              # sigma form
assert same_log(al * A**psi * fk_gr**(-psi), key_b)               # capital share k f'/f
opts_b = {"A": (al * A**psi)**(1 - psi) * N**psi,
          "B": (al * A**psi)**(-1 / (1 - psi)) * N**(psi / (1 - psi)),
          "C": key_b, "D": (al * A**psi)**(-(1 - psi)) * N**(-psi)}
fk_pow = (N / (al * A**psi))**(1 - psi)                           # f/k solved with power 1 - psi
assert same_log(N / fk_pow, opts_b["A"])                          # A: power 1 - psi
assert same_log(fk_gr / N, opts_b["B"])                           # B: inverts s f = N k
assert same_log(fk_pow / N, opts_b["D"])                          # D: both mistakes
assert sp.limit(key_b, psi, 0) == al                              # sigma -> 1: alpha
for key, lim in (("A", al), ("B", 1 / al), ("D", 1 / al)):        # Cobb-Douglas check keeps A
    assert same(sp.limit(opts_b[key], psi, 0), lim), key
dlog = sp.diff(sp.expand_log(sp.log(key_b), force=True), A) * A
assert same(dlog, sig - 1)                                        # d ln s / d ln(A/N)
assert same(sp.diff(sp.expand_log(sp.log(key_b), force=True), N) * N, 1 - sig)
# limits of f' (its range decides existence), at concrete psi of each sign;
# alpha = 1/(1+b), b > 0, tells sympy that 1 - alpha > 0
b = sp.Symbol("b", positive=True)
for ps in (sp.Rational(1, 2), sp.Rational(1, 3), sp.Integer(-1), sp.Integer(-2)):
    fpp = fp.subs({psi: ps, al: 1 / (1 + b)})
    edge = A * (1 / (1 + b))**(1 / ps)
    lim0, liminf = sp.limit(fpp, k, 0, "+"), sp.limit(fpp, k, sp.oo)
    if ps > 0:
        assert lim0 == sp.oo and same(liminf, edge)
    else:
        assert same(lim0, edge) and liminf == 0


def avg(kk, A_, a_, p_):
    """f(k)/k = A[a + (1-a) k^(-psi)]^(1/psi), the overflow-safe form."""
    return A_ * (a_ + (1 - a_) * kk**(-p_))**(1 / p_)


def mpk_ces(kk, A_, a_, p_):
    """f'(k) = a A^psi (f/k)^(1-psi)."""
    return a_ * A_**p_ * avg(kk, A_, a_, p_)**(1 - p_)


fn = sp.lambdify((k, A, al, psi), f, "math")
fpn = sp.lambdify((k, A, al, psi), fp, "math")
fppn = sp.lambdify((k, A, al, psi), sp.diff(f, k, 2), "math")
keyn = sp.lambdify((A, al, psi, N), key_b, "math")
optn = {key: sp.lambdify((A, al, psi, N), e, "math") for key, e in opts_b.items()}
n_yes = n_no = 0
while n_yes + n_no < DRAWS:
    A_, a_, N_ = u(0.3, 3.0), u(0.1, 0.9), u(0.02, 0.6)
    p_ = u(0.1, 0.9) if rng.random() < 0.5 else u(-3.0, -0.1)
    margin = math.log(a_ * (A_ / N_)**p_)                         # < 0 iff s_GR < 1
    if abs(margin) < 0.05 or abs(A_ - 1) < 0.01:
        continue                                                  # away from knife-edges
    kk = u(0.05, 20)
    assert abs(fpn(kk, A_, a_, p_) - mpk_ces(kk, A_, a_, p_)) < 1e-9 * fpn(kk, A_, a_, p_)
    assert abs(fn(kk, A_, a_, p_) / kk - avg(kk, A_, a_, p_)) < 1e-9 * avg(kk, A_, a_, p_)
    assert fppn(kk, A_, a_, p_) < 0 and avg(kk * 1.01, A_, a_, p_) < avg(kk, A_, a_, p_)
    edge = A_ * a_**(1 / p_)
    cond = N_ > edge if p_ > 0 else N_ < edge
    s_gr = keyn(A_, a_, p_, N_)
    assert cond == (margin < 0) == (s_gr < 1)
    g = lambda z: mpk_ces(math.exp(z), A_, a_, p_) - N_           # decreasing in z = ln k
    lo, hi = 0.0, 0.0
    for _ in range(400):
        if g(lo) > 0:
            break
        lo -= 0.5
    for _ in range(400):
        if g(hi) < 0:
            break
        hi += 0.5
    if g(lo) > 0 > g(hi):
        n_yes += 1
        assert cond, ("root found where the condition fails", A_, a_, p_, N_)
        kgr = math.exp(brentq(g, lo, hi, xtol=1e-14))
        share = kgr * mpk_ces(kgr, A_, a_, p_) / (avg(kgr, A_, a_, p_) * kgr)
        assert abs(N_ / avg(kgr, A_, a_, p_) - s_gr) < 1e-8 and abs(share - s_gr) < 1e-8
        for key in "ABD":
            assert differ(optn[key](A_, a_, p_, N_), s_gr), key
    else:
        n_no += 1
        assert not cond, ("no root found where the condition holds", A_, a_, p_, N_)
        grid = np.linspace(-120, 120, 481)
        signs = {g(z) > 0 for z in grid}
        assert len(signs) == 1                                    # f' - N never changes sign
        if p_ > 0:                                                # c = k(f/k - N) rises without bound
            c = [math.exp(z) * (avg(math.exp(z), A_, a_, p_) - N_) for z in (10, 40, 80)]
            assert signs == {True} and 0 < c[0] < c[1] < c[2]
        else:                                                     # s f/k < N for every s < 1
            assert signs == {False} and all(avg(math.exp(z), A_, a_, p_) < N_ for z in grid)
assert n_yes > 50 and n_no > 20, (n_yes, n_no)

# ===== Q3(c): Uzawa (constant Y/K with capital-augmenting progress) =====
t, gB, gx, u0, v0 = sp.symbols("t g_B g_x u0 v0", real=True)
uu, vv = u0 * sp.exp(psi * gB * t), v0 * sp.exp(psi * gx * t)
dsum = sp.diff(uu + vv, t)
assert same(dsum, psi * (gB * uu + gx * vv))
gx_sol = sp.solve(sp.Eq(dsum.subs(t, 0), 0), gx)
assert len(gx_sol) == 1 and same(gx_sol[0], -gB * u0 / v0)        # opposite sign to g_B
assert dsum.subs({gB: 0, gx: 0}) == 0
dsum1 = sp.lambdify((psi, gB, u0, v0), dsum.subs({gx: gx_sol[0], t: 1}))
for _ in range(DRAWS):
    p_ = u(0.1, 0.9) if rng.random() < 0.5 else u(-3.0, -0.1)
    gb_ = u(0.002, 0.05) * (1 if rng.random() < 0.7 else -1)
    assert abs(dsum1(p_, gb_, u(0.1, 2), u(0.1, 2))) > 1e-12      # Y/K not constant
B = sp.Symbol("B", positive=True)
assert same_log((B * K)**al * (A * L)**(1 - al), K**al * (B**(al / (1 - al)) * A * L)**(1 - al))

# ===== Q4: small open economy =====
r, d, ng, s, s0, s1 = sp.symbols("r delta ng s s0 s1", positive=True)
Nq, R = ng + d, r + d
Lam = Nq - s * R
kst = (al / R)**(1 / (1 - al))
yst = kst**al
# (a) firm's FOC, y*, (r+d) k* = a y*, no role for s; Lucas link to 3(a)
assert same_log(al * kst**(al - 1), R)
assert same_log(yst, (al / R)**(al / (1 - al)))
assert same_log(R * kst, al * yst)
assert sp.diff(kst, s) == 0 and sp.diff(yst, s) == 0
theta = phi / chi                                                 # A_BR/A_US from phi = theta chi
assert same(theta * chi, phi)
assert same_log(mpk(phi * y, chi * h, (theta**(1 - al)) * A) / mpk(y, h), sp.Integer(1))
# (b) law of motion, solution, half-life, stability
ys, E0, w0, wv = sp.symbols("ystar E0 w0 w", positive=True)
E = E0 * sp.exp(ng * t)                                           # effective labor A h L
W = sp.Function("W")(t)
Wdot = s * ((1 - al) * ys * E + R * W) - d * W
om_dot = sp.diff(W / E, t).subs(sp.Derivative(W, t), Wdot)
assert same(om_dot, s * (1 - al) * ys - Lam * W / E)
omst = s * (1 - al) * ys / Lam
om_t = omst + (w0 - omst) * sp.exp(-Lam * t)
assert same(sp.diff(om_t, t), s * (1 - al) * ys - Lam * om_t)
assert same((om_t - omst).subs(t, sp.log(2) / Lam), (w0 - omst) / 2)
assert sp.diff(Lam, s) == -R and same(Lam.subs(s, 1), ng - r)
assert same(Lam.subs(s, Nq / R), 0) and same(1 - Nq / R, (r - ng) / R)
# (c) net foreign assets, threshold, Golden Rule, GNI/GDP
ks = al * ys / R                                                  # FOC: (r+d) k* = a y*
sbar = al * Nq / R
assert same(s * (1 - al) * R - al * Lam, s * R - al * Nq)
assert same(omst - ks, ys * (s - sbar) / Lam)
assert same(sbar, Nq * ks / ys) and same(Nq / R - sbar, (1 - al) * Nq / R)
assert same(sbar - al, al * (ng - r) / R) and same(sbar.subs(r, ng), al)
gni = (1 - al) + R * omst / ys
wk = omst / ks
assert same(gni, (1 - al) * (1 + s * R / Lam)) and same(gni, (1 - al) * Nq / Lam)
assert same(gni, (1 - al) + al * wk) and same(wk, s * (1 - al) * R / (al * Lam))
assert same(gni - 1, R * (s - sbar) / Lam)
# (d) phase lines, crossing date T
assert same(sp.diff(s * (1 - al) * ys - Lam * wv, s), (1 - al) * ys + R * wv)
Lam0, Lam1 = Nq - s0 * R, Nq - s1 * R
om0, om1 = s0 * (1 - al) * ys / Lam0, s1 * (1 - al) * ys / Lam1
arg = (1 - al) * Nq * (s1 - s0) / (Lam0 * (s1 - sbar))
assert same((om1 - om0) / (om1 - ks), arg)
assert same((1 - al) * Nq * (s1 - s0) - Lam0 * (s1 - sbar), (sbar - s0) * Lam1)
T = sp.log(arg) / Lam1
assert same(T.subs(s0, sbar), 0)                                  # T -> 0 as s0 -> sbar
assert same(Lam.subs(s, sbar), (1 - al) * Nq)                     # closed-economy speed
fT = sp.lambdify((al, r, d, ng, s0, s1), T)
for _ in range(DRAWS):
    while True:
        a_, r_, d_, ng_ = u(0.1, 0.9), u(0.005, 0.15), u(0.01, 0.15), u(0.005, 0.1)
        N_, R_ = ng_ + d_, r_ + d_
        top, sb_ = min(1.0, N_ / R_), a_ * N_ / R_
        if sb_ < 0.95 * top:
            break
    s0_, s1_ = u(0.01, sb_), u(sb_ + 1e-3 * top, top * 0.999)
    k_ = (a_ / R_)**(1 / (1 - a_))
    y_ = k_**a_
    L0, L1 = N_ - s0_ * R_, N_ - s1_ * R_
    o0, o1 = s0_ * (1 - a_) * y_ / L0, s1_ * (1 - a_) * y_ / L1
    assert 0 < L1 < L0 and o0 < k_ < o1
    T_ = fT(a_, r_, d_, ng_, s0_, s1_)
    om_T = o1 - (o1 - o0) * math.exp(-L1 * T_)
    assert T_ > 0 and abs(om_T - k_) < 1e-9 * k_
    gni_path = lambda w: (1 - a_) + a_ * w / k_
    assert gni_path(o0) < 1 < gni_path(o1) and abs(gni_path(om_T) - 1) < 1e-9
    assert abs(gni_path(o0) - (1 - a_) * N_ / L0) < 1e-12
for vals in [(sp.Rational(1, 3), sp.Rational(4, 100), sp.Rational(5, 100), sp.Rational(3, 100))]:
    sub = dict(zip((al, r, d, ng), vals))
    sb = sbar.subs(sub)
    e = sp.Symbol("e", positive=True)
    Te = T.subs(sub).subs({s0: sp.Rational(15, 100), s1: sb + e})
    assert sp.limit(Te, e, 0, "+") == sp.oo                       # T -> oo as s1 -> sbar
# figure of 4(d): alpha = 1/3, r* = .04, delta = .05, n+g = .03, s0 = .15, s1 = .35
fig = {al: sp.Rational(1, 3), r: sp.Rational(4, 100), d: sp.Rational(5, 100),
       ng: sp.Rational(3, 100)}
k_fig, y_fig = float(kst.subs(fig)), float(yst.subs(fig))
for s_, icpt, slope, zero in [(0.15, 0.19245, 0.0665, 2.894), (0.35, 0.44905, 0.0485, 9.259)]:
    assert abs(s_ * (1 - 1 / 3) * y_fig - icpt) < 5e-5
    assert abs(float(Lam.subs(fig).subs(s, s_)) - slope) < 1e-12
    assert abs(icpt / slope - zero) < 2e-3
assert abs(k_fig - 7.128) < 1e-3 and 0.15 < float(sbar.subs(fig)) < 0.35
assert 0.35 < float((Nq / R).subs(fig))                           # stable at s1
assert 0.19245 - 0.0665 * 6.2 >= -0.22 and 0.44905 - 0.0485 * 11 >= -0.22
# (e) sign table: derivatives proved in the key, then signs at random draws
par = {"s": s, "r": r, "ng": ng, "d": d, "al": al}
res = {"wk": wk, "gni": gni, "hl": sp.log(2) / Lam, "sbar": sbar}
assert [sp.diff(Lam, par[p]) for p in ("s", "r", "ng", "d", "al")] == [-R, -s, 1, 1 - s, 0]
l2 = sp.log(2)
claimed = {
    ("wk", "s"): (1 - al) * Nq * R / (al * Lam**2), ("wk", "r"): (1 - al) * Nq * s / (al * Lam**2),
    ("wk", "ng"): -(1 - al) * s * R / (al * Lam**2), ("wk", "al"): -s * R / (al**2 * Lam),
    ("wk", "d"): s * (1 - al) / al * (Nq - R) / Lam**2,
    ("gni", "s"): (1 - al) * Nq * R / Lam**2, ("gni", "r"): (1 - al) * Nq * s / Lam**2,
    ("gni", "ng"): -(1 - al) * s * R / Lam**2, ("gni", "d"): (1 - al) * s * (Nq - R) / Lam**2,
    ("gni", "al"): -Nq / Lam,
    ("hl", "s"): l2 * R / Lam**2, ("hl", "r"): l2 * s / Lam**2, ("hl", "ng"): -l2 / Lam**2,
    ("hl", "d"): -l2 * (1 - s) / Lam**2, ("hl", "al"): sp.Integer(0),
    ("sbar", "s"): sp.Integer(0), ("sbar", "r"): -al * Nq / R**2, ("sbar", "ng"): al / R,
    ("sbar", "d"): al * (R - Nq) / R**2, ("sbar", "al"): Nq / R,
}
assert same(sp.diff(R / Lam, d), (Nq - R) / Lam**2)
# reading of delta: w*/k* = s(1-a)/(Lam k*/y*); k*/y* = a/R falls at rate 1/R, Lam rises at (1-s)/Lam
assert same(wk, s * (1 - al) / (Lam * (al / R)))
assert same(1 / R - (1 - s) / Lam, (Nq - R) / (R * Lam))         # first effect larger iff r* < n+g
table = {"wk": "++-*-", "gni": "++-*-", "hl": "++--0", "sbar": "0-+#+"}   # * sgn(ng-r), # sgn(r-ng)
dfun = {}
for (q, p), expr in claimed.items():
    assert same(sp.diff(res[q], par[p]), expr), (q, p)
    dfun[(q, p)] = sp.lambdify((s, r, ng, d, al), expr)
for key, e in [("gni", "s"), ("gni", "r"), ("gni", "ng"), ("gni", "d")]:
    assert same(claimed[(key, e)], al * claimed[("wk", e)])       # GNI/GDP moves with w*/k*
n_hi = n_lo = 0
for _ in range(DRAWS):
    a_, r_, d_, ng_ = u(0.05, 0.95), u(0.005, 0.15), u(0.01, 0.15), u(0.005, 0.1)
    s_ = u(0.01, 0.99 * min(1.0, (ng_ + d_) / (r_ + d_)))
    n_hi, n_lo = n_hi + (r_ > ng_), n_lo + (r_ < ng_)
    for q, row in table.items():
        for p, sign in zip(("s", "r", "ng", "d", "al"), row):
            v = dfun[(q, p)](s_, r_, ng_, d_, a_)
            want = {"+": 1, "-": -1, "0": 0, "*": np.sign(ng_ - r_), "#": np.sign(r_ - ng_)}[sign]
            assert np.sign(v) == want, (q, p, v, want)
assert n_hi > 30 and n_lo > 30
for (q, p) in [("wk", "d"), ("gni", "d")]:
    assert same(claimed[(q, p)].subs(r, ng), 0)                   # knife-edge r* = n+g
# limits in s
assert sp.limit(wk, s, 0) == 0 and same(sp.limit(gni, s, 0), 1 - al)
assert same(sp.limit(sp.log(2) / Lam, s, 0), sp.log(2) / Nq)
assert same(gni.subs(s, 1), (1 - al) * Nq / (ng - r))            # r* < n+g: finite at s = 1
for vals in [(sp.Rational(1, 3), sp.Rational(6, 100), sp.Rational(5, 100), sp.Rational(3, 100)),
             (sp.Rational(2, 5), sp.Rational(3, 100), sp.Rational(4, 100), sp.Rational(3, 100))]:
    sub = dict(zip((al, r, d, ng), vals))                         # r* >= n+g
    top = (Nq / R).subs(sub)
    for q in ("wk", "gni", "hl"):
        assert sp.limit(res[q].subs(sub), s, top, "-") == sp.oo, q
# knife-edge s = sbar
assert same((omst - ks).subs(s, sbar), 0) and same(gni.subs(s, sbar), 1)

print("practice-L1-L2-check-b2.py: all checks passed")
