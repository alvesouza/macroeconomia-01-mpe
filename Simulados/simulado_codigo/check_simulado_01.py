#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical checks for Simulados/simulado-01.tex (answer key and every MC option).

Each block recomputes the numbers printed in the solutions, and for every multiple-choice
item evaluates each option so that exactly one is true. Run: python check_simulado_01.py
Exits non-zero if any check fails.
"""
from __future__ import annotations

import math

failures: list[str] = []


def check(name, got, want, tol=1e-6):
    ok = abs(float(got) - float(want)) <= tol
    print(f"  {'ok  ' if ok else 'FAIL'}  {name:<60} {float(got):+.6f}  (want {float(want):+.6f})")
    if not ok:
        failures.append(name)


def check_true(name, cond):
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}")
    if not cond:
        failures.append(name)


# =============================================================================
print("Block I, Q1(a): two goods X, Z")
p0, q0 = {"X": 10, "Z": 5}, {"X": 10, "Z": 20}
p1, q1 = {"X": 5, "Z": 10}, {"X": 20, "Z": 16}
val = lambda p, q: sum(p[g] * q[g] for g in p)
check("nominal Y0", val(p0, q0), 200)
check("nominal Y1", val(p1, q1), 260)
check("Y1 at year-0 prices", val(p0, q1), 280)
check("Y0 at year-1 prices", val(p1, q0), 250)
gL = val(p0, q1) / val(p0, q0) - 1
gP = val(p1, q1) / val(p1, q0) - 1
gF = math.sqrt((1 + gL) * (1 + gP)) - 1
check("growth at year-1 prices (key A: 40%)", gL, 0.40)
check("growth at year-2 prices (key A: 4%)", gP, 0.04)
check("distractor C: nominal growth 30%", val(p1, q1) / val(p0, q0) - 1, 0.30)
check("distractor E: Fisher 20.7%", round(gF, 3), 0.207, tol=1e-9)
check_true("relative price of X fell and quantities moved toward X",
           p1["X"] / p1["Z"] < p0["X"] / p0["Z"] and q1["X"] / q1["Z"] > q0["X"] / q0["Z"])
check_true("T/F (c) TRUE: initial-price growth exceeds final-price growth", gL > gP)

# =============================================================================
print("\nBlock I, Q2: soybeans (s) and smartphones (m)")
P0, Q0 = {"s": 10, "m": 20}, {"s": 60, "m": 20}
P1, Q1 = {"s": 12, "m": 12}, {"s": 60, "m": 40}
N0, N1 = 200.0, 210.0
Y0n, Y1n = val(P0, Q0), val(P1, Q1)
check("nominal 2015", Y0n, 1000)
check("nominal 2025", Y1n, 1200)
check("nominal growth", Y1n / Y0n - 1, 0.20)
check("2025 at 2015 prices", val(P0, Q1), 1400)
check("2015 at 2025 prices", val(P1, Q0), 960)
gL2 = val(P0, Q1) / Y0n - 1
gP2 = Y1n / val(P1, Q0) - 1
gF2 = math.sqrt((1 + gL2) * (1 + gP2)) - 1
check("growth, 2015 prices", gL2, 0.40)
check("growth, 2025 prices", gP2, 0.25)
check("Fisher growth", gF2, math.sqrt(1.75) - 1)
check("Fisher growth rounded 32.29%", round(gF2 * 100, 2), 32.29, tol=1e-9)
check("deflator 2025 (base 2015)", Y1n / val(P0, Q1), 6 / 7)
check("deflator 2015 (base 2025)", Y0n / val(P1, Q0), 1000 / 960)
check("relative price m/s 2015", P0["m"] / P0["s"], 2)
check("relative price m/s 2025", P1["m"] / P1["s"], 1)
check("population growth", N1 / N0 - 1, 0.05)
check("per capita, 2015 prices", (1 + gL2) / 1.05 - 1, 1 / 3)
check("per capita, 2025 prices", (1 + gP2) / 1.05 - 1, 1.25 / 1.05 - 1)
check("per capita, 2025 prices rounded 19.05%", round(((1 + gP2) / 1.05 - 1) * 100, 2), 19.05, tol=1e-9)
check("per capita Fisher rounded 25.99%", round(((1 + gF2) / 1.05 - 1) * 100, 2), 25.99, tol=1e-9)
check("real GDP per capita 2015 (thousand reais)", Y0n / N0, 5.0)
check("real GDP per capita 2025 at 2015 prices", val(P0, Q1) / N1, 20 / 3)

# =============================================================================
print("\nBlock II, Q3: Solow  s=0.24, A=1, alpha=1/3, n=0.01, delta=0.05")
s, A, al, n, d = 0.24, 1.0, 1 / 3, 0.01, 0.05
kss = (s * A / (n + d)) ** (1 / (1 - al))
check("k* (key C = 8)", kss, 8)
check("y* = 2 (distractor A: y instead of k)", A * kss ** al, 2)
check("distractor B: sA/(n+d) = 4, no exponent", s * A / (n + d), 4)
check("distractor D: forgetting n, 10.52", round((s * A / d) ** 1.5, 2), 10.52, tol=1e-9)
check("distractor E: exponent 1/alpha, 64", (s * A / (n + d)) ** (1 / al), 64)
css = lambda sv: (1 - sv) * A * ((sv * A / (n + d)) ** (1 / (1 - al))) ** al
check("golden-rule s = alpha", max((i / 1000 for i in range(1, 1000)), key=css), 0.333, tol=1e-9)
check_true("MC(b) key: c* at s_gold exceeds c* at s=0.24", css(1 / 3) > css(0.24))
check("c* at s=0.24", css(0.24), 0.76 * 2)
check("c* at s=1/3", css(1 / 3), (2 / 3) * (1 / 3 / 0.06) ** 0.5)
check_true("distractor E false: economy below golden rule, not dynamically inefficient", 0.24 < 1 / 3)
# T/F (d): lower n raises k*, transition growth of y positive, SS growth zero.
k_new = (s * A / (0.0 + d)) ** 1.5
check_true("T/F (d): lower n raises k*", k_new > kss)
k1 = ((1 - d) * kss + s * A * kss ** al) / (1 + 0.0)
check_true("...and y grows during transition (k rises from old k*)", k1 > kss)

# =============================================================================
print("\nBlock II, Q4: German reunification, alpha=1/2, delta=0.05")
al, d = 0.5, 0.05
AW, sW, nW, LW, kW = 2.0, 0.275, 0.0, 64.0, 121.0
AE, sE, nE, LE, kE = 1.0, 0.375, 0.025, 16.0, 16.0
KW, KE = kW * LW, kE * LE
check("K_W", KW, 7744)
check("K_E", KE, 256)
yW, yE = AW * kW ** al, AE * kE ** al
check("y_W,0", yW, 22)
check("y_E,0", yE, 4)
kWs = (sW * AW / (nW + d)) ** 2
kEs = (sE * AE / (nE + d)) ** 2
check("sA/(n+d) West", sW * AW / (nW + d), 11)
check("sA/(n+d) East", sE * AE / (nE + d), 5)
check("k*_W", kWs, 121)
check("k*_E", kEs, 25)
check("y*_W", AW * kWs ** al, 22)
check("y*_E", AE * kEs ** al, 5)
check("y*_E / y*_W", 5 / 22, 0.227272727)
kE1 = ((1 - d) * kE + sE * AE * kE ** al) / (1 + nE)
check("East k_1 (first-period step)", kE1, 16.7 / 1.025)
check_true("East grows in period 1", kE1 > kE)
check("East k_1 rounded 16.29", round(kE1, 2), 16.29, tol=1e-9)
check("East y_1 rounded 4.036", round(AE * kE1 ** al, 3), 4.036, tol=1e-9)
check("East y growth period 1 rounded 0.91%", round((AE * kE1 ** al / yE - 1) * 100, 2), 0.91, tol=1e-9)
kW1 = ((1 - d) * kW + sW * AW * kW ** al) / (1 + nW)
check("West stays at k*", kW1, 121)
# Unification
K, L = KW + KE, LW + LE
kU = K / L
check("K unified", K, 8000)
check("L unified", L, 80)
check("k_U", kU, 100)
yU = AW * kU ** al
check("y_U", yU, 20)
check("dy West", yU - yW, -2)
check("dy West %", (yU - yW) / yW, -1 / 11)
check("dy East", yU - yE, 16)
check("dy East %", (yU - yE) / yE, 4)
# decomposition of the East gain
check("East: technology first (A only, k=16)", AW * kE ** al, 8)
check("East: then capital deepening 8 -> 20", yU - AW * kE ** al, 12)
check("East: capital first (k=100, A=1)", AE * kU ** al, 10)
check("log decomposition ln5 = ln2 + 0.5 ln(100/16)",
      math.log(2) + 0.5 * math.log(100 / 16), math.log(5))
check("share of ln-gain from technology", math.log(2) / math.log(5), 0.430677, tol=1e-6)
YW0, YE0 = yW * LW, yE * LE
check("Y_W before", YW0, 1408)
check("Y_E before", YE0, 64)
check("Y before", YW0 + YE0, 1472)
check("Y after", yU * L, 1600)
check("dY", yU * L - (YW0 + YE0), 128)
check("dY %", yU * L / (YW0 + YE0) - 1, 128 / 1472)
check("dY % rounded 8.70", round((yU * L / (YW0 + YE0) - 1) * 100, 2), 8.70, tol=1e-9)
check("Germany-wide y before", (YW0 + YE0) / L, 18.4)
check("West capital per worker falls (dilution) 121 -> 100", kU - kW, -21)
wage = lambda A_, k_: (1 - al) * A_ * k_ ** al
rK = lambda A_, k_: al * A_ * k_ ** (al - 1)
check("w West before", wage(AW, kW), 11)
check("w East before", wage(AE, kE), 2)
check("w unified", wage(AW, kU), 10)
check("rK West before", rK(AW, kW), 1 / 11)
check("rK East before", rK(AE, kE), 0.125)
check("rK unified", rK(AW, kU), 0.1)
# Unified steady state
nU = (LW * nW + LE * nE) / L
check("n_U labour-weighted", nU, 0.005)
kUs = (sW * AW / (nU + d)) ** 2
check("sA/(n_U+d)", sW * AW / (nU + d), 10)
check("k*_U", kUs, 100)
check("y*_U", AW * kUs ** al, 20)
check_true("unified economy exactly at its SS", abs(kUs - kU) < 1e-9)
check("y*_U - y*_W", AW * kUs ** al - 22, -2)
check("break-even investment per unit k: West vs unified", (nU + d) - (nW + d), 0.005)

# =============================================================================
print("\nBlock III, Q5(a): labour supply, u = ln c + psi ln l, psi=1, w=10, T=2")
psi, w, T = 1.0, 10.0, 2.0
hours = lambda tau, T=T: 1 / (1 + psi) - psi * T / ((1 + psi) * (1 - tau) * w)


def hours_num(tau, T=T):
    """Brute-force check of the closed form: maximise over a fine grid of hours."""
    best, arg = -1e18, None
    for i in range(1, 200000):
        h = i / 200000
        c = (1 - tau) * w * h + T
        v = math.log(c) + psi * math.log(1 - h)
        if v > best:
            best, arg = v, h
    return arg


check("hours at tau=0.2 (key A: 0.375)", hours(0.2), 0.375)
check("hours at tau=0.5 (key A: 0.300)", hours(0.5), 0.300)
check("numeric optimum tau=0.2", hours_num(0.2), 0.375, tol=1e-5)
check("numeric optimum tau=0.5", hours_num(0.5), 0.300, tol=1e-5)
check("with T=0, hours = 1/2 at tau=0.2", hours(0.2, 0), 0.5)
check("with T=0, hours = 1/2 at tau=0.5 (distractor B false)", hours(0.5, 0), 0.5)
check_true("distractor D false: hours do not rise to 0.45", abs(hours(0.5) - 0.45) > 1e-3)

print("\nBlock III, Q5(b): matching m = mu V^a U^(1-a), one more vacancy")
mu, a, U, V = 0.5, 0.5, 100.0, 64.0
m = lambda V, U: mu * V ** a * U ** (1 - a)
f = lambda V: m(V, U) / U
q = lambda V: m(V, U) / V
check_true("f rises with V (workers gain)", f(V + 1) > f(V))
check_true("q falls with V (other firms lose)", q(V + 1) < q(V))
dm = m(V + 1e-6, U) - m(V, U)
check("dm/dV = a q < q (distractor D false)", dm / 1e-6, a * q(V), tol=1e-5)

print("\nBlock III, Q5(d): GE fixed K, u = ln c + psi ln l: hours independent of A")
Kbar, alK = 1.0, 1 / 3
Lstar = lambda A: (1 - alK) / (1 - alK + psi)


def L_numeric(A):
    """Bisection on MRS - MPL with c = Y (no investment, fixed capital)."""
    g = lambda L: psi * A * Kbar ** alK * L ** (1 - alK) / (1 - L) - (1 - alK) * A * Kbar ** alK * L ** (-alK)
    lo, hi = 1e-9, 1 - 1e-9
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        lo, hi = (lo, mid) if g(mid) > 0 else (mid, hi)
    return 0.5 * (lo + hi)


check("L at A=1", L_numeric(1.0), Lstar(1.0))
check("L at A=2 (same)", L_numeric(2.0), Lstar(2.0))
check("closed form (1-alpha)/(1-alpha+psi) at alpha=1/3,psi=1", Lstar(1), 0.4)

# =============================================================================
print("\nBlock III, Q6: two-period household with taxes")


def solve(y1, y2, t1, t2, r, beta, sig, b=None):
    """Closed form; if b is given and the unconstrained a < -b, impose a = -b."""
    D = 1 + beta ** (1 / sig) * (1 + r) ** (1 / sig - 1)
    W = y1 - t1 + (y2 - t2) / (1 + r)
    c1 = W / D
    a = y1 - t1 - c1
    if b is not None and a < -b:
        a = -b
        c1 = y1 - t1 + b
    c2 = y2 - t2 + (1 + r) * a
    return c1, c2, a


y1, y2, t1, t2, r, beta = 60.0, 150.0, 20.0, 20.0, 0.25, 0.8
c1, c2, a = solve(y1, y2, t1, t2, r, beta, 1.0)
check("beta(1+r)", beta * (1 + r), 1.0)
check("D (sigma=1) = 1+beta", 1 + beta, 1.8)
check("W", y1 - t1 + (y2 - t2) / (1 + r), 144)
check("c1 baseline", c1, 80)
check("c2 baseline", c2, 80)
check("a baseline", a, -40)
check("Euler residual baseline", 1 / c1 - beta * (1 + r) / c2, 0)
# brute-force: maximise ln c1 + beta ln c2 over c1
best = max((i / 1000 for i in range(1, 143999)),
           key=lambda x: math.log(x) + beta * math.log((1 + r) * (144 - x)))
check("numeric c1 by grid", best, 80, tol=1e-3)
for sig in (0.5, 2.0):
    c1s, c2s, _ = solve(y1, y2, t1, t2, r, beta, sig)
    check(f"Euler holds sigma={sig}", c1s ** -sig - beta * (1 + r) * c2s ** -sig, 0, tol=1e-10)
    check(f"PV constraint holds sigma={sig}", c1s + c2s / (1 + r), 144, tol=1e-9)

# (b) sign of dc1/dr with y2 = tau = 0
def dc1dr(sig, y=100.0, r=0.25, beta=0.8, h=1e-6):
    c = lambda rr: solve(y, 0, 0, 0, rr, beta, sig)[0]
    return (c(r + h) - c(r - h)) / (2 * h)


def dc1dr_formula(sig, y=100.0, r=0.25, beta=0.8):
    D = 1 + beta ** (1 / sig) * (1 + r) ** (1 / sig - 1)
    return -y * beta ** (1 / sig) * ((1 - sig) / sig) * (1 + r) ** (1 / sig - 2) / D ** 2


for sig in (0.5, 1.0, 2.0):
    check(f"dc1/dr formula vs numeric sigma={sig}", dc1dr_formula(sig), dc1dr(sig), tol=1e-5)
check_true("sigma>1 => c1 rises with r", dc1dr(2.0) > 0)
check_true("sigma<1 => c1 falls with r", dc1dr(0.5) < 0)
check("sigma=1 => zero", dc1dr(1.0), 0, tol=1e-6)

# (c) Ricardian swap Delta = 10
Dl = 10.0
c1n, c2n, an = solve(y1, y2, t1 - Dl, t2 + (1 + r) * Dl, r, beta, 1.0)
check("tau2 after swap", t2 + (1 + r) * Dl, 32.5)
check("c1 unchanged", c1n, 80)
check("c2 unchanged", c2n, 80)
check("a rises by Delta", an - a, Dl)
check("a after swap", an, -30)
check("PV of taxes unchanged", (t1 - Dl) + (t2 + (1 + r) * Dl) / (1 + r), t1 + t2 / (1 + r))
check("PV of taxes = 36", t1 + t2 / (1 + r), 36)
# borrowing limit b = 20
bb = 20.0
c1b, c2b, ab = solve(y1, y2, t1, t2, r, beta, 1.0, b=bb)
check("constrained c1 before", c1b, 60)
check("constrained c2 before", c2b, 105)
check("constrained a before", ab, -20)
check_true("Euler inequality at kink: u'(c1) > beta(1+r)u'(c2)", 1 / c1b > beta * (1 + r) / c2b)
c1bn, c2bn, abn = solve(y1, y2, t1 - Dl, t2 + (1 + r) * Dl, r, beta, 1.0, b=bb)
check("constrained c1 after", c1bn, 70)
check("constrained c2 after", c2bn, 92.5)
check("dc1 constrained = Delta (MPC 1)", c1bn - c1b, Dl)
check("dc2 constrained = -(1+r)Delta", c2bn - c2b, -(1 + r) * Dl)
check_true("still binding after swap (desired a=-30 < -20)", an < -bb)
check("largest Delta keeping the limit binding (desired a = -40 + Delta < -20)", -a - bb, 20)

# =============================================================================
print("\nBlock IV, Q7(b): pi = mu - eta g")
pistar, g = 0.03, 0.02
mu_cb = pistar + 1.0 * g
check("mu chosen with eta=1", mu_cb, 0.05)
check("actual inflation with eta=1/2 (key C: 4%)", mu_cb - 0.5 * g, 0.04)
check("distractor E: sign error mu + eta g", mu_cb + 0.5 * g, 0.06)
check("distractor A: 2%", pistar - 0.5 * g, 0.02)

# =============================================================================
print("\nBlock IV, Q8: Baumol-Tobin with falling F")
mD = lambda F, Y, i: math.sqrt(F * Y / (2 * i))
Vf = lambda F, Y, i: Y / mD(F, Y, i)
F0, Y0, i0 = 2.0, 1000.0, 0.10
check("V = sqrt(2iY/F)", Vf(F0, Y0, i0), math.sqrt(2 * i0 * Y0 / F0))
check("dlnV/dlnF = -1/2", (math.log(Vf(F0 * 1.001, Y0, i0)) - math.log(Vf(F0, Y0, i0))) / math.log(1.001), -0.5)
check("dlnV/dlnY = +1/2", (math.log(Vf(F0, Y0 * 1.001, i0)) - math.log(Vf(F0, Y0, i0))) / math.log(1.001), 0.5)
check("dlnV/dlni = +1/2", (math.log(Vf(F0, Y0, i0 * 1.001)) - math.log(Vf(F0, Y0, i0))) / math.log(1.001), 0.5)
gg, ff = 0.02, -0.04
check("growth of V = (g - f)/2", 0.5 * (gg - ff), 0.03)
check("growth of m^D = (g + f)/2", 0.5 * (gg + ff), -0.01)
# continuous-time simulation: M grows at mu, p = M / m^D, measure pi
mu_new = 0.03 + 0.5 * (gg + ff)
check("mu hitting 3% with Pix", mu_new, 0.02)
check("mu before Pix (f=0)", 0.03 + 0.5 * gg, 0.04)
check("pi if mu kept at 4%", 0.04 - 0.5 * (gg + ff), 0.05)
t = 5.0
lnp = lambda tt, mu: mu * tt - math.log(mD(F0 * math.exp(ff * tt), Y0 * math.exp(gg * tt), i0))
check("simulated pi, mu=2%", (lnp(t + 1e-4, 0.02) - lnp(t, 0.02)) / 1e-4, 0.03, tol=1e-8)
check("simulated pi, mu=4%", (lnp(t + 1e-4, 0.04) - lnp(t, 0.04)) / 1e-4, 0.05, tol=1e-8)
# (c) i-target: M endogenous, grows at pi + (g+f)/2
check("M growth under i-target with pi=3%", 0.03 + 0.5 * (gg + ff), 0.02)
check("level drop in m^D on impact if F halves", mD(F0 / 2, Y0, i0) / mD(F0, Y0, i0), 1 / math.sqrt(2))

print()
if failures:
    print(f"{len(failures)} CHECK(S) FAILED: " + "; ".join(failures))
    raise SystemExit(1)
print("all checks pass")
