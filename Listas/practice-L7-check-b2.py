"""Lista 7, Block 2 (Questions 3-4, symbolic): independent check of practice-L7-block2.tex.

Run: python practice-L7-check-b2.py   (aborts on the first failed assertion).
Every closed form is re-derived from the model's equations with sympy; every sign, ordering and
existence claim is checked at >= 300 random admissible parameter draws; every limit with sp.limit.
"""
import random
import sympy as sp

random.seed(2026)
NDRAW = 300
U = random.uniform


def zero(e, what):
    assert sp.simplify(e) == 0, f"{what}: {sp.simplify(e)}"


# ---------------------------------------------------------------- symbols and primitives
sg, et, kp, th, rho, Dl, chi, d0, bt = sp.symbols("sigma eta kappa theta rho Delta chi d_0 beta", positive=True)
mu, a, dh = sp.symbols("mu a dhat", real=True)
y, p, pe, pbar, i, g, gb, tc, tcb, ybn, abar, pbn, pi0, ib, ynS, yeS, cc, ccb = sp.symbols(
    "y p p_e pbar i g gbar tau_c taubar_c ybar_n abar pbar_n pi0 ibar y_n y_e c cbar", real=True)
psy, psp, sc, stl, mth = sp.symbols("psi_y psi_pi s_c sigmatilde mu_theta", positive=True)
SYMS = [sg, et, kp, th, rho, Dl, chi, d0, bt, mu, a, dh]
inv = 1 / sg + et


def draw(debt=False):
    """Admissible draw; with debt=True also varpi > 0 and kappa < kmax (stable constant-inflation regime)."""
    v = dict(sigma=U(0.1, 4), eta=U(0.01, 4), kappa=U(0.01, 8), theta=U(1.01, 20), rho=U(0.001, 0.08),
             Delta=U(0.001, 0.2), chi=U(0.05, 0.95), d_0=U(0.01, 4), beta=U(0.5, 0.999),
             mu=U(0.001, 0.3), a=U(-0.2, 0.2), dhat=U(-0.5, -0.001))
    if debt:
        dmax = v["sigma"] * v["chi"] / ((1 - v["beta"]) * (1 - v["chi"]))
        v["d_0"] = U(0.001, 0.999) * min(4.0, dmax)
        v["kappa"] = U(0.001, 0.999) * v["chi"] / ((1 - v["chi"]) * v["d_0"])
    return [v[s.name] for s in SYMS]


def at_draws(expr, test, debt=False, n=NDRAW, what=""):
    """Evaluate expr (or a tuple of expressions) at n admissible draws and assert test(value)."""
    expr = tuple(sp.simplify(e) for e in expr) if isinstance(expr, tuple) else sp.simplify(expr)
    free = set().union(*(e.free_symbols for e in expr)) if isinstance(expr, tuple) else expr.free_symbols
    assert free <= set(SYMS), f"{what}: free symbols {free - set(SYMS)}"
    f = sp.lambdify(SYMS, expr, "math")
    for _ in range(n):
        val = f(*draw(debt))
        assert test(val), f"{what}: {val}"


# eq. (13) to first order: each tax enters ln(1+mu) with coefficient one
tw, ty, tl = sp.symbols("tau_w tau_y tau_l", real=True)
lnmu = sp.log(th / (th - 1)) + sp.log(1 + tw) + sp.log(1 + tc) - sp.log(1 - ty) - sp.log(1 - tl)
assert all(sp.diff(lnmu, t).subs({tw: 0, tc: 0, ty: 0, tl: 0}) == 1 for t in (tw, tc, ty, tl))
# natural output (15): flexible price p~ = w - a + mu, labour supply w - p = eta(y - a) + (y - g)/sigma, p~ = p
Yn = sp.solve(sp.Eq(et * (y - a) + (y - g) / sg - a + mu, 0), y)[0]
zero(Yn - ((1 + et) * a + g / sg - mu) / inv, "eq. (15)")
Ye = sp.solve(sp.Eq(et * (y - a) + (y - g) / sg, a), y)[0]                  # planner, eq. (19)
zero(Yn - Ye + mu / inv, "y_n - y_e")
# AD (21) from the log Euler with consumption taxes and y = s_c c + g, sigma = sigmatilde s_c
c_sol = sp.solve(sp.Eq((ccb - cc) / stl, i - (pbar - p) - (tcb - tc) - rho), cc)[0]
AD = (sc * c_sol + g).subs(ccb, (ybn - gb) / sc).subs(stl, sg / sc)
zero(AD - (ybn + (g - gb) - sg * (i - (pbar - p) - (tcb - tc) - rho)), "AD (21)")
# natural rate: the i that gives y = y_n at p = pbar = p^e
rn = rho + (ybn - ynS) / sg + (g - gb) / sg + (tcb - tc)
zero(sp.solve(sp.Eq(ynS, AD.subs({p: pe, pbar: pe})), i)[0] - rn, "r_n")
s0 = sp.solve([sp.Eq(y, AD), sp.Eq(p, pe + kp * (y - ynS))], [y, p], dict=True)[0]
zero(s0[y] - ynS - sg / (1 + sg * kp) * (rn - i + pbar - pe), "gap formula")
GAP = sg / (1 + sg * kp) * (rn - i + pbar - pe)

# ---------------------------------------------------------------- Q3(a): IPI cut
def rn_tc(t):
    return rn.subs({ynS: Yn.subs(mu, mth + t), tc: t, tcb: 0})
d_yn = sp.simplify(Yn.subs(mu, mth - Dl) - Yn.subs(mu, mth))
d_rn = sp.simplify(rn_tc(-Dl) - rn_tc(0))
key_a = (Dl / inv, et * Dl / inv)
zero(d_yn - key_a[0], "3a dy_n"); zero(d_rn - key_a[1], "3a dr_n")
assert d_rn.subs(et, 0) == 0
at_draws(d_rn, lambda v: v > 0, what="3a dr_n > 0")
opts_a = {"B": (Dl / inv, -Dl / (sg * inv)), "C": ((1 + et) * Dl / inv, (1 - 1 / sg) * et * Dl / inv),
          "D": (Dl / inv, (2 / sg + et) * Dl / inv)}
zero(opts_a["B"][1] - (-d_yn / sg), "3a B = supply only")
zero(opts_a["C"][1] - (Dl - (1 + et) * Dl / inv / sg), "3a C = productivity analogy")
zero(opts_a["D"][1] - (Dl + d_yn / sg), "3a D = sign slip")
for k, o in opts_a.items():
    at_draws((o[0] - key_a[0], o[1] - key_a[1]), lambda v: abs(v[0]) + abs(v[1]) > 1e-9, what=f"3a {k} differs")

# ---------------------------------------------------------------- Q3(b): spending multipliers
Om = inv * (1 + sg * kp)
yn_g = Yn.subs({a: 0, mu: 0})
ADg = AD.subs({tc: 0, tcb: 0, gb: 0})
sb = sp.solve([sp.Eq(y, ADg), sp.Eq(p, pe + kp * (y - yn_g))], [y, p], dict=True)[0]
m_y, m_gap = sp.diff(sb[y], g), sp.diff(sb[y] - yn_g, g)
key_b = ((1 / sg + et + kp) / Om, et / Om)
zero(m_y - key_b[0], "3b m_y"); zero(m_y - (1 / (1 + sg * kp) + kp / Om), "3b m_y form")
zero(m_gap - key_b[1], "3b m_gap"); zero(m_y - 1 + sg * et * kp / Om, "3b m_y - 1")
zero(m_gap / m_y - et / (1 / sg + et + kp), "3b gap share")
s_noAS = sp.solve([sp.Eq(y, ADg), sp.Eq(p, pe + kp * y)], [y, p], dict=True)[0]  # AS shift forgotten
opts_b = {"A": (sp.diff(s_noAS[y], g), sp.diff(s_noAS[y], g)), "B": (m_y, m_y), "C": (sp.diff(yn_g, g), sp.Integer(0))}
zero(opts_b["A"][0] - inv / Om, "3b A"); zero(opts_b["C"][0] - (1 / sg + kp) / Om, "3b C")
for k, o in opts_b.items():
    at_draws((o[0] - key_b[0], o[1] - key_b[1]), lambda v: abs(v[0]) + abs(v[1]) > 1e-9, what=f"3b {k} differs")

# ---------------------------------------------------------------- Q3(c): ZLB commitment
zero(GAP.subs({i: 0, pbar: pe - rn}), "3c gap closed")
assert kp not in rn.free_symbols and kp not in Yn.free_symbols            # cure independent of rigidity

# ---------------------------------------------------------------- Q4(a): targeting rule
L = (y - yeS) ** 2 / 2 + th / (2 * kp) * (kp * (y - ynS)) ** 2
zero(sp.diff(L, y, 2) - (1 + th * kp), "4a SOC")
ystar = sp.solve(sp.diff(L, y), y)[0]
zero(ystar - (yeS + th * kp * ynS) / (1 + th * kp), "4a y*")
zero((ystar - yeS) + th * kp * (ystar - ynS), "4a targeting rule")
zero(L.subs({ynS: yeS, y: yeS}), "4a divine coincidence"); zero(ystar.subs(ynS, yeS) - yeS, "4a y*=y_e")
zero(GAP.subs(i, rn + pbar - pe), "4a i = r_n + pbar - p^e")

# ---------------------------------------------------------------- Q4(b): cost-push shock
M = mu / inv
zero(M - (Ye - Yn), "4b M")
ys = (Ye + th * kp * Yn) / (1 + th * kp)
zero(ys - Yn - M / (1 + th * kp), "4b y*-y_n"); zero(ys - Ye + th * kp * M / (1 + th * kp), "4b y*-y_e")
pg = kp * (ys - Yn)
zero(pg - kp * M / (1 + th * kp), "4b p-p^e")
Ls = (ys - Ye) ** 2 / 2 + th / (2 * kp) * pg ** 2
zero(Ls - th * kp / (1 + th * kp) * M ** 2 / 2, "4b L*"); zero(Ls / ((Yn - Ye) ** 2 / 2) - th * kp / (1 + th * kp), "4b ratio")
at_draws(M - th * kp * M / (1 + th * kp), lambda v: v > 0, what="4b |y*-y_e| < M")
at_draws(kp * M - pg, lambda v: v > 0, what="4b p-p^e < kappa M")
sub_b = {ynS: Yn.subs(g, 0), ybn: 0, g: 0, gb: 0, tc: 0, tcb: 0, pbar: pe}
istar = sp.solve(sp.Eq(ys.subs(g, 0) - Yn.subs(g, 0), GAP.subs(sub_b)), i)[0]
rn_b = rn.subs(sub_b)
zero(rn_b - (rho + (mu - (1 + et) * a) / (sg * inv)), "4b r_n")
zero(istar - (rn_b - (1 / sg + kp) * M / (1 + th * kp)), "4b i*")
at_draws(rn_b - istar, lambda v: v > 0, what="4b i* < r_n")
zero(sp.diff(istar - rn_b, a), "4b offset one for one"); zero(sp.diff(ys - Yn, a), "4b gaps free of a")
ir = (kp * (th / sg - 1) * mu - (1 + et) * (1 + th * kp) * a / sg) / (inv * (1 + th * kp))
zero(istar - rho - ir, "4b i* - rho")
f_ir = sp.lambdify(SYMS, ir, "math")
for _ in range(NDRAW):
    v = draw(); v[SYMS.index(a)] = -abs(v[SYMS.index(a)]); v[SYMS.index(th)] = v[0] + U(0.01, 10)
    assert f_ir(*v) > 0, "4b i* > rho when a <= 0, theta > sigma"
at_draws((ir.subs(a, 0), th - sg), lambda v: (v[0] > 0) == (v[1] > 0), what="4b a=0: sign = sign(theta-sigma)")
# Taylor rule under a pure productivity shock
sub_t = {ybn: 0, g: 0, gb: 0, tc: 0, tcb: 0, pbar: pe}
yn0, ye0 = Yn.subs({mu: 0, g: 0}), Ye.subs(g, 0)
zero(yn0 - ye0, "4b y_n = y_e when mu = 0")
st = sp.solve([sp.Eq(y, AD.subs(sub_t)), sp.Eq(p, pe + kp * (y - yn0)),
               sp.Eq(i, ib + psy * (y - ye0) + psp * (p - pe))], [y, p, i], dict=True)[0]
rn_t = rn.subs(sub_t).subs(ynS, yn0)
gap_t = (rn_t - ib) / (1 / sg + kp + psy + psp * kp)
zero(st[y] - yn0 - gap_t, "4b gap under the rule")
zero(sp.diff(rn_t, a) + (1 + et) / (sg * inv), "4b dr_n/da")
assert sp.limit(gap_t, psp, sp.oo) == 0

# ---------------------------------------------------------------- Q4(c): pessimism and the ZLB
ybn_p = Yn.subs({a: abar, g: 0, mu: 0})
zero(ybn_p - (1 + et) * abar / inv, "4c ybar_n")
rn_c = rn.subs({ybn: ybn_p, ynS: 0, g: 0, gb: 0, tc: 0, tcb: 0})
zero(rn_c - (rho + (1 + et) * abar / (1 + sg * et)), "4c r_n")
zero(rn_c - (1 + et) / (1 + sg * et) * (abar + rho * (1 + sg * et) / (1 + et)), "4c threshold")
gap_c = GAP.subs({ynS: 0, ybn: ybn_p, g: 0, gb: 0, tc: 0, tcb: 0, pbar: pe})
zero(sp.diff(gap_c, i) + sg / (1 + sg * kp), "4c gap falls with i")
y0, p0 = gap_c.subs(i, 0), kp * gap_c.subs(i, 0)
zero(y0 - sg * rn_c / (1 + sg * kp), "4c y at i=0"); zero(p0 - sg * kp * rn_c / (1 + sg * kp), "4c p at i=0")
zero(GAP.subs({ynS: 0, ybn: ybn_p, g: 0, gb: 0, tc: 0, tcb: 0, i: 0, pbar: pe - rn_c}), "4c remedy")
assert sp.limit(y0, kp, sp.oo) == 0 and sp.simplify(sp.limit(p0, kp, sp.oo) - rn_c) == 0
assert sp.simplify(sp.limit(y0, kp, 0) - sg * rn_c) == 0 and sp.limit(p0, kp, 0) == 0

# ---------------------------------------------------------------- Q4(d): borrowers and savers
phi = (sg * chi + (1 - chi) * d0 * bt) / chi
AD32 = ybn - phi * (i - (pbn - p) - rho) + (g - gb) / chi + (1 - chi) / chi * (dh + d0 * (p - pe))
vp = sg - d0 * (1 - bt) * (1 - chi) / chi
zero(sp.diff(AD32, p) + vp, "4d anchored slope"); zero(phi - sg - (1 - chi) * d0 * bt / chi, "4d channels")
AD32c = AD32.subs(pbn, p + pi0)
zero(sp.diff(AD32c, p) - (1 - chi) * d0 / chi, "4d constant-inflation slope")
s = 1 / (1 + sg * et)
zero(sp.diff(yn_g, g) - s, "4d s")
x = (1 - chi) * d0 * kp
base = {ybn: 0, i: rho, gb: 0}
sA = sp.solve([sp.Eq(y, AD32.subs(base).subs(pbn, pe)), sp.Eq(p, pe + kp * (y - yn_g))], [y, p], dict=True)[0]
sC = sp.solve([sp.Eq(y, AD32c.subs(base).subs(pi0, 0)), sp.Eq(p, pe + kp * (y - yn_g))], [y, p], dict=True)[0]
mA, mC = sp.diff(sA[y], g), sp.diff(sC[y], g)
zero(mA - (1 / chi + vp * kp * s) / (1 + vp * kp), "4d m_A"); zero(mC - (1 - x * s) / (chi - x), "4d m_C")
w = vp * kp / (1 + vp * kp)
zero(mA - (w * s + (1 - w) / chi), "4d m_A average")
zero(mC - 1 / chi - x * (1 - chi * s) / (chi * (chi - x)), "4d m_C - 1/chi")
at_draws(mC - 1 / chi, lambda v: v > 0, debt=True, what="4d m_C > 1/chi")
at_draws(1 / chi - mA, lambda v: v > 0, debt=True, what="4d 1/chi > m_A")
at_draws(mA - s, lambda v: v > 0, debt=True, what="4d m_A > s")
zero(mA - 1 - ((1 - chi) / chi - vp * kp * (1 - s)) / (1 + vp * kp), "4d m_A - 1")
zero(vp * kp * (1 - s) - (1 - chi) / chi - (vp * kp - (1 - chi) * (1 + sg * et) / (chi * sg * et)) * (1 - s), "4d threshold")
at_draws((mA - 1, (1 - chi) * (1 + sg * et) / (chi * sg * et) - vp * kp), lambda v: (v[0] > 0) == (v[1] > 0),
         debt=True, what="4d m_A > 1 iff condition")
zero(mC - 1 - ((1 - chi) + x * (1 - s)) / (chi - x), "4d m_C - 1")
zero(sg - vp - d0 * (1 - bt) * (1 - chi) / chi, "4d sigma - varpi > 0")
zero(mA.subs(et, 0) - 1 - (1 - chi) / (chi * (1 + vp * kp)), "4d m_A > 1 when eta = 0")
zero(sp.limit(mA, chi, 1) - key_b[0], "4d chi -> 1 gives Q3(b)")

# ---------------------------------------------------------------- Q4(e) and Q3(d): deleveraging
yA, yC = sA[y].subs(g, 0), sC[y].subs(g, 0)
zero(yA - (1 - chi) * dh / (chi * (1 + vp * kp)), "4e y_A"); zero(yC - (1 - chi) * dh / (chi - x), "4e y_C")
zero(sp.diff(yC, kp) - (1 - chi) ** 2 * d0 * dh / (chi - x) ** 2, "3d dy_C/dkappa")
kmax = chi / ((1 - chi) * d0)
zero(x.subs(kp, kmax) - chi, "4e bound"); zero(1 / sp.diff(AD32c, p) - kmax, "4e AD slope = kmax")
at_draws(yC, lambda v: v < 0, debt=True, what="4e y_C < 0 below kmax")
lA, lC = -yA, -yC
zero(chi * (1 + vp * kp) - (chi * (1 + sg * kp) - (1 - bt) * d0 * (1 - chi) * kp), "4e identity (i)")
zero(sp.diff(lC, kp) - (1 - chi) ** 2 * d0 * (-dh) / (chi - x) ** 2, "4e dlC/dkappa")
zero(sp.diff(lC, d0) - (1 - chi) ** 2 * kp * (-dh) / (chi - x) ** 2, "4e dlC/dd0")
zero(sp.diff(lC, chi) + (-dh) / (chi - x) ** 2, "4e dlC/dchi")
z, ss = sp.symbols("z s", positive=True)
mAz = (1 / chi + z * ss) / (1 + z)
zero(sp.diff(mAz, z) - (ss - 1 / chi) / (1 + z) ** 2, "4e dmA/d(varpi kappa)")
zero(sp.diff(mAz, ss) - z / (1 + z), "4e dmA/ds")
xs = sp.Symbol("x", positive=True)
zero(sp.diff((1 - xs * ss) / (chi - xs), ss) + xs / (chi - xs), "4e dmC/ds")
zero(sp.diff(mC, chi) + (1 + d0 * kp * (1 - s)) / (chi - x) ** 2, "4e dmC/dchi")
TABLE = {"l_A": (lA, {kp: -1, d0: 1, chi: -1, sg: -1}), "l_C": (lC, {kp: 1, d0: 1, chi: -1, sg: 0}),
         "m_A": (mA, {kp: -1, d0: 1, chi: -1, sg: -1}), "m_C": (mC, {kp: 1, d0: 1, chi: -1, sg: 1})}
for name, (f, signs) in TABLE.items():
    for par, sgn in signs.items():
        der = sp.diff(f, par)
        if sgn == 0:
            zero(der, f"table {name}/{par}")
        else:
            at_draws(sgn * der, lambda v: v > 0, debt=True, what=f"table {name}/{par}")
zero(sp.diff(mC.subs(et, 0), sg), "table m_C/sigma = 0 at eta = 0")
# limits and knife-edges
wv = sp.Symbol("varpi", positive=True)
yAw, mAw = (1 - chi) * dh / (chi * (1 + wv * kp)), (1 / chi + wv * kp * s) / (1 + wv * kp)
for f in (yA, yC):
    zero(sp.limit(f, kp, 0) - (1 - chi) * dh / chi, "4e kappa -> 0 (y)")
for f in (mA, mC):
    zero(sp.limit(f, kp, 0) - 1 / chi, "4e kappa -> 0 (m)")
assert sp.limit(yAw, kp, sp.oo) == 0
zero(sp.limit(mAw, kp, sp.oo) - s, "4e m_A -> s")
eps = sp.Symbol("epsilon", positive=True)
q = sp.Symbol("q", positive=True)                                          # chi = 1/(1+q) in (0,1)
for f_ in (lC.subs(dh, -Dl), mC):
    assert sp.limit(sp.simplify(f_.subs(kp, kmax * (1 - eps)).subs(chi, 1 / (1 + q))), eps, 0, "+") == sp.oo
assert sp.limit(yA, chi, 1) == 0 and sp.limit(yC, chi, 1) == 0 and sp.limit(mC, chi, 1) == 1
d0k = sg * chi / ((1 - bt) * (1 - chi))
zero(vp.subs(d0, d0k), "4e varpi = 0")
zero(yA.subs(d0, d0k) - (1 - chi) * dh / chi, "4e knife-edge y_A"); zero(mA.subs(d0, d0k) - 1 / chi, "4e knife-edge m_A")
# figure: chi = 2/3, d0 = 1.2, beta = 0.98, sigma = 0.5, dhat = -0.1 (ticks suppressed in the .tex)
fig = {chi: sp.Rational(2, 3), d0: sp.Rational(6, 5), bt: sp.Rational(49, 50), sg: sp.Rational(1, 2), dh: sp.Rational(-1, 10)}
assert vp.subs(fig) == sp.Rational(61, 125)                                  # 0.488 > 0
zero(yA.subs(fig) - (-sp.Rational(1, 20)) / (1 + sp.Rational(61, 125) * kp), "fig y_A")
zero(yC.subs(fig) - (-sp.Rational(1, 30)) / (sp.Rational(2, 3) - sp.Rational(2, 5) * kp), "fig y_C")
assert kmax.subs(fig) == sp.Rational(5, 3) and ((1 - chi) * dh / chi).subs(fig) == -sp.Rational(1, 20)

print("practice-L7-check-b2.py: all checks passed")
