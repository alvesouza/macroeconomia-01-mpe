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
                             Prescott's implied elasticity (Kurlat Ex. 7.5)
  all notes                  the intermediate steps the notes spell out
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


# Expanded steps (note 01): the quotient rule, and the log form of the two-margin identity.
check("quotient rule: [(E+U) - U]/(E+U)^2 == E/(E+U)^2",
      ((E + U) - U) / (E + U) ** 2, E / (E + U) ** 2, tol=1e-15)
H0, E0, H1, E1 = 262500.0, 150.0, 255000.0, 146.0
check("ln-change of H == ln-change of H/E + ln-change of E",
      math.log(H1 / H0), math.log((H1 / E1) / (H0 / E0)) + math.log(E1 / E0), tol=1e-12)

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


# Expanded steps (note 02).
w, pi = 2.0, 0.3
l = THETA / (1 + THETA) * (w * HBAR + pi) / w
c = w * l / THETA                                  # MRS = w: theta c / l = w
check("c = w l/theta satisfies c + w l = w hbar + pi", c + w * l, w * HBAR + pi, tol=1e-12)
check("h = hbar/(1+theta) - theta/(1+theta) * pi/w",
      hours_loglog(w, pi), HBAR / (1 + THETA) - THETA / (1 + THETA) * pi / w, tol=1e-12)
d = 1e-6
check("dh/dw = theta pi / ((1+theta) w^2)",
      (hours_loglog(w + d, pi) - hours_loglog(w - d, pi)) / (2 * d),
      THETA * pi / ((1 + THETA) * w ** 2), tol=1e-7)
check("additive CRRA: MRS(mu c, l) / MRS(c, l) == mu^sigma",
      mrs_additive(3.0 * c0, l0, 2.0, gam) / mrs_additive(c0, l0, 2.0, gam), 3.0 ** 2.0, tol=1e-9)
for wt in (0.3, 0.9):                              # w^r = 0.45 at pi = 0.3
    util = lambda h, wt=wt: math.log(wt * h + 0.3) + THETA * math.log(HBAR - h)
    slope0 = (util(1e-8) - util(0.0)) / 1e-8
    check("dU/dh at the corner == w/pi - theta/hbar (w=%g)" % wt, slope0,
          wt / 0.3 - THETA / HBAR, tol=1e-5)
    check_true(f"...positive iff w > w^r (w={wt})", (slope0 > 0) == (wt > w_reservation(0.3)))

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

# Expanded steps (note 03): Slutsky for labour, eps_M = eps_H + w dh/dpi.
for pi in (0.0, 0.3):
    dh_dpi = (hours_loglog(2.0, pi + 1e-6) - hours_loglog(2.0, pi)) / 1e-6
    check(f"dh/dpi == -theta/((1+theta) w) (pi={pi})", dh_dpi, -THETA / ((1 + THETA) * 2.0), tol=1e-6)
    check(f"Slutsky: eps_M == eps_H + w dh/dpi (pi={pi})",
          eps_marshall(2.0, pi), eps_hicks(2.0, pi) + 2.0 * dh_dpi, tol=2e-3)
h = hours_loglog(2.0, 0.3)
eps_pi = (math.log(hours_loglog(2.0, 0.3 * (1 + 1e-6))) - math.log(h)) / math.log(1 + 1e-6)
check("income term: w dh/dpi == (w h / pi) eps_pi", 2.0 * dh_dpi, 2.0 * h / 0.3 * eps_pi, tol=1e-5)
check_true("...and NOT (w h / c) eps_pi", abs(2.0 * dh_dpi - 2.0 * h / (2.0 * h + 0.3) * eps_pi) > 0.1)
# Frisch in the log-log model: mu fixed, theta/l = mu w, so l = theta/(mu w) and eps_F = l/h.
for pi in (0.0, 0.3):
    h = hours_loglog(2.0, pi)
    mu = 1 / (2.0 * h + pi)
    hF = lambda ww, mu=mu: HBAR - THETA / (mu * ww)
    eF = (math.log(hF(2.0 * (1 + 1e-6))) - math.log(hF(2.0 * (1 - 1e-6)))) / (2e-6)
    check(f"log-log Frisch elasticity == l/h (pi={pi})", eF, (HBAR - h) / h, tol=1e-6)
    check_true(f"ordering eps_F >= eps_H >= eps_M (pi={pi})",
               eF >= eps_hicks(2.0, pi) >= eps_marshall(2.0, pi) - 1e-9)
check("at pi=0 the Frisch elasticity is theta", (HBAR - hours_loglog(2.0, 0)) / hours_loglog(2.0, 0),
      THETA, tol=1e-12)
# eps_F = 1/eta: ln h = (ln mu + ln w - ln chi)/eta, differentiate in ln w.
check("ln h = (ln mu + ln w - ln chi)/eta", math.log((2.0 * 1.3 / 0.7) ** (1 / 2.0)),
      (math.log(2.0) + math.log(1.3) - math.log(0.7)) / 2.0, tol=1e-12)

# Prescott, Kurlat Ex. 7.5: u = ln c + alpha ln l, c = w(1-tau)(1-l) + T, hbar = 1.
ALPHA_P = 1.54


def leisure_prescott(tau, T, alpha=ALPHA_P, w=1.0):
    """l = alpha/(1+alpha) * [1 + T/(w(1-tau))], from alpha c = w(1-tau) l and the budget."""
    return alpha / (1 + alpha) * (1 + T / (w * (1 - tau)))


def leisure_balanced(tau, alpha=ALPHA_P):
    """Balanced budget T = tau w (1-l): l = alpha / (1 + alpha - tau)."""
    return alpha / (1 + alpha - tau)


for tau in (0.34, 0.53):
    lfix = 0.5
    for _ in range(2000):                     # the fixed point l = l(tau, T(l))
        lfix = leisure_prescott(tau, tau * (1 - lfix))
    check(f"balanced-budget leisure alpha/(1+alpha-tau) (tau={tau})", lfix, leisure_balanced(tau),
          tol=1e-10)
    check(f"(1+alpha)(1-tau) + alpha tau == 1 + alpha - tau (tau={tau})",
          (1 + ALPHA_P) * (1 - tau) + ALPHA_P * tau, 1 + ALPHA_P - tau, tol=1e-12)
check("US hours 1 - l = 0.66/2.20 = 0.300", 1 - leisure_balanced(0.34), 0.3, tol=1e-12)
check("Europe hours 1 - l = 0.47/2.01", 1 - leisure_balanced(0.53), 0.47 / 2.01, tol=1e-12)
check("with Kurlat's rounded T: US leisure", leisure_prescott(0.34, 0.102), 0.700000, tol=1e-6)
check("with Kurlat's rounded T: Europe leisure", leisure_prescott(0.53, 0.124), 0.766259, tol=1e-6)
check("T = 0: leisure alpha/(1+alpha) whatever tau", leisure_prescott(0.53, 0.0),
      leisure_prescott(0.34, 0.0), tol=1e-15)
l_us = leisure_balanced(0.34)
c_us = 0.66 * (1 - l_us) + 0.34 * (1 - l_us)
check("FOC alpha c = w(1-tau) l holds at the US allocation", ALPHA_P * c_us, 0.66 * l_us, tol=1e-12)
h_c = lambda om: 1 - ALPHA_P * c_us / om                # c held fixed
implied_eis = (math.log(h_c(0.66 * (1 + 1e-6))) - math.log(h_c(0.66 * (1 - 1e-6)))) / 2e-6
check("Prescott's Frisch elasticity (c fixed) == l/(1-l) = 7/3", implied_eis, 7 / 3, tol=1e-6)
check_true("...above the 0.4-1 range Kurlat quotes and far above 0.1-0.3", implied_eis > 2 * 1.0)
# The eta form with full rebate (c = w h): chi h^eta = (1-tau) w / c  =>  chi h^(1+eta) = 1 - tau.
for eta in (0.5, 1.0, 3.0):
    def h_eta(tau, eta=eta, w=1.0, chi=1.0):
        lo, hi = 1e-9, 10.0
        for _ in range(200):                  # bisection on the first-order condition
            m = 0.5 * (lo + hi)
            c_m = (1 - tau) * w * m + tau * w * m
            if chi * m ** eta - (1 - tau) * w / c_m < 0:
                lo = m
            else:
                hi = m
        return 0.5 * (lo + hi)
    el = (math.log(h_eta(0.4 + 1e-5)) - math.log(h_eta(0.4 - 1e-5))) / \
         (math.log(0.6 - 1e-5) - math.log(0.6 + 1e-5))
    check(f"rebated tax: d ln h / d ln(1-tau) == 1/(1+eta) (eta={eta})", el, 1 / (1 + eta), tol=1e-5)
check_true("...so 0.40 vs 0.60 taxes cannot give a 1.5 hours ratio at any finite eta",
           all((0.4 / 0.6) ** (1 / (1 + e)) > 1 / 1.5 for e in (0.01, 0.1, 1.0)))

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


# Expanded steps (note 04).
check("exact d ln(h1/h2)/dr == 1/(eta(1+r))",
      (math.log(rel_hours(1, 1, r=R + 1e-6)) - math.log(rel_hours(1, 1, r=R - 1e-6))) / 2e-6,
      1 / (ETA * (1 + R)), tol=1e-6)
rho = 1 / BETA - 1
check("ln beta + ln(1+r) ~= r - rho to first order", math.log(BETA) + math.log(1 + R), R - rho,
      tol=1e-4)


def two_period(w1, w2, eta=ETA, chi=1.0, r=R, beta=BETA, pi=0.0):
    """Hours (h1, h2) of ln c - chi h^(1+eta)/(1+eta) over two periods, bisection on mu."""
    def excess(mu):
        c1, c2 = 1 / mu, beta * (1 + r) / mu
        h1 = (mu * w1 / chi) ** (1 / eta)
        h2 = (mu * w2 / (beta * (1 + r) * chi)) ** (1 / eta)
        return w1 * h1 + w2 * h2 / (1 + r) + pi - c1 - c2 / (1 + r), h1, h2
    lo, hi = 1e-6, 1e6
    for _ in range(300):
        m = math.sqrt(lo * hi)
        lo, hi = (lo, m) if excess(m)[0] > 0 else (m, hi)
    return excess(math.sqrt(lo * hi))[1:]


for eta in (0.5, 1.0, 3.0):
    b0, t1, p1 = two_period(1, 1, eta=eta), two_period(1.1, 1, eta=eta), two_period(1.1, 1.1, eta=eta)
    check(f"permanent +10%: h1 unchanged with ln c and pi=0 (eta={eta})", p1[0], b0[0], tol=1e-9)
    check(f"transitory +10%: h1/h2 moves by 1.1^(1/eta) (eta={eta})",
          (t1[0] / t1[1]) / (b0[0] / b0[1]), 1.1 ** (1 / eta), tol=1e-9)
    check_true(f"transitory: h1 up and h2 down (eta={eta})", t1[0] > b0[0] and t1[1] < b0[1])

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


# Expanded steps (note 05).
x0 = 0.05
check("deviation after one period == (1-lambda-f) x0",
      simulate_u(LAM, F, u_star(LAM, F) + x0, 1) - u_star(LAM, F), (1 - LAM - F) * x0, tol=1e-15)
exact_half = math.log(2) / -math.log(1 - (LAM + F))
check("exact discrete half-life, months", exact_half, 1.1115, tol=1e-4)
check("(1-lambda-f)^n == 1/2 at the exact half-life", (1 - LAM - F) ** exact_half, 0.5, tol=1e-12)
check_true("ln2/(lambda+f) overstates it because lambda+f is not small",
           math.log(2) / (LAM + F) > exact_half)
check("mean spell sum_k k (1-f)^(k-1) f == 1/f",
      sum(k * (1 - F) ** (k - 1) * F for k in range(1, 5000)), 1 / F, tol=1e-9)
U_, V_ = 0.07, 0.035
M_ = AM * U_ ** XI * V_ ** (1 - XI)
check("M/U == A_m theta^(1-xi)", M_ / U_, finding(V_ / U_), tol=1e-15)
check("M/V == A_m theta^(-xi)", M_ / V_, filling(V_ / U_), tol=1e-15)


def v_closed(u, lam=LAM, Am=AM, xi=XI):
    return (lam * (1 - u) / (Am * u ** xi)) ** (1 / (1 - xi))


for v in vs:
    check(f"closed-form Beveridge v(u) at v={v}", v_closed(u_given_v(v)), v, tol=1e-9)
u0_, h_ = 0.06, 1e-7
th0 = v_closed(u0_) / u0_
check("Beveridge slope dv/du == -(lambda + xi f)/((1-xi) q)",
      (v_closed(u0_ + h_) - v_closed(u0_ - h_)) / (2 * h_),
      -(LAM + XI * finding(th0)) / ((1 - XI) * filling(th0)), tol=1e-5)


check("log-form slope: (1/v) dv/du == [-1/(1-u) - xi/u]/(1-xi)",
      (math.log(v_closed(u0_ + h_)) - math.log(v_closed(u0_ - h_))) / (2 * h_),
      (-1 / (1 - u0_) - XI / u0_) / (1 - XI), tol=1e-5)
check("d ln v / d ln A_m == -1/(1-xi) at given u",
      (math.log(v_closed(u0_, Am=AM * 1.001)) - math.log(v_closed(u0_))) / math.log(1.001),
      -1 / (1 - XI), tol=1e-9)
check("d ln v / d ln lambda == +1/(1-xi) at given u",
      (math.log(v_closed(u0_, lam=LAM * 1.001)) - math.log(v_closed(u0_))) / math.log(1.001),
      1 / (1 - XI), tol=1e-9)
check("u* = (lambda/f)/(1 + lambda/f)", u_star(LAM, F), (LAM / F) / (1 + LAM / F), tol=1e-15)

def wr_equation(b, beta, offers):
    """Solve w - b = beta/(1-beta) E[(w'-w)^+] by bisection."""
    lo, hi = b, float(offers.max())
    for _ in range(100):
        m = 0.5 * (lo + hi)
        if m - b < beta / (1 - beta) * np.maximum(offers - m, 0).mean():
            lo = m
        else:
            hi = m
    return 0.5 * (lo + hi)


def wr_value_iteration(b, beta, offers):
    """Iterate V^U = b + beta E[max(w'/(1-beta), V^U)] and return w^r = (1-beta) V^U."""
    VU = b / (1 - beta)
    for _ in range(400):
        VU = b + beta * np.maximum(offers / (1 - beta), VU).mean()
    return (1 - beta) * VU


z = np.random.default_rng(3).standard_normal(200_000)
offers = 1.0 + 0.3 * z
wr0 = wr_equation(0.4, 0.8, offers)
check("reservation-wage equation == value iteration", wr0, wr_value_iteration(0.4, 0.8, offers),
      tol=1e-6)
check_true("b up raises w^r", wr_equation(0.6, 0.8, offers) > wr0)
check_true("beta up raises w^r", wr_equation(0.4, 0.9, offers) > wr0)
check_true("a mean-preserving spread raises w^r", wr_equation(0.4, 0.8, 1.0 + 0.45 * z) > wr0)

# ---------------------------------------------------------------------------
print()
if failures:
    print(f"{len(failures)} CHECK(S) FAILED: " + "; ".join(failures))
    raise SystemExit(1)
print("all checks pass")
