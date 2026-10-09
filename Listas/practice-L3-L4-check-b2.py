"""Practice list B v4, Block 2 (Questions 3-4 of practice-L3-L4-block2.tex): symbolic checks.

Every closed form is checked with sympy; every sign, ordering and limit by a signed closed form,
sp.limit or random admissible draws; every MC distractor against the key at random draws; every
existence or uniqueness claim by root-finding. Aborts on the first failed assert.
Run from Listas/: python practice-L3-L4-check-b2.py
"""
import numpy as np
import sympy as sp
from scipy.optimize import brentq, minimize_scalar

rng = np.random.default_rng(20261007)
DRAWS = 300


def zero(expr):
    """Assert that a sympy expression simplifies to zero."""
    assert sp.simplify(expr) == 0, expr


def f(expr, *syms):
    """Numeric function of syms (numpy backend)."""
    return sp.lambdify(syms, expr, "numpy")


# ======================= Q3(a): temporary raise in k of N periods =======================
eps, psi, w, x = sp.symbols("epsilon psi w x", positive=True)
N, k = sp.symbols("N k", positive=True)
# exact solution: c_t = c, psi h_t^(1/eps) = w_t/c, N c = sum_t w_t h_t  =>  closed form for c
c_ex = (psi ** (-eps) * (k * (w * sp.exp(x)) ** (1 + eps) + (N - k) * w ** (1 + eps)) / N) ** (1 / (1 + eps))
lnh_raised = eps * (sp.log(w) + x - sp.log(psi) - sp.log(c_ex))
key_a = eps * (N - k) / N
zero(sp.diff(lnh_raised, x).subs(x, 0) - key_a)
# linearized system: all periods in the budget (key) vs only the raised ones (distractor D)
dc, dhr, dho, s_ = sp.symbols("dc dh_r dh_o s")
full = sp.solve([sp.Eq(dc, s_ * (1 + dhr) + (1 - s_) * dho), sp.Eq(dhr, eps * (1 - dc)), sp.Eq(dho, -eps * dc)],
                [dc, dhr, dho])
zero(full[dc] - s_)
zero(full[dhr].subs(s_, k / N) - key_a)
zero(full[dho].subs(s_, k / N) + eps * k / N)
partial = sp.solve([sp.Eq(dc, s_ * (1 + dhr)), sp.Eq(dhr, eps * (1 - dc))], [dc, dhr])
optD = eps * (N - k) / (N + k * eps)
zero(partial[dhr].subs(s_, k / N) - optD)
zero(key_a.subs(k, N))                                           # permanent raise: 0
# distractor B = static compensated elasticity of the same preferences (pi = nonlabor income, at pi = 0)
pi_, hh = sp.symbols("pi h", positive=True)
F = w / (w * hh + pi_) - psi * hh ** (1 / eps)
h0 = psi ** (-eps / (1 + eps))
zero(F.subs({pi_: 0, hh: h0}))
at0 = {pi_: 0, hh: h0}
zero((-sp.diff(F, w) / sp.diff(F, hh)).subs(at0))                # Marshallian = 0 at pi = 0
zero(-w * (-sp.diff(F, pi_) / sp.diff(F, hh)).subs(at0) - eps / (1 + eps))   # Hicksian = -w dh/dpi
optB = eps / (1 + eps)
# brute force: solve the N-period problem by root-finding and difference the log wage
for _ in range(DRAWS):
    e_, p_, w_ = rng.uniform(0.05, 5), rng.uniform(0.2, 5), rng.uniform(0.2, 5)
    n_ = int(rng.integers(2, 61)); k_ = int(rng.integers(1, n_))
    def lnh(dl):
        ws = np.array([w_ * np.exp(dl)] * k_ + [w_] * (n_ - k_))
        c = brentq(lambda c: n_ * c - np.sum(ws * (ws / (p_ * c)) ** e_), 1e-12, 1e12, xtol=1e-14, rtol=1e-14)
        return e_ * np.log(ws[0] / (p_ * c))
    el = (lnh(1e-5) - lnh(-1e-5)) / 2e-5
    key = e_ * (n_ - k_) / n_
    assert abs(el - key) < 1e-6, (el, key)
    for opt in (e_, e_ / (1 + e_), e_ * (n_ - k_) / (n_ + k_ * e_)):
        assert abs(opt - key) > 1e-9

# ======================= Q3(b): rigid wage in the search model =======================
Am, xi, U, V, y, wr, r, s, kap, th, om = sp.symbols("A_m xi U V y w r s kappa theta omega", positive=True)
zero((Am * U ** xi * V ** (1 - xi) / V).subs(V, th * U) - Am * th ** (-xi))


def el_theta(q_expr, wage):
    """d ln theta / d ln y implied by free entry (y - wage) q(theta) = (r+s) kappa (implicit function)."""
    G = sp.log(y - wage) + sp.log(q_expr) - sp.log((r + s) * kap)
    return sp.simplify(-sp.diff(G, y) / sp.diff(G, th) * y / th)


key_b = y / (xi * (y - wr))
zero(el_theta(Am * th ** (-xi), wr) - key_b)
optB_b = y / ((1 - xi) * (y - wr))
zero(el_theta(Am * th ** (-(1 - xi)), wr) - optB_b)            # exponents swapped
zero(el_theta(Am * th ** (-xi), om * y) - 1 / xi)               # wage proportional to y: no amplification
optC_b = 1 / (1 - xi)                                           # C: exponents swapped and wage proportional to y
zero(el_theta(Am * th ** (-(1 - xi)), om * y) - optC_b)
optD_b = (1 - xi) * key_b                                       # elasticity of f = A theta^(1-xi)
zero(sp.diff(sp.log(Am * th ** (1 - xi)), th) * th - (1 - xi))
fk, fB, fD = f(key_b, xi, y, wr), f(optB_b, xi, y, wr), f(optD_b, xi, y, wr)
for _ in range(DRAWS):
    xv, yv = rng.uniform(0.02, 0.98), rng.uniform(0.5, 5)
    wv = yv * rng.uniform(0.02, 0.98)
    kv = fk(xv, yv, wv)
    assert yv / (yv - wv) > 1
    for opt in (fB(xv, yv, wv), 1 / (1 - xv), fD(xv, yv, wv)):
        assert abs(opt - kv) > 1e-9

# ======================= Q3(c): Hosios with a general constant-returns M =======================
phi = sp.Symbol("phi", positive=True)
m = sp.Function("m")
tht = V / U
mprime = sp.diff(m(tht), V) * U                                 # m'(theta)
q_ = m(tht) / tht
etaV = tht * mprime / m(tht)
Wp = sp.diff(y * U * m(tht) - kap * V, V)
zero(Wp - (y * mprime - kap))
zero(Wp - ((1 - phi) * y * q_ - kap) - y * q_ * (etaV - (1 - phi)))   # the wedge identity
Mcrs = U * m(tht)
zero(U * sp.diff(Mcrs, U) + V * sp.diff(Mcrs, V) - Mcrs)        # Euler: eta_U + eta_V = 1
a_, b_ = sp.symbols("a b", positive=True)
Md = U ** a_ * V ** b_
zero(U * sp.diff(Md, U) / Md + V * sp.diff(Md, V) / Md - (a_ + b_))   # degree d: eta_U + eta_V = d
Mg = sp.Function("M")(U, V)                                     # any M: the vacancy version survives
zero(sp.diff(y * Mg - kap * V, V) - ((1 - phi) * y * Mg / V - kap)
     - y * Mg / V * (V * sp.diff(Mg, V) / Mg - (1 - phi)))
# numeric: CES matching m(theta) = A (1 + theta^-g)^(-1/g), not Cobb-Douglas
A_, g_ = sp.symbols("A g", positive=True)
m_ces = A_ * (1 + th ** (-g_)) ** (-1 / g_)
zero(th * sp.diff(m_ces, th) / m_ces - 1 / (1 + th ** g_))     # eta_V
m_f, mp_f, mpp_f = f(m_ces, th, A_, g_), f(sp.diff(m_ces, th), th, A_, g_), f(sp.diff(m_ces, th, 2), th, A_, g_)
for _ in range(DRAWS):
    Av, gv, yv, thp = rng.uniform(0.3, 2), rng.uniform(0.2, 3), rng.uniform(1, 5), rng.uniform(0.1, 5)
    assert mpp_f(rng.uniform(0.05, 20), Av, gv) < 0                # strictly concave in V
    kv = yv * mp_f(thp, Av, gv)                                    # thp is the planner's tightness
    etaU = thp ** gv / (1 + thp ** gv)
    def theta_e(ph):
        """Equilibrium tightness from free entry; 0 if no vacancy is profitable."""
        g = lambda t: (1 - ph) * yv * m_f(t, Av, gv) / t - kv
        return 0.0 if g(1e-9) <= 0 else brentq(g, 1e-9, 1e9, xtol=1e-14, rtol=1e-13)
    assert abs(theta_e(etaU) - thp) < 1e-7 * thp                    # phi = eta_U: efficient
    assert theta_e(0.5 * etaU) > thp                                # phi < eta_U: too many vacancies
    assert theta_e(etaU + 0.5 * (1 - etaU)) < thp                   # phi > eta_U: too few

# ======================= Q3(d) and Q4(a): labor supply with a transfer =======================
al, tau, T, wn, h = sp.symbols("alpha tau T w_n h", positive=True)
h_ind = sp.solve(sp.Eq(wn / (wn * h + T), al / (1 - h)), h)[0]
zero(h_ind - (1 / (1 + al) - al * T / ((1 + al) * wn)))
hw, hT = sp.diff(h_ind, wn), sp.diff(h_ind, T)
zero(hw - al * T / ((1 + al) * wn ** 2))
hw_cf = al * T / ((1 + al) * wn ** 2)                          # closed form checked just above
assert hw_cf.is_positive                                        # T > 0: hours rise with w_n
assert hw_cf.subs(T, -T).is_negative                            # T < 0: they fall
zero(sp.solve(sp.Eq(h_ind, 0), T)[0] - wn / al)                 # interior iff w_n > alpha T
zero(1 - h_ind - al / (1 + al) * (wn + T) / wn)                 # leisure = full income / price
h_bb = sp.solve(sp.Eq(h, h_ind.subs({wn: 1 - tau, T: tau * h})), h)
assert len(h_bb) == 1
h_bb = h_bb[0]
zero(h_bb - (1 - tau) / (1 + al - tau))
zero((1 - tau) / h_bb - al / (1 - h_bb))                        # FOC with c = h
hp = sp.diff(h_bb, tau)
zero(hp + al / (1 + al - tau) ** 2)
zero(h_bb.subs(tau, 0) - 1 / (1 + al))
zero(sp.solve(sp.diff(sp.log(h) + al * sp.log(1 - h), h), h)[0] - 1 / (1 + al))   # rebate internalized

# ======================= Q4(b): Laffer curve =======================
R = tau * h_bb
Nt = tau ** 2 - 2 * (1 + al) * tau + (1 + al)
zero(sp.diff(R, tau) - Nt / (1 + al - tau) ** 2)
zero(Nt.subs(tau, 0) - (1 + al)); zero(Nt.subs(tau, 1) + al)
roots = sp.solve(Nt, tau)
ts = (1 + al) - sp.sqrt(al * (1 + al))
assert any(sp.simplify(rt - ts) == 0 for rt in roots)
assert any(sp.simplify(rt - (1 + al + sp.sqrt(al * (1 + al)))) == 0 for rt in roots)
zero(ts - sp.sqrt(1 + al) * (sp.sqrt(1 + al) - sp.sqrt(al)))
zero(1 - ts - sp.sqrt(al) * (sp.sqrt(1 + al) - sp.sqrt(al)))
zero(1 + al - ts - sp.sqrt(al * (1 + al)))
Rs = (sp.sqrt(1 + al) - sp.sqrt(al)) ** 2
zero(R.subs(tau, ts) - Rs)
zero(Rs - 1 / (sp.sqrt(1 + al) + sp.sqrt(al)) ** 2)
zero(sp.diff(R, al) + tau * (1 - tau) / (1 + al - tau) ** 2)
fts, fRs, fR = f(ts, al), f(Rs, al), f(R, tau, al)
for av, tv, rv in [(0.1, 0.76834, 0.53668), (1.0, 0.58579, 0.17157)]:   # figure ticks
    assert abs(fts(av) - tv) < 5e-6 and abs(fRs(av) - rv) < 5e-6
for _ in range(DRAWS):
    av = np.exp(rng.uniform(np.log(0.01), np.log(50)))
    t_num = minimize_scalar(lambda t: -fR(t, av), bounds=(0, 1), method="bounded", options={"xatol": 1e-11}).x
    assert abs(t_num - fts(av)) < 1e-6 and 0.5 < fts(av) < 1
    assert 1 + av + np.sqrt(av * (1 + av)) > 1
    t_root = brentq(lambda t: t ** 2 - 2 * (1 + av) * t + (1 + av), 0, 1, xtol=1e-14)   # unique root in (0,1)
    assert abs(t_root - fts(av)) < 1e-9

# ======================= Q4(c): welfare cost =======================
Uw = lambda hx: sp.log(hx) + al * sp.log(1 - hx)
ln1mx = sp.log(1 - tau) + (1 + al) * sp.log((1 + al) / (1 + al - tau))
xc = 1 - (1 - tau) * ((1 + al) / (1 + al - tau)) ** (1 + al)
fdiff, fx = f(Uw(h_bb) - Uw(h_bb.subs(tau, 0)) - ln1mx, tau, al), f(xc, tau, al)
dln = sp.diff(ln1mx, tau)
zero(dln + al * tau / ((1 - tau) * (1 + al - tau)))
zero(dln.subs(tau, 0))
zero(xc.subs(tau, 0))
zero(sp.series(xc, tau, 0, 3).removeO() - al / (1 + al) * tau ** 2 / 2)
assert sp.simplify(sp.limit(xc, tau, 1, "-") - 1) == 0
for _ in range(DRAWS):
    av, tv = rng.uniform(0.01, 20), rng.uniform(0.01, 0.99)
    assert abs(fdiff(tv, av)) < 1e-10 and abs(1 - fx(tv, av) - np.exp(float(ln1mx.subs({tau: tv, al: av})))) < 1e-10
    assert fx(tv, av) > 0 and fx(tv + 1e-4, av) > fx(tv, av)

# ======================= Q4(d): four elasticities =======================
bb = {T: tau * h_bb, wn: 1 - tau}
eM = sp.simplify((wn * hw / h_ind).subs(bb))
zero(eM - al * tau / ((1 + al) * (1 - tau)))
hH = hw - h_ind * hT                                            # Slutsky: dT_comp = -h dw_n
zero(hH - al * (T + wn * h_ind) / ((1 + al) * wn ** 2))
eH = sp.simplify((wn * hH / h_ind).subs(bb))
zero(eH - al / ((1 + al) * (1 - tau)))
eBB = sp.simplify(-sp.diff(sp.log(h_bb), tau) * (1 - tau))
zero(eBB - (1 - h_bb)); zero(eBB - al / (1 + al - tau))
lam = sp.Symbol("lambda", positive=True)
h_fr = 1 - al / (lam * wn)                                      # alpha/(1-h) = lambda w_n
eF = sp.simplify(sp.diff(h_fr, wn) * wn / h_fr)
zero(eF - (1 - h_fr) / h_fr)
eF = al / (1 - tau)
zero(((1 - h) / h).subs(h, h_bb) - eF)
zero(eF - (1 + al) * eH)
zero(eM - tau * eH)                                             # e_H > e_M for tau < 1
zero(eH - eBB - al ** 2 * tau / ((1 + al) * (1 - tau) * (1 + al - tau)))
zero(eBB - eM - al * Nt / ((1 + al) * (1 - tau) * (1 + al - tau)))
Rp = sp.diff(R, tau)
zero(hp - (-hw + hT * Rp).subs(bb))                             # h' = -h_w + h_T R'
zero(eBB - eM - ((1 - tau) / h_ind * (-hT)).subs(bb) * Rp)
zero(eBB.subs(tau, ts) - (1 - ts) / ts)                         # tau* = 1/(1 + e_BB(tau*))
zero((eBB - eM).subs(tau, ts))
zero(eBB.subs(tau, 0) - eH.subs(tau, 0)); zero(eM.subs(tau, 0))
hi_f = f(h_ind, wn, T, al)
V_f = lambda wv, Tv, av: np.log(wv * hi_f(wv, Tv, av) + Tv) + av * np.log(1 - hi_f(wv, Tv, av))
fM, fH, fB2, fF = f(eM, tau, al), f(eH, tau, al), f(eBB, tau, al), f(eF, tau, al)
for _ in range(DRAWS):
    av, tv = rng.uniform(0.05, 10), rng.uniform(0.02, 0.95)
    h0v = (1 - tv) / (1 + av - tv); T0 = tv * h0v; w0 = 1 - tv; V0 = V_f(w0, T0, av)
    def h_comp(dl):
        """Hours when w_n = w0 e^dl and T keeps utility at V0 (compensated)."""
        wv = w0 * np.exp(dl)
        Tc = brentq(lambda Tx: V_f(wv, Tx, av) - V0, T0 - 0.5 * w0, T0 + 0.5 * w0, xtol=1e-15)
        return hi_f(wv, Tc, av)
    d = 1e-5
    assert abs((np.log(h_comp(d)) - np.log(h_comp(-d))) / (2 * d) - fH(tv, av)) < 1e-5
    eM_num = (np.log(hi_f(w0 * np.exp(d), T0, av)) - np.log(hi_f(w0 * np.exp(-d), T0, av))) / (2 * d)
    assert abs(eM_num - fM(tv, av)) < 1e-5
    assert fF(tv, av) > fH(tv, av) > fB2(tv, av)
    tsv = fts(av)
    if abs(tv - tsv) > 1e-6:
        assert (fB2(tv, av) > fM(tv, av)) == (tv < tsv)

# ======================= Q4(e): parameter analysis =======================
zero(sp.diff(h_bb, al) + (1 - tau) / (1 + al - tau) ** 2)
zero(sp.diff(eBB, al) - (1 - tau) / (1 + al - tau) ** 2)
zero(sp.diff(eBB, tau) - al / (1 + al - tau) ** 2)
dts = sp.diff(ts, al)
zero(dts - (1 - (1 + 2 * al) / (2 * sp.sqrt(al * (1 + al)))))
zero(sp.expand((1 + 2 * al) ** 2 - 4 * al * (1 + al)) - 1)
a, z = sp.symbols("a z", positive=True)
ga = sp.diff(a * sp.log(a / (a - tau)), a)
zero(ga - (sp.log(1 + z) - z).subs(z, tau / (a - tau)))
zero(sp.diff(sp.log(1 + z) - z, z) + z / (1 + z))
zero(sp.expand((al + sp.Rational(1, 2)) ** 2 - al * (1 + al)) - sp.Rational(1, 4))   # tau* > 1/2
fdts, fdRs = f(dts, al), f(sp.diff(Rs, al), al)
fdRa, fdRt, fdxa = f(sp.diff(R, al), tau, al), f(sp.diff(R, tau), tau, al), f(sp.diff(xc, al), tau, al)
xinf = 1 - (1 - tau) * sp.exp(tau)
for _ in range(DRAWS):
    av, tv, zv = np.exp(rng.uniform(np.log(0.01), np.log(50))), rng.uniform(0.01, 0.99), rng.uniform(1e-3, 50)
    assert fdts(av) < 0 and fdRs(av) < 0 and fdRa(tv, av) < 0 and fdxa(tv, av) > 0
    assert np.log1p(zv) - zv < 0
    assert fx(tv, av) < float(xinf.subs(tau, tv))
    if abs(tv - fts(av)) > 1e-6:
        assert (fdRt(tv, av) > 0) == (tv < fts(av))
lims = [(ts, 0, 1), (ts, sp.oo, sp.Rational(1, 2)), (Rs, 0, 1), (Rs, sp.oo, 0), (4 * al * Rs, sp.oo, 1),
        (h_bb, 0, 1), (h_bb, sp.oo, 0), (xc, 0, 0), (eBB, 0, 0), (eBB, sp.oo, 1)]
for expr, pt, val in lims:
    assert sp.simplify(sp.limit(expr, al, pt) - val) == 0, (expr, pt)
assert sp.simplify(sp.limit((1 + al) * sp.log((1 + al) / (1 + al - tau)), al, sp.oo) - tau) == 0
assert sp.limit(al * (ts - sp.Rational(1, 2)), al, sp.oo) == sp.Rational(1, 8)   # tau* decreases to 1/2

print("practice-L3-L4-check-b2.py: all checks passed")
