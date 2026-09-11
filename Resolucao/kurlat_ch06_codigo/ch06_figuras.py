"""Figures for the Kurlat ch. 6 exercises. Writes PDFs into Resolucao/fig/.

  fig_k6_1_juros.pdf    -- 6.1(e): c1 against r for sigma below, at and above 1
  fig_k6_3_rotacao.pdf  -- 6.3(a): the budget line rotating about the endowment
  fig_k6_5_credito.pdf  -- 6.5(b): the budget set with a borrowing limit
  fig_k6_6_imposto.pdf  -- 6.6: the kinked constraint and the three cases
  fig_k6_7_solow.pdf    -- 6.7: c*(s) and the Friedmans' declining path

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

from ch06_numerico import solucao_2p, omega, problema_6_7

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "fig"))
os.makedirs(RAIZ, exist_ok=True)
AZUL, VERM, CINZA, VERDE = "#1f4e9c", "#b03030", "#808080", "#1f7a4d"


def salvar(fig, nome):
    fig.savefig(os.path.join(RAIZ, nome), bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)
    print("written:", nome)


def curva_indiferenca(c1, beta, sigma, c1_grid):
    """The indifference curve through (c1, c2) implied by the Euler equation."""
    return c1_grid


# ================================================= 6.1(e)  c1 against r
def fig_juros():
    beta, y1, a0 = 0.96, 1.0, 0.2
    r = np.linspace(0.0, 0.30, 400)
    fig, ax = plt.subplots(figsize=(TEXTWIDTH_IN * 0.62, TEXTWIDTH_IN * 0.36))
    for sigma, cor, rot in ((0.5, AZUL, r"$\sigma=0.5$ (high EIS)"),
                            (1.0, CINZA, r"$\sigma=1$ (log)"),
                            (2.0, VERM, r"$\sigma=2$ (low EIS)")):
        c1 = (a0 + y1) / omega(beta, r, sigma)
        ax.plot(r, c1, color=cor, lw=1.5, label=rot)
    ax.set_xlabel(r"interest rate $r$")
    ax.set_ylabel(r"$c_1$")
    ax.legend(frameon=False, loc="center right")
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title(r"6.1(e) --- $y_2=\tau_1=\tau_2=0$, $a_0=0.2$, $y_1=1$, "
                 r"$\beta=0.96$", fontsize=8.5)
    fig.tight_layout()
    salvar(fig, "fig_k6_1_juros.pdf")


# ================================================= 6.3  rotation about endowment
def fig_rotacao():
    y1 = y2 = 1.0
    sigma = 2.0
    r0, r1 = 0.05, 0.60          # a large change, so the picture is legible
    beta = (y2 / y1) ** (-sigma) / (1 + r0)

    fig, ax = plt.subplots(figsize=(TEXTWIDTH_IN * 0.62, TEXTWIDTH_IN * 0.55))
    c1g = np.linspace(0.05, 2.4, 500)

    for r, cor, rot in ((r0, CINZA, r"slope $-(1+r_0)$"),
                        (r1, AZUL, r"slope $-(1+r_1)$, steeper")):
        W = y1 + y2 / (1 + r)
        ax.plot(c1g, (1 + r) * (W - c1g), color=cor, lw=1.4, label=rot)

    # indifference curves through each optimum
    for r, cor in ((r0, CINZA), (r1, AZUL)):
        c1s, c2s, _, _ = solucao_2p(y1, y2, beta, r, sigma)
        U = (c1s ** (1 - sigma) - 1) / (1 - sigma) \
            + beta * (c2s ** (1 - sigma) - 1) / (1 - sigma)
        with np.errstate(invalid="ignore", divide="ignore"):
            termo = (U - (c1g ** (1 - sigma) - 1) / (1 - sigma)) * (1 - sigma) / beta + 1
            c2g = termo ** (1 / (1 - sigma))
        c2g = np.where(np.isfinite(c2g) & (c2g > 0) & (c2g < 2.6), c2g, np.nan)
        ax.plot(c1g, c2g, color=cor, lw=1.0, ls="--")
        ax.plot([c1s], [c2s], "o", color=cor, ms=4)

    ax.plot([y1], [y2], "s", color=VERM, ms=5)
    ax.annotate(r"endowment $(y_1,y_2)$", xy=(y1, y2), fontsize=7.5,
                xytext=(6, 6), textcoords="offset points", color=VERM)
    c1s, c2s, _, _ = solucao_2p(y1, y2, beta, r1, sigma)
    ax.annotate(r"new optimum", xy=(c1s, c2s), fontsize=7.5,
                xytext=(-52, 14), textcoords="offset points", color=AZUL,
                arrowprops=dict(arrowstyle="->", color=AZUL, lw=0.7))
    ax.set_xlim(0, 2.4)
    ax.set_ylim(0, 2.6)
    ax.set_xlabel(r"$c_1$")
    ax.set_ylabel(r"$c_2$")
    ax.legend(frameon=False, loc="upper right", fontsize=7.5)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title(r"6.3(a) --- the budget line rotates \emph{about the endowment}: "
                 r"no wealth effect", fontsize=8.5)
    fig.tight_layout()
    salvar(fig, "fig_k6_3_rotacao.pdf")


# ================================================= 6.5  borrowing limit
def fig_credito():
    y1, y2, r = 1.0, 3.0, 0.05
    beta, sigma = 0.96, 2.0
    b = 0.3
    W = y1 + y2 / (1 + r)
    c1u = solucao_2p(y1, y2, beta, r, sigma)[0]
    lim = y1 + b

    fig, ax = plt.subplots(figsize=(TEXTWIDTH_IN * 0.62, TEXTWIDTH_IN * 0.50))
    c1g = np.linspace(0.05, W, 400)
    ax.plot(c1g, (1 + r) * (W - c1g), color=CINZA, lw=1.4,
            label=r"budget line, slope $-(1+r)$")
    viavel = c1g <= lim
    ax.fill_between(c1g[viavel], 0, (1 + r) * (W - c1g[viavel]),
                    color=AZUL, alpha=0.10, label=r"feasible set")
    ax.axvline(lim, color=VERM, lw=1.2, ls="--")
    ax.annotate(r"$c_1=y_1-\tau_1+b$", xy=(lim, 2.6), fontsize=7.5,
                xytext=(5, 0), textcoords="offset points", color=VERM)
    ax.plot([c1u], [(1 + r) * (W - c1u)], "o", color=CINZA, ms=4)
    ax.annotate(r"unconstrained $c_1^{u}$", xy=(c1u, (1 + r) * (W - c1u)),
                fontsize=7.5, xytext=(4, 6), textcoords="offset points", color=CINZA)
    ax.plot([lim], [(1 + r) * (W - lim)], "o", color=VERM, ms=5)
    ax.annotate(r"actual choice", xy=(lim, (1 + r) * (W - lim)), fontsize=7.5,
                xytext=(-58, -16), textcoords="offset points", color=VERM,
                arrowprops=dict(arrowstyle="->", color=VERM, lw=0.7))
    ax.plot([y1], [y2], "s", color=VERDE, ms=5)
    ax.annotate(r"endowment", xy=(y1, y2), fontsize=7.5,
                xytext=(-20, 8), textcoords="offset points", color=VERDE)
    ax.set_xlim(0, W)
    ax.set_ylim(0, (1 + r) * W * 1.02)
    ax.set_xlabel(r"$c_1$")
    ax.set_ylabel(r"$c_2$")
    ax.legend(frameon=False, loc="upper right", fontsize=7.5)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title(r"6.5(b) --- the limit $a\ge-b$ truncates the budget set at "
                 r"$c_1=y_1-\tau_1+b$", fontsize=8.5)
    fig.tight_layout()
    salvar(fig, "fig_k6_5_credito.pdf")


# ================================================= 6.6  tax on interest income
def fig_imposto():
    # r is exaggerated relative to ch06_numerico.py so that the kink is visible;
    # the three cases are the same ones, and are re-verified below.
    r, tau = 0.80, 0.5
    y1, y2 = 2.0, 0.5
    rs = r * (1 - tau)                       # after-tax return when saving

    def linha(ax):
        c1a = np.linspace(0.05, y1, 200)     # saving side
        c1b = np.linspace(y1, y1 + y2 / (1 + r) - 0.02, 200)   # borrowing side
        ax.plot(c1a, y2 + (1 + r) * (y1 - c1a), color=CINZA, lw=1.1, ls=":",
                label=r"old: slope $-(1+r)$ throughout")
        ax.plot(c1a, y2 + (1 + rs) * (y1 - c1a), color=AZUL, lw=1.5,
                label=r"new: $-(1+r(1-\tau))$ when saving")
        ax.plot(c1b, y2 + (1 + r) * (y1 - c1b), color=AZUL, lw=1.5)
        ax.plot([y1], [y2], "s", color=VERM, ms=5)

    casos = [(5.0, r"(i) low EIS ($\sigma=5$): saves \emph{more}"),
             (0.4, r"(ii) high EIS ($\sigma=0.4$): saves \emph{less}"),
             (None, r"(iii) a borrower: nothing changes")]
    fig, axes = plt.subplots(1, 3, figsize=(TEXTWIDTH_IN, TEXTWIDTH_IN * 0.34))
    beta = 0.97

    for ax, (sigma, titulo) in zip(axes, casos):
        if sigma is None:
            yy1, yy2, sg = 0.5, 2.0, 2.0
            rs_loc, r_loc = r * (1 - tau), r
            c1a = np.linspace(0.05, yy1, 200)
            c1b = np.linspace(yy1, yy1 + yy2 / (1 + r_loc) - 0.02, 200)
            ax.plot(c1a, yy2 + (1 + r_loc) * (yy1 - c1a), color=CINZA, lw=1.1, ls=":")
            ax.plot(c1a, yy2 + (1 + rs_loc) * (yy1 - c1a), color=AZUL, lw=1.5)
            ax.plot(c1b, yy2 + (1 + r_loc) * (yy1 - c1b), color=AZUL, lw=1.5)
            ax.plot([yy1], [yy2], "s", color=VERM, ms=5)
            c1o = solucao_2p(yy1, yy2, beta, r_loc, sg)[0]
            ax.plot([c1o], [yy2 + (1 + r_loc) * (yy1 - c1o)], "o", color=VERDE, ms=5)
            ax.annotate(r"unchanged", xy=(c1o, yy2 + (1 + r_loc) * (yy1 - c1o)),
                        fontsize=7, xytext=(-16, -16), textcoords="offset points",
                        color=VERDE)
            ax.set_xlim(0, yy1 + yy2 / (1 + r_loc))
        else:
            linha(ax)
            c1_antes = solucao_2p(y1, y2, beta, r, sigma)[0]
            c1_dep = solucao_2p(y1, y2, beta, rs, sigma)[0]
            ax.plot([c1_antes], [y2 + (1 + r) * (y1 - c1_antes)], "o",
                    color=CINZA, ms=4)
            ax.plot([c1_dep], [y2 + (1 + rs) * (y1 - c1_dep)], "o", color=VERDE, ms=5)
            seta = r"$c_1\downarrow$" if c1_dep < c1_antes else r"$c_1\uparrow$"
            ax.annotate(seta, xy=(c1_dep, y2 + (1 + rs) * (y1 - c1_dep)), fontsize=8,
                        xytext=(-6, -18), textcoords="offset points", color=VERDE)
            ax.set_xlim(0, y1 + y2 / (1 + r))
        ax.set_ylim(0, None)
        ax.set_xlabel(r"$c_1$")
        ax.set_ylabel(r"$c_2$")
        ax.set_title(titulo, fontsize=8)
        ax.spines[["top", "right"]].set_visible(False)

    # the three cases must still be the three cases at these parameters
    assert solucao_2p(y1, y2, beta, rs, 5.0)[0] < solucao_2p(y1, y2, beta, r, 5.0)[0]
    assert solucao_2p(y1, y2, beta, rs, 0.4)[0] > solucao_2p(y1, y2, beta, r, 0.4)[0]
    assert solucao_2p(0.5, 2.0, beta, r, 2.0)[2] < 0
    h, l = axes[0].get_legend_handles_labels()
    fig.legend(h, l, frameon=False, fontsize=7.5, ncol=2,
               loc="lower center", bbox_to_anchor=(0.5, -0.12))
    fig.suptitle(r"6.6 --- a tax on interest income kinks the budget set at the "
                 r"endowment ($r=0.8$, $\tau=0.5$, exaggerated for legibility)",
                 fontsize=9, y=1.05)
    fig.tight_layout()
    salvar(fig, "fig_k6_6_imposto.pdf")


# ================================================= 6.7  Solow and the Friedmans
def fig_solow():
    kss, yss, css, rss = problema_6_7(verbose=False)
    alpha = 0.35
    s = np.linspace(0.02, 0.95, 500)

    fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH_IN, TEXTWIDTH_IN * 0.38))

    ax = axes[0]
    ax.plot(s, css(s), color=AZUL, lw=1.5, label=r"$c^{*}(s)=(1-s)y^{*}(s)$")
    ax.axvline(alpha, color=CINZA, lw=0.9, ls="--")
    ax.annotate(r"golden rule $s=\alpha=0.35$", xy=(alpha, 0.55), fontsize=7,
                xytext=(4, 0), textcoords="offset points", color=CINZA)
    for sv, cor in ((0.4, VERM), (0.5, VERDE)):
        ax.plot([sv], [css(sv)], "o", color=cor, ms=4.5)
        ax.annotate(r"$s=%.1f$" % sv, xy=(sv, css(sv)), fontsize=7.5,
                    xytext=(4, 6), textcoords="offset points", color=cor)
    ax.set_xlabel(r"saving rate $s$")
    ax.set_ylabel(r"steady-state consumption")
    ax.set_ylim(0, 1.45)
    ax.legend(frameon=False, loc="lower center", fontsize=7.5)
    ax.set_title(r"(c) raising $s$ past $\alpha$ \emph{lowers} $c^{*}$", fontsize=8.5)

    ax = axes[1]
    r = rss(0.4)
    t = np.arange(0, 61)
    for beta, sigma, cor, rot in ((0.96, 2.0, AZUL, r"$\beta=0.96$, $\sigma=2$"),
                                  (0.99, 2.0, VERDE, r"$\beta=0.99$, $\sigma=2$"),
                                  (0.99, 5.0, VERM, r"$\beta=0.99$, $\sigma=5$")):
        g = (beta * (1 + r)) ** (1 / sigma)
        ax.plot(t, g ** t, color=cor, lw=1.4, label=rot)
    ax.axhline(1.0, color=CINZA, lw=0.9, ls="--")
    ax.set_xlabel(r"years")
    ax.set_ylabel(r"$c_t/c_0$")
    ax.set_ylim(0, 1.1)
    ax.legend(frameon=False, loc="lower left", fontsize=7)
    ax.set_title(r"(d) $r=%.4f<0$, so $c_t$ falls for \emph{every} $\beta<1$" % r,
                 fontsize=8.5)

    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)

    fig.suptitle(r"6.7 --- an over-saving Solow economy ($\alpha=0.35$, "
                 r"$\delta=0.1$, $s=0.4$)", fontsize=9, y=1.04)
    fig.tight_layout()
    salvar(fig, "fig_k6_7_solow.pdf")


if __name__ == "__main__":
    fig_juros()
    fig_rotacao()
    fig_credito()
    fig_imposto()
    fig_solow()
    print("all figures written to", RAIZ)
