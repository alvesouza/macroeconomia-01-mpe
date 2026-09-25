"""Compute the Jones-Klenow lambda for Brazil against the US from the fetched WDI series.

The video never asserts a published lambda. It derives the four-term decomposition on
screen and then evaluates the three terms the data support, stating that the leisure term
is set to zero for want of a verified hours series and that the mortality term is at the
mercy of ubar, which has no market price.

Verification: the closed-form decomposition is checked against a brute-force expected
utility calculation over a simulated lognormal consumption distribution.
"""
import csv, math, collections, statistics, random

YEAR = 2023
SIGMA = 1.0          # Jones-Klenow's own choice: conservative, minimises the penalty
THETA_TERM = 0.0     # leisure term omitted; no verified hours series fetched


def load(name):
    d = collections.defaultdict(dict)
    for r in csv.DictReader(open(f"data/{name}", encoding="utf-8")):
        if r["value"]:
            d[r["iso3"]][int(r["year"])] = float(r["value"])
    return d


def latest(series, iso, upto=YEAR):
    """Most recent observation at or before `upto` -- Gini is published irregularly."""
    yrs = [y for y in series[iso] if y <= upto]
    return series[iso][max(yrs)], max(yrs)


def s_from_gini(g):
    """Log standard deviation implied by a Gini index under lognormality: G = 2*Phi(s/sqrt2)-1."""
    return math.sqrt(2) * statistics.NormalDist().inv_cdf((g / 100 + 1) / 2)


cons, pop = load("wdi_ne_con_prvt_pp_kd.csv"), load("wdi_sp_pop_totl.csv")
gini, life = load("wdi_si_pov_gini.csv"), load("wdi_sp_dyn_le00_in.csv")

c = {k: cons[k][YEAR] / pop[k][YEAR] for k in ("BRA", "USA")}
g = {k: latest(gini, k) for k in ("BRA", "USA")}
s = {k: s_from_gini(g[k][0]) for k in ("BRA", "USA")}
e = {k: life[k][YEAR] / 100 for k in ("BRA", "USA")}

print(f"--- inputs, {YEAR}")
for k in ("BRA", "USA"):
    print(f"{k}: c/head {c[k]:>9,.0f}   Gini {g[k][0]:.1f} ({g[k][1]}) -> s {s[k]:.3f}   "
          f"LE {life[k][YEAR]:.1f} -> e {e[k]:.3f}")

t1 = math.log(c["BRA"] / c["USA"])
t2 = -0.5 * SIGMA * (s["BRA"] ** 2 - s["USA"] ** 2)
t3 = -THETA_TERM

print(f"\n--- decomposition of ln(lambda), sigma = {SIGMA}")
print(f"(1) consumption      {t1:+.3f}   = ratio {math.exp(t1):.3f}")
print(f"(2) inequality       {t2:+.3f}   = factor {math.exp(t2):.3f}")
print(f"(3) leisure          {t3:+.3f}   (omitted: no verified hours series)")
for ubar in (0.0, 5.0, 10.0):
    flow = ubar + math.log(c["BRA"])
    t4 = (e["BRA"] - e["USA"]) / e["USA"] * flow
    lam = math.exp(t1 + t2 + t3 + t4)
    print(f"(4) life, ubar={ubar:4.1f}   {t4:+.3f}   ->  lambda = {lam:.3f}"
          f"   (income ratio at PPP = {c['BRA']/c['USA']:.3f})")

# --- brute force: does -s^2/2 really equal E[ln c] - ln E[c]?
random.seed(0)
for k in ("BRA", "USA"):
    mu = math.log(c[k]) - s[k] ** 2 / 2
    draws = [math.exp(random.gauss(mu, s[k])) for _ in range(400_000)]
    gap = statistics.fmean(math.log(x) for x in draws) - math.log(statistics.fmean(draws))
    assert abs(gap - (-s[k] ** 2 / 2)) < 0.01, (k, gap, -s[k] ** 2 / 2)
    print(f"check {k}: E[ln c] - ln E[c] = {gap:+.4f}  vs  -s^2/2 = {-s[k]**2/2:+.4f}  OK")
