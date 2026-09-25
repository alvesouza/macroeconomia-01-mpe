"""Build beats.json from script.md.

The spoken text is the script with markdown emphasis and [pause] markers stripped:
Speechify ignores ellipses (verified - identical clip duration with and without), so an
intra-clip silence cannot be bought. The pauses are realised as holds in scenes.py and,
at beat boundaries, by the silence explainer-compile pads to the longer stream.
"""
import json, re, pathlib

TITLES = {
    "BeatOpen": "Two windfalls, two marginal propensities",
    "BeatKeynes": "The Keynesian function, and its status as a rule",
    "BeatKuznets": "The puzzle: cross-section against time series",
    "BeatThreeFacts": "Smoothness, and news that moves consumption early",
    "BeatMethod": "What replacing a rule with a decision buys",
    "BeatPreferences": "Separability, concavity, geometric discounting",
    "BeatBudget": "The intertemporal budget constraint, and its three readings",
    "BeatEuler": "The Euler equation, three ways",
    "BeatSmoothing": "When r equals rho, the path is flat",
    "BeatClosedForms": "Log and CRRA, solved",
    "BeatEIS": "Risk aversion and the EIS are reciprocals by construction",
    "BeatPivot": "The line pivots about the endowment",
    "BeatDecomposition": "The elasticity, decomposed exactly",
    "BeatThreeCases": "Three cases, and why the slogan is not a theorem",
    "BeatPolicyCorollary": "Why a savings incentive can lower national saving",
    "BeatTwoMPCs": "0.51 against 1.00",
    "BeatHorizon": "In a real lifetime the gap is a factor of forty",
    "BeatKuznetsResolved": "The cross-section is a composition effect",
    "BeatRandomWalk": "Consumption should move only on news",
    "BeatTaxes": "The constraint contains G, and does not contain T",
    "BeatRicardian": "A deficit-financed tax cut is a forced loan",
    "BeatFiveAssumptions": "Five assumptions, five ways it fails",
    "BeatConstraints": "The wall, and the Euler equation as an inequality",
    "BeatTwoTypes": "Two types, and an aggregate MPC of a third",
    "BeatPrecaution": "Jensen, for the third time",
    "BeatClose": "One line, one wall",
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
