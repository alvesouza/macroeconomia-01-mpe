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
  symbolic                   every intermediate step written out in notes 01-05 (sympy,
                             numeric fallback at random points)
  companion-unification      Lista 2 Q1 read-outs at three control vectors (landmarks at the
                             list's values); unify() mirrors the page's JS model()

Stdlib + numpy + sympy (the symbolic step checks). Run: python Map/aula-02-solow-mecanica/check_solow.py
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
print("\ncompanion-unification -- Lista 2 Q1")
FIXED = dict(LN=10, LS=20, KS0=8000, aN=0.25, AN=4, aS=0.5, AS=5)
UNIFY_DEFAULTS = dict(sN=0.16, sS=0.30, nN=0.03, nS=0.01, delta=0.05, KN0=100)


def unify(sN, sS, nN, nS, delta, KN0, T=100):
    """Every read-out of companion-unification.html, same names as its JS model().

    sN, sS, nN, nS: saving and labour-growth rates; delta: common depreciation; KN0: North's
    initial capital. Other parameters are the list's fixed values (FIXED). T: path length.
    """
    P = FIXED
    fy = lambda A, a, k: A * k ** a
    kss_ = lambda s, A, a, n: (s * A / (n + delta)) ** (1 / (1 - a))
    L = P["LN"] + P["LS"]
    r = dict(kN0=KN0 / P["LN"], kS0=P["KS0"] / P["LS"], kU=(KN0 + P["KS0"]) / L)
    r["yN0"] = fy(P["AN"], P["aN"], r["kN0"])
    r["yS0"] = fy(P["AS"], P["aS"], r["kS0"])
    r["yU"] = fy(P["AS"], P["aS"], r["kU"])
    r["kssN"] = kss_(sN, P["AN"], P["aN"], nN)
    r["yssN"] = fy(P["AN"], P["aN"], r["kssN"])
    r["kssS"] = kss_(sS, P["AS"], P["aS"], nS)
    r["yssS"] = fy(P["AS"], P["aS"], r["kssS"])
    r["Ysep"] = P["LN"] * r["yN0"] + P["LS"] * r["yS0"]
    r["YU"] = L * r["yU"]
    r["gainN"] = P["LN"] * (r["yU"] - r["yN0"])
    r["gainS"] = P["LS"] * (r["yU"] - r["yS0"])
    r["nU"] = (P["LN"] * nN + P["LS"] * nS) / L
    r["kssU"] = kss_(sS, P["AS"], P["aS"], r["nU"])
    r["yssU"] = fy(P["AS"], P["aS"], r["kssU"])
    r["mpkNonS"] = P["aS"] * P["AS"] * r["kN0"] ** (P["aS"] - 1)
    r["mpkS0"] = P["aS"] * P["AS"] * r["kS0"] ** (P["aS"] - 1)
    # Exact difference equation, T periods, same as the page's chart.
    step = lambda k, s, A, a, n: ((1 - delta) * k + s * fy(A, a, k)) / (1 + n)
    kN, kS, kU = r["kN0"], r["kS0"], r["kU"]
    for _ in range(T):
        kN = step(kN, sN, P["AN"], P["aN"], nN)
        kS = step(kS, sS, P["AS"], P["aS"], nS)
        kU = step(kU, sS, P["AS"], P["aS"], r["nU"])
    r["yN_T"], r["yS_T"], r["yU_T"] = (fy(P["AN"], P["aN"], kN), fy(P["AS"], P["aS"], kS),
                                       fy(P["AS"], P["aS"], kU))
    return r


UNIFY_VECTORS = [UNIFY_DEFAULTS,
                 dict(sN=0.25, sS=0.20, nN=0.01, nS=0.02, delta=0.08, KN0=500),
                 dict(sN=0.10, sS=0.40, nN=0.05, nS=0.00, delta=0.03, KN0=5000)]

u = unify(**UNIFY_DEFAULTS)
for key, want, tol in [("kN0", 10, 1e-12), ("yN0", 7.113, 5e-4), ("kS0", 400, 1e-12),
                       ("yS0", 100, 1e-9), ("kssN", 16, 1e-9), ("yssN", 8, 1e-9),
                       ("kssS", 625, 1e-9), ("yssS", 125, 1e-9), ("kU", 270, 1e-9),
                       ("yU", 82.16, 5e-3), ("YU", 2464.75, 5e-3), ("Ysep", 2071.13, 5e-3),
                       ("nU", 1 / 60, 1e-12), ("kssU", 506.25, 1e-8), ("yssU", 112.5, 1e-9)]:
    check(f"defaults: {key}", u[key], want, tol=tol)
check_true("defaults: both start below their own SS (conditional convergence, both grow)",
           u["kN0"] < u["kssN"] and u["kS0"] < u["kssS"])
check_true("defaults: North gains, South loses per worker", u["yU"] > u["yN0"] and u["yU"] < u["yS0"])
check_true("defaults: aggregate Y rises", u["YU"] > u["Ysep"])
check_true("defaults: moved capital is more productive North (MPK)", u["mpkNonS"] > u["mpkS0"])
check_true("defaults: unified economy starts below k*_U", u["kU"] < u["kssU"])
check_true("defaults: y*_U < y*_S because n_U > n_S", u["yssU"] < u["yssS"] and u["nU"] > 0.01)

for i, vec in enumerate(UNIFY_VECTORS):
    u = unify(**vec)
    tag = f"v{i}"
    for side, s_, A_, a_, n_ in [("N", vec["sN"], 4, 0.25, vec["nN"]),
                                 ("S", vec["sS"], 5, 0.5, vec["nS"]),
                                 ("U", vec["sS"], 5, 0.5, u["nU"])]:
        k_ = u["kss" + side]
        check(f"{tag}: SS condition (n+delta)k* = sAk*^a, {side}",
              (n_ + vec["delta"]) * k_, s_ * A_ * k_ ** a_, tol=1e-9 * max(1, k_))
    check(f"{tag}: Y_U - (Y_N+Y_S) = North part + South part",
          u["YU"] - u["Ysep"], u["gainN"] + u["gainS"], tol=1e-9)
    u_long = unify(**vec, T=5000)
    for side in "NSU":
        check(f"{tag}: exact path converges to y*_{side}", u_long[f"y{side}_T"], u[f"yss{side}"], tol=1e-6)
    print("    " + ", ".join(f"{k}={u[k]:.6f}" for k in
                            ("kN0", "yN0", "kssN", "yssN", "kS0", "yS0", "kssS", "yssS", "kU", "yU",
                             "Ysep", "YU", "gainN", "gainS", "nU", "kssU", "yssU", "mpkNonS",
                             "mpkS0", "yN_T", "yS_T", "yU_T")))

# ---------------------------------------------------------------------------
print("\nsymbolic -- every intermediate step inserted in the notes (sympy)")
import sympy as sp

a_, s_, n_, d_, K_, L_, k_, lam_ = sp.symbols("alpha s n delta K L k lambda", positive=True)
Ks, Ls = sp.symbols("K_t L_t", positive=True)


def same(name, lhs, rhs):
    """Pass if lhs - rhs simplifies to 0, else if it vanishes at 20 random points.

    sympy cannot always simplify symbolic exponents like (s/(d+n))**(1/(1-a)); the numeric
    fallback draws every free symbol from (0.05, 0.9), so alpha stays inside (0, 1).
    """
    diff = lhs - rhs
    if sp.simplify(sp.expand_power_base(sp.expand(diff), force=True)) == 0:
        check_true(name, True)
        return
    rng = np.random.default_rng(0)
    syms = sorted(diff.free_symbols, key=str)
    fn = sp.lambdify(syms, diff, "math")
    ok = all(abs(fn(*rng.uniform(0.05, 0.9, len(syms)))) < 1e-9 for _ in range(20))
    check_true(name + " (numeric, 20 random points)", ok)


# 01: (1+g)^216 = 27 solved line by line; g vs its log approximation.
g27 = math.exp(math.log(27) / 216) - 1
check("01: g = e^(ln27/216) - 1", g27, 0.01538, tol=1e-5)
check_true("01: (1+g)^216 == 27", abs((1 + g27) ** 216 - 27) < 1e-9)
check("01: 0.35/3.2", 0.35 / 3.2, 0.109375)

# 02: Cobb-Douglas partials, second partials, Inada rewrite, Euler via d/dlambda.
Fs = K_ ** a_ * L_ ** (1 - a_)
same("02: F_K = alpha Y/K", sp.diff(Fs, K_), a_ * Fs / K_)
same("02: F_L = (1-alpha) Y/L", sp.diff(Fs, L_), (1 - a_) * Fs / L_)
same("02: F_LL = -alpha(1-alpha) K^a L^(-a-1)", sp.diff(Fs, L_, 2),
     -a_ * (1 - a_) * K_ ** a_ * L_ ** (-a_ - 1))
same("02: K^(a-1) L^(1-a) = (K/L)^(a-1)", K_ ** (a_ - 1) * L_ ** (1 - a_), (K_ / L_) ** (a_ - 1))
lmb = sp.symbols("lambda_", positive=True)
Kx, Lx = sp.symbols("Kx Lx", positive=True)
Fgen = sp.Function("F")
dlhs = sp.diff(Fgen(lmb * Kx, lmb * Lx), lmb).subs(lmb, 1).doit()
check_true("02: d/dlambda F(lam K, lam L) at lam=1 is F_K K + F_L L (chain rule)",
           sp.simplify(dlhs - (Kx * sp.Subs(sp.diff(Fgen(K_, Lx), K_), K_, Kx).doit()
                               + Lx * sp.Subs(sp.diff(Fgen(Kx, L_), L_), L_, Lx).doit())) == 0)
same("02: Euler for Cobb-Douglas", sp.diff(Fs, K_) * K_ + sp.diff(Fs, L_) * L_, Fs)
fk = k_ ** a_
w_pw = fk - sp.diff(fk, k_) * k_
same("02: per-worker wage f - f'k = (1-alpha) y", w_pw, (1 - a_) * fk)
same("02: F_K(K,L) = f'(K/L) (degree-zero)", sp.diff(Fs, K_), sp.diff(fk, k_).subs(k_, K_ / L_))

# 03: exact law step by step; common denominator; error factor; quotient rule.
ff = sp.Function("f")
kt = Ks / Ls
chain_start = ((1 - d_) * Ks + s_ * Ls * ff(kt)) / ((1 + n_) * Ls) - kt
same("03: [(1-d)K + sY]/L_{t+1} - k == [(1-d)k + s f(k)]/(1+n) - k",
     chain_start, ((1 - d_) * kt + s_ * ff(kt)) / (1 + n_) - kt)
same("03: common denominator gives [s f - (d+n) k]/(1+n)",
     ((1 - d_) * k_ + s_ * ff(k_)) / (1 + n_) - k_, (s_ * ff(k_) - (d_ + n_) * k_) / (1 + n_))
same("03: 1 - 1/(1+n) = n/(1+n)", 1 - 1 / (1 + n_), n_ / (1 + n_))
t_ = sp.symbols("t")
Kf, Lf = sp.Function("K")(t_), sp.Function("L")(t_)
kdot_sym = sp.diff(Kf / Lf, t_)
same("03: quotient rule: d(K/L)/dt = Kdot/L - (K/L)(Ldot/L)",
     kdot_sym, sp.diff(Kf, t_) / Lf - (Kf / Lf) * sp.diff(Lf, t_) / Lf)
kf = sp.Function("k")(t_)
same("03: d ln(k^a)/dt = alpha kdot/k", sp.diff(sp.log(kf ** a_), t_).simplify(),
     a_ * sp.diff(kf, t_) / kf)

# 04: closed form, elasticity, phi'(k_ss), G'(k_ss), f'(k)k - f(k) for CD.
kss_s = (s_ / (d_ + n_)) ** (1 / (1 - a_))
same("04: s k_ss^a == (d+n) k_ss", s_ * kss_s ** a_, (d_ + n_) * kss_s)
same("04: y_ss exponent a/(1-a)", kss_s ** a_, (s_ / (d_ + n_)) ** (a_ / (1 - a_)))
same("04: d ln y_ss / d ln s = a/(1-a)",
     sp.diff(sp.log((sp.exp(sp.Symbol("x")) / (d_ + n_)) ** (a_ / (1 - a_))),
             sp.Symbol("x")), a_ / (1 - a_))
same("04: f'(k)k - f(k) = -(1-a) k^a", sp.diff(fk, k_) * k_ - fk, -(1 - a_) * fk)
phi_p = (s_ * sp.diff(fk, k_) - (d_ + n_)).subs(k_, kss_s)
same("04: phi'(k_ss) = -(1-a)(d+n)", phi_p, -(1 - a_) * (d_ + n_))
same("04: s f'(k_ss) = a (d+n)", (s_ * sp.diff(fk, k_)).subs(k_, kss_s), a_ * (d_ + n_))
k0s, tt_ = sp.symbols("k0 tt", positive=True)
ksol = kss_s + (k0s - kss_s) * sp.exp(-lam_ * tt_)
same("04: k_t - k_ss = (k0 - k_ss) e^(-lam t) solves kdot = -lam (k - k_ss)",
     sp.diff(ksol, tt_), -lam_ * (ksol - kss_s))
check("04: half-life ln2/0.04", math.log(2) / 0.04, 17.33, tol=5e-3)

# 05: implicit derivative, elasticity cross-check, peak growth, dc/ds for general f.
dk_ds = sp.diff(kss_s, s_)
same("05: dk_ss/ds = f/((1-a)(d+n))", dk_ds, kss_s ** a_ / ((1 - a_) * (d_ + n_)))
same("05: elasticity (dk/ds)(s/k) = 1/(1-a)", dk_ds * s_ / kss_s, 1 / (1 - a_))
s0_, s1_ = sp.symbols("s0 s1", positive=True)
k_old = (s0_ / (d_ + n_)) ** (1 / (1 - a_))
peak = a_ * (s1_ * k_old ** a_ / k_old - (d_ + n_))
same("05: peak growth = a(d+n)(s1-s0)/s0", peak, a_ * (d_ + n_) * (s1_ - s0_) / s0_)
check("05: peak at the baseline", ALPHA * 0.06 * 0.05 / 0.20, 0.005)
check("05: linearised peak a*lam*(1.25^1.5-1)", ALPHA * 0.04 * (1.25 ** 1.5 - 1), 0.0053, tol=1e-4)
check("05: two half-lives", 2 * math.log(2) / 0.04, 34.66, tol=5e-3)
Fv, Fp = sp.symbols("f fp", positive=True)
dcds = -Fv + (1 - s_) * Fp * Fv / ((d_ + n_) - s_ * Fp)
same("05: dc_ss/ds = f[f' - (d+n)]/((d+n) - s f')", dcds,
     Fv * (Fp - (d_ + n_)) / ((d_ + n_) - s_ * Fp))
c_s = (1 - s_) * kss_s ** a_
same("05: dc_ss/ds matches the general formula for Cobb-Douglas", sp.diff(c_s, s_),
     dcds.subs({Fv: kss_s ** a_, Fp: a_ * kss_s ** (a_ - 1)}))
same("05: log level gain: ln(s1/(d+n)) - ln(s0/(d+n)) = ln(s1/s0)",
     sp.expand_log(sp.log(s1_ / (d_ + n_)) - sp.log(s0_ / (d_ + n_)), force=True),
     sp.expand_log(sp.log(s1_ / s0_), force=True))
check("05: regression coefficient (1-e^(-lam T))/T at T=50",
      (1 - math.exp(-0.04 * 50)) / 50, 0.0173, tol=1e-4)

# ---------------------------------------------------------------------------
print()
if failures:
    print(f"{len(failures)} CHECK(S) FAILED: " + "; ".join(failures))
    raise SystemExit(1)
print("all checks pass")
