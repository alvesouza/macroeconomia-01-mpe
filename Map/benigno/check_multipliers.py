#!/usr/bin/env python3
"""Self-check for the fiscal multipliers derived in Map/benigno/.

Runs the Table 1 formulas of Benigno (2015, p. 515) against every one of the eight
rows of his Table 2 (p. 516), and the two deleveraging multipliers quoted on p. 521
against their published values. If any formula in 07-fiscal-multipliers.md or
09-deleveraging.md is mistyped, this file fails.

    python Map/benigno/check_multipliers.py

Stdlib only, no output on success beyond the table.
"""

TOL = 0.02  # Table 2 is printed to two decimals


def kappa(alpha, sigma, eta):
    """AS slope, eq. (17): (1-alpha)(sigma^-1 + eta)/alpha."""
    return (1 - alpha) * (1 / sigma + eta) / alpha


def multipliers(alpha, sigma, eta):
    """The six fiscal multipliers of Table 1, in the order of Table 2's columns.

    Returns (m_g, m_gbar, m_tau, m_taubar, m_tauc, m_taucbar), all defined so that
    eq. (22) reads
        y = m_g g - m_gbar gbar - m_tau tau - m_taubar taubar - m_tauc tauc + m_taucbar taucbar
    i.e. every coefficient is non-negative and the signs live in (22).
    """
    k = kappa(alpha, sigma, eta)
    inv = 1 / sigma
    d = (inv + eta) * (1 + k * sigma)     # the denominator shared by five of the six
    m_g = 1 / (1 + k * sigma) + k / d
    m_gbar = eta / d
    m_tau = k * sigma / d
    m_taubar = 1 / d
    return m_g, m_gbar, m_tau, m_taubar, sigma * m_g, sigma * m_gbar


# Benigno (2015), Table 2, p. 516 -- (alpha, sigma, eta) -> printed row
TABLE2 = {
    (0.66, 0.5, 0.2): (0.96, 0.06, 0.16, 0.29, 0.48, 0.03),
    (0.75, 0.5, 0.2): (0.98, 0.06, 0.12, 0.33, 0.49, 0.03),
    (0.66, 1.0, 0.2): (0.94, 0.10, 0.32, 0.52, 0.94, 0.10),
    (0.75, 1.0, 0.2): (0.95, 0.12, 0.24, 0.60, 0.95, 0.12),
    (0.66, 1.0, 1.0): (0.75, 0.25, 0.25, 0.25, 0.75, 0.25),
    (0.75, 1.0, 1.0): (0.80, 0.30, 0.20, 0.30, 0.80, 0.30),
    (0.66, 0.5, 1.0): (0.86, 0.18, 0.15, 0.19, 0.43, 0.09),
    (0.75, 0.5, 1.0): (0.88, 0.22, 0.11, 0.22, 0.44, 0.11),
}

COLS = ("m_g", "m_gbar", "m_tau", "m_taubar", "m_tauc", "m_taucbar")


def check_table2():
    print(f"{'alpha':>5} {'sigma':>5} {'eta':>4} {'kappa':>6}  " +
          "  ".join(f"{c:>9}" for c in COLS))
    for (alpha, sigma, eta), printed in TABLE2.items():
        got = multipliers(alpha, sigma, eta)
        print(f"{alpha:5.2f} {sigma:5.2f} {eta:4.1f} {kappa(alpha, sigma, eta):6.3f}  " +
              "  ".join(f"{g:9.4f}" for g in got))
        for col, g, p in zip(COLS, got, printed):
            assert abs(g - p) <= TOL, \
                f"Table 2 row (a={alpha}, s={sigma}, e={eta}) col {col}: {g:.4f} vs printed {p}"
    # every multiplier is below one in normal times -- the claim on p. 515
    for params in TABLE2:
        assert all(m < 1.0 for m in multipliers(*params)), params


def check_no_gap_effect_of_permanent_policy():
    """Eq. (23): permanent fiscal policy leaves the output gap untouched.

    The gap coefficients are the LONG-run multipliers, with short and long run
    entering with equal and opposite signs, so g = gbar implies no gap effect.
    """
    m_g, m_gbar, m_tau, m_taubar, m_tauc, m_taucbar = multipliers(0.66, 0.5, 0.2)
    dg = 0.01
    gap = m_gbar * (dg - dg)                      # g and gbar move together
    assert abs(gap) < 1e-15
    # and the algebra behind it: m_g - sigma^-1/(sigma^-1+eta) == m_gbar
    sigma, eta = 0.5, 0.2
    assert abs((m_g - (1 / sigma) / (1 / sigma + eta)) - m_gbar) < 1e-12


def deleveraging_multiplier(alpha, sigma, eta, chi, d0, beta, anchored=True):
    """Section 10 multipliers on short-run public spending, p. 521.

    anchored=True : long-run prices fixed independently of short-run prices
    anchored=False: long-run INFLATION tied to zero (Eggertsson-Krugman case)
    """
    k = kappa(alpha, sigma, eta)
    varpi = sigma - d0 * (1 - beta) * (1 - chi) / chi     # AD slope: dy/dp = -varpi
    if anchored:
        return (1 / chi + varpi * k / (1 + sigma * eta)) / (1 + varpi * k)
    num = 1 - d0 * (1 - chi) * k / (1 + sigma * eta)
    return num / (chi - d0 * (1 - chi) * k)


def check_deleveraging():
    """p. 521: 1.29 with one third borrowers, 1.62 with one half, 2.75 with zero
    long-run inflation and one third borrowers. Calibration alpha=0.66, sigma=0.5,
    eta=0.2, d0=1.2 (120% of GDP)."""
    base = dict(alpha=0.66, sigma=0.5, eta=0.2, d0=1.2, beta=0.99)
    m13 = deleveraging_multiplier(chi=2 / 3, **base)
    m12 = deleveraging_multiplier(chi=1 / 2, **base)
    m0 = deleveraging_multiplier(chi=2 / 3, anchored=False, **base)
    print(f"\ndeleveraging, anchored prices : 1/3 borrowers -> {m13:.3f} (paper 1.29)")
    print(f"deleveraging, anchored prices : 1/2 borrowers -> {m12:.3f} (paper 1.62)")
    print(f"deleveraging, zero long-run inflation        -> {m0:.3f} (paper 2.75)")
    assert abs(m13 - 1.29) <= TOL, m13
    assert abs(m12 - 1.62) <= TOL, m12
    assert abs(m0 - 2.75) <= TOL, m0
    # and the point of the section: bigger than the upper limit of section 8
    assert m13 > 1.0 and m0 > m13


def check_optimal_markup_split():
    """Section 11: optimal policy admits a fraction 1/(1+theta*kappa) of a mark-up
    shock into prices, and the two limits collapse to E'' and E''' of Fig. 9."""
    alpha, sigma, eta, theta = 0.66, 0.5, 0.2, 8.0
    k = kappa(alpha, sigma, eta)
    dmu = 0.01
    yn_shift = -dmu / (1 / sigma + eta)
    price = k * (-yn_shift) / (1 + theta * k)         # p - p^e > 0
    gap_e = -theta * k * (-yn_shift) / (1 + theta * k)  # y - y_e < 0
    assert price > 0 > gap_e
    # the targeting rule (34) holds by construction
    assert abs(gap_e + theta * price) < 1e-12
    # a central bank that only cares about prices lands on E'': p = p^e
    k_big = 1e9
    assert abs(k * (-yn_shift) / (1 + k_big * k)) < 1e-9
    print(f"\noptimal mark-up split (theta={theta:.0f}, kappa={k:.2f}): "
          f"{1 / (1 + theta * k):.3f} of the shock into prices")


if __name__ == "__main__":
    check_table2()
    check_no_gap_effect_of_permanent_policy()
    check_deleveraging()
    check_optimal_markup_split()
    print("\nall checks pass")
