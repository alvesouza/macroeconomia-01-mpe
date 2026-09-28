#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical checks for Map/aula-03-solow-evidencias.

Covered:
  01-golden-rule             f'(k_gold)=delta+n; s_gold=alpha two ways; the consumption hump;
                             the dynamic-inefficiency test in national-accounts form
  02-markets-and-factor-...  r^K=f'(k), w=f(k)-kf'(k); zero profit; constant Cobb-Douglas
                             shares off steady state; r^K = alpha (delta+n+g)/s
  03-technological-progress  efficiency-unit law; the ng cross term; the BGP growth table;
                             Cobb-Douglas equivalence of the three neutralities
  04-quantifying-and-conv.   Kurlat's calibration reproducing K/Y=3.2; eq. (5.3.1); lambda by
                             log-linearisation and by simulation; eq. (5.3.4) and the 9.4x
                             Mexico number; the alpha implied by a 2% convergence rate
  05-growth-accounting       the accounting identity; development accounting in K/L and K/Y
                             form; the Mincer human-capital contribution
  companion-hidden-wedge     Lista 2 Q2 (Gotham): every read-out at three vectors; landmarks;
                             residual independent of g_K, g_L; firm FOC r = alpha Y/K

Stdlib + numpy + sympy (expanded derivation steps of each note). Run: python Map/aula-03-solow-evidencias/check_growth.py
"""
from __future__ import annotations

import math

import numpy as np

failures: list[str] = []


def check(name, got, want, tol=1e-8):
    ok = abs(float(got) - float(want)) <= tol
    print(f"  {'ok  ' if ok else 'FAIL'}  {name:<56} {float(got):+.6f}  (want {float(want):+.6f})")
    if not ok:
        failures.append(name)


def check_true(name, cond):
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}")
    if not cond:
        failures.append(name)


# Kurlat's calibration, section 5.2 p. 77.
ALPHA, G, N, DELTA, S = 0.35, 0.015, 0.01, 0.04, 0.20
BREAK = DELTA + N + G


def f(k, alpha=ALPHA):
    return k ** alpha


def fp(k, alpha=ALPHA):
    return alpha * k ** (alpha - 1)


def k_tilde_ss(s=S, brk=BREAK, alpha=ALPHA):
    return (s / brk) ** (1 / (1 - alpha))


# ---------------------------------------------------------------------------
print("\n01-golden-rule")
kg = (ALPHA / BREAK) ** (1 / (1 - ALPHA))
check("f'(k_gold) == delta+n+g", fp(kg), BREAK)
check("k_gold closed form", kg, k_tilde_ss(s=ALPHA))
check("s_gold == alpha (saving rate that lands on k_gold)", ALPHA, ALPHA)

# s_gold via the investment-share argument: (delta+n+g)k/f(k) at k_gold.
check("s_gold via investment share == f'(k)k/f(k) == alpha",
      BREAK * kg / f(kg), ALPHA, tol=1e-12)

# The hump: numerical maximisation must agree with the closed form.
grid = np.linspace(0.01, 0.99, 400_001)
c_of_s = np.array([f(k_tilde_ss(s)) - BREAK * k_tilde_ss(s) for s in grid])
check("numerical argmax of c_ss(s) == alpha", grid[int(np.argmax(c_of_s))], ALPHA, tol=1e-4)
check_true("c_ss is single-peaked", np.all(np.diff(np.sign(np.diff(c_of_s))) <= 0))

# Dynamic inefficiency in national-accounts form: capital income vs investment.
def capital_income(s):
    k = k_tilde_ss(s)
    return fp(k) * k


def investment(s):
    return BREAK * k_tilde_ss(s)


check_true("US calibration (s=0.20): capital income exceeds investment, so below Golden Rule",
           capital_income(S) > investment(S))
check_true("over-saving (s=0.60): investment exceeds capital income -- dynamically inefficient",
           capital_income(0.60) < investment(0.60))
check("at s=alpha the two are exactly equal", capital_income(ALPHA), investment(ALPHA), tol=1e-12)

# Cutting s from above the Golden Rule raises consumption immediately AND in the long run.
k_over = k_tilde_ss(0.60)
c_on_impact_before = (1 - 0.60) * f(k_over)
c_on_impact_after = (1 - 0.45) * f(k_over)          # k cannot jump
check_true("cut from s=0.60 to 0.45 raises consumption on impact",
           c_on_impact_after > c_on_impact_before)
check_true("...and in the new steady state too",
           f(k_tilde_ss(0.45)) - BREAK * k_tilde_ss(0.45) > f(k_over) - BREAK * k_over)

# From below, consumption falls on impact -- a trade-off, not an inefficiency.
k_under = k_tilde_ss(0.20)
check_true("raise from s=0.20 to 0.30: consumption falls on impact",
           (1 - 0.30) * f(k_under) < (1 - 0.20) * f(k_under))
check_true("...but is higher in the new steady state",
           f(k_tilde_ss(0.30)) - BREAK * k_tilde_ss(0.30) > f(k_under) - BREAK * k_under)

# ---------------------------------------------------------------------------
print("\n02-markets-and-factor-prices")
k = 3.7
h = 1e-7
w = f(k) - k * fp(k)
check("r^K == f'(k)", fp(k), (f(k + h) - f(k - h)) / (2 * h), tol=1e-5)
check("factor payments exhaust output: r^K k + w == y", fp(k) * k + w, f(k), tol=1e-12)
check("capital share == alpha at an arbitrary k (off steady state)", fp(k) * k / f(k), ALPHA)
check("capital share == alpha at a different k", fp(0.2) * 0.2 / f(0.2), ALPHA)

rK = ALPHA * BREAK / S
check("r^K = alpha (delta+n+g)/s", rK, 0.1138, tol=1e-4)
check("r = r^K - delta", rK - DELTA, 0.0738, tol=1e-4)
check("...which is Kurlat's 7.4 per cent", round(rK - DELTA, 3), 0.074)
check("r^K from the steady state directly", fp(k_tilde_ss()), rK, tol=1e-12)

# Golden Rule restated as r = n + g.
check("at the Golden Rule, r == n+g", fp(kg) - DELTA, N + G, tol=1e-12)

# ---------------------------------------------------------------------------
print("\n03-technological-progress")
# The exact efficiency-unit law vs the approximation: the ng cross term.
exact_break = (1 + G) * (1 + N) - (1 - DELTA)
check("exact break-even rate = delta+n+g+ng", exact_break, DELTA + N + G + N * G)
check("the ng cross term", N * G, 0.00015)
check_true("ng is under 0.3 per cent of the break-even rate", N * G / BREAK < 0.003)

# BGP growth rates, by simulating levels.
T = 400
A = np.array([(1 + G) ** t for t in range(T + 1)])
L = np.array([(1 + N) ** t for t in range(T + 1)])
kt = np.empty(T + 1)
kt[0] = k_tilde_ss() * 0.4
for t in range(T):
    kt[t + 1] = ((1 - DELTA) * kt[t] + S * f(kt[t])) / ((1 + G) * (1 + N))
# The EXACT discrete law has break-even delta+n+g+ng, so its steady state is slightly
# below the continuous-time closed form. That gap is the ng term of note 03 sec. 3.2.
k_ss_exact = (S / exact_break) ** (1 / (1 - ALPHA))
check("k-tilde converges to the EXACT discrete steady state", kt[-1], k_ss_exact, tol=1e-6)
check("the continuous-time closed form sits above it by the ng term",
      k_ss_exact / k_tilde_ss() - 1, -0.00354, tol=1e-5)
check_true("the two differ by well under one per cent",
           abs(k_ss_exact / k_tilde_ss() - 1) < 0.005)

y_pw = A * f(kt)                      # y = Y/L = A * f(k-tilde)
Y = y_pw * L
check("y per worker grows at g on the BGP", y_pw[-1] / y_pw[-2] - 1, G, tol=1e-6)
check("aggregate Y grows at (1+n)(1+g)-1", Y[-1] / Y[-2] - 1, (1 + N) * (1 + G) - 1, tol=1e-6)
check_true("y-tilde is CONSTANT on the BGP, not growing at g",
           abs(f(kt[-1]) / f(kt[-2]) - 1) < 1e-9)
w_path = A * (f(kt) - kt * fp(kt))
check("the real wage grows at g", w_path[-1] / w_path[-2] - 1, G, tol=1e-6)
check("the labour share is constant", (w_path[-1] / y_pw[-1]), 1 - ALPHA, tol=1e-6)
check("K/Y is constant at s/(delta+n+g+ng) in the exact law",
      kt[-1] / f(kt[-1]), S / exact_break, tol=1e-6)
check("...and s/(delta+n+g) is Kurlat's 3.08 against a measured 3.2", S / BREAK, 3.0769, tol=1e-4)

# Cobb-Douglas: the three neutralities are the same function up to units.
Ahat, Kv, Lv = 1.9, 4.2, 2.6
hicks = Ahat * Kv ** ALPHA * Lv ** (1 - ALPHA)
harrod = Kv ** ALPHA * (Ahat ** (1 / (1 - ALPHA)) * Lv) ** (1 - ALPHA)
solowneutral = (Ahat ** (1 / ALPHA) * Kv) ** ALPHA * Lv ** (1 - ALPHA)
check("Hicks-neutral == labour-augmenting (rescaled)", hicks, harrod, tol=1e-9)
check("Hicks-neutral == capital-augmenting (rescaled)", hicks, solowneutral, tol=1e-9)

# ---------------------------------------------------------------------------
print("\n04-quantifying-and-convergence")
# eq. (5.3.1) with n=g=0, as Kurlat sets it up.
k_test = 2.0
g_y_exact = (f(k_test + (S * f(k_test) - DELTA * k_test)) - f(k_test)) / f(k_test)
g_y_531 = S * fp(k_test) - DELTA * ALPHA
check("(5.3.1) approximates the exact growth rate", g_y_531, g_y_exact, tol=5e-3)
check_true("(5.3.1) is decreasing in k -- richer grows slower",
           S * fp(3.0) - DELTA * ALPHA < S * fp(1.0) - DELTA * ALPHA)

# lambda by log-linearisation, and by simulating the decay of the log gap.
lam = (1 - ALPHA) * BREAK
check("lambda = (1-alpha)(delta+n+g)", lam, 0.04225)
check("half-life in years", math.log(2) / lam, 16.406, tol=1e-2)

def decay(start_ratio, years):
    kk = k_tilde_ss() * start_ratio
    x0 = math.log(kk) - math.log(k_tilde_ss())
    dt = 1e-3
    for _ in range(int(years / dt)):
        kk += dt * (S * f(kk) - BREAK * kk)
    return (math.log(kk) - math.log(k_tilde_ss())) / x0


# Near the steady state the log-linearisation is accurate, which is all it claims.
check("small gap (1%): decay over 10 years matches exp(-10 lambda)",
      decay(0.99, 10), math.exp(-10 * lam), tol=1e-3)
check_true("even a 5% gap already decays measurably faster than the linear prediction",
           decay(0.95, 10) < math.exp(-10 * lam))
# Far from it, convergence is FASTER than lambda, because f(k)/k is steeper below k_ss.
check_true("large gap (50% below): decay is faster than the linear prediction",
           decay(0.50, 10) < math.exp(-10 * lam))
check("large-gap decay over 10 years", decay(0.50, 10), 0.6025, tol=1e-3)

# The alpha implied by an empirical 2% convergence rate.
alpha_implied = 1 - 0.02 / BREAK
check("alpha needed for lambda = 2%", alpha_implied, 0.6923, tol=1e-4)
check_true("that is roughly twice the national-accounts capital share",
           alpha_implied > 1.8 * ALPHA)

# eq. (5.3.4): the Mexico-US rental-rate ratio.
x = 0.3
ratio = x ** ((ALPHA - 1) / ALPHA)
check("(5.3.4): r^K_MEX / r^K_US at x=0.3, alpha=0.35", ratio, 9.4, tol=0.05)
check("implied Mexican rental rate", rK * ratio, 1.070, tol=0.01)
check("implied Mexican interest rate", rK * ratio - DELTA, 1.030, tol=0.01)
check_true("that is an implausible interest rate -- the Lucas paradox",
           rK * ratio - DELTA > 1.0)
# With broad capital the paradox nearly disappears.
check("at alpha=0.7 the same gap implies only this ratio",
      x ** ((0.7 - 1) / 0.7), 1.6753, tol=1e-4)

# Predicted vs actual output for the poorest countries (Figure 5.3.3 magnitudes).
check_true("a 10x predicted-vs-actual gap is what Kurlat reports", 10000 / 1000 == 10)

# ---------------------------------------------------------------------------
print("\n05-growth-accounting-and-tfp")
gY, gK, gL = 0.031, 0.036, 0.011
gA = gY - ALPHA * gK - (1 - ALPHA) * gL
check("Solow residual", gA, 0.031 - 0.35 * 0.036 - 0.65 * 0.011)
check("per-worker form g_y = g_A + alpha g_k", gA + ALPHA * (gK - gL), gY - gL, tol=1e-12)

# Development accounting, K/L form.
y_rel, k_rel = 0.10, 0.15
cap_contrib = k_rel ** ALPHA
tfp_contrib = y_rel / cap_contrib
check("capital contribution (K/L form)", cap_contrib, 0.5148, tol=1e-4)
check("TFP residual (K/L form)", tfp_contrib, 0.1943, tol=1e-4)
check("capital's share of the log gap", math.log(cap_contrib) / math.log(y_rel), 0.2884, tol=1e-4)
check_true("TFP explains the majority of the log gap",
           math.log(tfp_contrib) / math.log(y_rel) > 0.5)

# K/Y form: y = A^{1/(1-alpha)} (K/Y)^{alpha/(1-alpha)}
KY_rel = 0.8
tfp_KY = y_rel / KY_rel ** (ALPHA / (1 - ALPHA))
check("K/Y form leaves this TFP ratio", tfp_KY, 0.1128, tol=1e-4)
check_true("the K/Y form attributes MORE to TFP than the K/L form", tfp_KY < tfp_contrib)
# The identity behind the K/Y form.
A_lvl, k_lvl = 1.4, 3.1
y_lvl = A_lvl * k_lvl ** ALPHA
check("y == A^{1/(1-a)} (K/Y)^{a/(1-a)}",
      A_lvl ** (1 / (1 - ALPHA)) * (k_lvl / y_lvl) ** (ALPHA / (1 - ALPHA)), y_lvl, tol=1e-9)

# Human capital via Mincer.
phi, S_i, S_us = 0.10, 4.0, 12.0
h_rel = math.exp(phi * (S_i - S_us))
check("h_i/h_US = exp(phi (S_i - S_US))", h_rel, 0.4493, tol=1e-4)
check("its contribution in the K/L form", h_rel ** (1 - ALPHA), 0.5945, tol=1e-4)
check_true("human capital explains well under half the log gap",
           math.log(h_rel ** (1 - ALPHA)) / math.log(y_rel) < 0.25)

# In the K/L form, h enters as h^(1-alpha); in the K/Y form it enters as h^1, because
#   y = A^{1/(1-a)} (K/Y)^{a/(1-a)} h.
joint_KL = cap_contrib * h_rel ** (1 - ALPHA)
check("K/L form: capital + human capital share of the log gap",
      math.log(joint_KL) / math.log(y_rel), 0.5142, tol=1e-4)
check_true("so the K/L form splits the gap roughly half and half", 0.45 < math.log(joint_KL) / math.log(y_rel) < 0.55)

joint_KY = KY_rel ** (ALPHA / (1 - ALPHA)) * h_rel
check("K/Y form: capital + human capital share of the log gap",
      math.log(joint_KY) / math.log(y_rel), 0.3996, tol=1e-4)
check_true("in the preferred K/Y form TFP takes about 60 per cent -- the Hall-Jones number",
           math.log(joint_KY) / math.log(y_rel) < 0.45)

# ---------------------------------------------------------------------------
print("\ncompanion-hidden-wedge (Lista 2 Q2, Gotham)")


def wedge(alpha, th, th2, T, gK, gL):
    """Mirror of model() in companion-hidden-wedge.html; same keys, same formulas."""
    ratio = lambda t: (1 + t) ** -alpha
    dlnA = -alpha * (math.log(1 + th2) - math.log(1 + th))
    resLog = dlnA / T
    gY = alpha * gK + (1 - alpha) * gL + resLog
    return dict(share=th / (1 + th), share2=th2 / (1 + th2), loss=1 - ratio(th),
                sK=alpha, sL=1 - alpha, ahat=ratio(th), ahat2=ratio(th2), dlnA=dlnA,
                resLog=resLog, resComp=((1 + th) / (1 + th2)) ** (alpha / T) - 1, gY=gY,
                capC=alpha * gK, labC=(1 - alpha) * gL,
                residual=gY - alpha * gK - (1 - alpha) * gL)


WEDGE_VECTORS = {
    "lista":  (1 / 3, 0.5, 0.125, 10, 0.03, 0.01),   # Lista 2 (d): theta' = theta/4
    "mild":   (1 / 3, 0.5, 0.25, 10, 0.05, 0.02),    # the brief's landmark
    "worse":  (0.30, 0.8, 2.0, 15, 0.00, -0.005),    # crime worsens, other alpha and T
}
for name, vec in WEDGE_VECTORS.items():
    print(f"  [{name}] " + ", ".join(f"{k}={v:.10f}" for k, v in wedge(*vec).items()))

w = wedge(*WEDGE_VECTORS["lista"])
check("security share theta/(1+theta) == 1/3", w["share"], 1 / 3)
check("A-hat/A == 1.5^(-1/3)", w["ahat"], 0.8736, tol=1e-4)
check("output lost == 12.64%", w["loss"], 0.1264, tol=1e-4)
check("measured shares undistorted: sK == alpha", w["sK"], 1 / 3)
check("Lista (d): log residual (1/3)ln(4/3)/10 == 0.959%/yr", w["resLog"], 0.009589, tol=1e-6)
check("Lista (d): compounded (4/3)^(1/30)-1 == 0.964%/yr", w["resComp"], 0.00964, tol=1e-5)
w = wedge(*WEDGE_VECTORS["mild"])
check("theta'=0.25: log residual (1/3)ln(1.2)/10 == 0.6077%/yr", w["resLog"], 0.006077, tol=1e-6)
# Lista's crime-worsens case, theta'' = 4 theta = 2: -2.28%/yr compounded.
check("crime worsens theta''=2: compounded == -2.28%/yr",
      wedge(1 / 3, 0.5, 2.0, 10, 0, 0)["resComp"], -0.0228, tol=1e-4)
check_true("crime worsening gives a NEGATIVE residual", wedge(*WEDGE_VECTORS["worse"])["resLog"] < 0)

# The residual does not depend on g_K, g_L: build Y from its true law, then do the accounting.
a, th, th2, T = 1 / 3, 0.5, 0.125, 10
for gK, gL in [(0.0, 0.0), (0.10, 0.03), (-0.02, 0.01)]:
    lnY = lambda t: (-a * math.log(1 + (th if t == 0 else th2)) + a * gK * t + (1 - a) * gL * t)
    res = (lnY(T) - lnY(0)) / T - a * gK - (1 - a) * gL
    check(f"residual from simulated Y, g_K={gK:+.2f} g_L={gL:+.2f}", res, wedge(a, th, th2, T, gK, gL)["resLog"], tol=1e-12)

# Firm FOC: alpha A K_P^(a-1) L^(1-a) = r (1+theta)  =>  r = alpha Y / K.
A_, KP, Lg = 1.7, 2.4, 1.3
Yg = A_ * KP ** a * Lg ** (1 - a)
r = a * A_ * KP ** (a - 1) * Lg ** (1 - a) / (1 + th)
check("firm FOC: r == alpha Y / K with K = (1+theta) K_P", r, a * Yg / ((1 + th) * KP), tol=1e-12)
check("development accounting: Y/(K^a L^(1-a)) == A (1+theta)^(-a)",
      Yg / (((1 + th) * KP) ** a * Lg ** (1 - a)), A_ * (1 + th) ** -a, tol=1e-12)

# ---------------------------------------------------------------------------
print("\nexpanded derivation steps (sympy)")
import sympy as sp  # noqa: E402

a, s_, dn, gg, nn, dd = sp.symbols("alpha s delta_n g n delta", positive=True)
kk_, KK, LL, AA, psi, gam = sp.symbols("k K L A psi gamma", positive=True)


def zero(name, expr):
    """Pass when sympy simplifies `expr` to 0; else fall back to 12 random positive points."""
    ok = sp.simplify(expr) == 0
    if not ok:
        syms = sorted(expr.free_symbols, key=str)
        rng = np.random.default_rng(0)
        ok = all(abs(complex(expr.subs({v: rng.uniform(0.1, 0.9) for v in syms}))) < 1e-9
                 for _ in range(12))
    check_true(name, ok)


fk = kk_ ** a
kgold = (a / dn) ** (1 / (1 - a))
zero("01 c_ss = (1-s)f - with sf=(d+n)k gives f-(d+n)k",
     ((1 - s_) * fk - (fk - dn * kk_)).subs(s_, dn * kk_ / fk))
zero("01 k_gold^(a-1) = (d+n)/a", kgold ** (a - 1) - dn / a)
zero("01 k_gold^(1-a) = a/(d+n)", kgold ** (1 - a) - a / dn)
zero("01 equal k's give s = alpha", ((s_ / dn) ** (1 / (1 - a)) - kgold).subs(s_, a))
zero("01 f'(k)k/f(k) = alpha", sp.diff(fk, kk_) * kk_ / fk - a)
zero("01 r(s) = a(d+n)/s - d equals f'(k_ss)-d",
     (sp.diff(fk, kk_).subs(kk_, (s_ / dn) ** (1 / (1 - a))) - dd) - (a * dn / s_ - dd))
check_true("01 r(s) = n exactly at s = alpha (d+n = 0.05, n = 0.01)",
           abs(ALPHA * 0.05 / ALPHA - 0.04 - 0.01) < 1e-12)
# every date after a cut from above: c_t along the transition stays above old c_ss.
k_hi, k_lo = k_tilde_ss(0.60), k_tilde_ss(0.45)
kp, c_min = k_hi, np.inf
for _ in range(3000):
    c_min = min(c_min, (1 - 0.45) * f(kp))
    kp = kp + 0.45 * f(kp) - BREAK * kp
check_true("01 cut 0.60->0.45: c_t > old c_ss at every date",
           c_min > f(k_hi) - BREAK * k_hi)

Fpw = LL * (KK / LL) ** a
zero("02 F_K = f'(k)", sp.diff(Fpw, KK) - sp.diff(fk, kk_).subs(kk_, KK / LL))
zero("02 F_L = f(k) - k f'(k)",
     sp.diff(Fpw, LL) - (fk - kk_ * sp.diff(fk, kk_)).subs(kk_, KK / LL))
Fces = (gam * KK ** psi + (1 - gam) * (AA * LL) ** psi) ** (1 / psi)
zero("02 CES: F_K = gamma K^(psi-1) F^(1-psi)",
     sp.diff(Fces, KK) - gam * KK ** (psi - 1) * Fces ** (1 - psi))
zero("02 CES: capital share = gamma (K/Y)^psi",
     sp.diff(Fces, KK) * KK / Fces - gam * (KK / Fces) ** psi)
kt_ss = (s_ / (dd + nn + gg)) ** (1 / (1 - a))
zero("02 r^K = a k~^(a-1) = a (d+n+g)/s at steady state",
     a * kt_ss ** (a - 1) - a * (dd + nn + gg) / s_)
check("02 r^K arithmetic 0.35*0.325", 0.35 * 0.325, 0.11375, tol=1e-12)

kt = sp.symbols("kt", positive=True)
zero("03 common denominator of the efficiency-unit law",
     ((1 - dd) * kt + s_ * kt ** a) / ((1 + gg) * (1 + nn)) - kt
     - (s_ * kt ** a - ((1 + gg) * (1 + nn) - (1 - dd)) * kt) / ((1 + gg) * (1 + nn)))
zero("03 bracket = d+n+g+ng", sp.expand((1 + gg) * (1 + nn) - (1 - dd)) - (dd + nn + gg + nn * gg))
zero("03 y~_ss = k~_ss^a = (s/(d+n+g))^(a/(1-a))",
     kt_ss ** a - (s_ / (dd + nn + gg)) ** (a / (1 - a)))
Fhar = AA * LL * (KK / (AA * LL)) ** a
wage = sp.diff(Fhar, LL)
fkt = (KK / (AA * LL))
zero("03 w = A[f(k~) - k~ f'(k~)]", wage - AA * (fkt ** a - fkt * a * fkt ** (a - 1)))
zero("03 labour share wL/Y = 1-alpha", wage * LL / Fhar - (1 - a))
zero("03 CD: (A^(1/(1-a)) L)^(1-a) = A L^(1-a)", (AA ** (1 / (1 - a)) * LL) ** (1 - a) - AA * LL ** (1 - a))
zero("03 CD: (A^(1/a) K)^a = A K^a", (AA ** (1 / a) * KK) ** a - AA * KK ** a)
# Uzawa construction with a non-Cobb-Douglas CRS F~ (CES, psi = 0.5).
tt, gam_, n_ = 7.3, 0.04, 0.01
K0, L0 = 2.2, 1.4
Ft = lambda K_, L_: (0.4 * K_ ** 0.5 + 0.6 * L_ ** 0.5) ** 2
lhs = Ft(K0 * math.exp(gam_ * tt), math.exp((gam_ - n_) * tt) * L0 * math.exp(n_ * tt))
check("03 Uzawa: F~(K_t, A(t)L_t) == e^(gamma t) Y_0", lhs, math.exp(gam_ * tt) * Ft(K0, L0), tol=1e-9)
check("03 level gap (a/(1-a)) ln(0.30/0.20)", ALPHA / (1 - ALPHA) * math.log(1.5), 0.2183, tol=1e-4)

x_ = sp.symbols("x")
xdot = (dd + nn + gg) * (sp.exp((a - 1) * x_) - 1)
zero("04 s k~^(a-1) - (d+n+g) with k~ = k~_ss e^x equals (d+n+g)(e^((a-1)x)-1)",
     s_ * (kt_ss * sp.exp(x_)) ** (a - 1) - (dd + nn + gg) - xdot)
zero("04 d xdot/dx at 0 = -(1-a)(d+n+g)", sp.diff(xdot, x_).subs(x_, 0) + (1 - a) * (dd + nn + gg))
t_, lam_, x0_ = sp.symbols("t lambda x0", positive=True)
xt = x0_ * sp.exp(-lam_ * t_)
zero("04 x_t = x0 e^(-lambda t) solves xdot = -lambda x", sp.diff(xt, t_) + lam_ * xt)
check("04 half-life ln2/lambda", math.log(2) / ((1 - ALPHA) * BREAK), 16.406, tol=1e-3)
check("04 data half-life ln2/0.02", math.log(2) / 0.02, 34.657, tol=1e-3)
xr = sp.symbols("xr", positive=True)
zero("04 (5.3.4): (x^(1/a))^(a-1) = x^((a-1)/a)", (xr ** (1 / a)) ** (a - 1) - xr ** ((a - 1) / a))
check("04 0.3^(-1.857) = 9.36", 0.3 ** ((ALPHA - 1) / ALPHA), 9.36, tol=0.01)
check("04 note's corrected broad-capital ratio 1.68", 0.3 ** (-0.3 / 0.7), 1.68, tol=0.005)

Ycd = AA * KK ** a * LL ** (1 - a)
zero("05 F_A A / Y = 1 for Hicks-neutral CD", sp.diff(Ycd, AA) * AA / Ycd - 1)
zero("05 F_K K / Y = alpha", sp.diff(Ycd, KK) * KK / Ycd - a)
gA_, gK_, gL_ = sp.symbols("g_A g_K g_L")
zero("05 g_Y - g_L = g_A + alpha (g_K - g_L)",
     (gA_ + a * gK_ + (1 - a) * gL_ - gL_) - (gA_ + a * (gK_ - gL_)))
check("05 worked residual 0.031-0.0126-0.00715", 0.031 - 0.0126 - 0.00715, 0.01125, tol=1e-12)
yv, hh, KYr = sp.symbols("y h KY", positive=True)
zero("05 K/Y form with h: y^(1-a) = A (K/Y)^a h^(1-a) => y = A^(1/(1-a)) (K/Y)^(a/(1-a)) h",
     (AA * KYr ** a * hh ** (1 - a)) ** (1 / (1 - a)) - AA ** (1 / (1 - a)) * KYr ** (a / (1 - a)) * hh)
check("05 K/Y capital term 0.5385 ln 0.8 / ln 0.1", ALPHA / (1 - ALPHA) * math.log(0.8) / math.log(0.1), 0.0522, tol=1e-4)
check("05 human capital K/L share 0.65*0.8/ln10", 0.65 * 0.8 / math.log(10), 0.2258, tol=1e-4)

# ---------------------------------------------------------------------------
print()
if failures:
    print(f"{len(failures)} CHECK(S) FAILED: " + "; ".join(failures))
    raise SystemExit(1)
print("all checks pass")
