"""Nucleo dos dois modelos da Lista 4 (Kurlat 2020, cap. 7).

=========================  QUESTAO 1  =========================
Escolha estatica consumo-lazer, com imposto sobre salario e transferencia
lump-sum:

    max  ln(c) + b * l^(1-gamma)/(1-gamma)
     c,l
    s.a. c = (1-tau)*w*(hbar - l) + T

Escreva wt = (1-tau)*w (salario liquido = preco do lazer). A CPO intratemporal e

    TMS = b*c*l^(-gamma) = wt                                          (CPO)

Substituindo a restricao em (CPO) chega-se a equacao implicita do lazer:

    Phi(l) := l^gamma + b*l = b*hbar + b*T/wt                          (L)

Phi e estritamente crescente, entao (L) tem raiz unica. Dois casos fechados:

    T = 0, qualquer gamma  ->  l^gamma + b*l = b*hbar
                               l NAO depende de wt: oferta VERTICAL.
    gamma = 1, T qualquer  ->  l = b/(1+b) * (hbar + T/wt)

Orcamento equilibrado (T = tau*w*n endogeno, com c = w*n em equilibrio):

    (1-tau)*l^gamma + b*l = b*hbar                                     (LB)
    gamma = 1  ->  l = b/(b + 1 - tau)

Elasticidade de Frisch (mantendo c fixo, de (CPO)):  l/(gamma*n).

=========================  QUESTAO 2  =========================
Busca DMP. m(V,U) = mu * V^alpha * U^(1-alpha), separacao s, L = U+E fixo.

    E_{t+1} = (1-s)*E_t + m(V_t, U_t)                                  (LM)

Taxas: u = U/L, v = V/L, theta = V/U.

    f = m/U = mu*theta^alpha           (job finding)
    q = m/V = mu*theta^(alpha-1)       (job filling),  f = theta*q

Estado estacionario  s*(1-u) = mu*v^alpha*u^(1-alpha) = f*u  da:

    curva de Beveridge:  v = [s*(1-u)/mu]^(1/alpha) * u^(-(1-alpha)/alpha)
    desemprego:          u* = s/(s + f) = s/(s + mu*theta^alpha)
"""
import numpy as np
from scipy.optimize import brentq

# =====================================================================
#                            QUESTAO 1
# =====================================================================

def lazer(wt, b, gamma, T=0.0, hbar=1.0):
    """Raiz de Phi(l) = l^gamma + b*l = b*hbar + b*T/wt, no intervalo (0, hbar].

    Se wt <= b*T*hbar^(-gamma) o otimo e o canto l = hbar (nao participa).
    """
    if wt <= 0:
        return hbar
    rhs = b * hbar + b * T / wt
    if rhs >= hbar ** gamma + b * hbar:          # canto: nao participa
        return hbar
    phi = lambda l: l ** gamma + b * l - rhs
    return brentq(phi, 1e-12, hbar)


def horas(wt, b, gamma, T=0.0, hbar=1.0):
    """Oferta de trabalho n = hbar - l."""
    return hbar - lazer(wt, b, gamma, T, hbar)


def consumo(wt, b, gamma, T=0.0, hbar=1.0):
    return wt * horas(wt, b, gamma, T, hbar) + T


def salario_reserva(T, b, gamma, tau=0.0, hbar=1.0):
    """w^r: abaixo dele o domicilio nao participa. w^r = b*T*hbar^(-gamma)/(1-tau).

    Com T = 0 o salario de reserva e zero -- sempre se participa.
    """
    return b * T * hbar ** (-gamma) / (1.0 - tau)


def dn_dtau(w, tau, b, gamma, T=0.0, hbar=1.0):
    """Derivada analitica  dn/dtau = -b*T / [w*(1-tau)^2 * (gamma*l^(gamma-1)+b)].

    Zero se e somente se T = 0. Nunca positiva.
    """
    wt = (1.0 - tau) * w
    l = lazer(wt, b, gamma, T, hbar)
    if l >= hbar:
        return 0.0
    return -b * T / (w * (1.0 - tau) ** 2 * (gamma * l ** (gamma - 1.0) + b))


def elasticidade_marshall(wt, b, gamma, T=0.0, hbar=1.0):
    """(dn/dwt)*(wt/n) = (l^gamma - b*n) / [n*(gamma*l^(gamma-1)+b)]. Zero se T=0."""
    l = lazer(wt, b, gamma, T, hbar)
    n = hbar - l
    if n <= 0:
        return 0.0
    return (l ** gamma - b * n) / (n * (gamma * l ** (gamma - 1.0) + b))


def elasticidade_frisch(wt, b, gamma, T=0.0, hbar=1.0):
    """Frisch (consumo constante) = l/(gamma*n). Sempre positiva."""
    l = lazer(wt, b, gamma, T, hbar)
    return l / (gamma * (hbar - l))


def lazer_orcamento_equilibrado(tau, b, gamma, hbar=1.0):
    """Raiz de (1-tau)*l^gamma + b*l = b*hbar. Governo devolve toda a receita."""
    phi = lambda l: (1.0 - tau) * l ** gamma + b * l - b * hbar
    return brentq(phi, 1e-12, hbar)


# =====================================================================
#                            QUESTAO 2
# =====================================================================

def matches(V, U, mu, alpha):
    return mu * V ** alpha * U ** (1.0 - alpha)


def f_rate(theta, mu, alpha):
    """Taxa de saida do desemprego. Elasticidade em theta: +alpha."""
    return mu * theta ** alpha


def q_rate(theta, mu, alpha):
    """Taxa de preenchimento da vaga. Elasticidade em theta: -(1-alpha)."""
    return mu * theta ** (alpha - 1.0)


def beveridge(u, s, mu, alpha):
    """v(u) do estado estacionario: v = [s(1-u)/mu]^(1/alpha) * u^(-(1-alpha)/alpha)."""
    u = np.asarray(u, dtype=float)
    return (s * (1.0 - u) / mu) ** (1.0 / alpha) * u ** (-(1.0 - alpha) / alpha)


def dv_du(u, s, mu, alpha):
    """Inclinacao da curva de Beveridge: dv/du = -(v/(alpha*u))*[u/(1-u) + 1-alpha] < 0."""
    v = beveridge(u, s, mu, alpha)
    return -(v / (alpha * u)) * (u / (1.0 - u) + 1.0 - alpha)


def u_estrela(theta, s, mu, alpha):
    """u* = s/(s+f) com f = mu*theta^alpha."""
    return s / (s + f_rate(theta, mu, alpha))


def trajetoria_emprego(e0, v, s, mu, alpha, T=60):
    """Itera e_{t+1} = (1-s)*e_t + mu*v^alpha*(1-e_t)^(1-alpha) com v fixo."""
    e = np.empty(T + 1)
    e[0] = e0
    for t in range(T):
        e[t + 1] = (1.0 - s) * e[t] + mu * v ** alpha * (1.0 - e[t]) ** (1.0 - alpha)
    return e
