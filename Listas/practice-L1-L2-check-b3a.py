"""Checks every result of Question 5 (Block 3 objective items) of practice-L1-L2, symbolic version.

Closed forms are verified with sympy; signs, orderings and limits symbolically or at random
admissible draws; each multiple-choice distractor must differ from the key. Any mismatch aborts
with an AssertionError. Run from anywhere: python practice-L1-L2-check-b3a.py
"""
import math
import os
import random

import sympy as sp
from scipy.integrate import quad

random.seed(20261007)
N = 300  # random admissible draws per check


def zero(expr):
    """True when expr simplifies to 0; logs are expanded first so symbolic exponents cancel."""
    return sp.simplify(sp.expand_log(expr, force=True)) == 0


al, s, p, m, q = sp.symbols('alpha s p m q', positive=True)   # m = n+g+delta; alpha = q/(1+q) in limits

# ---------------------------------------------------------------- (a) PPP x growth (key B)
sB, sU, pU, pi = sp.symbols('s_B s_U p_U pi', positive=True)
kss = (s / (p * m)) ** (1 / (1 - al))
assert zero(sp.log((s / p) * kss ** al) - sp.log(m * kss))          # steady state of (s/p)k^a = m k
yss = lambda s_, p_: (s_ / (p_ * m)) ** (al / (1 - al))
assert zero(sp.log(kss ** al) - sp.log(yss(s, p)))
key_a = (sB / (pi * sU)) ** (al / (1 - al))
assert zero(sp.log(yss(sB, pi * pU) / yss(sU, pU)) - sp.log(key_a))  # ratio with p_B = pi p_U
assert sp.simplify(pU * (sB / (pi * pU)) - sB / pi) == 0              # p_U I_B / Y_B = s_B / pi
assert zero(sp.log(key_a.subs(sB, sU)) - sp.log(pi ** (-al / (1 - al))))
dist_a = {'A': (sB / (pi * sU)) ** (1 / (1 - al)), 'C': (sB / sU) ** al, 'D': (sB / (pi * sU)) ** al}
k_of = lambda s_, p_: kss.subs({s: s_, p: p_})
assert zero(sp.log(k_of(sB, pi * pU) / k_of(sU, pU)) - sp.log(dist_a['A']))   # A: capital ratio
k_naive = lambda s_, p_: s_ / (p_ * m)                              # k* proportional to s/p: no multiplier
assert zero(sp.log((k_naive(sB, pi * pU) / k_naive(sU, pU)) ** al) - sp.log(dist_a['D']))  # D
assert zero(sp.log((k_naive(sB, pU) / k_naive(sU, pU)) ** al) - sp.log(dist_a['C']))       # C: and no pi
f_key = sp.lambdify((al, sB, sU, pi), key_a, 'math')
f_dist = {k_: sp.lambdify((al, sB, sU, pi), e, 'math') for k_, e in dist_a.items()}
for _ in range(N):
    v = (random.uniform(0.05, 0.95), random.uniform(0.05, 0.6), random.uniform(0.05, 0.6),
         random.uniform(1.05, 4.0))
    kv = f_key(*v)
    assert v[3] ** (-v[0] / (1 - v[0])) < 1                          # gap with s_B = s_U
    for name, f in f_dist.items():
        assert abs(f(*v) - kv) > 1e-9 * kv, ('a', name, v)

# ---------------------------------------------------------------- (b) accounts x Golden Rule (key B)
k = sp.symbols('k', positive=True)
F = sp.Function('f')
alphaK, vK = F(k).diff(k) * k / F(k), k / F(k)
assert sp.simplify(alphaK / vK - F(k).diff(k)) == 0                 # alpha_K / v = f'(k), any f
assert sp.simplify(m * k / F(k) - m * vK) == 0                      # BGP: s f = m k  =>  s = m v
a = sp.symbols('a', positive=True)
ces = k / (a + (1 - a) * k)                                         # CES, elasticity 1/2
assert sp.simplify(ces.diff(k) - a / (a + (1 - a) * k) ** 2) == 0
kgr_ces = (sp.sqrt(a / m) - a) / (1 - a)
assert sp.simplify(ces.diff(k).subs(k, kgr_ces) - m) == 0
techs = {
    'CD': (lambda k_, a_: k_ ** a_, lambda k_, a_: a_ * k_ ** (a_ - 1),
           lambda m_, a_: (a_ / m_) ** (1 / (1 - a_))),
    'CES': (lambda k_, a_: k_ / (a_ + (1 - a_) * k_), lambda k_, a_: a_ / (a_ + (1 - a_) * k_) ** 2,
            lambda m_, a_: (math.sqrt(a_ / m_) - a_) / (1 - a_)),
}
for name, (f, fp, kgr) in techs.items():
    for _ in range(N):
        a_, d_, ng = random.uniform(0.2, 0.6), random.uniform(0.01, 0.1), random.uniform(0.005, 0.06)
        rho_, m_ = random.uniform(0.005, 0.1), ng + d_
        kg, kmgr = kgr(m_, a_), kgr(m_ + rho_, a_)                  # f'(k_mgr) = rho + n + g + delta
        assert kg > 0 and abs(fp(kg, a_) - m_) < 1e-9
        assert 0 < kmgr < kg and abs(fp(kmgr, a_) - m_ - rho_) < 1e-9
        k_ = kg * random.uniform(0.2, 3.0)
        aK, v_ = fp(k_, a_) * k_ / f(k_, a_), k_ / f(k_, a_)
        assert (aK / v_ - d_ > ng) == (k_ < kg), (name, a_, k_, kg)   # key B <=> below GR
        assert (aK > m_ * v_) == (k_ < kg)                             # alpha_K > s on the BGP
        assert (aK / v_ - d_ > rho_ + ng) == (k_ < kmgr)              # D <=> below the modified GR
disagree, c_errors = {'A': 0, 'C': 0, 'D': 0}, set()
for _ in range(N):
    ng, d_, rho_ = random.uniform(0.005, 0.06), random.uniform(0.01, 0.1), random.uniform(0.005, 0.1)
    x = random.uniform(0.0, 0.3)                                    # x = alpha_K / v
    thr = {'key': ng + d_, 'A': ng, 'C': rho_ + ng, 'D': rho_ + ng + d_}
    efficient = x > thr['key']
    for name in disagree:
        assert abs(thr[name] - thr['key']) > 1e-12
        passes = x > thr[name]
        if passes != efficient:                                     # A passes inefficient, D fails efficient,
            disagree[name] += 1                                     # C does the first iff rho < delta
            assert passes == {'A': True, 'D': False, 'C': rho_ < d_}[name], (name, x, thr)
            c_errors |= {passes} if name == 'C' else set()
assert min(disagree.values()) >= N // 50 and c_errors == {True, False}, (disagree, c_errors)

# ---------------------------------------------------------------- (c) welfare x discounting (F)
t, s0, s1, rho = sp.symbols('t s_0 s_1 rho', positive=True)
z = s1 / m + (s0 - s1) / m * sp.exp(-(1 - al) * m * t)              # z = k^(1-alpha), exact path
assert sp.simplify(z.diff(t) - (1 - al) * (s1 - m * z)) == 0
assert sp.simplify(z.subs(t, 0) - s0 / m) == 0
kpath = z ** (1 / (1 - al))
D_of = lambda Z: sp.log((1 - s1) / (1 - s0)) + al / (1 - al) * sp.log(Z * m / s0)
D = D_of(z)
c0ss = (1 - s0) * (s0 / m) ** (al / (1 - al))
assert zero(sp.log((1 - s1) * kpath ** al) - sp.log(c0ss) - D)      # D = ln c1(t) - ln c0*
D0 = sp.log((1 - s1) / (1 - s0))
assert zero(D.subs(t, 0) - D0)
Dp = al * (s1 / z - m)                                              # = alpha kdot/k
assert sp.simplify(D.diff(t) - Dp) == 0
Dp0 = al * m * (s1 - s0) / s0
assert sp.simplify(Dp.subs(t, 0) - Dp0) == 0
Dinf = sp.log((1 - s1) / (1 - s0)) + al / (1 - al) * sp.log(s1 / s0)
assert sp.limit(z.subs(al, q / (1 + q)), t, sp.oo) == s1 / m        # z -> s1/m, so D -> D_of(s1/m)
assert zero(D_of(s1 / m) - Dinf)
assert sp.limit(Dp0 / rho, rho, sp.oo) == 0                        # the bound D(0) + D'(0)/rho -> D(0)
lnc = sp.log((1 - s) * (s / m) ** (al / (1 - al)))
assert sp.simplify(sp.expand_log(lnc, force=True).diff(s) - (al - s) / ((1 - al) * s * (1 - s))) == 0
kgr_cd = (al / m) ** (1 / (1 - al))                                 # s_GR = alpha: f'(k*(alpha)) = m
assert zero(sp.log(al * kgr_cd ** (al - 1)) - sp.log(m))
args = (al, s0, s1, m, t)
f_k, f_res = sp.lambdify(args, kpath, 'math'), \
    sp.lambdify(args, kpath.diff(t) - (s1 * kpath ** al - m * kpath), 'math')
f_D, f_Dp, f_Dpp = (sp.lambdify(args, e, 'math') for e in (D, Dp, D.diff(t, 2)))
f_D0, f_Dp0, f_Dinf = (sp.lambdify((al, s0, s1, m), e, 'math') for e in (D0, Dp0, Dinf))


def disc(fun, r, prm):
    """Integral of e^{-r t} fun(prm, t) over [0, inf); prm = (alpha, s0, s1, m)."""
    return quad(lambda tt: math.exp(-r * tt) * fun(*prm, tt), 0, math.inf,
                epsabs=1e-13, epsrel=1e-11, limit=400)[0]


for _ in range(N):
    al_ = random.uniform(0.1, 0.7)
    s0_ = random.uniform(0.02, 0.9 * al_)
    s1_ = s0_ + random.uniform(0.05, 1.0) * (al_ - s0_)               # s0 < s1 <= s_GR = alpha
    prm = (al_, s0_, s1_, random.uniform(0.02, 0.15))
    d0, dp0, dinf = f_D0(*prm), f_Dp0(*prm), f_Dinf(*prm)
    assert d0 < 0 < dinf and dp0 > 0
    for tt in (0.0, random.uniform(0, 30), random.uniform(30, 300)):
        kk = f_k(*prm, tt)
        assert abs(f_res(*prm, tt)) <= 1e-9 * max(1.0, kk)            # k(t) solves the Solow ODE
        assert 0 < f_Dp(*prm, tt) <= dp0 + 1e-12 and f_Dpp(*prm, tt) < 0
    r = random.uniform(0.005, 0.5)                                  # integration by parts
    lhs, rhs = r * disc(f_D, r, prm), d0 + disc(f_Dp, r, prm)
    assert abs(lhs - rhs) <= 1e-7 * (1 + abs(lhs)), (prm, r, lhs, rhs)
    rbar = dp0 / abs(d0)
    assert abs(rbar - prm[0] * prm[3] * (s1_ - s0_) / (s0_ * math.log((1 - s0_) / (1 - s1_)))) < 1e-12 * rbar
    for r in (rbar, rbar * random.uniform(1.0, 3.0)):               # Delta W < 0 for rho >= rho_bar
        rdw = r * disc(f_D, r, prm)
        assert d0 < rdw < d0 + dp0 / r <= 1e-12 and rdw < 0, (prm, r, rdw)
    r = 1e-9                                                        # rho -> 0: rho dW -> D(inf) > 0
    assert abs(d0 + disc(f_Dp, r, prm) - dinf) < 1e-4 * max(1.0, abs(dinf))

# ---------------------------------------------------------------- (d) measurement x growth (T)
A0, g, gkt = sp.symbols('A_0 g gk', positive=True)
kf = sp.Function('k', positive=True)(t)
y = A0 * sp.exp(g * t) * kf ** al
gy = sp.expand_log(sp.log(y), force=True).diff(t)
assert sp.simplify(gy - (g + al * kf.diff(t) / kf)) == 0            # ydot/y = g + alpha kdot/k
assert sp.simplify(sp.expand_log(sp.log((1 - s1) * y), force=True).diff(t) - gy) == 0
assert sp.simplify(al * (g + gkt) + (1 - al) * g - (g + al * gkt)) == 0   # growth accounting
gk = s1 / z - m                                                     # kdot/k on the exact path
assert sp.limit(gk.subs(al, q / (1 + q)), t, sp.oo) == 0
f_gk, f_dgk = sp.lambdify(args, gk, 'math'), sp.lambdify(args, gk.diff(t), 'math')
for _ in range(N):
    al_ = random.uniform(0.1, 0.9)
    s0_ = random.uniform(0.02, 0.9)
    s1_ = random.uniform(s0_ + 1e-3, 0.99)                          # any s1 in (s0, 1)
    m_ = random.uniform(0.02, 0.15)
    prm = (al_, s0_, s1_, m_)
    assert (1 - s1_) / (1 - s0_) < 1                                # consumption jumps down
    k0, k1 = (s0_ / m_) ** (1 / (1 - al_)), (s1_ / m_) ** (1 / (1 - al_))
    kk = k0 + random.uniform(0, 1) * (k1 - k0) * (1 - 1e-9)
    assert s1_ * kk ** (al_ - 1) - m_ > 0                            # kdot/k > 0 on [k0*, k1*)
    tt = random.uniform(0, 300)
    assert f_gk(*prm, tt) > 0 and f_dgk(*prm, tt) < 0                # excess growth falls to 0

print(f'{os.path.basename(__file__)}: all checks passed')
