#!/usr/bin/env python3
"""Numerical checks for Simulados/simulado-02.tex (mock final exam 2).

Recomputes every number printed in the answer key, including the value behind each
multiple-choice option, so the key is right and every distractor is wrong.

Run: python Simulados/simulado_codigo/check_simulado_02.py   (stdlib only)
"""
from __future__ import annotations

import math

failures: list[str] = []


def check(name, got, want, tol=5e-4):
    ok = abs(float(got) - float(want)) <= tol
    print(f"  {'ok  ' if ok else 'FAIL'}  {name:<62} {float(got):+.6f}  (want {float(want):+.6f})")
    if not ok:
        failures.append(name)


def check_true(name, cond):
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}")
    if not cond:
        failures.append(name)


def only_key(name, options, key, truth):
    """Exactly one option equals the truth, and it is the key."""
    hits = [k for k, v in options.items() if truth(v)]
    check_true(f"{name}: only option {key} is correct (hits={hits})", hits == [key])


# ---------------------------------------------------------------- Block I
print("\nQ1(a) value added along the soy chain")
fert, soy, oil = 30.0, 100.0, 150.0          # gross output of each firm
soy_to_crusher, soy_export = 70.0, 30.0
va = [fert, soy - fert, oil - soy_to_crusher]
gdp = sum(va)
check("GDP by value added", gdp, 180)
check("GDP by final expenditure C + X", oil + soy_export, gdp)
check("gross production (distractor)", fert + soy + oil, 280)
check("gross minus soy input only (distractor)", fert + soy + oil - soy_to_crusher, 210)
check("sales of the last two stages (distractor)", soy + oil, 250)
only_key("Q1(a)", {"A": 150, "B": 280, "C": 180, "D": 210, "E": 250}, "C", lambda v: v == gdp)

print("\nQ1(b) GNI")
GDP, wages_in, profits_out, interest_out, transfers_in = 10_000, 50, 300, 150, 40
gni = GDP + wages_in - profits_out - interest_out
check("GNI = GDP + F_out - F_in", gni, 9_600)
opts = {"A": 9_640, "B": 10_400, "C": 9_750, "D": 9_600, "E": 10_000}
check("with transfers (distractor A)", gni + transfers_in, opts["A"])
check("signs flipped (distractor B)", GDP - wages_in + profits_out + interest_out, opts["B"])
check("interest left out (distractor C)", GDP + wages_in - profits_out, opts["C"])
only_key("Q1(b)", opts, "D", lambda v: v == gni)

print("\nQ1(c) stock vs flow")
I_Y, K_Y, delta = 0.17, 3.0, 0.04
check("net addition to K as share of GDP", I_Y - delta * K_Y, 0.05)
check_true("statement F: K rises by 5% of GDP, not 17%", abs((I_Y - delta * K_Y) - I_Y) > 0.1)

print("\nQ1(d) nominal vs real")
defl = 1.038 / 0.965 - 1
check("deflator growth", defl, 0.07565, tol=5e-5)
check_true("statement F: deflator grew MORE than nominal GDP", defl > 0.038)

print("\nQ2 Brazil vs Portugal")
qT_br, qN_br, pT_br, pN_br = 5, 10, 10.0, 4.0     # R$
qT_pt, qN_pt, pT_pt, pN_pt = 10, 15, 2.0, 2.0     # euros
e = pT_br / pT_pt                                 # R$ per euro, law of one price
check("market rate from the law of one price (R$/EUR)", e, 5)
nom_br = qT_br * pT_br + qN_br * pN_br
y_pt = qT_pt * pT_pt + qN_pt * pN_pt
y_br_mkt = nom_br / e
y_br_ppp = qT_br * pT_pt + qN_br * pN_pt
check("Brazil nominal GDP per capita (R$)", nom_br, 90)
check("Portugal GDP per capita (EUR)", y_pt, 50)
check("Brazil at the market rate (EUR)", y_br_mkt, 18)
check("Brazil at Portuguese prices (EUR)", y_br_ppp, 30)
check("alt. PPP at Brazilian prices (rubric)", nom_br / (qT_pt * pT_br + qN_pt * pN_br), 0.5625)
check("ratio at market rate", y_br_mkt / y_pt, 0.36)
check("ratio at PPP", y_br_ppp / y_pt, 0.60)
e_ppp = nom_br / y_br_ppp
check("PPP rate (R$/EUR)", e_ppp, 3)
check("Brazil price level relative to Portugal", e_ppp / e, 0.6)
check("traded output: market rate", qT_br * pT_br / e, 10)
check("traded output: PPP", qT_br * pT_pt, 10)
check("non-traded output: market rate", qN_br * pN_br / e, 8)
check("non-traded output: PPP", qN_br * pN_pt, 20)
AT_br, AN_br, AT_pt, AN_pt = 2.0, 5.0, 5.0, 5.0
check("B-S: Brazil pN/pT = AT/AN", AT_br / AN_br, pN_br / pT_br)
check("B-S: Portugal pN/pT = AT/AN", AT_pt / AN_pt, pN_pt / pT_pt)

print("\nQ2(c) consumption-equivalent welfare")
ubar, s_br, s_pt, le_br, le_pt, cbar_br = 5.0, 0.9, 0.5, 76, 81, 0.6
v_br = ubar + math.log(cbar_br) - s_br**2 / 2
v_pt = ubar + 0.0 - s_pt**2 / 2
lnlam = (le_br / le_pt) * v_br - v_pt
cons, ineq = math.log(cbar_br), -0.5 * (s_br**2 - s_pt**2)
life = (le_br / le_pt - 1) * v_br
check("E ln c Brazil", math.log(cbar_br) - s_br**2 / 2, -0.9158)
check("flow value of a Brazilian year v_BR", v_br, 4.0842)
check("consumption term", cons, -0.5108)
check("inequality term", ineq, -0.28)
check("life-expectancy term", life, -0.2521)
check("sum of terms == exact ln lambda", cons + ineq + life, lnlam, tol=1e-12)
check("ln lambda", lnlam, -1.0429)
check("lambda", math.exp(lnlam), 0.3524)
check("Gini s=0.9", math.erf(0.9 / 2), 0.475, tol=2e-3)       # G = 2Phi(s/sqrt2)-1 = erf(s/2)
check("Gini s=0.5", math.erf(0.5 / 2), 0.276, tol=2e-3)

# ---------------------------------------------------------------- Block II
print("\nQ3(a) Solow, fall in n")
s, d, a = 0.20, 0.05, 1 / 3
kss = lambda n: (s / (n + d)) ** (1 / (1 - a))
yss = lambda n: kss(n) ** a
check("k* old", kss(0.02), 4.8295)
check("k* new", kss(0.01), 6.0858)
check("y* ratio - 1 (key)", yss(0.01) / yss(0.02) - 1, 0.0801)
check("k* ratio - 1 (distractor 26.0%)", kss(0.01) / kss(0.02) - 1, 0.2599)
check("(n+d) ratio - 1 (distractor 16.7%)", 0.07 / 0.06 - 1, 0.1667)

print("\nQ3(b) golden rule")
alpha, nd = 0.35, 0.07
cstar = lambda s_: (1 - s_) * (s_ / nd) ** (alpha / (1 - alpha))
grid = [i / 10000 for i in range(1, 10000)]
s_gr = max(grid, key=cstar)
check("golden-rule s by grid search", s_gr, alpha, tol=1e-4)
check("c*(0.17)", cstar(0.17), 1.3382)
check("c*(0.25)", cstar(0.25), 1.4885)
check_true("raising s from 0.17 to 0.25 raises c*", cstar(0.25) > cstar(0.17))
check_true("s = 1 - alpha = 0.65 gives lower c* than 0.35", cstar(0.65) < cstar(0.35))

print("\nQ3(c) conditional convergence counterexample")
# Country X: k=3, s=0.10; country Z: k=5, s=0.30 (same n, d, alpha=1/3).
gk = lambda k, s_: s_ * k ** (a - 1) - (0.02 + 0.05)
check("growth of k, X (lower k)", gk(3, 0.10), -0.0219)
check("growth of k, Z (higher k)", gk(5, 0.30), 0.0326)
check_true("lower-k country grows slower here", gk(3, 0.10) < gk(5, 0.30))

print("\nQ4 Custo Brasil")
al, th0, th1 = 0.4, 0.6, 0.28
check("unproductive share, theta=0.6", th0 / (1 + th0), 0.375)
check("unproductive share, theta=0.28", th1 / (1 + th1), 0.21875)
wedge0 = (1 + th0) ** (-al)
check("wedge (1+theta)^-alpha", wedge0, 0.8286)
check("output lost vs theta=0 (base: undistorted)", 1 - wedge0, 0.1714)
check("output gain from theta->0 (base: distorted)", 1 / wedge0 - 1, 0.2068)
check("A-hat / A", wedge0, 0.8286)
# firm FOC: alpha A Kp^(alpha-1) L^(1-alpha) = r (1+theta)  =>  rK/Y = alpha
A_, K_, L_ = 1.0, 10.0, 1.0
Kp = K_ / (1 + th0)
Y_ = A_ * Kp**al * L_ ** (1 - al)
r_ = al * A_ * Kp ** (al - 1) * L_ ** (1 - al) / (1 + th0)
check("measured capital share rK/Y", r_ * K_ / Y_, al, tol=1e-12)
w_ = (1 - al) * Y_ / L_
check("measured labour share wL/Y", w_ * L_ / Y_, 1 - al, tol=1e-12)
check("Y == Ahat K^a L^(1-a)", Y_, wedge0 * K_**al * L_ ** (1 - al), tol=1e-12)
resid = al * math.log((1 + th0) / (1 + th1))
check("ratio (1+theta)/(1+theta')", (1 + th0) / (1 + th1), 1.25, tol=1e-12)
check("residual over the decade (log)", resid, 0.08926)
check("residual per year", resid / 10, 0.008926, tol=5e-6)
check("residual per year if theta rises 0.28->0.6", -resid / 10, -0.008926, tol=5e-6)
check("ln Ahat start", math.log(wedge0), -0.1880)
check("ln Ahat end", math.log((1 + th1) ** (-al)), -0.0987)

# ---------------------------------------------------------------- Block III
print("\nQ5(a) permanent income, log, beta=1, r=0")
c1 = lambda y1, y2, r=0.0, beta=1.0: (y1 + y2 / (1 + r)) / (1 + beta)
b = c1(10_000, 10_000)
trip = (c1(11_000, 10_000) - b, c1(10_000, 11_000) - b, c1(11_000, 11_000) - b)
check("dc1: bonus today", trip[0], 500)
check("dc1: announced raise tomorrow", trip[1], 500)
check("dc1: permanent raise", trip[2], 1000)
only_key("Q5(a)", {"A": (1000, 0, 1000), "B": (500, 0, 1000), "C": (500, 500, 1000),
                   "D": (500, 500, 500), "E": (1000, 500, 2000)}, "C", lambda v: v == trip)

print("\nQ5(b) savings tax vs equal-revenue lump sum (log, beta=1, y1=100, y2=0, r=0.5)")
y1, r, tau = 100.0, 0.5, 0.4
Rt = 1 + r * (1 - tau)
c1s = y1 / 2                                   # log: c1 = W/(1+beta), W = y1 when y2 = 0
a_s = y1 - c1s
c2s = Rt * a_s
T = tau * r * a_s                              # revenue, collected in period 2
c1l = (y1 - T / (1 + r)) / 2
c2l = (1 + r) * (y1 - T / (1 + r) - c1l)
check("c2/c1 under savings tax", c2s / c1s, Rt)
check("c2/c1 under lump sum == 1+r", c2l / c1l, 1 + r)
check("savings-tax plan costs exactly lump-sum wealth at market prices",
      c1s + c2s / (1 + r), y1 - T / (1 + r), tol=1e-12)
U = lambda x, y: math.log(x) + math.log(y)
check_true("lump sum strictly preferred at equal revenue", U(c1l, c2l) > U(c1s, c2s))

print("\nQ5(c) log, y2 = 0: c1 invariant to r")
for rr in (0.0, 0.25, 1.0):
    check(f"c1 at r={rr}", c1(100, 0, rr, 0.9), 100 / 1.9, tol=1e-12)

print("\nQ6 static GE, alpha=1/3, psi=2/3")
al6, psi = 1 / 3, 2 / 3


def solve_L(At, sigma, tau=0.0, rebate=True):
    """Bisection on psi/(1-L) = (1-tau) w c^-sigma, with c = Y (rebate) or Y - tau wL."""
    def resid(L):
        Y = At * L ** (1 - al6)
        w = (1 - al6) * Y / L
        c = Y if rebate else Y - tau * w * L
        return psi / (1 - L) - (1 - tau) * w * c ** (-sigma)
    lo, hi = 1e-9, 1 - 1e-9
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if resid(mid) < 0 else (lo, mid)
    return 0.5 * (lo + hi)


At0 = 2 ** (2 / 3)
L0 = solve_L(At0, 2.0)
check("L at baseline, sigma=2", L0, 0.5, tol=1e-9)
Y0 = At0 * L0 ** (1 - al6)
check("c = Y at baseline", Y0, 1.0, tol=1e-9)
check("w at baseline", (1 - al6) * Y0 / L0, 4 / 3, tol=1e-9)
check("rK Kbar at baseline", al6 * Y0, 1 / 3, tol=1e-9)
elas = lambda sigma, L: (1 - sigma) / (al6 + (1 - al6) * sigma + L / (1 - L))
check("dlnL/dlnA formula, sigma=2, L=1/2", elas(2.0, 0.5), -0.375, tol=1e-12)
h = 1e-6
num = (math.log(solve_L(At0 * math.exp(h), 2.0)) - math.log(L0)) / h
check("dlnL/dlnA numerical", num, -0.375, tol=1e-4)
check("dlnw/dlnA = 1 - alpha dlnL", 1 - al6 * elas(2, 0.5), 1.125, tol=1e-12)
check("dlnrK/dlnA = 1 + (1-alpha) dlnL", 1 + (1 - al6) * elas(2, 0.5), 0.75, tol=1e-12)
check("dlnc/dlnA", 1 + (1 - al6) * elas(2, 0.5), 0.75, tol=1e-12)
check_true("sigma<1: hours rise", solve_L(At0 * 1.1, 0.5) > solve_L(At0, 0.5))
check("sigma=1: hours invariant to A", solve_L(5.0, 1.0) - solve_L(1.0, 1.0), 0.0, tol=1e-9)
check("sigma=1 baseline L", solve_L(1.0, 1.0), 0.5, tol=1e-9)
check("tau=0.25 rebated", solve_L(1.0, 1.0, 0.25, True), 3 / 7, tol=1e-9)
check("tau=0.25 thrown away", solve_L(1.0, 1.0, 0.25, False), 9 / 19, tol=1e-9)
check("closed form, rebated", 0.75 * (2 / 3) / (psi + 0.75 * (2 / 3)), 3 / 7, tol=1e-12)
check("thrown-away RHS (1-tau)(1-a)/(1-tau(1-a))", 0.75 * (2 / 3) / (1 - 0.25 * 2 / 3), 0.6, tol=1e-12)
# alpha -> 0: thrown-away tax leaves hours unchanged (the Lista 4 result, T = 0)
check("alpha->0 limit: thrown-away RHS independent of tau", (1 - 0.25) / (1 - 0.25), 1.0, tol=1e-12)

# ---------------------------------------------------------------- Block IV
print("\nQ7(b) Cagan seigniorage, m = 0.10 e^{-4 pi}")
S = lambda p: p * 0.10 * math.exp(-4 * p)
pis = [i / 100000 for i in range(1, 200000)]
pmax = max(pis, key=S)
check("revenue-maximising pi = 1/a", pmax, 0.25, tol=1e-4)
check("peak revenue, % GDP", 100 * S(0.25), 0.9197)
opts = {"A": (0.125, 100 * S(0.125)), "B": (0.25, 2.50), "C": (0.50, 100 * S(0.5)), "D": (0.25, 100 * S(0.25))}
check("distractor A revenue", opts["A"][1], 0.7582)
check("distractor B ignores base erosion", 100 * 0.25 * 0.10, 2.50)
check("distractor C revenue", opts["C"][1], 0.6767)
only_key("Q7(b)", opts, "D", lambda v: abs(v[0] - pmax) < 1e-3 and abs(v[1] - 100 * S(pmax)) < 1e-3)

print("\nQ8 Benigno mark-up shock")
alp, sig, eta, th, rho = 0.66, 0.5, 0.2, 8.0, 5.0
S_ = 1 / sig + eta
kap = (1 - alp) * S_ / alp
check("kappa", kap, 1.1333)
dmu = 4.4
dyn = -dmu / S_
check("dy_n", dyn, -2.0, tol=1e-12)
check("AS vertical shift = (1-alpha)/alpha dmu", (1 - alp) / alp * dmu, -kap * dyn, tol=1e-12)
sk = sig * kap
dy = sk / (1 + sk) * dyn
dp = -kap / (1 + sk) * dyn
check("dy no policy", dy, -0.7234)
check("dp no policy", dp, 1.4468)
check("y - y_n", dy - dyn, 1.2766)
check("y - y_e", dy, -0.7234)
# AD: p = rho - i - y/sigma (pbar = 0, ybar_n = 0), AS: p = kappa (y - y_n)
check("AD passes through equilibrium", rho - rho - dy / sig, dp, tol=1e-12)
rn = rho + (0 - dyn) / sig
check("r_n after the shock", rn, 9.0, tol=1e-12)
i_of = lambda y: rn - (1 + sk) / sig * (y - dyn)
check("i under no policy reproduces rho", i_of(dy), rho, tol=1e-12)
# optimal policy, Benigno weights phi_y = 1/2, phi_p = theta/(2 kappa), y* = y_e = 0
py, pp = 0.5, th / (2 * kap)
yo = (py * 0 + pp * kap**2 * dyn) / (py + pp * kap**2)
po = kap * (yo - dyn)
check("theta kappa", th * kap, 9.0667)
check("share 1/(1+theta kappa)", 1 / (1 + th * kap), 0.09934)
check("y^o", yo, -1.8013)
check("y^o - y_n", yo - dyn, 0.1987)
check("p^o - p^e", po, 0.2252)
check("targeting rule phi_y(y-y*) + kappa phi_p (p-p^e) = 0", py * yo + kap * pp * po, 0.0, tol=1e-12)
check("IT line: (y - y_e) + theta (p - p^e) = 0", yo + th * po, 0.0, tol=1e-12)
# brute force along AS
grid = [dyn + j * 1e-5 for j in range(0, 300001)]
Lf = lambda y: py * y**2 + pp * (kap * (y - dyn)) ** 2
check("y^o by grid search along AS", min(grid, key=Lf), yo, tol=1e-4)
io = i_of(yo)
check("i^o", io, 8.377)
check("AD at i^o passes through the optimum", rho - io - yo / sig, po, tol=1e-9)
check("rate rise vs no policy (pp)", io - rho, 3.377)
check("strict price stability i = r_n", i_of(dyn), 9.0, tol=1e-12)
check("strict output stabilisation i", i_of(0.0), 2.7333)
check("loss at optimum", Lf(yo), 1.8013)
check("loss at optimum, closed form", py * pp * kap**2 / (py + pp * kap**2) * dyn**2, Lf(yo), tol=1e-9)
check("loss with no policy", Lf(dy), 7.6494)
check_true("raise iff theta > sigma (welfare weights)", (io > rho) == (th > sig))
# with sigma > theta-equivalent weights the bank would cut: phi_p/phi_y * kappa < sigma
pp_dove = 0.2 * py * sig / kap          # (phi_p/phi_y) kappa = 0.2 sigma < sigma
yo_d = pp_dove * kap**2 * dyn / (py + pp_dove * kap**2)
check_true("a dovish bank ((phi_p/phi_y) kappa < sigma) cuts instead", i_of(yo_d) < rho)

print()
if failures:
    print(f"{len(failures)} CHECK(S) FAILED: " + "; ".join(failures))
    raise SystemExit(1)
print("all checks pass")
