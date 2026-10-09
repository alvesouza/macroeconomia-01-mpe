"""Block 1 of practice-L5-L6.tex (symbolic): independent check of every closed form, sign, limit,
ordering, existence claim and multiple-choice distractor printed in practice-L5-L6-block1.tex.

Run from Listas/: python practice-L5-L6-check-b1.py   (aborts on the first failed assert).
Closed forms are checked with sympy; signs, orderings and existence at random admissible draws.
"""
import pathlib
from math import exp, log

import numpy as np
import sympy as sp
from scipy.optimize import brentq

HERE = pathlib.Path(__file__).parent
rng = np.random.default_rng(2026)
ND = 300                       # random admissible draws per claim
U = rng.uniform


def iszero(e):
    """Exact zero test: rational cancellation first (fast), simplify as the fallback."""
    e = sp.expand_log(e, force=True)           # all symbols are positive in the admissible ranges
    return sp.cancel(sp.together(e)) == 0 or sp.simplify(e) == 0


def root01(fun):
    """Unique root on (0,1) of an increasing function: asserts the sign change (existence) and
    strict monotonicity on a grid (uniqueness)."""
    grid = np.linspace(1e-6, 1 - 1e-6, 801)
    assert np.all(np.diff(fun(grid)) > 0)
    lo, hi = 1e-300, 1 - 1e-13          # x**a -> 0 slowly when a is small
    assert fun(lo) < 0 < fun(hi)
    return brentq(fun, lo, hi, xtol=1e-16, rtol=1e-15)


al, sg, ps, Kb, cb, Lb, Ls = sp.symbols("alpha sigma psi K cbar Lbar L", positive=True)
n, g, de, rho, tK, tau, h = sp.symbols("n g delta rho tau_K tau h", positive=True)
lA, lL, lK, lc = sp.symbols("lnA lnL lnK lnc", real=True)

# ===================== Q1(a): d lnL/d lnA in the static GE with CRRA =====================
Lx = sp.exp(lL)
Yx = sp.exp(lA) * Kb**al * Lx**(1 - al)


def elast(G):
    """d lnL/d lnA implied by the equilibrium condition G(lnA, lnL) = 0, written at L."""
    return (-sp.diff(G, lA) / sp.diff(G, lL)).subs(lL, sp.log(Ls))


key_a = (1 - sg) / (Ls / (1 - Ls) + al + (1 - al) * sg)
assert iszero(elast(sp.log(ps) - sp.log(1 - Lx) - sp.log(1 - al) - (1 - sg) * sp.log(Yx) + lL) - key_a)
lYbar = lA + sp.log(Kb**al * Lb**(1 - al))      # ln Y with hours held at Lbar: the "output fixed" mistake
opt_a = {  # each distractor re-derived from its named mistake(s); the key is B
    "A c fixed": (1 / (Ls / (1 - Ls) + al),
                  sp.log(ps) - sp.log(1 - Lx) - sp.log((1 - al) * Yx / Lx) + sg * sp.log(cb)),
    "D Y fixed": ((1 - sg) / (Ls / (1 - Ls) + 1),
                  sp.log(ps) - sp.log(1 - Lx) - sp.log(1 - al) - (1 - sg) * lYbar + lL),
    "C c fixed and Y fixed": (1 / (Ls / (1 - Ls) + 1),
                              sp.log(ps) - sp.log(1 - Lx) - sp.log(1 - al) - lYbar + lL + sg * sp.log(cb)),
}
for name, (opt, G) in opt_a.items():
    assert iszero(elast(G) - opt), name
f_key = sp.lambdify((Ls, al, sg), key_a)
f_opt = [sp.lambdify((Ls, al, sg), o) for o, _ in opt_a.values()]
for _ in range(ND):
    a_, s_, p_, A_, K_ = U(0.05, 0.95), U(0.2, 5), U(0.1, 10), U(0.5, 2), U(0.5, 5)
    e_ = a_ + (1 - a_) * s_

    def Leq(A):
        rhs = (1 - a_) * (A * K_**a_) ** (1 - s_)
        return root01(lambda L: p_ * L**e_ / (1 - L) - rhs)

    L0, k_ = Leq(A_), f_key(Leq(A_), a_, s_)
    num = (log(Leq(A_ * exp(1e-5))) - log(Leq(A_ * exp(-1e-5)))) / 2e-5
    assert abs(num - k_) < 1e-6 * max(1.0, abs(k_))
    assert np.sign(k_) == np.sign(1 - s_)
    for fo in f_opt:
        assert abs(fo(L0, a_, s_) - k_) > 1e-9

# ===================== Q1(b): Ramsey gross saving rate =====================
r_req = rho + de + sg * g
kst = (al / r_req) ** (1 / (1 - al))
assert iszero(sp.expand_log(sp.log(al * kst**(al - 1)), force=True) - sp.log(r_req))   # f'(k*) = rho+delta+sigma g
s_key = al * (n + g + de) / r_req
assert iszero(sp.expand_log(sp.log((n + g + de) * kst**(1 - al)), force=True)
              - sp.expand_log(sp.log(s_key), force=True))                               # s = (n+g+delta) k/f(k)
assert iszero(al - s_key - al * (rho - n - (1 - sg) * g) / r_req)
s_opts = {  # the key is A
    "D log Euler": s_key.subs(sg, 1),
    "C sigma read as the EIS": al * (n + g + de) / (rho + de + g / sg),
    "B log Euler and net investment": al * (n + g) / (rho + de + g),
}
assert iszero(sp.expand_log(sp.log((n + g) * kst.subs(sg, 1)**(1 - al)), force=True)
              - sp.expand_log(sp.log(s_opts["B log Euler and net investment"]), force=True))
fs = sp.lambdify((al, sg, n, g, de, rho), [s_key] + list(s_opts.values()))
for _ in range(ND):
    a_, s_, n_, g_, d_ = U(0.05, 0.95), U(0.2, 5), U(0, 0.05), U(0.001, 0.05), U(0.01, 0.15)
    r_ = max(n_ + (1 - s_) * g_, 0) + U(0.001, 0.1)
    key, *opts = fs(a_, s_, n_, g_, d_, r_)
    assert 0 < key < a_
    assert all(abs(o - key) > 1e-12 for o in opts)

# ===================== Q1(c): permanent G financed lump-sum =====================
Gs = sp.Symbol("G", positive=True)
c_ss = kst**al - (n + g + de) * kst - Gs
assert sp.diff(kst, Gs) == 0 and sp.diff(c_ss, Gs) == -1
# ===================== Q1(d): capital income tax rebated lump-sum =====================
k_tax = (al * (1 - tK) / (rho + sg * g + (1 - tK) * de)) ** (1 / (1 - al))
fd = sp.lambdify((al, sg, g, de, rho, tK), [(1 - tK) * (al * k_tax**(al - 1) - de) - rho - sg * g, sp.diff(k_tax, tK),
                                             (rho + sg * g) / ((1 - tK)**2 * al * (al - 1) * k_tax**(al - 2))])
for _ in range(ND):
    res, dk, dk_formula = fd(U(0.05, 0.95), U(0.2, 5), U(0.001, 0.05), U(0.01, 0.15), U(0.01, 0.1), U(0.01, 0.9))
    assert abs(res) < 1e-12 and dk < 0 and abs(dk / dk_formula - 1) < 1e-9

# ===================== Q2(a): implicit hours h(K,c) =====================
eps = (1 - h) / (al + (1 - al) * h)
th, chi, om = (1 - al) * (rho + de), rho + (1 - al) * de, al + (1 - al) * h
Ph = sp.log(ps) + lc + al * sp.log(h) - sp.log(1 - h) - sp.log((1 - tau) * (1 - al)) - al * lK
assert iszero(-sp.diff(Ph, lK) / sp.diff(Ph, h) / h - al * eps)
assert iszero(-sp.diff(Ph, lc) / sp.diff(Ph, h) / h + eps)
assert iszero(1 / (al + h / (1 - h)) - eps)


def hof(K, c, a_, t_, p_):
    return root01(lambda x: p_ * c * x**a_ / (1 - x) - (1 - t_) * (1 - a_) * K**a_)


for _ in range(ND):
    hof(U(0.1, 10), U(0.05, 5), U(0.05, 0.95), U(0, 0.95), U(0.05, 10))

# ===================== Q2(b): steady state =====================
kap = (al / (rho + de)) ** (1 / (1 - al))
assert iszero(sp.expand_log(sp.log(al * kap**(al - 1)), force=True) - sp.log(rho + de))
KY = al / (rho + de)
assert iszero(sp.expand_log(sp.log(kap**(1 - al)), force=True) - sp.log(KY))
CY = 1 - de * KY
assert iszero(CY - chi / (rho + de)) and iszero(CY - (1 - al * de / (rho + de)))
Phi = (1 - tau) * (1 - al) * (rho + de) / (ps * chi)
hsol = sp.solve(ps * CY / (1 - h) - (1 - tau) * (1 - al) / h, h)           # MRS = after-tax wage, Y cancels
hst = Phi / (1 + Phi)
assert len(hsol) == 1 and iszero(hsol[0] - hst)


def draw():
    """Admissible (alpha, rho, delta, psi, tau)."""
    return U(0.05, 0.95), U(0.005, 0.2), U(0.005, 0.3), U(0.05, 10), U(0, 0.95)


f_ss = sp.lambdify((al, rho, de, ps, tau), [hst, kap, CY])
for _ in range(ND):
    a_, r_, d_, p_, t_ = draw()
    h_, kp_, cy_ = f_ss(a_, r_, d_, p_, t_)
    K_ = kp_ * h_
    Y_ = K_**a_ * h_**(1 - a_)
    c_ = cy_ * Y_
    assert abs(hof(K_, c_, a_, t_, p_) / h_ - 1) < 1e-10
    assert abs(Y_ - c_ - d_ * K_) < 1e-12 * Y_ and abs(a_ * Y_ / K_ - r_ - d_) < 1e-12

# ===================== Q2(c): permanent tax rise =====================
nu, h0 = sp.symbols("nu h0", positive=True)
h1 = nu * (h0 / (1 - h0)) / (1 + nu * h0 / (1 - h0))
q = nu / (1 - (1 - nu) * h0)
assert iszero(h1 / h0 - q)
assert iszero(-(1 - tau) * sp.diff(sp.log(hst), tau) - (1 - hst))                  # dln h*/dln(1-tau) = 1-h*
fq = sp.lambdify((nu, h0), q)
for _ in range(ND):
    nu_, h0_ = U(0.01, 0.99), U(0.01, 0.99)
    assert nu_ < fq(nu_, h0_) < 1

# ===================== Q2(d): log-linear dynamics, saddle, impact =====================
Jc = sp.Matrix([[rho + th * eps, -(chi + th * eps) / al], [-th * (1 - al * eps), -th * eps]])
assert iszero(1 + (1 - al) * eps - 1 / om) and iszero(1 - al * eps - h / om)
assert iszero(Jc.trace() - rho) and iszero(Jc.det() + th * chi / (al * om))
D = th * chi / (al * om)
for sgn in (1, -1):
    mu = (rho + sgn * sp.sqrt(rho**2 + 4 * D)) / 2
    assert iszero(mu**2 - rho * mu - D)                       # roots of mu^2 - tr(J) mu + det(J)
Lam = th / (al * om)
pol = lambda x: x**2 + rho * x - chi * Lam
assert iszero(pol((1 - al) * de) - chi * ((1 - al) * de - Lam)) and iszero(pol(Lam) - Lam * (Lam - (1 - al) * de))
lam = sp.Symbol("lambda", positive=True)
xi = al * (rho + th * eps + lam) / (chi + th * eps)
assert iszero(xi - (Jc[0, 0] + lam) / (-Jc[0, 1]))
assert iszero(xi - al - al * (lam - (1 - al) * de) / (chi + th * eps))
assert iszero(1 - xi - al * (Lam - lam) / (chi + th * eps))
# Jacobian from primitives: dlnK/dt = Y/K - c/K - delta, dlnc/dt = alpha (K/h)^(alpha-1) - rho - delta, h = H(lnK, lnc)
Hs = sp.Symbol("H", positive=True)
F = [sp.exp((al - 1) * lK) * Hs**(1 - al) - sp.exp(lc - lK) - de, al * sp.exp((al - 1) * lK) * Hs**(1 - al) - rho - de]
dH = {lK: Hs * al * eps.subs(h, Hs), lc: -Hs * eps.subs(h, Hs)}            # implicit-function step of (a)
Jp = sp.Matrix([[sp.diff(Fi, v) + sp.diff(Fi, Hs) * dH[v] for v in (lK, lc)] for Fi in F])
fJp = sp.lambdify((lK, lc, Hs, al, rho, de), Jp)
fJc = sp.lambdify((h, al, rho, de), Jc)
fxi = sp.lambdify((h, al, rho, de, lam), xi)
# the partials printed in (d): Y/K, c/K and ln r^K with respect to (lnK, lnc), at the steady state
parts = [sp.exp((al - 1) * lK) * Hs**(1 - al), sp.exp(lc - lK), sp.log(al) + (al - 1) * lK + (1 - al) * sp.log(Hs)]
fPp = sp.lambdify((lK, lc, Hs, al, rho, de), sp.Matrix([[sp.diff(P, v) + sp.diff(P, Hs) * dH[v] for v in (lK, lc)] for P in parts]))
fPc = sp.lambdify((h, al, rho, de), sp.Matrix([[(rho + de) / al * (1 - al) * (al * eps - 1), -(rho + de) / al * (1 - al) * eps],
                                               [-chi / al, chi / al], [-(1 - al) * (1 - al * eps), -(1 - al) * eps]]))


def dyn(a_, r_, d_, h1_):
    """lambda, Lambda, xi, eps at the new steady state (closed forms of (d))."""
    th_, chi_, om_ = (1 - a_) * (r_ + d_), r_ + (1 - a_) * d_, a_ + (1 - a_) * h1_
    lam_ = (np.sqrt(r_**2 + 4 * th_ * chi_ / (a_ * om_)) - r_) / 2
    return lam_, th_ / (a_ * om_), fxi(h1_, a_, r_, d_, lam_), (1 - h1_) / om_


for _ in range(ND):
    a_, r_, d_, p_, t0_ = draw()
    t1_ = U(t0_, 0.99)
    h0_, kp_, cy_ = f_ss(a_, r_, d_, p_, t0_)
    h1_ = f_ss(a_, r_, d_, p_, t1_)[0]
    K1, c1 = kp_ * h1_, cy_ * kp_**a_ * h1_
    Jn = np.array(fJc(h1_, a_, r_, d_), dtype=float)
    assert np.allclose(np.array(fJp(log(K1), log(c1), h1_, a_, r_, d_), dtype=float), Jn, rtol=1e-9, atol=1e-12)
    assert np.allclose(np.array(fPp(log(K1), log(c1), h1_, a_, r_, d_), dtype=float),
                       np.array(fPc(h1_, a_, r_, d_), dtype=float), rtol=1e-9, atol=1e-12)

    def rhs(x):
        K, c = exp(x[0]), exp(x[1])
        hh = hof(K, c, a_, t1_, p_)                            # hours solved numerically: independent path
        return np.array([K**(a_ - 1) * hh**(1 - a_) - c / K - d_, a_ * K**(a_ - 1) * hh**(1 - a_) - r_ - d_])

    x0 = np.array([log(K1), log(c1)])
    Jfd = np.column_stack([(rhs(x0 + 1e-6 * e) - rhs(x0 - 1e-6 * e)) / 2e-6 for e in np.eye(2)])
    assert np.allclose(Jfd, Jn, rtol=1e-5, atol=1e-7)
    lam_, Lam_, xi_, e1 = dyn(a_, r_, d_, h1_)
    ev, V = np.linalg.eig(Jn)
    i = int(np.argmin(ev.real))
    assert np.all(np.isreal(ev)) and abs(ev[i] + lam_) < 1e-10 and abs(ev[1 - i] - r_ - lam_) < 1e-10
    assert abs(V[1, i] / V[0, i] - xi_) < 1e-8 * max(1.0, xi_)
    assert (1 - a_) * d_ < lam_ < Lam_ and a_ < xi_ < 1
    nu_ = (1 - t1_) / (1 - t0_)
    lq = log(h1_ / h0_)
    assert lq < 0 and abs(h1_ / h0_ - nu_ / (1 - (1 - nu_) * h0_)) < 1e-12
    k0 = -lq                                                    # K starts at the old level
    c_imp, h_imp = lq + xi_ * k0, lq + a_ * e1 * k0 - e1 * xi_ * k0
    assert abs(c_imp - (1 - xi_) * lq) < 1e-12 and abs(h_imp - (1 + e1 * (xi_ - a_)) * lq) < 1e-12
    assert lq < c_imp < 0 and h_imp < lq                        # partial fall of c; hours overshoot

# figure: admissible values alpha=1/3, rho=.04, delta=.06, h0=1/3 at tau0=.3, tau1=.45
nu_ = 0.55 / 0.7
h1_ = nu_ / 3 / (1 - (1 - nu_) / 3)
lam_, _, xi_, e1 = dyn(1 / 3, 0.04, 0.06, h1_)
tex = (HERE / "practice-L5-L6-block1.tex").read_text(encoding="utf-8")
for val, txt, pat in [(lam_, "0.156319", "exp(-{}*x)"), (xi_, "0.559017", "-(1-{}*exp"),
                      (e1 * (xi_ - 1 / 3), "0.310777", "-(1+{}*exp"), (log(2) / lam_, "4.4342", "xtick={{0,{}}}"),
                      (1 + e1 * (xi_ - 1 / 3), "1.3108", "ytick={{-{},-1,"), (1 - xi_, "0.441", ",-{},0}}")]:
    assert pat.format(txt) in tex and abs(float(txt) / val - 1) < 1e-4, txt

# ===================== Q2(e): comparative statics, sign table, limits =====================
assert iszero(sp.diff(sp.log(hst), tau) + (1 - hst) / (1 - tau))
assert iszero(ps * sp.diff(sp.log(hst), ps) + (1 - hst))
assert iszero(sp.diff(sp.log(hst), de) - (1 - hst) * al * rho / ((rho + de) * chi))
assert iszero(1 / (rho + de) - (1 - al) / chi - al * rho / ((rho + de) * chi))
lnkap = (sp.log(al) - sp.log(rho + de)) / (1 - al)
assert iszero(sp.diff(lnkap + sp.log(hst), de) - (al * (1 - al) * (1 - hst) * rho - chi) / ((1 - al) * (rho + de) * chi))
assert iszero(sp.diff(al * lnkap + sp.log(hst), de) - al * ((1 - al) * (1 - hst) * rho - chi) / ((1 - al) * (rho + de) * chi))
omst = om.subs(h, hst)
last = (1 - al) * hst * (1 - hst) * al * rho / (omst * (rho + de) * chi)
assert iszero(sp.diff(sp.log(th * chi / (al * omst)), de) - (1 / (rho + de) + (1 - al) / chi - last))
Dst = th * chi / (al * omst)
lam_cf = (sp.sqrt(rho**2 + 4 * Dst) - rho) / 2
kap_e = sp.exp(lnkap)
table = {  # row: (closed form, signs w.r.t. tau, psi, delta), as printed in the sign table of (e)
    "h*": (hst, "--+"), "K*": (kap_e * hst, "---"), "Y*": (kap_e**al * hst, "---"),
    "C*": (CY * kap_e**al * hst, "---"), "K/Y": (KY, "00-"), "C/Y": (CY, "00-"),
    "w*": ((1 - al) * kap_e**al, "00-"), "r*": (rho, "000"),
    "lambda": (lam_cf, "+++"), "half-life": (sp.log(2) / lam_cf, "---"),
}
X = [draw() for _ in range(ND)]
for row, (expr, signs) in table.items():
    for v, sgn in zip((tau, ps, de), signs):
        dv = sp.diff(expr, v)
        if sgn == "0":
            assert iszero(dv), (row, v)
            continue
        fdv = sp.lambdify((al, rho, de, ps, tau), dv)
        vals = np.array([fdv(*x) for x in X])
        assert np.all(vals > 0) if sgn == "+" else np.all(vals < 0), (row, v)
f_last = sp.lambdify((al, rho, de, ps, tau), [last * (rho + de), lam_cf])
lam_lo, lam_hi = [(sp.sqrt(rho**2 + 4 * th * chi / al**k) - rho) / 2 for k in (1, 2)]
f_b = sp.lambdify((al, rho, de), [lam_lo, lam_hi])
for x in X:
    ratio, lam_x = f_last(*x)
    lo_, hi_ = f_b(*x[:3])
    assert ratio < 1 and lo_ < lam_x < hi_
assert sp.limit(hst, tau, 1, "-") == 0 and sp.limit(hst, ps, sp.oo) == 0 and iszero(sp.limit(hst, ps, 0, "+") - 1)
assert iszero(sp.limit(D, h, 0) - th * chi / al**2) and iszero(sp.limit(D, h, 1) - th * chi / al)
assert CY.subs(de, 0) == 1 and sp.diff(Phi.subs(de, 0), rho) == 0      # knife-edge delta = 0

print(f"{pathlib.Path(__file__).stem}: all checks passed")
