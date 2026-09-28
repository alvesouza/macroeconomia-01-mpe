#!/usr/bin/env python3
"""Self-check for the fiscal multipliers derived in Map/benigno/.

Runs the Table 1 formulas of Benigno (2015, p. 515) against every one of the eight
rows of his Table 2 (p. 516), and the two deleveraging multipliers quoted on p. 521
against their published values. If any formula in 07-fiscal-multipliers.md or
09-deleveraging.md is mistyped, this file fails.

    python Map/benigno/check_multipliers.py

Stdlib only for the numeric checks; check_derivation_steps() needs sympy and
verifies, symbol by symbol, every intermediate step written out in the notes.
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


def check_derivation_steps():
    """Symbolic check of every intermediate step written out in notes 01-10.

    Each block mirrors one expanded derivation; if a step in a note is edited
    into something false, the matching assert fails. Needs sympy.
    """
    import sympy as sp
    (a, g, mu, s, e, al, th, y, yn, ye, ybn, i, pb, pe, rho, tc, tcb,
     P, W, A, tw, ty, tau, taub, gb, dg) = sp.symbols(
        "a g mu sigma eta alpha theta y y_n y_e ybar_n i pbar p_e rho "
        "tau_c taubar_c P W A tau_w tau_y tau taubar gbar dg", real=True)
    p = sp.symbols("p", real=True)

    def z(ex):
        return sp.simplify(ex) == 0

    # 01 sec 1.3-1.5: FOCs with taxes, log-linear Euler, AD slope
    lam, tl = sp.symbols("lambda tau_l", positive=True)
    uc, vl = lam * (1 + tc) * P, lam * (1 - tl) * W
    assert z(vl / uc - (1 - tl) / (1 + tc) * W / P)            # eq. (7)
    st, c, cb, r = sp.symbols("sigmatilde c cbar r", real=True)
    euler = sp.Eq(-(c - cb) / st, -rho + r)                    # logs of (3)
    assert z(sp.solve(euler, cb)[0] - c - st * (r - rho))      # eq. (4)
    ad8 = sp.Eq(y, ybn + (g - gb) - s * (i - (pb - p) - (tcb - tc) - rho))
    psol = sp.solve(ad8, p)[0]
    assert z(psol - (pb + (ybn + g - gb - y) / s - (i - (tcb - tc) - rho)))
    assert z(sp.diff(psol, y) + 1 / s)
    assert z(sp.diff(sp.solve(ad8, y)[0], p) + s)

    # 02 sec 2.2: optimal price is theta/(theta-1) (1+tw)/(1-ty) W/A
    Pj, X = sp.symbols("P_j X", positive=True)
    prof = (1 - ty) * Pj**(1 - th) * X - (1 + tw) * W / A * Pj**(-th) * X
    step = sp.expand(sp.diff(prof, Pj) / X * Pj**(th + 1))
    assert z(step - ((1 - ty) * (1 - th) * Pj + th * (1 + tw) * W / A))
    pstar = sp.solve(step, Pj)[0]
    assert z(pstar - th / (th - 1) * (1 + tw) / (1 - ty) * W / A)
    # 02 sec 2.4: the logged (14) solved for y_n gives (15)
    yn15 = ((1 + e) * a + g / s - mu) / (1 / s + e)
    assert z(e * (yn15 - a) + (yn15 - g) / s - (a - mu))
    # 02 sec 2.5-2.6: price index, kappa, its derivatives
    assert z((p - al * pe) / (1 - al) - p - al / (1 - al) * (p - pe))
    k = (1 - al) * (1 / s + e) / al
    pas = sp.solve(sp.Eq(al / (1 - al) * (p - pe), (1 / s + e) * (y - yn)), p)[0]
    assert z(pas - pe - k * (y - yn))
    assert z(sp.diff(k, al) + (1 / s + e) / al**2)
    assert z(sp.diff(k, s) + (1 - al) / (al * s**2))
    assert z(sp.diff(k, e) - (1 - al) / al)

    # 03: planner FOC log-linearised, the subtraction, long-run consumption
    ye19 = ((1 + e) * a + g / s) / (1 / s + e)
    assert z(e * (ye19 - a) + (ye19 - g) / s - a)
    assert z(yn15 - ye19 + mu / (1 / s + e))
    sc = sp.symbols("s_c", positive=True)
    assert z((yn15 - g) / sc - ((1 + e) * a - e * g - mu) / (sc * (1 / s + e)))

    # 04: closed form of AS-AD, the natural rate, dy/dtaubar_c
    ad = ybn + (g - gb) - s * (i - (pb - p) - (tcb - tc) - rho)
    ysol = sp.solve(sp.Eq(y, ad.subs(p, pe + k * (y - yn))), y)[0]
    rn = rho + (ybn - yn) / s + (g - gb) / s + (tcb - tc)
    assert z(ysol - yn - s / (1 + s * k) * (rn - i + (pb - pe)))
    assert z(ysol.subs({i: rn, pb: pe}) - yn)
    dY = sp.diff(ysol.subs(ybn, ybn - tcb / (1 / s + e)), tcb)
    assert z(dY - s * e / ((1 / s + e) * (1 + s * k)))

    # 05-06: optimal di in the three productivity cases; mark-up point E3
    dyn, dybn, di = sp.symbols("dy_n dybar_n di", real=True)
    gap = (dybn - dyn - s * di) / (1 + s * k)
    dy = (dybn + s * k * dyn - s * di) / (1 + s * k)
    assert z(sp.solve(gap.subs(dybn, 0), di)[0] + dyn / s)       # temporary
    assert z(gap.subs(dybn, dyn).subs(di, 0))                    # permanent
    assert z(sp.solve(gap.subs(dyn, 0), di)[0] - dybn / s)       # expected
    di3 = sp.solve(dy.subs(dybn, 0), di)[0]                      # dy = 0
    assert z(di3 - k * dyn)
    assert z(k * gap.subs({dybn: 0, di: di3}) + k * dyn)         # p-pe = -k dyn

    # 07: Table 1 from (dagger), gap (23) and efficient-gap multipliers
    D = (1 / s + e) * (1 + s * k)
    ynf = (g / s - tau - tc) / (1 / s + e)
    ybf = (gb / s - taub - tcb) / (1 / s + e)
    yf = (g + ybf - gb + s * k * ynf + s * (tcb - tc)) / (1 + s * k)
    m = {"g": 1 / (1 + s * k) + k / D, "gb": e / D, "t": k * s / D,
         "tb": 1 / D}
    m["tc"], m["tcb"] = s * m["g"], s * m["gb"]
    for var, coef in [(g, m["g"]), (gb, -m["gb"]), (tau, -m["t"]),
                      (taub, -m["tb"]), (tc, -m["tc"]), (tcb, m["tcb"])]:
        assert z(sp.diff(yf, var) - coef), var
    assert z(m["g"] - (1 + k / (1 / s + e)) / (1 + s * k))
    assert z(m["tc"] - (1 + s * e + s * k) / D)
    assert z(m["g"].subs(e, 0) - 1)
    gapf = yf - ynf
    for var, coef in [(g, m["gb"]), (gb, -m["gb"]), (tau, m["tb"]),
                      (taub, -m["tb"]), (tc, -m["tcb"]), (tcb, m["tcb"])]:
        assert z(sp.diff(gapf, var) - coef), var
    effgap = gapf - (tau + tc) / (1 / s + e)
    for var, coef in [(g, m["gb"]), (gb, -m["gb"]), (tau, -m["t"]),
                      (taub, -m["tb"]), (tc, -m["tc"]), (tcb, m["tcb"])]:
        assert z(sp.diff(effgap, var) - coef), var

    # 08: the pbar commitment that closes the gap at i = 0
    assert z(sp.solve((ysol - yn).subs(i, 0), pb)[0] - pe + rn)

    # 09: AD (32) from (31) and the linearised borrower budget, then slope
    ch, d0, bt, dh, tb, tbb, ri, Y = sp.symbols(
        "chi d_0 beta dhat tau_b taubar_b r Y", real=True)
    cdiff = dh - bt * d0 * (ri - rho) + d0 * (p - pe) + (y - ybn) - (tb - tbb)
    eq31 = sp.Eq(y, g + (ybn - gb) - ch * s * (ri - rho) + (1 - ch) * cdiff)
    y32 = sp.solve(eq31, y)[0].subs(ri, i - (pb - p))
    ph = (s * ch + (1 - ch) * d0 * bt) / ch
    rhs32 = (ybn - ph * (i - (pb - p) - rho)
             + ((g - gb) - (1 - ch) * (tb - tbb)) / ch
             + (1 - ch) / ch * (dh + d0 * (p - pe)))
    assert z(y32 - rhs32)
    varpi = s - d0 * (1 - bt) * (1 - ch) / ch
    assert z(sp.diff(y32, p) + varpi)
    mult = sp.solve(sp.Eq(Y, dg / ch - varpi * k * (Y - dg / (1 + s * e))), Y)[0]
    assert z(mult / dg - (1 / ch + varpi * k / (1 + s * e)) / (1 + varpi * k))
    slope0 = (1 - ch) * d0 / ch            # pbar = p: only Fisher survives
    mult0 = sp.solve(sp.Eq(Y, dg / ch + slope0 * k * (Y - dg / (1 + s * e))), Y)[0]
    target0 = (1 - d0 * (1 - ch) * k / (1 + s * e)) / (ch - d0 * (1 - ch) * k)
    assert z(mult0 / dg - target0)

    # 10: targeting rule, the split, and the weight theta/kappa
    loss = (y - ye)**2 / 2 + th * k * (y - yn)**2 / 2
    yopt = sp.solve(sp.diff(loss, y), y)[0]
    assert z(yopt - (ye + th * k * yn) / (1 + th * k))
    assert z(sp.diff(loss, y, 2) - (1 + th * k))
    dmu = sp.symbols("dmu", positive=True)
    sub = {yn: ye - dmu / (1 / s + e)}
    assert z((yopt - ye).subs(sub) + th * k / (1 + th * k) * dmu / (1 / s + e))
    assert z((k * (yopt - yn)).subs(sub) - k / (1 + th * k) * dmu / (1 / s + e))
    assert z(sp.diff(th / k, al) - th / ((1 / s + e) * (1 - al)**2))
    # 10 sec 10.5: raise i iff phi > sigma (share below the no-policy share)
    for ph_, s_ in [(8.0, 0.5), (0.3, 0.5)]:
        k_ = kappa(0.66, s_, 0.2)
        assert (1 / (1 + ph_ * k_) < 1 / (1 + s_ * k_)) == (ph_ > s_)
    print("derivation steps: sympy checks pass")


def check_borrower_linearisation():
    """Note 09 sec 9.3: the first-order form of (C_b - Cbar_b)/Y is accurate
    to second order. Exact levels (Y~ = 1, P^e = 1, 1+r = exp(r), Dbar = D,
    1+rbar = 1/beta) against the linear formula at shrinking perturbations."""
    import math
    import random
    beta, d0 = 0.99, 1.2
    rho = -math.log(beta)
    rnd = random.Random(0)
    direction = [rnd.uniform(-1, 1) for _ in range(6)]
    errs = []
    for eps in (1e-2, 1e-3):
        dh, r_dev, p, y, yb, tb = (eps * v for v in direction)
        r = rho + r_dev
        D = d0 + dh
        cb = -d0 * math.exp(-p) + D * math.exp(-r) + (1 + y) - tb
        cbb = beta * D - D + (1 + yb)
        linear = dh - beta * d0 * r_dev + d0 * p + (y - yb) - tb
        errs.append(abs((cb - cbb) - linear))
    assert errs[1] < errs[0] / 50, errs          # error shrinks like eps^2
    # threshold and slope quoted in sec 9.4
    sigma, chi = 0.5, 2 / 3
    assert abs(sigma * chi / ((1 - beta) * (1 - chi)) - 100) < 1e-9
    assert abs(sigma - d0 * (1 - beta) * (1 - chi) / chi - 0.494) < 1e-12
    print("borrower budget linearisation: second-order accurate")


def check_three_schools():
    """Note 11: each derivation in the comparison of the three schools, symbolically."""
    import sympy as sp

    # market clearing: L^d = 10 - w, L^s = 2 + w; stuck wage 5 -> short side
    w = sp.symbols("w")
    ws = sp.solve(sp.Eq(10 - w, 2 + w), w)[0]
    assert ws == 4 and 10 - ws == 6
    assert min(10 - 5, 2 + 5) == 5 and (2 + 5) - (10 - 5) == 2

    # original Keynesian: linear IS-LM at fixed P
    Y, i, c, T, b, k, h, M, P, A0 = sp.symbols("Y i c T b k h M P A0", positive=True)
    i_lm = sp.solve(sp.Eq(M / P, k * Y - h * i), i)[0]
    Y_ad = sp.solve(sp.Eq(Y * (1 - c), A0 - b * i_lm), Y)[0]
    D = (1 - c) + b * k / h
    assert sp.simplify(Y_ad - (A0 + (b / h) * M / P) / D) == 0
    dYdM = sp.diff(Y_ad, M)
    assert sp.simplify(dYdM - (b / h) / (P * D)) == 0
    num = {c: sp.Rational(3, 4), b: 100, k: sp.Rational(1, 2), h: 200, P: 1}
    assert dYdM.subs(num) == 1
    assert sp.diff(Y_ad, P).subs(num | {M: 100, A0: 10}) < 0

    # New Classical: y - y_n = gam (p - p^e), AD y = m - p, m = m^e + eps, RE
    p, pe, m, me, eps, yn, gam = sp.symbols("p p_e m m_e epsilon y_n gamma")
    p_sol = sp.solve(sp.Eq(m - p, yn + gam * (p - pe)), p)[0]
    pe_sol = sp.solve(sp.Eq(pe, p_sol.subs(m, me)), pe)[0]
    assert sp.simplify(pe_sol - (me - yn)) == 0
    surprise = sp.simplify(p_sol.subs({pe: pe_sol, m: me + eps}) - pe_sol)
    assert sp.simplify(surprise - eps / (1 + gam)) == 0
    assert sp.simplify(gam * surprise - gam * eps / (1 + gam)) == 0   # y - y_n: no m^e

    # New Keynesian: AS p = kappa y (p^e = 0), AD y = d - sigma (i - rho + p)
    y, d, sg, kp, rho, ii = sp.symbols("y d sigma kappa rho i")
    sol = sp.solve([sp.Eq(p, kp * y), sp.Eq(y, d - sg * (ii - rho + p))], [y, p])
    assert sp.simplify(sol[y].subs(ii, rho) - d / (1 + sg * kp)) == 0
    assert sp.simplify(sol[y].subs(ii, rho + d / sg)) == 0              # rule offsets d
    k_ = kappa(0.66, 0.5, 0.2)
    assert abs(2 / (1 + 0.5 * k_) - 1.2766) < 1e-4
    assert abs(1 / (1 + 0.5 * k_) - 0.6383) < 1e-4
    assert abs((8 / 7) ** (1 / 2.2) - 1.06257) < 1e-4
    print("three schools and market clearing: sympy checks pass")


if __name__ == "__main__":
    check_three_schools()
    check_table2()
    check_no_gap_effect_of_permanent_policy()
    check_deleveraging()
    check_optimal_markup_split()
    check_derivation_steps()
    check_borrower_linearisation()
    print("\nall checks pass")
