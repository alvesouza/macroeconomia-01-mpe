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
  derivation steps           every intermediate line the notes write out (sympy)
  companion-taxes-and-limits every read-out at three Lista 3 vectors, and the page's own JS
                             model run under node against the Python mirror (skipped if no node)

Stdlib + numpy, plus sympy for the derivation-step block (scipy not required). Run: python Map/aula-04-consumo/check_consumption.py
"""
from __future__ import annotations

import json
import math
import pathlib
import re
import shutil
import subprocess

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
print("\ncompanion-taxes-and-limits (Lista 3)")
# Mirror of the MODEL block in companion-taxes-and-limits.html; the two are compared below.
def tl_solve(y1, y2, a0, r, beta, sigma, tau1, tau2, taus, b):
    """Lista 3 household: c1 + a = a0 + y1 - tau1, c2 = y2 - tau2 + (1+r-taus)a, a >= -b.

    b = math.inf means no limit. Returns the page's read-outs as a dict.
    """
    R = 1 + r - taus
    x1, x2 = a0 + y1 - tau1, y2 - tau2
    W = x1 + x2 / R
    D = 1 + beta ** (1 / sigma) * R ** (1 / sigma - 1)
    c1 = W / D
    a = x1 - c1
    binds = a < -b
    if binds:
        a, c1 = -b, x1 + b
    c2 = x2 + R * a
    return dict(c1=c1, c2=c2, a=a, W=W, R=R, binds=binds, ratio=c2 / c1,
                pv=tau1 + (tau2 + taus * a) / (1 + r), U=u(c1, sigma) + beta * u(c2, sigma))


def tl_compare(p):
    """Savings tax against a period-2 lump sum raising the same revenue; T* by bisection."""
    S = tl_solve(**{**p, "tau2": 0.0})
    rev = p["taus"] * S["a"]
    L = tl_solve(**{**p, "tau2": rev, "taus": 0.0})
    UL = lambda T: tl_solve(**{**p, "tau2": T, "taus": 0.0})["U"]
    lo, hi = rev, rev + 1
    while UL(hi) > S["U"]:
        hi = rev + 2 * (hi - rev)
    for _ in range(100):
        m = 0.5 * (lo + hi)
        lo, hi = (m, hi) if UL(m) > S["U"] else (lo, m)
    return S, L, rev, 0.5 * (lo + hi) - rev


def tl_dc1dr(p):
    s, R = p["sigma"], 1 + p["r"]
    D = 1 + p["beta"] ** (1 / s) * R ** (1 / s - 1)
    return -(p["a0"] + p["y1"]) * p["beta"] ** (1 / s) * (1 / s - 1) * R ** (1 / s - 2) / D ** 2


base3 = dict(r=0.5, beta=0.96, sigma=2.0, taus=0.0, b=math.inf)
V = {
    "unconstrained": {**base3, "y1": 100, "y2": 69, "a0": 10, "tau1": 6, "tau2": 9},
    "binding":       {**base3, "y1": 20, "y2": 132, "a0": 0, "tau1": 0, "tau2": 0, "b": 10},
    "savings tax":   {**base3, "y1": 100, "y2": 66, "a0": 0, "tau1": 0, "tau2": 0, "taus": 0.2},
}
tl = {}
for name, p in V.items():
    s = tl_solve(**p)
    swp = tl_solve(**{**p, "tau1": p["tau1"] - 1, "tau2": p["tau2"] + 1 + p["r"]})
    tl[name] = dict(s=s, swap=swp)
    check(f"[{name}] period-1 budget c1 + a = a0 + y1 - tau1",
          s["c1"] + s["a"], p["a0"] + p["y1"] - p["tau1"], tol=1e-10)
    check(f"[{name}] period-2 budget", s["c2"], p["y2"] - p["tau2"] + s["R"] * s["a"], tol=1e-10)
    if s["binds"]:
        check_true(f"[{name}] Euler is a strict inequality at the corner",
                   up(s["c1"], p["sigma"]) > p["beta"] * s["R"] * up(s["c2"], p["sigma"]))
        check(f"[{name}] swap raises c1 by exactly 1", swp["c1"] - s["c1"], 1.0, tol=1e-10)
    else:
        check(f"[{name}] Euler holds", up(s["c1"], p["sigma"]) - p["beta"] * s["R"] * up(s["c2"], p["sigma"]),
              0.0, tol=1e-12)
        if p["taus"] == 0:
            check(f"[{name}] swap leaves c1 unchanged", swp["c1"], s["c1"], tol=1e-10)
            check(f"[{name}] swap leaves c2 unchanged", swp["c2"], s["c2"], tol=1e-10)
            check(f"[{name}] swap raises a by exactly 1", swp["a"] - s["a"], 1.0, tol=1e-10)
    check(f"[{name}] swap leaves the PV of lump-sum taxes unchanged", swp["pv"] - s["pv"],
          (p["taus"] * (swp["a"] - s["a"])) / (1 + p["r"]), tol=1e-10)

# Lista 3 reference numbers (Resolucao/lista3_resolucao.tex).
check("1(a): c1 = 80", tl["unconstrained"]["s"]["c1"], 80.0, tol=1e-9)
check("1(a): c2 = 96", tl["unconstrained"]["s"]["c2"], 96.0, tol=1e-9)
check("1(a): a = 24", tl["unconstrained"]["s"]["a"], 24.0, tol=1e-9)
check_true("2(c): the young household's limit binds", tl["binding"]["s"]["binds"])
check("2(c): c1 = y1 + b = 30", tl["binding"]["s"]["c1"], 30.0, tol=1e-12)
check("2(c): c2/c1 = 3.90", tl["binding"]["s"]["ratio"], 3.9, tol=1e-12)

pS = V["savings tax"]
S, L, rev, dwl = tl_compare(pS)
tl["savings tax"].update(L=L, rev=rev, dwl=dwl)
check("2(d): savings-tax c1 = 81.09", S["c1"], 81.09, tol=5e-3)
check("2(d): equal-revenue lump sum T = 3.78", rev, 3.78, tol=5e-3)
check("2(d): lump-sum c1 = 78.60", L["c1"], 78.60, tol=5e-3)
check("2(d): deadweight loss 0.27", dwl, 0.27, tol=5e-3)
check("savings tax: (c2/c1)^sigma = beta(1+r-taus)", S["ratio"] ** 2, 0.96 * 1.3, tol=1e-12)
check("lump sum: c2/c1 unchanged at [beta(1+r)]^(1/sigma)", L["ratio"], math.sqrt(0.96 * 1.5), tol=1e-12)
check("lump-sum plan costs the same revenue: savings plan lies on its budget line",
      S["c1"] + S["c2"] / 1.5, L["c1"] + L["c2"] / 1.5, tol=1e-10)
check_true("lump sum is welfare-superior: U_L > U_S", L["U"] > S["U"])
Sb, Lb, revb, dwlb = tl_compare({**V["binding"], "b": math.inf, "taus": 0.2})
check_true("borrower (a<0): the 'tax' is a subsidy, revenue negative", revb < 0 and Sb["a"] < 0)
check_true("...and the lump-sum transfer still beats it", Lb["U"] > Sb["U"] and dwlb > 0)

for sig in (0.5, 1.0, 2.0, 4.0):
    p = {**V["unconstrained"], "y2": 0, "tau1": 0, "tau2": 0, "sigma": sig}
    h = 1e-6
    fd = (tl_solve(**{**p, "r": p["r"] + h})["c1"] - tl_solve(**{**p, "r": p["r"] - h})["c1"]) / (2 * h)
    check(f"dc1/dr formula vs finite difference, sigma={sig}", tl_dc1dr(p), fd, tol=1e-6)
    check_true(f"sign(dc1/dr) = sign(sigma - 1) at sigma={sig}",
               (fd > 1e-9) == (sig > 1) and (fd < -1e-9) == (sig < 1))
    tl.setdefault("dc1dr", {})[sig] = tl_dc1dr(p)

# The page's JS model, run under node on the same vectors.
node = shutil.which("node")
if node is None:
    print("  SKIP  node not found: JS model not cross-checked")
else:
    html = (pathlib.Path(__file__).with_name("companion-taxes-and-limits.html")).read_text(encoding="utf-8")
    model = re.search(r"// MODEL-BEGIN.*?// MODEL-END", html, re.S).group(0)
    js_vec = {k: {**p, "b": 1e300 if p["b"] == math.inf else p["b"]} for k, p in V.items()}
    js = model + f"""
const V = {json.dumps(js_vec)}, out = {{}};
for (const [k, p] of Object.entries(V)) {{
  const [s, w] = swap(p); out[k] = {{s, swap: w}};
}}
const c = taxCompare(V["savings tax"]); Object.assign(out["savings tax"], {{L: c.L, rev: c.rev, dwl: c.dwl}});
out.dc1dr = {{}};
for (const sg of [0.5, 1.0, 2.0, 4.0]) out.dc1dr[sg] = dc1dr({{...V.unconstrained, y2: 0, tau1: 0, tau2: 0, sigma: sg}});
console.log(JSON.stringify(out));"""
    J = json.loads(subprocess.run([node, "-e", js], capture_output=True, text=True, check=True).stdout)
    for name in V:
        for part in ("s", "swap"):
            for key in ("c1", "c2", "a", "pv", "ratio", "U"):
                check(f"JS == Python [{name}] {part}.{key}", J[name][part][key], tl[name][part][key], tol=1e-6)
            check_true(f"JS == Python [{name}] {part}.binds", J[name][part]["binds"] == tl[name][part]["binds"])
    for key in ("c1", "c2", "a", "U"):
        check(f"JS == Python [savings tax] lump-sum {key}", J["savings tax"]["L"][key], L[key], tol=1e-6)
    check("JS == Python revenue", J["savings tax"]["rev"], rev, tol=1e-6)
    check("JS == Python deadweight loss", J["savings tax"]["dwl"], dwl, tol=1e-6)
    for sig in (0.5, 1.0, 2.0, 4.0):
        key = str(int(sig)) if sig == int(sig) else str(sig)
        check(f"JS == Python dc1/dr sigma={sig}", J["dc1dr"][key], tl["dc1dr"][sig], tol=1e-6)

# ---------------------------------------------------------------------------
print("\nderivation steps written out in the notes (sympy)")
import sympy as sp  # noqa: E402  (only this block needs it)

zero = lambda e: sp.simplify(e) == 0  # noqa: E731
c1_, c2_, y1_, y2_, W_, lam_ = sp.symbols("c1 c2 y1 y2 W lambda", positive=True)
r_, b_, s_, x_, Y_, Cb_, m_, I_, h_ = sp.symbols("r beta sigma x Y Cbar mpc I h", positive=True)
uf = sp.Function("u")

# 01: APC falls; the multiplier; the cross-section regression.
check_true("01 d(C/Y)/dY = -Cbar/Y^2", zero(sp.diff((Cb_ + m_ * Y_) / Y_, Y_) + Cb_ / Y_**2))
Ysol = sp.solve(sp.Eq(Y_, Cb_ + m_ * Y_ + I_), Y_)[0]
check_true("01 Y = (Cbar+I)/(1-mpc) and dY/dI = 1/(1-mpc)",
           zero(Ysol - (Cb_ + I_) / (1 - m_)) and zero(sp.diff(Ysol, I_) - 1 / (1 - m_)))
rng = np.random.default_rng(0)
yp = 80 + rng.normal(0, np.sqrt(0.6), 400_000) * 20
e = rng.normal(0, np.sqrt(0.4), 400_000) * 20
slope, icpt = np.polyfit(yp + e, 0.9 * yp, 1)
check("01 cross-section slope = k*lambda (k=0.9, lambda=0.6)", slope, 0.54, tol=5e-3)
check("01 cross-section intercept = k(1-lambda)*mean Yp", icpt, 0.9 * 0.4 * 80, tol=0.5)
pv_reb = 1.04 ** -3
check("01 announced rebate: flat-path rise over t=2..9", ((0.04 / 1.04) / (1 - 1.04 ** -8)) * pv_reb, 0.127,
      tol=5e-4)

# 02: budget constraint, the three Euler routes, closed forms, slopes.
ibc = sp.expand(((1 + r_) * c1_ + c2_ - (1 + r_) * y1_ - y2_) / (1 + r_))
check_true("02 c2 = y2+(1+r)(y1-c1) rearranges to the IBC",
           zero(ibc.subs(c2_, y2_ + (1 + r_) * (y1_ - c1_))) and
           zero(ibc - (c1_ + c2_ / (1 + r_) - y1_ - y2_ / (1 + r_))))
obj = uf(c1_) + b_ * uf((1 + r_) * (W_ - c1_))
d_obj = sp.diff(obj, c1_).doit()
up_c2 = sp.Subs(sp.Derivative(uf(x_), x_), x_, (1 + r_) * (W_ - c1_)).doit()
check_true("02 chain rule: d/dc1 = u'(c1) - beta(1+r)u'(c2)",
           zero(d_obj - (sp.diff(uf(c1_), c1_) - b_ * (1 + r_) * up_c2)))
check_true("02 Lagrange: lambda / (lambda/(1+r)) = 1+r", zero(lam_ / (lam_ / (1 + r_)) - (1 + r_)))
c1log = sp.solve(sp.Eq(c1_ + b_ * (1 + r_) * c1_ / (1 + r_), W_), c1_)[0]
check_true("02 log: c1 = W/(1+beta)", zero(c1log - W_ / (1 + b_)))
crra = (c1_ ** (1 - s_) - 1) / (1 - s_)
check_true("02 CRRA: u'(c) = c^(-sigma)", zero(sp.diff(crra, c1_) - c1_ ** (-s_)))
check_true("02 c1^-s / c2^-s = (c2/c1)^s", zero(sp.powsimp(c1_ ** (-s_) / c2_ ** (-s_) - (c2_ / c1_) ** s_,
                                                         force=True)))
rho_ = sp.symbols("rho", positive=True)
lin = sp.series(sp.log(1 / (1 + rho_)) + sp.log(1 + r_), r_, 0, 2).removeO()
lin = sp.series(lin, rho_, 0, 2).removeO()
check_true("02 ln beta + ln(1+r) = r - rho to first order", zero(lin - (r_ - rho_)))
lnratio = (sp.log(b_) + x_) / s_               # x = ln(1+r)
check_true("02 d ln(c2/c1) / d ln(1+r) = 1/sigma", zero(sp.diff(lnratio, x_) - 1 / s_))
check_true("02 [beta(1+r)]^(1/s)/(1+r) = beta^(1/s)(1+r)^(1/s-1)",
           zero(sp.powsimp(sp.expand_power_base((b_ * (1 + r_)) ** (1 / s_), force=True) / (1 + r_)
                           - b_ ** (1 / s_) * (1 + r_) ** (1 / s_ - 1), force=True)))
for sig, rr_, bb in ((0.5, 0.3, 0.9), (2.0, 0.1, 0.97), (3.7, 0.5, 0.8)):
    Dn = 1 + bb ** (1 / sig) * (1 + rr_) ** (1 / sig - 1)
    c1n = 100 / Dn
    c2n = (bb * (1 + rr_)) ** (1 / sig) * c1n
    check(f"02 level formula satisfies the IBC (sigma={sig})", c1n + c2n / (1 + rr_), 100, tol=1e-10)
c2_of_c1 = sp.Function("c2")(c1_)
ic = sp.diff(uf(c1_) + b_ * uf(c2_of_c1), c1_)
slope_ic = sp.solve(ic, sp.diff(c2_of_c1, c1_))[0]
check_true("02 IC slope = -u'(c1)/(beta u'(c2))",
           zero(slope_ic + sp.diff(uf(c1_), c1_) / (b_ * sp.Subs(sp.Derivative(uf(x_), x_), x_, c2_of_c1).doit())))

# 03: the elasticity, term by term; the y1 = 0 case; Slutsky in endowment form.
Wr = y1_ + y2_ / (1 + r_)
check_true("03 dW/dr = -y2/(1+r)^2", zero(sp.diff(Wr, r_) + y2_ / (1 + r_) ** 2))
Wx = y1_ + y2_ * sp.exp(-x_)
check_true("03 d ln W / d ln(1+r) = -(y2/(1+r))/W",
           zero(sp.diff(sp.log(Wx), x_) + (y2_ * sp.exp(-x_)) / Wx))
Dx = 1 + b_ ** (1 / s_) * sp.exp((1 / s_ - 1) * x_)
check_true("03 d ln D / d ln(1+r) = (1 - 1/D)(1/sigma - 1)",
           zero(sp.diff(sp.log(Dx), x_) - (1 - 1 / Dx) * (1 / s_ - 1)))
check_true("03 theta = (W - c1)/W = 1 - 1/D", zero((W_ - W_ / Dx) / W_ - (1 - 1 / Dx)))
th_ = sp.symbols("theta", positive=True)
check_true("03 omega=1: -1 - theta(1/s-1) = -(1-theta) - theta/s",
           zero(-1 - th_ * (1 / s_ - 1) + (1 - th_) + th_ / s_))
# Slutsky: c1(p, W) = W / (1 + beta^(1/s) p^(1-1/s)), W = y1 + p y2, p = 1/(1+r).
sig, bb, Y1, Y2, p0, hh = 3.0, 0.96, 150.0, 50.0, 1 / 1.04, 1e-6
c1m = lambda p, W: W / (1 + bb ** (1 / sig) * p ** (1 - 1 / sig))  # noqa: E731
Wp = lambda p: Y1 + p * Y2  # noqa: E731


def hicks_c1(p, U):
    """Compensated c1: on the optimal ray c2 = (beta/p)^(1/s) c1, find c1 giving utility U."""
    kr = (bb / p) ** (1 / sig)
    uu = lambda c: (c ** (1 - sig) - 1) / (1 - sig)  # noqa: E731
    lo_, hi_ = 1e-6, 1e6
    for _ in range(200):
        mid = 0.5 * (lo_ + hi_)
        lo_, hi_ = (mid, hi_) if uu(mid) + bb * uu(kr * mid) < U else (lo_, mid)
    return 0.5 * (lo_ + hi_)


c10 = c1m(p0, Wp(p0))
c20 = (Wp(p0) - c10) / p0
U0 = (c10 ** (1 - sig) - 1) / (1 - sig) + bb * (c20 ** (1 - sig) - 1) / (1 - sig)
total_fd = (c1m(p0 + hh, Wp(p0 + hh)) - c1m(p0 - hh, Wp(p0 - hh))) / (2 * hh)
comp_fd = (hicks_c1(p0 + hh, U0) - hicks_c1(p0 - hh, U0)) / (2 * hh)
dW_fd = (c1m(p0, Wp(p0) + hh) - c1m(p0, Wp(p0) - hh)) / (2 * hh)
check("03 Slutsky: dc1/dp = comp + (y2 - c2) dc1/dW", total_fd, comp_fd + (Y2 - c20) * dW_fd, tol=1e-3)
check_true("03 compensated effect of p on c1 is positive", comp_fd > 0)
om = (50 / 1.04) / (150 + 50 / 1.04)
tot = lambda s: -om - (1 - 1 / (1 + 0.96 ** (1 / s) * 1.04 ** (1 / s - 1))) * (1 / s - 1)  # noqa: E731
lo_, hi_ = 1.0, 6.0
for _ in range(80):
    mid = 0.5 * (lo_ + hi_)
    lo_, hi_ = (lo_, mid) if tot(mid) > 0 else (mid, hi_)
check("03 omega for the (150, 50) lender", om, 0.243, tol=5e-4)
check("03 sigma* where the elasticity is zero", 0.5 * (lo_ + hi_), 1.98, tol=5e-3)
A3 = solve_closed(150, 20, r=0.10, sigma=3.0)
Wc3 = A3[0] + A3[1] / 2.0
B3 = Wc3 / (1 + 0.96 ** (1 / 3) * 2.0 ** (1 / 3 - 1))
C3 = solve_closed(150, 20, r=1.0, sigma=3.0)[0]
check("03 Hicks figure: substitution A->B", B3 - A3[0], -6.0, tol=0.05)
check("03 Hicks figure: income B->C", C3 - B3, 17.4, tol=0.05)

# 04: MPC arithmetic, the 1/T limit, the geometric series, the random walk.
check_true("04 Delta - Delta/(1+beta) = beta Delta/(1+beta)", zero(1 - 1 / (1 + b_) - b_ / (1 + b_)))
check_true("04 permanent MPC = 1 when beta = 1/(1+r)",
           zero((1 / (1 + b_) * (2 + r_) / (1 + r_)).subs(b_, 1 / (1 + r_)) - 1))
T_ = sp.symbols("T", positive=True)
g = (1 + r_) - (1 + r_) ** (1 - T_)
check_true("04 MPC = r / g(r)", zero((r_ / (1 + r_)) / (1 - (1 + r_) ** (-T_)) - r_ / g))
check_true("04 g(0) = 0 and g'(0) = T", zero(g.subs(r_, 0)) and zero(sp.diff(g, r_).subs(r_, 0) - T_))
check_true("04 g'' = -T(T-1)(1+r)^(-T-1)", zero(sp.diff(g, r_, 2) + T_ * (T_ - 1) * (1 + r_) ** (-T_ - 1)))
check("04 T=40 pieces: 1.04^-40", 1.04 ** -40, 0.2083, tol=5e-5)
check("04 T=40 MPC", (0.04 / 1.04) / (1 - 1.04 ** -40), 0.0486, tol=5e-5)
q_ = sp.symbols("q", positive=True)
for T in (3, 7, 12):
    check_true(f"04 S - qS = 1 - q^T, T={T}",
               zero(sum(q_ ** t for t in range(T)) * (1 - q_) - (1 - q_ ** T)))
check_true("04 1/(1 - 1/(1+r)) = (1+r)/r", zero(1 / (1 - 1 / (1 + r_)) - (1 + r_) / r_))
check("04 ratio of MPCs (1+r)/r", 1.04 / 0.04, 26.0, tol=1e-9)
cb_ = sp.symbols("b", positive=True)
up_q = sp.diff(x_ - cb_ / 2 * x_ ** 2, x_)
check_true("04 quadratic u: u'(c) = 1 - bc (linear)", zero(up_q - (1 - cb_ * x_)))

# 05: KKT, aggregate MPC, Jensen by Taylor, CRRA third derivative.
a_, mu_ = sp.symbols("a mu")
Lk = uf(y1_ - a_) + b_ * uf(y2_ + (1 + r_) * a_) + mu_ * a_
foc = sp.diff(Lk, a_).doit()
up1 = sp.Subs(sp.Derivative(uf(x_), x_), x_, y1_ - a_).doit()
up2 = sp.Subs(sp.Derivative(uf(x_), x_), x_, y2_ + (1 + r_) * a_).doit()
check_true("05 KKT FOC: -u'(c1) + beta(1+r)u'(c2) + mu = 0", zero(foc - (-up1 + b_ * (1 + r_) * up2 + mu_)))
kk = 0.04 / 1.04
check("05 aggregate MPC arithmetic", 0.7 * kk + 0.3, 0.327, tol=5e-4)
check("05 constrained share giving MPC 0.2", (0.2 - kk) / (1 - kk), 0.168, tol=5e-4)
check("05 constrained share giving MPC 0.4", (0.4 - kk) / (1 - kk), 0.376, tol=5e-4)
cbar = sp.symbols("cbar", positive=True)
upf = cbar ** (-3)                                   # any smooth u' works; use a concrete one
avg = (sp.Rational(1, 2) * ((cbar + h_) ** (-3) + (cbar - h_) ** (-3)))
taylor = sp.series(avg, h_, 0, 3).removeO()
check_true("05 average of u'(c+-h) = u'(c) + u'''(c) h^2/2 + O(h^4)",
           zero(taylor - (upf + sp.Rational(1, 2) * sp.diff(upf, cbar, 2) * h_ ** 2)))
check_true("05 CRRA u''' = sigma(sigma+1)c^(-sigma-2)",
           zero(sp.diff(x_ ** (-s_), x_, 2) - s_ * (s_ + 1) * x_ ** (-s_ - 2)))
check("05 Jensen figure: E[u'] x 1e4 at 70/130, sigma=2", 0.5 * (70.0 ** -2 + 130.0 ** -2) * 1e4, 1.316,
      tol=5e-4)
cu = solve_closed(40, 120)
check("05 constraint figure: wanted c1", cu[0], 79.3, tol=0.05)
check("05 constraint figure: IC slope at (40,120)", (1 / 40) / (0.96 / 120), 3.125, tol=1e-9)

# ---------------------------------------------------------------------------
print()
if failures:
    print(f"{len(failures)} CHECK(S) FAILED: " + "; ".join(failures))
    raise SystemExit(1)
print("all checks pass")
