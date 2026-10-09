"""Practice list B v4 (symbolic): runs every block check of practice-L3-L4.tex; each aborts on its first mismatch.
Then checks that every multiple-choice answer letter points at its key and that the letters spread over A-D.

Run from Listas/: python practice-L3-L4-check.py
"""
import pathlib
import re
import runpy

HERE = pathlib.Path(__file__).parent
for part in ("b1", "b2", "b3a", "b3b"):
    runpy.run_path(str(HERE / f"practice-L3-L4-check-{part}.py"), run_name="__main__")

# Multiple choice, in order Q1(a), Q1(b), Q3(a), Q3(b), Q5(a), Q5(b): the option the block checks verify as the key.
KEYS = [r"\gamma=\beta^{1/\sigma}(1+r)^{1/\sigma-1}", r"r=(1+g)^{\sigma}/\beta-1", r"\varepsilon\,(N-k)/N$",
        r"\frac{1}{\xi}\,\frac{y}{y-w}", r"\Delta\bar c_1=\lambda T", r"+\theta(h_0^2-h_1^2)"]
tex = "".join((HERE / f"practice-L3-L4-block{b}.tex").read_text(encoding="utf-8") for b in ("1", "2", "3a"))
items = re.findall(r"\\begin\{alternativas\}(.*?)\\end\{alternativas\}\s*\\gabarito\{([A-D])\}", tex, re.S)
assert len(items) == len(KEYS), f"{len(items)} multiple-choice items"
letters = [letter for _, letter in items]
for (body, letter), key in zip(items, KEYS):
    options = body.split(r"\item")[1:]
    assert len(options) == 4 and sum(key in o for o in options) == 1, f"key option not unique: {key}"
    assert key in options["ABCD".index(letter)], f"\\gabarito{{{letter}}} does not point at {key}"
assert all(1 <= letters.count(c) <= 2 for c in "ABCD") and letters[:2] != letters[2:4], f"key letters {letters}"
print("practice-L3-L4: all checks passed")
