"""Lista 1, Questao 3 -- os tres diagramas de dispersao pedidos (mais o mundo)."""
import estilo_mpl  # noqa: F401  (backend pgf; ver docstring)
import numpy as np
import matplotlib.pyplot as plt
from q3_convergencia import montar_painel, regressao, REGIOES

w = montar_painel()

# nomes de exibicao acentuados (as chaves do dicionario ficam em ASCII)
TITULO = {"Europa": "Europa", "America Latina": "América Latina",
          "Africa": "África", "Mundo": "Mundo (todos os países)"}

# paises anotados e deslocamento do rotulo, em pontos, para nao cair sobre a reta
DESTAQUE = {
    "Europa":         {"IRL": (4, 4), "PRT": (-16, -10), "CHE": (4, -8), "ROU": (4, 4)},
    "America Latina": {"BRA": (4, 4), "ARG": (4, -10), "VEN": (4, -10), "PAN": (4, 4)},
    "Africa":         {"BWA": (5, -2), "COD": (5, 0), "ZAF": (5, 0), "GNQ": (5, -2)},
}

# 2x2 (e nao 1x4) para que a figura caiba na largura do texto em escala 1:1 --
# quatro paineis lado a lado precisariam ser reduzidos a 40% e o texto sumiria.
paineis = list(REGIOES.items()) + [("Mundo", None)]
fig, axes = plt.subplots(2, 2, figsize=(estilo_mpl.TEXTWIDTH_IN, 5.4), sharey=True)
axes = axes.ravel()

for ax, (nome, membros) in zip(axes, paineis):
    sub = w if membros is None else w[w.countrycode.isin(membros)]
    r = regressao(sub)
    ax.scatter(sub.ly60, 100 * sub.g, s=22, color="#1E64B4",
               alpha=.75, edgecolor="white", linewidth=.5)
    xs = np.linspace(sub.ly60.min(), sub.ly60.max(), 20)
    ax.plot(xs, 100 * (r["intercepto"] + r["inclinacao"] * xs),
            color="#B3243C", lw=1.6)
    ax.axhline(0, color="0.8", lw=0.7)
    ax.set_title(f"{TITULO[nome]}\n"
                 f"$n={r['n']}$,  incl.\\ $={100*r['inclinacao']:+.3f}$ p.p. "
                 f"($t={r['t']:+.2f}$),  $R^2={r['r2']:.2f}$", fontsize=9)
    ax.set_xlabel("$\\ln$ PIB per capita em 1960 (PPC)")
    for c, deslok in DESTAQUE.get(nome, {}).items():
        p = sub[sub.countrycode == c]
        if len(p):
            ax.annotate(c, (p.ly60.iloc[0], 100 * p.g.iloc[0]), fontsize=7,
                        xytext=deslok, textcoords="offset points")
    ax.spines[["top", "right"]].set_visible(False)

for a in (axes[0], axes[2]):
    a.set_ylabel("cresc.\\ médio de $y$, 1960--2014 (\\% a.a.)")
fig.tight_layout()
fig.savefig("fig_q3_convergencia.pdf", bbox_inches="tight")
print("figura salva: fig_q3_convergencia.pdf")
