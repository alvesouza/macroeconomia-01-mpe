"""Shared matplotlib style for every figure embedded in the Map/ notes.

Import it before plotting so all folders read as one system (reference palette of the
dataviz skill, light surface, recessive grid, text kept as SVG text):

    import sys, pathlib
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "fig"))
    from mapstyle import S, INK, INK2, SURF, save

Series colours are used in fixed order S[0], S[1], ... and never cycled past S[4].
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

S = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4"]
INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"

plt.rcParams.update({
    "svg.fonttype": "none", "font.size": 10, "axes.edgecolor": INK2,
    "axes.labelcolor": INK, "xtick.color": INK2, "ytick.color": INK2,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8,
    "figure.facecolor": SURF, "axes.facecolor": SURF, "lines.linewidth": 2,
    "legend.frameon": False,
})


def save(fig, path: Path) -> None:
    """Write `fig` as SVG to `path` (creating its folder) and close it.

    path: full target path ending in .svg, normally <note folder>/fig/<name>.svg.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(path, format="svg")
    plt.close(fig)
    print("wrote", path.name)
