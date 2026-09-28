#!/usr/bin/env python3
"""Figures for the Map/aula-04-consumo notes (Kurlat ch. 6, consumption and saving).

Every number drawn or labelled is computed here, and the ones the notes quote are asserted
before drawing, so a figure never illustrates a number the text does not support.

Run:  python Map/aula-04-consumo/make_figures.py            (writes fig/fig_c0*.svg)
      python Map/aula-04-consumo/make_figures.py --png DIR  (also writes PNG previews to DIR)
"""
from __future__ import annotations

import math
import pathlib
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "fig"))
from mapstyle import INK, INK2, S, SURF, save  # noqa: E402

import matplotlib.pyplot as plt  # noqa: E402  (mapstyle has already chosen the backend)

OUT = pathlib.Path(__file__).resolve().parent / "fig"
PNG = pathlib.Path(sys.argv[sys.argv.index("--png") + 1]) if "--png" in sys.argv else None
BETA, R = 0.96, 0.04
RHO = 1 / BETA - 1


def out(fig, name):
    """Save `fig` as fig/<name>.svg through mapstyle, plus a PNG preview when --png is given."""
    if PNG is not None:
        PNG.mkdir(parents=True, exist_ok=True)
        fig.tight_layout()
        fig.savefig(PNG / f"{name}.png", dpi=110)
    save(fig, OUT / f"{name}.svg")


def title(ax, text):
    ax.set_title(text, loc="left", color=INK, fontsize=10.5)


def closed(y1, y2, r=R, beta=BETA, sigma=1.0, W=None):
    """CRRA closed form of note 02 sec. 2.4: returns (c1, c2, W)."""
    W = y1 + y2 / (1 + r) if W is None else W
    c1 = W / (1 + beta ** (1 / sigma) * (1 + r) ** (1 / sigma - 1))
    return c1, (1 + r) * (W - c1), W


def annuity_factor(r, T):
    """Consumption per unit of wealth on a flat path over T periods (note 04 sec. 4.3)."""
    return (r / (1 + r)) / (1 - (1 + r) ** (-T))


def indiff(c1, U, beta=BETA, sigma=1.0):
    """c2 on the indifference curve u(c1) + beta u(c2) = U."""
    if sigma == 1.0:
        return np.exp((U - np.log(c1)) / beta)
    v = (U - (c1 ** (1 - sigma) - 1) / (1 - sigma)) / beta
    with np.errstate(invalid="ignore"):          # NaN left of the curve's asymptote: not drawn
        return (v * (1 - sigma) + 1) ** (1 / (1 - sigma))


def util(c1, c2, beta=BETA, sigma=1.0):
    uu = (lambda c: math.log(c)) if sigma == 1.0 else (lambda c: (c ** (1 - sigma) - 1) / (1 - sigma))
    return uu(c1) + beta * uu(c2)


# =========================== note 01 ===========================
# Kuznets: permanent income Yp, measured Y = Yp + transitory, C = k Yp. Within one year the
# regression of C on Y has slope k*lam and intercept k(1-lam)*mean(Yp) (lam = signal share),
# so it looks Keynesian; across decades the era means lie on the ray C = kY.
k, lam = 0.9, 0.6
eras = [("1870s", 40.0), ("1900s", 80.0), ("1940s", 160.0)]
fig, ax = plt.subplots(figsize=(6.8, 4.0))
yy = np.linspace(0, 230, 10)
ax.plot(yy, k * yy, color=INK2, lw=1.2, label=f"long run: C = {k}·Y (APC constant)")
for (lab, m), col in zip(eras, S):
    slope, icpt = k * lam, k * (1 - lam) * m
    assert math.isclose(icpt + slope * m, k * m)   # each cross-section crosses the ray at its mean
    x = np.linspace(0.4 * m, 1.6 * m, 20)
    ax.plot(x, icpt + slope * x, color=col, label=f"{lab} cross-section: C = {icpt:.1f} + {slope:.2f}·Y")
    ax.plot([m], [k * m], "o", color=col, ms=6, zorder=3)
x0 = 1.5 * eras[0][1]
apc_hi = (k * (1 - lam) * eras[0][1] + k * lam * x0) / x0
x1 = 0.5 * eras[0][1]
apc_lo = (k * (1 - lam) * eras[0][1] + k * lam * x1) / x1
assert apc_lo > k > apc_hi
ax.annotate(f"within a year APC falls\nfrom {apc_lo:.2f} to {apc_hi:.2f}", (x0, apc_hi * x0),
            xytext=(95, 20), color=INK2, fontsize=8.5,
            arrowprops=dict(arrowstyle="->", color=INK2, lw=0.8))
ax.set_xlim(0, 260)
ax.set_ylim(0, 240)
ax.set_xlabel("measured income Y (index)")
ax.set_ylabel("consumption C (index)")
ax.legend(fontsize=8, loc="upper left")
title(ax, "Each year's cross-section looks Keynesian; the decades line up on one ray")
out(fig, "fig_c01_kuznets")

# Announcement: rebate of 1 known at t=2, paid at t=5; flat-path household, r = rho = 4%,
# horizon ends at t=9. Keynesian: C moves by mpc at t=5 only.
mpc_k, r_a, T_end, t_ann, t_pay = 0.8, 0.04, 10, 2, 5
pv = 1 / (1 + r_a) ** (t_pay - t_ann)
dc = annuity_factor(r_a, T_end - t_ann) * pv
assert math.isclose(sum(dc / (1 + r_a) ** j for j in range(T_end - t_ann)), pv)
t = np.arange(T_end)
d_inc = (t == t_pay).astype(float)
d_key = mpc_k * d_inc
d_pih = np.where(t >= t_ann, dc, 0.0)
fig, ax = plt.subplots(figsize=(6.8, 3.6))
ax.bar(t - 0.2, d_inc, width=0.2, color=INK2, alpha=0.35, label="income (rebate paid)")
ax.bar(t, d_key, width=0.2, color=S[1], label=f"Keynesian, mpc = {mpc_k}")
ax.bar(t + 0.2, d_pih, width=0.2, color=S[0], label="permanent income: flat path from the news")
ax.axvline(t_ann - 0.4, color=INK2, lw=0.8, ls=":")
ax.text(t_ann - 0.35, 0.93, "announced", color=INK2, fontsize=8.5)
ax.text(t_pay + 0.35, 0.93, "paid", color=INK2, fontsize=8.5)
ax.text(t_ann + 0.2, dc + 0.03, f"+{dc:.3f}", color=S[0], fontsize=8.5, ha="center")
ax.text(t_pay, mpc_k + 0.03, f"+{mpc_k}", color=S[1], fontsize=8.5, ha="center")
ax.set_xticks(t)
ax.set_ylim(0, 1.25)
ax.set_xlabel("period t")
ax.set_ylabel("change from baseline (units)")
ax.legend(fontsize=8, loc="upper right")
title(ax, "News moves PIH consumption at t = 2; the Keynesian one waits for the cash")
out(fig, "fig_c01_announcement")

# =========================== note 02 ===========================
y1, y2, r2 = 100.0, 66.0, 0.5
c1s, c2s, W2 = closed(y1, y2, r2)
assert math.isclose(W2, 144.0) and math.isclose(c1s, W2 / (1 + BETA))
U2 = util(c1s, c2s)
eps = 1e-6
ic_slope = (indiff(c1s + eps, U2) - indiff(c1s - eps, U2)) / (2 * eps)
assert math.isclose(ic_slope, -(1 + r2), rel_tol=1e-6)   # tangency = Euler
fig, ax = plt.subplots(figsize=(6.4, 4.6))
x = np.linspace(0, W2, 50)
ax.plot(x, (1 + r2) * (W2 - x), color=S[0], label=f"budget line, slope −(1+r) = −{1 + r2}")
xi = np.linspace(40, W2 * 0.99, 200)
ax.plot(xi, indiff(xi, U2), color=S[1], label="indifference curve through the optimum")
ax.plot([y1], [y2], "o", color=INK, ms=6)
ax.annotate(f"endowment ({y1:.0f}, {y2:.0f})", (y1, y2), xytext=(-8, -14), textcoords="offset points",
            fontsize=8.5, ha="right")
ax.plot([c1s], [c2s], "o", color=S[1], ms=7)
ax.annotate(f"optimum ({c1s:.1f}, {c2s:.1f})", (c1s, c2s), xytext=(8, 6), textcoords="offset points",
            fontsize=8.5)
ax.annotate("", (c1s, 8), (y1, 8), arrowprops=dict(arrowstyle="<->", color=S[2]))
ax.text((c1s + y1) / 2, 12, f"saving y₁ − c₁ = {y1 - c1s:.1f}", color=S[2], ha="center", fontsize=8.5)
ax.text(W2 + 2, 6, f"W = {W2:.0f}", fontsize=8.5, color=INK2)
ax.text(3, (1 + r2) * W2 + 4, f"(1+r)W = {(1 + r2) * W2:.0f}", fontsize=8.5, color=INK2)
ax.set_xlim(0, 170)
ax.set_ylim(0, 240)
ax.set_xlabel("c₁, consumption today")
ax.set_ylabel("c₂, consumption tomorrow")
ax.legend(fontsize=8, loc="upper right")
title(ax, f"Tangency left of the endowment: this household saves (log, r = {r2})")
out(fig, "fig_c02_budget")

# Route 3 as a picture: objective and the two sides of the Euler equation.
c1g = np.linspace(30, 125, 300)
V = np.log(c1g) + BETA * np.log((1 + r2) * (W2 - c1g))
mc, mb = 1 / c1g, BETA * (1 + r2) / ((1 + r2) * (W2 - c1g))
assert math.isclose(1 / c1s, BETA / (W2 - c1s))
fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.4, 3.6))
a1.plot(c1g, V, color=S[0])
a1.axvline(c1s, color=INK2, lw=0.8, ls=":")
a1.plot([c1s], [util(c1s, c2s)], "o", color=S[0])
a1.text(c1s + 2, V.min() + 0.05, f"c₁* = {c1s:.1f}", color=INK2, fontsize=8.5)
a1.set_xlabel("c₁ (c₂ = (1+r)(W − c₁) substituted in)")
a1.set_ylabel("lifetime utility")
title(a1, "Route 1: maximise over c₁ alone")
a2.plot(c1g, mc * 100, color=S[0], label="cost of saving 1 more: u′(c₁)")
a2.plot(c1g, mb * 100, color=S[1], label="benefit: β(1+r)u′(c₂)")
a2.plot([c1s], [100 / c1s], "o", color=INK)
a2.text(c1s + 3, 100 / c1s + 0.15, f"equal at c₁* = {c1s:.1f}", fontsize=8.5)
a2.text(33, 0.45, "left: cost > benefit\n→ raise c₁", fontsize=8, color=INK2)
a2.text(75, 2.6, "right: benefit > cost\n→ lower c₁", fontsize=8, color=INK2)
a2.set_xlabel("c₁")
a2.set_ylabel("marginal utility (×100)")
a2.set_ylim(0, 4)
a2.legend(fontsize=8, loc="upper left")
title(a2, "Route 3: the perturbation balances")
out(fig, "fig_c02_perturbation")

# Tilt of the path: exact ln(c2/c1) against (r - rho)/sigma.
rr = np.linspace(0.0, 0.10, 100)
fig, ax = plt.subplots(figsize=(6.4, 3.8))
for sig, col in zip((0.5, 1.0, 2.0), S):
    exact = (math.log(BETA) + np.log(1 + rr)) / sig
    ax.plot(rr * 100, exact, color=col, label=f"σ = {sig}  (EIS = {1 / sig:g})")
    ax.plot(rr * 100, (rr - RHO) / sig, color=col, lw=1, ls=":")
    c1t, c2t, _ = closed(100, 100, 0.08, sigma=sig)
    assert math.isclose(math.log(c2t / c1t), (math.log(BETA) + math.log(1.08)) / sig)
ax.axhline(0, color=INK2, lw=0.8)
ax.plot([RHO * 100], [0], "o", color=INK)
ax.annotate(f"r = ρ = {RHO * 100:.2f}%: flat path", (RHO * 100, 0), xytext=(5.2, -0.06), fontsize=8.5,
            arrowprops=dict(arrowstyle="->", color=INK2, lw=0.8))
ax.plot([], [], color=INK2, lw=1, ls=":", label="dotted: first-order (r − ρ)/σ")
ax.set_xlabel("real interest rate r (%)")
ax.set_ylabel("ln(c₂/c₁), growth of consumption")
ax.legend(fontsize=8, loc="upper left")
title(ax, "The path tilts up when r > ρ, by 1/σ per unit of r")
out(fig, "fig_c02_tilt")

# =========================== note 03 ===========================
# Hicks decomposition for a lender whose income effect wins (sigma = 3), with long periods.
yh1, yh2, r0, r1, sh = 150.0, 20.0, 0.10, 1.00, 3.0
A = closed(yh1, yh2, r0, sigma=sh)
Cc = closed(yh1, yh2, r1, sigma=sh)
Wc = A[0] + A[1] / (1 + r1)                       # wealth that just buys the old bundle at r1
B = closed(0, 0, r1, sigma=sh, W=Wc)
assert A[0] < yh1                                  # a lender
assert B[0] < A[0] and Cc[0] > B[0] and Cc[0] > A[0]   # subst lowers c1, income raises it more
fig, ax = plt.subplots(figsize=(6.6, 4.8))
x = np.linspace(0, 170, 50)
ax.plot(x, yh2 + (1 + r0) * (yh1 - x), color=S[0], ls="--", label=f"old line, r = {r0:.0%}")
ax.plot(x, yh2 + (1 + r1) * (yh1 - x), color=S[0], label=f"new line, r = {r1:.0%} (pivots on endowment)")
ax.plot(x, (1 + r1) * (Wc - x), color=INK2, lw=1, ls=":", label="compensated: new slope, old bundle")
for P, lab, col in ((A, "A old", S[1]), (B, "B compensated", S[2]), (Cc, "C new", S[3])):
    ax.plot([P[0]], [P[1]], "o", color=col, ms=7, zorder=3)
    ax.annotate(f"{lab} ({P[0]:.1f}, {P[1]:.1f})", (P[0], P[1]), xytext=(8, -2), textcoords="offset points",
                fontsize=8.5, color=INK)
xi = np.linspace(55, 160, 200)
ax.plot(xi, indiff(xi, util(A[0], A[1], sigma=sh), sigma=sh), color=S[1], lw=1, ls="--")
ax.plot(xi, indiff(xi, util(Cc[0], Cc[1], sigma=sh), sigma=sh), color=S[3], lw=1)
ax.plot([yh1], [yh2], "o", color=INK, ms=6)
ax.annotate("endowment", (yh1, yh2), xytext=(6, 4), textcoords="offset points", fontsize=8.5)
ax.annotate("", (B[0], 45), (A[0], 45), arrowprops=dict(arrowstyle="->", color=S[2]))
ax.text(B[0] - 1, 50, f"substitution {B[0] - A[0]:+.1f}", fontsize=8, color=S[2], ha="right")
ax.annotate("", (Cc[0], 35), (B[0], 35), arrowprops=dict(arrowstyle="->", color=S[3]))
ax.text(B[0] + 1, 25, f"income {Cc[0] - B[0]:+.1f}", fontsize=8, color=S[3])
ax.set_xlim(0, 175)
ax.set_ylim(0, 200)
ax.set_xlabel("c₁")
ax.set_ylabel("c₂")
ax.legend(fontsize=8, loc="upper right")
title(ax, f"Lender, σ = {sh:g}: the income effect outweighs substitution, so c₁ rises by {Cc[0] - A[0]:.1f}")
out(fig, "fig_c03_hicks")

# The two terms of d ln c1 / d ln(1+r) against sigma, for the lender (150, 50) at r = 4%.
yl1, yl2 = 150.0, 50.0
Wl = yl1 + yl2 / (1 + R)
omega = (yl2 / (1 + R)) / Wl
sg = np.linspace(0.25, 6, 300)
D = 1 + BETA ** (1 / sg) * (1 + R) ** (1 / sg - 1)
theta = 1 - 1 / D
fixw = -theta * (1 / sg - 1)
total = -omega + fixw


def total_at(s):
    Ds = 1 + BETA ** (1 / s) * (1 + R) ** (1 / s - 1)
    return -omega - (1 - 1 / Ds) * (1 / s - 1)


lo, hi = 1.0, 6.0
for _ in range(80):
    mid = 0.5 * (lo + hi)
    lo, hi = (lo, mid) if total_at(mid) > 0 else (mid, hi)
s_star = 0.5 * (lo + hi)
h = 1e-6                                           # the formula against a finite difference at s*
fd = (math.log(closed(yl1, yl2, math.expm1(math.log1p(R) + h), sigma=s_star)[0])
      - math.log(closed(yl1, yl2, R, sigma=s_star)[0])) / h
assert abs(fd) < 1e-4
fig, ax = plt.subplots(figsize=(6.6, 3.8))
ax.plot(sg, np.full_like(sg, -omega), color=S[0], label=f"human-wealth term −ω = {-omega:.3f}")
ax.plot(sg, fixw, color=S[1], label="fixed-W term −θ(1/σ − 1)")
ax.plot(sg, total, color=INK, label="total d ln c₁ / d ln(1+r)")
ax.axhline(0, color=INK2, lw=0.8)
ax.axvline(1, color=INK2, lw=0.8, ls=":")
ax.text(1.05, 0.33, "σ = 1: fixed-W term is 0", fontsize=8, color=INK2)
ax.plot([s_star], [0], "o", color=INK)
ax.annotate(f"σ* = {s_star:.2f}: c₁ stops falling", (s_star, 0), xytext=(s_star + 0.4, -0.35),
            fontsize=8.5, arrowprops=dict(arrowstyle="->", color=INK2, lw=0.8))
ax.set_xlabel("σ (inverse EIS)")
ax.set_ylabel("elasticity of c₁ w.r.t. 1+r")
ax.set_ylim(-0.9, 0.45)
ax.legend(fontsize=8, loc="lower right")
title(ax, f"Lender (y₁, y₂) = ({yl1:.0f}, {yl2:.0f}): above σ* ≈ {s_star:.1f} a higher r raises c₁")
out(fig, "fig_c03_terms")

# Saving against r for a lender and a borrower.
rg = np.linspace(0.0, 0.20, 100)
yb1, yb2 = 20.0, 200.0
fig, axs = plt.subplots(1, 2, figsize=(8.6, 3.6))
for ax_, (p1, p2, who) in zip(axs, ((yl1, yl2, "lender"), (yb1, yb2, "borrower"))):
    for sig, col in zip((0.5, 1.0, 4.0), S):
        sv = np.array([p1 - closed(p1, p2, r_, sigma=sig)[0] for r_ in rg])
        ax_.plot(rg * 100, sv, color=col, label=f"σ = {sig:g}")
        rising = sv[-1] > sv[0]
        if who == "borrower":
            assert rising and np.all(np.diff(sv) > 0)
        else:
            assert rising == (sig <= 1.0) and np.all(sv > 0)
    ax_.set_xlabel("r (%)")
    ax_.set_ylabel("saving s₁ = y₁ − c₁")
    ax_.legend(fontsize=8)
title(axs[0], f"Lender ({yl1:.0f}, {yl2:.0f}): sign depends on σ")
title(axs[1], f"Borrower ({yb1:.0f}, {yb2:.0f}): saving rises for every σ")
out(fig, "fig_c03_saving")

# =========================== note 04 ===========================
base = closed(100, 100)[0]
mpc_t = closed(101, 100)[0] - base
mpc_p = closed(101, 101)[0] - base
assert math.isclose(mpc_t, 1 / (1 + BETA)) and math.isclose(mpc_p, (2 + R) / ((1 + R) * (1 + BETA)))
assert round(mpc_t, 2) == 0.51 and round(mpc_p, 2) == 1.00
fig, ax = plt.subplots(figsize=(6.6, 2.8))
labels = ["transitory: y₁ +1", "permanent: y₁ and y₂ +1"]
cons, sav = [mpc_t, mpc_p], [1 - mpc_t, 1 - mpc_p]
ax.barh(labels, cons, color=S[0], height=0.5, label="Δc₁ (MPC)")
ax.barh(labels, [max(s_, 0) for s_ in sav], left=cons, color=S[1], height=0.5, label="Δs₁")
for i, (c_, s_) in enumerate(zip(cons, sav)):
    ax.text(c_ / 2, i, f"Δc₁ = {c_:.3f}", color=SURF, ha="center", va="center", fontsize=9)
    ax.text(1.02, i, f"Δs₁ = {s_:+.3f}", color=INK2, va="center", fontsize=9)
ax.invert_yaxis()
ax.set_xlim(0, 1.3)
ax.set_xlabel("response in period 1 to a +1 rise in y₁ (log, β = 0.96, r = 4%)")
ax.grid(axis="y", visible=False)
ax.legend(fontsize=8, loc="upper center", bbox_to_anchor=(0.5, -0.32), ncol=2)
title(ax, "Half of a transitory windfall is saved, none of a permanent one")
out(fig, "fig_c04_mpc_split")

# The windfall MPC against the horizon: the annuity factor against 1/T.
Ts = np.arange(1, 81)
af = annuity_factor(R, Ts)
assert math.isclose(annuity_factor(R, 40), 0.0485, abs_tol=5e-4)
assert math.isclose(annuity_factor(R, 2), 0.5098, abs_tol=1e-4)
fig, ax = plt.subplots(figsize=(6.6, 3.8))
ax.plot(Ts, af, color=S[0], label="exact MPC at r = 4%: (r/(1+r)) / [1 − (1+r)^(−T)]")
ax.plot(Ts, 1 / Ts, color=S[1], ls=":", label="r → 0 rule: 1/T")
ax.axhline(R / (1 + R), color=INK2, lw=0.9, ls="--")
ax.text(52, R / (1 + R) * 0.84, f"floor r/(1+r) = {R / (1 + R):.3f}", fontsize=8.5, color=INK2)
for T_ in (2, 40):
    ax.plot([T_], [annuity_factor(R, T_)], "o", color=S[0])
    ax.annotate(f"T = {T_}: {annuity_factor(R, T_):.3f} vs 1/T = {1 / T_:.3f}", (T_, annuity_factor(R, T_)),
                xytext=(8, 6), textcoords="offset points", fontsize=8.5)
ax.set_yscale("log")
ax.set_xlabel("remaining horizon T (periods)")
ax.set_ylabel("MPC out of a windfall (log scale)")
ax.legend(fontsize=8, loc="upper right")
title(ax, "Longer horizons shrink the windfall MPC, but it bottoms out at r/(1+r)")
out(fig, "fig_c04_horizon")

# Smoothing: income with transitory noise and one permanent step; consumption by the PIH.
rng = np.random.default_rng(4)
n, t_step, step = 60, 30, 10.0
eps_t = rng.normal(0, 5, n)
perm = np.where(np.arange(n) >= t_step, step, 0.0)
y_path = 100 + perm + eps_t
kk = R / (1 + R)
dc_path = kk * eps_t + np.diff(np.concatenate([[0.0], perm]))   # permanent news moves c 1-for-1
c_path = 100 + np.cumsum(dc_path)
assert math.isclose(np.std(kk * eps_t) / np.std(eps_t), kk)
fig, ax = plt.subplots(figsize=(6.8, 3.6))
ax.plot(y_path, color=S[1], lw=1.2, label="income y_t = ȳ + permanent step + transitory noise")
ax.plot(c_path, color=S[0], label="consumption: moves r/(1+r) per transitory unit, 1 per permanent")
ax.annotate(f"permanent +{step:.0f}: c jumps +{step:.0f}", (t_step, c_path[t_step]),
            xytext=(38, 90), fontsize=8.5, arrowprops=dict(arrowstyle="->", color=INK2, lw=0.8))
ax.text(1, 82, f"sd(Δc)/sd(ε) = r/(1+r) = {kk:.3f} for transitory shocks", fontsize=8.5, color=INK2)
ax.set_ylim(80, 134)
ax.set_xlabel("period t")
ax.set_ylabel("level (units)")
ax.legend(fontsize=8, loc="upper left")
title(ax, "Consumption ignores transitory noise, follows the permanent shift")
out(fig, "fig_c04_smoothing")

# =========================== note 05 ===========================
ys1, ys2 = 40.0, 120.0
cu1, cu2, Ws = closed(ys1, ys2)
assert cu1 > ys1                                          # wants to borrow
ic_E = (1 / ys1) / (BETA / ys2)                           # |slope| of IC at the endowment
assert ic_E > 1 + R                                       # Euler inequality at the corner
fig, ax = plt.subplots(figsize=(6.4, 4.6))
xa = np.linspace(0, Ws, 50)
ax.plot(xa, (1 + R) * (Ws - xa), color=S[0], ls="--", lw=1.3, label="budget line with free borrowing")
xf = np.linspace(0, ys1, 20)
ax.plot(xf, (1 + R) * (Ws - xf), color=S[0], lw=2.6, label="feasible with a ≥ 0 (c₁ ≤ y₁)")
ax.axvline(ys1, color=INK2, lw=0.8, ls=":")
xi = np.linspace(15, 150, 300)
ax.plot(xi, indiff(xi, util(cu1, cu2)), color=S[1], lw=1, ls="--")
ax.plot([cu1], [cu2], "o", color=S[1])
ax.annotate(f"wanted ({cu1:.1f}, {cu2:.1f})", (cu1, cu2), xytext=(8, 4), textcoords="offset points",
            fontsize=8.5)
xi2 = np.linspace(28, 150, 300)
ax.plot(xi2, indiff(xi2, util(ys1, ys2)), color=S[2], label="indifference curve through the corner")
ax.plot([ys1], [ys2], "o", color=INK, ms=7)
ax.annotate(f"corner = endowment ({ys1:.0f}, {ys2:.0f})\nIC slope −{ic_E:.2f} vs budget −{1 + R:.2f}",
            (ys1, ys2), xytext=(55, 150), fontsize=8.5, arrowprops=dict(arrowstyle="->", color=INK2, lw=0.8))
ax.set_xlim(0, 170)
ax.set_ylim(0, 200)
ax.set_xlabel("c₁")
ax.set_ylabel("c₂")
ax.legend(fontsize=8, loc="upper right")
title(ax, "A binding limit parks the household at its endowment: u′(c₁) > β(1+r)u′(c₂)")
out(fig, "fig_c05_constraint")

# Aggregate MPC against the constrained share.
share = np.linspace(0, 1, 50)
agg = (1 - share) * kk + share
assert math.isclose(0.7 * kk + 0.3, 0.3269, abs_tol=1e-4)
lo_s, hi_s = (0.2 - kk) / (1 - kk), (0.4 - kk) / (1 - kk)
fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.axhspan(0.2, 0.4, color=S[3], alpha=0.18, lw=0, label="estimated rebate MPCs, 0.2–0.4")
ax.plot(share * 100, agg, color=S[0], label="aggregate MPC = χ·r/(1+r) + (1 − χ)·1")
ax.plot([30], [0.7 * kk + 0.3], "o", color=INK)
ax.annotate(f"30% constrained → {0.7 * kk + 0.3:.3f}", (30, 0.7 * kk + 0.3), xytext=(40, 0.2),
            fontsize=8.5, arrowprops=dict(arrowstyle="->", color=INK2, lw=0.8))
ax.axvline(lo_s * 100, color=INK2, lw=0.8, ls=":")
ax.axvline(hi_s * 100, color=INK2, lw=0.8, ls=":")
ax.text(lo_s * 100 + 0.8, 0.9, f"{lo_s:.0%}–{hi_s:.0%}", fontsize=8.5, color=INK2)
ax.set_xlabel("share of hand-to-mouth households 1 − χ (%)")
ax.set_ylabel("aggregate MPC")
ax.legend(fontsize=8, loc="lower right")
title(ax, f"A constrained share of {lo_s:.0%}–{hi_s:.0%} puts the aggregate MPC in the data's range")
out(fig, "fig_c05_mpc_mix")

# Jensen: convex u' (CRRA sigma = 2) against linear u' (quadratic utility).
clo, chi_, cm = 70.0, 130.0, 100.0
cg = np.linspace(55, 150, 200)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.6, 3.6))
for ax_, f, lab, unit in ((a1, lambda c: 1e4 * c ** -2.0, "CRRA σ = 2: u′ convex", "u′(c) × 10⁴"),
                          (a2, lambda c: 1 - 0.005 * c, "quadratic: u′ = 1 − 0.005c, linear", "u′(c)")):
    Eu = 0.5 * (f(clo) + f(chi_))
    ax_.plot(cg, f(cg), color=S[0], label=lab)
    ax_.plot([clo, chi_], [f(clo), f(chi_)], color=INK2, lw=1, ls=":")
    ax_.plot([cm], [Eu], "o", color=S[1], label=f"E[u′(c₂)] = {Eu:.3f}")
    ax_.plot([cm], [f(cm)], "o", color=INK, label=f"u′(E c₂) = {f(cm):.3f}")
    for c_ in (clo, chi_):
        ax_.axvline(c_, color=INK2, lw=0.6, ls=":")
    ax_.set_xlabel(f"c₂ (equally likely {clo:.0f} or {chi_:.0f}, mean {cm:.0f})")
    ax_.set_ylabel(unit)
    ax_.legend(fontsize=8, loc="upper right")
assert 0.5 * (clo ** -2 + chi_ ** -2) > cm ** -2
assert math.isclose(0.5 * ((1 - 0.005 * clo) + (1 - 0.005 * chi_)), 1 - 0.005 * cm)
title(a1, "Risk raises expected u′: save more")
title(a2, "No gap: no precautionary saving")
out(fig, "fig_c05_jensen")
