#!/usr/bin/env python3
"""Checks for Simulados/simulado-05.tex (mock exam 5, whole course).

Re-derives every closed form with sympy and recomputes every number printed in the
answer key; exits non-zero on the first mismatch list. Also prints the Solow
time-path coordinates plotted in Q1(b).

Run: python Simulados/simulado_codigo/check_simulado_05.py
"""
from __future__ import annotations

import math
import sys

import sympy as sp

failures: list[str] = []


def check(name, got, want, tol=5e-4):
    ok = abs(float(got) - float(want)) <= tol
    print(f"  {'ok  ' if ok else 'FAIL'}  {name:<60} {float(got):+.6f}  (want {float(want):+.6f})")
    if not ok:
        failures.append(name)


def check_sym(name, expr):
    """expr must simplify to zero."""
    ok = sp.simplify(expr) == 0
    print(f"  {'ok  ' if ok else 'FAIL'}  {name}")
    if not ok:
        failures.append(name)


def check_true(name, cond):
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}")
    if not cond:
        failures.append(name)


# ======================================================================= Q1(a)
print("\nQ1(a) coffee chain, three approaches")
fert_imp, fert_sale, w_tr = 50, 80, 10
coffee, to_roaster, exports, stock, w_farm = 300, 200, 60, 40, 120
pack_imp, roasted, w_roast = 20, 450, 150
teachers = 100
check_true("farm output splits into sales + exports + stock", to_roaster + exports + stock == coffee)
va = {"trader": fert_sale - fert_imp, "farm": coffee - fert_sale,
      "roaster": roasted - to_roaster - pack_imp, "gov": teachers}
gdp_p = sum(va.values())
check("VA trader", va["trader"], 30)
check("VA farm", va["farm"], 220)
check("VA roaster", va["roaster"], 230)
check("GDP product", gdp_p, 580)
prof = {"trader": va["trader"] - w_tr, "farm": va["farm"] - w_farm,
        "roaster": va["roaster"] - w_roast, "gov": 0}
check("profit trader", prof["trader"], 20)
check("profit farm", prof["farm"], 100)
check("profit roaster", prof["roaster"], 80)
wages = w_tr + w_farm + w_roast + teachers
check("wages", wages, 380)
check("GDP income", wages + sum(prof.values()), 580)
C, I, G, X, M = roasted, stock, teachers, exports, fert_imp + pack_imp
check("GDP expenditure", C + I + G + X - M, 580)
check("imports", M, 70)
# next year: stock sold to roaster, roasted and sold for 90
check("year-2 VA of this coffee (roaster)", 90 - stock, 50)
check("year-2 expenditure C + dInv", 90 + (-stock), 50)

# ======================================================================= Q1(b)
print("\nQ1(b) Solow golden rule")
s, a, A, nd = sp.symbols("s alpha A n_delta", positive=True)
k_ss = (s * A / nd) ** (1 / (1 - a))
c_ss = (1 - s) * A * k_ss ** a
foc = sp.diff(sp.log(c_ss), s)
sol = sp.solve(sp.Eq(foc, 0), s)
check_true(f"s_GR = alpha (sympy gives {sol})", len(sol) == 1 and sp.simplify(sol[0] - a) == 0)
kgr = sp.symbols("k", positive=True)
k_gr = sp.solve(sp.Eq(a * A * kgr ** (a - 1), nd), kgr)[0]
xc = (nd * k_gr / (A * k_gr ** a) - a)
check_true("cross-check: s = (n+delta) k_GR / f(k_GR) = alpha (draws)",
           all(abs(float(xc.subs({a: a_, A: A_, nd: n_}))) < 1e-12
               for a_ in (0.2, 1 / 3, 0.6) for A_ in (0.5, 2) for n_ in (0.03, 0.1)))
c_ratio = lambda s1, s0, al: ((1 - s1) * s1 ** (al / (1 - al))) / ((1 - s0) * s0 ** (al / (1 - al)))
al, s0, s1 = 1 / 3, 0.15, 1 / 3
check("c* ratio new/old", c_ratio(s1, s0, al), 1.169186)
check("impact c ratio (1-s1)/(1-s0)", (1 - s1) / (1 - s0), 0.784314)
check("y* ratio", (s1 / s0) ** (al / (1 - al)), 1.490712)
check("k* ratio", (s1 / s0) ** (1 / (1 - al)), 3.312693)
check("wrong-exponent answer s=1/(2-alpha) (Prova 01 slip)", 1 / (2 - al), 0.6)
# time path, A = 1, n = 1%, delta = 5%, annual
n, d = 0.01, 0.05
k = (s0 / (n + d)) ** (1 / (1 - al))
c_old = (1 - s0) * k ** al
path, cross = [], None
for t in range(0, 151):
    c_t = (1 - s1) * k ** al
    path.append((t, c_t / c_old, k))
    if cross is None and c_t >= c_old:
        cross = t
    k = ((1 - d) * k + s1 * k ** al) / (1 + n)
print("  time path (t, c/c_old, y/y_old):")
y_old = ((s0 / (n + d)) ** (1 / (1 - al))) ** al
coords_c = " ".join(f"({t},{v:.4f})" for t, v, _ in path[::10])
coords_y = " ".join(f"({t},{kk ** al / y_old:.4f})" for t, _, kk in path[::10])
print("   c:", coords_c)
print("   y:", coords_y)
print(f"   c regains c_old in year {cross}")
check("c regains old level in year", cross, 18, tol=0.5)
check("c/c_old at t=150 close to 1.169", path[150][1], 1.169186, tol=2e-3)

# ======================================================================= Q2
print("\nQ2 labour supply in general equilibrium")
L, tau, psi, alp = sp.symbols("L tau psi alpha", positive=True)
# rebate: c = Y, FOC psi/(1-L) = (1-tau)(1-alpha)/L
L_reb = sp.solve(sp.Eq(psi * L, (1 - tau) * (1 - alp) * (1 - L)), L)[0]
L_was = sp.solve(sp.Eq(psi * L * (1 - tau * (1 - alp)), (1 - tau) * (1 - alp) * (1 - L)), L)[0]
L_pl = sp.solve(sp.Eq(sp.diff((1 - alp) * sp.log(L) + psi * sp.log(1 - L), L), 0), L)[0]
check_sym("rebate closed form", L_reb - (1 - tau) * (1 - alp) / (psi + (1 - tau) * (1 - alp)))
check_sym("planner L = (1-a)/(1-a+psi)", L_pl - (1 - alp) / (1 - alp + psi))
check_sym("CE(tau=0) = planner (First Welfare Theorem)", L_reb.subs(tau, 0) - L_pl)
check_sym("waste with alpha=0: L independent of tau", sp.diff(L_was.subs(alp, 0), tau))
check_sym("waste with tau=0 equals planner", L_was.subs(tau, 0) - L_pl)
dreb = sp.diff(L_reb, tau)
check_true("dL_rebate/dtau < 0 (random draws)",
           all(dreb.subs({tau: t_, psi: p_, alp: a_}) < 0
               for t_ in (0.1, 0.4, 0.8) for p_ in (0.2, 1, 3) for a_ in (0.1, 0.33, 0.6)))
check_true("L_rebate < L_waste < L0 for tau in (0,1), alpha in (0,1) (draws)",
           all(L_reb.subs({tau: t_, psi: p_, alp: a_}) < L_was.subs({tau: t_, psi: p_, alp: a_})
               < L_pl.subs({psi: p_, alp: a_})
               for t_ in (0.1, 0.4, 0.8) for p_ in (0.2, 1, 3) for a_ in (0.1, 0.33, 0.6)))
vals = {tau: sp.Rational(1, 4), psi: sp.Rational(1, 3), alp: sp.Rational(1, 3)}
L0 = L_pl.subs(vals)
Lr = L_reb.subs(vals)
Lw = L_was.subs(vals)
check("L0", L0, 2 / 3)
check("L rebate", Lr, 0.6)
check("L waste", Lw, 9 / 14)
check("substitution effect Lr - L0", Lr - L0, -1 / 15)
check("income effect Lw - Lr", Lw - Lr, 9 / 14 - 0.6)
check("total Lw - L0", Lw - L0, 9 / 14 - 2 / 3)
# with A Kbar^alpha = 1
Y = lambda l: float(l) ** (2 / 3)
check("Y0 = (2/3)^(2/3)", Y(L0), 0.763143)
check("Y rebate = 0.6^(2/3)", Y(Lr), 0.711379)
check("Y waste", Y(Lw), (9 / 14) ** (2 / 3))
w0, wr = (2 / 3) * Y(L0) / float(L0), (2 / 3) * Y(Lr) / float(Lr)
check("w0", w0, 0.763143)
check("w rebate", wr, 0.790421)
check("after-tax wage rebate", 0.75 * wr, 0.592816)
check("MRS at rebate point = psi c / l", (1 / 3) * Y(Lr) / (1 - float(Lr)), 0.75 * wr)
check("transfer T = tau w L", 0.25 * wr * float(Lr), 0.118563)
check("capital income alpha Y", Y(Lr) / 3, 0.237126)
check("budget intercept at l=1 (rK + T)", Y(Lr) / 3 + 0.25 * wr * float(Lr), 0.355689)
Gw = 0.25 * (2 / 3) * Y(Lw)
check("G (waste) = tau (1-a) Y", Gw, 0.124144)
check("c waste = (5/6) Y", (5 / 6) * Y(Lw), Y(Lw) - Gw)
U = lambda l: math.log(Y(l)) + (1 / 3) * math.log(1 - float(l))
check("U0", U(L0), -0.636514)
check("U rebate", U(Lr), -0.645979)
lam = math.exp(U(L0) - U(Lr)) - 1
check("consumption-equivalent loss (rebate)", lam, 0.009510, tol=2e-5)
check("rebate revenue share of Y: tau (1-a)", 0.25 * 2 / 3, 1 / 6)
check("ln(1+lambda) = U0 - UR", U(L0) - U(Lr), 0.00947, tol=5e-5)
check("Y waste printed 0.7449", Y(Lw), 0.7449, tol=5e-5)
check("c waste printed 0.6207", (5 / 6) * Y(Lw), 0.6207, tol=5e-5)
# same G raised lump-sum: psi (Y - G)/(1 - L) = (1 - alpha) Y / L, Y = L^(2/3)
L_ls = sp.nsolve(sp.Rational(1, 3) * (L ** sp.Rational(2, 3) - Gw) / (1 - L)
                 - sp.Rational(2, 3) * L ** sp.Rational(2, 3) / L, L, 0.7)
check("lump-sum L for the same G", L_ls, 0.703470)
check_true("lump-sum L above L0 (pure income effect)", L_ls > L0)
U_g = lambda l, c: math.log(c) + (1 / 3) * math.log(1 - float(l))
Uw, Uls = U_g(Lw, (5 / 6) * Y(Lw)), U_g(L_ls, Y(L_ls) - Gw)
check("U waste (labour tax)", Uw, -0.8201, tol=5e-5)
check("U lump-sum", Uls, -0.8104, tol=5e-5)
check("consumption-equivalent gap labour vs lump-sum", math.exp(Uls - Uw) - 1, 0.00971, tol=5e-5)
U_tau = lambda t: U((1 - t) * (2 / 3) / (1 / 3 + (1 - t) * (2 / 3)))
dU0 = sp.diff(((1 - alp) * sp.log(L_reb) + psi * sp.log(1 - L_reb)), tau).subs(tau, 0)
check_sym("envelope: dU/dtau = 0 at tau = 0", dU0)
lam_half = math.exp(U(L0) - U_tau(0.125)) - 1
check("loss at tau = 12.5%", lam_half, 0.002012, tol=5e-6)
check("ratio of losses 12.5% / 25%", lam_half / lam, 0.2115, tol=5e-4)

# ======================================================================= Q3
print("\nQ3 Baumol-Tobin, inflation, seigniorage")
N, i, Yv, F = sp.symbols("N i Y F", positive=True)
cost = i * Yv / (2 * N) + F * N
N_star = sp.solve(sp.Eq(sp.diff(cost, N), 0), N)[0]
check_sym("N* = sqrt(iY/2F)", N_star - sp.sqrt(i * Yv / (2 * F)))
m_bt = Yv / (2 * N_star)
check_sym("m = sqrt(FY/2i)", m_bt - sp.sqrt(F * Yv / (2 * i)))
check_sym("income elasticity 1/2", sp.diff(sp.log(m_bt), Yv) * Yv - sp.Rational(1, 2))
check_sym("interest elasticity -1/2", sp.diff(sp.log(m_bt), i) * i + sp.Rational(1, 2))
check_sym("velocity Y/m = 2N", Yv / m_bt - 2 * N_star)
check_sym("min cost = sqrt(2iFY)", cost.subs(N, N_star) - sp.sqrt(2 * i * F * Yv))
check_sym("trip cost F N* = sqrt(iFY/2)", F * N_star - sp.sqrt(i * F * Yv / 2))
num = {Yv: 60000, F: 25}
for iv, Nw, mw in ((0.12, 12, 2500), (0.06, math.sqrt(72), 60000 / (2 * math.sqrt(72)))):
    check(f"N at i={iv}", N_star.subs(num).subs(i, iv), Nw)
    check(f"m at i={iv}", m_bt.subs(num).subs(i, iv), mw)
check("velocity at 12%", 60000 / 2500, 24)
r, g, eta = 0.03, 0.04, 0.5
mu0, mu1 = 0.11, 0.05
pi0, pi1 = mu0 - eta * g, mu1 - eta * g
check("pi before", pi0, 0.09)
check("pi after", pi1, 0.03)
check("i before (Kurlat Fisher)", r + pi0, 0.12)
check("i after", r + pi1, 0.06)
check("exact Fisher before", 1.03 * 1.09 - 1, 0.1227)
jump = math.sqrt(0.12 / 0.06)
check("m jump factor", jump, 1.414214)
check("p jump (level) 1/sqrt2 - 1", 1 / jump - 1, -0.292893)
check("remonetisation dM/M", jump - 1, 0.414214)
m0, m1 = 2500, 2500 * jump
check("m after", m1, 3535.534)
check("S before = mu m", mu0 * m0, 275)
check("S after", mu1 * m1, 176.777)
check("inflation tax before pi m", pi0 * m0, 225)
check("inflation tax after", pi1 * m1, 106.066)
check("growth part before eta g m", eta * g * m0, 50)
check("growth part after", eta * g * m1, 70.711)
# d ln S / d mu > 0 for BT whenever i > 0
mu = sp.symbols("mu", positive=True)
S_bt = mu * sp.sqrt(F * Yv / (2 * (r + mu - eta * g)))
dlnS = sp.simplify(sp.diff(sp.log(S_bt), mu))
check_sym("dlnS/dmu = 1/mu - 1/(2 i)", dlnS - (1 / mu - 1 / (2 * (r + mu - eta * g))))
check_true("BT seigniorage increasing on mu in (0, 50)",
           all(dlnS.subs(mu, x) > 0 for x in (0.001, 0.05, 0.5, 1, 5, 50)))
aa = sp.symbols("a", positive=True)
S_cg = mu * Yv * sp.exp(-aa * (r + mu - eta * g))
mu_peak = sp.solve(sp.Eq(sp.diff(S_cg, mu), 0), mu)
check_true(f"Cagan peak mu = 1/a ({mu_peak})", len(mu_peak) == 1 and sp.simplify(mu_peak[0] - 1 / aa) == 0)
check_true("Cagan SOC < 0 at peak",
           sp.simplify(sp.diff(S_cg, mu, 2).subs(mu, 1 / aa)).subs({aa: 2, Yv: 1}) < 0)
check("Cagan peak with a=2", 1 / 2, 0.5)
check("trip cost before", 25 * 12, 300)
check("trip cost before / Y", 300 / 60000, 0.005)
check("trip cost after", math.sqrt(0.06 * 25 * 60000 / 2), 212.132)
check("trip cost after / Y", math.sqrt(0.06 * 25 * 60000 / 2) / 60000, 0.0035355)
check("Friedman rule pi = -r", -r, -0.03)
check("Friedman rule mu = eta g - r", eta * g - r, -0.01)
# normalised Laffer values used in the figure (index S(mu)/S(0.11))
bt = lambda x: x / math.sqrt(r + x - eta * g)
cg = lambda x: x * math.exp(-2 * (r + x - eta * g))
check("BT index at mu=3", bt(3) / bt(0.11), 5.4455, tol=1e-3)
check("Cagan index at peak 0.5", cg(0.5) / cg(0.11), 2.0836, tol=1e-3)

# ======================================================================= Q4
print("\nQ4 Benigno: mark-up, optimal policy, ZLB, fiscal")
y = sp.symbols("y", real=True)
sig, et, kap, phi, Dl = sp.symbols("sigma eta kappa phi Delta", positive=True)
yn = -Dl          # y_e = 0, y_n = -Delta, Delta = mu/(1/sigma+eta)
Loss = sp.Rational(1, 2) * y ** 2 + phi / (2 * kap) * (kap * (y - yn)) ** 2
y_opt = sp.solve(sp.diff(Loss, y), y)[0]
p_opt = kap * (y_opt - yn)
check_sym("y* = -phi kappa Delta/(1+phi kappa)", y_opt + phi * kap * Dl / (1 + phi * kap))
check_sym("targeting rule (y-ye) + phi (p-pe) = 0", y_opt + phi * p_opt)
i_gap = -(y_opt + sig * p_opt) / sig          # i* - rho from AD with ybar_n = pbar = 0
check_sym("i* - rho = kappa (phi - sigma) Delta / (sigma (1+phi kappa))",
          i_gap - kap * (phi - sig) * Dl / (sig * (1 + phi * kap)))
check_sym("phi -> inf: i* - rho = Delta/sigma", sp.limit(i_gap, phi, sp.oo) - Dl / sig)
check_sym("phi = 0: i* - rho = -kappa Delta", i_gap.subs(phi, 0) + kap * Dl)
nv = {sig: 1, et: 1, kap: sp.Rational(1, 2), Dl: 2}
check("Delta = 4/(1+1)", 4 / (1 + 1), 2)
check("y* (phi=4)", y_opt.subs(nv).subs(phi, 4), -4 / 3)
check("p* (phi=4)", p_opt.subs(nv).subs(phi, 4), 1 / 3)
check("i* - rho (phi=4)", i_gap.subs(nv).subs(phi, 4), 1)
check("i* - rho (phi=1/2)", i_gap.subs(nv).subs(phi, sp.Rational(1, 2)), -0.4)
check("i* - rho (phi=sigma=1)", i_gap.subs(nv).subs(phi, 1), 0)
check("no policy y = sk yn/(1+sk)", 0.5 * (-2) / 1.5, -2 / 3)
check("no policy p", 0.5 * (-2 / 3 + 2), 2 / 3)
loss = lambda yy, pp, ph=4: 0.5 * yy ** 2 + ph / (2 * 0.5) * pp ** 2
check("loss no policy (phi=4)", loss(-2 / 3, 2 / 3), 0.5 * 4 / 9 + 4 * 4 / 9)
check("loss optimum (phi=4)", loss(-4 / 3, 1 / 3), 0.5 * 16 / 9 + 4 / 9)
check_true("optimum beats no policy", loss(-4 / 3, 1 / 3) < loss(-2 / 3, 2 / 3))
# ZLB
rho = 2
r_n = rho + (-4 - 0) / 1
check("r_n after ybar_n = -4", r_n, -2)
ys, ps = sp.symbols("ys ps")
z = sp.solve([sp.Eq(ys, -4 - 1 * (0 - (0 - ps) - rho)), sp.Eq(ps, sp.Rational(1, 2) * ys)], [ys, ps])
check("ZLB y", z[ys], -4 / 3)
check("ZLB p", z[ps], -2 / 3)
check("ZLB loss (phi=4)", loss(-4 / 3, -2 / 3), 8 / 3)
check("forward guidance pbar = -r_n", -r_n, 2)
gg = sp.symbols("g")
om = sp.Rational(1, 2)  # sigma^-1/(sigma^-1+eta)
zg = sp.solve([sp.Eq(ys, -4 + gg - 1 * (0 - (0 - ps) - rho)),
               sp.Eq(ps, sp.Rational(1, 2) * (ys - om * gg))], [ys, ps])
mg = sp.diff(zg[ys], gg)
check("ZLB multiplier on y", mg, 5 / 6)
s_, k_, o_ = sp.symbols("s k o", positive=True)
om_s = (1 / s_) / (1 / s_ + et)
check_sym("m_g = (1 + s k omega)/(1 + s k) equals Benigno Table 1 form",
          (1 + s_ * k_ * om_s) / (1 + s_ * k_)
          - (1 / (1 + s_ * k_) + k_ / ((1 / s_ + et) * (1 + s_ * k_))))
check_sym("gap multiplier (1 - omega)/(1 + s k) = eta/D (Benigno m_gbar)",
          (1 - om_s) / (1 + s_ * k_) - et / ((1 / s_ + et) * (1 + s_ * k_)))
check("gap multiplier", mg - om, 1 / 3)
g_close = sp.solve(sp.Eq(zg[ys] - om * gg, 0), gg)[0]
check("g that closes the gap", g_close, 4)
check("y at g=4", zg[ys].subs(gg, 4), 2)
check("p at g=4", zg[ps].subs(gg, 4), 0)
check("multiplier under unconstrained optimal policy = omega_g", om, 0.5)
check_true("ZLB multiplier > omega_g iff omega_g < 1", (1 + 0.5 * om) / 1.5 > om)

print()
if failures:
    print(f"{len(failures)} FAILURE(S):", *failures, sep="\n  ")
    sys.exit(1)
print("ALL CHECKS PASSED")
