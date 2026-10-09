"""Practice list C v4 (symbolic), Block 2 = Questions 3-4 of practice-L5-L6-block2.tex.

Independent check of every closed form (sympy), every sign, limit and ordering (sympy limits or >= 300 random
admissible draws), every multiple-choice distractor (differs from the key at random draws), every existence or
uniqueness claim (root-finding at random draws), and the tick values hard-coded in the figure of Question 4(e).
Run from anywhere: python practice-L5-L6-check-b2.py   (aborts on the first failure).
"""
import math

import numpy as np
import sympy as sp
from scipy.optimize import brentq
from scipy.special import lambertw

rng = np.random.default_rng(20261007)
NDRAW = 300


def zero(expr, what):
    """Assert that the sympy expression `expr` simplifies to 0; `what` names the claim being checked."""
    res = sp.simplify(expr)
    if res != 0:  # x**(T+1) = x * x**T is not applied by simplify on its own
        res = sp.simplify(sp.expand_power_exp(sp.expand(expr)))
    assert res == 0, f"{what}: residual {res}"


def branch(expr):
    """Generic branch of a Piecewise returned by sp.summation: the |x|<1 branch of an infinite geometric-type sum,
    else the branch whose condition is True (the x != 1 branch of a finite one)."""
    if not isinstance(expr, sp.Piecewise):
        return expr
    for val, cond in expr.args:
        if isinstance(cond, (sp.StrictLessThan, sp.LessThan)):
            return val
    for val, cond in expr.args:
        if cond == sp.true:
            return val
    raise AssertionError(f"no generic branch in {expr}")


def differ(fk, fd, args, what):
    """Assert that distractor value fd differs from key value fk at the same admissible draw."""
    vk, vd = fk(*args), fd(*args)
    assert abs(vk - vd) > 1e-9 * max(1.0, abs(vk)), f"{what} equals the key at {args}"


# ============================ Q3(a): Baumol-Tobin, Bailey area ============================
F, Y, i, x, N = sp.symbols("F Y i x N", positive=True)
cost = F * N + i * Y / (2 * N)
Nst = sp.sqrt(i * Y / (2 * F))
zero(sp.diff(cost, N).subs(N, Nst), "3a FOC")
zero(sp.diff(cost, N, 2) - i * Y / N**3, "3a second derivative iY/N^3 (>0)")
m_i = sp.sqrt(F * Y / (2 * i))
zero(Y / (2 * Nst) - m_i, "3a m(i)")
area = sp.integrate(m_i.subs(i, x), (x, 0, i))
zero(area - sp.sqrt(2 * F * Y * i), "3a integral of demand")
W = sp.sqrt(F * Y * i / 2)
zero(area - i * m_i - W, "3a Bailey area")
zero(W - F * Nst, "3a W = F N*")
C = cost.subs(N, Nst)
zero(C - area, "3a C(i) = area under demand")
zero(sp.diff(C, i) - m_i, "3a envelope C' = m")
assert sp.limit(C, i, 0, "+") == 0, "3a C(0+) = 0"
zero(i * m_i - F * Nst, "3a forgone interest = trip cost at the optimum")
zero(sp.sqrt(2 * F * Y * i) - 2 * W, "3a option B = C(i) = 2W")
zero(i * m_i / 2 - sp.sqrt(F * Y * i / 8), "3a option C = triangle i m / 2")
NB, mB = sp.sqrt(i * Y / F), sp.sqrt(F * Y / i)
zero(sp.diff(F * N + i * Y / N, N).subs(N, NB), "3a option A: FOC with average balance Y/N")
zero(Y / NB - mB, "3a option A: m = sqrt(FY/i)")
zero(i * mB / 2 - sp.sqrt(F * Y * i / 4), "3a option A = triangle with average balances")
opt_a = {k: sp.lambdify((F, Y, i), v) for k, v in  # the key is D
         {"A": sp.sqrt(F * Y * i / 4), "B": sp.sqrt(2 * F * Y * i), "C": sp.sqrt(F * Y * i / 8), "D": W}.items()}
for _ in range(NDRAW):
    arg = tuple(rng.uniform([0.01, 1.0, 1e-3], [10.0, 1e4, 0.5]))
    for k in "ABC":
        differ(opt_a["D"], opt_a[k], arg, f"3a distractor {k}")

# ============================ Q3(b): Cagan jump on news ============================
a, th = sp.symbols("a theta", positive=True)
k = sp.symbols("k", integer=True, positive=True)
j = sp.symbols("j", integer=True, nonnegative=True)
lam = a / (1 + a)
mt, pt, pt1 = sp.symbols("m_t p_t p_tp1")
zero(sp.solve(sp.Eq(mt - pt, -a * (pt1 - pt)), pt)[0] - (mt / (1 + a) + lam * pt1), "3b p_t = m_t/(1+a) + lam p_t+1")
zero(1 / ((1 + a) * (1 - lam)) - 1, "3b weights sum to one")
tail = branch(sp.summation(lam**j, (j, k, sp.oo)))
zero(tail - lam**k / (1 - lam), "3b geometric tail")
zero(th / (1 + a) * tail - lam**k * th, "3b jump = lam^k theta")
s_ = sp.symbols("s", integer=True, positive=True)  # s = k - t >= 1: path p_t - m_old = lam^(k-t) theta
zero(-lam**s_ * th + a * (lam**(s_ - 1) - lam**s_) * th, "3b path solves m_t - p_t = -a(p_t+1 - p_t)")
opt_b = {key: sp.lambdify((a, k, th), v) for key, v in  # the key is C
         {"A": (1 - lam**k) * th, "B": lam**k * th / (1 + a), "C": lam**k * th, "D": (1 - lam**k) * th / (1 + a)}.items()}
for _ in range(NDRAW):
    av, kv, tv = rng.uniform(0.05, 20.0), int(rng.integers(1, 13)), rng.uniform(0.01, 1.0)
    for key in "ABD":
        differ(opt_b["C"], opt_b[key], (av, kv, tv), f"3b distractor {key}")
    lv, J = av / (1 + av), np.arange(4000)
    w = lv**J / (1 + av)
    assert abs(w[J >= kv].sum() * tv - opt_b["C"](av, kv, tv)) < 1e-9, "3b numeric forward sum (permanent)"
    assert abs(tv - w[J >= kv].sum() * tv - opt_b["A"](av, kv, tv)) < 1e-9, "3b option A = rise still to come"
    temp = w[kv - np.arange(kv + 1)] * tv                      # one-off rise of m_k: p_t - p_old for t = 0..k
    assert np.all(np.diff(temp) > 0) and abs(temp[-1] - tv / (1 + av)) < 1e-12, "3b temporary path peaks at k"
    assert abs(temp[0] - opt_b["B"](av, kv, tv)) < 1e-12, "3b option B = impact of a one-off rise of m_k"
    assert abs(temp[-1] - temp[0] - opt_b["D"](av, kv, tv)) < 1e-12, "3b option D = rise still to come, temporary"

# ============================ Q3(d): Darby effect ============================
tau, rbar, pe, ii = sp.symbols("tau rbar pi_e i", positive=True)
isol = sp.solve(sp.Eq((1 - tau) * ii - pe, rbar), ii)[0]
zero(isol - (rbar + pe) / (1 - tau), "3d i")
zero(sp.diff(isol, pe) - 1 / (1 - tau), "3d di/dpi_e")
zero(isol - pe - (rbar + tau * pe) / (1 - tau), "3d before-tax real rate")
zero(sp.diff(isol - pe, pe) - tau / (1 - tau), "3d its slope")
zero(sp.diff(isol, pe).subs(tau, 0) - 1, "3d tau = 0: one-for-one Fisher effect")
for tv in rng.uniform(1e-4, 1 - 1e-4, NDRAW):
    assert 1 / (1 - tv) > 1 and tv / (1 - tv) > 0, "3d signs"

# ============================ Q3(c) and Q4(d): forward-looking Cagan path ============================
mu1, mu2, mts, m0 = sp.symbols("mu1 mu2 m_ts m0", real=True)
Tn = sp.symbols("T", integer=True, positive=True)
tt = sp.symbols("t", integer=True)
D = mu2 - mu1
Sj = branch(sp.summation(j * lam**j, (j, 0, sp.oo)))
zero(Sj - lam / (1 - lam)**2, "4d sum j lam^j")
zero(Sj / (1 + a) - a, "4d (1/(1+a)) sum j lam^j = a")
nn = sp.symbols("n", integer=True, nonnegative=True)
zero(lam**nn * Sj / (1 + a) - a * lam**nn, "4d shifted sum = lam^n * first sum = a lam^n")
zero(a * (1 - lam) - lam, "4d a(1 - lam) = lam")


def p_pre(t, m_t):
    """Price level for 0 <= t <= T (Question 4(d)); m_t is the log money stock at t."""
    return m_t + a * mu1 + a * D * lam**(Tn - t)


def p_post(m_t):
    """Price level for t >= T."""
    return m_t + a * mu2


zero((mts - p_pre(tt, mts)) + a * (p_pre(tt + 1, mts + mu1) - p_pre(tt, mts)), "4d path solves the condition, t < T")
zero((mts - p_post(mts)) + a * (p_post(mts + mu2) - p_post(mts)), "4d path solves the condition, t >= T")
zero(p_pre(Tn, mts) - p_post(mts), "4d continuity at T")
zero(p_pre(tt, mts + mu1) - p_pre(tt - 1, mts) - (mu1 + D * lam**(Tn - tt + 1)), "4d pi(s) for 1 <= s <= T")
zero(p_pre(0, m0) - (m0 + a * mu1) - a * D * lam**Tn, "4d jump on announcement")
kk = sp.symbols("kk", integer=True, positive=True)
fin = branch(sp.summation(lam**kk, (kk, 1, Tn)))
zero(fin - lam * (1 - lam**Tn) / (1 - lam), "4d finite geometric sum")
zero(a * D * lam**Tn + D * fin - a * D, "4d jump + cumulated excess = a Delta")
zero(sp.expand_log(sp.log(lam), force=True) + sp.expand_log(sp.log((1 + a) / a), force=True), "4d ln lam = -ln(1+1/a)")
for _ in range(NDRAW):
    av, Tv = rng.uniform(0.1, 10.0), int(rng.integers(1, 16))
    m1v = rng.uniform(0.0, 0.5)
    lv = av / (1 + av)
    hv = math.log(2) / math.log(1 + 1 / av)
    assert abs(lv**hv - 0.5) < 1e-12, "4d half-life"
    for m2v in (rng.uniform(m1v + 1e-3, 1.0), rng.uniform(-0.3, m1v - 1e-3)):  # 4(d) rise, 3(c) fall
        Dv = m2v - m1v
        steps = np.r_[np.zeros(1), np.where(np.arange(1, Tv + 4000) <= Tv, m1v, m2v)]
        mpath = np.cumsum(steps)                       # m_0 = 0, growth mu1 up to T, mu2 after
        w = lv**np.arange(3000) / (1 + av)
        p = np.array([w @ mpath[t:t + 3000] for t in range(Tv + 3)])
        formula = [mpath[t] + av * m1v + av * Dv * lv**(Tv - t) if t <= Tv else mpath[t] + av * m2v for t in range(Tv + 3)]
        assert np.max(np.abs(p - formula)) < 1e-8, "4d/3c numeric forward solution"
        pis = np.diff(p)                               # pi(s), s = 1..T+2
        assert np.allclose(pis[:Tv], m1v + Dv * lv**(Tv - np.arange(1, Tv + 1) + 1), atol=1e-8), "4d pi(s) formula"
        assert abs(pis[Tv] - m2v) < 1e-8, "4d pi = mu2 after T"
        ann = m1v + av * Dv * lv**Tv                   # inflation in the announcement period (old p_-1 = m_-1 + a mu1)
        assert abs((p[0] - (-m1v + av * m1v)) - ann) < 1e-8, "4d/3c announcement-period inflation"
        if Dv > 0:
            assert np.all(pis[:Tv] > m1v) and np.all(pis[:Tv] < m2v) and np.all(np.diff(pis[:Tv]) > 0), "4d bounds/monotone"
            assert ann > m1v, "4d jump up"
        else:
            assert np.all(pis[:Tv] < m1v) and ann < m1v, "3c (F): inflation falls below mu1 at once"
        assert abs(av * Dv * lv**Tv + Dv * sum(lv**q for q in range(1, Tv + 1)) - av * Dv) < 1e-10, "4d sum = a Delta"
        assert abs((mpath[Tv] - p[Tv]) + av * m2v) < 1e-8, "4d real balances at T = -a mu2"

# ============================ Q4(a): Laffer curve, roots, pi_L ============================
kap, pp, Ss = sp.symbols("kappa pi S", positive=True)
Sf = kap * pp * sp.exp(-a * pp)
S1d, S2d = sp.diff(Sf, pp), sp.diff(Sf, pp, 2)
zero(S1d - kap * sp.exp(-a * pp) * (1 - a * pp), "4a S'")
zero(S2d + a * kap * sp.exp(-a * pp) * (2 - a * pp), "4a S''")
assert sp.solve(sp.Eq(S1d, 0), pp) == [1 / a], "4a unique stationary point 1/a"
Smax_s = kap / (a * sp.E)
zero(Sf.subs(pp, 1 / a) - Smax_s, "4a S_max")
assert sp.limit(Sf, pp, sp.oo) == 0 and Sf.subs(pp, 0) == 0, "4a S(0) = 0, S -> 0"
assert sp.limit(1 / S1d, pp, 1 / a, "-") == sp.oo, "4a pi_L' -> oo as S -> S_max"
fS = sp.Function("pf")(Ss)  # implicit pi(S): S(pi(S)) = S
d1 = sp.diff(Sf.subs(pp, fS), Ss)
pi1d = sp.solve(sp.Eq(d1, 1), sp.diff(fS, Ss))[0]
pi2d = sp.diff(pi1d, Ss).subs(sp.diff(fS, Ss), pi1d)
zero((pi1d - 1 / S1d.subs(pp, fS)), "4a pi_L' = 1/S'")
zero((pi2d + S2d.subs(pp, fS) / S1d.subs(pp, fS)**3), "4a pi_L'' = -S''/S'^3")
zero(1 / S1d - sp.exp(a * pp) / (kap * (1 - a * pp)), "4a pi_L' closed form")


def piL(S, kv, av):
    """Low-branch inflation that raises seigniorage S (requires 0 < S < kv/(av e))."""
    return brentq(lambda q: kv * q * math.exp(-av * q) - S, 0.0, 1.0 / av, xtol=1e-15, rtol=1e-15, maxiter=500)


for _ in range(NDRAW):
    kv, av = rng.uniform(0.1, 5.0), rng.uniform(0.2, 10.0)
    smax = kv / (av * math.e)
    S = rng.uniform(0.01, 0.99) * smax
    grid = np.linspace(1e-9, 60 / av, 200001)
    f = kv * grid * np.exp(-av * grid) - S
    assert np.count_nonzero(np.diff(np.sign(f))) == 2, "4a exactly two roots"
    assert np.all(np.diff(kv * grid * np.exp(-av * grid))[grid[1:] < 1 / av] > 0), "4a S rises below 1/a"
    assert np.all(np.diff(kv * grid * np.exp(-av * grid))[grid[:-1] > 1 / av] < 0), "4a S falls above 1/a"
    lo = piL(S, kv, av)
    hi = brentq(lambda q: kv * q * math.exp(-av * q) - S, 1 / av, 60 / av, xtol=1e-14)
    assert abs(lo + lambertw(-av * S / kv, 0).real / av) < 1e-9 and abs(hi + lambertw(-av * S / kv, -1).real / av) < 1e-7
    assert S / kv < lo < math.e * S / kv and lo < 1 / av < hi, "4a bounds S/kappa < pi_L < eS/kappa"
    assert 1 / (kv * math.exp(-av * hi) * (1 - av * hi)) < 0, "4a pi_H' < 0"
    h = 1e-6 * S
    d1n = (piL(S + h, kv, av) - piL(S - h, kv, av)) / (2 * h)
    assert abs(d1n - math.exp(av * lo) / (kv * (1 - av * lo))) < 1e-5 * abs(d1n), "4a pi_L' numeric"
    assert -float(S2d.subs({kap: kv, a: av, pp: lo})) / float(S1d.subs({kap: kv, a: av, pp: lo}))**3 > 0, "4a pi_L'' > 0"
    big = rng.uniform(1.001, 3.0) * smax
    assert np.all(kv * grid * np.exp(-av * grid) - big < 0), "4a no root above S_max"

# ============================ Q4(b)-(c): debt, S2, ordering, Jensen, T* ============================
r, d, b0, S1, T, Sm, S0s = sp.symbols("r d b0 S1 T S_m S0", positive=True)
S0 = d + r * b0
bbar = (S1 - d) / r
bT = bbar + (1 + r)**T * (b0 - bbar)
zero(bT - ((1 + r)**T * b0 + (d - S1) * ((1 + r)**T - 1) / r), "4b b_T two forms")
zero(bT.subs(T, T + 1) - ((1 + r) * bT + d - S1), "4b b_T solves the debt equation")
zero(bT.subs(T, 0) - b0, "4b b_0")
zero(d + r * bbar - S1, "4b fixed point")
zero(r * (b0 - bbar) - (S0 - S1), "4b r(b0 - bbar) = S0 - S1")
zero(bT.subs(T, T + 1) - bT - (1 + r)**T * (S0 - S1), "4b debt increments (1+r)^t (S0 - S1)")
S2 = S1 + (1 + r)**T * (S0 - S1)
zero(d + r * bT - S2, "4b S2 = d + r b_T")
zero(S2 - S0 - ((1 + r)**T - 1) * (S0 - S1), "4c S2 - S0")
om = (1 + r)**(-T)
zero((1 - om) * S1 + om * S2 - S0, "4c discounted seigniorage unchanged")
Ti, tq = sp.symbols("T_i t_q", integer=True, nonnegative=True)
zero(r / (1 + r) * branch(sp.summation((1 + r)**(-tq), (tq, 0, sp.oo))) - 1, "4c weights sum to one")
zero(r / (1 + r) * branch(sp.summation((1 + r)**(-tq), (tq, Ti, sp.oo))) - (1 + r)**(-Ti), "4c tail weight omega")
Tstar = sp.log((Sm - S1) / (S0 - S1)) / sp.log(1 + r)
zero(S1 + sp.exp(Tstar * sp.log(1 + r)) * (S0 - S1) - Sm, "4c S2(T*) = S_max")
zero(sp.diff(Tstar, S1) - (1 / (S0 - S1) - 1 / (Sm - S1)) / sp.log(1 + r), "4e dT*/dS1")
zero(sp.diff(S2, S1) - (1 - (1 + r)**T), "4e dS2/dS1")
zero(sp.diff(S2, T) - (1 + r)**T * sp.log(1 + r) * (S0 - S1), "4e dS2/dT")
zero(sp.diff(S2, r) - (T * (1 + r)**(T - 1) * (S0 - S1) + (1 + r)**T * b0), "4e dS2/dr")
zero(sp.diff(S2, d) - (1 + r)**T, "4e dS2/dd")
zero(sp.diff(S2, b0) - r * (1 + r)**T, "4e dS2/db0")
zero(sp.diff(S2, T, 2) - (1 + r)**T * sp.log(1 + r)**2 * (S0 - S1), "4e d2S2/dT2 (>0)")
assert not (S2.free_symbols & {kap, a}) and T not in Tstar.free_symbols, "4e zero entries of the table"
g, hh = pp / (1 - a * pp), pp**2 / (1 - a * pp)
G = kap * pp * sp.exp(-a * pp) - Ss
zero(-sp.diff(G, Ss) / sp.diff(G, pp) - sp.exp(a * pp) / (kap * (1 - a * pp)), "4e dpi/dS")
zero(-sp.diff(G, kap) / sp.diff(G, pp) + g / kap, "4e dpi/dkappa = -G/kappa")
zero(-sp.diff(G, a) / sp.diff(G, pp) - hh, "4e dpi/da = H")
zero(sp.diff(g, pp) - 1 / (1 - a * pp)**2, "4e G' > 0")
zero(sp.diff(hh, pp) - pp * (2 - a * pp) / (1 - a * pp)**2, "4e H' > 0 on (0,1/a)")


def model(kv, av, rv, dv, b0v, s1v, Tv):
    """Outcomes of Question 4 at one parameter point: S2, pi_2, pi_2 - pi_1, T*, plus pi_0 and pi_1."""
    s0, smax = dv + rv * b0v, kv / (av * math.e)
    s2 = s1v + (1 + rv)**Tv * (s0 - s1v)
    p1, p2 = piL(s1v, kv, av), piL(s2, kv, av)
    return dict(S2=s2, pi2=p2, gap=p2 - p1, Tst=math.log((smax - s1v) / (s0 - s1v)) / math.log(1 + rv),
                pi0=piL(s0, kv, av), pi1=p1)


def draw():
    """One admissible point: S0 < S_max, d >= 0, b0 > 0, 0 < S1 < S0, 0 < T < T* (continuous T)."""
    kv, av, rv = rng.uniform(0.1, 5.0), rng.uniform(0.2, 10.0), rng.uniform(0.005, 0.2)
    smax = kv / (av * math.e)
    s0 = rng.uniform(0.05, 0.95) * smax
    b0v = rng.uniform(0.02, 0.98) * s0 / rv
    s1v = rng.uniform(0.05, 0.95) * s0
    tst = math.log((smax - s1v) / (s0 - s1v)) / math.log(1 + rv)
    return [kv, av, rv, s0 - rv * b0v, b0v, s1v, rng.uniform(0.05, 0.95) * tst]


NAMES = ["kap", "a", "r", "d", "b0", "S1", "T"]
TABLE = {"S2": dict(S1=-1, T=1, r=1, d=1, b0=1, kap=0, a=0),
         "pi2": dict(S1=-1, T=1, r=1, d=1, b0=1, kap=-1, a=1),
         "gap": dict(S1=-1, T=1, r=1, d=1, b0=1, kap=-1, a=1),
         "Tst": dict(S1=1, T=0, r=-1, d=-1, b0=-1, kap=1, a=-1)}
for _ in range(NDRAW):
    P = draw()
    out = model(*P)
    kv, av, rv, dv, b0v, s1v, Tv = P
    s0, smax = dv + rv * b0v, kv / (av * math.e)
    bb = b0v
    for _t in range(int(Tv)):
        bb = (1 + rv) * bb + dv - s1v
    assert abs(bb - float(bT.subs({r: rv, d: dv, b0: b0v, S1: s1v, T: int(Tv)}))) < 1e-9 * max(1, abs(bb)), "4b iteration"
    assert out["Tst"] > 0 and out["S2"] < smax, "4c T* > 0 and S2 < S_max for T < T*"
    assert out["pi1"] < out["pi0"] < out["pi2"], "4c pi_1 < pi_0 < pi_2"
    w = (1 + rv)**(-Tv)
    assert (1 - w) * out["pi1"] + w * out["pi2"] > out["pi0"], "4c Jensen: discounted inflation rises"
    s2_over = s1v + (1 + rv)**(out["Tst"] * rng.uniform(1.001, 1.5)) * (s0 - s1v)
    assert s2_over > smax, "4c beyond T* no steady state"
    for row, signs in TABLE.items():
        for name, sgn in signs.items():
            q = NAMES.index(name)
            hstep = 1e-6 * abs(P[q])
            up, dn = list(P), list(P)
            up[q] += hstep
            dn[q] -= hstep
            der = (model(*up)[row] - model(*dn)[row]) / (2 * hstep)
            if sgn == 0:
                assert der == 0.0, f"4e table {row}/{name} should be 0"
            else:
                assert np.sign(der) == sgn, f"4e table {row}/{name}: {der}"
    p1, p2 = out["pi1"], out["pi2"]
    hk, ha = 1e-6 * kv, 1e-6 * av
    dk = (model(kv + hk, *P[1:])["gap"] - model(kv - hk, *P[1:])["gap"]) / (2 * hk)
    assert abs(dk + (p2 / (1 - av * p2) - p1 / (1 - av * p1)) / kv) < 1e-4 * abs(dk), "4e gap kappa formula"
    da = (model(kv, av + ha, *P[2:])["gap"] - model(kv, av - ha, *P[2:])["gap"]) / (2 * ha)
    assert abs(da - (p2**2 / (1 - av * p2) - p1**2 / (1 - av * p1))) < 1e-4 * abs(da), "4e gap a formula"
    hT = 1e-3 * Tv
    sec = model(*P[:6], Tv + hT)["pi2"] - 2 * p2 + model(*P[:6], Tv - hT)["pi2"]
    assert sec > 0, "4e pi_2 convex in T"

# ============================ Q4(e): limits ============================
S2g = S1 + (1 + r)**T * (S0s - S1)
assert sp.limit(S2g, T, 0) == S0s and sp.simplify(S2g.subs(S1, S0s) - S0s) == 0, "4e T->0, S1->S0: S2 -> S0"
eps, dlt = sp.symbols("epsilon delta", positive=True)
assert sp.limit(sp.log((S0s + eps - S1) / (S0s - S1)) / sp.log(1 + r), S1, S0s, "-") == sp.oo, "4e T* -> oo as S1 -> S0"
assert sp.limit(S2, r, 0) == d, "4e r -> 0: S2 -> d"
qq = sp.symbols("q", positive=True)  # S1 = d - delta and S_max - S1 = delta (1 + q), so S_max > d
Tr = sp.log(dlt * (1 + qq) / (d + r * b0 - (d - dlt))) / sp.log(1 + r)
assert sp.limit(Tr, r, 0, "+") == sp.oo, "4e r -> 0: T* -> oo"
assert sp.limit(Smax_s, a, 0, "+") == sp.oo and sp.limit(lam, a, 0) == 0, "4e a -> 0: S_max -> oo, lam -> 0"
assert sp.simplify(sp.limit(-sp.LambertW(-a * Ss / kap) / a, a, 0, "+") - Ss / kap) == 0, "4e a -> 0: pi_L -> S/kappa"
for _ in range(50):
    kv, s0, s1v, rv = rng.uniform(0.5, 3), rng.uniform(0.05, 0.3), 0.0, rng.uniform(0.01, 0.1)
    s1v = rng.uniform(0.1, 0.9) * s0
    av, Tv = 1e-6, rng.uniform(1, 30)
    s2, w = s1v + (1 + rv)**Tv * (s0 - s1v), (1 + rv)**(-Tv)
    assert abs(piL(s0, kv, av) - s0 / kv) < 1e-4 * s0 / kv, "4e a -> 0 numeric pi_L"
    gap = (1 - w) * piL(s1v, kv, av) + w * piL(s2, kv, av) - piL(s0, kv, av)
    assert 0 < gap < 1e-4 * s0 / kv, "4e a -> 0: Jensen gap vanishes"
P = draw()
near = model(*P[:6], model(*P)["Tst"] * (1 - 1e-7))
assert near["pi2"] > 0.99 / P[1], "4e T -> T*: pi_2 -> 1/a"

# ============================ Figure of Q4(e): tick values and curve equation ============================
r_f, s0_f, smax_f = 0.05, 0.28, 1 / math.e
assert 0.12 < 0.22 < s0_f < smax_f
assert abs(piL(s0_f, 1.0, 1.0) - 0.4308) < 5e-5, "figure pi_0 tick"
for s1f, tick in ((0.12, 8.972), (0.22, 18.488)):
    assert abs(math.log((smax_f - s1f) / (s0_f - s1f)) / math.log(1 + r_f) - tick) < 5e-4, "figure T* tick"
    for Tv in rng.uniform(0.01, 0.99, 50) * tick:
        p2 = piL(s1f + (1 + r_f)**Tv * (s0_f - s1f), 1.0, 1.0)
        assert abs(math.log((p2 * math.exp(-p2) - s1f) / (s0_f - s1f)) / math.log(1 + r_f) - Tv) < 1e-8, "plotted curve"

print("practice-L5-L6-check-b2.py: all checks passed")
