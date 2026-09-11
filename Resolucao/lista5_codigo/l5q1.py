"""Question 1 of Problem Set 5: verification of every asserted result.

Each analytical formula in the resolution is checked against an independent
numerical route, and the script aborts on any mismatch.

Run:  python l5q1.py
"""
import numpy as np

from modelo import (ALPHA, PSI, KBAR, BETA, c_de_L, w_de_L, rK_de_L,
                    residuo_bruto, residuo_compacto, L_equilibrio,
                    elasticidade_L, elasticidades, juro_equilibrio)

SIGMAS = (0.25, 0.5, 1.0, 2.0, 4.0)


def check_zero_lucro(A=1.0, L=0.3, alpha=ALPHA, Kbar=KBAR):
    """(a) CRS + competitive pricing => Pi = 0, by Euler's theorem."""
    Y = A * Kbar ** alpha * L ** (1 - alpha)
    custo = w_de_L(L, A) * L + rK_de_L(L, A) * Kbar
    assert np.isclose(Y, custo), "revenue must equal total factor payments"
    assert np.isclose(rK_de_L(L, A) * Kbar / Y, alpha), "capital share = alpha"
    assert np.isclose(w_de_L(L, A) * L / Y, 1 - alpha), "labour share = 1-alpha"
    return Y, custo


def check_formas_equivalentes():
    """(d) the raw MRS=MRT condition and the tidied form share the same root."""
    for sigma in SIGMAS:
        for A in (0.7, 1.0, 1.5, 2.5):
            La = L_equilibrio(A, sigma, compacto=False)
            Lb = L_equilibrio(A, sigma, compacto=True)
            assert abs(La - Lb) < 1e-9, (sigma, A, La, Lb)
            # and both residuals really vanish there
            assert abs(residuo_bruto(Lb, A, sigma)) < 1e-8
            assert abs(residuo_compacto(La, A, sigma)) < 1e-12
    return True


def check_unicidade():
    """LHS of the compact form is strictly increasing on (0,1): unique root."""
    for sigma in SIGMAS:
        L = np.linspace(1e-6, 1 - 1e-6, 200001)
        lhs = L ** (ALPHA + (1 - ALPHA) * sigma) / (1 - L)
        assert np.all(np.diff(lhs) > 0), "LHS must be strictly increasing"
    return True


def check_elasticidade(h=1e-6):
    """(e) the closed-form elasticity against a symmetric finite difference,
    and the induced elasticities of w, r^K and c against their own."""
    linhas = []
    for sigma in SIGMAS:
        A = 1.0
        L, eL, ew, erK, ec = elasticidades(A, sigma)

        num = (np.log(L_equilibrio(A * np.exp(h), sigma))
               - np.log(L_equilibrio(A * np.exp(-h), sigma))) / (2 * h)
        assert abs(num - eL) < 1e-6, ("labour elasticity", sigma, num, eL)

        for f, claimed, nome in ((w_de_L, ew, "w"),
                                 (rK_de_L, erK, "r^K"),
                                 (c_de_L, ec, "c")):
            d = (np.log(f(L_equilibrio(A * np.exp(h), sigma), A * np.exp(h)))
                 - np.log(f(L_equilibrio(A * np.exp(-h), sigma), A * np.exp(-h)))
                 ) / (2 * h)
            assert abs(d - claimed) < 1e-5, (nome, sigma, d, claimed)

        # sign of the labour response is the sign of 1 - sigma
        assert np.sign(eL) == np.sign(1 - sigma) or abs(1 - sigma) < 1e-9
        # w, r^K and c rise for EVERY sigma
        assert ew > 0 and erK > 0 and ec > 0, ("all must be positive", sigma)
        # r^K and c share the same elasticity, exactly
        assert np.isclose(erK, ec), "r^K = alpha c / Kbar, so they move together"
        linhas.append((sigma, L, eL, ew, erK))
    return linhas


def check_rK_proporcional_a_c():
    """r^K = alpha * c / Kbar exactly, which is why their elasticities match."""
    for sigma in (0.5, 1.0, 2.0):
        L = L_equilibrio(1.0, sigma)
        assert np.isclose(rK_de_L(L, 1.0), ALPHA * c_de_L(L, 1.0) / KBAR)
    return True


def check_juro():
    """(d) the equilibrium interest rate, and the no-growth special case."""
    linhas = []
    for sigma in (0.5, 2.0):
        for A1, A2_ in ((1.0, 1.0), (1.0, 1.2), (1.0, 0.9)):
            L1 = L_equilibrio(A1, sigma)
            L2 = L_equilibrio(A2_, sigma)
            c1, c2 = c_de_L(L1, A1), c_de_L(L2, A2_)
            # independent route: straight from the Euler equation in levels
            r_euler = (1 / BETA) * (c2 / c1) ** sigma - 1
            r_form = juro_equilibrio(A1, A2_, sigma)
            assert np.isclose(r_euler, r_form), (sigma, A1, A2_)
            if A1 == A2_:
                assert np.isclose(r_form, 1 / BETA - 1), "no growth => r = rho"
                assert np.isclose(L1, L2), "same A => same L"
            linhas.append((sigma, A2_ / A1, L1, L2, r_form))
    return linhas


if __name__ == "__main__":
    print("=" * 74)
    print("QUESTION 1  --  two periods, capital fixed at Kbar, no investment")
    print("=" * 74)
    print("  calibration: alpha=%.2f  psi=%.1f  Kbar=%.1f  beta=%.2f"
          % (ALPHA, PSI, KBAR, BETA))

    Y, custo = check_zero_lucro()
    print()
    print("(a) zero profit:  Y = %.6f, w L + r^K Kbar = %.6f  -> Pi = %.2e"
          % (Y, custo, Y - custo))
    print("    factor shares: capital = alpha = %.2f, labour = %.2f"
          % (ALPHA, 1 - ALPHA))

    check_formas_equivalentes()
    check_unicidade()
    print()
    print("(d) the raw and tidied labour equations share the same unique root,")
    print("    for sigma in %s and A in {0.7, 1.0, 1.5, 2.5}." % (SIGMAS,))

    print()
    print("(e) elasticities with respect to A   (A = 1)")
    print("    sigma      L*        dlnL/dlnA    dlnw/dlnA   dlnr^K/dlnA = dlnc/dlnA")
    for sigma, L, eL, ew, erK in check_elasticidade():
        print("    %5.2f   %8.5f   %+10.6f   %+10.6f   %+10.6f"
              % (sigma, L, eL, ew, erK))
    check_rK_proporcional_a_c()
    print("    sign(dlnL/dlnA) = sign(1-sigma);  w, r^K and c rise for every sigma")
    print("    r^K = alpha c / Kbar exactly, so the last two columns coincide")

    print()
    print("(d) equilibrium interest rate")
    print("    sigma   A2/A1      L1         L2          r")
    for sigma, g, L1, L2, r in check_juro():
        print("    %5.2f   %5.2f   %8.5f   %8.5f   %+9.6f" % (sigma, g, L1, L2, r))
    print("    with A2 = A1:  r = 1/beta - 1 = %.6f" % (1 / BETA - 1))

    print()
    print("all Question 1 checks passed.")
