"""Build beats.json from script.md.

The spoken text is the script with markdown emphasis and [pause] markers stripped:
Speechify ignores ellipses (verified - identical clip duration with and without), so an
intra-clip silence cannot be bought. The pauses are realised as holds in scenes.py and,
at beat boundaries, by the silence explainer-compile pads to the longer stream.
"""
import json, re, pathlib

TITLES = {
    "BeatOpen": "Three answers to one question",
    "BeatFirmIdentity": "One firm: production is income",
    "BeatTelescope": "Value added telescopes",
    "BeatExpenditure": "The expenditure side, and the minus sign",
    "BeatConventions": "Four conventions, not theorems",
    "BeatGNP": "Territory against ownership; stocks against flows",
    "BeatExpandia": "Expandia: seventy per cent or fifty-five",
    "BeatCovariance": "The gap is a covariance",
    "BeatFisher": "Fisher, and why 'ideal' is earned",
    "BeatBias": "Substitution bias, proved and sized",
    "BeatDeflatorCPI": "Deflator against CPI, and Brazil as the mirror",
    "BeatLogs": "Log growth and its error term",
    "BeatProducts": "Products, ratios, powers",
    "BeatCAGR": "Why the arithmetic mean lies; the rule of seventy",
    "BeatLogScale": "Reading a log scale: Brazil and the US",
    "BeatPPPproblem": "The market rate cannot separate output from prices",
    "BeatPPPconstruct": "PPP: Laspeyres in space",
    "BeatBalassaSetup": "Balassa-Samuelson: the relative price is a technology ratio",
    "BeatBalassaPrediction": "From relative price to price level, and the prediction",
    "BeatDenominator": "Per person, per worker, per hour",
    "BeatHDI": "The HDI, and what a list can and cannot do",
    "BeatRawls": "Rawls behind the veil",
    "BeatJensen": "Jensen's inequality, and a warning",
    "BeatLambdaDerive": "Lambda, in four additive terms",
    "BeatLambdaBrazil": "Brazil against the US, term by term",
    "BeatClose": "The ladder",
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
