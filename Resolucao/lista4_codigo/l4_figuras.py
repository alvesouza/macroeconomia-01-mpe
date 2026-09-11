"""Figuras da Lista 4. Gera os PDFs em Resolucao/fig/.

Calibracao das figuras da Questao 1: b = 1,54 e gamma = 1 (o caso de Prescott,
Kurlat Ex. 7.5), hbar = 1, w = 1, tau entre 0,34 (EUA) e 0,53 (Europa).
Questao 2: s = 0,02, alpha = 0,5, mu = 0,30/sqrt(0,7)  ->  u* = 6,25%.

Backend pgf (ver estilo_mpl): o texto das figuras e composto pelo pdflatex com
lmodern + cmap, entao o PDF final continua 100% copiavel.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import estilo_mpl                                       # noqa: F401  (antes do pyplot)
from estilo_mpl import TEXTWIDTH_IN
import numpy as np
import matplotlib.pyplot as plt
from modelo import (lazer, horas, beveridge, f_rate, q_rate, u_estrela,
                    salario_reserva)

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "fig"))
os.makedirs(RAIZ, exist_ok=True)

AZUL, VERM, CINZA, VERDE = "#1f4e9c", "#b03030", "#808080", "#1f7a4d"
B, GAMMA, HBAR, W = 1.54, 1.0, 1.0, 1.0
S, ALPHA, THETA0 = 0.02, 0.5, 0.7
MU = 0.30 / THETA0 ** ALPHA


def salvar(fig, nome):
    caminho = os.path.join(RAIZ, nome)
    fig.savefig(caminho, bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)
    print("gravado:", caminho)


def indiferenca(l, l_star, c_star):
    """Curva de indiferenca de ln c + b*ln l passando por (l_star, c_star)."""
    return c_star * (l_star / l) ** B


# =====================================================================
# Fig. 1 -- plano (lazer, consumo): o imposto GIRA a reta em torno de
#           (hbar, T). Com T = 0 o pivo e o eixo e o otimo nao se move.
# =====================================================================
def fig_lazer():
    fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH_IN, TEXTWIDTH_IN * 0.42))
    l = np.linspace(0.28, 1.0, 400)

    for ax, T, titulo in [
            (axes[0], 0.0, r"(i) $T=0$: o \'otimo \textbf{n\~ao se move}"),
            (axes[1], 0.102, r"(ii) $T>0$: o \'otimo \textbf{desliza} para mais lazer")]:
        for tau, cor, estilo in [(0.34, AZUL, "-"), (0.53, VERM, "--")]:
            wt = (1 - tau) * W
            reta = wt * (HBAR - l) + T
            ax.plot(l, reta, color=cor, ls=estilo, lw=1.4,
                    label=r"$\tau=%.2f$" % tau)
            ls = lazer(wt, B, GAMMA, T)
            cs = wt * (HBAR - ls) + T
            ind = indiferenca(l, ls, cs)
            ax.plot(l, ind, color=cor, ls=":", lw=0.9, alpha=0.75)
            ax.plot([ls], [cs], "o", color=cor, ms=4.5, zorder=5)
            ax.vlines(ls, 0, cs, color=cor, lw=0.6, ls=(0, (1, 2)))
        # ponto-pivo: nao trabalhar
        ax.plot([HBAR], [T], "s", color="black", ms=4, zorder=6)
        ax.annotate(r"piv\^o $(\bar h,\,T)$: n\~ao trabalhar", xy=(HBAR, T),
                    xytext=(0.46, 0.035), fontsize=7.5,
                    arrowprops=dict(arrowstyle="->", lw=0.6, color="black"))
        ax.set_xlim(0.28, 1.06)
        ax.set_ylim(0, 0.78)
        ax.set_xlabel(r"lazer $\ell$")
        ax.set_ylabel(r"consumo $c$")
        ax.set_title(titulo, fontsize=8.5)
        ax.legend(loc="upper right", frameon=False)
        ax.spines[["top", "right"]].set_visible(False)

    fig.suptitle(r"O imposto \textbf{gira} a restri\c{c}\~ao em torno do ponto de "
                 r"n\~ao trabalhar --- $b=1{,}54$, $\gamma=1$, $w=1$",
                 fontsize=9, y=1.02)
    salvar(fig, "fig_l4q1_lazer.pdf")


# =====================================================================
# Fig. 2 -- a curva de oferta de trabalho no plano (n, w)
# =====================================================================
def fig_oferta():
    fig, ax = plt.subplots(figsize=(TEXTWIDTH_IN * 0.72, TEXTWIDTH_IN * 0.44))
    ws = np.linspace(0.02, 2.0, 500)

    casos = [(0.0, 0.34, AZUL, "-", r"$T=0$, $\tau=0{,}34$"),
             (0.102, 0.34, VERDE, "-", r"$T=0{,}102$, $\tau=0{,}34$"),
             (0.102, 0.53, VERM, "--", r"$T=0{,}102$, $\tau=0{,}53$")]
    for T, tau, cor, estilo, rot in casos:
        ns = [horas((1 - tau) * w, B, GAMMA, T) for w in ws]
        ax.plot(ns, ws, color=cor, ls=estilo, lw=1.5, label=rot)
        if T > 0:
            wr = salario_reserva(T, B, GAMMA, tau)
            ax.plot([0], [wr], "o", color=cor, ms=4, zorder=5)
            ax.hlines(wr, 0, 0.035, color=cor, lw=0.7)

    ax.annotate(r"$T=0$: \textbf{vertical}" "\n" r"renda e substitui\c{c}\~ao"
                "\n" r"se cancelam",
                xy=(1 / (1 + B), 1.30), xytext=(0.035, 1.66), fontsize=7.5,
                color=AZUL, arrowprops=dict(arrowstyle="->", lw=0.6, color=AZUL))
    ax.annotate(r"$w^r=\dfrac{bT\bar h^{-\gamma}}{1-\tau}$",
                xy=(0.006, 0.334), xytext=(0.105, 0.09), fontsize=7.5, color=VERM,
                arrowprops=dict(arrowstyle="->", lw=0.6, color=VERM))
    ax.annotate("", xy=(0.2389, 0.85), xytext=(0.2835, 0.85),
                arrowprops=dict(arrowstyle="->", lw=1.0, color=VERM))
    ax.text(0.243, 0.90, r"$\tau\uparrow$", fontsize=8.5, color=VERM)

    ax.set_xlim(0, 0.56)
    ax.set_ylim(0, 2.0)
    ax.set_xlabel(r"horas trabalhadas $n=\bar h-\ell$")
    ax.set_ylabel(r"sal\'ario bruto $w$")
    ax.set_title(r"Oferta de trabalho: $T$ \'e o que quebra o empate", fontsize=9)
    ax.legend(loc="center right", frameon=False, fontsize=7.5)
    ax.spines[["top", "right"]].set_visible(False)
    salvar(fig, "fig_l4q1_oferta.pdf")


# =====================================================================
# Fig. 3 -- Beveridge: movimento AO LONGO x DESLOCAMENTO
# =====================================================================
def fig_beveridge():
    fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH_IN, TEXTWIDTH_IN * 0.42))
    us = np.linspace(0.022, 0.16, 500)
    v_base = beveridge(us, S, MU, ALPHA)
    u0 = u_estrela(THETA0, S, MU, ALPHA)
    v0 = THETA0 * u0

    # ---- painel (i): movimento ao longo, dirigido por theta ----
    ax = axes[0]
    ax.plot(us, v_base, color=AZUL, lw=1.6, label=r"curva de Beveridge")
    for th, cor, alpha_ in [(0.35, CINZA, 0.9), (THETA0, "black", 0.9),
                            (1.40, CINZA, 0.9)]:
        u_th = u_estrela(th, S, MU, ALPHA)
        ax.plot(us, th * us, color=cor, lw=0.7, ls=(0, (4, 3)), alpha=alpha_)
        ax.plot([u_th], [th * u_th], "o", color=AZUL, ms=4.5, zorder=5)
        ax.annotate(r"$\theta=%.2f$" % th, xy=(u_th, th * u_th),
                    xytext=(u_th + 0.003, th * u_th + 0.011), fontsize=7)
    ax.annotate("", xy=(u_estrela(1.40, S, MU, ALPHA), 1.40 * u_estrela(1.40, S, MU, ALPHA)),
                xytext=(u_estrela(0.35, S, MU, ALPHA), 0.35 * u_estrela(0.35, S, MU, ALPHA)),
                arrowprops=dict(arrowstyle="->", lw=1.2, color=VERDE,
                                connectionstyle="arc3,rad=-0.25"))
    ax.text(0.157, 0.108, r"\textbf{movimento ao longo}" "\n"
            r"($\theta$ varia; $\mu$ e $s$ fixos)",
            fontsize=7.5, color=VERDE, ha="right", va="top")
    ax.set_title(r"(i) O ciclo desliza sobre a curva", fontsize=8.5)

    # ---- painel (ii): deslocamento, dirigido por mu ----
    ax = axes[1]
    mu1 = 0.8 * MU
    ax.plot(us, v_base, color=AZUL, lw=1.6, label=r"$\mu$ inicial")
    ax.plot(us, beveridge(us, S, mu1, ALPHA), color=VERM, lw=1.6, ls="--",
            label=r"$\mu$ 20\% menor")
    ax.plot(us, THETA0 * us, color="black", lw=0.7, ls=(0, (4, 3)))
    ax.plot([u0], [v0], "o", color=AZUL, ms=4.5, zorder=5)
    u1 = u_estrela(THETA0, S, mu1, ALPHA)
    ax.plot([u1], [THETA0 * u1], "o", color=VERM, ms=4.5, zorder=5)
    ax.annotate("", xy=(u0, beveridge(u0, S, mu1, ALPHA)), xytext=(u0, v0),
                arrowprops=dict(arrowstyle="->", lw=1.2, color=VERM))
    ax.text(0.157, 0.108, r"\textbf{deslocamento}" "\n"
            r"mesmo $u$, \textbf{mais} vagas:" "\n"
            r"$\partial\ln v/\partial\ln\mu|_u=-1/\alpha$",
            fontsize=7.5, color=VERM, ha="right", va="top")
    ax.annotate(r"a $\theta$ constante," "\n" r"$u^\ast$ sobe", xy=(u1, THETA0 * u1),
                xytext=(u1 + 0.026, THETA0 * u1 - 0.030), fontsize=7,
                arrowprops=dict(arrowstyle="->", lw=0.6, color="black"))
    ax.set_title(r"(ii) A pior efici\^encia move a curva", fontsize=8.5)
    ax.legend(loc="lower left", frameon=False, fontsize=7.5)

    for ax in axes:
        ax.set_xlim(0.02, 0.16)
        ax.set_ylim(0, 0.115)
        ax.set_xlabel(r"taxa de desemprego $u$")
        ax.set_ylabel(r"taxa de vagas $v$")
        ax.spines[["top", "right"]].set_visible(False)

    fig.suptitle(r"Curva de Beveridge --- $s=0{,}02$, $\alpha=0{,}5$, "
                 r"$u^\ast=6{,}25\%$ no ponto de refer\^encia", fontsize=9, y=1.02)
    salvar(fig, "fig_l4q2_beveridge.pdf")


# =====================================================================
# Fig. 4 -- f e q como funcoes de theta, e a vaga extra
# =====================================================================
def fig_fq():
    fig, ax = plt.subplots(figsize=(TEXTWIDTH_IN * 0.72, TEXTWIDTH_IN * 0.44))
    th = np.linspace(0.08, 2.4, 500)
    ax.plot(th, f_rate(th, MU, ALPHA), color=AZUL, lw=1.6,
            label=r"$f(\theta)=\mu\theta^{\alpha}$ --- acha emprego")
    ax.plot(th, q_rate(th, MU, ALPHA), color=VERM, lw=1.6, ls="--",
            label=r"$q(\theta)=\mu\theta^{\alpha-1}$ --- preenche vaga")

    f0, q0 = f_rate(THETA0, MU, ALPHA), q_rate(THETA0, MU, ALPHA)
    ax.plot([THETA0], [f0], "o", color=AZUL, ms=4.5, zorder=5)
    ax.plot([THETA0], [q0], "o", color=VERM, ms=4.5, zorder=5)
    ax.vlines(THETA0, 0, max(f0, q0), color=CINZA, lw=0.7, ls=(0, (1, 2)))

    th1 = 1.32 * THETA0          # deslocamento exagerado, so para ficar visivel
    ax.annotate("", xy=(th1, f_rate(th1, MU, ALPHA)), xytext=(THETA0, f0),
                arrowprops=dict(arrowstyle="->", lw=1.3, color=AZUL))
    ax.annotate("", xy=(th1, q_rate(th1, MU, ALPHA)), xytext=(THETA0, q0),
                arrowprops=dict(arrowstyle="->", lw=1.3, color=VERM))
    ax.text(2.35, 0.90, r"uma vaga a mais: $\theta\uparrow$" "\n"
            r"$f\uparrow$ --- ganham os desempregados" "\n"
            r"$q\downarrow$ --- perdem as outras firmas" "\n"
            r"{\footnotesize (seta ampliada para visualiza\c{c}\~ao)}",
            fontsize=7.5, ha="right", va="top")
    ax.plot([1.0], [MU], "^", color="black", ms=4.5, zorder=6)
    ax.annotate(r"$f=q=\mu$ em $\theta=1$", xy=(1.0, MU),
                xytext=(1.28, 0.53), fontsize=7.5,
                arrowprops=dict(arrowstyle="->", lw=0.6, color="black"))

    ax.set_xlim(0, 2.4)
    ax.set_ylim(0, 0.95)
    ax.set_xlabel(r"tightness $\theta=V/U$")
    ax.set_ylabel(r"taxa mensal")
    ax.set_title(r"$f=\theta q$: os dois lados do mesmo encontro", fontsize=9)
    ax.legend(loc="lower right", frameon=False, fontsize=7.5)
    ax.spines[["top", "right"]].set_visible(False)
    salvar(fig, "fig_l4q2_fq.pdf")


if __name__ == "__main__":
    fig_lazer()
    fig_oferta()
    fig_beveridge()
    fig_fq()
