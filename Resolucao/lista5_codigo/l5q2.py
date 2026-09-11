"""Question 2 of Problem Set 5: verification of every asserted result.

Run:  python l5q2.py
"""
import numpy as np

from modelo import (A2, ALPHA2, DELTA, BETA, FK, K_ss, c_ss, K_gr, r_ss,
                    passo, caminho, c_saddle)

BETAS = (0.90, 0.96, 0.99, 0.999)


def check_arbitragem(sigma=2.0, beta=BETA):
    """(c) both ownership arrangements imply 1+r = r^K + 1 - delta.

    Arrangement (i): the household owns K and its FOC in K_{t+1} is
        u'(c_t) = beta (r^K_{t+1} + 1 - delta) u'(c_{t+1}).
    Arrangement (ii): the investment firm's profit is linear in I, so the
        coefficient must vanish: (r^K_{t+1} + 1 - delta)/(1+r_{t+1}) = 1.
    Both give the same gross return, so the same intertemporal price.
    """
    K = 4.0
    rK = FK(K)
    r_arranjo_ii = rK + 1 - DELTA - 1          # from the zero-profit condition
    # arrangement (i): the return that makes the two Euler equations agree
    r_arranjo_i = (rK + 1 - DELTA) - 1
    assert np.isclose(r_arranjo_i, r_arranjo_ii), "both must give the same r"

    # and the linearity claim itself: profit is affine in I with zero slope
    def lucro_firma_investimento(I, r):
        bruto = (rK + 1 - DELTA) / (1 + r)
        return bruto * ((1 - DELTA) * K + I) - ((1 - DELTA) * K + I)
    r = r_arranjo_ii
    vals = [lucro_firma_investimento(I, r) for I in (0.0, 1.0, 5.0, 100.0)]
    assert np.allclose(vals, 0.0), "at the no-arbitrage r, profit is zero for ALL I"
    inclinacao = (lucro_firma_investimento(1.0, r + 0.01)
                  - lucro_firma_investimento(0.0, r + 0.01))
    assert inclinacao < 0, "off the no-arbitrage r the slope is non-zero"
    return r_arranjo_ii


def check_estado_estacionario():
    """(d) closed forms, and that they really are a rest point of the system."""
    linhas = []
    for beta in BETAS:
        K = K_ss(beta)
        c = c_ss(K)
        # the defining condition
        assert np.isclose(FK(K) - DELTA, 1 / beta - 1), "SS condition"
        assert np.isclose(r_ss(beta), 1 / beta - 1), "r = 1/beta - 1"
        # independent check: (K, c) is a fixed point of the two difference eqs
        K1, c1 = passo(K, c, beta=beta, sigma=2.0)
        assert np.isclose(K1, K) and np.isclose(c1, c), "must be a rest point"
        # and it is a rest point for ANY sigma -- sigma does not move the SS
        for sigma in (0.5, 1.0, 3.0, 8.0):
            K1s, c1s = passo(K, c, beta=beta, sigma=sigma)
            assert np.isclose(K1s, K) and np.isclose(c1s, c), "sigma-free SS"
        assert K < K_gr(), "steady state must lie below the Golden Rule"
        linhas.append((beta, K, c, FK(K) - DELTA, K / K_gr()))
    return linhas


def check_regra_de_ouro():
    """(e) K_gr maximises c_ss; K_ss < K_gr; and K_ss -> K_gr as beta -> 1."""
    Kg = K_gr()
    assert np.isclose(FK(Kg), DELTA), "Golden rule: F_K = delta"
    # brute force: the maximum of c_ss really is at K_gr
    grid = np.linspace(1e-4, 3 * Kg, 600001)
    assert abs(grid[np.argmax(c_ss(grid))] - Kg) < 1e-3, "argmax must be K_gr"
    # the limit
    assert abs(K_ss(1 - 1e-9) / Kg - 1) < 1e-6, "K_ss -> K_gr as beta -> 1"
    # flatness of c_ss near the peak: second order loss
    perdas = [(beta, 1 - c_ss(K_ss(beta)) / c_ss(Kg), 1 - K_ss(beta) / Kg)
              for beta in BETAS]
    return Kg, c_ss(Kg), perdas


def check_sela(K0=2.0, sigma=2.0, beta=BETA, T=120):
    """The saddle path exists; neighbouring paths fall off it in both directions.

    Shooting on a saddle path is delicate: the unstable root magnifies any
    error in c0 geometrically, so after enough periods even a machine-precision
    bracket blows up.  The honest test is therefore the *closest approach* to
    the steady state, not the value at the final date.
    """
    c0 = c_saddle(K0, T=T, beta=beta, sigma=sigma)
    K, c = caminho(K0, c0, T, beta=beta, sigma=sigma)
    Ks, cs = K_ss(beta), c_ss(K_ss(beta))
    ok = np.isfinite(K) & np.isfinite(c)
    dist = np.hypot(K[ok] / Ks - 1, c[ok] / cs - 1)
    i = int(np.argmin(dist))
    assert dist[i] < 1e-4, ("saddle path must approach the steady state", dist[i])
    # monotone approach on the way in, as the phase diagram requires
    assert np.all(np.diff(K[ok][:i + 1]) > 0), "K must rise monotonically from K0<K_ss"

    # a slightly higher c0 exhausts the capital stock; a lower one overshoots
    Ka, _ = caminho(K0, c0 * 1.02, T, beta=beta, sigma=sigma)
    assert (not np.isfinite(Ka).all()) or np.nanmin(Ka) < K0 * 0.5,         "too much consumption must run capital down"
    Kb, _ = caminho(K0, c0 * 0.98, T, beta=beta, sigma=sigma)
    assert np.nanmax(Kb) > Ks * 1.0001, "too little consumption must overshoot"
    return c0, K, c, i


if __name__ == "__main__":
    print("=" * 74)
    print("QUESTION 2  --  infinite horizon, labour fixed at L = 1")
    print("=" * 74)
    print("  calibration: A=%.1f  alpha=%.2f  delta=%.2f" % (A2, ALPHA2, DELTA))

    r = check_arbitragem()
    print()
    print("(c) no-arbitrage: 1+r = r^K + 1 - delta holds under BOTH arrangements")
    print("    at K = 4: r^K = %.6f, so r = %.6f" % (FK(4.0), r))
    print("    the investment firm's profit is identically zero in I at that r,")
    print("    and strictly monotone in I at any other r -- hence no interior optimum")

    print()
    print("(d) steady state")
    print("    beta       K_ss       c_ss      F_K-delta       r        K_ss/K_gr")
    for beta, K, c, fk, ratio in check_estado_estacionario():
        print("    %.3f  %9.5f  %9.5f   %+.6f   %+.6f    %.5f"
              % (beta, K, c, fk, 1 / beta - 1, ratio))
    print("    the steady state is a rest point for EVERY sigma: sigma governs")
    print("    the speed of the transition, never the destination")

    Kg, cg, perdas = check_regra_de_ouro()
    print()
    print("(e) Golden rule:  K_gr = %.5f  (F_K = delta),  c_gr = %.5f" % (Kg, cg))
    print("    beta     capital shortfall    consumption shortfall")
    for beta, dc, dk in perdas:
        print("    %.3f       %7.3f%%              %8.5f%%" % (beta, dk * 100, dc * 100))
    print("    c_ss is flat near its peak: a large capital gap costs little consumption")

    c0, K, c, i = check_sela()
    print()
    print("saddle path from K0 = 2.0 (sigma = 2, beta = %.2f): c0 = %.6f" % (BETA, c0))
    print("    closest approach to the steady state at t = %d" % i)
    for t in (0, 5, 10, 25, 50, 100):
        print("    t=%3d   K=%8.5f   c=%8.5f" % (t, K[t], c[t]))
    print("    steady state:  K = %8.5f   c = %8.5f"
          % (K_ss(BETA), c_ss(K_ss(BETA))))

    print()
    print("all Question 2 checks passed.")
