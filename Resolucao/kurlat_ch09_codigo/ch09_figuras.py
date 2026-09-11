"""Figuras dos exercicios do Kurlat, cap. 9. Gera PDFs em Resolucao/fig/.

  fig_k9_3_ces.pdf     -- 9.3(a): curvas de indiferenca CES, epsilon = 0,5 e 2
  fig_k9_9_fase.pdf    -- 9.9: dois diagramas de fase (e=0 e e=ebar) e a transicao
  fig_k9_12_consumo.pdf-- 9.12(c): consumo sob poupanca fixa e otima, 150 anos

Backend pgf: texto composto pelo pdflatex com lmodern + cmap, PDF copiavel.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import estilo_mpl                                       # noqa: F401
from estilo_mpl import TEXTWIDTH_IN
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from ch09_numerico import (K_ss, iy_ss, caminho_fixo, caminho_otimo, rho_de,
                           A, B, D, S, T, K0)

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "fig"))
os.makedirs(RAIZ, exist_ok=True)
AZUL, VERM, CINZA, VERDE = "#1f4e9c", "#b03030", "#808080", "#1f7a4d"


def salvar(fig, nome):
    fig.savefig(os.path.join(RAIZ, nome), bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)
    print("gravado:", nome)


# ===================================================== 9.3(a) CES
def fig_ces():
    fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH_IN, TEXTWIDTH_IN * 0.42))
    alpha = 0.5
    x = np.linspace(0.05, 3.0, 600)

    for ax, eps, titulo in [
            (axes[0], 0.5, r"(i) $\varepsilon=0{,}5$ --- substitutos \emph{ruins}"),
            (axes[1], 2.0, r"(ii) $\varepsilon=2$ --- substitutos \emph{bons}")]:
        r = (eps - 1.0) / eps
        for u0 in [0.6, 1.0, 1.4, 1.8]:
            # u = [a^(1/e) x^r + (1-a)^(1/e) y^r]^(1/r) = u0
            termo = u0 ** r - alpha ** (1 / eps) * x ** r
            with np.errstate(invalid="ignore"):
                y = (termo / (1 - alpha) ** (1 / eps)) ** (1 / r)
            y = np.where(np.isfinite(y) & (y > 0) & (y < 3.2), y, np.nan)
            ax.plot(x, y, color=AZUL, lw=1.3)
            ok = np.isfinite(y)
            if ok.any():
                i = np.where(ok)[0][len(np.where(ok)[0]) // 2]
                ax.annotate(r"$u=%.1f$" % u0, xy=(x[i], y[i]), fontsize=6.5,
                            xytext=(3, 3), textcoords="offset points", color=AZUL)
        ax.set_xlim(0, 3.0); ax.set_ylim(0, 3.0)
        ax.set_xlabel(r"$x$ (roupas)"); ax.set_ylabel(r"$y$ (quartetos)")
        ax.set_title(titulo, fontsize=8.5)
        ax.spines[["top", "right"]].set_visible(False)

    fig.suptitle(r"9.3(a) --- curvas de indiferen\c{c}a CES, $\alpha=0{,}5$. "
                 r"Menor $\varepsilon$, mais curvatura: os bens deixam de se substituir",
                 fontsize=9, y=1.03)
    salvar(fig, "fig_k9_3_ces.pdf")


# ===================================================== 9.9 fase
def fig_fase():
    alpha, delta, beta = 0.4, 0.08, 0.95
    ebar = 0.30
    Kstar = K_ss(alpha, beta, delta)          # NAO depende de e
    K = np.linspace(0.35, 14.0, 700)
    curva = lambda e: K ** alpha + e - delta * K

    fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH_IN, TEXTWIDTH_IN * 0.44))

    # ---- painel (i): os dois diagramas sobrepostos
    ax = axes[0]
    ax.plot(K, curva(0.0), color=AZUL, lw=1.6, label=r"$\Delta K=0$ com $e=0$")
    ax.plot(K, curva(ebar), color=VERM, lw=1.6, ls="--",
            label=r"$\Delta K=0$ com $e=\bar e$")
    ax.axvline(Kstar, color="black", lw=1.2)
    ax.annotate(r"$\Delta c=0$", xy=(Kstar, 2.35), xytext=(Kstar + 0.5, 2.35),
                fontsize=7.5)
    for e, cor in [(0.0, AZUL), (ebar, VERM)]:
        ax.plot([Kstar], [Kstar ** alpha + e - delta * Kstar], "o", color=cor,
                ms=5, zorder=5)
    ax.annotate(r"as duas verticais" "\n" r"\textbf{coincidem}: $F_K$" "\n"
                r"n\~ao cont\'em $e$",
                xy=(Kstar, 0.55), xytext=(7.6, 0.35), fontsize=7,
                arrowprops=dict(arrowstyle="->", lw=0.6, color="black"))
    ax.annotate("", xy=(3.2, curva(ebar)[np.argmin(abs(K - 3.2))]),
                xytext=(3.2, curva(0.0)[np.argmin(abs(K - 3.2))]),
                arrowprops=dict(arrowstyle="->", lw=1.1, color=VERM))
    ax.text(3.4, 1.35, r"sobe exatamente $\bar e$", fontsize=7, color=VERM)
    ax.set_title(r"(i) O petr\'oleo desloca s\'o a curva", fontsize=8.5)
    ax.legend(loc="lower right", frameon=False, fontsize=7)

    # ---- painel (ii): a transicao quando o petroleo acaba em T
    ax = axes[1]
    ax.plot(K, curva(0.0), color=AZUL, lw=1.6)
    ax.plot(K, curva(ebar), color=VERM, lw=1.4, ls="--", alpha=0.8)
    ax.axvline(Kstar, color="black", lw=1.2)
    c_ini = Kstar ** alpha + ebar - delta * Kstar
    c_fim = Kstar ** alpha - delta * Kstar
    KT, cT = 8.6, 1.42
    ax.plot([Kstar], [c_ini], "o", color=VERM, ms=5, zorder=6)
    ax.plot([Kstar], [c_fim], "o", color=AZUL, ms=5, zorder=6)
    ax.annotate("", xy=(Kstar, 1.30), xytext=(Kstar, c_ini),
                arrowprops=dict(arrowstyle="->", lw=1.4, color=VERDE))
    ax.text(Kstar - 3.6, 1.55, r"1. $c$ \textbf{salta para baixo}" "\n"
            r"(efeito riqueza)", fontsize=7, color=VERDE)
    Karc = np.linspace(Kstar, KT, 60)
    ax.plot(Karc, 1.30 + (cT - 1.30) * (Karc - Kstar) / (KT - Kstar),
            color=VERDE, lw=1.5)
    ax.annotate("", xy=(KT, cT), xytext=(KT - 0.7, cT - 0.02),
                arrowprops=dict(arrowstyle="->", lw=1.4, color=VERDE))
    ax.text(7.0, 1.12, r"2. $K$ \textbf{cresce} at\'e $T$", fontsize=7, color=VERDE)
    Kb = np.linspace(Kstar, KT, 60)
    ax.plot(Kb, c_fim + (cT - c_fim) * ((Kb - Kstar) / (KT - Kstar)) ** 0.75,
            color=AZUL, lw=1.7)
    ax.annotate("", xy=(Kstar + 0.6, c_fim + 0.09), xytext=(Kstar + 1.6, c_fim + 0.16),
                arrowprops=dict(arrowstyle="->", lw=1.4, color=AZUL))
    ax.text(9.0, 1.62, r"3. de $T$ em diante," "\n" r"o \emph{saddle path} de $e=0$",
            fontsize=7, color=AZUL)
    ax.plot([KT], [cT], "s", color="black", ms=4.5, zorder=7)
    ax.annotate(r"$T$", xy=(KT, cT), xytext=(KT + 0.35, cT + 0.06), fontsize=8)
    ax.set_title(r"(ii) O petr\'oleo vira capital, e depois se gasta", fontsize=8.5)

    for ax in axes:
        ax.set_xlim(0, 14); ax.set_ylim(0, 2.6)
        ax.set_xlabel(r"capital $K$"); ax.set_ylabel(r"consumo $c$")
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle(r"9.9 --- economia com petr\'oleo: $F(K,L)=K^{\alpha}L^{1-\alpha}+e$",
                 fontsize=9, y=1.02)
    salvar(fig, "fig_k9_9_fase.pdf")


# ===================================================== 9.12
def fig_consumo():
    s = iy_ss(A, B, D)
    from ch09_numerico import c0 as c0_shoot
    Kf, cf, If, Yf = caminho_fixo(s)
    Ko, co = caminho_otimo(c0_shoot)
    t = np.arange(T)

    fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH_IN, TEXTWIDTH_IN * 0.40))
    ax = axes[0]
    ax.plot(t, cf, color=VERM, lw=1.6, ls="--", label=r"poupan\c{c}a fixa, $s=0{,}2413$")
    ax.plot(t, co[:T], color=AZUL, lw=1.6, label=r"poupan\c{c}a \'otima")
    ax.axhline(K_ss(A, B, D) ** A - D * K_ss(A, B, D), color=CINZA, lw=0.8,
               ls=(0, (1, 2)))
    ax.annotate(r"a \'otima come\c{c}a \textbf{abaixo}:" "\n"
                r"com $K_0$ baixo o retorno \'e alto," "\n" r"vale a pena investir mais",
                xy=(3, 0.95), xytext=(22, 0.80), fontsize=7, color=AZUL,
                arrowprops=dict(arrowstyle="->", lw=0.6, color=AZUL))
    ax.set_xlabel(r"ano"); ax.set_ylabel(r"consumo $c_t$")
    ax.set_title(r"(i) As duas trajet\'orias de consumo", fontsize=8.5)
    ax.legend(loc="lower right", frameon=False, fontsize=7.5)

    ax = axes[1]
    ax.plot(t, Kf[:T], color=VERM, lw=1.6, ls="--")
    ax.plot(t, Ko[:T], color=AZUL, lw=1.6)
    ax.axhline(K_ss(A, B, D), color=CINZA, lw=0.8, ls=(0, (1, 2)))
    ax.annotate(r"$K_{ss}=%.2f$" % K_ss(A, B, D), xy=(95, K_ss(A, B, D)),
                xytext=(70, 4.6), fontsize=7.5,
                arrowprops=dict(arrowstyle="->", lw=0.6, color=CINZA))
    ax.set_xlabel(r"ano"); ax.set_ylabel(r"capital $K_t$")
    ax.set_title(r"(ii) O mesmo destino, caminhos diferentes", fontsize=8.5)

    for ax in axes:
        ax.set_xlim(0, T); ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle(r"9.12 --- $\alpha=0{,}4$, $\beta=0{,}95$, $\delta=0{,}08$, "
                 r"$\sigma=2$, $K_0=2$", fontsize=9, y=1.03)
    salvar(fig, "fig_k9_12_consumo.pdf")


if __name__ == "__main__":
    fig_ces()
    fig_fase()
    fig_consumo()
