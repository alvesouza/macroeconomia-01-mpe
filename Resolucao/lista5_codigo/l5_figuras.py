"""Figures for the Problem Set 5 resolution.  Writes PDFs into Resolucao/fig/.

  fig_l5q1_trabalho.pdf      -- Q1(d): the labour equation and its unique root
  fig_l5q1_elasticidades.pdf -- Q1(e): the three elasticities against sigma
  fig_l5q2_fase.pdf          -- Q2(d): phase diagram and the saddle path
  fig_l5q2_regradeouro.pdf   -- Q2(e): steady state against the Golden Rule

pgf backend: figure text is typeset by pdflatex with lmodern + cmap, so the
final PDF stays fully copyable (no Type 3 fonts).
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import estilo_mpl                                        # noqa: F401
from estilo_mpl import TEXTWIDTH_IN
import numpy as np
import matplotlib.pyplot as plt

from modelo import (ALPHA, PSI, KBAR, A2, ALPHA2, DELTA, BETA,
                    L_equilibrio, elasticidades, c_de_L,
                    K_ss, c_ss, K_gr, caminho, c_saddle, FK)

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "fig"))
os.makedirs(RAIZ, exist_ok=True)
AZUL, VERM, CINZA, VERDE, ROXO = "#1f4e9c", "#b03030", "#808080", "#1f7a4d", "#5b2d8e"


def salvar(fig, nome):
    fig.savefig(os.path.join(RAIZ, nome), bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)
    print("written:", nome)


# ============================================= Q1(d) the labour equation
def fig_trabalho():
    fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH_IN, TEXTWIDTH_IN * 0.40))

    # --- panel (i): LHS rises from 0 to infinity, RHS is a constant
    ax = axes[0]
    L = np.linspace(1e-4, 0.92, 2000)
    for sigma, cor in ((0.5, AZUL), (1.0, VERDE), (2.0, ROXO)):
        lhs = L ** (ALPHA + (1 - ALPHA) * sigma) / (1 - L)
        rhs = (1 - ALPHA) / PSI * (1.0 * KBAR ** ALPHA) ** (1 - sigma)
        ax.plot(L, lhs, color=cor, lw=1.4,
                label=r"LHS, $\sigma=%.1f$" % sigma)
        ax.axhline(rhs, color=cor, lw=0.9, ls="--")
        Ls = L_equilibrio(1.0, sigma)
        ax.plot([Ls], [rhs], "o", color=cor, ms=4)
    ax.set_xlim(0, 0.92)
    ax.set_ylim(0, 1.6)
    ax.set_xlabel(r"$L_t$")
    ax.set_ylabel(r"$L_t^{\alpha+(1-\alpha)\sigma}/(1-L_t)$")
    ax.legend(loc="upper left", frameon=False, fontsize=7)
    ax.set_title(r"(i) strictly increasing LHS $\Rightarrow$ a unique root",
                 fontsize=8.5)

    # --- panel (ii): equilibrium hours against sigma, for three A
    ax = axes[1]
    sig = np.linspace(0.15, 5.0, 300)
    for A, cor, ls in ((0.8, CINZA, ":"), (1.0, AZUL, "-"), (1.4, VERM, "--")):
        Ls = [L_equilibrio(A, s) for s in sig]
        ax.plot(sig, Ls, color=cor, lw=1.4, ls=ls, label=r"$A=%.1f$" % A)
    ax.axvline(1.0, color=VERDE, lw=0.9, ls="--")
    ax.annotate(r"$\sigma=1$", xy=(1.0, 0.06), fontsize=7.5,
                xytext=(4, 0), textcoords="offset points", color=VERDE)
    ax.set_xlabel(r"$\sigma$")
    ax.set_ylabel(r"$L_t^{*}$")
    ax.set_xlim(0.15, 5.0)
    ax.legend(loc="lower right", frameon=False, fontsize=7)
    ax.set_title(r"(ii) at $\sigma=1$ the curves cross: $A$ stops mattering",
                 fontsize=8.5)

    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)

    fig.suptitle(r"Q1(d) --- the equation that pins down $L_t$ "
                 r"($\alpha=0.35$, $\psi=1.8$, $\bar K=2$)", fontsize=9, y=1.04)
    fig.tight_layout()
    salvar(fig, "fig_l5q1_trabalho.pdf")


# ============================================= Q1(e) the elasticities
def fig_elasticidades():
    fig, ax = plt.subplots(figsize=(TEXTWIDTH_IN, TEXTWIDTH_IN * 0.36))
    sig = np.linspace(0.15, 5.0, 400)
    eL, ew, ec = [], [], []
    for s in sig:
        _, a, b, _, d = elasticidades(1.0, s)
        eL.append(a); ew.append(b); ec.append(d)

    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(1.0, color=VERDE, lw=1.0, ls="--")
    ax.plot(sig, eL, color=AZUL, lw=1.6, label=r"$d\ln L_t/d\ln A_t$")
    ax.plot(sig, ew, color=VERM, lw=1.6, label=r"$d\ln w_t/d\ln A_t$")
    ax.plot(sig, ec, color=ROXO, lw=1.6,
            label=r"$d\ln c_t/d\ln A_t = d\ln r^K_t/d\ln A_t$")
    ax.axhline(1.0, color=CINZA, lw=0.7, ls=":")

    ax.annotate(r"$\sigma=1$: hours frozen, everything else scales one-for-one",
                xy=(1.0, 1.0), fontsize=7.5, xytext=(8, 14),
                textcoords="offset points", color=VERDE,
                arrowprops=dict(arrowstyle="->", color=VERDE, lw=0.7))
    ax.annotate("substitution wins\n(hours rise)", xy=(0.35, 0.75), fontsize=7,
                color=AZUL, ha="center")
    ax.annotate("income wins\n(hours fall)", xy=(3.6, -0.55), fontsize=7,
                color=AZUL, ha="center")

    ax.set_xlim(0.15, 5.0)
    ax.set_xlabel(r"$\sigma$")
    ax.set_ylabel(r"elasticity with respect to $A_t$")
    ax.legend(loc="upper right", frameon=False, fontsize=7.5)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title(r"Q1(e) --- the sign of the hours response is the sign of "
                 r"$1-\sigma$; $w$, $r^K$ and $c$ rise for every $\sigma$",
                 fontsize=8.5)
    fig.tight_layout()
    salvar(fig, "fig_l5q1_elasticidades.pdf")


# ============================================= Q2(d) the phase diagram
def fig_fase(beta=BETA, sigma=2.0):
    fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH_IN, TEXTWIDTH_IN * 0.42))
    Ks, cs = K_ss(beta), c_ss(K_ss(beta))
    Kg = K_gr()

    # --- panel (i): the two loci, four regions, the saddle path
    ax = axes[0]
    K = np.linspace(0.05, 12.0, 600)
    ax.plot(K, c_ss(K), color=VERM, lw=1.5,
            label=r"$\Delta K=0$:  $c=AK^{\alpha}-\delta K$")
    ax.axvline(Ks, color=AZUL, lw=1.5,
               label=r"$\Delta c=0$:  $F_K-\delta=\frac{1}{\beta}-1$")
    ax.plot([Ks], [cs], "o", color="black", ms=5, zorder=5)
    ax.annotate(r"steady state", xy=(Ks, cs), fontsize=7.5,
                xytext=(6, -12), textcoords="offset points")

    for K0, cor in ((2.0, VERDE), (9.0, ROXO)):
        c0 = c_saddle(K0, T=200, beta=beta, sigma=sigma)
        Kp, cp = caminho(K0, c0, 90, beta=beta, sigma=sigma)
        ok = np.isfinite(Kp) & np.isfinite(cp)
        ax.plot(Kp[ok], cp[ok], color=cor, lw=1.5, ls="-")
        ax.plot([K0], [c0], "o", color=cor, ms=4)
    ax.annotate("saddle path", xy=(3.2, 1.02), fontsize=7.5, color=VERDE)

    # direction arrows, one per region
    for Kq, cq, dx, dy in ((3.0, 1.55, 0.0, -0.06), (3.0, 0.75, 0.55, 0.0),
                           (7.5, 1.55, -0.55, 0.0), (7.5, 0.85, 0.0, 0.06)):
        ax.arrow(Kq, cq, dx, dy, head_width=0.045, head_length=0.16,
                 fc=CINZA, ec=CINZA, lw=0.6, length_includes_head=True)

    ax.set_xlim(0, 12)
    ax.set_ylim(0, 1.8)
    ax.set_xlabel(r"$K_t$")
    ax.set_ylabel(r"$c_t$")
    ax.legend(loc="lower right", frameon=False, fontsize=7)
    ax.set_title(r"(i) the two loci and the unique convergent path", fontsize=8.5)

    # --- panel (ii): time paths from below
    ax = axes[1]
    K0 = 2.0
    c0 = c_saddle(K0, T=200, beta=beta, sigma=sigma)
    Kp, cp = caminho(K0, c0, 80, beta=beta, sigma=sigma)
    t = np.arange(len(Kp))
    ax.plot(t, Kp, color=AZUL, lw=1.5, label=r"$K_t$")
    ax.plot(t, cp, color=VERM, lw=1.5, label=r"$c_t$")
    ax.axhline(Ks, color=AZUL, lw=0.8, ls="--")
    ax.axhline(cs, color=VERM, lw=0.8, ls="--")
    ax.set_xlim(0, 80)
    ax.set_xlabel(r"periods")
    ax.set_ylabel(r"level")
    ax.legend(loc="center right", frameon=False, fontsize=7.5)
    ax.set_title(r"(ii) both rise monotonically to the steady state", fontsize=8.5)

    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)

    fig.suptitle(r"Q2(d) --- $\beta=%.2f$, $\sigma=%.0f$, $\alpha=%.2f$, "
                 r"$\delta=%.2f$, $A=%.0f$" % (beta, sigma, ALPHA2, DELTA, A2),
                 fontsize=9, y=1.03)
    fig.tight_layout()
    salvar(fig, "fig_l5q2_fase.pdf")


# ============================================= Q2(e) the Golden Rule
def fig_regra_de_ouro():
    fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH_IN, TEXTWIDTH_IN * 0.40))
    Kg = K_gr()

    # --- panel (i): the hump, with K_ss(beta) marked
    ax = axes[0]
    K = np.linspace(0.05, 1.6 * Kg, 800)
    ax.plot(K, c_ss(K), color=AZUL, lw=1.6)
    ax.axvline(Kg, color=VERM, lw=1.1, ls="--")
    ax.plot([Kg], [c_ss(Kg)], "o", color=VERM, ms=5)
    ax.annotate(r"$K_{gr}$: $F_K=\delta$", xy=(Kg, c_ss(Kg)), fontsize=7.5,
                xytext=(-6, 8), textcoords="offset points", color=VERM, ha="right")
    for beta, cor in ((0.90, CINZA), (0.96, VERDE), (0.99, ROXO)):
        Ks = K_ss(beta)
        ax.plot([Ks], [c_ss(Ks)], "o", color=cor, ms=4)
        ax.annotate(r"$\beta=%.2f$" % beta, xy=(Ks, c_ss(Ks)), fontsize=7,
                    xytext=(2, -11), textcoords="offset points", color=cor)
    ax.set_xlabel(r"$K$")
    ax.set_ylabel(r"$c^{ss}(K)=AK^{\alpha}-\delta K$")
    ax.set_ylim(0, 1.6)
    ax.set_title(r"(i) every steady state sits to the \emph{left} of $K_{gr}$",
                 fontsize=8.5)

    # --- panel (ii): the two shortfalls against beta
    ax = axes[1]
    b = np.linspace(0.86, 0.9995, 400)
    fk = [1 - K_ss(x) / Kg for x in b]
    fc = [1 - c_ss(K_ss(x)) / c_ss(Kg) for x in b]
    ax.plot(b, np.array(fk) * 100, color=AZUL, lw=1.6, label=r"capital shortfall")
    ax.plot(b, np.array(fc) * 100, color=VERM, lw=1.6, label=r"consumption shortfall")
    ax.set_xlabel(r"$\beta$")
    ax.set_ylabel(r"shortfall relative to the Golden Rule (\%)")
    ax.legend(loc="upper right", frameon=False, fontsize=7.5)
    ax.set_title(r"(ii) a huge capital gap costs very little consumption",
                 fontsize=8.5)

    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)

    fig.suptitle(r"Q2(e) --- $K^{ss}<K_{gr}$, and the two converge as "
                 r"$\beta\to1$", fontsize=9, y=1.04)
    fig.tight_layout()
    salvar(fig, "fig_l5q2_regradeouro.pdf")


if __name__ == "__main__":
    fig_trabalho()
    fig_elasticidades()
    fig_fase()
    fig_regra_de_ouro()
    print("all figures written to", RAIZ)
