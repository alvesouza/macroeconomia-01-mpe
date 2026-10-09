"""Graduate practice list C (Listas 5-6): independent check of every number and key derivation.

Run: python practice-L5-L6-check.py   (aborts on the first mismatch).
Each chk() mirrors a value printed in practice-L5-L6.tex; sympy checks the closed forms.
"""
from math import e, exp, log, sqrt

import sympy as sp
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq


def chk(name, value, expected, tol=5e-4):
    assert abs(value - expected) <= tol * max(1, abs(expected)), f"{name}: {value} != {expected}"
    print(f"{name:<46} {value:.5f}")


# ===================== Block 1: general equilibrium =====================
# Q1a static GE with fixed K: psi/(1-L) = (1-alpha) Y^(1-sigma)/L, Y = A K^alpha L^(1-alpha)
lA, lL, al, sg, ps, K = sp.symbols("lnA lnL alpha sigma psi K", positive=True)
L = sp.exp(lL)
Y = sp.exp(lA) * K ** al * L ** (1 - al)
G = sp.log(ps) - sp.log(1 - L) - sp.log(1 - al) - (1 - sg) * sp.log(Y) + lL
dlnL = sp.simplify(-sp.diff(G, lA) / sp.diff(G, lL))
target = (1 - sg) / (L / (1 - L) + al + (1 - al) * sg)
assert sp.simplify(dlnL - target) == 0
chk("C1a dlnL/dlnA (sigma=2, alpha=1/3, L=1/3)",
    float(target.subs({sg: 2, al: sp.Rational(1, 3), lL: sp.log(sp.Rational(1, 3))})), -0.46154)
# Q1b Ramsey saving rate s = alpha (n+g+delta)/(rho+delta+sigma g)
al_, d, rho, sig, g, n = 1 / 3, 0.05, 0.03, 2.0, 0.02, 0.01
chk("C1b Ramsey saving rate", al_ * (n + g + d) / (rho + d + sig * g), 0.22222)

# Q2 Ramsey-Cass-Koopmans in continuous time, per effective worker
fp = rho + d + sig * g                                  # f'(k*) = rho + delta + sigma g
k = (al_ / fp) ** (1 / (1 - al_))
y = k ** al_
c = y - (n + g + d) * k
chk("C2b k*", k, 4.62963)
chk("C2b y*", y, 1.66667)
chk("C2b c*", c, 1.29630)
chk("C2b r*", fp - d, 0.07)
chk("C2b k_gold", (al_ / (n + g + d)) ** 1.5, 8.50517)
fpp = al_ * (al_ - 1) * k ** (al_ - 2)
chk("C2c f''(k*)", fpp, -0.01728)
bR = fp - (n + g + d)
disc = sqrt(bR ** 2 - 4 * c * fpp / sig)
mu_m, mu_p = (bR - disc) / 2, (bR + disc) / 2
chk("C2c b = rho+sigma g-n-g", bR, 0.04)
chk("C2c stable root", mu_m, -0.08770)
chk("C2c unstable root", mu_p, 0.12770)
chk("C2c half-life", log(2) / -mu_m, 7.9035)
chk("C2c saddle slope b - mu", bR - mu_m, 0.12770)
chk("C2c Solow speed at the same s", (1 - al_) * (n + g + d), 0.05333)
# symbolic Jacobian and eigenvalues
kk, cc, ff1, ff2, B, S = sp.symbols("k c fprime fsecond b sigma", real=True)
J = sp.Matrix([[B, -1], [cc * ff2 / S, 0]])
lam = sp.Symbol("lambda")
assert sp.expand(J.charpoly(lam).as_expr() - (lam ** 2 - B * lam + cc * ff2 / S)) == 0
# g = 0 limits: speed falls with sigma
for s_lo, s_hi in [(0.5, 1.0), (1.0, 4.0), (4.0, 50.0)]:
    def speed(sv):
        kf = (al_ / (rho + d)) ** 1.5
        cf = kf ** al_ - (n + d) * kf
        f2 = al_ * (al_ - 1) * kf ** (al_ - 2)
        b0 = rho - n
        return -(b0 - sqrt(b0 ** 2 - 4 * cf * f2 / sv)) / 2
    assert speed(s_lo) > speed(s_hi)
# capital-income tax tau = 0.25 on (f' - delta), rebated lump-sum
tau = 0.25
fp2 = d + (rho + sig * g) / (1 - tau)
k2 = (al_ / fp2) ** 1.5
c2 = k2 ** al_ - (n + g + d) * k2
chk("C2d f'(k) with tax", fp2, 0.14333)
chk("C2d new k*", k2, 3.54647)
chk("C2d % fall in k*", 100 * (k2 / k - 1), -23.395)
chk("C2d new c*", c2, 1.24127)
fpp2 = al_ * (al_ - 1) * k2 ** (al_ - 2)
b2 = fp2 - (n + g + d)
mu2 = (b2 - sqrt(b2 ** 2 - 4 * c2 * (1 - tau) * fpp2 / sig)) / 2
chk("C2d stable root with tax", mu2, -0.08471)
slope2 = b2 - mu2
chk("C2d saddle slope", slope2, 0.14804)
c0_lin = c2 + slope2 * (k - k2)
chk("C2d linear c(0)", c0_lin, 1.40163)
chk("C2d linear jump vs old c* %", 100 * (c0_lin / c - 1), 8.126)


def rhs(t, x):
    kx, cx = x
    return [kx ** al_ - cx - (n + g + d) * kx,
            cx * ((1 - tau) * (al_ * kx ** (al_ - 1) - d) - rho - sig * g) / sig]


def classify(c_init):
    """+1 if c_init is too high (k undershoots k2), -1 if too low (c undershoots c2)."""
    def ev_hi(t, x): return x[0] - 0.9 * k2
    def ev_lo(t, x): return x[1] - 0.9 * c2
    ev_hi.terminal = ev_lo.terminal = True
    sol = solve_ivp(rhs, (0, 400), [k, c_init], events=[ev_hi, ev_lo], rtol=1e-10, atol=1e-12)
    if sol.t_events[0].size:
        return 1
    if sol.t_events[1].size:
        return -1
    return 1 if sol.y[0, -1] < k2 else -1


lo_c, hi_c = c2, 1.6
for _ in range(80):
    mid = (lo_c + hi_c) / 2
    if classify(mid) > 0:
        hi_c = mid
    else:
        lo_c = mid
c0_exact = (lo_c + hi_c) / 2
chk("C2d exact c(0) by shooting", c0_exact, 1.39060)
chk("C2d exact jump vs old c* %", 100 * (c0_exact / c - 1), 7.275)


def rhs_back(t, x):
    return [-v for v in rhs(t, x)]


def at_old_k(t, x): return x[0] - k
at_old_k.terminal = True
back = solve_ivp(rhs_back, (0, 500), [k2 + 1e-5, c2 + slope2 * 1e-5], events=at_old_k, rtol=1e-11, atol=1e-13)
chk("C2d exact c(0) by backward integration", back.y_events[0][0][1], 1.39060)

# ===================== Block 2: money =====================
Yb, F, i = 1200.0, 2.0, 0.06
N = sqrt(i * Yb / (2 * F))
m = Yb / (2 * N)
bailey = quad(lambda x: sqrt(F * Yb / (2 * x)), 0, i)[0] - i * m
chk("C3a trips per year", N, 4.24264)
chk("C3a real balances", m, 141.42136)
chk("C3a Bailey triangle", bailey, 8.48528)
chk("C3a resource cost F N", F * N, 8.48528)
chk("C3a total cost F N + i m", F * N + i * m, 16.97056)
aC = 4.0
chk("C3b price jump on news %", 10 * (aC / (1 + aC)) ** 4, 4.096)
chk("C3d Darby di/dpi with t=0.3", 1 / (1 - 0.3), 1.42857)

# Q4 seigniorage with Cagan demand m = kappa exp(-a pi^e), deficit d (share of GDP)
kap, a, dd, gam = 0.3, 2.5, 0.03, 0.3
dmax = kap / (a * e)
chk("C4a d_max", dmax, 0.044146)
pL = brentq(lambda p: p * kap * exp(-a * p) - dd, 1e-9, 1 / a)
pH = brentq(lambda p: p * kap * exp(-a * p) - dd, 1 / a, 20)
chk("C4a low-inflation steady state", pL, 0.14296, tol=1e-4)
chk("C4a high-inflation steady state", pH, 0.86132, tol=1e-4)
chk("C4b a pi_L", a * pL, 0.35740, tol=1e-4)
chk("C4b a pi_H", a * pH, 2.15329, tol=1e-4)
fac = gam / (1 - a * gam)
chk("C4b gamma/(1 - a gamma)", fac, 1.2)
# stability: h(pi) = (d/kappa) e^{a pi} - pi, h'(pi_s) = a pi_s - 1
hprime = lambda p: a * dd / kap * exp(a * p) - 1
chk("C4b h'(pi_L)", hprime(pL), -0.64260, tol=1e-4)
chk("C4b h'(pi_H)", hprime(pH), 1.15329, tol=1e-4)
chk("C4b gamma threshold 1/a", 1 / a, 0.4)
chk("C4b local eigenvalue at pi_L", fac * hprime(pL), -0.77112)
chk("C4b local eigenvalue at pi_H", fac * hprime(pH), 1.38395)
# d > dmax: minimum of h is positive
d2 = 0.05
pmin = log(kap / (a * d2)) / a
hmin = (1 - log(kap / (a * d2))) / a
chk("C4c argmin of h", pmin, 0.35019, tol=1e-4)
chk("C4c min of h (d=0.05)", hmin, 0.04981, tol=1e-4)
hh = lambda p: d2 / kap * exp(a * p) - p
T_inf = quad(lambda p: 1 / (fac * hh(p)), pL, 40, limit=200)[0]   # tail beyond 40 ~ e^-100
T_100 = quad(lambda p: 1 / (fac * hh(p)), pL, 1.0)[0]
chk("C4d time to pi^e = 100%", T_100, 6.5760, tol=1e-3)
chk("C4d time to explosion", T_inf, 6.8174, tol=1e-3)
chk("C4d time from 100% to divergence", T_inf - T_100, 0.24141)
chk("C2d linearization error %", 100 * (c0_lin / c0_exact - 1), 0.7926)
chk("C2d initial gap k_old/k_new - 1 %", 100 * (k / k2 - 1), 30.542)
chk("C2d fall in c* %", 100 * (c2 / c - 1), -4.2451)
print("\nall checks passed")
