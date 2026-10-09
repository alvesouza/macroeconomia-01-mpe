"""Practice list A v4 (symbolic): runs every block check of practice-L1-L2.tex; each aborts on its first mismatch.
Then checks that every multiple-choice answer letter points at its key and that the letters spread over A-D.

Run from Listas/: python practice-L1-L2-check.py
"""
import pathlib
import re
import runpy

HERE = pathlib.Path(__file__).parent
for part in ("b1", "b2", "b3a", "b3b"):
    runpy.run_path(str(HERE / f"practice-L1-L2-check-{part}.py"), run_name="__main__")

# Multiple choice, in order Q1(a), Q1(b), Q3(a), Q3(b), Q5(a), Q5(b): the option the block checks verify as the key.
KEYS = [r"-\frac{1}{1-\eta}\ln(\omega R^{1-\eta}", r"\big(\bar u+gT-\frac{v_T}{2}\big)", r"(\chi/\phi)^{(1-\alpha)/\alpha}",
        r"^{1/(1-\psi)}N^{-\psi/(1-\psi)}", r"\big)^{\alpha/(1-\alpha)}", r"$\alpha_K/v-\delta>n+g$"]
tex = "".join((HERE / f"practice-L1-L2-block{b}.tex").read_text(encoding="utf-8") for b in ("1", "2", "3a"))
items = re.findall(r"\\begin\{alternativas\}(.*?)\\end\{alternativas\}\s*\\gabarito\{([A-D])\}", tex, re.S)
assert len(items) == len(KEYS), f"{len(items)} multiple-choice items"
letters = [letter for _, letter in items]
for (body, letter), key in zip(items, KEYS):
    options = body.split(r"\item")[1:]
    assert len(options) == 4 and sum(key in o for o in options) == 1, f"key option not unique: {key}"
    assert key in options["ABCD".index(letter)], f"\\gabarito{{{letter}}} does not point at {key}"
pairs = list(zip(letters[::2], letters[1::2]))                        # (a), (b) of Questions 1, 3, 5
offsets = {("ABCD".index(b) - "ABCD".index(a)) % 4 for a, b in pairs}
assert all(1 <= letters.count(c) <= 2 for c in "ABCD") and len(offsets) == len(pairs), f"key letters {letters}"
print("practice-L1-L2: all checks passed")
