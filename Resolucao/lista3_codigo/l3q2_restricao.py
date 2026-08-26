"""Questao 2 da Lista 3 -- restricao de credito e imposto sobre a poupanca."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from scipy.optimize import minimize_scalar, brentq
from modelo import (Omega, pmgc, theta, solucao, solucao_restrita,
                    solucao_imposto_poupanca, solucao_lump_sum,
                    bem_estar)

OK = "  [ok]"
BETA, R, SIGMA = 0.96, 0.50, 2.0

# ============================================================ itens (a)-(c)
print("=" * 78)
print("(c)  DOIS REGIMES: RESTRICAO FOLGADA  x  RESTRICAO ATIVA")
print("=" * 78)
print(f"  beta={BETA}  r={R}  sigma={SIGMA}   =>  Omega={Omega(BETA,R,SIGMA):.6f},"
      f"  PMgC={pmgc(BETA,R,SIGMA):.6f},"
      f"  [beta(1+r)]^(1/sigma)={theta(BETA,R,SIGMA):.6f}\n")

casos = [("poupador (folgada)",    100.0,  66.0, 10.0),
         ("jovem  (ATIVA)",         20.0, 132.0, 10.0),
         ("jovem, b=0 (ATIVA)",     20.0, 132.0,  0.0),
         ("jovem, b=50 (folgada)",  20.0, 132.0, 50.0)]

print(f"  {'caso':<22}{'c1':>9}{'c2':>9}{'a':>9}{'ativa':>7}{'phi':>10}"
      f"{'c2/c1':>9}{'teta':>8}")
for nome, y1, y2, b in casos:
    c1, c2, a, ativa, phi = solucao_restrita(y1, y2, R, BETA, SIGMA, b)

    def objetivo(x, y1=y1, y2=y2):
        cc1, cc2 = y1 - x, y2 + (1 + R) * x
        if cc1 <= 0 or cc2 <= 0:
            return np.inf
        return -bem_estar(cc1, cc2, BETA, SIGMA)

    an = minimize_scalar(objetivo, bounds=(-b, y1 - 1e-9), method="bounded",
                         options={"xatol": 1e-12}).x
    assert abs(an - a) < 1e-5, (nome, an, a)
    assert (phi > 0) == ativa and phi >= -1e-12
    print(f"  {nome:<22}{c1:9.4f}{c2:9.4f}{a:9.4f}{str(ativa):>7}{phi:10.2e}"
          f"{c2/c1:9.5f}{theta(BETA,R,SIGMA):8.5f}")
print("\n  Ativa  =>  c2/c1 < [beta(1+r)]^(1/sigma):  o consumidor QUERIA")
print("             trazer recursos para o presente e nao consegue.")
print(OK, "KKT confere com a otimizacao numerica restrita nos 4 casos.\n")

print("  Limiar: a restricao morde exatamente quando c1_irrestrito > y1-t1+b.")
for y1, y2 in [(20.0, 132.0), (40.0, 90.0)]:
    c1u = solucao(0, y1, y2, R, BETA, SIGMA)[0]
    bstar = c1u - y1
    print(f"    y1={y1:6.1f}  y2={y2:6.1f}  ->  c1_irrestrito={c1u:8.4f},"
          f"  b* = {bstar:8.4f}  (b < b* morde)")
    for eps in (-1e-6, +1e-6):
        ativa = solucao_restrita(y1, y2, R, BETA, SIGMA, bstar + eps)[3]
        assert ativa == (eps < 0)
print(OK, "b* = c1_irrestrito - (y1-tau1) separa os dois regimes.\n")

# ================================================ ponte com 1(e)
print("=" * 78)
print("PONTE COM 1(e):  O ESTIMULO NEUTRO EM VALOR PRESENTE")
print("=" * 78)
DELTA = 5.0
print(f"  d tau1 = -{DELTA},  d tau2 = +{DELTA}(1+r) = {DELTA*(1+R)}"
      f"   (VP dos impostos inalterado)\n")
print(f"  {'caso':<22}{'c1 antes':>10}{'c1 depois':>11}{'dc1':>8}"
      f"{'a antes':>10}{'a depois':>10}")
for nome, y1, y2, b in casos[:3]:
    v0 = solucao_restrita(y1, y2, R, BETA, SIGMA, b, t1=0.0, t2=0.0)
    v1 = solucao_restrita(y1, y2, R, BETA, SIGMA, b,
                          t1=-DELTA, t2=DELTA * (1 + R))
    esperado = 0.0 if not v0[3] else DELTA
    assert abs((v1[0] - v0[0]) - esperado) < 1e-9, (nome, v1[0] - v0[0])
    print(f"  {nome:<22}{v0[0]:10.4f}{v1[0]:11.4f}{v1[0]-v0[0]:8.4f}"
          f"{v0[2]:10.4f}{v1[2]:10.4f}")
print("\n  Folgada  -> dc1 = 0    (equivalencia ricardiana, item 1e)")
print("  ATIVA    -> dc1 = +5   (PMgC = 1: o estimulo e integralmente gasto)")
print(OK, "a restricao de credito e o contraexemplo exato de 1(e).\n")

# ==================================================== (d) imposto sobre poupanca
print("=" * 78)
print("(d)  IMPOSTO SOBRE O RETORNO DA POUPANCA  x  LUMP-SUM DE MESMA RECEITA")
print("=" * 78)
Y1, Y2, TAU = 100.0, 66.0, 0.20
print(f"  y1={Y1}  y2={Y2}  r={R}  tau2={TAU}"
      f"  (= {TAU/R:.0%} da renda de juros)   sigma={SIGMA}\n")

c1S, c2S, aS, Rtil = solucao_imposto_poupanca(Y1, Y2, R, BETA, SIGMA, TAU)
receita = TAU * aS
c1L, c2L, aL = solucao_lump_sum(Y1, Y2, R, BETA, SIGMA, receita)
c10, c20, a00 = solucao(0, Y1, Y2, R, BETA, SIGMA)

print(f"  {'regime':<30}{'c1':>10}{'c2':>10}{'a':>10}{'c2/c1':>10}{'U':>12}")
for nome, trio in [("sem imposto", (c10, c20, a00)),
                   (f"imposto s/ poupanca tau2={TAU}", (c1S, c2S, aS)),
                   (f"lump-sum T={receita:.5f}", (c1L, c2L, aL))]:
    x, y, z = trio
    print(f"  {nome:<30}{x:10.5f}{y:10.5f}{z:10.5f}{y/x:10.5f}"
          f"{bem_estar(x, y, BETA, SIGMA):12.6f}")

print("\n  razao c2/c1 imposta pela equacao de Euler:")
print(f"    sem imposto / lump-sum : [beta(1+r)]^(1/sigma)      "
      f"= {theta(BETA,R,SIGMA):.6f}")
print(f"    imposto sobre poupanca : [beta(1+r-tau2)]^(1/sigma) "
      f"= {(BETA*Rtil)**(1/SIGMA):.6f}")
assert abs(c2L / c1L - c2S / c1S) > 1e-4
assert abs(c2L / c1L - theta(BETA, R, SIGMA)) < 1e-12
assert abs(c20 / c10 - theta(BETA, R, SIGMA)) < 1e-12
print(OK, "lump-sum NAO mexe em c2/c1; imposto sobre poupanca DERRUBA a razao.\n")

vp_S_sob_L = c1S + c2S / (1 + R)
vp_orcamento_L = Y1 + (Y2 - receita) / (1 + R)
print(f"  VP do plano (c1_S, c2_S) precificado a (1+r): {vp_S_sob_L:.10f}")
print(f"  VP da restricao lump-sum com T = tau2*a_S    : {vp_orcamento_L:.10f}")
assert abs(vp_S_sob_L - vp_orcamento_L) < 1e-9
print(OK, "o plano do regime S esta EXATAMENTE sobre a reta do regime L")
print("       -> era factivel sob L e nao foi escolhido -> U_L > U_S.\n")

US, UL = bem_estar(c1S, c2S, BETA, SIGMA), bem_estar(c1L, c2L, BETA, SIGMA)
assert UL > US


def util_lump(T):
    x, y, _ = solucao_lump_sum(Y1, Y2, R, BETA, SIGMA, T)
    return bem_estar(x, y, BETA, SIGMA)


Tstar = brentq(lambda T: util_lump(T) - US, receita, 60.0, xtol=1e-12)
print(f"  U(imposto s/ poupanca)     = {US:.8f}")
print(f"  U(lump-sum, mesma receita) = {UL:.8f}   (maior)")
print(f"  receita do imposto sobre poupanca      T  = {receita:.6f}")
print(f"  lump-sum que deixaria o agente igual   T* = {Tstar:.6f}")
print(f"  PESO MORTO = T* - T = {Tstar-receita:.6f}"
      f"  ({(Tstar-receita)/receita:.2%} da receita)")
print(OK, "excesso de gravame estritamente positivo.\n")

tms_S = (c1S ** (-SIGMA)) / (BETA * c2S ** (-SIGMA))
tms_L = (c1L ** (-SIGMA)) / (BETA * c2L ** (-SIGMA))
print(f"  TMS no otimo com imposto s/ poupanca = {tms_S:.6f}"
      f"   (= 1+r-tau2 = {Rtil:.6f})")
print(f"  TMS no otimo com lump-sum            = {tms_L:.6f}"
      f"   (= 1+r      = {1+R:.6f})")
print(f"  taxa de transformacao da economia    = 1+r = {1+R:.6f}")
print(OK, "a cunha e exatamente tau2: a margem distorcida e a INTERTEMPORAL.\n")

print("  Sensibilidade: a razao c2/c1 cai para TODO sigma; a poupanca, nao.")
print(f"  {'sigma':>7}{'a (sem)':>10}{'a (tau2)':>10}{'variacao':>10}"
      f"{'c2/c1 (sem)':>13}{'c2/c1 (tau2)':>14}")
for s in (0.5, 1.0, 2.0, 4.0):
    a_sem = solucao(0, Y1, Y2, R, BETA, s)[2]
    _, _, a_com, _ = solucao_imposto_poupanca(Y1, Y2, R, BETA, s, TAU)
    r_sem, r_com = theta(BETA, R, s), (BETA * Rtil) ** (1 / s)
    assert r_com < r_sem
    print(f"  {s:7.2f}{a_sem:10.5f}{a_com:10.5f}{a_com-a_sem:+10.5f}"
          f"{r_sem:13.6f}{r_com:14.6f}")
print(OK, "sinal de da/dtau2 depende de sigma; o da razao c2/c1 nunca depende.\n")

print("=" * 78)
print("RESUMO: todos os asserts passaram.")
print("=" * 78)
