#!/usr/bin/env python3
"""Checks for Simulados/simulado-04.tex (mock exam 4, real-exam format).

Every closed form in the answer key is verified with sympy; every number (Q1 and the
coordinates drawn in the figures) is recomputed. Any mismatch raises AssertionError.

Run: python Simulados/simulado_codigo/check_simulado_04.py
"""
import random

import sympy as sp


def zero(expr, name):
    """Assert that expr is identically 0: symbolically, or (when sympy cannot reduce
    fractional powers) at 20 random draws of every free symbol in (0.05, 0.95)."""
    e = sp.sympify(expr)
    # ponytail: large fractional-power expressions skip simplify (minutes) and go numeric
    if sp.count_ops(e) > 120 or sp.simplify(e) != 0:
        rng = random.Random(4)
        for _ in range(20):
            v = e.subs({x: rng.uniform(0.05, 0.95) for x in e.free_symbols})
            assert abs(complex(sp.N(v))) < 1e-9, f"{name}: {e} -> {sp.N(v)}"
    print(f"  ok  {name}")


def pos(expr, name, subs_list):
    """Assert expr > 0 at every parameter draw in subs_list."""
    for s in subs_list:
        v = float(expr.subs(s))
        assert v > 0, f"{name} fails at {s}: {v}"
    print(f"  ok  {name} (> 0 at {len(subs_list)} draws)")


# ------------------------------------------------------------------ Q1
print("Q1 national accounts")
# (a) farm F, roastery R
F_out, F_w = 400, 250
R_out, R_beans, R_pack_imp, R_w = 700 + 200, 400, 100, 300
va_F, va_R = F_out, R_out - R_beans - R_pack_imp
prof_F, prof_R = F_out - F_w, va_R - R_w
gdp_a = va_F + va_R
assert (va_F, va_R, gdp_a) == (400, 400, 800)
assert F_w + R_w + prof_F + prof_R == gdp_a == 700 + 200 - 100
assert (prof_F, prof_R) == (150, 100)
assert F_out + R_out == 1300  # sum of sales: the double-counting trap
print("  ok  1.a GDP = 800 by product, income, expenditure")
# (b) households buy 600, 100 of output stays in inventory
C_b, dInv = 600, 100
prod_R_b = C_b + 200 + dInv
assert prod_R_b == R_out
assert prod_R_b - R_beans - R_pack_imp == 400
assert C_b + dInv + 200 - 100 == 800
assert (prod_R_b - R_beans - R_pack_imp - R_w) == 100
assert (+100) + (-100) == 0  # next year: C up, inventories down
print("  ok  1.b GDP = 800, I = 100 (inventories); next-year sale nets to 0")
# (c) government
wages_g, meds_imp, transfers, tax = 120, 30, 50, 200
G = wages_g + meds_imp            # output valued at cost = final consumption
va_G = G - meds_imp
gdp_c = va_F + va_R + va_G
assert (G, va_G, gdp_c) == (150, 120, 920)
assert F_w + R_w + wages_g + prof_F + prof_R == 920
assert 700 + G + 200 - (100 + meds_imp) == 920
assert gdp_c - gdp_a == wages_g and gdp_c - gdp_a not in (tax, G, transfers)
print("  ok  1.c GDP = 920 (rise = 120 = nurses' wages)")

# ------------------------------------------------------------------ Q2 Solow
print("Q2 Solow with labour-augmenting technology and population growth")
al, s, d, g, n = sp.symbols("alpha s delta g n", positive=True)
k, kp = sp.symbols("k kp", positive=True)
A, L, K = sp.symbols("A L K", positive=True)
xi = (1 + g) * (1 + n) - (1 - d)
# K' = (1-d)K + s K^a (AL)^(1-a); divide by A'L' = (1+g)(1+n)AL
Kp = (1 - d) * K + s * K**al * (A * L) ** (1 - al)
kp_expr = sp.simplify(Kp / ((1 + g) * (1 + n) * A * L)).subs(K, k * A * L)
zero((kp_expr - ((1 - d) * k + s * k**al) / ((1 + g) * (1 + n))),
     "2.a law of motion (1+g)(1+n)k' = (1-d)k + s k^a")
ratio = ((1 - d) + s * k ** (al - 1)) / ((1 + g) * (1 + n))
zero((kp_expr / k - ratio), "2.a k'/k ratio")
kss = (s / xi) ** (1 / (1 - al))
zero(((ratio - 1).subs(k, kss)), "2.a k_SS = (s/xi)^(1/(1-a)) is a fixed point")
zero(sp.expand(xi - (n + g + n * g + d)), "2.a xi = n + g + ng + delta")
draws = [{al: a_, s: s_, d: d_, g: g_, n: n_}
         for a_, s_, d_, g_, n_ in [(0.3, 0.2, 0.05, 0.02, 0.01), (0.5, 0.4, 0.1, 0.0, 0.03),
                                    (0.2, 0.1, 0.9, 0.5, 0.2), (0.7, 0.6, 0.3, 0.1, 0.0)]]
slope_ss = sp.diff(((1 - d) * k + s * k**al) / ((1 + g) * (1 + n)), k).subs(k, kss)
pos(1 - slope_ss, "2.a stability: slope of k' map at k_SS < 1", draws)
pos(slope_ss, "2.a slope at k_SS > 0", draws)
# BGP: y = A k~^a grows at g; Y grows at (1+g)(1+n)-1
zero(sp.expand((1 + g) * (1 + n) - 1 - (g + n + g * n)), "2.a g_Y = g + n + gn")

# 2.b golden rule
c_ss = (1 - s) * kss**al
dlnc = sp.diff(sp.log(c_ss), s)
s_gr = sp.solve(sp.Eq(sp.simplify(dlnc), 0), s)
assert s_gr == [al], s_gr
print("  ok  2.b s_GR = alpha")
d2 = sp.diff(sp.log(1 - s) + al / (1 - al) * sp.log(s), s, 2)
pos(-d2.subs(s, al), "2.b SOC: second derivative of ln c at s_GR < 0", draws)
kgr = (al / xi) ** (1 / (1 - al))
zero((al * kgr ** (al - 1) - xi), "2.b f'(k_GR) = (1+g)(1+n) - (1-d)")
zero((xi * kgr / kgr**al - al), "2.b s at k_GR = xi k / f(k) = alpha")
pos(-sp.diff(kgr, g), "2.b dk_GR/dg < 0", draws)
# knife edge: wrong exponent 1/(1-a) would give s = 1/(2-a)
wrong = sp.solve(sp.Eq(sp.diff(sp.log(1 - s) + sp.log(s) / (1 - al), s), 0), s)
assert sp.simplify(wrong[0] - 1 / (2 - al)) == 0
print("  ok  2.b dropped-exponent error gives 1/(2-a) (trap noted in rubric)")

# ------------------------------------------------------------------ Q2 GE
print("Q2 two-period GE with leisure")
b, gm, r = sp.symbols("beta gamma r", positive=True)
c1, c2, L1, L2, a1, lam = sp.symbols("c1 c2 L1 L2 a1 lambda", positive=True)
W1, W2, P1, P2 = sp.symbols("W1 W2 Pi1 Pi2", positive=True)   # W_t = w_t A_t
H = W1 + P1 + (W2 + P2) / (1 + r)
Lag = (sp.log(c1) + gm * sp.log(1 - L1) + b * (sp.log(c2) + gm * sp.log(1 - L2))
       + lam * (W1 * L1 + P1 + (W2 * L2 + P2) / (1 + r) - c1 - c2 / (1 + r)))
foc = [sp.diff(Lag, v) for v in (c1, c2, L1, L2)] + [sp.diff(Lag, lam)]
sol = sp.solve(foc, [c1, c2, L1, L2, lam], dict=True)
assert len(sol) == 1
sol = sol[0]
zero(sol[c1] - H / ((1 + b) * (1 + gm)), "2.d c1 = H/((1+b)(1+g))")
zero(sol[c2] - b * (1 + r) * sol[c1], "2.d Euler c2 = b(1+r)c1")
zero(sol[L1] - (1 - gm * sol[c1] / W1), "2.d intratemporal 1: gamma c1/(1-L1) = w1A1")
zero(sol[L2] - (1 - gm * sol[c2] / W2), "2.d intratemporal 2: gamma c2/(1-L2) = w2A2")
# a1 from period-1 constraint and period-2 constraint agree
a1_1 = W1 * sol[L1] + P1 - sol[c1]
a1_2 = (sol[c2] - W2 * sol[L2] - P2) / (1 + r)
zero(a1_1 - a1_2, "2.d a1 consistent across the two period constraints")

# Equilibrium closed forms, then plug into every condition
A1, A2, K1 = sp.symbols("A1 A2 K1", positive=True)
s_star = al * b / (1 + al * b)
L1s = (1 - al) * (1 + al * b) / ((1 - al) * (1 + al * b) + gm)
L2s = (1 - al) / (1 - al + gm)
Y1 = K1**al * (A1 * L1s) ** (1 - al)
K2 = s_star * Y1
Y2 = K2**al * (A2 * L2s) ** (1 - al)
w1A1 = (1 - al) * Y1 / L1s
w2A2 = (1 - al) * Y2 / L2s
R = al * Y2 / K2                      # 1 + r, full depreciation
Pi1 = Y1 - w1A1 * L1s
Pi2 = Y2 - w2A2 * L2s - R * K2
c1s = Y1 - K2
c2s = Y2
zero(Pi1 - al * Y1, "2.e Pi1 = alpha Y1")
zero(Pi2, "2.e Pi2 = 0 (CRS, capital rented at its marginal product)")
zero(1 / c1s - b * R / c2s, "2.e Euler holds at equilibrium")
zero(gm * c1s / (1 - L1s) - w1A1, "2.e intratemporal 1 at equilibrium")
zero(gm * c2s / (1 - L2s) - w2A2, "2.e intratemporal 2 at equilibrium")
zero(c1s + K2 - (w1A1 * L1s + Pi1), "2.e period-1 budget with a1 = K2")
zero(c2s - (R * K2 + w2A2 * L2s + Pi2), "2.e period-2 budget")
zero(K2 / (w1A1 * L1s + Pi1) - s_star, "2.e saving rate = ab/(1+ab)")
gdraws = [{al: a_, b: b_, gm: g_} for a_, b_, g_ in
          [(0.3, 0.9, 1.0), (0.5, 0.5, 0.2), (0.1, 0.99, 3.0), (0.8, 0.3, 0.5)]]
pos(al - s_star, "2.f s* < s_GR = alpha", gdraws)
pos(L1s - L2s, "2.e L1 > L2", gdraws)
pos(sp.diff(L1s, b), "2.e dL1/dbeta > 0", gdraws)
pos(-sp.diff(L1s, gm), "2.e dL1/dgamma < 0", gdraws)
zero(sp.diff(L1s, K1), "2.e L1 independent of K1")
# map in k^ = K/A with A2 = (1+g)A1
k1h = sp.symbols("khat1", positive=True)
map_ = (K2 / A2).subs({K1: k1h * A1, A2: (1 + g) * A1})
zero(map_ - s_star * L1s ** (1 - al) * k1h**al / (1 + g), "2.e k^2 = s* L1^(1-a) k^1^a /(1+g)")
khat_ss = (s_star * L1s ** (1 - al) / (1 + g)) ** (1 / (1 - al))
zero(map_.subs(k1h, khat_ss) - khat_ss, "2.e k^_SS fixed point")
zero((sp.diff(map_, k1h).subs(k1h, khat_ss) - al), "2.e slope at k^_SS = alpha < 1")
# Solow analog: delta = 1, n = 0, effective labour A*L1
zero((khat_ss - L1s * ((s_star / xi.subs({d: 1, n: 0})) ** (1 / (1 - al)))),
     "2.f k^_SS = L1 * Solow k~_SS with delta=1, n=0, s=s*")
# figure: normalised map k2 = k1^(1/3); golden-rule map scaled by alpha/s*
fig = {al: sp.Rational(1, 3), b: sp.Rational(96, 100)}
scale = (al / s_star).subs(fig)
assert abs(float(scale) - 1.375) < 1e-12
assert abs(float(scale ** sp.Rational(3, 2)) - 1.6124) < 1e-4
print("  ok  2.e/2.f figure: GR map scale 1.375, fixed point 1.612")
stairs = [0.15]
for _ in range(3):
    stairs.append(stairs[-1] ** (1 / 3))
assert [round(x, 4) for x in stairs[1:]] == [0.5313, 0.8099, 0.9321], stairs
assert abs(1.375 * 2.1 ** (1 / 3) - 1.761) < 1e-3 and abs(2.1 ** (1 / 3) - 1.281) < 1e-3
print("  ok  2.e figure staircase 0.5313, 0.8099, 0.9321")
zero(sp.limit(s_star, b, 1) - al / (1 + al), "2.f beta -> 1: s* -> alpha/(1+alpha)")
# Solow figures: k~_SS = (0.2/0.1)^(3/2), c~(s) max at 1/3
assert abs((0.2 / 0.1) ** 1.5 - 2.828) < 1e-3 and abs(0.2 * 2.828 ** (1 / 3) - 0.2828) < 1e-3
assert abs((2 / 3) * (1 / 3 / 0.1) ** 0.5 - 1.217) < 1e-3
print("  ok  2.a/2.b figure coordinates")

# ------------------------------------------------------------------ Q3 Benigno
print("Q3 Benigno AS-AD")
sg, kap, eta, rho, phi = sp.symbols("sigma kappa eta rho phi", positive=True)
y, p, i, ab, mu = sp.symbols("y p i abar mu", real=True)
Gam = (1 + eta) / (1 / sg + eta)
m = mu / (1 / sg + eta)


def AD(ybar, pbar=0):
    """AD: y = ybar - sigma(i - (pbar - p)) - sigma ln beta, with -ln beta = rho."""
    return sp.Eq(y, ybar - sg * (i - (pbar - p)) + sg * rho)


def AS(yn, pe=0):
    return sp.Eq(p, pe + kap * (y - yn))


ea = sp.solve([AD(Gam * ab).subs(i, rho), AS(0)], [y, p], dict=True)[0]
zero(ea[y] - Gam * ab / (1 + sg * kap), "3.a dy = Gamma dabar/(1+sigma kappa)")
zero(ea[p] - kap * Gam * ab / (1 + sg * kap), "3.a dp = kappa Gamma dabar/(1+sigma kappa)")
eb = sp.solve([AD(Gam * ab), AS(0), sp.Eq(p, 0)], [y, p, i], dict=True)[0]
zero(eb[i] - (rho + Gam * ab / sg), "3.b i = rho + Gamma dabar / sigma")
zero(eb[y], "3.b y = y_n = y_e = 0 (both gaps closed)")
rn = rho + (Gam * ab - 0) / sg
zero(eb[i] - rn, "3.b i equals the natural rate r_n")

# 3.c: loss along AS
ye, yn = 0, -m
Lfun = sp.Rational(1, 2) * (y - ye) ** 2 + phi / (2 * kap) * (kap * (y - yn)) ** 2
ystar = sp.solve(sp.diff(Lfun, y), y)[0]
zero(ystar + phi * kap * m / (1 + phi * kap), "3.c y* = -phi kappa m/(1+phi kappa)")
pstar = kap * (ystar - yn)
zero(pstar - kap * m / (1 + phi * kap), "3.c p* - pe = kappa m/(1+phi kappa)")
zero((ystar - ye) + phi * pstar, "3.c targeting rule (y-ye) + phi(p-pe) = 0")
ec = sp.solve([AD(Gam * ab).subs({y: ystar, p: pstar})], [i], dict=True)[0]
istar = rho + Gam * ab / sg + kap * m * (phi - sg) / (sg * (1 + phi * kap))
zero(ec[i] - istar, "3.c i* decomposition")
zero(sp.diff(sp.diff(istar, ab), phi), "3.c news component of i* independent of phi")
zero(sp.limit(ystar, phi, sp.oo) - yn, "3.c phi -> oo: y* = y_n (strict price stability)")
zero(ystar.subs(phi, 0) - ye, "3.c phi = 0: y* = y_e")
zero(sp.limit(istar, phi, sp.oo) - (rho + Gam * ab / sg + m / sg), "3.c phi->oo: i* = rho + (Gamma dabar + m)/sigma")
# no-policy-on-markup point (AD at the news-offset rate)
enp = sp.solve([AD(Gam * ab).subs(i, rho + Gam * ab / sg), AS(yn)], [y, p], dict=True)[0]
zero(enp[y] - sg * kap * yn / (1 + sg * kap), "3.c AD at news-offset rate: y = sigma kappa y_n/(1+sigma kappa)")
diff_y = sp.factor(sp.simplify(ystar - enp[y]))
# y* - y_np = kappa m (sigma - phi) / ((1+phi kappa)(1+sigma kappa)) : below iff phi > sigma
zero(diff_y - kap * m * (sg - phi) / ((1 + phi * kap) * (1 + sg * kap)), "3.c y* < y_np iff phi > sigma")
# second-order condition
pos(sp.diff(Lfun, y, 2), "3.c SOC d2L/dy2 = 1 + phi kappa > 0",
    [{phi: 0.5, kap: 1.0}, {phi: 8.0, kap: 0.1}])

# figure coordinates: sigma=1/2, kappa=1, Gamma dabar=1, m=1, phi=2
fv = {sg: sp.Rational(1, 2), kap: 1, phi: 2}
yo = (-phi * kap / (1 + phi * kap)).subs(fv)
po = (kap / (1 + phi * kap)).subs(fv)
assert (yo, po) == (sp.Rational(-2, 3), sp.Rational(1, 3))
ynp = (sg * kap * (-1) / (1 + sg * kap)).subs(fv)
assert ynp == sp.Rational(-1, 3) and kap.subs(fv) * (ynp + 1) == sp.Rational(2, 3)
assert (1 / (1 + sg * kap)).subs(fv) == sp.Rational(2, 3)   # 3.a figure E1 = (2/3, 2/3)
# AD through O: p = c - 2y with c = po + 2 yo = -1, i.e. shift down by 1 vs AD (p=-2y)
assert po + 2 * yo == -1
di_markup = (kap * (phi - sg) / (sg * (1 + phi * kap))).subs(fv)
assert di_markup == 1   # extra rise in i beyond the news offset (vertical AD shift = di)
# 3.c figure E1: AD1 (p = 2 - 2y) meets AS1 (p = y + 1) at (1/3, 4/3)
e1 = sp.solve([sp.Eq(p, 2 - 2 * y), sp.Eq(p, y + 1)], [y, p], dict=True)[0]
assert (e1[y], e1[p]) == (sp.Rational(1, 3), sp.Rational(4, 3))
# 3.b time path: LR y = Gamma dabar = 1, p = pbar = 0; SR no policy (2/3, 2/3)
print("  ok  3 figure coordinates")

print("\nAll checks passed.")
