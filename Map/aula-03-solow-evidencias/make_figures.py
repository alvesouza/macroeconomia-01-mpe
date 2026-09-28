#!/usr/bin/env python3
"""Figures for the notes in Map/aula-03-solow-evidencias.

Every number drawn or labelled is computed here from Kurlat's calibration (section 5.2)
and asserted against the value the notes quote (the same values check_growth.py checks),
so a figure never illustrates a number the text does not support.

Run: python Map/aula-03-solow-evidencias/make_figures.py [--png DIR]
Writes fig/*.svg next to this file; --png also writes PNG previews to DIR.
"""
from __future__ import annotations

import math
import pathlib
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "fig"))
from mapstyle import INK, INK2, S, save  # noqa: E402

import matplotlib.pyplot as plt  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
FIG = HERE / "fig"
PNG_DIR: pathlib.Path | None = None

ALPHA, G, N, DELTA, SAV = 0.35, 0.015, 0.01, 0.04, 0.20
BREAK = DELTA + N + G


def f(k, alpha=ALPHA):
    """Cobb-Douglas intensive production function f(k) = k^alpha."""
    return k ** alpha


def fp(k, alpha=ALPHA):
    """Marginal product f'(k) = alpha k^(alpha-1)."""
    return alpha * k ** (alpha - 1)


def k_ss(s, brk, alpha=ALPHA):
    """Steady state of s f(k) = brk * k for Cobb-Douglas."""
    return (s / brk) ** (1 / (1 - alpha))


def out(fig, name):
    """Save `fig` as fig/<name>.svg, plus a PNG preview when --png was given."""
    if PNG_DIR is not None:
        fig.tight_layout()
        PNG_DIR.mkdir(parents=True, exist_ok=True)
        fig.savefig(PNG_DIR / (name + ".png"), dpi=110)
    save(fig, FIG / (name + ".svg"))


# ------------------------------------------------------------------ 01-golden-rule
def fig_gr_geometry():
    """f(k) against (delta+n)k: the Golden Rule is the widest vertical gap."""
    brk = DELTA + N
    kg = (ALPHA / brk) ** (1 / (1 - ALPHA))
    assert math.isclose(fp(kg), brk)
    cg = f(kg) - brk * kg
    k20, k50 = k_ss(0.20, brk), k_ss(0.50, brk)
    c20, c50 = f(k20) - brk * k20, f(k50) - brk * k50
    assert c20 < cg and c50 < cg
    k = np.linspace(0.01, 40, 600)
    fig, ax = plt.subplots(figsize=(7, 4.2))
    ax.plot(k, f(k), color=S[0], label="output f(k) = k^0.35")
    ax.plot(k, brk * k, color=S[1], label="break-even investment (δ+n)k")
    ax.plot(k, f(kg) + brk * (k - kg), color=INK2, lw=1, ls=":",
            label="tangent at k_gold, slope δ+n = 0.05")
    for kk, cc, col, lab in [(k20, c20, S[2], "s = 0.20"), (kg, cg, INK, "k_gold, s = α = 0.35"),
                             (k50, c50, S[3], "s = 0.50")]:
        ax.annotate("", xy=(kk, f(kk)), xytext=(kk, brk * kk),
                    arrowprops=dict(arrowstyle="<->", color=col, lw=1.6))
        ax.text(kk + 0.5, brk * kk + cc / 2, f"{lab}\nc = {cc:.2f}", color=col,
                fontsize=9, va="center")
    ax.set_xlim(0, 40)
    ax.set_ylim(0, 3.8)
    ax.set_xlabel("capital per worker, k")
    ax.set_ylabel("output per worker")
    ax.set_title("Golden Rule: c = f(k) − (δ+n)k is widest where f′(k) = δ+n", fontsize=11)
    ax.legend(loc="upper left", fontsize=9)
    out(fig, "fig_gr_geometry")
    return kg, cg


def fig_gr_r_vs_n():
    """Steady-state r(s) = alpha(delta+n)/s - delta against n: r < n iff s > alpha."""
    brk = DELTA + N
    s = np.linspace(0.12, 0.8, 400)
    r = ALPHA * brk / s - DELTA
    r_us = ALPHA * brk / SAV - DELTA
    assert math.isclose(ALPHA * brk / ALPHA - DELTA, N)
    assert math.isclose(r_us, 0.0475)
    fig, ax = plt.subplots(figsize=(7, 3.8))
    ax.plot(s * 100, r * 100, color=S[0], label="steady-state interest rate r = α(δ+n)/s − δ")
    ax.axhline(N * 100, color=S[1], label="population growth n = 1%")
    ax.axvspan(ALPHA * 100, 80, color=S[1], alpha=0.10, lw=0)
    ax.plot([ALPHA * 100], [N * 100], "o", color=INK)
    ax.annotate("Golden Rule: s = α = 35%, r = n", (ALPHA * 100, N * 100),
                xytext=(38, 5.2), fontsize=9, arrowprops=dict(arrowstyle="-", color=INK2))
    ax.plot([SAV * 100], [r_us * 100], "o", color=S[2])
    ax.annotate(f"US, s = 20%: r = {r_us*100:.2f}% > n", (SAV * 100, r_us * 100),
                xytext=(22, 9), fontsize=9, color=S[2],
                arrowprops=dict(arrowstyle="-", color=S[2]))
    ax.text(62, 6.2, "shaded: r < n,\ndynamically inefficient", ha="center", color=S[1], fontsize=9)
    ax.set_xlim(12, 80)
    ax.set_xlabel("saving rate s (%)")
    ax.set_ylabel("per cent a year")
    ax.set_title("Over-saving is visible in prices: past s = α the interest rate drops below n",
                 fontsize=11)
    ax.legend(loc="upper right", fontsize=9)
    out(fig, "fig_gr_r_vs_n")


# ------------------------------------------------------------ 02-markets-and-factor-prices
def fig_mk_wage_geometry():
    """Tangent to f at k: intercept = w, rise over [0, k] = r^K k."""
    k0 = 6.0
    y0, slope = f(k0), fp(k0)
    w = y0 - k0 * slope
    assert math.isclose(slope * k0 + w, y0)
    assert math.isclose(slope * k0 / y0, ALPHA)
    k = np.linspace(0, 12, 400)
    fig, ax = plt.subplots(figsize=(7, 4.2))
    ax.plot(k, f(k), color=S[0], label="f(k) = k^0.35")
    ax.plot(k, w + slope * k, color=S[1], lw=1.3, label=f"tangent at k = {k0:g}, slope r^K = f′(k) = {slope:.3f}")
    ax.plot([k0], [y0], "o", color=INK)
    ax.plot([0], [w], "o", color=S[2])
    ax.hlines(w, 0, k0, color=INK2, lw=0.8, ls="--")
    ax.annotate("", xy=(k0 + 0.3, 0), xytext=(k0 + 0.3, w),
                arrowprops=dict(arrowstyle="<->", color=S[2], lw=1.6))
    ax.text(k0 + 0.5, w / 2, f"w = f(k) − k f′(k) = {w:.3f}\n(labour share {w/y0:.0%})",
            color=S[2], fontsize=9, va="center")
    ax.annotate("", xy=(k0 + 0.3, w), xytext=(k0 + 0.3, y0),
                arrowprops=dict(arrowstyle="<->", color=S[3], lw=1.6))
    ax.text(k0 + 0.5, (w + y0) / 2, f"r^K·k = f′(k)·k = {slope*k0:.3f}\n(capital share {slope*k0/y0:.0%})",
            color=S[3], fontsize=9, va="center")
    ax.text(k0 - 0.2, y0 + 0.12, f"y = f({k0:g}) = {y0:.3f}", ha="right", fontsize=9)
    ax.text(0.2, w + 0.08, "intercept = w", color=S[2], fontsize=9)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 2.6)
    ax.set_xlabel("capital per worker, k")
    ax.set_ylabel("output per worker")
    ax.set_title("The tangent at k splits output: intercept = wage, rise = capital income",
                 fontsize=11)
    ax.legend(loc="upper left", fontsize=9)
    out(fig, "fig_mk_wage_geometry")


def fig_mk_ces_share():
    """CES capital share gamma (K/Y)^psi for three elasticities of substitution."""
    ky0 = SAV / BREAK
    ky = np.linspace(1.5, 6, 300)
    fig, ax = plt.subplots(figsize=(7, 3.8))
    for psi, col in [(-0.5, S[0]), (0.0, S[1]), (1 / 3, S[2])]:
        gamma = ALPHA / ky0 ** psi          # normalised: share 0.35 at K/Y = 3.08
        share = gamma * ky ** psi
        sigma = 1 / (1 - psi)
        lab = f"σ = {sigma:.2g}" + (" (Cobb–Douglas)" if psi == 0 else "")
        ax.plot(ky, share * 100, color=col, label=lab)
        ax.text(6.05, share[-1] * 100, f"{share[-1]*100:.0f}%", color=col, fontsize=9, va="center")
    ax.plot([ky0], [ALPHA * 100], "o", color=INK)
    ax.annotate(f"calibration: K/Y = {ky0:.2f}, share 35%", (ky0, 35), xytext=(3.4, 23),
                fontsize=9, arrowprops=dict(arrowstyle="-", color=INK2))
    ax.set_xlim(1.5, 6.5)
    ax.set_ylim(21, 52)
    ax.set_xlabel("capital–output ratio K/Y")
    ax.set_ylabel("capital share r^K K / Y (%)")
    ax.set_title("Only σ = 1 keeps the capital share flat as K/Y moves", fontsize=11)
    ax.legend(loc="upper left", fontsize=9)
    out(fig, "fig_mk_ces_share")


# ------------------------------------------------------------- 03-technological-progress
def fig_tp_breakeven():
    """Adding g to the break-even rate: k-tilde_ss falls from 8.44 to 5.64."""
    k0, k1 = k_ss(SAV, DELTA + N), k_ss(SAV, BREAK)
    assert round(k0, 2) == 8.44 and round(k1, 2) == 5.64
    k = np.linspace(0.01, 11, 400)
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(k, SAV * f(k), color=S[0], label="saving s·f(k̃), s = 0.20")
    ax.plot(k, (DELTA + N) * k, color=S[1], ls="--", label="(δ+n)k̃ — before, g = 0")
    ax.plot(k, BREAK * k, color=S[1], label="(δ+n+g)k̃ — after, g = 0.015")
    for kk, lab, dy in [(k0, "k̃_ss = {:.2f}", -0.07), (k1, "k̃_ss = {:.2f}", 0.07)]:
        yy = SAV * f(kk)
        ax.plot([kk], [yy], "o", color=INK)
        ax.vlines(kk, 0, yy, color=INK2, lw=0.8, ls=":")
        ax.text(kk + 0.15, yy + dy, lab.format(kk), fontsize=9)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 0.62)
    ax.set_xlabel("capital per efficiency unit, k̃ = K/(AL)")
    ax.set_ylabel("per efficiency unit, per year")
    ax.set_title("Adding g steepens the break-even line: k̃_ss falls from 8.44 to 5.64",
                 fontsize=11)
    ax.legend(loc="upper left", fontsize=9)
    out(fig, "fig_tp_breakeven")


def simulate(k0, s_path, T):
    """Exact discrete efficiency-unit law, as in check_growth.py; returns k-tilde path."""
    kt = np.empty(T + 1)
    kt[0] = k0
    for t in range(T):
        kt[t + 1] = ((1 - DELTA) * kt[t] + s_path[t] * f(kt[t])) / ((1 + G) * (1 + N))
    return kt


def fig_tp_bgp():
    """ln Y, ln y, ln y-tilde from a start at 40% of k-tilde_ss."""
    T = 150
    kt = simulate(0.4 * k_ss(SAV, BREAK), [SAV] * T, T)
    t = np.arange(T + 1)
    A, L = (1 + G) ** t, (1 + N) ** t
    ly_t = np.log(f(kt))
    ly = np.log(A) + ly_t
    lY = ly + np.log(L)
    assert math.isclose(math.exp(ly[-1] - ly[-2]) - 1, G, abs_tol=1e-4)
    fig, ax = plt.subplots(figsize=(7, 4))
    for series, col, lab, rate in [(lY, S[0], "aggregate Y", (1 + N) * (1 + G) - 1),
                                   (ly, S[1], "per worker y = Y/L", G),
                                   (ly_t, S[2], "per efficiency unit ỹ = Y/(AL)", 0.0)]:
        ax.plot(t, series - series[0], color=col, label=lab)
        ax.text(T + 2, series[-1] - series[0], f"slope {rate*100:.2f}%", color=col,
                fontsize=9, va="center")
    ax.set_xlim(0, T + 22)
    ax.set_xlabel("years")
    ax.set_ylabel("log level relative to year 0")
    ax.set_title("On the BGP ỹ is flat, y grows at g = 1.5%, Y at ≈ n+g", fontsize=11)
    ax.legend(loc="upper left", fontsize=9)
    out(fig, "fig_tp_bgp")


def fig_tp_level_effect():
    """s rises 0.20 -> 0.30 at t = 20: ln y shifts up, slope stays g."""
    T, t0 = 150, 20
    k0 = (SAV / ((1 + G) * (1 + N) - (1 - DELTA))) ** (1 / (1 - ALPHA))  # exact discrete ss
    base = simulate(k0, [SAV] * T, T)
    new = simulate(k0, [SAV] * t0 + [0.30] * (T - t0), T)
    t = np.arange(T + 1)
    lyb, lyn = t * math.log(1 + G) + np.log(f(base)), t * math.log(1 + G) + np.log(f(new))
    gap = ALPHA / (1 - ALPHA) * math.log(0.30 / 0.20)
    assert math.isclose(lyn[-1] - lyb[-1], gap, abs_tol=2e-3)
    assert math.isclose(lyn[-1] - lyn[-2], math.log(1 + G), abs_tol=1e-4)
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(t, lyb - lyb[0], color=S[0], ls="--", label="before: s = 0.20 throughout")
    ax.plot(t, lyn - lyb[0], color=S[0], label="after: s rises to 0.30 in year 20")
    ax.axvline(t0, color=INK2, lw=0.8, ls=":")
    ax.annotate("", xy=(T - 5, lyn[T - 5] - lyb[0]), xytext=(T - 5, lyb[T - 5] - lyb[0]),
                arrowprops=dict(arrowstyle="<->", color=S[1], lw=1.6))
    ax.annotate(f"level gap = (α/(1−α))·ln(0.30/0.20)\n= {gap:.3f} log points (+{math.exp(gap)-1:.0%})",
                (T - 5, (lyn[T - 5] + lyb[T - 5]) / 2 - lyb[0]), xytext=(80, 0.45),
                color=S[1], fontsize=9, arrowprops=dict(arrowstyle="-", color=S[1]))
    ax.text(t0 + 1, 0.05, "s rises", fontsize=9, color=INK2)
    ax.set_xlabel("years")
    ax.set_ylabel("ln y relative to year 0")
    ax.set_title("A higher s raises the level of the path; both end with slope g", fontsize=11)
    ax.legend(loc="upper left", fontsize=9)
    out(fig, "fig_tp_level_effect")


# --------------------------------------------------------- 04-quantifying-and-convergence
def fig_q_growth_vs_k():
    """Eq. (5.3.1) with n = g = 0 against the exact one-period growth rate."""
    kss = k_ss(SAV, DELTA)
    k = np.linspace(0.5, 16, 400)
    approx = SAV * fp(k) - DELTA * ALPHA
    exact = f(k + SAV * f(k) - DELTA * k) / f(k) - 1
    assert math.isclose(SAV * fp(kss) - DELTA * ALPHA, 0, abs_tol=1e-12)
    assert np.all(np.diff(approx) < 0)
    fig, ax = plt.subplots(figsize=(7, 3.8))
    ax.plot(k, approx * 100, color=S[0], label="(5.3.1): g_y ≈ s f′(k) − δα")
    ax.plot(k, exact * 100, color=S[1], ls="--", label="exact: f(k_{t+1})/f(k_t) − 1")
    ax.axhline(0, color=INK2, lw=0.8)
    ax.plot([kss], [0], "o", color=INK)
    ax.annotate(f"steady state k = {kss:.1f}: g_y = 0", (kss, 0), xytext=(9.5, 2.2),
                fontsize=9, arrowprops=dict(arrowstyle="-", color=INK2))
    for kk in (1.0, 3.0):
        gy = SAV * fp(kk) - DELTA * ALPHA
        ax.plot([kk], [gy * 100], "o", color=S[0])
        ax.text(kk + 0.3, gy * 100 + 0.25, f"k = {kk:g}: {gy*100:.1f}%", fontsize=9, color=S[0])
    ax.set_xlim(0, 16)
    ax.set_xlabel("capital per worker, k (same f, same s)")
    ax.set_ylabel("growth of y (% per year)")
    ax.set_title("Under Conjecture 5.1 the poorer economy always grows faster", fontsize=11)
    ax.legend(loc="upper right", fontsize=9)
    out(fig, "fig_q_growth_vs_k")


def decay_path(start_ratio, years, dt=1e-2):
    """x_t / x_0 from Euler-integrating the continuous law, sampled yearly."""
    kss = k_ss(SAV, BREAK)
    kk = kss * start_ratio
    x0 = math.log(start_ratio)
    res, steps = [1.0], int(round(1 / dt))
    for _ in range(years):
        for _ in range(steps):
            kk += dt * (SAV * f(kk) - BREAK * kk)
        res.append((math.log(kk) - math.log(kss)) / x0)
    return np.array(res)


def fig_q_loglin():
    """Normalised log gap x_t/x_0: model lambda, simulation from 50% below, data lambda."""
    lam = (1 - ALPHA) * BREAK
    hl, hl_data = math.log(2) / lam, math.log(2) / 0.02
    assert round(hl, 1) == 16.4 and round(hl_data) == 35
    Y = 70
    t = np.arange(Y + 1)
    sim = decay_path(0.5, Y)
    assert math.isclose(sim[10], 0.6025, abs_tol=2e-3)
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(t, np.exp(-lam * t), color=S[0], label=f"log-linear model, λ = {lam:.4f}")
    ax.plot(t, sim, color=S[1], ls="--", label="exact model path, start 50% below k̃_ss")
    ax.plot(t, np.exp(-0.02 * t), color=S[2], label="convergence regressions, λ ≈ 0.02")
    ax.axhline(0.5, color=INK2, lw=0.8, ls=":")
    for h, col in [(hl, S[0]), (hl_data, S[2])]:
        ax.plot([h], [0.5], "o", color=col)
        ax.text(h + 1, 0.53, f"half-life {h:.1f} yrs", color=col, fontsize=9)
    ax.set_xlim(0, Y)
    ax.set_ylim(0, 1.02)
    ax.set_xlabel("years")
    ax.set_ylabel("remaining log gap x_t / x_0")
    ax.set_title("The model closes half the gap in 16.4 years; the data take about 35",
                 fontsize=11)
    ax.legend(loc="upper right", fontsize=9)
    out(fig, "fig_q_loglin")


def fig_q_lucas():
    """Eq. (5.3.4): rental-rate ratio x^((alpha-1)/alpha) for alpha = 0.35 and 0.7."""
    x = np.linspace(0.1, 1, 300)
    xm = 0.3
    fig, ax = plt.subplots(figsize=(7, 4))
    for a, col in [(ALPHA, S[0]), (0.7, S[1])]:
        ax.plot(x, x ** ((a - 1) / a), color=col, label=f"α = {a:g}: exponent (α−1)/α = {(a-1)/a:.3f}")
        rm = xm ** ((a - 1) / a)
        ax.plot([xm], [rm], "o", color=col)
        ax.text(xm + 0.02, rm * 1.12, f"Mexico: {rm:.2f}×", color=col, fontsize=9)
    assert round(xm ** ((ALPHA - 1) / ALPHA), 1) == 9.4
    assert round(xm ** ((0.7 - 1) / 0.7), 1) == 1.7
    ax.set_yscale("log")
    ax.set_yticks([1, 2, 5, 10, 20, 50, 100])
    ax.set_yticklabels(["1", "2", "5", "10", "20", "50", "100"])
    ax.axvline(xm, color=INK2, lw=0.8, ls=":")
    ax.set_xlabel("income ratio x = y_poor / y_rich")
    ax.set_ylabel("implied r^K_poor / r^K_rich (log scale)")
    ax.set_title("With α = 0.35, Mexico's income gap implies a rental rate 9.4× the US one",
                 fontsize=11)
    ax.legend(loc="upper right", fontsize=9)
    out(fig, "fig_q_lucas")


# ---------------------------------------------------------- 05-growth-accounting-and-tfp
def fig_ga_growth():
    """Growth accounting of the check-script example, aggregate and per worker."""
    gY, gK, gL = 0.031, 0.036, 0.011
    gA = gY - ALPHA * gK - (1 - ALPHA) * gL
    assert math.isclose(gA, 0.01125)
    rows = [("output Y\ng_Y = 3.10%", [ALPHA * gK, (1 - ALPHA) * gL, gA]),
            ("output per worker y\ng_y = 2.00%", [ALPHA * (gK - gL), 0.0, gA])]
    labels = ["capital: α·g_K (α·g_k)", "labour: (1−α)·g_L", "residual g_A"]
    cols = [S[0], S[3], S[2]]
    fig, ax = plt.subplots(figsize=(7, 3.4))
    for i, (name, parts) in enumerate(rows):
        left = 0.0
        for j, p in enumerate(parts):
            if p == 0:
                continue
            ax.barh(i, p * 100, left=left, color=cols[j], label=labels[j] if i == 0 else None)
            ax.text(left + p * 50, i, f"{p*100:.3f}".rstrip("0"), ha="center", va="center",
                    color="white", fontsize=9, fontweight="bold")
            left += p * 100
    ax.set_yticks([0, 1])
    ax.set_yticklabels([r[0] for r in rows])
    ax.invert_yaxis()
    ax.set_xlabel("percentage points per year")
    ax.grid(axis="y", visible=False)
    ax.set_title("The residual g_A = 1.125 pp is what the inputs leave unexplained",
                 fontsize=11)
    ax.set_ylim(1.75, -1.0)
    ax.legend(loc="upper center", ncol=3, fontsize=9)
    out(fig, "fig_ga_growth")


def fig_ga_dev_forms():
    """Share of the log income gap by source, K/L form against K/Y form."""
    y_rel, k_rel, ky_rel = 0.10, 0.15, 0.8
    h_rel = math.exp(0.10 * (4 - 12))
    ln_gap = math.log(y_rel)
    kl = [ALPHA * math.log(k_rel), (1 - ALPHA) * math.log(h_rel)]
    ky = [ALPHA / (1 - ALPHA) * math.log(ky_rel), math.log(h_rel)]
    kl.append(ln_gap - sum(kl))
    ky.append(ln_gap - sum(ky))
    kl, ky = [100 * v / ln_gap for v in kl], [100 * v / ln_gap for v in ky]
    assert round(kl[0], 1) == 28.8 and round(kl[0] + kl[1]) == 51
    assert round(ky[0], 1) == 5.2 and round(ky[0] + ky[1]) == 40
    labels = ["physical capital", "human capital", "TFP (residual)"]
    cols = [S[0], S[1], S[2]]
    fig, ax = plt.subplots(figsize=(7, 3.4))
    for i, parts in enumerate([kl, ky]):
        left = 0.0
        for j, p in enumerate(parts):
            ax.barh(i, p, left=left, color=cols[j], label=labels[j] if i == 0 else None)
            if p > 8:
                ax.text(left + p / 2, i, f"{p:.1f}%", ha="center", va="center", color="white",
                        fontsize=9, fontweight="bold")
            else:
                ax.text(left, i + 0.48, f"{p:.1f}%", va="top", color=cols[j], fontsize=9)
            left += p
    ax.set_yticks([0, 1])
    ax.set_yticklabels(["K/L form\ny = A k^α h^(1−α)", "K/Y form\ny = A^(1/(1−α)) (K/Y)^(α/(1−α)) h"],
                       fontsize=9)
    ax.invert_yaxis()
    ax.set_xlim(0, 100)
    ax.set_xlabel("share of the log income gap ln(0.10) (%)")
    ax.grid(axis="y", visible=False)
    ax.set_title("Two decompositions of one gap: TFP takes 49% or 60% of it",
                 fontsize=11)
    ax.set_ylim(1.75, -1.0)
    ax.legend(loc="upper center", ncol=3, fontsize=9)
    out(fig, "fig_ga_dev_forms")


def main():
    """Build every figure; `--png DIR` also writes previews."""
    global PNG_DIR
    if "--png" in sys.argv:
        PNG_DIR = pathlib.Path(sys.argv[sys.argv.index("--png") + 1])
    fig_gr_geometry()
    fig_gr_r_vs_n()
    fig_mk_wage_geometry()
    fig_mk_ces_share()
    fig_tp_breakeven()
    fig_tp_bgp()
    fig_tp_level_effect()
    fig_q_growth_vs_k()
    fig_q_loglin()
    fig_q_lucas()
    fig_ga_growth()
    fig_ga_dev_forms()


if __name__ == "__main__":
    main()
