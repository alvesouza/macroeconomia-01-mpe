"""Can saving-rate differences explain the Brazil-US income gap? Evaluate, do not assert.

The Solow steady state gives d ln y_ss / d ln s = alpha/(1-alpha). With alpha = 1/3 that
elasticity is 0.5, so even a large saving-rate difference moves income by its square root.
This script puts the measured Brazilian and American investment rates through it and
compares the model's predicted ratio with the observed one.
"""
import csv, collections, statistics

ALPHA, DELTA = 1 / 3, 0.05


def load(name):
    d = collections.defaultdict(dict)
    for r in csv.DictReader(open(f"data/{name}", encoding="utf-8")):
        if r["value"]:
            d[r["iso3"]][int(r["year"])] = float(r["value"])
    return d


y, inv, pop = (load("wdi_ny_gdp_pcap_pp_kd.csv"), load("wdi_ne_gdi_totl_zs.csv"),
               load("wdi_sp_pop_grow.csv"))


def avg(series, iso, lo=2000, hi=2023):
    v = [series[iso][t] for t in range(lo, hi + 1) if t in series[iso]]
    return statistics.fmean(v)


print(f"--- averages 2000-2023, alpha = {ALPHA:.3f}, delta = {DELTA}")
par = {}
for iso in ("BRA", "USA"):
    s, n = avg(inv, iso) / 100, avg(pop, iso) / 100
    par[iso] = (s, n)
    print(f"{iso}: s = {s:.3f}   n = {n:.4f}   y(2023) = {y[iso][2023]:,.0f}")

(sb, nb), (su, nu) = par["BRA"], par["USA"]
obs = y["BRA"][2023] / y["USA"][2023]

# Steady-state ratio implied by the model's own closed form.
pred_s_only = (sb / su) ** (ALPHA / (1 - ALPHA))
pred_full = ((sb / (nb + DELTA)) / (su / (nu + DELTA))) ** (ALPHA / (1 - ALPHA))

print(f"\nobserved  y_BR / y_US                      = {obs:.3f}")
print(f"predicted from saving rates alone          = {pred_s_only:.3f}")
print(f"predicted from s and (n+delta) together    = {pred_full:.3f}")
print(f"\nunexplained factor (observed vs full model) = {pred_full / obs:.2f}x")

# What saving rate would Brazil need for the model to fit? Invert the closed form.
needed = su * (obs ** ((1 - ALPHA) / ALPHA)) * (nb + DELTA) / (nu + DELTA)
print(f"\nBrazil's investment rate would have to be   = {needed:.3f}"
      f"  ({needed * 100:.1f}% of GDP) for saving alone to explain the gap")
assert needed < 0.05, "the required rate should be implausibly small"

# The elasticity itself, stated as the video states it.
print(f"\nd ln y_ss / d ln s = alpha/(1-alpha) = {ALPHA/(1-ALPHA):.3f}")
print(f"so doubling the saving rate raises y_ss by a factor {2 ** (ALPHA/(1-ALPHA)):.3f}")
