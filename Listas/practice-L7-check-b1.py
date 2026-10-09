"""Practice list D v4, Block 1 (practice-L7-block1.tex, Questions 1-2): symbolic checks.

Run: python practice-L7-check-b1.py   (aborts on the first failed assert).
Closed forms are checked with sympy (simplify(lhs - rhs) == 0); signs, orderings, the sign condition of
Q2(d), the sign table of Q2(e) and the multiple-choice distractors at N random admissible draws;
uniqueness claims by root-finding and sign-change counts at random draws.
"""
import math
import random

import sympy as sp
from scipy.optimize import brentq

random.seed(20261007)
N = 300


def zero(expr):
    """Assert that a sympy expression simplifies to 0."""
    assert sp.simplify(expr) == 0, expr


al, sg, et, th, mu, rho, st, sc, beta = sp.symbols("alpha sigma eta theta mu rho sigma_t s_c beta", positive=True)
y, p, pe, a, g, i, pb, ybn, ab, gb, mub = sp.symbols("y p p_e a g i pbar ybar_n abar gbar mubar", real=True)
inv = 1 / sg + et
kap = (1 - al) * inv / al
ARGS = (al, sg, et, th, mu, a)
# admissible draws: 0<alpha<1, sigma, eta > 0, theta > 1; oil shock a < 0 < mu
D = [dict(al=random.uniform(0.02, 0.98), sg=random.uniform(0.05, 5.0), et=random.uniform(0.02, 5.0),
          th=random.uniform(1.05, 20.0), mu=random.uniform(0.01, 1.0), a=-random.uniform(0.01, 1.0)) for _ in range(N)]


def num(expr):
    """Float function of a draw dict for a sympy expression whose free symbols are in ARGS."""
    f = sp.lambdify(ARGS, expr, "math")
    return lambda d: f(d["al"], d["sg"], d["et"], d["th"], d["mu"], d["a"])


# ------------------------------------------------------------- Q1(a), Q2(b): AS from primitives
zero((et * (y - a) + (y - g) / sc / st).subs(st, sg / sc) - (et * (y - a) + (y - g) / sg))  # eta l + sigma_t^-1 c
ptil = p + et * (y - a) + (y - g) / sg - a + mu            # p~ = w - a + mu, w - p from labor supply
yn = ((1 + et) * a + g / sg - mu) / inv
zero(sp.solve(sp.Eq(ptil, p), y)[0] - yn)                  # y_n where p~ = p
zero(ptil - p - inv * (y - yn))                            # gap relation (16)
P_as = sp.solve(sp.Eq(p, al * pe + (1 - al) * ptil), p)[0]
zero(P_as - pe - kap * (y - yn))                           # AS (17)
assert all(num(sp.diff(kap, al))(d) < 0 for d in D)        # kappa falls in alpha
assert sp.limit(kap, al, 0, "+") == sp.oo and sp.limit(kap, al, 1, "-") == 0
kA = (1 - al) * sp.diff(ptil - p, y)                       # A: p - p^e = (1-alpha)(p~ - p), feedback dropped
zero(kA - (1 - al) * inv)
kC = (1 - al) * sp.diff(et * (y - a) + sg * (y - g) - a + mu, y)   # C: feedback dropped and sigma read as curvature
zero(kC - (1 - al) * (sg + et))
for k_ in (kA, al * inv / (1 - al), kC):                   # A, B, C differ from the key D
    f = num(k_ - kap)
    assert all(abs(f(d)) > 1e-9 for d in D)

# ------------------------------------------------------------- Q1(b): natural vs efficient output
ye = sp.solve(sp.Eq((y - g) / sg + et * (y - a), a), y)[0]                    # planner in logs
zero(ye - ((1 + et) * a + g / sg) / inv)                                       # (19)
zero(yn - ye + mu / inv)                                                       # y_n - y_e = -mu/(sigma^-1+eta)
kb = (yn.subs(g, 0), ye.subs(g, 0))
zero(kb[0] - ((1 + et) * a - mu) / inv)
zero(kb[1] - (1 + et) * a / inv)
ynA = sp.solve(sp.Eq(p + et * y + (y - g) / sg - a + mu, p), y)[0].subs(g, 0)  # A: l = y
yeA = sp.solve(sp.Eq((y - g) / sg + et * y, a), y)[0].subs(g, 0)
zero(ynA - (a - mu) / inv)
zero(yeA - a / inv)
ynD = ynA.subs(mu, 0)                                                          # D: l = y and the payroll tax as lump sum
zero(ynD - a / inv)
Db = [dict(d, a=-d["a"]) for d in D]                                           # Q1(b): a > 0
for d0, d1 in [(ynA, yeA), (kb[0], kb[0]), (ynD, yeA)]:                        # A, C, D vs key B
    f0, f1 = num(d0 - kb[0]), num(d1 - kb[1])
    assert all(abs(f0(d)) + abs(f1(d)) > 1e-9 for d in Db)

# ------------------------------------------------------------- Q1(c): theta and the AS slope
assert sp.diff(kap, th) == 0
dyn_dth = sp.diff(yn.subs(mu, sp.log(th / (th - 1))), th)
zero(dyn_dth - 1 / (th * (th - 1) * inv))
assert all(num(dyn_dth)(d) > 0 for d in D)

# ------------------------------------------------------------- Q1(d): news of higher long-run spending
ybn_e = ((1 + et) * ab + gb / sg - mub) / inv                                  # long-run (15)
AD = ybn_e + (g - gb) - sg * (i - (pb - p) - rho)
eqg = sp.solve([sp.Eq(y, AD), sp.Eq(p - pe, kap * (y - yn))], [y, p], dict=True)[0]
dy_dgb = sp.diff(eqg[y], gb)
zero(dy_dgb + et / (inv * (1 + sg * kap)))                                     # -m_gbar, Table 1
zero(ybn_e - gb - ((1 + et) * ab - mub - et * gb) / inv)                      # closed form in the key
zero(sp.diff(ybn_e - gb, gb) + et / inv)
assert all(num(dy_dgb)(d) < 0 and 0 < num(sp.diff(ybn_e, gb))(d) < 1 for d in D)
assert sp.limit(dy_dgb, et, 0) == 0

# ------------------------------------------------------------- Q2(a): Euler, AD, slope, shifters
lm, Pp, Pbp, uC, uCb = sp.symbols("lambda P Pbar u_C u_Cbar", positive=True)
foc = sp.solve([sp.Eq(uC, lm * Pp), sp.Eq(beta * uCb, lm * Pbp / (1 + i))], [uC, uCb], dict=True)[0]
zero(foc[uC] / (beta * foc[uCb]) - (1 + i) * Pp / Pbp)
c, cb = sp.symbols("c cbar", real=True)
euler = sp.Eq((cb - c) / st - sp.log(beta), i + p - pb)    # log of (3) with u_c = C^(-1/sigma_t), ln(1+i) ~ i
zero(sp.solve(euler, cb)[0] - c - st * (i - (pb - p) + sp.log(beta)))         # rho = -ln beta
yAD = sp.solve(euler.subs({c: (y - g) / sc, cb: (ybn - gb) / sc}), y)[0]
zero(yAD - (ybn + (g - gb) - st * sc * (i - (pb - p) + sp.log(beta))))        # (6) with sigma = sigma_t s_c
zero(sp.diff(sp.solve(sp.Eq(y, AD), p)[0], y) + 1 / sg)                        # slope -1/sigma
assert sp.diff(AD, i) == -sg and sp.diff(AD, g) == 1 and sp.diff(AD, pb) == sg
zero(sp.diff(AD, ab) - (1 + et) / inv)
zero(sp.diff(AD, mub) + 1 / inv)
zero(sp.diff(AD, gb) + et / inv)

# ------------------------------------------------------------- Q2(b): optimal flexible price
Pj, W, A, K, Y, G = sp.symbols("P_j W A K Y G", positive=True)
ty, tw, tl, tc = sp.symbols("tau_y tau_w tau_l tau_c", real=True)
PiT = ((1 - ty) * Pj - (1 + tw) * W / A) * (Pj / Pp) ** (-th) * K             # profits (10)
bracket = (1 - th) * (1 - ty) * Pj + th * (1 + tw) * W / A
zero(sp.diff(PiT, Pj) * Pj / ((Pj / Pp) ** (-th) * K) - bracket)               # sign of Pi' = sign of bracket
PT = th / (th - 1) * (1 + tw) / (1 - ty) * W / A
zero(bracket.subs(Pj, PT))
dPi = sp.lambdify((Pj, W, A, th), sp.diff(PiT.subs({ty: 0, tw: 0, Pp: 1, K: 1}), Pj), "math")
for d in D[:200]:                                                              # one sign change: unique max
    Wv, Av, t = random.uniform(0.5, 2), random.uniform(0.5, 2), d["th"]
    star = t / (t - 1) * Wv / Av
    grid = [Wv / Av * 0.5 * (40 * star / (Wv / Av)) ** (k / 400) for k in range(401)]
    sg_ = [dPi(x, Wv, Av, t) > 0 for x in grid]
    assert sg_[0] and not sg_[-1] and sum(s1 != s2 for s1, s2 in zip(sg_, sg_[1:])) == 1
    assert abs(brentq(lambda x: dPi(x, Wv, Av, t), grid[0], grid[-1]) - star) < 1e-7 * star

# ------------------------------------------------------------- Q2(c): planner, taxes, subsidy
U = (Y - G) ** (1 - 1 / st) / (1 - 1 / st) - (Y / A) ** (1 + et) / (1 + et)
zero(sp.diff(U, Y) - ((Y - G) ** (-1 / st) - (Y / A) ** et / A))
zero(sp.diff(U, Y, 2) + (Y - G) ** (-1 / st - 1) / st + et * (Y / A) ** (et - 1) / A ** 2)   # strictly concave
dU = sp.lambdify((Y, G, A, st, et), sp.diff(U, Y), "math")
for d in D[:200]:                                                              # unique root of the FOC
    Gv, Av, s_ = random.uniform(0.05, 1), random.uniform(0.5, 2), d["sg"]
    hi = Gv + 1.0
    while dU(hi, Gv, Av, s_, d["et"]) > 0:
        hi = Gv + 2 * (hi - Gv)
    grid = [Gv + (hi - Gv) * (k / 400) ** 3 for k in range(1, 401)]
    sg_ = [dU(x, Gv, Av, s_, d["et"]) > 0 for x in grid]
    assert sg_[0] and not sg_[-1] and sum(s1 != s2 for s1, s2 in zip(sg_, sg_[1:])) == 1
    brentq(lambda x: dU(x, Gv, Av, s_, d["et"]), grid[0], hi)
WP = sp.solve(sp.Eq(PT, Pp), W)[0] / Pp                                        # flexible prices: P_j = P
e_mu = th / (th - 1) * (1 + tw) * (1 + tc) / ((1 - ty) * (1 - tl))           # gross markup e^mu, (13)
zero((1 - tl) / (1 + tc) * WP - A / e_mu)                                    # v_l/u_c = A e^-mu via (7)
for tax, rhs in [(tw, e_mu / (1 + tw)), (tc, e_mu / (1 + tc)), (ty, e_mu / (1 - ty)), (tl, e_mu / (1 - tl))]:
    zero(sp.diff(e_mu, tax) - rhs)
    f = sp.lambdify((th, ty, tw, tl, tc), sp.diff(e_mu, tax), "math")      # > 0: tau_y, tau_l < 1; tau_w, tau_c > -1
    assert all(f(d["th"], *[random.uniform(-0.9, 0.9) for _ in range(4)]) > 0 for d in D)
zero(sp.diff(yn, mu) + 1 / inv)
assert sp.diff(ye, mu) == 0
sub_y = sp.solve(sp.Eq(e_mu.subs({tw: 0, tc: 0, tl: 0}), 1), ty)
sub_w = sp.solve(sp.Eq(e_mu.subs({ty: 0, tc: 0, tl: 0}), 1), tw)
assert len(sub_y) == 1 and len(sub_w) == 1
zero(sub_y[0] + 1 / (th - 1))
zero(sub_w[0] + 1 / th)
assert sp.limit(1 / (th - 1), th, sp.oo) == 0 and sp.limit(1 / (th - 1), th, 1, "+") == sp.oo
zero(sp.diff(1 / (th - 1), th) + 1 / (th - 1) ** 2)

# ------------------------------------------------------------- Q2(d): oil shock
yns = sp.Symbol("y_n", real=True)
eqd = sp.solve([sp.Eq(y, ybn - sg * (i - (pb - p) - rho)), sp.Eq(p - pe, kap * (y - yns))], [y, p], dict=True)[0]
rn = rho + (ybn - yns) / sg
zero(eqd[y] - yns - sg / (1 + sg * kap) * (rn - i + pb - pe))                 # gap formula
yn1, ye1 = kb                                                                  # y_n', y_e' (g = 0)
rn1 = rn.subs({ybn: 0, yns: yn1})
zero(rn1 - rho - (mu - (1 + et) * a) / (1 + sg * et))
assert sp.diff(rn1, mu).is_positive and sp.diff(rn1, a).is_negative            # both halves (mu up, a down) raise r_n
base = {ybn: 0, pb: 0, pe: 0, yns: yn1}
yE, pE = eqd[y].subs(base).subs(i, rho), eqd[p].subs(base).subs(i, rho)
zero(yE - yn1 + yn1 / (1 + sg * kap))                                          # gap (ybar_n - y_n')/(1+sigma kappa)
zero(yE - sg * kap * yn1 / (1 + sg * kap))
zero(pE + kap * yn1 / (1 + sg * kap))
zero(yE - ye1 - (-(1 + et) * a - sg * kap * mu) / (inv * (1 + sg * kap)))     # (1+eta)|a| = -(1+eta) a
F = {k: num(v) for k, v in dict(yn=yn1, ye=ye1, rn=rn1 - rho, y=yE, p=pE, gap=yE - ye1,
                                 cond=-(1 + et) * a - sg * kap * mu).items()}
signs = set()
for d in D:
    v = {k: f(d) for k, f in F.items()}
    assert v["yn"] < v["ye"] < 0 and v["rn"] > 0 and v["yn"] < v["y"] < 0 and v["p"] > 0
    assert (v["gap"] > 0) == (v["cond"] > 0)
    signs.add(v["gap"] > 0)
assert signs == {True, False}                                                  # sign of y - y_e' is ambiguous
yF, pF = eqd[y].subs(base).subs(i, rn1), eqd[p].subs(base).subs(i, rn1)
zero(yF - yn1)
zero(pF)
zero(yF - ye1 + mu / inv)
zero(sp.diff(yn1, a) - sp.diff(ye1, a))                                         # productivity moves y_n, y_e alike
assert sp.diff(ye1, mu) == 0 and sp.diff(yn1, mu) != 0                         # the markup moves only y_n
fig = {al: sp.Rational(3, 4), sg: sp.Rational(1, 2), et: sp.Rational(1, 5), a: -3, mu: 5}    # TikZ values
Fkp, Fyn, Fye = (1 - 0.75) * (1 / 0.5 + 0.2) / 0.75, ((1 + 0.2) * (-3) - 5) / (1 / 0.5 + 0.2), (1 + 0.2) * (-3) / (1 / 0.5 + 0.2)
FyE, FpE = 0.5 * Fkp * Fyn / (1 + 0.5 * Fkp), -Fkp * Fyn / (1 + 0.5 * Fkp)
for tex, exact in [(Fkp, kap), (Fyn, yn1), (Fye, ye1), (FyE, yE), (FpE, pE)]:
    assert abs(tex - float(exact.subs(fig))) < 1e-12
assert float((-(1 + et) * a - sg * kap * mu).subs(fig)) > 0 and Fyn < Fye < FyE < 0        # drawn case
assert abs(FpE + FyE / 0.5) < 1e-12 and abs(FpE - Fkp * (FyE - Fyn)) < 1e-12             # E' on AD and AS'
assert -5 < Fyn and FpE < 3.6                                                              # inside the axis

# ------------------------------------------------------------- Q2(e): markup shock alone
L = sp.Symbol("xi", positive=True)                                            # xi = (1-alpha)/alpha
Dl = 1 + L * (1 + sg * et)
zero(sp.diff((1 - al) / al, al) + 1 / al ** 2)
zero((sg * kap).subs(al, 1 / (1 + L)) - L * (1 + sg * et))                    # alpha = 1/(1+xi)
yn0, y0, p0 = yn1.subs(a, 0), yE.subs(a, 0), pE.subs(a, 0)
gap0 = y0 - yn0
zero(yn0 + sg * mu / (1 + sg * et))
zero(y0 + mu / inv * sg * kap / (1 + sg * kap))
zero(p0 - mu / inv * kap / (1 + sg * kap))
y0l, p0l, g0l = [e.subs(al, 1 / (1 + L)) for e in (y0, p0, gap0)]
zero(y0l + sg * mu * L / Dl)
zero(p0l - mu * L / Dl)
zero(g0l - sg * mu / ((1 + sg * et) * Dl))
ks = sp.Symbol("kappa", positive=True)
zero(sp.diff(ks / (1 + sg * ks), ks) - 1 / (1 + sg * ks) ** 2)
share = sg * ks / (1 + sg * ks)                                                # y / y_n
zero(y0 / yn0 - share.subs(ks, kap))
zero(sp.diff(share, ks) - sg / (1 + sg * ks) ** 2)                             # rises in kappa
zero(sp.diff(L * (1 + sg * et) / Dl, sg) - L * et / Dl ** 2)                  # rises in sigma (alpha, eta fixed)
zero(sp.diff(kap, et) - (1 - al) / al)                                         # higher eta steepens the AS
claims = [(y0l, L, -sg * mu / Dl ** 2), (p0l, L, mu / Dl ** 2), (g0l, L, -sg * mu / Dl ** 2),
          (y0l, sg, -mu * L * (1 + L) / Dl ** 2), (p0l, sg, -mu * et * L ** 2 / Dl ** 2),
          (g0l, sg, mu * (1 + L - L * sg ** 2 * et ** 2) / ((1 + sg * et) ** 2 * Dl ** 2)),
          (y0l, et, sg ** 2 * mu * L ** 2 / Dl ** 2), (p0l, et, -sg * mu * L ** 2 / Dl ** 2),
          (g0l, et, -sg ** 2 * mu * (1 + 2 * L * (1 + sg * et)) / ((1 + sg * et) ** 2 * Dl ** 2)),
          (yn0, sg, -mu / (1 + sg * et) ** 2), (yn0, et, sg ** 2 * mu / (1 + sg * et) ** 2)]
for e, v, rhs in claims:
    zero(sp.diff(e, v) - rhs)
table = {"y_n": (yn0, (0, -1, 1, -1)), "y": (y0, (1, -1, 1, -1)),          # columns: alpha, sigma, eta, mu
         "p-p^e": (p0, (-1, -1, -1, 1)), "y-y_n": (gap0, (1, None, -1, 1))}
for name, (e, row) in table.items():
    for v, s in zip((al, sg, et, mu), row):
        de = sp.diff(e, v)
        if s == 0:
            assert sp.simplify(de) == 0, name
            continue
        f = num(de)
        for d in D:
            gap_ = 1 / (1 - d["al"]) - (d["sg"] * d["et"]) ** 2
            if s is None and abs(gap_) < 1e-9:
                continue
            assert f(d) * (s if s is not None else (1 if gap_ > 0 else -1)) > 0, (name, v, d)
for d in D:                                                                    # y_n < y < 0 = y_e, p > p^e
    assert num(yn0)(d) < num(y0)(d) < 0 < num(p0)(d)
assert sp.limit(y0, al, 1, "-") == 0 and sp.limit(p0, al, 1, "-") == 0
zero(sp.limit(gap0, al, 1, "-") + yn0)
zero(sp.limit(y0, al, 0, "+") - yn0)
zero(sp.limit(p0, al, 0, "+") - mu / (1 + sg * et))
assert sp.limit(gap0, al, 0, "+") == 0
num_s = 1 + L - L * sg ** 2 * et ** 2
zero(num_s.subs(L, (1 - al) / al).subs(sg, 1 / (et * sp.sqrt(1 - al))))      # sigma* = 1/(eta sqrt(1-alpha))
zero(sp.diff(num_s, sg) + 2 * L * sg * et ** 2)                                # falls in sigma: single crossing
dgs = sp.lambdify((sg, al, et, mu), sp.diff(gap0, sg), "math")
for d in D[:200]:
    s_star = 1 / (d["et"] * math.sqrt(1 - d["al"]))
    r = brentq(lambda s: dgs(s, d["al"], d["et"], d["mu"]), s_star * 1e-3, s_star * 1e3, xtol=1e-14, rtol=1e-12)
    assert abs(r - s_star) < 1e-6 * s_star
    assert dgs(0.5 * r, d["al"], d["et"], d["mu"]) > 0 > dgs(2 * r, d["al"], d["et"], d["mu"])   # a maximum

print("practice-L7-check-b1: all checks passed")
