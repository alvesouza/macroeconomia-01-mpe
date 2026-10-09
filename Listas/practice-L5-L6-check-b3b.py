"""Checks for Question 6 of practice list C (practice-L5-L6-block3b.tex): growth x equilibrium
interest rates x money demand x seigniorage x welfare, symbolic version.

Verifies every closed form (sympy simplify, else >= 400 random admissible draws), every claimed
sign (closed form plus draws), every limit (sp.limit), every ordering, and each existence or
uniqueness claim (bisection / nsolve at random draws). Aborts on the first mismatch.
Run: python practice-L5-L6-check-b3b.py
"""
import math
import random

import sympy as sp

random.seed(20261007)
NDRAW = 400

sig, b, a, k, i, x, c, R = sp.symbols('sigma beta a kappa i x c R', positive=True)
g = sp.Symbol('g', nonnegative=True)
mu = sp.Symbol('mu', real=True)
ps = sp.Symbol('pi_star', positive=True)
SYMS = (sig, g, b, a, k, mu, ps, i, x)


def draw(g_zero=False):
    """One admissible point: sigma>0, beta in (0,1), g>=0 with beta(1+g)^(1-sigma)<1, a, kappa>0,
    mu above the Friedman bound 1/A-1, pi*>0, and free i, x>0 for the welfare functions."""
    while True:
        s_, b_ = random.uniform(0.05, 5.0), random.uniform(0.5, 0.999)
        g_ = 0.0 if g_zero else random.uniform(0.0, 0.15)
        if b_ * (1 + g_) ** (1 - s_) < 1:
            break
    A_ = (1 + g_) ** (s_ - 1) / b_
    return {sig: s_, g: g_, b: b_, a: random.uniform(0.1, 20.0), k: random.uniform(0.01, 1.0),
            mu: random.uniform(1 / A_ - 1, 1 / A_), ps: random.uniform(0.001, 0.5),
            i: random.uniform(1e-3, 3.0), x: random.uniform(1e-3, 10.0)}


DRAWS = [draw(g_zero=(n % 4 == 0)) for n in range(NDRAW)]
_cache = {}


def num(expr, d):
    """Value of a sympy expression at draw d (lambdified once per expression)."""
    f = _cache.get(expr)
    if f is None:
        f = _cache[expr] = sp.lambdify(SYMS, expr, 'math')
    return f(*(d[s] for s in SYMS))


def same(lhs, rhs, msg):
    """lhs == rhs: sympy simplify, else relative gap <= 1e-9 at every random admissible draw."""
    if sp.simplify(lhs - rhs) == 0:
        return
    for d in DRAWS:
        u, v = num(lhs, d), num(rhs, d)
        assert abs(u - v) <= 1e-9 * (1 + abs(u) + abs(v)), (msg, d, u, v)


def sgn(v, tol=0.0):
    return 0 if abs(v) <= tol else (1 if v > 0 else -1)


def bisect(f, lo, hi, n=200):
    """Root of f on [lo, hi] given a sign change."""
    flo = f(lo)
    assert flo * f(hi) < 0
    for _ in range(n):
        mid = 0.5 * (lo + hi)
        if (f(mid) > 0) == (flo > 0):
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


# ---------------- (a) Euler, real rate, finite wealth, money market, Fisher ----------------
Rsol = sp.solve(sp.Eq(c ** (-sig), b * R * ((1 + g) * c) ** (-sig)), R)
assert len(Rsol) == 1
R_expr = (1 + g) ** sig / b                                    # 1 + r
assert sp.simplify(sp.expand_power_base(Rsol[0], force=True) - R_expr) == 0, 'Euler'
A = (1 + g) ** (sig - 1) / b
same((1 + g) / R_expr, b * (1 + g) ** (1 - sig), '(1+g)/(1+r)')
same(A, R_expr / (1 + g), 'A=(1+r)/(1+g)')
same(A, 1 / (b * (1 + g) ** (1 - sig)), 'A=1/(beta(1+g)^(1-sigma))')
t = sp.Symbol('t', positive=True)
assert sp.simplify(sp.expand_log(sp.log(b ** t * ((1 + g) ** t) ** (1 - sig)), force=True)
                   - sp.expand_log(sp.log((b * (1 + g) ** (1 - sig)) ** t), force=True)) == 0, 'utility ratio'
sides = [0, 0]
for _ in range(3000):                                          # finite wealth <=> r > g, both sides
    s_, b_, g_ = random.uniform(0.05, 2), random.uniform(0.3, 0.999), random.uniform(0, 1.0)
    ok = b_ * (1 + g_) ** (1 - s_) < 1
    assert ok == ((1 + g_) ** s_ / b_ - 1 > g_)
    sides[ok] += 1
assert min(sides) > 100
P = sp.Symbol('P', positive=True)                              # 1 + pi
Pt, Yt = sp.symbols('P_t Y_t', positive=True)
Mt = k * sp.exp(-a * i) * Pt * Yt
assert sp.simplify(Mt.subs({Pt: P * Pt, Yt: (1 + g) * Yt}) / Mt - P * (1 + g)) == 0, 'M growth'
lam1, I1 = sp.symbols('lambda1 I1', positive=True)              # lambda_{t+1}, 1 + i_t
fis = sp.solve(sp.Eq(b * R * lam1 / Pt, b * I1 * lam1 / (P * Pt)), I1)  # nominal-bond FOC, lambda_t from the real one
assert len(fis) == 1 and sp.simplify(fis[0] - R * P) == 0, 'Fisher from the two bond FOCs'
same(sp.solve(sp.Eq(1 + mu, P * (1 + g)), P)[0], (1 + mu) / (1 + g), '1+pi=(1+mu)/(1+g)')
I_MG = R_expr * (1 + mu) / (1 + g)                             # 1 + i under the money rule
same(I_MG, (1 + g) ** (sig - 1) * (1 + mu) / b, '1+i rule')
same(I_MG, A * (1 + mu), '1+i=A(1+mu)')
for d in DRAWS:
    assert num(A, d) > 1 and num(R_expr, d) > 1                # A>1, r>0
    assert num(I_MG, d) >= 1 - 1e-12                           # drawn mu admissible: i >= 0
    assert num(R_expr - 1, d) > d[g]                           # r > g

# ---------------- (b) regimes and the two forces ----------------
i_MG = I_MG - 1
same(sp.diff(i_MG, g), I_MG * (sig - 1) / (1 + g), 'di/dg rule')
I_IT = (1 + g) ** sig * (1 + ps) / b
same(I_IT, R_expr * (1 + ps), '1+i target')
MU_IT = (1 + ps) * (1 + g) - 1
same(sp.diff(MU_IT, g), 1 + ps, 'dmu/dg target')
same(sp.diff(I_IT, g), I_IT * sig / (1 + g), 'di/dg target')
for d in DRAWS:
    assert sgn(num(sp.diff(i_MG, g), d)) == sgn(d[sig] - 1)
    assert num(sp.diff(I_IT, g), d) > 0
    assert num(sp.diff((1 + mu) / (1 + g), g), d) < 0           # inflation falls with g (rule)
G = sp.Symbol('G', positive=True)


def elast(expr):
    return sp.simplify(sp.diff(sp.expand_log(sp.log(expr.subs(g, sp.exp(G) - 1)), force=True), G))


assert sp.simplify(elast(R_expr) - sig) == 0
assert sp.simplify(elast((1 + mu) / (1 + g)) + 1) == 0
assert sp.simplify(elast(I_IT) - elast(I_MG) - 1) == 0         # target exceeds rule by one

# ---------------- (c) seigniorage Laffer curve ----------------
i_of_mu = A * (1 + mu) - 1
s_mu = k * mu * sp.exp(-a * i_of_mu)
ds = sp.diff(s_mu, mu)
same(ds, k * sp.exp(-a * i_of_mu) * (1 - a * A * mu), "s'(mu)")
crit = sp.solve(ds, mu)
assert len(crit) == 1
mu_star = 1 / (a * A)
same(crit[0], mu_star, 'mu*')
same(mu_star, b * (1 + g) ** (1 - sig) / a, 'mu* explicit')
s2 = sp.diff(s_mu, mu, 2)
same(s2, k * a * A * sp.exp(-a * i_of_mu) * (a * A * mu - 2), "s''")
i_star = i_of_mu.subs(mu, mu_star)
same(i_star, A - 1 + 1 / a, 'i*')
same(s2.subs(mu, mu_star), -k * a * A * sp.exp(-a * i_star), "s''(mu*)")
same((sp.diff(-a * i_of_mu, mu) * mu).subs(mu, mu_star), -1, 'unit base elasticity at mu*')
s_max = k * mu_star * sp.exp(-a * i_star)
same(s_max, k / (a * A) * sp.exp(-1 - a * (A - 1)), 's_max (A form)')
same(s_max, k * b / (a * (1 + g) ** (sig - 1)) * sp.exp(-1 - a * ((1 + g) ** (sig - 1) / b - 1)), 's_max')
f_ds = sp.lambdify(SYMS, ds, 'math')
f_s = sp.lambdify(SYMS, s_mu, 'math')
for d in DRAWS[:250]:
    ms, smx, Ad = num(mu_star, d), num(s_max, d), num(A, d)
    lo, hi = 1 / Ad - 1, ms + 10 / (d[a] * Ad) + 1
    assert num(i_star, d) > 0 and ms > lo
    dd = dict(d)

    def fd(v):
        dd[mu] = v
        return f_ds(*(dd[s] for s in SYMS))

    root = bisect(fd, lo, hi)                                  # existence by root-finding
    assert abs(root - ms) <= 1e-9 * (1 + ms)
    changes, prev = 0, sgn(fd(lo))
    for j in range(1, 801):                                    # uniqueness and global maximum
        v = lo + (hi - lo) * j / 800
        cur = sgn(fd(v))
        changes += cur != prev and cur != 0
        prev = cur if cur != 0 else prev
        dd[mu] = v
        assert f_s(*(dd[s] for s in SYMS)) <= smx * (1 + 1e-12)
    assert changes == 1
same(sp.diff(A, g), (sig - 1) * A / (1 + g), 'dA/dg')
same(sp.diff(sp.log(mu_star), g) * (1 + g), 1 - sig, 'dln mu*/dln(1+g)')
same(sp.diff(i_star, g), (sig - 1) * A / (1 + g), 'di*/dg')
As = sp.Symbol('A', positive=True)
ln_smax = sp.log(k) - sp.log(a) - sp.log(As) - 1 - a * (As - 1)
same(sp.log(s_max), ln_smax.subs(As, A), 'ln s_max')
assert sp.simplify(sp.diff(ln_smax, As) + (1 / As + a)) == 0
same(sp.diff(sp.log(s_max), g), -(sig - 1) * (1 + a * A) / (1 + g), 'dln s_max/dg')
PiL = (1 + mu_star) / (1 + g)                                  # 1 + pi^L
same(PiL, 1 / (1 + g) + b / (a * (1 + g) ** sig), '1+pi^L')
for d in DRAWS:
    assert num(sp.diff(PiL, g), d) < 0
    assert sgn(num(sp.diff(mu_star, g), d)) == sgn(1 - d[sig])
    assert sgn(num(sp.diff(s_max, g), d)) == sgn(1 - d[sig])
    assert sgn(num(sp.diff(i_star, g), d)) == sgn(d[sig] - 1)

# ---------------- (d) Bailey area, Friedman rule, cost per unit of seigniorage ----------------
mm = sp.Symbol('m', positive=True)
m_of_i = k * sp.exp(-a * i)
inv = sp.log(k / mm) / a
assert sp.simplify(m_of_i.subs(i, inv) - mm) == 0, 'inverse demand'
W = k * ((1 - sp.exp(-a * i)) / a - i * sp.exp(-a * i))
same(sp.integrate(inv, (mm, m_of_i, k)), W, 'area under inverse demand')
same(sp.integrate(a * k * x * sp.exp(-a * x), (x, 0, i)), W, 'substituted integral')
same(sp.integrate(k * sp.exp(-a * x), (x, 0, i)) - i * m_of_i, W, 'surplus minus transfer')
dW = sp.diff(W, i)
same(dW, k * a * i * sp.exp(-a * i), "W'")
same(sp.diff(W, i, 2), k * a * sp.exp(-a * i) * (1 - a * i), "W''")
assert sp.simplify(W.subs(i, 0)) == 0 and sp.simplify(dW.subs(i, 0)) == 0
same(W, k / a * (1 - (1 + a * i) * sp.exp(-a * i)), 'W compact')
assert sp.simplify(sp.limit(W, i, sp.oo) - k / a) == 0
assert sp.simplify(sp.limit(W / (k * a * i ** 2 / 2), i, 0) - 1) == 0
same(k / a - W, k / a * (1 + a * i) * sp.exp(-a * i), 'gap to kappa/a (positive)')
for d in DRAWS:
    w = num(W, d)
    assert 0 < w < num(k * a * i ** 2 / 2, d) and w <= num(k / a, d) * (1 + 1e-12) and num(dW, d) > 0
    assert sgn(num(sp.diff(W, i, 2), d)) == sgn(1 - d[a] * d[i])
PF = sp.Symbol('PF', positive=True)                            # 1 + pi_F
PFs = sp.solve(sp.Eq(R_expr * PF, 1), PF)[0]
same(PFs, b / (1 + g) ** sig, '1+pi_F')
same(PFs * (1 + g), b * (1 + g) ** (1 - sig), '1+mu_F')
same(PFs - 1, -(R_expr - 1) / R_expr, 'pi_F=-r/(1+r)')
muF = b * (1 + g) ** (1 - sig) - 1
same(s_mu.subs(mu, muF), k * muF, 's(mu_F)=kappa mu_F')
for d in DRAWS:
    assert num(PFs, d) < 1 and num(muF, d) < 0
iT = I_IT - 1
WT = W.subs(i, iT)
sT = k * MU_IT * sp.exp(-a * iT)
same(WT / sT, (sp.exp(a * iT) - 1 - a * iT) / (a * MU_IT), 'average cost')
same(sp.diff(iT, ps), R_expr, 'di_T/dpi*')
same(sp.diff(MU_IT, ps), 1 + g, 'dmu_T/dpi*')
marg = sp.diff(WT, ps) / sp.diff(sT, ps)
same(marg, dW.subs(i, iT) * R_expr / (k * sp.exp(-a * iT) * ((1 + g) - a * MU_IT * R_expr)), 'marginal (middle)')
same(marg, a * A * iT / (1 - a * A * MU_IT), 'marginal cost')
pos = [0, 0]
for d in DRAWS:
    assert num(MU_IT, d) > 0 and num(iT, d) > 0 and num(WT / sT, d) > 0
    mt, ms = num(MU_IT, d), num(mu_star, d)
    assert (num(marg, d) > 0) == (mt < ms)
    pos[mt < ms] += 1
assert min(pos) > 10
ii, mt_ = sp.symbols('ii mt', positive=True)
assert sp.limit(a * As * ii / (1 - a * As * mt_), mt_, 1 / (a * As), dir='-') == sp.oo
assert abs(math.exp(-0.9) - 0.40657) < 5e-6                    # figure: m(i_T) tick with kappa=a=1

# ---------------- (e) sign table, q(x), limits ----------------
h = 1 - (1 + x) * sp.exp(-x)
q = x * sp.diff(h, x) - h
same(sp.diff(h, x), x * sp.exp(-x), "h'")
same(q, (1 + x + x ** 2) * sp.exp(-x) - 1, 'q')
same(sp.diff(q, x), x * (1 - x) * sp.exp(-x), "q'")
assert q.subs(x, 0) == 0 and sp.simplify(q.subs(x, 1) - (3 / sp.E - 1)) == 0
assert sp.simplify(q.subs(x, 2) - (7 / sp.E ** 2 - 1)) == 0
assert 3 / math.e - 1 > 0 and 7 / math.e ** 2 - 1 < 0 and sp.limit(q, x, sp.oo) == -1
fq = sp.lambdify(x, q, 'math')
xhat = bisect(fq, 1.0, 2.0)
assert abs(xhat - float(sp.nsolve(q, x, 1.8))) < 1e-10 and 1 < xhat < 2
for j in range(1, 6001):                                       # q>0 on (0,xhat), <0 beyond: unique root
    xv = 0.01 * j
    if abs(xv - xhat) > 1e-6:
        assert sgn(fq(xv)) == sgn(xhat - xv)
same(W, k * h.subs(x, a * i) / a, 'W=kappa h(ai)/a')
same(sp.diff(W, a), k * q.subs(x, a * i) / a ** 2, 'dW/da=kappa q(ai)/a^2')
assert sp.simplify(sp.limit(2 * h / x ** 2, x, 0) - 1) == 0
RESULTS = {'r': R_expr - 1, 'i_rule': i_MG, 'i_target': iT, 'mu_star': mu_star, 's_max': s_max, 'W_T': WT}
PARAMS = {'sigma': sig, 'g': g, 'beta': b, 'a': a, 'kappa': k}
TABLE = {  # expected sign as a function of the draw; 'dag' = + (or -) if g>0, 0 at g=0
    'r': {'sigma': 'dag+', 'g': 1, 'beta': -1, 'a': 0, 'kappa': 0},
    'i_rule': {'sigma': 'dag+', 'g': 'sgn(s-1)', 'beta': -1, 'a': 0, 'kappa': 0},
    'i_target': {'sigma': 'dag+', 'g': 1, 'beta': -1, 'a': 0, 'kappa': 0},
    'mu_star': {'sigma': 'dag-', 'g': 'sgn(1-s)', 'beta': 1, 'a': -1, 'kappa': 0},
    's_max': {'sigma': 'dag-', 'g': 'sgn(1-s)', 'beta': 1, 'a': -1, 'kappa': 1},
    'W_T': {'sigma': 'dag+', 'g': 1, 'beta': -1, 'a': 'xhat', 'kappa': 1},
}
seen_xhat = [0, 0]
for rn, rexpr in RESULTS.items():
    for pn, p in PARAMS.items():
        dexpr = sp.diff(rexpr, p)
        for d in DRAWS:
            e = TABLE[rn][pn]
            if e == 'dag+':
                e = 1 if d[g] > 0 else 0
            elif e == 'dag-':
                e = -1 if d[g] > 0 else 0
            elif e == 'sgn(s-1)':
                e = sgn(d[sig] - 1)
            elif e == 'sgn(1-s)':
                e = sgn(1 - d[sig])
            elif e == 'xhat':
                z = d[a] * num(iT, d)
                if abs(z - xhat) < 1e-6:
                    continue
                e = 1 if z < xhat else -1
                seen_xhat[z < xhat] += 1
            v = num(dexpr, d)
            assert sgn(v) == e, (rn, pn, d, v)  # zero entries are exact zeros (log(1+0) = 0)
assert min(seen_xhat) > 20
assert sum(d[g] == 0 for d in DRAWS) >= 100
# limits and knife-edges
assert sp.limit(R_expr, sig, 0) == 1 / b
assert sp.simplify(sp.limit(I_MG, sig, 0) - (1 + mu) / (b * (1 + g))) == 0
assert sp.simplify(sp.diff((1 + mu) / (b * (1 + g)), g) + (1 + mu) / (b * (1 + g) ** 2)) == 0
assert sp.simplify(sp.limit(mu_star, sig, 0) - b * (1 + g) / a) == 0
assert sp.simplify(sp.limit(b * (1 + g) ** (1 - sig), sig, 0) - b * (1 + g)) == 0
assert sp.simplify(I_MG.subs(sig, 1) - (1 + mu) / b) == 0
assert sp.simplify(mu_star.subs(sig, 1) - b / a) == 0
assert sp.simplify(sp.diff(s_max.subs(sig, 1), g)) == 0
assert sp.simplify(sp.diff(I_IT.subs(sig, 1), g) - (1 + ps) / b) == 0
assert sp.simplify(sp.limit(R_expr - 1, g, 0) - (1 / b - 1)) == 0
for rexpr in RESULTS.values():
    assert sp.simplify(sp.diff(rexpr, sig).subs(g, 0)) == 0
assert sp.simplify((I_MG - I_IT).subs(g, 0).subs(ps, mu)) == 0
assert sp.simplify(PFs.subs(g, 0) - b) == 0
assert sp.simplify(mu_star.subs(g, 0) - b / a) == 0
assert sp.simplify(s_max.subs(g, 0) - k * b / a * sp.exp(-1 - a * (1 / b - 1))) == 0
assert sp.limit(W, a, 0) == 0 and sp.limit(mu_star, a, 0) == sp.oo
Rr = sp.Symbol('Rr', positive=True)
assert sp.simplify(sp.diff(sp.log(Rr * (1 + ps)), Rr) * Rr - 1) == 0  # dln(1+i)/dln(1+r)=1 (target)

print('practice-L5-L6-check-b3b.py: all checks passed')
