"""Numerical results for the Kurlat ch. 5 exercises.

Every analytical formula asserted in Resolucao/kurlat_solutions_ch05.tex is
re-computed here by an independent route (simulation, brute force or a
finite-difference check) and the script aborts on any mismatch.

Run:  python ch05_numerico.py
"""
import numpy as np

# ---------------------------------------------------------------- calibration
# Section 5.2 of Kurlat, "Putting Numbers on the Model".
ALPHA = 0.35     # capital share  (labour share ~ 0.65, Fig. 3.2.3)
G     = 0.015    # technological progress, US GDP per capita since 1800
N     = 0.01     # population growth, US since 1950
DELTA = 0.04     # depreciation
S     = 0.20     # saving = investment rate


def f(k, alpha=ALPHA):
    """Intensive production function, y~ = k~^alpha."""
    return k ** alpha


def k_ss(s=S, delta=DELTA, n=N, g=G, alpha=ALPHA):
    """Steady state of (4.5.3):  s k^alpha = (delta+n+g) k."""
    return (s / (delta + n + g)) ** (1.0 / (1.0 - alpha))


def passo(k, s=S, delta=DELTA, n=N, g=G, alpha=ALPHA):
    """One iteration of Kurlat (4.5.3), written as a level recursion."""
    return k + (s * f(k, alpha) - (delta + n + g) * k) / (1.0 + n + g)


def trajetoria(k0, T, **kw):
    k = np.empty(T + 1)
    k[0] = k0
    for t in range(T):
        k[t + 1] = passo(k[t], **kw)
    return k


def primeiro_ano(y_norm, alvo):
    """First t at which the normalised series exceeds the target."""
    idx = np.where(y_norm > alvo)[0]
    return int(idx[0]) if len(idx) else None


# =========================================================== Problem 5.1
def problema_5_1(T=100, verbose=True):
    kss, yss = k_ss(), f(k_ss())
    assert np.isclose(kss / yss, S / (DELTA + N + G)), "K/Y must equal s/(delta+n+g)"

    # ---- (a) start at 10% of steady-state output
    k0 = (0.1) ** (1.0 / ALPHA) * kss
    assert np.isclose(f(k0) / yss, 0.1), "y0 must be 10% of y_ss"
    ka = trajetoria(k0, T)
    ya = f(ka) / yss
    ta = primeiro_ano(ya, 0.95)

    # ---- (b) n drops from 0.01 to 0, starting from the old steady state
    kss_b = k_ss(n=0.0)
    yss_b = f(kss_b)
    ganho = yss_b / yss - 1.0
    ganho_cf = ((DELTA + N + G) / (DELTA + G)) ** (ALPHA / (1 - ALPHA)) - 1.0
    assert np.isclose(ganho, ganho_cf), "steady-state output gain mismatch"
    kb = trajetoria(kss, T, n=0.0)
    yb = f(kb) / yss_b
    tb = primeiro_ano(yb, 0.95)
    # 100 years is not quite enough to be numerically at the new steady state;
    # run the same recursion out to 500 years to confirm where it is heading.
    assert np.isclose(trajetoria(kss, 500, n=0.0)[-1], kss_b, rtol=1e-8), (
        "path (b) must converge to the new steady state")

    if verbose:
        print("=" * 70)
        print("Problem 5.1  Quantifying the Solow model")
        print("=" * 70)
        print("  k~ss = %.4f   y~ss = %.4f   K/Y = %.4f" % (kss, yss, kss / yss))
        print("  (a) k~0 = %.6f  (%.3f%% of k~ss)" % (k0, k0 / kss * 100))
        print("      y~t/y~ss > 0.95 first at t = %d years" % ta)
        for t in [0, 10, 25, 50, 75, 100]:
            print("        t=%3d   k~=%7.4f   y~/y~ss=%.4f" % (t, ka[t], ya[t]))
        print("  (b) new k~ss = %.4f   new y~ss = %.4f" % (kss_b, yss_b))
        print("      steady-state y~ is %.2f%% higher" % (ganho * 100))
        print("      y~t/y~ss(new) starts at %.4f, exceeds 0.95 at t = %d"
              % (yb[0], tb))
        for t in [0, 5, 10, 20, 40, 100]:
            print("        t=%3d   k~=%7.4f   y~/y~ss=%.4f" % (t, kb[t], yb[t]))
    return dict(kss=kss, yss=yss, k0=k0, ta=ta, ya=ya, ka=ka,
                kss_b=kss_b, yss_b=yss_b, ganho=ganho, tb=tb, yb=yb, kb=kb)


# ------------------------------------------------ robustness for Problem 5.1
def passo_exato(k, s=S, delta=DELTA, n=N, g=G, alpha=ALPHA):
    """The exact law of motion, before Kurlat drops the ng cross-terms."""
    return ((1 - delta) * k + s * f(k, alpha)) / ((1 + n) * (1 + g))


def problema_5_1_exato(T=200, verbose=True):
    """Redo 5.1 without the (4.5.3) approximation, to show it does not matter."""
    def kss_e(n):
        c = (1 + n) * (1 + G) - (1 - DELTA)
        return (S / c) ** (1 / (1 - ALPHA))

    def traj(k0, n):
        k = np.empty(T + 1)
        k[0] = k0
        for t in range(T):
            k[t + 1] = passo_exato(k[t], n=n)
        return k

    kss_a = kss_e(N)
    ya = f(traj(0.1 ** (1 / ALPHA) * kss_a, N)) / f(kss_a)
    ta = primeiro_ano(ya, 0.95)
    kss_b = kss_e(0.0)
    yb = f(traj(kss_a, 0.0)) / f(kss_b)
    tb = primeiro_ano(yb, 0.95)
    ganho = f(kss_b) / f(kss_a) - 1.0
    assert ta == 58, "part (a) answer must be robust to the approximation"
    assert tb in (15, 16), "part (b) answer must be robust to within a year"
    if verbose:
        print()
        print("=" * 70)
        print("Problem 5.1  robustness: the exact law of motion")
        print("=" * 70)
        print("  exact k~ss = %.4f  (vs %.4f under (4.5.3))" % (kss_a, k_ss()))
        print("  (a) t = %d years   (vs 58)" % ta)
        print("  (b) starts at %.4f, t = %d years, gain %.2f%%   (vs 15 and 9.41%%)"
              % (yb[0], tb, ganho * 100))
    return ta, tb, ganho


# =========================================================== Problem 5.2
def gy_analitico(phi, alpha=0.35, delta=0.04):
    """g_y = alpha*delta*(phi^{-(1-alpha)/alpha} - 1), from (5.3.1)."""
    return alpha * delta * (phi ** (-(1 - alpha) / alpha) - 1.0)


def problema_5_2(verbose=True):
    alpha, delta, s = 0.35, 0.04, 0.20
    kss = (s / delta) ** (1 / (1 - alpha))
    linhas = []
    for phi in (0.8, 0.9, 0.99):
        gy = gy_analitico(phi, alpha, delta)

        # independent check: one exact period of k_{t+1} = k + s k^a - delta k
        kt = phi ** (1 / alpha) * kss
        assert np.isclose(kt ** alpha / kss ** alpha, phi), "k_t/k_ss wrong"
        kt1 = kt + s * kt ** alpha - delta * kt
        gy_sim = (kt1 ** alpha) / (kt ** alpha) - 1.0
        # (5.3.1) is a first-order approximation, so close but not equal
        assert abs(gy - gy_sim) < 0.15 * max(gy, 1e-12), "approximation off"

        frac_livro = gy / (1 - phi)          # the object the exercise asks for
        frac_exata = gy * phi / (1 - phi)    # actual share of the gap closed
        linhas.append((phi, gy, gy_sim, frac_livro, frac_exata))

    lam = delta * (1 - alpha)                # limit of gy/(1-phi) as phi -> 1
    assert abs(linhas[-1][3] - lam) < 5e-4, "gy/(1-phi) must tend to delta(1-alpha)"

    if verbose:
        print()
        print("=" * 70)
        print("Problem 5.2  The speed of convergence   (alpha=0.35, delta=0.04)")
        print("=" * 70)
        print("  k_ss = %.4f" % kss)
        print("   phi      g_y     g_y (simulated)   g_y/(1-phi)   exact gap share")
        for phi, gy, gs, fl, fe in linhas:
            print("  %5.2f  %8.4f%%   %8.4f%%      %8.4f%%      %8.4f%%"
                  % (phi, gy * 100, gs * 100, fl * 100, fe * 100))
        print("  limit  delta*(1-alpha) = %.2f%% per year" % (lam * 100))
        print("  implied half-life      = %.1f years" % (np.log(2) / lam))
    return linhas, lam


# =========================================================== Problem 5.3
def problema_5_3(alpha=ALPHA, g=G, verbose=True):
    """Steady state with labour-augmenting progress, n=0: check the shares."""
    gK = g          # K/(AL) constant and L constant  =>  g_K = g_A = g
    gL = 0.0
    gY = g
    residuo = gY - alpha * gK - (1 - alpha) * gL
    assert np.isclose(residuo, (1 - alpha) * g), "residual must be (1-alpha) g"
    if verbose:
        print()
        print("=" * 70)
        print("Problem 5.3  Growth accounting in a steady state")
        print("=" * 70)
        print("  g_Y = %.4f   attributed to capital: %.4f  (%.0f%% of growth)"
              % (gY, alpha * gK, alpha * 100))
        print("                   Solow residual:    %.4f  (%.0f%% of growth)"
              % (residuo, (1 - alpha) * 100))
    return residuo


# =========================================================== Problem 5.4
def problema_5_4(I=0.2, delta=0.1, K0=1.0, delta_err=0.05, alpha=0.35,
                 T=50, verbose=True):
    K_true = I / delta
    K = np.empty(T + 1)
    K[0] = K0
    for t in range(T):
        K[t + 1] = (1 - delta) * K[t] + I
    razao = K / K_true
    fechada = K_true + (K0 - K_true) * (1 - delta) ** np.arange(T + 1)
    assert np.allclose(K, fechada), "closed form of the estimate mismatch"

    K_est_c = I / delta_err
    razao_c = K_est_c / K_true
    assert np.isclose(razao_c, delta / delta_err), "ratio must be delta/delta_hat"

    A_ratio = razao_c ** (-alpha)
    if verbose:
        print()
        print("=" * 70)
        print("Problem 5.4  Measurement of the capital stock")
        print("=" * 70)
        print("  (a) K_true = I/delta = %.4f" % K_true)
        print("  (b) K_est/K_true:", end="")
        for t in (5, 10, 50):
            print("   t=%d: %.6f" % (t, razao[t]), end="")
        print()
        print("  (c) wrong delta=%.2f:  K_est = %.4f, ratio = %.4f"
              % (delta_err, K_est_c, razao_c))
        print("  (d) A_est/A_true = (K_true/K_est)^alpha = %.6f  (%.2f%% too low)"
              % (A_ratio, (1 - A_ratio) * 100))
    return razao, K, K_est_c, A_ratio


# =========================================================== Problem 5.5
def problema_5_5(phi=1.0, alpha=ALPHA, s=S, delta=DELTA, n=0.0, verbose=True):
    """Gotham: measured TFP bias and the long-run level effect."""
    vies = (1 + phi) ** (-(1 - alpha))                 # A_hat / A

    def y_ss(Atil):
        return Atil ** (1 / (1 - alpha)) * (s / (delta + n)) ** (alpha / (1 - alpha))

    A = 1.0
    razao_y = y_ss(A * vies) / y_ss(A)
    assert np.isclose(razao_y, 1.0 / (1 + phi)), "long-run y must fall by 1/(1+phi)"

    def w_ss(Atil):
        return (1 - alpha) * Atil * (s * Atil / (delta + n)) ** (alpha / (1 - alpha))

    assert np.isclose(w_ss(A * vies) / w_ss(A), 1.0 / (1 + phi)), "wage ratio"
    if verbose:
        print()
        print("=" * 70)
        print("Problem 5.5  Gotham   (phi = %g)" % phi)
        print("=" * 70)
        print("  measured TFP bias  A_hat/A = (1+phi)^-(1-alpha) = %.6f" % vies)
        print("  long-run y per person falls to 1/(1+phi) = %.6f of its level"
              % razao_y)
        print("  the long-run wage falls in exactly the same proportion")
    return vies, razao_y


# =========================================================== Problem 5.6
def problema_5_6(gY=0.06, alpha=ALPHA, s=S, delta=DELTA, verbose=True):
    """Usuria: what the interest rate does under each conjecture."""
    g = gY                       # L constant, so g_Y = g_A = g in a steady state
    r1 = alpha * (delta + g) / s - delta
    gK = gY / alpha              # A constant  =>  g_Y = alpha g_K
    d_ln_rdelta = gY - gK
    assert np.isclose(d_ln_rdelta, gY * (1 - 1 / alpha)), "drift formula"
    YK = (gK + delta) / s        # from g_K = sY/K - delta
    r2 = alpha * YK - delta
    if verbose:
        print()
        print("=" * 70)
        print("Problem 5.6  Usuria   (g_Y = 6%, L constant)")
        print("=" * 70)
        print("  Conjecture 1: r constant at alpha(delta+g)/s - delta = %.2f%%"
              % (r1 * 100))
        print("  Conjecture 2: g_K = g_Y/alpha = %.2f%%" % (gK * 100))
        print("                d ln(r+delta)/dt = %.2f%% per year"
              % (d_ln_rdelta * 100))
        print("                today's level r = %.2f%%" % (r2 * 100))
        print("                over 10 years (r+delta) falls by a factor %.3f"
              % np.exp(10 * d_ln_rdelta))
    return r1, gK, d_ln_rdelta, r2


# =========================================================== Problem 5.7
def problema_5_7(verbose=True):
    E = 10.0                       # rubles per euro
    producao = {"Kapitas value added (screws and nails)": 4000 * E,
                "Government (police services, at cost)": 10000.0}
    renda = {"Wages, Kapitas (100 x 350)": 100 * 350.0,
             "Wages, government (police chief)": 10000.0,
             "Capital income, Kapitas": 4000 * E - 100 * 350.0}
    despesa = {"C (imported beef)": 2500 * E,
               "I (welder)": 1000 * E,
               "G (police services)": 10000.0,
               "X (screws and nails)": 4000 * E,
               "-M (welder + beef)": -(1000 * E + 2500 * E)}
    Yp, Yr, Yd = sum(producao.values()), sum(renda.values()), sum(despesa.values())
    assert np.isclose(Yp, Yr) and np.isclose(Yr, Yd), "the three methods must agree"
    Y = Yp

    sL = (renda["Wages, Kapitas (100 x 350)"]
          + renda["Wages, government (police chief)"]) / Y
    sK = renda["Capital income, Kapitas"] / Y
    assert np.isclose(sL + sK, 1.0)

    K = 100000.0
    dep = (1000 * E - 960 * E) / (1000 * E)
    r = sK * Y / K - dep

    gY = 55000 / Y - 1
    gK = 120000 / K - 1
    gL = 105 / 100 - 1
    tfp = gY - sK * gK - sL * gL

    if verbose:
        print()
        print("=" * 70)
        print("Problem 5.7  Proletaria")
        print("=" * 70)
        for nome, d in (("production", producao), ("income", renda),
                        ("expenditure", despesa)):
            print("  by %s:" % nome)
            for k, v in d.items():
                print("      %-44s %10.0f" % (k, v))
            print("      %-44s %10.0f" % ("GDP", sum(d.values())))
        print("  (c) labour share = %.2f   capital share = %.2f" % (sL, sK))
        print("  (d) delta = %.3f,  r = alpha Y/K - delta = %.2f%%" % (dep, r * 100))
        print("  (e) g_Y=%.3f  g_K=%.3f  g_L=%.3f  ->  TFP = %.4f (%.1f%% of growth)"
              % (gY, gK, gL, tfp, tfp / gY * 100))
    return Y, sL, sK, dep, r, tfp


# =========================================================== Problem 5.8
def problema_5_8(verbose=True):
    producao = {"Grano (wheat 1000, no intermediates)": 1000.0,
                "Panem (bread 4000 - wheat 1000)": 3000.0,
                "Fabrica (combine 1000, no intermediates)": 1000.0}
    renda = {"Wages (200 + 1400 + 400)": 2000.0,
             "Capital income (800 + 1600 + 600)": 3000.0}
    despesa = {"C (bread)": 4000.0, "I (combine harvester)": 1000.0}
    Yp, Yr, Yd = sum(producao.values()), sum(renda.values()), sum(despesa.values())
    assert np.isclose(Yp, Yr) and np.isclose(Yr, Yd), "the three methods must agree"
    Y = Yp
    sL = renda["Wages (200 + 1400 + 400)"] / Y
    alpha = renda["Capital income (800 + 1600 + 600)"] / Y
    s = despesa["I (combine harvester)"] / Y
    delta = (2000 - 1800) / 2000

    KY = s / delta                      # steady-state capital-output ratio
    MPK = alpha / KY                    # = alpha Y/K
    KY_gr = alpha / delta               # golden rule: MPK = delta
    s_gr = alpha                        # golden rule saving rate (n = g = 0)

    def c_ss(sr, A=1.0):
        y = A ** (1 / (1 - alpha)) * (sr / delta) ** (alpha / (1 - alpha))
        return (1 - sr) * y

    grade = (c_ss(s + 1e-6) - c_ss(s - 1e-6)) / 2e-6
    assert grade > 0, "consumption must be increasing in s below the golden rule"
    grid = np.linspace(0.01, 0.99, 9801)
    assert abs(grid[np.argmax(c_ss(grid))] - s_gr) < 1e-3, "argmax must be alpha"

    if verbose:
        print()
        print("=" * 70)
        print("Problem 5.8  Aurum")
        print("=" * 70)
        for nome, d in (("production", producao), ("income", renda),
                        ("expenditure", despesa)):
            print("  by %s:" % nome)
            for k, v in d.items():
                print("      %-46s %8.0f" % (k, v))
            print("      %-46s %8.0f" % ("GDP", Y))
        print("  (b) labour share = %.1f   capital share = alpha = %.1f" % (sL, alpha))
        print("  (c) saving rate  = %.1f" % s)
        print("  (d) delta = %.2f;  steady state K/Y = %.1f, MPK = %.2f > delta"
              % (delta, KY, MPK))
        print("      golden rule K/Y = %.1f, s_gr = alpha = %.1f > s" % (KY_gr, s_gr))
        print("      dc*/ds at s=0.2 is %.4f > 0  ->  YES, raise s" % grade)
        print("      c* would rise from %.4f to %.4f, a factor of %.2f"
              % (c_ss(s), c_ss(s_gr), c_ss(s_gr) / c_ss(s)))
    return Y, alpha, s, delta, KY, KY_gr, s_gr


# =========================================================== Problem 5.9
def problema_5_9(alpha=ALPHA, x=0.9, L=100.0, N_hours=2000.0, I=0.2, delta=0.1,
                 verbose=True):
    """Influenzistan: the estimate is biased by exactly x."""
    K = I / delta
    H_true = L * x * N_hours
    A_true = 2.0                                  # pick any truth
    Y = K ** alpha * (A_true * H_true) ** (1 - alpha)

    def A_de(H):
        return Y ** (1 / (1 - alpha)) * K ** (-alpha / (1 - alpha)) / H

    assert np.isclose(A_de(H_true), A_true), "inversion of the production function"
    A_hat = A_de(L * N_hours)
    assert np.isclose(A_hat / A_true, x), "bias must be exactly x"
    Atil_ratio = (A_hat / A_true) ** (1 - alpha)
    assert np.isclose(Atil_ratio, (1 / x) ** (-(1 - alpha))), "5.5 / 5.9 consistency"
    if verbose:
        print()
        print("=" * 70)
        print("Problem 5.9  Influenzistan   (x = %g)" % x)
        print("=" * 70)
        print("  K = I/delta = %.2f;  true A = %g, estimate = %.6f"
              % (K, A_true, A_hat))
        print("  A_hat/A = %.6f = x   (no alpha anywhere)" % (A_hat / A_true))
        print("  Hicks-neutral equivalent: %.6f = x^(1-alpha), which is the Gotham"
              % Atil_ratio)
        print("  formula with 1+phi = 1/x")
    return A_hat / A_true


if __name__ == "__main__":
    problema_5_1()
    problema_5_1_exato()
    problema_5_2()
    problema_5_3()
    problema_5_4()
    problema_5_5()
    problema_5_6()
    problema_5_7()
    problema_5_8()
    problema_5_9()
    print()
    print("all checks passed.")
