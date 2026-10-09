"""Independent check of every numeric answer in the practice lists A-D.

Run: python practice-lists-check.py   (aborts on the first wrong value).
Each `chk(value, expected)` mirrors a number printed in a practice-L*.tex answer key.
"""
from math import exp, log, sqrt

from scipy.optimize import brentq


def chk(name, value, expected, tol=5e-3):
    assert abs(value - expected) <= tol * max(1, abs(expected)), f"{name}: {value} != {expected}"
    print(f"{name:<34} {value:.4f}")


# ============================ LIST A: Listas 1-2 ============================
# Q1 two goods (food, electronics): 2024 p=(2,10) q=(10,5); 2025 p=(3,7) q=(12,8)
nom24 = 2 * 10 + 10 * 5
nom25 = 3 * 12 + 7 * 8
real25_b24 = 2 * 12 + 10 * 8
real24_b25 = 3 * 10 + 7 * 5
chk("A1a deflator 2025", 100 * nom25 / real25_b24, 88.46)
chk("A1a CPI 2025 (distractor)", 100 * real24_b25 / nom24, 92.86)
gI, gF = real25_b24 / nom24, nom25 / real24_b25
chk("A1b growth base 2024", 100 * (gI - 1), 48.57)
chk("A1b growth base 2025", 100 * (gF - 1), 41.54)
chk("A1b chained growth", 100 * (sqrt(gI * gF) - 1), 45.01)
chk("A1b nominal growth (distractor)", 100 * (nom25 / nom24 - 1), 31.43)

# Q2 PPP: tradable T, non-tradable N
br = dict(pT=10, qT=50, pN=20, qN=100)          # reais
us = dict(pT=2, qT=200, pN=20, qN=150)          # dollars
e = 5
gdp_br_reais = br["pT"] * br["qT"] + br["pN"] * br["qN"]
gdp_us = us["pT"] * us["qT"] + us["pN"] * us["qN"]
chk("A2a BR GDP reais", gdp_br_reais, 2500)
chk("A2a BR at market rate", gdp_br_reais / e, 500)
chk("A2a BR at US prices (PPP)", us["pT"] * br["qT"] + us["pN"] * br["qN"], 2100)
chk("A2a US GDP", gdp_us, 3400)
chk("A2a ratio market", 500 / 3400, 0.1471)
chk("A2a ratio PPP", 2100 / 3400, 0.6176)
chk("A2a PPP rate (reais per $)", gdp_br_reais / 2100, 1.1905)
# Jones-Klenow, sigma=1, no leisure gap, u = a(ubar + ln c), c_US = 1
ubar, aUS, aBR = 5.0, 0.79, 0.76
lam_eq = exp(aBR / aUS * (ubar + log(0.3)) - ubar)
chk("A2b lambda (no inequality)", lam_eq, 0.2597)
lam_cons_only = 0.3
chk("A2b life-exp factor", lam_eq / lam_cons_only, 0.8657)
Elnc = 0.5 * log(0.12) + 0.5 * log(0.48)
lam_ineq = exp(aBR / aUS * (ubar + Elnc) - ubar)
chk("A2c lambda (with inequality)", lam_ineq, 0.2095)
chk("A2c inequality factor exp(Elnc)/0.3", exp(Elnc) / 0.3, 0.8)

# Q3 Solow, alpha=1/3, s=0.2, n=0.02, d=0.08
al, s, n, d = 1 / 3, 0.2, 0.02, 0.08
k = (s / (n + d)) ** (1 / (1 - al))
chk("A3a k*", k, 2.8284)
chk("A3a y*", k ** al, 1.4142)
c0 = (1 - s) * k ** al
kg = (al / (n + d)) ** (1 / (1 - al))
cg = kg ** al - (n + d) * kg
chk("A3b c* at s=0.2", c0, 1.1314)
chk("A3b c gold", cg, 1.2172)
chk("A3b % gain", 100 * (cg / c0 - 1), 7.58)
chk("A3d residual", 3 - al * 4.5 - (1 - al) * 1.5, 0.5)

# Q4 Solow with tech progress
s, n, g, d = 0.24, 0.01, 0.02, 0.05
kt = (s / (n + g + d)) ** 1.5
chk("A4a k tilde*", kt, 5.1962)
chk("A4a y tilde*", kt ** al, 1.7321)
chk("A4a c tilde*", (1 - s) * kt ** al, 1.3164)
kgt = (al / (n + g + d)) ** 1.5
chk("A4a c tilde gold", kgt ** al - (n + g + d) * kgt, 1.3608)
lam = (1 - al) * (n + g + d)
chk("A4b convergence speed", lam, 0.05333)
chk("A4b half-life", log(2) / lam, 13.00)
chk("A4b impact on y (30% K lost)", 100 * (0.7 ** al - 1), -11.21)
chk("A4b growth of y right after", 100 * (g + lam * (-al * log(0.7))), 2.634)
kt2 = (s / (0.005 + g + d)) ** 1.5
chk("A4b new y tilde* (n=0.005)", kt2 ** al, 1.7889)
chk("A4b level gain %", 100 * (kt2 ** al / kt ** al - 1), 3.28)
A_ratio = 0.25 / (0.2 ** al * 0.6 ** (1 - al))
chk("A4c TFP ratio (measured k)", A_ratio, 0.6010)
A_true = 0.25 / (0.15 ** al * 0.6 ** (1 - al))
chk("A4c TFP ratio (productive k)", A_true, 0.6615)
chk("A4c share of gap from TFP (log)", log(A_ratio) / log(0.25), 0.3671)

# ============================ LIST B: Listas 3-4 ============================
beta, r, y1, y2 = 0.8, 0.25, 60, 150
W = y1 + y2 / (1 + r)
c1 = W / (1 + beta)
chk("B1a wealth", W, 180)
chk("B1a c1", c1, 100)
chk("B1a saving a", y1 - c1, -40)
# sigma=2 CRRA: c2/c1 = (beta(1+r))^(1/2) = 1 -> same
chk("B1b c1 sigma=2", W / (1 + (beta * (1 + r)) ** 0.5 / (1 + r)), 100)
# borrowing limit b=10, tax cut 10 today, +12.5 tomorrow
chk("B1d constrained c1 after cut", y1 + 10 + 10, 80)

# Q2: log, beta=0.8, r=0.25, y1=150, y2=0, tax on interest 40% rebated lump-sum in period 2
y1 = 150
c1_nt = y1 / (1 + beta)
chk("B2b c1 no tax", c1_nt, 83.333)
ratio = beta * (1 + r * (1 - 0.4))
chk("B2b c2/c1 with tax", ratio, 0.92)
c1_t = y1 / (1 + ratio / (1 + r))
chk("B2b c1 with tax", c1_t, 86.406)
chk("B2b c2 with tax", ratio * c1_t, 79.493)
chk("B2b saving with tax", y1 - c1_t, 63.594)
chk("B2b revenue", 0.4 * r * (y1 - c1_t), 6.359)
U_nt = log(c1_nt) + beta * log(c1_nt)            # c2 = c1 when beta(1+r)=1
U_t = log(c1_t) + beta * log(ratio * c1_t)
cev = 1 - exp((U_t - U_nt) / (1 + beta))
chk("B2b consumption-equivalent loss %", 100 * cev, 0.0855)
# Q2c permanent income: log, beta=0.8, r=0.25
chk("B2c MPC transitory", 1 / (1 + beta), 0.5556)
chk("B2c dc1 permanent", (10 + 10 / 1.25) / (1 + beta), 10)

# Q3 labor: u = ln c + theta ln l, theta=1, w=20, pi=4
th, w, pi_ = 1, 20, 4
lei = th / (1 + th) * (w + pi_) / w
chk("B3a hours", 1 - lei, 0.4)
chk("B3b reservation wage", th * pi_, 4)

# Q4 labor with tax: u = ln c + b ln l (gamma=1), b=1
for tau, hours in [(0.0, 0.5), (0.5, 1 / 3)]:
    l = 1 / (2 - tau)                              # rebated: (1-l) = (1-tau) l
    chk(f"B4b hours tau={tau}", 1 - l, hours)
# DMP
sep, mu, a_ = 0.03, 0.6, 0.5
theta = 0.25
f = mu * theta ** a_
chk("B4c job finding f", f, 0.3)
chk("B4c u*", sep / (sep + f), 0.0909)
chk("B4c v*", theta * sep / (sep + f), 0.0227)
chk("B4c q", mu * theta ** (a_ - 1), 1.2)
f2 = 0.45 * theta ** a_
chk("B4c u* after mu=0.45", sep / (sep + f2), 0.1176)
# vacancies needed at u=0.0909 after mu falls: sep(1-u) = mu v^a u^(1-a)
u0 = 0.03 / 0.33
v_needed = (sep * (1 - u0) / (0.45 * u0 ** (1 - a_))) ** (1 / a_)
chk("B4c v needed at old u", v_needed, 0.0404)

# ============================ LIST C: Listas 5-6 ============================
chk("C1a r (log, y2/y1=1.04, beta=.96)", 104 / (0.96 * 100) - 1, 0.08333)
chk("C1b r (sigma=2,beta=.98,g=2%)", 1.02 ** 2 / 0.98 - 1, 0.06163)
beta, al, d, sig = 0.95, 1 / 3, 0.1, 2
rss = 1 / beta - 1
rK = rss + d
K = (al / rK) ** (1 / (1 - al))
Y = K ** al
chk("C2b r_ss", rss, 0.05263)
chk("C2b rK", rK, 0.15263)
chk("C2b K_ss", K, 3.2275)
chk("C2b Y_ss", Y, 1.4777)
chk("C2b C_ss", Y - d * K, 1.1550)
chk("C2b w_ss", (1 - al) * Y, 0.9851)
chk("C2b saving rate dK/Y", d * K / Y, 0.2184)
Kg = (al / d) ** 1.5
chk("C2c K_gold", Kg, 6.0858)
chk("C2c C_gold", Kg ** al - d * Kg, 1.2172)
chk("C2c K scale if A=1.1", 1.1 ** 1.5, 1.1537)

# Q3 money
cr, rr = 0.25, 0.15
m = (1 + cr) / (rr + cr)
chk("C3a multiplier", m, 3.125)
chk("C3a M with B=200", m * 200, 625)
chk("C3b Laffer peak 1/a, a=4", 1 / 4, 0.25)

# Q4 Cagan seigniorage: m/Y = kappa exp(-a i), i = r + pi, pi = mu - g
kap, a, rr_, gg = 0.3, 2.5, 0.04, 0.02
S = lambda mu_: mu_ * kap * exp(-a * (rr_ + mu_ - gg))
chk("C4b mu* = 1/a", 1 / a, 0.4)
chk("C4b pi at peak", 0.4 - gg, 0.38)
chk("C4b max seigniorage/Y", S(0.4), 0.04199)
chk("C4b inflation tax share pi/mu", 0.38 / 0.4, 0.95)
lo = brentq(lambda x: S(x) - 0.03, 1e-6, 0.4)
hi = brentq(lambda x: S(x) - 0.03, 0.4, 5)
chk("C4c low mu", lo, 0.1548)
chk("C4c high mu", hi, 0.8232)
chk("C4c Friedman rule pi", -rr_, -0.04)

# ============================ LIST D: Lista 7 ============================
# sigma=eta=1, kappa=0.5, rho=0.02, p^e = pbar = 0, ybar_n = 0
sig, eta, kap, rho = 1.0, 1.0, 0.5, 0.02


def eq(i, yn, ybar_n=0.0, pbar=0.0, pe=0.0, dg=0.0):
    X = ybar_n + dg - sig * (i - rho) + sig * pbar
    y = (X - sig * pe + sig * kap * yn) / (1 + sig * kap)
    return y, pe + kap * (y - yn)


yn_a = (1 + eta) / (1 / sig + eta) * 0.03
chk("D2b y_n (a=0.03)", yn_a, 0.03)
y, p = eq(rho, yn_a)
chk("D2b y at i=rho", y, 0.01)
chk("D2b p at i=rho", p, -0.01)
chk("D2b required i", rho - yn_a / sig, -0.01)
y, p = eq(0.0, yn_a)
chk("D2b y at ZLB", y, 0.02333)
chk("D2b p at ZLB", p, -0.00333)
y, p = eq(0.0, yn_a, pbar=0.01)
chk("D2b y at ZLB, pbar=0.01", y, 0.03)
chk("D2b p at ZLB, pbar=0.01", p, 0.0)
yn_mu = -1 / (1 / sig + eta) * 0.04
chk("D2c y_n (mu=0.04)", yn_mu, -0.02)
y, p = eq(rho, yn_mu)
chk("D2c y at i=rho", y, -0.00667)
chk("D2c p at i=rho", p, 0.00667)
lam_w = 0.25
y_opt = kap ** 2 * yn_mu / (kap ** 2 + lam_w)
chk("D2c optimal y", y_opt, -0.01)
chk("D2c optimal p", kap * (y_opt - yn_mu), 0.005)
i_opt = brentq(lambda i: eq(i, yn_mu)[0] - y_opt, -1, 1)
chk("D2c optimal i", i_opt, 0.025)
i_strict = brentq(lambda i: eq(i, yn_mu)[1], -1, 1)
chk("D2c strict price-stability i", i_strict, 0.04)
# D3b spending multiplier: dg=0.01 temporary, y_n rises by 0.5*dg
dg = 0.01
yn_g = (1 / sig) / (1 / sig + eta) * dg
y, p = eq(rho, yn_g, dg=dg)
chk("D3b multiplier dy/dg", y / dg, 0.8333)
chk("D3b gap", y - yn_g, 0.00333)
print("\nall checks passed")
