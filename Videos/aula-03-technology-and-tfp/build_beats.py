"""Build beats.json from script.md.

The spoken text is the script with markdown emphasis and [pause] markers stripped:
Speechify ignores ellipses (verified - identical clip duration with and without), so an
intra-clip silence cannot be bought. The pauses are realised as holds in scenes.py and,
at beat boundaries, by the silence explainer-compile pads to the longer stream.
"""
import json, re, pathlib

TITLES = {
    "BeatOpen": "A hundred and thirty-eight per cent a year",
    "BeatGoldenSetup": "Unfinished business: which steady state is best?",
    "BeatGoldenFOC": "The last machine earns its own upkeep",
    "BeatSGold": "Save exactly capital's share of income",
    "BeatAsymmetry": "Over-accumulation is a mistake; under-accumulation is a preference",
    "BeatDynamicTest": "The test that needs no capital stock",
    "BeatFirmProblem": "Where the wage and the rental rate come from",
    "BeatZeroProfit": "Zero profit is forced, not assumed",
    "BeatAlphaEquilibrium": "Alpha as an equilibrium object, and the CES caveat",
    "BeatInterestRate": "r = f'(k) - delta, and the Golden Rule as r = n",
    "BeatEfficiencyUnits": "Technology, and the units nobody cares about",
    "BeatTildeLaw": "The law of motion with g in the break-even rate",
    "BeatBGP": "The balanced growth path, translated back",
    "BeatUzawa": "Why technology must multiply labour",
    "BeatDisappointing": "The model assumes the thing it was built to explain",
    "BeatCalibration": "Five facts in, a sixth fact out",
    "BeatConjecture": "Conjecture 5.1, stated to be tested",
    "BeatTest1": "Test one: convergence, and two honest qualifications",
    "BeatSpeed": "The speed the model demands, against the speed observed",
    "BeatTest2": "Test two: ten thousand dollars against one thousand",
    "BeatLucas": "Test three: the Lucas paradox, run on Brazil",
    "BeatResidual": "The Solow residual, derived and then solved for",
    "BeatIgnorance": "A measure of our ignorance",
    "BeatDevAccounting": "Development accounting: capital 29%, TFP 71%",
    "BeatKYform": "The K/Y form, and why the answer moves to 95%",
    "BeatHumanCapital": "Mincer, schooling, and the exponent trap",
    "BeatClose": "The bar, drawn twice",
}

def spoken(body: str) -> str:
    """Strip markdown and stage directions; return one paragraph of speakable prose."""
    body = re.sub(r"\[pause\]", "", body)
    body = re.sub(r"\*\*(.+?)\*\*", r"\1", body, flags=re.S)
    body = re.sub(r"\*(.+?)\*", r"\1", body, flags=re.S)
    body = body.replace("—", " - ").replace("*", "")
    return re.sub(r"\s+", " ", body).strip()

text = pathlib.Path("script.md").read_text(encoding="utf-8")
beats = []
for m in re.finditer(r"## (Beat\w+) . (\d+) s\n(.*?)(?=\n## |\Z)", text, re.S):
    bid, budget, body = m.group(1), int(m.group(2)), m.group(3)
    t = spoken(body)
    beats.append({"id": bid, "title": TITLES[bid], "text": t,
                  "audio": f"audio/{bid}.mp3", "seconds": 0.0, "budget_seconds": budget})

manifest = {"voice": None, "model": "simba-3.2", "total_seconds": 0.0, "beats": beats}
pathlib.Path("beats.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False),
                                      encoding="utf-8")
chars = sum(len(b["text"]) for b in beats)
over = [b["id"] for b in beats if len(b["text"]) > 2000]
print(f"{len(beats)} beats, {chars:,} characters, {sum(len(b['text'].split()) for b in beats):,} words")
print(f"beats over the 2000-char single-request cap (client chunks them): {len(over)}")
