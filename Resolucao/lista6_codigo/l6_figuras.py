"""Figures for the Problem Set 6 resolution.  Writes PDFs into Resolucao/fig/.

  fig_l6q2_eta.pdf    -- Q2(b): pi = mu - eta*g, and the required mu(g) schedules
  fig_l6q2_trips.pdf  -- Q2(c): a falling trip cost F under a fixed money-growth rule

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

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "fig"))
os.makedirs(RAIZ, exist_ok=True)
AZUL, VERM, CINZA, VERDE, ROXO = "#1f4e9c", "#b03030", "#808080", "#1f7a4d", "#5b2d8e"

PI_ALVO, G = 0.02, 0.03          # target inflation and output growth of item (b)
ETA_BT, ETA_CAMB = 0.5, 1.0      # Baumol-Tobin and Cambridge income elasticities


def inflacao(mu, eta, g=G):
    """Steady-state inflation of item (a): pi = mu - eta*g."""
    return mu - eta * g


def mu_requerido(eta, pi=PI_ALVO, g=G):
    """Money growth a bank must pick to hit pi, believing the elasticity is eta."""
    return pi + eta * g


def salvar(fig, nome):
    fig.savefig(os.path.join(RAIZ, nome), bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)
    print("written:", nome)


# ===================================== Q2(b) the elasticity and the target miss
def fig_eta():
    mu_bt = mu_requerido(ETA_BT)
    fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH_IN, TEXTWIDTH_IN * 0.40))

    # --- panel (i): with mu locked at 3,5%, realised inflation falls in eta
    ax = axes[0]
    eta = np.linspace(0, 1.4, 400)
    ax.plot(eta, 100 * inflacao(mu_bt, eta), color=AZUL, lw=1.6,
            label=r"$\pi=\mu-\eta g$, $\mu=3{,}5\%$")
    ax.axhline(100 * PI_ALVO, color=CINZA, lw=0.9, ls="--")
    ax.annotate(r"target $\pi^{\ast}=2\%$", (1.32, 100 * PI_ALVO + 0.12),
                ha="right", fontsize=7.5, color=CINZA)
    for e, cor, rot in ((ETA_BT, VERDE, "Baumol--Tobin"), (ETA_CAMB, VERM, "Cambridge")):
        p = 100 * inflacao(mu_bt, e)
        ax.plot([e], [p], "o", color=cor, ms=5)
        ax.vlines(e, 0, p, color=cor, lw=0.8, ls=":")
        dx, dy = (-0.44, 0.30) if e == ETA_BT else (0.04, 0.22)
        ax.annotate(r"%s: $\eta=%.1f$, $\pi=%.1f\%%$" % (rot, e, p),
                    (e + dx, p + dy), fontsize=7.5, color=cor)
    ax.set_xlim(0, 1.4)
    ax.set_ylim(0, 4)
    ax.set_xlabel(r"income elasticity of real money demand $\eta$")
    ax.set_ylabel(r"realised inflation $\pi$ (\% p.a.)")
    ax.set_title(r"(i) one $\mu$, two beliefs: the miss is $(\eta-\tfrac12)g$",
                 fontsize=8.5)

    # --- panel (ii): the mu the bank must announce, as a function of g
    ax = axes[1]
    g = np.linspace(0, 0.06, 200)
    for e, cor, lab in ((ETA_BT, VERDE, r"$\eta=\tfrac12$ (Baumol--Tobin)"),
                        (ETA_CAMB, VERM, r"$\eta=1$ (Cambridge)")):
        ax.plot(100 * g, 100 * mu_requerido(e, g=g), color=cor, lw=1.5, label=lab)
    ax.axhline(100 * mu_bt, color=VERDE, lw=0.8, ls=":")
    ax.plot([100 * G], [100 * mu_bt], "o", color=VERDE, ms=5)
    ax.plot([100 * G], [100 * mu_requerido(ETA_CAMB)], "o", color=VERM, ms=5)
    ax.annotate("", xy=(100 * G, 100 * mu_requerido(ETA_CAMB)),
                xytext=(100 * G, 100 * mu_bt),
                arrowprops=dict(arrowstyle="<->", color=ROXO, lw=1.0))
    ax.annotate(r"$1{,}5$ p.p.\ short", (100 * G - 0.15, 100 * (mu_bt + 0.0075)),
                ha="right", fontsize=7.5, color=ROXO)
    ax.set_xlim(0, 6)
    ax.set_ylim(1.8, 8.2)
    ax.set_xlabel(r"output growth $g$ (\% p.a.)")
    ax.set_ylabel(r"$\mu$ needed for $\pi^{\ast}=2\%$ (\% p.a.)")
    ax.legend(loc="upper left", frameon=False, fontsize=7.5)
    ax.set_title(r"(ii) $\mu=\pi^{\ast}+\eta g$: the slope \emph{is} $\eta$",
                 fontsize=8.5)

    salvar(fig, "fig_l6q2_eta.pdf")


# ============================ Q2(c) a falling trip cost under a fixed mu rule
def fig_trips():
    mu, f = 0.035, -0.02
    T = np.linspace(0, 20, 300)
    fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH_IN, TEXTWIDTH_IN * 0.40))

    # --- panel (i): log paths.  m grows at (g+f)/2, so p absorbs the rest.
    ax = axes[0]
    ax.plot(T, 100 * mu * T, color=AZUL, lw=1.6, label=r"$\ln M$ (rule: $\mu=3{,}5\%$)")
    for ff, cor, ls, lab in ((0.0, VERDE, "-", r"$f=0$"), (f, VERM, "-", r"$f=-2\%$")):
        m = 0.5 * (G + ff)
        ax.plot(T, 100 * m * T, color=cor, lw=1.2, ls="--",
                label=r"$\ln m^{D}$, %s" % lab)
        ax.plot(T, 100 * (mu - m) * T, color=cor, lw=1.6, ls=ls,
                label=r"$\ln p$, %s: $\pi=%.1f\%%$" % (lab, 100 * (mu - m)))
    ax.set_xlim(0, 20)
    ax.set_xlabel(r"time (years)")
    ax.set_ylabel(r"log level, $\times 100$ (base year $=0$)")
    ax.legend(loc="upper left", frameon=True, framealpha=0.92,
              edgecolor="none", facecolor="white", fontsize=7)
    ax.set_title(r"(i) $p$ is the residual: $\pi=\mu-\tfrac12(g+f)$", fontsize=8.5)

    # --- panel (ii): inflation against the rate of decline of F
    ax = axes[1]
    ff = np.linspace(-0.06, 0.02, 200)
    pi = mu - 0.5 * (G + ff)
    ax.plot(100 * ff, 100 * pi, color=AZUL, lw=1.6,
            label=r"$\pi=\mu-\tfrac12(g+f)$")
    ax.axvline(0, color=CINZA, lw=0.8)
    ax.axhline(100 * (mu - 0.5 * G), color=VERDE, lw=0.9, ls="--")
    ax.plot([0], [100 * (mu - 0.5 * G)], "o", color=VERDE, ms=5)
    ax.annotate(r"$f=0$: $\pi=2\%$ (the target)", (-0.3, 100 * (mu - 0.5 * G) - 0.40),
                ha="right", fontsize=7.5, color=VERDE)
    ax.plot([100 * f], [100 * (mu - 0.5 * (G + f))], "o", color=VERM, ms=5)
    ax.annotate(r"Pix, ATMs, cards: $f<0\Rightarrow\pi\uparrow$",
                (100 * f + 0.2, 100 * (mu - 0.5 * (G + f)) + 0.1),
                fontsize=7.5, color=VERM)
    ax.fill_between(100 * ff, 100 * (mu - 0.5 * G), 100 * pi,
                    where=(ff < 0), color=VERM, alpha=0.10)
    ax.set_xlim(-6, 2)
    ax.set_xlabel(r"rate of change of the trip cost $f=\dot F/F$ (\% p.a.)")
    ax.set_ylabel(r"inflation $\pi$ (\% p.a.)")
    ax.legend(loc="lower left", frameon=False, fontsize=7.5)
    ax.set_title(r"(ii) payments innovation is inflationary under a fixed $\mu$",
                 fontsize=8.5)

    salvar(fig, "fig_l6q2_trips.pdf")


def demo():
    """Self-check: the three numbers item (b) asks for, and (c)'s cross-check."""
    assert abs(mu_requerido(ETA_BT) - 0.035) < 1e-12          # b(ii)
    assert abs(inflacao(0.035, ETA_CAMB) - 0.005) < 1e-12      # b(iii)
    # (c) via velocity: pi = mu + V_hat - g with V_hat = (g-f)/2 must equal mu - (g+f)/2
    for f in (-0.04, -0.02, 0.0, 0.01):
        direto = 0.035 - 0.5 * (G + f)
        via_v = 0.035 + 0.5 * (G - f) - G
        assert abs(direto - via_v) < 1e-12
    print("b(i) eta = 1/2 | b(ii) mu = %.2f%% | b(iii) pi = %.2f%%"
          % (100 * mu_requerido(ETA_BT), 100 * inflacao(mu_requerido(ETA_BT), ETA_CAMB)))
    print("c: f=-2%% -> pi = %.2f%%" % (100 * (0.035 - 0.5 * (G - 0.02))))


if __name__ == "__main__":
    demo()
    fig_eta()
    fig_trips()
