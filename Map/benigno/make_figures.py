#!/usr/bin/env python3
"""Figures for the Benigno (2015) notes in Map/benigno/.

Every number drawn or labelled is computed here from the closed forms derived in
the notes, and the multipliers come from check_multipliers.py so the two files
cannot drift apart. Calibration is the article's: alpha=0.66, sigma=0.5, eta=0.2,
theta=8 (p. 515, footnote 24). Shocks are sized so that the moved anchor
(dy_n or dybar_n) is one percent, so every label reads in percent.

Run:  python Map/benigno/make_figures.py [--png DIR]
      writes Map/benigno/fig/fig_b*.svg; --png also writes PNG previews to DIR.
"""
from __future__ import annotations

import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[0] / "fig"))
sys.path.insert(0, str(HERE))
from mapstyle import S, INK, INK2, SURF, save as _save  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from check_multipliers import (kappa, multipliers,  # noqa: E402
                               deleveraging_multiplier)

OUT = HERE / "fig"
PNG = pathlib.Path(sys.argv[sys.argv.index("--png") + 1]) if "--png" in sys.argv else None

AL, SG, ET, TH = 0.66, 0.5, 0.2, 8.0
K = kappa(AL, SG, ET)
SK = SG * K
INV = 1 / SG + ET                       # sigma^-1 + eta
assert math.isclose(K, 1.1333, abs_tol=1e-4)


def save(fig, name):
    """Write fig/<name>.svg through mapstyle; also a PNG preview if --png."""
    if PNG:
        PNG.mkdir(parents=True, exist_ok=True)
        fig.tight_layout()
        fig.savefig(PNG / name.replace(".svg", ".png"), dpi=110)
    _save(fig, OUT / name)


def line(ax, slope, y0, p0, xs, **kw):
    """Draw p = p0 + slope (y - y0) over the y-range xs."""
    xs = np.asarray(xs)
    ax.plot(xs, p0 + slope * (xs - y0), **kw)


def dot(ax, y, p, label, col=INK, off=(6, 6), ha="left"):
    """Mark an equilibrium point and label it with its coordinates."""
    ax.plot(y, p, "o", ms=7, color=col, mec=SURF, mew=1.5, zorder=5)
    ax.annotate(label, (y, p), xytext=off, textcoords="offset points",
                fontsize=8.5, color=INK, ha=ha)


def legend_below(ax, ncol=2):
    """Legend under the axes, for diagrams whose corners are all occupied."""
    ax.legend(fontsize=8, loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=ncol)


def axes_yp(ax):
    ax.set_xlabel("output y (% from initial steady state)")
    ax.set_ylabel("price level p (% from pᵉ)")
    ax.axhline(0, color=INK2, lw=0.6)
    ax.axvline(0, color=INK2, lw=0.6)


def bars(ax, cats, series, width=0.8):
    """Grouped bars; series = [(label, colour, values)]; values printed on bars."""
    n = len(series)
    x = np.arange(len(cats))
    w = width / n
    for j, (lab, col, vals) in enumerate(series):
        xs = x - width / 2 + w * (j + 0.5)
        ax.bar(xs, vals, w, color=col, label=lab, edgecolor=SURF, linewidth=1.5)
        for xi, v in zip(xs, vals):
            ax.annotate(f"{v:+.2f}" if abs(v) > 5e-4 else "0", (xi, v),
                        xytext=(0, 3 if v >= 0 else -10), textcoords="offset points",
                        ha="center", fontsize=7.5, color=INK2)
    ax.set_xticks(x, cats)
    ax.axhline(0, color=INK2, lw=0.8)
    ax.grid(axis="x", visible=False)


# =============================== note 01 ===============================
fig, axs = plt.subplots(1, 2, figsize=(8.4, 3.6), sharey=True)
xs = np.linspace(-2, 2, 50)
ax = axs[0]
for sg, col in [(0.5, S[0]), (1.0, S[1])]:
    line(ax, -1 / sg, 0, 0, xs, color=col, label=f"σ = {sg}: slope −1/σ = {-1 / sg:.0f}")
axes_yp(ax)
ax.set_ylim(-3, 3)
ax.set_title("Larger σ, flatter AD", loc="left", fontsize=10)
ax.legend(fontsize=8, loc="upper right")
ax = axs[1]
di = -1.0
shift = -SG * di                      # dy at given p from eq. (8)
assert math.isclose(shift, 0.5)
line(ax, -1 / SG, 0, 0, xs, color=S[0], ls="--", label="AD, i = r (before)")
line(ax, -1 / SG, shift, 0, xs, color=S[0], label="AD after a 1-point cut in i")
ax.annotate("", (shift, 0.0), (0, 0.0),
            arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))
ax.text(shift + 0.1, 0.25, f"shift = σ·1 = {shift:.1f}", ha="left", fontsize=8.5)
axes_yp(ax)
ax.set_ylabel("")
ax.set_title("A rate cut shifts AD right by σ", loc="left", fontsize=10)
ax.legend(fontsize=8, loc="upper right")
fig.suptitle("Eq. (8): AD is an Euler equation, slope −1/σ, shifted by −σ·di",
             x=0.02, ha="left", fontsize=11)
save(fig, "fig_b01_ad_slope.svg")

# causal chains: NK AD vs IS-LM AD
fig, ax = plt.subplots(figsize=(8.4, 2.9))
ax.axis("off")
rows = [
    (0.72, S[0], "New-Keynesian AD, eq. (8)",
     ["p ↑\n(p̄ fixed)", "expected inflation\np̄ − p ↓", "real rate\nr = i − (p̄ − p) ↑",
      "save more:\nc̄ − c = σ̃(r − ρ) ↑", "c ↓ so y ↓"]),
    (0.22, S[1], "IS-LM AD (not this model)",
     ["p ↑\n(M fixed)", "real balances\nM/p ↓", "money market:\ni must rise",
      "investment ↓", "y ↓"]),
]
for yrow, col, title, boxes in rows:
    ax.text(0.0, yrow + 0.2, title, color=col, fontsize=10, fontweight="bold",
            transform=ax.transAxes)
    xpos = np.linspace(0.08, 0.92, len(boxes))
    for j, (xp, txt) in enumerate(zip(xpos, boxes)):
        ax.text(xp, yrow, txt, ha="center", va="center", fontsize=8.5,
                transform=ax.transAxes,
                bbox=dict(boxstyle="round,pad=0.4", fc=SURF, ec=col, lw=1.4))
        if j:
            ax.annotate("", (xp - 0.085, yrow), (xpos[j - 1] + 0.085, yrow),
                        xycoords="axes fraction",
                        arrowprops=dict(arrowstyle="->", color=INK2, lw=1.2))
ax.set_title("Two downward-sloping AD curves, two different mechanisms: "
             "only the top one is in Benigno", loc="left", fontsize=11)
save(fig, "fig_b01_two_ads.svg")

# =============================== note 02 ===============================
fig, ax = plt.subplots(figsize=(6.6, 3.6))
x = np.linspace(1.0, 1.35, 300)             # P(j) / (marginal cost)
prof = (x - 1) * x ** (-TH)
xstar = TH / (TH - 1)
pmax = (xstar - 1) * xstar ** (-TH)
assert abs(x[np.argmax(prof)] - xstar) < 2e-3
assert math.isclose(xstar, 1.143, abs_tol=5e-4)
loss2 = 1 - ((xstar * 1.02 - 1) * (xstar * 1.02) ** (-TH)) / pmax
ax.plot(x, prof / pmax, color=S[0], label="profit / maximum profit, θ = 8")
dot(ax, xstar, 1.0, f"optimum P/MC = θ/(θ−1) = {xstar:.3f}", S[0], off=(-8, 8), ha="right")
xe = xstar * 1.02
ye_ = (xe - 1) * xe ** (-TH) / pmax
assert math.isclose(loss2, 0.010, abs_tol=5e-4)
dot(ax, xe, ye_, f"price 2% too high: profit −{loss2 * 100:.1f}%", S[1], off=(8, -14))
ax.set_xlabel("relative price P(j) / marginal cost W/A")
ax.set_ylabel("share of maximum profit")
ax.set_ylim(0, 1.12)
ax.set_title("Mark-up pricing (11): the top is flat, so a small price error costs little",
             loc="left", fontsize=10.5)
save(fig, "fig_b02_markup.svg")

fig, axs = plt.subplots(1, 2, figsize=(8.4, 3.6))
ax = axs[0]
al = np.linspace(0.3, 0.95, 200)
for et, col in [(0.2, S[0]), (1.0, S[1])]:
    ax.plot(al, kappa(al, SG, et), color=col, label=f"η = {et}")
for a_ in (0.66, 0.75):
    k_ = kappa(a_, SG, 0.2)
    dot(ax, a_, k_, f"α = {a_}: κ = {k_:.2f}", S[0], off=(-8, -14), ha="right")
assert math.isclose(kappa(0.75, SG, 0.2), 0.7333, abs_tol=1e-4)
ax.set_xlabel("share of sticky-price firms α")
ax.set_ylabel("AS slope κ")
ax.set_ylim(0, 6)
ax.set_title("κ = (1−α)(σ⁻¹+η)/α falls in α", loc="left", fontsize=10)
ax.legend(fontsize=8)
ax = axs[1]
xs = np.linspace(-1.5, 1.5, 20)
for a_, col in [(0.66, S[0]), (0.75, S[2])]:
    line(ax, kappa(a_, SG, 0.2), 0, 0, xs, color=col,
         label=f"AS, α = {a_} (κ = {kappa(a_, SG, 0.2):.2f})")
dot(ax, 0, 0, "anchor (yₙ, pᵉ)", INK, off=(8, -14))
axes_yp(ax)
ax.set_xlabel("output y (% from yₙ)")
ax.set_title("More rigidity, flatter AS", loc="left", fontsize=10)
ax.legend(fontsize=8, loc="upper left")
fig.suptitle("Eq. (17), σ = 0.5: α sits in the denominator of κ",
             x=0.02, ha="left", fontsize=11)
save(fig, "fig_b02_kappa.svg")

fig, ax = plt.subplots(figsize=(6.6, 3.8))
dyn_a = (1 + ET) / INV                  # da = 1
dyn_mu = -1 / INV                       # dmu = 1
assert math.isclose(dyn_a, 0.5455, abs_tol=1e-4) and math.isclose(dyn_mu, -0.4545, abs_tol=1e-4)
xs = np.linspace(-1.3, 1.3, 20)
line(ax, K, 0, 0, xs, color=INK2, ls="--", label="AS before, through (0, pᵉ)")
line(ax, K, dyn_a, 0, xs, color=S[0], label="AS after a 1% rise in a")
line(ax, K, dyn_mu, 0, xs, color=S[1], label="AS after a 1-point rise in μ")
dot(ax, dyn_a, 0, f"yₙ′ = +{dyn_a:.2f}", S[0], off=(6, -14))
dot(ax, dyn_mu, 0, f"yₙ′ = {dyn_mu:.2f}", S[1], off=(-6, 8), ha="right")
dot(ax, 0, 0, "", INK)
axes_yp(ax)
ax.legend(fontsize=8, loc="upper left")
ax.set_title("Shift the anchor along p = pᵉ by dyₙ from (15), keep the slope κ",
             loc="left", fontsize=10.5)
save(fig, "fig_b02_as_shift.svg")

# =============================== note 03 ===============================
fig, ax = plt.subplots(figsize=(6.6, 3.8))
mu0 = 0.10
y = np.linspace(-0.09, 0.03, 100)
ax.plot(y * 100, INV * y * 100, color=S[0],
        label="household: log MRS = (σ⁻¹+η) y   (a = g = 0)")
ax.axhline(0, color=S[2], label="planner: log MRT = a = 0")
ax.axhline(-mu0 * 100, color=S[1], label=f"market: a − μ, μ = {mu0:.0%}")
yn_w, ye_w = -mu0 / INV, 0.0
assert math.isclose(yn_w, -0.04545, abs_tol=1e-5)
ax.fill([yn_w * 100, 0, yn_w * 100], [-mu0 * 100, 0, 0], color=S[3], alpha=0.35,
        label="lost surplus (second order)")
dot(ax, yn_w * 100, -mu0 * 100, f"yₙ = −μ/(σ⁻¹+η) = {yn_w * 100:.2f}%", S[1], off=(6, -14))
dot(ax, ye_w, 0, "yₑ = 0", S[2], off=(-6, 8), ha="right")
ax.annotate("", (yn_w * 100 - 0.6, 0), (yn_w * 100 - 0.6, -mu0 * 100),
            arrowprops=dict(arrowstyle="<->", color=INK, lw=1))
ax.text(yn_w * 100 - 0.8, -mu0 * 50, "wedge μ", ha="right", va="center", fontsize=8.5)
ax.set_xlabel("output y (% from efficient level)")
ax.set_ylabel("log marginal rate (%)")
ax.set_ylim(-20, 7)
ax.legend(fontsize=7.8, loc="lower right")
ax.set_title("FOCs (14) and §3.3: same MRS line, the market cuts it μ lower",
             loc="left", fontsize=10.5)
save(fig, "fig_b03_wedge.svg")

fig, ax = plt.subplots(figsize=(6.6, 3.5))
yn_resp = [(1 + ET) / INV, (1 / SG) / INV, -1 / INV]
ye_resp = [(1 + ET) / INV, (1 / SG) / INV, 0.0]
assert math.isclose(yn_resp[1], 0.9091, abs_tol=1e-4)
assert math.isclose(mu0 / INV * 100, 4.545, abs_tol=1e-3)
bars(ax, ["a +1%", "g +1% of GDP", "μ +1 point"],
     [("natural yₙ, eq. (15)", S[0], yn_resp), ("efficient yₑ, eq. (19)", S[2], ye_resp)])
ax.set_ylabel("response (% of output)")
ax.set_ylim(-0.7, 1.15)
ax.legend(fontsize=8.5, loc="upper right")
ax.set_title("yₙ − yₑ = −μ/(σ⁻¹+η): only the mark-up pulls the two targets apart",
             loc="left", fontsize=10.5)
save(fig, "fig_b03_targets.svg")

# =============================== note 04 ===============================
fig, ax = plt.subplots(figsize=(6.6, 3.8))
xs = np.linspace(-1.2, 1.2, 20)
line(ax, K, 0, 0, xs, color=S[0], label=f"AS: slope +κ = {K:.2f}, through (yₙ, pᵉ) always")
line(ax, -1 / SG, 0, 0, xs, color=S[1],
     label=f"AD: slope −1/σ = {-1 / SG:.0f}, through (yₙ, pᵉ) only if i = rₙ, p̄ = pᵉ")
dot(ax, 0, 0, "E: y = yₙ = yₑ, p = pᵉ = p̄", INK, off=(8, -14))
axes_yp(ax)
ax.set_ylim(-1.6, 1.8)
legend_below(ax, ncol=1)
ax.set_title("Fig. 5 of the article: two lines, two unknowns (y, p)", loc="left", fontsize=10.5)
save(fig, "fig_b04_equilibrium.svg")

fig, ax = plt.subplots(figsize=(6.6, 3.6))
al = np.linspace(0.05, 0.95, 200)
sk = SG * kappa(al, SG, ET)
ax.plot(al, sk / (1 + sk), color=S[0], label="dy / dyₙ = σκ/(1+σκ)  (output follows)")
ax.plot(al, 1 / (1 + sk), color=S[1], label="−d(y−yₙ)/dyₙ = 1/(1+σκ)  (gap opens)")
out_s = SK / (1 + SK)
dot(ax, AL, out_s, f"α = 0.66: {out_s:.2f}", S[0], off=(6, 6))
dot(ax, AL, 1 - out_s, f"{1 - out_s:.2f}", S[1], off=(6, -12))
assert math.isclose(out_s, 0.3617, abs_tol=1e-4)
ax.set_xlabel("share of sticky-price firms α")
ax.set_ylabel("share of a 1% move in yₙ")
ax.set_ylim(0, 1.05)
ax.legend(fontsize=8, loc="center left")
ax.set_title(f"Temporary supply shock, fixed i: output moves {out_s:.0%}, the gap takes the rest",
             loc="left", fontsize=10.5)
save(fig, "fig_b04_split.svg")

fig, ax = plt.subplots(figsize=(6.8, 3.5))
rho, growth, gdiff, tcdiff = 1.0, -2.0, 0.5, 0.25     # illustrative, in %
terms = [("ρ", rho), ("σ⁻¹(ȳₙ − yₙ)\nȳₙ − yₙ = −2", growth / SG),
         ("σ⁻¹(g − ḡ)\ng − ḡ = +0.5", gdiff / SG), ("τ̄c − τc", tcdiff)]
rn = sum(v for _, v in terms)
assert math.isclose(rn, -1.75)
cum = 0.0
for j, (lab, v) in enumerate(terms):
    ax.bar(j, v, bottom=cum, color=S[0] if v >= 0 else S[1], edgecolor=SURF, width=0.6)
    top = max(cum, cum + v)
    ax.text(j, top + 0.12, f"{v:+.2f}", ha="center", fontsize=8.5)
    cum += v
ax.bar(len(terms), rn, color=S[2], width=0.6, edgecolor=SURF)
ax.text(len(terms), 0.12, f"rₙ = {rn:+.2f}", ha="center", fontsize=8.5)
ax.set_ylim(-3.5, 1.7)
ax.set_xticks(range(len(terms) + 1), [t for t, _ in terms] + ["rₙ"], fontsize=8)
ax.axhline(0, color=INK2, lw=0.8)
ax.grid(axis="x", visible=False)
ax.set_ylabel("percentage points")
ax.set_title("rₙ, term by term (σ = 0.5, illustrative numbers): pessimism makes it negative",
             loc="left", fontsize=10.5)
save(fig, "fig_b04_rn.svg")

fig, ax = plt.subplots(figsize=(6.6, 3.5))
cats, mk, it, net = [], [], [], []
for et in (0.0, 0.2, 1.0):
    k_ = kappa(AL, SG, et)
    inv_ = 1 / SG + et
    mk.append(-1 / (inv_ * (1 + SG * k_)))
    it.append(SG / (1 + SG * k_))
    net.append(SG * et / (inv_ * (1 + SG * k_)))
    cats.append(f"η = {et}")
    assert math.isclose(mk[-1] + it[-1], net[-1])
assert math.isclose(net[1], multipliers(AL, SG, 0.2)[5])
bars(ax, cats, [("mark-up channel via ȳₙ", S[1], mk),
                ("intertemporal channel via rₙ", S[0], it), ("net dy/dτ̄c", S[2], net)])
ax.set_ylabel("dy / dτ̄c")
ax.set_ylim(-0.45, 0.45)
ax.legend(fontsize=8, loc="lower right")
ax.set_title("A future consumption-tax rise: two channels, the net is ση/D ≥ 0",
             loc="left", fontsize=10.5)
save(fig, "fig_b04_taucbar.svg")

# =============================== note 05 ===============================
fig, axs = plt.subplots(1, 3, figsize=(10.2, 3.8), sharey=True)
xs = np.linspace(-1.2, 2.0, 20)
dy_t, dp_t = SK / (1 + SK), -K / (1 + SK)
dy_x, dp_x = 1 / (1 + SK), K / (1 + SK)
cases = [
    ("Temporary: a ↑ → cut i by 2", 1, 0, (dy_t, dp_t), (1, 0), -1 / SG),
    ("Permanent: a, ā ↑ → do nothing", 1, 1, (1, 0), None, 0.0),
    ("Expected: ā ↑ → raise i by 2", 0, 1, (dy_x, dp_x), (0, 0), 1 / SG),
]
for ax, (ttl, dyn, dybn, e1, e2, di_opt) in zip(axs, cases):
    line(ax, K, 0, 0, xs, color=S[0], ls="--", lw=1.4)
    line(ax, -1 / SG, 0, 0, xs, color=S[1], ls="--", lw=1.4)
    line(ax, K, dyn, 0, xs, color=S[0], label="AS after")
    line(ax, -1 / SG, dybn, 0, xs, color=S[1], label="AD after, i unchanged")
    if e2 is not None:
        line(ax, -1 / SG, dybn - SG * di_opt, 0, xs, color=S[2],
             label=f"AD after di = {di_opt:+.0f}")
        dot(ax, *e2, "E''", S[2], off=(6, 6))
    dot(ax, *e1, f"E′ ({e1[0]:.2f}, {e1[1]:+.2f})", INK, off=(6, 8))
    dot(ax, 0, 0, "E", INK2, off=(-6, -14), ha="right")
    axes_yp(ax)
    ax.set_ylim(-2, 2)
    ax.set_title(ttl, loc="left", fontsize=9.5)
    ax.legend(fontsize=7.5, loc="lower left")
for ax in axs[1:]:
    ax.set_ylabel("")
fig.suptitle("§6, the moved anchor = 1%: dashed = before; the same shock variable, "
             "three signs for policy", x=0.02, ha="left", fontsize=11)
save(fig, "fig_b05_three_cases.svg")

fig, ax = plt.subplots(figsize=(6.6, 3.5))
gaps = [-1 / (1 + SK), 0.0, 1 / (1 + SK)]
dis = [-1 / SG, 0.0, 1 / SG]
bars(ax, ["temporary\n(dyₙ = 1)", "permanent\n(dyₙ = dȳₙ = 1)", "expected\n(dȳₙ = 1)"],
     [("gap y − yₙ if i is held", S[1], gaps), ("optimal di = drₙ", S[0], dis)])
ax.set_ylabel("percent / percentage points")
ax.set_ylim(-2.4, 2.4)
ax.legend(fontsize=8.5, loc="upper left")
ax.set_title("The invariant rule: move i by drₙ = σ⁻¹(dȳₙ − dyₙ)", loc="left", fontsize=10.5)
save(fig, "fig_b05_policy.svg")

# =============================== note 06 ===============================
fig, ax = plt.subplots(figsize=(6.8, 4.2))
dyn = -1.0
xs = np.linspace(-1.8, 0.8, 20)
E1 = (SK / (1 + SK) * dyn, -K * dyn / (1 + SK))
E2 = (dyn, 0.0)
E3 = (0.0, -K * dyn)
line(ax, K, 0, 0, xs, color=S[0], ls="--", lw=1.4, label="AS before")
line(ax, K, dyn, 0, xs, color=S[0], label="AS after μ ↑ (yₙ′ = −1)")
line(ax, -1 / SG, 0, 0, xs, color=S[1], label="AD, i unchanged → E′")
line(ax, -1 / SG, E2[0], 0, xs, color=S[2], label=f"AD, raise i by {-dyn / SG:.0f} → E''")
line(ax, -1 / SG, 0, E3[1], xs, color=S[3], label=f"AD, cut i by {-K * dyn:.2f} → E'''")
dot(ax, *E1, f"E′ ({E1[0]:.2f}, {E1[1]:+.2f})", INK, off=(8, 2))
dot(ax, *E2, "E'' (−1, 0): p stable", S[2], off=(-6, -16), ha="right")
dot(ax, *E3, f"E''' (0, {E3[1]:+.2f}): y = yₑ", S[3], off=(8, 4))
dot(ax, 0, 0, "E", INK2, off=(6, -14))
axes_yp(ax)
ax.set_ylim(-1.3, 2.3)
legend_below(ax)
ax.set_title("Mark-up shock: AS shifts, yₑ does not; no i reaches p = pᵉ and y = yₑ",
             loc="left", fontsize=10.5)
save(fig, "fig_b06_three_points.svg")

fig, ax = plt.subplots(figsize=(7.0, 3.6))
yopt = TH * K * dyn / (1 + TH * K)
pts = {"E′ (no policy)": E1, "E'' (price stability)": E2, "E''' (efficient y)": E3,
       "optimum (note 10)": (yopt, K * (yopt - dyn))}
assert math.isclose(pts["optimum (note 10)"][1], -K / (1 + TH * K) * dyn)
gap_n = [v[0] - dyn for v in pts.values()]
gap_e = [v[0] for v in pts.values()]
pp = [v[1] for v in pts.values()]
bars(ax, list(pts), [("y − yₙ", S[0], gap_n), ("y − yₑ", S[1], gap_e), ("p − pᵉ", S[2], pp)])
ax.tick_params(axis="x", labelsize=8)
ax.set_ylabel("percent")
ax.set_ylim(-1.3, 1.4)
ax.legend(fontsize=8.5, loc="upper left", ncol=3)
ax.set_title("After a mark-up shock the two gaps have opposite signs, except at the corners",
             loc="left", fontsize=10.5)
save(fig, "fig_b06_gaps.svg")

# =============================== note 07 ===============================
mg, mgb, mt, mtb, mtc, mtcb = multipliers(AL, SG, ET)
out = [mg, -mgb, -mt, -mtb, -mtc, mtcb]
gapn = [mgb, -mgb, mtb, -mtb, -mtcb, mtcb]
gape = [mgb, -mgb, -mt, -mtb, -mtc, mtcb]
assert math.isclose(mg - (1 / SG) / INV, mgb)
fig, ax = plt.subplots(figsize=(9.0, 3.9))
bars(ax, ["g", "ḡ", "τ", "τ̄", "τc", "τ̄c"],
     [("output y, eq. (22)", S[0], out), ("gap y − yₙ, eq. (23)", S[1], gapn),
      ("gap y − yₑ, §7.5", S[2], gape)], width=0.84)
ax.set_xlabel("instrument raised by 1 point (of GDP, or tax rate)")
ax.set_ylabel("effect (points)")
ax.set_ylim(-0.6, 1.1)
ax.legend(fontsize=8.5, loc="upper right")
ax.set_title(f"Baseline calibration: g lifts output {mg:.2f} but the gap only {mgb:.2f} "
             f"(1/{mg / mgb:.0f})", loc="left", fontsize=10.5)
save(fig, "fig_b07_output_vs_gap.svg")

fig, ax = plt.subplots(figsize=(6.6, 3.6))
eta = np.linspace(0, 1.5, 200)
m_all = np.array([multipliers(AL, SG, et) for et in eta])
ax.plot(eta, m_all[:, 0], color=S[0], label="m_g: short-run spending on output")
ax.plot(eta, m_all[:, 1], color=S[1], label="m_ḡ: long-run spending = spending on the gap")
assert math.isclose(multipliers(AL, SG, 0.0)[0], 1.0)
dot(ax, 0, 1.0, "η = 0: m_g = 1 exactly", S[0], off=(6, -16))
for et in (0.2, 1.0):
    m_ = multipliers(AL, SG, et)
    dot(ax, et, m_[0], f"{m_[0]:.2f}", S[0], off=(4, 6))
    dot(ax, et, m_[1], f"{m_[1]:.2f}", S[1], off=(4, 6))
ax.set_xlabel("inverse Frisch elasticity η")
ax.set_ylabel("multiplier")
ax.set_ylim(0, 1.15)
ax.legend(fontsize=8, loc="center right")
ax.set_title("α = 0.66, σ = 0.5: m_g − m_ḡ = σ⁻¹/(σ⁻¹+η) is the part of g that adds capacity",
             loc="left", fontsize=10)
save(fig, "fig_b07_mg_eta.svg")

fig, ax = plt.subplots(figsize=(6.8, 4.0))
et1 = 1.0
k1 = kappa(AL, SG, et1)
mg1, mgb1 = multipliers(AL, SG, et1)[:2]
dg = 1.0
dyn_g = (1 / SG) / (1 / SG + et1) * dg
Ey = mg1 * dg
Ep = k1 * (Ey - dyn_g)
assert math.isclose(Ey - dyn_g, mgb1 * dg)
xs = np.linspace(-0.8, 1.8, 20)
line(ax, k1, 0, 0, xs, color=S[0], ls="--", lw=1.4, label="AS before")
line(ax, k1, dyn_g, 0, xs, color=S[0], label=f"AS after: yₙ′ = {dyn_g:.2f}")
line(ax, -1 / SG, 0, 0, xs, color=S[1], ls="--", lw=1.4, label="AD before")
line(ax, -1 / SG, dg, 0, xs, color=S[1], label="AD after: shifted right by dg = 1")
line(ax, -1 / SG, dyn_g, 0, xs, color=S[2], label="AD after raising i → E''")
dot(ax, Ey, Ep, f"E′ ({Ey:.2f}, {Ep:+.2f}): gap m_ḡ = {mgb1:.2f}", INK, off=(8, 4))
dot(ax, dyn_g, 0, "E''", S[2], off=(-6, -14), ha="right")
dot(ax, 0, 0, "E", INK2, off=(-6, 6), ha="right")
axes_yp(ax)
ax.set_ylim(-1.2, 1.6)
legend_below(ax)
ax.set_title("Fig. 10, η = 1 to make the gap visible: g moves both curves, E′ lands right of yₙ′",
             loc="left", fontsize=10)
save(fig, "fig_b07_fig10.svg")

# =============================== note 08 ===============================
fig, ax = plt.subplots(figsize=(7.0, 4.2))
rho = 1.0
dybn = -3.0
rn = rho + dybn / SG
assert math.isclose(rn, -5.0)
best_gap = SG * rn / (1 + SK)
xs = np.linspace(-4.5, 1.2, 20)
line(ax, K, 0, 0, xs, color=S[0], label="AS (unchanged)")
line(ax, -1 / SG, dybn, 0, xs, color=S[1], label=f"AD after ȳₙ falls {-dybn:.0f}%, i = ρ")
line(ax, -1 / SG, dybn + SG * rho, 0, xs, color=S[3], label="AD₀ ceiling: i = 0")
line(ax, -1 / SG, dybn + SG * rho + SG * (-rn), 0, xs, color=S[2],
     label=f"AD₀ with p̄ − pᵉ = −rₙ = {-rn:.0f}: the initial AD again")
dot(ax, best_gap, K * best_gap, f"E′ at i = 0: gap = σrₙ/(1+σκ) = {best_gap:.2f}", INK, off=(8, -4))
dot(ax, 0, 0, "E = E'' (i = 0, p̄ raised)", S[2], off=(8, 4))
axes_yp(ax)
ax.set_ylim(-4, 2.5)
legend_below(ax)
ax.set_title(f"Pessimism drives rₙ to {rn:.0f}%: i = 0 cannot close the gap, p̄ can",
             loc="left", fontsize=10.5)
save(fig, "fig_b08_trap.svg")

fig, axs = plt.subplots(1, 2, figsize=(8.4, 3.4))
r = np.linspace(-6, 3, 200)
ax = axs[0]
ax.plot(r, np.minimum(0, SG * r / (1 + SK)), color=S[0], label="best gap at i ≥ 0, p̄ = pᵉ")
ax.axvline(0, color=INK2, lw=0.6)
dot(ax, -5, SG * -5 / (1 + SK), f"rₙ = −5: {SG * -5 / (1 + SK):.2f}", S[0], off=(6, 4))
ax.set_xlabel("natural real rate rₙ (%)")
ax.set_ylabel("output gap y − yₙ (%)")
ax.set_title("A kink at rₙ = 0", loc="left", fontsize=10)
ax.legend(fontsize=8, loc="lower right")
ax = axs[1]
ax.plot(r, np.maximum(0, -r), color=S[2], label="needed p̄ − pᵉ = max(0, −rₙ)")
ax.set_xlabel("natural real rate rₙ (%)")
ax.set_ylabel("long-run price commitment (%)")
ax.set_title("The exit: one point of p̄ per point of −rₙ", loc="left", fontsize=10)
ax.legend(fontsize=8, loc="upper right")
fig.suptitle("§8.2 and §8.4: a trap is rₙ < 0, and p̄ fills the slot i cannot",
             x=0.02, ha="left", fontsize=11)
save(fig, "fig_b08_gap_rn.svg")

# =============================== note 09 ===============================
CHI, D0, BETA = 2 / 3, 1.2, 0.99
saver = -SG
limit = -(1 - CHI) * D0 * BETA / CHI
fisher = (1 - CHI) * D0 / CHI
varpi = SG - D0 * (1 - BETA) * (1 - CHI) / CHI
assert math.isclose(saver + limit + fisher, -varpi)
thresh = SG * CHI / ((1 - BETA) * (1 - CHI))
fig, ax = plt.subplots(figsize=(7.0, 3.6))
terms = [("savers' Euler\n−σ", saver), ("borrowing limit\n−(1−χ)d₀β/χ", limit),
         ("Fisher effect\n+(1−χ)d₀/χ", fisher)]
cum = 0.0
for j, (lab, v) in enumerate(terms):
    ax.bar(j, v, bottom=cum, color=S[0] if v >= 0 else S[1], edgecolor=SURF, width=0.6)
    ax.text(j, cum + v / 2, f"{v:+.3f}", ha="center", va="center", fontsize=8.5,
            color=SURF, fontweight="bold")
    cum += v
ax.bar(3, -varpi, color=S[2], width=0.6, edgecolor=SURF)
ax.text(3, -varpi / 2, f"−ϖ =\n{-varpi:.3f}", ha="center", va="center", fontsize=8.5,
        color=SURF, fontweight="bold")
ax.bar(4, fisher, color=S[3], width=0.6, edgecolor=SURF)
ax.text(4, fisher + 0.04, f"+{fisher:.2f}", ha="center", fontsize=8.5)
ax.set_xticks(range(5), [t for t, _ in terms] + ["dy/dp, p̄\nanchored", "dy/dp, p̄ = p\n(Eggertsson–Krugman)"],
              fontsize=7.8)
ax.axhline(0, color=INK2, lw=0.8)
ax.grid(axis="x", visible=False)
ax.set_ylabel("contribution to dy/dp")
ax.set_ylim(-1.25, 0.85)
ax.set_title(f"χ = 2/3, d₀ = 1.2, β = 0.99: AD slopes up only if p̄ tracks p "
             f"(or d₀ > {thresh:.0f})", loc="left", fontsize=10)
save(fig, "fig_b09_slope.svg")

fig, axs = plt.subplots(1, 2, figsize=(8.8, 3.8), sharey=True)
dyn = 0.5
xs = np.linspace(-2, 1.5, 20)
for ax, slope_ad, ttl in [(axs[0], -1 / varpi, f"p̄ anchored: AD slope −1/ϖ = {-1 / varpi:.2f}"),
                          (axs[1], 1 / fisher, f"p̄ = p: AD slope +1/{fisher:.1f} = {1 / fisher:.2f} > κ")]:
    yeq = K * dyn / (K - slope_ad)          # AD: p = slope_ad*y ; AS: p = K(y - dyn)
    peq = slope_ad * yeq
    assert math.isclose(yeq, 0.18 if slope_ad < 0 else -1.06, abs_tol=5e-3)
    line(ax, K, 0, 0, xs, color=S[0], ls="--", lw=1.4, label="AS before")
    line(ax, K, dyn, 0, xs, color=S[0], label=f"AS after yₙ +{dyn}")
    line(ax, slope_ad, 0, 0, xs, color=S[1], label="AD")
    dot(ax, yeq, peq, f"E′: y = {yeq:+.2f}", INK, off=(8, -12))
    dot(ax, 0, 0, "E", INK2, off=(-6, 6), ha="right")
    axes_yp(ax)
    ax.set_ylim(-3, 2)
    ax.set_title(ttl, loc="left", fontsize=9.5)
    ax.legend(fontsize=7.5, loc="lower right")
axs[1].set_ylabel("")
assert K < 1 / fisher                   # footnote 19: AS flatter than AD
fig.suptitle("Paradox of toil: the same favourable AS shift, opposite signs for output",
             x=0.02, ha="left", fontsize=11)
save(fig, "fig_b09_toil.svg")

fig, ax = plt.subplots(figsize=(6.8, 3.8))
d = np.linspace(0, 1.72, 300)
base = dict(alpha=AL, sigma=SG, eta=ET, beta=BETA)
ax.plot(d, [deleveraging_multiplier(chi=CHI, d0=x, **base) for x in d], color=S[0],
        label="p̄ anchored, 1/3 borrowers")
ax.plot(d, [deleveraging_multiplier(chi=0.5, d0=x, **base) for x in d], color=S[1],
        label="p̄ anchored, 1/2 borrowers")
ax.plot(d, [deleveraging_multiplier(chi=CHI, d0=x, anchored=False, **base) for x in d],
        color=S[2], label="zero long-run inflation, 1/3 borrowers")
asym = CHI / ((1 - CHI) * K)
ax.axvline(asym, color=S[2], ls=":", lw=1)
ax.text(asym - 0.02, 0.3, f"pole d₀ = {asym:.2f}", ha="right", fontsize=8, color=S[2])
ax.axhline(1, color=INK2, lw=0.8, ls="--")
ax.axhline(mg, color=INK2, lw=0.8, ls=":")
ax.text(0.02, mg - 0.3, f"normal times m_g = {mg:.2f}", fontsize=8, color=INK2)
for chi, anch, col in [(CHI, True, S[0]), (0.5, True, S[1]), (CHI, False, S[2])]:
    v = deleveraging_multiplier(chi=chi, d0=D0, anchored=anch, **base)
    dot(ax, D0, v, f"{v:.2f}", col, off=(6, 4))
ax.axvline(D0, color=INK2, lw=0.6)
ax.set_xlabel("initial debt d₀ (share of GDP)")
ax.set_ylabel("multiplier on short-run g")
ax.set_ylim(0, 6)
ax.legend(fontsize=8, loc="upper left")
ax.set_title("§9.6: constrained borrowers push the multiplier past one; with p̄ = p it explodes in d₀",
             loc="left", fontsize=10.5)
save(fig, "fig_b09_multiplier.svg")

# =============================== note 10 ===============================
fig, ax = plt.subplots(figsize=(6.8, 4.2))
dyn = -1.0
yo = TH * K * dyn / (1 + TH * K)
po = K * (yo - dyn)
assert math.isclose(yo + TH * po, 0, abs_tol=1e-12)     # targeting rule (34)
aE1 = (SK / (1 + SK) * dyn, -K * dyn / (1 + SK))
di_opt = ((yo - po / (-1 / SG)) - 0) / (-SG)            # AD intercept shift / -sigma
assert math.isclose(di_opt, 1.689, abs_tol=1e-3)
xs = np.linspace(-1.8, 0.8, 20)
line(ax, K, 0, 0, xs, color=S[0], ls="--", lw=1.4, label="AS before")
line(ax, K, dyn, 0, xs, color=S[0], label="AS after μ ↑ (yₙ′ = −1)")
line(ax, -1 / SG, 0, 0, xs, color=S[1], ls="--", lw=1.4, label="AD, i unchanged")
line(ax, -1 / SG, yo, po, xs, color=S[1], label=f"AD at the optimum: i raised {di_opt:.2f}")
line(ax, -1 / TH, 0, 0, xs, color=S[2], label="IT: (y − yₑ) + θ(p − pᵉ) = 0, θ = 8")
dot(ax, *aE1, f"E′ ({aE1[0]:.2f}, {aE1[1]:+.2f})", INK, off=(8, 2))
dot(ax, yo, po, f"optimum ({yo:.2f}, {po:+.2f})", S[2], off=(-8, 10), ha="right")
dot(ax, 0, 0, "E (yₑ, pᵉ)", INK2, off=(6, -14))
axes_yp(ax)
ax.set_ylim(-1.3, 1.6)
legend_below(ax)
ax.set_title(f"Fig. 14: optimum = AS′ ∩ IT; {1 / (1 + TH * K):.0%} of the shock reaches prices",
             loc="left", fontsize=10.5)
save(fig, "fig_b10_it.svg")

fig, ax = plt.subplots(figsize=(6.8, 3.6))
ph = np.linspace(0, 20, 300)
for a_, col in [(0.66, S[0]), (0.75, S[1])]:
    k_ = kappa(a_, SG, ET)
    ax.plot(ph, 1 / (1 + ph * k_), color=col, label=f"α = {a_} (κ = {k_:.2f})")
    dot(ax, TH, 1 / (1 + TH * k_), f"φ = θ = 8: {1 / (1 + TH * k_):.3f}", col,
        off=(6, 8) if a_ == 0.75 else (6, -14))
nopol = 1 / (1 + SK)
dot(ax, SG, nopol, f"φ = σ: {nopol:.2f} = no-policy E′", INK, off=(8, 2))
ax.axvline(SG, color=INK2, lw=0.8, ls=":")
ax.text(SG + 0.3, 0.9, "φ < σ: cut i        φ > σ: raise i", fontsize=8, color=INK2)
ax.set_xlabel("weight on price stability φ (θ for the household)")
ax.set_ylabel("share of shock into prices 1/(1+φκ)")
ax.set_ylim(0, 1.05)
ax.legend(fontsize=8, loc="center right")
ax.set_title("The mandate, not the economy, sets how much of a mark-up shock prices absorb",
             loc="left", fontsize=10.5)
save(fig, "fig_b10_share.svg")

# ---------------------------------------------------------------------------
# Note 11: the three schools and market clearing
# ---------------------------------------------------------------------------

# (1) A market clears at the price where the quantities agree; a stuck price does not.
# Illustrative linear labour market: L^d = 10 - w, L^s = 2 + w.
w_star = (10 - 2) / 2
L_star = 10 - w_star
assert (w_star, L_star) == (4.0, 6.0)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.4, 3.6), sharey=True)
Lg = np.linspace(0, 10, 50)
for ax in (a1, a2):
    ax.plot(Lg, 10 - Lg, color=S[0], label="labour demand Lᵈ = 10 − w")
    ax.plot(Lg, Lg - 2, color=S[1], label="labour supply Lˢ = 2 + w")
    ax.set_xlabel("hours L")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 9)
dot(a1, L_star, w_star, f"clears: w* = {w_star:.0f}, L* = {L_star:.0f}", INK, off=(8, 4))
a1.set_ylabel("real wage w")
a1.set_title("Flexible wage: Lᵈ = Lˢ", loc="left", fontsize=10)
a1.legend(fontsize=7.5, loc="upper right")
wb = 5.0
Ld, Ls = 10 - wb, 2 + wb
assert (Ld, Ls) == (5.0, 7.0)
a2.axhline(wb, color=INK2, ls="--", lw=1)
a2.annotate("", xy=(Ls, wb), xytext=(Ld, wb),
            arrowprops=dict(arrowstyle="<->", color=S[4], lw=1.8))
a2.text((Ld + Ls) / 2 + 0.6, wb + 0.7, f"excess supply {Ls - Ld:.0f}\n= unemployment",
        ha="center", fontsize=8, color=INK)
dot(a2, Ld, wb, f"employed = min(Lᵈ, Lˢ) = {Ld:.0f}", S[0], off=(-8, -18), ha="right")
a2.text(0.3, wb + 0.2, f"w̄ = {wb:.0f} stuck above w*", fontsize=8, color=INK2)
a2.set_title("Wage stuck above w*: the short side decides", loc="left", fontsize=10)
save(fig, "fig_b11_clearing.svg")

# (2) Why a New-Keynesian firm serves extra demand at its posted price.
# Posted price = desired mark-up over marginal cost at y_n; real marginal cost
# rises with output at elasticity sigma^-1 + eta (note 02 section 2.4).
mk = TH / (TH - 1)
y_max = mk ** (1 / INV)
assert math.isclose(mk, 1.142857, abs_tol=1e-6) and math.isclose(y_max, 1.06257, abs_tol=1e-4)
fig, ax = plt.subplots(figsize=(6.8, 3.6))
yy = np.linspace(0.9, 1.12, 200)
ax.plot(100 * (yy - 1), yy ** INV, color=S[0], label="marginal cost (y/yₙ)^(σ⁻¹+η), =1 at yₙ")
ax.axhline(mk, color=S[1], label=f"posted price Pᵉ = θ/(θ−1) × MC(yₙ) = {mk:.3f}")
ax.fill_between(100 * (yy[yy <= y_max] - 1), yy[yy <= y_max] ** INV, mk,
                color=S[2], alpha=0.15, lw=0)
dot(ax, 0, 1, "yₙ: price is 14.3% above MC", INK, off=(8, -14))
dot(ax, 100 * (y_max - 1), mk, f"MC = Pᵉ at +{100 * (y_max - 1):.1f}%", S[1], off=(-8, 8), ha="right")
ax.text(-9.5, 1.07, "shaded: P > MC, the firm\nwants every extra sale", fontsize=8, color=INK)
ax.set_xlabel("output relative to natural (%)")
ax.set_ylabel("price, marginal cost (MC(yₙ) = 1)")
ax.legend(fontsize=8, loc="upper left")
ax.set_title("P > MC: a stuck firm serves the demand, so output is demand-determined",
             loc="left", fontsize=10)
save(fig, "fig_b11_posted_price.svg")

# (3) One demand expansion, four readings: shift AD right by d = 2 at a given p.
d_ = 2.0
gam = 1.0                                   # Lucas supply: y - y_n = gam (p - p^e)
y_nc = gam * d_ / (1 + gam)                 # surprise, AD y = m - p (slope -1)
y_nk = d_ / (1 + SK)                        # AD y = d - sigma p, AS p = kappa y
assert math.isclose(y_nc, 1.0) and math.isclose(y_nk, 1.2766, abs_tol=1e-4)
fig, axs = plt.subplots(2, 2, figsize=(8.4, 6.2), sharex=True, sharey=True)
xs = np.linspace(-1, 3.2, 50)
panels = [
    (axs[0, 0], "Original Keynesian: p fixed", None, (d_, 0.0), -1.0),
    (axs[0, 1], "New Classical, anticipated", "vertical", (0.0, d_), -1.0),
    (axs[1, 0], "New Classical, surprise (γ = 1)", 1 / gam, (y_nc, y_nc / gam), -1.0),
    (axs[1, 1], "New Keynesian (κ = 1.13, σ = 0.5)", K, (y_nk, K * y_nk), -1 / SG),
]
for ax, title, as_slope, (ye, pe_), ad_slope in panels:
    ax.axhline(0, color=INK2, lw=0.5)
    ax.axvline(0, color=INK2, lw=0.5)
    line(ax, ad_slope, 0, 0, xs, color=S[0], ls="--", lw=1.4, label="AD before")
    line(ax, ad_slope, d_, 0, xs, color=S[0], label="AD after (+2 at given p)")
    if as_slope is None:
        ax.axhline(0, color=S[1], label="AS")
    elif as_slope == "vertical":
        ax.axvline(0, color=S[1], label="AS")
    else:
        line(ax, as_slope, 0, 0, xs, color=S[1], label="AS")
    dot(ax, ye, pe_, f"y = {ye:+.2f}, p = {pe_:+.2f}", INK, off=(6, 6))
    ax.set_title(title, loc="left", fontsize=9.5)
    ax.set_xlim(-1, 3.2)
    ax.set_ylim(-1, 3)
axs[1, 0].set_xlabel("output y (% from yₙ)")
axs[1, 1].set_xlabel("output y (% from yₙ)")
axs[0, 0].set_ylabel("price level p (% from pᵉ)")
axs[1, 0].set_ylabel("price level p (% from pᵉ)")
axs[0, 0].legend(fontsize=7.5, loc="upper right")
fig.suptitle("The same demand push: where it lands depends on the AS each school writes",
             x=0.02, ha="left", fontsize=10.5)
save(fig, "fig_b11_four_readings.svg")
