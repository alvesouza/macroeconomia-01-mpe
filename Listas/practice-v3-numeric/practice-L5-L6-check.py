"""Practice list C v3 (Listas 5-6, qualifier level): independent check of every number and derivation.

Run: python practice-L5-L6-check.py   (aborts on the first mismatch).
Each chk() mirrors a value printed in practice-L5-L6.tex; sympy checks the closed forms.
"""
from math import e, exp, log, sqrt

import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq


def chk(name, value, expected, tol=5e-4):
    assert abs(value - expected) <= tol * max(abs(expected), 1e-3), f"{name}: {value} != {expected}"
    print(f"{name:<50} {value:.6f}")


# ===================== Block 1 objective (kept from v2, cross-topic) =====================
lA, lL, al_, sg, ps, K_ = sp.symbols("lnA lnL alpha sigma psi K", positive=True)
L_ = sp.exp(lL)
Y_ = sp.exp(lA) * K_ ** al_ * L_ ** (1 - al_)
G_ = sp.log(ps) - sp.log(1 - L_) - sp.log(1 - al_) - (1 - sg) * sp.log(Y_) + lL
target = (1 - sg) / (L_ / (1 - L_) + al_ + (1 - al_) * sg)
assert sp.simplify(-sp.diff(G_, lA) / sp.diff(G_, lL) - target) == 0
chk("C1a dlnL/dlnA", float(target.subs({sg: 2, al_: sp.Rational(1, 3), lL: sp.log(sp.Rational(1, 3))})), -0.461538)
chk("C1b Ramsey saving rate", (1 / 3) * 0.08 / 0.12, 0.222222)

# ===================== Block 1 Q2: Ramsey with hours and a labor tax =====================
al, rho, de = 1 / 3, 0.04, 0.06
kb = (al / (rho + de)) ** (1 / (1 - al))
yh, ch = kb ** al, kb ** al - de * kb
chk("C2b K/h", kb, 6.085806)
chk("C2b y/h", yh, 1.825742)
chk("C2b c/h", ch, 1.460593)
chk("C2b c/y", ch / yh, 0.8)
tau0, tau1 = 0.30, 0.45
psi = (1 - tau0) * (1 - al) / (0.5 * (ch / yh))
chk("C2b calibrated psi", psi, 1.166667)
hss = lambda t, p=psi: 1 / (1 + p * (ch / yh) / ((1 - t) * (1 - al)))
h0, h1 = hss(tau0), hss(tau1)
chk("C2c h old", h0, 0.333333)
chk("C2c h new", h1, 0.282051)
chk("C2c % change in h, K, Y, C", 100 * (h1 / h0 - 1), -15.384615)
K0, K1, c0, c1 = kb * h0, kb * h1, ch * h0, ch * h1
chk("C2c K new", K1, 1.716509)
chk("C2c c new", c1, 0.411962)


def hof(K, c, t=tau1):
    return brentq(lambda h: psi * c / (1 - h) - (1 - t) * (1 - al) * K ** al * h ** (-al), 1e-12, 1 - 1e-12)


def rhs(_t, x, t=tau1):
    K, c = x
    h = hof(K, c, t)
    return [K ** al * h ** (1 - al) - c - de * K, c * (al * K ** (al - 1) * h ** (1 - al) - de - rho)]


x0, eps = np.array([K1, c1]), 1e-6
J = np.zeros((2, 2))
for j in range(2):
    dx = np.zeros(2); dx[j] = eps
    J[:, j] = (np.array(rhs(0, x0 + dx)) - np.array(rhs(0, x0 - dx))) / (2 * eps)
chk("C2d J11", J[0, 0], 0.131803)
chk("C2d J12", J[0, 1], -2.147541)
chk("C2d J21", J[1, 0], -0.008656)
chk("C2d J22", J[1, 1], -0.091803)
ev, evec = np.linalg.eig(J)
i = int(np.argmin(ev)); mu = ev[i]; v = evec[:, i]; slope = v[1] / v[0]
chk("C2d stable root", mu, -0.156319)
chk("C2d unstable root", ev[1 - i], 0.196319)
chk("C2d half-life", log(2) / -mu, 4.434173)
chk("C2d saddle slope dc/dK", slope, 0.134164)
c_lin = c1 + slope * (K0 - K1)
chk("C2d linear c(0) % vs old c", 100 * (c_lin / c0 - 1), -6.784360)
def back(_t, x): return [-w for w in rhs(_t, x)]
def hit(_t, x): return x[0] - K0
hit.terminal = True
sgn = np.sign(K0 - K1)
sol = solve_ivp(back, (0, 800), [K1 + 1e-6 * sgn, c1 + 1e-6 * slope * sgn], events=hit, rtol=1e-10, atol=1e-12)
c_ex = sol.y_events[0][0][1]
h_ex = hof(K0, c_ex)
chk("C2d exact c(0) % vs old c", 100 * (c_ex / c0 - 1), -7.044403)
chk("C2d exact h(0) % vs old h", 100 * (h_ex / h0 - 1), -19.818864)
hK = (hof(K1 + 1e-6, c1) - hof(K1 - 1e-6, c1)) / 2e-6
hc = (hof(K1, c1 + 1e-6) - hof(K1, c1 - 1e-6)) / 2e-6
chk("C2d dh/dK along the saddle path", hK + hc * slope, -0.051066)
# impulse-response coordinates used in the figure (linear solution, % deviation from old SS)
for t_ in (0, 5, 10, 20):
    Kt = K1 + (K0 - K1) * exp(mu * t_)
    ct = c1 + slope * (Kt - K1)
    ht = h1 + (hK + hc * slope) * (Kt - K1)
    print(f"   figure t={t_:>2}: K {100*(Kt/K0-1):7.3f}  c {100*(ct/c0-1):7.3f}  h {100*(ht/h0-1):7.3f}")
# parameter analysis: h as a function of tau and psi (closed form), and the convergence speed
for t, hv in [(0.3, 0.333333), (0.45, 0.282051), (0.6, 0.222222)]:
    chk(f"C2e h(tau={t})", hss(t), hv)
for p, hv in [(0.8, 0.421687), (1.5, 0.28)]:
    chk(f"C2e h(psi={p}, tau=.3)", hss(0.3, p), hv)
# symbolic: h/(1-h) = (1-tau)(1-alpha)/(psi (c/y)), with c/y = 1 - delta alpha/(rho+delta)
rng = np.random.default_rng(0)
for A_, R_, D_ in rng.uniform([0.2, 0.01, 0.02], [0.5, 0.08, 0.12], size=(5, 3)):
    kbar = (A_ / (R_ + D_)) ** (1 / (1 - A_))                 # c/y = 1 - delta alpha/(rho+delta)
    assert abs((kbar ** A_ - D_ * kbar) / kbar ** A_ - (1 - D_ * A_ / (R_ + D_))) < 1e-12
chk("C2e investment share delta*alpha/(rho+delta)", 0.06 * (1 / 3) / 0.1, 0.2)
# speed of convergence for other taxes (re-linearize)
def speed(t):
    hS = hss(t); KS, cS = kb * hS, ch * hS
    def f(x):
        K, c = x
        h = brentq(lambda hh: psi * c / (1 - hh) - (1 - t) * (1 - al) * K ** al * hh ** (-al), 1e-12, 1 - 1e-12)
        return np.array([K ** al * h ** (1 - al) - c - de * K, c * (al * K ** (al - 1) * h ** (1 - al) - de - rho)])
    Jt = np.zeros((2, 2))
    for j in range(2):
        dx = np.zeros(2); dx[j] = 1e-6
        Jt[:, j] = (f(np.array([KS, cS]) + dx) - f(np.array([KS, cS]) - dx)) / 2e-6
    return min(np.linalg.eigvals(Jt).real)
for t, sv in [(0.0, -0.143039), (0.3, -0.150880), (0.45, -0.156319), (0.6, -0.163387)]:
    chk(f"C2e stable root at tau={t}", speed(t), sv)

# ===================== Block 2 objective (kept from v2) =====================
Yb, F, i = 1200.0, 2.0, 0.06
N = sqrt(i * Yb / (2 * F)); m = Yb / (2 * N)
chk("C3a Bailey triangle", quad(lambda x: sqrt(F * Yb / (2 * x)), 0, i)[0] - i * m, 8.485281)
chk("C3b price jump on news %", 10 * (4 / 5) ** 4, 4.096)
chk("C3d Darby di/dpi", 1 / (1 - 0.3), 1.428571)

# ===================== Block 2 Q4: unpleasant monetarist arithmetic =====================
kap, a = 0.3, 2.5
S = lambda p: p * kap * exp(-a * p)
Smax = kap / (a * e)
chk("C4a S_max", Smax, 0.044146)
low = lambda s: brentq(lambda p: S(p) - s, 1e-12, 1 / a)
b0, d, r = 0.3, 0.005, 0.05
S0 = d + r * b0
chk("C4a S0 = d + r b0", S0, 0.02)
chk("C4a pi0 (immediate stabilization)", low(S0), 0.081793)
S2 = lambda S1, T: S1 + (1 + r) ** T * (S0 - S1)
# closed form against direct iteration of the debt equation
bb = b0
for _ in range(10):
    bb = (1 + r) * bb + d - 0.01
chk("C4b b_T by iteration (S1=.01,T=10)", bb, 0.425779)
chk("C4b S2 closed form (S1=.01,T=10)", S2(0.01, 10), d + r * bb)
chk("C4c pi2 (S1=.01,T=10)", low(S2(0.01, 10)), 0.117572)
chk("C4c pi1 (S1=.01)", low(0.01), 0.036520)
Tstar = lambda S1: log((Smax - S1) / (S0 - S1)) / log(1 + r)
chk("C4c T* (S1=.01)", Tstar(0.01), 25.169964)
chk("C4c T* (S1=.005)", Tstar(0.005), 19.660440)
chk("C4c T* (S1=.015)", Tstar(0.015), 36.131540)
# (d) forward-looking Cagan: pi_s = mu1 + (mu2-mu1) lam^(T-s+1) before T
lam = a / (1 + a)
mu1, mu2 = low(0.01), low(S2(0.01, 10))
for k_, val in [(1, 0.094414), (3, 0.066058), (5, 0.051590)]:
    chk(f"C4d inflation {k_} year(s) before the switch", mu1 + (mu2 - mu1) * lam ** k_, val)
# symbolic check of the forward-solution formula on a long horizon
aa = 2.5; ll = aa / (1 + aa); Tt = 12; m1, m2 = 0.03, 0.10
mpath = [m1 * t for t in range(Tt + 1)] + [m1 * Tt + m2 * (t - Tt) for t in range(Tt + 1, 2000)]
p = [sum(ll ** j * mpath[t + j] for j in range(0, 2000 - t - 1)) / (1 + aa) for t in range(Tt + 3)]
for s_ in (Tt - 4, Tt - 1, Tt):
    assert abs((p[s_] - p[s_ - 1]) - (m1 + (m2 - m1) * ll ** (Tt - s_ + 1))) < 1e-6
assert abs((p[Tt + 1] - p[Tt]) - m2) < 1e-6
# (e) parameter table: pi2 for S1 x T (None when no steady state)
table = {(0.005, 5): 0.104511, (0.005, 10): 0.138815, (0.005, 20): None,
         (0.01, 5): 0.096603, (0.01, 10): 0.117572, (0.01, 20): 0.201560,
         (0.015, 5): 0.089041, (0.015, 10): 0.098752, (0.015, 20): 0.130602}
for (S1, T), val in table.items():
    s2 = S2(S1, T)
    if val is None:
        assert s2 > Smax, (S1, T)
        print(f"C4e S1={S1} T={T}: S2={s2:.5f} > Smax -> no steady state")
    else:
        chk(f"C4e pi2 S1={S1} T={T}", low(s2), val)
# figure: pi2 against T for the three S1 (coordinates printed for the plot)
for S1 in (0.005, 0.01, 0.015):
    pts = [(T, low(S2(S1, T))) for T in range(0, 41, 2) if S2(S1, T) < Smax]
    print(f"   figure S1={S1}: " + " ".join(f"({T},{100*q:.2f})" for T, q in pts))
print("\nall checks passed")
