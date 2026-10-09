"""Romer (2012) Problems 6.10 and 6.7: independent check of every formula and number in
romer-6-10.tex and romer-6-7.tex (this folder).

Run: python check-6-10-6-7.py   (aborts on the first mismatch, ends with "all checks passed").
6.10: sympy re-derives p*, p, y, the incentive G(f) and the interior equilibrium; a grid scan of
      G(f) - Z finds the equilibria without using the closed forms.
6.7:  the AD curve is solved by bisection (not from the piecewise formula A), and
      pi' = lambda * A(pi) is integrated by RK4 and compared with the closed-form paths.
"""
import math
import random

import sympy as sp


def chk(name, value, expected, tol=5e-4):
    assert abs(value - expected) <= tol * max(1, abs(expected)), f"{name}: {value} != {expected}"
    print(f"{name:<56} {value:.6f}")


# ======================================================================== Romer 6.10
f, phi, m, K, Z = sp.symbols("f phi m K Z", positive=True)  # m stands for m' (only m'^2, |m'| matter)
p, ps = sp.symbols("p p_star", real=True)
sol = sp.solve([sp.Eq(ps, p + phi * (m - p)), sp.Eq(p, f * ps)], [p, ps], dict=True)[0]
D = 1 - (1 - phi) * f
y_f = m - sol[p]
assert sp.simplify(sol[ps] - phi * m / D) == 0                                # (a) p*
assert sp.simplify(sol[p] - f * phi * m / D) == 0                             # (a) p
assert sp.simplify(y_f - m * (1 - f) / D) == 0                                # (a) y
assert sp.simplify(sp.diff(y_f, f) + phi * m / D**2) == 0                     # dy/df = -phi m'/D^2
G = K * sol[ps] ** 2
assert sp.simplify(G.subs(f, 0) - K * phi**2 * m**2) == 0                     # (b) G(0)
assert sp.simplify(G.subs(f, 1) - K * m**2) == 0                              # (b) G(1)
assert sp.simplify(sp.diff(G, f) - 2 * K * phi**2 * m**2 * (1 - phi) / D**3) == 0
assert sp.simplify(sp.diff(G, f, 2) - 6 * K * phi**2 * m**2 * (1 - phi) ** 2 / D**4) == 0
Dst = phi * m * sp.sqrt(K / Z)
fst = (Dst - 1) / (phi - 1)
assert sp.simplify(D.subs(f, fst) - Dst) == 0
assert sp.simplify(G.subs(f, fst) - Z) == 0                                    # (c) G(f*) = Z
assert sp.simplify(sol[ps].subs(f, fst) - sp.sqrt(Z / K)) == 0                # |p*| = sqrt(Z/K)
assert sp.simplify(y_f.subs(f, fst) - m * (phi - Dst) / ((phi - 1) * Dst)) == 0
assert sp.simplify(fst - (1 - Dst) / (1 - phi)) == 0                           # f** is the same root
print("6.10 symbolic: p*, p, y, G, G', G'', f*, |p*|, y* all re-derived")


def equilibria(ph, z, k=1.0, mm=1.0, n=400):
    """Equilibria f of the menu-cost game, by brute force: the corners by the best-response test,
    interior points as sign changes of G(f) - Z on an n-cell grid, refined by bisection."""
    g = lambda x: k * (ph * mm / (1 - (1 - ph) * x)) ** 2 - z
    eq = ([0.0] if g(0) <= 0 else []) + ([1.0] if g(1) >= 0 else [])
    for j in range(n):
        lo, hi = j / n, (j + 1) / n
        if g(lo) * g(hi) < 0:
            for _ in range(60):
                mid = (lo + hi) / 2
                lo, hi = (mid, hi) if g(lo) * g(mid) > 0 else (lo, mid)
            eq.append((lo + hi) / 2)
    return sorted(eq)


e = equilibria(0.5, 0.55)
assert len(e) == 3 and e[0] == 0.0 and e[2] == 1.0
chk("6.10 phi=1/2, Z=0.55: interior (unstable) f**", e[1], 0.6516)
chk("6.10 closed-form f** = (1 - phi sqrt(K/Z))/(1 - phi)", (1 - 0.5 * math.sqrt(1 / 0.55)) / 0.5, e[1], 1e-9)
assert equilibria(0.5, 0.25) == [0.0, 1.0] and equilibria(0.5, 1.0) == [0.0, 1.0]   # closed interval
assert equilibria(0.5, 0.2) == [1.0] and equilibria(0.5, 1.2) == [0.0]
e = equilibria(2.0, 2.0)
assert len(e) == 1
chk("6.10 phi=2, Z=2: unique interior f* = sqrt2 - 1", e[0], math.sqrt(2) - 1, 1e-9)
chk("6.10 phi=2, Z=2: y* = m'(1-f*)/D(f*)", (1 - e[0]) / (1 + e[0]), math.sqrt(2) - 1, 1e-9)
for ph in (0.5, 0.75, 1.5, 2.0):                     # K = m' = 1, so G(0) = phi^2, G(1) = 1
    for j in range(500):
        z = (j + 0.5) / 100
        e = equilibria(ph, z)
        both, neither = (0.0 in e and 1.0 in e), (0.0 not in e and 1.0 not in e)
        assert both == (ph**2 <= z <= 1) and neither == (1 < z < ph**2), (ph, z)
        assert not neither or len(e) == 1                          # unique interior equilibrium
        assert not (both and ph**2 < z < 1) or len(e) == 3         # third, interior equilibrium
        assert ph < 1 or len(e) == 1                               # phi > 1: always unique
print("6.10 interval claims hold on a Z grid for phi = 0.5, 0.75, 1.5, 2")

# ======================================================================== Romer 6.7
TH, A_, B_, LAM = 2.0, 1.0, 3.0, 0.5                 # theta, a, b, lambda of the figures


def lin_rule(c, a=A_, b=B_):
    return lambda y, pi: c + a * y + b * pi


def ad(pi, r, delta=0.0, th=TH):
    """Output on the AD curve at inflation pi: the root in y of max(th y - pi - delta, th y + r(y, pi)),
    strictly increasing in y, found by bisection (delta: expected minus current inflation)."""
    lo, hi = -1e3, 1e3
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if max(th * mid - pi - delta, th * mid + r(mid, pi)) < 0 else (lo, mid)
    return (lo + hi) / 2


def rk4(pi0, F, T, dt=0.01, stop=lambda x: False):
    """RK4 path of pi' = F(pi) on [0, T], halted early when stop(pi) is true; returns (ts, pis)."""
    ts, xs = [0.0], [pi0]
    while ts[-1] < T - 1e-12 and not stop(xs[-1]):
        x = xs[-1]
        k1 = F(x); k2 = F(x + dt * k1 / 2); k3 = F(x + dt * k2 / 2); k4 = F(x + dt * k3)
        xs.append(x + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6)
        ts.append(ts[-1] + dt)
    return ts, xs


random.seed(1)
for _ in range(1000):                                # (a) pi - max(0, pi + r) = min(pi, -r)
    x, rr = random.uniform(-5, 5), random.uniform(-5, 5)
    assert abs((x - max(0, x + rr)) - min(x, -rr)) < 1e-12

grid = [k / 10 for k in range(-60, 61)]
for c, yt, pt, piH in ((-9.0, 1.0, 2.0, 3.0), (4.5, -0.5, -1.0, -1.5)):
    r = lin_rule(c)
    chk(f"6.7 c={c}: kink y~ = -c/(theta+a+b theta)", -c / (TH + A_ + B_ * TH), yt, 1e-12)
    chk(f"6.7 c={c}: pi~ = theta y~", TH * yt, pt, 1e-12)
    chk(f"6.7 c={c}: pi^H = -c/b", -c / B_, piH, 1e-12)
    assert abs(pt + r(yt, pt)) < 1e-12 and abs(ad(pt, r) - yt) < 1e-9       # kink on AD, i* = 0
    A = lambda x: x / TH if x <= pt else -(c + B_ * x) / (TH + A_)
    vals = [ad(x, r) for x in grid]
    assert all(abs(v - A(x)) < 1e-9 for v, x in zip(vals, grid))           # bisection = piecewise A
    assert all((v1 < v2) == (x2 <= pt) for v1, v2, x2 in zip(vals, vals[1:], grid[1:]))
    chk(f"6.7 c={c}: slope dpi/dy on U = -(theta+a)/b", 0.2 / (ad(pt + 0.3, r) - ad(pt + 0.1, r)), -1.0)
    chk(f"6.7 c={c}: slope dpi/dy on L = theta", 0.2 / (ad(pt - 0.1, r) - ad(pt - 0.3, r)), 2.0)

# general-r claims on a nonlinear rule: branch split at pi~, U slope -(theta + r1)/r2
rnl = lambda y, pi: -2 + y + 0.5 * y**3 + pi + 0.2 * pi**3
lo, hi = -10.0, 10.0
for _ in range(80):                                  # h(y) = theta y + r(y, theta y) = 0
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if TH * mid + rnl(mid, TH * mid) < 0 else (lo, mid)
ytn = (lo + hi) / 2; ptn = TH * ytn
assert all(abs(ad(x, rnl) - x / TH) < 1e-9 for x in grid if x <= ptn)
assert all(abs(TH * ad(x, rnl) + rnl(ad(x, rnl), x)) < 1e-9 and x + rnl(ad(x, rnl), x) >= -1e-9
           for x in grid if x >= ptn)
x0 = ptn + 1.0; y0 = ad(x0, rnl); h = 1e-5
slope = 2 * h / (ad(x0 + h, rnl) - ad(x0 - h, rnl))
chk("6.7 nonlinear rule: U slope = -(theta+r1)/r2", slope, -(TH + 1 + 1.5 * y0**2) / (1 + 0.6 * x0**2), 1e-6)

# (b) dynamics with the linear rule
F = lambda c, delta=0.0: (lambda x: LAM * ad(x, lin_rule(c), delta))
ts, xs = rk4(4.0, F(-9.0), 8.0)                                            # case (i)
chk("6.7 (i) pi(8) = 3 + e^-4", xs[-1], 3 + math.exp(-4), 1e-6)
chk("6.7 (i) y(8) = -e^-4", ad(xs[-1], lin_rule(-9.0)), -math.exp(-4), 1e-5)
assert all(a > b > 3 for a, b in zip(xs, xs[1:]))                          # monotone, stays above pi^H
ts, xs = rk4(1.0, F(4.5), 8.0, dt=0.002)                                   # case (ii)
k = next(j for j, x in enumerate(xs) if x <= -1.0)
t1 = ts[k - 1] + (ts[k] - ts[k - 1]) * (xs[k - 1] + 1.0) / (xs[k - 1] - xs[k])
chk("6.7 (ii) t1 = 2 ln 5", t1, 2 * math.log(5), 1e-5)
chk("6.7 (ii) pi(8) = -exp((8 - t1)/4)", xs[-1], -math.exp((8 - 2 * math.log(5)) / 4), 1e-5)
ys = [ad(x, lin_rule(4.5)) for x in xs]
chk("6.7 (ii) peak output = y~ = -0.5, reached at t1", max(ys), -0.5, 5e-4)   # grid step: dt*|pi'| <= 5e-4
assert max(ys) <= -0.5 + 1e-9 and abs(ts[ys.index(max(ys))] - t1) < 0.01
assert all(a > b for a, b in zip(xs, xs[1:]))                              # inflation falls for ever
ts, xs = rk4(-0.5, F(-9.0), 8.0)                                           # case (iii)
chk("6.7 (iii) pi(8) = -0.5 e^2", xs[-1], -0.5 * math.exp(2), 1e-6)
assert all(x + lin_rule(-9.0)(ad(x, lin_rule(-9.0)), x) <= 0 for x in xs)  # i = 0 throughout
ts, xs = rk4(0.1, F(-9.0), 60.0)                                           # 0 < pi(0) < pi~
chk("6.7 pi(0)=0.1 recovers to pi^H = 3", xs[-1], 3.0, 1e-6)
for c in (-30.0, -9.0, 0.0, 4.5):                                          # no rule escapes pi < 0
    for a in (0.5, 5.0):
        for b in (0.5, 10.0):
            assert all(ad(x, lin_rule(c, a, b)) < 0 for x in grid if x < 0)
ts, xs = rk4(-0.05, lambda x: LAM * ad(x, lin_rule(-30.0, 5.0, 10.0)), 30.0)
chk("6.7 aggressive rule, pi(0)=-0.05: pi(30) = -0.05 e^7.5", xs[-1], -0.05 * math.exp(7.5), 1e-5)

# the way out: expected inflation above current inflation by Delta, only while pi <= 0
ts, xs = rk4(-0.5, F(-9.0, 1.0), 20.0, stop=lambda x: x > 0)
chk("6.7 Delta=1: pi turns positive at t = 4 ln 2", ts[-1], 4 * math.log(2), 5e-3)
ts, xs = rk4(xs[-1], F(-9.0), 90.0)
chk("6.7 Delta=1 then 0: converges to pi^H = 3", xs[-1], 3.0, 1e-6)
ts, xs = rk4(-0.5, F(-9.0, 0.3), 20.0)
chk("6.7 Delta=0.3 < -pi(0): pi(20) = -0.3 - 0.2 e^5", xs[-1], -0.3 - 0.2 * math.exp(5), 1e-5)

# kink formulas with a natural rate r^n and with the expectations wedge Delta (sympy)
yy, pp, cc, aa, bb, th, rn, pH, dl = sp.symbols("y pi c a b theta r_n pi_H Delta", real=True)
kn = sp.solve([sp.Eq(th * yy, rn + pp), sp.Eq(pp + rn + aa * yy + bb * (pp - pH), 0)], [yy, pp], dict=True)[0]
assert sp.simplify(kn[yy] - bb * (rn + pH) / (th + aa + bb * th)) == 0     # sign y~ = sign(r^n + pi^H)
kd = sp.solve([sp.Eq(th * yy, pp + dl), sp.Eq(pp + dl + cc + aa * yy + bb * pp, 0)], [yy, pp], dict=True)[0]
assert sp.simplify(kd[yy] - (bb * dl - cc) / (th + aa + bb * th)) == 0     # y~ > 0 iff Delta > -pi^H
print("6.7 symbolic: kink with r^n and with Delta re-derived")
print("all checks passed")
