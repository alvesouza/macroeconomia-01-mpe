"""Practice list D (Lista 7), Question 6 (practice-L7-block3b.tex): a pandemic in Benigno's borrower-saver AS-AD.

Independent check of every closed form, sign, limit, ordering and plotted point of the question.
Run: python practice-L7-check-b3b.py   (aborts on the first failed assertion).
Closed forms: sympy, simplify(lhs - rhs) == 0. Signs and orderings: a signed closed form or NDRAW random
admissible draws (0<alpha<1, sigma, eta > 0, theta > 1, 0<chi<1, d0 > 0, 0<beta<1, a<0, mu>0, abar<0, dhat<0).
"""
import math
import random
from functools import lru_cache

import sympy as sp

random.seed(20261007)
NDRAW = 400


def same(lhs, rhs, what):
    """Assert the symbolic identity lhs == rhs; `what` names the claim in the .tex."""
    diff = sp.together(lhs - rhs)
    assert sp.cancel(diff) == 0 or sp.simplify(diff) == 0, what


sg, et, al, th, ch, d0, be, kap, rho, z = sp.symbols("sigma eta alpha theta chi d_0 beta kappa rho z", positive=True)
a, mu, ab, dh, i, p, y, Dl, g = sp.symbols("a mu abar dhat i p y Delta g", real=True)
pe, pbn, gb, tb, tbb, r, pi0 = sp.symbols("p^e pbar_n gbar tau_b taubar_b r pi0", real=True)
SYMS = (sg, et, al, th, ch, d0, be, rho, kap, a, mu, ab, dh)
S = 1 / sg + et


@lru_cache(maxsize=None)
def _fn(expr):
    return sp.lambdify(SYMS, expr, "math")


def ev(expr, d):
    """Value of a sympy expression at the draw d (a tuple ordered as SYMS)."""
    return float(_fn(expr)(*d))


def draws(keep=None, n=NDRAW):
    """n admissible parameter draws (rho = -ln beta, kappa from alpha), filtered by keep(d)."""
    out = []
    while len(out) < n:
        s, e, A = random.uniform(.1, 5), random.uniform(.05, 5), random.uniform(.05, .95)
        B = random.uniform(.8, .999)
        d = (s, e, A, random.uniform(1.01, 20), random.uniform(.05, .95), random.uniform(.01, 3), B, -math.log(B),
             (1 - A) * (1 / s + e) / A, -random.uniform(.01, 1), random.uniform(.01, 1), -random.uniform(.01, 1),
             -random.uniform(.01, 1))
        if keep is None or keep(d):
            out.append(d)
    return out


# ---------------------------------------------------------------- (a) supply side
Ls, Lb, Cs, Cb, Ws, Wb, P = sp.symbols("L_s L_b C_s C_b W_s W_b P", positive=True)
foc = lambda L, C, W: L**et * sp.exp(z * C) / z / (W / P)                    # v_l/u_c over W/P, = 1 at each optimum
agg = foc(Ls**ch * Lb**(1 - ch), ch * Cs + (1 - ch) * Cb, Ws**ch * Wb**(1 - ch))
same(sp.expand_log(sp.log(foc(Ls, Cs, Ws)**ch * foc(Lb, Cb, Wb)**(1 - ch)), force=True),
     sp.expand_log(sp.log(agg), force=True), "aggregation of the two labor conditions")
yn = ((1 + et) * a - mu) / S
ye = (1 + et) * a / S
ybn = (1 + et) * ab / S
gap_rel = et * (y - a) + y / sg - a + mu                                      # p~ - p with g = 0
same(gap_rel, S * (y - yn), "p~ - p = (1/sigma+eta)(y - y_n)")
same(sp.solve(gap_rel, y)[0], yn, "y_n")
Psol = sp.solve(sp.Eq(p, al * pe + (1 - al) * (p + S * (y - yn))), p)[0]
same(Psol - pe, (1 - al) * S / al * (y - yn), "AS slope kappa")
same(ye, yn.subs(mu, 0), "y_e is y_n without the wedge")
same(ye - yn, mu / S, "wedge y_e - y_n")
same(sp.diff(yn, a), (1 + et) / S, "dy_n/da")
same(sp.diff(ye, a), (1 + et) / S, "dy_e/da")
same(sp.diff(yn, mu), -1 / S, "dy_n/dmu")
assert sp.diff(ye, mu) == 0 and sp.diff(yn, ab) == 0 and sp.diff(ybn, a) == 0 and sp.diff(ybn, mu) == 0
for d in draws():
    assert ev(yn, d) < 0 and ev(ye, d) < 0 and ev(ybn, d) < 0 and ev(ye - yn, d) > 0, "(a) signs"
    assert ev(-(1 - al) * S / al * sp.diff(yn, mu), d) > 0, "(a) AS shifts up with mu"

# ---------------------------------------------------------------- (b) demand and equilibrium
phi = (sg * ch + (1 - ch) * d0 * be) / ch
AD32 = ybn - phi * (i - (pbn - p) - rho) + ((g - gb) - (1 - ch) * (tb - tbb)) / ch + (1 - ch) / ch * (dh + d0 * (p - pe))
varpi = sg - d0 * (1 - be) * (1 - ch) / ch
zeta = ybn - phi * (i - rho) + (1 - ch) / ch * dh
base = {pbn: 0, pe: 0, g: 0, gb: 0, tb: 0, tbb: 0}
same(AD32.subs(base), zeta - varpi * p, "anchored AD y = zeta - varpi p")
same(phi - (1 - ch) * d0 / ch, varpi, "varpi = phi - (1-chi)d0/chi")
same(ch * varpi, sg * ch - d0 * (1 - be) * (1 - ch), "chi varpi (AD slopes down iff sigma chi > d0(1-beta)(1-chi))")
ze, w, ynx = sp.symbols("zeta varpi y_n", real=True)
eq = sp.solve([sp.Eq(y, ze - w * p), sp.Eq(p, kap * (y - ynx))], [y, p], dict=True)[0]
same(eq[y], (ze + w * kap * ynx) / (1 + w * kap), "equilibrium y")
same(eq[p], kap * (ze - ynx) / (1 + w * kap), "equilibrium p")
assert sp.Matrix([[1, w], [-kap, 1]]).det() == 1 + w * kap                    # unique iff 1 + varpi kappa != 0
i_n = rho + (ybn - yn + (1 - ch) / ch * dh) / phi
same(sp.solve(sp.Eq(zeta, yn), i)[0], i_n, "i_n")
same(zeta - yn, phi * (i_n - i), "zeta - y_n = phi (i_n - i)")
Yeq = (zeta + varpi * kap * yn) / (1 + varpi * kap)
same(Yeq - yn, phi * (i_n - i) / (1 + varpi * kap), "natural gap")
same(Yeq - ye, phi * (i_n - i) / (1 + varpi * kap) - mu / S, "efficient gap")
same(phi * (i_n - rho), ((1 + et) * (ab - a) + mu) / S + (1 - ch) / ch * dh, "decomposition of i_n")
for v, sgn in [(a, -1), (mu, 1), (ab, 1), (dh, 1)]:                           # supply raises i_n, demand shocks lower it
    for d in draws(n=50):
        assert sgn * ev(sp.diff(i_n, v), d) > 0, f"di_n/d{v}"
stable = lambda d: ev(1 + varpi * kap, d) > 0
signs = [ev(i_n, d) < 0 for d in draws(stable)]
assert any(signs) and not all(signs), "sign of i_n is ambiguous"
for d in draws(lambda d: stable(d) and ev(i_n, d) < 0):
    assert ev((Yeq - yn).subs(i, 0), d) < 0 and ev((Yeq - ye).subs(i, 0), d) < 0, "(b) gaps at i=0"
    assert ev(kap * (Yeq - yn).subs(i, 0), d) < 0 and ev(phi, d) > 0, "(b) deflation at i=0"

# ---------------------------------------------------------------- (c) fiscal transfers
Cdiff = dh - be * d0 * (r - rho) + d0 * (p - pe) + (y - ybn) - (tb - tbb)     # (C_b - Cbar_b)/Y~
y31 = sp.solve(sp.Eq(y, ybn + (g - gb) - ch * sg * (r - rho) + (1 - ch) * Cdiff).subs(r, i - (pbn - p)), y)[0]
same(y31, AD32, "eq. (32) from (31) and the borrowers' budget")
dy = sp.Symbol("dy")
same(sp.solve(sp.Eq(dy, (1 - ch) * (dy + Dl)), dy)[0], (1 - ch) * Dl / ch, "fixed-price cross")
AD_T = zeta + (1 - ch) / ch * Dl - varpi * p
same(AD32.subs({**base, tb: -Dl}), AD_T, "transfer enters (32) as (1-chi)/chi Delta")
solT = sp.solve([sp.Eq(y, AD_T), sp.Eq(p, kap * (y - yn))], [y, p], dict=True)[0]
mT = 1 / (ch * (1 + varpi * kap))
same(sp.diff(solT[y], Dl) / (1 - ch), mT, "transfer multiplier m_T")
same(sp.diff(solT[p], Dl) / (1 - ch), kap * mT, "price effect kappa m_T")
yn_g = ((1 + et) * a + g / sg - mu) / S
same(sp.diff(yn_g, g), 1 / (1 + sg * et), "dy_n/dg")
solG = sp.solve([sp.Eq(y, zeta + g / ch - varpi * p), sp.Eq(p, kap * (y - yn_g))], [y, p], dict=True)[0]
same(sp.diff(solG[y], g) - mT, varpi * kap / ((1 + sg * et) * (1 + varpi * kap)), "m_g - m_T")
De = sp.solve(sp.Eq(solT[y].subs(i, rho), ye), Dl)[0]
same(De, -dh + ch / (1 - ch) * ((1 + et) * (a - ab) + varpi * kap * mu) / S, "Delta_e")
same(solT[p].subs({i: rho, Dl: De}), kap * mu / S, "p - p^e at Delta_e")
same(De * (1 - ch) * S, (1 - ch) * (-dh) * S + ch * ((1 + et) * (a - ab) + varpi * kap * mu), "sign of Delta_e")
for d in draws(lambda d: ev(varpi, d) > 0 and d[9] >= d[11]):
    assert ev(De, d) > 0, "Delta_e > 0 when a >= abar and varpi > 0"
same(sp.limit(mT, ch, 1), 1 / (1 + sg * kap), "m_T as chi -> 1")
assert sp.limit(ch * (1 + varpi * kap) / (1 - ch), ch, 1, "-") == sp.oo        # transfer per borrower explodes

# ---------------------------------------------------------------- (d) policy mix
yex, ynx2 = sp.symbols("y_e y_nn", real=True)
Lg = (y - yex)**2 / 2 + th / kap * (kap * (y - ynx2))**2 / 2                   # loss (33) on the AS
same(sp.solve(sp.diff(Lg, y), y)[0], (yex + th * kap * ynx2) / (1 + th * kap), "y* from the loss")
dlt = mu / (S * (1 + th * kap))
ystar = (ye + th * kap * yn) / (1 + th * kap)
same(ystar, yn + dlt, "y* = y_n + delta")
same((ystar - ye) + th * kap * (ystar - yn), 0, "targeting rule at y*")
zs = sp.solve(sp.Eq((ze + varpi * kap * yn) / (1 + varpi * kap), ystar), ze)[0]
same(zs, yn + (1 + varpi * kap) * dlt, "zeta implementing y*")
zetaD = ybn - phi * (i - rho) + (1 - ch) / ch * (dh + Dl)
istar = sp.solve(sp.Eq(zetaD.subs(Dl, 0), zs), i)[0]
same(istar, i_n - (1 + varpi * kap) * dlt / phi, "i*")
line = ch * phi * (i - istar) / (1 - ch)
same(zetaD.subs(Dl, line), zs, "every (i, Delta) on the line implements y*")
same(sp.diff(line, i), ch * phi / (1 - ch), "slope of the line")
y1 = Yeq.subs(i, 0)
same(y1 - ystar, phi * istar / (1 + varpi * kap), "y_1 - y*")
Ly = (y - ye)**2 / 2 + th * kap * (y - yn)**2 / 2
same(Ly - Ly.subs(y, ystar), (1 + th * kap) * (y - ystar)**2 / 2, "loss is a parabola around y*")
cost = (1 + th * kap) * phi**2 * istar**2 / (2 * (1 + varpi * kap)**2)
same(((1 + th * kap) * (y - ystar)**2 / 2).subs(y, ystar + phi * istar / (1 + varpi * kap)), cost, "welfare cost")
for d in draws():                                                               # direct evaluation of L(y_1) - L(y*)
    assert abs(ev(Ly.subs(y, y1) - Ly.subs(y, ystar), d) - ev(cost, d)) <= 1e-9 * max(1., ev(cost, d)), "welfare cost"
yD = (zetaD + varpi * kap * yn) / (1 + varpi * kap)
Drho = sp.solve(sp.Eq(yD.subs(i, rho), ystar), Dl)[0]
Dzlb = sp.solve(sp.Eq(yD.subs(i, 0), ystar), Dl)[0]
same(Drho, ch * phi * (rho - istar) / (1 - ch), "Delta_rho")
same(Dzlb, ch * phi * (-istar) / (1 - ch), "Delta_zlb")
same(Dzlb, ch / (1 - ch) * ((1 + varpi * kap) * dlt - phi * i_n), "Delta_zlb, second form")
same(Drho - Dzlb, ch * phi * rho / (1 - ch), "Delta_rho - Delta_zlb")
for d in draws(stable):
    assert ev(istar, d) < ev(i_n, d) and ev(ch * phi / (1 - ch), d) > 0, "i* < i_n; line slopes up"
for d in draws(lambda d: stable(d) and ev(istar, d) < 0):
    assert ev(y1 - ystar, d) < 0 and ev(kap * (y1 - ystar), d) < 0, "(i) shortfall at the bound"
    assert ev(Dzlb, d) > 0 and ev(Drho - Dzlb, d) > 0 and ev(Ly.subs(y, y1) - Ly.subs(y, ystar), d) > 0, "(ii)-(iii)"
binds = [ev(istar, d) < 0 for d in draws(lambda d: stable(d) and ev(i_n, d) >= 0)]
assert any(binds) and not all(binds), "i* < 0 <= i_n occurs: the optimum's condition is weaker"
# graph: the values in the tikzpicture (admissible), and the picture's claims
Gv = (1., 1., .75, 1.5, .6, 1., .9, -math.log(.9), (1 - .75) * 2 / .75, -.5, 1., -1., -1.5)
gx = lambda e: ev(e, Gv)
assert gx(varpi) > 0 and gx(i_n) < 0 and gx(istar) < 0, "graph: AD slopes down, the bound binds"
Y1, Yn, Ys, Ye, P1, Ps = gx(y1), gx(yn), gx(ystar), gx(ye), gx(kap * (y1 - yn)), gx(kap * dlt)
assert Y1 < Yn < Ys < Ye < 0 and P1 < 0 < Ps, "graph: orderings of the ticks"
assert -2.1 < Y1 and Ps < .7 and P1 > -.7, "graph: points inside the axis box"
Z1, Zs, VP, K = gx(zeta.subs(i, 0)), gx(zs), gx(varpi), gx(kap)
assert Z1 < Zs < 0 and abs(Z1 - (Yn + gx(phi * i_n))) < 1e-12, "graph: AD1 left of AD2 left of AD0"
assert abs(P1 - (Z1 - Y1) / VP) < 1e-9 and abs(Ps - (Zs - Ys) / VP) < 1e-9, "graph: E1 on AD1, E* on AD2"
assert abs(Ps - K * (Ys - Yn)) < 1e-9 and abs(Ps + (Ys - Ye) / 1.5) < 1e-9, "graph: E* on AS1 and on the rule"
print(f"graph: y1={Y1:.4f} yn={Yn:.4f} y*={Ys:.4f} ye={Ye:.4f} p1={P1:.4f} p*={Ps:.4f} zeta1={Z1:.4f} zeta*={Zs:.4f}")

# ---------------------------------------------------------------- (e) parameter analysis
same(ch * (1 + varpi * kap), ch * (1 + sg * kap) - kap * d0 * (1 - be) * (1 - ch), "chi(1+varpi kappa)")
same(sp.diff(mT, ch), -mT**2 * (1 + sg * kap + kap * d0 * (1 - be)), "dm_T/dchi")
same(sp.diff(mT, d0), mT**2 * kap * (1 - be) * (1 - ch), "dm_T/dd0")
same(sp.diff(mT, kap), -mT**2 * ch * varpi, "dm_T/dkappa")
F = ch * (1 + varpi * kap) * dlt - ch * phi * i_n
same(F, (1 - ch) * Dzlb, "F = (1-chi) Delta_zlb")
same(ch * phi * i_n, ch * phi * rho + ch * (ybn - yn) + (1 - ch) * dh, "chi phi i_n")
same(ch * phi, sg * ch + (1 - ch) * be * d0, "chi phi")
assert all(sp.diff(e, v) == 0 for e in (yn, ybn) for v in (ch, d0, al))        # y_n, ybar_n: none of chi, d0, alpha
assert sp.diff(dlt, ch) == 0 and sp.diff(dlt, d0) == 0                          # delta: neither chi nor d0 ...
assert sp.diff(dlt.subs(kap, (1 - al) * S / al), al) != 0                       # ... but alpha, through kappa
same(sp.diff(Dzlb, d0), -(kap * (1 - be) * dlt + be * rho), "dDelta_zlb/dd0")
same(sp.diff(Dzlb, kap), ch / (1 - ch) * mu * (varpi - th) / (S * (1 + th * kap)**2), "dDelta_zlb/dkappa")
same(sp.diff(F, ch, 2), 0, "F affine in chi")
F1 = F.subs(ch, 1)
same(F1, (1 + sg * kap) * dlt - sg * rho - (ybn - yn), "F(1)")
same(F1, -sg * istar.subs(ch, 1), "F(1) = -sigma i*_RA")
same(sp.diff(Dzlb, ch), F1 / (1 - ch)**2, "dDelta_zlb/dchi")
same(sp.limit(F, ch, 1), F1, "Delta_zlb (1-chi) -> F(1) as chi -> 1")
yC = sp.solve([sp.Eq(y, AD32.subs({**base, pbn: p + pi0, tb: -Dl})), sp.Eq(p, kap * (y - yn))], [y, p], dict=True)[0][y]
mTc = 1 / (ch - (1 - ch) * d0 * kap)
same(sp.diff(yC, Dl) / (1 - ch), mTc, "m_T^c")
same(sp.diff(mTc, ch), -mTc**2 * (1 + d0 * kap), "dm_T^c/dchi")
same(sp.diff(mTc, d0), mTc**2 * (1 - ch) * kap, "dm_T^c/dd0")
same(sp.diff(mTc, kap), mTc**2 * (1 - ch) * d0, "dm_T^c/dkappa")
same(1 / mT - 1 / mTc, kap * ch * phi, "1/m_T - 1/m_T^c")
same(sp.diff(yC, dh), (1 - ch) * mTc, "slump from dhat, constant inflation")
same(sp.diff(solT[y], dh), (1 - ch) * mT, "slump from dhat, anchored")
dMk, dDk, dDc = sp.diff(mT, kap), sp.diff(Dzlb, kap), sp.diff(Dzlb, ch)
for d in draws(stable):                                                         # the sign table, row by row
    assert ev(sp.diff(mT, ch), d) < 0 and ev(sp.diff(mT, d0), d) > 0 and (ev(dMk, d) < 0) == (ev(varpi, d) > 0), "m_T row"
    assert ev(sp.diff(Dzlb, d0), d) < 0 and (ev(dDk, d) < 0) == (ev(varpi, d) < d[3]), "Delta_zlb row, d0 and kappa"
    assert (ev(dDc, d) > 0) == (ev(istar.subs(ch, 1), d) < 0), "Delta_zlb row, chi"
    assert ev(1 / mT - 1 / mTc, d) > 0, "m_T^c > m_T"
for d in draws(lambda d: ev(ch - (1 - ch) * d0 * kap, d) > 0):
    assert ev(sp.diff(mTc, ch), d) < 0 and ev(sp.diff(mTc, d0), d) > 0 and ev(sp.diff(mTc, kap), d) > 0, "m_T^c row"
    assert ev(sp.diff((1 - ch) * mTc * dh, kap), d) < 0, "paradox of flexibility: slump deepens with kappa"
dd = draws(stable)
assert any(ev(varpi, d) > d[3] for d in dd) and any(ev(varpi, d) < d[3] for d in dd), "varpi vs theta both occur"
assert any(ev(istar.subs(ch, 1), d) < 0 for d in dd) and any(ev(istar.subs(ch, 1), d) > 0 for d in dd), "i*_RA both signs"
wp, eps = sp.symbols("w_p epsilon", positive=True)
assert sp.limit(mT, kap, 0) == 1 / ch and sp.limit(1 / (ch * (1 + wp * kap)), kap, sp.oo) == 0
same(sp.limit(mT, d0, 0), 1 / (ch * (1 + sg * kap)), "m_T as d0 -> 0")
assert sp.limit(mTc, kap, 0) == 1 / ch and sp.limit(mTc, d0, 0) == 1 / ch and sp.limit(mTc, ch, 1) == 1
same(mTc.subs(kap, ch / ((1 - ch) * d0) - eps), 1 / ((1 - ch) * d0 * eps), "m_T^c diverges at the bound")
same(mT.subs(kap, (eps - 1) / varpi), 1 / (ch * eps), "m_T diverges as 1 + varpi kappa -> 0+")
same(sp.limit(Dzlb, kap, 0), ch / (1 - ch) * (mu / S - phi * i_n), "Delta_zlb as kappa -> 0")
for d in draws(lambda d: ev(varpi, d) < 0):
    assert (d[8] < -1 / ev(varpi, d)) == (ev(1 + varpi * kap, d) > 0), "anchored stability"
for d in draws():
    assert (d[8] < d[4] / ((1 - d[4]) * d[5])) == (ev(ch - (1 - ch) * d0 * kap, d) > 0), "constant-inflation stability"
iLB = sp.Symbol("i_lb", real=True)
same(sp.solve(sp.Eq(yD.subs(i, iLB), ystar), Dl)[0], ch * phi * (iLB - istar) / (1 - ch), "effective lower bound")
same(sp.diff(yD, Dl), (1 - ch) * mT, "y rises with Delta (and p = kappa (y - y_n) with it)")

print("practice-L7-check-b3b.py: all checks passed")
