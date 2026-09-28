#!/usr/bin/env python3
"""Figures for the Map/aula-07-moeda-inflacao notes (Kurlat chs. 10-11).

Every number drawn or labelled is computed here and asserted against the value the
notes (and check_money.py) quote, so a figure never illustrates a wrong claim. The
companion pages already draw the single Baumol-Tobin cost curve, the sawtooth, the
realised-inflation dial and the Laffer curve with a revenue need; these figures show
the shifts, contrasts and time paths the companions do not.

Run: python Map/aula-07-moeda-inflacao/make_figures.py [--png DIR]
     writes fig/*.svg next to this file; --png also writes PNG previews to DIR.
"""
from __future__ import annotations

import math
import pathlib
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "fig"))
from mapstyle import S, INK, INK2, save  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

FIG = pathlib.Path(__file__).resolve().parent / "fig"
PNG = pathlib.Path(sys.argv[sys.argv.index("--png") + 1]) if "--png" in sys.argv else None


def out(fig, name: str) -> None:
    """Save `fig` as fig/<name>.svg via mapstyle, plus a PNG preview when --png was given."""
    if PNG:
        PNG.mkdir(parents=True, exist_ok=True)
        fig.tight_layout()
        fig.savefig(PNG / f"{name}.png", dpi=110)
    save(fig, FIG / f"{name}.svg")


def title(ax, text):
    ax.set_title(text, loc="left", color=INK, fontsize=11)


def close(a, b, tol=1e-9):
    return abs(a - b) <= tol


# ============================================================ 01 money supply
c, th = 0.20, 0.10


def mult(c, th):
    return (c + 1) / (c + th)


m = mult(c, th)
assert close(m, 4.0)

# Deposit-expansion chain: one unit of base; share s of each new receipt is kept as currency.
s = c / (1 + c)
rounds = np.arange(0, 26)
dep_k = (1 - s) * ((1 - th) * (1 - s)) ** rounds          # new deposits in round k
cur_k = np.where(rounds == 0, s, s * (1 - th) * np.r_[0, dep_k[:-1]])  # new currency
D_cum, C_cum = np.cumsum(dep_k), np.cumsum(cur_k)
assert close(D_cum[-1] + C_cum[-1], m, 2e-2)
assert close((1 - s) / (1 - (1 - th) * (1 - s)), 1 / (c + th))  # D total = 1/(c+theta)

fig, ax = plt.subplots(figsize=(6.6, 3.6))
ax.plot(rounds, C_cum + D_cum, color=S[0], marker="o", ms=3, label="M1 = currency + deposits")
ax.plot(rounds, D_cum, color=S[1], label="deposits D")
ax.plot(rounds, C_cum, color=S[2], label="currency C")
ax.axhline(m, color=INK2, ls="--", lw=1)
ax.text(25, m + 0.08, f"limit m = (c+1)/(c+θ) = {m:.1f}", ha="right", va="bottom", color=INK2)
ax.axhline(1 / (c + th), color=S[1], ls=":", lw=1)
ax.text(25, 1 / (c + th) - 0.1, f"D → 1/(c+θ) = {1 / (c + th):.2f}", ha="right", va="top",
        color=S[1], fontsize=9)
ax.set_xlabel("round of re-lending k")
ax.set_ylabel("cumulative stock per unit of base")
ax.set_ylim(0, 4.6)
ax.legend(loc="center right", fontsize=8.5, bbox_to_anchor=(1.0, 0.45))
title(ax, f"One unit of base becomes {m:.0f} units of M1 (c = {c}, θ = {th})")
out(fig, "fig_07_deposit_chain")

th_grid = np.linspace(0.02, 1.0, 300)
fig, ax = plt.subplots(figsize=(6.4, 3.6))
for cc, col in ((0.2, S[0]), (0.4, S[1])):
    ax.plot(th_grid, mult(cc, th_grid), color=col, label=f"c = {cc}")
pts = [(0.10, "normal: θ = 0.10"), (0.95, "post-2008: θ = 0.95")]
for t, lab in pts:
    v = mult(0.2, t)
    ax.plot(t, v, "o", color=S[0])
    ax.annotate(f"{lab}, m = {v:.2f}", (t, v), xytext=(8, 10) if t < 0.5 else (0, 40),
                textcoords="offset points", arrowprops=None if t < 0.5 else dict(arrowstyle="-", color=INK2),
                ha="left" if t < 0.5 else "right", color=INK)
assert close(mult(0.2, 0.95), 1.2 / 1.15) and close(mult(0.2, 1.0), 1.0)
ax.axhline(1, color=INK2, ls="--", lw=1)
ax.text(0.3, 0.55, "m = 1 at θ = 1: the base is the money stock", color=INK2, fontsize=9)
ax.set_xlabel("reserve ratio θ = R/D")
ax.set_ylabel("money multiplier m = M1/B")
ax.set_ylim(0, 7)
ax.legend(loc="upper right", fontsize=8.5)
title(ax, "Raising θ (or c) shrinks the multiplier toward one")
out(fig, "fig_07_multiplier_theta")

# ============================================================ 02 money demand
F, Y = 2.0, 1000.0


def nstar(i, F=F, Y=Y):
    return math.sqrt(i * Y / (2 * F))


def md(i, F=F, Y=Y):
    return math.sqrt(F * Y / (2 * i))


def vel(i, F=F, Y=Y):
    return math.sqrt(2 * i * Y / F)


assert close(md(0.05), math.sqrt(20000), 1e-9) and close(md(0.10), 100.0)
assert close(nstar(0.05), math.sqrt(12.5)) and close(nstar(0.10), 5.0)

n = np.linspace(0.6, 12, 400)
fig, ax = plt.subplots(figsize=(6.6, 3.8))
ax.plot(n, F * n, color=INK2, lw=1.2, label="transaction cost F·n (same for both)")
for i, ls, col, lab in ((0.05, "--", S[0], "total cost, i = 5% (before)"),
                        (0.10, "-", S[1], "total cost, i = 10% (after)")):
    ax.plot(n, F * n + i * Y / (2 * n), color=col, ls=ls, label=lab)
    ns = nstar(i)
    cs = 2 * math.sqrt(F * i * Y / 2)
    assert close(cs, F * ns + i * Y / (2 * ns))
    ax.plot(ns, cs, "o", color=col)
    ax.annotate(f"n* = {ns:.2f}, cost {cs:.1f}", (ns, cs), xytext=(0, -24 if i < 0.07 else 14),
                textcoords="offset points", ha="center", color=col, fontsize=9)
ax.set_xlabel("trips to the bank per period, n")
ax.set_ylabel("cost per period (goods)")
ax.set_ylim(0, 60)
ax.legend(loc="upper right", fontsize=8.5)
title(ax, "A higher i moves the minimum right: more trips, less cash")
out(fig, "fig_07_bt_cost_shift")

ii = np.linspace(0.01, 0.15, 300)
fig, ax = plt.subplots(figsize=(6.4, 3.8))
for FF, ls, col, lab in ((2.0, "--", S[0], "F = 2 (before)"), (1.0, "-", S[1], "F = 1 (after: ATMs, cards)")):
    ax.plot([md(x, F=FF) for x in ii], ii * 100, color=col, ls=ls, label=lab)
    v = md(0.05, F=FF)
    ax.plot(v, 5, "o", color=col)
    ax.annotate(f"{v:.1f}", (v, 5), xytext=(10, 10) if FF > 1.5 else (-34, -16),
                textcoords="offset points", color=col)
assert close(md(0.05, F=1.0) / md(0.05, F=2.0), 1 / math.sqrt(2))
ax.annotate("", xy=(md(0.05, F=1.0) + 3, 5), xytext=(md(0.05, F=2.0) - 3, 5),
            arrowprops=dict(arrowstyle="->", color=INK2))
ax.text(170, 8, "every point moves left by × 1/√2 = 0.707", color=INK2, fontsize=9)
ax.set_xlabel("real balances M/P (goods, Y = 1000)")
ax.set_ylabel("nominal interest rate i (%)")
ax.set_xlim(0, 330)
ax.legend(loc="upper right", fontsize=8.5)
title(ax, "Halving F shifts money demand left at every i")
out(fig, "fig_07_md_F_shift")

YY = np.linspace(100, 3000, 300)
k = md(0.05) / Y                     # Cambridge k chosen so both agree at Y = 1000
fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.plot(YY, [md(0.05, Y=y) for y in YY], color=S[0], label="Baumol–Tobin √(FY/2i), ε_Y = ½")
ax.plot(YY, k * YY, color=S[1], label=f"Cambridge kY (k = {k:.4f}), ε_Y = 1")
for y, col, val in ((1000, INK2, md(0.05)), (2000, S[0], md(0.05, Y=2000)), (2000, S[1], k * 2000)):
    ax.plot(y, val, "o", color=col)
    ax.annotate(f"{val:.0f}", (y, val), xytext=(8, -4), textcoords="offset points", color=col)
assert close(md(0.05, Y=2000) / md(0.05), math.sqrt(2)) and close(k * 2000 / md(0.05), 2.0)
ax.set_xlabel("income Y (goods per period), i = 5%, F = 2")
ax.set_ylabel("real balances M/P (goods)")
ax.legend(loc="upper left", fontsize=8.5)
title(ax, "Doubling Y raises cash by √2 = 1.41, not by 2")
out(fig, "fig_07_bt_vs_cambridge")

fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.plot(ii * 100, [vel(x) for x in ii], color=S[0], label="Baumol–Tobin V = √(2iY/F)")
ax.axhline(vel(0.05), color=S[1], ls="--", label="quantity theory: V held at its 5% value")
for x in (0.05, 0.10):
    ax.plot(x * 100, vel(x), "o", color=S[0])
    ax.annotate(f"V = {vel(x):.2f}", (x * 100, vel(x)), xytext=(6, -14), textcoords="offset points",
                color=S[0])
assert close(vel(0.05), math.sqrt(50)) and close(vel(0.10), 10.0)
ax.set_xlabel("nominal interest rate i (%)")
ax.set_ylabel("velocity V = PY/M (per period)")
ax.legend(loc="upper left", fontsize=8.5)
title(ax, "Velocity rises with i: constant V is an assumption")
out(fig, "fig_07_velocity")

# ============================================================ 03 equilibrium
gap = 0.10
pis = np.linspace(0, 0.6, 300)
r_ex = gap / (1 + pis)                # (1+i)/(1+pi) - 1 with i = pi + gap
assert close((1 + 0.60) / (1 + 0.50) - 1, gap / 1.5) and close(gap / 1.5, 0.0666667, 1e-6)
fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.plot(pis * 100, np.full_like(pis, gap * 100), color=S[1], ls="--", label="approximation r ≈ i − π")
ax.plot(pis * 100, r_ex * 100, color=S[0], label="exact r = (1+i)/(1+π) − 1 = (i − π)/(1+π)")
for p in (0.02, 0.50):
    rv = gap / (1 + p)
    ax.plot(p * 100, rv * 100, "o", color=S[0])
    ax.annotate(f"π = {p:.0%}: r = {rv:.2%}", (p * 100, rv * 100),
                xytext=(6, 7.0) if p < 0.1 else (36, 6.0), textcoords="data", color=S[0],
                fontsize=9, arrowprops=dict(arrowstyle="->", color=S[0]))
ax.annotate("gap = rπ", xy=(50, 8.3), xytext=(36, 8.3), color=INK2, va="center",
            arrowprops=dict(arrowstyle="-", color=INK2))
ax.plot([50, 50], [gap / 1.5 * 100, 10], color=INK2, lw=1)
ax.set_xlabel("inflation π (%), with i = π + 10 points")
ax.set_ylabel("real rate r (%)")
ax.set_ylim(5, 11)
ax.legend(loc="lower left", fontsize=8.5)
title(ax, "At high inflation i − π overstates the real rate")
out(fig, "fig_07_fisher_exact")

t = np.linspace(0, 20, 200)
cases = [(0.0, 0.0, S[0], "(a) μ = 0"), (0.05, 0.0, S[1], "(b) μ = 5%, g = 0"),
         (0.05, 0.04, S[2], "(c) μ = 5%, g = 4%, ε_Y = ½")]
fig, ax = plt.subplots(figsize=(6.4, 3.6))
for mu, g, col, lab in cases:
    pi = mu - 0.5 * g
    ax.plot(t, pi * t, color=col, label=f"{lab}: π = {pi:.0%}")
    ax.annotate(f"P × {math.exp(pi * 20):.2f}", (20, pi * 20), xytext=(-4, 6),
                textcoords="offset points", ha="right", color=col, fontsize=9)
assert close(0.05 - 0.5 * 0.04, 0.03)
ax.set_xlabel("years t")
ax.set_ylabel("ln P_t − ln P_0 (slope = π)")
ax.legend(loc="upper left", fontsize=8.5)
title(ax, "Same money growth, less inflation when the economy grows")
out(fig, "fig_07_steady_states")

r_real, mu0, mu1 = 0.02, 0.02, 0.10
i0, i1 = r_real + mu0, r_real + mu1
jump = 0.5 * math.log(i1 / i0)
assert close(math.exp(jump), math.sqrt(3)) and close(math.exp(jump), md(i0) / md(i1))
tt = np.linspace(-5, 10, 301)
lnM = np.where(tt < 0, mu0 * tt, mu1 * tt)
lnP = np.where(tt < 0, mu0 * tt, mu1 * tt + jump)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.4, 3.6))
a1.plot(tt[tt < 0], lnP[tt < 0], color=S[0], label="ln P, actual")
a1.plot(tt[tt >= 0], lnP[tt >= 0], color=S[0])
a1.plot(tt[tt >= 0], mu0 * tt[tt >= 0], color=S[0], ls="--", lw=1.2, label="ln P if μ had stayed 2%")
a1.plot(tt, lnM, color=S[1], lw=1.2, label="ln M (continuous at t = 0)")
a1.annotate(f"jump ½ln(i₁/i₀) = {jump:.3f}\n(P × √3 = {math.exp(jump):.3f})", (0, jump),
            xytext=(0.6, 1.05), textcoords="data", color=INK, fontsize=9,
            arrowprops=dict(arrowstyle="->", color=INK2))
a1.axvline(0, color=INK2, lw=0.8)
a1.set_xlabel("years from the announcement")
a1.set_ylabel("log level, relative to t = 0⁻")
a1.legend(loc="upper left", fontsize=8)
title(a1, "P jumps, then grows faster")
mb = np.where(tt < 0, md(i0), md(i1))
a2.plot(tt, mb, color=S[2], drawstyle="steps-post")
a2.annotate(f"i = {i0:.0%}: M/P = {md(i0):.1f}", (-5, md(i0)), xytext=(2, 6),
            textcoords="offset points", color=S[2], fontsize=9)
a2.annotate(f"i = {i1:.0%}: M/P = {md(i1):.1f}", (1, md(i1)), xytext=(2, 6),
            textcoords="offset points", color=S[2], fontsize=9)
a2.axvline(0, color=INK2, lw=0.8)
a2.set_ylim(0, 190)
a2.set_xlabel("years from the announcement")
a2.set_ylabel("real balances M/P (goods)")
title(a2, "Desired M/P drops at once")
out(fig, "fig_07_price_jump")

# ============================================================ 04 seigniorage
L = 1.0


def seig(p, a):
    return p * L * np.exp(-a * p)


pp = np.linspace(0, 1.2, 400)
fig, ax = plt.subplots(figsize=(6.4, 3.8))
for a, ls, col, lab in ((3.0, "--", S[0], "a = 3 (before)"), (5.0, "-", S[1], "a = 5 (after people learn to economise)")):
    ax.plot(pp * 100, seig(pp, a), color=col, ls=ls, label=lab)
    pk, sk = 1 / a, L / (a * math.e)
    assert close(float(seig(pk, a)), sk)
    ax.plot(pk * 100, sk, "o", color=col)
    ax.annotate(f"peak π = 1/a = {pk:.1%}\nS = L/(ae) = {sk:.4f}", (pk * 100, sk),
                xytext=(-8, 10) if a < 4 else (12, 4), textcoords="offset points",
                ha="right" if a < 4 else "left", color=col, fontsize=9)
assert close(L / (3 * math.e), 0.12263, 1e-5)
ax.set_xlabel("inflation π (% per year)")
ax.set_ylabel("seigniorage S (share of L)")
ax.set_ylim(0, 0.17)
ax.legend(loc="upper right", fontsize=8.5)
title(ax, "A higher a pulls the peak left and down")
out(fig, "fig_07_laffer_a_shift")

a = 3.0
pp2 = np.linspace(0.08, 1.0, 300)
fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.plot(pp2 * 100, 1 / pp2, color=S[0], label="rate effect 1/π")
ax.axhline(a, color=S[1], label=f"base effect a = {a:.0f}")
ax.plot(100 / a, a, "o", color=INK)
ax.annotate(f"cross at π = 1/a = {1 / a:.1%}:\nbase elasticity −aπ = −1", (100 / a, a),
            xytext=(45, 5.3), textcoords="data", color=INK, fontsize=9,
            arrowprops=dict(arrowstyle="->", color=INK2))
ax.text(14, 3.3, "revenue rises", color=INK2, fontsize=9)
ax.text(68, 2.3, "revenue falls", color=INK2, fontsize=9)
ax.set_xlabel("inflation π (% per year)")
ax.set_ylabel("d ln S/dπ terms (π as a decimal)")
ax.set_ylim(0, 8)
ax.legend(loc="upper right", fontsize=8.5)
title(ax, "d ln S/dπ = 1/π − a: the peak is where the two effects cancel")
out(fig, "fig_07_laffer_decomposition")

rr = 0.02
pf = np.linspace(-rr / (1 + rr), 0.20, 300)
inom = (1 + rr) * (1 + pf) - 1
cost = np.sqrt(F * np.clip(inom, 0, None) * Y / 2)
assert close(float(inom[0]), 0.0, 1e-12)
fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.plot(pf * 100, cost, color=S[0], label="resource cost F·n* = √(FiY/2)")
for p, lab in ((-rr / (1 + rr), "Friedman rule"), (0.02, "2% target"), (0.10, "10%")):
    iv = (1 + rr) * (1 + p) - 1
    cv = math.sqrt(F * max(iv, 0) * Y / 2)
    ax.plot(p * 100, cv, "o", color=S[0])
    ax.annotate(f"{lab}: π = {p:.2%}, i = {iv:.2%}\ncost {cv:.2f} ({cv / Y:.2%} of Y)",
                (p * 100, cv), xytext=(8, -26 if p > 0.05 else 4), textcoords="offset points",
                color=INK, fontsize=8.5)
assert close(math.sqrt(F * ((1.02 * 1.02) - 1) * Y / 2), math.sqrt(40.4))
ax.set_xlabel("inflation π (% per year), r = 2%, exact Fisher")
ax.set_ylabel("trip cost per period (goods, Y = 1000)")
ax.set_ylim(0, 16)
ax.legend(loc="upper left", fontsize=8.5)
title(ax, "Shoe-leather cost is zero only at i = 0 (π = −r/(1+r))")
out(fig, "fig_07_shoe_leather")
