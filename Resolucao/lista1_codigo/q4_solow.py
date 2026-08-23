"""Lista 1, Questao 4 -- terremoto no modelo de Solow (sem progresso tecnologico).

Cenario (a): em t0 metade do estoque de capital e destruida.  s, n, delta iguais.
Cenario (b): alem disso, a taxa de crescimento populacional cai de n para n/2.

Calibracao ilustrativa: Cobb-Douglas alpha=1/3, s=0.20, delta=0.05, n=0.02.
Tempo discreto:  k_{t+1} = [(1-delta) k_t + s f(k_t)] / (1+n).
"""
import estilo_mpl  # noqa: F401  (backend pgf; ver docstring)
import numpy as np
import matplotlib.pyplot as plt

ALPHA, S, DELTA, N = 1/3, 0.20, 0.05, 0.02
T0, T = 20, 220                      # terremoto em t0=20; horizonte de 220 anos

f = lambda k: k ** ALPHA


def k_estrela(n=N, s=S, delta=DELTA, alpha=ALPHA):
    return (s / (n + delta)) ** (1 / (1 - alpha))


def simular(n_pos, destruir=True, k0=None, T=T, t0=T0):
    """Devolve (k, y, L, Y). n_pos = crescimento populacional apos t0."""
    k = np.empty(T + 1)
    L = np.empty(T + 1)
    k[0], L[0] = (k0 if k0 is not None else k_estrela()), 1.0
    for t in range(T):
        n_t = N if t < t0 else n_pos
        k_ini = k[t] * (0.5 if (destruir and t == t0) else 1.0)
        if destruir and t == t0:
            k[t] = k_ini                     # o choque atinge o inicio do periodo t0
        k[t + 1] = ((1 - DELTA) * k[t] + S * f(k[t])) / (1 + n_t)
        L[t + 1] = L[t] * (1 + n_t)
    y = f(k)
    return k, y, L, y * L


# ------------------------------------------------------------------ cenarios
kc, yc, Lc, Yc = simular(N, destruir=False)          # contrafactual: nada acontece
ka, ya, La, Ya = simular(N, destruir=True)           # (a) so o terremoto
kb, yb, Lb, Yb = simular(N / 2, destruir=True)       # (b) terremoto + n -> n/2

ks, kss = k_estrela(N), k_estrela(N / 2)
print(f"k*  (n={N})     = {ks:.4f}      y*  = {f(ks):.4f}")
print(f"k** (n={N/2})   = {kss:.4f}      y** = {f(kss):.4f}")
print(f"y**/y* = {f(kss)/f(ks):.4f}  (analitico: "
      f"{((N+DELTA)/(N/2+DELTA))**(ALPHA/(1-ALPHA)):.4f})  -> "
      f"{100*(f(kss)/f(ks)-1):+.2f}% de nivel permanente")

# ---------------------------------------------------------------- no impacto
queda = 2 ** (-ALPHA) - 1
print(f"\nQueda instantanea de y (e de Y) no impacto: {100*queda:+.2f}% "
      f"(= 2^-alpha - 1); simulado: {100*(ya[T0]/yc[T0]-1):+.2f}%")

# crescimento de k logo apos o choque (tempo continuo, para leitura analitica)
g_k = (N + DELTA) * (2 ** (1 - ALPHA) - 1)
print(f"Crescimento de k logo apos o choque, cenario (a): "
      f"(n+delta)(2^(1-alpha)-1) = {100*g_k:.2f}% a.a.  -> g_y = alpha*g_k = "
      f"{100*ALPHA*g_k:.2f}% a.a.")
g_k_b = (N/2 + DELTA) * ((kss / (ks/2)) ** (1 - ALPHA) - 1)
print(f"Crescimento de k logo apos o choque, cenario (b): {100*g_k_b:.2f}% a.a. "
      f"-> g_y = {100*ALPHA*g_k_b:.2f}% a.a.  (mais rapido: alvo mais distante)")

# --------------------------------------------------- tempo de recuperacao (a)
hiato = np.log(f(ks)) - np.log(ya[T0:])
for frac in (0.5, 0.9, 0.99):
    idx = np.argmax(hiato <= (1 - frac) * hiato[0])
    print(f"Cenario (a): {100*frac:.0f}% do hiato de y fechado em {idx} anos")

# em (b) y ultrapassa o nivel antigo y*
cruza = T0 + np.argmax(yb[T0:] >= f(ks))
print(f"Cenario (b): y volta ao y* antigo em t0+{cruza-T0} anos e segue subindo ate y**")

# --------------------------------------------- PIB agregado: efeito permanente
print(f"\nPIB agregado no fim do horizonte (t={T}), relativo ao contrafactual:")
print(f"  (a) Y/Y_contrafactual = {Ya[T]/Yc[T]:.4f}   -> volta a trajetoria original")
print(f"  (b) Y/Y_contrafactual = {Yb[T]/Yc[T]:.4f}   -> cai indefinidamente "
      f"(L cresce a n/2 < n)")
print(f"  (b) y/y_contrafactual = {yb[T]/yc[T]:.4f}   -> permanentemente MAIOR")

# ------------------------------------------------------------------- graficos
t = np.arange(T + 1)
fig, ax = plt.subplots(1, 3, figsize=(estilo_mpl.TEXTWIDTH_IN, 2.5))
cinza, azul, verm = "0.45", "#1E64B4", "#B3243C"

for a in ax:
    a.axvline(T0, color="0.8", lw=0.8, ls="--")
    a.set_xlabel("$t$", labelpad=1)
    a.set_xlim(0, T)

ax[0].plot(t, kc, color=cinza, lw=1.2, ls=":", label="sem terremoto")
ax[0].plot(t, ka, color=azul, lw=1.6, label="(a) terremoto")
ax[0].plot(t, kb, color=verm, lw=1.6, label="(b) terremoto + $n/2$")
ax[0].axhline(kss, color=verm, lw=0.7, ls="--")
ax[0].set_title("Capital por trabalhador $k_t$")

ax[1].plot(t, np.log(yc), color=cinza, lw=1.2, ls=":", label="sem terremoto")
ax[1].plot(t, np.log(ya), color=azul, lw=1.6, label="(a) terremoto")
ax[1].plot(t, np.log(yb), color=verm, lw=1.6, label="(b) terremoto + $n/2$")
ax[1].set_title(r"PIB per capita, $\ln y_t$")

ax[2].plot(t, np.log(Yc), color=cinza, lw=1.2, ls=":", label="sem terremoto")
ax[2].plot(t, np.log(Ya), color=azul, lw=1.6, label="(a) terremoto")
ax[2].plot(t, np.log(Yb), color=verm, lw=1.6, label="(b) terremoto + $n/2$")
ax[2].set_title(r"PIB agregado, $\ln Y_t$")

ax[0].legend(fontsize=6.5, loc="lower right", frameon=False)
for a in ax:
    a.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("fig_q4_trajetorias.pdf", bbox_inches="tight")   # vetorial
print("\nfigura salva: fig_q4_trajetorias.pdf")
