#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical checks for Map/aula-07-moeda-inflacao (Kurlat chs. 10-11).

Covered:
  01-money-and-its-supply    the multiplier from two ratios, against a simulated deposit chain;
                             its comparative statics
  02-money-demand            Baumol-Tobin by numerical minimisation vs the closed form; the two
                             costs equal at the optimum; all three elasticities; velocity
  03-equilibrium-and-neut.   Kurlat's deflator/CPI arithmetic and his 8.8% Fisher example; the
                             exact-vs-approximate Fisher error; pi = mu - eps*g; the policy-error
                             formula; superneutrality failing through trip costs
  04-seigniorage-and-costs   the Laffer peak at 1/a analytically and numerically; the unit-
                             elasticity condition; revenue at the peak
  companion-money-regimes    Lista 6 Q1: the money market solved for p, (Y, i) or M by regime;
                             neutrality, i0 (M0/M1)^2, (i0/i1)^(1/2), V = sqrt(2iY/F) = Y/m

Stdlib + numpy; sympy for the expanded derivation steps. Run: python Map/aula-07-moeda-inflacao/check_money.py
"""
from __future__ import annotations

import math

import numpy as np

failures: list[str] = []


def check(name, got, want, tol=1e-9):
    ok = abs(float(got) - float(want)) <= tol
    print(f"  {'ok  ' if ok else 'FAIL'}  {name:<58} {float(got):+.6f}  (want {float(want):+.6f})")
    if not ok:
        failures.append(name)


def check_true(name, cond):
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}")
    if not cond:
        failures.append(name)


# ---------------------------------------------------------------------------
print("\n01-money-and-its-supply")
def multiplier(c, theta):
    return (c + 1) / (c + theta)


c_ratio, theta = 0.20, 0.10
m = multiplier(c_ratio, theta)
check("m = (c+1)/(c+theta)", m, 1.20 / 0.30)
check("...numerically", m, 4.0)

# Simulate the deposit-expansion chain and compare with the closed form.
# One unit of base enters; a share c/(1+c) is held as currency at each round.
def simulate_chain(c, theta, rounds=4000):
    currency_share = c / (1 + c)
    deposits = 0.0
    new_money = 1.0 * (1 - currency_share)     # the part that reaches a bank
    currency = 1.0 * currency_share
    for _ in range(rounds):
        deposits += new_money
        lent = new_money * (1 - theta)
        currency += lent * currency_share
        new_money = lent * (1 - currency_share)
        if new_money < 1e-15:
            break
    return currency + deposits


check("simulated deposit chain reproduces the multiplier",
      simulate_chain(c_ratio, theta), m, tol=1e-6)
for cc, th in ((0.05, 0.02), (0.5, 0.25), (0.1, 0.9)):
    check(f"...also at c={cc}, theta={th}", simulate_chain(cc, th), multiplier(cc, th), tol=1e-6)

check_true("m falls when reserves rise", multiplier(0.2, 0.20) < multiplier(0.2, 0.10))
check_true("m falls when the public holds more currency (theta<1)",
           multiplier(0.4, 0.10) < multiplier(0.2, 0.10))
check("with 100% reserves the multiplier is one", multiplier(0.2, 1.0), 1.0)
check_true("post-2008 style: a big rise in theta collapses the multiplier",
           multiplier(0.2, 0.95) < 1.1)

# ---------------------------------------------------------------------------
print("\n02-money-demand -- Baumol-Tobin")
F, Y, i = 2.0, 1000.0, 0.05


def total_cost(n, F=F, Y=Y, i=i):
    return F * n + i * Y / (2 * n)


def md_closed(F=F, Y=Y, i=i):
    return math.sqrt(F * Y / (2 * i))


def n_star(F=F, Y=Y, i=i):
    return math.sqrt(i * Y / (2 * F))


# Numerical minimisation by golden section on a convex function.
lo, hi = 1e-6, 1e4
gr = (math.sqrt(5) - 1) / 2
a_, b_ = lo, hi
for _ in range(400):
    x1, x2 = b_ - gr * (b_ - a_), a_ + gr * (b_ - a_)
    if total_cost(x1) < total_cost(x2):
        b_ = x2
    else:
        a_ = x1
n_num = 0.5 * (a_ + b_)
check("numerical n* matches the closed form", n_num, n_star(), tol=1e-6)
check("average balances Y/(2n*) match the square-root formula", Y / (2 * n_star()), md_closed())
check("the square-root formula", md_closed(), math.sqrt(2.0 * 1000.0 / (2 * 0.05)), tol=1e-12)

# At the optimum the two costs are equal.
check("transaction cost == forgone interest at n*",
      F * n_star(), i * Y / (2 * n_star()), tol=1e-9)

# Second-order condition.
check_true("total cost is convex at n*", i * Y / n_star() ** 3 > 0)

# The three elasticities, by finite differences on logs.
def elast(var, base, f):
    d = 1e-6
    return (math.log(f(base * (1 + d))) - math.log(f(base * (1 - d)))) / (2 * d)


check("income elasticity == 1/2", elast("Y", Y, lambda y: md_closed(Y=y)), 0.5, tol=1e-6)
check("interest elasticity == -1/2", elast("i", i, lambda x: md_closed(i=x)), -0.5, tol=1e-6)
check("F elasticity == 1/2", elast("F", F, lambda x: md_closed(F=x)), 0.5, tol=1e-6)

# Scale economies: doubling income does NOT double cash.
check("doubling Y raises balances by sqrt(2), not 2",
      md_closed(Y=2 * Y) / md_closed(), math.sqrt(2.0), tol=1e-12)
check_true("...which is strictly less than proportional", md_closed(Y=2 * Y) / md_closed() < 2.0)
check("...while the Cambridge form would give exactly 2", (2 * Y) / Y, 2.0)

# Velocity is an implication, and it is not constant.
def velocity(F=F, Y=Y, i=i):
    return Y / md_closed(F, Y, i)


check("V = sqrt(2iY/F)", velocity(), math.sqrt(2 * i * Y / F), tol=1e-9)
check_true("velocity rises with the interest rate", velocity(i=0.10) > velocity(i=0.05))
check_true("velocity rises with income", velocity(Y=2000) > velocity(Y=1000))
check_true("velocity RISES when trips get cheaper (V = sqrt(2iY/F))",
           velocity(F=1.0) > velocity(F=2.0))
check_true("...equivalently, velocity falls as F rises", velocity(F=4.0) < velocity(F=2.0))
check("MV = PY holds by construction", md_closed() * velocity(), Y, tol=1e-9)

# Financial innovation lowers money demand with no change in Y or i.
check_true("halving F cuts real balances by 1/sqrt(2)",
           abs(md_closed(F=1.0) / md_closed(F=2.0) - 1 / math.sqrt(2)) < 1e-12)

# ---------------------------------------------------------------------------
print("\n03-equilibrium-and-neutrality")
# Kurlat's deflator example: wheat and computers.
p0 = np.array([50.0, 1000.0]); q0 = np.array([10.0, 1.0])
p1 = np.array([60.0, 600.0]);  q1 = np.array([11.0, 2.0])
deflator = 100 * float(p1 @ q1) / float(p0 @ q1)
check("GDP deflator (2018 at 2017 prices)", deflator, 72.94, tol=0.01)
check("...implying inflation of about -27%", deflator / 100 - 1, -0.2706, tol=1e-4)

# The three-good basket: 300 -> 330.
check("CPI goes 100 -> 110", 100 * 330.0 / 300.0, 110.0)
check("...inflation of 10%", 330.0 / 300.0 - 1, 0.10, tol=1e-12)

# Fisher, exact and approximate. Kurlat's 8.8% example.
i_ex, pi_ex = 0.11, 0.02
r_exact = (1 + i_ex) / (1 + pi_ex) - 1
check("exact Fisher real rate", r_exact, 0.08824, tol=1e-5)
check("baskets bought back: 111/102", 111.0 / 102.0, 1.08824, tol=1e-5)
check("...so the real rate is about 8.8 per cent", round(r_exact, 3), 0.088)
check("the approximation gives 9 per cent", i_ex - pi_ex, 0.09)
check("approximation error ~= r*pi", (i_ex - pi_ex) - r_exact, r_exact * pi_ex, tol=1e-4)

# At high inflation the approximation is useless.
i_hi, pi_hi = 0.60, 0.50
r_hi = (1 + i_hi) / (1 + pi_hi) - 1
check("exact real rate at 60% nominal, 50% inflation", r_hi, 0.06667, tol=1e-5)
check("the approximation would say 10 per cent", i_hi - pi_hi, 0.10)
check_true("...a 50% overstatement", (i_hi - pi_hi) / r_hi > 1.4)

# The steady-state decomposition and the policy-error formula.
def inflation(mu, g, eps):
    return mu - eps * g


check("pi = mu - eps*g", inflation(0.035, 0.03, 0.5), 0.02, tol=1e-12)
check("Kurlat's example: believed eps=1/2, true eps=1", inflation(0.035, 0.03, 1.0), 0.005, tol=1e-12)
check("the error equals (eps_hat - eps) * g", (0.5 - 1.0) * 0.03, 0.005 - 0.02, tol=1e-12)
check_true("the error is zero in a stagnant economy", abs((0.5 - 1.0) * 0.0) < 1e-15)
check("a faster-growing economy has LOWER inflation at the same money growth",
      inflation(0.05, 0.06, 0.5) - inflation(0.05, 0.02, 0.5), -0.02, tol=1e-12)

# Neutrality: doubling M doubles P and leaves real balances alone.
def price_level(M, Y, i, F=F):
    return M / md_closed(F, Y, i)


P1 = price_level(1000.0, Y, i)
P2 = price_level(2000.0, Y, i)
check("doubling M doubles P", P2 / P1, 2.0, tol=1e-12)
check("...and leaves real balances unchanged", 2000.0 / P2, 1000.0 / P1, tol=1e-9)

# Superneutrality FAILS: higher money growth raises i, cuts real balances, raises trips.
r_real = 0.02
def trips_at(mu):
    i_nom = r_real + mu                      # Fisher, with pi = mu
    return n_star(i=i_nom)


check_true("faster money growth means more trips to the bank", trips_at(0.10) > trips_at(0.02))
check_true("...and lower real balances", md_closed(i=r_real + 0.10) < md_closed(i=r_real + 0.02))
cost_extra = F * (trips_at(0.10) - trips_at(0.02))
check_true("...costing real resources, so money growth is NOT superneutral", cost_extra > 0)
check("the extra real resource cost", cost_extra, 4.6299, tol=1e-3)

# The price-level jump: M unchanged at the instant of the announcement, so P must jump.
P_before = price_level(1000.0, Y, r_real + 0.02)
P_after = price_level(1000.0, Y, r_real + 0.10)
check_true("announcing faster money growth makes P jump UP immediately", P_after > P_before)
check("the size of the jump", P_after / P_before, math.sqrt((r_real + 0.10) / (r_real + 0.02)), tol=1e-9)

# ---------------------------------------------------------------------------
print("\n04-seigniorage-and-costs")
L, a = 1.0, 3.0


def seigniorage(pi, L=L, a=a):
    return pi * L * math.exp(-a * pi)


pi_peak = 1 / a
check("Laffer peak at pi = 1/a", pi_peak, 1 / 3, tol=1e-12)
grid = np.linspace(1e-6, 3.0, 600001)
rev = grid * L * np.exp(-a * grid)
check("numerical argmax matches 1/a", float(grid[int(np.argmax(rev))]), pi_peak, tol=1e-5)
check("revenue at the peak = L/(a e)", seigniorage(pi_peak), L / (a * math.e), tol=1e-12)
check("...numerically", seigniorage(pi_peak), 0.12263, tol=1e-5)

# Second-order condition.
sec = -a * L * math.exp(-1.0)
check_true("S''(pi_peak) < 0", sec < 0)

# The unit-elasticity condition at the peak.
d = 1e-7
elast_base = (math.log(L * math.exp(-a * (pi_peak * (1 + d)))) -
              math.log(L * math.exp(-a * (pi_peak * (1 - d))))) / (2 * d)
check("base elasticity is exactly -1 at the peak", elast_base, -1.0, tol=1e-6)

# Below the peak more inflation raises revenue; above it, less.
check_true("below the peak, revenue rises with inflation", seigniorage(0.20) < seigniorage(0.30))
check_true("above the peak, revenue FALLS with inflation", seigniorage(0.50) > seigniorage(0.80))
check_true("doubling inflation past the peak lowers revenue",
           seigniorage(2 * pi_peak) < seigniorage(pi_peak))

# A government needing more than the peak cannot get it at any rate.
need = seigniorage(pi_peak) * 1.05
check_true("a demand above the peak is unattainable at every inflation rate",
           all(seigniorage(p) < need for p in np.linspace(1e-6, 50.0, 200001)))

# A higher semi-elasticity pulls the peak down and shrinks the maximum revenue.
check_true("as people learn to economise (a up), the peak falls", 1 / 5.0 < 1 / 3.0)
check_true("...and maximum revenue falls too",
           seigniorage(1 / 5.0, a=5.0) < seigniorage(1 / 3.0, a=3.0))

# The Friedman rule: i = 0 means pi = -r.
check("Friedman rule inflation", -r_real, -0.02)
check("...sets the nominal rate to zero", r_real + (-r_real), 0.0, tol=1e-15)

# ---------------------------------------------------------------------------
print("\ncompanion-money-regimes -- Lista 6 Q1, the four regimes")
# Mirror of solve() in companion-money-regimes.html. Log-split for fixed p under M control:
# d ln m = 1/2 d ln Y - 1/2 d ln i, with share s of ln(M1/M0) carried by Y.
def regimes(inst, flex, Y, i, F, p=1.0, dM=0.0, s=0.0, i1=None):
    b = {"p": p, "Y": Y, "i": i}
    b["M"] = p * md_closed(F, Y, i)
    if inst == "M":
        k = 1 + dM / 100
        a = ({"p": p * k, "Y": Y, "i": i} if flex
             else {"p": p, "Y": Y * k ** (2 * s), "i": i * k ** (-2 * (1 - s))})
        a["M"] = b["M"] * k
    else:
        a = {"p": p, "Y": Y, "i": i1}              # flexible p: level not pinned; today's p held
        a["M"] = p * md_closed(F, Y, i1)
    for x in (b, a):
        x["m"] = md_closed(F, x["Y"], x["i"])
        x["V"] = x["p"] * x["Y"] / x["M"]
    return b, a


REGIME_VECTORS = {
    "flex, M control, +20%": dict(inst="M", flex=True, Y=1000.0, i=0.05, F=2.0, dM=20.0),
    "fixed, M control, +20%, s=0": dict(inst="M", flex=False, Y=1000.0, i=0.05, F=2.0, dM=20.0, s=0.0),
    "fixed, M control, +20%, s=0.5": dict(inst="M", flex=False, Y=1000.0, i=0.05, F=2.0, dM=20.0, s=0.5),
    "fixed, i control, 5% -> 4%": dict(inst="i", flex=False, Y=1000.0, i=0.05, F=2.0, i1=0.04),
}
for name, vec in REGIME_VECTORS.items():
    b, a = regimes(**vec)
    print(f"  [{name}]  " + "  ".join(f"{k}: {b[k]:.6f} -> {a[k]:.6f}" for k in "MpYimV"))
    for tag, x in (("before", b), ("after", a)):
        check(f"{name}: M = p*mD(Y,i) {tag}", x["M"], x["p"] * md_closed(F, x["Y"], x["i"]), tol=1e-9)
        check(f"{name}: V = sqrt(2iY/F) {tag}", x["V"], math.sqrt(2 * x["i"] * x["Y"] / F), tol=1e-9)
        check(f"{name}: V = Y/m {tag}", x["V"], x["Y"] / x["m"], tol=1e-9)

b, a = regimes(**REGIME_VECTORS["flex, M control, +20%"])
check("neutrality: p rises one-for-one with M", a["p"] / b["p"], a["M"] / b["M"], tol=1e-12)
check("...Y unchanged", a["Y"], b["Y"]); check("...i unchanged", a["i"], b["i"])
check("...real balances unchanged", a["m"], b["m"], tol=1e-9)

b, a = regimes(**REGIME_VECTORS["fixed, M control, +20%, s=0"])
check("fixed p, s=0: i1 = i0 (M0/M1)^2", a["i"], b["i"] * (b["M"] / a["M"]) ** 2, tol=1e-12)
check("...Y unchanged", a["Y"], b["Y"])
check("...real balances rise one-for-one with M", a["m"] / b["m"], 1.2, tol=1e-9)
b1, a1 = regimes(inst="M", flex=False, Y=1000.0, i=0.05, F=2.0, dM=20.0, s=1.0)
check("fixed p, s=1: Y1 = Y0 (M1/M0)^2", a1["Y"], b1["Y"] * 1.2 ** 2, tol=1e-9)
check("...i unchanged", a1["i"], b1["i"])
b, a = regimes(**REGIME_VECTORS["fixed, M control, +20%, s=0.5"])
check("fixed p, s=0.5: half of ln(M1/M0) through Y", 0.5 * math.log(a["Y"] / b["Y"]), 0.5 * math.log(1.2), tol=1e-12)
check("...and half through i", -0.5 * math.log(a["i"] / b["i"]), 0.5 * math.log(1.2), tol=1e-12)

b, a = regimes(**REGIME_VECTORS["fixed, i control, 5% -> 4%"])
check("i control: M1/M0 = (i0/i1)^(1/2)", a["M"] / b["M"], math.sqrt(0.05 / 0.04), tol=1e-12)
check_true("...and the bank's rate is what it announced", a["i"] == 0.04)

# ---------------------------------------------------------------------------
print("\nexpanded derivation steps (sympy)")
import sympy as sp  # noqa: E402

cs, ths, Fs, Ys, is_, ns, ts, rs, ps, As, Ls = sp.symbols(
    "c theta F Y i n t r pi a L", positive=True)
zero = lambda e: sp.simplify(e) == 0  # noqa: E731

m_s = (cs + 1) / (cs + ths)
check_true("01: dm/dtheta = -(c+1)/(c+theta)^2", zero(sp.diff(m_s, ths) + (cs + 1) / (cs + ths) ** 2))
check_true("01: dm/dc = (theta-1)/(c+theta)^2", zero(sp.diff(m_s, cs) - (ths - 1) / (cs + ths) ** 2))
s_s = cs / (1 + cs)
D_s = (1 - s_s) / (1 - (1 - ths) * (1 - s_s))
C_s = s_s + s_s * (1 - ths) * D_s
check_true("01: chain deposits D = 1/(c+theta)", zero(D_s - 1 / (cs + ths)))
check_true("01: chain currency C = c/(c+theta)", zero(C_s - cs / (cs + ths)))
check_true("01: C + theta*D = 1 (the base) and C + D = m",
           zero(C_s + ths * D_s - 1) and zero(C_s + D_s - m_s))

avg = ns * sp.integrate(Ys / ns - Ys * ts, (ts, 0, 1 / ns))
check_true("02: sawtooth average = Y/(2n)", zero(avg - Ys / (2 * ns)))
cost = Fs * ns + is_ * Ys / (2 * ns)
nst = sp.sqrt(is_ * Ys / (2 * Fs))
check_true("02: FOC F - iY/(2n^2)", zero(sp.diff(cost, ns) - (Fs - is_ * Ys / (2 * ns ** 2))))
check_true("02: n* solves the FOC", zero(sp.diff(cost, ns).subs(ns, nst)))
check_true("02: C''(n) = iY/n^3", zero(sp.diff(cost, ns, 2) - is_ * Ys / ns ** 3))
check_true("02: F n* = sqrt(FiY/2) = iY/(2n*)",
           zero(Fs * nst - sp.sqrt(Fs * is_ * Ys / 2)) and zero(is_ * Ys / (2 * nst) - sp.sqrt(Fs * is_ * Ys / 2)))
md_s = sp.sqrt(Fs * Ys / (2 * is_))
check_true("02: Y/(2n*) = sqrt(FY/2i)", zero(Ys / (2 * nst) - md_s))
check_true("02: log expansion of M/P",
           zero(sp.expand_log(sp.log(md_s), force=True)
                - (sp.log(Fs) + sp.log(Ys) - sp.log(is_) - sp.log(2)) / 2))
for var, want in ((Ys, sp.Rational(1, 2)), (is_, -sp.Rational(1, 2)), (Fs, sp.Rational(1, 2))):
    check_true(f"02: elasticity wrt {var} = {want}", zero(sp.diff(sp.log(md_s), var) * var - want))
check_true("02: V = Y/(M/P) = sqrt(2iY/F)", zero(Ys / md_s - sp.sqrt(2 * is_ * Ys / Fs)))

ii_s = sp.symbols("i_nom", positive=True)
r_exact = (1 + ii_s) / (1 + ps) - 1
check_true("03: exact r = (i - pi)/(1+pi)", zero(r_exact - (ii_s - ps) / (1 + ps)))
check_true("03: (i - pi) - r = r*pi exactly", zero((ii_s - ps) - r_exact - r_exact * ps))
g_s, eh, et, pt = sp.symbols("g eps_hat eps pi_T")
check_true("03: pi - pi_T = (eps_hat - eps) g",
           zero((pt + eh * g_s - et * g_s) - pt - (eh - et) * g_s))
i0s, i1s = sp.symbols("i0 i1", positive=True)
jump_s = md_s.subs(is_, i0s) / md_s.subs(is_, i1s)
check_true("03: P jump = sqrt(i1/i0)", zero(jump_s - sp.sqrt(i1s / i0s)))
# chain rule for d ln L/dt with Y = Y0 e^{g t}, i = i(t) arbitrary, L Baumol-Tobin
it = sp.Function("i")(ts)
Yt = sp.Symbol("Y0", positive=True) * sp.exp(g_s * ts)
lnL = sp.log(sp.sqrt(Fs * Yt / (2 * it)))
check_true("03: d ln L/dt = eps_Y g + eps_i (di/dt)/i",
           zero(sp.diff(lnL, ts) - (g_s / 2 - sp.diff(it, ts) / (2 * it))))

S_s = ps * Ls * sp.exp(-As * ps)
check_true("04: S' = L e^{-a pi}(1 - a pi)", zero(sp.diff(S_s, ps) - Ls * sp.exp(-As * ps) * (1 - As * ps)))
check_true("04: S'' = -a L e^{-a pi}(2 - a pi)",
           zero(sp.diff(S_s, ps, 2) + As * Ls * sp.exp(-As * ps) * (2 - As * ps)))
check_true("04: S''(1/a) = -a L/e", zero(sp.diff(S_s, ps, 2).subs(ps, 1 / As) + As * Ls * sp.exp(-1)))
check_true("04: S(1/a) = L/(a e)", zero(S_s.subs(ps, 1 / As) - Ls / (As * sp.E)))
base = Ls * sp.exp(-As * ps)
check_true("04: semi-elasticity d ln(M/P)/d pi = -a", zero(sp.diff(sp.log(base), ps) + As))
check_true("04: d ln S/d pi = 1/pi - a", zero(sp.diff(sp.log(S_s), ps) - (1 / ps - As)))
check_true("04: Friedman rule exact: i = 0 at pi = -r/(1+r)",
           zero((1 + rs) * (1 - rs / (1 + rs)) - 1))
check("04: ...which is -1.96% at r = 2%", -0.02 / 1.02, -0.019608, tol=1e-6)
check("04: shoe-leather cost at 2% target, sqrt(F i Y/2)",
      math.sqrt(F * ((1.02 * 1.02) - 1) * Y / 2), 6.3561, tol=1e-4)

# ---------------------------------------------------------------------------
print()
if failures:
    print(f"{len(failures)} CHECK(S) FAILED: " + "; ".join(failures))
    raise SystemExit(1)
print("all checks pass")
