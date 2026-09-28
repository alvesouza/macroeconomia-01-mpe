#!/usr/bin/env python3
"""Figures for the notes in Map/aula-02-solow-mecanica.

Every number drawn or labelled is computed here and, where a note quotes it, asserted
against the note's value first, so a figure never illustrates a wrong claim.

Run: python Map/aula-02-solow-mecanica/make_figures.py [--png DIR]
Writes fig/fig_0*.svg next to this file; --png also writes PNG previews to DIR.
"""
from __future__ import annotations

import math
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "fig"))
from mapstyle import S, INK, INK2, SURF, save  # noqa: E402

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

OUT = pathlib.Path(__file__).resolve().parent / "fig"
PNG_DIR = None
if "--png" in sys.argv:
    PNG_DIR = pathlib.Path(sys.argv[sys.argv.index("--png") + 1])
    PNG_DIR.mkdir(parents=True, exist_ok=True)


def out(fig, name):
    """Save `fig` as fig/<name>.svg, plus a PNG preview when --png was given."""
    if PNG_DIR is not None:
        fig.tight_layout()
        fig.savefig(PNG_DIR / f"{name}.png", format="png", dpi=110)
    save(fig, OUT / f"{name}.svg")


def title(ax, text):
    ax.set_title(text, loc="left", color=INK, fontsize=10.5)


# ---------- the model, as in check_solow.py ----------
ALPHA, SAV, DELTA, N = 1 / 3, 0.20, 0.05, 0.01


def f(k, alpha=ALPHA):
    return k ** alpha


def fprime(k, alpha=ALPHA):
    return alpha * k ** (alpha - 1)


def k_ss(s=SAV, delta=DELTA, n=N, alpha=ALPHA):
    return (s / (delta + n)) ** (1 / (1 - alpha))


KSS = k_ss()
KSS_NO_N = k_ss(n=0.0)
LAM = (1 - ALPHA) * (DELTA + N)
assert math.isclose(KSS, 6.0858, abs_tol=1e-4)
assert math.isclose(KSS_NO_N, 8.0)
assert math.isclose(LAM, 0.04)

# ======================= 01-growth-facts =======================
g_book, factor = 0.015, 27
g_27 = factor ** (1 / 216) - 1
assert math.isclose(1.015 ** 216, 24.93, abs_tol=0.01)
assert math.isclose(math.log(27) / 216, 0.015258, abs_tol=1e-6)
assert math.isclose(g_27, 0.01538, abs_tol=1e-5)

years = np.arange(1800, 2017)
p15 = 1.015 ** (years - 1800)
p27 = (1 + g_27) ** (years - 1800)
fig, axes = plt.subplots(1, 2, figsize=(8.2, 3.4))
for ax, log in zip(axes, (False, True)):
    ax.plot(years, p15, color=S[0], label="1.5% a year")
    ax.plot(years, p27, color=S[1], ls="--", label="1.54% a year (27× by 2016)")
    ax.set_xlabel("year")
    if log:
        ax.set_yscale("log")
        ax.set_yticks([1, 2, 5, 10, 20])
        ax.set_yticklabels(["1", "2", "5", "10", "20"])
        title(ax, "Log scale: a straight line")
    else:
        title(ax, "Linear scale: looks like an explosion")
    ax.set_ylabel("GDP per capita, 1800 = 1")
    ax.set_xlim(1790, 2060)
    ax.annotate(f"{p15[-1]:.1f}×", (2016, p15[-1]), xytext=(4, -10),
                textcoords="offset points", color=S[0])
    ax.annotate(f"{p27[-1]:.0f}×", (2016, p27[-1]), xytext=(4, 2),
                textcoords="offset points", color=S[1])
axes[0].legend(loc="upper left", fontsize=8.5)
fig.suptitle("Fact 1: constant growth compounds to ~25–27× over 216 years",
             x=0.01, ha="left", color=INK, fontsize=11)
out(fig, "fig_01_log_scale")

r_gross = (1 - 0.65) / 3.2
r_net = r_gross - 0.05
assert math.isclose(r_gross, 0.109375) and math.isclose(r_net, 0.059375)
fig, ax = plt.subplots(figsize=(7.0, 2.0))
ax.barh([0], [0.05 * 100], color=S[1], height=0.5, label="depreciation δ = 5.0%")
ax.barh([0], [r_net * 100], left=[5], color=S[0], height=0.5,
        label=f"net return = {r_net * 100:.1f}%")
ax.text(2.5, 0, "δ\n5.0%", ha="center", va="center", color=SURF, fontsize=9)
ax.text(5 + r_net * 50, 0, f"net\n{r_net * 100:.1f}%", ha="center", va="center",
        color=SURF, fontsize=9)
ax.text(r_gross * 100 + 0.15, 0, f"gross = 0.35 / 3.2\n= {r_gross * 100:.1f}%",
        va="center", color=INK, fontsize=9)
ax.set_xlim(0, 14.5)
ax.set_yticks([])
ax.set_xlabel("return on capital, % a year")
ax.grid(axis="y", visible=False)
title(ax, "Fact 4: the gross return (capital share ÷ K/Y) splits into δ plus the net return")
out(fig, "fig_01_return")

# ======================= 02-ingredients =======================
k = np.linspace(0.001, 12, 600)
a_lin = 0.25
fig, axes = plt.subplots(1, 2, figsize=(8.2, 3.4))
ax = axes[0]
ax.plot(k, f(k), color=S[0], label="Cobb–Douglas f(k) = k^(1/3)")
ax.plot(k, a_lin * k, color=S[1], ls="--", label="linear f(k) = 0.25 k")
ax.set_xlabel("capital per worker k")
ax.set_ylabel("output per worker y")
ax.legend(fontsize=8.5, loc="upper left")
title(ax, "Levels: concave against straight")
ax = axes[1]
kk = np.linspace(0.02, 12, 600)
ax.plot(kk, fprime(kk), color=S[0], label="f'(k) = (1/3) k^(−2/3)")
ax.axhline(a_lin, color=S[1], ls="--", label="f'(k) = 0.25, constant")
ax.set_ylim(0, 2.5)
ax.set_xlabel("capital per worker k")
ax.set_ylabel("marginal product f'(k)")
ax.annotate("→ ∞ as k → 0", (0.1, fprime(0.1)), xytext=(1.2, 2.2), color=S[0],
            arrowprops=dict(arrowstyle="->", color=S[0]))
ax.annotate("→ 0 as k → ∞", (11, fprime(11)), xytext=(7.5, 0.55), color=S[0])
ax.legend(fontsize=8.5, loc="center right")
title(ax, "Slopes: Inada holds only for Cobb–Douglas")
out(fig, "fig_02_cd_inada")

k0 = 4.0
y0, mpk = f(k0), fprime(k0)
w0 = y0 - mpk * k0
assert math.isclose(mpk * k0, ALPHA * y0) and math.isclose(w0, (1 - ALPHA) * y0)
fig, ax = plt.subplots(figsize=(6.4, 3.8))
kx = np.linspace(0, 9, 400)
ax.plot(kx, f(kx), color=S[0], label="f(k) = k^(1/3)")
ax.plot(kx, w0 + mpk * kx, color=S[1], ls="--", label=f"tangent at k = {k0:.0f}, slope f'(k) = {mpk:.3f}")
ax.plot([k0, k0], [0, y0], color=INK2, lw=1, ls=":")
ax.plot([0], [w0], "o", color=S[1])
ax.plot([k0], [y0], "o", color=S[0])
ax.annotate("", (k0 + 0.25, 0), (k0 + 0.25, w0),
            arrowprops=dict(arrowstyle="<->", color=S[2]))
ax.text(k0 + 0.4, w0 / 2, f"labour income w = f − f'k\n= (1−α) y = {w0:.3f}",
        color=S[2], va="center", fontsize=9)
ax.annotate("", (k0 + 0.25, w0), (k0 + 0.25, y0),
            arrowprops=dict(arrowstyle="<->", color=S[3]))
ax.text(k0 + 0.4, (w0 + y0) / 2 + 0.05, f"capital income f'(k)·k\n= α y = {mpk * k0:.3f}",
        color=S[3], va="center", fontsize=9)
ax.text(0.15, w0 - 0.15, f"intercept = w = {w0:.3f}", color=S[1], fontsize=9)
ax.set_xlim(0, 9)
ax.set_ylim(0, 2.4)
ax.set_xlabel("capital per worker k")
ax.set_ylabel("output per worker y")
ax.legend(fontsize=8.5, loc="upper left")
title(ax, f"Euler per worker: y = {y0:.3f} splits exactly into wage + capital income")
out(fig, "fig_02_euler_tangent")

# ======================= 03-fundamental-equation =======================
kx = np.linspace(0, 10, 500)
fig, ax = plt.subplots(figsize=(6.8, 3.9))
ax.plot(kx, SAV * f(kx), color=S[0], label="actual investment s f(k)")
ax.plot(kx, (DELTA + N) * kx, color=S[1], label="break-even (δ+n) k")
ax.plot(kx, DELTA * kx, color=S[1], ls="--", lw=1.4, label="trap 3: δ k only")
yss = SAV * f(KSS)
ax.plot([KSS], [yss], "o", color=INK)
ax.plot([KSS_NO_N], [SAV * f(KSS_NO_N)], "o", color=INK2)
ax.annotate(f"k_ss = {KSS:.2f}", (KSS, yss), xytext=(4.4, 0.45), color=INK,
            arrowprops=dict(arrowstyle="->", color=INK))
ax.annotate(f"wrong k_ss = {KSS_NO_N:.2f}", (KSS_NO_N, SAV * f(KSS_NO_N)),
            xytext=(7.4, 0.2), color=INK2, arrowprops=dict(arrowstyle="->", color=INK2))
kb = 3.0
ax.annotate("", (kb, DELTA * kb), (kb, (DELTA + N) * kb),
            arrowprops=dict(arrowstyle="<->", color=S[2], shrinkA=0, shrinkB=0))
ax.text(kb + 0.3, 0.09, "n k: equip\nnew workers", color=S[2],
        fontsize=8.5)
ax.annotate("", (kb, (DELTA + N) * kb), (kb, SAV * f(kb)),
            arrowprops=dict(arrowstyle="<->", color=S[3], shrinkA=0, shrinkB=0))
ax.text(kb - 1.9, 0.235, "Δk > 0\n(gap)", color=S[3], fontsize=8.5)
ax.set_xlim(0, 10)
ax.set_ylim(0, 0.5)
ax.set_xlabel("capital per worker k")
ax.set_ylabel("investment per worker")
ax.legend(fontsize=8.5, loc="upper left")
title(ax, "Break-even has two parts; dropping n k overstates k_ss by 31%")
assert math.isclose(KSS_NO_N / KSS - 1, 0.3145, abs_tol=1e-3)
out(fig, "fig_03_diagram")

kx = np.linspace(0.3, 12, 500)
fig, ax = plt.subplots(figsize=(6.6, 3.7))
ax.plot(kx, SAV * f(kx) / kx, color=S[0], label="s f(k)/k = s k^(α−1)")
ax.axhline(DELTA + N, color=S[1], label="δ + n = 0.06")
for kk_, col in ((1.0, S[2]), (3.0, S[3])):
    gk = SAV * f(kk_) / kk_ - (DELTA + N)
    ax.annotate("", (kk_, DELTA + N), (kk_, SAV * f(kk_) / kk_),
                arrowprops=dict(arrowstyle="<->", color=col, shrinkA=0, shrinkB=0))
    ax.text(kk_ - 0.2, 0.03, f"k̇/k = {gk * 100:.1f}%", color=col, fontsize=9)
ax.plot([KSS], [DELTA + N], "o", color=INK)
ax.annotate(f"k_ss = {KSS:.2f}: k̇/k = 0", (KSS, DELTA + N), xytext=(KSS + 0.4, 0.12),
            color=INK, arrowprops=dict(arrowstyle="->", color=INK))
ax.set_ylim(0, 0.3)
ax.set_xlabel("capital per worker k")
ax.set_ylabel("rate per year")
ax.legend(fontsize=8.5, loc="upper right")
title(ax, "The growth rate of k is the vertical gap, and it shrinks as k rises")
assert math.isclose(SAV * 1 - 0.06, 0.14)
out(fig, "fig_03_growth_rate")

# ======================= 04-steady-state-and-stability =======================
k1 = 4.0
chord, tang = f(k1) / k1, fprime(k1)
assert tang < chord and math.isclose(tang / chord, ALPHA)
kx = np.linspace(0, 8, 400)
fig, ax = plt.subplots(figsize=(6.4, 3.8))
ax.plot(kx, f(kx), color=S[0], label="f(k) = k^(1/3)")
ax.plot(kx, chord * kx, color=S[1], label=f"chord from origin, slope f(k)/k = {chord:.3f}")
ax.plot(kx, f(k1) + tang * (kx - k1), color=S[2], ls="--",
        label=f"tangent, slope f'(k) = {tang:.3f}")
ax.plot([k1], [f(k1)], "o", color=INK)
ax.text(k1 + 0.15, f(k1) - 0.18, f"k = {k1:.0f}", color=INK)
ax.plot([0], [f(k1) - tang * k1], "o", color=S[2])
ax.text(0.15, f(k1) - tang * k1 - 0.2, f"intercept f − f'k = {f(k1) - tang * k1:.3f} > 0",
        color=S[2], fontsize=9)
ax.set_xlim(0, 8)
ax.set_ylim(0, 3.2)
ax.set_xlabel("capital per worker k")
ax.set_ylabel("output per worker y")
ax.legend(fontsize=8.5, loc="upper left")
title(ax, "Chord steeper than tangent: f'(k)k < f(k), so f(k)/k falls with k")
out(fig, "fig_04_chord_tangent")

fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.5))
ax = axes[0]
kx = np.linspace(0, 12, 500)
phi = SAV * f(kx) - (DELTA + N) * kx
ax.plot(kx, phi, color=S[0], label="φ(k) = s k^(1/3) − (δ+n) k")
ax.axhline(0, color=INK2, lw=1)
ax.plot([KSS], [0], "o", color=INK)
ax.annotate(f"one root, k_ss = {KSS:.2f}", (KSS, 0), xytext=(KSS - 2.5, 0.07), color=INK,
            arrowprops=dict(arrowstyle="->", color=INK))
ax.text(0.3, -0.125, "φ > 0: near k = 0 (Inada at 0)\nφ < 0: for large k (Inada at ∞)", color=INK2, fontsize=8.5)
ax.set_xlabel("capital per worker k")
ax.set_ylabel("excess investment φ(k)")
ax.set_ylim(-0.14, 0.14)
ax.legend(fontsize=8.5, loc="upper right")
title(ax, "Cobb–Douglas: + then −, crosses once")
ax = axes[1]
for A_, col in ((0.40, S[1]), (0.20, S[2])):
    slope = SAV * A_ - (DELTA + N)
    ax.plot(kx, slope * kx, color=col,
            label=f"A = {A_:.2f}: φ = ({slope:+.2f}) k, {'grows forever' if slope > 0 else 'collapses to 0'}")
ax.axhline(0, color=INK2, lw=1)
ax.set_xlabel("capital per worker k")
ax.set_ylabel("excess investment φ(k)")
ax.set_ylim(-0.3, 0.3)
ax.legend(fontsize=8.5, loc="upper left")
title(ax, "AK (s = 0.2): φ never crosses zero for k > 0")
assert math.isclose(SAV * 0.40 - 0.06, 0.02) and math.isclose(SAV * 0.20 - 0.06, -0.02)
fig.suptitle("Existence needs Inada, uniqueness needs concavity; AK has neither",
             x=0.01, ha="left", color=INK, fontsize=11)
out(fig, "fig_04_existence_ak")

# Discrete map with a decade as the period, so the steps are visible.
d10 = 1 - (1 - DELTA) ** 10
n10 = (1 + N) ** 10 - 1
k10 = k_ss(SAV, d10, n10)


def G(k):
    return ((1 - d10) * k + SAV * f(k)) / (1 + n10)


g_slope = (1 - d10 + ALPHA * (d10 + n10)) / (1 + n10)
assert math.isclose((G(k10 + 1e-6) - G(k10 - 1e-6)) / 2e-6, g_slope, rel_tol=1e-6)
assert 0 < g_slope < 1 and math.isclose(G(k10), k10)
fig, ax = plt.subplots(figsize=(6.2, 4.2))
kx = np.linspace(0, 2.2 * k10, 400)
ax.plot(kx, G(kx), color=S[0], label="k_{t+1} = G(k_t)")
ax.plot(kx, kx, color=INK2, lw=1.2, ls="--", label="45° line: k_{t+1} = k_t")
for kstart, col in ((0.1 * k10, S[1]), (2.0 * k10, S[2])):
    kc = kstart
    xs, ys = [kc], [0]
    for _ in range(8):
        kn = G(kc)
        xs += [kc, kn]
        ys += [kn, kn]
        kc = kn
    ax.plot(xs, ys, color=col, lw=1.2, label=f"path from k_0 = {kstart:.2f}")
ax.plot([k10], [k10], "o", color=INK)
ax.annotate(f"k_ss = {k10:.2f}, G'(k_ss) = {g_slope:.2f}", (k10, k10),
            xytext=(k10 * 1.1, k10 * 0.45), color=INK, arrowprops=dict(arrowstyle="->", color=INK))
ax.set_xlim(0, 2.2 * k10)
ax.set_ylim(0, 2.2 * k10)
ax.set_xlabel("k_t (period = 10 years)")
ax.set_ylabel("k_{t+1}")
ax.legend(fontsize=8.5, loc="upper left")
title(ax, "0 < G' < 1: every path steps monotonically into k_ss, never past it")
out(fig, "fig_04_map")

half = math.log(2) / LAM
assert math.isclose(half, 17.33, abs_tol=0.01)
T, dt = 100, 0.01
kc, ts, dev = KSS / 2, [0.0], [math.log(0.5)]
for i in range(int(T / dt)):
    kc += dt * (SAV * f(kc) - (DELTA + N) * kc)
    ts.append((i + 1) * dt)
    dev.append(math.log(kc / KSS))
ts, dev = np.array(ts), np.array(dev)
fig, ax = plt.subplots(figsize=(6.6, 3.6))
ax.plot(ts, dev / dev[0], color=S[0], label="exact path, ln(k/k_ss) ÷ its start value")
ax.plot(ts, np.exp(-LAM * ts), color=S[1], ls="--", label="linear approximation e^(−λt), λ = 0.04")
ax.axhline(0.5, color=INK2, lw=1, ls=":")
ax.axvline(half, color=INK2, lw=1, ls=":")
share_at_half = dev[int(half / dt)] / dev[0]
ax.text(45, 0.53, f"half-life ln2/λ = {half:.1f} years", color=INK, fontsize=9)
ax.text(45, 0.45, f"exact path at {half:.1f} y: {share_at_half:.2f} of gap left",
        color=S[0], fontsize=9)
ax.set_xlabel("years since start (k_0 = k_ss / 2)")
ax.set_ylabel("share of the log gap remaining")
ax.set_ylim(0, 1.05)
ax.legend(fontsize=8.5, loc="upper right")
title(ax, "The gap closes at about 4% a year: half gone in 17 years")
out(fig, "fig_04_half_life")

# ======================= 05-comparative-statics =======================
s0, s1 = 0.20, 0.25
ka, kb_ = k_ss(s0), k_ss(s1)
assert math.isclose(kb_, 8.505, abs_tol=1e-3)
kx = np.linspace(0, 11, 500)
fig, ax = plt.subplots(figsize=(6.6, 3.8))
ax.plot(kx, s0 * f(kx), color=S[0], ls="--", label="before: s₀ f(k), s₀ = 0.20")
ax.plot(kx, s1 * f(kx), color=S[0], label="after: s₁ f(k), s₁ = 0.25")
ax.plot(kx, (DELTA + N) * kx, color=S[1], label="break-even (δ+n) k")
ax.plot([ka, kb_], [s0 * f(ka), s1 * f(kb_)], "o", color=INK)
ax.annotate("", (ka, s1 * f(ka)), (ka, s0 * f(ka)),
            arrowprops=dict(arrowstyle="->", color=S[2], shrinkA=0, shrinkB=0))
ax.text(ka + 0.2, 0.27,
        f"impact: Δk̇ = (s₁−s₀) f(k) = {(s1 - s0) * f(ka):.3f}", color=S[2], fontsize=8.5)
ax.annotate("", (kb_, 0.03), (ka, 0.03), arrowprops=dict(arrowstyle="->", color=INK))
ax.text((ka + kb_) / 2, 0.045, f"k_ss: {ka:.2f} → {kb_:.2f}", ha="center", color=INK,
        fontsize=9)
ax.set_xlim(0, 11)
ax.set_ylim(0, 0.62)
ax.set_xlabel("capital per worker k")
ax.set_ylabel("investment per worker")
ax.legend(fontsize=8.5, loc="upper left")
title(ax, "A higher s rotates the curve up; k_ss rises 40%, k itself cannot jump")
out(fig, "fig_05_shift")

# Transition in continuous time from k_ss(s0), shock at t = 0.
dt = 0.01
tt = np.arange(-10, 100 + dt / 2, dt)
kpath = np.empty_like(tt)
kc = ka
for i, t in enumerate(tt):
    kpath[i] = kc
    s_ = s0 if t < 0 else s1
    kc += dt * (s_ * f(kc) - (DELTA + N) * kc)
spath = np.where(tt < 0, s0, s1)
lny = np.log(f(kpath) / f(ka))
gy = ALPHA * (spath * f(kpath) / kpath - (DELTA + N))
cpath = (1 - spath) * f(kpath)
gain = ALPHA / (1 - ALPHA) * math.log(s1 / s0)
peak = ALPHA * (s1 - s0) * (DELTA + N) / s0
assert math.isclose(gain, 0.11157, abs_tol=1e-5) and math.isclose(math.expm1(gain), 0.118, abs_tol=5e-4)
assert math.isclose(peak, 0.005) and math.isclose(gy.max(), peak, rel_tol=1e-3)
c0, c_imp, c1 = (1 - s0) * f(ka), (1 - s1) * f(ka), (1 - s1) * f(kb_)
assert c_imp < c0 < c1
fig, axes = plt.subplots(3, 1, figsize=(6.6, 7.2), sharex=True)
ax = axes[0]
ax.plot(tt, lny, color=S[0])
ax.axhline(gain, color=S[0], ls="--", lw=1)
ax.text(60, gain - 0.025, f"new level: +{gain:.4f} log pts = +{math.expm1(gain) * 100:.1f}%",
        color=S[0], fontsize=9)
ax.set_ylabel("ln y − ln y_ss(s₀)")
title(ax, "Level: permanently higher, reached slowly")
ax = axes[1]
ax.plot(tt, gy * 100, color=S[1])
ax.text(3, peak * 100 * 0.92, f"peak α(s₁−s₀)(δ+n)/s₀ = {peak * 100:.1f}% a year",
        color=S[1], fontsize=9)
ax.text(60, 0.08, "long-run growth: back to 0", color=S[1], fontsize=9)
ax.set_ylabel("growth of y, % a year")
title(ax, "Rate: spikes, then decays to zero (area under it = level gain)")
ax = axes[2]
ax.plot(tt, cpath, color=S[2])
ax.axhline(c0, color=S[2], ls="--", lw=1)
ax.text(-9, c0 + 0.012, f"old c_ss = {c0:.3f}", color=S[2], fontsize=9)
ax.text(2, c_imp - 0.005, f"impact drop to {c_imp:.3f}", color=S[2], fontsize=9, va="top")
ax.text(60, c1 - 0.03, f"new c_ss = {c1:.3f}", color=S[2], fontsize=9)
ax.set_ylim(c_imp - 0.05, c1 + 0.05)
ax.set_ylabel("consumption per worker c")
ax.set_xlabel("years since s rises from 0.20 to 0.25")
title(ax, "Consumption: falls on impact, overtakes the old level later")
for ax in axes:
    ax.axvline(0, color=INK2, lw=1, ls=":")
out(fig, "fig_05_transition")


def c_ss(s):
    return (1 - s) * f(k_ss(s))


sg = np.linspace(0.01, 0.95, 400)
assert math.isclose(fprime(k_ss(ALPHA)), DELTA + N)
assert c_ss(ALPHA) >= c_ss(sg).max() - 1e-12
fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.5))
ax = axes[0]
ax.plot(sg, c_ss(sg), color=S[0], label="c_ss(s) = (1−s) f(k_ss(s))")
OFF = {"s = 0.20: rising": (0.02, 0.9), "s = α = 1/3: peak": (0.30, 1.78),
       "s = 0.50: falling": (0.55, 1.2)}
for sm, lab in ((0.20, "s = 0.20: rising"), (ALPHA, "s = α = 1/3: peak"), (0.50, "s = 0.50: falling")):
    ax.plot([sm], [c_ss(sm)], "o", color=INK)
    ax.annotate(f"{lab}\nc = {c_ss(sm):.3f}", (sm, c_ss(sm)), xytext=OFF[lab],
                fontsize=8.5, color=INK, arrowprops=dict(arrowstyle="->", color=INK2))
ax.set_xlabel("saving rate s")
ax.set_ylabel("steady-state consumption per worker")
ax.set_ylim(0, 2.2)
ax.legend(fontsize=8.5, loc="lower center")
title(ax, "c_ss is hump-shaped in s")
ax = axes[1]
ax.plot(sg, fprime(k_ss(sg)), color=S[1], label="f'(k_ss(s))")
ax.axhline(DELTA + N, color=INK2, ls="--", lw=1.2, label="δ + n = 0.06")
ax.axvline(ALPHA, color=INK2, lw=1, ls=":")
ax.text(0.05, 0.02, "f' > δ+n:\nsave more", color=S[1], fontsize=8.5)
ax.text(0.6, 0.12, "f' < δ+n:\nsave less", color=S[1], fontsize=8.5)
ax.set_ylim(0, 0.3)
ax.set_xlabel("saving rate s")
ax.set_ylabel("marginal product at k_ss")
ax.legend(fontsize=8.5, loc="upper right")
title(ax, "The sign of dc_ss/ds is the sign of f' − (δ+n)")
fig.suptitle("More saving raises long-run consumption only while f'(k_ss) > δ + n",
             x=0.01, ha="left", color=INK, fontsize=11)
out(fig, "fig_05_golden")

# Model-simulated cross-section: absolute vs conditional convergence.
rng = np.random.default_rng(7)
ncty, horizon = 60, 50
s_c = rng.uniform(0.05, 0.35, ncty)
k0_c = k_ss(s_c) * np.exp(rng.uniform(-1.5, 0.3, ncty))
kc = k0_c.copy()
for _ in range(int(horizon / 0.05)):
    kc = kc + 0.05 * (s_c * f(kc) - (DELTA + N) * kc)
growth = ALPHA * np.log(kc / k0_c) / horizon * 100
lny0 = ALPHA * np.log(k0_c)
gap = ALPHA * np.log(k_ss(s_c) / k0_c)
slope_c = np.polyfit(gap, growth, 1)[0]
slope_a = np.polyfit(lny0, growth, 1)[0]
pred = (1 - math.exp(-LAM * horizon)) / horizon * 100
assert abs(slope_c - pred) < 0.35 * pred and slope_c > 0
fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.5), sharey=True)
ax = axes[0]
ax.scatter(lny0, growth, s=16, color=S[0])
ax.set_xlabel("initial ln y")
ax.set_ylabel(f"avg growth of y over {horizon} years, %")
title(ax, f"Against initial income: a cloud (slope {slope_a:+.2f})")
ax = axes[1]
ax.scatter(gap, growth, s=16, color=S[0])
xg = np.linspace(gap.min(), gap.max(), 10)
ax.plot(xg, np.polyval(np.polyfit(gap, growth, 1), xg), color=S[1],
        label=f"fitted slope {slope_c:.2f}; theory (1−e^(−λT))/T = {pred:.2f}")
ax.set_xlabel("gap to own steady state, ln y_ss − ln y₀")
ax.legend(fontsize=8.5, loc="upper left")
title(ax, "Against the gap to its own y_ss: a line")
fig.suptitle(f"{ncty} model economies with s drawn from 0.05–0.35: conditional, not absolute, convergence",
             x=0.01, ha="left", color=INK, fontsize=10.5)
out(fig, "fig_05_convergence")
