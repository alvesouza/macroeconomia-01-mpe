#!/usr/bin/env python3
"""Check Simulado 3: every number in the solution notes, and every link in them.

For each question the numbers are recomputed from the exam's data and compared with the
value printed in the note (the printed string must also appear in that note). Then every
[[wiki-link]] and relative Markdown link in Map/simulado-03/*.md must resolve to a file:
[[name]] is searched as name.md anywhere under Map/ (or the repo root), [[folder/name]] is
taken as a path under Map/ (or the repo root), and (relative/path) from the note's folder.

Run from anywhere: python Simulados/simulado_codigo/check_simulado_03.py
Exits non-zero with the list of failures.
"""
from __future__ import annotations

import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAP = ROOT / "Map"
NOTES = MAP / "simulado-03"
fails: list[str] = []


def note(q: str) -> str:
    return next(NOTES.glob(f"{q}-*.md")).read_text(encoding="utf-8")


def check(q: str, value: float, printed: str, tol: float) -> None:
    """Assert `value` rounds to the number in `printed` (within tol) and that `printed`
    appears verbatim in note `q`."""
    num = float(re.sub(r"[^0-9.\-]", "", printed.replace("−", "-").replace(",", "")))
    if not math.isclose(value, num, abs_tol=tol):
        fails.append(f"{q}: computed {value:.6g}, note prints {printed}")
    if printed not in note(q):
        fails.append(f"{q}: string '{printed}' not found in note")


# ---------------- Q1 index numbers
Y1, Y2 = 40 * 10 + 20 * 30, 20 * 30 + 25 * 25
L = (40 * 30 + 20 * 25) / Y1
P = Y2 / (20 * 10 + 25 * 30)
check("q1", Y2, "1225", 0)
check("q1", 100 * (L - 1), "70.0%", 0.05)
check("q1", 100 * (P - 1), "28.9%", 0.05)
check("q1", 100 * (math.sqrt(L * P) - 1), "48.1%", 0.05)
check("q1", L * P, "2.1921", 5e-5)

# ---------------- Q2 Brazil and Paraguay
gpy, gbr = 1.035 / 1.02 - 1, 1.025 / 1.005 - 1
check("q2", 100 * gpy, "1.47%", 0.005)
check("q2", 100 * gbr, "1.99%", 0.005)
assert gbr > gpy and 0.035 > 0.025          # the ranking flips
check("q2", (1 + gpy) ** 10, "1.1572", 5e-5)
check("q2", (1 + gbr) ** 10, "1.2178", 5e-5)
check("q2", 1.035 ** 10, "1.4106", 5e-5)
check("q2", 1.025 ** 10, "1.2801", 5e-5)
pbr, ppy = 9000 / 0.55, 6000 / 0.40
check("q2", pbr, "16{,}364", 0.5)
check("q2", ppy, "15{,}000", 0.5)
check("q2", pbr / ppy, "1.091", 5e-4)
check("q2", 1.5 / (pbr / ppy), "1.375", 5e-4)
check("q2", pbr / 0.45, "36{,}364", 0.5)
check("q2", ppy / 0.50, "30{,}000", 0.5)
check("q2", (pbr / 0.45) / (ppy / 0.5), "1.212", 5e-4)

# ---------------- Q3 Solow
a, nd = 1 / 3, 0.07
gk_poor = nd * ((1 / 0.8) ** (1 - a) - 1)
gk_rich = nd * ((1 / 0.35) ** (1 - a) - 1)
check("q3", 100 * gk_poor, "1.12\\%", 0.005)
check("q3", 100 * a * gk_poor, "0.37\\%", 0.005)
check("q3", 100 * gk_rich, "7.09\\%", 0.005)
check("q3", 100 * a * gk_rich, "2.36\\%", 0.005)
check("q3", (0.2 / 0.07) ** 1.5, "4.83", 0.005)
check("q3", (0.2 / 0.06) ** 1.5, "6.09", 0.005)
check("q3", (0.2 / 0.07) ** 0.5, "1.690", 5e-4)
check("q3", (0.2 / 0.06) ** 0.5, "1.826", 5e-4)
check("q3", (0.07 / 0.06) ** 0.5, "1.0801", 5e-5)

# ---------------- Q4 compliance wedge
Ahat0, Ahat1 = 1.25 ** (-2 / 3), 1.10 ** (-2 / 3)
check("q4", Ahat0, "0.862", 5e-4)
check("q4", Ahat1, "0.938", 5e-4)
check("q4", 100 * 0.25 / 1.25, "20\\%", 1e-9)
# firm FOC: wage bill equals (1-alpha) Y whatever phi is
K, LP, phi = 5.0, 2.0, 0.25
Y = K ** a * LP ** (1 - a)
w = (1 - a) * Y / LP / (1 + phi)
assert math.isclose(w * (1 + phi) * LP / Y, 2 / 3)
resid = (2 / 3) * math.log(1.25 / 1.10) / 5
check("q4", 100 * resid, "1.70\\%", 0.005)
check("q4", 100 * ((1.25 / 1.10) ** (2 / 15) - 1), "1.72\\%", 0.005)
check("q4", math.log(1.25 / 1.10), "0.12783", 5e-6)
check("q4", Ahat1 / Ahat0, "1.089", 5e-4)
check("q4", (Ahat1 / Ahat0) ** 1.5, "1.136", 5e-4)
check("q4", (1.25 / 1.10) ** a, "1.0435", 5e-5)

# ---------------- Q5 labour and search


def hours(tau, T, b=1.0, wage=1.0):
    return 1 / (1 + b) - b / (1 + b) * T / ((1 - tau) * wage)


assert hours(0.2, 0) == hours(0.3, 0) == 0.5
check("q5", hours(0.2, 0.1), "0.4375", 5e-5)
check("q5", hours(0.3, 0.1), "0.4286", 5e-5)
# numeric optimum agrees with the closed form
grid = [i / 100000 for i in range(1, 100000)]
lbest = max(grid, key=lambda l: math.log(0.7 * (1 - l) + 0.1) + math.log(l))
assert abs((1 - lbest) - hours(0.3, 0.1)) < 1e-4


def vac(u, mu, s=0.02, al=0.5):
    return (s * (1 - u) / (mu * u ** (1 - al))) ** (1 / al)


check("q5", 100 * vac(0.08, 0.5), "1.69\\%", 0.005)
check("q5", vac(0.08, 0.5) / 0.08, "0.21", 0.005)
check("q5", 0.5 * (vac(0.08, 0.5) / 0.08) ** 0.5, "0.23", 0.005)
check("q5", 100 * vac(0.06, 0.5), "2.36\\%", 0.005)
check("q5", vac(0.06, 0.5) / 0.06, "0.39", 0.005)
check("q5", 0.5 * (vac(0.06, 0.5) / 0.06) ** 0.5, "0.31", 0.005)
check("q5", 100 * vac(0.08, 0.4), "2.645\\%", 5e-4)
for u in (0.06, 0.08):   # steady state: job creation = job destruction, f = s(1-u)/u
    th = vac(u, 0.5) / u
    assert math.isclose(0.5 * th ** 0.5, 0.02 * (1 - u) / u)

# ---------------- Q6 consumption and GE


def D(r, s, beta=0.96):
    return 1 + beta ** (1 / s) * (1 + r) ** (1 / s - 1)


check("q6", D(0.04, 2), "1.96077", 5e-6)
check("q6", D(0.06, 2), "1.95166", 5e-6)
check("q6", 100 / D(0.04, 2), "51.00", 0.005)
check("q6", 100 / D(0.06, 2), "51.24", 0.005)
assert 100 / D(0.06, 0.5) < 100 / D(0.04, 0.5) and math.isclose(D(0.04, 1), D(0.06, 1))
check("q6", 100 * (1 / 0.96 - 1), "4.17\\%", 0.005)
check("q6", 100 * (1.03 ** 2 / 0.96 - 1), "10.51\\%", 0.005)
beta, r = 1 / 1.05, 0.05
W0 = 30 + 73.5 / 1.05
W1 = 40 + 63 / 1.05
assert math.isclose(W0, 100) and math.isclose(W1, 100)
c1 = W0 / (1 + beta)
check("q6", c1, "51.22", 0.005)
check("q6", 30 - c1, "-21.22", 0.005)
check("q6", 40 - c1, "-11.22", 0.005)
assert 30 - c1 < -15 < 40 - c1                  # binds before, slack after
check("q6", 73.5 - 1.05 * 15, "57.75", 1e-9)
check("q6", c1 - 45, "+6.22", 0.005)
beta = 0.96
c1T = 100 / (1 + beta)
aT = 100 - c1T
c2T = 1.03 * aT
R = 0.02 * aT
WL = 100 - R / 1.05
c1L = WL / (1 + beta)
c2L = 1.008 * c1L
check("q6", c1T, "51.02", 0.005)
check("q6", aT, "48.98", 0.005)
check("q6", c2T, "50.45", 0.005)
check("q6", c2T / c1T, "0.9888", 5e-5)
check("q6", R, "0.980", 5e-4)
check("q6", WL, "99.067", 5e-4)
check("q6", c1L, "50.54", 0.005)
check("q6", c2L, "50.95", 0.005)
check("q6", c2L / c1L, "1.008", 5e-4)
assert math.isclose(c1T + c2T / 1.05, WL)       # the tax plan is affordable under the lump sum
UT = math.log(c1T) + beta * math.log(c2T)
UL = math.log(c1L) + beta * math.log(c2L)
check("q6", UL, "7.69644", 5e-6)
check("q6", UT, "7.69635", 5e-6)
assert UL > UT

# ---------------- Q7 money
check("q7", 100 * (1.06 * 1.03 / 1.10 - 1), "-0.75\\%", 0.005)
check("q7", 1.06 * 1.03 / 1.10, "0.99255", 5e-6)
check("q7", math.sqrt(6 / 12), "0.7071", 5e-5)
check("q7", 100 * (1 - math.sqrt(0.5)), "29.3\\%", 0.05)
check("q7", 100 * (math.sqrt(2) - 1), "41.4%", 0.05)

# ---------------- Q8 NK
sg, kp, eta, th = 0.5, 1.133, 0.2, 8.0
m = sg / (1 + sg * kp)
check("q8", m, "0.3192", 5e-5)
dyn = -2.0
drn = -dyn / sg
gap = m * drn
check("q8", gap, "+1.277", 5e-4)
check("q8", dyn + gap, "-0.723", 5e-4)
check("q8", kp * gap, "+1.447", 5e-4)
assert math.isclose(dyn + gap, sg * kp / (1 + sg * kp) * dyn)
check("q8", -4.4 / (1 / sg + eta), "-2", 1e-9)
x = th * kp / (1 + th * kp) * dyn
ph = kp * (x - dyn)
check("q8", th * kp, "9.064", 1e-9)
check("q8", x, "-1.801", 5e-4)
check("q8", ph, "+0.225", 5e-4)
assert abs(x + th * ph) < 1e-12                  # Benigno (34)
check("q8", 100 / (1 + th * kp), "9.9\\%", 0.05)
rmi = (x - dyn) / m
check("q8", rmi, "0.623", 5e-4)
check("q8", drn - rmi, "+3.38", 0.005)
check("q8", kp * dyn, "-2.27", 0.005)             # E''': di = kappa * dy_n


def loss(xx, pp):
    return xx ** 2 + th / kp * pp ** 2


check("q8", loss(dyn + gap, kp * gap), "15.30", 0.005)
check("q8", loss(-2, 0), "4.00", 1e-9)
check("q8", loss(0, -kp * dyn), "36.26", 0.005)
check("q8", loss(x, ph), "3.60", 0.005)
# the optimum beats every point on AS
assert all(loss(z, kp * (z - dyn)) >= loss(x, ph) - 1e-12 for z in [i / 100 - 4 for i in range(500)])

# ---------------- links
WIKI = re.compile(r"\[\[([^\]]+?)\]\]")
REL = re.compile(r"\]\(([^)\s]+)\)")
names = {p.stem for p in ROOT.rglob("*.md")}
for md in sorted(NOTES.glob("*.md")):
    text = md.read_text(encoding="utf-8")
    for raw in WIKI.findall(text):
        target = raw.split("|")[0].split("#")[0].rstrip("\\").strip()
        if target.endswith(".md"):
            target = target[:-3]
        if "/" in target:
            ok = (MAP / f"{target}.md").exists() or (ROOT / f"{target}.md").exists()
        else:
            ok = target in names
        if not ok:
            fails.append(f"{md.name}: unresolved [[{raw}]]")
    for rel in REL.findall(text):
        if rel.startswith(("http:", "https:", "#")):
            continue
        if not (md.parent / rel.split("#")[0]).exists():
            fails.append(f"{md.name}: missing file ({rel})")

n_notes = len(list(NOTES.glob("*.md")))
if fails:
    print("FAIL\n" + "\n".join(fails))
    sys.exit(1)
print(f"OK: every number recomputed and found in its note; all links in {n_notes} notes resolve.")
