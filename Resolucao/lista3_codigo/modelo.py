"""Nucleo do modelo de dois periodos da Lista 3 (Kurlat 2020, cap. 6).

Toda a lista e um unico modelo:

    max u(c1) + beta*u(c2)   s.a.   c1 + a = a0 + y1 - t1
                                    c2 = y2 - t2 + (1+r)a

com u(c) = c^(1-sigma)/(1-sigma)  (u(c) = ln c quando sigma = 1).

Objeto central: Omega = beta^(1/sigma) * (1+r)^(1/sigma - 1).
E o denominador da eq. (6.2.9) do Kurlat menos 1. Dele saem TODAS as respostas:

    PMgC (propensao marginal a consumir a riqueza)  =  1/(1+Omega)
    c1 = W/(1+Omega),  c2 = [beta(1+r)]^(1/sigma) * c1
    d ln c1 / d ln(1+r)  =  (1 - 1/sigma) * Omega/(1+Omega)      [com y2=t1=t2=0]
"""
import numpy as np

# ---------------------------------------------------------------- utilidade
def u(c, sigma):
    """CRRA. sigma=1 cai no log por continuidade."""
    c = np.asarray(c, dtype=float)
    if np.isclose(sigma, 1.0):
        return np.log(c)
    return c ** (1.0 - sigma) / (1.0 - sigma)


def up(c, sigma):
    """Utilidade marginal: u'(c) = c^(-sigma). Vale inclusive no log."""
    return np.asarray(c, dtype=float) ** (-sigma)


# ------------------------------------------------------------------ blocos
def Omega(beta, r, sigma):
    """Omega = beta^(1/sigma) (1+r)^(1/sigma - 1). Kurlat eq. (6.2.9)."""
    return beta ** (1.0 / sigma) * (1.0 + r) ** (1.0 / sigma - 1.0)


def pmgc(beta, r, sigma):
    """Propensao marginal a consumir a riqueza: 1/(1+Omega) in (0,1)."""
    return 1.0 / (1.0 + Omega(beta, r, sigma))


def riqueza(a0, y1, y2, r, t1=0.0, t2=0.0):
    """W = a0 + (y1 - t1) + (y2 - t2)/(1+r)."""
    return a0 + (y1 - t1) + (y2 - t2) / (1.0 + r)


def theta(beta, r, sigma):
    """Razao c2/c1 = [beta(1+r)]^(1/sigma) imposta pela equacao de Euler."""
    return (beta * (1.0 + r)) ** (1.0 / sigma)


# ------------------------------------------------- Questao 1: solucao livre
def solucao(a0, y1, y2, r, beta, sigma, t1=0.0, t2=0.0):
    """Forma fechada do item 1(a). Devolve (c1, c2, a)."""
    W = riqueza(a0, y1, y2, r, t1, t2)
    c1 = W / (1.0 + Omega(beta, r, sigma))
    c2 = theta(beta, r, sigma) * c1
    a = a0 + y1 - t1 - c1
    return c1, c2, a


def residuo_euler(c1, c2, r, beta, sigma):
    """u'(c1) - beta(1+r)u'(c2). Zero na solucao interior."""
    return up(c1, sigma) - beta * (1.0 + r) * up(c2, sigma)


# ------------------------------------- Questao 2: restricao de credito a>=-b
def solucao_restrita(y1, y2, r, beta, sigma, b, t1=0.0, t2=0.0):
    """Item 2(c). Devolve (c1, c2, a, ativa, phi).

    'ativa' diz se a restricao a >= -b esta ativa; phi e o multiplicador
    (u'(c1) - beta(1+r)u'(c2)), positivo exatamente quando ela esta ativa.
    """
    c1u, c2u, au = solucao(0.0, y1, y2, r, beta, sigma, t1, t2)
    if au >= -b:                                   # caso 1: folgada
        return c1u, c2u, au, False, 0.0
    a = -b                                         # caso 2: ativa
    c1 = y1 - t1 + b
    c2 = y2 - t2 - (1.0 + r) * b
    return c1, c2, a, True, residuo_euler(c1, c2, r, beta, sigma)


# ---------------------------- Questao 2(d): imposto sobre o retorno da poupanca
def solucao_imposto_poupanca(y1, y2, r, beta, sigma, tau):
    """c2 = y2 + (1+r-tau)a. Basta trocar (1+r) por Rtil = 1+r-tau."""
    Rtil = 1.0 + r - tau
    W = y1 + y2 / Rtil
    c1 = W / (1.0 + beta ** (1 / sigma) * Rtil ** (1 / sigma - 1))
    c2 = (beta * Rtil) ** (1 / sigma) * c1
    a = y1 - c1
    return c1, c2, a, Rtil


def solucao_lump_sum(y1, y2, r, beta, sigma, T):
    """Comparacao do item 2(d): mesma receita, cobrada como soma fixa em t=2."""
    return solucao(0.0, y1, y2, r, beta, sigma, t1=0.0, t2=T)[:3]


def bem_estar(c1, c2, beta, sigma):
    return u(c1, sigma) + beta * u(c2, sigma)
