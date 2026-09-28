#!/usr/bin/env python3
"""Figures for the notes in Map/aula-01-mensuracao.

Every number drawn or labelled is computed here and asserted against the value the
note quotes, so a figure never illustrates a wrong claim. The interactive companions
already cover the log-scale time paths, the index bench, the Balassa-Samuelson line and
the lambda waterfall; these figures show the mechanisms the companions do not draw.

Run: python Map/aula-01-mensuracao/make_figures.py   (writes fig/fig_0*_*.svg)
"""
from __future__ import annotations

import math
import pathlib
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "fig"))
from mapstyle import INK, INK2, S, SURF, save  # noqa: E402

import matplotlib.pyplot as plt  # noqa: E402

OUT = pathlib.Path(__file__).resolve().parent / "fig"
close = math.isclose


def title(ax, text):
    """Left-aligned takeaway title in the shared style."""
    ax.set_title(text, loc="left", color=INK, fontsize=11)


# ======================================================================
# 01 -- three approaches
# ======================================================================
# Kurlat Example 1.2: fertiliser 0.80 -> lettuce 1.00.
rev = [0.80, 1.00]
va = [rev[0] - 0.0, rev[1] - rev[0]]
assert close(sum(rev), 1.80) and close(sum(va), 1.00) and close(va[1], 0.20)

fig, ax = plt.subplots(figsize=(6.4, 3.6))
x = [0, 1]
ax.bar(0, rev[0], color=S[0], width=0.55, label="fertiliser plant")
ax.bar(0, rev[1], bottom=rev[0], color=S[1], width=0.55, label="lettuce farm")
ax.bar(1, va[0], color=S[0], width=0.55)
ax.bar(1, va[1], bottom=va[0], color=S[1], width=0.55)
ax.text(0, rev[0] / 2, "$0.80", ha="center", color=SURF, fontsize=10)
ax.text(0, rev[0] + rev[1] / 2, "$1.00\n(contains the\n$0.80 again)",
        ha="center", va="center", color=SURF, fontsize=9)
ax.text(1, va[0] / 2, "$0.80", ha="center", color=SURF)
ax.text(1, va[0] + va[1] / 2, "$0.20", ha="center", va="center", color=SURF)
ax.text(0, sum(rev) + 0.04, f"total ${sum(rev):.2f}", ha="center", color=INK)
ax.text(1, sum(va) + 0.04, f"total ${sum(va):.2f} = price of lettuce",
        ha="center", color=INK)
ax.set_xticks(x, ["sum of revenues", "sum of value added"])
ax.set_ylabel("dollars")
ax.set_ylim(0, 2.1)
ax.grid(axis="x", visible=False)
ax.legend(loc="upper right", fontsize=9)
title(ax, "Summing revenues counts the fertiliser twice; value added does not")
save(fig, OUT / "fig_01_double_counting.svg")

# Kurlat Example 1.6: production vs expenditure, with the inventory entry.
prod = {"car value added": 20 - 5, "lettuce (exported)": 2}
spend = {"C (car)": 20, "I (inventory)": 5, "X (lettuce)": 2,
         "−M (imports)": -10}
assert sum(prod.values()) == 17 and sum(spend.values()) == 17
assert 20 + 2 - 10 == 12  # without the inventory entry

fig, ax = plt.subplots(figsize=(7.0, 3.8))
bottom = 0.0
for (lab, v), col in zip(prod.items(), S):
    ax.bar(0, v, bottom=bottom, color=col, width=0.6)
    ax.text(0, bottom + v / 2, f"{v}", ha="center", va="center", color=SURF)
    bottom += v
pos = 0.0
xt = ["production\n(car VA 15 +\nlettuce 2)"]
for i, ((lab, v), col) in enumerate(zip(spend.items(), [S[2], S[3], S[1], S[4]])):
    ax.bar(i + 1, v, bottom=pos, color=col, width=0.6)
    ax.text(i + 1, pos + v / 2, f"{v:+d}", ha="center", va="center", color=INK)
    pos += v
    xt.append(lab.replace(" (", "\n("))
ax.bar(5, pos, color=S[0], width=0.6)
ax.text(5, pos / 2, f"{pos:.0f}", ha="center", va="center", color=SURF)
xt.append("expenditure\ntotal")
ax.axhline(17, color=INK2, lw=1, ls="--")
ax.text(3.0, 16.4, "GDP = 17 both ways; drop the +5 and expenditure is 12",
        ha="center", va="top", color=INK, fontsize=8.5)
ax.set_xticks(range(6), xt, fontsize=8)
ax.set_ylim(0, 30)
ax.set_ylabel("dollars")
ax.grid(axis="x", visible=False)
title(ax, "Imports stacked inside C and I are taken out by −M")
save(fig, OUT / "fig_01_example16_columns.svg")

# ======================================================================
# 02 -- indices
# ======================================================================
p0, q0 = np.array([50.0, 1000.0]), np.array([10.0, 1.0])
p1, q1 = np.array([60.0, 600.0]), np.array([11.0, 2.0])
QL = (p0 @ q1) / (p0 @ q0)
QP = (p1 @ q1) / (p1 @ q0)
QF = math.sqrt(QL * QP)
assert close(QL, 1.70) and close(QP, 1.55) and close(QF, 1.6233, abs_tol=1e-4)
s0 = p0 * q0 / (p0 @ q0)
ph, qh = p1 / p0, q1 / q0
Ep, Eq, Epq = s0 @ ph, s0 @ qh, s0 @ (ph * qh)
cov = Epq - Ep * Eq
assert close(cov, -0.12) and close(QP - QL, cov / Ep)

fig, ax = plt.subplots(figsize=(6.4, 3.6))
labels = ["at 2017 prices\n(Laspeyres, $g^I$)", "chained Fisher\n$\\sqrt{Q^LQ^P}$",
          "at 2018 prices\n(Paasche, $g^F$)"]
vals = [QL - 1, QF - 1, QP - 1]
ax.bar(range(3), [v * 100 for v in vals], color=[S[0], S[2], S[1]], width=0.55)
for i, v in enumerate(vals):
    ax.text(i, v * 100 + 1.5, f"{v * 100:.1f}%", ha="center", color=INK)
ax.annotate("", xy=(2.35, (QP - 1) * 100), xytext=(2.35, (QL - 1) * 100),
            arrowprops=dict(arrowstyle="<->", color=INK2))
ax.text(2.42, (QL + QP - 2) * 50,
        f"gap = Cov/E[p̂]\n= {cov:.2f}/{Ep:.1f}\n= {cov / Ep:.2f}",
        va="center", fontsize=8.5, color=INK)
ax.set_xticks(range(3), labels)
ax.set_xlim(-0.5, 3.1)
ax.set_ylim(0, 85)
ax.set_ylabel("real GDP growth 2017→18 (%)")
ax.grid(axis="x", visible=False)
title(ax, "Expandia: the base year moves growth by 15 points")
save(fig, OUT / "fig_02_expandia_growth.svg")

fig, ax = plt.subplots(figsize=(6.4, 3.8))
names = ["wheat", "computers"]
for i in range(2):
    ax.scatter(ph[i], qh[i], s=2400 * s0[i], color=S[i], alpha=0.85,
               edgecolor=SURF)
    ax.text(ph[i] + 0.09, qh[i] + 0.08,
            f"{names[i]}: p̂={ph[i]:.1f}, q̂={qh[i]:.1f}, s={s0[i]:.2f}",
            fontsize=8.5, color=INK)
ax.plot(ph, qh, color=INK2, lw=1, ls="--")
ax.axvline(Ep, color=INK2, lw=0.8, ls=":")
ax.axhline(Eq, color=INK2, lw=0.8, ls=":")
ax.text(Ep + 0.01, 0.82, f"E[p̂] = {Ep:.1f}", fontsize=8.5, color=INK2)
ax.text(0.42, Eq + 0.04, f"E[q̂] = {Eq:.2f}", fontsize=8.5, color=INK2)
ax.text(0.95, 1.5, f"Cov = E[p̂q̂] − E[p̂]E[q̂]\n= {Epq:.2f} − {Ep * Eq:.2f}"
        f" = {cov:.2f}", fontsize=9, color=INK)
ax.set_xlim(0.4, 1.6)
ax.set_ylim(0.8, 2.3)
ax.set_xlabel("gross price change p̂ = p₁/p₀")
ax.set_ylabel("gross quantity change q̂ = q₁/q₀")
title(ax, "The good that got cheaper grew more: the covariance is negative")
save(fig, OUT / "fig_02_covariance.svg")


def ces_bias(d, eps):
    """Exact ln P^L - ln P^F for two equal-share goods with log price changes +-d."""
    pi = np.array([d, -d])
    s = np.array([0.5, 0.5])
    PL = s @ np.exp(pi)
    PP = (s @ np.exp((1 - eps) * pi)) / (s @ np.exp(-eps * pi))
    return math.log(PL) - 0.5 * (math.log(PL) + math.log(PP))


ds = np.linspace(0, 0.6, 121)
fig, ax = plt.subplots(figsize=(6.4, 3.8))
for eps, col in zip((0.5, 1.0, 2.0), S):
    exact = [ces_bias(d, eps) * 100 for d in ds]
    ax.plot(ds, exact, color=col, label=f"ε = {eps:g}, exact")
    ax.plot(ds, 0.5 * eps * ds ** 2 * 100, color=col, ls="--", lw=1.2,
            label=f"ε = {eps:g}, ½ε·Var")
assert abs(ces_bias(0.1, 1.0) - 0.5 * 0.01) < 1e-4
b = ces_bias(0.3, 1.0)
ax.plot(0.3, b * 100, "o", color=S[1])
ax.annotate(f"sd 0.3, ε = 1: bias {b * 100:.1f} pts", (0.3, b * 100),
            xytext=(0.05, 12), fontsize=8.5, color=INK,
            arrowprops=dict(arrowstyle="-", color=INK2, lw=0.8))
ax.set_xlabel("dispersion of log price changes, sd(π)")
ax.set_ylabel(r"$\ln P^L - \ln P^F$ (log points, ×100)")
ax.legend(fontsize=8, ncol=2, loc="upper left")
ax.set_ylim(0, 40)
title(ax, "Substitution bias grows with price dispersion and with ε")
save(fig, OUT / "fig_02_ces_bias.svg")

# ======================================================================
# 03 -- growth arithmetic
# ======================================================================
g = np.linspace(0, 1.0, 201)
g_mark = 0.5
gap = g_mark - math.log1p(g_mark)
assert close(gap, 0.09454, abs_tol=1e-5)
fig, ax = plt.subplots(figsize=(6.4, 3.8))
ax.plot(g, g, color=S[0], label="net rate g (tangent at 0)")
ax.plot(g, np.log1p(g), color=S[1], label="log rate g̃ = ln(1+g)")
ax.vlines(g_mark, math.log1p(g_mark), g_mark, color=INK, lw=1.5)
ax.text(g_mark + 0.02, g_mark - gap / 2,
        f"gap at g = 0.5: {gap:.3f}\n≈ g²/2 − g³/3 = {0.125 - 0.125 / 3:.3f}",
        va="center", fontsize=8.5, color=INK)
for gm in (0.05, 0.10):
    ax.plot(gm, math.log1p(gm), "o", color=S[1], ms=4)
ax.text(0.12, 0.03, "at g ≤ 0.10 the curves are\nindistinguishable (gap < 0.005)",
        fontsize=8.5, color=INK2)
ax.set_xlabel("net growth rate g")
ax.set_ylabel("growth rate")
ax.legend(fontsize=9, loc="upper left")
title(ax, "ln(1+g) bends below g; the gap starts as g²/2")
save(fig, OUT / "fig_03_log_tangent.svg")

gx, gz = 0.30, 0.20
fig, ax = plt.subplots(figsize=(5.6, 4.2))
parts = [((0, 0), 1, 1, S[0], "1"), ((1, 0), gx, 1, S[1], "g_X"),
         ((0, 1), 1, gz, S[2], "g_Z"), ((1, 1), gx, gz, S[3], "g_X·g_Z")]
for (x0, y0), w, h, col, lab in parts:
    ax.add_patch(plt.Rectangle((x0, y0), w, h, color=col, alpha=0.85,
                               ec=SURF, lw=2))
    ax.text(x0 + w / 2, y0 + h / 2, lab, ha="center", va="center",
            color=SURF if lab == "1" else INK, fontsize=10)
area = (1 + gx) * (1 + gz)
assert close(area, 1 + gx + gz + gx * gz) and close(gx * gz, 0.06)
ax.text(0.5, -0.12, "1", ha="center")
ax.text(1 + gx / 2, -0.12, f"g_X = {gx}", ha="center")
ax.text(-0.08, 0.5, "1", va="center", ha="right")
ax.text(-0.08, 1 + gz / 2, f"g_Z = {gz}", va="center", ha="right")
ax.text(0.02, 1.33, f"area = (1+g_X)(1+g_Z) = {area:.2f} = 1 + {gx} + {gz} + "
        f"{gx * gz:.2f}", fontsize=9, color=INK)
ax.set_xlim(-0.45, 1.45)
ax.set_ylim(-0.25, 1.45)
ax.set_aspect("equal")
ax.axis("off")
title(ax, "Discrete growth of a product: the corner is the cross term")
save(fig, OUT / "fig_03_cross_term.svg")

gp = np.linspace(0.5, 12, 200)
exact = np.log(2) / np.log1p(gp / 100)
fig, ax = plt.subplots(figsize=(6.4, 3.8))
ax.plot(gp, exact - 69.3 / gp, color=S[0], label="exact − 69.3/(100g)")
ax.plot(gp, exact - 70 / gp, color=S[1], label="exact − 70/(100g)")
ax.axhline(0.347, color=S[0], ls="--", lw=1.2)
ax.text(11.8, 0.37, "ln 2 / 2 = 0.347", ha="right", va="bottom", fontsize=8.5,
        color=S[0])
ax.axhline(0, color=INK2, lw=1)
for pct in (2, 7):
    t = math.log(2) / math.log1p(pct / 100)
    ax.plot(pct, t - 70 / pct, "o", color=S[1])
    ax.annotate(f"{pct}%: exact {t:.2f} vs rule {70 / pct:.2f}",
                (pct, t - 70 / pct), xytext=(pct + 0.6, t - 70 / pct - 0.45),
                fontsize=8.5, arrowprops=dict(arrowstyle="-", color=INK2, lw=0.8))
assert close(math.log(2) / math.log1p(0.02), 35.003, abs_tol=1e-2)
assert abs((math.log(2) / math.log1p(0.02) - 69.3 / 2) - 0.347) < 0.01
ax.set_xlabel("growth rate (% per year)")
ax.set_ylabel("error of the rule (years)")
ax.set_ylim(-1.3, 0.8)
ax.legend(fontsize=9, loc="lower left")
title(ax, "69.3/g is short by a constant 0.35 years; 70/g absorbs it near 2%")
save(fig, OUT / "fig_03_doubling_time.svg")

# ======================================================================
# 04 -- PPP and Balassa-Samuelson
# ======================================================================
us_pc = 20.5e12 / 327e6
mx_pc_local = 23.5e12 / 127e6
mx_mkt = mx_pc_local / 19
mx_ppp = 18000.0
e_mkt, e_ppp = 1 / 19, mx_ppp / mx_pc_local
price_level = e_mkt / e_ppp
assert close(us_pc, 62691, abs_tol=5) and close(mx_mkt, 9739, abs_tol=5)
assert close(price_level, 0.54, abs_tol=0.01)
log_gap_mkt = math.log(us_pc / mx_mkt)
log_gap_ppp = math.log(us_pc / mx_ppp)
share_price = (log_gap_mkt - log_gap_ppp) / log_gap_mkt
assert close(share_price, 0.33, abs_tol=0.01)

fig, ax = plt.subplots(figsize=(6.4, 3.8))
bars = [("US", us_pc, S[0]), ("Mexico,\nmarket rate", mx_mkt, S[1]),
        ("Mexico,\nPPP", mx_ppp, S[2])]
for i, (lab, v, col) in enumerate(bars):
    ax.bar(i, v / 1000, color=col, width=0.55)
    ax.text(i, v / 1000 + 1.2, f"${v / 1000:.1f}k", ha="center", color=INK)
ax.annotate("", xy=(2, mx_ppp / 1000), xytext=(2, mx_mkt / 1000),
            arrowprops=dict(arrowstyle="->", color=INK, lw=1.4))
ax.text(2.33, 13.5, f"÷ price level {price_level:.2f}\n(×{1 / price_level:.2f})",
        fontsize=8.5, color=INK)
ax.text(0.45, 45, f"US/Mexico ratio:\nmarket {us_pc / mx_mkt:.1f}×, "
        f"PPP {us_pc / mx_ppp:.1f}×", fontsize=9, color=INK)
ax.set_xticks(range(3), [b[0] for b in bars])
ax.set_xlim(-0.5, 3.0)
ax.set_ylim(0, 72)
ax.set_ylabel("GDP per head (thousand US$)")
ax.grid(axis="x", visible=False)
title(ax, "Valued at US prices, Mexican output per head nearly doubles")
save(fig, OUT / "fig_04_mexico_ppp.svg")

# Balassa-Samuelson chain, with check_measurement.py's rich/poor numbers.
AT_r, AN_r, AT_p, AN_p, gam = 4.0, 1.25, 1.0, 1.0, 0.5
t_gap = math.log(AT_p) - math.log(AT_r)
n_gap = math.log(AN_p) - math.log(AN_r)
bracket = t_gap - n_gap
lnP = gam * bracket
assert close(math.exp(lnP), ((AT_p / AN_p) / (AT_r / AN_r)) ** gam)
fig, ax = plt.subplots(figsize=(7.2, 3.9))
steps = [("tradable gap\nln A_T: poor − rich", t_gap, S[0]),
         ("non-tradable gap\nln A_N: poor − rich", n_gap, S[1]),
         ("bracket\n= first − second", bracket, S[2]),
         (f"ln(P_poor/P_rich)\n= γ × bracket, γ={gam}", lnP, S[3])]
for i, (lab, v, col) in enumerate(steps):
    ax.bar(i, v, color=col, width=0.55)
    ax.text(i, v - 0.08, f"{v:+.3f}", ha="center", va="top", color=INK)
ax.axhline(0, color=INK2, lw=1)
ax.text(2.6, 0.12, f"P_poor/P_rich = e^{lnP:.3f} = {math.exp(lnP):.2f}",
        ha="center", fontsize=9, color=INK)
ax.set_xticks(range(4), [s_[0] for s_ in steps], fontsize=8)
ax.set_ylim(-1.75, 0.35)
ax.set_ylabel("log points")
ax.grid(axis="x", visible=False)
title(ax, "A gap concentrated in tradables makes the poor country cheap")
save(fig, OUT / "fig_04_bs_chain.svg")

# ======================================================================
# 05 -- beyond GDP
# ======================================================================
educ = 0.8
grid = np.linspace(0.01, 1, 300)
L, I = np.meshgrid(grid, grid)
geo = (L * educ * I) ** (1 / 3)
ari = (L + educ + I) / 3
pt = (0.15, 1.0)
geo_pt = (pt[0] * educ * pt[1]) ** (1 / 3)
ari_pt = (pt[0] + educ + pt[1]) / 3
assert geo_pt < ari_pt
fig, ax = plt.subplots(figsize=(6.2, 4.4))
lv = [0.5, 0.7]
cg = ax.contour(L, I, geo, levels=lv, colors=S[0], linewidths=2)
ca = ax.contour(L, I, ari, levels=lv, colors=S[1], linewidths=2,
                linestyles="--")
ax.clabel(cg, fmt="geo %.1f", fontsize=8)
ax.clabel(ca, fmt="arith %.1f", fontsize=8)
ax.plot(*pt, "o", color=INK)
ax.annotate(f"rich, short-lived: I_life={pt[0]}, I_inc={pt[1]:.0f}\n"
            f"arithmetic {ari_pt:.2f}, geometric {geo_pt:.2f}", pt,
            xytext=(0.22, 1.1), fontsize=8.5,
            arrowprops=dict(arrowstyle="-", color=INK2, lw=0.8))
ax.plot([], [], color=S[0], label="geometric mean (HDI since 2010)")
ax.plot([], [], color=S[1], ls="--", label="arithmetic mean (pre-2010)")
ax.legend(fontsize=8.5, loc="lower left")
ax.set_xlabel("life index I_life")
ax.set_ylabel("income index I_inc")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.25)
title(ax, f"Iso-HDI curves (I_educ = {educ}): income cannot buy off health")
save(fig, OUT / "fig_05_hdi_isoquants.svg")


def inc_index(gni):
    """HDI income sub-index, Kurlat p. 32."""
    return (np.log(gni) - math.log(100)) / (math.log(75000) - math.log(100))


gni = np.linspace(100, 80000, 800)
d_low = float(inc_index(3000) - inc_index(2000))
d_high = float(inc_index(61000) - inc_index(60000))
assert close(d_low, 0.0613, abs_tol=1e-4) and close(d_high, 0.0025, abs_tol=1e-4)
fig, ax = plt.subplots(figsize=(6.4, 3.8))
ax.plot(gni / 1000, inc_index(gni), color=S[0])
for a, b_, col in ((2000, 3000, S[1]), (60000, 61000, S[2])):
    ax.plot([a / 1000, b_ / 1000], [inc_index(a)] * 2, color=col, lw=2)
    ax.plot([b_ / 1000] * 2, [inc_index(a), inc_index(b_)], color=col, lw=2)
ax.annotate(rf"+\$1,000 at \$2,000: +{d_low:.3f}", (3, float(inc_index(3000))),
            xytext=(12, 0.45), fontsize=8.5,
            arrowprops=dict(arrowstyle="-", color=INK2, lw=0.8))
ax.annotate(rf"+\$1,000 at \$60,000: +{d_high:.4f}", (61, float(inc_index(61000))),
            xytext=(38, 0.78), fontsize=8.5,
            arrowprops=dict(arrowstyle="-", color=INK2, lw=0.8))
ax.axvline(75, color=INK2, ls=":", lw=1)
ax.text(74, 0.2, "cap $75k", ha="right", fontsize=8.5, color=INK2)
ax.set_xlabel("GNI per head (thousand PPP $)")
ax.set_ylabel("income index I_inc")
title(ax, "The log makes the same $1,000 worth 25 times more to the poor")
save(fig, OUT / "fig_05_income_index.svg")

c_poor, c_rich = 10000.0, 50000.0
c_mean = (c_poor + c_rich) / 2
u_mean = math.log(c_mean)
Eu = 0.5 * (math.log(c_poor) + math.log(c_rich))
ce = math.exp(Eu)
assert u_mean > Eu and close(ce, math.sqrt(c_poor * c_rich))
cc = np.linspace(5000, 60000, 300)
fig, ax = plt.subplots(figsize=(6.4, 3.8))
ax.plot(cc / 1000, np.log(cc), color=S[0], label="u(c) = ln c")
ax.plot([c_poor / 1000, c_rich / 1000], [math.log(c_poor), math.log(c_rich)],
        color=S[1], ls="--", label="chord: the 50–50 gamble")
ax.plot(c_mean / 1000, u_mean, "o", color=S[0])
ax.plot(c_mean / 1000, Eu, "o", color=S[1])
ax.plot(ce / 1000, Eu, "o", color=S[2])
ax.hlines(Eu, ce / 1000, c_mean / 1000, color=S[2], lw=1.5)
ax.text(c_mean / 1000 + 0.8, u_mean - 0.05, f"u(E c) = ln {c_mean:,.0f} = {u_mean:.2f}",
        fontsize=8.5, va="top")
ax.text(c_mean / 1000 + 0.8, Eu - 0.07, f"E u(c) = {Eu:.2f}", fontsize=8.5,
        va="top")
ax.text(ce / 1000 - 0.5, Eu + 0.08,
        f"certainty equivalent\n{ce:,.0f} < mean {c_mean:,.0f}", fontsize=8.5,
        ha="right")
ax.set_xlabel("consumption c (thousand $)")
ax.set_ylabel("utility")
ax.legend(fontsize=9, loc="lower right")
title(ax, "Jensen: behind the veil, a spread costs Rawls consumption")
save(fig, OUT / "fig_05_jensen.svg")

Phi = np.vectorize(lambda z: 0.5 * (1 + math.erf(z / math.sqrt(2))))
ss = np.linspace(0, 2, 200)
fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.plot(ss, 2 * Phi(ss / math.sqrt(2)) - 1, color=S[0],
        label="G = 2Φ(s/√2) − 1")
for sv in (0.5, 1.0):
    G = float(2 * Phi(sv / math.sqrt(2)) - 1)
    ax.plot(sv, G, "o", color=S[1])
    ax.annotate(f"s = {sv}: G = {G:.2f}, penalty s²/2 = {sv * sv / 2:.3f}",
                (sv, G), xytext=(sv + 0.15, G - 0.12), fontsize=8.5,
                arrowprops=dict(arrowstyle="-", color=INK2, lw=0.8))
assert close(float(2 * Phi(0.5 / math.sqrt(2)) - 1), 0.276, abs_tol=1e-3)
ax.set_xlabel("s, standard deviation of ln c")
ax.set_ylabel("Gini coefficient G")
ax.legend(fontsize=9, loc="upper left")
title(ax, "A published Gini gives s, and s gives the inequality term")
save(fig, OUT / "fig_05_gini_s.svg")
