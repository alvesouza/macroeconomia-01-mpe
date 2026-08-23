"""Figuras da Lista 2. Gera tres PDFs vetoriais no tamanho exato do texto."""
import estilo_mpl  # noqa: F401  (backend pgf -> texto em Type 1)
import numpy as np
import matplotlib.pyplot as plt

from l2q1_coreia import (PAIS, DELTA, k_estrela, y_de_k, trajetoria, passo)

W = estilo_mpl.TEXTWIDTH_IN
AZUL, VERM, CINZA, VERDE = "#1E64B4", "#B3243C", "0.45", "#1B7A4B"

# ======================================================= fig 1: diagrama de Solow
fig, axes = plt.subplots(1, 2, figsize=(W, 2.7))
for ax, nome in zip(axes, ("Norte", "Sul")):
    p = PAIS[nome]
    a, A, s, n = p["alpha"], p["A"], p["s"], p["n"]
    ks = k_estrela(s, A, a, n)
    k0 = p["K0"] / p["L0"]
    kmax = 1.55 * ks
    k = np.linspace(1e-6, kmax, 500)
    ax.plot(k, s * A * k ** a, color=AZUL, lw=1.5,
            label=rf"$s_{{{nome[0]}}}A_{{{nome[0]}}}k^{{\alpha}}$")
    ax.plot(k, (n + DELTA) * k, color=VERM, lw=1.5,
            label=rf"$(n_{{{nome[0]}}}+\delta)k$")
    ax.axvline(ks, color=CINZA, lw=0.7, ls=":")
    ax.axvline(k0, color=VERDE, lw=0.9, ls="--")
    ax.annotate("", xy=(k0 + 0.16 * (ks - k0), 0.055 * s * A * ks ** a),
                xytext=(k0, 0.055 * s * A * ks ** a),
                arrowprops=dict(arrowstyle="-|>", color=VERDE, lw=1.1))
    ax.set_xlim(0, kmax)
    ax.set_ylim(0, 1.28 * s * A * ks ** a)
    ax.set_xticks([k0, ks])
    ax.set_xticklabels([rf"$k_0={k0:g}$", rf"$k^*={ks:g}$"])
    ax.set_yticks([])
    ax.set_xlabel("$k$")
    ax.set_title(rf"Coreia do {nome}: $\alpha={a}$, $A={A}$, $s={s}$, $n={n}$",
                 fontsize=8.5)
    ax.legend(frameon=False, fontsize=7.5, loc="upper left")
    ax.spines[["top", "right"]].set_visible(False)
axes[0].set_ylabel("por trabalhador")
fig.tight_layout()
fig.savefig("fig_l2q1_solow.pdf", bbox_inches="tight")
print("fig_l2q1_solow.pdf")

# ================================================== fig 2: trajetorias de y
T = 160
aS, AS, sS = PAIS["Sul"]["alpha"], PAIS["Sul"]["A"], PAIS["Sul"]["s"]
n_U = (PAIS["Norte"]["L0"] * PAIS["Norte"]["n"]
       + PAIS["Sul"]["L0"] * PAIS["Sul"]["n"]) / (PAIS["Norte"]["L0"] + PAIS["Sul"]["L0"])

kN = trajetoria(10.0, PAIS["Norte"]["s"], PAIS["Norte"]["A"],
                PAIS["Norte"]["alpha"], PAIS["Norte"]["n"], T=T)
kS = trajetoria(400.0, sS, AS, aS, PAIS["Sul"]["n"], T=T)
kU = trajetoria(270.0, sS, AS, aS, n_U, T=T)

yN = y_de_k(kN, PAIS["Norte"]["A"], PAIS["Norte"]["alpha"])
yS = y_de_k(kS, AS, aS)
yU = y_de_k(kU, AS, aS)

t = np.arange(T + 1)
fig, ax = plt.subplots(figsize=(W, 3.0))
# y* vai no rotulo da legenda: as tres retas ficam a menos de 5% da altura do eixo
# em escala log, e rotulos na borda direita se sobrepoem.
ax.plot(t, yS, color=AZUL, lw=1.6,
        label=r"Sul, sem unificação \quad($y^*_S = 125$)")
ax.plot(t, yU, color=VERDE, lw=1.8,
        label=r"Coreia unificada, de $k_U=270$ \quad($y^*_U = 112{,}5$)")
ax.plot(t, yN, color=VERM, lw=1.6,
        label=r"Norte, sem unificação \quad($y^*_N = 8$)")
for val, cor in [(125, AZUL), (112.5, VERDE), (8, VERM)]:
    ax.axhline(val, color=cor, lw=0.7, ls=":")
ax.set_yscale("log")
ax.set_yticks([8, 10, 20, 50, 100, 125])
ax.set_yticklabels(["8", "10", "20", "50", "100", "125"])
ax.set_ylim(6.4, 200)
ax.set_xlim(0, T)
ax.set_xlabel("$t$ (períodos após a unificação)")
ax.set_ylabel("PIB per capita $y$ (escala log)")
ax.legend(frameon=False, fontsize=7.5, loc="center right")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("fig_l2q1_trajetorias.pdf", bbox_inches="tight")
print("fig_l2q1_trajetorias.pdf")

# =============================================== fig 3: Gotham, crime e PTF medida
ALPHA = 1 / 3
th = np.linspace(0, 1.2, 400)
fig, axes = plt.subplots(1, 2, figsize=(W, 2.5))

axes[0].plot(th, 100 * th / (1 + th), color=VERM, lw=1.6)
axes[0].set_ylabel(r"\% do capital medido")
axes[0].set_title(r"Capital em segurança: $\theta/(1+\theta)$", fontsize=8.5)

axes[1].plot(th, (1 + th) ** (-ALPHA), color=AZUL, lw=1.6)
axes[1].set_ylabel(r"$\hat{A}/A = Y/Y_{\theta=0}$")
axes[1].set_title(r"PTF medida e produto: $(1+\theta)^{-\alpha}$", fontsize=8.5)

# deslocamentos por painel: no da esquerda a curva sobe rapido perto de theta',
# e um rotulo acima/a direita cairia sobre ela.
PAINEIS = [
    (lambda x: 100 * x / (1 + x), {0.5: (8, -12), 0.125: (10, -10)}),
    (lambda x: (1 + x) ** (-ALPHA), {0.5: (6, 6), 0.125: (6, 6)}),
]
for ax, (f, deslok) in zip(axes, PAINEIS):
    for tv, cor, lab in [(0.5, VERM, r"$\theta=0{,}5$"),
                         (0.125, VERDE, r"$\theta'=0{,}125$")]:
        ax.plot([tv], [f(tv)], "o", ms=4, color=cor, zorder=5)
        ax.annotate(lab, (tv, f(tv)), fontsize=7, color=cor,
                    xytext=deslok[tv], textcoords="offset points")
    ax.set_xlabel(r"$\theta$ (unidades de segurança por unidade produtiva)")
    ax.set_xlim(0, 1.2)
    ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("fig_l2q2_crime.pdf", bbox_inches="tight")
print("fig_l2q2_crime.pdf")
