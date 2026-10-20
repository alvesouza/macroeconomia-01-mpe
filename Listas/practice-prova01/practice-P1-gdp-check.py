"""Checks every number in the solutions of practice-P1-gdp.tex; aborts (AssertionError) on the first mismatch.

Run from anywhere: python practice-P1-gdp-check.py
"""
import math
from fractions import Fraction as F


def agree(label, prod, inc, exp, gdp):
    """Assert that the product, income and expenditure columns (lists of entries) all sum to the stated GDP."""
    assert sum(prod) == sum(inc) == sum(exp) == gdp, (label, sum(prod), sum(inc), sum(exp), gdp)


# Q1 --- Kurlat 1.1
agree("1.1a", [1 - 1], [0], [1, -1], 0)
agree("1.1b", [F(2) + F(1, 2) - 1], [F(2) - F(1, 2)], [2, F(1, 2), -1], F(3, 2))
agree("Kurlat Ex.1.6 (x10)", [20 + 5 - 10], [15], [20, 5, -10], 15)  # book's worked example the 1.1(b) answer scales
assert F(3, 2) * 10 == 15
assert 5000 - 2000 - 1000 == 2000 and 15000 - 5000 == 10000
agree("1.1c", [10000, 5000 - 2000], [10000, 1000, 2000], [10000 + 5000, -2000], 13000)
agree("1.1d", [1500 - 1200], [300], [1500, -1200], 300)
agree("1.1d alt", [1200, 300], [1200, 300], [1500], 1500)
assert 1_000_000 - 200_000 - 100_000 - 300_000 == 400_000 and 50_000 - 20_000 == 30_000
agree("1.1e", [1_000_000 - 300_000, 50_000], [200_000 + 20_000, 100_000, 400_000 + 30_000],
      [1_000_000, 25_000, 25_000, -300_000], 750_000)
agree("1.1g", [4000], [4000], [4000], 4000)

# Q2 --- Jones Ex. 2 and 3 (answers as in Jones p.41 and the Jones IM p.12)
assert 2_000_000 == 1_000_000 + 1_000_000           # 3(a): final sale = VA of maker + VA of parts chain
assert 50_000_000 - 50_000_000 == 0                  # 3(d): I up, M up
assert 125_000 - 100_000 == 25_000                   # 3(f): C up 125k, M up 100k

# Q3 --- Kurlat 5.8
gr, pa, fa = 1000 - 200, 4000 - 1000 - 1400, 1000 - 400
dep = 2000 - 1800
assert (gr, pa, fa, dep) == (800, 1600, 600, 200) and gr - dep == 600
agree("5.8a", [1000, 4000 - 1000, 1000], [200 + 1400 + 400, 600 + 1600 + 600, 200], [4000, 1000], 5000)
alpha, s, delta = F(3000, 5000), F(1000, 5000), F(dep, 2000)
assert F(2000, 5000) == F(2, 5) and alpha == F(3, 5) and s == F(1, 5) and delta == F(1, 10)
dlnc = -1 / (1 - s) + alpha / ((1 - alpha) * s)
assert -1 / (1 - s) == F(-5, 4) and alpha / ((1 - alpha) * s) == F(15, 2) and dlnc == F(25, 4) > 0
K_Y = s / delta
assert K_Y == 2 and alpha / K_Y == F(3, 10) > delta  # MPK 0.3 > delta + n = 0.1
for s_try in (F(1, 10), F(3, 10), F(59, 100)):        # d ln c/ds > 0 exactly when s < alpha
    assert (-1 / (1 - s_try) + alpha / ((1 - alpha) * s_try) > 0) == (s_try < alpha)
assert -1 / (1 - alpha) + alpha / ((1 - alpha) * alpha) == 0

# Q4 --- Kurlat 5.7 (rubles, 10 per euro)
e = 10
welder, exports, beef = 1000 * e, 4000 * e, 2500 * e
wages_k, dep57, taxes = 100 * 350, (1000 - 960) * e, 100 * 100
assert (welder, exports, beef, wages_k, dep57, taxes) == (10_000, 40_000, 25_000, 35_000, 400, 10_000)
profit_k = exports - wages_k
assert profit_k == 5000 and profit_k - dep57 == 4600
agree("5.7b", [exports, 10_000], [wages_k, 10_000, profit_k], [beef, welder, 10_000, exports, -(welder + beef)], 50_000)
assert welder + beef == 35_000
alpha57 = F(profit_k, 50_000)
assert F(wages_k + 10_000, 50_000) == F(9, 10) and alpha57 == F(1, 10)
r = alpha57 * F(50_000, 100_000) - F(1000 - 960, 1000)
assert alpha57 * F(50_000, 100_000) == F(5, 100) and r == F(1, 100)
gY, gK, gL = F(55_000, 50_000) - 1, F(120_000, 100_000) - 1, F(105, 100) - 1
assert (gY, gK, gL) == (F(1, 10), F(1, 5), F(1, 20))
residual = gY - alpha57 * gK - (1 - alpha57) * gL
assert alpha57 * gK == F(2, 100) and (1 - alpha57) * gL == F(45, 1000) and residual == F(35, 1000)
assert residual / gY == F(35, 100)
lr = math.log(1.1) - 0.1 * math.log(1.2) - 0.9 * math.log(1.05)
assert (round(math.log(1.1), 4), round(0.1 * math.log(1.2), 4), round(0.9 * math.log(1.05), 4)) == (0.0953, 0.0182, 0.0439)
assert round(lr, 4) == 0.0332 and round(100 * lr / math.log(1.1), 1) == 34.8

# Q7 --- inventories and data sales
vaA, vaB, vaN = 600 + 200, (900 + 150) - (600 + 100 + 60), 100 + 60 + 40
assert (vaA, vaB, vaN) == (800, 290, 200) and 600 + 100 + 60 == 760
pA, pB, pN = 800 - 500, 1050 - 760 - 200, 200 - 120
assert (pA, pB, pN) == (300, 90, 80) and 500 + 200 + 120 == 820 and pA + pB + pN == 470
agree("Q7a", [vaA, vaB, vaN], [500, pA, 200, pB, 120, pN], [900, 200 + 150, 40], 1290)
assert 1290 - 200 - 150 == 940  # rubric: GDP if inventories are left out
agree("Q7c", [150 - 150], [150 - 150], [150, -150], 0)

# Q8 --- imports, app, dividends, government
vaA, vaB, vaN, vaG = 600 - 100, 1000 - 600 - 100, 100 + 80 + 100, 30
assert (vaA, vaB, vaN) == (500, 300, 280)
pA, pB, pN = 600 - 100 - 350, 1000 - 600 - 100 - 250, vaN - 150
assert (pA, pB, pN) == (150, 50, 130) and 350 + 250 + 150 + 30 == 780 and pA + pB + pN == 330
agree("Q8a", [vaA, vaB, vaN, vaG], [350, pA, 250, pB, 150, pN, 30], [850 + 80, 100, 30, 150, -100], 1110)
assert 850 + 80 == 930 and 850 + 150 == 1000 and 30 + 25 == 55
assert 1110 - 40 // 2 == 1090                   # GNI
assert 1100 + 80 + 30 - 100 == 1110              # bridge from Prova 01 Q1(c)

# Q9 --- capitalise vs expense
agree("Q9a(i)", [600, 1000 - 600 - 100, 100 + 100], [600, 300, 100, 200 - 100], [1000, 100], 1100)
agree("Q9a(ii)", [600, 300, 100], [600, 300, 100, 100 - 100], [1000], 1000)
vaB2, vaN2 = 1000 - 600 - 100 - 20, 100 + 50 + 20
assert (vaB2, vaN2) == (280, 170) and vaN2 - 30 == 140 and 100 // 4 == 25 and 140 - 25 == 115
agree("Q9b", [600, vaB2, vaN2], [600, vaB2, 30, 140], [1000 + 50], 1050)
assert 1050 - 25 == 1025                          # NDP
assert round(float(100 * (F(1050, 1100) - 1)), 2) == -4.55 and 100 * (F(1050, 1000) - 1) == 5
assert 300 - vaB2 == 20 and vaN2 - 100 == 70      # d): B's VA falls by 20; N's rises by the full 70

print("practice-P1-gdp: all checks passed")
