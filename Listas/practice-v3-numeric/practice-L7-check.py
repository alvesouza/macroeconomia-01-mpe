"""Graduate practice list D (Lista 7, Benigno 2015): independent check of every number and derivation.

Run: python practice-L7-check.py   (aborts on the first mismatch).
Each chk() mirrors a value printed in practice-L7.tex; sympy re-derives the article's closed forms.
"""
import sympy as sp


def chk(name, value, expected, tol=5e-4):
    assert abs(value - expected) <= tol * max(abs(expected), 1e-3), f"{name}: {value} != {expected}"
    print(f"{name:<48} {value:.6f}")


# ------------------------------------------------------------------ symbolic derivations
y, p, pe, yn, a, g, mu, al, sg, et, th = sp.symbols("y p p^e y_n a g mu alpha sigma eta theta", real=True)
# flexible-price firms: p~ = w - a + mu, labour supply w - p = eta l + sigma^-1 (y - g), l = y - a
ptilde = p + et * (y - a) + (y - g) / sg - a + mu
yn_expr = ((1 + et) * a + g / sg - mu) / (1 / sg + et)
assert sp.simplify(ptilde - p - (1 / sg + et) * (y - yn_expr)) == 0          # eq. (16)
# preset fraction alpha: p = alpha p^e + (1-alpha) p~  ->  p - p^e = kappa (y - y_n)
P = sp.solve(sp.Eq(p, al * pe + (1 - al) * ptilde), p)[0]
kap_expr = (1 - al) * (1 / sg + et) / al
assert sp.simplify(P - pe - kap_expr * (y - yn_expr)) == 0                    # eq. (17)
# planner: eta (y - a) + sigma^-1 (y - g) = a  ->  y_e
ye_expr = sp.solve(sp.Eq(et * (y - a) + (y - g) / sg, a), y)[0]
assert sp.simplify(ye_expr - ((1 + et) * a + g / sg) / (1 / sg + et)) == 0    # eq. (19)
assert sp.simplify(yn_expr - ye_expr + mu / (1 / sg + et)) == 0
# targeting rule from loss (33): min 1/2 (y-y_e)^2 + 1/2 (theta/kappa)(p-p^e)^2 s.t. AS
ye_, kap = sp.symbols("y_e kappa", real=True)
loss = (y - ye_) ** 2 / 2 + th / kap * (kap * (y - yn)) ** 2 / 2
ystar = sp.solve(sp.diff(loss, y), y)[0]
assert sp.simplify(ystar - (ye_ + th * kap * yn) / (1 + th * kap)) == 0
assert sp.simplify((ystar - ye_) + th * kap * (ystar - yn)) == 0            # (y-y_e)+theta(p-p^e)=0
# equilibrium gap: AD y = ybar_n - sigma[i - (pbar - p) - rho], AS; with g = gbar, taus = 0
i, rho, pbar, ybn = sp.symbols("i rho pbar ybar_n", real=True)
rn = rho + (ybn - yn) / sg
sol = sp.solve([sp.Eq(y, ybn - sg * (i - (pbar - p) - rho)), sp.Eq(p - pe, kap * (y - yn))], [y, p], dict=True)[0]
assert sp.simplify(sol[y] - yn - sg / (1 + sg * kap) * (rn - i + pbar - pe)) == 0
# fiscal multiplier m_g = 1/(1+kappa sigma) + kappa/D, D = (sigma^-1+eta)(1+kappa sigma)
gg = sp.Symbol("g", real=True)
ynG = (gg / sg) / (1 / sg + et)
solg = sp.solve([sp.Eq(y, gg - sg * (i - (pbar - p) - rho)), sp.Eq(p - pe, kap * (y - ynG))], [y, p], dict=True)[0]
mg = sp.diff(solg[y], gg)
D = (1 / sg + et) * (1 + kap * sg)
assert sp.simplify(mg - (1 / (1 + kap * sg) + kap / D)) == 0
# deleveraging AD (32) with borrowers; anchored long-run prices vs constant inflation
chi, d0, bs, dhat, pbn = sp.symbols("chi d_0 beta d_hat pbar_n", real=True)
phi = (sg * chi + (1 - chi) * d0 * bs) / chi
AD32 = ybn - phi * (i - (pbn - p) - rho) + (gg) / chi + (1 - chi) / chi * (dhat + d0 * (p - pe))
varpi = sg - d0 * (1 - bs) * (1 - chi) / chi
assert sp.simplify(sp.diff(AD32, p) + varpi) == 0
ynG2 = gg / (1 + sg * et)                                                     # = (g/sigma)/(1/sigma+eta)
sa = sp.solve([sp.Eq(y, AD32), sp.Eq(p - pe, kap * (y - ynG2))], [y, p], dict=True)[0]
m_anch = sp.diff(sa[y], gg)
assert sp.simplify(m_anch - (1 / chi + varpi * kap / (1 + sg * et)) / (1 + varpi * kap)) == 0
AD_const = AD32.subs(pbn, p + sp.Symbol("pi0"))                              # pbar_n - p held fixed
sc = sp.solve([sp.Eq(y, AD_const), sp.Eq(p - pe, kap * (y - ynG2))], [y, p], dict=True)[0]
m_const = sp.diff(sc[y], gg)
assert sp.simplify(m_const - (1 - d0 * (1 - chi) * kap / (1 + sg * et)) / (chi - d0 * (1 - chi) * kap)) == 0
dy_ddhat_const = sp.diff(sc[y], dhat)
assert sp.simplify(dy_ddhat_const - (1 - chi) / (chi - (1 - chi) * d0 * kap)) == 0

# ------------------------------------------------------------------ numbers
S, E, A, TH, RHO = 0.5, 0.2, 0.75, 8.0, 0.01
K = (1 - A) * (1 / S + E) / A
inv = 1 / S + E
chk("D1a kappa (alpha=.75, sigma=.5, eta=.2)", K, 0.733333)
chk("D1b dy_n (a=.02, mu=.05)", (1.2 * 0.02 - 0.05) / inv, -0.011818)
chk("D1b dy_e (a=.02)", 1.2 * 0.02 / inv, 0.010909)
Dn = inv * (1 + K * S)
chk("D1d m_gbar = eta/D", E / Dn, 0.066519)
gapc = S / (1 + S * K)
chk("D2 gap coefficient sigma/(1+sigma kappa)", gapc, 0.365854)
yn2 = (1.2 * -0.02 - 0.05) / inv
ye2 = 1.2 * -0.02 / inv
rn2 = RHO + (0 - yn2) / S
chk("D2d y_n (a=-.02, mu=.05)", yn2, -0.033636)
chk("D2d y_e", ye2, -0.010909)
chk("D2d r_n", rn2, 0.077273)
gap2 = gapc * (rn2 - RHO)
chk("D2d gap at i=rho", gap2, 0.024612)
chk("D2d y at i=rho", yn2 + gap2, -0.009024)
chk("D2d p-p^e at i=rho", K * gap2, 0.018049)
chk("D2d y - y_e at i=rho", yn2 + gap2 - ye2, 0.001885)
dyn = 0.02 / inv
chk("D3a dy_n from IPI cut", dyn, 0.009091)
chk("D3a d r_n", -dyn / S + 0.02, 0.001818)
mg_num = 1 / (1 + K * S) + K / Dn
chk("D3b m_g", mg_num, 0.975610)
chk("D3b gap multiplier", mg_num - (1 / S) / inv, 0.066519)
# optimal policy under the combined shock
tk = TH * K
ys = (ye2 + tk * yn2) / (1 + tk)
chk("D4 theta kappa", tk, 5.866667)
chk("D4 loss weight theta/kappa", TH / K, 10.909091)
chk("D4b optimal y", ys, -0.030326)
chk("D4b optimal p - p^e", K * (ys - yn2), 0.002428)
chk("D4b optimal y - y_e", ys - ye2, -0.019417)
chk("D4b optimal i", rn2 - (ys - yn2) / gapc, 0.068225)
# Taylor-rule critique: productivity shock a = .004 alone
yn_a = 1.2 * 0.004 / inv
chk("D4b y_n = y_e (a=.004)", yn_a, 0.002182)
chk("D4b r_n (a=.004)", RHO - yn_a / S, 0.005636)
chk("D4b r_n (a=-.004)", RHO + yn_a / S, 0.014364)
# markup shock alone mu = .05
yn_m = -0.05 / inv
ys_m = tk * yn_m / (1 + tk)
rn_m = RHO - yn_m / S
chk("D4b r_n (mu=.05)", rn_m, 0.055455)
chk("D4b optimal i (mu=.05)", rn_m - (ys_m - yn_m) / gapc, 0.046408)
# ZLB: pessimism abar = -.05
ybn_p = 1.2 * -0.05 / inv
rn_p = RHO + ybn_p / S
chk("D4c ybar_n", ybn_p, -0.027273)
chk("D4c r_n", rn_p, -0.044545)
chk("D4c gap at i=0", gapc * rn_p, -0.016297)
chk("D4c p-p^e at i=0", K * gapc * rn_p, -0.011951)
chk("D4c gap as kappa -> 0 (sigma r_n)", S * rn_p, -0.022273)
# deleveraging: chi = 2/3, d0 = 1.2, beta_s = .98
ch, dz, bt = 2 / 3, 1.2, 0.98
vp = S - dz * (1 - bt) * (1 - ch) / ch
chk("D4d varpi", vp, 0.488)
for A_, lab, ma, mc, ya, yc in [(0.75, ".75", 1.344266, 1.964286, -0.036823, -0.089286),
                                (0.66, ".66", 1.289597, 2.755682, -0.032195, -0.156250)]:
    Kx = (1 - A_) * inv / A_
    chk(f"D4d kappa alpha={lab}", Kx, (1 - A_) * 2.2 / A_)
    chk(f"D4d m anchored alpha={lab}", (1 / ch + vp * Kx / (1 + S * E)) / (1 + vp * Kx), ma)
    chk(f"D4d m const-infl alpha={lab}", (1 - dz * (1 - ch) * Kx / (1 + S * E)) / (ch - dz * (1 - ch) * Kx), mc)
    chk(f"D4d y anchored, dhat=-.1, alpha={lab}", (1 - ch) / ch * -0.1 / (1 + vp * Kx), ya)
    chk(f"D4d y const-infl, dhat=-.1, alpha={lab}", (1 - ch) * -0.1 / (ch - (1 - ch) * dz * Kx), yc)
    assert ch > (1 - ch) * dz * Kx                                            # stability (fn. 19)
x75 = (1 - ch) * dz * 0.733333 / ch
chk("D4d paradox of toil dy/dy_n (alpha=.75)", -x75 / (1 - x75), -0.785714)

# ---------------------------------------------------------------- v3 additions
# Q2(d) graph: AS-AD with the oil + productivity shock, units x100 (p^e = pbar = 0, i = rho)
yE, pE = 100 * (yn2 + gap2), 100 * K * gap2
chk("D2d graph E' y (x100)", yE, -0.902439)
chk("D2d graph E' p (x100)", pE, 1.804878)
assert abs(pE - (-2 * yE)) < 1e-9                                   # on the AD p = -y/sigma
assert abs(pE - K * (yE - 100 * yn2)) < 1e-9                        # on the new AS through (y_n', 0)
# Q2(e) markup shock alone (mu = .05, a = 0, i = rho) as a function of price rigidity alpha
def markup_response(A_, mu_=0.05):
    Kx = (1 - A_) * inv / A_
    gap_ = mu_ / ((1 + S * Kx) * inv)
    return Kx, -mu_ / inv + gap_, Kx * gap_
for A_, kv, yv, pv in [(0.5, 2.2, -0.011905, 0.023810), (0.66, 1.133333, -0.008221, 0.016441),
                       (0.75, 0.733333, -0.006098, 0.012195), (0.9, 0.244444, -0.002475, 0.004950)]:
    kx, yx, px = markup_response(A_)
    chk(f"D2e kappa alpha={A_}", kx, kv)
    chk(f"D2e y alpha={A_}", yx, yv)
    chk(f"D2e p-p^e alpha={A_}", px, pv)
chk("D2e limit alpha->0: p-p^e = mu/(1+sigma eta)", 0.05 / (1 + S * E), 0.045455)
# signs: y falls and p rises with kappa (closed forms)
ks = sp.Symbol("kappa", positive=True)
ymk = -1 / (1 / sg + et) + 1 / ((1 + sg * ks) * (1 / sg + et))
pmk = ks / ((1 + sg * ks) * (1 / sg + et))
assert sp.simplify(sp.diff(ymk, ks) + sg / ((1 + sg * ks) ** 2 * (1 / sg + et))) == 0
assert sp.simplify(sp.diff(pmk, ks) - 1 / ((1 + sg * ks) ** 2 * (1 / sg + et))) == 0
# Q4(e) deleveraging response vs alpha and the stability bound
chk("D4e stability bound kappa < chi/((1-chi) d0)", ch / ((1 - ch) * dz), 1.666667)
for A_, ya, yc in [(0.66, -0.032194, -0.156250), (0.75, -0.036822, -0.089286), (0.9, -0.044671, -0.058594)]:
    Kx = (1 - A_) * inv / A_
    chk(f"D4e y anchored alpha={A_}", (1 - ch) / ch * -0.1 / (1 + vp * Kx), ya)
    chk(f"D4e y const-infl alpha={A_}", (1 - ch) * -0.1 / (ch - (1 - ch) * dz * Kx), yc)
# multipliers vs alpha for the table
for A_, ma, mc in [(0.66, 1.289570, 2.755682), (0.75, 1.344266, 1.964286), (0.9, 1.437024, 1.601563)]:
    Kx = (1 - A_) * inv / A_
    chk(f"D4e m anchored alpha={A_}", (1 / ch + vp * Kx / (1 + S * E)) / (1 + vp * Kx), ma)
    chk(f"D4e m const-infl alpha={A_}", (1 - dz * (1 - ch) * Kx / (1 + S * E)) / (ch - dz * (1 - ch) * Kx), mc)
print("\nall checks passed")
