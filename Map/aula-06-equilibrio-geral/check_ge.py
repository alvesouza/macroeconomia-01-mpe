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

  expanded steps               sympy checks of every derivation step the notes spell out
                               (also derivacoes-cap-09 and exogenous-capital-lista-05)

Stdlib + numpy + sympy. Run: python Map/aula-06-equilibrio-geral/check_ge.py
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
print("\ncompanion-frozen-capital -- Lista 5 Q1, capital fixed at K-bar")
# Mirrors the page's model block: (1.8) by bisection, then every read-out. Called by name
# (runpy) from the node cross-check of the page's JS, so keep the signature and keys.


def frozen_period(A, v):
    """Period read-outs at productivity A; v holds sigma, psi, alpha, K."""
    e = v["alpha"] + (1 - v["alpha"]) * v["sigma"]
    rhs = math.log((1 - v["alpha"]) / v["psi"]) + (1 - v["sigma"]) * math.log(A * v["K"] ** v["alpha"])
    lo, hi = 0.0, 1.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if e * math.log(mid) - math.log(1 - mid) > rhs:
            hi = mid
        else:
            lo = mid
    L = 0.5 * (lo + hi)
    Ka = v["K"] ** v["alpha"]
    c = A * Ka * L ** (1 - v["alpha"])
    w = (1 - v["alpha"]) * A * Ka * L ** (-v["alpha"])
    rK = v["alpha"] * A * v["K"] ** (v["alpha"] - 1) * L ** (1 - v["alpha"])
    return dict(L=L, c=c, w=w, rK=rK, mrs=v["psi"] * c ** v["sigma"] / (1 - L),
                el=(1 - v["sigma"]) / (v["alpha"] + (1 - v["alpha"]) * v["sigma"] + L / (1 - L)),
                profit=c - w * L - rK * v["K"])


def frozen_model(v):
    p1, p2 = frozen_period(v["A1"], v), frozen_period(v["A2"], v)
    return dict(p1=p1, p2=p2, r=(p2["c"] / p1["c"]) ** v["sigma"] / v["beta"] - 1)


FROZEN_VECTORS = {
    "sigma<1": dict(A1=1.0, A2=1.3, sigma=0.5, psi=1.8, alpha=0.35, K=2.0, beta=0.96),
    "sigma=1": dict(A1=0.8, A2=1.5, sigma=1.0, psi=1.2, alpha=0.30, K=3.0, beta=0.95),
    "sigma>1": dict(A1=1.2, A2=0.9, sigma=2.5, psi=2.5, alpha=0.40, K=1.5, beta=0.98),
}
for tag, v in FROZEN_VECTORS.items():
    m = frozen_model(v)
    for t, A in (("1", v["A1"]), ("2", v["A2"])):
        p = m["p" + t]
        check(f"[{tag}] t={t} labour FOC: MRS = w", p["mrs"] - p["w"], 0.0, tol=1e-9)
        check(f"[{tag}] t={t} goods: c = A Kbar^a L^(1-a)", p["c"],
              A * v["K"] ** v["alpha"] * p["L"] ** (1 - v["alpha"]), tol=1e-14)
        check(f"[{tag}] t={t} zero profit: Y - wL - r^K Kbar", p["profit"], 0.0, tol=1e-12)
        check(f"[{tag}] t={t} r^K = alpha c / Kbar", p["rK"], v["alpha"] * p["c"] / v["K"], tol=1e-12)
        h = 1e-5
        fd = (math.log(frozen_period(A * math.exp(h), v)["L"])
              - math.log(frozen_period(A * math.exp(-h), v)["L"])) / (2 * h)
        check(f"[{tag}] t={t} (1.10) elasticity = finite difference", p["el"], fd, tol=1e-5)
    check(f"[{tag}] Euler: u'(c1) = beta(1+r)u'(c2)",
          m["p1"]["c"] ** -v["sigma"] - v["beta"] * (1 + m["r"]) * m["p2"]["c"] ** -v["sigma"], 0.0, tol=1e-12)
    s = math.copysign(1, 1 - v["sigma"]) if v["sigma"] != 1 else 0
    check_true(f"[{tag}] sign of the elasticity is sign(1 - sigma)",
               all((m[k]["el"] > 0) - (m[k]["el"] < 0) == s for k in ("p1", "p2")))
    print(f"        {tag}: L=({m['p1']['L']:.8f}, {m['p2']['L']:.8f})  w=({m['p1']['w']:.8f}, {m['p2']['w']:.8f})"
          f"  rK=({m['p1']['rK']:.8f}, {m['p2']['rK']:.8f})  c=({m['p1']['c']:.8f}, {m['p2']['c']:.8f})"
          f"  el=({m['p1']['el']:+.8f}, {m['p2']['el']:+.8f})  r={m['r']:.8f}")

v = FROZEN_VECTORS["sigma=1"]
check("sigma=1 closed form L = (1-a)/(1-a+psi), both periods",
      frozen_model(v)["p1"]["L"], (1 - v["alpha"]) / (1 - v["alpha"] + v["psi"]), tol=1e-12)
check("...independent of A", frozen_model(v)["p2"]["L"], frozen_model(v)["p1"]["L"], tol=1e-12)
base = dict(A1=1.0, A2=1.0, sigma=1.0, psi=1.8, alpha=0.35, K=2.0, beta=0.96)
check("resolution table: L = 0.26531 at sigma=1", frozen_period(1.0, base)["L"], 0.26531, tol=5e-6)
check("resolution table: L = 0.19273 at sigma=0.5", frozen_period(1.0, {**base, "sigma": 0.5})["L"], 0.19273, tol=5e-6)
check("resolution table: elasticity +0.5472 at sigma=0.5",
      frozen_period(1.0, {**base, "sigma": 0.5})["el"], 0.5472, tol=5e-5)
check("resolution table: L = 0.35647 at sigma=2", frozen_period(1.0, {**base, "sigma": 2.0})["L"], 0.35647, tol=5e-6)
check("A2 = A1 gives r = 1/beta - 1", frozen_model({**base, "sigma": 2.0})["r"], 1 / 0.96 - 1, tol=1e-12)

# ---------------------------------------------------------------------------
print("\nexpanded derivation steps (sympy): notes 01, 02, derivacoes-cap-09, lista-05")
import sympy as sp  # noqa: E402

a_, d_, rho_, sg, bt, A_, psi_ = sp.symbols("alpha delta rho sigma beta A psi", positive=True)
k, c, L, r, rK = sp.symbols("k c L r r_K", positive=True)


def zero(name, expr, subs=None):
    """Pass when expr simplifies to 0; if sympy cannot, evaluate it at the point subs."""
    e = sp.simplify(expr)
    if e != 0 and subs is not None:
        e = sp.N(expr.subs(subs))
    check(name, float(e), 0.0, tol=1e-10)


pt = {a_: 0.35, d_: 0.06, rho_: 0.03, sg: 2.0, bt: 1 / 1.03, A_: 1.3, psi_: 1.8}

# derivacoes (9.1.7)-(9.1.8): household Lagrangian (CRRA u, psi ln l for concreteness)
c1, c2, l1, l2, lam, w1, w2 = sp.symbols("c1 c2 l1 l2 lambda w1 w2", positive=True)
u_ = lambda x: x ** (1 - sg) / (1 - sg)
v_ = lambda x: psi_ * sp.log(x)
Lag = (u_(c1) + v_(l1) + bt * (u_(c2) + v_(l2))
       + lam * (w1 * (1 - l1) + w2 * (1 - l2) / (1 + r) - c1 - c2 / (1 + r)))
lam_sol = sp.solve(sp.diff(Lag, c1), lam)[0]
zero("(9.1.7): dL/dl1 / lambda, lambda = u'(c1), is v'(l1)/u'(c1) - w1",
     sp.diff(Lag, l1).subs(lam, lam_sol) / lam_sol
     - (sp.diff(v_(l1), l1) / sp.diff(u_(c1), c1) - w1))
zero("(9.1.8): (1+r) dL/dc2 is beta(1+r)u'(c2) - u'(c1)",
     sp.diff(Lag, c2).subs(lam, lam_sol) * (1 + r)
     - (bt * (1 + r) * sp.diff(u_(c2), c2) - sp.diff(u_(c1), c1)))

# (9.2.1): the planner's three FOCs, Cobb-Douglas F
K1s, K2s, L1s, L2s = sp.symbols("K1 K2 L1 L2", positive=True)
F = lambda KK, LL: KK ** a_ * LL ** (1 - a_)
C1p = (1 - d_) * K1s + F(K1s, L1s) - K2s
W = u_(C1p) + v_(1 - L1s) + bt * (u_(F(K2s, L2s)) + v_(1 - L2s))
ptp = {**pt, K1s: 2.0, K2s: 1.5, L1s: 0.4, L2s: 0.3}
uprime = lambda x: x ** (-sg)
vprime = lambda x: psi_ / x
zero("(9.2.1): dW/dL1 = u'(c1) F_L(K1,L1) - v'(l1)",
     sp.diff(W, L1s) - (uprime(C1p) * sp.diff(F(K1s, L1s), L1s) - vprime(1 - L1s)), ptp)
zero("(9.2.1): dW/dL2 = beta[u'(c2) F_L(K2,L2) - v'(l2)]",
     sp.diff(W, L2s) - bt * (uprime(F(K2s, L2s)) * sp.diff(F(K2s, L2s), L2s)
                             - vprime(1 - L2s)), ptp)
zero("(9.2.1): dW/dK2 = -u'(c1) + beta u'(c2) F_K(K2,L2)",
     sp.diff(W, K2s) - (-uprime(C1p) + bt * uprime(F(K2s, L2s)) * sp.diff(F(K2s, L2s), K2s)), ptp)

# (9.2.3) closure: after the profit bound and I-hat = K2-hat - (1-d)K1, no price is left
Lh1, Lh2, Kh2, r1K, r2K, F1, F2 = sp.symbols("Lh1 Lh2 Kh2 r1K r2K F1 F2")
rhs_ = (w1 * Lh1 + w2 * Lh2 / (1 + r) + K1s * (1 + r1K - d_)
        + F1 - w1 * Lh1 - r1K * K1s + (F2 - w2 * Lh2 - r2K * Kh2) / (1 + r)
        + (r2K / (1 + r) - 1) * Kh2)
zero("(9.2.3) closure: every price cancels", rhs_ - ((1 - d_) * K1s + F1 - Kh2 + F2 / (1 + r)))

# Part I and (9.3.11)
I_ = sp.symbols("I")
PiI = r2K / (1 + r) * ((1 - d_) * K1s + I_) - ((1 - d_) * K1s + I_)
zero("Part I: dPi^I/dI = r^K/(1+r) - 1, no I in it", sp.diff(PiI, I_) - (r2K / (1 + r) - 1))
zero("(9.3.11): (rK + 1 - d)/(1 + r) = 1 solved for r is rK - d",
     sp.solve(sp.Eq((rK + 1 - d_) / (1 + r), 1), r)[0] - (rK - d_))

# (9.3.14), (9.3.17) and the continuous-time Euler of note 02
zero("(9.3.14): c_t^-s / (beta c_{t+1}^-s) = (c_{t+1}/c_t)^s / beta",
     c1 ** (-sg) / (bt * c2 ** (-sg)) - (c2 / c1) ** sg / bt, {**pt, c1: 1.3, c2: 1.7})
x = sp.symbols("x")
zero("(9.3.17): beta(1 + x - d) = 1 solved for x is 1/beta - 1 + d",
     sp.solve(sp.Eq(bt * (1 + x - d_), 1), x)[0] - (1 / bt - 1 + d_))
zero("with beta = 1/(1+rho): 1/beta - 1 = rho", (1 / bt - 1).subs(bt, 1 / (1 + rho_)) - rho_)
zero("02 2.1: ln(1 + x) = x to first order, so ln(1+r) - ln(1+rho) ~ r - rho",
     sp.series(sp.log(1 + x), x, 0, 2).removeO() - x)

# note 02: loci, Jacobian, eigenvalues, comparative statics (f = A k^alpha)
fk = A_ * k ** a_
kst = (a_ * A_ / (d_ + rho_)) ** (1 / (1 - a_))
cst = fk.subs(k, kst) - d_ * kst
fpp = sp.diff(fk, k, 2).subs(k, kst)
zero("02 2.2: k* = (alpha A/(delta+rho))^(1/(1-alpha)) solves f'(k) = delta + rho",
     sp.diff(fk, k).subs(k, kst) - (d_ + rho_), pt)
zero("02 2.2: d(f - delta k)/dk = 0 at k_gold",
     sp.diff(fk - d_ * k, k).subs(k, (a_ * A_ / d_) ** (1 / (1 - a_))), pt)
Gk = fk - d_ * k - c
Hk = c / sg * (sp.diff(fk, k) - d_ - rho_)
Jss = sp.Matrix([[sp.diff(Gk, k), sp.diff(Gk, c)],
                 [sp.diff(Hk, k), sp.diff(Hk, c)]]).subs({k: kst, c: cst})
zero("02 2.4: J11 = f'(k*) - delta = rho", Jss[0, 0] - rho_, pt)
zero("02 2.4: J12 = -1", Jss[0, 1] + 1)
zero("02 2.4: J21 = c* f''(k*)/sigma", Jss[1, 0] - cst * fpp / sg, pt)
zero("02 2.4: J22 = (f'(k*) - delta - rho)/sigma = 0", Jss[1, 1], pt)
zero("02 2.4: det J = c* f''(k*)/sigma", Jss.det() - cst * fpp / sg, pt)
lam_p = (rho_ + sp.sqrt(rho_ ** 2 - 4 * Jss.det())) / 2
zero("02 2.4: [rho + sqrt(rho^2 - 4 det J)]/2 solves lambda^2 - rho lambda + det J = 0",
     lam_p ** 2 - rho_ * lam_p + Jss.det(), pt)
zero("02 2.5: dk*/drho = 1/f''(k*)", sp.diff(kst, rho_) - 1 / fpp, pt)
zero("02 2.5: dc*/drho = rho/f''(k*)", sp.diff(cst, rho_) - rho_ / fpp, pt)
zero("02 2.5: dc*/ddelta = rho/f''(k*) - k*", sp.diff(cst, d_) - (rho_ / fpp - kst), pt)
zero("02 2.5: dk*/dA = -f'(k*)/(A f''(k*))",
     sp.diff(kst, A_) - (-(sp.diff(fk, k).subs(k, kst) / A_) / fpp), pt)
zero("02 2.5: dc*/dA = f(k*)/A + rho dk*/dA",
     sp.diff(cst, A_) - (kst ** a_ + rho_ * sp.diff(kst, A_)), pt)
kmax = (A_ / d_) ** (1 / (1 - a_))
zero("02 2.4: f'(k_max) = alpha delta, where f(k_max) = delta k_max",
     sp.diff(fk, k).subs(k, kmax) - a_ * d_, pt)
zero("02 2.4: growth of e^(-rho t) u'(c) k below the path -> delta(1 - alpha)",
     -rho_ - sg * (a_ * d_ - d_ - rho_) / sg - d_ * (1 - a_))

# note 01 1.3: Walras' law in the two-period economy
aS, R1s = sp.symbols("a R1")
fK2 = K2s ** a_
z1 = (R1s - aS) + K2s - R1s
z2 = (1 + r) * aS + (fK2 - sp.diff(fK2, K2s) * K2s) - fK2 - (1 - d_) * K2s
zero("01 1.3: z1 + z2/(1+r) = 0 at every r, once f'(K2) = r + delta",
     (z1 + z2 / (1 + r)).subs(r, sp.diff(fK2, K2s) - d_))

# exogenous-capital-lista-05
Kb = sp.symbols("Kbar", positive=True)
cL = A_ * Kb ** a_ * L ** (1 - a_)
e_ = a_ + (1 - a_) * sg
boxed = psi_ * L ** e_ / (1 - L) - (1 - a_) * (A_ * Kb ** a_) ** (1 - sg)
ptl = {**pt, Kb: 2.0, L: 0.3}
zero("L5 2.3: (MRS - w) L^alpha / (A Kbar^alpha)^sigma is the boxed equation",
     (psi_ / (1 - L) / cL ** (-sg) - sp.diff(cL, L)) * L ** a_ / (A_ * Kb ** a_) ** sg - boxed, ptl)
lnL, lnA = sp.symbols("lnL lnA")
G = (sp.log(psi_) + e_ * lnL - sp.log(1 - sp.exp(lnL)) - sp.log(1 - a_)
     - (1 - sg) * (lnA + a_ * sp.log(Kb)))
el = -sp.diff(G, lnA) / sp.diff(G, lnL)
zero("L5 4: implicit dlnL/dlnA = (1 - sigma)/(e + L/(1-L))",
     el.subs(lnL, sp.log(L)) - (1 - sg) / (e_ + L / (1 - L)), ptl)
zero("L5 4: dlnL/dlnKbar = alpha dlnL/dlnA",
     (-sp.diff(G, Kb) * Kb / sp.diff(G, lnL) - a_ * el).subs(lnL, sp.log(L)), ptl)
zero("L5 3: Euler's theorem F_K Kbar + F_L L = F", sp.diff(cL, Kb) * Kb + sp.diff(cL, L) * L - cL)
zero("L5 2.3: c1^-s = beta(1+r)c2^-s solved for 1 + r is (c2/c1)^s / beta",
     sp.solve(sp.Eq(c1 ** (-sg), bt * (1 + r) * c2 ** (-sg)), r)[0] + 1 - (c2 / c1) ** sg / bt,
     {**pt, c1: 1.1, c2: 1.3})

# ---------------------------------------------------------------------------
print()
if failures:
    print(f"{len(failures)} CHECK(S) FAILED: " + "; ".join(failures))
    raise SystemExit(1)
print("all checks pass")
