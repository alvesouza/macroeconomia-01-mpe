#!/usr/bin/env python3
"""Figures for the Map/aula-05-trabalho notes (Kurlat 2020, ch. 7).

Every number drawn or labelled is computed here and asserted against the closed form the
notes derive, so a figure never illustrates a claim the algebra does not support. The same
closed forms are verified independently in check_labour.py.

Run:  python Map/aula-05-trabalho/make_figures.py            (writes fig/*.svg)
      python Map/aula-05-trabalho/make_figures.py --png DIR  (also writes PNG previews to DIR)
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
EF, EH, EM, WR = (r"$\varepsilon^F$", r"$\varepsilon^H$", r"$\varepsilon^M$", "$w^r$")
PNG = pathlib.Path(sys.argv[sys.argv.index("--png") + 1]) if "--png" in sys.argv else None


def out(fig, name: str) -> None:
    """Save `fig` as fig/<name>.svg via mapstyle, plus a PNG preview when --png was given."""
    if PNG is not None:
        PNG.mkdir(parents=True, exist_ok=True)
        fig.tight_layout()
        fig.savefig(PNG / name.replace(".svg", ".png"), dpi=110)
    save(fig, OUT / name)


def close(a, b, tol=1e-9):
    assert abs(a - b) <= tol, (a, b)


def dot(ax, x, y, col, label=None, dx=8, dy=6, ha="left"):
    """Mark a key point and label it with its values."""
    ax.plot(x, y, "o", ms=7, color=col, mec=SURF, mew=1.5, zorder=5)
    if label:
        ax.annotate(label, (x, y), xytext=(dx, dy), textcoords="offset points",
                    color=INK, fontsize=8.5, ha=ha)


# ============================================================ 01-measurement
E, U, N = 150.0, 10.0, 40.0
scen = [("baseline", E, U, N),
        ("2 stop searching\n(U → N)", E, U - 2, N + 2),
        ("recession: 3 jobs lost,\n8 leave the labour force", E - 3, U - 5, N + 8)]
urate = [100 * u / (e + u) for _, e, u, n in scen]
epop = [100 * e / (e + u + n) for _, e, u, n in scen]
close(urate[0], 6.25), close(urate[1], 100 * 8 / 158), close(urate[2], 100 * 5 / 152)
close(epop[0], 75.0), close(epop[1], 75.0), close(epop[2], 73.5)
assert urate[1] < urate[0] and urate[2] < urate[0] and epop[2] < epop[0]

fig, axes = plt.subplots(1, 2, figsize=(8.2, 3.5))
x = np.arange(3)
for ax, vals, col, lab, top in [(axes[0], urate, S[0], "unemployment rate U/(E+U), %", 8),
                                (axes[1], epop, S[1], "employment–population E/(E+U+N), %", 80)]:
    ax.bar(x, vals, 0.6, color=col, edgecolor=SURF, linewidth=2)
    for i, v in enumerate(vals):
        ax.text(i, v + top * 0.015, f"{v:.2f}", ha="center", color=INK, fontsize=9)
    ax.set_xticks(x, [s[0] for s in scen], fontsize=7.8)
    ax.set_ylabel(lab)
    ax.set_ylim(0, top)
    ax.grid(axis="x", visible=False)
axes[1].set_ylim(60, 80)
axes[0].set_title("The rate falls in both changes", loc="left", fontsize=10)
axes[1].set_title("E/pop is unmoved by giving up, falls with job loss", loc="left", fontsize=10)
fig.suptitle("Discouragement lowers the unemployment rate; only E/pop shows the recession",
             x=0.02, ha="left", fontsize=11)
out(fig, "fig_discouragement.svg")

# ---------- the Beveridge curve in note notation: M = A_m U^xi V^(1-xi)
LAM, AM, XI = 0.034, 0.6, 0.5


def bev_v(u, lam=LAM, am=AM, xi=XI):
    """Vacancy rate on the Beveridge curve: lam(1-u) = A_m v^(1-xi) u^xi solved for v."""
    return (lam * (1 - u) / (am * u ** xi)) ** (1 / (1 - xi))


def u_at_theta(theta, lam=LAM, am=AM, xi=XI):
    """Steady-state unemployment at tightness theta: lam/(lam + A_m theta^(1-xi))."""
    return lam / (lam + am * theta ** (1 - xi))


uu = np.linspace(0.025, 0.14, 300)
AM1 = 0.45
uB, uS = 0.04, 0.09
vB, vS = bev_v(uB), bev_v(uS)
thB, thS = vB / uB, vS / uS
close(u_at_theta(thB), uB, 1e-12), close(u_at_theta(thS), uS, 1e-12)
uB1 = u_at_theta(thB, am=AM1)
vB1 = thB * uB1
close(bev_v(uB1, am=AM1), vB1, 1e-12)            # B' lies on the shifted curve
assert uB1 > uB and vB1 > vB

fig, ax = plt.subplots(figsize=(6.6, 4.2))
ax.plot(uu * 100, bev_v(uu) * 100, "--", color=S[0], label=f"before: A_m = {AM}")
ax.plot(uu * 100, bev_v(uu, am=AM1) * 100, color=S[0], label=f"after: A_m = {AM1} (worse matching)")
for th, col in [(thB, INK2), (thS, INK2)]:
    ax.plot([0, 14], [0, 14 * th], ":", color=col, linewidth=1)
ax.text(2.3, 2.3 * thB + 1.3, f"ray θ = v/u = {thB:.2f}", color=INK2, fontsize=8.5)
ax.text(11.6, 12.3 * thS + 0.5, f"ray θ = {thS:.2f}", color=INK2, fontsize=8.5)
dot(ax, uB * 100, vB * 100, S[1], f"boom: u = {uB:.0%}, v = {vB:.1%}", dx=8, dy=0)
dot(ax, uS * 100, vS * 100, S[1], f"slump: u = {uS:.0%}, v = {vS:.1%}", dx=-4, dy=-16, ha="right")
dot(ax, uB1 * 100, vB1 * 100, S[2], f"same θ after the shift:\nu = {uB1:.1%}, v = {vB1:.1%}",
    dx=10, dy=4)
ax.text(8.0, 7.0, f"movement along the dashed curve:\nθ falls from {thB:.2f} to {thS:.2f}",
        color=S[1], fontsize=8.5)
ax.set_xlim(2, 14), ax.set_ylim(0, 14)
ax.set_xlabel("unemployment rate u, %")
ax.set_ylabel("vacancy rate v, %")
ax.legend(fontsize=8.5, loc="upper right")
ax.set_title("Along the curve θ moves; a fall in A_m moves the whole curve out",
             loc="left", fontsize=10.5)
out(fig, "fig_beveridge_along_vs_shift.svg")

# ============================================================ 02-static-model
HBAR, TH = 1.0, 1.5


def leisure(w, pi, th=TH, hbar=HBAR):
    """Log-log leisure, corner-capped: theta/(1+theta) (w hbar + pi)/w, at most hbar."""
    return min(th / (1 + th) * (w * hbar + pi) / w, hbar)


# Slutsky decomposition at pi = 0: w 1 -> 2.
w0, w1 = 1.0, 2.0
lA = leisure(w0, 0.0)
cA = w0 * (HBAR - lA)
ubar = math.log(cA) + TH * math.log(lA)
lB = math.exp((ubar - math.log(w1 / TH)) / (1 + TH))   # tangency c = w1 l/theta on IC ubar
cB = w1 * lB / TH
lC = leisure(w1, 0.0)
cC = w1 * (HBAR - lC)
close(lA, 0.6), close(lC, 0.6), close(math.log(cB) + TH * math.log(lB), ubar)
close(TH * cB / lB, w1)
assert lB < lA

ll = np.linspace(0.05, 1.0, 400)
fig, ax = plt.subplots(figsize=(6.6, 4.3))
ax.plot([0, HBAR], [w0 * HBAR, 0], "--", color=S[0], label=f"budget before, w = {w0:g}")
ax.plot([0, HBAR], [w1 * HBAR, 0], color=S[0], label=f"budget after, w = {w1:g}")
ax.plot(ll, cB + w1 * (lB - ll), ":", color=INK2, linewidth=1.3,
        label="compensated budget (slope −2, old utility)")
ax.plot(ll, np.exp(ubar) * ll ** -TH, color=S[1], linewidth=1.5, label="indifference curves")
ax.plot(ll, np.exp(math.log(cC) + TH * math.log(lC)) * ll ** -TH, color=S[1], linewidth=1.5)
dot(ax, lA, cA, S[2], f"A: ℓ = {lA:.2f}, c = {cA:.2f}", dx=8, dy=-2)
dot(ax, lB, cB, S[2], f"B: ℓ = {lB:.3f}", dx=-8, dy=8, ha="right")
dot(ax, lC, cC, S[2], f"C: ℓ = {lC:.2f}, c = {cC:.2f}", dx=8, dy=2)
ax.annotate("", (lB, cB - 0.05), (lA, cA + 0.05),
            arrowprops=dict(arrowstyle="->", color=INK2, lw=1.2))
ax.text(0.08, 0.3, "A→B substitution:\nleisure dearer, ℓ falls", fontsize=8.5, color=INK2)
ax.text(0.63, 1.0, "B→C income:\nℓ rises back", fontsize=8.5, color=INK2)
ax.set_xlim(0, 1.05), ax.set_ylim(0, 2.1)
ax.set_xlabel("leisure ℓ (share of the time endowment h̄ = 1)")
ax.set_ylabel("consumption c")
ax.legend(fontsize=8, loc="upper right")
ax.set_title("ln c + 1.5 ln ℓ, π = 0: doubling w moves A→B→C and leisure ends at 0.60",
             loc="left", fontsize=10)
out(fig, "fig_slutsky_loglog.svg")

# Hours against the wage for three levels of non-wage income.
ww = np.linspace(0.05, 5, 500)
fig, ax = plt.subplots(figsize=(6.6, 3.9))
for pi, col in [(0.0, S[0]), (0.3, S[1]), (0.6, S[2])]:
    h = [HBAR - leisure(w, pi) for w in ww]
    ax.plot(ww, h, color=col, label=f"π = {pi:g}")
    if pi > 0:
        wr = TH * pi / HBAR
        close(HBAR - leisure(wr, pi), 0.0, 1e-12)
        dot(ax, wr, 0, col, f"{WR} = θπ/h̄ = {wr:.2f}", dx=6, dy=-14 if pi > 0.4 else 10)
ax.text(3.3, HBAR / (1 + TH) + 0.012, f"h̄/(1+θ) = {HBAR / (1 + TH):.2f}", color=INK2, fontsize=8.5)
close(HBAR - leisure(3.0, 0.3), HBAR / (1 + TH) - TH / (1 + TH) * 0.3 / 3.0)
ax.set_xlabel("real wage w")
ax.set_ylabel("hours h (share of h̄)")
ax.set_ylim(-0.05, 0.46)
ax.legend(fontsize=9, loc="lower right")
ax.set_title("π = 0: vertical supply. π > 0: a reservation wage, then hours rise with w",
             loc="left", fontsize=10.5)
out(fig, "fig_hours_vs_wage.svg")

# The participation corner.
pi_c = 0.3
wr_c = TH * pi_c / HBAR
u_end = math.log(pi_c) + TH * math.log(HBAR)
wlo, whi = 0.3, 0.9
l_hi = leisure(whi, pi_c)
c_hi = pi_c + whi * (HBAR - l_hi)
close(l_hi, 0.8), close(TH * c_hi / l_hi, whi)
ll = np.linspace(0.45, 1.0, 300)
fig, ax = plt.subplots(figsize=(6.4, 4.0))
ax.plot(ll, np.exp(u_end) * ll ** -TH, color=S[1], label="indifference curve through the endowment")
ax.plot(ll, pi_c + wr_c * (HBAR - ll), ":", color=INK2, linewidth=1.2,
        label=f"its slope at the endowment: {WR} = {wr_c:.2f}")
ax.plot(ll, pi_c + wlo * (HBAR - ll), color=S[0], linewidth=1.6,
        label=f"budget, w = {wlo} < {WR}: stay at the corner")
ax.plot(ll, pi_c + whi * (HBAR - ll), color=S[2], linewidth=1.6,
        label=f"budget, w = {whi} > {WR}: work")
dot(ax, HBAR, pi_c, INK, f"endowment (h̄, π) = (1, {pi_c})", dx=-8, dy=-14, ha="right")
dot(ax, l_hi, c_hi, S[2], f"optimum: h = {HBAR - l_hi:.2f}", dx=8, dy=4)
ax.set_xlim(0.45, 1.03), ax.set_ylim(0.2, 1.0)
ax.set_xlabel("leisure ℓ")
ax.set_ylabel("consumption c")
ax.legend(fontsize=8, loc="upper right")
ax.set_title("Work iff the budget line is steeper than the indifference curve at the corner",
             loc="left", fontsize=10)
out(fig, "fig_reservation_corner.svg")

# ============================================================ 03-elasticities
# Three responses through the same point: pi = 0, w0 = 2.
w0 = 2.0
l0 = leisure(w0, 0.0)
h0 = HBAR - l0
c0 = w0 * h0
mu0 = 1 / c0
u0 = math.log(c0) + TH * math.log(l0)
wg = np.linspace(1.4, 3.0, 200)
hM = np.full_like(wg, h0)
hH = HBAR - np.exp((u0 - np.log(wg / TH)) / (1 + TH))
hF = HBAR - TH / (mu0 * wg)
eH, eF = TH / (1 + TH), l0 / h0
d = 1e-6
num = lambda f: (math.log(f(w0 * (1 + d))) - math.log(f(w0 * (1 - d)))) / (2 * d)
close(num(lambda w: HBAR - math.exp((u0 - math.log(w / TH)) / (1 + TH))), eH, 1e-6)
close(num(lambda w: HBAR - TH / (mu0 * w)), eF, 1e-6)
close(eF, TH)
fig, ax = plt.subplots(figsize=(6.6, 4.0))
ax.plot(wg, hF, color=S[0], label=f"Frisch, μ fixed: {EF} = ℓ/h = {eF:.2f}")
ax.plot(wg, hH, color=S[1], label=f"Hicksian, utility fixed: {EH} = θ/(1+θ) = {eH:.2f}")
ax.plot(wg, hM, color=S[2], label=f"Marshallian, π fixed: {EM} = 0")
ax.set_xscale("log"), ax.set_yscale("log")
ax.set_xticks([1.5, 2, 2.5, 3], ["1.5", "2", "2.5", "3"])
ax.set_yticks([0.2, 0.3, 0.4, 0.5, 0.6], ["0.2", "0.3", "0.4", "0.5", "0.6"])
ax.minorticks_off()
dot(ax, w0, h0, INK, f"common point: w = {w0:g}, h = {h0:.2f}", dx=8, dy=-14)
ax.set_xlabel("real wage w (log scale)")
ax.set_ylabel("hours h (log scale)")
ax.legend(fontsize=8.5, loc="upper left")
ax.set_title(f"Slopes on log axes are the elasticities: {EF} ≥ {EH} ≥ {EM} (ln c + 1.5 ln ℓ, π = 0)",
             loc="left", fontsize=10)
out(fig, "fig_three_elasticities.svg")

# Prescott, Kurlat Ex. 7.5: u = ln c + alpha ln l, balanced budget T = tau w (1 - l).
ALPHA = 1.54
tau_us, tau_eu = 0.34, 0.53
h_bal = lambda t: (1 - t) / (1 + ALPHA - t)
close(h_bal(tau_us), 0.3, 1e-12), close(h_bal(tau_eu), 0.47 / 2.01, 1e-12)
frisch_us = (1 - h_bal(tau_us)) / h_bal(tau_us)
close(frisch_us, 7 / 3, 1e-12)
tt = np.linspace(0, 0.7, 200)
fig, ax = plt.subplots(figsize=(6.6, 3.9))
ax.plot(tt, h_bal(tt), color=S[0], label="revenue rebated as T = τw(1−ℓ): h = (1−τ)/(1+α−τ)")
ax.plot(tt, np.full_like(tt, 1 / (1 + ALPHA)), color=S[1],
        label=f"revenue thrown away (T = 0): h = 1/(1+α) = {1 / (1 + ALPHA):.3f}")
dot(ax, tau_us, h_bal(tau_us), S[0], f"US: τ = {tau_us}, h = {h_bal(tau_us):.3f}", dx=8, dy=4)
dot(ax, tau_eu, h_bal(tau_eu), S[0], f"Europe: τ = {tau_eu}, h = {h_bal(tau_eu):.3f}",
    dx=-6, dy=-16, ha="right")
ax.set_xlabel("marginal tax rate on labour τ")
ax.set_ylabel("hours h (share of lifetime)")
ax.set_ylim(0.15, 0.45)
ax.legend(fontsize=8.5, loc="upper right")
ax.set_title(f"α = {ALPHA}: taxes cut hours only because the revenue comes back",
             loc="left", fontsize=10.5)
out(fig, "fig_prescott_hours.svg")

# Evidence ranges against what the model needs.
rows = [("Prime-age men, intensive margin", 0.1, 0.3),
        ("Extensive margin, all", 0.2, 0.4),
        ("Kurlat's empirical range, Ex. 7.5(l)", 0.4, 1.0),
        ("Married women, secondary earners", 0.5, 1.0),
        ("Macro calibrations", 2.0, 4.0)]
fig, ax = plt.subplots(figsize=(7.0, 3.3))
for i, (lab, lo, hi) in enumerate(rows):
    ax.plot([lo, hi], [i, i], color=S[0], linewidth=8, solid_capstyle="butt")
    ax.text(hi + 0.06, i, f"{lo:g}–{hi:g}", va="center", fontsize=8.5, color=INK2)
ax.axvline(frisch_us, color=S[1], linewidth=1.8)
ax.text(frisch_us + 0.05, -0.55, f"Prescott's model, US: ℓ/h = {frisch_us:.2f}",
        color=S[1], fontsize=8.5)
ax.set_yticks(range(len(rows)), [r[0] for r in rows], fontsize=8.5)
ax.invert_yaxis()
ax.set_xlim(0, 4.6), ax.set_ylim(len(rows) - 0.5, -0.9)
ax.set_xlabel(f"Frisch elasticity of hours {EF}")
ax.grid(axis="y", visible=False)
ax.set_title(f"The model needs {EF} ≈ 2.3; micro evidence sits at 0.1–1",
             loc="left", fontsize=10.5)
out(fig, "fig_elasticity_evidence.svg")

# ============================================================ 04-dynamic
fig, ax = plt.subplots(figsize=(6.4, 3.9))
rw = np.linspace(0.8, 1.2, 200)
for eta, col in [(0.5, S[0]), (1.0, S[1]), (3.0, S[2])]:
    ax.plot(rw, rw ** (1 / eta), color=col, label=f"η = {eta:g}  ({EF} = {1 / eta:.2f})")
    y = 1.1 ** (1 / eta)
    dot(ax, 1.1, y, col, f"{y:.3f}", dx=6, dy=-4)
close(1.1 ** 2, 1.21)
ax.axvline(1.1, color=INK2, linestyle=":", linewidth=1)
ax.set_xlabel("relative wage w₁/w₂ (with β(1+r) = 1)")
ax.set_ylabel("relative hours h₁/h₂")
ax.legend(fontsize=8.5, loc="upper left")
ax.set_title(r"$h_1/h_2=(w_1/w_2)^{1/\eta}$: a" + f" 10% transitory premium moves hours by ≈ {EF} × 10%",
             loc="left", fontsize=10)
out(fig, "fig_relative_hours.svg")

R2 = 0.04
BETA2 = 1 / (1 + R2)


def two_period(w1, w2, eta=1.0, chi=1.0, r=R2, beta=BETA2, pi=0.0):
    """Solve ln c1 - chi h1^(1+eta)/(1+eta) + beta[...] s.t. lifetime budget, by bisection on mu."""
    def gap(mu):
        c1, c2 = 1 / mu, beta * (1 + r) / mu
        h1 = (mu * w1 / chi) ** (1 / eta)
        h2 = (mu * w2 / (beta * (1 + r) * chi)) ** (1 / eta)
        return w1 * h1 + w2 * h2 / (1 + r) + pi - c1 - c2 / (1 + r), h1, h2
    lo, hi = 1e-6, 1e6
    for _ in range(300):
        mid = math.sqrt(lo * hi)
        if gap(mid)[0] > 0:
            hi = mid
        else:
            lo = mid
    return gap(math.sqrt(lo * hi))[1:]


base = two_period(1.0, 1.0)
temp = two_period(1.1, 1.0)
perm = two_period(1.1, 1.1)
close(base[0], 1.0, 1e-9), close(perm[0], 1.0, 1e-9), close(perm[1], 1.0, 1e-9)
close(temp[0] / temp[1], 1.1, 1e-9)
mu_t = math.sqrt((1 + 1 / (1 + R2)) / (1.21 + 1 / (1 + R2)))
close(temp[0], 1.1 * mu_t, 1e-9), close(temp[1], mu_t, 1e-9)
pct = lambda a: [100 * (a[0] - 1), 100 * (a[1] - 1)]
fig, ax = plt.subplots(figsize=(6.4, 3.6))
x = np.arange(2)
for k, (lab, vals, col) in enumerate([("period 1 hours h₁", [pct(temp)[0], pct(perm)[0]], S[0]),
                                      ("period 2 hours h₂", [pct(temp)[1], pct(perm)[1]], S[1])]):
    bars = ax.bar(x + (k - 0.5) * 0.36, vals, 0.34, color=col, label=lab,
                  edgecolor=SURF, linewidth=2)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + (0.25 if v >= 0 else -0.6),
                f"{v + 0.0:+.2f}%".replace("-0.00", "0.00"), ha="center", fontsize=9, color=INK)
ax.axhline(0, color=INK2, linewidth=1)
ax.set_xticks(x, ["transitory: w₁ +10%, w₂ fixed", "permanent: w₁ and w₂ +10%"])
ax.set_ylabel("change in hours vs. baseline, %")
ax.set_ylim(-7, 7)
ax.grid(axis="x", visible=False)
ax.legend(fontsize=8.5, loc="upper right")
ax.set_title("η = 1, ln c, β(1+r) = 1: only the transitory rise moves hours",
             loc="left", fontsize=10.5)
out(fig, "fig_temp_vs_perm.svg")

# ============================================================ 05-search
us, eu = (0.035, 0.40), (0.009, 0.10)
ustar = lambda lam, f: lam / (lam + f)
close(ustar(*us) * 100, 8.046, 1e-3), close(ustar(*eu) * 100, 8.257, 1e-3)
ug = np.linspace(0, 0.2, 200)
fig, axes = plt.subplots(1, 2, figsize=(8.2, 3.6), sharey=True)
for ax, (lam, f), name in [(axes[0], us, "US-style"), (axes[1], eu, "Europe-style")]:
    us_ = ustar(lam, f)
    flow = f * us_
    close(lam * (1 - us_), flow, 1e-15)
    ax.plot(ug * 100, lam * (1 - ug) * 100, color=S[0], label=f"inflow λ(1−u), λ = {lam}")
    ax.plot(ug * 100, f * ug * 100, color=S[1], label=f"outflow f·u, f = {f}")
    dot(ax, us_ * 100, flow * 100, INK,
        f"u* = {us_:.2%}\nflow = {flow:.2%} of L/month\nspell 1/f = {1 / f:g} months",
        dx=8, dy=-44 if lam > 0.02 else 30)
    ax.set_title(name, loc="left", fontsize=10)
    ax.set_xlabel("unemployment rate u, %")
    ax.legend(fontsize=8, loc="upper right")
    ax.set_ylim(0, 8)
axes[0].set_ylabel("flow, % of the labour force per month")
fig.suptitle("Same u* ≈ 8%: Europe gets there with flows four times smaller and spells four "
             "times longer", x=0.02, ha="left", fontsize=10.5)
out(fig, "fig_flow_balance.svg")

tg = np.linspace(0.2, 3.0, 300)
f_ = lambda th: AM * th ** (1 - XI)
q_ = lambda th: AM * th ** (-XI)
close(f_(2.0), 2.0 * q_(2.0), 1e-12)
fig, ax = plt.subplots(figsize=(6.4, 3.8))
ax.plot(tg, f_(tg), color=S[0], label=r"job-finding rate $f = A_m\theta^{1-\xi}$")
ax.plot(tg, q_(tg), color=S[1], label=r"vacancy-filling rate $q = A_m\theta^{-\xi}$")
dot(ax, 1.0, f_(1.0), INK, f"θ = 1: f = q = {AM}", dx=-8, dy=8, ha="right")
dot(ax, 2.0, f_(2.0), S[0], f"θ = 2: f = {f_(2.0):.3f} = θ·q", dx=6, dy=6)
dot(ax, 2.0, q_(2.0), S[1], f"q = {q_(2.0):.3f}", dx=6, dy=-12)
ax.set_xlabel("market tightness θ = V/U (vacancies per unemployed worker)")
ax.set_ylabel("rate per month")
ax.set_ylim(0, 1.45)
ax.legend(fontsize=8.5, loc="upper center")
ax.set_title(f"A_m = {AM}, ξ = {XI}: tighter markets help workers and hurt firms",
             loc="left", fontsize=10.5)
out(fig, "fig_matching_rates.svg")

v_mark = 0.04


def u_on_curve(v, lam=LAM, am=AM, xi=XI):
    """Invert the Beveridge curve at vacancy rate v by bisection."""
    lo, hi = 1e-6, 0.999
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if bev_v(m, lam, am, xi) > v:
            lo = m
        else:
            hi = m
    return 0.5 * (lo + hi)


cases = [("before: A_m = 0.6, λ = 0.034", LAM, AM, S[0], "--"),
         ("A_m falls to 0.45", LAM, AM1, S[1], "-"),
         ("λ rises to 0.040", 0.040, AM, S[2], "-")]
fig, ax = plt.subplots(figsize=(6.6, 4.0))
for lab, lam, am, col, ls in cases:
    ax.plot(uu * 100, bev_v(uu, lam, am) * 100, ls, color=col, label=lab)
    um = u_on_curve(v_mark, lam, am)
    close(bev_v(um, lam, am), v_mark, 1e-9)
    dot(ax, um * 100, v_mark * 100, col, f"u = {um:.2%}", dx=4, dy=-14 if lam > LAM else 8)
ax.axhline(v_mark * 100, color=INK2, linestyle=":", linewidth=1)
ax.set_xlim(2, 14), ax.set_ylim(0, 14)
ax.set_xlabel("unemployment rate u, %")
ax.set_ylabel("vacancy rate v, %")
ax.legend(fontsize=8.5, loc="upper right")
ax.set_title("Worse matching and more separations both shift the curve out (v = 4% marked)",
             loc="left", fontsize=10)
out(fig, "fig_beveridge_shifters.svg")

# Reservation wage: w - b = beta/(1-beta) E[(w' - w)^+], offers w' ~ N(1, 0.3^2).
MU_W, SD_W, BETA_S = 1.0, 0.3, 0.8


def phi(z):
    return math.exp(-z * z / 2) / math.sqrt(2 * math.pi)


def Phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def option(w, sd=SD_W):
    """E[(w' - w)^+] for w' ~ N(MU_W, sd^2)."""
    z = (w - MU_W) / sd
    return sd * phi(z) + (MU_W - w) * (1 - Phi(z))


def w_res(b, beta=BETA_S, sd=SD_W):
    lo, hi = b, b + 10
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if m - b < beta / (1 - beta) * option(m, sd):
            lo = m
        else:
            hi = m
    return 0.5 * (lo + hi)


b0, b1 = 0.4, 0.6
wr0, wr1 = w_res(b0), w_res(b1)
assert wr1 > wr0
acc0, acc1 = 1 - Phi((wr0 - MU_W) / SD_W), 1 - Phi((wr1 - MU_W) / SD_W)
wv = np.linspace(0.6, 1.8, 300)
rhs = np.array([BETA_S / (1 - BETA_S) * option(w) for w in wv])
fig, ax = plt.subplots(figsize=(6.6, 4.0))
ax.plot(wv, rhs, color=S[0], label="β/(1−β)·E[(w′−w)⁺]: value of waiting for a better offer")
ax.plot(wv, wv - b0, "--", color=S[1], label=f"w − b, b = {b0}: gain from accepting now")
ax.plot(wv, wv - b1, color=S[1], label=f"w − b, b = {b1}")
dot(ax, wr0, wr0 - b0, S[1]), dot(ax, wr1, wr1 - b1, S[1])
ax.text(1.22, 0.22, f"b = {b0}: {WR} = {wr0:.3f}, accept {acc0:.0%} of offers\n"
        f"b = {b1}: {WR} = {wr1:.3f}, accept {acc1:.0%} of offers", fontsize=8.5, color=INK)
ax.set_xlabel("candidate wage w")
ax.set_ylabel("per-period value, units of the wage")
ax.set_ylim(0, 1.4)
ax.legend(fontsize=8, loc="upper right")
ax.set_title(f"β = {BETA_S}, offers N(1, 0.3²): higher benefits raise {WR} and cut acceptance",
             loc="left", fontsize=10)
out(fig, "fig_reservation_wage_search.svg")
