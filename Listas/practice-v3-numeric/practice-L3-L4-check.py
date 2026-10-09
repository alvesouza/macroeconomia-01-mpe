"""Practice list B v3 (Listas 3-4, qualifier level): independent check of every number and derivation.

Run: python practice-L3-L4-check.py   (aborts on the first mismatch).
Each chk() mirrors a value printed in practice-L3-L4.tex; sympy checks the closed forms.
"""
from math import exp, log, sqrt

import sympy as sp
from scipy.optimize import brentq, minimize_scalar


def chk(name, value, expected, tol=5e-4):
    assert abs(value - expected) <= tol * max(abs(expected), 1e-3), f"{name}: {value} != {expected}"
    print(f"{name:<50} {value:.6f}")


# ===================== Block 1: consumption =====================
# Q1a finite-horizon CRRA propensity to consume out of wealth
sig, beta, r, T = 2.0, 0.97, 0.04, 40
gam = beta ** (1 / sig) * (1 + r) ** (1 / sig - 1)
chk("B1a gamma", gam, 0.965760)
chk("B1a MPC finite horizon %", 100 * (1 - gam) / (1 - gam ** T), 4.5543)
chk("B1a MPC infinite horizon % (distractor)", 100 * (1 - gam), 3.4240)
c0 = (1 - gam) / (1 - gam ** T)
assert abs(sum(c0 * (beta * (1 + r)) ** (t / sig) / (1 + r) ** t for t in range(T)) - 1) < 1e-12


# Q1b / Q2: present bias with CRRA, three periods, r = 0, delta = 1, W = 100
def u(c, s):
    return log(c) if s == 1 else c ** (1 - s) / (1 - s)


def plans(s, b, W=100.0):
    k = 1 / (1 + b ** (1 / s))                                   # self 1 consumes share k of W1
    xs = (b * (k ** (1 - s) + (1 - k) ** (1 - s))) ** (-1 / s)   # sophisticated c0/W1
    c0s = xs * W / (1 + xs)
    xn = b ** (-1 / s) / 2                                       # naive c0/W1
    c0n = xn * W / (1 + xn)
    cc = W / (b ** (-1 / s) + 2)                                 # commitment c1 = c2
    com = (b ** (-1 / s) * cc, cc, cc)
    soph = (c0s, k * (W - c0s), (1 - k) * (W - c0s))
    naive = (c0n, k * (W - c0n), (1 - k) * (W - c0n))
    return com, naive, soph


com, naive, soph = plans(2.0, 0.5)
chk("B1b sophisticated c0", soph[0], 41.0595)
chk("B1b naive c0", naive[0], 41.4214)
chk("B2a commitment c0", com[0], 41.4214)
chk("B2a commitment c1 = c2", com[1], 29.2893)
chk("B2a naive c1", naive[1], 34.3146)
chk("B2a naive c2", naive[2], 24.2641)
chk("B2a sophisticated c1", soph[1], 34.5269)
chk("B2a sophisticated c2", soph[2], 24.4136)
res = minimize_scalar(lambda c: -(u(c, 2) + 0.5 * (u((100 - c) / (1 + 0.5 ** 0.5), 2)
                                              + u((100 - c) * 0.5 ** 0.5 / (1 + 0.5 ** 0.5), 2))),
                      bounds=(1, 99), method="bounded", options={"xatol": 1e-10})
chk("B2a sophisticated c0 (brute force)", res.x, 41.0595)
U0 = lambda pl, s=2.0, b=0.5: u(pl[0], s) + b * (u(pl[1], s) + u(pl[2], s))
chk("B2d self-0 utility, commitment", U0(com), -0.058284)
chk("B2d self-0 utility, sophisticated", U0(soph), -0.059317)
chk("B2d self-0 utility, naive", U0(naive), -0.059320)
wtp2 = 1 - U0(com) / U0(soph)                 # V(lambda W) = V(W)/lambda when sigma = 2
chk("B2d willingness to pay %, sigma=2", 100 * wtp2, 1.7404)
xb = brentq(lambda x: U0(plans(2.0, 0.5, 100 * (1 - x))[0]) - U0(soph), 0, 0.5)
chk("B2d willingness to pay % (brute force)", 100 * xb, 1.7404)
gain = 0.5 * log(1.5 ** 2 / 2)
chk("B2d willingness to pay %, log", 100 * (1 - exp(-gain / 2)), 2.9017)
for s in (0.5, 0.8, 1.5, 3.0):                # sophisticated c0 < naive c0 iff sigma > 1
    _, nv, sp_ = plans(s, 0.5)
    assert (sp_[0] < nv[0]) == (s > 1), s
_, nv, sp_ = plans(1.0, 0.5)
assert abs(sp_[0] - nv[0]) < 1e-9
assert 1 - U0(plans(2.0, 0.999)[0], b=0.999) / U0(plans(2.0, 0.999)[2], b=0.999) < 1e-5

# ===================== Block 2: labor =====================
chk("B3a hours response % (eps=.5, T=40, 10%)", 100 * 0.5 * (1 - 1 / 40) * 0.10, 4.875)
eps, psi = 0.5, 1.0


def hours(wvec):
    lam = brentq(lambda L: sum(w * (L * w / psi) ** eps for w in wvec) - len(wvec) / L, 1e-6, 1e6)
    return [(lam * w / psi) ** eps for w in wvec]


h0 = hours([1.0] * 40)[0]
h1 = hours([1.1] + [1.0] * 39)[0]
chk("B3a exact log change of hours (discrete 10%)", log(h1 / h0), 0.046377)
chk("B3b elasticity with rigid wage", 1 / (1 - 0.5) * 1 / (1 - 0.95), 40.0)

# Q4 labor tax with rebated revenue: h = (1-tau)/(1-tau+alpha)
al = 0.8
h = lambda t: (1 - t) / (1 - t + al)
R = lambda t: t * h(t)
tstar = (1 + al) - sqrt(al * (1 + al))
chk("B4b Laffer peak tau*", tstar, 0.6)
chk("B4b revenue at the peak", R(tstar), 0.2)
tnum = minimize_scalar(lambda t: -R(t), bounds=(0, 1), method="bounded", options={"xatol": 1e-10}).x
chk("B4b Laffer peak (numeric)", tnum, 0.6)
t_, a_ = sp.symbols("tau alpha", positive=True)
Rs = t_ * (1 - t_) / (1 + a_ - t_)
num = sp.expand(sp.numer(sp.together(sp.diff(Rs, t_))))
target = sp.expand(t_ ** 2 - 2 * (1 + a_) * t_ + (1 + a_))
assert sp.simplify(num - target) == 0 or sp.simplify(num + target) == 0
U = lambda t: log(h(t)) + al * log(1 - h(t))                 # c = h when w = 1 and revenue is rebated
chk("B4a hours at tau=0", h(0), 0.555556)
for t, hv, rv, x in [(0.4, 0.428571, 0.171429, 5.6794), (0.5, 0.384615, 0.192308, 10.1813), (0.6, 0.333333, 0.2, 17.0098)]:
    chk(f"B4d hours tau={t}", h(t), hv)
    chk(f"B4d revenue tau={t}", R(t), rv)
    chk(f"B4d welfare cost % tau={t}", 100 * (1 - exp(U(t) - U(0))), x)
assert abs((U(1e-6) - U(0)) / 1e-6) < 1e-5                   # zero first-order loss at tau = 0

# ---- Q1b: two-period endowment economy with growth, CRRA: 1+r = (y2/y1)^sigma / beta
chk("B1b equilibrium r % (sigma=2)", 100 * (1.03 ** 2 / 0.97 - 1), 9.3711)
chk("B1b equilibrium r % (log, distractor)", 100 * (1.03 / 0.97 - 1), 6.1856)

# ---- Q2(d): equilibrium interest rates with sophisticated present-biased households
def r01_r12(b):
    return (1 + b) / (2 * b) - 1, 1 / b - 1
for b, e01, e12 in [(0.5, 0.5, 1.0), (0.7, 0.214286, 0.428571), (0.9, 0.055556, 0.111111), (1.0, 0.0, 0.0)]:
    a_, c_ = r01_r12(b)
    chk(f"B2d r01 beta={b}", a_, e01)
    chk(f"B2d r12 beta={b}", c_, e12)
# brute force: at these prices a sophisticated self 0 with sigma = 2 chooses c0 = y (markets clear)
def self0_choice(s, b, R01, R12, y=1.0):
    def U0(c0):
        W1 = (1 + R01) * (y - c0) + y + y / (1 + R12)
        c1 = W1 / (1 + b ** (1 / s) * (1 + R12) ** (1 / s - 1))
        c2 = (b * (1 + R12)) ** (1 / s) * c1
        return -(u(c0, s) + b * (u(c1, s) + u(c2, s)))
    return minimize_scalar(U0, bounds=(0.2, 1.8), method="bounded", options={"xatol": 1e-11}).x
for s in (1.0, 2.0, 4.0):
    R01, R12 = r01_r12(0.5)
    chk(f"B2d market-clearing c0 (sigma={s})", self0_choice(s, 0.5, R01, R12), 1.0)

# ---- Q2(e): willingness to pay for commitment, sigma x beta table
def wtp(s, b):
    com_, naive_, soph_ = plans(s, b)
    if s == 1.0:
        g_ = U0(com_, s, b) - U0(soph_, s, b)
        return 1 - exp(-g_ / (1 + 2 * b))
    return 1 - (U0(soph_, s, b) / U0(com_, s, b)) ** (1 / (1 - s))
table = {(1.0, 0.5): 2.901646, (1.0, 0.7): 0.918504, (1.0, 0.9): 0.089122,
         (1.5, 0.5): 2.199382, (1.5, 0.7): 0.645921, (1.5, 0.9): 0.060187,
         (2.0, 0.5): 1.740373, (2.0, 0.7): 0.496159, (2.0, 0.9): 0.045421,
         (5.0, 0.5): 0.753609, (5.0, 0.7): 0.206239, (5.0, 0.9): 0.018366}
for (s, b), val in table.items():
    chk(f"B2e WTP % sigma={s} beta={b}", 100 * wtp(s, b), val)

# ---- Q4(d): elasticities at tau = 0.4 (alpha = 0.8)
t4 = 0.4; h4 = h(t4)
chk("B4d Marshallian elasticity", al * t4 / ((1 + al) * (1 - t4)), 0.296296)
chk("B4d Hicksian elasticity", al / ((1 + al) * (1 - t4)), 0.740741)
chk("B4d balanced-budget elasticity", 1 - h4, 0.571429)
chk("B4d Frisch elasticity", (1 - h4) / h4, 1.333333)
hind = lambda wn, T_: (wn - al * T_) / ((1 + al) * wn)        # individual supply, T taken as given
T4, e_ = t4 * h4, 1e-7
chk("B4d Marshallian (numeric)", (hind((1 - t4) * (1 + e_), T4) / hind(1 - t4, T4) - 1) / e_, 0.296296)

# ---- Q4(e): Laffer peak and costs as functions of alpha
tau_star = lambda a_: (1 + a_) - sqrt(a_ * (1 + a_))
for a_, ts, h5, x5 in [(0.4, 0.651669, 0.555556, 7.1868), (0.8, 0.6, 0.384615, 10.1822),
                        (1.54, 0.562223, 0.245098, 12.7457), (3.0, 0.535898, 0.142857, 14.7022)]:
    hh = lambda t, a=a_: (1 - t) / (1 - t + a)
    UU = lambda t, a=a_: log(hh(t)) + a * log(1 - hh(t))
    chk(f"B4e tau* alpha={a_}", tau_star(a_), ts)
    chk(f"B4e hours at tau=.5 alpha={a_}", hh(0.5), h5)
    chk(f"B4e welfare cost % at tau=.5 alpha={a_}", 100 * (1 - exp(UU(0.5) - UU(0))), x5)
a_s = sp.Symbol("alpha", positive=True)
dts = sp.diff((1 + a_s) - sp.sqrt(a_s * (1 + a_s)), a_s)
assert all(float(dts.subs(a_s, v)) < 0 for v in (0.01, 0.5, 1, 5, 50))
assert abs(float(sp.limit((1 + a_s) - sp.sqrt(a_s * (1 + a_s)), a_s, sp.oo)) - 0.5) < 1e-12
print("\nall checks passed")
