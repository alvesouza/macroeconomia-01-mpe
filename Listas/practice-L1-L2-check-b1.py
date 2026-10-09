"""Practice list A v4, Block 1 (Questions 1-2): checks practice-L1-L2-block1.tex.

Run from Listas/: python practice-L1-L2-check-b1.py   (aborts on the first failed assert).
Closed forms are checked with sympy; signs, orderings, distractors and existence claims at
DRAWS random admissible parameter draws.
"""
import numpy as np
import sympy as sp
from scipy.optimize import brentq
from sympy.stats import E, Normal

rng = np.random.default_rng(2026)
DRAWS = 300


def zero(expr, msg):
    """Assert that a sympy expression simplifies to zero; msg names the claim."""
    assert sp.simplify(expr) == 0, msg


def pmean(r, R, w):
    """Power mean of order r of the relatives R with weights w (summing to one)."""
    return float(np.exp(w @ np.log(R))) if r == 0 else float((w @ R ** r) ** (1 / r))


def eta_draw(lo=0.05, hi=8.0):
    """An elasticity draw kept away from the Cobb-Douglas knife-edge eta = 1."""
    e = rng.uniform(lo, hi)
    return e + 0.1 if abs(e - 1) < 0.05 else e


# ===================== Q1(a): Laspeyres overstatement, two goods, base share omega of good 1
eta, R, om = sp.symbols("eta R omega", positive=True)
lnL = sp.log(om * R + 1 - om)
key_a = lnL - sp.log(om * R ** (1 - eta) + 1 - om) / (1 - eta)                # option C
dis_a = {"A": lnL - om * sp.log(R),                                           # Cobb-Douglas
         "B": lnL - sp.log(om * R ** (eta - 1) + 1 - om) / (eta - 1),         # order eta-1
         "D": lnL - sp.log(om * R ** (eta - 1) + 1 - om)}                     # order eta-1, no root
cost = lambda p1, p2: (om * p1 ** (1 - eta) + (1 - om) * p2 ** (1 - eta)) ** (1 / (1 - eta))
p1s = sp.Symbol("p1", positive=True)
zero((p1s * sp.diff(sp.log(cost(p1s, 1)), p1s)).subs(p1s, 1) - om, "Q1a base share omega (Shephard)")
zero(sp.expand_log(lnL - sp.log(cost(R, 1) / cost(1, 1)) - key_a, force=True), "Q1a key")
zero(key_a.subs(eta, 0), "Q1a bias vanishes at eta = 0 (Leontief)")
eps = sp.Symbol("epsilon")
ser = sp.series(key_a.subs(R, sp.exp(eps)), eps, 0, 3).removeO()
zero(ser - eta * om * (1 - om) * eps ** 2 / 2, "Q1a second-order bias (eta/2) omega(1-omega)(ln R)^2")
f_key, f_dkey = sp.lambdify((eta, R, om), key_a), sp.lambdify((eta, R, om), sp.diff(key_a, eta))
f_dis = {k: sp.lambdify((eta, R, om), v) for k, v in dis_a.items()}
for _ in range(DRAWS):
    e, r, o = eta_draw(0.05, 6.0), rng.uniform(1.2, 5.0), rng.uniform(0.05, 0.95)
    k = f_key(e, r, o)
    w, Rv = np.array([o, 1 - o]), np.array([r, 1.0])
    lnL_v = np.log(w @ Rv)
    assert abs(k - lnL_v + np.log(pmean(1 - e, Rv, w))) < 1e-10, "Q1a power mean"
    assert k > 0 and f_dkey(e, r, o) > 0, "Q1a bias positive and rising in eta"
    assert abs(f_dis["B"](e, r, o) - lnL_v + np.log(pmean(e - 1, Rv, w))) < 1e-10, "Q1a B is order eta-1"
    assert abs(f_dis["D"](e, r, o) - lnL_v + np.log(w @ Rv ** (e - 1))) < 1e-10, "Q1a D is B without the root"
    for name, f in f_dis.items():
        assert abs(f(e, r, o) - k) > 1e-6, f"Q1a distractor {name} equals the key"
    assert abs(f_key(1 + 1e-7, r, o) - f_dis["A"](1, r, o)) < 1e-6, "Q1a A is the eta -> 1 limit"

# ===================== Q1(b): consumption-equivalent welfare growth
g, T, v0, vT, a0, aT, ub, lnlam = sp.symbols("g T v_0 v_T a_0 a_T ubar lnlambda", real=True)
mu, v = sp.Symbol("mu", real=True), sp.Symbol("v", positive=True)
lognormal_gap = E(sp.exp(Normal("X", mu, sp.sqrt(v)))) - sp.exp(mu + v / 2)
zero(lognormal_gap.rewrite(sp.erf), "lognormal mean")
Eln0, ElnT = -v0 / 2, g * T - vT / 2                                         # E ln c = ln cbar - v/2
key_b = g + (v0 - vT) / (2 * T) + (aT / a0 - 1) * (ub + g * T - vT / 2) / T  # option A
sol_b = sp.solve(sp.Eq(a0 * (ub + lnlam + Eln0), aT * (ub + ElnT)), lnlam)[0]
zero(sol_b / T - key_b, "Q1b key")
dis_b = {"B": g + (vT - v0) / (2 * T) + (aT / a0 - 1) * (ub + g * T + vT / 2) / T,
         "C": g + (v0 - vT) / (2 * T) + sp.log(aT / a0) / T,
         "D": g + (vT - v0) / (2 * T) + (1 - a0 / aT) * (ub + v0 / 2) / T}
sol_B = sp.solve(sp.Eq(a0 * (ub + lnlam + v0 / 2), aT * (ub + g * T + vT / 2)), lnlam)[0]
zero(sol_B / T - dis_b["B"], "Q1b B = Jensen sign error")
sol_C = sp.solve(sp.Eq(sp.log(a0) + lnlam + Eln0, sp.log(aT) + ElnT), lnlam)[0]   # survival as a consumption factor
zero(sp.expand_log(sol_C / T - dis_b["C"], force=True), "Q1b C = proportional longevity")
sol_D = sp.solve(sp.Eq(a0 * (ub + v0 / 2), aT * (ub + g * T + vT / 2 - lnlam)), lnlam)[0]
zero(sol_D / T - dis_b["D"], "Q1b D = date-T reference and Jensen sign error")
args_b = (g, T, v0, vT, a0, aT, ub)
f_b = sp.lambdify(args_b, key_b)
f_bd = {k: sp.lambdify(args_b, x) for k, x in dis_b.items()}
f_lon = sp.lambdify(args_b, (aT / a0 - 1) * (ub + g * T - vT / 2))
for _ in range(DRAWS):
    gg, TT, x0, xT = rng.uniform(-0.02, 0.05), rng.uniform(5, 50), rng.uniform(0, 2), rng.uniform(0, 2)
    A0 = rng.uniform(0.3, 0.8)
    AT = rng.uniform(A0 + 0.01, 1.0)
    U = max(x0 / 2, xT / 2 - gg * TT) + rng.uniform(0.1, 5)                 # positive flow utility
    pt = (gg, TT, x0, xT, A0, AT, U)
    assert f_lon(*pt) > 0, "Q1b longevity term positive"
    for name, f in f_bd.items():
        assert abs(f(*pt) - f_b(*pt)) > 1e-8, f"Q1b distractor {name} equals the key"

# ===================== Q1(c): Bortkiewicz decomposition and counterexample
p0, p1, q0, q1 = (sp.symbols(f"{s}_1:4", positive=True) for s in ("p0", "p1", "q0", "q1"))
E0 = sum(p0[i] * q0[i] for i in range(3))
w = [p0[i] * q0[i] / E0 for i in range(3)]
Rp, Rq = [p1[i] / p0[i] for i in range(3)], [q1[i] / q0[i] for i in range(3)]
Lasp = sum(p1[i] * q0[i] for i in range(3)) / E0
Paas = sum(p1[i] * q1[i] for i in range(3)) / sum(p0[i] * q1[i] for i in range(3))
Rpb, Rqb = sum(w[i] * Rp[i] for i in range(3)), sum(w[i] * Rq[i] for i in range(3))
cov = sum(w[i] * (Rp[i] - Rpb) * (Rq[i] - Rqb) for i in range(3))
zero(Lasp - Rpb, "Q1c Laspeyres = mean price relative")
zero(Paas / Lasp - 1 - cov / (Rpb * Rqb), "Q1c Bortkiewicz")
u1, u2 = sp.symbols("u1 u2", positive=True)                                  # R = 1+u1, Q = 1+u2
Rc, Qc = 1 + u1, 1 + u2
covc = sp.Rational(1, 2) * ((Rc - (Rc + 1) / 2) * (Qc - (Qc + 1) / 2) + (1 - (Rc + 1) / 2) * (1 - (Qc + 1) / 2))
zero(covc - (Rc - 1) * (Qc - 1) / 4, "Q1c covariance")
ratio = (Rc * Qc + 1) / (Qc + 1) / ((Rc + 1) / 2)                            # Paasche / Laspeyres
zero(ratio - 1 - (Rc - 1) * (Qc - 1) / ((Rc + 1) * (Qc + 1)), "Q1c ratio")
assert sp.factor(ratio - 1).is_positive, "Q1c Paasche > Laspeyres"

# ===================== Q1(d): Balassa-Samuelson in growth rates
gam = sp.Symbol("gamma", positive=True)
pT, pN, t, gT, gN, Dl, Ex = sp.symbols("p_T p_N t g_T g_N Delta E", positive=True)
kap = (1 - gam) ** (gam - 1) * gam ** (-gam)
Pb = kap * pT ** (1 - gam) * pN ** gam
cT, cN = (1 - gam) * Pb / pT, gam * Pb / pN                                  # CD demands, one basket
zero(sp.expand_log(sp.log(cT ** (1 - gam) * cN ** gam), force=True), "Q1d unit cost")
zero((1 - gam) / gam * cN / cT - pT / pN, "Q1d cost-minimizing MRS")
price = lambda p_t, AT_, AN_: kap * p_t * (AT_ / AN_) ** gam                  # p_N = p_T A_T / A_N
ratio_d = price(Ex * pT, sp.exp((gT + Dl) * t), sp.exp(gN * t)) / (Ex * price(pT, sp.exp(gT * t), sp.exp(gN * t)))
growth = sp.diff(sp.expand_log(sp.log(ratio_d), force=True), t)
zero(growth - gam * Dl, "Q1d growth gamma*Delta")
assert sp.diff(gam * Dl, gam) == Dl, "Q1d increasing in gamma"

# ===================== Q2(a): cost of a util and shares
rho_s = (eta - 1) / eta
zero(1 / (1 - rho_s) - eta, "Q2a 1/(1-rho)")
zero(rho_s / (1 - rho_s) - (eta - 1), "Q2a rho/(1-rho)")
for _ in range(DRAWS):
    n, e = int(rng.integers(2, 6)), rng.uniform(1.05, 8)
    rho = (e - 1) / e
    p, b = rng.uniform(0.2, 5, n), rng.uniform(0.2, 3, n)
    Pi = np.sum((p / b) ** (1 - e)) ** (1 / (1 - e))
    x = Pi ** e * b ** (e - 1) * p ** (-e)
    assert abs(np.sum((b * x) ** rho) - 1) < 1e-9, "Q2a U = 1"
    m = p / (rho * b ** rho * x ** (rho - 1))
    assert np.allclose(m, m[0]) and abs(m[0] * rho - Pi) < 1e-9 * Pi, "Q2a FOC, mu*rho = P"
    assert abs(p @ x - Pi) < 1e-9 * Pi, "Q2a spending = P"
    assert np.allclose(p * x / Pi, (p / b) ** (1 - e) / Pi ** (1 - e)), "Q2a shares"
    for _ in range(5):                                                       # minimum cost
        y = x * rng.uniform(0.3, 3, n)
        y /= np.sum((b * y) ** rho) ** (1 / rho)
        assert p @ y >= Pi * (1 - 1e-12), "Q2a another bundle with U = 1 is cheaper"

# ===================== Q2(b)-(c): exact index, ranking, Feenstra correction
for _ in range(DRAWS):
    n, e = int(rng.integers(2, 6)), rng.uniform(1.05, 8)
    b, pp0 = rng.uniform(0.2, 3, n), rng.uniform(0.2, 5, n)
    Rr = np.exp(rng.normal(0, 0.4, n))
    pp1 = pp0 * Rr
    Pt = lambda p_: np.sum((p_ / b) ** (1 - e)) ** (1 / (1 - e))
    exact = Pt(pp1) / Pt(pp0)
    w0, w1 = (pp0 / b) ** (1 - e) / Pt(pp0) ** (1 - e), (pp1 / b) ** (1 - e) / Pt(pp1) ** (1 - e)
    assert abs(pmean(1 - e, Rr, w0) - exact) < 1e-9 * exact, "Q2b base weights"
    assert np.allclose(w1, w0 * Rr ** (1 - e) / np.sum(w0 * Rr ** (1 - e))), "Q2b w1"
    assert abs(pmean(e - 1, Rr, w1) - exact) < 1e-9 * exact, "Q2b current weights"
    U0, U1 = rng.uniform(0.5, 3, 2)                                           # homothetic demands
    x0 = U0 * Pt(pp0) ** e * b ** (e - 1) * pp0 ** (-e)
    x1 = U1 * Pt(pp1) ** e * b ** (e - 1) * pp1 ** (-e)
    Lq, Pq = pp1 @ x0 / (pp0 @ x0), pp1 @ x1 / (pp0 @ x1)
    assert abs(Lq - pmean(1, Rr, w0)) < 1e-9 and abs(Pq - pmean(-1, Rr, w1)) < 1e-9, "Q2b L, P"
    assert Pq <= exact * (1 + 1e-12) and exact <= Lq * (1 + 1e-12), "Q2b Paasche <= exact <= Laspeyres"
    r = rng.choice([-1, 1]) * rng.uniform(0.1, 4)                            # d ln M_r/dr = KL/r^2
    h, wt = 1e-5, w0 * Rr ** r / np.sum(w0 * Rr ** r)
    kl = np.sum(wt * np.log(wt / w0))
    dnum = (np.log(pmean(r + h, Rr, w0)) - np.log(pmean(r - h, Rr, w0))) / (2 * h)
    assert kl >= 0 and abs(dnum - kl / r ** 2) < 1e-6, "Q2b power means rise with the order"
    # (c) new varieties at date 1: P1 = P1^cont lambda1^(1/(eta-1)); beta_C = -ln(1-nu)/(eta-1)
    m_new = int(rng.integers(1, 4))
    bn, pn = rng.uniform(0.2, 3, m_new), rng.uniform(0.2, 5, m_new)
    P1all = (np.sum((pp1 / b) ** (1 - e)) + np.sum((pn / bn) ** (1 - e))) ** (1 / (1 - e))
    xall = np.concatenate([pp1, pn]) * U1 * P1all ** e * np.concatenate([b, bn]) ** (e - 1) \
        * np.concatenate([pp1, pn]) ** (-e)
    lam1 = xall[:n].sum() / xall.sum()                                       # spending share, continuing
    assert abs(P1all - Pt(pp1) * lam1 ** (1 / (e - 1))) < 1e-9 * P1all, "Q2c Feenstra"
    betaC_num = np.log(Pt(pp1) / Pt(pp0)) - np.log(P1all / Pt(pp0))
    assert abs(betaC_num + np.log(lam1) / (e - 1)) < 1e-10 and betaC_num > 0, "Q2d beta_C"
w1, w2, d1, d2 = sp.symbols("w1 w2 d1 d2", positive=True)
r_ = sp.Symbol("r", real=True, nonzero=True)
w3, d3 = 1 - w1 - w2, -(w1 * d1 + w2 * d2) / (1 - w1 - w2)                  # mean-zero deviations
lnM = sp.log(w1 * sp.exp(r_ * eps * d1) + w2 * sp.exp(r_ * eps * d2) + w3 * sp.exp(r_ * eps * d3)) / r_
V = w1 * d1 ** 2 + w2 * d2 ** 2 + w3 * d3 ** 2
zero(sp.series(lnM, eps, 0, 3).removeO() - r_ * eps ** 2 * V / 2, "Q2b ln M_r = zbar + (r/2)V")
uu = sp.Symbol("u", positive=True)                                           # lambda1 = 1/(1+u) < 1
corr = (1 / (1 + uu)) ** (1 / (eta - 1))
assert sp.limit(corr, eta, sp.oo) == 1 and sp.limit(corr, eta, 1, "+") == 0, "Q2c limits"

# ===================== Q2(d): measured output, capital and the residual
nu = sp.Symbol("nu", positive=True)
betaC_s = -sp.log(1 - nu) / (eta - 1)
sC, sI, al, betaC, betaI, gC, gI, gK, gL, gY, dl, kp = sp.symbols(
    "s_C s_I alpha beta_C beta_I g_C g_I g_K g_L g_Y delta kappa", positive=True)
zero(sC * (gC - betaC) + sI * (gI - betaI) - (sC * gC + sI * gI) + (sC * betaC + sI * betaI), "Q2d g_Y^m")
K, I0, x0 = sp.Function("K"), *sp.symbols("I_0 x_0", positive=True)
Im = I0 * sp.exp((gK - betaI) * t)                                              # measured investment
xdot = sp.diff(K(t) / Im, t).subs(sp.Derivative(K(t), t), Im - dl * K(t))
zero(xdot - (1 - (gK - betaI + dl) * K(t) / Im), "Q2d x-dot = 1 - (g_K - beta_I + delta) x")
x_t = 1 / kp + (x0 - 1 / kp) * sp.exp(-kp * t)                               # kp = g_K - beta_I + delta > 0
zero(sp.diff(x_t, t) - (1 - kp * x_t), "Q2d x(t) solves the ODE")
assert sp.limit(x_t, t, sp.oo) == 1 / kp, "Q2d x -> 1/kappa"
assert sp.simplify(sp.limit(1 / x_t - dl, t, sp.oo) - (kp - dl)) == 0, "Q2d K^m growth -> g_K - beta_I"
assert sp.solve(sp.Eq(sp.exp(-kp * t), sp.Rational(1, 2)), t) == [sp.log(2) / kp], "Q2d half-life"
gYm, gKm = gY - (sC * betaC + sI * betaI), gK - betaI
Dlt = (gYm - al * gKm - (1 - al) * gL) - (gY - al * gK - (1 - al) * gL)
zero(Dlt - (-(sC * betaC + sI * betaI) + al * betaI), "Q2d residual bias")
Dlt = (-sC * betaC - (sI - al) * betaI).subs(sC, 1 - sI)
zero(Dlt.subs(betaI, 0) + (1 - sI) * betaC, "Q2d beta_I = 0")
zero(Dlt.subs(betaI, betaC) + (1 - al) * betaC, "Q2d beta_I = beta_C")
zero(Dlt.subs(betaI, betaC) - Dlt.subs(betaI, 0) - (al - sI) * betaC, "Q2d comparison")

# ===================== Q2(e): signs, threshold, limits, reading
ell = -sp.log(1 - nu)
zero(sp.diff(betaC_s, eta) + ell / (eta - 1) ** 2, "Q2e dbeta_C/deta")
zero(sp.diff(betaC_s, nu) - 1 / ((1 - nu) * (eta - 1)), "Q2e dbeta_C/dnu")
zero(sp.diff(betaC_s, eta, 2) - 2 * ell / (eta - 1) ** 3, "Q2e d2beta_C/deta2")
D_e = Dlt.subs(betaC, betaC_s)
part = {s: sp.diff(D_e, s) for s in (eta, nu, betaI, al, sI)}
zero(part[betaI] - (al - sI), "Q2e dDelta/dbeta_I")
zero(part[al] - betaI, "Q2e dDelta/dalpha")
zero(part[sI] - (betaC_s - betaI), "Q2e dDelta/ds_I")
bstar = sp.solve(Dlt, betaI)[0]
zero(bstar - (1 - sI) * betaC / (al - sI), "Q2e beta_I*")
zero(sp.diff(bstar, al) + (1 - sI) * betaC / (al - sI) ** 2, "Q2e dbeta_I*/dalpha")
zero(sp.diff(bstar, sI) - (1 - al) * betaC / (al - sI) ** 2, "Q2e dbeta_I*/ds_I")
bstar_e = bstar.subs(betaC, betaC_s)
syms = (eta, nu, betaI, al, sI)
f = {k: sp.lambdify(syms, x) for k, x in
     {"betaC_eta": sp.diff(betaC_s, eta), "betaC_nu": sp.diff(betaC_s, nu), "betaC_ee": sp.diff(betaC_s, eta, 2),
      "D_eta": part[eta], "D_nu": part[nu], "bs_eta": sp.diff(bstar_e, eta),
      "bs_nu": sp.diff(bstar_e, nu), "bs_al": sp.diff(bstar_e, al), "bs_sI": sp.diff(bstar_e, sI),
      "D": D_e, "bs": bstar_e}.items()}
for _ in range(DRAWS):
    pt = (rng.uniform(1.05, 10), rng.uniform(0.01, 0.9), rng.uniform(0, 0.1),
          rng.uniform(0.05, 0.95), rng.uniform(0.05, 0.95))
    assert f["betaC_eta"](*pt) < 0 and f["betaC_nu"](*pt) > 0 and f["betaC_ee"](*pt) > 0, "Q2e beta_C signs"
    assert f["D_eta"](*pt) > 0 and f["D_nu"](*pt) < 0, "Q2e Delta signs in eta, nu"
    e_, n_, _, a_, s_ = pt
    D_of = lambda b_: f["D"](e_, n_, b_, a_, s_)
    betaC_v = -np.log(1 - n_) / (e_ - 1)
    assert D_of(0) < 0 and D_of(betaC_v) < 0, "Q2d both cases negative"
    if a_ > s_:                                                              # unique positive root
        bs = f["bs"](*pt)
        assert bs > 0 and abs(brentq(D_of, 0, 10 * bs + 1) - bs) < 1e-9 * (1 + bs), "Q2e root"
        assert D_of(0.5 * bs) < 0 < D_of(1.5 * bs), "Q2e Delta > 0 iff beta_I > beta_I*"
        assert f["bs_eta"](*pt) < 0 and f["bs_nu"](*pt) > 0, "Q2e beta_I* in eta, nu"
        assert f["bs_al"](*pt) < 0 and f["bs_sI"](*pt) > 0, "Q2e beta_I* in alpha, s_I"
    else:
        assert all(D_of(b_) < 0 for b_ in np.linspace(0, 100, 50)), "Q2e no sign switch"
hh = sp.Symbol("h", positive=True)                                           # eta = 1 + h, nu = u/(1+u)
betaC_hu = sp.log(1 + uu) / hh
zero(sp.expand_log(betaC_s.subs({eta: 1 + hh, nu: uu / (1 + uu)}) - betaC_hu, force=True), "Q2e reparametrization")
assert sp.limit(betaC_hu, hh, 0, "+") == sp.oo and sp.limit(betaC_hu, hh, sp.oo) == 0, "Q2e eta limits"
assert sp.limit(betaC_s.subs(eta, 1 + hh), nu, 1, "-") == sp.oo, "Q2e nu -> 1"
zero(sp.series(betaC_s, nu, 0, 2).removeO() - nu / (eta - 1), "Q2e nu -> 0, first order")
zero(sp.diff(Dlt.subs(al, sI), betaI), "Q2e knife-edge alpha = s_I")
zero(bstar.subs(al, sI + uu) - (1 - sI) * betaC / uu, "Q2e beta_I* near alpha = s_I")      # alpha = s_I + u
assert sp.limit(sC * betaC / uu, uu, 0, "+") == sp.oo, "Q2e beta_I* -> oo as alpha -> s_I (s_C > 0)"
KY, fp, a_cd, k = sp.symbols("KY fprime a k", positive=True)                # reading: one-good path
zero(fp * KY - (gK + dl) * KY - KY * (fp - dl - gK), "Q2e alpha - s_I = (K/Y)(f' - delta - g_K)")
k_gr = (a_cd / (gK + dl)) ** (1 / (1 - a_cd))                                # f(k) = k^a: f'(k_gr) = g_K + delta
same_log = lambda lhs, rhs, msg: zero(sp.expand_log(sp.log(lhs) - sp.log(rhs), force=True), msg)
same_log(sp.diff(k ** a_cd, k).subs(k, k_gr), gK + dl, "Q2e golden rule k")
same_log((gK + dl) * k_gr / k_gr ** a_cd, a_cd, "Q2e golden-rule saving rate = alpha")
for _ in range(DRAWS):                                                       # alpha > s_I iff k < k_gr
    a_, n_ = rng.uniform(0.1, 0.9), rng.uniform(0.01, 0.2)                   # n_ = g_K + delta
    kk = rng.uniform(0.01, 3) * (a_ / n_) ** (1 / (1 - a_))
    assert (a_ > n_ * kk ** (1 - a_)) == (kk < (a_ / n_) ** (1 / (1 - a_))), "Q2e golden-rule reading"
for nu_, lo in ((0.1, 1.09), (0.2, 1.19), (0.4, 1.43)):                     # figure stays in the box
    assert -np.log(1 - nu_) / (lo - 1) < 1.25

print("practice-L1-L2-check-b1: all checks passed")
