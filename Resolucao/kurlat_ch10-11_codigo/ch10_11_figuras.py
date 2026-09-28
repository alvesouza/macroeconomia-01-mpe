"""Figures for Kurlat (2020) chapters 10-11. Writes PDFs to Resolucao/fig/.

  fig_k11_4_inflation.pdf     -- 11.4: money growth and inflation, countries A and B
  fig_k11_6_laffer.pdf        -- 11.6(g)-(h): seignorage S against gamma, peak at 1/mu
  fig_k11_6_stabilisation.pdf -- 11.6(p)-(t): base and price level around the reform

pgf backend (estilo_mpl): text typeset by pdflatex with lmodern + cmap, so the PDF stays
copyable. Run:  python ch10_11_figuras.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import estilo_mpl                                       # noqa: F401
from estilo_mpl import TEXTWIDTH_IN
import numpy as np
import matplotlib.pyplot as plt
from ch10_11_numerico import (price_path, YEARS, MU_A, MU_B, r4, S_formula, m_real,
                              Yss, mu, rss, w)

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "fig"))
os.makedirs(RAIZ, exist_ok=True)
BLUE, RED, GREY = "#1f4e9c", "#b03030", "#808080"


def save(fig, name):
    fig.savefig(os.path.join(RAIZ, name), bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)
    print("written:", name)


def fig_inflation():
    _, pA = price_path(MU_A, 0.03, r4)
    MB, pB = price_path(MU_B, 0.0, r4)
    piA, piB = 100 * (pA[1:] / pA[:-1] - 1), 100 * (pB[1:] / pB[:-1] - 1)
    fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH_IN, TEXTWIDTH_IN * 0.38))
    ax = axes[0]
    ax.plot(YEARS, 100 * np.array(MU_A), color=BLUE, lw=1.4, ls="--", marker="o", ms=3,
            label=r"A: money growth $=\pi$")
    ax.plot(YEARS, 100 * np.array(MU_B), color=RED, lw=1.4, ls="--", marker="s", ms=3,
            label=r"B: money growth")
    ax.plot(YEARS, piB, color=RED, lw=1.8, marker="s", ms=3, label=r"B: inflation")
    ax.axvline(2012, color=GREY, lw=0.7, ls=":")
    ax.set_ylabel(r"per cent"); ax.set_title(r"(i) Money growth and inflation")
    ax.legend(frameon=False, fontsize=7)
    ax = axes[1]
    ax.plot(YEARS, MB[1:] / pB[1:], color=RED, lw=1.8, marker="s", ms=3)
    ax.set_ylabel(r"real balances $M_t/p_t$ in B")
    ax.set_title(r"(ii) Real balances in B rise")
    for a in axes:
        a.spines[["top", "right"]].set_visible(False); a.set_xticks(YEARS)
    fig.suptitle(r"11.4 --- Baumol--Tobin demand, $r=2\%$, path fully anticipated", y=1.03)
    save(fig, "fig_k11_4_inflation.pdf")


def fig_laffer():
    g = np.linspace(0, 0.8, 400)
    fig, ax = plt.subplots(figsize=(TEXTWIDTH_IN * 0.62, TEXTWIDTH_IN * 0.36))
    ax.plot(g, S_formula(g), color=BLUE, lw=1.8)
    ax.axvline(0.25, color=GREY, lw=0.7, ls=":")
    ax.annotate(r"$\gamma^\ast=1/\mu=0.25$, $S^\ast=%.4f$" % S_formula(0.25),
                xy=(0.25, S_formula(0.25)), xytext=(0.36, 0.0170), fontsize=7.5,
                arrowprops=dict(arrowstyle="->", lw=0.6))
    ax.set_xlabel(r"monthly money growth $\gamma$"); ax.set_ylabel(r"seignorage $S$ (share of $Y_{ss}$)")
    ax.set_xlim(0, 0.8); ax.set_ylim(0, 0.019)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title(r"11.6(g) --- $Y_{ss}=1$, $\mu=4$, $r_{ss}=0.0025$, $\omega=5$")
    save(fig, "fig_k11_6_laffer.pdf")


def fig_stabilisation():
    g = 0.25
    t = np.arange(-4, 5)                        # reform announced at the end of month 0
    Mbar = (1 + g) ** mu
    MB = np.where(t <= 0, (1 + g) ** t.astype(float), Mbar)
    P0 = w / (Yss * ((1 + rss) * (1 + g)) ** (-mu))
    P = np.where(t <= 0, P0 * (1 + g) ** t.astype(float), P0)
    fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH_IN, TEXTWIDTH_IN * 0.36))
    for a, y, lab in ((axes[0], MB, r"monetary base $M^B_t/M^B_0$"),
                      (axes[1], P / P0, r"price level $P_t/P_0$")):
        a.step(t, y, where="post", color=BLUE, lw=1.6)
        a.plot(t, y, "o", color=BLUE, ms=3)
        a.axvline(0.5, color=GREY, lw=0.7, ls=":")
        a.set_xlabel(r"month ($t=0$: announcement)"); a.set_ylabel(lab)
        a.spines[["top", "right"]].set_visible(False)
    axes[0].plot([0, 1], [1, 1 + g], color=RED, ls="--", lw=1.0)
    axes[0].annotate(r"old rule: $\times1.25$", xy=(1, 1.25), xytext=(1.5, 1.35), color=RED, fontsize=7)
    axes[0].annotate(r"$\bar M=1.25^4=%.2f$" % Mbar, xy=(1, Mbar), xytext=(1.5, 2.05), fontsize=7)
    axes[0].set_title(r"(i) One last, larger injection, then flat")
    axes[1].set_title(r"(ii) Inflation stops at once")
    fig.suptitle(r"11.6(p)--(t) --- ending a hyperinflation at $\gamma^\ast=0.25$", y=1.03)
    save(fig, "fig_k11_6_stabilisation.pdf")


if __name__ == "__main__":
    fig_inflation()
    fig_laffer()
    fig_stabilisation()
