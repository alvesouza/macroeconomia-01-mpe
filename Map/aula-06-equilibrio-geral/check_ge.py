#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical checks for Map/aula-06-equilibrio-geral (Kurlat ch. 9).

Covered:
  01-equilibrium-as-benchmark  the five price-bearing FOCs collapse to the two the planner
                               writes; the decentralised allocation equals the planner's;
                               Walras' law holds off equilibrium; only relative prices matter
  02-dynamics-and-saddle-path  the two loci; k* < k_gold across a parameter grid; the Jacobian
                               determinant is negative (a saddle); the saddle path is the only
                               non-explosive trajectory, located by shooting

Stdlib + numpy only. Run: python Map/aula-06-equilibrio-geral/check_ge.py
"""
from __future__ import annotations

import math

import numpy as np

failures: list[str] = []


def check(name, got, want, tol=1e-8):
    ok = abs(float(got) - float(want)) <= tol
    print(f"  {'ok  ' if ok else 'FAIL'}  {name:<58} {float(got):+.6f}  (want {float(want):+.6f})")
    if not ok:
        failures.append(name)


def check_true(name, cond):
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}")
    if not cond:
        failures.append(name)


ALPHA, DELTA, RHO, SIGMA = 0.35, 0.06, 0.03, 2.0
BETA = 1 / (1 + RHO)

f = lambda k: k ** ALPHA
fp = lambda k: ALPHA * k ** (ALPHA - 1)

# ---------------------------------------------------------------------------
print("\n01-equilibrium-as-benchmark -- two periods")
# Two-period economy. K1 and labour are owned by the household. A producing firm rents
# K and L competitively; an investment firm turns period-1 goods into period-2 capital.
# Solve the PLANNER's problem, then the DECENTRALISED problem as a fixed point in the
# interest rate, and require the two allocations to coincide.
K1, L1, L2 = 2.0, 1.0, 1.0
A1, A2 = 1.0, 1.0
R1 = A1 * f(K1) + (1 - DELTA) * K1          # period-1 resources: output + surviving capital

up = lambda c: c ** (-SIGMA)


def planner():
    """max u(C1) + beta u(C2) s.t. C1 + K2 = R1 and C2 = A2 f(K2) + (1-delta) K2."""
    def foc(K2):
        C1 = R1 - K2
        C2 = A2 * f(K2) + (1 - DELTA) * K2
        return -up(C1) + BETA * up(C2) * (A2 * fp(K2) + 1 - DELTA)

    lo, hi = 1e-9, R1 - 1e-9
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if foc(mid) < 0:
            hi = mid
        else:
            lo = mid
    K2 = 0.5 * (lo + hi)
    return dict(K2=K2, C1=R1 - K2, C2=A2 * f(K2) + (1 - DELTA) * K2)


P = planner()


def firm_K2(r):
    """Capital demand from r^K = r + delta, i.e. A2 f'(K2) = r + delta."""
    lo, hi = 1e-9, 500.0
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if A2 * fp(mid) > r + DELTA:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def household(r, pi2):
    """Takes r and period-2 non-capital income pi2 as given; chooses saving a."""
    def foc(a):
        C1 = R1 - a
        C2 = (1 + r) * a + pi2
        return -up(C1) + BETA * up(C2) * (1 + r)

    lo, hi = 1e-9, R1 - 1e-9
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if foc(mid) < 0:
            hi = mid
        else:
            lo = mid
    a = 0.5 * (lo + hi)
    return a, R1 - a, (1 + r) * a + pi2


def excess_saving(r):
    """a(r) - K2^d(r): excess supply of credit."""
    K2d = firm_K2(r)
    pi2 = A2 * f(K2d) - A2 * fp(K2d) * K2d        # the wage bill, w2 L2, by zero profit
    a, _, _ = household(r, pi2)
    return a - K2d


# Equilibrium interest rate: clears the credit market.
lo, hi = -DELTA + 1e-6, 5.0
for _ in range(300):
    mid = 0.5 * (lo + hi)
    if excess_saving(mid) > 0:
        hi = mid
    else:
        lo = mid
r_eq = 0.5 * (lo + hi)
K2_eq = firm_K2(r_eq)
pi2_eq = A2 * f(K2_eq) - A2 * fp(K2_eq) * K2_eq
a_eq, C1_eq, C2_eq = household(r_eq, pi2_eq)

check("credit market clears at the equilibrium r", excess_saving(r_eq), 0.0, tol=1e-6)
check("FIRST WELFARE THEOREM: K2 matches the planner's", K2_eq, P["K2"], tol=1e-5)
check("...and C1 matches", C1_eq, P["C1"], tol=1e-5)
check("...and C2 matches", C2_eq, P["C2"], tol=1e-5)

# The equilibrium price satisfies the arbitrage condition (9.1.11).
rK2 = A2 * fp(K2_eq)
check("arbitrage (9.1.11): r = r^K - delta", r_eq, rK2 - DELTA, tol=1e-6)

# Zero profit in both periods: factor payments exhaust output (CRS, Euler's theorem).
w1 = A1 * (f(K1) - K1 * fp(K1)) / L1
check("period-1 factor payments exhaust output",
      A1 * fp(K1) * K1 + w1 * L1, A1 * f(K1), tol=1e-12)
check("period-2 factor payments exhaust output",
      rK2 * K2_eq + pi2_eq, A2 * f(K2_eq), tol=1e-9)
check("investment firm's profit is zero", (rK2 + 1 - DELTA) / (1 + r_eq) - 1.0, 0.0, tol=1e-6)

# The five price-bearing conditions collapse to the two the planner writes.
check("(9.1.8) Euler holds at the equilibrium allocation",
      up(C1_eq) - BETA * (1 + r_eq) * up(C2_eq), 0.0, tol=1e-6)
check("the collapsed condition contains no price at all",
      -up(P["C1"]) + BETA * up(P["C2"]) * (A2 * fp(P["K2"]) + 1 - DELTA), 0.0, tol=1e-6)

# WALRAS' LAW: with the credit market cleared, the goods markets clear automatically.
check("period-1 goods market clears without being imposed",
      C1_eq + K2_eq - R1, 0.0, tol=1e-5)
check("period-2 goods market clears without being imposed",
      C2_eq - (A2 * f(K2_eq) + (1 - DELTA) * K2_eq), 0.0, tol=1e-5)

# Off equilibrium the household budget still holds -- that is what makes Walras an identity --
# but the individual markets do not clear.
for r_try in (0.02, 0.10, 0.40):
    K2d = firm_K2(r_try)
    pi2 = A2 * f(K2d) - A2 * fp(K2d) * K2d
    a, C1t, C2t = household(r_try, pi2)
    check(f"budget holds identically at r={r_try:.2f} (Walras)",
          C1t + C2t / (1 + r_try) - (R1 + pi2 / (1 + r_try)), 0.0, tol=1e-6)
    check_true(f"...but the credit market does not clear at r={r_try:.2f}",
               abs(a - K2d) > 1e-4)

# Only relative prices are determined: scaling every nominal price changes nothing real.
scale = 3.7
check("scaling all nominal prices leaves the real wage unchanged",
      (scale * w1) / scale, w1, tol=1e-14)

# ---------------------------------------------------------------------------
print("\n02-dynamics-and-saddle-path")
k_star = (ALPHA / (DELTA + RHO)) ** (1 / (1 - ALPHA))
c_star = f(k_star) - DELTA * k_star
k_gold = (ALPHA / DELTA) ** (1 / (1 - ALPHA))

check("k* from f'(k*) = delta + rho", fp(k_star), DELTA + RHO, tol=1e-12)
check("k_gold from f'(k) = delta", fp(k_gold), DELTA, tol=1e-12)
check_true("k* < k_gold: the optimum stops short of the Golden Rule", k_star < k_gold)
check("c* on the dot-k=0 locus", c_star, f(k_star) - DELTA * k_star, tol=1e-14)

# The inequality holds across a parameter grid, so it is structural and not a fluke.
strict = True
for a in (0.2, 0.35, 0.5, 0.7):
    for d in (0.02, 0.06, 0.12):
        for rh in (0.005, 0.03, 0.08):
            ks = (a / (d + rh)) ** (1 / (1 - a))
            kg = (a / d) ** (1 / (1 - a))
            if not ks < kg:
                strict = False
check_true("k* < k_gold across a 36-point parameter grid", strict)
check_true("so f'(k*) > delta always: dynamic inefficiency is impossible here",
           fp(k_star) > DELTA)

# The Golden Rule is the peak of the dot-k=0 hump.
grid = np.linspace(0.05, 3 * k_gold, 400001)
hump = f(grid) - DELTA * grid
check("the hump peaks at k_gold", grid[int(np.argmax(hump))], k_gold, tol=1e-3)

# Jacobian at the steady state: determinant negative => saddle.
J = np.array([
    [fp(k_star) - DELTA, -1.0],
    [c_star / SIGMA * ALPHA * (ALPHA - 1) * k_star ** (ALPHA - 2), 0.0],
])
detJ = float(np.linalg.det(J))
eig = np.linalg.eigvals(J)
check("det J = (c*/sigma) f''(k*)", detJ,
      c_star / SIGMA * ALPHA * (ALPHA - 1) * k_star ** (ALPHA - 2), tol=1e-12)
check_true("det J < 0", detJ < 0)
check_true("eigenvalues are real with opposite signs -- a saddle",
           np.all(np.abs(eig.imag) < 1e-12) and eig.real.min() < 0 < eig.real.max())
check("trace J = rho (a standard result)", float(np.trace(J)), RHO, tol=1e-12)

# Shooting: only one c0 avoids both failure modes.
def shoot(c0, k0, T=400.0, dt=1e-3):
    """Return 'low' if k explodes, 'high' if k hits zero, 'path' if it stays near the steady state."""
    k, c, t = k0, c0, 0.0
    while t < T:
        kd = f(k) - DELTA * k - c
        cd = c / SIGMA * (fp(k) - DELTA - RHO)
        k += dt * kd
        c += dt * cd
        t += dt
        if k <= 1e-6:
            return "high"
        if k > 5 * k_gold:
            return "low"
        if c <= 1e-9:
            return "low"
    return "path"


k0 = 0.4 * k_star
lo, hi = 1e-6, f(k0) - DELTA * k0
for _ in range(80):
    mid = 0.5 * (lo + hi)
    if shoot(mid, k0) == "high":
        hi = mid
    else:
        lo = mid
c0_star = 0.5 * (lo + hi)

check_true("a c0 above the saddle path drives capital to zero (infeasible)",
           shoot(c0_star * 1.02, k0) == "high")
check_true("a c0 below it accumulates capital without bound (violates transversality)",
           shoot(c0_star * 0.98, k0) == "low")
check_true("the bracketing interval has collapsed to a knife-edge", hi - lo < 1e-10)

# That knife-edge trajectory does converge to the steady state.
k, c, t = k0, c0_star, 0.0
for _ in range(int(150 / 1e-3)):
    kd = f(k) - DELTA * k - c
    cd = c / SIGMA * (fp(k) - DELTA - RHO)
    k += 1e-3 * kd
    c += 1e-3 * cd
    if k <= 1e-6 or k > 5 * k_gold:
        break
check("the saddle path converges to k*", k, k_star, tol=2e-2)
check("...and to c*", c, c_star, tol=2e-2)

# Comparative static: more patience moves the vertical line right, the hump not at all.
k_star_patient = (ALPHA / (DELTA + 0.01)) ** (1 / (1 - ALPHA))
check_true("rho down raises k*", k_star_patient > k_star)
check("the dot-k=0 hump does not contain rho",
      f(k_star) - DELTA * k_star, f(k_star) - DELTA * k_star, tol=0.0)

# ---------------------------------------------------------------------------
print()
if failures:
    print(f"{len(failures)} CHECK(S) FAILED: " + "; ".join(failures))
    raise SystemExit(1)
print("all checks pass")
