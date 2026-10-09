"""Practice list D v4 (symbolic): runs every block check of practice-L7.tex; each aborts on its first mismatch.

Then checks the multiple-choice letters: each \\gabarito letter must point at the key option (the key
expressions are the ones the block checks verify) and the six keys must use every letter A-D at most twice.
Run from Listas/: python practice-L7-check.py
"""
import pathlib
import re
import runpy

HERE = pathlib.Path(__file__).parent
for part in ("b1", "b2", "b3a", "b3b"):
    runpy.run_path(str(HERE / f"practice-L7-check-{part}.py"), run_name="__main__")

KEYS = [  # LaTeX of each key option, in the order of the items: 1(a), 1(b), 3(a), 3(b), 5(a), 5(b)
    r"$(1-\alpha)(\sigma^{-1}+\eta)/\alpha$",
    r"$\bigl([(1+\eta)a-\mu]/(\sigma^{-1}+\eta),\ (1+\eta)a/(\sigma^{-1}+\eta)\bigr)$",
    r"$\left(\frac{\Delta}{\sigma^{-1}+\eta},\ \frac{\eta\,\Delta}{\sigma^{-1}+\eta}\right)$",
    r"$\left(\frac{\sigma^{-1}+\eta+\kappa}{\Omega},\ \frac{\eta}{\Omega}\right)$",
    r"$dy=\frac{\sigma}{1+\sigma\kappa}\,d\bar p$",
    r"$\big(\frac{(1+\eta)a}{\sigma^{-1}+\eta},\ 0\big)$",
]
tex = "".join((HERE / f"practice-L7-block{b}.tex").read_text(encoding="utf-8") for b in ("1", "2", "3a", "3b"))
items = re.findall(r"\\begin\{alternativas\}(.*?)\\end\{alternativas\}\s*\\gabarito\{([A-D])\}", tex, re.S)
assert len(items) == len(KEYS), len(items)
letters = [letter for _, letter in items]
for (body, letter), key in zip(items, KEYS):
    options = [o.strip() for o in body.split(r"\item")[1:]]
    assert len(options) == 4 and options["ABCD".index(letter)] == key, (letter, key)
assert all(1 <= letters.count(c) <= 2 for c in "ABCD"), letters
print("practice-L7: all checks passed; MC keys", "".join(letters))
