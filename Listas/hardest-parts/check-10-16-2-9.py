"""Checks for Romer 10.16 and 2.9 (hardest-parts/romer-10-16.tex, hardest-parts/romer-2-9.tex).

Every claim checked is an assert; the script prints 'all checks passed' only if all hold.
Run: python check-10-16-2-9.py
"""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

rng = np.random.default_rng(0)


def vanishes(expr, syms):
    """True if expr simplifies to 0; otherwise True only if it is ~0 at random points with every
    symbol in syms drawn from (0.05, 0.9). The fallback exists because sympy does not always clear
    fractional powers such as (k**(1 - alpha))**(1/(1 - alpha))."""
    if sp.simplify(expr) == 0:
        return True
    for _ in range(6):
        val = sp.N(expr.subs({s: rng.uniform(0.05, 0.9) for s in syms}), 30)
        if abs(complex(val)) > 1e-12:
            return False
    return True


# ---------------- Romer 10.16 ----------------
U, V, y, c, phi = sp.symbols('U V y c phi', positive=True)
M = sp.Function('M')(U, V)
q, MV = M / V, sp.diff(M, V)
eta = V * MV / M
Wprime = MV * y - c                     # planner FOC (10.74) with a general M
free_entry = q * (1 - phi) * y - c      # free entry (10.71) with a general M
assert sp.simplify(Wprime - free_entry - q * y * (eta - (1 - phi))) == 0
# social - private = gain to workers - congestion on other firms
assert sp.simplify(MV * y - q * (1 - phi) * y - (phi * y * MV - (1 - phi) * y * (q - MV))) == 0

Mex = U * V / (1 + U + V)               # neither Cobb-Douglas nor constant returns
assert sp.simplify(V * sp.diff(Mex, V) / Mex - (1 + U) / (1 + U + V)) == 0
assert sp.simplify(sp.diff(Mex, V, 2) + 2 * U * (1 + U) / (1 + U + V)**3) == 0     # M_VV < 0
assert sp.simplify(Mex.subs({U: 2 * U, V: 2 * V}, simultaneous=True) - 2 * Mex) != 0  # not CRS
f_q = sp.lambdify((U, V), Mex / V)
f_MV = sp.lambdify((U, V), sp.diff(Mex, V))
f_eta = sp.lambdify((U, V), (1 + U) / (1 + U + V))


def search(Uv, yv, cv, ph):
    """V^EQ from free entry (F) and V* from the planner FOC (P), both by root-finding."""
    veq = brentq(lambda v: f_q(Uv, v) * (1 - ph) * yv - cv, 1e-9, 1e6, xtol=1e-14)
    vst = brentq(lambda v: f_MV(Uv, v) * yv - cv, 1e-9, 1e6, xtol=1e-14)
    return veq, vst, f_eta(Uv, veq)


veq, vst, e = search(1, 8, 1, 0.5)      # eta(V^EQ) = 1 - phi: efficient
assert abs(veq - 2) < 1e-9 and abs(vst - 2) < 1e-9 and abs(e - 0.5) < 1e-9
veq, vst, e = search(1, 8, 1, 0.25)     # eta < 1 - phi: too many vacancies
assert abs(veq - 4) < 1e-9 and abs(vst - 2) < 1e-9 and abs(e - 1 / 3) < 1e-9 and veq > vst
veq, vst, e = search(1, 8, 1, 0.6)      # eta > 1 - phi: too few vacancies
assert abs(veq - 1.2) < 1e-9 and abs(e - 0.625) < 1e-9 and e > 0.4 and veq < vst
phi3 = 1 - np.sqrt((1 + 3) / (8 * 3))   # efficient share at U = 3: 1-phi = [c(1+U)/(yU)]^(1/2)
veq, vst, e = search(3, 8, 1, phi3)
assert abs(veq - vst) < 1e-9 and abs(e - (1 - phi3)) < 1e-9 and abs(phi3 - 0.59175) < 1e-5

# ---------------- Romer 2.9 ----------------
k, cc, al, rho, n, g, t, z0 = sp.symbols('k c alpha rho n g t z0', positive=True)
theta = al
kdot = k**al - cc - (n + g) * k                       # (2.25), no depreciation
gc = (al * k**(al - 1) - rho - theta * g) / theta     # (2.24): cdot/c
z, x = k**(1 - al), cc / k
kstar = (al / (rho + al * g))**(1 / (1 - al))
xs, zs = (rho - al * n) / al, al / (rho + al * g)
cstar = xs * kstar
beta = rho - n - (1 - theta) * g
lam = (1 - al) / zs

# (a), (b)
assert vanishes(gc.subs(k, kstar), [al, rho, g])
assert vanishes(kdot.subs({k: kstar, cc: cstar}), [al, rho, n, g])
assert vanishes(zs - kstar**(1 - al), [al, rho, g])
assert sp.expand(beta + (1 - al) * (n + g) - (rho - al * n)) == 0
# (c)
assert vanishes(sp.diff(z, k) * kdot - (1 - al) * (1 - (x + n + g) * z), [k, cc, al, n, g])
assert vanishes(gc - kdot / k - (x - xs), [k, cc, al, rho, n, g])
# (d) x = 1/u with u(t) = 1/x* + (u0 - 1/x*) e^{x* t}; blow-up time when x0 = x* + d > x*
x0, xsym, d = sp.symbols('x0 xs d', positive=True)
u = 1 / xsym + (1 / x0 - 1 / xsym) * sp.exp(xsym * t)
assert vanishes(sp.diff(1 / u, t) - (1 / u) * (1 / u - xsym), [x0, xsym, t])
assert sp.simplify(u.subs(x0, xsym + d).subs(t, sp.log((xsym + d) / d) / xsym)) == 0
assert vanishes(xs + n + g - 1 / zs, [al, rho, n, g])
assert vanishes(lam - (1 - al) * (rho + al * g) / al, [al, rho, g])
# (d)-(e) closed form satisfies (2.24) and (2.25) identically
zt = zs + (z0 - zs) * sp.exp(-lam * t)
kt = zt**(1 / (1 - al))
ct = xs * kt
assert vanishes(sp.diff(kt, t) - (kt**al - ct - (n + g) * kt), [al, rho, n, g, t, z0])
assert vanishes(sp.diff(ct, t) / ct - (al * kt**(al - 1) - rho - theta * g) / theta,
                [al, rho, n, g, t, z0])
# (2.39) with theta = alpha: mu1 = (beta - sqrt(D))/2 = -lambda iff D = (beta + 2 lambda)^2
# (beta + 2 lambda > 0 since beta > 0); linearized saddle slope beta - mu1 = x*
D = beta**2 + 4 / theta * (1 - al) / al * (rho + theta * g) * (rho + theta * g - al * (n + g))
assert vanishes(D - (beta + 2 * lam)**2, [al, rho, n, g])
assert vanishes(beta + lam - xs, [al, rho, n, g])

# Numerical integration of (2.24)-(2.25) from c(0) = x* k(0) vs the exact z path
P = {al: sp.Rational(1, 3), rho: 0.04, n: 0.01, g: 0.02}
a_, r_, n_, g_ = 1 / 3, 0.04, 0.01, 0.02
ks, xsv, zsv, lamv = (float(ex.subs(P)) for ex in (kstar, xs, zs, lam))
assert float(beta.subs(P)) > 0
k0 = ks / 2


def rhs(_, s):
    kk, cv = s
    return [kk**a_ - cv - (n_ + g_) * kk, cv * (a_ * kk**(a_ - 1) - r_ - a_ * g_) / a_]


T = np.linspace(0, 40, 81)
sol = solve_ivp(rhs, (0, 40), [k0, xsv * k0], t_eval=T, method='DOP853', rtol=1e-12, atol=1e-12)
z_exact = zsv + (k0**(1 - a_) - zsv) * np.exp(-lamv * T)
assert sol.success
assert np.max(np.abs(sol.y[0]**(1 - a_) - z_exact)) < 1e-8
assert np.max(np.abs(sol.y[1] / sol.y[0] - xsv)) < 1e-8      # c/k stays at x*

# Speed of convergence of y (path starts below the BGP, so y* > y)
yt, ys = zt**(al / (1 - al)), zs**(al / (1 - al))
psi_expr = -sp.diff(sp.log(ys - yt), t) / lam
for a_val in (sp.Rational(1, 3), sp.Rational(1, 2)):
    Q = {al: a_val, rho: 0.04, n: 0.01, g: 0.02}
    Q[z0] = (kstar.subs(Q) / 2)**(1 - a_val)
    psi = [float(psi_expr.subs(Q).subs(t, tv)) for tv in (0, 10, 30)]
    if a_val == sp.Rational(1, 2):
        assert np.allclose(psi, 1, atol=1e-12)             # constant speed lambda
    else:
        ref = [float(((1 + ys / yt) / 2).subs(Q).subs(t, tv)) for tv in (0, 10, 30)]
        assert np.allclose(psi, ref, atol=1e-12) and min(psi) > 1 and psi[0] - psi[2] > 0.01

print("all checks passed")
