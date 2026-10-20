"""Practice list P1-ADAS (practice-P1-adas.tex): sympy checks of every closed form, sign and number.

Run: python practice-P1-adas-check.py   (aborts on the first failed assert).
Each equilibrium is solved from the exam's AD and AS equations themselves (sp.solve), then compared
with the closed form printed in the answer key; signs are checked at random admissible draws.
"""
import random

import sympy as sp

random.seed(20261016)
N = 300

sg, et, kp, ph, rho = sp.symbols("sigma eta kappa phi rho", positive=True)
y, p = sp.symbols("y p", real=True)
Om = 1 / sg + et


def zero(expr):
    """Assert that a sympy expression simplifies to 0."""
    assert sp.simplify(expr) == 0, sp.simplify(expr)


def yn_of(a=0, g=0, mu=0):
    """Natural output (exam notation) for given a, g, mu."""
    return ((1 + et) * a + g / sg - mu) / Om


def ye_of(a=0, g=0):
    """Efficient output: y_n without the markup."""
    return ((1 + et) * a + g / sg) / Om


def eq(i=0, a=0, ab=0, mu=0, mub=0, g=0, gb=0, pb=0, pe=0):
    """Changes (dy, dp) solved from AD and AS, starting from y=y_n=ybar=0, p=p^e=pbar=0, i=rho."""
    yb = yn_of(ab, gb, mub)
    ad = sp.Eq(y, yb + (g - gb) - sg * (i - (pb - p)) + sg * rho)
    as_ = sp.Eq(p - pe, kp * (y - yn_of(a, g, mu)))
    s = sp.solve([ad, as_], [y, p], dict=True)[0]
    return s[y], s[p]


def i_for(target_y, **kw):
    """Policy rate that puts output at target_y (expression)."""
    ii = sp.Symbol("ii")
    return sp.solve(sp.Eq(eq(i=ii, **kw)[0], target_y), ii)[0]


def opt(**kw):
    """Optimal (dy, dp, i) by minimising the exam loss along AS, solved from dL/dy = 0."""
    yn = yn_of(kw.get("a", 0), kw.get("g", 0), kw.get("mu", 0))
    ye = ye_of(kw.get("a", 0), kw.get("g", 0))
    pe = kw.get("pe", 0)
    L = sp.Rational(1, 2) * (y - ye) ** 2 + ph / (2 * kp) * (kp * (y - yn)) ** 2
    ys = sp.solve(sp.diff(L, y), y)[0]
    assert sp.simplify(sp.diff(L, y, 2) - (1 + ph * kp)) == 0
    return ys, pe + kp * (ys - yn), i_for(ys, **kw)


D = [dict(sg=random.uniform(0.05, 5), et=random.uniform(0.02, 5), kp=random.uniform(0.02, 5),
          ph=random.uniform(0.01, 20), rho=random.uniform(0.001, 0.1)) for _ in range(N)]


def allpos(expr):
    """expr > 0 at every admissible draw (shock sizes set to 1; every use is linear in them)."""
    expr = expr.subs({s: 1 for s in expr.free_symbols - {sg, et, kp, ph, rho}})
    f = sp.lambdify((sg, et, kp, ph, rho), expr, "math")
    assert all(f(d["sg"], d["et"], d["kp"], d["ph"], d["rho"]) > 0 for d in D), expr


d = sp.Symbol("d", positive=True)  # size of a shock

# ---------------------------------------------------------------- Q1 temporary / permanent productivity fall
a = -d
dyn = (1 + et) * a / Om
dy, dp = eq(i=rho, a=a)
zero(dy - sg * kp * dyn / (1 + sg * kp)); zero(dp + kp * dyn / (1 + sg * kp))
zero(dy - dyn + dyn / (1 + sg * kp))                      # gap y - y_n = -dyn/(1+sk) > 0
zero(ye_of(a=a) - dyn)                                    # y_e moves with y_n
iPS = i_for(dyn, a=a); zero(iPS - rho + dyn / sg); allpos(iPS - rho)   # price stability: raise
zero(eq(i=iPS, a=a)[1])
dy, dp = eq(i=rho, a=a, ab=a); zero(dy - dyn); zero(dp)                # permanent: no gap, no price move
for k in (opt(a=a), opt(a=a, ab=a)):
    zero(k[0] - dyn); zero(k[1])                                      # optimum = price stability, any phi
zero(opt(a=a, ab=a)[2] - rho)

# ---------------------------------------------------------------- Q2 optimism (abar up) and mubar down
for kw, dyb in ((dict(ab=d), (1 + et) * d / Om), (dict(mub=-d), d / Om)):
    dy, dp = eq(i=rho, **kw)
    zero(dy - dyb / (1 + sg * kp)); zero(dp - kp * dyb / (1 + sg * kp))
    ys, ps, io = opt(**kw); zero(ys); zero(ps); zero(io - rho - dyb / sg); io = sp.simplify(io)
    assert not io.has(ph)
# figure Q2: sigma=1, kappa=.5, dybar=1 -> (2/3, 1/3)
v = {sg: 1, kp: sp.Rational(1, 2), et: sp.Rational(1, 2)}
dy, dp = eq(i=rho, mub=-sp.Rational(3, 2)); assert (dy.subs(v), dp.subs(v)) == (sp.Rational(2, 3), sp.Rational(1, 3))

# ---------------------------------------------------------------- Q3 temporary markup fall
mu = -d
dyn = -mu / Om
dy, dp = eq(i=rho, mu=mu)
zero(dy - sg * kp * dyn / (1 + sg * kp)); zero(dp + kp * dyn / (1 + sg * kp))
allpos(dy); allpos(-dp); allpos(-(dy - dyn))               # gaps of opposite sign: y-y_e>0, y-y_n<0
iPS = i_for(dyn, mu=mu); zero(iPS - rho + dyn / sg); allpos(rho - iPS)
iE = i_for(0, mu=mu); zero(iE - rho - kp * dyn); zero(eq(i=iE, mu=mu)[1] + kp * dyn)
ys, ps, io = opt(mu=mu)
zero(ys - ph * kp * dyn / (1 + ph * kp)); zero(ps + kp * dyn / (1 + ph * kp))
zero(io - rho + kp * dyn * (ph - sg) / (sg * (1 + ph * kp)))

# ---------------------------------------------------------------- Q4 targeting rule, comparative statics, phi-independence
W = sp.Symbol("W", positive=True)       # wedge y_e - y_n
L4 = sp.Rational(1, 2) * (y - W) ** 2 + ph / (2 * kp) * (kp * y) ** 2   # y_n = 0, y_e = W
yo = sp.solve(sp.diff(L4, y), y)[0]                                     # y* - y_n
zero(yo - W / (1 + ph * kp))
yme = yo - W; pmp = kp * yo
zero(yme + ph * kp * W / (1 + ph * kp)); zero(pmp - kp * W / (1 + ph * kp)); zero(yme + ph * pmp)
allpos(-sp.diff(pmp, ph) / W); allpos(sp.diff(pmp, kp) / W); allpos(-sp.diff(yme, ph) / W); allpos(-sp.diff(yme, kp) / W)
zero(sp.diff(pmp, ph) + kp ** 2 * W / (1 + ph * kp) ** 2); zero(sp.diff(pmp, kp) - W / (1 + ph * kp) ** 2)
zero(sp.diff(yme, ph) + kp * W / (1 + ph * kp) ** 2); zero(sp.diff(yme, kp) + ph * W / (1 + ph * kp) ** 2)
# Lista 7 Q4 mapping: phi_y = 1/2, phi_p = phi/(2 kappa), y* = y_e
fy, fp, ystar, yn0 = sp.symbols("phi_y phi_p ystar yn0", real=True)
L7 = fy * (y - ystar) ** 2 + fp * (kp * (y - yn0)) ** 2
rule = sp.diff(L7, y) / 2
zero(rule - (fy * (y - ystar) + kp * fp * kp * (y - yn0)))
zero(rule.subs({fy: sp.Rational(1, 2), fp: ph / (2 * kp)}) * 2 - ((y - ystar) + ph * kp * (y - yn0)))
# general di*: depends on phi iff dy_e != dy_n
dyn_, dye_, dybar = sp.symbols("dyn dye dybar", real=True)
dys = (dye_ + ph * kp * dyn_) / (1 + ph * kp); dps = kp * (dye_ - dyn_) / (1 + ph * kp)
di = (dybar - dys - sg * dps) / sg
zero(dys + sg * dps - dye_ - (sg - ph) * kp * (dye_ - dyn_) / (1 + ph * kp))
zero(sp.diff(di, ph) - kp * (dye_ - dyn_) * (1 + sg * kp) / (sg * (1 + ph * kp) ** 2))
zero(di.subs(dye_, dyn_) - (dybar - dyn_) / sg)

# ---------------------------------------------------------------- Q5 table: shifts and price-stabilising di
cases = dict(a=dict(a=d), ab=dict(ab=d), mu=dict(mu=d), mub=dict(mub=d), g=dict(g=d), gb=dict(gb=d),
             pb=dict(pb=d), pe=dict(pe=d))
expected_di = dict(a=-(1 + et) * d / (sg * Om), ab=(1 + et) * d / (sg * Om), mu=d / (sg * Om),
                   mub=-d / (sg * Om), g=et * d / (sg * Om), gb=-et * d / (sg * Om), pb=d, pe=-d)
for name, kw in cases.items():
    yn = yn_of(kw.get("a", 0), kw.get("g", 0), kw.get("mu", 0))
    iPS = i_for(yn, **kw)                                   # gap closed: p = p^e (+ dp^e)
    zero(iPS - rho - expected_di[name])
    zero(eq(i=iPS, **kw)[1] - kw.get("pe", 0))
    tradeoff = sp.simplify(yn - ye_of(kw.get("a", 0), kw.get("g", 0))) != 0
    assert tradeoff == (name == "mu"), name
# AD horizontal shift of gbar: dybar - dgbar = -eta/Om
zero(yn_of(g=d) - d - (-et * d / Om))

# ---------------------------------------------------------------- Q8 ZLB after mubar news
m = sp.Symbol("mbar", positive=True)
ireq = i_for(0, mub=m); zero(ireq - rho + m / (sg * Om))
zero(sp.solve(sp.Eq(ireq, 0), m)[0] - sg * Om * rho)
dy, dp = eq(i=0, mub=m)
zero(dy - (sg * rho - m / Om) / (1 + sg * kp)); zero(dp - kp * (sg * rho - m / Om) / (1 + sg * kp))
pbs = sp.solve(sp.Eq(eq(i=0, mub=m, pb=sp.Symbol("x"))[0], 0), sp.Symbol("x"))[0]
zero(pbs - (m / (sg * Om) - rho))
gs = sp.solve(sp.Eq(eq(i=0, mub=m, g=sp.Symbol("x"))[0] - yn_of(g=sp.Symbol("x")), 0), sp.Symbol("x"))[0]
zero(gs - (m - sg * Om * rho) / et)
zero(eq(i=0, mub=m, g=gs)[1])                                # fiscal fix keeps p = p^e

# ---------------------------------------------------------------- Q9 current mu and mubar news, general phi
m1, m2 = sp.symbols("dmu dmubar", positive=True)
dy, dp = eq(i=rho, mu=m1, mub=m2)
zero(dy + (m2 + sg * kp * m1) / (Om * (1 + sg * kp))); zero(dp - kp * (m1 - m2) / (Om * (1 + sg * kp)))
ys, ps, io = opt(mu=m1, mub=m2)
zero(ys + ph * kp * m1 / ((1 + ph * kp) * Om)); zero(ps - kp * m1 / ((1 + ph * kp) * Om))
dI = io - rho
zero(dI - (-m2 / (sg * Om) + kp * (ph - sg) * m1 / (sg * (1 + ph * kp) * Om)))
zero(sp.diff(dI, ph) - kp * m1 * (1 + sg * kp) / (sg * Om * (1 + ph * kp) ** 2))
assert not sp.simplify(sp.diff(dI, m2)).has(ph)                                  # news part free of phi
zero(sp.limit(dI, ph, sp.oo) - (m1 - m2) / (sg * Om)); zero(dI.subs(ph, 0) + m2 / (sg * Om) + kp * m1 / Om)
zero(i_for(yn_of(mu=m1), mu=m1, mub=m2) - rho - (m1 - m2) / (sg * Om))   # strict price stability
perm = dI.subs(m2, m1); zero(perm + m1 * (1 + sg * kp) / (sg * Om * (1 + ph * kp))); allpos(-perm / m1)
zero(sp.solve(sp.Eq(dI, 0), m2)[0] - kp * (ph - sg) * m1 / (1 + ph * kp))
# figure numbers: sigma=1, eta=.5, kappa=.5, phi=3, dmu=1.5, dmubar=.75
v = {sg: 1, et: sp.Rational(1, 2), kp: sp.Rational(1, 2), ph: 3, m1: sp.Rational(3, 2), m2: sp.Rational(3, 4)}
assert (dy.subs(v), dp.subs(v)) == (-sp.Rational(2, 3), sp.Rational(1, 6))
assert (ys.subs(v), ps.subs(v), dI.subs(v)) == (-sp.Rational(3, 5), sp.Rational(1, 5), -sp.Rational(1, 10))
assert ((m1 - m2) / (sg * Om)).subs(v) == sp.Rational(1, 2)          # strict price stability at (-1, 0)
assert ((-m2 / (sg * Om)).subs(v), (kp * (ph - sg) * m1 / (sg * (1 + ph * kp) * Om)).subs(v)) == (-sp.Rational(1, 2), sp.Rational(2, 5))

# ---------------------------------------------------------------- Q10 fiscal timing
D_ = sp.Symbol("Delta", positive=True)
res = {}
for name, kw in (("temp", dict(g=D_)), ("perm", dict(g=D_, gb=D_)), ("news", dict(gb=D_))):
    dy, dp = eq(i=rho, **kw)
    yn = yn_of(g=kw.get("g", 0))
    ys, ps, io = opt(**kw)
    zero(ys - yn); zero(ps); io = sp.simplify(io); assert not io.has(ph)
    res[name] = (dy, dp, sp.simplify(dy - yn), io - rho, ys)
zero(res["temp"][0] - D_ * (1 + kp / Om) / (1 + sg * kp)); zero(res["temp"][2] - et * D_ / (Om * (1 + sg * kp)))
zero(res["temp"][1] - kp * et * D_ / (Om * (1 + sg * kp))); zero(res["temp"][3] - et * D_ / (sg * Om))
zero(res["perm"][1]); zero(res["perm"][2]); zero(res["perm"][3]); zero(res["perm"][0] - D_ / (sg * Om))
zero(res["news"][0] + et * D_ / (Om * (1 + sg * kp))); zero(res["news"][3] + et * D_ / (sg * Om))
zero(res["temp"][3] + res["news"][3] - res["perm"][3])
for k in ("temp", "perm"):
    zero(res[k][4] - D_ / (sg * Om)); allpos(1 - 1 / (sg * Om))       # optimal multiplier < 1
zero(res["news"][4])
v = {sg: 1, et: sp.Rational(1, 2), kp: sp.Rational(1, 2), D_: sp.Rational(3, 2)}
assert [res["temp"][j].subs(v) for j in (0, 1)] == [sp.Rational(4, 3), sp.Rational(1, 6)]
assert [res["news"][j].subs(v) for j in (0, 1)] == [-sp.Rational(1, 3), -sp.Rational(1, 6)]
assert res["perm"][0].subs(v) == 1 and res["temp"][3].subs(v) == sp.Rational(1, 2)

print("practice-P1-adas-check: all assertions passed")
