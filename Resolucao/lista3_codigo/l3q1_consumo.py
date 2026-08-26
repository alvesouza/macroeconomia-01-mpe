"""Questao 1 da Lista 3 -- verificacao numerica de todos os itens.

Cada bloco confere a formula fechada contra um caminho independente:
otimizacao numerica direta, derivada por diferencas centrais, ou identidade
contabil da restricao orcamentaria.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from scipy.optimize import minimize_scalar
from modelo import (Omega, pmgc, riqueza, theta, solucao, residuo_euler,
                    bem_estar, u)

OK = "  [ok]"

# calibracao de referencia da resolucao
BETA, R = 0.96, 0.50
A0, Y1, Y2, T1, T2 = 10.0, 100.0, 69.0, 6.0, 9.0


def bruto(a, a0, y1, y2, r, beta, sigma, t1, t2):
    """Utilidade como funcao SO de 'a' (as duas restricoes ja substituidas)."""
    c1 = a0 + y1 - t1 - a
    c2 = y2 - t2 + (1 + r) * a
    if c1 <= 0 or c2 <= 0:
        return np.inf
    return -bem_estar(c1, c2, beta, sigma)


print("=" * 74)
print("(a)  FORMA FECHADA  x  OTIMIZACAO NUMERICA DIRETA")
print("=" * 74)
print(f"  beta={BETA}  r={R}  a0={A0}  y1={Y1}  y2={Y2}  tau1={T1}  tau2={T2}")
print(f"  W = {riqueza(A0, Y1, Y2, R, T1, T2):.6f}\n")
print(f"  {'sigma':>6} {'Omega':>9} {'PMgC':>8} {'c1':>10} {'c2':>10} {'a':>10}"
      f" {'a (num.)':>10} {'Euler':>11}")
for s in (0.5, 1.0, 2.0, 5.0):
    c1, c2, a = solucao(A0, Y1, Y2, R, BETA, s, T1, T2)
    num = minimize_scalar(bruto, bounds=(-60, 100), method="bounded",
                          args=(A0, Y1, Y2, R, BETA, s, T1, T2),
                          options={"xatol": 1e-10}).x
    assert abs(num - a) < 1e-5, (s, num, a)
    assert abs(residuo_euler(c1, c2, R, BETA, s)) < 1e-12
    # identidade contabil: a RIO tem de fechar
    assert abs(c1 + c2 / (1 + R) - riqueza(A0, Y1, Y2, R, T1, T2)) < 1e-10
    print(f"  {s:6.2f} {Omega(BETA,R,s):9.5f} {pmgc(BETA,R,s):8.5f}"
          f" {c1:10.5f} {c2:10.5f} {a:10.5f} {num:10.5f}"
          f" {residuo_euler(c1,c2,R,BETA,s):11.2e}")
print(OK, "forma fechada = otimo numerico; Euler = 0; RIO fecha.\n")

print("=" * 74)
print("(b)  dc1/dy2  =  PMgC/(1+r)   e   dc1/dy1 = PMgC")
print("=" * 74)
h = 1e-5
print(f"  {'sigma':>6} {'dc1/dy2':>12} {'PMgC/(1+r)':>12} {'dc1/dy1':>12}"
      f" {'razao':>8} {'da/dy2':>10}")
for s in (0.5, 1.0, 2.0):
    d2 = (solucao(A0, Y1, Y2 + h, R, BETA, s, T1, T2)[0]
          - solucao(A0, Y1, Y2 - h, R, BETA, s, T1, T2)[0]) / (2 * h)
    d1 = (solucao(A0, Y1 + h, Y2, R, BETA, s, T1, T2)[0]
          - solucao(A0, Y1 - h, Y2, R, BETA, s, T1, T2)[0]) / (2 * h)
    da = (solucao(A0, Y1, Y2 + h, R, BETA, s, T1, T2)[2]
          - solucao(A0, Y1, Y2 - h, R, BETA, s, T1, T2)[2]) / (2 * h)
    teor = pmgc(BETA, R, s) / (1 + R)
    assert abs(d2 - teor) < 1e-6 and abs(d1 - pmgc(BETA, R, s)) < 1e-6
    assert abs(da + d2) < 1e-6                 # da/dy2 = -dc1/dy2
    print(f"  {s:6.2f} {d2:12.6f} {teor:12.6f} {d1:12.6f}"
          f" {d2/d1:8.5f} {da:10.6f}")
print(f"  razao dc1/dy2 : dc1/dy1 = 1/(1+r) = {1/(1+R):.5f} para todo sigma")
print(OK, "0 < dc1/dy2 < dc1/dy1 < 1; poupanca CAI com otimismo.\n")

print("=" * 74)
print("(c)  y2 = tau1 = tau2 = 0:  SINAL DE dc1/dr E DECIDIDO POR sigma")
print("=" * 74)
print(f"  {'sigma':>6} {'c1':>10} {'dc1/dr (num)':>14} {'formula':>12}"
      f" {'elast.':>9}  efeito dominante")
for s in (0.3, 0.5, 0.999, 1.0, 1.001, 2.0, 4.0):
    c1 = solucao(A0, Y1, 0.0, R, BETA, s)[0]
    dnum = (solucao(A0, Y1, 0.0, R + h, BETA, s)[0]
            - solucao(A0, Y1, 0.0, R - h, BETA, s)[0]) / (2 * h)
    om = Omega(BETA, R, s)
    dteo = c1 / (1 + R) * om / (1 + om) * (s - 1) / s
    elast = (1 - 1 / s) * om / (1 + om)
    assert abs(dnum - dteo) < 1e-4, (s, dnum, dteo)
    dom = ("substituicao" if s < 1 else
           "EMPATE (log)" if np.isclose(s, 1) else "renda")
    print(f"  {s:6.3f} {c1:10.5f} {dnum:14.6f} {dteo:12.6f} {elast:9.5f}"
          f"  {dom}")
print(OK, "dc1/dr tem o sinal de (sigma-1); zero exatamente em sigma=1.\n")

print("=" * 74)
print("(d)  ESTATICA COMPARATIVA DOS IMPOSTOS (caso geral)")
print("=" * 74)
print(f"  {'sigma':>6} {'dc1/dt1':>10} {'dc1/dt2':>10} {'dc2/dt1':>10}"
      f" {'dc2/dt2':>10} {'da/dt1':>9} {'da/dt2':>9}")
for s in (0.5, 1.0, 2.0):
    def dd(k, arg):
        p = dict(t1=T1, t2=T2); p[arg] = p[arg] + h
        m = dict(t1=T1, t2=T2); m[arg] = m[arg] - h
        return (solucao(A0, Y1, Y2, R, BETA, s, **p)[k]
                - solucao(A0, Y1, Y2, R, BETA, s, **m)[k]) / (2 * h)
    mp, th_ = pmgc(BETA, R, s), theta(BETA, R, s)
    vals = [dd(0,'t1'), dd(0,'t2'), dd(1,'t1'), dd(1,'t2'), dd(2,'t1'), dd(2,'t2')]
    teor = [-mp, -mp/(1+R), -th_*mp, -th_*mp/(1+R), -(1-mp), mp/(1+R)]
    for v, t in zip(vals, teor):
        assert abs(v - t) < 1e-5, (s, v, t)
    print(f"  {s:6.2f}" + "".join(f"{v:10.5f}" if i < 4 else f"{v:9.5f}"
                                  for i, v in enumerate(vals)))
print("  sinais: dc1/dt<0, dc2/dt<0 sempre;  da/dt1<0  mas  da/dt2>0")
print(OK, "imposto lump-sum NAO mexe em c2/c1 -- so desloca a reta.\n")
for s in (0.5, 1.0, 2.0):
    r1 = np.array([solucao(A0, Y1, Y2, R, BETA, s, t, T2)[1]
                   / solucao(A0, Y1, Y2, R, BETA, s, t, T2)[0]
                   for t in (0, 5, 20, 40)])
    assert np.allclose(r1, theta(BETA, R, s))
print(OK, f"c2/c1 = [beta(1+r)]^(1/sigma) invariante a tau1 e tau2.\n")

print("=" * 74)
print("(e)  EQUIVALENCIA RICARDIANA:  d tau1 = -1,  d tau2 = +(1+r)")
print("=" * 74)
print(f"  {'sigma':>6} {'c1 antes':>10} {'c1 depois':>10} {'c2 antes':>10}"
      f" {'c2 depois':>10} {'a antes':>9} {'a depois':>9} {'da':>7}")
for s in (0.5, 1.0, 2.0, 5.0):
    v0 = solucao(A0, Y1, Y2, R, BETA, s, T1, T2)
    v1 = solucao(A0, Y1, Y2, R, BETA, s, T1 - 1.0, T2 + (1 + R))
    assert abs(v1[0] - v0[0]) < 1e-10 and abs(v1[1] - v0[1]) < 1e-10
    assert abs((v1[2] - v0[2]) - 1.0) < 1e-10
    print(f"  {s:6.2f} {v0[0]:10.5f} {v1[0]:10.5f} {v0[1]:10.5f} {v1[1]:10.5f}"
          f" {v0[2]:9.5f} {v1[2]:9.5f} {v1[2]-v0[2]:7.4f}")
pv0 = T1 + T2 / (1 + R)
pv1 = (T1 - 1) + (T2 + (1 + R)) / (1 + R)
print(f"  VP dos impostos: antes = {pv0:.6f}   depois = {pv1:.6f}"
      f"   (diferenca = {pv1-pv0:.1e})")
print(OK, "c1 e c2 INALTERADOS; poupanca privada sobe exatamente 1,00.\n")

print("=" * 74)
print("RESUMO: todos os asserts passaram.")
print("=" * 74)
