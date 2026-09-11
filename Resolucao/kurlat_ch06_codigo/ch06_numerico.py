"""Numerical results for the Kurlat ch. 6 exercises.

Every analytical formula asserted in Resolucao/kurlat_solutions_ch06.tex is
re-computed here by an independent route (direct numerical maximisation of the
household's problem, brute force, or a finite-difference check) and the script
aborts on any mismatch.

Run:  python ch06_numerico.py
"""
import numpy as np
from scipy.optimize import minimize_scalar


# ================================================== the two-period household
def omega(beta, r, sigma):
    """Omega = 1 + beta^(1/sigma) (1+r)^((1-sigma)/sigma), the denominator of (6.2.9)."""
    return 1.0 + beta ** (1 / sigma) * (1 + r) ** ((1 - sigma) / sigma)


def solucao_2p(y1, y2, beta, r, sigma, tau1=0.0, tau2=0.0, a0=0.0):
    """Closed-form solution of Problem 6.1."""
    W = a0 + y1 - tau1 + (y2 - tau2) / (1 + r)
    c1 = W / omega(beta, r, sigma)
    c2 = (beta * (1 + r)) ** (1 / sigma) * c1
    a = a0 + y1 - tau1 - c1
    return c1, c2, a, W


def u(c, sigma):
    if abs(sigma - 1.0) < 1e-12:
        return np.log(c)
    return (c ** (1 - sigma) - 1) / (1 - sigma)


def solucao_2p_numerica(y1, y2, beta, r, sigma, tau1=0.0, tau2=0.0, a0=0.0,
                        limite=None):
    """Maximise directly over c1, with an optional borrowing limit a >= -limite."""
    W = a0 + y1 - tau1 + (y2 - tau2) / (1 + r)
    teto = W - 1e-9
    if limite is not None:
        teto = min(teto, a0 + y1 - tau1 + limite)

    def objetivo(c1):
        c2 = (1 + r) * (W - c1)
        if c1 <= 0 or c2 <= 0:
            return 1e12
        return -(u(c1, sigma) + beta * u(c2, sigma))

    res = minimize_scalar(objetivo, bounds=(1e-9, teto), method="bounded",
                          options={"xatol": 1e-12})
    c1 = res.x
    return c1, (1 + r) * (W - c1), a0 + y1 - tau1 - c1


# =========================================================== Problem 6.1
def problema_6_1(verbose=True):
    y1, y2, beta, r = 1.0, 0.8, 0.96, 0.05
    linhas = []
    for sigma in (0.5, 1.0, 2.0, 4.0):
        c1, c2, a, W = solucao_2p(y1, y2, beta, r, sigma)
        c1n, c2n, an = solucao_2p_numerica(y1, y2, beta, r, sigma)
        assert abs(c1 - c1n) < 1e-6, "closed form must match direct maximisation"
        assert abs(c2 - c2n) < 1e-6

        # Euler equation holds
        assert np.isclose(c1 ** (-sigma), beta * (1 + r) * c2 ** (-sigma))
        # budget constraint holds
        assert np.isclose(c1 + c2 / (1 + r), W)

        # comparative statics, by finite differences on c1/y1
        h = 1e-6
        d_y2 = (solucao_2p(y1, y2 + h, beta, r, sigma)[0]
                - solucao_2p(y1, y2 - h, beta, r, sigma)[0]) / (2 * h) / y1
        d_a0 = (solucao_2p(y1, y2, beta, r, sigma, a0=h)[0]
                - solucao_2p(y1, y2, beta, r, sigma, a0=-h)[0]) / (2 * h) / y1
        d_be = (solucao_2p(y1, y2, beta + h, r, sigma)[0]
                - solucao_2p(y1, y2, beta - h, r, sigma)[0]) / (2 * h) / y1
        assert d_y2 > 0, "dc1/dy2 must be positive"
        assert np.isclose(d_y2, 1 / (omega(beta, r, sigma) * (1 + r) * y1))
        assert d_a0 > 0, "dc1/da0 must be positive"
        assert np.isclose(d_a0, 1 / (omega(beta, r, sigma) * y1))
        assert d_be < 0, "dc1/dbeta must be negative: patience means saving"

        # part (e): y2 = tau1 = tau2 = 0, sign of dc1/dr is the sign of sigma - 1
        d_r = (solucao_2p(y1, 0.0, beta, r + h, sigma, a0=0.2)[0]
               - solucao_2p(y1, 0.0, beta, r - h, sigma, a0=0.2)[0]) / (2 * h)
        analitico = -(0.2 + y1) * beta ** (1 / sigma) * ((1 - sigma) / sigma) \
            * (1 + r) ** ((1 - 2 * sigma) / sigma) / omega(beta, r, sigma) ** 2
        assert abs(d_r - analitico) < 1e-4, "dc1/dr closed form"
        assert np.sign(d_r) == np.sign(sigma - 1) or abs(d_r) < 1e-9, \
            "sign of dc1/dr must be the sign of sigma-1"
        linhas.append((sigma, c1, c2, a, d_r))

    if verbose:
        print("=" * 74)
        print("Problem 6.1  Two-period problem   (y1=1, y2=0.8, beta=0.96, r=0.05)")
        print("=" * 74)
        print("  sigma      c1        c2         a      dc1/dr  (part e, a0=0.2, y2=0)")
        for sg, c1, c2, a, dr in linhas:
            print("  %5.2f  %8.5f  %8.5f  %8.5f   %+10.6f" % (sg, c1, c2, a, dr))
        print("  the sign of dc1/dr is the sign of sigma-1: negative, zero, positive")
    return linhas


# =========================================================== Problem 6.9
def problema_6_9(verbose=True):
    y1, beta, sigma = 1.0, 0.96, 2.0
    linhas = []
    for m in (0.0, 0.5, 1.0, 3.0):
        for r in (0.02, 0.05, 0.20):
            c1, c2, _, _ = solucao_2p(y1, m * y1, beta, r, sigma)
            x = 0.01
            # (a) both incomes up by x%
            c1a, c2a, _, _ = solucao_2p(y1 * (1 + x), m * y1 * (1 + x), beta, r, sigma)
            assert np.isclose(c1a / c1 - 1, x), "homothetic: both up by x%"
            assert np.isclose(c2a / c2 - 1, x)
            # (b) only y1 up by x%
            c1b, c2b, _, _ = solucao_2p(y1 * (1 + x), m * y1, beta, r, sigma)
            elast = (1 + r) / (1 + r + m)
            assert np.isclose(c1b / c1 - 1, x * elast), "elasticity = y1/W"
            assert np.isclose(c2b / c2 - 1, x * elast), "c2 moves in the same proportion"
            linhas.append((m, r, elast))
    if verbose:
        print()
        print("=" * 74)
        print("Problem 6.9  Proportional MPC   (elasticity of c1 to y1 = y1/W)")
        print("=" * 74)
        print("     m      r    (1+r)/(1+r+m)")
        for m, r, e in linhas:
            print("  %5.1f  %5.2f      %8.5f" % (m, r, e))
        print("  independent of beta and sigma: CRRA preferences are homothetic")
    return linhas


# =========================================================== Problem 6.3
def problema_6_3(verbose=True):
    """At the endowment point a rise in r lowers c1 and raises utility."""
    y1, y2, sigma = 1.0, 1.0, 2.0
    r0 = 0.05
    # pick beta so that the household exactly consumes its endowment at r0:
    # Euler c1^-s = beta(1+r) c2^-s with c1=y1, c2=y2  =>  beta = (y2/y1)^-s/(1+r)
    beta = (y2 / y1) ** (-sigma) / (1 + r0)
    c1, c2, a, _ = solucao_2p(y1, y2, beta, r0, sigma)
    assert np.isclose(c1, y1) and np.isclose(c2, y2) and abs(a) < 1e-12, \
        "calibration must put the household exactly at its endowment"
    U0 = u(c1, sigma) + beta * u(c2, sigma)

    linhas = []
    for r1 in (0.08, 0.12, 0.20):
        c1n, c2n, an, _ = solucao_2p(y1, y2, beta, r1, sigma)
        U1 = u(c1n, sigma) + beta * u(c2n, sigma)
        assert c1n < y1, "(a) c1 must fall"
        assert an > 0, "the household must become a lender"
        assert U1 > U0, "(b) utility must rise"
        linhas.append((r1, c1n, c2n, an, U1 - U0))
    if verbose:
        print()
        print("=" * 74)
        print("Problem 6.3  A rise in r at the endowment point  (y1=y2=1, sigma=2)")
        print("=" * 74)
        print("  calibrated beta = %.6f so that c1=y1 and c2=y2 at r=%.2f" % (beta, r0))
        print("      r        c1        c2         a      U - U0")
        print("  %5.2f  %8.5f  %8.5f  %8.5f   %8.5f" % (r0, c1, c2, a, 0.0))
        for r1, c1n, c2n, an, dU in linhas:
            print("  %5.2f  %8.5f  %8.5f  %8.5f   %+8.5f" % (r1, c1n, c2n, an, dU))
        print("  c1 falls (so a one-year consumption measure records a welfare loss)")
        print("  while lifetime utility rises: that is the content of parts (c)-(d)")
    return beta, linhas


# =========================================================== Problem 6.6
def problema_6_6(verbose=True):
    """A tax on interest income: saving can rise, fall, or not move."""
    r, tau = 0.10, 0.5
    casos = []

    def resolve_com_kink(y1, y2, beta, sigma):
        """Optimise over the kinked budget set: r(1-tau) if saving, r if borrowing."""
        melhor = None
        for taxa, lado in ((r * (1 - tau), "save"), (r, "borrow")):
            c1, c2, a, _ = solucao_2p(y1, y2, beta, taxa, sigma)
            ok = (a >= -1e-12) if lado == "save" else (a <= 1e-12)
            if not ok:                      # the interior solution is on the wrong side
                continue
            val = u(c1, sigma) + beta * u(c2, sigma)
            if melhor is None or val > melhor[0]:
                melhor = (val, c1, c2, a)
        if melhor is None:                  # corner: stay at the kink
            return u(y1, sigma) + beta * u(y2, sigma), y1, y2, 0.0
        # the kink itself is always feasible; compare
        val_kink = u(y1, sigma) + beta * u(y2, sigma)
        if val_kink > melhor[0]:
            return val_kink, y1, y2, 0.0
        return melhor

    # (i) a saver with a low EIS (sigma large): saves MORE when the return falls
    y1, y2, beta, sigma = 2.0, 0.5, 0.97, 5.0
    _, _, a_antes, _ = solucao_2p(y1, y2, beta, r, sigma)
    a_dep = resolve_com_kink(y1, y2, beta, sigma)[3]
    assert a_antes > 0 and a_dep > a_antes, "(i) low EIS saver must save more"
    casos.append(("(i)  saver, sigma=5.0 (low EIS)", a_antes, a_dep))

    # (ii) a saver with a high EIS (sigma small): saves LESS
    sigma = 0.4
    _, _, a_antes, _ = solucao_2p(y1, y2, beta, r, sigma)
    a_dep = resolve_com_kink(y1, y2, beta, sigma)[3]
    assert a_antes > 0 and a_dep < a_antes, "(ii) high EIS saver must save less"
    casos.append(("(ii) saver, sigma=0.4 (high EIS)", a_antes, a_dep))

    # (iii) a borrower: untouched, since the tax falls on interest income only
    y1, y2, sigma = 0.5, 2.0, 2.0
    _, _, a_antes, _ = solucao_2p(y1, y2, beta, r, sigma)
    a_dep = resolve_com_kink(y1, y2, beta, sigma)[3]
    assert a_antes < 0 and np.isclose(a_antes, a_dep), "(iii) borrower unaffected"
    casos.append(("(iii) borrower, sigma=2.0", a_antes, a_dep))

    if verbose:
        print()
        print("=" * 74)
        print("Problem 6.6  A tax on interest income   (r=%.2f, tau=%.2f)" % (r, tau))
        print("=" * 74)
        print("  case                                 a before    a after")
        for nome, a0_, a1_ in casos:
            print("  %-34s %9.5f  %9.5f" % (nome, a0_, a1_))
    return casos


# =========================================================== Problem 6.4
def problema_6_4(verbose=True):
    beta, r, sigma = 1.0, 0.0, 2.0
    dados = {"A": (2.0, 4.0), "B": (6.0, 4.0)}
    out = {}
    for nome, (y1, y2) in dados.items():
        c1, c2, a, _ = solucao_2p(y1, y2, beta, r, sigma)
        assert np.isclose(c1, (y1 + y2) / 2) and np.isclose(c2, c1), \
            "beta=1 and r=0 must give perfect smoothing"
        out[nome] = (y1, y2, c1, c2, a)

    # (c) fit a line through the two period-1 points
    y = np.array([out["A"][0], out["B"][0]])
    c = np.array([out["A"][2], out["B"][2]])
    b, a_int = np.polyfit(y, c, 1)
    assert np.isclose(b, 0.5) and np.isclose(a_int, 2.0), "Keynesian fit c = 2 + 0.5 y"
    apc = c / y

    # (d) pooling both periods, the same income maps to two consumption levels
    ypool = np.array([out["A"][0], out["B"][0], out["A"][1], out["B"][1]])
    cpool = np.array([out["A"][2], out["B"][2], out["A"][3], out["B"][3]])
    iguais = np.isclose(ypool, 4.0)
    assert not np.isclose(cpool[iguais][0], cpool[iguais][1]), \
        "same income, different consumption: no consumption function of y exists"
    b2 = np.polyfit(ypool, cpool, 1)[0]
    if verbose:
        print()
        print("=" * 74)
        print("Problem 6.4  Two households, beta=1, r=0")
        print("=" * 74)
        print("  household   y1   y2    c1    c2      a       APC1")
        for nome in "AB":
            y1, y2, c1, c2, a = out[nome]
            print("      %s      %4.1f %4.1f  %4.1f  %4.1f  %+5.1f     %5.3f"
                  % (nome, y1, y2, c1, c2, a, c1 / y1))
        print("  (c) period-1 fit:  c = %.1f + %.1f y   -> looks perfectly Keynesian"
              % (a_int, b))
        print("      APC falls with income: %.3f then %.3f" % (apc[0], apc[1]))
        print("  (d) pooling both periods: y=4 gives c=3 for A and c=5 for B,")
        print("      so no function c(y) exists; the pooled slope collapses to %.2f" % b2)
    return out, b, a_int


# =========================================================== Problem 6.2
def problema_6_2(verbose=True):
    """Athletes vs residents: saving rates and the response to a fall in r."""
    beta, sigma = 0.97, 2.0
    r0, r1 = 0.06, 0.02
    perfis = {"athlete  (y1=10, y2=2)": (10.0, 2.0),
              "resident (y1=3,  y2=9)": (3.0, 9.0)}
    linhas = []
    for nome, (y1, y2) in perfis.items():
        c1, _, a, _ = solucao_2p(y1, y2, beta, r0, sigma)
        s0 = (y1 - c1) / y1
        c1b, _, ab, _ = solucao_2p(y1, y2, beta, r1, sigma)
        s1 = (y1 - c1b) / y1
        linhas.append((nome, s0, s1, s1 - s0, a))
    assert linhas[0][1] > linhas[1][1], "(a) the athlete must save more"
    assert linhas[0][4] > 0 > linhas[1][4], "athlete lends, resident borrows"
    assert abs(linhas[1][3]) > abs(linhas[0][3]), \
        "(b) the resident's saving rate must react more to r"
    if verbose:
        print()
        print("=" * 74)
        print("Problem 6.2  Athletes and residents   (r: %.2f -> %.2f)" % (r0, r1))
        print("=" * 74)
        print("  profile                     s at r0     s at r1     change      a")
        for nome, s0, s1, d, a in linhas:
            print("  %-26s %8.4f  %10.4f  %+9.4f  %+7.3f" % (nome, s0, s1, d, a))
        print("  the resident's saving rate moves %.1fx more than the athlete's"
              % (abs(linhas[1][3]) / abs(linhas[0][3])))
    return linhas


# =========================================================== Problem 6.5
def problema_6_5(verbose=True):
    """Credit constraints: when they bind, and the two stimulus policies."""
    beta, sigma, r = 0.96, 2.0, 0.05
    Om = omega(beta, r, sigma)

    def liga(y1, y2, b, tau1=0.0, tau2=0.0):
        """True if the constraint a >= -b binds."""
        c1u = solucao_2p(y1, y2, beta, r, sigma, tau1, tau2)[0]
        return c1u > y1 - tau1 + b

    def resolve(y1, y2, b, tau1=0.0, tau2=0.0):
        c1u = solucao_2p(y1, y2, beta, r, sigma, tau1, tau2)[0]
        c1 = min(c1u, y1 - tau1 + b)
        return c1, y2 - tau2 + (1 + r) * (y1 - tau1 - c1), y1 - tau1 - c1

    # the closed-form binding condition
    for (y1, y2, b) in [(1.0, 3.0, 0.1), (3.0, 1.0, 0.1), (1.0, 3.0, 5.0),
                        (2.0, 2.0, 0.0), (0.5, 4.0, 0.3)]:
        cond = (y2 / (1 + r)) > (Om - 1) * y1 + Om * b
        assert cond == liga(y1, y2, b), "closed-form binding condition"

    # monotonicity claims of part (d)
    assert liga(1.0, 4.0, 0.1) and not liga(1.0, 0.5, 0.1), "(i)  y2 up -> binds"
    assert liga(0.5, 3.0, 0.1) and not liga(5.0, 3.0, 0.1), "(ii) y1 down -> binds"
    assert liga(1.0, 3.0, 0.1) and not liga(1.0, 3.0, 5.0), "(iii) b down -> binds"

    # (e) a present-value-neutral tax cut
    Delta = 0.2
    livres = (3.0, 1.0, 1.0)          # unconstrained household
    presos = (1.0, 4.0, 0.05)         # constrained household
    saida = {}
    for nome, (y1, y2, b) in (("unconstrained", livres), ("constrained", presos)):
        base = resolve(y1, y2, b)[0]
        estim = resolve(y1, y2, b, tau1=-Delta, tau2=Delta * (1 + r))[0]
        credito = resolve(y1, y2, b + Delta)[0]     # (f) a government loan
        saida[nome] = (base, estim, credito)
    assert np.isclose(saida["unconstrained"][1], saida["unconstrained"][0]), \
        "(e) Ricardian equivalence must hold when the constraint is slack"
    assert np.isclose(saida["constrained"][1] - saida["constrained"][0], Delta), \
        "(e) a constrained household must consume the entire tax cut"
    assert np.isclose(saida["constrained"][2], saida["constrained"][1]), \
        "(f) the loan and the tax cut must give the same c1"
    assert np.isclose(saida["unconstrained"][2], saida["unconstrained"][0]), \
        "(f) an unconstrained household ignores the loan too"

    if verbose:
        print()
        print("=" * 74)
        print("Problem 6.5  Credit constraints   (beta=%.2f, sigma=%.1f, r=%.2f, "
              "Delta=%.1f)" % (beta, sigma, r, Delta))
        print("=" * 74)
        print("  Omega = %.6f;  binds iff  y2/(1+r) > (Omega-1) y1 + Omega b" % Om)
        print("  household        c1 base   c1 stimulus   c1 with loan")
        for nome, (b0, b1, b2) in saida.items():
            print("  %-15s %8.5f    %8.5f      %8.5f" % (nome, b0, b1, b2))
        print("  Ricardian equivalence holds for the first, fails for the second;")
        print("  the loan does exactly what the tax cut does.")
    return saida


# =========================================================== Problem 6.7
def problema_6_7(verbose=True):
    alpha, delta = 0.35, 0.1

    def kss(s):
        return (s / delta) ** (1 / (1 - alpha))

    def yss(s):
        return kss(s) ** alpha

    def css(s):
        return (1 - s) * yss(s)

    def rss(s):
        return alpha * kss(s) ** (alpha - 1) - delta

    # (a)-(b) closed forms, checked against the definitions
    for s in (0.2, 0.4, 0.5, 0.6):
        assert np.isclose(s * yss(s), delta * kss(s)), "steady state sY = deltaK"
        assert np.isclose(rss(s), delta * (alpha - s) / s), "r = delta(alpha-s)/s"

    s0, s1 = 0.4, 0.5
    # (c) golden rule is at s = alpha
    grid = np.linspace(0.01, 0.99, 9801)
    assert abs(grid[np.argmax(css(grid))] - alpha) < 1e-3, "golden rule s = alpha"
    assert yss(s1) > yss(s0), "(c-i) GDP must rise"
    assert css(s1) < css(s0), "(c-ii) consumption must fall: s already above alpha"
    assert rss(s0) < 0, "at s=0.4 the interest rate is negative"

    # (d) the Friedmans' Euler equation, for any beta < 1
    r = rss(s0)
    for beta in (0.90, 0.96, 0.99, 0.999):
        for sigma in (0.5, 1.0, 2.0, 5.0):
            g = (beta * (1 + r)) ** (1 / sigma)
            assert g < 1, "consumption must fall for every beta<1 and sigma>0"

    if verbose:
        print()
        print("=" * 74)
        print("Problem 6.7  One rational household   (alpha=%.2f, delta=%.2f)"
              % (alpha, delta))
        print("=" * 74)
        print("      s      K*        Y*        c*         r")
        for s in (0.35, 0.4, 0.5):
            print("  %5.2f  %8.4f  %8.4f  %8.4f  %+8.4f"
                  % (s, kss(s), yss(s), css(s), rss(s)))
        print("  (c-i)  GDP rises: %.4f -> %.4f" % (yss(s0), yss(s1)))
        print("  (c-ii) consumption FALLS: %.4f -> %.4f, because s=0.4 > alpha=0.35"
              % (css(s0), css(s1)))
        print("  (d) r = %.4f < 0, so beta(1+r) < 1 for every beta < 1:" % r)
        print("      the Friedmans' consumption starts high and falls forever, at")
        print("      a factor (beta(1+r))^(1/sigma) per period, e.g. %.5f for"
              % ((0.96 * (1 + r)) ** (1 / 2)))
        print("      beta=0.96, sigma=2.")
    return kss, yss, css, rss


# =========================================================== Problem 6.8
def problema_6_8(r=0.04, verbose=True):
    """Infinite horizon with beta(1+r)=1: flat consumption and the annuity MPC."""
    beta = 1 / (1 + r)
    y0, ybar = 2.0, 1.0
    c0 = (r * y0 + ybar) / (1 + r)

    # independent check: simulate the flat path and verify the budget constraint
    T = 4000
    pv_c = sum(c0 / (1 + r) ** t for t in range(T))
    pv_y = y0 + sum(ybar / (1 + r) ** t for t in range(1, T))
    assert abs(pv_c - pv_y) < 1e-6, "budget constraint must hold"
    # assets stay non-negative and converge to the annuity level
    a, caminho = 0.0, []
    yt = [y0] + [ybar] * (T - 1)
    for t in range(T):
        a = (1 + r) * a + yt[t] - c0
        caminho.append(a)
    a_perm = (y0 - ybar) / (1 + r)
    assert abs(caminho[-1] - a_perm) < 1e-9, (
        "assets must settle at the annuitised windfall, (y0-ybar)/(1+r)")
    assert np.isclose(c0, ybar + r * a_perm), (
        "flat consumption = permanent income + interest on the windfall")

    mpc_temp = r / (1 + r)
    h = 1e-7
    mpc_num = ((r * (y0 + h) + ybar) / (1 + r) - (r * (y0 - h) + ybar) / (1 + r)) / (2 * h)
    assert np.isclose(mpc_temp, mpc_num), "MPC out of temporary income"
    mpc_perm = (r / (1 + r)) + 1 / (1 + r)
    assert np.isclose(mpc_perm, 1.0), "MPC out of permanent income must be one"

    if verbose:
        print()
        print("=" * 74)
        print("Problem 6.8  Marginal propensity to consume   (r=%.2f)" % r)
        print("=" * 74)
        print("  c0 = (r y0 + ybar)/(1+r) = %.6f  with y0=%.1f, ybar=%.1f"
              % (c0, y0, ybar))
        print("  the path is flat: assets settle at (y0-ybar)/(1+r) = %.6f,"
              % a_perm)
        print("  and c0 = ybar + r a = %.6f  -- the windfall is annuitised"
              % (ybar + r * a_perm))
        print("  MPC out of a temporary increase = r/(1+r) = %.6f  (%.2f%%)"
              % (mpc_temp, mpc_temp * 100))
        print("  MPC out of a permanent increase = %.4f" % mpc_perm)
        print("  so %.1f%% of a windfall is saved" % ((1 - mpc_temp) * 100))
    return c0, mpc_temp


if __name__ == "__main__":
    problema_6_1()
    problema_6_9()
    problema_6_3()
    problema_6_6()
    problema_6_2()
    problema_6_4()
    problema_6_5()
    problema_6_8()
    problema_6_7()
    print()
    print("all checks passed.")
