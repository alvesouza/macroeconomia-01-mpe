"""Graduate practice list B (Listas 3-4): independent check of every number and key derivation.

Run: python practice-L3-L4-check.py   (aborts on the first mismatch).
Each chk() mirrors a value printed in practice-L3-L4.tex; sympy checks the closed forms.
"""
from math import exp, log, sqrt

import sympy as sp
from scipy.optimize import brentq, minimize_scalar


def chk(name, value, expected, tol=5e-4):
    assert abs(value - expected) <= tol * max(1, abs(expected)), f"{name}: {value} != {expected}"
    print(f"{name:<44} {value:.5f}")


# ===================== Block 1: consumption =====================
# Q1a credit spread: neither borrows nor lends iff (b(1+rs))^(1/s) <= y2/y1 <= (b(1+rb))^(1/s)
b, rs, rb, sg = 0.95, 0.02, 0.30, 2.0
chk("B1a lower bound", (b * (1 + rs)) ** (1 / sg), 0.98438)
chk("B1a upper bound", (b * (1 + rb)) ** (1 / sg), 1.11131)
# Q1b present bias: beta=1/2, delta=1, r=0, log, W=100; sophisticated self 0
bb, W = 0.5, 100.0
c0 = W / (1 + 2 * bb)
c1, c2 = (W - c0) / (1 + bb), bb * (W - c0) / (1 + bb)
chk("B1b c0", c0, 50.0)
chk("B1b actual c1", c1, 33.333)
chk("B1b actual c2", c2, 16.667)
U_nc = log(c0) + bb * (log(c1) + log(c2))
U_c = log(c0) + bb * 2 * log((W - c0) / 2)
gain = U_c - U_nc
chk("B1b utility gain of commitment", gain, 0.05889)
chk("B1b Romer-style formula d ln[(1+d)^2/(4d)]", bb * log((1 + bb) ** 2 / (4 * bb)), 0.05889)
x = 1 - exp(-gain / (1 + 2 * bb))                 # share of consumption self 0 would give up
chk("B1b willingness to pay for commitment %", 100 * x, 2.9017)
# CRRA check that naive and sophisticated differ once sigma != 1 (log is the knife edge)
def c0_soph(sig):
    from scipy.optimize import minimize_scalar as ms
    def U0(c):
        W1 = W - c
        k = 1 / (1 + bb ** (1 / sig))                  # self 1 consumes share k of W1
        u = (lambda z: (z ** (1 - sig) - 1) / (1 - sig))
        return -(u(c) + bb * (u(k * W1) + u((1 - k) * W1)))
    return ms(U0, bounds=(1, 99), method="bounded").x
def c0_naive(sig):
    from scipy.optimize import minimize_scalar as ms
    u = (lambda z: (z ** (1 - sig) - 1) / (1 - sig))
    return ms(lambda c: -(u(c) + 2 * bb * u((W - c) / 2)), bounds=(1, 99), method="bounded").x
assert c0_soph(2.0) < c0_naive(2.0) and c0_soph(0.5) > c0_naive(0.5)
# naive self 0 also picks W/(1+2b) under log: max ln c0 + 2b ln((W-c0)/2)
res = minimize_scalar(lambda c: -(log(c) + 2 * bb * log((W - c) / 2)), bounds=(1, 99), method="bounded")
chk("B1c naive c0", res.x, 50.0)
# Q1d pure borrower: c1 = y2 / [(1+r) + beta^(1/s)(1+r)^(1/s)] falls with r for every s>0
r_, s_, be_, y2_ = sp.symbols("r sigma beta y2", positive=True)
c1b = y2_ / ((1 + r_) + be_ ** (1 / s_) * (1 + r_) ** (1 / s_))
d = sp.diff(1 / c1b, r_)                     # derivative of the denominator / y2 > 0
assert all(float(d.subs({r_: rv, s_: sv, be_: 0.9, y2_: 1})) > 0
           for rv in (0.01, 0.1, 0.5) for sv in (0.2, 1, 5))

# Q2 permanent income, beta(1+r)=1, r=4%
r = 0.04
R = 1 + r
# Campbell identity on a random finite income path (truncated, discounting kills the tail)
import random
random.seed(1)
ys = [100 + random.uniform(-20, 20) for _ in range(2000)]
H = lambda t: sum(ys[t + j] / R ** j for j in range(len(ys) - t))
t0 = 3
s_lhs = ys[t0] - r / R * H(t0)
s_rhs = -sum((ys[t0 + j] - ys[t0 + j - 1]) / R ** j for j in range(1, len(ys) - t0))
assert abs(s_lhs - s_rhs) < 1e-8
# pension news: cut of 15 from t=30 on
dc0 = -r / R * 15 * R ** (-30) / (1 - 1 / R)
chk("B2c dc0 from pension cut", dc0, -4.62478)
chk("B2c closed form -15 R^-30", -15 * R ** -30, -4.62478)
# rising income 50 (t<10) then 100, a0 = 0
c_unc = r / R * (50 * (1 - R ** -10) / (1 - 1 / R) + 100 * R ** -10 / (1 - 1 / R))
chk("B2d unconstrained consumption", c_unc, 83.7782)
bet = 1 / R
Uc = sum(bet ** t * log(50) for t in range(10)) + bet ** 10 / (1 - bet) * log(100)
Uu = log(c_unc) / (1 - bet)
cev = 1 - exp((Uc - Uu) * (1 - bet))
chk("B2d welfare cost of the limit %", 100 * cev, 4.6756)
chk("B2d multiplier mu_10 / beta^9", (1 / 50 - 1 / 100), 0.01)
mpc0 = (r / R) / (1 - R ** -10)
chk("B2d MPC at t=0", mpc0, 0.11855)

# ===================== Block 2: labor =====================
# Q3a: u = ln c - psi h^(1+phi)/(1+phi), c = w h + pi.  Elasticities at pi = 0, phi = 1/eps = 2
h, w, pi_, psi, phi = sp.symbols("h w pi psi phi", positive=True)
F = psi * h ** phi * (w * h + pi_) - w                      # FOC: psi h^phi c = w
dh_dw = -sp.diff(F, w) / sp.diff(F, h)
dh_dpi = -sp.diff(F, pi_) / sp.diff(F, h)
on_foc = {pi_: 0, psi: h ** (-(phi + 1))}                    # the FOC at pi = 0: psi h^(phi+1) = 1
marsh = sp.simplify((dh_dw * w / h).subs(on_foc))
hicks = sp.simplify(((dh_dw - h * dh_dpi) * w / h).subs(on_foc))
assert sp.simplify(marsh) == 0
assert sp.simplify(hicks - 1 / (1 + phi)) == 0
chk("B3a Hicksian elasticity (eps=1/2)", float(hicks.subs(phi, 2)), 0.33333)
# Q3b Prescott: alpha c/(1-h) = (1-tau)(1-theta) y/h
th = 1 / 3
al_l = (1 - 0.40) * (1 - th) / (0.75 * (0.40 / 0.60))
chk("B3b calibrated leisure weight", al_l, 0.8)
x_br = (1 - 0.50) * (1 - th) / (al_l * 0.80)
chk("B3b Brazil hours", x_br / (1 + x_br), 0.34247)

# Q4 DMP (monthly): (1-phi)(y-z) q(theta) = kappa (r + s + phi f(theta)), f = mu th^a, q = mu th^(a-1)
rr, s, a, ph, y, z = 0.004, 0.03, 0.5, 0.5, 1.0, 0.7


def jc(theta, mu=0.3, phi_=ph, y_=y, z_=z, kap=None, r_=rr):
    return (1 - phi_) * (y_ - z_) * mu * theta ** (a - 1) - kap * (r_ + s + phi_ * mu * theta ** a)


kap = (1 - ph) * (y - z) * 0.3 / (rr + s + ph * 0.3)
chk("B4b calibrated vacancy cost", kap, 0.24457)
theta0 = brentq(lambda t: jc(t, kap=kap), 1e-6, 50)
chk("B4b theta*", theta0, 1.0)
u0 = s / (s + 0.3 * theta0 ** a)
chk("B4b u*", u0, 0.09091)
th_mu = brentq(lambda t: jc(t, mu=0.225, kap=kap), 1e-6, 50)
u_mu = s / (s + 0.225 * th_mu ** a)
qa, qb, qc = kap * ph * 0.225, kap * (rr + s), -(1 - ph) * (y - z) * 0.225
assert abs(((-qb + sqrt(qb ** 2 - 4 * qa * qc)) / (2 * qa)) ** 2 - th_mu) < 1e-9
chk("B4d theta after mu=0.225", th_mu, 0.93451)
chk("B4d u after mu=0.225", u_mu, 0.12121)
th_z = brentq(lambda t: jc(t, z_=0.8, kap=kap), 1e-6, 50)
chk("B4d theta after z=0.8", th_z, 0.63689)
chk("B4d u after z=0.8", s / (s + 0.3 * th_z ** a), 0.11135)
th_y = brentq(lambda t: jc(t, y_=1.01, kap=kap), 1e-6, 50)
chk("B4d elasticity dln theta/dln y (numeric)", (log(th_y) - log(theta0)) / log(1.01), 3.6281)
num = y * (1 - ph) * 0.3
den = (1 - ph) * (y - z) * 0.3 * (1 - a) + kap * ph * 0.3 * a
chk("B4d elasticity (analytical, at theta=1)", num / den, 3.67266)
chk("B4d dln u / dln y", -a * 0.3 / (s + 0.3) * num / den, -1.66939)
th_prop = brentq(lambda t: jc(t, y_=1.1, z_=0.77, kap=1.1 * kap), 1e-6, 50)
chk("B4d theta with y, z, kappa all x1.1", th_prop, 1.0)
# Hosios at r -> 0: planner a(y-z) = kappa s/q + (1-a) kappa theta; market (1-phi)(y-z) = kappa s/q + phi kappa theta
T, Y, Z, K, S, M, A, PH = sp.symbols("theta y z kappa s mu a phi", positive=True)
q = M * T ** (A - 1)
fT = M * T ** A
uT = S / (S + fT)
Wp = Y * (1 - uT) + Z * uT - K * T * uT
foc_planner = sp.simplify(sp.diff(Wp, T) * (S + fT) ** 2 / (S * M * T ** (A - 1)))
planner_cond = A * (Y - Z) - K * S / q - (1 - A) * K * T
assert sp.simplify(foc_planner - planner_cond * (sp.simplify(foc_planner / planner_cond))) == 0
ratio = sp.simplify(foc_planner / planner_cond)
assert not ratio.has(Y) and not ratio.has(Z)          # FOC is proportional to the planner condition
market_cond = (1 - PH) * (Y - Z) - K * S / q - PH * K * T
assert sp.simplify((market_cond - planner_cond).subs(PH, 1 - A)) == 0
# planner vs market when phi = 0.7 (r = 0)
kap0 = kap
th_pl = brentq(lambda t: a * (y - z) - kap0 * s / (0.3 * t ** (a - 1)) - (1 - a) * kap0 * t, 1e-6, 50)
th_mk = brentq(lambda t: (1 - 0.7) * (y - z) - kap0 * s / (0.3 * t ** (a - 1)) - 0.7 * kap0 * t, 1e-6, 50)
chk("B4c efficient theta (r=0)", th_pl, 1.02426)
chk("B4c market theta, phi=0.7 (r=0)", th_mk, 0.43184)
chk("B4c efficient u", s / (s + 0.3 * th_pl ** a), 0.08992)
chk("B4c market u, phi=0.7", s / (s + 0.3 * th_mk ** a), 0.13208)
print("\nall checks passed")
