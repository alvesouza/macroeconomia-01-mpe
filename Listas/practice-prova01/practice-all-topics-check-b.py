"""All-topics practice list, blocks 6-9 (Aulas 6-9): every closed form, number and MC key.

Run: python practice-all-topics-check-b.py   (aborts on the first failed assert, prints OK per block).
Closed forms: sympy simplify(lhs - rhs) == 0. Printed numbers: compared at the precision printed.
"""
import math
import random

import sympy as sp


def zero(expr):
    """Assert expr == 0: symbolically when simplify can, otherwise at 6 random points in (0.1, 0.9)
    for every free symbol (an identity in admissible parameters; alpha, beta < 1 there)."""
    if sp.simplify(sp.powsimp(expr, force=True)) == 0:
        return
    rng = random.Random(7)
    for _ in range(6):
        val = complex(expr.subs({s_: rng.uniform(0.1, 0.9) for s_ in expr.free_symbols}).evalf(30))
        assert abs(val) < 1e-12, expr


def near(x, target, tol):
    assert abs(x - target) < tol, (x, target)


# ============================ Block 6: general equilibrium (Kurlat ch. 9) ============================
al, be, A, K1, de, sg = sp.symbols("alpha beta A K1 delta sigma", positive=True)
K2, c1, Kx = sp.symbols("K2 c1 K", positive=True)

# Objective (b): endowment economy, log utility, a = 0 => 1+r = y2/(beta y1)
y1, y2 = sp.symbols("y1 y2", positive=True)
r_end = sp.solve(sp.Eq(1 / y1, be * (1 + sp.Symbol("r")) / y2), sp.Symbol("r"))[0]
zero(1 + r_end - y2 / (be * y1))
assert sp.diff(r_end, y2).subs({be: 0.9, y1: 1, y2: 1}) > 0

# Exercise 9.11 (a)-(c): alpha K^(alpha-1) = 1/beta - 1 + delta
X = sp.Symbol("X", positive=True)                  # X = 1/beta - 1 + delta > 0
KssX = (al / X) ** (1 / (1 - al))
zero(al * KssX ** (al - 1) - X)
zero(de * KssX / KssX ** al - al * de / X)         # I/Y = delta K / K^alpha
zero((al * de / X).subs(X, 1 / be - 1 + de) - al * be * de / (1 - be + be * de))
Kss = KssX.subs(X, 1 / be - 1 + de)
s_ss = al * be * de / (1 - be + be * de)
Kgr = (al / de) ** (1 / (1 - al))
zero(de * Kgr / Kgr ** al - al)                    # golden-rule saving rate = alpha
assert sp.limit(s_ss, be, 1) == al
v = {al: 0.4, be: 0.95, de: 0.08}
near(float(Kss.subs(v)), 6.30, 0.005)
near(float((Kss ** al).subs(v)), 2.087, 0.0005)
near(float(s_ss.subs(v)), 0.2413, 0.00005)
near(float(Kgr.subs(v)), 14.62, 0.005)
near(float((1 / be - 1 + de).subs(v)), 0.1326, 0.00005)
assert float(s_ss.subs(v)) < 0.4 and float(Kss.subs(v)) < float(Kgr.subs(v))
# K_ss < K_gr for every beta < 1 (since 1/beta - 1 > 0)
for b in (0.5, 0.9, 0.99):
    assert float(s_ss.subs({al: 0.3, be: b, de: 0.1})) < 0.3

# Discursive: two-period production economy, delta = 1, L = 1
Y1 = A * K1 ** al
R2 = al * A * K2 ** (al - 1)
w2 = (1 - al) * A * K2 ** al
zero(A * Kx ** al - (1 - al) * A * Kx ** al - al * A * Kx ** (al - 1) * Kx)     # profits = 0 (CRS)
K2_eq = al * be / (1 + al * be) * Y1
c1_eq = Y1 / (1 + al * be)
zero(c1_eq + K2_eq - Y1)                                                        # goods market t=1
zero((A * K2 ** al - be * R2 * c1).subs({K2: K2_eq, c1: c1_eq}))                # Euler c2 = beta(1+r)c1
# household side: c1 = [Y1 + w2/(1+r)]/(1+beta) with prices at K2_eq
zero(((Y1 + w2 / R2) / (1 + be) - c1_eq).subs(K2, K2_eq))
zero(w2 / R2 - (1 - al) * K2 / al)
# planner: max ln(Y1 - K2) + beta*alpha*ln K2
plan = sp.log(Y1 - K2) + be * al * sp.log(K2)
zero(sp.solve(sp.diff(plan, K2), K2)[0] - K2_eq)
assert sp.simplify(sp.diff(plan, K2, 2)).subs({A: 1, K1: 1, al: 0.3, be: 0.9, K2: 0.2}) < 0
# infinite horizon, delta = 1: K' = alpha beta A K^alpha satisfies Euler and TVC
Kt = sp.Symbol("K_t", positive=True)
Kn = al * be * A * Kt ** al
Knn = al * be * A * Kn ** al
ct, cn = (1 - al * be) * A * Kt ** al, (1 - al * be) * A * Kn ** al
zero(1 / ct - be * al * A * Kn ** (al - 1) / cn)
zero(Kn / ct - al * be / (1 - al * be))                                          # u'(c_t) K_{t+1} constant
Kstar = (al * be * A) ** (1 / (1 - al))
zero(al * A * Kstar ** (al - 1) - 1 / be)                                        # modified golden rule, delta=1
zero(sp.diff(al * be * A * Kt ** al, Kt).subs(Kt, Kstar) - al)                   # slope alpha < 1 at K*
assert al * be / (1 + al * be) != al * be
near((0.7 / 3) ** 1.5, 0.1127, 0.00005)  # graph: alpha=1/3, beta=0.7, A=1 => K* = (alpha beta)^1.5
near((1 / 3) ** 1.5, 0.1925, 0.00005)    # golden-rule map crossing
# MC 6a key C is conceptual (externality); TF 6b = True (checked above)
print("Block 6 OK")

# ============================ Block 7: money and inflation (Kurlat ch. 10-11) ============================
# MC 7a: after-tax real return (1-tau) i - pi, i = r + pi
tau, r = 0.15, 0.07
before = (1 - tau) * (r + 0.05) - 0.05
after = (1 - tau) * (r + 0.10) - 0.10
near(before, 0.052, 1e-12); near(after, 0.0445, 1e-12)
near(after - before, -tau * 0.05, 1e-12)
near((1 - tau) * r, 0.0595, 1e-12)                 # distractor A
# TF 7b False: BT real balances fall when i rises with pi
F, Y, i = sp.symbols("F Y i", positive=True)
m_bt = sp.sqrt(F * Y / (2 * i))
zero(sp.diff(sp.log(m_bt), sp.log(i)) if False else sp.diff(m_bt, i) * i / m_bt + sp.Rational(1, 2))
zero(sp.diff(m_bt, Y) * Y / m_bt - sp.Rational(1, 2))

# Exercise 11.6 (Cagan): S = gamma/(omega(1+gamma)) * Y [(1+r)(1+gamma)]^(-mu)
gm, mu, om, rr = sp.symbols("gamma mu omega r", positive=True)
S = gm / (om * (1 + gm)) * Y * ((1 + rr) * (1 + gm)) ** (-mu)
Mt = sp.Symbol("M_t", positive=True)
zero((Mt - Mt / (1 + gm)) / Mt - gm / (1 + gm))
dlogS = sp.diff(sp.log(S), gm)
zero(dlogS - (1 / gm - (1 + mu) / (1 + gm)))
zero(sp.solve(sp.Eq(dlogS, 0), gm)[0] - 1 / mu)
num = {Y: 1, mu: 4, rr: 0.0025, om: 5}
Sf = sp.lambdify(gm, S.subs(num))
gstar = 0.25
near(Sf(gstar), 0.01622, 0.000005)
near(1.0025 * 1.25, 1.253125, 1e-12)
near(1.253125 ** 4, 2.4659, 0.00005)
assert Sf(gstar) > Sf(0.2) and Sf(gstar) > Sf(0.3)
grid = [k / 1000 for k in range(1, 801)]
assert abs(max(grid, key=Sf) - 0.25) < 0.0015
near(Sf(0.8), 0.0084, 0.00005)
near(1.25 ** 12 - 1, 13.55, 0.005)                 # annual inflation 1355%
near(float(((1 + rr) * (1 + gm) - 1).subs({rr: 0.0025, gm: 0.25})), 0.253125, 1e-12)
near(float((Y * ((1 + rr) * (1 + gm)) ** (-mu)).subs(num).subs(gm, 0.25)), 0.4055, 0.00005)
# d2 log S / d gamma2 < 0 at gamma* (so it is a max)
assert sp.diff(sp.log(S), gm, 2).subs(num).subs(gm, 0.25) < 0

# Discursive 7: multiplier, BT, pi = mu - eta g, Fisher, price-level jump
c, th = sp.symbols("c theta", positive=True)
mult = (1 + c) / (c + th)
near(float(mult.subs({c: 0.25, th: 0.20})), 2.778, 0.0005)
near(float(mult.subs({c: 0.25, th: 0.15})), 3.125, 1e-9)
near(3.125 / (1.25 / 0.45), 1.125, 1e-9)
zero(sp.diff(mult, th) + (1 + c) / (c + th) ** 2)
N = sp.Symbol("N", positive=True)
cost = F * N + i * Y / (2 * N)
Nst = sp.solve(sp.diff(cost, N), N)[0]
zero(Nst - sp.sqrt(i * Y / (2 * F)))
zero(Y / (2 * Nst) - m_bt)
zero(Y / m_bt - sp.sqrt(2 * i * Y / F))
mu_M, g_ = sp.symbols("mu_M g", positive=True)     # pi = mu - eta g, eta = 1/2
pi0, pi1 = 0.06 - 0.5 * 0.02, 0.04 - 0.5 * 0.02
near(pi0, 0.05, 1e-12); near(pi1, 0.03, 1e-12)
i0, i1 = 1.04 * 1.05 - 1, 1.04 * 1.03 - 1
near(i0, 0.092, 1e-12); near(i1, 0.0712, 1e-12)
jump = math.sqrt(i0 / i1)
near(i0 / i1, 1.2921, 0.00005)
near(jump, 1.1367, 0.00005)
near(0.5 * math.log(i0 / i1), 0.1281, 0.00005)
near(1 / jump - 1, -0.1203, 0.00005)
print("Block 7 OK")

# ============================ Blocks 8-9: Benigno (2015) ============================
sg, et, ka, th8, al8 = sp.symbols("sigma eta kappa theta alpha", positive=True)
a, g, mu8, y, p, i8, rho, pb, ybn, tc, tcb = sp.symbols("a g mu y p i rho pbar ybar_n tau_c taubar_c", real=True)
inv = 1 / sg + et
# y_n and y_e from MRS = real wage
y_n = ((1 + et) * a + g / sg - mu8) / inv
y_e = ((1 + et) * a + g / sg) / inv
zero(et * (y_n - a) + (y_n - g) / sg - (a - mu8))
zero(et * (y_e - a) + (y_e - g) / sg - a)
zero(y_n - y_e + mu8 / inv)
cal = {sg: 0.5, et: 0.2}
near(float((-0.05 / inv).subs(cal)), -0.02273, 0.000005)
near(float((sp.Rational(1, 2) * 0.05 ** 2 / inv).subs(cal)), 0.000568, 0.0000005)
# Harberger triangle: integral of (1/sigma+eta)(y_e - x) from y_n to y_e
x, yN, yE = sp.symbols("x y_N y_E", real=True)
zero(sp.integrate(inv * (yE - x), (x, yN, yE)) - inv * (yE - yN) ** 2 / 2)

# AD from Euler with consumption taxes (log-linear): sigma_t^-1 (cbar - c) = i - (pbar - p) - (tcb - tc) - rho
st, scc = sp.symbols("sigma_t s_c", positive=True)
yy, ybar, gg, gbar = sp.symbols("y ybar g gbar", real=True)
lhs = scc * ((ybar - gbar) / scc - (yy - gg) / scc)     # s_c (cbar - c), with c = (y - g)/s_c; sigma = sigma_t s_c
ad_y = sp.solve(sp.Eq(lhs, st * scc * (i8 - (pb - p) - (tcb - tc) - rho)), yy)[0]
zero(ad_y - (ybar + (gg - gbar) - st * scc * (i8 - (pb - p) - (tcb - tc) - rho)))
# Block 8 discursive (b): horizontal AD shift per unit of announced tbar_c: sigma - 1/(1/sigma+eta) = sigma*eta/(1/sigma+eta)
zero(sg - 1 / inv - sg * et / inv)
# (c): announced payroll tax, i fixed: dy = dybar/(1+sigma kappa), dp = kappa dy
dyb = sp.Symbol("dybar")
dy, dp = sp.symbols("dy dp")
sol = sp.solve([sp.Eq(dy, dyb - sg * dp), sp.Eq(dp, ka * dy)], [dy, dp])
zero(sol[dy] - dyb / (1 + sg * ka)); zero(sol[dp] - ka * dyb / (1 + sg * ka))
kap = (1 - al8) * inv / al8
c9 = {sg: 0.5, et: 0.2, al8: 0.66}
kv = float(kap.subs(c9))
near(kv, 1.1333, 0.00005)
dybar_v = -0.01 / 2.2
near(dybar_v, -0.004545, 0.0000005)
# Block 9 discursive (a): optimism d abar = 1 => dybar 0.545, dy 0.348, dp 0.395, di 1.09
near(1.2 / 2.2, 0.5455, 0.00005); near(1.2 / 2.2 / (1 + 0.5 * kv), 0.3482, 0.00005)
near(kv * 1.2 / 2.2 / (1 + 0.5 * kv), 0.3946, 0.00005); near(1.2 / 2.2 / 0.5, 1.0909, 0.00005)
near(dybar_v / (1 + 0.5 * kv), -0.002901, 0.0000005)
near(kv * dybar_v / (1 + 0.5 * kv), -0.003288, 0.0000005)
near(0.01 / (0.5 * 2.2), 0.009091, 0.0000005)        # rate cut that restores E
# MC 8a key D: dp/dy along AD = -1/sigma (higher p => lower pbar - p => higher real rate)
AD_y = ybn - sg * (i8 - (pb - p) - rho)
zero(sp.diff(AD_y, p) + sg)
print("Block 8 OK")

# ---- Block 9 ----
D = inv * (1 + sg * ka)
m_g = (1 + ka / inv) / (1 + sg * ka)
# AD+AS with fiscal terms: (1+sk) y = g + ybar_n - gbar + sk y_n ; y_n has g/sigma/(inv)
gv = sp.Symbol("g_v")
y_sol = (gv + sg * ka * (gv / sg) / inv) / (1 + sg * ka)
zero(sp.diff(y_sol, gv) - m_g)
zero(m_g - (inv + ka) / D)
zero((1 - m_g) - ka * sg * et / D)       # 1 - m_g = sigma*kappa*eta/D >= 0, = 0 iff eta = 0
zero(m_g.subs(et, 0) - 1)
zero(m_g - (1 / sg) / inv - et / D)      # gap multiplier eta/D (same against y_e)
kb = float(kap.subs(c9))
Dv = 2.2 * (1 + 0.5 * kb)
near(Dv, 3.4467, 0.00005)
near((2.2 + kb) / Dv, 0.9671, 0.00005)
near(0.2 / Dv, 0.05803, 0.000005)
near(0.5 * kb * 0.2 / Dv, 0.0329, 0.00005)   # 1 - m_g
# labor tax tau: output multiplier -kappa sigma/D, gap multiplier +1/D (TF 9b False)
y_tau = (sg * ka * (-1 / inv)) / (1 + sg * ka)
zero(y_tau + ka * sg / D)
zero(y_tau - (-1 / inv) - 1 / D)
# MC 9a key A: only current mu separates y_n from y_e
zero(sp.diff(y_n - y_e, a)); zero(sp.diff(y_n - y_e, g)); assert sp.diff(y_n - y_e, mu8) != 0

# Discursive (a): optimism abar, i = rho: dy = dybar/(1+sk), policy di = dybar/sigma
zero((sg * (dyb / sg) / (1 + sg * ka)) - dyb / (1 + sg * ka))
abar_coef = (1 + et) / inv
near(float(abar_coef.subs(cal)), 0.54545, 0.000005)
# Discursive (b): markup shock, loss 1/2 y^2 + theta/(2 kappa) (p)^2 along AS p = kappa (y - y_n)
yn_ = sp.Symbol("y_n", real=True)
L = y ** 2 / 2 + th8 / (2 * ka) * (ka * (y - yn_)) ** 2
ystar = sp.solve(sp.diff(L, y), y)[0]
zero(ystar - th8 * ka * yn_ / (1 + th8 * ka))
pstar = ka * (ystar - yn_)
zero(pstar + ka * yn_ / (1 + th8 * ka))
zero(ystar + th8 * pstar)                               # targeting rule (y - y_e) + theta (p - p^e) = 0
assert sp.diff(L, y, 2) > 0 or sp.simplify(sp.diff(L, y, 2) - (1 + th8 * ka)) == 0
istar = rho - pstar - ystar / sg                        # AD with ybar_n = g = pbar = 0
r_n = rho - yn_ / sg
zero(istar - r_n - yn_ * (ka + 1 / sg) / (1 + th8 * ka))
zero(istar - rho - ka * yn_ * (1 - th8 / sg) / (1 + th8 * ka))
# no policy (i = rho): y = -sigma p, p = kappa (y - y_n)
y0 = sp.solve(sp.Eq(y, -sg * ka * (y - yn_)), y)[0]
zero(y0 - sg * ka * yn_ / (1 + sg * ka))
ynv = -0.05 / 2.2
tk = 8 * kb
near(ynv, -0.022727, 0.0000005)
near(tk, 9.0667, 0.00005)
near(tk / (1 + tk) * ynv, -0.020470, 0.0000005)
near(-kb * ynv / (1 + tk), 0.002559, 0.0000005)
near(0.5 * kb * ynv / (1 + 0.5 * kb), -0.008221, 0.0000005)
near(-kb * ynv / (1 + 0.5 * kb), 0.016441, 0.0000005)
rhov = 0.02
near(rhov - ynv / 0.5, 0.065455, 0.0000005)
near(rhov + kb * ynv * (1 - 8 / 0.5) / (1 + tk), 0.058380, 0.0000005)
# Discursive (c): ZLB. gap = sigma/(1+sk) [r_n - i + pbar - p^e]
pe = sp.Symbol("p_e", real=True)
yy2 = sp.solve(sp.Eq(y, ybn - sg * (i8 - (pb - (pe + ka * (y - yn_))) - rho)), y)[0]
zero((yy2 - yn_) - sg / (1 + sg * ka) * ((rho + (ybn - yn_) / sg) - i8 + pb - pe))
ybz = 0.54545454 * -0.05
near(ybz, -0.027273, 0.0000005)
rnz = rhov + ybz / 0.5
near(rnz, -0.034545, 0.0000005)
gapz = 0.5 / (1 + 0.5 * kb) * rnz
near(gapz, -0.011025, 0.0000005)
near(kb * gapz, -0.012495, 0.0000005)
print("Block 9 OK")
