"""Lista 2, Questao 1 -- Coreia do Norte e do Sul no modelo de Solow.

Y_i = A_i K^{alpha_i} L^{1-alpha_i};  k_{i,t+1} = [(1-d)k + s_i A_i k^{a_i}]/(1+n_i)

Todos os numeros do gabarito saem daqui. Onde ha forma fechada, o valor analitico
e comparado com a simulacao / com Fraction exata.
"""
from fractions import Fraction as F
import numpy as np

DELTA = 0.05

PAIS = {
    "Norte": dict(L0=10, K0=100,  alpha=0.25, A=4, s=0.16, n=0.03),
    "Sul":   dict(L0=20, K0=8000, alpha=0.50, A=5, s=0.30, n=0.01),
}


def y_de_k(k, A, alpha):
    """Produto por trabalhador: y = A k^alpha."""
    return A * k ** alpha


def k_estrela(s, A, alpha, n, delta=DELTA):
    """k* resolve k(n+delta) = s A k^alpha  =>  k* = [sA/(n+delta)]^{1/(1-alpha)}."""
    return (s * A / (n + delta)) ** (1 / (1 - alpha))


def passo(k, s, A, alpha, n, delta=DELTA):
    return ((1 - delta) * k + s * A * k ** alpha) / (1 + n)


def trajetoria(k0, s, A, alpha, n, T=400, delta=DELTA):
    k = np.empty(T + 1)
    k[0] = k0
    for t in range(T):
        k[t + 1] = passo(k[t], s, A, alpha, n, delta)
    return k


def relatorio():
    """Imprime todos os numeros do gabarito. Nada roda na importacao."""
    # ============================================================== (a) periodo 0
    print("=" * 70)
    print("(a) capital por trabalhador e PIB per capita em t = 0")
    print("=" * 70)
    base = {}
    for nome, p in PAIS.items():
        k0 = F(p["K0"], p["L0"])                     # exato
        y0 = y_de_k(float(k0), p["A"], p["alpha"])
        Y0 = y0 * p["L0"]
        base[nome] = dict(k0=float(k0), y0=y0, Y0=Y0)
        print(f"  {nome:6s}: k_0 = {p['K0']}/{p['L0']} = {k0} = {float(k0):g}"
              f" | y_0 = {p['A']}*{float(k0):g}^{p['alpha']} = {y0:.6f}"
              f" | Y_0 = {Y0:.4f}")
    r = base["Sul"]["y0"] / base["Norte"]["y0"]
    print(f"  razao y_Sul/y_Norte = {r:.4f}x")

    # ============================================================== (b) estado estacionario
    print()
    print("=" * 70)
    print("(b) estado estacionario")
    print("=" * 70)
    ss = {}
    for nome, p in PAIS.items():
        ks = k_estrela(p["s"], p["A"], p["alpha"], p["n"])
        ys = y_de_k(ks, p["A"], p["alpha"])
        # verificacao 1: k* e ponto fixo da lei de movimento
        fixo = passo(ks, p["s"], p["A"], p["alpha"], p["n"])
        # verificacao 2: investimento efetivo == reposicao
        esq, dir_ = p["s"] * p["A"] * ks ** p["alpha"], (p["n"] + DELTA) * ks
        # velocidade de convergencia (log-linearizacao): lambda = (1-alpha)(n+delta)
        lam = (1 - p["alpha"]) * (p["n"] + DELTA)
        ss[nome] = dict(ks=ks, ys=ys, lam=lam)
        print(f"  {nome:6s}: sA/(n+d) = {p['s']*p['A']}/{p['n']+DELTA:g} = "
              f"{p['s']*p['A']/(p['n']+DELTA):g}, expoente 1/(1-a) = {1/(1-p['alpha']):g}")
        print(f"          k* = {ks:.4f}   y* = {ys:.4f}")
        print(f"          [check] passo(k*) = {fixo:.10f} (= k*? {abs(fixo-ks)<1e-9})"
              f" | sAk*^a = {esq:.6f} vs (n+d)k* = {dir_:.6f}")
        print(f"          k_0/k* = {base[nome]['k0']/ks:.4f}"
              f" | y_0/y* = {base[nome]['y0']/ys:.4f}"
              f" | lambda = {100*lam:.2f}%/ano, meia-vida = {np.log(2)/lam:.1f} anos")

    print(f"  razao y*_Sul/y*_Norte = {ss['Sul']['ys']/ss['Norte']['ys']:.4f}x"
          f"  (era {r:.4f}x em t=0 -> o hiato AUMENTA)")

    # crescimento no primeiro periodo, para mostrar que ambos crescem
    print("\n  crescimento no primeiro periodo:")
    for nome, p in PAIS.items():
        k1 = passo(base[nome]["k0"], p["s"], p["A"], p["alpha"], p["n"])
        y1 = y_de_k(k1, p["A"], p["alpha"])
        print(f"    {nome:6s}: g_k = {100*(k1/base[nome]['k0']-1):.3f}%"
              f" | g_y = {100*(y1/base[nome]['y0']-1):.3f}%")

    # ============================================================== (c) unificacao
    print()
    print("=" * 70)
    print("(c) unificacao: tecnologia do Sul (alpha_S, A_S), K e L dos dois")
    print("=" * 70)
    aS, AS = PAIS["Sul"]["alpha"], PAIS["Sul"]["A"]
    K_U = PAIS["Norte"]["K0"] + PAIS["Sul"]["K0"]
    L_U = PAIS["Norte"]["L0"] + PAIS["Sul"]["L0"]
    k_U = F(K_U, L_U)
    y_U = y_de_k(float(k_U), AS, aS)
    Y_U = y_U * L_U
    print(f"  K_U = {K_U}, L_U = {L_U}, k_U = {k_U} = {float(k_U):g}")
    print(f"  y_U = {AS}*{float(k_U):g}^{aS} = {y_U:.6f}")
    print(f"  Y_U = {Y_U:.4f}   [check via A K^a L^(1-a) = "
          f"{AS * K_U**aS * L_U**(1-aS):.4f}]")

    for nome in ("Norte", "Sul"):
        y0 = base[nome]["y0"]
        print(f"  {nome:6s}: y {y0:.4f} -> {y_U:.4f}  "
              f"({100*(y_U/y0-1):+.2f}%, fator {y_U/y0:.4f}x)")

    Y_antes = base["Norte"]["Y0"] + base["Sul"]["Y0"]
    print(f"\n  PIB agregado: {Y_antes:.4f} -> {Y_U:.4f} ({100*(Y_U/Y_antes-1):+.3f}%)")

    # --- de onde vem o ganho: decomposicao em dois canais -----------------------
    print("\n  decomposicao do ganho AGREGADO em dois canais:")
    Y_N_techS = y_de_k(base["Norte"]["k0"], AS, aS) * PAIS["Norte"]["L0"]
    Y_meio = base["Sul"]["Y0"] + Y_N_techS      # Norte ja com a tecnologia do Sul, k ainda 10
    c1 = Y_meio / Y_antes
    c2 = Y_U / Y_meio
    print(f"    1) Norte adota a tecnologia do Sul (k ainda = 10): "
          f"{Y_antes:.4f} -> {Y_meio:.4f}  ({100*(c1-1):+.3f}%)")
    print(f"    2) capital e repartido entre 30 trabalhadores (k -> 270): "
          f"{Y_meio:.4f} -> {Y_U:.4f}  ({100*(c2-1):+.3f}%)")
    print(f"    produto dos canais = {c1*c2:.6f} vs direto {Y_U/Y_antes:.6f}"
          f" -> {'OK' if abs(c1*c2 - Y_U/Y_antes) < 1e-9 else 'FALHOU'}")

    # --- decomposicao do ganho do NORTE (A, alpha, aprofundamento) --------------
    kN0 = base["Norte"]["k0"]
    yN_A = y_de_k(kN0, AS, PAIS["Norte"]["alpha"])         # so A: 4 -> 5
    yN_Aa = y_de_k(kN0, AS, aS)                            # + alpha: 0.25 -> 0.5
    print("\n  decomposicao do ganho do NORTE (y: 7.113 -> 82.158):")
    print(f"    A de 4 para 5           : {base['Norte']['y0']:.4f} -> {yN_A:.4f} "
          f"(fator {yN_A/base['Norte']['y0']:.4f})")
    print(f"    alpha de 0.25 para 0.50 : {yN_A:.4f} -> {yN_Aa:.4f} "
          f"(fator {yN_Aa/yN_A:.4f})")
    print(f"    k de 10 para 270        : {yN_Aa:.4f} -> {y_U:.4f} "
          f"(fator {y_U/yN_Aa:.4f})")
    print(f"    produto = {(yN_A/base['Norte']['y0'])*(yN_Aa/yN_A)*(y_U/yN_Aa):.4f}"
          f" vs direto {y_U/base['Norte']['y0']:.4f}")

    # a partir de que k a tecnologia do Sul supera a do Norte?
    k_cruza = (PAIS["Norte"]["A"] / AS) ** (1 / (aS - PAIS["Norte"]["alpha"]))
    print(f"\n  tecnologias se cruzam em k = (4/5)^(1/0.25) = {k_cruza:.4f}"
          f"  -> acima disso a do Sul rende mais (ambos operam MUITO acima)")

    # produto marginal do capital: o motor do ganho de realocacao
    def mpk(k, A, alpha):
        return alpha * A * k ** (alpha - 1)

    print("\n  PMgK sob a tecnologia do Sul (equalizacao e a fonte do canal 2):")
    print(f"    Norte, k=10  : {mpk(10, AS, aS):.6f}")
    print(f"    Sul,   k=400 : {mpk(400, AS, aS):.6f}")
    print(f"    unificado,   k=270 : {mpk(270, AS, aS):.6f}")

    # ============================================================== (d) bonus
    print()
    print("=" * 70)
    print("(d) BONUS -- estado estacionario da Coreia unificada")
    print("=" * 70)
    n_U = F(PAIS["Norte"]["L0"] * 3 + PAIS["Sul"]["L0"] * 1, 100 * L_U)  # média ponderada
    n_U_f = (PAIS["Norte"]["L0"] * PAIS["Norte"]["n"]
             + PAIS["Sul"]["L0"] * PAIS["Sul"]["n"]) / L_U
    print(f"  n_U = (10*0.03 + 20*0.01)/30 = {n_U} = {n_U_f:.6f}")
    print(f"  n_U + delta = {n_U_f + DELTA:.6f} = {F(n_U_f + DELTA).limit_denominator(100)}")
    ks_U = k_estrela(PAIS["Sul"]["s"], AS, aS, n_U_f)
    ys_U = y_de_k(ks_U, AS, aS)
    print(f"  sA/(n_U+d) = {PAIS['Sul']['s']*AS}/{n_U_f+DELTA:.6f} = "
          f"{PAIS['Sul']['s']*AS/(n_U_f+DELTA):g}")
    print(f"  k*_U = {ks_U:.4f}   y*_U = {ys_U:.4f}")
    print(f"  [check] passo(k*_U) = {passo(ks_U, PAIS['Sul']['s'], AS, aS, n_U_f):.8f}")
    print(f"\n  k_U = {float(k_U):g} vs k*_U = {ks_U:.4f} -> "
          f"{'ABAIXO' if float(k_U) < ks_U else 'ACIMA'} ({100*float(k_U)/ks_U:.2f}% de k*_U)")
    print(f"  y_U = {y_U:.4f} vs y*_U = {ys_U:.4f} ({100*y_U/ys_U:.2f}% de y*_U)")
    print(f"\n  y*_U = {ys_U:.4f} vs y*_Sul = {ss['Sul']['ys']:.4f}"
          f"  -> razao {ys_U/ss['Sul']['ys']:.4f} ({100*(ys_U/ss['Sul']['ys']-1):+.2f}%)")
    analitico = ((PAIS["Sul"]["n"] + DELTA) / (n_U_f + DELTA)) ** (aS / (1 - aS))
    print(f"  formula: [(n_S+d)/(n_U+d)]^(a/(1-a)) = {analitico:.4f}"
          f" -> {'OK' if abs(analitico - ys_U/ss['Sul']['ys']) < 1e-9 else 'FALHOU'}")
    print(f"  y*_U vs y*_Norte: {ys_U/ss['Norte']['ys']:.4f}x")

    # media ponderada dos estados estacionarios separados, para comparar no LP
    y_med = (PAIS["Norte"]["L0"] * ss["Norte"]["ys"]
             + PAIS["Sul"]["L0"] * ss["Sul"]["ys"]) / L_U
    print(f"\n  media ponderada dos y* separados = (20*125 + 10*8)/30 = {y_med:.4f}")
    print(f"  y*_U = {ys_U:.4f} -> unificacao eleva o y* MEDIO em "
          f"{100*(ys_U/y_med-1):+.2f}%, mas reduz o do Sul em "
          f"{100*(ys_U/ss['Sul']['ys']-1):+.2f}%")
    print(f"\n  crescimento agregado de LP: g_Y = n_U = {100*n_U_f:.4f}%"
          f" (era {100*PAIS['Sul']['n']:.0f}% no Sul e {100*PAIS['Norte']['n']:.0f}% no Norte)")


if __name__ == "__main__":
    relatorio()
