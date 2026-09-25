#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical checks for Map/aula-02-solow-mecanica.

Each closed form in the notes is verified against an independent path: a simulated
trajectory, a numerical root, or a direct integral. Exits non-zero if anything is mistyped.

Covered:
  01-growth-facts            Kaldor fact 4 derived from facts 2 and 3; the 1.5% / 27x check
  02-ingredients             Cobb-Douglas satisfies 4.1-4.4; Euler exhaustion; alpha is the
                             capital share
  03-fundamental-equation    (4.2.2) exact vs approximate; the n/(1+n) error; continuous time
  04-steady-state-and-...    closed form vs simulation; existence/uniqueness; AK counterexample;
                             global stability; |G'(k_ss)| < 1; lambda = (1-alpha)(delta+n)
  05-comparative-statics     elasticities; the transition integral identity; the consumption
                             criterion f'(k_ss) vs delta+n

Stdlib + numpy only. Run: python Map/aula-02-solow-mecanica/check_solow.py
"""
from __future__ import annotations

import math

import numpy as np

failures: list[str] = []


def check(name, got, want, tol=1e-8):
    ok = abs(float(got) - float(want)) <= tol
    print(f"  {'ok  ' if ok else 'FAIL'}  {name:<54} {float(got):+.6f}  (want {float(want):+.6f})")
    if not ok:
        failures.append(name)


def check_true(name, cond):
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}")
    if not cond:
        failures.append(name)


# ---------------------------------------------------------------------------
# The model, written once. f(k) = k**alpha.
# ---------------------------------------------------------------------------
ALPHA, S, DELTA, N = 1 / 3, 0.20, 0.05, 0.01


def f(k, alpha=ALPHA):
    return k ** alpha


def fprime(k, alpha=ALPHA):
    return alpha * k ** (alpha - 1)


def k_ss(s=S, delta=DELTA, n=N, alpha=ALPHA):
    """Closed form of note 04 sec. 4.1."""
    return (s / (delta + n)) ** (1 / (1 - alpha))


def step_exact(k, s=S, delta=DELTA, n=N, alpha=ALPHA):
    """Exact discrete law, note 03 eq. (4.2.2)."""
    return ((1 - delta) * k + s * f(k, alpha)) / (1 + n)


def step_approx(k, s=S, delta=DELTA, n=N, alpha=ALPHA):
    """The textbook approximation: k + s f(k) - (delta+n) k."""
    return k + s * f(k, alpha) - (delta + n) * k


def simulate(k0, T, stepper=step_exact, **kw):
    k = np.empty(T + 1)
    k[0] = k0
    for t in range(T):
        k[t + 1] = stepper(k[t], **kw)
    return k


# ---------------------------------------------------------------------------
print("\n01-growth-facts")
# Fact 4 from facts 2 and 3: r = (1 - labour share) / (K/Y).
labour_share, KY = 0.65, 3.2
r_gross = (1 - labour_share) / KY
check("gross return on capital = (1-labour share)/(K/Y)", r_gross, 0.109375)
check("net return after delta = 0.05", r_gross - 0.05, 0.059375)

# 1.5% for 216 years, against the book's "about 27 times higher".
check("1.5% compounded 1800-2016", 1.015 ** 216, 24.93, tol=0.02)
check("rate implied by a factor of 27", math.log(27) / 216, 0.015258, tol=1e-6)
check_true("the two statements agree to the book's rounding",
           abs(1.015 ** 216 - 27) / 27 < 0.08)

# ---------------------------------------------------------------------------
print("\n02-ingredients -- Cobb-Douglas and Euler")
K, L, a = 7.3, 4.1, ALPHA
F = lambda K, L: K ** a * L ** (1 - a)
lam = 2.7
check("CRS: F(lam K, lam L) == lam F(K,L)", F(lam * K, lam * L), lam * F(K, L), tol=1e-9)

h = 1e-6
FK = (F(K + h, L) - F(K - h, L)) / (2 * h)
FL = (F(K, L + h) - F(K, L - h)) / (2 * h)
check("F_K == alpha Y/K", FK, a * F(K, L) / K, tol=1e-6)
check("F_L == (1-alpha) Y/L", FL, (1 - a) * F(K, L) / L, tol=1e-6)
check("Euler exhaustion: F_K K + F_L L == Y", FK * K + FL * L, F(K, L), tol=1e-5)
check("capital income share == alpha", FK * K / F(K, L), a, tol=1e-6)

FKK = (F(K + h, L) - 2 * F(K, L) + F(K - h, L)) / h ** 2
check_true("F_KK < 0 (diminishing returns)", FKK < 0)
check_true("Inada at zero: f'(k) -> infinity", fprime(1e-10) > 1e5)
check_true("Inada at infinity: f'(k) -> 0", fprime(1e10) < 1e-5)

# ---------------------------------------------------------------------------
print("\n03-fundamental-equation")
k0 = 1.7
dk_exact = step_exact(k0) - k0
dk_approx = step_approx(k0) - k0
raw = S * f(k0) - (DELTA + N) * k0
check("exact change == [s f(k) - (delta+n)k] / (1+n)", dk_exact, raw / (1 + N))
check("approximate change == s f(k) - (delta+n)k", dk_approx, raw)
check("error == n/(1+n) times the raw change", dk_approx - dk_exact, N / (1 + N) * raw)
check_true("the approximation overstates movement by about 1% at n=0.01",
           abs((dk_approx - dk_exact) / raw - 0.0099) < 1e-3)

# Dividing by 1+n cannot move the zero: both laws share the steady state.
kss = k_ss()
check("exact law is stationary at the closed-form k_ss", step_exact(kss) - kss, 0.0, tol=1e-12)
check("approximate law is stationary at the same k_ss", step_approx(kss) - kss, 0.0, tol=1e-12)

# Continuous time via the quotient rule, checked against a fine Euler integration.
def kdot(k, s=S, delta=DELTA, n=N):
    return s * f(k) - (delta + n) * k


dt = 1e-4
k = k0
for _ in range(int(1 / dt)):
    k += dt * kdot(k)
check("one year of continuous time ~= one approximate discrete step",
      k, step_approx(k0), tol=2e-3)

# Growth of output is alpha times growth of capital.
check("y-growth == alpha * k-growth", ALPHA * kdot(k0) / k0,
      (f(k0 + 1e-7) - f(k0)) / 1e-7 * kdot(k0) / f(k0), tol=1e-5)

# ---------------------------------------------------------------------------
print("\n04-steady-state-and-stability")
check("closed form k_ss", kss, (S / (DELTA + N)) ** (1 / (1 - ALPHA)))
check("steady-state condition s f(k_ss) == (delta+n) k_ss",
      S * f(kss), (DELTA + N) * kss)
check("y_ss", f(kss), (S / (DELTA + N)) ** (ALPHA / (1 - ALPHA)))
check("c_ss", (1 - S) * f(kss), (1 - S) * (S / (DELTA + N)) ** (ALPHA / (1 - ALPHA)))

# Simulation from far away must land on the closed form.
for k_start in (0.01, 0.5, kss, 5.0, 50.0):
    path = simulate(k_start, 4000)
    check(f"simulation from k0={k_start:<5} converges to k_ss", path[-1], kss, tol=1e-6)

# Monotone, never overshooting.
path = simulate(0.05, 800)
d = np.diff(path)
check_true("path from below is monotonically increasing (no overshoot)", np.all(d > -1e-15))
path_hi = simulate(40.0, 800)
check_true("path from above is monotonically decreasing", np.all(np.diff(path_hi) < 1e-15))

# Existence and uniqueness: exactly one positive root of phi.
grid = np.logspace(-6, 6, 200001)
phi = S * f(grid) - (DELTA + N) * grid
sign_changes = np.sum(np.diff(np.sign(phi)) != 0)
check_true(f"phi has exactly one sign change on (0, inf) (found {sign_changes})",
           sign_changes == 1)
check_true("phi > 0 for small k (first Inada condition)", phi[0] > 0)
check_true("phi < 0 for large k (second Inada condition)", phi[-1] < 0)

# f(k)/k strictly decreasing -- the uniqueness argument.
ratio = f(grid) / grid
check_true("f(k)/k is strictly decreasing", np.all(np.diff(ratio) < 0))

# AK counterexample: drop diminishing returns and the interior steady state disappears.
A_ak = 0.40
phi_ak = lambda k: S * A_ak * k - (DELTA + N) * k
check_true("AK with sA > delta+n: phi > 0 everywhere, no interior steady state",
           all(phi_ak(k) > 0 for k in (1e-6, 1.0, 1e6)))
check("AK permanent growth rate = sA - delta - n", S * A_ak - DELTA - N, 0.02)

# Discrete-time stability: G' positive and below one.
def Gprime(k, s=S, delta=DELTA, n=N, alpha=ALPHA):
    return ((1 - delta) + s * fprime(k, alpha)) / (1 + n)


check("G'(k_ss) closed form", Gprime(kss),
      (1 - DELTA + ALPHA * (DELTA + N)) / (1 + N), tol=1e-9)
check_true("0 < G'(k_ss) < 1, so convergence is monotone", 0 < Gprime(kss) < 1)

grid_ok = True
for s_ in (0.05, 0.2, 0.5, 0.9):
    for n_ in (0.0, 0.01, 0.04):
        for d_ in (0.02, 0.05, 0.15):
            for a_ in (0.2, 1 / 3, 0.5, 0.7):
                kk = k_ss(s_, d_, n_, a_)
                if not (0 < Gprime(kk, s_, d_, n_, a_) < 1):
                    grid_ok = False
check_true("0 < G'(k_ss) < 1 across a 144-point parameter grid", grid_ok)

# Local convergence rate.
lam = (1 - ALPHA) * (DELTA + N)
num = -(S * fprime(kss) - (DELTA + N))      # -phi'(k_ss)
check("lambda = (1-alpha)(delta+n) equals -phi'(k_ss)", num, lam, tol=1e-9)
check("lambda at the baseline calibration", lam, 0.04)
check("half-life of the gap, years", math.log(2) / lam, 17.33, tol=1e-2)

# ---------------------------------------------------------------------------
print("\n05-comparative-statics")
check("d ln k_ss / d ln s == 1/(1-alpha)",
      (math.log(k_ss(S * 1.0001)) - math.log(k_ss(S))) / math.log(1.0001),
      1 / (1 - ALPHA), tol=1e-3)
check("d ln y_ss / d ln s == alpha/(1-alpha)",
      (math.log(f(k_ss(S * 1.0001))) - math.log(f(k_ss(S)))) / math.log(1.0001),
      ALPHA / (1 - ALPHA), tol=1e-3)
check_true("n and delta enter identically",
           abs(k_ss(S, DELTA + 0.01, N) - k_ss(S, DELTA, N + 0.01)) < 1e-12)

# The saving-rate elasticity is too small to explain observed income gaps.
check("a 4x saving-rate gap buys only this income ratio",
      4 ** (ALPHA / (1 - ALPHA)), 2.0)
check_true("observed 30x income gaps are far outside the model's reach",
           4 ** (ALPHA / (1 - ALPHA)) < 30 / 10)

# The transition: integral of the growth rate equals the log level gain.
s0, s1 = 0.20, 0.25
k_start, k_end = k_ss(s0), k_ss(s1)
level_gain = math.log(f(k_end)) - math.log(f(k_start))
check("log level gain == alpha/(1-alpha) * ln(s1/s0)",
      level_gain, ALPHA / (1 - ALPHA) * math.log(s1 / s0))
check("level gain in per cent", math.expm1(level_gain) * 100, 11.80, tol=0.05)

# Integrate the growth rate of y along the continuous-time path from k_start under s1.
dt, k, integral, t = 1e-3, k_start, 0.0, 0.0
while t < 4000 and k < k_end * (1 - 1e-12):
    g_y = ALPHA * (s1 * f(k) / k - (DELTA + N))
    integral += g_y * dt
    k += dt * (s1 * f(k) - (DELTA + N) * k)
    t += dt
check("integral of the growth spike == the level gain", integral, level_gain, tol=1e-4)

# Impact effects.
check("k does not jump on impact", k_start, k_ss(s0))
check("consumption falls on impact by (s1-s0) f(k)", (s1 - s0) * f(k_start), 0.05 * f(k_start))
check_true("kdot jumps up on impact", s1 * f(k_start) - (DELTA + N) * k_start > 0)

# The consumption criterion.
def c_ss(s):
    return (1 - s) * f(k_ss(s))


s_gold = (ALPHA)  # Golden Rule saving rate for Cobb-Douglas is alpha
check("f'(k_ss) == delta+n exactly at s = alpha", fprime(k_ss(s_gold)), DELTA + N, tol=1e-12)
check_true("dc_ss/ds > 0 when f'(k_ss) > delta+n", c_ss(0.20 + 1e-5) > c_ss(0.20))
check_true("dc_ss/ds < 0 when f'(k_ss) < delta+n", c_ss(0.50 + 1e-5) < c_ss(0.50))
check_true("c_ss is maximised at s = alpha",
           all(c_ss(s_gold) >= c_ss(x) - 1e-12 for x in np.linspace(0.05, 0.95, 400)))

# ---------------------------------------------------------------------------
print()
if failures:
    print(f"{len(failures)} CHECK(S) FAILED: " + "; ".join(failures))
    raise SystemExit(1)
print("all checks pass")
