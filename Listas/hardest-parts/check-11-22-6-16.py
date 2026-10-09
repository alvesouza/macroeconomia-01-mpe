"""Romer 11.22 and 6.16 (hardest-parts/romer-11-22.tex, romer-6-16.tex): independent checks.

Run: python check-11-22-6-16.py   (aborts on the first failed assert; else "all checks passed").
Labels (1)-(6) and (A)-(D) refer to the equations tagged in the two LaTeX fragments.
"""
import math

import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


def chk(name, value, expected, tol=5e-4):
    """Assert that value matches expected to a relative tol, then print it.

    name labels the printed line; value is the number recomputed here and expected the one
    printed in the .tex. Raises AssertionError on mismatch.
    """
    assert abs(value - expected) <= tol * max(1, abs(expected)), f"{name}: {value} != {expected}"
    print(f"{name:<52} {value:.6f}")


def simulate(f, x0, t_end=60.0, cap=30.0):
    """Integrate d(pi_e)/dt = f(pi_e) from pi_e(0) = x0 until t_end or until pi_e reaches cap.

    f is the law of motion (3) as a float function; reaching cap (m = C e^{-b cap}, i.e. m ~ 0)
    stands for the blow-up. Returns (path of pi_e, final time); final time < t_end iff cap was hit.
    """
    hit = lambda t, y: y[0] - cap
    hit.terminal = True
    s = solve_ivp(lambda t, y: [f(y[0])], (0.0, t_end), [x0], events=hit, rtol=1e-10, atol=1e-12)
    assert s.success
    return s.y[0], s.t[-1]


# ------------------------------------------------------------ Romer 11.22 (a): law of motion
b, beta, C, G, m = sp.symbols("b beta C G m", positive=True)
pe, pi, dpe = sp.symbols("pi_e pi dpi_e", real=True)
# unknowns pi, dpi_e: G = (mdot/m + pi) m with mdot/m = -b dpi_e (eq. 1), and the adaptive rule
sol = sp.solve([sp.Eq(G, (-b * dpe + pi) * m), sp.Eq(dpe, beta * (pi - pe))], [pi, dpe], dict=True)[0]
k = beta / (1 - b * beta)
assert sp.simplify(sol[dpe] - k * (G / m - pe)) == 0                                   # (3)
assert sp.simplify(sol[pi] - (G / m - b * beta * pe) / (1 - b * beta)) == 0            # (4)
Phi = k * (G / C * sp.exp(b * pe) - pe)
assert sp.simplify(sol[dpe].subs(m, C * sp.exp(-b * pe)) - Phi) == 0                   # (3), line 2
# identical to (11.75): mdot/m = -b dpi_e with pi_e = (ln C - ln m)/b
lhs = (-b * sol[dpe]).subs(pe, (sp.log(C) - sp.log(m)) / b)
rhs = b * beta / (1 - b * beta) / m * ((sp.log(C) - sp.log(m)) / b * m - G)
assert sp.simplify(lhs - rhs) == 0
# pi is not monotone in pi_e: d pi / d pi_e = b (g_M - beta)/(1 - b beta), g_M = G/m
pi_of_pe = sol[pi].subs(m, C * sp.exp(-b * pe))
assert sp.simplify(sp.diff(pi_of_pe, pe) - b * (G / C * sp.exp(b * pe) - beta) / (1 - b * beta)) == 0

# ------------------------------------------------------------ Romer 11.22 (b)-(c): shape of Phi
x = sp.Symbol("x", real=True)
S = C * x * sp.exp(-b * x)                                     # steady-state seignorage (11.68)
assert sp.solve(sp.diff(S, x), x) == [1 / b]
Smax = S.subs(x, 1 / b)
assert sp.simplify(Smax - C / (sp.E * b)) == 0
pehat = sp.log(C / (b * G)) / b
assert sp.simplify(sp.diff(Phi, pe).subs(pe, pehat)) == 0
assert sp.simplify(sp.diff(Phi, pe, 2) - k * b**2 * G / C * sp.exp(b * pe)) == 0       # convex
gap = Phi.subs(pe, pehat) - beta / (b * (1 - b * beta)) * sp.log(G / Smax)
assert sp.simplify(sp.expand_log(gap, force=True)) == 0                                # (6)

num = {b: 1, C: 1, beta: sp.Rational(1, 2)}
smax = float(Smax.subs(num))
chk("11.22 S^MAX = 1/e (C = b = 1)", smax, math.exp(-1))
bb, bt = 1.0, 0.5

# (b) G = 1/2 > S^MAX: Phi > 0 everywhere, finite-time collapse of m
Gb = 0.5
f_b = sp.lambdify(pe, Phi.subs(num).subs(G, Gb), "math")
assert Gb > smax and min(f_b(-8 + 0.01 * i) for i in range(1601)) > 0
chk("11.22(b) min Phi = ln(G/S^MAX)", f_b(math.log(2)), math.log(Gb / smax))
path, t_hit = simulate(f_b, 0.0)
t_bar = (1 - bb * bt) * 1.0 / (bb * bt * (Gb - smax))      # m(0) = C e^0 = 1
assert t_hit < t_bar and all(a < c for a, c in zip(path, path[1:]))   # pi_e rises, m falls
assert all(2 * (Gb * math.exp(v) - 0.5 * v) > v for v in path)          # pi > pi_e along the path, by (4)
chk("11.22(b) time at which pi_e hits 30 (< t_bar = 7.57)", t_hit, 4.7466)

# (c) G = 1/4 < S^MAX: two steady states, g1 stable, g2 unstable
Gc = 0.25
f_c = sp.lambdify(pe, Phi.subs(num).subs(G, Gc), "math")
df_c = sp.lambdify(pe, sp.diff(Phi, pe).subs(num).subs(G, Gc), "math")
xh = math.log(1 / Gc)                                       # pehat with C = b = 1
g1, g2 = brentq(f_c, -5, xh), brentq(f_c, xh, 20)
chk("11.22(c) g1", g1, 0.357)
chk("11.22(c) g2", g2, 2.153)
for g in (g1, g2):
    assert abs(g * math.exp(-g) - Gc) < 1e-12               # S(g_i) = G
assert g1 < 1 < g2 and g1 < xh < g2 and df_c(g1) < 0 < df_c(g2)
# signs of (5); the solution manual's text says Phi < 0 outside [g1, g2]: it is > 0
assert f_c(-1) > 0 and f_c(g1 - 0.1) > 0 and f_c((g1 + g2) / 2) < 0 and f_c(g2 + 0.1) > 0
for x0 in (-0.5, 0.0, 1.0, 2.1):
    path, t_end = simulate(f_c, x0)
    assert t_end == 60.0 and abs(path[-1] - g1) < 1e-6
path, t_hit = simulate(f_c, 2.2)
bound = (1 - bb * bt) * math.exp(-2.2) / (bb * bt * (Gc - 2.2 * math.exp(-2.2)))
assert t_hit < bound
chk("11.22(c) m1 = C e^{-b g1} = G/g1", math.exp(-g1), Gc / g1)

# ------------------------------------------------------------ Romer 6.16
phi, q = sp.symbols("phi q", positive=True)
mm, Em, pr, pf, u = sp.symbols("m Em p_r p_f u", real=True)
D = q + phi * (1 - q)
# (a) p_f = (1-phi) p + phi m with p = q p_r + (1-q) p_f
pf_sol = sp.solve(sp.Eq(pf, (1 - phi) * (q * pr + (1 - q) * pf) + phi * mm), pf)[0]
assert sp.simplify(pf_sol - (pr + phi / D * (mm - pr))) == 0                           # (A)
# (b) brute force: E is linear and p_r is known when set, so E p_f is (A) at m = Em
Ep = q * pr + (1 - q) * pf_sol.subs(mm, Em)
pr_sol = sp.solve(sp.Eq(pr, (1 - phi) * Ep + phi * Em), pr)[0]
assert sp.simplify(pr_sol - Em) == 0                                                    # (B)
# (c) price level and output
p_sol = (q * pr + (1 - q) * pf_sol).subs(pr, pr_sol)
y_sol = mm - p_sol
assert sp.simplify(y_sol - q / D * (mm - Em)) == 0                                      # (C)
assert sp.simplify(sp.diff(p_sol, mm) - (1 - q) * phi / D) == 0
y_u = y_sol.subs(mm, Em + u)
assert sp.simplify(sp.diff(y_u, Em)) == 0               # anticipated: m and Em move together
assert sp.simplify(sp.diff(y_u, u) - q / D) == 0        # unanticipated
# AS curve (D) and Benigno's kappa
kappa = (1 - q) * phi / q
Ep_sol = Ep.subs(pr, pr_sol)
assert sp.simplify(Ep_sol - Em) == 0
assert sp.simplify(p_sol - Ep_sol - kappa * y_sol) == 0                                 # (D)
al, sg, et = sp.symbols("alpha sigma eta", positive=True)
kappa_benigno = (1 - al) * (1 / sg + et) / al
assert sp.simplify(kappa.subs({q: al, phi: 1 / sg + et}) - kappa_benigno) == 0
assert sp.simplify(y_sol - (mm - Em) / (1 + kappa)) == 0
dy = sp.diff(q / D, phi)
assert sp.simplify(dy + q * (1 - q) / D**2) == 0
# solution manual: denominator phi + (1-phi) q and its eq. (19)
assert sp.expand(D - (phi + (1 - phi) * q)) == 0
assert sp.simplify(sp.diff(y_sol, phi) + (1 - q) * q * (mm - Em) / (phi + (1 - phi) * q) ** 2) == 0
for qv in (0.1, 0.5, 0.9):
    for fv in (0.05, 0.5, 1.0, 3.0):
        r = float((q / D).subs({q: qv, phi: fv}))
        assert 0 < r < 1 and float(dy.subs({q: qv, phi: fv})) < 0
assert sp.limit(q / D, phi, 0) == 1 and sp.limit(q / D, phi, sp.oo) == 0
assert sp.simplify((q / D).subs(phi, 1) - q) == 0
kb = float(kappa_benigno.subs({al: 0.66, sg: 0.5, et: 0.2}))
chk("6.16 kappa, Benigno calibration", kb, 1.1333)
chk("6.16 output effect 1/(1+kappa)", 1 / (1 + kb), 0.46875)
kr = float(kappa.subs({q: 0.66, phi: 0.2}))
chk("6.16 kappa, phi = 0.2", kr, 0.1030)
chk("6.16 output effect, phi = 0.2", 1 / (1 + kr), 0.9066)

print("all checks passed")
