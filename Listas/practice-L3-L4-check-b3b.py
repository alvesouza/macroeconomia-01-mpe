"""Checks for practice-L3-L4-block3b.tex (Question 6: pension design, symbolic).

Every closed form is checked with sympy (simplify(lhs - rhs) == 0); log/power identities with a
symbolic exponent, and every claimed sign or ordering, at >= 300 random admissible draws; limits
with sp.limit; existence and uniqueness of tau_p and tau_bar by root counting at random draws.
R = 1 + r and G = 1 + n (both > 0), so q = G/R. Run: python practice-L3-L4-check-b3b.py
"""
import math
import random

import numpy as np
import sympy as sp

random.seed(6)
ND = 300
beta, gam, tau, w, alpha, R, G = sp.symbols('beta gamma tau w alpha R G', positive=True)
c1, c2, h, mu, P, Om, x = sp.symbols('c1 c2 h mu P Omega x', positive=True)
q = G / R
om = 1 - tau + tau * q
rho = (1 + beta + gam) / (1 + beta)
ARGS = (beta, gam, tau, w, alpha, R, G)


def zero(e, msg):
    assert sp.simplify(e) == 0, msg


def draw(case):
    """One admissible parameter draw; case in {'gt','lt','eq','any'} for r vs n."""
    if case == 'any':
        case = random.choice(['gt', 'lt', 'eq'])
    n = random.uniform(-0.5, 1.5)
    r = {'gt': n + random.uniform(0.01, 2.0), 'eq': n,
         'lt': random.uniform(max(-0.95, n - 2.0), n - 0.005)}[case]
    return dict(beta=random.uniform(0.02, 0.98), gam=math.exp(random.uniform(-3, 1.6)),
                tau=random.uniform(0.01, 0.99), w=random.uniform(0.1, 10),
                alpha=random.uniform(0.05, 0.95), R=1 + r, G=1 + n)


def holds(expr, pred, case, msg, cond=None):
    """Assert pred(value) at ND draws (draws failing cond are redrawn)."""
    f = sp.lambdify(ARGS, expr, 'math')
    k = 0
    while k < ND:
        d = draw(case)
        if cond and not cond(d):
            continue
        v = f(d['beta'], d['gam'], d['tau'], d['w'], d['alpha'], d['R'], d['G'])
        assert pred(v), f'{msg}: {v} at {d}'
        k += 1


def same(e1, e2, case, msg, cond=None):
    holds(e1 - e2, lambda v: abs(v) < 1e-9, case, msg, cond)


# ---------------- (a) funded and Bismarck ----------------
lifetime = c1 + ((R) * ((1 - tau) * w * h - c1) + P) / R          # c1 + c2/(1+r) from period budgets
zero(lifetime.subs(P, R * tau * w * h) - w * h, 'funded omega = 1')
zero(lifetime.subs(P, G * tau * w * h) - om * w * h, 'Bismarck lifetime budget')
zero(om - (1 - tau * ((R - 1) - (G - 1)) / R), 'omega = 1 - tau(r-n)/(1+r)')
zero(om - q - (1 - tau) * (1 - q), 'omega - q'); zero(1 - om - tau * (1 - q), '1 - omega')
holds(om - q, lambda v: v > 0, 'gt', 'omega > q'); holds(1 - om, lambda v: v > 0, 'gt', 'omega < 1')
zero(R * om - ((1 - tau) * R + tau * G), '(1+r) omega'); holds(om, lambda v: v > 0, 'any', 'omega > 0')

foc = [1 / c1 - mu, beta / c2 - mu / R, gam / (1 - h) - mu * Om * w, c1 + c2 / R - Om * w * h]
sol = sp.solve(foc, [c1, c2, h, mu], dict=True)
assert len(sol) == 1, 'unique FOC solution (a)'
sol = sol[0]
hF = (1 + beta) / (1 + beta + gam)
zero(sol[c1] - Om * w / (1 + beta + gam), 'c1 (a)')
zero(sol[c2] - beta * R * Om * w / (1 + beta + gam), 'c2 (a)')
zero(sol[h] - hF, 'h (a)')
assert sp.diff(sol[h], Om) == 0 and sp.diff(sol[h], w) == 0, 'hours independent of omega, w'
zero(sol[c1].subs(Om, om) / sol[c1].subs(Om, 1) - om, 'Bismarck scales consumption by omega')

# ---------------- (b) Beveridge ----------------
focB = [1 / c1 - mu, beta / c2 - mu / R, gam / (1 - h) - mu * (1 - tau) * w,
        c1 + c2 / R - (1 - tau) * w * h - P / R]
solB = sp.solve(focB, [c1, c2, h, mu], dict=True)
assert len(solB) == 1, 'unique FOC solution (b)'
hP = solB[0][h]
heq = sp.solve(sp.Eq(h, hP.subs(P, G * tau * w * h)), h)
assert len(heq) == 1, 'unique equilibrium hours'
hBev = (1 + beta) * (1 - tau) / ((1 + beta) * (1 - tau) + gam * om)
zero(heq[0] - hBev, 'h_Bev closed form')
X = (1 - tau) / om
zero(hBev - ((1 + beta) * x / ((1 + beta) * x + gam)).subs(x, X), 'h_Bev in x')
zero(((1 + beta) * x / ((1 + beta) * x + gam)).subs(x, 1) - hF, 'h_F = h(x=1)')
zero(om - (1 - tau) - q * tau, 'omega - (1 - tau) = q tau')
holds(hF - hBev, lambda v: v > 0, 'any', 'h_Bev < h_F')
assert sp.limit(hBev, tau, 1) == 0, 'h_Bev -> 0 as tau -> 1'
for qq, curve in [(sp.Rational(1, 2), lambda t: sp.Rational(9, 5) * (1 - t) / (sp.Rational(9, 5) * (1 - t) + (1 - t + t / 2))),
                  (1, lambda t: sp.Rational(9, 5) * (1 - t) / (sp.Rational(9, 5) * (1 - t) + 1))]:
    zero(hBev.subs({beta: sp.Rational(4, 5), gam: 1}).subs(G, qq * R) - curve(tau), 'plotted curve')
assert abs(float(hF.subs({beta: 0.8, gam: 1})) - 0.642857) < 1e-6, 'plotted h_F'
zero((1 - tau) - om * (1 - q * tau / om), 'Beveridge marginal wage = omega w (1 - q tau/omega)')
Qs = sp.symbols('Q', positive=True)
zero(sp.diff(Qs * tau / (1 - tau + tau * Qs), Qs) - tau * (1 - tau) / (1 - tau + tau * Qs) ** 2, 'wedge rises with q')
gap = (hBev.subs(G, R / 2) - hBev.subs(G, R)).subs({beta: sp.Rational(4, 5), gam: 1})
assert all(gap.subs(tau, t / 100) > 0 for t in range(1, 100)), 'r=n curve below r>n curve'

# ---------------- (c) saving and capital ----------------
XBev = (1 - tau) * w + q * tau * w * hBev
XBis = om * w
xw = om * (1 + beta + gam) / (1 + beta)
zero((1 - tau) / hBev - ((1 - tau) + gam * om / (1 + beta)), '(1 - tau)/h_Bev')
zero(XBev / (w * hBev) - xw, 'X/(wh) Beveridge'); zero(XBis / (w * hF) - xw, 'X/(wh) Bismarck')
zero(XBev / (1 + beta + gam) / (w * hBev) - om / (1 + beta), 'c1/(wh) Beveridge')
zero(sol[c1].subs(Om, om) / (w * hF) - om / (1 + beta), 'c1/(wh) Bismarck')
sP = (1 - tau) - om / (1 + beta)
zero(sP - (beta - tau * (beta + q)) / (1 + beta), 's_PAYG closed form')
sBis = (1 - tau) - sol[c1].subs(Om, om) / (w * hF)              # no pension assets: national = private saving
sBev = (1 - tau) - XBev / (1 + beta + gam) / (w * hBev)
zero(sBis - sP, 's_Bis = s_PAYG'); zero(sBev - sP, 's_Bev = s_PAYG')
c1F = sol[c1].subs(Om, 1)
zero(c1F - w * hF / (1 + beta), 'funded c1 = wh/(1+beta)')
aF = (1 - tau) - c1F / (w * hF)
zero(aF - (beta / (1 + beta) - tau), 'funded private saving')
sF = aF + tau
zero(sF - beta / (1 + beta), 's_F')
zero(sF - sP - tau * (beta + q) / (1 + beta), 's_F - s_PAYG')
zero(sF - sP - (tau - (1 - om) / (1 + beta)), 's_F - s_PAYG decomposition')
holds(sF - sP, lambda v: v > 0, 'any', 's_PAYG < s_F')
rt = sp.solve(sP, tau)                                 # s_PAYG is decreasing in tau (checked in (e))
assert len(rt) == 1 and sp.simplify(rt[0] - beta / (beta + q)) == 0, 's_PAYG > 0 iff tau < beta/(beta+q)'
zero(sP / sF - (1 - tau * (1 + q / beta)), 's ratio')
dlt, gg, nn = sp.symbols('delta g nu', positive=True)
ys = lambda s: (s / (dlt + nn + gg)) ** (alpha / (1 - alpha))      # Kurlat 4.5 steady state
ratio = (sP / sF) ** (alpha / (1 - alpha))
pos = lambda d: d['tau'] < d['beta'] / (d['beta'] + d['G'] / d['R'])
for e in (ys(sP) / ys(sF), ys((1 - alpha) * sP) / ys((1 - alpha) * sF)):
    same(e.subs({dlt: 0.07, gg: 0.02, nn: 0.01}), ratio, 'any', 'Solow ratio', pos)
holds(ratio, lambda v: 0 < v < 1, 'any', 'ratio in (0,1)', pos)

# ---------------- (d) welfare ----------------
U = lambda a1, a2, hh: sp.log(a1) + gam * sp.log(1 - hh) + beta * sp.log(a2)
c1Bis = sol[c1].subs(Om, om); c1Bev = XBev / (1 + beta + gam)
UF = U(c1F, beta * R * c1F, hF)
UBis = U(c1Bis, beta * R * c1Bis, hF)
UBev = U(c1Bev, beta * R * c1Bev, hBev)
same(UBis - UF, (1 + beta) * sp.log(om), 'any', 'U_Bis - U_F')
lamBis = 1 - om
zero(lamBis - tau * ((R - 1) - (G - 1)) / R, 'lambda_Bis')
oneLamBev = (1 - tau) * ((1 + beta + gam) * om / ((1 + beta) * (1 - tau) + gam * om)) ** rho
same(sp.exp((UBev - UF) / (1 + beta)), oneLamBev, 'any', 'lambda_Bev closed form')
same(om * hBev / hF * ((1 - hBev) / (1 - hF)) ** (gam / (1 + beta)), oneLamBev, 'any', 'lambda_Bev middle form')
zero(c1Bev / c1F - om * hBev / hF, 'c_Bev/c_F')
zero(hBev / hF - ((1 + beta + gam) * x / ((1 + beta) * x + gam)).subs(x, X), 'h ratio')
zero((1 - hBev) / (1 - hF) - ((1 + beta + gam) / ((1 + beta) * x + gam)).subs(x, X), 'leisure ratio')
zero(c1Bev + beta * R * c1Bev / R - om * w * hBev, 'Beveridge allocation on Bismarck budget')
holds(UBis - UBev, lambda v: v > 0, 'any', 'U_Bev < U_Bis')
holds(UF - UBis, lambda v: v > 0, 'gt', 'U_F > U_Bis'); holds(lamBis, lambda v: v < 0, 'lt', 'lambda_Bis < 0 if r < n')
assert sp.simplify(lamBis.subs(G, R)) == 0, 'lambda_Bis = 0 at r = n'
lamEq = 1 - (1 - tau) * ((1 + beta + gam) / ((1 + beta) * (1 - tau) + gam)) ** rho
same((1 - oneLamBev).subs(G, R), lamEq, 'eq', 'lambda_Bev at r = n')
holds(lamEq, lambda v: v > 0, 'eq', 'lambda_Bev > 0 at r = n')
b = 1 - gam * q / (1 + beta + gam)
zero((1 + beta) * (1 - tau) + gam * om - (1 + beta + gam) * (1 - b * tau), 'b identity')
L = sp.log(1 - tau) + rho * sp.log(om) - rho * sp.log(1 - b * tau)
same(L, sp.log(oneLamBev), 'any', 'L = ln(1 - lambda_Bev)')
Lp = sp.diff(L, tau)
N = q * (1 - tau) - om * (1 - b * tau)
zero(Lp - (q / (om * (1 - b * tau)) - 1 / (1 - tau)), "L'")
zero(Lp - N / ((1 - tau) * om * (1 - b * tau)), "L' = N/(...)")
zero(L.subs(tau, 0), 'L(0) = 0'); zero(Lp.subs(tau, 0) - (q - 1), "L'(0) = q - 1")
zero(N.subs(tau, 0) - (q - 1), 'N(0)'); zero(N.subs(tau, 1) + gam * q ** 2 / (1 + beta + gam), 'N(1)')
assert sp.degree(sp.expand(N * R ** 2 * (1 + beta + gam)), tau) <= 2, 'deg N <= 2'
fL = sp.lambdify(ARGS, L, 'math'); fLp = sp.lambdify(ARGS, Lp, 'math')
Ncoef = [sp.lambdify(ARGS, cf, 'math') for cf in sp.Poly(sp.expand(N), tau).all_coeffs()]
grid = sorted(set([k / 4000 for k in range(1, 4000)] + [1 - 10.0 ** (-k) for k in range(4, 15)]))
for _ in range(ND):
    d = draw('lt'); a = [d['beta'], d['gam'], 0, d['w'], d['alpha'], d['R'], d['G']]
    co = [f(*a) for f in Ncoef]
    rts = [z.real for z in np.roots(co) if abs(z.imag) < 1e-12 and 0 < z.real < 1]
    assert len(rts) == 1, f'unique tau_p {co}'
    tp = rts[0]
    Lv = [fL(*(a[:2] + [t] + a[3:])) for t in grid]
    sc = [i for i in range(len(grid) - 1) if (Lv[i] > 0) != (Lv[i + 1] > 0)]
    assert len(sc) == 1 and Lv[0] > 0, 'unique tau_bar'
    lo, hi = grid[sc[0]], grid[sc[0] + 1]
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if fL(*(a[:2] + [mid] + a[3:])) > 0 else (lo, mid)
    assert tp < lo, 'tau_bar > tau_p'
    for t in grid[:-11]:
        v = fLp(*(a[:2] + [t] + a[3:]))
        assert (v > 0) == (t < tp) or abs(t - tp) < 1e-3, "L' sign vs tau_p"
for case in ('gt', 'eq'):
    for _ in range(ND):
        d = draw(case); a = [d['beta'], d['gam'], 0, d['w'], d['alpha'], d['R'], d['G']]
        assert all(fLp(*(a[:2] + [t] + a[3:])) < 0 for t in grid[:-11:20]), "L' < 0 if r >= n"
for _ in range(10):
    sub = {beta: sp.Rational(random.randint(1, 9), 10), gam: sp.Rational(random.randint(1, 40), 10),
           R: sp.Rational(random.randint(50, 250), 100), G: sp.Rational(random.randint(50, 250), 100)}
    assert sp.limit(L.subs(sub), tau, 1, '-') == -sp.oo, 'L -> -oo as tau -> 1'

# ---------------- (e) parameter analysis ----------------
zero(sp.diff(om, R) + tau * G / R ** 2, 'domega/dr'); zero(sp.diff(om, G) - tau / R, 'domega/dn')
zero(sp.diff(om, tau) - (q - 1), 'domega/dtau'); zero(q - 1 + ((R - 1) - (G - 1)) / R, 'q - 1 = -(r-n)/(1+r)')
zero(sp.diff((1 + beta) * x / ((1 + beta) * x + gam), x) - (1 + beta) * gam / ((1 + beta) * x + gam) ** 2, 'dh/dx')
zero(sp.diff(X, tau) + q / om ** 2, 'dx/dtau')
zero(sp.diff(X, R) + X / om * sp.diff(om, R), 'dx/dr'); zero(sp.diff(X, G) + X / om * sp.diff(om, G), 'dx/dn')
for e, var, sg, case in [(hBev, tau, -1, 'any'), (hBev, R, 1, 'any'), (hBev, G, -1, 'any'),
                         (sP, R, 1, 'any'), (sP, G, -1, 'any'), (sP, tau, -1, 'any'),
                         (lamBis, R, 1, 'any'), (lamBis, G, -1, 'any'), (lamBis, tau, 1, 'gt'), (lamBis, tau, -1, 'lt'),
                         (om, tau, -1, 'gt'), (om, tau, 1, 'lt'),
                         # 1 - oneLamBev is lambda_Bev itself
                         (1 - oneLamBev, R, 1, 'any'), (1 - oneLamBev, G, -1, 'any'), (1 - oneLamBev, tau, 1, 'gt'),
                         (1 - oneLamBev, tau, 1, 'eq')]:
    holds(sp.diff(e, var), lambda v, s=sg: s * v > 0, case, f'sign d{e}/d{var}')
for var, sg in [(R, 1), (G, -1), (tau, -1)]:
    holds(sp.diff(ratio, var), lambda v, s=sg: s * v > 0, 'any', f'sign dratio/d{var}', pos)
zero(sp.diff(sP, R) - tau * G / ((1 + beta) * R ** 2), 'ds/dr'); zero(sp.diff(sP, G) + tau / ((1 + beta) * R), 'ds/dn')
zero(sp.diff(sP, tau) + (beta + q) / (1 + beta), 'ds/dtau')
assert all(sp.diff(e, v) == 0 for e in (hF, sF) for v in (R, G, tau)), 'h_F, s_F constant'
Fom = sp.log(1 - tau) + rho * sp.log((1 + beta + gam) * Om / ((1 + beta) * (1 - tau) + gam * Om))
zero(sp.diff(Fom, Om) - rho * (1 + beta) * (1 - tau) / (Om * ((1 + beta) * (1 - tau) + gam * Om)), 'dln(1-lam)/domega')
phi = sp.log(x) + rho * sp.log((1 + beta + gam) / ((1 + beta) * x + gam))
zero(phi.subs(x, 1), 'phi(1) = 0')
zero(sp.diff(phi, x) - gam * (1 - x) / (x * ((1 + beta) * x + gam)), "phi'")
zero(sp.diff(phi, x, 2).subs(x, 1) + gam / (1 + beta + gam), "phi''(1)")
same(om * sp.exp(phi.subs(x, X)), oneLamBev, 'any', '1 - lambda_Bev = omega e^phi')
same(sp.log(om) + phi.subs(x, X), L, 'any', 'L = ln omega + phi(x)')
same((q - 1) / om - sp.diff(phi, x).subs(x, X) * q / om ** 2, Lp, 'any', "L' via phi")
holds(phi.subs(x, X), lambda v: v < 0, 'any', 'phi(x) < 0 on (0,1)')
zero(X - 1 + q * tau / om, 'x - 1 = -q tau/omega')
for e, lim in [(om, 1), (X, 1), (hBev, hF), (sP, sF), (ratio, 1), (lamBis, 0), (1 - oneLamBev, 0)]:
    zero(sp.limit(e, tau, 0) - lim, f'limit tau->0 of {e}')
exc = om - oneLamBev                                    # lambda_Bev - lambda_Bis
zero(exc.subs(tau, 0), 'excess(0)'); zero(sp.diff(exc, tau).subs(tau, 0), "excess'(0) = 0")
zero(sp.diff(exc, tau, 2).subs(tau, 0) - gam * q ** 2 / (1 + beta + gam), 'Harberger second-order term')
zero(Om * w * (1 - sol[h]) / (Om * w) - gam / (1 + beta + gam), 'leisure share of full income')
zero(sp.diff(gam / (1 + beta + gam), gam) - (1 + beta) / (1 + beta + gam) ** 2, 'leading term rises with gamma')
for e, lim in [(om, 1), (lamBis, 0), (hBev, (1 + beta) * (1 - tau) / ((1 + beta) * (1 - tau) + gam)),
               (sP, sF - tau), (1 - oneLamBev, lamEq)]:
    zero(sp.limit(e, G, R) - lim, f'limit r->n of {e}')
holds(hF - (1 + beta) * (1 - tau) / ((1 + beta) * (1 - tau) + gam), lambda v: v > 0, 'any', 'h_Bev(r=n) < h_F')
print('practice-L3-L4-check-b3b.py: all checks passed')
