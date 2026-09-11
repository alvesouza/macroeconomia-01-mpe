"""Verificacoes numericas dos exercicios do Kurlat, cap. 9.

Cobre:
  9.6  Capital Income Taxes  -- mostra que dc^w/dtau = 0 EXATAMENTE em tau=0
  9.11 Patience and Investment -- K_ss, Y_ss, I/Y = alpha*delta/(rho+delta)
  9.12 Optimal vs Fixed Savings Rates -- shooting, 150 anos, lambda
  9.13 Enclosure Acts -- razao L_A/L_I antes e depois, e o ganho de PIB

Rodar:  python ch09_numerico.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from scipy.optimize import brentq

# ============================================================ 9.11
def rho_de(beta):
    return 1.0 / beta - 1.0


def K_ss(alpha, beta, delta):
    """(9.3.17): alpha*K^(alpha-1) = 1/beta - 1 + delta. Note: sigma NAO entra."""
    return (alpha / (rho_de(beta) + delta)) ** (1.0 / (1.0 - alpha))


def iy_ss(alpha, beta, delta):
    """I/Y = delta*K_ss^(1-alpha) = alpha*delta/(rho+delta)."""
    return alpha * delta / (rho_de(beta) + delta)


print("=" * 74)
print("9.11 -- estado estacionario")
print("=" * 74)
A, B, D, S = 0.4, 0.95, 0.08, 2.0
Kss, Yss = K_ss(A, B, D), K_ss(A, B, D) ** A
print("  alpha=%.2f beta=%.2f delta=%.2f sigma=%.1f   rho = 1/beta-1 = %.6f"
      % (A, B, D, S, rho_de(B)))
print("  K_ss = %.6f   Y_ss = %.6f   I/Y = %.6f" % (Kss, Yss, iy_ss(A, B, D)))
# checagens
assert np.isclose(A * Kss ** (A - 1), rho_de(B) + D), "(9.3.17) nao fecha"
assert np.isclose(iy_ss(A, B, D), D * Kss ** (1 - A)), "I/Y nao fecha"
print("  Confere: alpha*K^(alpha-1) = %.6f = rho+delta" % (A * Kss ** (A - 1)))
print("  I/Y = alpha*delta/(rho+delta) = %.6f  -- e MENOR que alpha = %.2f,"
      % (iy_ss(A, B, D), A))
print("  que seria a taxa da Regra de Ouro. A diferenca e a impaciencia.")
K_gr = (A / D) ** (1 / (1 - A))
print("  K_gr = (alpha/delta)^(1/(1-alpha)) = %.6f  >  K_ss = %.6f  OK\n"
      % (K_gr, Kss))

# ============================================================ 9.6
print("=" * 74)
print("9.6 -- imposto sobre renda do capital: o efeito sobre os TRABALHADORES")
print("=" * 74)


def steady_tax(tau, alpha=A, beta=B, delta=D, L=1.0):
    """Estado estacionario com imposto tau sobre (r^K - delta).

    Euler pos-imposto:  (1-tau)*(r^K - delta) = rho   =>  r^K = delta + rho/(1-tau)
    """
    rho = rho_de(beta)
    rK = delta + rho / (1.0 - tau)
    K = L * (alpha / rK) ** (1.0 / (1.0 - alpha))
    Y = K ** alpha * L ** (1.0 - alpha)
    w = (1.0 - alpha) * (K / L) ** alpha
    receita = tau * (rK - delta) * K
    return dict(rK=rK, K=K, Y=Y, w=w, wL=w * L, T=receita, cw=w * L + receita)


print("  %6s %9s %9s %9s %9s %9s" % ("tau", "r^K", "K", "Y", "wL", "c^w"))
for tau in [0.0, 0.05, 0.10, 0.20, 0.40, 0.60]:
    d = steady_tax(tau)
    print("  %6.2f %9.5f %9.5f %9.5f %9.5f %9.5f"
          % (tau, d["rK"], d["K"], d["Y"], d["wL"], d["cw"]))

h = 1e-6
dcw = (steady_tax(h)["cw"] - steady_tax(0.0)["cw"]) / h
print("\n  d c^w / d tau em tau=0  =  %+.3e   (previsao analitica: ZERO)" % dcw)
assert abs(dcw) < 1e-4, "a derivada deveria ser nula"
print("  Motivo: ganho de receita = rho*K; perda de salario = alpha*rho*Y/r^K.")
print("  Como r^K = alpha*Y/K, os dois termos sao IGUAIS e se cancelam.")
d2 = (steady_tax(h)["cw"] - 2 * steady_tax(0.0)["cw"] + steady_tax(-h)["cw"]) / h ** 2
print("  Segunda derivada = %+.4f  <  0  ->  tau=0 e um MAXIMO." % d2)
print("  Qualquer imposto positivo sobre capital REDUZ o consumo dos trabalhadores")
print("  no estado estacionario, mesmo com toda a receita devolvida a eles.\n")

# ============================================================ 9.12
print("=" * 74)
print("9.12 -- poupanca fixa contra poupanca otima, 150 anos, K_0 = 2")
print("=" * 74)
T, K0 = 150, 2.0


def caminho_fixo(s, K0=K0, T=T, alpha=A, delta=D):
    K = np.empty(T + 1); c = np.empty(T); I = np.empty(T); Y = np.empty(T)
    K[0] = K0
    for t in range(T):
        Y[t] = K[t] ** alpha
        I[t] = s * Y[t]
        c[t] = (1 - s) * Y[t]
        K[t + 1] = (1 - delta) * K[t] + I[t]
    return K, c, I, Y


def caminho_otimo(c0, K0=K0, T=T, alpha=A, beta=B, delta=D, sigma=S):
    """Itera (9.3.15) e (9.3.14) para frente a partir de (K0, c0)."""
    K = np.empty(T + 1); c = np.empty(T + 1)
    K[0], c[0] = K0, c0
    for t in range(T):
        K[t + 1] = (1 - delta) * K[t] + K[t] ** alpha - c[t]
        if K[t + 1] <= 1e-10:
            K[t + 1:] = 1e-10; c[t + 1:] = 1e-10; break
        fator = beta * (1 + alpha * K[t + 1] ** (alpha - 1) - delta)
        c[t + 1] = c[t] * fator ** (1.0 / sigma)
    return K, c


def desvio(c0):
    """Positivo se a trajetoria explode em c (c0 alto), negativo se K explode."""
    K, c = caminho_otimo(c0, T=400)
    return (K[-1] - K_ss(A, B, D))


s_fix = iy_ss(A, B, D)
c0 = brentq(desvio, 0.30, 1.20, xtol=1e-15, rtol=1e-15)
print("  taxa fixa usada (= I/Y de 9.11): s = %.6f" % s_fix)
print("  c_0 do saddle path (shooting):    c_0 = %.10f" % c0)

Kf, cf, If, Yf = caminho_fixo(s_fix)
Ko, co = caminho_otimo(c0)
co = co[:T]; Ko_ = Ko[:T + 1]
Yo = Ko_[:T] ** A
Io = Yo + (1 - D) * Ko_[:T] - Ko_[1:T + 1]

print("\n  %5s %10s %10s %10s %10s" % ("t", "K fixo", "K otimo", "c fixo", "c otimo"))
for t in [0, 1, 5, 10, 25, 50, 100, 149]:
    print("  %5d %10.5f %10.5f %10.5f %10.5f" % (t, Kf[t], Ko_[t], cf[t], co[t]))
print("  %5s %10.5f %10.5f %10.5f %10.5f" % ("ss", Kss, Kss, (1 - s_fix) * Yss,
                                             Yss - D * Kss))

u = lambda x: x ** (1 - S) / (1 - S)
disc = B ** np.arange(T)
U_fix = float(np.sum(disc * u(cf)))
U_opt = float(np.sum(disc * u(co)))
lam = (U_fix / U_opt) ** (1.0 / (1.0 - S))
print("\n  U (poupanca fixa)  = %.6f" % U_fix)
print("  U (poupanca otima) = %.6f" % U_opt)
assert U_opt > U_fix, "a poupanca otima tem de dominar"
print("  lambda = (U_fix/U_opt)^(1/(1-sigma)) = %.6f" % lam)
print("  Reduzir o consumo otimo em %.3f%% deixa o domicilio indiferente entre"
      % (100 * (1 - lam)))
print("  as duas economias. O ganho de escolher bem a poupanca e pequeno --")
print("  porque a taxa fixa usada JA e a taxa de estado estacionario correta;")
print("  toda a diferenca esta no formato da TRANSICAO, nao no destino.\n")

# ============================================================ 9.13
print("=" * 74)
print("9.13 -- Enclosure Acts: propriedade comum contra propriedade privada")
print("=" * 74)
for alpha in [0.3, 0.4, 0.5]:
    razao_eff = 1.0
    razao_comum = (1.0 - alpha) ** (-1.0 / alpha)
    print("  alpha=%.2f | (L_A/L_I) com propriedade comum e %.4f vez a razao eficiente N/K"
          % (alpha, razao_comum))
print("\n  Como (1-alpha)^(-1/alpha) > 1 sempre, a agricultura de uso comum SEMPRE")
print("  atrai trabalhadores demais: o trabalhador recebe o produto MEDIO, e com")
print("  rendimentos decrescentes o medio excede o marginal.")

N, K, Ltot = 1.0, 1.0, 1.0
for alpha in [0.4]:
    LA_eff = Ltot * (N / K) / (1 + N / K)
    LI_eff = Ltot - LA_eff
    Y_eff = N ** alpha * LA_eff ** (1 - alpha) + K ** alpha * LI_eff ** (1 - alpha)
    r = (N / K) * (1 - alpha) ** (-1.0 / alpha)
    LA_c = Ltot * r / (1 + r); LI_c = Ltot - LA_c
    Y_c = N ** alpha * LA_c ** (1 - alpha) + K ** alpha * LI_c ** (1 - alpha)
    print("\n  Com N=K=L=1, alpha=%.2f:" % alpha)
    print("    eficiente: L_A=%.4f L_I=%.4f  ->  Y=%.6f" % (LA_eff, LI_eff, Y_eff))
    print("    comum:     L_A=%.4f L_I=%.4f  ->  Y=%.6f" % (LA_c, LI_c, Y_c))
    print("    ganho de PIB com o cercamento: %+.3f%%" % (100 * (Y_eff / Y_c - 1)))
    w_c = (1 - alpha) * (K / LI_c) ** alpha
    w_e = (1 - alpha) * (K / LI_eff) ** alpha
    print("    salario industrial: %.6f -> %.6f  (%+.2f%%)"
          % (w_c, w_e, 100 * (w_e / w_c - 1)))
    rK_c = alpha * K ** (alpha - 1) * LI_c ** (1 - alpha)
    rK_e = alpha * K ** (alpha - 1) * LI_eff ** (1 - alpha)
    print("    aluguel do capital: %.6f -> %.6f  (%+.2f%%)"
          % (rK_c, rK_e, 100 * (rK_e / rK_c - 1)))
    assert Y_eff > Y_c and w_e < w_c and rK_e > rK_c
print("\n  PIB sobe, salario industrial CAI, aluguel do capital SOBE.")
print("  Eficiencia e distribuicao andam em direcoes opostas -- e exatamente o")
print("  que o 1o TBE separa.")
