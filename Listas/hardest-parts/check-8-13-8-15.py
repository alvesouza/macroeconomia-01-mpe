"""Checks for Romer 8.13 and 8.15 (hardest-parts/romer-8-13.tex, romer-8-15.tex).

Every claim checked is an assert: Euler equations, the linearization, the exact
internal-habit path, the three consumption plans, naive = sophisticated under
log utility, and the CRRA ordering. Prints 'all checks passed' only if all hold.
Run: python check-8-13-8-15.py
"""
import numpy as np
import sympy as sp
from scipy.optimize import minimize, minimize_scalar

rng = np.random.default_rng(0)
th, rho, r, phi, dC, eps = sp.symbols('theta rho r phi dC epsilon', real=True)
beta = 1 / (1 + rho)


def u(c, z):
    """Romer 8.13 period utility (C/Z)^(1-theta)/(1-theta); c own consumption,
    z reference level (sympy expressions)."""
    return (c / z)**(1 - th) / (1 - th)


def vanishes(expr, syms, n=20):
    """True if sympy expr is ~0 (abs < 1e-10) at n random points of syms:
    theta in (0.2, 0.9) or (1.1, 4), rho and r in (0, 0.2), phi in (0, 1),
    every other symbol (a consumption level) in (0.5, 2)."""
    f = sp.lambdify(syms, expr, 'numpy')
    for _ in range(n):
        vals = []
        for sym in syms:
            if sym == th:
                vals.append(rng.choice([rng.uniform(0.2, 0.9),
                                        rng.uniform(1.1, 4)]))
            elif sym in (rho, r):
                vals.append(rng.uniform(0, 0.2))
            elif sym == phi:
                vals.append(rng.uniform(0, 1))
            else:
                vals.append(rng.uniform(0.5, 2))
        if abs(f(*vals)) > 1e-10:
            return False
    return True


# ---- 8.13(a)(i): external habits, Z_it = C_{t-1}^phi -----------------------
ci0, ci1, A0, A1 = sp.symbols('C_it C_it1 C_tm1 C_t', positive=True)
dU = sp.diff(u(ci0 - dC, A0**phi) + beta * u(ci1 + (1 + r) * dC, A1**phi),
             dC).subs(dC, 0)
ratio = ((1 + r) / (1 + rho))**(1 / th) * (A1 / A0)**(phi * (th - 1) / th)
assert vanishes(dU.subs(ci1, ci0 * ratio), [ci0, A0, A1, th, rho, r, phi]), \
    "8.13(a)(i) Euler ratio"

# ---- 8.13(a)(ii): equilibrium coefficient b = phi(theta-1)/theta -----------
b = lambda f, t: f * (t - 1) / t
assert all(b(f, 1.0) == 0 for f in np.linspace(0.1, 1, 10)), "b=0 at theta=1"
for f in np.linspace(0.05, 1, 20):
    for t in np.linspace(1.05, 20, 50):
        assert 0 < b(f, t) < 1, "0<b<1 for theta>1"
        assert 1 <= t - f * (t - 1) + 1e-12 and t - f * (t - 1) < t
f_, t_, r_, rho_ = 0.8, 3.0, 0.05, 0.02
a_ = (np.log(1 + r_) - np.log(1 + rho_)) / t_
x = 0.2
for _ in range(400):
    x = a_ + b(f_, t_) * x
xstar = (np.log(1 + r_) - np.log(1 + rho_)) / (t_ - f_ * (t_ - 1))
assert abs(x - xstar) < 1e-12, "8.13(a)(ii) steady-state growth"

# ---- 8.13(b)(i): internal habits, Z_it = C_{i,t-1} -------------------------
cm1, c0, c1, c2 = sp.symbols('C_tm1 C_t C_tp1 C_tp2', positive=True)
U3 = (u(c0 - dC, cm1) + beta * u(c1 + (1 + r) * dC, c0 - dC)
      + beta**2 * u(c2, c1 + (1 + r) * dC))
D = sp.diff(U3, dC).subs(dC, 0)
M_t = c0**-th * cm1**(th - 1) - beta * c1**(1 - th) * c0**(th - 2)
M_t1 = c1**-th * c0**(th - 1) - beta * c2**(1 - th) * c1**(th - 2)
lev = [cm1, c0, c1, c2, th, rho, r]
assert vanishes(D - (-M_t + beta * (1 + r) * M_t1), lev), "8.13(b)(i) Euler"
X0, X1, X2 = c0 / cm1, c1 / c0, c2 / c1
growth = (X1 * (X0**(1 - th) - beta * X1**(1 - th))
          - (1 + r) * beta * (X1**(1 - th) - beta * X2**(1 - th)))
assert vanishes(c1 * (M_t - beta * (1 + r) * M_t1) - growth, lev), \
    "8.13(b)(i) growth form"

# ---- 8.13(b)(ii): first-order expansion with rho = r = 0 -------------------
g0, g1, g2 = sp.symbols('g0 g1 g2', real=True)
Xs = [1 + eps * g for g in (g0, g1, g2)]
F = (Xs[1] * (Xs[0]**(1 - th) - Xs[1]**(1 - th))
     - (Xs[1]**(1 - th) - Xs[2]**(1 - th)))
lin = sp.series(F, eps, 0, 2).removeO()
assert sp.simplify(lin - eps * (1 - th) * (g0 - 2 * g1 + g2)) == 0, \
    "8.13(b)(ii) linearization: second difference of g is zero"
kept = sp.solve(sp.Eq((1 + g1) * (1 - th) * (g0 - g1), (1 - th) * (g1 - g2)),
                g2)[0]
assert sp.simplify(kept - g1 - (1 + g1) * (g1 - g0)) == 0, "interaction kept"

# ---- 8.13(b): exact path, rho = r = 0, theta = 3, T = 6, C_0 = 1, W = 6 -----
T, TH, C0, W = 6, 3.0, 1.0, 6.0


def neg_U(y):
    """Minus lifetime utility (internal habits, rho = 0) at log-consumption y."""
    c = np.exp(np.concatenate(([np.log(C0)], y)))
    return -np.sum((c[1:] / c[:-1])**(1 - TH)) / (1 - TH)


sol = minimize(neg_U, np.full(T, np.log(W / T)), method='SLSQP',
               constraints={'type': 'eq', 'fun': lambda y: np.exp(y).sum() - W},
               options={'ftol': 1e-15, 'maxiter': 2000})
assert sol.success, sol.message
C = np.concatenate(([C0], np.exp(sol.x)))
X = C[1:] / C[:-1]
m = np.append(X**(1 - TH), 0.0)             # m_{T+1} = 0
M = (m[:-1] - m[1:]) / C[1:]                # full marginal utility M_t
R = np.cumsum(C[1:][::-1])[::-1]            # R_t = sum_{s>=t} C_s
assert np.ptp(M) / M.mean() < 1e-5, "8.13(b) M_t constant (Euler)"
assert np.ptp(m[:-1] / R) / M.mean() < 1e-5, "8.13(b) X_t^(1-theta) = mu R_t"
assert np.all(np.diff(X) > 0), "8.13(b) growth rises when theta > 1"
assert X[0] < 1 < X[-1], "U-shaped consumption"
assert round(X[0], 2) == 0.85 and round(X[-1], 2) == 1.60, "printed numbers"
# the trap: theta < 1 unbounded; theta = 1 with rho = 0 telescopes
cpath = lambda e: np.array([1.0, e, 2.0, 2.0])
Uhalf = lambda c: np.sum(np.sqrt(c[1:] / c[:-1])) / 0.5
assert Uhalf(cpath(1e-6)) > Uhalf(cpath(1e-4)) > 100, "theta<1 unbounded"
cr = rng.uniform(0.5, 2, 5)
assert abs(np.sum(np.log(cr[1:] / cr[:-1])) - np.log(cr[-1] / cr[0])) < 1e-12

# ---- 8.15(a): log utility, three plans -------------------------------------
k1, k2, Wd, W2, d, s = sp.symbols('c1 c2 W W2 delta s', positive=True)
U1 = sp.log(k1) + d * sp.log(k2) + d * sp.log(Wd - k1 - k2)
com = sp.solve([sp.diff(U1, k1), sp.diff(U1, k2)], [k1, k2], dict=True)[0]
assert sp.simplify(com[k1] - Wd / (1 + 2 * d)) == 0, "8.15 commitment c1"
assert sp.simplify(com[k2] - d * Wd / (1 + 2 * d)) == 0, "8.15 commitment c2"
rule2 = sp.solve(sp.diff(sp.log(k2) + d * sp.log(W2 - k2), k2), k2)[0]
assert sp.simplify(rule2 - W2 / (1 + d)) == 0, "8.15 date-2 rule"
c1N = Wd / (1 + 2 * d)
c2N, c3N = rule2.subs(W2, Wd - c1N), d * rule2.subs(W2, Wd - c1N)
assert sp.simplify(c2N - 2 * d * Wd / ((1 + d) * (1 + 2 * d))) == 0
assert sp.simplify(c3N - 2 * d**2 * Wd / ((1 + d) * (1 + 2 * d))) == 0
V = (sp.log(k1) + d * sp.log(rule2.subs(W2, Wd - k1))
     + d * sp.log(d * rule2.subs(W2, Wd - k1)))
c1S = sp.solve(sp.diff(V, k1), k1)
assert len(c1S) == 1 and sp.simplify(c1S[0] - c1N) == 0, "8.15 naive = soph."
Vs = sp.log(k1) + d * sp.log(s * (Wd - k1)) + d * sp.log((1 - s) * (Wd - k1))
assert sp.simplify(sp.diff(Vs, k1, s)) == 0, "8.15 share s drops out of FOC"
gain = (U1.subs({k1: c1N, k2: com[k2]})
        - (sp.log(c1N) + d * sp.log(c2N) + d * sp.log(c3N)))
for dv in (0.1, 0.5, 0.9):
    val = float(gain.subs({d: dv, Wd: 3.7}))
    assert abs(val - dv * np.log((1 + dv)**2 / (4 * dv))) < 1e-12 and val > 0


# ---- 8.15: CRRA, delta = 1/2 (closed forms vs numerical optimization) -----
def argmax(f, hi):
    """Maximizer of the scalar function f on the open interval (0, hi)."""
    return minimize_scalar(lambda x: -f(x), bounds=(1e-9, hi - 1e-9),
                           method='bounded', options={'xatol': 1e-12}).x


dl, Wn = 0.5, 1.0
for sg, cS_txt, cN_txt in ((2.0, 0.4106, 0.4142), (0.5, 0.6897, 0.6667)):
    uc = lambda c: c**(1 - sg) / (1 - sg)
    sstar = argmax(lambda c: uc(c) + dl * uc(1 - c), 1.0)    # W2 = 1
    assert abs(sstar - 1 / (1 + dl**(1 / sg))) < 1e-7, "CRRA date-2 share"
    cN = argmax(lambda c: uc(c) + 2 * dl * uc((Wn - c) / 2), Wn)
    assert abs(cN - Wn / (1 + 2 * dl**(1 / sg))) < 1e-7, "CRRA commitment"
    cS = argmax(lambda c: uc(c) + dl * (uc(sstar * (Wn - c))
                                        + uc((1 - sstar) * (Wn - c))), Wn)
    A = sstar**(1 - sg) + (1 - sstar)**(1 - sg)
    assert abs(cS - Wn / (1 + (dl * A)**(1 / sg))) < 1e-7, "CRRA soph."
    assert (cS > cN) == (sg < 1), "sign of c1S - c1N"
    assert round(cS, 4) == cS_txt and round(cN, 4) == cN_txt, "printed numbers"
    assert abs(2**sg - 2 * 0.5**(1 - sg)) < 1e-12, "A(1/2) = 2^sigma"

print("all checks passed")
