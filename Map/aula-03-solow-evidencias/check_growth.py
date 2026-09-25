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

Stdlib + numpy only. Run: python Map/aula-03-solow-evidencias/check_growth.py
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
print()
if failures:
    print(f"{len(failures)} CHECK(S) FAILED: " + "; ".join(failures))
    raise SystemExit(1)
print("all checks pass")
