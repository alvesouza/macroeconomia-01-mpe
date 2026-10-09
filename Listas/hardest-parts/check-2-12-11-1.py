"""Romer 2.12 and 11.1: independent checks of hardest-parts/romer-2-12.tex and romer-11-1.tex.

Run: python check-2-12-11-1.py   (aborts on the first failed assert; ends with "all checks passed").
2.12: sympy for the loci, then a shooting simulation of the Ramsey-Cass-Koopmans economy of Romer
ch. 2 (Cobb-Douglas f(k) = k^alpha, no depreciation) under the tax regimes of problems 2.10(b),
2.11, 2.12(a) and 2.12(b). The figures in romer-2-12.tex plot these paths.
11.1: sympy re-derivation of the forward (no-bubbles) solution and of the constant-growth case.
"""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

# ================================================================ Romer 2.12 -- symbolic
k, c, tx, n_, g_ = sp.symbols("k c tau n g", positive=True)
fk = sp.Function("f")(k)
fp = sp.diff(fk, k)
# flow budget of a household holding k_h = k: after-tax return, wage f - k f', rebate tau f' k
budget = (1 - tx) * fp * k + (fk - k * fp) + tx * fp * k - c - (n_ + g_) * k
assert sp.simplify(budget - (fk - c - (n_ + g_) * k)) == 0        # kdot = 0 locus does not move

# ================================================================ Romer 2.12 -- simulation
AL, RHO, TH, N, G, TAU = 1 / 3, 0.04, 2.0, 0.01, 0.02, 0.3
assert RHO - N - (1 - TH) * G > 0                                  # Romer's beta > 0


def kss(tau):
    """Steady-state k when investment income is taxed at rate tau: (1-tau) f'(k) = rho + theta g."""
    return (AL * (1 - tau) / (RHO + TH * G)) ** (1 / (1 - AL))


def cbar(kk):
    """The kdot = 0 locus c = f(k) - (n+g) k, the same with and without the rebated tax."""
    return kk ** AL - (N + G) * kk


KS, KT, KGR = kss(0), kss(TAU), (AL / (N + G)) ** (1 / (1 - AL))
CS, CT = cbar(KS), cbar(KT)
assert KT < KS < KGR and CT < CS
assert abs((1 - TAU) * AL * KT ** (AL - 1) - (RHO + TH * G)) < 1e-12


def rhs(t, x, tau):
    """Equations of motion: kdot = f - c - (n+g)k, cdot/c = ((1-tau) f' - rho - theta g)/theta."""
    kk, cc = x
    return [kk ** AL - cc - (N + G) * kk,
            cc * ((1 - tau) * AL * kk ** (AL - 1) - RHO - TH * G) / TH]


def simulate(c0, regimes, horizon, stop=True):
    """Integrate from (k*, c0) through regimes [(start, tau), ...]; the last one runs to horizon.

    stop=True ends the run once k leaves (0.5, 2) times the final steady state, i.e. on a
    divergent path. Returns the solve_ivp segments and sign(k_end - k_final): +1 means c0 too low.
    """
    kf = kss(regimes[-1][1])

    def away(t, x, tau):
        return abs(np.log(x[0] / kf)) - 0.7
    away.terminal = True
    x, segs = [KS, c0], []
    for j, (start, tau) in enumerate(regimes):
        end = regimes[j + 1][0] if j + 1 < len(regimes) else horizon
        s = solve_ivp(rhs, (start, end), x, args=(tau,), method="DOP853", rtol=1e-12,
                      atol=1e-12, events=away if stop else None, dense_output=True)
        segs.append(s)
        x = s.y[:, -1]
        if s.status == 1:
            break
    return segs, np.sign(x[0] - kf)


def path(regimes, horizon=150.0):
    """Shoot c(0) by bisection (too high: k collapses; too low: c collapses), then return
    c0, a time grid on [0, horizon] and k(t), c(t) along the saddle-consistent path."""
    lo, hi = 0.5 * CS, 1.5 * CS
    while hi - lo > 1e-14 * CS:
        mid = 0.5 * (lo + hi)
        lo, hi = (lo, mid) if simulate(mid, regimes, 400.0)[1] < 0 else (mid, hi)
    c0 = 0.5 * (lo + hi)
    segs, _ = simulate(c0, regimes, horizon, stop=False)
    t = np.linspace(0, horizon, 30001)
    K, C = np.empty_like(t), np.empty_like(t)
    for s in segs:
        m = (t >= s.t[0]) & (t <= s.t[-1])
        K[m], C[m] = s.sol(t[m])
    return c0, t, K, C


def mono(t, x, a, b, sign):
    """True if x is strictly monotone on the open interval (a, b): sign +1 rising, -1 falling."""
    m = (t > a) & (t < b)
    return bool(np.all(np.sign(np.diff(x[m])) == sign))


def at(t, x, s):
    """Value of the gridded series x at time s."""
    return x[np.argmin(abs(t - s))]


# S_N: stable arm of the untaxed system, traced backward in time from E along its stable eigenvector
J = np.array([[AL * KS ** (AL - 1) - (N + G), -1.0],
              [CS * AL * (AL - 1) * KS ** (AL - 2) / TH, 0.0]])
lam, V = np.linalg.eig(J)
v = V[:, np.argmin(lam)] * np.sign(V[0, np.argmin(lam)])


def low_k(t, x):
    return x[0] - 0.7 * KS
low_k.terminal = True
arm = solve_ivp(lambda t, x: [-d for d in rhs(t, x, 0.0)], (0, 600), np.array([KS, CS]) - 1e-7 * v,
                method="DOP853", rtol=1e-12, atol=1e-14, events=low_k, dense_output=True)
ka, ca = arm.sol(np.linspace(arm.t[-1], 0, 40001))               # increasing in k
assert np.all(np.diff(ka) > 0) and np.all(np.diff(ca) > 0)        # S_N is increasing
assert np.all(ca[:-50] < cbar(ka[:-50])) and ka[0] < 0.75 * KS    # below the locus for k < k*


def gap(kk, cc):
    """Distance of (k, c) from S_N, relative to c*."""
    return abs(cc - np.interp(kk, ka, ca)) / CS


def dev(x, ref):
    return 100 * np.log(x / ref)


# 2.10(b): permanent tax from 0 -> jump onto S_T, then c and k fall to E_tau
c0p, t, K, C = path([(0, TAU)])
assert c0p > CS and mono(t, C, 0, 120, -1) and mono(t, K, 0, 120, -1) and abs(K[-1] / KT - 1) < 1e-3
# 2.11: announced at 0, permanent from t1 = 5 -> smaller jump, c rises until t1, k falls throughout
c011, t, K, C = path([(0, 0.0), (5, TAU)])
assert CS < c011 < c0p and mono(t, C, 0, 5, +1) and mono(t, C, 5, 120, -1) and mono(t, K, 0, 120, -1)

# 2.12(a): tax on [0, 10), unanticipated
c0a, t, K, C = path([(0, TAU), (10, 0.0)])
tma = t[np.argmin(K)]
assert CS < c0a < c0p                                              # up, but less than 2.10(b)
assert mono(t, C, 0, 10, -1) and mono(t, C, 10, 120, +1)           # c falls, kink, c rises
assert 0 < tma < 10 and mono(t, K, 0, tma, -1) and mono(t, K, tma, 120, +1)
assert at(t, C, 10) < CS and at(t, K, 10) < KS                     # lands below and left of E
assert gap(at(t, K, 10), at(t, C, 10)) < 1e-7 < 1e-3 < gap(at(t, K, 9), at(t, C, 9))
k1, c1 = at(t, K, 10), at(t, C, 10)
assert rhs(0, [k1, c1], TAU)[1] < 0 < rhs(0, [k1, c1], 0.0)[1]     # cdot switches sign at t1
assert abs(K[-1] / KS - 1) < 1e-3
assert abs(dev(c0a, CS) - 7.54) < 0.01 and abs(tma - 8.40) < 0.01

# 2.12(b): announced at 0, tax on [5, 15)
c0b, t, K, C = path([(0, 0.0), (5, TAU), (15, 0.0)])
tmb = t[np.argmin(K)]
assert CS < c0b < c0a
assert mono(t, C, 0, 5, +1) and mono(t, C, 5, 15, -1) and mono(t, C, 15, 120, +1)
assert 5 < tmb < 15 and mono(t, K, 0, tmb, -1) and mono(t, K, tmb, 120, +1)
assert at(t, K, 5) > KT                                            # in region A when the tax starts
assert at(t, C, 15) < CS and at(t, K, 15) < KS
assert gap(at(t, K, 15), at(t, C, 15)) < 1e-7 < 1e-3 < gap(at(t, K, 14), at(t, C, 14))
assert abs(K[-1] / KS - 1) < 1e-3
assert abs(dev(c0b, CS) - 4.49) < 0.01 and abs(tmb - 12.48) < 0.01 and abs(dev(at(t, C, 5), CS) - 4.85) < 0.01
print(f"2.12: jumps 100 ln(c0/c*): 2.10b {dev(c0p, CS):.2f}, 2.11 {dev(c011, CS):.2f}, "
      f"(a) {dev(c0a, CS):.2f}, (b) {dev(c0b, CS):.2f}; k minimum at t = {tma:.2f} (a), {tmb:.2f} (b)")

# ================================================================ Romer 11.1 -- sympy
b, g = sp.symbols("b g", positive=True)
m, cst, Ep, pt = sp.symbols("m c E_tp_t1 p_t", real=True)
i = sp.Symbol("i", integer=True, nonnegative=True)
nn = sp.Symbol("n", integer=True, positive=True)
phi = b / (1 + b)
# (a) solve m - p = c - b (E_t p_{t+1} - p) for p
pa = sp.solve(sp.Eq(m - pt, cst - b * (Ep - pt)), pt)[0]
assert sp.simplify(pa - ((m - cst) / (1 + b) + phi * Ep)) == 0
# (b)-(c): eight forward substitutions of E_t p_{t+j} = (1-phi)(E_t m_{t+j} - c) + phi E_t p_{t+j+1}
M = sp.symbols("M0:8", real=True)                                  # M_j = E_t m_{t+j}
P8 = sp.Symbol("P8", real=True)                                    # E_t p_{t+8}
expr = P8
for j in reversed(range(8)):
    expr = (1 - phi) * (M[j] - cst) + phi * expr
assert sp.simplify(expr - (sum((1 - phi) * phi ** j * (M[j] - cst) for j in range(8))
                           + phi ** 8 * P8)) == 0
for j in range(8):                                                 # (d): weights b^j/(1+b)^(j+1)
    assert sp.simplify(sp.diff(expr, M[j]) - b ** j / (1 + b) ** (j + 1)) == 0
assert sp.simplify(sp.summation((1 - phi) * phi ** i, (i, 0, sp.oo))) == 1
assert sp.simplify(sp.summation(i * phi ** i, (i, 0, sp.oo)) - phi / (1 - phi) ** 2) == 0
# (e): E_t m_{t+i} = m + g i
pe = sp.simplify(sp.summation((1 - phi) * phi ** i * (m + g * i - cst), (i, 0, sp.oo)))
assert sp.simplify(pe - (m - cst + b * g)) == 0
pnext = pe.subs(m, m + g)
assert sp.simplify((m - pe) - (cst - b * (pnext - pe))) == 0      # money market clears
assert sp.diff(pe, g) == b
assert sp.limit(phi ** nn * pe.subs(m, m + g * nn), nn, sp.oo) == 0   # no-bubbles condition holds
Bt = sp.Symbol("B_t", positive=True)                               # bubble: E_t B_{t+1} = B_t / phi
assert sp.simplify(pe + Bt - ((1 - phi) * (m - cst) + phi * (pnext + Bt / phi))) == 0
s = sum((1 / 3) * (2 / 3) ** j * (1.0 + 0.05 * j - 0.3) for j in range(3000))  # b = 2
assert abs(s - (1.0 - 0.3 + 2 * 0.05)) < 1e-12
print("11.1: p_t = -c + sum b^i/(1+b)^(i+1) E_t m_{t+i}; constant growth: p_t = m_t - c + b g")
print("all checks passed")
