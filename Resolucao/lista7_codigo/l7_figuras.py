"""Numbers and figures for the Problem Set 7 resolution (Benigno, 2015).

Prints every number quoted in lista7_resolucao.tex, then writes into Resolucao/fig/:

  fig_l7q2_shocks.pdf  -- Q2: (a) temporary mark-up rise, (b) nominal-rate cut
  fig_l7q2_paths.pdf   -- Q2: before / short-run / long-run paths (short version)
  fig_l7q3_wedge.pdf   -- Q3: the mark-up wedge between y_n and y_e, against a
                          productivity shock that moves both
  fig_l7q4_loss.pdf    -- Q4: iso-loss ellipses tangent to AS, and the loss along AS

All variables are log-deviations from an efficient steady state (mu = 0 there),
shown in per cent. Calibration is Benigno's own: alpha, sigma, eta from p. 515,
theta from footnote 24, p. 522. pgf backend: no Type 3 fonts in the final PDF.
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
AZUL, VERM, CINZA, VERDE, ROXO, OCRE = ("#1f4e9c", "#b03030", "#808080",
                                        "#1f7a4d", "#5b2d8e", "#b5761f")

ALPHA, SIGMA, ETA, THETA, RHO = 0.66, 0.5, 0.2, 8.0, 2.0   # RHO in per cent
S = 1 / SIGMA + ETA                                        # sigma^-1 + eta
KAPPA = (1 - ALPHA) * S / ALPHA                            # eq. (17)
DMU, DI = 5.0, -1.0              # Q2 shocks, per cent / percentage points


def y_nat(a=0.0, g=0.0, mu=0.0):
    """Natural output, eq. (15). a, g, mu and the result in per cent."""
    return ((1 + ETA) * a + g / SIGMA - mu) / S


def y_eff(a=0.0, g=0.0):
    """Efficient output, eq. (19): eq. (15) with the wedge mu removed."""
    return ((1 + ETA) * a + g / SIGMA) / S


def equilibrio(yn, i, ybar_n=0.0, pe=0.0, pbar=0.0):
    """AS (17) meets AD (21), with g = gbar and no taxes. Returns (y, p)."""
    y = (ybar_n + SIGMA * KAPPA * yn - SIGMA * (i - RHO - (pbar - pe))) / (1 + SIGMA * KAPPA)
    return y, pe + KAPPA * (y - yn)


def otimo(phi_y, phi_p, y_star, yn, kappa=KAPPA):
    """Q4: minimise phi_y (y-y*)^2 + phi_p (p-pe)^2 subject to AS; pe = 0."""
    y = (phi_y * y_star + phi_p * kappa**2 * yn) / (phi_y + phi_p * kappa**2)
    p = kappa * (y - yn)
    return y, p, phi_y * (y - y_star)**2 + phi_p * p**2


def numeros():
    """Every number the .tex quotes, printed once so the text can be checked."""
    print(f"kappa = {KAPPA:.4f}, sigma*kappa = {SIGMA*KAPPA:.4f}, theta*kappa = {THETA*KAPPA:.4f}")
    # Q2(a)
    yn1 = y_nat(mu=DMU)
    y1, p1 = equilibrio(yn1, RHO)
    print(f"Q2a  dy_n={yn1:.4f}  dy={y1:.4f}  dp={p1:.4f}  y-y_n={y1-yn1:.4f}  y-y_e={y1:.4f}"
          f"  r_n={RHO - yn1/SIGMA:.4f}")
    # Q2(b)
    y2, p2 = equilibrio(0.0, RHO + DI)
    print(f"Q2b  AD up by {-DI:.2f} in p, right by {-SIGMA*DI:.2f} in y;"
          f"  dy={y2:.4f}  dp={p2:.4f}  gaps={y2:.4f}")
    # Q3
    print(f"Q3   y_n-y_e={y_nat(mu=DMU)-y_eff():.4f}  DWL=1/2 mu^2/S={0.5*DMU**2/S:.4f}"
          f"  a=+2%: y_n={y_nat(a=2):.4f} y_e={y_eff(a=2):.4f}")
    # Q4 with Benigno weights and y* = y_e = 0
    phi_y, phi_p = 0.5, THETA / (2 * KAPPA)
    yo, po, lo = otimo(phi_y, phi_p, 0.0, yn1)
    i_opt = (RHO - yn1 / SIGMA) - (1 + SIGMA * KAPPA) * (yo - yn1) / SIGMA
    print(f"Q4   phi_p={phi_p:.4f}  y={yo:.4f}  p={po:.4f}  share to prices="
          f"{1/(1+THETA*KAPPA):.4f}  loss={lo:.4f}  i*={i_opt:.4f}"
          f"  rule={phi_y*yo + phi_p*KAPPA*po:.2e}")
    print(f"     strict price: y={yn1:.4f} p=0 ; strict output: y=0 p={-KAPPA*yn1:.4f}")
    return yn1, (y1, p1), (y2, p2), (yo, po, lo)


def salvar(fig, nome):
    fig.savefig(os.path.join(RAIZ, nome), bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)
    print("written:", nome)


def eixos(ax, xlab=r"output $y$ (\%)", ylab=r"$p-p^{e}$ (\%)"):
    ax.axhline(0, color=CINZA, lw=0.5)
    ax.axvline(0, color=CINZA, lw=0.5)
    ax.set_xlabel(xlab)
    ax.set_ylabel(ylab)
    ax.spines[["top", "right"]].set_visible(False)


def ponto(ax, x, y, rot, dx, dy, cor="black"):
    ax.plot([x], [y], "o", color=cor, ms=4.5, zorder=5)
    ax.annotate(rot, (x, y), (x + dx, y + dy), fontsize=8, color=cor)


# ============================================================ Q2: two diagrams
def fig_q2(yn1, e_a, e_b):
    fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH_IN, TEXTWIDTH_IN * 0.50))
    as_ = lambda y, yn: KAPPA * (y - yn)
    ad = lambda y, i: RHO - i + (0.0 - y) / SIGMA

    ax = axes[0]
    y = np.linspace(-4, 2.5, 300)
    ax.plot(y, as_(y, 0), color=OCRE, lw=1.1, ls="--", label=r"AS$_0$")
    ax.plot(y, as_(y, yn1), color=OCRE, lw=1.7, label=r"AS$_1$: $y_n\downarrow$")
    ax.plot(y, ad(y, RHO), color=AZUL, lw=1.7, label="AD (unchanged)")
    ax.axvline(yn1, color=CINZA, lw=0.8, ls=":")
    ax.annotate(r"$y_n'$", (yn1, -2.3), (yn1 - 0.35, -2.3), fontsize=8, color=CINZA)
    ax.annotate(r"$y_e=y_n$", (0, -2.3), (0.08, -2.3), fontsize=8, color=ROXO)
    ax.annotate("", (yn1 + 0.05, 0.25), (-0.05, 0.25),
                arrowprops=dict(arrowstyle="->", color=OCRE, lw=0.9))
    ponto(ax, 0, 0, r"$E$", 0.12, -0.45)
    ponto(ax, *e_a, r"$E'$", 0.15, 0.1)
    ax.set_xlim(-4, 2.5)
    ax.set_ylim(-2.5, 3.5)
    ax.set_title(r"(a) temporary mark-up rise, $d\mu=+5\%$")
    eixos(ax)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=3,
              frameon=False, fontsize=7, handlelength=1.6, columnspacing=1.0)

    ax = axes[1]
    y = np.linspace(-2, 2, 300)
    ax.plot(y, as_(y, 0), color=OCRE, lw=1.7, label="AS (unchanged)")
    ax.plot(y, ad(y, RHO), color=AZUL, lw=1.1, ls="--", label=r"AD$_0$: $i=r_n$")
    ax.plot(y, ad(y, RHO + DI), color=AZUL, lw=1.7, label=r"AD$_1$: $i=r_n-1$ pp")
    ax.annotate("", (0.05 - SIGMA * DI, -0.1), (0.05, -0.1),
                arrowprops=dict(arrowstyle="->", color=AZUL, lw=0.9))
    ponto(ax, 0, 0, r"$E$", -0.35, -0.4)
    ponto(ax, *e_b, r"$E'$", 0.1, -0.35)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1.5, 2)
    ax.set_title(r"(b) nominal-rate cut, $di=-1$ pp")
    eixos(ax)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=3,
              frameon=False, fontsize=7, handlelength=1.6, columnspacing=1.0)
    fig.tight_layout()
    salvar(fig, "fig_l7q2_shocks.pdf")


# ============================================================ Q3: the wedge
def fig_q3():
    fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH_IN, TEXTWIDTH_IN * 0.42))
    mrs = lambda y, a=0.0, g=0.0: ETA * (y - a) + (y - g) / SIGMA   # log v_l/u_c

    ax = axes[0]
    y = np.linspace(-4, 1.5, 200)
    yn, ye = y_nat(mu=DMU), y_eff()
    ax.plot(y, mrs(y), color=VERDE, lw=1.7, label=r"MRS $=(\sigma^{-1}+\eta)y$")
    ax.axhline(0, color=ROXO, lw=1.5, label=r"MRT $=a$ (planner)")
    ax.axhline(-DMU, color=OCRE, lw=1.5, label=r"$a-\mu$ (what firms pay)")
    tri = np.linspace(yn, ye, 50)
    ax.fill_between(tri, mrs(tri), 0, color=VERM, alpha=0.18, lw=0)
    ax.annotate("lost surplus", (-2.15, -1.4), fontsize=7.5, color=VERM)
    ax.vlines([yn, ye], -8, [-DMU, 0], color=CINZA, lw=0.8, ls=":")
    ax.annotate(r"$y_n$", (yn, -7.6), (yn + 0.07, -7.6), fontsize=8)
    ax.annotate(r"$y_e$", (ye, -7.6), (ye + 0.07, -7.6), fontsize=8)
    ax.annotate("", (-0.2, -DMU), (-0.2, 0), arrowprops=dict(arrowstyle="<->", lw=0.8))
    ax.annotate(r"$\mu$", (-0.15, -2.8), fontsize=8)
    ax.set_ylim(-8, 3)
    ax.set_title(r"(i) mark-up $\mu=+5\%$: only $y_n$ moves")
    eixos(ax, ylab=r"log real wage (\%)")
    ax.legend(loc="upper left", frameon=False, fontsize=7)

    ax = axes[1]
    a = 2.0
    y = np.linspace(-1.5, 3, 200)
    ax.plot(y, mrs(y), color=VERDE, lw=1.0, ls="--", label=r"MRS, $a=0$")
    ax.plot(y, mrs(y, a=a), color=VERDE, lw=1.7, label=r"MRS, $a=2\%$")
    ax.axhline(0, color=ROXO, lw=1.0, ls="--")
    ax.axhline(a, color=ROXO, lw=1.5, label=r"MRT $=a=2\%$")
    yn2 = y_nat(a=a)
    ax.vlines([0, yn2], -2, [0, a], color=CINZA, lw=0.8, ls=":")
    ax.annotate(r"$y_n=y_e$", (yn2, -1.8), (yn2 + 0.07, -1.8), fontsize=8)
    ax.set_ylim(-2, 5)
    ax.set_title(r"(ii) productivity $a=+2\%$: both move")
    eixos(ax, ylab=r"log real wage (\%)")
    ax.legend(loc="upper left", frameon=False, fontsize=7)
    fig.tight_layout()
    salvar(fig, "fig_l7q3_wedge.pdf")


# ============================================================ Q4: the loss bowl
def fig_q4(yn1, opt):
    phi_y, phi_p = 0.5, THETA / (2 * KAPPA)
    yo, po, lo = opt
    fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH_IN, TEXTWIDTH_IN * 0.44))

    ax = axes[0]
    Y, P = np.meshgrid(np.linspace(-3.5, 1.5, 300), np.linspace(-1, 3, 300))
    L = phi_y * Y**2 + phi_p * P**2
    ax.contour(Y, P, L, levels=[lo / 4, lo, 2.25 * lo], colors=VERM,
               linewidths=[0.6, 1.4, 0.6])
    y = np.linspace(-3.5, 1.5, 200)
    ax.plot(y, KAPPA * (y - yn1), color=OCRE, lw=1.7, label=r"AS: $p-p^e=\kappa(y-y_n)$")
    ax.plot(y, -phi_y / (phi_p * KAPPA) * y, color=ROXO, lw=1.2, ls="--",
            label="targeting rule (IT)")
    ponto(ax, 0, 0, r"bliss $(y^{\ast},p^e)$", 0.1, 0.12, ROXO)
    ponto(ax, yo, po, "optimum", -1.3, 0.25, VERM)
    ponto(ax, yn1, 0, "strict price", -1.15, -0.45, CINZA)
    ponto(ax, 0, -KAPPA * yn1, "strict output", 0.1, -0.05, CINZA)
    ax.set_xlim(-3.5, 1.5)
    ax.set_ylim(-1, 3)
    ax.set_title(r"(i) iso-loss ellipses and the AS constraint")
    eixos(ax)
    ax.legend(loc="upper left", frameon=False, fontsize=7)

    ax = axes[1]
    y = np.linspace(yn1 - 0.6, 0.6, 300)
    out = phi_y * y**2
    pri = phi_p * (KAPPA * (y - yn1))**2
    ax.plot(y, out, color=AZUL, lw=1.1, ls="--", label=r"$\phi_y(y-y^{\ast})^2$")
    ax.plot(y, pri, color=OCRE, lw=1.1, ls="--", label=r"$\phi_p\kappa^2(y-y_n)^2$")
    ax.plot(y, out + pri, color=VERM, lw=1.7, label="total loss on AS")
    ponto(ax, yo, lo, "min", 0.08, 0.3, VERM)
    ax.axvline(yn1, color=CINZA, lw=0.8, ls=":")
    ax.axvline(0, color=CINZA, lw=0.8, ls=":")
    ax.set_ylim(0, 6)
    ax.set_title(r"(ii) loss along AS, Benigno weights")
    eixos(ax, ylab=r"loss $\mathcal{L}$")
    ax.legend(loc="upper right", frameon=False, fontsize=7)
    fig.tight_layout()
    salvar(fig, "fig_l7q4_loss.pdf")


# ================================================= Q2: time paths (short version)
def fig_q2_paths(e_a, e_b):
    """Two-period paths of y and p - p^e under each Q2 change.

    Period 0 is the pre-shock steady state, 1 the short run (AS-AD crossing),
    2 the long run: every firm resets, y = ybar_n = 0 and p = pbar = p^e.
    Used by lista7_resolucao_curta.tex, which pairs each AS-AD panel with a path.
    """
    t = [0, 1, 2]
    fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH_IN, TEXTWIDTH_IN * 0.26))
    for ax, (y1, p1), titulo in ((axes[0], e_a, r"(a) $d\mu=+5\%$"),
                                 (axes[1], e_b, r"(b) $di=-1$ pp")):
        ax.plot(t, [0, y1, 0], "o-", color=AZUL, lw=1.4, ms=3.5, label=r"$y$")
        ax.plot(t, [0, p1, 0], "s--", color=OCRE, lw=1.4, ms=3.5, label=r"$p-p^e$")
        ax.axhline(0, color=CINZA, lw=0.5)
        ax.set_xticks(t, ["before", "SR", "LR"])
        ax.set_title(titulo)
        ax.spines[["top", "right"]].set_visible(False)
        ax.legend(loc="upper left", frameon=False,
                  fontsize=7, ncol=2)
    axes[0].set_ylabel(r"\% dev.")
    fig.tight_layout()
    salvar(fig, "fig_l7q2_paths.pdf")


if __name__ == "__main__":
    yn1, e_a, e_b, opt = numeros()
    fig_q2(yn1, e_a, e_b)
    fig_q2_paths(e_a, e_b)
    fig_q3()
    fig_q4(yn1, opt)
