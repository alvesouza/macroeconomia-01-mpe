"""Romer 4.8 and 8.1 (romer-4-8.tex, romer-8-1.tex): independent check of every key result.

Run: python check-4-8-8-1.py   (aborts on the first failed assert).
Identities with symbolic exponents are checked at random parameter draws; dynamics with scipy.
"""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

rng = np.random.default_rng(0)


def chk(name, value, expected, tol=5e-4):
    assert abs(value - expected) <= tol * max(1, abs(expected)), f"{name}: {value} != {expected}"
    print(f"{name:<44} {value:.5f}")


def zero_at(expr, draws, tol=1e-9):
    """Assert expr vanishes at every draw (dict symbol -> number), relative to its largest term."""
    for d in draws:
        scale = max([1.0] + [abs(float(sp.N(a.subs(d)))) for a in sp.Add.make_args(sp.expand(expr))])
        v = float(sp.N(expr.subs(d)))
        assert abs(v) < tol * scale, f"{expr} = {v} at {d}"


# ===================== Romer 4.8 =====================
al, ga, ph, s, B, aK, aH, n, g, dK, dH, r = sp.symbols(
    "alpha gamma phi s B a_K a_H n g delta_K delta_H r", positive=True)
k, h = sp.symbols("k h", positive=True)
xK, xH, D = n + g + dK, n + g + dH, 1 - ga - ph
cK = s * (1 - aK) ** al * (1 - aH) ** (1 - al)
cH = B * aK ** ga * aH ** ph
kdot = cK * k ** al * h ** (1 - al) - xK * k
hdot = cH * k ** ga * h ** ph - xH * h


def draw():
    G = rng.uniform(0.05, 0.6)
    return {al: rng.uniform(0.2, 0.6), ga: G, ph: rng.uniform(0.05, 0.85 - G), s: rng.uniform(0.1, 0.4),
            B: rng.uniform(0.5, 2), aK: rng.uniform(0.05, 0.3), aH: rng.uniform(0.05, 0.5),
            n: rng.uniform(0, 0.03), g: rng.uniform(0, 0.03), dK: rng.uniform(0.02, 0.08),
            dH: rng.uniform(0.02, 0.08), r: rng.uniform(1.05, 2.0)}


draws = [draw() for _ in range(8)]

# (a) laws of motion: d/dt [K/(AL)] and d/dt [H/(AL)] from the level equations
t, A0, L0, Kv, Hv = sp.symbols("t A_0 L_0 K_v H_v", positive=True)
Kf, Hf = sp.Function("K")(t), sp.Function("H")(t)
AL = A0 * sp.exp(g * t) * L0 * sp.exp(n * t)
Ylev = ((1 - aK) * Kf) ** al * ((1 - aH) * Hf) ** (1 - al)
rules = {Kf.diff(t): s * Ylev - dK * Kf,
         Hf.diff(t): B * (aK * Kf) ** ga * (aH * Hf) ** ph * AL ** (1 - ga - ph) - dH * Hf}
lev = {Kf: Kv, Hf: Hv}
on = {k: Kv / AL, h: Hv / AL}
extra = [{**d, t: 3.7, A0: 1.3, L0: 0.8, Kv: 4.1, Hv: 2.2} for d in draws]
zero_at((sp.diff(Kf / AL, t).subs(rules) - kdot.subs(on)).subs(lev), extra)
zero_at((sp.diff(Hf / AL, t).subs(rules) - hdot.subs(on)).subs(lev), extra)

# (b) loci: k = kappa h and k = lam h^eta (eta > 1); signs of kdot, hdot off them
kappa, lam, eta = (cK / xK) ** (1 / (1 - al)), (xH / cH) ** (1 / ga), (1 - ph) / ga
zero_at(kdot.subs(k, kappa * h).subs(h, 1.7), draws)
zero_at(hdot.subs(k, lam * h ** eta).subs(h, 1.7), draws)
for d in draws:
    assert float(eta.subs(d)) > 1
    for hv in (0.3, 1.0, 4.0):
        kr, kc = float((kappa * hv).subs(d)), float((lam * hv ** eta).subs(d))
        f = lambda e, kk: float(e.subs(d).subs({k: kk, h: hv}))
        assert f(kdot, 1.1 * kr) < 0 < f(kdot, 0.9 * kr) and f(hdot, 0.9 * kc) < 0 < f(hdot, 1.1 * kc)
        assert float(sp.diff(lam * h ** eta, h, 2).subs(d).subs(h, hv)) > 0

# (c) balanced path, uniqueness, Jacobian
hs = (cK / xK) ** (ga / ((1 - al) * D)) * (cH / xH) ** (1 / D)
ks = (cK / xK) ** ((1 - ph) / ((1 - al) * D)) * (cH / xH) ** (1 / D)
bgp = {k: ks, h: hs}
zero_at(kdot.subs(bgp), draws)
zero_at(hdot.subs(bgp), draws)
zero_at(ks - kappa * hs, draws)
for d in draws[:3]:  # kappa h - lam h^eta changes sign once, at h*
    hstar = float(hs.subs(d))
    gap = [float((kappa * x - lam * x ** eta).subs(d)) for x in hstar * np.array([0.05, 0.5, 0.9, 1.1, 2, 5])]
    assert all(v > 0 for v in gap[:3]) and all(v < 0 for v in gap[3:])
J = sp.Matrix([[sp.diff(kdot, k), sp.diff(kdot, h)], [sp.diff(hdot, k), sp.diff(hdot, h)]]).subs(bgp)
trJ, detJ = -(1 - al) * xK - (1 - ph) * xH, (1 - al) * D * xK * xH
zero_at(J[0, 0] + (1 - al) * xK, draws)
zero_at(J[0, 1] - (1 - al) * xK * ks / hs, draws)
zero_at(J[1, 0] - ga * xH * hs / ks, draws)
zero_at(J[1, 1] + (1 - ph) * xH, draws)
zero_at(J.trace() - trJ, draws)
zero_at(J.det() - detJ, draws)
assert sp.expand(trJ ** 2 - 4 * detJ - ((1 - al) * xK - (1 - ph) * xH) ** 2 - 4 * (1 - al) * ga * xK * xH) == 0
for d in draws:
    ev = np.linalg.eigvals(np.array(J.subs(d).evalf(), dtype=float))
    assert np.all(np.isreal(ev)) and np.all(ev.real < 0)

# growth on the balanced path, simulated in levels: K/L, H/L, Y/L all grow at g
d = draws[0]
p = {str(key): float(v) for key, v in d.items()}
kst, hst = float(ks.subs(d)), float(hs.subs(d))


def levels(tt, z):
    K, H = z
    A, L = np.exp(p["g"] * tt), np.exp(p["n"] * tt)
    Y = ((1 - p["a_K"]) * K) ** p["alpha"] * ((1 - p["a_H"]) * H) ** (1 - p["alpha"])
    Hd = p["B"] * (p["a_K"] * K) ** p["gamma"] * (p["a_H"] * H) ** p["phi"] * (A * L) ** (
        1 - p["gamma"] - p["phi"]) - p["delta_H"] * H
    return [p["s"] * Y - p["delta_K"] * K, Hd]


sol = solve_ivp(levels, (0, 50), [kst, hst], rtol=1e-11, atol=1e-12)
K50, H50 = sol.y[:, -1]
L50 = np.exp(p["n"] * 50)
Y = lambda K, H: ((1 - p["a_K"]) * K) ** p["alpha"] * ((1 - p["a_H"]) * H) ** (1 - p["alpha"])
for name, x0, x50 in (("K/L", kst, K50 / L50), ("H/L", hst, H50 / L50), ("Y/L", Y(kst, hst), Y(K50, H50) / L50)):
    chk(f"4.8c growth of {name} on the BGP minus g", np.log(x50 / x0) / 50 - p["g"], 0.0, tol=1e-7)

# (d) rise s -> r s: growth jump, its initial slope, long-run elasticity
kdot_new = kdot.subs(s, r * s)
G = al * kdot_new / k + (1 - al) * hdot / h  # growth of y = Y/(AL)
zero_at(G.subs(bgp) - al * (r - 1) * xK, draws)
slope = (sp.diff(G, k) * kdot_new + sp.diff(G, h) * hdot).subs(bgp)
zero_at(slope - (1 - al) * (r - 1) * xK * (ga * xH - al * r * xK), draws)
ys = (1 - aK) ** al * (1 - aH) ** (1 - al) * ks ** al * hs ** (1 - al)
zero_at(s * sp.diff(sp.log(ys), s) - (al / (1 - al) + ga / ((1 - al) * D)), draws)
assert all(float((ga / ((1 - al) * D)).subs(d)) > 0 for d in draws)  # exceeds the Solow alpha/(1-alpha)

# monotone transition from E to E', and global convergence from 20 random starts
fk = sp.lambdify((k, h), kdot_new.subs(d))
fh = sp.lambdify((k, h), hdot.subs(d))
rhs = lambda tt, z: [fk(*z), fh(*z)]
kn, hn = float(ks.subs(s, r * s).subs(d)), float(hs.subs(s, r * s).subs(d))  # E' at s' = r s
sol = solve_ivp(rhs, (0, 3000), [kst, hst], rtol=1e-10, atol=1e-12, max_step=1.0)
assert np.all(np.diff(sol.y[0]) >= -1e-12) and np.all(np.diff(sol.y[1]) >= -1e-12)
chk("4.8d k(end)/k*' after the rise in s", sol.y[0, -1] / kn, 1.0, tol=1e-4)
chk("4.8d h(end)/h*' after the rise in s", sol.y[1, -1] / hn, 1.0, tol=1e-4)
for _ in range(20):
    z0 = rng.uniform(0.05, 3, 2) * np.array([kn, hn])
    end = solve_ivp(rhs, (0, 5000), z0, rtol=1e-10, atol=1e-12).y[:, -1]
    assert abs(end[0] / kn - 1) < 1e-4 and abs(end[1] / hn - 1) < 1e-4, (z0, end)
print("4.8 convergence from 20 random starts       ok")

# ===================== Romer 8.1 =====================
Y0, gg, R, T, tau, tt = sp.symbols("Y_0 g R T tau t", positive=True)
res = sp.integrate(Y0 + gg * tt, (tt, 0, R))
assert sp.simplify(res - (Y0 * R + gg * R ** 2 / 2)) == 0
Cb = res / T
assert sp.simplify(Cb - R / T * (Y0 + gg * R / 2)) == 0
assert sp.simplify(sp.integrate(Cb, (tt, 0, T)) - res) == 0  # flat path exhausts the budget
W1 = sp.integrate(Y0 + gg * tau - Cb, (tau, 0, tt))
assert sp.simplify(W1 - ((Y0 - Cb) * tt + gg * tt ** 2 / 2)) == 0
WR = W1.subs(tt, R)
assert sp.simplify(WR - Cb * (T - R)) == 0
W2 = WR - sp.integrate(Cb, (tau, R, tt))
assert sp.simplify(W2 - Cb * (T - tt)) == 0 and sp.simplify(W2.subs(tt, T)) == 0
assert sp.simplify((Cb - Y0) - (gg * R ** 2 - 2 * Y0 * (T - R)) / (2 * T)) == 0  # borrowing iff gR^2 > 2Y0(T-R)
tm, th = (Cb - Y0) / gg, 2 * (Cb - Y0) / gg
assert sp.simplify(sp.diff(W1, tt).subs(tt, tm)) == 0
assert sp.simplify(W1.subs(tt, tm) + (Cb - Y0) ** 2 / (2 * gg)) == 0
assert sp.simplify(W1.subs(tt, th)) == 0
assert sp.simplify(R - th - 2 / gg * (1 - R / T) * (Y0 + gg * R / 2)) == 0  # so t_hat < R
SR = Y0 + gg * R - Cb
assert sp.simplify(SR - (1 - R / T) * (Y0 + gg * R / 2) - gg * R / 2) == 0

Wf = sp.lambdify((tt, Y0, gg, R, T), sp.Piecewise((W1, tt <= R), (W2, True)))
for _ in range(200):  # wealth peaks at R whenever g >= 0
    y0, g0, T0 = rng.uniform(0.1, 2), rng.uniform(0, 1), rng.uniform(5, 60)
    R0 = rng.uniform(0.2, 0.95) * T0
    grid = np.linspace(0, T0, 4001)
    W = Wf(grid, y0, g0, R0, T0)
    assert abs(grid[np.argmax(W)] - R0) <= T0 / 4000 and abs(W[-1]) < 1e-9

# flat path beats budget-neutral perturbations (log and CRRA theta = 2)
y0, g0, R0, T0 = 0.6, 0.3, 7.0, 10.0
cbar = R0 / T0 * (y0 + g0 * R0 / 2)
for u in (np.log, lambda c: -1 / c):
    for _ in range(50):
        eta_ = rng.normal(size=2000)
        eta_ -= eta_.mean()
        C = cbar + 0.05 * eta_
        assert C.min() > 0 and u(C).mean() < u(cbar)

# values drawn in Figure 8.1-1
chk("8.1 Cbar", cbar, 1.155)
chk("8.1 W(R) = Cbar (T-R)", float(WR.subs({Y0: y0, gg: g0, R: R0, T: T0})), 3.465)
chk("8.1 t_m", (cbar - y0) / g0, 1.85)
chk("8.1 W(t_m)", -(cbar - y0) ** 2 / (2 * g0), -0.513375)
chk("8.1 t_hat", 2 * (cbar - y0) / g0, 3.7)
chk("8.1 TikZ linear coefficient Y0 - Cbar", y0 - cbar, -0.555)
assert g0 * R0 ** 2 > 2 * y0 * (T0 - R0)

print("all checks passed")
