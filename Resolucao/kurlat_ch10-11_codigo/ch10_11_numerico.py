"""Numerical checks for Kurlat (2020), chapters 10-11, problems 10.1-10.5 and 11.1-11.9.

Every analytical result in kurlat_solutions_ch10-11.tex is recomputed here by an
independent route (simulated deposit chains, direct minimisation, finite differences,
backward-solved perfect-foresight price paths, root finding) and the script aborts with
exit code 1 on any mismatch.

Run:  python ch10_11_numerico.py
"""
import math
import sys

import numpy as np
from scipy.optimize import brentq, minimize_scalar

failures = []


def check(name, got, want, tol=1e-9):
    ok = abs(float(got) - float(want)) <= tol
    print("  %s  %-60s %+.6f  (want %+.6f)" % ("ok  " if ok else "FAIL", name, got, want))
    if not ok:
        failures.append(name)


def check_true(name, cond):
    print("  %s  %s" % ("ok  " if cond else "FAIL", name))
    if not cond:
        failures.append(name)


def header(t):
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78)


# ============================================================ 10.1-10.3 multiplier
def omega(rho, chi):
    """(10.3.1): M1 multiplier 1/(rho + chi - rho*chi)."""
    return 1.0 / (rho + chi - rho * chi)


def chain(rho, chi, delta=1.0, rounds=20000):
    """Simulates Kurlat's deposit-expansion rounds for a base injection delta.

    Each round: new loan -> share chi withdrawn as cash, (1-chi) redeposited; the bank
    keeps rho of the new deposits and lends out the rest. Returns (currency, deposits).
    """
    cur = dep = 0.0
    loan = delta
    for _ in range(rounds):
        cur += chi * loan
        dep += (1 - chi) * loan
        loan *= (1 - rho) * (1 - chi)
        if loan < 1e-16:
            break
    return cur, dep


header("10.1-10.3 -- the money multiplier")
rho0, chi0 = 0.10, 0.30
cur, dep = chain(rho0, chi0)
check("simulated chain: dM1/dMB = omega", cur + dep, omega(rho0, chi0), 1e-9)
check("reserves + currency = base injection", rho0 * dep + cur, 1.0, 1e-9)
h = 1e-7
d_rho = (omega(rho0 + h, chi0) - omega(rho0 - h, chi0)) / (2 * h)
check("10.1 d omega/d rho = -(1-chi) omega^2", d_rho, -(1 - chi0) * omega(rho0, chi0) ** 2, 1e-5)
check_true("10.1 raising rho lowers M1 at a fixed base", d_rho < 0)
check("10.1 rho needed to cut M1 by 10% (chi=0.3)",
      brentq(lambda r: omega(r, chi0) - 0.9 * omega(rho0, chi0), rho0, 1.0),
      (1 / (0.9 * omega(rho0, chi0)) - chi0) / (1 - chi0), 1e-10)
d_chi = (omega(rho0, chi0 + h) - omega(rho0, chi0 - h)) / (2 * h)
check("10.2 d omega/d chi = -(1-rho) omega^2", d_chi, -(1 - rho0) * omega(rho0, chi0) ** 2, 1e-5)
MB = 100.0
for chi in (0.30, 0.20):
    c, d = chain(rho0, chi, MB)
    print("  chi=%.2f  M1=%.4f  currency=%.4f  deposits=%.4f  reserves=%.4f"
          % (chi, c + d, c, d, rho0 * d))
c3, d3 = chain(rho0, 0.30, MB)
c2, d2 = chain(rho0, 0.20, MB)
check("10.2 M1 at chi=0.3", c3 + d3, 100 / 0.37, 1e-6)
check("10.2 M1 at chi=0.2", c2 + d2, 100 / 0.28, 1e-6)
check_true("10.2 pickpockets (chi down): M1 up, currency down, deposits up",
           c2 + d2 > c3 + d3 and c2 < c3 and d2 > d3)
for eps in (1e-1, 1e-2, 1e-3):
    print("  10.3 rho=chi=%g   omega=%.3f   ~1/(2 eps)=%.3f" % (eps, omega(eps, eps), 1 / (2 * eps)))
check_true("10.3(a) omega grows without bound as rho, chi -> 0", omega(1e-6, 1e-6) > 4.9e5)

# ============================================================ 10.4-10.5 Baumol-Tobin
def md_bt(Y, F, i):
    """(10.4.4): real money demand sqrt(YF/2i)."""
    return math.sqrt(Y * F / (2 * i))


def n_bt(Y, F, i):
    """(10.4.3): trips per period sqrt(iY/2F)."""
    return math.sqrt(i * Y / (2 * F))


def n_numeric(Y, F, i):
    """Minimises F*N + i*Y/(2N) directly (10.4.2), p normalised to 1."""
    res = minimize_scalar(lambda n: F * n + i * Y / (2 * n), bounds=(1e-6, 1e6),
                          method="bounded", options={"xatol": 1e-12})
    return res.x


header("10.4 -- ATMs: a fall in F")
Y, F, i = 60000.0, 66.0, 0.02
for Fx in (F, F / 4):
    print("  F=%7.3f  N*=%.4f  M/p=%.2f" % (Fx, n_numeric(Y, Fx, i), md_bt(Y, Fx, i)))
check("10.4 cutting F by 3/4 halves money demand", md_bt(Y, F / 4, i) / md_bt(Y, F, i), 0.5, 1e-12)
check("10.4 ...and doubles the trips (numerically)", n_numeric(Y, F / 4, i) / n_numeric(Y, F, i), 2.0, 1e-5)

header("10.5 -- going to the bank")
M, PY = 10000.0, 60000.0
N_a = PY / (2 * M)
check("(a) N = pY/(2M)", N_a, 3.0, 1e-12)
F_b = brentq(lambda f: n_numeric(PY, f, 0.02) - N_a, 1.0, 1000.0, xtol=1e-12)
check("(b) F solving N*(F)=3 at i=2% (numerical)", F_b, 0.02 * PY / (2 * 9), 1e-4)
check("(b) F = 200/3", 0.02 * PY / 18, 200 / 3, 1e-12)
F_b = 200 / 3
check("(c) N at i=3%, numerical", n_numeric(PY, F_b, 0.03), 3 * math.sqrt(1.5), 1e-5)
print("  (c) N = 3 sqrt(1.5) = %.4f trips/yr, one every %.1f days" % (3 * math.sqrt(1.5), 365 / (3 * math.sqrt(1.5))))
check("(c) average balance falls to", PY / (2 * 3 * math.sqrt(1.5)), 8164.97, 0.01)
F_d = brentq(lambda f: n_numeric(PY, f, 0.015) - N_a, 1.0, 1000.0, xtol=1e-12)
check("(d) F with opportunity cost 1.5% (numerical)", F_d, 50.0, 1e-4)

# ============================================================ 11.1-11.2
header("11.1 -- income elasticity of Baumol-Tobin demand")
d = 1e-6
eta = (math.log(md_bt(Y * (1 + d), F, i)) - math.log(md_bt(Y * (1 - d), F, i))) / (2 * d)
check("eta by finite differences", eta, 0.5, 1e-8)

header("11.2 -- constant velocity")
k = 0.25
V = lambda Y_, i_: Y_ / (k * Y_)
check_true("mD = kY gives V = 1/k at every (Y, i)",
           all(abs(V(y, ii) - 1 / k) < 1e-12 for y in (1, 50, 900) for ii in (0.01, 0.1, 0.5)))
check("trips implied by sawtooth: N = Y/(2m) = V/2", 1.0 / (2 * k), 2.0, 1e-12)
# The Baumol-Tobin F that would rationalise constant N moves one-for-one with iY:
Nbar = 2.0
check("F = iY/(2 Nbar^2) reproduces Nbar", n_bt(100, 0.05 * 100 / (2 * Nbar ** 2), 0.05), Nbar, 1e-12)

# ============================================================ 11.3
header("11.3 -- seignorage with zero inflation and growth")


def seign_sim(g, F, om, r=0.03, Y0=1.0, T=5):
    """Simulates p=1, Y_t = Y0(1+g)^t, M_t = p*mD, MB = M/omega; returns dMB/(pY) at T."""
    Ys = [Y0 * (1 + g) ** t for t in range(T + 1)]
    MBs = [md_bt(y, F, r) / om for y in Ys]
    return (MBs[T] - MBs[T - 1]) / Ys[T], Ys[T]


def seign_formula(g, F, om, r, Yt):
    return (1 / om) * math.sqrt(F / (2 * r * Yt)) * (1 - (1 + g) ** -0.5)


g, Fs, om, r = 0.03, 0.02, 5.0, 0.03
sim, Yt = seign_sim(g, Fs, om, r)
check("simulated dMB/(pY) = closed form", sim, seign_formula(g, Fs, om, r, Yt), 1e-14)
approx = 0.5 * g * md_bt(Yt, Fs, r) / Yt / om
print("  exact %.8f   eta*g*(m/Y)/omega = %.8f   rel. gap %.4f (O(g))" % (sim, approx, sim / approx - 1))
check_true("first-order approximation within 3g/4 relative", abs(sim / approx - 1) < 0.75 * g)
check_true("rises with g", seign_sim(0.04, Fs, om, r)[0] > seign_sim(0.03, Fs, om, r)[0])
check_true("rises with F", seign_sim(g, 0.04, om, r)[0] > sim)
check_true("falls with omega", seign_sim(g, Fs, 10.0, r)[0] < sim)
check_true("zero with no growth", seign_sim(0.0, Fs, om, r)[0] == 0.0)
check("scales with sqrt(F): F x4 -> revenue x2", seign_sim(g, 4 * Fs, om, r)[0] / sim, 2.0, 1e-12)

# ============================================================ 11.4
header("11.4 -- two countries, Baumol-Tobin demand, perfect foresight")
YEARS = list(range(2009, 2016))
MU_A = [0.03] * 7
MU_B = [0.06, 0.05, 0.04, 0.03, 0.02, 0.01, 0.00]
r4, F4, Y4 = 0.02, 1.0, 1.0


def price_path(mus, mu_after, r_, M0=1.0):
    """Backward solution of M_t = p_t mD(Y, r + pi_{t+1}) given money growth.

    After the last listed year money grows at mu_after forever, so p grows at mu_after
    and i = r + mu_after. p_t depends only on current and future money (forward-looking).
    Returns M and p for the listed years plus the year before the first.
    """
    Ms = [M0]
    for m in mus:
        Ms.append(Ms[-1] * (1 + m))
    ps = [None] * len(Ms)
    ps[-1] = Ms[-1] / md_bt(Y4, F4, r_ + mu_after)
    for t in range(len(Ms) - 2, -1, -1):
        f = lambda p: p * md_bt(Y4, F4, r_ + ps[t + 1] / p - 1) - Ms[t]
        ps[t] = brentq(f, ps[t + 1] / 3, ps[t + 1] / (1 - r_) * (1 - 1e-9))
    return np.array(Ms), np.array(ps)


MA, pA = price_path(MU_A, 0.03, r4)
MB_, pB = price_path(MU_B, 0.0, r4)
piA, piB = pA[1:] / pA[:-1] - 1, pB[1:] / pB[:-1] - 1
print("  year   mu_A   pi_A     mu_B    pi_B     m_B = M/p")
for j, yr in enumerate(YEARS):
    print("  %d  %5.2f%%  %6.3f%%  %5.2f%%  %7.4f%%  %.6f"
          % (yr, 100 * MU_A[j], 100 * piA[j], 100 * MU_B[j], 100 * piB[j], MB_[j + 1] / pB[j + 1]))
for j in range(7):
    check("A: pi = 3%% in %d" % YEARS[j], piA[j], 0.03, 1e-10)
j12 = YEARS.index(2012)
check_true("B: pi(2012) < 3%% = pi_A(2012)   [pi_B = %.4f%%]" % (100 * piB[j12]), piB[j12] < 0.03)
check_true("B: pi < mu in 2009-2014 (real balances rising), pi = mu = 0 in 2015",
           all(piB[:6] < np.array(MU_B[:6])) and abs(piB[6]) < 1e-12)
# money market clears in every year under the solved path
for t in range(len(pB) - 1):
    i_next = r4 + pB[t + 1] / pB[t] - 1
    assert abs(pB[t] * md_bt(Y4, F4, i_next) - MB_[t]) < 1e-10
check_true("B: money market clears every year on the solved path", True)
check("B: decomposition pi+1 = (1+mu)(m_{t-1}/m_t) in 2012",
      1 + piB[j12], (1 + MU_B[j12]) * (MB_[j12] / pB[j12]) / (MB_[j12 + 1] / pB[j12 + 1]), 1e-12)

# ============================================================ 11.5
header("11.5 -- inflation targeting, r falls 3% -> 1%")
Y5, F5 = 1.0, 1.0
jump = md_bt(Y5, F5, 0.03) / md_bt(Y5, F5, 0.05)
check("required one-off level jump = sqrt(5/3)", jump, math.sqrt(5 / 3), 1e-12)
print("  money must jump by %.2f%% on top of the 2%% trend" % (100 * (jump - 1)))


def pi_at_shock(x, T=40):
    """Money grows 2% until t-1 (old r=3%), then M_t = 1.02 x M_{t-1}, 2% after, new r=1%."""
    # before the shock: steady state with i = 3% + 2%
    M_prev = 1.0
    p_prev = M_prev / md_bt(Y5, F5, 0.05)
    M_t = 1.02 * x * M_prev
    _, ps = price_path([0.02] * T, 0.02, 0.01, M0=M_t)
    return ps[0] / p_prev - 1, ps


x_num = brentq(lambda x: pi_at_shock(x)[0] - 0.02, 0.5, 3.0, xtol=1e-14)
check("root-found jump that keeps pi = 2% in the shock year", x_num, jump, 1e-9)
_, ps_after = pi_at_shock(x_num)
check_true("pi = 2% every year after the shock", np.allclose(ps_after[1:] / ps_after[:-1] - 1, 0.02, atol=1e-10))
pi_passive, _ = pi_at_shock(1.0)
check("inflation in shock year if the CB does NOT jump M", pi_passive, 1.02 * math.sqrt(3 / 5) - 1, 1e-9)

# ============================================================ 11.6 Cagan
header("11.6 -- Cagan demand, seignorage Laffer curve")
Yss, mu, rss, w = 1.0, 4.0, 0.0025, 5.0


def m_real(gam):
    """(c): M/P = Yss [(1+rss)(1+gam)]^(-mu)."""
    return Yss * ((1 + rss) * (1 + gam)) ** (-mu)


def S_formula(gam):
    """(e): S = (1/omega) gam/(1+gam) * m_real(gam)."""
    return gam / (1 + gam) * m_real(gam) / w


def S_sim(gam, T=6):
    """Builds MB_t and P_t from the definitions and returns (MB_T - MB_{T-1})/P_T."""
    MS = [1.0 * (1 + gam) ** t for t in range(T + 1)]
    P = [None] * (T + 1)
    # steady state: pi = gam; P from the money market with exact Fisher i
    for t in range(T + 1):
        i_next = (1 + rss) * (1 + gam) - 1
        P[t] = MS[t] / (Yss * (1 + i_next) ** (-mu))
    for t in range(1, T + 1):
        assert abs(P[t] / P[t - 1] - 1 - gam) < 1e-12        # (a) pi = gamma
    MBs = [m / w for m in MS]
    return (MBs[T] - MBs[T - 1]) / P[T]


for gam in (0.05, 0.25, 0.6):
    check("S simulated = formula (e) at gamma=%.2f" % gam, S_sim(gam), S_formula(gam), 1e-14)
res = minimize_scalar(lambda x: -S_sim(x), bounds=(1e-6, 0.8), method="bounded",
                      options={"xatol": 1e-12})
gstar = res.x
check("(h) numerical argmax gamma* = 1/mu", gstar, 0.25, 1e-7)
grid = np.linspace(0, 0.8, 800001)
Sg = grid / (1 + grid) * Yss * ((1 + rss) * (1 + grid)) ** (-mu) / w
check("(h) grid argmax", grid[np.argmax(Sg)], 0.25, 2e-6)
g = 0.25
i_star = (1 + rss) * (1 + g) - 1
check("(j) monthly inflation", g, 0.25)
check("(k) monthly nominal rate", i_star, 0.253125, 1e-12)
check("(l) annual inflation 1.25^12 - 1", (1 + g) ** 12 - 1, 13.551915228366852, 1e-10)
check("(m) M/P at gamma*", m_real(g), 1.253125 ** -4, 1e-15)
print("  (m) M/P = %.6f" % m_real(g))
check("(n) max S / GDP", S_formula(g), 0.2 * 0.2 * 1.253125 ** -4, 1e-15)
print("  (n) S* = %.6f of monthly GDP" % S_formula(g))
# elasticity of the base w.r.t. (1+gamma) at gamma* equals -mu; rate term gamma/(1+gamma)
h = 1e-6
el_base = (math.log(m_real(g + h)) - math.log(m_real(g - h))) / (math.log(1 + g + h) - math.log(1 + g - h))
check("(i) d ln(M/P)/d ln(1+gamma) = -mu", el_base, -mu, 1e-6)
el_rate = (math.log((g + h) / (1 + g + h)) - math.log((g - h) / (1 + g - h))) / (math.log(1 + g + h) - math.log(1 + g - h))
check("(i) d ln(gamma/(1+gamma))/d ln(1+gamma) = 1/gamma = mu at gamma*", el_rate, 4.0, 1e-5)
check_true("(i) S falls beyond gamma*", S_formula(0.3) < S_formula(0.25) and S_formula(0.8) < S_formula(0.5))

print("\n  (p)-(t) stabilisation. P_t set under the old regime (announcement at end of t).")
MBt = 1.0
Pt = w * MBt / (Yss * ((1 + rss) * (1 + g)) ** (-mu))


def P_next(Mbar):
    """(r): money constant at Mbar from t+1 on -> pi = 0 after t+1, i_{t+2} = rss."""
    return w * Mbar / (Yss * (1 + rss) ** (-mu))


Mbar = brentq(lambda x: P_next(x) - Pt, 1e-6, 100.0, xtol=1e-15)
check("(s) Mbar solving P_{t+1} = P_t (root find)", Mbar, (1 + g) ** mu * MBt, 1e-12)
check("(s) Mbar / [MB_t(1+gamma*)] = (1+gamma*)^(mu-1)", Mbar / (MBt * (1 + g)), 1.25 ** 3, 1e-12)
S_t1 = (Mbar - MBt) / P_next(Mbar)
check("(t) S_{t+1} = (MB/P)_t [(1+g)^mu - 1]", S_t1, m_real(g) / w * ((1 + g) ** mu - 1), 1e-14)
check("(t) S_{t+1}/S* = (1+g)((1+g)^mu - 1)/g", S_t1 / S_formula(g), 1.25 * (1.25 ** 4 - 1) / 0.25, 1e-10)
print("  Mbar = %.6f MB_t ; S_{t+1} = %.6f ; S* = %.6f ; ratio %.4f"
      % (Mbar, S_t1, S_formula(g), S_t1 / S_formula(g)))
print("  German peak (Jones 2020, ch. 8): prices ~300-fold in one month -> pi ~ %.0f%%/month, %.0fx gamma*"
      % (100 * 299, 299 / 0.25))

# ============================================================ 11.7
header("11.7 -- bank seignorage")


def s_bank(i_, A_, eta_, chi_):
    """(a): s = i (1-chi) (A - eta i)."""
    return i_ * (1 - chi_) * (A_ - eta_ * i_)


def s_bank_direct(i_, A_, eta_, chi_, pY=100.0):
    """Builds M, deposits and interest income in levels, then divides by pY."""
    Mv = (A_ - eta_ * i_) * pY
    D = (1 - chi_) * Mv
    return i_ * D / pY


A7, eta7, chi7 = 0.186, 0.2, 0.435
check("(a) level-built s = formula", s_bank_direct(0.02, A7, eta7, chi7), s_bank(0.02, A7, eta7, chi7), 1e-15)
h = 1e-7
ds = (s_bank(0.02 + h, A7, eta7, chi7) - s_bank(0.02 - h, A7, eta7, chi7)) / (2 * h)
check("(b) ds/di = (1-chi)(A - 2 eta i)", ds, (1 - chi7) * (A7 - 2 * eta7 * 0.02), 1e-7)
# 2018 data (FRED, approximate; see tex): currency ~1.63T, M1 ~3.75T, GDP ~20.6T
cur18, m1_18, gdp18 = 1.63, 3.75, 20.6
chi_d, mpy = cur18 / m1_18, m1_18 / gdp18
print("  (c) chi = %.3f   M/pY = %.4f   s(2%%) = %.5f of GDP" % (chi_d, mpy, 0.02 * (1 - chi_d) * mpy))
A_cal = mpy + 0.2 * 0.02
s2, s3 = s_bank(0.02, A_cal, 0.2, chi_d), s_bank(0.03, A_cal, 0.2, chi_d)
check("(d) calibrated A reproduces M/pY at 2%", A_cal - 0.2 * 0.02, mpy, 1e-15)
print("  (d) A = %.5f   M/pY(3%%) = %.5f   s(3%%) = %.5f   ratio %.4f"
      % (A_cal, A_cal - 0.006, s3, s3 / s2))
check_true("(d) s rises with i at these values (i < A/(2 eta))", s3 > s2 and 0.03 < A_cal / 0.4)

# ============================================================ 11.8
header("11.8 -- realized vs expected real rates")
i8, Epi = 0.06, 0.03
for pi in (0.01, 0.03, 0.05):
    r_real, r_exp = i8 - pi, i8 - Epi
    lender_gain = r_real - r_exp          # per unit lent, in real terms
    print("  pi=%.2f  r=%.3f  r^E=%.3f  lender gains %+.3f, borrower %+.3f"
          % (pi, r_real, r_exp, lender_gain, -lender_gain))
check("r - r^E = E(pi) - pi", (i8 - 0.01) - (i8 - Epi), Epi - 0.01, 1e-15)

# ============================================================ done
print()
if failures:
    print("%d CHECK(S) FAILED: %s" % (len(failures), "; ".join(failures)))
    sys.exit(1)
print("all checks pass")
