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

Stdlib + numpy only. Run: python Map/aula-07-moeda-inflacao/check_money.py
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
print()
if failures:
    print(f"{len(failures)} CHECK(S) FAILED: " + "; ".join(failures))
    raise SystemExit(1)
print("all checks pass")
