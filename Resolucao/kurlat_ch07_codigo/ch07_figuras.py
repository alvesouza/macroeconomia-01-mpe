"""Figures for the Kurlat ch. 7 exercises. Writes PDFs into Resolucao/fig/.

  fig_k7_1_oferta.pdf     -- 7.1(b): hours against the wage, three utility functions
  fig_k7_5_prescott.pdf   -- 7.5: leisure against the tax rate, and the hours gap
  fig_k7_6_equilibrio.pdf -- 7.6: vertical labour supply and the fall in the wage
  fig_k7_7_beveridge.pdf  -- 7.7: the two experiments in (hat-U, V) space

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

from ch07_numerico import (lazer, lazer_orcamento_equilibrado, problema_7_5,
                           problema_7_7, ALPHA_P)

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "fig"))
os.makedirs(RAIZ, exist_ok=True)
AZUL, VERM, CINZA, VERDE = "#1f4e9c", "#b03030", "#808080", "#1f7a4d"


def salvar(fig, nome):
    fig.savefig(os.path.join(RAIZ, nome), bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)
    print("written:", nome)


# ================================================= 7.1  hours against the wage
def fig_oferta():
    phi, alpha = 0.4, 1.54
    w = np.linspace(0.42, 6.0, 500)

    fig, ax = plt.subplots(figsize=(TEXTWIDTH_IN * 0.64, TEXTWIDTH_IN * 0.38))
    ax.plot(w, 1 - phi / w, color=AZUL, lw=1.6,
            label=r"$u=c+\phi\log l$ (this exercise): $1-l=1-\phi/w$")
    ax.plot(w, np.full_like(w, 1 / (1 + alpha)), color=VERDE, lw=1.6,
            label=r"$u=\log c+\alpha\log l$: $1-l=1/(1+\alpha)$, flat")
    # a case where the income effect dominates: sigma > 1 in Kurlat's (7.2.4),
    # 1-l = theta^{-1/(eta+sigma)} w^{(1-sigma)/(eta+sigma)}, theta set so that
    # hours are 0.4 at w = 1.
    sigma, eta = 2.0, 1.0
    theta = 0.4 ** (-(eta + sigma))
    ax.plot(w, theta ** (-1 / (eta + sigma)) * w ** ((1 - sigma) / (eta + sigma)),
            color=VERM, lw=1.6,
            label=r"(7.2.4) with $\sigma=2>1$: hours \emph{fall} --- the data's sign")
    ax.set_xlabel(r"wage $w$")
    ax.set_ylabel(r"hours worked, $1-l$")
    ax.set_ylim(0, 1.0)
    ax.set_xlim(0.42, 6.0)
    handles, labels = ax.get_legend_handles_labels()
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title(r"7.1(b) --- what each utility function predicts as wages rise",
                 fontsize=8.5)
    fig.tight_layout()
    fig.legend(handles, labels, frameon=False, fontsize=7, loc="lower center",
               bbox_to_anchor=(0.5, -0.20))
    salvar(fig, "fig_k7_1_oferta.pdf")


# ================================================= 7.5  Prescott
def fig_prescott():
    us, eu, razao_Y, lam, _, _ = problema_7_5(verbose=False)
    tau = np.linspace(0.0, 0.75, 400)

    fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH_IN, TEXTWIDTH_IN * 0.38))

    ax = axes[0]
    ax.plot(tau, np.full_like(tau, ALPHA_P / (1 + ALPHA_P)), color=CINZA, lw=1.5,
            ls="--", label=r"$T=0$: $l=\alpha/(1+\alpha)$, flat")
    ax.plot(tau, lazer_orcamento_equilibrado(tau), color=AZUL, lw=1.6,
            label=r"balanced budget: $l=\alpha/(1+\alpha-\tau)$")
    for pais, cor, desloc in ((us, VERM, (-4, 8)), (eu, VERDE, (6, -10))):
        ax.plot([pais["tau"]], [pais["l"]], "o", color=cor, ms=4.5)
        ax.annotate(pais["nome"], xy=(pais["tau"], pais["l"]), fontsize=7.5,
                    xytext=desloc, textcoords="offset points", color=cor)
    ax.set_xlabel(r"income tax rate $\tau$")
    ax.set_ylabel(r"leisure $l$")
    ax.set_ylim(0.50, 0.86)
    ax.legend(frameon=False, loc="lower right", fontsize=7)
    ax.set_title(r"(c) taxes bite only once the revenue comes back as $T$",
                 fontsize=8.5)

    ax = axes[1]
    rotulos = [r"US", r"Europe's $\tau$," "\n" r"US $T$",
               r"US $\tau$," "\n" r"Europe's $T$", r"Europe"]
    valores = [us["L"],
               1 - lazer(eu["tau"], us["T"]),
               1 - lazer(us["tau"], eu["T"]),
               eu["L"]]
    cores = [VERM, CINZA, CINZA, VERDE]
    ax.bar(range(4), valores, color=cores, width=0.62)
    for i, v in enumerate(valores):
        ax.text(i, v + 0.004, r"$%.3f$" % v, ha="center", fontsize=7)
    ax.set_xticks(range(4))
    ax.set_xticklabels(rotulos, fontsize=6.8)
    ax.set_ylabel(r"hours worked, $1-l$")
    ax.set_ylim(0, 0.35)
    ax.set_title(r"(d) decomposing the hours gap", fontsize=8.5)

    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)

    fig.suptitle(r"7.5 --- Prescott's calculation, $\alpha=1.54$, $w=1$ "
                 r"($\lambda=%.3f$, output gap $%.1f\%%$)"
                 % (lam, (1 - razao_Y) * 100), fontsize=9, y=1.04)
    fig.tight_layout()
    salvar(fig, "fig_k7_5_prescott.pdf")


# ================================================= 7.6  labour market equilibrium
def fig_equilibrio():
    theta = 0.35
    L = np.linspace(0.05, 0.95, 400)
    demanda = (1 - theta) * L ** (-theta)

    fig, ax = plt.subplots(figsize=(TEXTWIDTH_IN * 0.64, TEXTWIDTH_IN * 0.44))
    ax.plot(L, demanda, color=CINZA, lw=1.6,
            label=r"labour demand $w=F_L=(1-\theta)L^{-\theta}$")

    for alpha, cor, rot in ((2.5, AZUL, r"$\alpha=2.5$ (leisure-loving)"),
                            (0.5, VERM, r"$\alpha=0.5$ (work ethic)")):
        Ls = 1 / (1 + alpha)
        w = (1 - theta) * Ls ** (-theta)
        ax.axvline(Ls, color=cor, lw=1.5)
        ax.plot([Ls], [w], "o", color=cor, ms=5)
        ax.annotate(r"$w=%.3f$" % w, xy=(Ls, w), fontsize=7.5,
                    xytext=(6, 6), textcoords="offset points", color=cor)
        ax.annotate(rot, xy=(Ls, 1.62), fontsize=7,
                    xytext=(3, 0), textcoords="offset points", color=cor,
                    rotation=90, va="top")

    ax.annotate("", xy=(1 / 1.5, 1.5), xytext=(1 / 3.5, 1.5),
                arrowprops=dict(arrowstyle="->", color=VERDE, lw=1.1))
    ax.text(0.47, 1.53, r"supply shifts right", fontsize=7, color=VERDE,
            ha="center")

    ax.set_xlabel(r"labour $L=1-l$")
    ax.set_ylabel(r"wage $w$")
    ax.set_xlim(0.1, 0.95)
    ax.set_ylim(0.6, 1.7)
    ax.legend(frameon=False, loc="lower left", fontsize=7.5)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title(r"7.6 --- log-log preferences give \emph{vertical} labour supply "
                 r"at $1/(1+\alpha)$", fontsize=8.5)
    fig.tight_layout()
    salvar(fig, "fig_k7_6_equilibrio.pdf")


# ================================================= 7.7  Beveridge curve
def fig_beveridge():
    linhas_a, linhas_b = problema_7_7(verbose=False)

    fig, ax = plt.subplots(figsize=(TEXTWIDTH_IN * 0.68, TEXTWIDTH_IN * 0.44))

    Ua = [x[2] for x in linhas_a]
    Va = [x[1] for x in linhas_a]
    ax.plot(Ua, Va, "-o", color=AZUL, lw=1.5, ms=4.5,
            label=r"(a) better matching, $A\uparrow$ (U fixed)")
    for (mult, V, Uh, f) in linhas_a[1:]:
        ax.annotate(r"$A/A_0=%.1f$" % mult, xy=(Uh, V), fontsize=6.5,
                    xytext=(4, -8), textcoords="offset points", color=AZUL)

    Ub = [x[2] for x in linhas_b]
    Vb = [x[1] for x in linhas_b]
    ax.plot(Ub, Vb, "-s", color=VERM, lw=1.5, ms=4.5,
            label=r"(b) higher initial $U$ ($A$ fixed)")
    for (U, V, Uh, t, f) in linhas_b[::2]:
        ax.annotate(r"$U=%.2f$" % U, xy=(Uh, V), fontsize=6.5,
                    xytext=(-30, 3), textcoords="offset points", color=VERM)

    ax.set_xlabel(r"after-hiring unemployment $\hat U$")
    ax.set_ylabel(r"vacancies $V$")
    ax.legend(frameon=False, loc="lower right", fontsize=7.5)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title(r"7.7 --- (a) traces a Beveridge curve; (b) does not, it shifts it",
                 fontsize=8.5)
    fig.tight_layout()
    salvar(fig, "fig_k7_7_beveridge.pdf")


if __name__ == "__main__":
    fig_oferta()
    fig_prescott()
    fig_equilibrio()
    fig_beveridge()
    print("all figures written to", RAIZ)
