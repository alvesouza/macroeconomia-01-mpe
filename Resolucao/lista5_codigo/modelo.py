"""Closed-form solutions for Problem Set 5 (Kurlat ch. 9), imported by the scripts.

Question 1  -- two-period economy, capital FIXED at Kbar, no depreciation, no
               investment technology.  u(c)=c^(1-s)/(1-s), v(l)=psi*ln(l),
               F(K,L)=A_t * Kbar^alpha * L^(1-alpha).

Question 2  -- infinite-horizon economy, labour FIXED at L=1.
               u(c)=c^(1-s)/(1-s), F(K,L)=A K^alpha L^(1-alpha), depreciation delta.

Every formula asserted in lista5_resolucao.tex lives here once, and the two
driver scripts check each of them against an independent numerical route.
"""
import numpy as np
from scipy.optimize import brentq

# ------------------------------------------------------- reference calibration
# Q1: chosen so that equilibrium hours land in a plausible 0.15-0.45 range.
ALPHA, PSI, KBAR = 0.35, 1.8, 2.0
# Q2:
A2, ALPHA2, DELTA = 1.0, 0.35, 0.08
BETA = 0.96


# =============================================================== QUESTION 1
def c_de_L(L, A, alpha=ALPHA, Kbar=KBAR):
    """Goods market clearing: c_t = F(Kbar, L_t).  No investment term."""
    return A * Kbar ** alpha * L ** (1 - alpha)


def w_de_L(L, A, alpha=ALPHA, Kbar=KBAR):
    """F_L = (1-alpha) A Kbar^alpha L^-alpha."""
    return (1 - alpha) * A * Kbar ** alpha * L ** (-alpha)


def rK_de_L(L, A, alpha=ALPHA, Kbar=KBAR):
    """F_K = alpha A Kbar^(alpha-1) L^(1-alpha) = alpha * c / Kbar."""
    return alpha * A * Kbar ** (alpha - 1) * L ** (1 - alpha)


def residuo_bruto(L, A, sigma, alpha=ALPHA, psi=PSI, Kbar=KBAR):
    """MRS - MRT written out in full, before any rearrangement.

    psi/(1-L) * c^sigma - (1-alpha) A Kbar^alpha L^-alpha
    """
    c = c_de_L(L, A, alpha, Kbar)
    return psi / (1 - L) * c ** sigma - w_de_L(L, A, alpha, Kbar)


def residuo_compacto(L, A, sigma, alpha=ALPHA, psi=PSI, Kbar=KBAR):
    """The tidied form:  L^(a+(1-a)s)/(1-L) - (1-a)/psi * (A Kbar^a)^(1-s)."""
    lhs = L ** (alpha + (1 - alpha) * sigma) / (1 - L)
    rhs = (1 - alpha) / psi * (A * Kbar ** alpha) ** (1 - sigma)
    return lhs - rhs


def L_equilibrio(A, sigma, compacto=True, **kw):
    """Unique root in (0,1).  LHS of the compact form is strictly increasing."""
    f = residuo_compacto if compacto else residuo_bruto
    return brentq(lambda L: f(L, A, sigma, **kw), 1e-12, 1 - 1e-12,
                  xtol=1e-15, rtol=8.9e-16)


def elasticidade_L(L, sigma, alpha=ALPHA):
    """d ln L / d ln A = (1-sigma) / (alpha + (1-alpha) sigma + L/(1-L))."""
    return (1 - sigma) / (alpha + (1 - alpha) * sigma + L / (1 - L))


def elasticidades(A, sigma, alpha=ALPHA, **kw):
    """Returns (L, eps_L, eps_w, eps_rK, eps_c) -- all d ln x / d ln A."""
    L = L_equilibrio(A, sigma, alpha=alpha, **kw)
    eL = elasticidade_L(L, sigma, alpha)
    ew = 1 - alpha * eL                 # w = (1-a) A Kbar^a L^-a
    erK = 1 + (1 - alpha) * eL          # r^K = a A Kbar^(a-1) L^(1-a)
    ec = 1 + (1 - alpha) * eL           # c   = A Kbar^a L^(1-a)   -- same
    return L, eL, ew, erK, ec


def juro_equilibrio(A1, A2_, sigma, beta=BETA, alpha=ALPHA, **kw):
    """1+r = (1/beta) [ (A2/A1) (L2/L1)^(1-alpha) ]^sigma, from the Euler eq."""
    L1 = L_equilibrio(A1, sigma, alpha=alpha, **kw)
    L2 = L_equilibrio(A2_, sigma, alpha=alpha, **kw)
    return (1 / beta) * ((A2_ / A1) * (L2 / L1) ** (1 - alpha)) ** sigma - 1


# =============================================================== QUESTION 2
def FK(K, A=A2, alpha=ALPHA2):
    """Marginal product of capital with L=1."""
    return alpha * A * K ** (alpha - 1)


def K_ss(beta=BETA, A=A2, alpha=ALPHA2, delta=DELTA):
    """F_K(K,1) - delta = 1/beta - 1   =>   K = [aA/(1/b-1+d)]^(1/(1-a))."""
    return (alpha * A / (1 / beta - 1 + delta)) ** (1 / (1 - alpha))


def c_ss(K, A=A2, alpha=ALPHA2, delta=DELTA):
    """Resource constraint with K_{t+1}=K_t:  c = A K^a - delta K."""
    return A * K ** alpha - delta * K


def K_gr(A=A2, alpha=ALPHA2, delta=DELTA):
    """Golden rule: F_K(K,1) = delta."""
    return (alpha * A / delta) ** (1 / (1 - alpha))


def r_ss(beta=BETA):
    """Steady-state interest rate.  Depends on beta and nothing else."""
    return 1 / beta - 1


def passo(K, c, beta=BETA, sigma=2.0, A=A2, alpha=ALPHA2, delta=DELTA):
    """One period of the two difference equations (9.3.14) and (9.3.15)."""
    K1 = (1 - delta) * K + A * K ** alpha - c
    if K1 <= 0:
        return K1, np.nan
    c1 = c * (beta * (1 + FK(K1, A, alpha) - delta)) ** (1 / sigma)
    return K1, c1


def caminho(K0, c0, T=400, **kw):
    K, c = np.empty(T + 1), np.empty(T + 1)
    K[0], c[0] = K0, c0
    for t in range(T):
        K[t + 1], c[t + 1] = passo(K[t], c[t], **kw)
        if not np.isfinite(c[t + 1]) or K[t + 1] <= 0:
            K[t + 1:], c[t + 1:] = np.nan, np.nan
            break
    return K, c


def c_saddle(K0, T=300, **kw):
    """Shoot on c0 to find the point of the saddle path above K0.

    Classification is by which way the path falls off the saddle, and the two
    failure modes are unambiguous:
      * c0 too HIGH -> the economy eats its capital and K collapses to zero;
      * c0 too LOW  -> K overshoots the steady state, F_K - delta falls below
        1/beta - 1, and consumption collapses to zero instead.
    Bisect on that dichotomy.
    """
    beta = kw.get("beta", BETA)
    A = kw.get("A", A2)
    alpha = kw.get("alpha", ALPHA2)
    delta = kw.get("delta", DELTA)
    Kstar = K_ss(beta, A, alpha, delta)
    cstar = c_ss(Kstar, A, alpha, delta)

    def cai_por_capital(c0):
        """True if capital collapses first (c0 too high), False otherwise."""
        K, c = K0, c0
        for _ in range(T):
            K, c = passo(K, c, **kw)
            if not np.isfinite(K) or not np.isfinite(c):
                return True
            if K <= 1e-8:
                return True                     # capital gone: c0 too high
            if K > 3 * Kstar or c <= 1e-8:
                return False                    # overshot: c0 too low
        return K < Kstar                        # still inside: use the side

    lo, hi = 1e-12, cstar + K0                  # lo: too low, hi: too high
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if cai_por_capital(mid):
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)
