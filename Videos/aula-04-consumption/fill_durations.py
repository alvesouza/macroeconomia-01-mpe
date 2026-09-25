"""Fill beats.json seconds from cached audio; estimate any clip not yet synthesised.

Speechify credits ran out mid-run, so the client never wrote the manifest. Measured
durations come from ffprobe on the clips already paid for; the rest are estimated at the
rate `george` actually speaks (197 wpm, measured in aula-01), and flagged `estimated` so
they can be re-measured and re-rendered when credits return.
"""
import json, pathlib, subprocess

WPM = 197.0
m = json.loads(pathlib.Path("beats.json").read_text(encoding="utf-8"))

for b in m["beats"]:
    f = pathlib.Path(b["audio"])
    if f.exists():
        out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                              "-of", "csv=p=0", str(f)], capture_output=True, text=True)
        b["seconds"] = round(float(out.stdout.strip()), 3)
        b.pop("estimated", None)
    else:
        b["seconds"] = round(len(b["text"].split()) / WPM * 60, 3)
        b["estimated"] = True

m["voice"] = "george"
m["total_seconds"] = round(sum(b["seconds"] for b in m["beats"]), 3)
pathlib.Path("beats.json").write_text(json.dumps(m, indent=2, ensure_ascii=False), encoding="utf-8")

est = [b["id"] for b in m["beats"] if b.get("estimated")]
held = sum(b.get("pauses", 0) * 2.5 for b in m["beats"])
print(f"{len(m['beats']) - len(est)} measured, {len(est)} estimated: {', '.join(est)}")
print(f"total {m['total_seconds'] / 60:.1f} min + {held / 60:.1f} min held "
      f"= {(m['total_seconds'] + held) / 60:.1f} min")
