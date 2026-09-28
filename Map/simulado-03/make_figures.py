#!/usr/bin/env python3
"""Figures for the Simulado 3 solution notes (Map/simulado-03/q*.md).

Each figure carries the argument of one exam item. Parameters are the ones stated in the
exam; the numbers quoted in the notes are asserted in
Simulados/simulado_codigo/check_simulado_03.py, not here.

Run: python Map/simulado-03/make_figures.py   (writes Map/simulado-03/fig/*.svg)
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "fig"))
from mapstyle import INK, INK2, S, save  # noqa: E402

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Ellipse, FancyBboxPatch  # noqa: E402

FIG = HERE / "fig"


def arrow(ax, xy_from, xy_to, color=INK2):
    ax.annotate("", xy=xy_to, xytext=xy_from,
                arrowprops=dict(arrowstyle="->", color=color, lw=1.5))


# ---------------------------------------------------------------- Q1 index numbers
def q1_index():
    fig, ax = plt.subplots(figsize=(6.4, 3.2))
    names = ["Year-1 prices\n(Laspeyres)", "Fisher\n(geometric mean)", "Year-2 prices\n(Paasche)"]
    vals = [70.0, 48.1, 28.9]
    bars = ax.barh(names, vals, color=[S[1], S[2], S[0]])
    for b, v in zip(bars, vals):
        ax.text(v + 1, b.get_y() + b.get_height() / 2, f"{v:.1f}%", va="center", color=INK)
    ax.set_xlim(0, 85)
    ax.invert_yaxis()
    ax.set_xlabel("Measured real growth, year 1 to year 2 (%)")
    ax.set_title("Old prices overweight the good that got cheap",
                 fontsize=9, loc="left")
    save(fig, FIG / "q1_index_bias.svg")


def q1_baskets():
    fig, ax = plt.subplots(figsize=(6.4, 3.0))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")
    ax.add_patch(FancyBboxPatch((0.3, 0.5), 5.2, 3.8, boxstyle="round,pad=0.1", fc="none",
                                ec=S[0], lw=2))
    ax.add_patch(FancyBboxPatch((4.2, 0.9), 5.4, 3.0, boxstyle="round,pad=0.1", fc="none",
                                ec=S[1], lw=2))
    ax.text(0.5, 4.5, "GDP deflator: everything PRODUCED here", color=S[0], fontsize=9)
    ax.text(5.7, 4.05, "CPI: what households BUY", color=S[1], fontsize=9)
    ax.text(0.7, 3.2, "iron ore exports\nmachinery, public services", fontsize=8.5, color=INK2)
    ax.text(4.5, 2.2, "food, rent,\nhaircuts", fontsize=8.5, color=INK)
    ax.text(6.9, 1.5, "IMPORTED TVs\n(price up 30%)", fontsize=9, color=S[1], weight="bold")
    save(fig, FIG / "q1_deflator_cpi.svg")


# ---------------------------------------------------------------- Q2 Brazil vs Paraguay
def q2_percapita():
    t = np.arange(0, 11)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.4, 3.1), sharey=True)
    a1.plot(t, 100 * 1.035 ** t, color=S[1], label="Paraguay (3.5%)")
    a1.plot(t, 100 * 1.025 ** t, color=S[0], label="Brazil (2.5%)")
    a1.set_title("Aggregate real GDP, index", fontsize=9, loc="left")
    a2.plot(t, 100 * (1.035 / 1.02) ** t, color=S[1], label="Paraguay (1.47%)")
    a2.plot(t, 100 * (1.025 / 1.005) ** t, color=S[0], label="Brazil (1.99%)")
    a2.set_title("Real GDP per capita, index", fontsize=9, loc="left")
    for a in (a1, a2):
        a.set_xlabel("years")
        a.legend(fontsize=8)
    a1.set_ylabel("year 0 = 100")
    save(fig, FIG / "q2_aggregate_vs_percapita.svg")


def q2_ppp():
    fig, ax = plt.subplots(figsize=(6.4, 3.2))
    labels = ["market rate\n(per capita)", "PPP\n(per capita)", "PPP\n(per worker)"]
    br = [9000, 16364, 36364]
    py = [6000, 15000, 30000]
    x = np.arange(3)
    ax.bar(x - 0.18, br, 0.36, color=S[0], label="Brazil")
    ax.bar(x + 0.18, py, 0.36, color=S[1], label="Paraguay")
    for i, (b, p) in enumerate(zip(br, py)):
        ax.text(i, max(b, p) + 1200, f"ratio {b / p:.2f}", ha="center", fontsize=8.5, color=INK)
    ax.set_xticks(x, labels)
    ax.set_ylabel("USD")
    ax.set_ylim(0, 42000)
    ax.legend(fontsize=8, loc="upper left")
    save(fig, FIG / "q2_ppp_denominators.svg")


# ---------------------------------------------------------------- Q3 Solow
def q3_convergence():
    a, nd = 1 / 3, 0.07
    k = np.linspace(0.3, 60, 400)
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    k = np.linspace(0.8, 80, 400)
    sp, sr = 0.07 * 5 ** (2 / 3), 0.07 * 60 ** (2 / 3)   # s*A giving k* = 5 and k* = 60
    for sA, c, lab in [(sp, S[1], "poor country: low $s$, low $A$ ($k^*=5$)"),
                       (sr, S[0], "rich country: high $s$, high $A$ ($k^*=60$)")]:
        ax.plot(k, sA * k ** (a - 1), color=c, label=lab)
    ax.axhline(nd, color=INK2, lw=1.4)
    ax.text(52, nd + 0.006, "$n+\\delta$", color=INK2)
    ax.plot([4], [sp * 4 ** (a - 1)], "o", color=S[1])
    ax.plot([21], [sr * 21 ** (a - 1)], "o", color=S[0])
    ax.annotate("poor, at 80% of its own $k^*$:\nsmall gap, slow growth", (4, sp * 4 ** (a - 1)),
                xytext=(8, 0.22), fontsize=8, arrowprops=dict(arrowstyle="->", color=INK2))
    ax.annotate("richer, at 35% of its $k^*$:\nlarge gap, fast growth", (21, sr * 21 ** (a - 1)),
                xytext=(35, 0.19), fontsize=8, arrowprops=dict(arrowstyle="->", color=INK2))
    ax.set_ylim(0, 0.3)
    ax.set_xlabel("capital per worker $k$")
    ax.set_ylabel("growth of $k$ = vertical gap")
    ax.legend(fontsize=8, loc="upper right")
    save(fig, FIG / "q3_conditional_convergence.svg")


def q3_nfall():
    a, s_, d = 1 / 3, 0.2, 0.05
    k = np.linspace(0, 12, 300)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 3.2))
    a1.plot(k, s_ * k ** a, color=S[0], label="$s\\,k^{\\alpha}$")
    a1.plot(k, 0.07 * k, color=S[1], label="$(n+\\delta)k$, $n=2\\%$")
    a1.plot(k, 0.06 * k, color=S[2], label="$(n'+\\delta)k$, $n'=1\\%$")
    k0, k1 = (s_ / 0.07) ** 1.5, (s_ / 0.06) ** 1.5
    for kk, c in [(k0, S[1]), (k1, S[2])]:
        a1.axvline(kk, color=c, lw=0.8, ls="--")
    a1.set_xlabel("$k$")
    a1.legend(fontsize=7.5, loc="upper left")
    a1.set_title("Mechanism: flatter break-even line", fontsize=9, loc="left")
    # time paths
    T = 120
    kt, lny, lnY = k0, [], []
    L = 1.0
    for t in range(T):
        n = 0.02 if t < 20 else 0.01
        lny.append(a * np.log(kt))
        lnY.append(a * np.log(kt) + np.log(L))
        kt = (s_ * kt ** a + (1 - d) * kt) / (1 + n)
        L *= 1 + n
    tt = np.arange(T)
    a2.plot(tt, np.array(lny) - lny[0], color=S[0], label="$\\ln y$ (per capita)")
    a2.plot(tt, (np.array(lnY) - lnY[0]) / 10, color=S[1], label="$\\ln Y$ / 10 (aggregate)")
    a2.axvline(20, color=INK2, lw=0.8, ls=":")
    a2.text(21, 0.02, "$n$ falls", fontsize=8, color=INK2)
    a2.set_xlabel("time")
    a2.legend(fontsize=7.5)
    a2.set_title("Paths: $y$ level up, $Y$ slope down", fontsize=9, loc="left")
    save(fig, FIG / "q3_fall_in_n.svg")


# ---------------------------------------------------------------- Q4 compliance wedge
def q4_wedge():
    fig, ax = plt.subplots(figsize=(6.4, 2.8))
    vals = [1.0, 1.25 ** (-2 / 3), 1.10 ** (-2 / 3)]
    names = ["true $A$", "measured $\\hat A$, $\\varphi=0.25$", "measured $\\hat A$, $\\varphi=0.10$"]
    bars = ax.barh(names, vals, color=[INK2, S[1], S[2]])
    for b, v in zip(bars, vals):
        ax.text(v + 0.01, b.get_y() + b.get_height() / 2, f"{v:.3f}", va="center")
    ax.set_xlim(0, 1.2)
    ax.invert_yaxis()
    ax.set_xlabel("relative to true $A$")
    ax.set_title("The observer's TFP is $A(1+\\varphi)^{-(1-\\alpha)}$: the wedge sits inside it",
                 fontsize=9, loc="left")
    save(fig, FIG / "q4_measured_tfp.svg")


def q4_accounting():
    fig, ax = plt.subplots(figsize=(6.4, 2.6))
    gK, gL = 0.03, 0.01
    parts = [("$\\alpha g_K$", gK / 3, S[0]), ("$(1-\\alpha)g_L$", 2 * gL / 3, S[2]),
             ("residual (all of it the reform)", 0.017044, S[1])]
    left = 0
    for lab, v, c in parts:
        ax.barh([0], [100 * v], left=100 * left, color=c)
        ax.text(100 * (left + v / 2), 0, lab + f"\n{100 * v:.2f}", ha="center", va="center",
                fontsize=8, color="white")
        left += v
    ax.set_yticks([])
    ax.set_xlabel("contribution to $g_Y$, % a year (illustrative $g_K=3\\%$, $g_L=1\\%$)")
    ax.set_xlim(0, 100 * left * 1.05)
    save(fig, FIG / "q4_growth_accounting.svg")


def q4_transition():
    a, s_, nd = 1 / 3, 0.2, 0.07
    A0, A1 = 1.25 ** (-2 / 3), 1.10 ** (-2 / 3)
    k = np.linspace(0, 8, 300)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 3.2))
    a1.plot(k, s_ * A0 * k ** a, color=S[1], label="$s\\hat A k^\\alpha$ before")
    a1.plot(k, s_ * A1 * k ** a, color=S[2], label="$s\\hat A' k^\\alpha$ after")
    a1.plot(k, nd * k, color=INK2, label="$(n+\\delta)k$")
    a1.set_xlabel("$k$")
    a1.legend(fontsize=7.5, loc="upper left")
    a1.set_title("Mechanism: saving curve shifts up", fontsize=9, loc="left")
    kt = (s_ * A0 / nd) ** 1.5
    ys, gs = [], []
    for t in range(80):
        A = A0 if t < 5 else A1
        y = A * kt ** a
        ys.append(y)
        kt = kt + s_ * y - nd * kt
    ys = np.array(ys)
    a2.plot(np.arange(80), ys / ys[0], color=S[0])
    a2.axhline(1.25 / 1.10, color=S[2], lw=0.8, ls="--")
    a2.text(35, 1.112, "new $y^*$: +13.6%", fontsize=8, color=S[2])
    a2.text(10, 1.07, "jump: +8.9% (TFP)", fontsize=8, color=S[1])
    a2.set_xlabel("time (reform at $t=5$)")
    a2.set_ylabel("$y_t/y_0$")
    a2.set_title("Path: jump, then capital deepening", fontsize=9, loc="left")
    save(fig, FIG / "q4_transition.svg")


# ---------------------------------------------------------------- Q5 labour and search
def q5_labour():
    tau = np.linspace(0, 0.6, 200)
    fig, ax = plt.subplots(figsize=(6.4, 3.2))
    for T, c in [(0.0, S[0]), (0.1, S[1]), (0.2, S[2])]:
        ax.plot(tau, 0.5 - 0.5 * T / (1 - tau), color=c, label=f"$T={T}$")
    ax.set_xlabel("labour-income tax $\\tau$")
    ax.set_ylabel("hours $n$")
    ax.legend(fontsize=8)
    ax.set_title("$n=\\frac{1}{1+b}-\\frac{b}{1+b}\\frac{T}{(1-\\tau)w}$ ($b=w=1$): flat when $T=0$",
                 fontsize=9, loc="left")
    save(fig, FIG / "q5_hours_vs_tax.svg")


def q5_beveridge():
    u = np.linspace(0.03, 0.14, 300)

    def v(u, mu, s=0.02):
        return (s * (1 - u) / mu) ** 2 / u

    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.plot(100 * u, 100 * v(u, 0.5), color=S[0], label="$\\mu=0.5$")
    ax.plot(100 * u, 100 * v(u, 0.4), color=S[1], label="$\\mu=0.4$ (worse matching)")
    for uu, lab, xy in [(0.08, "slack: $\\theta=0.21$", (8.3, 1.2)),
                        (0.06, "tight: $\\theta=0.39$", (3.6, 2.2))]:
        vv = v(uu, 0.5)
        ax.plot([0, 100 * uu * 1.4], [0, 100 * vv * 1.4], color=INK2, lw=0.8, ls=":")
        ax.plot(100 * uu, 100 * vv, "o", color=S[0])
        ax.text(*xy, lab, fontsize=8)
    arrow(ax, (8, 100 * v(0.08, 0.5)), (6.1, 100 * v(0.06, 0.5)), S[0])
    ax.text(4.2, 0.35, "movement along:\n$\\theta$ changes, $\\mu$ fixed", fontsize=8, color=S[0])
    arrow(ax, (8, 100 * v(0.08, 0.5)), (8, 100 * v(0.08, 0.4)), S[1])
    ax.text(9.6, 3.3, "shift: $\\mu$ falls,\nmore $v$ at the same $u$", fontsize=8, color=S[1])
    ax.set_xlim(2, 14)
    ax.set_ylim(0, 6)
    ax.set_xlabel("unemployment rate $u$ (%)")
    ax.set_ylabel("vacancy rate $v$ (%)")
    ax.legend(fontsize=8)
    save(fig, FIG / "q5_beveridge.svg")


# ---------------------------------------------------------------- Q6 consumption and GE
def q6_sigma():
    r = np.linspace(0.0, 0.12, 200)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 3.2))
    for sig, c in [(0.5, S[0]), (1.0, INK2), (2.0, S[1])]:
        D = 1 + 0.96 ** (1 / sig) * (1 + r) ** (1 / sig - 1)
        a1.plot(100 * r, 100 / D, color=c, label=f"$\\sigma={sig}$")
    a1.set_xlabel("$r$ (%)")
    a1.set_ylabel("$c_1$ of a saver ($y_1=100$, $y_2=0$)")
    a1.legend(fontsize=8)
    a1.set_title("PE: sign of $\\partial c_1/\\partial r$ = sign of $\\sigma-1$", fontsize=9, loc="left")
    g = np.linspace(0.98, 1.05, 200)
    for sig, c in [(0.5, S[0]), (1.0, INK2), (2.0, S[1])]:
        a2.plot(100 * (g - 1), 100 * (g ** sig / 0.96 - 1), color=c, label=f"$\\sigma={sig}$")
    a2.axhline(100 * (1 / 0.96 - 1), color=INK2, lw=0.8, ls=":")
    a2.text(-1.9, 4.6, "$\\rho=4.17\\%$", fontsize=8)
    a2.set_xlabel("endowment growth $y_2/y_1-1$ (%)")
    a2.set_ylabel("equilibrium $r$ (%)")
    a2.set_title("GE, frozen factors: $1+r=(y_2/y_1)^\\sigma/\\beta$", fontsize=9, loc="left")
    a2.legend(fontsize=8)
    save(fig, FIG / "q6_sigma_and_ge.svg")


def q6_ricardo():
    fig, ax = plt.subplots(figsize=(6.4, 3.8))
    R = 1.05
    c1 = np.linspace(0, 110, 300)
    W = 100
    ax.plot(c1, R * (W - c1), color=INK2, lw=1.2, label="PV budget line ($W=100$), both plans")
    # borrowing limits a >= -15: c1 <= y1 - tau1 + 15
    for x1, c, lab in [(45, S[1], "limit before swap: $c_1\\leq 30+15$"),
                       (55, S[2], "limit after swap: $c_1\\leq 40+15$")]:
        ax.axvline(x1, color=c, ls="--", lw=1.2, label=lab)
    ax.plot([30], [73.5], "s", color=S[1])
    ax.text(31, 76, "endowment before", fontsize=8, color=S[1])
    ax.plot([40], [63.0], "s", color=S[2])
    ax.text(42, 66, "endowment after", fontsize=8, color=S[2])
    ax.plot([51.22], [51.22], "o", color=S[0])
    ax.text(57, 53, "unconstrained optimum (51.2, 51.2)", fontsize=8, color=S[0])
    ax.plot([45], [57.75], "o", color=S[1])
    ax.text(12, 43, "constrained before: (45, 57.75)", fontsize=8, color=S[1])
    ax.set_xlim(0, 110)
    ax.set_ylim(0, 120)
    ax.set_xlabel("$c_1$")
    ax.set_ylabel("$c_2$")
    ax.legend(fontsize=7.5, loc="upper right")
    save(fig, FIG / "q6_ricardo_limit.svg")


def q6_savings_tax():
    beta, r, t, y1 = 0.96, 0.05, 0.02, 100.0
    c1T, aT = y1 / (1 + beta), y1 - y1 / (1 + beta)
    c2T = (1 + r - t) * aT
    Rv = t * aT
    WL = y1 - Rv / (1 + r)
    c1L = WL / (1 + beta)
    c2L = beta * (1 + r) * c1L
    # The tax plan lies on the lump-sum budget line (same revenue), so both are affordable
    # there; drawn as budget lines they nearly coincide, so show the two consequences instead.
    assert abs(c2T - (1 + r) * (WL - c1T)) < 1e-9
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.0, 3.6))
    ratios = [beta * (1 + r), beta * (1 + r), beta * (1 + r - t)]
    names = ["no tax", "lump sum", "savings tax"]
    a1.bar(names, ratios, color=[INK2, S[0], S[1]], width=0.55)
    for k, v in enumerate(ratios):
        a1.text(k, v + 0.0015, f"{v:.4f}", ha="center", fontsize=8.5, color=INK2)
    a1.set_ylim(0.97, 1.02)
    a1.set_ylabel("$c_2/c_1$ chosen (log utility)")
    a1.set_title("1. The savings tax moves the Euler ratio;\nthe lump sum does not", fontsize=9, loc="left")
    a1.grid(axis="x", visible=False)
    # utility along the lump-sum budget line, in excess of its maximum
    c1 = np.linspace(c1L - 2.0, c1L + 2.0, 300)
    U = np.log(c1) + beta * np.log((1 + r) * (WL - c1))
    Umax = np.log(c1L) + beta * np.log(c2L)
    a2.plot(c1, 1e4 * (U - Umax), color=S[0], label="utility along the lump-sum line")
    for x, c, lab, off, ha in [(c1L, S[0], "lump-sum choice", (-12, -28), "right"),
                               (c1T, S[1], "savings-tax plan", (12, -28), "left")]:
        u = np.log(x) + beta * np.log((1 + r) * (WL - x))
        a2.plot([x], [1e4 * (u - Umax)], "o", ms=8, color=c)
        a2.annotate(f"{lab}\nc1 = {x:.2f}", (x, 1e4 * (u - Umax)), xytext=off, ha=ha,
                    textcoords="offset points", fontsize=8, color=c)
    a2.set_xlabel("$c_1$ on the lump-sum budget line")
    a2.set_ylabel("utility − max (×10⁻⁴)")
    a2.set_title("2. The tax plan is affordable under the lump sum\nbut not chosen: it is worse", fontsize=9, loc="left")
    save(fig, FIG / "q6_savings_tax.svg")


# ---------------------------------------------------------------- Q7 money
def q7_identity():
    fig, ax = plt.subplots(figsize=(6.4, 2.8))
    items = [("$g_M$", 10.0, S[0]), ("$\\pi$", 6.0, S[1]), ("$g_Y$", 3.0, S[2]),
             ("$g_V$ (residual)", -0.75, S[3])]
    for i, (lab, v, c) in enumerate(items):
        ax.bar(i, v, color=c)
        ax.text(i, v + (0.3 if v > 0 else -0.8), f"{v:+.2f}%", ha="center", fontsize=8.5)
    ax.axhline(0, color=INK2, lw=0.8)
    ax.set_xticks(range(4), [x[0] for x in items])
    ax.set_ylim(-2, 12)
    ax.set_title("$(1+g_M)(1+g_V)=(1+\\pi)(1+g_Y)$ holds by construction: $V$ absorbs the rest",
                 fontsize=9, loc="left")
    save(fig, FIG / "q7_identity.svg")


def q7_superneutral():
    i = np.linspace(0.02, 0.2, 200)
    m = np.sqrt(0.06 / i)          # normalised so m(6%) = 1
    fig, ax = plt.subplots(figsize=(6.4, 3.2))
    ax.plot(100 * i, m, color=S[0], label="real balances $m=\\sqrt{FY/2i}$ (index)")
    ax.plot(100 * i, 1 / m, color=S[1], label="velocity $V=Y/m$ (index)")
    for ii in (0.06, 0.12):
        ax.axvline(100 * ii, color=INK2, lw=0.8, ls=":")
    ax.text(6.3, 1.9, "$\\mu=4\\%$\n$i=6\\%$", fontsize=8)
    ax.text(12.3, 1.9, "$\\mu=10\\%$\n$i=12\\%$", fontsize=8)
    ax.set_xlabel("nominal interest rate $i$ (%)")
    ax.set_ylim(0, 2.2)
    ax.legend(fontsize=8, loc="lower right")
    save(fig, FIG / "q7_superneutrality.svg")


# ---------------------------------------------------------------- Q8 NK
def q8_regimes():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 3.1))
    m = np.linspace(0.5, 3, 200)
    for ax, title in [(a1, "Bank sets $M$: $i$ is endogenous"),
                      (a2, "Bank sets $i$: $M$ is endogenous")]:
        ax.plot(m, 1.2 / m, color=S[0], label="$m^D(Y,i)$")
        ax.plot(m, 1.2 / m * 1.35, color=S[0], ls="--", lw=1.2, label="$m^D$ after $Y\\uparrow$")
        ax.set_xlabel("real balances $M/p$")
        ax.set_ylabel("$i$")
        ax.set_title(title, fontsize=9, loc="left")
        ax.set_ylim(0, 2.5)
    a1.axvline(1.2, color=S[1], label="$M^S/\\bar p$ fixed")
    a1.plot([1.2, 1.2], [1.0, 1.35], "o", color=S[1])
    a1.text(1.3, 1.45, "$i$ rises", fontsize=8)
    a2.axhline(1.0, color=S[1], label="$i$ target fixed")
    a2.plot([1.2, 1.62], [1.0, 1.0], "o", color=S[1])
    a2.text(1.3, 1.1, "$M$ supplied rises", fontsize=8)
    for ax in (a1, a2):
        ax.legend(fontsize=7, loc="upper right")
    save(fig, FIG / "q8_money_regimes.svg")


def asad(ax, yn, title, show_opt=False):
    s_, k = 0.5, 1.133
    y = np.linspace(-4, 2.5, 200)
    ax.plot(y, 0 + k * (y - 0), color=S[1], lw=1.2, ls="--", label="AS before")
    ax.plot(y, k * (y - yn), color=S[1], label="AS after ($y_n'=-2$)")
    ax.plot(y, -(y - 0) / s_, color=S[0], label="AD ($i$ unchanged)")
    dy = s_ * k / (1 + s_ * k) * yn
    dp = -k * yn / (1 + s_ * k)
    ax.plot([0], [0], "o", color=INK2)
    ax.plot([dy], [dp], "o", color=S[1])
    ax.text(dy + 0.15, dp + 0.2, f"E'  ({dy:.2f}, {dp:+.2f})", fontsize=7.5)
    ax.axvline(yn, color=INK2, lw=0.8, ls=":")
    ax.text(yn + 0.05, -3.6, "$y_n'$", fontsize=8)
    ax.set_xlim(-4, 2.5)
    ax.set_ylim(-4, 4)
    ax.set_xlabel("output $y$ (% from initial $y_n$)")
    ax.set_ylabel("$p-p^e$ (%)")
    ax.set_title(title, fontsize=9, loc="left")
    ax.axhline(0, color=INK2, lw=0.6)


def q8_productivity():
    fig, ax = plt.subplots(figsize=(6.4, 3.8))
    asad(ax, -2.0, "Drought: AS shifts, AD stays; $y_e$ moves with $y_n$")
    # AD after raising i to r_n: shifts down by 4 so it passes (y_n', 0)
    y = np.linspace(-4, 2.5, 200)
    ax.plot(y, -(y + 2) / 0.5, color=S[2], label="AD after $i=r_n'$ (+4 pp)")
    ax.plot([-2], [0], "o", color=S[2])
    ax.text(-3.9, 0.25, "both gaps 0", fontsize=8, color=S[2])
    ax.legend(fontsize=7.5, loc="upper right")
    save(fig, FIG / "q8_productivity.svg")


def q8_markup():
    s_, k, th = 0.5, 1.133, 8.0
    fig, ax = plt.subplots(figsize=(6.4, 3.8))
    y = np.linspace(-4, 1, 200)
    ax.plot(y, k * (y + 2), color=S[1], label="AS after the mark-up shock")
    ax.axvline(0, color=INK2, lw=0.8, ls=":")
    ax.text(0.05, -2.6, "$y_e$ (unchanged)", fontsize=8)
    pts = {"E': no response": (-0.723, 1.447), "E'': $p=p^e$": (-2.0, 0.0),
           "E''': $y=y_e$": (0.0, 2.266), "optimum": (-1.801, 0.225)}
    cols = [INK2, S[0], S[3], S[2]]
    for (lab, (x, p)), c in zip(pts.items(), cols):
        ax.plot([x], [p], "o", color=c)
        dx = -0.95 if x == -2.0 else 0.08
        ax.text(x + dx, p - 0.35, lab, fontsize=7.5, color=c)
    # iso-loss ellipses (y-y_e)^2 + (theta/kappa)(p-p^e)^2 = L, centred at (0, 0)
    Lo = (-1.801) ** 2 + th / k * 0.225 ** 2
    for f in (0.5, 1.0, 1.6):
        LL = Lo * f
        ax.add_patch(Ellipse((0, 0), 2 * np.sqrt(LL), 2 * np.sqrt(LL * k / th), fill=False,
                             ec=S[2], lw=0.9, ls="-" if f == 1 else ":"))
    ax.plot([0], [0], "+", color=S[2], ms=10)
    ax.text(0.08, 0.1, "bliss $(y_e,p^e)$", fontsize=7.5, color=S[2])
    ax.set_xlim(-4, 1)
    ax.set_ylim(-3, 3)
    ax.set_xlabel("$y-y_e$ (%)")
    ax.set_ylabel("$p-p^e$ (%)")
    ax.set_title("AS is the menu: the bank slides AD along it; best point = tangency", fontsize=9,
                 loc="left")
    ax.legend(fontsize=7.5, loc="upper left")
    save(fig, FIG / "q8_markup_tradeoff.svg")


if __name__ == "__main__":
    for f in [q1_index, q1_baskets, q2_percapita, q2_ppp, q3_convergence, q3_nfall, q4_wedge,
              q4_accounting, q4_transition, q5_labour, q5_beveridge, q6_sigma, q6_ricardo,
              q6_savings_tax, q7_identity, q7_superneutral, q8_regimes, q8_productivity,
              q8_markup]:
        f()
