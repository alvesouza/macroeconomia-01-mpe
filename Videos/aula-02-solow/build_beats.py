"""Build beats.json from script.md.

The spoken text is the script with markdown emphasis and [pause] markers stripped:
Speechify ignores ellipses (verified - identical clip duration with and without), so an
intra-clip silence cannot be bought. The pauses are realised as holds in scenes.py and,
at beat boundaries, by the silence explainer-compile pads to the longer stream.
"""
import json, re, pathlib

TITLES = {
    "BeatOpen": "Eighteen per cent against twenty-one",
    "BeatVeryLongRun": "Growth is recent, and the date of take-off orders the world",
    "BeatKaldor": "The Kaldor facts, with the numbers",
    "BeatFactFour": "Fact four is facts two and three, divided",
    "BeatScatter": "The scatter that kills absolute convergence",
    "BeatCRS": "Four assumptions about technology, and what each buys",
    "BeatCobbDouglas": "Verifying Cobb-Douglas, all four",
    "BeatEuler": "Euler's theorem: alpha IS the capital share",
    "BeatSavingRate": "Population, closure, saving, depreciation",
    "BeatPerWorker": "Constant returns buys the per-worker form",
    "BeatLawOfMotion": "The law of motion, seven lines",
    "BeatApproximation": "The one plus n changes speed, never destination",
    "BeatContinuous": "Continuous time, and the Romer reconciliation",
    "BeatGrowthRate": "A falling curve against a flat line",
    "BeatDiagram": "The Solow diagram, built",
    "BeatClosedForm": "The steady state in closed form",
    "BeatExistence": "Existence is exactly Inada",
    "BeatUniqueness": "Uniqueness is exactly diminishing returns",
    "BeatAK": "Take diminishing returns away: the AK model",
    "BeatStability": "Stability proved, and the seventeen-year half-life",
    "BeatCompStatics": "Every row's growth column is zero",
    "BeatTransition": "The transition: what jumps and what cannot",
    "BeatNumbers": "What saving more actually buys",
    "BeatConsumption": "The criterion that turns out to be the Golden Rule",
    "BeatBrazil": "Pointing the model at Brazil",
    "BeatClose": "Two dots, and what session three must do",
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
