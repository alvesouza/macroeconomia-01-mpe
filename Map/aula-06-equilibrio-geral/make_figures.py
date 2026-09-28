#!/usr/bin/env python3
"""Figures for the Aula 6 notes (Kurlat ch. 9) and the two Map/ files that belong to it.

Writes SVGs to Map/aula-06-equilibrio-geral/fig/. Parameters are the ones check_ge.py uses
(alpha 0.35, delta 0.06, rho 0.03, sigma 2; two-period economy with K1 = 2), and every
number drawn is recomputed here and asserted against a closed form before plotting.

Run: python Map/aula-06-equilibrio-geral/make_figures.py [PNG_PREVIEW_DIR]
With a directory argument every figure is also written there as PNG, for eyeballing.
"""
from __future__ import annotations

import math
import pathlib
import sys
from types import SimpleNamespace

import numpy as np
from matplotlib.figure import Figure
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "fig"))
from mapstyle import S, INK, INK2, SURF, save  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

OUT = pathlib.Path(__file__).resolve().parent / "fig"

if len(sys.argv) > 1:
    PNG = pathlib.Path(sys.argv[1])
    PNG.mkdir(parents=True, exist_ok=True)
    _svg_save = Figure.savefig

    def _both(self, path, **kw):
        _svg_save(self, path, **kw)
        _svg_save(self, PNG / (pathlib.Path(path).stem + ".png"), format="png", dpi=110)

    Figure.savefig = _both

ALPHA, DELTA, RHO, SIGMA = 0.35, 0.06, 0.03, 2.0
BETA = 1 / (1 + RHO)


def f(k, a=ALPHA):
    return k ** a


def fp(k, a=ALPHA):
    return a * k ** (a - 1)


def dot(ax, x, y, col, label, dx=8, dy=6, ha="left"):
    """Mark (x, y) with a ringed dot and a value label offset by (dx, dy) points."""
    ax.plot(x, y, "o", ms=7, color=col, mec=SURF, mew=2, zorder=5)
    ax.annotate(label, (x, y), xytext=(dx, dy), textcoords="offset points",
                color=INK, fontsize=8.5, ha=ha)


# =====================================================================================
# 01-equilibrium-as-benchmark: the two-period economy of check_ge.py
# =====================================================================================
K1 = 2.0
R1 = f(K1) + (1 - DELTA) * K1


def u(c):
    return c ** (1 - SIGMA) / (1 - SIGMA)


def k2_demand(r):
    """Producing firm: f'(K2) = r + delta."""
    return (ALPHA / (r + DELTA)) ** (1 / (1 - ALPHA))


def household(r):
    """C1, C2 at interest r, with the period-2 wage bill pi2 set by the firm's K2 demand."""
    K = k2_demand(r)
    pi2 = f(K) - fp(K) * K
    wealth = R1 + pi2 / (1 + r)
    g = (BETA * (1 + r)) ** (1 / SIGMA)          # Euler: C2 = g C1
    C1 = wealth / (1 + g / (1 + r))
    return C1, g * C1, K, pi2


def z_goods(r):
    """Excess demand in the period-1 goods market, and period-2's in present value."""
    C1, C2, K, _ = household(r)
    return C1 + K - R1, (C2 - f(K) - (1 - DELTA) * K) / (1 + r)


r_eq = brentq(lambda r: z_goods(r)[0], 0.0, 1.0)
C1e, C2e, K2e, pi2e = household(r_eq)
K2p = brentq(lambda K: -(R1 - K) ** -SIGMA
             + BETA * (f(K) + (1 - DELTA) * K) ** -SIGMA * (fp(K) + 1 - DELTA), 0.01, R1 - 0.01)
assert math.isclose(K2e, K2p, rel_tol=1e-8), "first welfare theorem: market K2 = planner K2"
assert math.isclose(C1e, R1 - K2p, rel_tol=1e-8)
U_star = u(C1e) + BETA * u(C2e)


def ppf(C1):
    K = R1 - C1
    return f(K) + (1 - DELTA) * K


def budget(C1):
    return (1 + r_eq) * (R1 - C1) + pi2e


def indiff(C1):
    return ((U_star - u(C1)) / BETA * (1 - SIGMA)) ** (1 / (1 - SIGMA))


assert math.isclose(ppf(C1e), C2e, rel_tol=1e-9) and math.isclose(budget(C1e), C2e, rel_tol=1e-9)
mrt = fp(K2e) + 1 - DELTA
mrs = C1e ** -SIGMA / (BETA * C2e ** -SIGMA)
assert math.isclose(mrs, 1 + r_eq, rel_tol=1e-8) and math.isclose(mrt, 1 + r_eq, rel_tol=1e-8)

# a preferred allocation x-hat: more C2 at the same C1
xh = (C1e, 1.07 * C2e)
assert u(xh[0]) + BETA * u(xh[1]) > U_star          # preferred
assert xh[1] > budget(xh[0])                        # so unaffordable
assert xh[1] > ppf(xh[0])                           # so infeasible

C1g = np.linspace(1.3, 2.6, 300)
fig, ax = plt.subplots(figsize=(6.6, 4.2))
ax.plot(C1g, ppf(C1g), color=S[0], label="technology: C₂ = f(R₁ − C₁) + (1 − δ)(R₁ − C₁)")
ax.plot(C1g, budget(C1g), color=S[1], label=f"budget line at the market price, slope −(1 + r) = −{1 + r_eq:.3f}")
ic = indiff(C1g)
ax.plot(C1g[ic < 2.9], ic[ic < 2.9], color=S[2], label="indifference curve through the equilibrium")
dot(ax, C1e, C2e, INK, f"market = planner\n(C₁, C₂) = ({C1e:.3f}, {C2e:.3f})", dx=-10, dy=-30, ha="right")
dot(ax, *xh, S[4], "x̂: preferred ⇒ above the budget\nline ⇒ outside technology", dx=8, dy=2)
ax.set_xlim(1.3, 2.6)
ax.set_ylim(1.3, 2.9)
ax.set_xlabel("period-1 consumption C₁ (goods)")
ax.set_ylabel("period-2 consumption C₂ (goods)")
ax.set_title(f"MRS = 1 + r = MRT = {1 + r_eq:.3f}: the price is only the common slope",
             loc="left", fontsize=10.5)
ax.legend(fontsize=8, loc="lower left")
save(fig, OUT / "fig_ge_tangency.svg")

# ---------- Walras' law: the two goods markets mirror each other at every r ----------
rg = np.linspace(0.05, 0.45, 300)
z1, z2 = np.array([z_goods(r) for r in rg]).T
assert np.max(np.abs(z1 + z2)) < 1e-12, "Walras: z1 + z2/(1+r) = 0 at every r"
fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.plot(rg * 100, z1, color=S[0], label="period-1 goods: C₁ + K₂ − R₁")
ax.plot(rg * 100, z2, color=S[1], label="period-2 goods, in present value: [C₂ − Y₂ − (1 − δ)K₂]/(1 + r)")
ax.plot(rg * 100, z1 + z2, color=INK2, linestyle="--", linewidth=1.2,
        label="their sum: zero at every r, not only at r*")
dot(ax, r_eq * 100, 0.0, INK, f"r* = {r_eq * 100:.2f}%: both clear", dx=8, dy=10)
ax.set_xlabel("real interest rate r (%)")
ax.set_ylabel("excess demand (goods)")
ax.set_title("Walras' law: clear one goods market and the other clears for free",
             loc="left", fontsize=10.5)
ax.legend(fontsize=8, loc="upper right")
save(fig, OUT / "fig_ge_walras.svg")

# =====================================================================================
# 02-dynamics-and-saddle-path
# =====================================================================================


def steady(rho=RHO, a=ALPHA, d=DELTA, A=1.0):
    k = (a * A / (d + rho)) ** (1 / (1 - a))
    return k, A * f(k, a) - d * k


k_star, c_star = steady()
k_gold = (ALPHA / DELTA) ** (1 / (1 - ALPHA))
k_max = (1 / DELTA) ** (1 / (1 - ALPHA))          # f(k) = delta k: c = 0 on the hump
assert math.isclose(fp(k_star), DELTA + RHO) and math.isclose(fp(k_gold), DELTA)
assert k_star < k_gold < k_max and math.isclose(f(k_max), DELTA * k_max)


def rhs(t, y, rho=RHO):
    k, c = y
    return [f(k) - DELTA * k - c, c / SIGMA * (fp(k) - DELTA - rho)]


def saddle_branch(rho=RHO, side=-1, T=400):
    """Stable arm through the steady state, integrated backward from a nudge along the
    stable eigenvector. side=-1 gives the branch with k < k*."""
    ks, cs = steady(rho)
    J = np.array([[fp(ks) - DELTA, -1.0],
                  [cs / SIGMA * ALPHA * (ALPHA - 1) * ks ** (ALPHA - 2), 0.0]])
    lam, vec = np.linalg.eig(J)
    v = vec[:, np.argmin(lam)]
    v = v * np.sign(v[0]) * side
    y0 = np.array([ks, cs]) + 1e-6 * v
    stop = lambda t, y, *a: y[0] - 0.02
    stop.terminal = True
    sol = solve_ivp(rhs, [0, -T], y0, args=(rho,), events=stop, rtol=1e-10, atol=1e-12,
                    max_step=0.5)
    return sol.y[0][::-1], sol.y[1][::-1], sol.t[::-1] - sol.t[-1]


sk, sc, st = saddle_branch()
k0 = 0.4 * k_star
c0 = float(np.interp(k0, sk, sc))


def forward(c_init, T, rho=RHO):
    hit0 = lambda t, y, *a: y[0] - 1e-4
    hit0.terminal = True
    return solve_ivp(rhs, [0, T], [k0, c_init], args=(rho,), events=hit0, rtol=1e-10,
                     atol=1e-12, dense_output=True, max_step=0.25)


# The saddle path as a time series: the backward solution read forward from k0, because
# forward integration of an unstable system cannot stay on the knife-edge.
m = sk >= k0
on = SimpleNamespace(t=np.append(st[m] - st[m][0], 400.0),
                     y=np.array([np.append(sk[m], k_star), np.append(sc[m], c_star)]))
hi = forward(1.05 * c0, 400)
lo = forward(0.95 * c0, 400)
assert abs(on.y[0][-2] - k_star) / k_star < 1e-4, "the saddle path converges"
assert hi.status == 1, "c0 above the path: k reaches zero in finite time"
t_crash = float(hi.t_events[0][0])
assert lo.y[0][-1] > k_gold and lo.y[1][-1] < 0.05 * c_star, "c0 below: c -> 0, k -> k_max"

# the transversality term e^{-rho t} u'(c) k; below the path it grows at delta(1 - alpha)
tv = lambda s: np.exp(-RHO * s.t) * s.y[1] ** -SIGMA * s.y[0]
tail = lo.t > 300
slope = np.polyfit(lo.t[tail], np.log(tv(lo)[tail]), 1)[0]
assert abs(slope - DELTA * (1 - ALPHA)) < 2e-3, slope
assert tv(on)[-1] < 1e-2 * tv(on)[0]

fig, axes = plt.subplots(1, 3, figsize=(10.0, 3.5))
for s, col, lab in [(hi, S[1], "c₀ 5% above the path"), (on, S[0], "c₀ on the saddle path"),
                    (lo, S[2], "c₀ 5% below the path")]:
    axes[0].plot(s.t, s.y[0], color=col, label=lab)
    axes[1].plot(s.t, s.y[1], color=col, label=lab)
    axes[2].semilogy(s.t, tv(s), color=col, label=lab)
axes[0].axhline(k_star, color=INK2, linestyle="--", linewidth=1)
axes[0].axhline(k_max, color=INK2, linestyle=":", linewidth=1)
axes[0].text(400, k_star, f" k* = {k_star:.2f}", va="bottom", ha="right", color=INK2, fontsize=8.5)
axes[0].text(400, k_max, f" k_max = {k_max:.1f}", va="top", ha="right", color=INK2, fontsize=8.5)
axes[0].annotate(f"k = 0 at t = {t_crash:.1f}", (t_crash, 0), xytext=(20, 25),
                 textcoords="offset points", color=S[1], fontsize=8.5,
                 arrowprops=dict(arrowstyle="->", color=S[1]))
axes[1].axhline(c_star, color=INK2, linestyle="--", linewidth=1)
axes[1].text(400, c_star, f"c* = {c_star:.3f}", va="bottom", ha="right", color=INK2, fontsize=8.5)
axes[0].set_ylabel("capital k")
axes[1].set_ylabel("consumption c")
axes[2].set_ylabel("e^(−ρt) u′(c) k  (log scale)")
axes[0].set_title("capital", loc="left", fontsize=10)
axes[1].set_title("consumption", loc="left", fontsize=10)
axes[2].set_title("transversality term", loc="left", fontsize=10)
axes[2].text(390, 3e2, f"slope δ(1−α) = {DELTA * (1 - ALPHA):.3f}", color=S[2], fontsize=8.5,
             ha="right")
for ax in axes:
    ax.set_xlabel("time t")
    ax.set_xlim(0, 400)
axes[1].legend(fontsize=7.5, loc="upper right")
fig.suptitle(f"From k₀ = {k0:.2f}: only c₀ = {c0:.4f} survives — above it k hits 0, "
             "below it transversality fails", x=0.01, ha="left", fontsize=11)
save(fig, OUT / "fig_ge_three_paths.svg")

# ---------- rho falls: the vertical locus moves right, c jumps down ----------
RHO2 = 0.015
k2s, c2s = steady(RHO2)
sk2, sc2, st2 = saddle_branch(RHO2)
c_jump = float(np.interp(k_star, sk2, sc2))
assert k2s > k_star and c2s > c_star, "more patience: more k and more c in the long run"
assert c_jump < c_star, "on impact c jumps down onto the new saddle path"
m2 = sk2 >= k_star
path2 = SimpleNamespace(t=np.append(st2[m2] - st2[m2][0], 300.0),
                        y=np.array([np.append(sk2[m2], k2s), np.append(sc2[m2], c2s)]))
assert abs(path2.y[0][-2] - k2s) / k2s < 1e-4

kg = np.linspace(0.01, 1.35 * k2s, 400)
fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.8), gridspec_kw=dict(width_ratios=[1.3, 1]))
ax = axes[0]
ax.plot(kg, f(kg) - DELTA * kg, color=S[0], label="k̇ = 0 (no ρ in it: does not move)")
ax.axvline(k_star, color=S[1], linestyle="--", linewidth=1.5, label=f"ċ = 0 before, ρ = {RHO}")
ax.axvline(k2s, color=S[1], label=f"ċ = 0 after, ρ = {RHO2}")
m = sk2 <= k2s
ax.plot(sk2[m], sc2[m], color=S[2], label="new saddle path")
dot(ax, k_star, c_star, INK, f"old ({k_star:.2f}, {c_star:.3f})", dx=-8, dy=8, ha="right")
dot(ax, k_star, c_jump, S[2], f"jump to {c_jump:.3f}", dx=8, dy=-12)
dot(ax, k2s, c2s, INK, f"new ({k2s:.2f}, {c2s:.3f})", dx=8, dy=-18)
ax.annotate("", (k_star, c_jump), (k_star, c_star),
            arrowprops=dict(arrowstyle="->", color=INK, lw=1.4))
ax.set_ylim(c_star - 0.35, c2s + 0.25)
ax.set_xlim(0, 1.35 * k2s)
ax.set_xlabel("capital k")
ax.set_ylabel("consumption c")
ax.legend(fontsize=7.5, loc="upper left")
ax = axes[1]
tt = np.concatenate([[-40, 0], path2.t])
cc = np.concatenate([[c_star, c_star], path2.y[1]])
ax.plot(tt[:2], cc[:2], color=S[2])
ax.plot(path2.t, path2.y[1], color=S[2], label="consumption c(t)")
ax.plot([0, 0], [c_star, c_jump], color=S[2], linestyle=":")
ax.axhline(c_star, color=INK2, linestyle="--", linewidth=1)
ax.axhline(c2s, color=INK2, linewidth=1)
ax.text(300, c_star, f"old c* {c_star:.3f}", va="bottom", ha="right", color=INK2, fontsize=8.5)
ax.text(300, c2s, f"new c* {c2s:.3f}", va="bottom", ha="right", color=INK2, fontsize=8.5)
ax.set_xlabel("time t (shock at t = 0)")
ax.set_ylabel("consumption c")
ax.set_xlim(-40, 300)
fig.suptitle("ρ falls: only the vertical locus moves; c drops on impact, then climbs above "
             "its old level", x=0.01, ha="left", fontsize=11)
save(fig, OUT / "fig_ge_rho_shift.svg")

# ---------- modified golden rule: k* below k_gold for every rho > 0 ----------
rr = np.linspace(0.0, 0.10, 300)
kk = (ALPHA / (DELTA + rr)) ** (1 / (1 - ALPHA))
assert np.all(kk[1:] < k_gold) and math.isclose(kk[0], k_gold)
assert round(k_star / k_gold, 3) == round((DELTA / (DELTA + RHO)) ** (1 / (1 - ALPHA)), 3) == 0.536
fig, ax = plt.subplots(figsize=(6.2, 3.5))
ax.plot(rr * 100, kk, color=S[0], label="k*(ρ): f′(k*) = δ + ρ")
ax.axhline(k_gold, color=S[1], label="k_gold: f′(k) = δ")
dot(ax, RHO * 100, k_star, INK, f"ρ = 3%: k* = {k_star:.2f} vs k_gold = {k_gold:.2f}", dx=8, dy=8)
ax.set_xlabel("rate of time preference ρ (% per period)")
ax.set_ylabel("capital per worker k")
ax.set_title("The gap between k* and k_gold is impatience: it closes only at ρ = 0",
             loc="left", fontsize=10.5)
ax.legend(fontsize=8.5, loc="lower left")
save(fig, OUT / "fig_ge_modified_golden.svg")

# =====================================================================================
# derivacoes-cap-09
# =====================================================================================
Ig = np.linspace(-(1 - DELTA) * K1, 3.0, 50)
fig, ax = plt.subplots(figsize=(6.2, 3.6))
for ratio, col in [(1.10, S[0]), (1.00, INK2), (0.90, S[1])]:
    prof = (ratio - 1) * ((1 - DELTA) * K1 + Ig)
    slope = np.polyfit(Ig, prof, 1)[0]
    assert math.isclose(slope, ratio - 1, abs_tol=1e-12)
    tag = {1.10: "profit → +∞ as I → ∞", 1.00: "Π = 0 for every I: equilibrium",
           0.90: "wants I → −∞"}[ratio]
    ax.plot(Ig, prof, color=col, label=f"r^K₂/(1+r) = {ratio:.2f}: slope {ratio - 1:+.2f}, {tag}")
ax.axvline(-(1 - DELTA) * K1, color=INK2, linestyle=":", linewidth=1)
ax.text(-(1 - DELTA) * K1, -0.47, "  K₂ = 0", color=INK2, fontsize=8.5, va="bottom")
ax.set_xlabel("investment I (goods)")
ax.set_ylabel("investment-firm profit Πᴵ (goods)")
ax.set_title("(9.1.2) is linear in I: the FOC fixes the price, not the quantity",
             loc="left", fontsize=10.5)
ax.legend(fontsize=8, loc="upper left")
save(fig, OUT / "fig_ge_invest_linear.svg")

K_ss = (ALPHA / (1 / BETA - 1 + DELTA)) ** (1 / (1 - ALPHA))
assert math.isclose(K_ss, k_star)
Kg = np.linspace(0.6 * K_ss, 1.15 * k_gold, 300)
fig, ax = plt.subplots(figsize=(6.4, 3.6))
for sig, col in [(0.5, S[0]), (2.0, S[1]), (5.0, S[2])]:
    g = (BETA * (1 + fp(Kg) - DELTA)) ** (1 / sig)
    assert math.isclose((BETA * (1 + fp(K_ss) - DELTA)) ** (1 / sig), 1.0)
    assert (BETA * (1 + fp(k_gold) - DELTA)) ** (1 / sig) < 1
    ax.plot(Kg, g, color=col, label=f"σ = {sig:g}")
ax.axhline(1, color=INK2, linewidth=1)
ax.axvline(k_gold, color=INK2, linestyle=":", linewidth=1)
ax.text(k_gold, 1.02, " K_gr (c falls here)", color=INK2, fontsize=8.5)
dot(ax, K_ss, 1.0, INK, f"K_ss = {K_ss:.2f} for every σ", dx=8, dy=-16)
ax.set_ylim(0.955, 1.04)
ax.set_xlabel("next period's capital Kₜ₊₁")
ax.set_ylabel("consumption growth cₜ₊₁/cₜ")
ax.set_title("(9.3.14): σ changes the speed, never where growth stops",
             loc="left", fontsize=10.5)
ax.legend(fontsize=8.5, loc="lower left")
save(fig, OUT / "fig_ge_euler_growth.svg")

# =====================================================================================
# exogenous-capital-lista-05: capital frozen at K-bar (base vector of check_ge)
# =====================================================================================
FZ = dict(sigma=0.5, psi=1.8, alpha=0.35, K=2.0, beta=0.96)


def hours(A, v):
    """Solve psi L^e/(1-L) = (1-alpha)(A K^alpha)^(1-sigma), e = alpha + (1-alpha) sigma."""
    e = v["alpha"] + (1 - v["alpha"]) * v["sigma"]
    rhs_ = (1 - v["alpha"]) * (A * v["K"] ** v["alpha"]) ** (1 - v["sigma"])
    return brentq(lambda L: v["psi"] * L ** e / (1 - L) - rhs_, 1e-12, 1 - 1e-12)


assert math.isclose(hours(1.0, {**FZ, "sigma": 1.0}), 0.26531, abs_tol=5e-6)
assert math.isclose(hours(1.0, FZ), 0.19273, abs_tol=5e-6)
a_, K_ = FZ["alpha"], FZ["K"]
Kgrid = np.linspace(0.6, 4.0, 300)
fig, ax = plt.subplots(figsize=(6.2, 3.6))
for A, col in [(1.0, S[0]), (1.3, S[1])]:
    L = hours(A, FZ)
    rK = a_ * A * K_ ** (a_ - 1) * L ** (1 - a_)
    assert math.isclose(rK, a_ * A * K_ ** a_ * L ** (1 - a_) / K_)   # r^K = alpha c / K
    ax.plot(Kgrid, a_ * A * Kgrid ** (a_ - 1) * L ** (1 - a_), color=col,
            label=f"demand F_K(K, L) at A = {A}, L = {L:.3f}")
    dot(ax, K_, rK, col, f"r^K = {rK:.3f}", dx=8, dy=4)
ax.axvline(K_, color=INK, linewidth=2.2, label=f"supply: K̄ = {K_}, vertical")
ax.set_xlabel("capital K")
ax.set_ylabel("rental rate r^K (goods per unit)")
ax.set_title("No investment technology: r^K is the residual that clears K̄",
             loc="left", fontsize=10.5)
ax.legend(fontsize=8.5, loc="upper right")
save(fig, OUT / "fig_ge_frozen_rental.svg")

ratio = np.linspace(0.7, 1.4, 120)
fig, ax = plt.subplots(figsize=(6.2, 3.6))
for sig, col in [(0.5, S[0]), (1.0, S[1]), (2.5, S[2])]:
    v = {**FZ, "sigma": sig}
    L1 = hours(1.0, v)
    c1 = K_ ** a_ * L1 ** (1 - a_)
    r = []
    for q in ratio:
        c2 = q * K_ ** a_ * hours(q, v) ** (1 - a_)
        r.append((c2 / c1) ** sig / FZ["beta"] - 1)
    r = np.array(r)
    assert np.all(np.diff(r) > 0)
    ax.plot(ratio, r * 100, color=col, label=f"σ = {sig:g}")
r0 = 1 / FZ["beta"] - 1
dot(ax, 1.0, r0 * 100, INK, f"A₂ = A₁: r = 1/β − 1 = {r0 * 100:.2f}% for every σ", dx=8, dy=-14)
ax.axhline(0, color=INK2, linewidth=1)
ax.set_xlabel("productivity growth A₂/A₁")
ax.set_ylabel("equilibrium interest rate r (%)")
ax.set_title("r comes last: it prices an output profile nobody can reshape",
             loc="left", fontsize=10.5)
ax.legend(fontsize=8.5, loc="upper left")
save(fig, OUT / "fig_ge_frozen_r.svg")
