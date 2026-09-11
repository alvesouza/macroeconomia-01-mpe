"""Numerical results for the Kurlat ch. 7 exercises.

Every analytical formula asserted in Resolucao/kurlat_solutions_ch07.tex is
re-computed here by an independent route (direct numerical maximisation of the
household's problem, finite differences, or brute force) and the script aborts
on any mismatch.

Run:  python ch07_numerico.py
"""
import numpy as np
from scipy.optimize import minimize_scalar, brentq


# ============================================ the static consumption-leisure problem
def resolve_numerico(uc, vl, w, tau=0.0, T=0.0, tau_c=0.0):
    """Maximise u(c)+v(l) over l in (0,1) with c = w(1-tau)(1-l)/(1+tau_c) + T."""
    def objetivo(l):
        c = w * (1 - tau) * (1 - l) / (1 + tau_c) + T
        if c <= 0 or l <= 0 or l >= 1:
            return 1e12
        return -(uc(c) + vl(l))
    res = minimize_scalar(objetivo, bounds=(1e-9, 1 - 1e-9), method="bounded",
                          options={"xatol": 1e-13})
    return res.x


# =========================================================== Problem 7.1
def problema_7_1(phi=0.4, verbose=True):
    """u = c + phi log l: labour supply is 1 - phi/w, increasing in w."""
    linhas = []
    for w in (0.5, 1.0, 2.0, 5.0, 20.0):
        l_teoria = min(phi / w, 1.0)
        L_teoria = max(1 - phi / w, 0.0)
        l_num = resolve_numerico(lambda c: c, lambda l: phi * np.log(l), w)
        if phi / w < 1:
            assert abs(l_num - l_teoria) < 1e-7, "closed form l = phi/w"
        linhas.append((w, l_teoria, L_teoria, l_num))
    # labour supply is strictly increasing in w, and tends to 1
    Ls = [x[2] for x in linhas]
    assert all(b > a for a, b in zip(Ls, Ls[1:])), "hours must rise with the wage"
    assert 1 - phi / 1e6 > 0.999999, "hours tend to one as w grows"

    # contrast: log-log preferences give hours independent of w
    alpha = 1.54
    for w in (0.5, 2.0, 20.0):
        l_num = resolve_numerico(np.log, lambda l: alpha * np.log(l), w)
        assert abs(l_num - alpha / (1 + alpha)) < 1e-7, "log-log: l = alpha/(1+alpha)"

    if verbose:
        print("=" * 74)
        print("Problem 7.1  u = c + phi log(l)   (phi = %.2f)" % phi)
        print("=" * 74)
        print("      w      l = phi/w    hours 1-l    l (numerical)")
        for w, l, L, ln in linhas:
            print("  %6.2f     %8.4f     %8.4f      %8.4f" % (w, l, L, ln))
        print("  hours are strictly INCREASING in w and tend to 1 --- the data")
        print("  (Bick et al. 2018, Fig. 7.3.2) show the opposite sign.")
        print("  With u = log c + alpha log l instead, hours are constant at")
        print("  1/(1+alpha) = %.4f, independent of w." % (1 / (1 + alpha)))
    return linhas


# =========================================================== Problem 7.2
def problema_7_2(w=2.0, tau=0.3, sigma=2.0, eta=1.5, verbose=True):
    """Lump-sum tax used to hire soldiers == conscription of m = tau/w units."""
    def uc(c):
        return (c ** (1 - sigma) - 1) / (1 - sigma)

    def vl(l):
        return 3.0 * (l ** (1 - eta) - 1) / (1 - eta)

    m = tau / w

    # policy 1: lump-sum tax tau, c = w(1-l) - tau
    def obj1(l):
        c = w * (1 - l) - tau
        if c <= 0 or l <= 0 or l >= 1:
            return 1e12
        return -(uc(c) + vl(l))

    # policy 2: conscription of m units, c = w(1 - m - l)
    def obj2(l):
        c = w * (1 - m - l)
        if c <= 0 or l <= 0 or l >= 1 - m:
            return 1e12
        return -(uc(c) + vl(l))

    l1 = minimize_scalar(obj1, bounds=(1e-9, 1 - 1e-9), method="bounded",
                         options={"xatol": 1e-13}).x
    l2 = minimize_scalar(obj2, bounds=(1e-9, 1 - m - 1e-9), method="bounded",
                         options={"xatol": 1e-13}).x
    c1, c2 = w * (1 - l1) - tau, w * (1 - m - l2)
    assert abs(l1 - l2) < 1e-6, "leisure must be identical under both policies"
    assert abs(c1 - c2) < 1e-6, "consumption must be identical"
    # non-army labour
    n1, n2 = 1 - l1 - m, 1 - m - l2
    assert abs(n1 - n2) < 1e-6, "non-army labour must be identical"

    if verbose:
        print()
        print("=" * 74)
        print("Problem 7.2  Military service   (w=%.1f, tau=%.2f, m=tau/w=%.3f)"
              % (w, tau, m))
        print("=" * 74)
        print("  policy            leisure l    consumption c   army   non-army")
        print("  lump-sum tax      %9.6f    %12.6f  %5.3f   %8.6f" % (l1, c1, m, n1))
        print("  conscription      %9.6f    %12.6f  %5.3f   %8.6f" % (l2, c2, m, n2))
        print("  the two budget constraints are literally the same line, since")
        print("  w*m = tau by construction.")
    return l1, c1, m


# =========================================================== Problem 7.3
def problema_7_3(w=2.0, tau=0.3, sigma=2.0, eta=1.5, verbose=True):
    """An income tax and a consumption tax enter only through (1-tau)/(1+tau_c)."""
    def uc(c):
        return (c ** (1 - sigma) - 1) / (1 - sigma)

    def vl(l):
        return 3.0 * (l ** (1 - eta) - 1) / (1 - eta)

    # (d) the equivalent consumption tax
    tau_c = tau / (1 - tau)
    assert np.isclose((1 - tau) / (1 + 0.0), (1 - 0.0) / (1 + tau_c)), \
        "the two wedges must coincide"

    l_renda = resolve_numerico(uc, vl, w, tau=tau, tau_c=0.0)
    l_consumo = resolve_numerico(uc, vl, w, tau=0.0, tau_c=tau_c)
    assert abs(l_renda - l_consumo) < 1e-7, "(d) the allocation must be unchanged"

    def receita(l, tau, tau_c):
        c = w * (1 - tau) * (1 - l) / (1 + tau_c)
        R_formula = w * (1 - l) * (tau + tau_c) / (1 + tau_c)
        R_direta = tau * w * (1 - l) + tau_c * c
        R_recurso = w * (1 - l) - c            # revenue = output minus consumption
        assert np.isclose(R_formula, R_direta), "(c) revenue formula"
        assert np.isclose(R_formula, R_recurso), "revenue = w(1-l) - c"
        return R_formula, c

    R1, c1 = receita(l_renda, tau, 0.0)
    R2, c2 = receita(l_consumo, 0.0, tau_c)
    assert np.isclose(R1, R2), "(e) revenue must be identical"
    assert np.isclose(c1, c2), "consumption must be identical"

    # a grid of (tau, tau_c) pairs that leave the wedge (1-tau)/(1+tau_c) unchanged
    pares = []
    for tc in (0.0, 0.15, 0.30, tau_c):
        t = 1 - (1 - tau) * (1 + tc)          # solves (1-t)/(1+tc) = (1-tau)/1
        l = resolve_numerico(uc, vl, w, tau=t, tau_c=tc)
        assert abs(l - l_renda) < 1e-6, "every pair on the iso-wedge line agrees"
        R, _ = receita(l, t, tc)
        assert np.isclose(R, R1), "and raises exactly the same revenue"
        pares.append((t, tc, l, R))

    if verbose:
        print()
        print("=" * 74)
        print("Problem 7.3  Income vs consumption taxes   (w=%.1f, tau=%.2f)" % (w, tau))
        print("=" * 74)
        print("  (d) equivalent consumption tax: tau_c = tau/(1-tau) = %.6f" % tau_c)
        print("      leisure under the income tax      = %.8f" % l_renda)
        print("      leisure under the consumption tax = %.8f" % l_consumo)
        print("  (e) revenue: %.8f vs %.8f  --- identical" % (R1, R2))
        print("      consumption: %.8f vs %.8f" % (c1, c2))
        print("  every (tau, tau_c) with the same wedge gives the same allocation:")
        print("      tau      tau_c        l          revenue")
        for t, tc, l, R in pares:
            print("   %7.4f  %7.4f   %8.6f   %10.6f" % (t, tc, l, R))
    return tau_c, R1, R2


# =========================================================== Problem 7.5
ALPHA_P, W_P = 1.54, 1.0
US = dict(nome="US", tau=0.34, T=0.102)
EU = dict(nome="Europe", tau=0.53, T=0.124)


def lazer(tau, T, alpha=ALPHA_P, w=W_P):
    """Part (b): l = alpha (w(1-tau) + T) / [(1+alpha) w(1-tau)]."""
    return alpha * (w * (1 - tau) + T) / ((1 + alpha) * w * (1 - tau))


def lazer_orcamento_equilibrado(tau, alpha=ALPHA_P):
    """With T = tau w (1-l) the closed form collapses to l = alpha/(1+alpha-tau)."""
    return alpha / (1 + alpha - tau)


def problema_7_5(verbose=True):
    alpha, w = ALPHA_P, W_P

    # (a)-(b) verified against direct maximisation
    for pais in (US, EU):
        l_cf = lazer(pais["tau"], pais["T"])
        l_num = resolve_numerico(np.log, lambda l: alpha * np.log(l), w,
                                 tau=pais["tau"], T=pais["T"])
        assert abs(l_cf - l_num) < 1e-7, "closed form for l"
        pais["l"] = l_cf
        pais["L"] = 1 - l_cf
        pais["c"] = w * (1 - pais["tau"]) * pais["L"] + pais["T"]
        pais["R"] = pais["tau"] * w * pais["L"]

    # (c) with T = 0, leisure does not depend on tau at all
    for tau in (0.0, 0.2, 0.34, 0.53, 0.8):
        assert np.isclose(lazer(tau, 0.0), alpha / (1 + alpha)), \
            "(c) with T=0 leisure is alpha/(1+alpha), independent of tau"

    # (e) the budgets balance
    for pais in (US, EU):
        assert abs(pais["R"] - pais["T"]) < 6e-4, "(e) budget must balance"
        # and the exact balanced-budget closed form is very close
        assert abs(pais["l"] - lazer_orcamento_equilibrado(pais["tau"])) < 2e-4

    # (f) GDP
    razao_Y = EU["L"] / US["L"]

    # (g) welfare
    lam = (EU["c"] / US["c"]) * (EU["l"] / US["l"]) ** alpha
    lhs = np.log(EU["c"]) + alpha * np.log(EU["l"])
    rhs = np.log(lam * US["c"]) + alpha * np.log(US["l"])
    assert np.isclose(lhs, rhs), "lambda must equate the two utilities"

    # decomposition of the hours gap
    L_so_tau = 1 - lazer(US["tau"], EU["T"])     # Europe's T, US tax rate
    L_so_T = 1 - lazer(EU["tau"], US["T"])       # Europe's tax rate, US transfer
    gap = US["L"] - EU["L"]
    parte_tau = (L_so_tau - EU["L"]) / gap
    parte_T = (L_so_T - EU["L"]) / gap

    # (k)-(l) the Frisch elasticity is l/(1-l)
    for pais in (US, EU):
        e_cf = pais["l"] / pais["L"]
        # finite-difference check, holding c fixed:  1-l = 1 - alpha c / (w(1-tau))
        wn, c = w * (1 - pais["tau"]), pais["c"]
        h = 1e-7

        def L_de(wn_):
            return 1 - alpha * c / wn_
        e_num = (L_de(wn + h) - L_de(wn - h)) / (2 * h) * wn / L_de(wn)
        assert abs(e_cf - e_num) < 1e-4, "Frisch elasticity = l/(1-l)"
        pais["frisch"] = e_cf

    if verbose:
        print()
        print("=" * 74)
        print("Problem 7.5  Prescott's calculation   (alpha=%.2f, w=%.1f)" % (alpha, w))
        print("=" * 74)
        print("  country    tau      T        l         1-l        c      revenue")
        for pais in (US, EU):
            print("  %-8s %5.2f  %6.3f  %8.6f  %8.6f  %8.6f  %8.6f"
                  % (pais["nome"], pais["tau"], pais["T"], pais["l"], pais["L"],
                     pais["c"], pais["R"]))
        print("  (c) with T=0: l = alpha/(1+alpha) = %.6f for EVERY tau"
              % (alpha / (1 + alpha)))
        print("      with a balanced budget: l = alpha/(1+alpha-tau) = %.6f (US), "
              "%.6f (EU)" % (lazer_orcamento_equilibrado(US["tau"]),
                             lazer_orcamento_equilibrado(EU["tau"])))
        print("  (d) Americans work %.1f%% of their adult lives, Europeans %.1f%%"
              % (US["L"] * 100, EU["L"] * 100))
        print("      decomposition of the %.6f gap in hours:" % gap)
        print("        moving Europe to the US tax rate alone: %.1f%% of the gap"
              % (parte_tau * 100))
        print("        moving Europe to the US transfer alone: %.1f%% of the gap"
              % (parte_T * 100))
        print("  (e) revenue vs transfer: US %.6f vs %.3f;  EU %.6f vs %.3f"
              % (US["R"], US["T"], EU["R"], EU["T"]))
        print("  (f) Europe's GDP per capita is %.1f%% lower" % ((1 - razao_Y) * 100))
        print("  (g) lambda = %.6f, so Europe is %.1f%% worse off in consumption"
              % (lam, (1 - lam) * 100))
        print("      equivalent terms --- about half the output gap")
        print("  (l) Frisch elasticity l/(1-l): US %.4f, Europe %.4f"
              % (US["frisch"], EU["frisch"]))
        print("      empirical estimates are 0.4 to 1.0")
    return US, EU, razao_Y, lam, parte_tau, parte_T


# =========================================================== Problem 7.6
def problema_7_6(theta=0.35, verbose=True):
    """Protestant work ethic: alpha falls, labour supply rises, the wage falls."""
    def equilibrio(alpha):
        L = 1 / (1 + alpha)                 # inelastic supply, log-log preferences
        w = (1 - theta) * L ** (-theta)     # = F_L with K = 1
        Y = L ** (1 - theta)
        c = w * L
        return L, w, Y, c

    linhas = [(a,) + equilibrio(a) for a in (2.5, 1.54, 1.0, 0.5)]
    # w = (1-theta)(1+alpha)^theta, increasing in alpha
    for a, L, w, Y, c in linhas:
        assert np.isclose(w, (1 - theta) * (1 + a) ** theta), "closed form for w"
        assert np.isclose(c, (1 - theta) * Y), "labour income share is 1-theta"
    ws = [x[2] for x in linhas]
    assert all(b < a for a, b in zip(ws, ws[1:])), "lower alpha must lower the wage"
    Ys = [x[3] for x in linhas]
    assert all(b > a for a, b in zip(Ys, Ys[1:])), "lower alpha must raise output"

    # the household's supply really is inelastic: check by direct maximisation
    for alpha in (0.5, 1.54, 2.5):
        for w in (0.4, 1.0, 3.0):
            l = resolve_numerico(np.log, lambda l: alpha * np.log(l), w)
            assert abs(l - alpha / (1 + alpha)) < 1e-7, "vertical labour supply"

    if verbose:
        print()
        print("=" * 74)
        print("Problem 7.6  The Protestant work ethic   (theta=%.2f, K=1)" % theta)
        print("=" * 74)
        print("   alpha    L=1/(1+alpha)      w         Y         c")
        for a, L, w, Y, c in linhas:
            print("  %6.2f      %8.5f     %8.5f  %8.5f  %8.5f" % (a, L, w, Y, c))
        print("  a fall in alpha (less taste for leisure) raises L and Y")
        print("  but LOWERS w, because K is fixed and the MPL is decreasing.")
    return linhas


# =========================================================== Problem 7.7
def problema_7_7(kappa=0.12, beta_bar=0.5, y=1.0, b=0.4, gamma=0.5, A0=0.4,
                 verbose=True):
    """DMP with a constant-returns matching function m = A V^gamma U^(1-gamma)."""
    def m(V, U, A):
        return A * V ** gamma * U ** (1 - gamma)

    def q(V, U, A):
        return m(V, U, A) / V

    q_bar = kappa / ((1 - beta_bar) * (y - b))     # free entry pins q at this value

    def V_equilibrio(U, A):
        """Solve kappa = q(V,U) (1-beta)(y-b) for V."""
        return brentq(lambda V: q(V, U, A) - q_bar, 1e-10, 1e6,
                      xtol=1e-15, rtol=1e-15)

    def resultado(U, A):
        V = V_equilibrio(U, A)
        matches = m(V, U, A)
        assert matches < U, "matches cannot exceed the pool of searchers"
        return V, U - matches, matches / U      # V, hat-U, job-finding rate

    U0 = 0.08

    # ---- (a) a better recruiting technology, U held fixed
    linhas_a = [(mult,) + resultado(U0, A0 * mult) for mult in (1.0, 1.1, 1.2, 1.3)]
    Vs = [x[1] for x in linhas_a]
    Uhs = [x[2] for x in linhas_a]
    assert all(y2 > y1 for y1, y2 in zip(Vs, Vs[1:])), "(a) V must rise with A"
    assert all(y2 < y1 for y1, y2 in zip(Uhs, Uhs[1:])), "(a) hat-U must fall with A"

    # ---- (b) a higher initial unemployment rate, A held fixed
    linhas_b = []
    for U in (0.06, 0.08, 0.10, 0.14):
        V, Uh, f = resultado(U, A0)
        linhas_b.append((U, V, Uh, V / U, f))
    Vs = [x[1] for x in linhas_b]
    Uhs = [x[2] for x in linhas_b]
    aperto = [x[3] for x in linhas_b]
    assert all(y2 > y1 for y1, y2 in zip(Vs, Vs[1:])), "(b) V must rise with U"
    assert all(y2 > y1 for y1, y2 in zip(Uhs, Uhs[1:])), "(b) hat-U must ALSO rise"
    assert max(aperto) - min(aperto) < 1e-9,         "with constant returns, (7.5.1) pins V/U, so it cannot move with U"
    # and hat-U is exactly proportional to U
    prop = [x[2] / x[0] for x in linhas_b]
    assert max(prop) - min(prop) < 1e-9, "hat-U is proportional to U"

    if verbose:
        print()
        print("=" * 74)
        print("Problem 7.7  The Beveridge curve   (kappa=%.2f, beta=%.1f, y-b=%.1f, "
              "gamma=%.1f, A=%.1f)" % (kappa, beta_bar, y - b, gamma, A0))
        print("=" * 74)
        print("  free entry pins q = kappa/[(1-beta)(y-b)] = %.4f, and with constant"
              % q_bar)
        print("  returns that pins the ratio V/U at %.4f." % linhas_b[0][3])
        print("  (a) better recruiting technology (A up), U = %.2f fixed:" % U0)
        print("         A/A0        V        hat-U    finding rate")
        for mult, V, Uh, f in linhas_a:
            print("      %6.2f   %8.5f   %8.5f     %8.5f" % (mult, V, Uh, f))
        print("      V up, hat-U down: a NEGATIVE comovement, so the points trace")
        print("      out something that looks like a Beveridge curve.")
        print("  (b) a higher initial unemployment rate, A fixed:")
        print("          U         V        hat-U      V/U    finding rate")
        for U, V, Uh, t, f in linhas_b:
            print("      %5.2f   %8.5f   %8.5f   %6.3f     %8.5f" % (U, V, Uh, t, f))
        print("      V up and hat-U up: a POSITIVE comovement. This does NOT look")
        print("      like a Beveridge curve --- it shifts the curve outward.")
    return linhas_a, linhas_b


if __name__ == "__main__":
    problema_7_1()
    problema_7_2()
    problema_7_3()
    problema_7_5()
    problema_7_6()
    problema_7_7()
    print()
    print("all checks passed.")
