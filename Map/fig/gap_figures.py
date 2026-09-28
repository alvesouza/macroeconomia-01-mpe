#!/usr/bin/env python3
"""Figures for Map/avaliacao-listas-2-3-6.md and the notes it links to.

Each figure shows the correct answer to an item lost on a graded list. The numbers the
diagnosis quotes are asserted here first, so a figure never illustrates a wrong claim.

Run: python Map/fig/gap_figures.py   (writes Map/fig/fig_gap_*.svg)
"""
from __future__ import annotations

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent

# Reference palette (dataviz skill), light mode: slots 1-5 in fixed order.
S1, S2, S3, S4, S5 = "#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4"
INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"

plt.rcParams.update({
    "svg.fonttype": "none", "font.size": 10, "axes.edgecolor": INK2,
    "axes.labelcolor": INK, "xtick.color": INK2, "ytick.color": INK2,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8,
    "figure.facecolor": SURF, "axes.facecolor": SURF, "lines.linewidth": 2,
    "legend.frameon": False,
})


def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / name, format="svg")
    plt.close(fig)
    print("wrote", name)


# ---------- numbers the diagnosis quotes ----------

def solow_ss(s, A, alpha, n, delta=0.05):
    k = (s * A / (n + delta)) ** (1 / (1 - alpha))
    return k, A * k ** alpha


kN0, kS0 = 100 / 10, 8000 / 20
yN0, yS0 = 4 * kN0 ** 0.25, 5 * kS0 ** 0.5
kNs, yNs = solow_ss(0.16, 4, 0.25, 0.03)
kSs, ySs = solow_ss(0.30, 5, 0.5, 0.01)
kU = 8100 / 30
yU = 5 * kU ** 0.5
nU = (10 * 0.03 + 20 * 0.01) / 30
kUs, yUs = solow_ss(0.30, 5, 0.5, nU)
assert math.isclose(yN0, 7.1131, abs_tol=1e-4) and yS0 == 100
assert math.isclose(kNs, 16) and math.isclose(yNs, 8)
assert math.isclose(kSs, 625) and math.isclose(ySs, 125)
assert math.isclose(yU, 82.158, abs_tol=1e-3) and math.isclose(yU * 30, 2464.75, abs_tol=0.01)
assert math.isclose(kUs, 506.25) and math.isclose(yUs, 112.5)

alpha_g = 1 / 3
A_hat = 1.5 ** -alpha_g
resid = alpha_g * math.log(1.5 / 1.125) / 10  # theta' = theta/4
assert math.isclose(A_hat, 0.8736, abs_tol=1e-4)
assert math.isclose(resid, 0.0095894, abs_tol=1e-6)


def c1_of_r(r, sigma, beta=0.96, wealth=1.0):
    """Lista 3 1(c): y2 = tau1 = tau2 = 0, so c1 = (a0 + y1) / D."""
    D = 1 + beta ** (1 / sigma) * (1 + r) ** (1 / sigma - 1)
    return wealth / D


for sig, sign in [(0.5, -1), (1.0, 0), (2.0, 1)]:
    d = c1_of_r(0.051, sig) - c1_of_r(0.05, sig)
    assert (d > 1e-9) - (d < -1e-9) == sign, sig  # sigma>1 -> c1 RISES with r

# ---------- figure 1: where the marks went ----------

lists = ["Lista 1", "Lista 2", "Lista 3", "Lista 4", "Lista 6"]
kinds = [
    ("Object asked for, not answered", S1, [1, 2, 4, 0, 2]),
    ("Explanation missing or wrong", S2, [3, 1, 1, 3, 3]),
    ("Words contradict own math", S3, [0, 0, 2, 1, 0]),
    ("Arithmetic slip", S4, [2, 0, 0, 0, 0]),
    ("Left blank", S5, [1, 1, 0, 0, 0]),
]
fig, ax = plt.subplots(figsize=(7.2, 3.4))
left = np.zeros(len(lists))
for label, col, vals in kinds:
    ax.barh(lists, vals, left=left, color=col, label=label,
            edgecolor=SURF, linewidth=2, height=0.62)
    left += vals
for i, tot in enumerate(left):
    ax.text(tot + 0.15, i, f"{int(tot)}", va="center", color=INK2)
ax.invert_yaxis()
ax.set_xlabel("items marked wrong or half-credit")
ax.grid(axis="y", visible=False)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.22), ncol=3, fontsize=8.5)
ax.set_title("None of the lost items was a model set up wrongly", loc="left",
             color=INK, fontsize=11)
save(fig, "fig_gap_scorecard.svg")

# ---------- figure 2: Lista 3 1(c), sign of dc1/dr ----------

r = np.linspace(0.0, 0.15, 200)
fig, ax = plt.subplots(figsize=(6.4, 3.6))
for sig, col, txt in [(0.5, S1, "σ = 0.5: substitution dominates, c₁ falls"),
                      (1.0, INK2, "σ = 1 (log): the effects cancel"),
                      (2.0, S2, "σ = 2: income effect dominates, c₁ rises")]:
    y = c1_of_r(r, sig)
    ax.plot(r * 100, y, color=col, label=txt)
ax.set_xlabel("real interest rate r (%)")
ax.set_ylabel("c₁ as a share of a₀ + y₁")
ax.set_title("Lista 3 1(c): a pure saver, y₂ = τ₁ = τ₂ = 0, β = 0.96", loc="left", fontsize=11)
ax.legend(fontsize=8.5, loc="lower left")
save(fig, "fig_gap_l3_sigma.svg")

# ---------- figure 3: Lista 3 1(e), the Ricardian swap ----------

rr = 0.05
cats = ["Δc₁", "Δc₂", "Δa"]
free = [0, 0, 1]                       # tax cut fully saved
bound = [1, -(1 + rr), 0]              # a = -b fixed: the cut is spent
x = np.arange(3)
fig, ax = plt.subplots(figsize=(6.0, 3.3))
ax.bar(x - 0.19, free, 0.36, color=S1, label="can borrow freely: equivalence holds",
       edgecolor=SURF, linewidth=2)
ax.bar(x + 0.19, bound, 0.36, color=S2, label="borrowing limit binds: equivalence fails",
       edgecolor=SURF, linewidth=2)
ax.axhline(0, color=INK2, linewidth=1)
ax.set_xticks(x, cats)
ax.set_ylabel("change, units of goods")
ax.set_title("Lista 3 1(e): cut τ₁ by 1, raise τ₂ by 1 + r (r = 5%)", loc="left", fontsize=11)
ax.legend(fontsize=8.5, loc="lower left")
ax.grid(axis="x", visible=False)
save(fig, "fig_gap_l3_ricardo.svg")

# ---------- figure 4: Lista 2 1(b)-(d), Korea paths ----------


def path(k0, s, A, alpha, n, T=150, delta=0.05):
    k = [k0]
    for _ in range(T):
        k.append(((1 - delta) * k[-1] + s * A * k[-1] ** alpha) / (1 + n))
    return A * np.array(k) ** alpha


t = np.arange(151)
fig, axes = plt.subplots(1, 2, figsize=(8.0, 3.4))
for ax, (y, ss, col, name) in zip(axes, [
        (path(kS0, 0.30, 5, 0.5, 0.01), ySs, S1, "South"),
        (path(kN0, 0.16, 4, 0.25, 0.03), yNs, S2, "North")]):
    ax.plot(t, y, color=col, label=f"{name}, no unification")
    ax.axhline(ss, color=col, linestyle="--", linewidth=1)
    ax.set_xlabel("period")
axes[0].plot(t, path(kU, 0.30, 5, 0.5, nU), color=S3, label="unified Korea")
axes[0].axhline(yUs, color=S3, linestyle="--", linewidth=1)
axes[0].set_ylabel("GDP per worker y")
axes[0].set_title("South 100 → 125; unified 82.2 → 112.5", loc="left", fontsize=10)
axes[1].set_title("North 7.11 → 8: converges, not diverges", loc="left", fontsize=10)
for ax in axes:
    ax.legend(fontsize=8, loc="lower right")
fig.suptitle("Lista 2 Q1: each economy converges to its own steady state (dashed)",
             x=0.02, ha="left", fontsize=11)
save(fig, "fig_gap_l2_korea.svg")

# ---------- figure 5: Lista 2 Q2, security capital read as TFP ----------

th = np.linspace(0, 1, 200)
fig, ax = plt.subplots(figsize=(6.2, 3.4))
ax.plot(th, (1 + th) ** -alpha_g, color=S1, label="measured Â / A = (1 + θ)^(−α)")
for v, lab in [(0.5, "θ = 0.5"), (0.125, "θ′ = θ/4 = 0.125")]:
    ax.plot(v, (1 + v) ** -alpha_g, "o", ms=8, color=S2, mec=SURF, mew=2)
    ax.annotate(f"{lab}: {(1 + v) ** -alpha_g:.4f}", (v, (1 + v) ** -alpha_g),
                xytext=(8, 6), textcoords="offset points", color=INK2, fontsize=9)
ax.set_xlabel("security capital per unit of productive capital θ")
ax.set_ylabel("Â / A")
ax.set_title(f"Lista 2 2(d): θ 0.5 → 0.125 in 10 years = {resid * 100:.2f}% TFP growth a year",
             loc="left", fontsize=10.5)
ax.legend(fontsize=9)
save(fig, "fig_gap_l2_gotham.svg")

# ---------- figure 6: Lista 6 1(c)-(d), who moves in the money market ----------

F, Y, p = 1.0, 100.0, 1.0
mm = np.linspace(2, 30, 300)
i_of_m = F * Y / (2 * mm ** 2)          # inverse Baumol-Tobin demand
fig, axes = plt.subplots(1, 2, figsize=(8.0, 3.4), sharey=True)
ax = axes[0]
ax.plot(mm, i_of_m, color=INK2, label="money demand m(Y, i)")
m0, m1 = 10, 14
for m, col, lab in [(m0, S1, "M₀/p̄"), (m1, S2, "M₁/p̄")]:
    ax.axvline(m, color=col, label=f"supply {lab}")
    ax.plot(m, F * Y / (2 * m * m), "o", ms=8, color=col, mec=SURF, mew=2)
ax.set_title("M target, p fixed: i falls (if Y is held)", loc="left", fontsize=10)
ax.set_xlabel("real balances M/p")
ax.set_ylabel("nominal rate i")
ax.set_ylim(0, 0.8)
ax.legend(fontsize=8)
ax = axes[1]
ax.plot(mm, i_of_m, color=INK2, label="money demand m(Y, i)")
for ib, col, lab in [(0.5, S1, "ī₀"), (0.25, S2, "ī₁")]:
    ax.axhline(ib, color=col, label=f"target {lab}")
    ax.plot(math.sqrt(F * Y / (2 * ib)), ib, "o", ms=8, color=col, mec=SURF, mew=2)
ax.set_title("i target: M adjusts to whatever is demanded", loc="left", fontsize=10)
ax.set_xlabel("real balances M/p")
ax.legend(fontsize=8)
fig.suptitle("Lista 6 1(c)-(d): the instrument decides which variable is endogenous",
             x=0.02, ha="left", fontsize=11)
save(fig, "fig_gap_l6_regimes.svg")
