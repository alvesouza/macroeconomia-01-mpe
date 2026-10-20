"""Checks every symbolic and numeric result of practice-P1-growth-ge.tex (blocks 1-3); aborts on the first mismatch.

Closed forms: sympy (simplify(lhs - rhs) == 0). Signs and inequalities: random admissible draws. Simulations (Kurlat 9.12,
the created OLG maps): pure-Python iteration and bisection, and the pgfplots coordinates written in the .tex are parsed
and compared with the computed paths. Run from this folder: python practice-P1-growth-ge-check.py
"""
import pathlib
import random
import re

import sympy as sp

random.seed(20261016)
HERE = pathlib.Path(__file__).parent
TEX = {b: (HERE / f"practice-P1-growth-ge-block{b}.tex").read_text(encoding="utf-8") for b in (1, 2, 3)}


def zero(expr):
    """Assert that a sympy expression is identically 0.

    Tries simplify after forcing power rules (all symbols are positive); if sympy cannot close the identity, evaluates it
    at 30 random points with every symbol in (0.05, 0.95), which is admissible for every parameter of this list.
    """
    e = sp.simplify(sp.powsimp(sp.expand_power_base(expr, force=True), force=True))
    if e == 0:
        return
    for _ in range(30):
        v = complex(e.subs({x: random.uniform(0.05, 0.95) for x in e.free_symbols}).evalf())
        assert abs(v) < 1e-9, (expr, v)


def close(x, y, tol=5e-5):
    """Assert two numbers agree to tol (absolute)."""
    assert abs(float(x) - float(y)) <= tol, (x, y)


def bisect(f, a, b, it=200):
    """Root of f on [a, b] by bisection; f(a), f(b) must differ in sign."""
    fa = f(a)
    assert fa * f(b) < 0, (a, b)
    for _ in range(it):
        m = (a + b) / 2
        if fa * f(m) <= 0:
            b = m
        else:
            a, fa = m, f(m)
    return (a + b) / 2


def coords(tex, nth):
    """The nth pgfplots `coordinates {...}` list in tex, as [(x, y)]."""
    block = re.findall(r"coordinates \{([^}]*)\}", tex)[nth]
    return [tuple(map(float, p.split(","))) for p in re.findall(r"\(([^)]*)\)", block)]


al, be, s, n, g, d, A, r, sg, psi = sp.symbols("alpha beta s n g delta A r sigma psi", positive=True)

# ---------------------------------------------------------------- Q1 Kurlat 5.8
va = [1000 - 0, 4000 - 1000, 1000 - 0]; wages = [200, 1400, 400]
assert sum(va) == 5000 and sum(wages) + (800 + 1600 + 600) == 5000 and 4000 + 1000 == 5000
assert [v - w for v, w in zip(va, wages)] == [800, 1600, 600]
alpha5, s5, d5 = 3000 / 5000, 1000 / 5000, (2000 - 1800) / 2000
assert (alpha5, s5, d5) == (0.6, 0.2, 0.1)
cs = (1 - s) * s ** (al / (1 - al))
assert sp.solve(sp.diff(sp.log(cs), s), s) == [al]                   # s_GR = alpha
close(sp.diff((1 - s) * s ** 1.5, s).subs(s, 0.2), 0.447, 1e-3)      # s^0.5 (1.5 - 2.5 s) at 0.2
close(alpha5 / (s5 / d5), 0.3, 1e-12); close(alpha5 / d5, 6, 1e-12)

# ---------------------------------------------------------------- Q2 Jones RQ4 and created (b)-(d)
Ab, db = sp.symbols("Abar dbar", positive=True)
Kst = (s * Ab / db) ** sp.Rational(3, 2)
zero(s * Ab * Kst ** sp.Rational(1, 3) - db * Kst)                    # sY = dK with L = 1
cst = (1 - s) * Ab ** sp.Rational(3, 2) * (s / db) ** sp.Rational(1, 2)
zero((1 - s) * Ab * Kst ** sp.Rational(1, 3) - cst)
assert sp.solve(sp.diff(sp.log(cst), s), s) == [sp.Rational(1, 3)]
zero((sp.Rational(1, 3) * db / s).subs(s, sp.Rational(1, 3)) - db)    # MPK = dbar at s = 1/3
assert sp.diff(sp.log(cst), db).subs({s: 0.3, db: 0.05}) < 0         # depreciation lowers c*
slip = sp.solve(sp.diff(sp.log((1 - s) * s ** (1 / (1 - al))), s), s)
assert len(slip) == 1; zero(slip[0] - 1 / (2 - al))
assert sp.limit(1 / (2 - al), al, 0) == sp.Rational(1, 2) and sp.limit(al, al, 0) == 0
N = (1 + n) * (1 + g) - 1 + d
kt = (s / N) ** (1 / (1 - al))
zero(((1 - d) * kt + s * kt ** al) / ((1 + n) * (1 + g)) - kt)        # fixed point of the law of motion
zero(sp.powsimp(al * kt ** (al - 1) - al * N / s, force=True))       # MPK = alpha N / s
num = {al: sp.Rational(1, 3), n: 0.01, g: 0.02, d: 0.05}
close(N.subs(num), 0.0802, 1e-12)
for sv, k_, c_, m_ in ((0.2, 3.9381, 1.2633, 0.1337), (1 / 3, 8.4734, 1.3591, 0.0802), (0.6, 20.4628, 1.0941, 0.0446)):
    close(kt.subs(num).subs(s, sv), k_, 1e-4); close(((1 - s) * kt ** al).subs(num).subs(s, sv), c_, 1e-4)
    close((al * N / s).subs(num).subs(s, sv), m_, 1e-4)
close(1 - 1.0941 / 1.3591, 0.195, 5e-4)

# ---------------------------------------------------------------- Q3 Kurlat 6.1
a0, y1, y2, t1, t2, c1 = sp.symbols("a0 y1 y2 tau1 tau2 c1", positive=True)
u = lambda c: c ** (1 - sg) / (1 - sg)
c2_of = y2 - t2 + (1 + r) * (a0 + y1 - t1 - c1)
W = a0 + y1 - t1 + (y2 - t2) / (1 + r)
D = 1 + be ** (1 / sg) * (1 + r) ** (1 / sg - 1)
C1, C2 = W / D, (be * (1 + r)) ** (1 / sg) * W / D
foc = sp.diff(u(c1) + be * u(c2_of), c1)
pt = {a0: 1.3, y1: 2.0, y2: 1.1, t1: 0.2, t2: 0.4, r: 0.07, be: 0.93, sg: 2.5}
for p in (pt, {**pt, sg: 0.6}, {**pt, sg: 1.0001}):
    close(foc.subs(c1, C1).subs(p), 0, 1e-10)                         # Euler holds at the closed form
    close(c2_of.subs(c1, C1).subs(p), C2.subs(p), 1e-10)
    pset_c2 = (y2 - t2 + (1 + r) * (a0 + y1 - t1)) / D                # PSET 3's boxed c2: a slip
    right_c2 = (y2 - t2 + (1 + r) * (a0 + y1 - t1)) / (1 + be ** (-1 / sg) * (1 + r) ** (1 - 1 / sg))
    close(right_c2.subs(p), C2.subs(p), 1e-10); assert abs((pset_c2 - C2).subs(p)) > 1e-3
zero(sp.diff(C1, y2) - 1 / ((1 + r) * D)); zero(sp.diff(C1, a0) - 1 / D); zero(sp.diff(C1, y1) - 1 / D)
zero(sp.diff(C1, be) + W / D ** 2 * be ** (1 / sg - 1) * (1 + r) ** (1 / sg - 1) / sg)
e_c1 = ((a0 + y1) / D)
zero(sp.diff(e_c1, r) - (a0 + y1) * be ** (1 / sg) * (1 + r) ** (1 / sg - 2) / D ** 2 * (sg - 1) / sg)

# ---------------------------------------------------------------- Q4 Kurlat 6.2
def s_cur(y1v, y2v, rv, bv=0.97, sv=2.0):
    """Saving rate out of current income, 6.1 with a0 = taxes = 0."""
    Dv = 1 + bv ** (1 / sv) * (1 + rv) ** (1 / sv - 1)
    return 1 - (y1v + y2v / (1 + rv)) / Dv / y1v
close(s_cur(10, 2, 0.06), 0.392, 5e-4); close(s_cur(3, 9, 0.06), -0.958, 5e-4)
close(s_cur(10, 2, 0.02) - s_cur(10, 2, 0.06), 0.002, 5e-4); close(s_cur(3, 9, 0.02) - s_cur(3, 9, 0.06), -0.038, 5e-4)
dc1dr = sp.lambdify((y1, y2, r, be, sg), sp.diff((y1 + y2 / (1 + r)) / D, r))
for _ in range(400):                                                   # borrowers: c1 falls when r rises
    v = (random.uniform(0.1, 5), random.uniform(0.1, 10), random.uniform(0, 0.3), random.uniform(0.5, 0.999), random.uniform(0.2, 6))
    if s_cur(*v[:3], v[3], v[4]) < 0:
        assert dc1dr(*v) < 0, v

# ---------------------------------------------------------------- Q5 Kurlat 9.2
assert (1 + 1 - 1) - 1 == 0                                            # 1 + r = r^K + 1 - delta with r^K = 1, delta = 1

# ---------------------------------------------------------------- Q6 Kurlat 9.11-9.12
rho = 1 / be - 1
Kss = (al / (rho + d)) ** (1 / (1 - al))
zero(sp.powsimp(al * Kss ** (al - 1) - d - rho, force=True))         # (9.3.17)
zero(sp.powsimp(d * Kss / Kss ** al - al * d / (rho + d), force=True))
P = {al: 0.4, be: 0.95, d: 0.08}
close(rho.subs(P), 0.052632, 1e-6); close(Kss.subs(P), 6.2954, 1e-4); close((Kss ** al).subs(P), 2.0874, 1e-4)
sF = float((al * d / (rho + d)).subs(P)); close(sF, 0.241270, 1e-6)
KssF, cssF = float(Kss.subs(P)), float((Kss ** al - d * Kss).subs(P)); close(cssF, 1.5838, 1e-4)
close((0.4 / 0.08) ** (1 / 0.6), 14.62, 5e-3)


def path(c0, T=150):
    """Optimal-economy iteration; returns K, c lists and +1 (c0 too high), -1 (too low) or 0."""
    K, C = [2.0], [c0]
    for _ in range(T - 1):
        Kn = 0.92 * K[-1] + K[-1] ** 0.4 - C[-1]
        if Kn <= 0:
            return K, C, 1
        if Kn > KssF * (1 + 1e-7):
            return K, C, -1
        cn = C[-1] * (0.95 * (1 + 0.4 * Kn ** -0.6 - 0.08)) ** 0.5
        if cn < C[-1]:
            return K, C, 1
        K.append(Kn); C.append(cn)
    return K, C, 0


lo, hi = 0.0, 2 ** 0.4 + 1.84
for _ in range(200):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if path(mid)[2] < 0 else (lo, mid)
c0 = (lo + hi) / 2
close(c0, 0.9206271904, 1e-8)
Ko, Co = [2.0], [c0]
for _ in range(149):
    Kn = 0.92 * Ko[-1] + Ko[-1] ** 0.4 - Co[-1]
    cn = Co[-1] * (0.95 * (1 + 0.4 * Kn ** -0.6 - 0.08)) ** 0.5
    Kn, cn = (KssF, cssF) if Kn > KssF or abs(Kn - KssF) < 1e-7 else (Kn, cn)
    Ko.append(Kn); Co.append(cn)
Kf = [2.0]
for _ in range(149):
    Kf.append(0.92 * Kf[-1] + sF * Kf[-1] ** 0.4)
Cf = [(1 - sF) * k ** 0.4 for k in Kf]
table = {0: (2.0, 2.0, 1.0012, 0.9206, 0.3184, 0.3989), 5: (2.7603, 3.1169, 1.1389, 1.1297, 0.3622, 0.4461),
         10: (3.4262, 4.0048, 1.2417, 1.2719, 0.3948, 0.4701), 25: (4.8324, 5.4958, 1.4248, 1.4818, 0.4531, 0.4953),
         50: (5.8509, 6.1667, 1.5381, 1.5678, 0.4891, 0.5025), 149: (6.2919, 6.2954, 1.5834, 1.5838, 0.5035, 0.5036)}
for t, row in table.items():
    got = (Kf[t], Ko[t], Cf[t], Co[t], sF * Kf[t] ** 0.4, Ko[t] ** 0.4 - Co[t])
    for x, y in zip(got, row):
        close(x, y)
for nth, series in ((0, Cf), (1, Co)):
    for t, c in coords(TEX[2], nth):
        close(series[int(t)], c)
assert [t for t in range(149) if (Co[t] - Cf[t]) * (Co[t + 1] - Cf[t + 1]) < 0] == [5]
Uf = sum(0.95 ** t * (-1 / Cf[t]) for t in range(150)); Uo = sum(0.95 ** t * (-1 / Co[t]) for t in range(150))
close(Uf, -15.79988); close(Uo, -15.74360); close(Uo / Uf, 0.996438, 1e-6)
close(Kf[1], 2.1584); close(Ko[1], 2.2389)

# ---------------------------------------------------------------- Q7 Romer 2.16
rh = sp.symbols("rho", positive=True)
zero((be / (1 + be)).subs(be, 1 / (1 + rh)) - 1 / (2 + rh))
for _ in range(400):
    a_, b_ = random.uniform(0.01, 0.99), random.uniform(0.01, 0.99)
    assert ((1 - a_) * b_ / (1 + b_) > a_) == (b_ * (1 - 2 * a_) > a_)
    assert not (b_ * (1 - 2 * a_) > a_) or a_ < 1 / 3
close(0.8 * 0.9 / 1.9, 0.379, 5e-4)

# ---------------------------------------------------------------- Q9 created: leisure, profits, OLG
w1, Pi1, a00, lam, L1, cc1, cc2 = sp.symbols("w1 Pi1 a0 lambda L1 c1 c2", positive=True)
X = a00 + w1 + Pi1
sol = {cc1: X / (1 + be + psi), cc2: be * (1 + r) * X / (1 + be + psi), L1: 1 - psi * X / ((1 + be + psi) * w1), lam: (1 + be + psi) / X}
for eq in (1 / cc1 - lam, be / cc2 - lam / (1 + r), psi / (1 - L1) - lam * w1, a00 + w1 * L1 + Pi1 - cc1 - cc2 / (1 + r)):
    zero(eq.subs(sol))
R = a00 + w1 * sol[L1] + Pi1
zero(sol[cc2] / (1 + r) / R - be / (1 + be))
zero((1 + be + psi) * w1 * sol[L1] - ((1 + be) * w1 - psi * (a00 + Pi1)))       # L1 > 0 iff psi(a0+Pi1) < (1+beta)w1
zero(sp.limit(sol[L1], psi, 0) - 1)
K1, Lx = sp.symbols("K1 L", positive=True)
Y1 = A * K1 ** al * Lx ** (1 - al)
Lstar = (1 - al) * (1 + be) / ((1 - al) * (1 + be) + psi)
w1e = (1 - al) * Y1 / Lx
zero((w1e * (1 - Lx) - psi * (w1e + al * Y1) / (1 + be + psi)).subs(Lx, Lstar))   # labour condition in equilibrium
assert not (Lstar.free_symbols & {A, K1})
Lbar = (1 + be) / (1 + be + psi)
zero(sol[L1].subs({a00: 0, Pi1: 0}) - Lbar)
coef = be * (1 - al) / (1 + be) * A * Lbar ** (1 - al)
Kst9 = coef ** (1 / (1 - al))
zero(sp.powsimp(coef * Kst9 ** al - Kst9, force=True)); zero(sp.powsimp(al * coef * Kst9 ** (al - 1) - al, force=True))
for _ in range(400):
    a_, b_, p_ = random.uniform(0.01, 0.99), random.uniform(0.01, 0.99), random.uniform(0.01, 10)
    Ls = float(Lstar.subs({al: a_, be: b_, psi: p_}))
    assert p_ * a_ * Ls < (1 - a_) * (1 + b_) and Ls < float(Lbar.subs({be: b_, psi: p_}))
Q9 = {al: sp.Rational(1, 3), be: 0.8, psi: 0.5, A: 5}
close(Lbar.subs(Q9), 0.7826, 1e-4); close(Lstar.subs(Q9), 0.7059, 1e-4); close(coef.subs(Q9), 1.2581, 1e-4)
close(Kst9.subs(Q9), 1.4112, 1e-4)
Y1n = float(Y1.subs(Q9).subs({K1: 1, Lx: Lstar.subs(Q9)})); close(Y1n, 3.9639, 1e-4)
Ks = [0.8 / 1.8 * Y1n]
for _ in range(3):
    Ks.append(float(coef.subs(Q9)) * Ks[-1] ** (1 / 3))
for x, y in zip(Ks, (1.7617, 1.5195, 1.4464, 1.4228)):
    close(x, y, 1e-4)
cw = coords(TEX[3], 0)
assert [round(p[0], 4) for p in cw[::2]] == [round(k, 4) for k in Ks[:3]]
for (xa, ya), (xb, yb) in zip(cw[::2], cw[1::2]):
    close(xa, ya, 0); close(yb, float(coef.subs(Q9)) * xb ** (1 / 3), 2e-4)
for a_, b_, sv, rv in ((1 / 3, 0.8, 0.2963, 0.125), (0.2, 0.9, 0.3789, -0.472)):
    se = b_ * (1 - a_) / (1 + b_); close(se, sv, 1e-4); close(a_ / se - 1, rv, 5e-4)

# ---------------------------------------------------------------- Q10 created: CRRA, n, OLG
Dr = 1 + be ** (1 / sg) * (1 + r) ** (1 / sg - 1)
sr = (Dr - 1) / Dr
wv = sp.symbols("w", positive=True)
foc10 = sp.diff(u(c1) + be * u((1 + r) * (wv - c1)), c1)
close(foc10.subs(c1, wv * (1 - sr)).subs({wv: 1.7, r: 0.4, be: 0.6, sg: 2.2}), 0, 1e-10)
dsr = sp.lambdify((r, be, sg), sp.diff(sr, r))
for _ in range(400):
    rv_, bv_, sv_ = random.uniform(-0.5, 3), random.uniform(0.05, 0.99), random.uniform(0.1, 5)
    if abs(sv_ - 1) > 1e-3:
        assert (dsr(rv_, bv_, sv_) > 0) == (sv_ < 1)
zero(sr.subs(sg, 1) - be / (1 + be))
kk = (al * A / (1 + r)) ** (1 / (1 - al))
zero(sp.powsimp((1 + n) * kk / (A * kk ** al) - al * (1 + n) / (1 + r), force=True))
zero((al * (1 + n) / (1 + r)).subs(r, n) - al)
P10 = dict(a=0.2, b=0.5, n=0.3, A=5)
close(0.2 * 1.3 * 1.5 / (0.8 * 0.5), 0.975, 1e-12); close(0.26 / 0.975, 0.2667, 1e-4)
kst10, kgr = (0.5 * 0.8 * 5 / (1.5 * 1.3)) ** 1.25, (0.2 * 5 / 1.3) ** 1.25
close(kst10, 1.0322, 1e-4); close(kgr, 0.7204, 1e-4)
cons = lambda k: 5 * k ** 0.2 - 1.3 * k
close(cons(kst10), 3.6899, 1e-4); close(cons(kgr), 3.7461, 1e-4)
for sv_, rv_, iy in ((0.5, 0.314, 0.198), (2.0, -0.287, 0.365), (1.0, -0.025, 0.2667)):
    s_ = lambda x: 1 - 1 / (1 + 0.5 ** (1 / sv_) * (1 + x) ** (1 / sv_ - 1))
    H = lambda x: 0.8 * s_(x) * (1 + x) - 0.2 * 1.3
    grid = [H(-0.99 + 0.01 * i) for i in range(5000)]
    assert sum(1 for i in range(4999) if grid[i] * grid[i + 1] < 0) == 1
    rs = bisect(H, -0.99, 49); close(rs, rv_, 5e-4); close(0.8 * s_(rs), iy, 5e-4)
    assert (rs < 0.3) == (0.8 * s_(rs) > 0.2)
ks = [0.3]
for _ in range(3):
    ks.append(1.0256410256 * ks[-1] ** 0.2)
for x, y in zip(ks[1:], (0.8062, 0.9824, 1.0220)):
    close(x, y, 1e-4)
cw = coords(TEX[3], 2)
for (xa, ya), (xb, yb) in zip(cw[1::2], cw[2::2]):
    close(ya, 1.0256 * xa ** 0.2, 2e-4); close(xb, ya, 0)
print("practice-P1-growth-ge: all checks passed (Q1-Q10).")
