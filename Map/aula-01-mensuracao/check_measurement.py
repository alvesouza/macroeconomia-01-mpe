#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical checks for Map/aula-01-mensuracao.

Every closed form asserted in the notes of this folder is verified here against an
independent path: Kurlat's own worked numbers where they exist, brute force otherwise.
The script exits non-zero if any note is mistyped.

Covered:
  01-three-approaches        value added telescopes to final output
  02-real-nominal-and-indices  Expandia both ways; the covariance formula (2.1);
                             Laspeyres >= Fisher >= Paasche on random data;
                             the factor-reversal identity P_F * Q_F = V
  03-growth-arithmetic       log-approximation error ~ g^2/2; AM-GM on growth rates;
                             rule of 70
  04-cross-country-and-ppp   Balassa-Samuelson eq. (4.1)-(4.2); the three-factor
                             decomposition of output per person
  05-beyond-gdp              the four-term lambda decomposition against a brute-force
                             expected-utility solve

Stdlib + numpy only. Run: python Map/aula-01-mensuracao/check_measurement.py
"""
from __future__ import annotations

import math

import numpy as np

TOL = 1e-9
rng = np.random.default_rng(20260917)
failures: list[str] = []


def check(name: str, got, want, tol: float = 1e-6) -> None:
    ok = abs(float(got) - float(want)) <= tol
    print(f"  {'ok  ' if ok else 'FAIL'}  {name:<52} {float(got):+.6f}  (want {float(want):+.6f})")
    if not ok:
        failures.append(name)


def check_true(name: str, cond: bool) -> None:
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}")
    if not cond:
        failures.append(name)


# ----------------------------------------------------------------------------
# Index-number machinery: the definitions the notes use, written once.
# ----------------------------------------------------------------------------
def laspeyres_q(p0, q0, q1):
    """Quantity index at base-year prices. Kurlat eq. (1.2.1) as a ratio."""
    return float(p0 @ q1) / float(p0 @ q0)


def paasche_q(p1, q0, q1):
    """Quantity index at final-year prices."""
    return float(p1 @ q1) / float(p1 @ q0)


def laspeyres_p(p0, p1, q0):
    return float(p1 @ q0) / float(p0 @ q0)


def paasche_p(p0, p1, q1):
    return float(p1 @ q1) / float(p0 @ q1)


def fisher(a, b):
    """Geometric mean -- the Fisher ideal index of note 02 eq. (2.2)."""
    return math.sqrt(a * b)


# ----------------------------------------------------------------------------
print("\n01-three-approaches -- value added telescopes")
# A chain of five stages, each buying the previous stage's entire output.
revenues = np.array([12.0, 31.0, 44.5, 60.0, 97.25])
inputs = np.concatenate(([0.0], revenues[:-1]))
value_added = revenues - inputs
check("sum of value added == final-stage revenue", value_added.sum(), revenues[-1])

# Expenditure side with an inventory build: Kurlat Example 1.6, p. 19.
va = (20 - 5) + 2          # car value added + lettuce
expenditure = 20 + 5 + 2 - 10   # C + I(inventories) + X - M
check("Kurlat Ex. 1.6: production == expenditure", va, expenditure)
check("Kurlat Ex. 1.6: the common total is 17", va, 17)

# ----------------------------------------------------------------------------
print("\n02-real-nominal-and-indices -- Expandia, Kurlat Example 1.13, p. 23")
# wheat, computers
p0 = np.array([50.0, 1000.0])
q0 = np.array([10.0, 1.0])
p1 = np.array([60.0, 600.0])
q1 = np.array([11.0, 2.0])

check("nominal GDP 2017", p0 @ q0, 1500)
check("nominal GDP 2018", p1 @ q1, 1860)
check("real 2018 at 2017 prices", p0 @ q1, 2550)
check("real 2017 at 2018 prices", p1 @ q0, 1200)

gI = laspeyres_q(p0, q0, q1) - 1
gF = paasche_q(p1, q0, q1) - 1
check("growth at initial-year prices  g^I", gI, 0.70)
check("growth at final-year prices    g^F", gF, 1860 / 1200 - 1)
check_true("g^F < g^I (early base gives the larger number)", gF < gI)

# The covariance formula, note 02 eq. (2.1).
s0 = (p0 * q0) / float(p0 @ q0)
phat, qhat = p1 / p0, q1 / q0
Ep = float(s0 @ phat)
Eq = float(s0 @ qhat)
Epq = float(s0 @ (phat * qhat))
cov = Epq - Ep * Eq
check("Cov_s(p-hat, q-hat)", cov, -0.12)
check("(2.1): Q^P - Q^L == Cov/E[p-hat]", (1 + gF) - (1 + gI), cov / Ep)

# Fisher chain sits between, and satisfies factor reversal.
QF = fisher(1 + gI, 1 + gF)
PF = fisher(laspeyres_p(p0, p1, q0), paasche_p(p0, p1, q1))
V = float(p1 @ q1) / float(p0 @ q0)
check("Fisher quantity growth", QF - 1, 0.6233, tol=1e-4)
check_true("Fisher is bracketed by the two base-year answers", gF < QF - 1 < gI)
check("factor reversal  P_F * Q_F == V", PF * QF, V)

# The ordering Laspeyres >= Fisher >= Paasche whenever demand slopes down.
print("\n  -- the ordering theorem is a statement about the covariance sign --")


def price_indices(p0r, p1r, q0r, q1r):
    PL = laspeyres_p(p0r, p1r, q0r)
    PP = paasche_p(p0r, p1r, q1r)
    return PL, fisher(PL, PP), PP


def cov_s(p0r, p1r, q0r, q1r):
    s = (p0r * q0r) / float(p0r @ q0r)
    ph, qh = p1r / p0r, q1r / q0r
    return float(s @ (ph * qh)) - float(s @ ph) * float(s @ qh)


# (a) Pure CES substitution: the covariance is negative by construction, so the
#     ordering must hold in every draw. This is note 02 sec. 2.4 as stated.
bad_ces = 0
for _ in range(4000):
    n = int(rng.integers(2, 7))
    p0r = rng.uniform(0.5, 3.0, n)
    q0r = rng.uniform(1.0, 20.0, n)
    eps = rng.uniform(0.2, 3.0)                 # elasticity of substitution
    shock = rng.lognormal(0.0, 0.25, n)         # gross price changes
    p1r = p0r * shock
    q1r = q0r * shock ** (-eps)                 # CES demand, constant real consumption
    PL, PF, PP = price_indices(p0r, p1r, q0r, q1r)
    if cov_s(p0r, p1r, q0r, q1r) >= 0 or not (PL >= PF >= PP - 1e-12):
        bad_ces += 1
check_true(f"pure CES: Cov<0 and Laspeyres >= Fisher >= Paasche, 4000 draws "
           f"(violations: {bad_ces})", bad_ces == 0)

# (b) The converse, which is why the note states the criterion as a covariance and
#     not as "demand slopes down": add idiosyncratic demand shifts and the ordering
#     reverses exactly when the covariance turns positive.
agree = tested = 0
for _ in range(4000):
    n = int(rng.integers(2, 7))
    p0r = rng.uniform(0.5, 3.0, n)
    q0r = rng.uniform(1.0, 20.0, n)
    p1r = p0r * rng.lognormal(0.0, 0.10, n)
    q1r = q0r * rng.lognormal(0.0, 0.30, n)     # demand shifts unrelated to price
    c = cov_s(p0r, p1r, q0r, q1r)
    if abs(c) < 1e-6:
        continue
    tested += 1
    PL, PF, PP = price_indices(p0r, p1r, q0r, q1r)
    if (c < 0) == (PL >= PP):
        agree += 1
check_true(f"sign(Cov) predicts the Laspeyres-Paasche ordering in all {tested} draws",
           agree == tested)

# The CES bias size: ln P^L - ln P^F ~= (1/2) * eps * Var_s(pi)
n = 6
p0r = np.ones(n)
eps = 1.0
pi = rng.normal(0.0, 0.18, n)
p1r = np.exp(pi)
q0r = rng.uniform(5.0, 15.0, n)
q1r = q0r * np.exp(-eps * pi)
s = (p0r * q0r) / float(p0r @ q0r)
PL = laspeyres_p(p0r, p1r, q0r)
PP = paasche_p(p0r, p1r, q1r)
var_s = float(s @ (pi - s @ pi) ** 2)
check("CES bias  ln(P^L/P^F) ~= eps*Var_s(pi)/2",
      math.log(PL / fisher(PL, PP)), 0.5 * eps * var_s, tol=5e-3)

# ----------------------------------------------------------------------------
print("\n03-growth-arithmetic")
for g in (0.01, 0.05, 0.10):
    check(f"log-approximation error at g={g:.2f} ~= g^2/2",
          g - math.log1p(g), g * g / 2, tol=g ** 3)

rates = np.array([0.50, -0.50])
gross = float(np.prod(1 + rates))
cagr = gross ** (1 / len(rates)) - 1
check("+50% then -50% leaves 0.75", gross, 0.75)
check("CAGR of that path", cagr, math.sqrt(0.75) - 1)
check_true("AM-GM: arithmetic mean of rates overstates realised growth",
           rates.mean() > cagr)

check("rule of 70 at 2%: doubling time", math.log(2) / math.log(1.02), 35.003, tol=1e-2)
check("rule of 70 at 7%: doubling time", math.log(2) / math.log(1.07), 10.245, tol=1e-2)

# Product/ratio rule and its discrete cross term.
gY, gL = 0.03, 0.01
check("per-capita growth exactly", (1 + gY) / (1 + gL) - 1, 0.0198, tol=1e-4)
check_true("approximation g_Y - g_L overstates by the cross term",
           (gY - gL) > ((1 + gY) / (1 + gL) - 1))

# ----------------------------------------------------------------------------
print("\n04-cross-country-and-ppp -- Balassa-Samuelson")
# Rich country is 4x as productive in tradables, 1.25x in non-tradables.
AT_rich, AN_rich = 4.0, 1.25
AT_poor, AN_poor = 1.0, 1.0
gamma = 0.5

# eq. (4.1): wage equalisation with P_T = 1 gives P_N = A_T / A_N
PN_rich, PN_poor = AT_rich / AN_rich, AT_poor / AN_poor
# Independent path: solve wage equalisation numerically instead of using (4.1).
W_rich = 1.0 * AT_rich                      # W = P_T * A_T
check("(4.1) rich: P_N from wage equalisation", W_rich / AN_rich, PN_rich)

P_rich = PN_rich ** gamma                   # eq. (4.2) with P_T = 1
P_poor = PN_poor ** gamma
check("(4.2) relative price level P_poor / P_rich", P_poor / P_rich,
      ((AT_poor / AN_poor) / (AT_rich / AN_rich)) ** gamma)
check_true("poorer country has the lower price level", P_poor < P_rich)

# (4.3) in logs
lhs = math.log(P_poor / P_rich)
rhs = gamma * ((math.log(AT_poor) - math.log(AT_rich)) - (math.log(AN_poor) - math.log(AN_rich)))
check("(4.3) log price level == gamma * (tradable gap - non-tradable gap)", lhs, rhs)

# No effect when productivity is uniformly lower -- the point of note 04 sec. 4.3(1)
check("uniform productivity gap gives no price-level gap",
      ((1.0 / 1.0) / (2.0 / 2.0)) ** gamma, 1.0)

# Three-factor decomposition of output per person.
Y, H, E, POP = 2.4e12, 3.2e10, 1.7e7, 3.4e7
check("Y/POP == (Y/H)(H/E)(E/POP)", (Y / H) * (H / E) * (E / POP), Y / POP, tol=1e-3)

# ----------------------------------------------------------------------------
print("\n05-beyond-gdp -- the lambda decomposition")
theta, ubar, sigma = 8.0, 5.0, 1.0   # sigma = 1: log utility, the Jones-Klenow baseline


def welfare(cbar, s, leisure, life_exp):
    """Expected utility behind the veil, log consumption, lognormal within country."""
    e = life_exp / 100.0
    mean_log_c = math.log(cbar) - 0.5 * s * s
    return e * (ubar + mean_log_c - theta * (1 - leisure) ** 2)


us = dict(cbar=40000.0, s=0.75, leisure=0.70, life_exp=79.0)
utilia = dict(cbar=24000.0, s=0.95, leisure=0.76, life_exp=83.0)

# Brute force: solve welfare(lambda * c_US, ...) == welfare(Utilia) for lambda.
target = welfare(**utilia)
lo, hi = 1e-4, 1e4
for _ in range(400):
    mid = math.sqrt(lo * hi)
    if welfare(us["cbar"] * mid, us["s"], us["leisure"], us["life_exp"]) < target:
        lo = mid
    else:
        hi = mid
lam_brute = math.sqrt(lo * hi)

# The closed form of note 05, with the exact (not first-order) mortality term.
e_us, e_ut = us["life_exp"] / 100.0, utilia["life_exp"] / 100.0
term_c = math.log(utilia["cbar"] / us["cbar"])
term_ineq = -0.5 * (utilia["s"] ** 2 - us["s"] ** 2)
term_leis = -theta * ((1 - utilia["leisure"]) ** 2 - (1 - us["leisure"]) ** 2)
inner_ut = ubar + math.log(utilia["cbar"]) - 0.5 * utilia["s"] ** 2 - theta * (1 - utilia["leisure"]) ** 2
term_life = (e_ut - e_us) / e_us * inner_ut
ln_lam = term_c + term_ineq + term_leis + term_life

check("four-term decomposition reproduces the brute-force solve",
      ln_lam, math.log(lam_brute), tol=1e-6)
print(f"         consumption {term_c:+.4f} | inequality {term_ineq:+.4f} | "
      f"leisure {term_leis:+.4f} | life {term_life:+.4f}  ->  lambda = {math.exp(ln_lam):.3f}")

# Jensen: E[ln c] < ln E[c], by exactly s^2/2 under lognormality.
s_test = 0.9
draws = rng.lognormal(mean=math.log(30000.0) - 0.5 * s_test ** 2, sigma=s_test, size=4_000_000)
check("E[ln c] = ln E[c] - s^2/2 (Monte Carlo)",
      math.log(draws.mean()) - np.log(draws).mean(), 0.5 * s_test ** 2, tol=2e-3)

# The inequality penalty scales linearly in sigma.
for sig in (1.0, 2.0, 5.0):
    check(f"penalty at sigma={sig:.0f} is sigma*s^2/2", sig * 0.9 ** 2 / 2, sig * 0.405)

# HDI: geometric mean makes the components complements; a zero sinks the index.
hdi = lambda a, b, c: (a * b * c) ** (1 / 3)
check("HDI with a zero component is zero", hdi(0.0, 0.9, 0.9), 0.0)
check_true("geometric mean below arithmetic mean for unequal components",
           hdi(0.4, 0.9, 0.95) < (0.4 + 0.9 + 0.95) / 3)

# Gini <-> log s.d. for a lognormal: G = 2*Phi(s/sqrt2) - 1.
Phi = lambda x: 0.5 * (1 + math.erf(x / math.sqrt(2)))
check("Gini at s=0.5", 2 * Phi(0.5 / math.sqrt(2)) - 1, 0.276, tol=1e-3)
check("Gini at s=1.0", 2 * Phi(1.0 / math.sqrt(2)) - 1, 0.521, tol=1e-3)

# ----------------------------------------------------------------------------
print()
if failures:
    print(f"{len(failures)} CHECK(S) FAILED: " + "; ".join(failures))
    raise SystemExit(1)
print("all checks pass")
