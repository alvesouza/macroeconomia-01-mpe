"""Practice list A v4, Block 3b (Question 6): Solow saving reform x national accounts x welfare x discounting.

Independent check of every closed form (sympy), sign, limit, ordering and existence claim (random admissible
draws, root-finding) printed in practice-L1-L2-block3b.tex. Aborts on the first mismatch.
Run from Listas/: python practice-L1-L2-check-b3b.py
"""
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq

rng = np.random.default_rng(20261007)
NDRAW = 300


def zero(expr, name):
    """Assert expr == 0 symbolically (logs split and powers denested with force=True, valid because every base
    and log argument is positive here); if sympy cannot close it, at 300 random admissible draws."""
    e = sp.simplify(sp.powdenest(sp.expand_log(expr, force=True), force=True))
    if e == 0:
        return
    for _ in range(NDRAW):
        a = rng.uniform(0.1, 0.9)
        v1 = rng.uniform(0.05, 1.0) * a
        val = {"alpha": a, "s1": v1, "s0": rng.uniform(0.05, 0.95) * v1, "N": rng.uniform(0.01, 0.3),
               "t": rng.uniform(0.0, 50.0), "rho": rng.uniform(0.001, 0.2), "k": rng.uniform(0.1, 10.0),
               "E": rng.uniform(0.0, 1.0), "s": rng.uniform(0.05, 0.95) * a}
        res = complex(e.subs({v: val.get(v.name, rng.uniform(0.1, 1.0)) for v in e.free_symbols}).evalf())
        assert abs(res) < 1e-9, f"{name}: {e} = {res}"


def close(a, b, name, tol=1e-7):
    assert abs(a - b) <= tol * max(1.0, abs(b)), f"{name}: {a} != {b}"


# ----------------------------------------------------------------------------- symbolic model
al, s0, s1, N, t, rho, k, E, dt, s = sp.symbols("alpha s0 s1 N t rho k E dt s", positive=True)
lam, eta, b = (1 - al) * N, al / (1 - al), (s1 - s0) / s1
z = (s1 - (s1 - s0) * sp.exp(-lam * t)) / N
D_form1 = sp.log((1 - s1) / (1 - s0)) + eta * sp.log(1 + (s1 - s0) / s0 * (1 - sp.exp(-lam * t)))
D0 = sp.log((1 - s1) / (1 - s0))
Dinf = D0 + eta * sp.log(s1 / s0)
D_form2 = Dinf + eta * sp.log(1 - b * sp.exp(-lam * t))
G = lambda x_: sp.log(1 - x_) + eta * sp.log(x_)
m = s1 * (1 - E) + s0 * E  # E = exp(-lambda t), from 1 at t = 0 to 0 as t -> oo
DE = sp.log(1 - s1) + eta * sp.log(m) - sp.log(1 - s0) - eta * sp.log(s0)
q = sp.Symbol("q", positive=True)  # q = 1 - alpha > 0, so that sympy can sign lambda in limits t -> oo
lim_t = lambda e: sp.limit(e.subs(al, 1 - q), t, sp.oo).subs(q, 1 - al)
num = lambda e, *extra: sp.lambdify((al, s0, s1, N) + extra, e, "numpy")

# (a) Bernoulli substitution, exact path, D(t), long-run gain, recovery time
zero((1 - al) * k ** (-al) * (s1 * k ** al - N * k) - (1 - al) * (s1 - N * k ** (1 - al)), "zdot from kdot")
zero(sp.diff(z, t) - (1 - al) * (s1 - N * z), "z(t) solves the linear ODE")
zero(z.subs(t, 0) - s0 / N, "z(0) = s0/N")
zero(lim_t(z) - s1 / N, "z -> s1/N")
zero(sp.diff(D_form2, t) - al * N * b * sp.exp(-lam * t) / (1 - b * sp.exp(-lam * t)), "D'(t)")
zero(sp.diff(G(s1), s1) - (al - s1) / ((1 - al) * s1 * (1 - s1)), "G'(s)")
zero(Dinf - (G(s1) - G(s0)), "D(inf) = G(s1) - G(s0)")
zero(D_form1.subs(t, 0) - D0, "D(0)")
zero(DE.subs(E, sp.exp(-lam * t)) - D_form1, "D in terms of E")
zero(DE.subs(E, 0) - Dinf, "D(inf): E -> 0")


def D_num(tt, a, x0, x1, n):
    """Log consumption gap D(t) from the primitives: c1(t) = (1-s1) z(t)^eta, c0 = (1-s0)(s0/N)^eta."""
    zz = (x1 - (x1 - x0) * np.exp(-(1 - a) * n * tt)) / n
    e = a / (1 - a)
    return np.log((1 - x1) * zz ** e) - np.log((1 - x0) * (x0 / n) ** e)


def draw(beyond_alpha=False):
    a = rng.uniform(0.1, 0.9)
    x1 = rng.uniform(0.05 * a, 0.999 if beyond_alpha else a)
    if not beyond_alpha and rng.random() < 0.15:
        x1 = a  # golden-rule reform included
    return a, rng.uniform(0.05, 0.95) * x1, x1, rng.uniform(0.01, 0.3)


def TR(a, x0, x1, n):
    R = ((1 - x0) / (1 - x1)) ** ((1 - a) / a)
    return np.log((x1 - x0) / (x1 - R * x0)) / ((1 - a) * n)


f_D1, f_D2, f_D0, f_Dinf = num(D_form1, t), num(D_form2, t), num(D0), num(Dinf)
for _ in range(NDRAW):
    a, x0, x1, n = draw()
    for tt in (0.0, 0.7, 5.0, 40.0):
        dn = D_num(tt, a, x0, x1, n)
        close(f_D1(a, x0, x1, n, tt), dn, "D form 1 = primitives")
        close(f_D2(a, x0, x1, n, tt), dn, "D form 2 = primitives")
    assert f_D0(a, x0, x1, n) < 0 < f_Dinf(a, x0, x1, n), "D(0) < 0 < D(inf) for s0 < s1 <= alpha"
    R = ((1 - x0) / (1 - x1)) ** ((1 - a) / a)
    close(R, np.exp(-f_D0(a, x0, x1, n) * (1 - a) / a), "R = exp(-D(0)/eta)")
    T1 = TR(a, x0, x1, n)
    close(T1, -np.log(1 - x0 * (R - 1) / (x1 - x0)) / ((1 - a) * n), "two forms of T_R")
    assert abs(D_num(T1, a, x0, x1, n)) < 1e-9, "D(T_R) = 0"
    close(brentq(lambda tt: D_num(tt, a, x0, x1, n), 0.0, 1e4 / n, xtol=1e-12), T1, "T_R = root", tol=1e-6)
nonexist = 0
for _ in range(NDRAW):  # existence of T_R iff D(inf) > 0 iff s1 > R s0 (draws include s1 > alpha)
    a, x0, x1, n = draw(beyond_alpha=True)
    R = ((1 - x0) / (1 - x1)) ** ((1 - a) / a)
    dinf = f_Dinf(a, x0, x1, n)
    assert (x1 > R * x0) == (dinf > 0), "s1 > R s0 iff D(inf) > 0"
    if dinf <= 0:
        nonexist += 1
        assert np.all(D_num(np.linspace(0.0, 200.0 / n, 2001), a, x0, x1, n) < 0), "no recovery if D(inf) <= 0"
assert nonexist > 10, "draws must include reforms without recovery"

# (b) national accounts: growth rates, growth accounting, output gap
gam = eta * sp.diff(z, t) / z
excess = al * N * (s1 - s0) * sp.exp(-lam * t) / (s1 - (s1 - s0) * sp.exp(-lam * t))
zero(gam - excess, "excess growth of y and c")
zero(al * sp.diff(sp.log(z ** (1 / (1 - al))), t) - gam, "growth accounting: alpha kdot/k = eta zdot/z")
zero(excess.subs(t, 0) - al * N * (s1 - s0) / s0, "excess growth right after the reform")
zero(lim_t(excess), "excess growth -> 0")
gap = eta * sp.log(1 + (s1 - s0) / s0 * (1 - sp.exp(-lam * t)))
zero(D_form1 - gap - D0, "D = output gap + D(0)")
f_exc, f_dexc = num(excess, t), num(sp.diff(excess, t), t)
for _ in range(NDRAW):
    a, x0, x1, n = draw()
    for tt in (0.0, 1.0, 10.0, 60.0):
        assert f_exc(a, x0, x1, n, tt) > 0 > f_dexc(a, x0, x1, n, tt), "excess growth > 0 and falling"

# (c) welfare: consumption equivalent, integration by parts, series, limits, rho*, scaling
x, W, bb = sp.symbols("x W b", positive=True)
kk = sp.symbols("k", positive=True, integer=True)
zero(sp.integrate(sp.exp(-rho * t) * sp.log(1 + x), (t, 0, sp.oo)) - sp.log(1 + x) / rho, "PV of log(1+x)")
assert sp.solve(sp.Eq(sp.log(1 + x) / rho, W), x) == [sp.exp(rho * W) - 1], "x = exp(rho dW) - 1"
zero(al * N / (rho + kk * lam) - eta / (rho / lam + kk), "alpha N/(rho+k lam) = eta/(rho/lam+k)")
ser = sp.summation(bb ** kk / kk, (kk, 1, sp.oo))
for bv in (sp.Rational(1, 5), sp.Rational(1, 3), sp.Rational(9, 10)):
    zero(ser.subs(bb, bv) + sp.log(1 - bv), "sum b^k/k = -ln(1-b)")
zero(-sp.log(1 - b) - sp.log(s1 / s0), "-ln(1-b) = ln(s1/s0)")
zero(sp.exp(D0) - 1 + (s1 - s0) / (1 - s0), "x(inf) = -(s1-s0)/(1-s0)")
cstar = lambda x_: (1 - x_) * (x_ / N) ** eta
zero(Dinf - sp.log(cstar(s1) / cstar(s0)), "x(0) = steady-state consumption gain")
K = np.arange(1, 4001)


def V_ser(r, a, x0, x1, n):
    """rho * Delta W from the series D(0) + eta * sum b^k / (rho/lambda + k), summed until |b|^k < 1e-18."""
    bv = (x1 - x0) / x1
    kk_ = np.arange(1, int(np.ceil(-41.5 / np.log(abs(bv)))) + 11)
    return np.log((1 - x1) / (1 - x0)) + a / (1 - a) * np.sum(bv ** kk_ / (r / ((1 - a) * n) + kk_))


def V_quad(r, a, x0, x1, n):
    return r * quad(lambda tt: np.exp(-r * tt) * D_num(tt, a, x0, x1, n), 0, np.inf, limit=200)[0]


def rho_star(a, x0, x1, n):
    return brentq(lambda r: V_ser(r, a, x0, x1, n), 1e-12, 1e6, xtol=1e-14, rtol=1e-13)


for _ in range(NDRAW):
    a, x0, x1, n = draw()
    lm = (1 - a) * n
    bv = (x1 - x0) / x1
    for r in (0.3 * lm, lm, 4 * lm):
        vq = V_quad(r, a, x0, x1, n)
        dprime = lambda tt: a * n * bv * np.exp(-lm * tt) / (1 - bv * np.exp(-lm * tt))
        ibp = np.log((1 - x1) / (1 - x0)) + quad(lambda tt: np.exp(-r * tt) * dprime(tt), 0, np.inf)[0]
        close(vq, ibp, "integration by parts", tol=1e-6)
        close(vq, V_ser(r, a, x0, x1, n), "series = quadrature", tol=1e-6)
    vals = np.array([V_ser(r, a, x0, x1, n) for r in np.geomspace(1e-4 * lm, 1e3 * lm, 60)])
    assert np.all(np.diff(vals) < 0), "V strictly decreasing in rho"
    close(V_ser(1e-9 * lm, a, x0, x1, n), f_Dinf(a, x0, x1, n), "V(0+) = D(inf)", tol=1e-6)
    close(V_ser(1e9 * lm, a, x0, x1, n), f_D0(a, x0, x1, n), "V(inf) = D(0)", tol=1e-6)
    rs = rho_star(a, x0, x1, n)
    assert V_ser(0.999 * rs, a, x0, x1, n) > 0 > V_ser(1.001 * rs, a, x0, x1, n), "sign change at rho*"
    close(V_quad(rs, a, x0, x1, n), 0.0, "V(rho*) = 0 by quadrature", tol=1e-6)
    f = rng.uniform(0.2, 5.0)
    close(rho_star(a, x0, x1, f * n), f * rs, "rho* proportional to N", tol=1e-8)

# (d) marginal reform, modified golden rule, rho* < rho_m
kss = (s0 / N) ** (1 / (1 - al))
yss = kss ** al
kdot = s * k ** al - N * k
zero(sp.diff(kdot, k).subs({s: s0, k: kss}) + lam, "linearized slope = -lambda")
zero(sp.diff(kdot, s).subs(k, kss) - yss, "d kdot / ds = y0*")
dk = yss / lam * (1 - sp.exp(-lam * t))
zero(sp.diff(dk, t) - (yss - lam * dk), "Delta k solves the linearized ODE")
zero(dk.subs(t, 0), "Delta k(0) = 0")
zero(sp.diff(z ** (1 / (1 - al)), s1).subs(s1, s0) - dk, "Delta k = dk/ds1 of the exact path")
fp = al * kss ** (al - 1)
zero(fp - al * yss / kss, "f'(k0*) = alpha y0*/k0*")
zero(fp - al * N / s0, "f'(k0*) = alpha N/s0")
zero(sp.diff(sp.log((1 - s) * k ** al), s) + 1 / (1 - s), "dln c/ds")
zero(sp.diff(sp.log((1 - s) * k ** al), k) - al / k, "dln c/dk")
zero(rho * sp.integrate(sp.exp(-rho * t) * (1 - sp.exp(-lam.subs(al, 1 - q) * t)), (t, 0, sp.oo)).subs(q, 1 - al)
     - lam / (rho + lam), "rho * PV of (1 - e^{-lambda t})")
zero(sp.diff(D_form1, s1).subs(s1, s0) - (-1 / (1 - s0) + fp * (1 - sp.exp(-lam * t)) / lam), "dD/ds1 at s1=s0")
Vs1 = -1 / (1 - s0) + fp / (rho + lam)
rho_m = N * (al - s0) / s0
zero((1 - s0) * fp - lam - (fp - N), "(1-s0) f' - lambda = f' - N")
zero(fp - N - rho_m, "rho_m = f' - N = N(alpha - s0)/s0")
zero(Vs1.subs(rho, rho_m), "V_s1(s0; rho_m) = 0")
zero(sp.diff(Vs1, rho) + fp / (rho + lam) ** 2, "V_s1(s0; rho) falls with rho")
fk = sp.Symbol("fk", positive=True)
zero(sp.limit((-rho * dt + sp.log(1 + (fk - N) * dt)) / dt, dt, 0) - (fk - N - rho), "Euler from perturbation")
n_, g_, d_ = sp.symbols("n g delta", positive=True)
zero((rho + n_ + g_ + d_) - d_ - (rho + n_ + g_), "f' = rho + N  <=>  f' - delta = rho + n + g")
zero(al * kss ** (al - 1) - (rho_m + N), "k0* is the planner's steady state at rho_m")
d2s1 = sp.diff(DE, s1, 2)
zero(d2s1 - (-1 / (1 - s1) ** 2 - eta * (1 - E) ** 2 / m ** 2), "d2D/ds1^2")
f_Vs1, f_d2s1 = num(Vs1, rho), num(d2s1, E)
for _ in range(NDRAW):
    a, x0, x1, n = draw()
    rm = n * (a - x0) / x0
    h = 1e-5 * x0  # central difference of the series (machine precision; checked against quadrature in (c))
    for r in (0.5 * rm, rm, 2 * rm):
        fd = (V_ser(r, a, x0, x0 + h, n) - V_ser(r, a, x0, x0 - h, n)) / (2 * h)
        close(fd, f_Vs1(a, x0, x1, n, r), "V_s1(s0) by finite differences", tol=1e-6)
    assert rho_star(a, x0, x1, n) < rm, "rho* < rho_m"
    assert V_ser(rm, a, x0, x1, n) < 0, "V(s1; rho_m) < 0"
    assert all(f_d2s1(a, x0, x1, n, e) < 0 for e in (0.0, 0.3, 0.9, 1.0)), "D strictly concave in s1"

# (e) parameter analysis
zero(sp.diff(D0, s1) + 1 / (1 - s1), "dD(0)/ds1")
zero(sp.diff(D0, s0) - 1 / (1 - s0), "dD(0)/ds0")
zero(sp.diff(Dinf, s1) - sp.diff(G(s1), s1), "dD(inf)/ds1 = G'(s1)")
zero(sp.diff(Dinf, s0) + sp.diff(G(s0), s0), "dD(inf)/ds0 = -G'(s0)")
zero(sp.diff(G(s1), s1).subs(s1, al), "G'(alpha) = 0")
zero(sp.diff(rho_m, s1), "rho_m independent of s1")
zero(sp.diff(D0, N) + sp.diff(Dinf, N), "D(0) and D(inf) independent of N")
assert sp.diff(D0, N) == 0, "D(0) independent of N"
zero(sp.diff(rho_m / N, N), "rho_m proportional to N")
zero(sp.diff(rho_m, s0) + N * al / s0 ** 2, "d rho_m / d s0 < 0")
zero(sp.diff(DE, s0) - (1 / (1 - s0) - eta * s1 * (1 - E) / (s0 * s1 * (1 - E) + s0 ** 2 * E)), "dD/ds0")
Rf = ((1 - s0) / (1 - s1)) ** ((1 - al) / al)
zero(sp.diff(Rf, s1, 2) - (1 - al) / al * ((1 - al) / al + 1) * Rf / (1 - s1) ** 2, "R'' > 0: R convex in s1")
zero(sp.diff(DE, s1).subs(s1, al) + s0 * E / ((1 - al) * (al * (1 - E) + s0 * E)), "dD/ds1 at s1 = alpha")
zero(sp.limit(rho_m, s0, al), "rho_m -> 0 as s0 -> alpha")
lim_TR = sp.log(al * (1 - s0) / (al - s0))
assert sp.limit(lim_TR.subs(al, s0 + q), q, 0, "+") == sp.oo, "marginal lambda T_R -> oo as s0 -> alpha"
zero(al * (1 - s0) - (al - s0) - s0 * (1 - al), "alpha(1-s0) - (alpha-s0) = s0(1-alpha) > 0")
f_d2s0, f_dDa = num(sp.diff(DE, s0, 2), E), num(sp.diff(DE, s1).subs(s1, al), E)
f_dDinf1, f_dDinf0 = num(sp.diff(Dinf, s1)), num(sp.diff(Dinf, s0))
f_lim_TR = num(lim_TR)
for _ in range(NDRAW):
    a, x0, x1, n = draw()
    lm, rm = (1 - a) * n, n * (a - x0) / x0
    assert all(f_d2s0(a, x0, x1, n, e) > 0 for e in (0.0, 0.2, 0.8, 1.0)), "D strictly convex in s0"
    assert all(f_dDa(a, x0, x1, n, e) < 0 for e in (0.2, 0.8, 1.0)), "dD/ds1 < 0 at s1 = alpha"
    if x1 < a:
        assert f_dDinf1(a, x0, x1, n) > 0, "D(inf) rises with s1 below alpha"
    assert f_dDinf0(a, x0, x1, n) < 0, "D(inf) falls with s0"
    h = 1e-5 * min(x0, x1 - x0, 1 - x1)
    sec = lambda y: (((1 - x0) / (1 - y)) ** ((1 - a) / a) - 1) / (y - x0)
    assert sec(x1 + h) > sec(x1), "secant slope of R rises with s1"
    assert TR(a, x0, x1 + h, n) > TR(a, x0, x1, n) < TR(a, x0 + h, x1, n), "T_R rises with s1 and s0"
    close(TR(a, x0, x1, 2 * n), TR(a, x0, x1, n) / 2, "T_R proportional to 1/N")
    rs = rho_star(a, x0, x1, n)
    assert rho_star(a, x0, x1 + h, n) < rs > rho_star(a, x0 + h, x1, n), "rho* falls with s1 and s0"
    eps = 1e-6 * x0
    close(TR(a, x0, x0 + eps, n) * lm, f_lim_TR(a, x0, x1, n), "lambda T_R as s1 -> s0", tol=1e-4)
    assert f_lim_TR(a, x0, x1, n) > 0, "limit of lambda T_R is positive"
    close(rho_star(a, x0, x0 + eps, n), rm, "rho* -> rho_m as s1 -> s0", tol=1e-4)
    for r in (0.05 * rm, rm, 3 * rm):
        vga = r * quad(lambda tt: np.exp(-r * tt) * f_dDa(a, x0, x1, n, np.exp(-lm * tt)), 0, np.inf, limit=200)[0]
        assert vga < 0, "V_s1(alpha; rho) < 0"
    vs = lambda y, r: (V_ser(r, a, x0, y + 1e-5, n) - V_ser(r, a, x0, y - 1e-5, n)) / 2e-5  # dV/ds1
    r = rng.uniform(0.05, 0.95) * rm
    assert vs(x0 + 1e-6, r) > 0 > vs(a - 1e-6, r), "V_s1 changes sign on (s0, alpha)"
    assert x0 < brentq(lambda y: vs(y, r), x0 + 1e-6, a - 1e-6) < a, "best constant saving rate in (s0, alpha)"
    r = rng.uniform(1.0, 3.0) * rm                                  # rho >= rho_m: every reform loses, s0 is best
    assert all(V_ser(r, a, x0, y, n) < 0 for y in np.linspace(x0, a, 6)[1:]), "no reform is best for rho >= rho_m"
    assert abs(vs(a, 1e-9 * lm)) < 1e-6 and vs(a, 1e-3 * lm) < 0, "V_s1(alpha; rho) < 0, -> 0 as rho -> 0"

# figures: label positions (alpha = 1/3, s0 = 0.2, lambda = 1) and the 14-term truncation of the series
a, x0 = 1 / 3, 0.2
n1 = 1 / (1 - a)
close(TR(a, x0, 0.3, n1), 0.94738, "fig (b): T_R", tol=1e-5)
close(np.log(7 / 8), -0.133531, "fig (b): D(0)", tol=1e-5)
close(np.log(7 / 8) + 0.5 * np.log(1.5), 0.069202, "fig (b): D(inf)", tol=1e-5)
close(0.5 * np.log(1.5), 0.202733, "fig (b): eta ln(s1/s0)", tol=1e-5)
close(rho_star(a, x0, 0.25, n1), 0.782745, "fig (e): rho*(s1)", tol=1e-5)
close(rho_star(a, x0, 1 / 3, n1), 0.466616, "fig (e): rho*(s1')", tol=1e-5)
close(n1 * (a - x0) / x0, 1.0, "fig (e): rho_m")
assert 0.466616 < 0.782745 < 1.0, "ordering rho*(s1') < rho*(s1) < rho_m"
for bv, x1 in ((0.2, 0.25), (0.4, 1 / 3)):
    close((x1 - x0) / x1, bv, "fig (e): b")
    assert max(0.5 * np.sum(bv ** K[14:] / (u + K[14:])) for u in np.linspace(0, 2.6, 27)) < 1e-6, "14 terms"
close(15 / 16 - 1, -0.0625, "fig (e): asymptote for s1")
close(5 / 6 - 1, -0.166667, "fig (e): asymptote for s1'", tol=1e-5)

print("practice-L1-L2-check-b3b.py: all checks passed")
