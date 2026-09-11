"""Figures for the Kurlat ch. 5 exercises. Writes PDFs into Resolucao/fig/.

  fig_k5_1_convergencia.pdf -- 5.1(a) and 5.1(b): the two simulated transitions
  fig_k5_2_velocidade.pdf   -- 5.2(d): g_y and g_y/(1-phi) as phi -> 1
  fig_k5_4_capital.pdf      -- 5.4(b) and 5.4(c): the two measurement errors

pgf backend: the figure text is typeset by pdflatex with lmodern + cmap, so the
final PDF stays fully copyable (no Type 3 fonts).
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import estilo_mpl                                        # noqa: F401
from estilo_mpl import TEXTWIDTH_IN
import numpy as np
import matplotlib.pyplot as plt

from ch05_numerico import (problema_5_1, problema_5_2, problema_5_4,
                           gy_analitico, ALPHA, DELTA)

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "fig"))
os.makedirs(RAIZ, exist_ok=True)
AZUL, VERM, CINZA, VERDE = "#1f4e9c", "#b03030", "#808080", "#1f7a4d"


def salvar(fig, nome):
    fig.savefig(os.path.join(RAIZ, nome), bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)
    print("written:", nome)


# ================================================= 5.1  the two transitions
def fig_convergencia():
    r = problema_5_1(verbose=False)
    t = np.arange(len(r["ya"]))
    fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH_IN, TEXTWIDTH_IN * 0.40))

    ax = axes[0]
    ax.plot(t, r["ya"], color=AZUL, lw=1.5)
    ax.axhline(0.95, color=VERM, lw=0.9, ls="--")
    ax.axvline(r["ta"], color=VERM, lw=0.9, ls=":")
    ax.annotate(r"$t=%d$" % r["ta"], xy=(r["ta"], 0.45), fontsize=7.5,
                xytext=(4, 0), textcoords="offset points", color=VERM)
    ax.annotate(r"$0.95$", xy=(2, 0.95), fontsize=7.5,
                xytext=(0, 4), textcoords="offset points", color=VERM)
    ax.set_title(r"(a) starting from $\tilde y_0=0.1\,\tilde y^{*}$", fontsize=8.5)

    ax = axes[1]
    ax.plot(t, r["yb"], color=VERDE, lw=1.5)
    ax.axhline(0.95, color=VERM, lw=0.9, ls="--")
    ax.axvline(r["tb"], color=VERM, lw=0.9, ls=":")
    ax.annotate(r"$t=%d$" % r["tb"], xy=(r["tb"], 0.925), fontsize=7.5,
                xytext=(4, 0), textcoords="offset points", color=VERM)
    ax.set_ylim(0.90, 1.005)
    ax.set_title(r"(b) after $n$ falls from $0.01$ to $0$", fontsize=8.5)

    for ax in axes:
        ax.set_xlabel(r"years")
        ax.set_ylabel(r"$\tilde y_t/\tilde y^{*}$")
        ax.set_xlim(0, 100)
        ax.spines[["top", "right"]].set_visible(False)

    fig.suptitle(r"5.1 --- convergence under the calibration of \S5.2 "
                 r"($\alpha=0.35$, $s=0.2$, $\delta=0.04$, $g=0.015$)",
                 fontsize=9, y=1.04)
    fig.tight_layout()
    salvar(fig, "fig_k5_1_convergencia.pdf")


# ================================================= 5.2  the speed of convergence
def fig_velocidade():
    linhas, lam = problema_5_2(verbose=False)
    phi = np.linspace(0.55, 0.9995, 800)
    gy = gy_analitico(phi)
    frac = gy / (1 - phi)

    fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH_IN, TEXTWIDTH_IN * 0.40))

    ax = axes[0]
    ax.plot(phi, gy * 100, color=AZUL, lw=1.5)
    for p, g, _, _, _ in linhas:
        ax.plot([p], [g * 100], "o", color=VERM, ms=3.5)
        ax.annotate(r"$\phi=%.2f$" % p, xy=(p, g * 100), fontsize=7,
                    xytext=(4, 4), textcoords="offset points", color=VERM)
    ax.set_ylabel(r"$g_y$ (\% per year)")
    ax.set_title(r"growth falls to zero as $\phi\to1$", fontsize=8.5)

    ax = axes[1]
    ax.plot(phi, frac * 100, color=AZUL, lw=1.5)
    ax.axhline(lam * 100, color=VERM, lw=0.9, ls="--")
    ax.annotate(r"$\delta(1-\alpha)=%.1f\%%$" % (lam * 100), xy=(0.62, lam * 100),
                fontsize=7.5, xytext=(0, 5), textcoords="offset points", color=VERM)
    for p, _, _, fl, _ in linhas:
        ax.plot([p], [fl * 100], "o", color=VERM, ms=3.5)
    ax.set_ylabel(r"$g_y/(1-\phi)$ (\% per year)")
    ax.set_title(r"the gap closes at a nearly constant rate", fontsize=8.5)

    for ax in axes:
        ax.set_xlabel(r"$\phi=y_t/y^{*}$")
        ax.set_xlim(0.55, 1.0)
        ax.spines[["top", "right"]].set_visible(False)

    fig.suptitle(r"5.2(d) --- speed of convergence, $\alpha=0.35$, $\delta=0.04$",
                 fontsize=9, y=1.04)
    fig.tight_layout()
    salvar(fig, "fig_k5_2_velocidade.pdf")


# ================================================= 5.4  measuring the capital stock
def fig_capital():
    razao, K, K_est_c, _ = problema_5_4(verbose=False)
    t = np.arange(len(K))
    K_true = 2.0

    fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH_IN, TEXTWIDTH_IN * 0.40))

    ax = axes[0]
    ax.plot(t, K, color=AZUL, lw=1.5, label=r"estimate, $K^{EST}_t$")
    ax.axhline(K_true, color=CINZA, lw=1.2, ls="--", label=r"truth, $K=2$")
    for y in (5, 10, 50):
        ax.plot([y], [K[y]], "o", color=VERM, ms=3.5)
        ax.annotate(r"$%.3f$" % razao[y], xy=(y, K[y]), fontsize=7,
                    xytext=(3, -9), textcoords="offset points", color=VERM)
    ax.set_ylim(0.9, 2.2)
    ax.legend(loc="lower right", frameon=False)
    ax.set_title(r"(b) a wrong guess for $K_0$ dies out at rate $1-\delta$",
                 fontsize=8.5)

    ax = axes[1]
    ax.plot(t, np.full_like(t, K_est_c, dtype=float), color=VERM, lw=1.5,
            label=r"$\hat\delta=0.05$: $K^{EST}=4$")
    ax.axhline(K_true, color=CINZA, lw=1.2, ls="--", label=r"truth, $K=2$")
    ax.fill_between(t, K_true, K_est_c, color=VERM, alpha=0.08)
    ax.set_ylim(0.9, 4.4)
    ax.legend(loc="center right", frameon=False)
    ax.set_title(r"(c) a wrong $\delta$ never dies out", fontsize=8.5)

    for ax in axes:
        ax.set_xlabel(r"years since the office started measuring")
        ax.set_ylabel(r"capital stock")
        ax.set_xlim(0, 50)
        ax.spines[["top", "right"]].set_visible(False)

    fig.suptitle(r"5.4 --- two ways of getting the capital stock wrong "
                 r"($I=0.2$, $\delta=0.1$)", fontsize=9, y=1.04)
    fig.tight_layout()
    salvar(fig, "fig_k5_4_capital.pdf")


if __name__ == "__main__":
    fig_convergencia()
    fig_velocidade()
    fig_capital()
    print("all figures written to", RAIZ)
