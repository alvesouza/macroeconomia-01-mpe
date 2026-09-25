"""Kurlat's three rejections of the capital hypothesis, evaluated on measured data.

Conjecture 5.1: technology is the same everywhere and income differences are capital
differences. Test 3 needs no capital data at all -- only relative income and the capital
share -- which is why it is the one the video animates.
"""
import csv, collections, math, statistics

ALPHA, DELTA, N, G, S_US = 0.35, 0.04, 0.01, 0.015, 0.20


def load(name):
    d = collections.defaultdict(dict)
    for r in csv.DictReader(open(f"data/{name}", encoding="utf-8")):
        if r["value"] and len(r["iso3"]) == 3:
            d[r["iso3"]][int(r["year"])] = float(r["value"])
    return d


y = load("wdi_ny_gdp_pcap_pp_kd.csv")

# --- the US calibration, and the K/Y consistency check that needs no capital data
r_k_us = ALPHA * (DELTA + N + G) / S_US
print(f"US: r^K = alpha(d+n+g)/s = {r_k_us:.3f}, r = {r_k_us - DELTA:.3f}")
print(f"    K/Y = s/(d+n+g) = {S_US / (DELTA + N + G):.2f}  (measured 3.2)")

# --- Test 3: the rental-rate ratio implied by Conjecture 5.1
print(f"\nrental ratio r^K_i / r^K_US = x^((a-1)/a), exponent {(ALPHA - 1) / ALPHA:.3f}")
for iso in ("MEX", "BRA", "IND"):
    x = y[iso][2023] / y["USA"][2023]
    ratio = x ** ((ALPHA - 1) / ALPHA)
    r_k = r_k_us * ratio
    print(f"{iso}: y/y_US = {x:.3f} -> rental {ratio:5.1f}x US, "
          f"r^K = {r_k:5.2f}, r = {r_k - DELTA:5.2f} ({(r_k - DELTA) * 100:.0f}% a year)")

# Kurlat's own Mexico figure, on his x = 0.3, is 9.4x. Reproduce it exactly.
assert abs(0.3 ** ((ALPHA - 1) / ALPHA) - 9.4) < 0.1, "Kurlat's 9.4x must reproduce"
print(f"\nKurlat's x=0.3 case: {0.3 ** ((ALPHA - 1) / ALPHA):.1f}x  (his 9.4) OK")

# --- convergence speed, model against data
lam = (1 - ALPHA) * (DELTA + N + G)
print(f"\nlambda = (1-a)(d+n+g) = {lam:.3f}, half-life {math.log(2) / lam:.1f} years")
a_needed = 1 - 0.02 / (DELTA + N + G)
print(f"to match the 2% found in data, alpha would have to be {a_needed:.2f}")

# --- development accounting, both forms, on the worked example
yi, ki, kyi, h_ratio = 0.10, 0.15, 0.80, math.exp(0.10 * (4 - 12))
cap_kl = ALPHA * math.log(ki) / math.log(yi)
cap_ky = (ALPHA / (1 - ALPHA)) * math.log(kyi) / math.log(yi)
print(f"\ndevelopment accounting, y_i/y_US = {yi}")
print(f"  K/L form: capital {cap_kl * 100:.1f}% of the log gap, TFP {100 - cap_kl * 100:.1f}%")
print(f"  K/Y form: capital {cap_ky * 100:.1f}% of the log gap, TFP {100 - cap_ky * 100:.1f}%")
print(f"  human capital h_i/h_US = {h_ratio:.2f}, contributing "
      f"{h_ratio ** (1 - ALPHA):.2f} in the K/L form")
assert cap_ky < cap_kl, "the K/Y form must attribute less to capital"
