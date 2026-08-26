"""Figuras da Lista 3. Gera os PDFs em Resolucao/fig/.

Calibracao de referencia: beta = 0,96, r = 0,50, sigma = 2. Com ela
Omega = sqrt(beta/(1+r)) = 0,8 e [beta(1+r)]^(1/sigma) = 1,2 exatos.

Backend pgf (ver estilo_mpl): o texto das figuras e composto pelo pdflatex com
lmodern + cmap, entao o PDF final continua 100% copiavel.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import estilo_mpl                                       # noqa: F401  (antes do pyplot)
from estilo_mpl import TEXTWIDTH_IN
import numpy as np
import matplotlib.pyplot as plt
from modelo import (solucao, solucao_restrita, solucao_imposto_poupanca,
                    solucao_lump_sum, theta, bem_estar, u)

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "fig"))
os.makedirs(RAIZ, exist_ok=True)

BETA, R, SIGMA = 0.96, 0.50, 2.0
AZUL, ROXO, VERM, CINZA = "#0F3773", "#5B2D8E", "#B4272B", "#7A7A7A"
VERDE = "#1B6E3C"


def salvar(fig, nome):
    caminho = os.path.join(RAIZ, nome + ".pdf")
    fig.savefig(caminho, bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)
    print("  gravado:", caminho)


def curva_indiferenca(Ubar, c1grid, beta=BETA, sigma=SIGMA):
    """c2 tal que u(c1) + beta u(c2) = Ubar, elemento a elemento."""
    alvo = (Ubar - u(c1grid, sigma)) / beta
    if np.isclose(sigma, 1.0):
        return np.exp(alvo)
    with np.errstate(invalid="ignore"):
        base = alvo * (1.0 - sigma)
        return np.where(base > 0, np.abs(base) ** (1.0 / (1.0 - sigma)), np.nan)


# ==================================================================== FIGURA 1
# Item 1(c): sigma decide o sinal de dc1/dr.
def fig_sigma():
    a0, y1 = 10.0, 100.0
    W, r2 = a0 + y1, 1.20
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(TEXTWIDTH_IN, 3.6))

    # -- painel esquerdo: a reta gira em torno de (W, 0)
    for rr, cor in [(R, AZUL), (r2, ROXO)]:
        c1 = np.linspace(0.01, W, 300)
        ax1.plot(c1, (W - c1) * (1 + rr), color=cor, lw=1.6,
                 label=rf"$1+r={1+rr:.2f}$")
    for s, mk, cor in [(0.5, "o", VERM), (1.0, "s", VERDE), (2.0, "^", CINZA)]:
        xs, ys = zip(*[solucao(a0, y1, 0.0, rr, BETA, s)[:2] for rr in (R, r2)])
        ax1.plot(xs, ys, ":", color=cor, lw=1.0)
        ax1.annotate("", xy=(xs[1], ys[1]), xytext=(xs[0], ys[0]),
                     arrowprops=dict(arrowstyle="-|>", color=cor, lw=1.2))
        ax1.plot(xs, ys, mk, color=cor, ms=5.5,
                 label=rf"$\sigma={s:g}$" + (" (log)" if s == 1 else ""))
    c1log = solucao(a0, y1, 0.0, R, BETA, 1.0)[0]
    ax1.axvline(c1log, color=VERDE, lw=0.7, ls="--", alpha=0.7)
    ax1.text(c1log - 2, 232, r"$\sigma=1$: fica parado", color=VERDE,
             fontsize=7, rotation=90, va="top", ha="right")
    ax1.set_xlim(0, W * 1.02)
    ax1.set_ylim(0, 250)
    ax1.set_xlabel(r"$c_1$")
    ax1.set_ylabel(r"$c_2$")
    ax1.set_title(r"A reta gira em torno de $(W,0)$;" "\n"
                  r"para onde o ponto anda depende de $\sigma$"
                  r"\quad{\footnotesize$(y_2=\tau_1=\tau_2=0)$}")
    ax1.legend(fontsize=7, loc="upper right", framealpha=0.95)

    # -- painel direito: a derivada como funcao de sigma
    sg = np.linspace(0.15, 5.0, 600)
    om = BETA ** (1 / sg) * (1 + R) ** (1 / sg - 1)
    dc = (W / (1 + om)) / (1 + R) * om / (1 + om) * (sg - 1) / sg
    ax2.axhline(0, color="k", lw=0.7)
    ax2.axvline(1, color=VERDE, lw=1.0, ls="--")
    ax2.plot(sg, dc, color=AZUL, lw=1.9)
    ax2.fill_between(sg, dc, 0, where=(sg < 1), color=VERM, alpha=0.13)
    ax2.fill_between(sg, dc, 0, where=(sg > 1), color=CINZA, alpha=0.18)
    ax2.set_ylim(-42, 22)
    ax2.set_xlim(0.15, 5.0)
    ax2.text(0.62, -30, "substituição domina\n" r"$\partial c_1/\partial r<0$",
             color=VERM, fontsize=7.5, ha="left", va="center")
    ax2.text(3.9, 6.0, "renda domina\n" r"$\partial c_1/\partial r>0$",
             color="#3C3C3C", fontsize=7.5, ha="center", va="center")
    ax2.annotate(r"$\sigma=1$ (log): empate exato", xy=(1.0, 0.0),
                 xytext=(1.9, 16.5), fontsize=7.5, color=VERDE,
                 arrowprops=dict(arrowstyle="->", color=VERDE, lw=0.9))
    ax2.set_xlabel(r"$\sigma$ \quad{\footnotesize(EIS $=1/\sigma$)}")
    ax2.set_ylabel(r"$\partial c_1/\partial r$")
    ax2.set_title(r"$\dfrac{\partial c_1}{\partial r}"
                  r"=\dfrac{c_1}{1+r}\,\dfrac{\Omega}{1+\Omega}\,"
                  r"\dfrac{\sigma-1}{\sigma}$" "\n"
                  r"{\footnotesize o sinal é o de $\sigma-1$, e nada mais}")
    fig.tight_layout()
    salvar(fig, "fig_l3q1_sigma")


# ==================================================================== FIGURA 2
# Item 1(e): a reta nao se mexe; so a dotacao desliza sobre ela.
def fig_ricardo():
    a0, y1, y2, t1, t2 = 10.0, 100.0, 69.0, 6.0, 9.0
    D = 20.0                       # deslocamento ampliado, so para enxergar
    W = a0 + (y1 - t1) + (y2 - t2) / (1 + R)
    c1s, c2s, a = solucao(a0, y1, y2, R, BETA, SIGMA, t1, t2)
    ab = solucao(a0, y1, y2, R, BETA, SIGMA, t1 - D, t2 + D * (1 + R))[2]

    fig, ax = plt.subplots(figsize=(TEXTWIDTH_IN * 0.66, 3.7))
    c1 = np.linspace(0.01, W, 300)
    ax.plot(c1, (W - c1) * (1 + R), color=AZUL, lw=2.2,
            label=r"$c_1+\frac{c_2}{1+r}=W=144$ \ (a MESMA reta nos dois regimes)")
    Ub = bem_estar(c1s, c2s, BETA, SIGMA)
    cg = np.linspace(45, 135, 400)
    ax.plot(cg, curva_indiferenca(Ub, cg), color=VERDE, lw=1.0, ls="--",
            alpha=0.85, label=r"curva de indiferença ótima (também a mesma)")
    d1a, d2a = a0 + y1 - t1, y2 - t2
    d1b, d2b = a0 + y1 - (t1 - D), y2 - (t2 + D * (1 + R))
    ax.annotate("", xy=(d1b, d2b), xytext=(d1a, d2a),
                arrowprops=dict(arrowstyle="-|>", color=VERM, lw=1.6))
    ax.plot(d1a, d2a, "o", color=ROXO, ms=8, mfc="white", mew=1.8,
            label=rf"dotação antes: $({d1a:.0f},\,{d2a:.0f})$")
    ax.plot(d1b, d2b, "s", color=VERM, ms=8, mfc="white", mew=1.8,
            label=rf"dotação depois: $({d1b:.0f},\,{d2b:.0f})$")
    ax.plot(c1s, c2s, "*", color=VERDE, ms=17,
            label=rf"escolha $({c1s:.0f},\,{c2s:.0f})$ --- \textbf{{inalterada}}")
    ax.annotate(r"a dotação desliza \emph{sobre} a reta:" "\n"
                r"$\Delta\tau_1=-20$, $\Delta\tau_2=+30=20(1+r)$" "\n"
                r"$\Rightarrow$ poupança privada $+20$; $W$ intacto",
                xy=((d1a + d1b) / 2, (d2a + d2b) / 2 + 3), xytext=(20, 22),
                fontsize=7.2, color=VERM,
                arrowprops=dict(arrowstyle="->", color=VERM, lw=0.9))
    ax.text(0.985, 0.30, rf"por unidade de corte: $a:\ {a:.0f}\rightarrow{a+1:.0f}$",
            transform=ax.transAxes, fontsize=7, color=AZUL, ha="right")
    ax.set_xlim(10, 150)
    ax.set_ylim(0, 230)
    ax.set_xlabel(r"$c_1$")
    ax.set_ylabel(r"$c_2$")
    ax.set_title("Equivalência ricardiana: a dotação anda,\n a reta e a escolha não")
    ax.legend(fontsize=6.6, loc="upper right", framealpha=0.96)
    fig.tight_layout()
    salvar(fig, "fig_l3q1_ricardo")


# ==================================================================== FIGURA 3
# Item 2(c): o conjunto factivel truncado e os dois regimes.
def fig_restricao():
    b = 10.0
    fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH_IN, 3.9))
    casos = [("Restrição FOLGADA \\ {\\footnotesize(poupador)}", 100.0, 66.0),
             ("Restrição ATIVA \\ {\\footnotesize(jovem)}", 20.0, 132.0)]
    for ax, (titulo, y1, y2) in zip(axes, casos):
        W = y1 + y2 / (1 + R)
        cmax = y1 + b
        c1 = np.linspace(0.01, W, 500)
        c2 = (W - c1) * (1 + R)
        ax.plot(c1, c2, color=CINZA, lw=1.0, ls=":",
                label=r"reta orçamentária sem a restrição")
        viavel = c1 <= cmax
        ax.plot(c1[viavel], c2[viavel], color=AZUL, lw=2.4,
                label=r"fronteira factível com $a\ge-b$")
        ax.axvline(cmax, color=VERM, lw=1.5, ls="--")
        ax.fill_betweenx([0, max(0.0, (W - cmax) * (1 + R))], cmax, W,
                         color=VERM, alpha=0.10)
        ax.text(cmax + 2, W * (1 + R) * 0.955,
                rf"$c_1\le y_1-\tau_1+b={cmax:.0f}$", color=VERM,
                fontsize=7.2, ha="left", va="top")
        ax.plot(y1, y2, "P", color=ROXO, ms=7,
                label=rf"dotação $({y1:.0f},{y2:.0f})$, $a=0$")

        cu, c2u, _ = solucao(0, y1, y2, R, BETA, SIGMA)
        c1r, c2r, ar, ativa, phi = solucao_restrita(y1, y2, R, BETA, SIGMA, b)
        if ativa:
            ax.plot(cu, c2u, "x", color=CINZA, ms=9, mew=1.8,
                    label=rf"desejo irrestrito $c_1^u={cu:.0f}$ (inviável)")
        ax.plot(c1r, c2r, "*", color=VERDE, ms=16,
                label=rf"escolha $({c1r:.0f},\,{c2r:.0f})$, $a={ar:.0f}$")
        Ub = bem_estar(c1r, c2r, BETA, SIGMA)
        cg = np.linspace(max(1.0, c1r * 0.45), min(W * 0.99, c1r * 2.6), 500)
        ax.plot(cg, curva_indiferenca(Ub, cg), color=VERDE, lw=1.0, ls="--",
                alpha=0.85)
        sub = (rf"$\phi>0$;\ \ $c_2/c_1={c2r/c1r:.2f}<"
               rf"[\beta(1+r)]^{{1/\sigma}}=1{{,}}20$" if ativa else
               rf"$\phi=0$;\ \ $c_2/c_1=[\beta(1+r)]^{{1/\sigma}}=1{{,}}20$")
        ax.set_title(titulo + "\n" + r"{\footnotesize " + sub + "}")
        ax.set_xlim(0, W * 1.02)
        ax.set_ylim(0, W * (1 + R) * 1.03)
        ax.set_xlabel(r"$c_1$")
        ax.set_ylabel(r"$c_2$")
        ax.legend(fontsize=6.4, loc="lower left", framealpha=0.96)
    fig.tight_layout()
    salvar(fig, "fig_l3q2_restricao")


# ==================================================================== FIGURA 4
# Item 2(d): girar (imposto sobre poupanca) x transladar (lump-sum).
def fig_imposto():
    y1, y2, tau = 100.0, 66.0, 0.20
    c1S, c2S, aS, Rtil = solucao_imposto_poupanca(y1, y2, R, BETA, SIGMA, tau)
    T = tau * aS
    c1L, c2L, aL = solucao_lump_sum(y1, y2, R, BETA, SIGMA, T)
    c10, c20, _ = solucao(0, y1, y2, R, BETA, SIGMA)

    fig, ax = plt.subplots(figsize=(TEXTWIDTH_IN * 0.68, 4.1))
    c1 = np.linspace(70, 101, 300)
    ax.plot(c1, y2 + (1 + R) * (y1 - c1), color=CINZA, lw=1.3, ls=":",
            label=r"sem imposto: inclinação $-(1+r)=-1{,}5$")
    ax.plot(c1, y2 - T + (1 + R) * (y1 - c1), color=AZUL, lw=2.0,
            label=rf"lump-sum $T={T:.2f}$: \textbf{{translação}} paralela")
    ax.plot(c1, y2 + Rtil * (y1 - c1), color=VERM, lw=2.0,
            label=r"imposto s/ poupança: \textbf{rotação}, $-(1+r-\tau_2)=-1{,}3$")
    for x, y, cor, mk, lab in [
            (c10, c20, CINZA, "o", rf"sem imposto: $c_2/c_1={c20/c10:.3f}$"),
            (c1L, c2L, AZUL, "s", rf"lump-sum: $c_2/c_1={c2L/c1L:.3f}$"),
            (c1S, c2S, VERM, "^", rf"imposto s/ poup.: $c_2/c_1={c2S/c1S:.3f}$")]:
        ax.plot(x, y, mk, color=cor, ms=8, label=lab)
    for x, y, cor in [(c1L, c2L, AZUL), (c1S, c2S, VERM)]:
        cg = np.linspace(74, 101, 500)
        ax.plot(cg, curva_indiferenca(bem_estar(x, y, BETA, SIGMA), cg),
                color=cor, lw=0.9, ls="--", alpha=0.8)
    ax.plot(y1, y2, "P", color=ROXO, ms=8,
            label=r"dotação $(y_1,y_2)$: eixo da rotação")
    ax.annotate(r"o ponto vermelho está \emph{sobre} a reta azul:" "\n"
                r"era factível com o lump-sum e não foi escolhido" "\n"
                r"$\Rightarrow$ peso morto de $7{,}1\%$ da receita",
                xy=(c1S, c2S), xytext=(85.2, 96.5), fontsize=7,
                arrowprops=dict(arrowstyle="->", color="k", lw=0.9))
    ax.set_xlim(73.5, 102.5)
    ax.set_ylim(56, 104)
    ax.set_xlabel(r"$c_1$")
    ax.set_ylabel(r"$c_2$")
    ax.set_title("Mesma receita, margens diferentes: o lump-sum\n"
                 "translada; o imposto sobre a poupança gira")
    ax.legend(fontsize=6.4, loc="lower left", framealpha=0.96)
    fig.tight_layout()
    salvar(fig, "fig_l3q2_imposto")


if __name__ == "__main__":
    fig_sigma()
    fig_ricardo()
    fig_restricao()
    fig_imposto()
    print("  ok - 4 figuras geradas.")
