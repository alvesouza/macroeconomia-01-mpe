"""Practice list C v4 (symbolic): runs every block check of practice-L5-L6.tex; each aborts on its first mismatch.

Run from Listas/: python practice-L5-L6-check.py
"""
import pathlib
import runpy

HERE = pathlib.Path(__file__).parent
for part in ("b1", "b2", "b3a", "b3b"):
    runpy.run_path(str(HERE / f"practice-L5-L6-check-{part}.py"), run_name="__main__")
print("practice-L5-L6: all checks passed")
