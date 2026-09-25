#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical checks for Map/aula-05-trabalho.

Covered:
  01-measurement             discouragement lowers the unemployment rate while the
                             employment-population ratio does not rise; the two-margin identity
  02-static-model            MRS = w against numerical optimisation; log-log makes hours
                             wage-independent at pi=0 and not otherwise; the balanced-growth
                             restriction rules out additive CRRA unless sigma = 1; reservation wage
  03-elasticities-and-ev.    the three elasticities and their ordering; Slutsky; eps_F = 1/eta;
                             Prescott's implied elasticity
  04-dynamic-labour-supply   the relative-hours condition; transitory vs permanent wage changes
  05-search-and-equilibrium  u* = lambda/(lambda+f) against simulation; stability and half-life;
                             the matching function, tightness and the Beveridge curve

Stdlib + numpy only. Run: python Map/aula-05-trabalho/check_labour.py
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


HBAR, THETA = 1.0, 1.5

# ---------------------------------------------------------------------------
print("\n01-measurement")
E, U, N = 150.0, 10.0, 40.0
urate = lambda E, U: U / (E + U)
epop = lambda E, U, N: E / (E + U + N)
u0, e0 = urate(E, U), epop(E, U, N)

# Two unemployed become discouraged: U -> N.
u1, e1 = urate(E, U - 2), epop(E, U - 2, N + 2)
check_true("discouragement lowers the unemployment rate", u1 < u0)
check("the employment-population ratio is untouched by discouragement", e1, e0, tol=1e-12)

# A recession with job loss AND discouragement: both fall together.
u2, e2 = urate(E - 6, U + 4), epop(E - 6, U + 4, N + 2)
check_true("job loss alone raises the unemployment rate", u2 > u0)
check_true("...while the employment-population ratio falls", e2 < e0)
# The diagnostic case: rate falls and epop falls.
u3, e3 = urate(E - 3, U - 5), epop(E - 3, U - 5, N + 8)
check_true("rate down AND epop down is the discouragement signature", u3 < u0 and e3 < e0)

# The exact derivative of the rate with respect to a U -> N transfer.
dU = -1e-6
check("du/dU == E/(E+U)^2", (urate(E, U + dU) - urate(E, U)) / dU, E / (E + U) ** 2, tol=1e-6)

# Two-margin identity.
H_per_E, Emp = 1750.0, 150.0
check("H = (H/E) * E", H_per_E * Emp, 262500.0)

# ---------------------------------------------------------------------------
print("\n02-static-model")
def hours_loglog(w, pi=0.0, theta=THETA, hbar=HBAR):
    leisure = theta / (1 + theta) * (w * hbar + pi) / w
    return max(hbar - leisure, 0.0)


def solve_static_numeric(w, pi=0.0, theta=THETA, hbar=HBAR):
    """Maximise ln c + theta ln l over l, by bisection on the first-order condition."""
    # FOC: theta/l = w * (1/c) with c = w(hbar - l) + pi  =>  theta*c - w*l = 0
    g = lambda l: theta * (w * (hbar - l) + pi) - w * l
    lo, hi = 1e-12, hbar - 1e-12
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if g(mid) > 0:
            lo = mid
        else:
            hi = mid
    return hbar - 0.5 * (lo + hi)


for w in (0.5, 1.0, 2.0, 8.0):
    for pi in (0.0, 0.3):
        check(f"closed form == numerical optimum (w={w}, pi={pi})",
              hours_loglog(w, pi), solve_static_numeric(w, pi), tol=1e-9)

# MRS = w at the optimum.
w, pi = 2.0, 0.3
h = hours_loglog(w, pi)
l = HBAR - h
c = w * h + pi
check("MRS = u_l/u_c = theta*c/l equals w at the optimum", THETA * c / l, w, tol=1e-9)

# Log-log with pi = 0: hours do not depend on the wage at all.
base = hours_loglog(1.0, 0.0)
for w in (0.2, 1.0, 5.0, 50.0):
    check(f"pi=0: hours independent of w (w={w})", hours_loglog(w, 0.0), base, tol=1e-12)
check("hours = hbar/(1+theta)", base, HBAR / (1 + THETA), tol=1e-12)

# With pi > 0 the cancellation breaks and hours RISE with w.
check_true("pi>0: hours rise with the wage", hours_loglog(3.0, 0.3) > hours_loglog(1.0, 0.3))
# A pure income effect: pi up lowers hours at a fixed wage.
check_true("pi up lowers hours (the clean test)", hours_loglog(2.0, 0.6) < hours_loglog(2.0, 0.2))

# Balanced growth: additive CRRA in both arguments needs sigma = 1.
def mrs_additive(c, l, sigma, gamma):
    return (l ** (-gamma)) / (c ** (-sigma))


c0, l0, gam = 1.0, 0.4, 2.0
for sig in (0.5, 1.0, 2.0):
    mu = 3.0                       # scale both c and w by mu, as balanced growth requires
    lhs = mrs_additive(mu * c0, l0, sig, gam)
    rhs = mu * mrs_additive(c0, l0, sig, gam)
    ok = abs(lhs - rhs) < 1e-12
    check_true(f"additive CRRA is balanced-growth consistent at sigma={sig}: {ok}",
               ok == (abs(sig - 1) < 1e-12))

# Reservation wage.
def w_reservation(pi, theta=THETA, hbar=HBAR):
    """u_l/u_c evaluated at the corner (c=pi, l=hbar)."""
    return theta * pi / hbar


wr = w_reservation(0.3)
check("reservation wage = theta*pi/hbar", wr, THETA * 0.3 / HBAR)
check_true("below the reservation wage the household does not work",
           hours_loglog(wr * 0.9, 0.3) <= 1e-12)
check_true("above it the household works", hours_loglog(wr * 1.1, 0.3) > 0)
check_true("higher non-wage income raises the reservation wage",
           w_reservation(0.6) > w_reservation(0.3))

# ---------------------------------------------------------------------------
print("\n03-elasticities-and-evidence")
# Marshallian elasticity from the log-log closed form.
def eps_marshall(w, pi, theta=THETA, hbar=HBAR):
    d = 1e-6
    h1, h2 = hours_loglog(w * (1 - d), pi), hours_loglog(w * (1 + d), pi)
    return (math.log(h2) - math.log(h1)) / (2 * d)


check("Marshallian elasticity is exactly zero at pi=0", eps_marshall(2.0, 0.0), 0.0, tol=1e-6)
check_true("Marshallian elasticity is positive at pi>0", eps_marshall(2.0, 0.3) > 0)

# Hicksian: compensate pi so utility is unchanged.
def utility(w, pi, theta=THETA, hbar=HBAR):
    h = hours_loglog(w, pi)
    return math.log(w * h + pi) + theta * math.log(hbar - h)


def eps_hicks(w, pi, theta=THETA, hbar=HBAR):
    u0 = utility(w, pi)
    w2 = w * 1.000001
    lo, hi = -0.999 * w2 * hbar, 10.0
    for _ in range(200):                      # find the pi that restores utility at w2
        mid = 0.5 * (lo + hi)
        if utility(w2, mid) < u0:
            lo = mid
        else:
            hi = mid
    pi2 = 0.5 * (lo + hi)
    return (math.log(hours_loglog(w2, pi2)) - math.log(hours_loglog(w, pi))) / math.log(w2 / w)


eh = eps_hicks(2.0, 0.0)
check_true("Hicksian elasticity is strictly positive even when Marshallian is zero", eh > 0.1)
check_true("ordering: Hicksian >= Marshallian at pi=0", eh >= eps_marshall(2.0, 0.0) - 1e-9)
check("at pi=0 the compensated elasticity equals theta/(1+theta)",
      eh, THETA / (1 + THETA), tol=1e-3)

# Frisch: eps_F = 1/eta for v(h) = chi h^(1+eta)/(1+eta).
def frisch(eta, mu=1.0, w=1.0, chi=1.0):
    h = (mu * w / chi) ** (1 / eta)
    d = 1e-6
    h2 = (mu * w * (1 + d) / chi) ** (1 / eta)
    return (math.log(h2) - math.log(h)) / math.log(1 + d)


for eta in (0.5, 1.0, 2.0, 5.0):
    check(f"Frisch elasticity == 1/eta (eta={eta})", frisch(eta), 1 / eta, tol=1e-5)

# Prescott: the elasticity implied by the Europe-US hours gap and tax wedges.
tau_us, tau_eu, hours_ratio = 0.40, 0.60, 1 / 1.5
implied_eis = math.log(hours_ratio) / math.log((1 - tau_eu) / (1 - tau_us))
check("Prescott's implied Frisch elasticity", implied_eis, 1.0, tol=0.01)
check_true("...far above the 0.1-0.3 found for prime-age men on the intensive margin",
           implied_eis > 3 * 0.3)
# Sensitivity: a smaller assumed tax gap requires a LARGER elasticity.
implied_small_gap = math.log(hours_ratio) / math.log((1 - 0.50) / (1 - 0.40))
check_true("a smaller tax gap demands a larger elasticity", implied_small_gap > implied_eis)

# ---------------------------------------------------------------------------
print("\n04-dynamic-labour-supply")
BETA, R, ETA = 0.96, 0.04, 1.0


def rel_hours(w1, w2, beta=BETA, r=R, eta=ETA):
    return (beta * (1 + r) * w1 / w2) ** (1 / eta)


check("relative hours closed form at w1=w2", rel_hours(1, 1), (BETA * (1 + R)) ** (1 / ETA))
check("d ln(h1/h2) / d ln(w1/w2) == 1/eta",
      (math.log(rel_hours(1.01, 1)) - math.log(rel_hours(1, 1))) / math.log(1.01),
      1 / ETA, tol=1e-6)
check_true("a higher interest rate shifts work toward the present",
           rel_hours(1, 1, r=0.08) > rel_hours(1, 1, r=0.04))
check_true("more impatience shifts work toward the FUTURE (future disutility is discounted)",
           rel_hours(1, 1, beta=0.90) < rel_hours(1, 1, beta=0.99))
check("beta and (1+r) enter only through their product",
      rel_hours(1, 1, beta=0.96, r=0.04),
      rel_hours(1, 1, beta=0.96 * 1.04 / 1.10, r=0.10), tol=1e-12)
check("beta(1+r)=1 equalises hours across periods", rel_hours(1, 1, beta=1 / 1.04), 1.0, tol=1e-12)

# Transitory vs permanent: only the RELATIVE wage moves relative hours.
check_true("a transitory wage rise raises relative hours a lot",
           rel_hours(1.10, 1.00) > rel_hours(1.00, 1.00) * 1.09)
check("a permanent wage rise leaves relative hours unchanged",
      rel_hours(1.10, 1.10), rel_hours(1.00, 1.00), tol=1e-12)

# ---------------------------------------------------------------------------
print("\n05-search-and-equilibrium")
def u_star(lam, f):
    return lam / (lam + f)


def simulate_u(lam, f, u0, T):
    u = u0
    for _ in range(T):
        u = u + lam * (1 - u) - f * u
    return u


LAM, F = 0.034, 0.43
check("u* = lambda/(lambda+f)", u_star(LAM, F), 0.034 / 0.464, tol=1e-9)
check("...as a percentage", u_star(LAM, F) * 100, 7.328, tol=1e-3)
for u0 in (0.0, 0.02, 0.30, 0.95):
    check(f"simulation from u0={u0} converges to u*", simulate_u(LAM, F, u0, 500),
          u_star(LAM, F), tol=1e-9)
check_true("the map is a contraction: |1-(lambda+f)| < 1", abs(1 - (LAM + F)) < 1)
check("half-life of a deviation, months", math.log(2) / (LAM + F), 1.494, tol=1e-3)

# Only the ratio matters.
check("tripling both flows leaves u* unchanged", u_star(3 * LAM, 3 * F), u_star(LAM, F), tol=1e-12)
check_true("...but cuts spell duration to a third",
           abs((1 / (3 * F)) - (1 / F) / 3) < 1e-12)

# Same rate, different experience: the US-Europe comparison of note 05 sec. 5.2.
us = (0.035, 0.40)
eu = (0.009, 0.10)
check("US-style u*", u_star(*us) * 100, 8.046, tol=1e-3)
check("Europe-style u*", u_star(*eu) * 100, 8.257, tol=1e-3)
check_true("the two rates are within half a point of each other",
           abs(u_star(*us) - u_star(*eu)) < 0.005)
check("US-style duration, months", 1 / us[1], 2.5)
check("Europe-style duration, months", 1 / eu[1], 10.0)
check_true("Europe-style spells are four times as long", (1 / eu[1]) / (1 / us[1]) == 4.0)

# unemployment = separation rate x duration, approximately.
check("u* ~= lambda * duration for small lambda/f", LAM * (1 / F), u_star(LAM, F), tol=6e-3)

# Matching function, tightness and the Beveridge curve.
XI, AM = 0.5, 0.6


def finding(theta, Am=AM, xi=XI):
    return Am * theta ** (1 - xi)


def filling(theta, Am=AM, xi=XI):
    return Am * theta ** (-xi)


check_true("f rises with tightness", finding(2.0) > finding(0.5))
check_true("q falls with tightness", filling(2.0) < filling(0.5))
check("f * U == q * V == M at theta = V/U", finding(2.0) * 1.0, filling(2.0) * 2.0, tol=1e-12)

# The Beveridge curve: solve u given v, then check it slopes down.
def u_given_v(v, lam=LAM, Am=AM, xi=XI):
    lo, hi = 1e-9, 0.999
    for _ in range(300):
        u = 0.5 * (lo + hi)
        f = finding(v / u, Am, xi)
        if lam * (1 - u) - f * u > 0:
            lo = u
        else:
            hi = u
    return 0.5 * (lo + hi)


vs = [0.01, 0.02, 0.04, 0.08]
us_curve = [u_given_v(v) for v in vs]
check_true("the Beveridge curve slopes down", all(np.diff(us_curve) < 0))
# An outward shift needs worse matching or more separations.
check_true("lower matching efficiency shifts the curve out",
           u_given_v(0.04, Am=0.4) > u_given_v(0.04, Am=0.6))
check_true("a higher separation rate also shifts it out",
           u_given_v(0.04, lam=0.05) > u_given_v(0.04, lam=0.034))

# Unemployment insurance: a higher reservation wage lowers f and raises u*.
def f_from_reservation(wr, mean=1.0, sd=0.3, draws=400_000, seed=7):
    rng = np.random.default_rng(seed)
    offers = rng.normal(mean, sd, draws)
    return float((offers >= wr).mean())


f_low, f_high = f_from_reservation(0.8), f_from_reservation(1.0)
check_true("a higher reservation wage lowers the job-finding rate", f_high < f_low)
check_true("...and therefore raises steady-state unemployment",
           u_star(LAM, f_high) > u_star(LAM, f_low))
check_true("...and lengthens spells", 1 / f_high > 1 / f_low)

# ---------------------------------------------------------------------------
print()
if failures:
    print(f"{len(failures)} CHECK(S) FAILED: " + "; ".join(failures))
    raise SystemExit(1)
print("all checks pass")
