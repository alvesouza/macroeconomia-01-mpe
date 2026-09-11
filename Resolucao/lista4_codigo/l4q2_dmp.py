"""Questao 2 -- verificacoes numericas do modelo de busca DMP.

Calibracao mensal de referencia, escolhida para bater com os fatos do Kurlat
(sec. 7.1, Fig. 7.1.3: perda de emprego 1-2% ao mes, saida do desemprego ~30%
ao mes) e com a JOLTS (taxa de vagas ~4,4%):

    s = 0,02    alpha = 0,5    theta = 0,7    ->    mu = 0,30/sqrt(0,7)

que entrega f = 0,30, q = 0,4286, u* = 6,25%, v = 4,375%.

Checa:
  1. f = theta*q, e as elasticidades +alpha e -(1-alpha);
  2. a curva de Beveridge satisfaz a condicao criacao = destruicao;
  3. a inclinacao analitica dv/du contra diferenca finita;
  4. u* = s/(s+f) coincide com o ponto da curva de Beveridge;
  5. a lei de movimento converge para u*;
  6. produto MARGINAL de uma vaga (alpha*q) contra o produto MEDIO (q);
  7. o deslocamento da curva quando mu cai: d ln v / d ln mu = -1/alpha.

Rodar:  python l4q2_dmp.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from modelo import (matches, f_rate, q_rate, beveridge, dv_du, u_estrela,
                    trajetoria_emprego)

S, ALPHA, THETA0 = 0.02, 0.5, 0.7
MU = 0.30 / THETA0 ** ALPHA

print("=" * 74)
print("CALIBRACAO:  s = %.3f   alpha = %.2f   mu = %.6f" % (S, ALPHA, MU))
f0, q0 = f_rate(THETA0, MU, ALPHA), q_rate(THETA0, MU, ALPHA)
u0 = u_estrela(THETA0, S, MU, ALPHA)
v0 = THETA0 * u0
print("  theta = %.3f  ->  f = %.4f  q = %.4f  u* = %.4f  v = %.4f"
      % (THETA0, f0, q0, u0, v0))
print("  duracao esperada do desemprego 1/f = %.2f meses;  da vaga 1/q = %.2f meses"
      % (1 / f0, 1 / q0))
print("=" * 74, "\n")

print("=" * 74)
print("1. f = theta*q e as elasticidades")
print("=" * 74)
for th in [0.2, 0.5, 0.7, 1.0, 2.0]:
    f, q = f_rate(th, MU, ALPHA), q_rate(th, MU, ALPHA)
    h = 1e-6
    ef = (np.log(f_rate(th + h, MU, ALPHA)) - np.log(f_rate(th - h, MU, ALPHA))) / \
         (np.log(th + h) - np.log(th - h))
    eq = (np.log(q_rate(th + h, MU, ALPHA)) - np.log(q_rate(th - h, MU, ALPHA))) / \
         (np.log(th + h) - np.log(th - h))
    print("  theta=%.2f | f=%.5f  q=%.5f  theta*q=%.5f | elast_f=%+.5f (alpha=%+.2f)"
          "  elast_q=%+.5f (-(1-alpha)=%+.2f)" % (th, f, q, th * q, ef, ALPHA, eq,
                                                  -(1 - ALPHA)))
    assert np.isclose(f, th * q) and np.isclose(ef, ALPHA, atol=1e-6) \
        and np.isclose(eq, -(1 - ALPHA), atol=1e-6)
print("  OK: f sobe com theta, q cai com theta, e as elasticidades somam 1.\n")

print("=" * 74)
print("2. A curva de Beveridge satisfaz  s*(1-u) = mu*v^alpha*u^(1-alpha)?")
print("=" * 74)
for u in [0.03, 0.0625, 0.10, 0.20]:
    v = beveridge(u, S, MU, ALPHA)
    destruicao, criacao = S * (1 - u), matches(v, u, MU, ALPHA)
    print("  u=%.4f -> v=%.6f | destruicao s(1-u)=%.8f  criacao m(v,u)=%.8f"
          % (u, v, destruicao, criacao))
    assert np.isclose(destruicao, criacao)
print("  OK.\n")

print("=" * 74)
print("3. Inclinacao dv/du: analitica contra diferenca finita")
print("=" * 74)
for u in [0.03, 0.0625, 0.10, 0.20]:
    h = 1e-7
    num = (beveridge(u + h, S, MU, ALPHA) - beveridge(u - h, S, MU, ALPHA)) / (2 * h)
    ana = dv_du(u, S, MU, ALPHA)
    print("  u=%.4f | analitica=%+.6f   numerica=%+.6f" % (u, ana, num))
    assert np.isclose(ana, num, rtol=1e-5) and ana < 0
print("  OK: negativa em todo o dominio -- a curva e decrescente e convexa.\n")

print("=" * 74)
print("4. u* = s/(s+f) coincide com o ponto da curva de Beveridge em theta fixo?")
print("=" * 74)
for th in [0.3, 0.7, 1.5]:
    u = u_estrela(th, S, MU, ALPHA)
    v_bc = beveridge(u, S, MU, ALPHA)
    print("  theta=%.2f | u*=%.6f   v da curva=%.6f   theta*u*=%.6f"
          % (th, u, v_bc, th * u))
    assert np.isclose(v_bc, th * u)
print("  OK: as duas formas da condicao de estado estacionario sao a mesma coisa.\n")

print("=" * 74)
print("5. A lei de movimento converge para o estado estacionario?")
print("=" * 74)
v_fix = v0
for e0 in [0.80, 0.90, 0.99]:
    traj = trajetoria_emprego(e0, v_fix, S, MU, ALPHA, T=400)
    u_fim = 1 - traj[-1]
    print("  e_0=%.2f (u_0=%.2f) -> u apos 400 meses = %.6f   (u* teorico com v fixo)"
          % (e0, 1 - e0, u_fim))
u_lim = 1 - trajetoria_emprego(0.90, v_fix, S, MU, ALPHA, T=4000)[-1]
print("  Limite comum = %.6f. Note que aqui v foi mantido FIXO em %.5f, entao o"
      % (u_lim, v_fix))
print("  ponto limite e o u que resolve s(1-u) = mu*v^alpha*u^(1-alpha) -- a")
print("  propria curva de Beveridge lida na horizontal.")
assert np.isclose(beveridge(u_lim, S, MU, ALPHA), v_fix, rtol=1e-5)
print("  OK.\n")

print("=" * 74)
print("6. Uma vaga a mais: produto MARGINAL contra produto MEDIO")
print("=" * 74)
L = 1_000_000.0
U, V = u0 * L, v0 * L
m0 = matches(V, U, MU, ALPHA)
dm = matches(V + 1, U, MU, ALPHA) - m0
print("  L=%.0f  U=%.0f  V=%.0f  ->  m = %.2f matches/mes" % (L, U, V, m0))
print("  A firma espera preencher a propria vaga com prob. q = %.6f  (produto MEDIO)"
      % q0)
print("  O acrescimo EFETIVO de matches na economia foi   %.6f  (produto MARGINAL)"
      % dm)
print("  Previsao teorica dm/dV = alpha*q = %.6f" % (ALPHA * q0))
assert np.isclose(dm, ALPHA * q0, rtol=1e-4)
print("  Cunha (1-alpha)*q = %.6f matches por mes: sao os encontros que as OUTRAS"
      % ((1 - ALPHA) * q0))
print("  firmas deixam de fazer. A firma nao paga por eles -- externalidade de")
print("  congestao. Em paralelo, f sobe de %.6f para %.6f: ganho dos desempregados"
      % (f0, f_rate((V + 1) / U, MU, ALPHA)))
print("  que a firma tambem nao cobra -- externalidade de thick market.\n")

print("=" * 74)
print("7. Queda de mu: deslocamento da curva. d ln v / d ln mu = -1/alpha")
print("=" * 74)
for corte in [0.05, 0.10, 0.20]:
    mu1 = MU * (1 - corte)
    for u in [0.0625, 0.10]:
        v_a, v_b = beveridge(u, S, MU, ALPHA), beveridge(u, S, mu1, ALPHA)
        elast = np.log(v_b / v_a) / np.log(mu1 / MU)
        print("  mu cai %2.0f%% | u=%.4f: v vai de %.5f para %.5f (%+.1f%%)   "
              "elasticidade=%.4f  (-1/alpha=%.2f)"
              % (100 * corte, u, v_a, v_b, 100 * (v_b / v_a - 1), elast, -1 / ALPHA))
        assert np.isclose(elast, -1 / ALPHA, atol=1e-9)
print("  OK: a curva desloca para FORA -- mais vagas para o mesmo desemprego.")
u_novo = u_estrela(THETA0, S, MU * 0.9, ALPHA)
print("  A theta constante (%.2f), u* sobe de %.4f para %.4f quando mu cai 10%%."
      % (THETA0, u0, u_novo))
print("  Nota: s tambem desloca a curva para fora (d ln v/d ln s = +1/alpha = %.2f),"
      % (1 / ALPHA))
print("  entao um deslocamento observado NAO identifica sozinho se caiu mu ou subiu s.")
