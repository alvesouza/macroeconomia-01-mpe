#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical checks for Map/aula-04-consumo.

Covered:
  02-two-period-problem      closed forms against numerical optimisation; the Euler equation
                             holds at the optimum and fails off it; CRRA nests log; the
                             Benigno (4) log-linearisation
  03-income-and-substitution the total effect against the boxed formula; the Hicksian
                             decomposition by wealth compensation; lender vs borrower signs
  04-permanent-income        both MPCs; the annuity formula; the 1/T scaling; the smoothing
                             ratio r/(1+r)
  05-ricardian-and-constr.   Ricardian equivalence numerically, then broken by a borrowing
                             limit; the Euler INEQUALITY at a binding constraint;
                             precautionary saving and the quadratic counterexample

Stdlib + numpy only (scipy not required). Run: python Map/aula-04-consumo/check_consumption.py
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


BETA, R = 0.96, 0.04


def u(c, sigma):
    return math.log(c) if abs(sigma - 1) < 1e-12 else (c ** (1 - sigma) - 1) / (1 - sigma)


def up(c, sigma):
    return c ** (-sigma)


def wealth(y1, y2, r=R):
    return y1 + y2 / (1 + r)


def solve_closed(y1, y2, r=R, beta=BETA, sigma=1.0):
    """Note 02 sec. 2.4 closed form."""
    W = wealth(y1, y2, r)
    c1 = W / (1 + beta ** (1 / sigma) * (1 + r) ** (1 / sigma - 1))
    c2 = (beta * (1 + r)) ** (1 / sigma) * c1
    return c1, c2


def solve_numeric(y1, y2, r=R, beta=BETA, sigma=1.0, a_min=-1e12):
    """Bisection on the Euler residual, with an optional borrowing limit a >= a_min.

    The residual u'(c1) - beta(1+r)u'(c2) is strictly decreasing in c1, so bisection is
    exact to machine precision -- unlike a direct search on the objective, which is very
    flat for large sigma.
    """
    W = wealth(y1, y2, r)
    cap = min(W - 1e-12, y1 - a_min)          # c1 <= y1 - a_min enforces a >= a_min
    g = lambda c1: up(c1, sigma) - beta * (1 + r) * up((1 + r) * (W - c1), sigma)
    lo, hi = 1e-12, W - 1e-12
    if g(cap) > 0:                            # the constraint binds: corner solution
        c1 = cap
    else:
        for _ in range(300):
            mid = 0.5 * (lo + hi)
            if g(mid) > 0:
                lo = mid
            else:
                hi = mid
        c1 = 0.5 * (lo + hi)
    return c1, (1 + r) * (W - c1)


# ---------------------------------------------------------------------------
print("\n02-two-period-problem")
y1, y2 = 100.0, 100.0
for sig in (0.5, 1.0, 2.0, 5.0):
    c1c, c2c = solve_closed(y1, y2, sigma=sig)
    c1n, c2n = solve_numeric(y1, y2, sigma=sig)
    check(f"closed form == numerical optimum, sigma={sig}", c1c, c1n, tol=1e-5)
    check(f"Euler holds at the optimum, sigma={sig}",
          up(c1c, sig) - BETA * (1 + R) * up(c2c, sig), 0.0, tol=1e-10)

# The Euler equation fails off the optimum -- it is a condition, not an identity.
c1_off = solve_closed(y1, y2)[0] * 1.1
c2_off = (1 + R) * (wealth(y1, y2) - c1_off)
check_true("Euler residual is non-zero away from the optimum",
           abs(up(c1_off, 1.0) - BETA * (1 + R) * up(c2_off, 1.0)) > 1e-4)

# CRRA nests log.
check("CRRA at sigma=1 equals the log closed form",
      solve_closed(y1, y2, sigma=1.0)[0], wealth(y1, y2) / (1 + BETA), tol=1e-12)
check("log share of wealth consumed today == 1/(1+beta)", 1 / (1 + BETA), 0.5102, tol=1e-4)

# Perfect smoothing when beta(1+r) = 1.
beta_star = 1 / (1 + R)
c1s, c2s = solve_closed(120.0, 80.0, beta=beta_star, sigma=2.0)
check("beta(1+r)=1 gives a flat path whatever sigma", c1s, c2s, tol=1e-9)
check_true("r > rho (beta=0.98) tilts consumption toward the future",
           solve_closed(100, 100, beta=0.98)[1] > solve_closed(100, 100, beta=0.98)[0])
check_true("r < rho (beta=0.90) tilts it toward the present",
           solve_closed(100, 100, beta=0.90)[1] < solve_closed(100, 100, beta=0.90)[0])

# The Benigno (4) log-linearisation: ln c2 - ln c1 ~= (r - rho)/sigma.
sig = 2.0
c1b, c2b = solve_closed(100, 100, sigma=sig)
rho = 1 / BETA - 1
check("ln(c2/c1) == (1/sigma)[ln beta + ln(1+r)] exactly",
      math.log(c2b / c1b), (math.log(BETA) + math.log(1 + R)) / sig, tol=1e-12)
check("...which is (r - rho)/sigma to first order",
      math.log(c2b / c1b), (R - rho) / sig, tol=2e-4)

# ---------------------------------------------------------------------------
print("\n03-income-and-substitution")
def dlnc1_dlnR(y1, y2, r=R, beta=BETA, sigma=1.0):
    """The boxed formula: -omega - theta(1/sigma - 1)."""
    W = wealth(y1, y2, r)
    omega = (y2 / (1 + r)) / W
    D = 1 + beta ** (1 / sigma) * (1 + r) ** (1 / sigma - 1)
    theta = 1 - 1 / D
    return -omega - theta * (1 / sigma - 1)


for sig in (0.5, 1.0, 2.0, 4.0):
    h = 1e-6
    c1a = solve_closed(y1, y2, r=R, sigma=sig)[0]
    c1b_ = solve_closed(y1, y2, r=math.expm1(math.log1p(R) + h), sigma=sig)[0]
    numeric = (math.log(c1b_) - math.log(c1a)) / h
    check(f"d ln c1 / d ln(1+r) matches the formula, sigma={sig}",
          numeric, dlnc1_dlnR(y1, y2, sigma=sig), tol=1e-4)

# A genuine LENDER needs front-loaded income: with y1 = y2 and beta(1+r) < 1 the
# household is impatient enough to borrow a little, so it is not the relevant case.
yl1, yl2 = 150.0, 50.0
sl = lambda sig, r: yl1 - solve_closed(yl1, yl2, r=r, sigma=sig)[0]
check_true("this household is genuinely a lender", sl(1.0, R) > 0)
check_true("lender, sigma<1: substitution wins, saving rises with r", sl(0.5, 0.06) > sl(0.5, 0.04))
check_true("lender, sigma>1: income effect wins, saving FALLS with r", sl(4.0, 0.06) < sl(4.0, 0.04))
check_true("lender, sigma=1: saving still rises, because the wealth term shrinks W",
           sl(1.0, 0.06) > sl(1.0, 0.04))

# A borrower: both effects push the same way, so saving rises unambiguously.
yb1, yb2 = 20.0, 200.0
sb = lambda sig, r: yb1 - solve_closed(yb1, yb2, r=r, sigma=sig)[0]
check_true("borrower is indeed borrowing at the baseline", sb(1.0, R) < 0)
for sig in (0.5, 1.0, 2.0, 4.0):
    check_true(f"borrower: saving rises with r at sigma={sig}", sb(sig, 0.06) > sb(sig, 0.04))

# Hicksian decomposition: compensate wealth so the household can just afford the old bundle.
sig = 4.0
r0, r1 = 0.04, 0.06
c1_0, c2_0 = solve_closed(yl1, yl2, r=r0, sigma=sig)
c1_1, _ = solve_closed(yl1, yl2, r=r1, sigma=sig)
W_comp = c1_0 + c2_0 / (1 + r1)          # wealth needed at r1 to afford the old bundle
c1_comp = W_comp / (1 + BETA ** (1 / sig) * (1 + r1) ** (1 / sig - 1))
subst = c1_comp - c1_0
income = c1_1 - c1_comp
check("substitution + income == total effect on c1", subst + income, c1_1 - c1_0, tol=1e-9)
check_true("substitution effect lowers c1 (raises saving)", subst < 0)
check_true("income effect raises c1 for this lender (lowers saving)", income > 0)
check_true("at sigma=4 the income effect wins, so c1 rises overall", c1_1 > c1_0)

# ---------------------------------------------------------------------------
print("\n04-permanent-income")
base = solve_closed(100, 100)[0]
mpc_trans = solve_closed(101, 100)[0] - base
mpc_perm = solve_closed(101, 101)[0] - base
check("transitory MPC (two-period log)", mpc_trans, 1 / (1 + BETA), tol=1e-9)
check("...numerically", mpc_trans, 0.5102, tol=1e-4)
check("permanent MPC", mpc_perm, (1 / (1 + BETA)) * (2 + R) / (1 + R), tol=1e-9)
check("...numerically", mpc_perm, 1.0008, tol=1e-3)
check_true("permanent MPC is about twice the transitory one", mpc_perm / mpc_trans > 1.9)

# Exactly one when beta(1+r) = 1.
b2 = 1 / (1 + R)
base2 = solve_closed(100, 100, beta=b2)[0]
check("permanent MPC is exactly 1 when beta(1+r)=1",
      solve_closed(101, 101, beta=b2)[0] - base2, 1.0, tol=1e-9)

# The annuity formula, against a direct T-period solve with a flat path.
def annuity(W, r, T):
    return (r / (1 + r)) * W / (1 - (1 + r) ** (-T))


for T in (2, 10, 40):
    W = sum(100 / (1 + R) ** t for t in range(T))
    c = annuity(W, R, T)
    pv = sum(c / (1 + R) ** t for t in range(T))
    check(f"annuity exhausts wealth over T={T}", pv, W, tol=1e-8)
check("infinite-horizon annuity c = rW/(1+r)", annuity(1000, R, 10**9), R / (1 + R) * 1000, tol=1e-6)

check("MPC out of a windfall, infinite horizon", R / (1 + R), 0.03846, tol=1e-5)
perm_raise = R / (1 + R) * (1 * (1 + R) / R)     # a permanent +1 raises W by (1+r)/r
check("MPC out of a permanent rise, infinite horizon", perm_raise, 1.0, tol=1e-12)
check("the ratio of the two MPCs", perm_raise / (R / (1 + R)), 26.0, tol=1e-9)

# The transitory MPC is the annuity factor, which tends to 1/T only as r -> 0.
for T in (2, 10, 40):
    W = sum(100 / (1 + R) ** t for t in range(T))
    mpc = annuity(W + 1, R, T) - annuity(W, R, T)
    check(f"transitory MPC at T={T} equals the annuity factor",
          mpc, (R / (1 + R)) / (1 - (1 + R) ** (-T)), tol=1e-9)
    check_true(f"...and exceeds 1/T at r=4% (T={T})", mpc >= 1 / T - 1e-12)
for T in (2, 10, 40):
    tiny = 1e-7
    mpc0 = (tiny / (1 + tiny)) / (1 - (1 + tiny) ** (-T))
    check(f"as r -> 0 the annuity factor collapses to 1/T (T={T})", mpc0, 1 / T, tol=1e-6)
check("at r=4%, T=40 the MPC is nearly twice 1/T",
      ((R / (1 + R)) / (1 - (1 + R) ** (-40))) / (1 / 40), 1.943, tol=1e-3)

# ---------------------------------------------------------------------------
print("\n05-ricardian-and-constraints")
# Ricardian equivalence: shift taxes across periods at constant present value.
def c1_with_taxes(T1, T2, sigma=1.0, a_min=-1e12):
    return solve_numeric(100 - T1, 100 - T2, sigma=sigma, a_min=a_min)[0]


c_ref = c1_with_taxes(10.0, 10.0)
for shift in (5.0, -5.0, 9.0):
    T1n = 10.0 - shift
    T2n = 10.0 + shift * (1 + R)          # same present value
    check(f"Ricardian: consumption unchanged when taxes shift by {shift}",
          c1_with_taxes(T1n, T2n), c_ref, tol=1e-5)
    # Private saving rises exactly as much as public saving falls.
    s_new = (100 - T1n) - c1_with_taxes(T1n, T2n)
    s_ref = (100 - 10.0) - c_ref
    check(f"private saving offsets the deficit exactly (shift={shift})",
          s_new - s_ref, shift, tol=1e-5)

# A change in G is NOT neutral.
check_true("a rise in G lowers consumption -- only tax TIMING is irrelevant",
           c1_with_taxes(20.0, 10.0 + 0 * R) < c_ref)

# Credit constraints: a student with low y1 and high y2.
ys1, ys2 = 20.0, 200.0
c_un = solve_numeric(ys1, ys2)[0]
check_true("unconstrained student wants to borrow", c_un > ys1)
c_con = solve_numeric(ys1, ys2, a_min=0.0)[0]
check("constrained student consumes exactly current income", c_con, ys1, tol=1e-5)

# The Euler equation holds as an INEQUALITY at the corner.
resid = up(ys1, 1.0) - BETA * (1 + R) * up(ys2, 1.0)
check_true("u'(c1) > beta(1+r) u'(c2) at a binding constraint", resid > 0)

# The MPC jumps to one for the constrained household.
mpc_con = solve_numeric(ys1 + 1, ys2, a_min=0.0)[0] - c_con
check("constrained MPC out of transitory income", mpc_con, 1.0, tol=1e-4)
check_true("...against 0.51 for the same household unconstrained",
           abs((solve_numeric(ys1 + 1, ys2)[0] - c_un) - 1 / (1 + BETA)) < 1e-3)

# Ricardian equivalence fails under the constraint.
def c1_taxed_constrained(T1, T2):
    return solve_numeric(ys1 - T1, ys2 - T2, a_min=0.0)[0]


base_c = c1_taxed_constrained(5.0, 5.0)
cut_c = c1_taxed_constrained(0.0, 5.0 + 5.0 * (1 + R))
check_true("a deficit-financed tax cut RAISES consumption when the constraint binds",
           cut_c > base_c + 1e-6)

# Aggregate MPC with a share of constrained households.
chi = 0.7
agg_mpc = chi * (R / (1 + R)) + (1 - chi) * 1.0
check("aggregate MPC with 30% constrained", agg_mpc, 0.3269, tol=1e-4)
check_true("...which lands in the empirically estimated 0.2-0.4 range", 0.2 < agg_mpc < 0.4)

# Precautionary saving: needs u''' > 0, not merely concavity.
def euler_gap_under_risk(sigma, spread):
    """E[u'(c2)] vs u'(E c2): positive gap means precaution."""
    lo, hi = 100 - spread, 100 + spread
    return 0.5 * (up(lo, sigma) + up(hi, sigma)) - up(100.0, sigma)


for sig in (1.0, 2.0, 5.0):
    check_true(f"CRRA sigma={sig} is prudent: E[u'] > u'(E)", euler_gap_under_risk(sig, 30) > 0)
check_true("CRRA third derivative is positive", 2.0 * 3.0 * 100.0 ** (-4.0) > 0)

# Quadratic utility: risk averse but NOT prudent, so no precautionary saving.
uq_p = lambda c: 1 - 0.001 * c                    # u'(c) linear  =>  u''' = 0
gap_quad = 0.5 * (uq_p(70) + uq_p(130)) - uq_p(100)
check("quadratic utility has zero precautionary gap", gap_quad, 0.0, tol=1e-15)
check_true("...which is exactly why the random walk needs quadratic utility",
           abs(gap_quad) < 1e-15)

# ---------------------------------------------------------------------------
print()
if failures:
    print(f"{len(failures)} CHECK(S) FAILED: " + "; ".join(failures))
    raise SystemExit(1)
print("all checks pass")
