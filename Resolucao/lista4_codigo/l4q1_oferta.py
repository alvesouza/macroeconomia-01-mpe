"""Questao 1 -- verificacoes numericas da oferta de trabalho estatica.

Checa, contra a solucao numerica do problema de maximizacao:
  1. a CPO  b*c*l^(-gamma) = (1-tau)*w;
  2. a neutralidade do salario quando T = 0 (para varios gamma);
  3. o sinal e o valor de dn/dtau (derivada analitica x diferenca finita);
  4. a forma fechada com gamma = 1;
  5. a calibracao de Prescott do Kurlat, Ex. 7.5(d)-(e);
  6. a elasticidade de Frisch l/(gamma*n)  --  Kurlat, Ex. 7.5(k)-(l).

Rodar:  python l4q1_oferta.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from scipy.optimize import minimize_scalar
from modelo import (lazer, horas, consumo, dn_dtau, salario_reserva,
                    elasticidade_frisch, elasticidade_marshall,
                    lazer_orcamento_equilibrado)

HBAR = 1.0


def util(l, wt, b, gamma, T):
    """Utilidade indireta em funcao so do lazer, ja substituida a restricao."""
    c = wt * (HBAR - l) + T
    if c <= 0:
        return -np.inf
    leis = np.log(l) if np.isclose(gamma, 1.0) else l ** (1 - gamma) / (1 - gamma)
    return np.log(c) + b * leis


def otimo_por_forca_bruta(wt, b, gamma, T):
    """Maximiza a utilidade indireta sem usar a CPO -- controle independente."""
    r = minimize_scalar(lambda l: -util(l, wt, b, gamma, T),
                        bounds=(1e-9, HBAR - 1e-12), method="bounded",
                        options={"xatol": 1e-12})
    return r.x


print("=" * 74)
print("1. A CPO b*c*l^(-gamma) = (1-tau)*w vale no otimo?")
print("=" * 74)
for b, gamma, tau, T in [(1.54, 1.0, 0.34, 0.102), (2.0, 2.5, 0.20, 0.30),
                         (0.8, 0.5, 0.45, 0.05), (1.2, 3.0, 0.10, 0.00)]:
    w, wt = 1.0, (1 - tau) * 1.0
    l = lazer(wt, b, gamma, T)
    c = consumo(wt, b, gamma, T)
    lhs, rhs = b * c * l ** (-gamma), wt
    lbf = otimo_por_forca_bruta(wt, b, gamma, T)
    print("  b=%.2f gamma=%.1f tau=%.2f T=%.3f | TMS=%.9f  wt=%.9f  |  "
          "l(CPO)=%.9f  l(forca bruta)=%.9f" % (b, gamma, tau, T, lhs, rhs, l, lbf))
    assert np.isclose(lhs, rhs, rtol=1e-8) and np.isclose(l, lbf, atol=1e-6)
print("  OK: CPO satisfeita e coincide com a maximizacao direta.\n")

print("=" * 74)
print("2. Com T = 0, as horas dependem do salario liquido? (deveriam NAO depender)")
print("=" * 74)
for gamma in [0.5, 1.0, 2.0, 4.0]:
    hs = [horas(wt, b=1.54, gamma=gamma, T=0.0) for wt in (0.1, 0.5, 1.0, 5.0, 50.0)]
    print("  gamma=%4.1f   n(wt) para wt em {0,1; 0,5; 1; 5; 50} = %s   amplitude=%.2e"
          % (gamma, np.array2string(np.array(hs), precision=6), max(hs) - min(hs)))
    assert max(hs) - min(hs) < 1e-9
print("  OK: oferta perfeitamente VERTICAL quando T = 0, para todo gamma.")
print("     Motivo: com ln(c) o salario entra aditivamente na utilidade indireta,")
print("     ln[wt*(hbar-l)] = ln(wt) + ln(hbar-l), e some do argmax.\n")

print("=" * 74)
print("3. dn/dtau: derivada analitica contra diferenca finita")
print("=" * 74)
w = 1.0
for b, gamma, tau, T in [(1.54, 1.0, 0.34, 0.102), (1.54, 1.0, 0.34, 0.000),
                         (2.00, 2.5, 0.20, 0.300), (0.80, 0.5, 0.45, 0.050)]:
    ana = dn_dtau(w, tau, b, gamma, T)
    h = 1e-6
    num = (horas((1 - (tau + h)) * w, b, gamma, T)
           - horas((1 - (tau - h)) * w, b, gamma, T)) / (2 * h)
    print("  b=%.2f gamma=%.1f tau=%.2f T=%.3f |  analitica=%+.9f   numerica=%+.9f"
          % (b, gamma, tau, T, ana, num))
    assert np.isclose(ana, num, atol=1e-5)
print("  OK: dn/dtau <= 0 sempre, e = 0 exatamente quando T = 0.\n")

print("=" * 74)
print("4. gamma = 1: forma fechada l = b/(1+b) * (hbar + T/wt)")
print("=" * 74)
for tau, T in [(0.34, 0.102), (0.53, 0.124), (0.00, 0.200)]:
    b, wt = 1.54, (1 - tau)
    fechada = b / (1 + b) * (HBAR + T / wt)
    print("  tau=%.2f T=%.3f |  fechada=%.9f   numerica=%.9f"
          % (tau, T, fechada, lazer(wt, b, 1.0, T)))
    assert np.isclose(fechada, lazer(wt, b, 1.0, T), atol=1e-9)
print("  OK.\n")

print("=" * 74)
print("5. Calibracao de Prescott -- Kurlat (2020), Ex. 7.5(d)-(f)")
print("   b (= alpha no livro) = 1,54;  w = 1;  hbar = 1")
print("=" * 74)
b, w = 1.54, 1.0
print("  %-8s %6s %6s | %8s %8s | %10s %10s" %
      ("", "tau", "T", "lazer", "horas n", "receita", "T (dado)"))
res = {}
for nome, tau, T in [("EUA", 0.34, 0.102), ("Europa", 0.53, 0.124)]:
    wt = (1 - tau) * w
    l = lazer(wt, b, 1.0, T)
    n = HBAR - l
    receita = tau * w * n
    res[nome] = (l, n)
    print("  %-8s %6.2f %6.3f | %8.4f %8.4f | %10.4f %10.3f"
          % (nome, tau, T, l, n, receita, T))
    assert abs(receita - T) < 5e-4, "orcamento do governo nao fecha"
print("  OK: os dois governos tem orcamento equilibrado (Ex. 7.5(e)).")
nEU, nUS = res["Europa"][1], res["EUA"][1]
print("  Horas na Europa / horas nos EUA = %.4f  ->  a Europa trabalha %.1f%% menos."
      % (nEU / nUS, 100 * (1 - nEU / nUS)))
print("  Com Y = L = n, o PIB per capita europeu e %.1f%% menor (Ex. 7.5(f)).\n"
      % (100 * (1 - nEU / nUS)))

print("=" * 74)
print("6. Orcamento equilibrado endogeno: T = tau*w*n  ->  l = b/(b+1-tau)")
print("=" * 74)
for tau in [0.00, 0.34, 0.53, 0.70]:
    fechada = b / (b + 1 - tau)
    numerica = lazer_orcamento_equilibrado(tau, b, 1.0)
    print("  tau=%.2f |  l fechada=%.6f   l numerica=%.6f   n=%.6f"
          % (tau, fechada, numerica, 1 - numerica))
    assert np.isclose(fechada, numerica, atol=1e-9)
print("  OK: aqui dn/dtau < 0 SEMPRE -- o rebate anula o efeito renda e sobra")
print("     so o efeito substituicao. Contraste com o caso T = 0 do bloco 2.\n")

print("=" * 74)
print("7. Elasticidade de Frisch = l/(gamma*n)  --  Kurlat, Ex. 7.5(k)-(l)")
print("=" * 74)
for nome, tau, T in [("EUA", 0.34, 0.102), ("Europa", 0.53, 0.124)]:
    wt = (1 - tau) * w
    fr = elasticidade_frisch(wt, b, 1.0, T)
    ma = elasticidade_marshall(wt, b, 1.0, T)
    print("  %-8s Frisch = %.3f   Marshall (nao compensada) = %.3f" % (nome, fr, ma))
print("  Estimativas empiricas da Frisch ficam entre 0,4 e 1 (Kurlat, Ex. 7.5(l)).")
print("  O modelo de Prescott precisa de ~2,3 -- muito acima. E a critica padrao:")
print("  sem essa elasticidade alta, o imposto nao explica o hiato EUA-Europa.\n")

print("=" * 74)
print("8. Salario de reserva e margem extensiva")
print("=" * 74)
for T in [0.0, 0.102, 0.30]:
    wr = salario_reserva(T, b, 1.0, tau=0.34)
    n_abaixo = horas((1 - 0.34) * (wr * 0.99), b, 1.0, T) if wr > 0 else None
    print("  T=%.3f |  w^r = b*T*hbar^(-gamma)/(1-tau) = %.4f   n logo abaixo de w^r = %s"
          % (T, wr, "%.4f" % n_abaixo if n_abaixo is not None else "n/a (w^r=0)"))
print("  OK: com T = 0 o salario de reserva e zero -- participa-se a qualquer salario.")
print("      Com T > 0, tau mais alto ELEVA w^r e expulsa gente pela margem extensiva.")
