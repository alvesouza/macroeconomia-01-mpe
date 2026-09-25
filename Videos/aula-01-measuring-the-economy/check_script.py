"""Word-budget gate for script.md: each beat's narration against its budgeted seconds at 150 wpm."""
import re, pathlib

text = pathlib.Path("script.md").read_text(encoding="utf-8")
total_w = total_b = 0
print(f"{'beat':22} {'words':>6} {'est s':>7} {'budget':>7} {'delta':>7}")
for m in re.finditer(r"## (Beat\w+) . (\d+) s\n(.*?)(?=\n## |\Z)", text, re.S):
    beat, budget, body = m.group(1), int(m.group(2)), m.group(3)
    body = re.sub(r"\[pause\]", "", body)
    w = len(body.split())
    est = w / 2.5
    total_w += w; total_b += budget
    flag = "  <-- over" if est > budget * 1.12 else ("  <-- thin" if est < budget * 0.80 else "")
    print(f"{beat:22} {w:6d} {est:7.0f} {budget:7d} {est-budget:+7.0f}{flag}")
print(f"\n{'TOTAL':22} {total_w:6d} {total_w/2.5:7.0f} {total_b:7d}  "
      f"({total_w/2.5/60:.1f} min narration, {total_b/60:.1f} min budgeted)")
