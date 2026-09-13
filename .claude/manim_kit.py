# -*- coding: utf-8 -*-
"""Reusable Manim layer for narrated explainer videos.

Import this instead of hand-writing scene plumbing. It exists to make three failures
structurally impossible, because all three were observed in production:

1. GLACIAL PACING. Spreading a beat's whole duration across seven animations gave an
   average of 15 seconds per animation, five to thirty times slower than the idiom.
   `Beat` fixes this by construction: you declare each animation's own natural duration
   (about a second) and the kit absorbs the narration's remaining time as *holds*, which
   are still frames while the voice keeps talking. The beat still ends exactly on time.

2. OVERLAPPING TEXT. Free-floating labels placed with `next_to` eventually collide, and
   the result is unreadable. `Stage` gives every region of the screen a name and allows
   one occupant at a time: showing something new in a slot removes what was there.

3. FAKE TABLES. Three labels stacked inside one big rectangle is not a table. `table()`
   and `balance_sheet()` draw real cells with real rules, one row per item.

Usage:

    from manim_kit import Beat, Stage, palette, table, axes_panel

    class BeatSix(Scene):
        def construct(self):
            st = Stage(self)
            b = Beat(self, "BeatSix")
            sheet = balance_sheet([("reserves", "YELLOW"), ("bonds", None)],
                                  [("deposits", None)])
            b.step(st.show("main", sheet), t=1.0, hold=3)
            b.step(st.show("note", note_text("the reserves did not leave")), t=0.8, hold=5)
            b.run()

Durations come from beats.json, which holds the MEASURED length of each narration clip.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np
from manim import *

# --------------------------------------------------------------------- timing

#: An animation should feel like a gesture, not a journey.
FAST, NORMAL, SLOW = 0.6, 1.0, 1.8
#: Nothing on screen should ever take longer than this to happen.
MAX_RUN_TIME = 3.0


def load_beats(path=None):
    """Measured narration durations, by beat id."""
    p = Path(path) if path else Path.cwd() / "beats.json"
    if not p.exists():
        p = Path(__file__).parent / "beats.json"
    data = json.loads(p.read_text(encoding="utf-8"))
    return {b["id"]: b["seconds"] for b in data["beats"]}


class Beat:
    """Declare animations at natural speed; the kit distributes the narration's slack.

    The contract: every animation runs at a human speed (under MAX_RUN_TIME), and the
    time the voice needs beyond that is spent holding a still, readable frame. The sum
    of animation time and hold time equals the measured narration length exactly.
    """

    def __init__(self, scene, beat_id, beats=None):
        self.scene = scene
        self.beat_id = beat_id
        self.total = (beats or load_beats())[beat_id]
        self._steps = []

    def step(self, anims, t=NORMAL, hold=1.0):
        """One visual event.

        anims: a list of Animations (or None for a pure pause).
        t:     how long the motion itself takes. Keep it near a second.
        hold:  relative weight of the still frame that follows, while narration continues.
        """
        if t > MAX_RUN_TIME:
            raise ValueError(
                f"{self.beat_id}: run_time {t}s exceeds {MAX_RUN_TIME}s. "
                "Long beats get MORE steps, not slower ones.")
        self._steps.append((anims, t, max(hold, 0.0)))
        return self

    def run(self):
        if not self._steps:
            raise ValueError(f"{self.beat_id}: no steps declared")
        motion = sum(t for _, t, _ in self._steps)
        slack = self.total - motion
        if slack < 0:
            raise ValueError(
                f"{self.beat_id}: {motion:.1f}s of animation exceeds the "
                f"{self.total:.1f}s narration. Remove steps or shorten them.")
        weights = sum(h for _, _, h in self._steps) or 1.0
        for anims, t, hold in self._steps:
            if anims:
                self.scene.play(*anims, run_time=t)
            elif t > 0:
                self.scene.wait(t)
            pause = slack * hold / weights
            if pause > 0.02:
                self.scene.wait(pause)

    @property
    def events(self):
        return len(self._steps)


# ---------------------------------------------------------------------- stage

#: Named regions. One occupant each, so nothing can be drawn on top of anything else.
SLOTS = {
    "title": {"center": UP * 3.45, "width": 12.6, "height": 0.9},
    "main": {"center": UP * 0.25, "width": 12.6, "height": 5.1},
    "left": {"center": LEFT * 3.35 + UP * 0.25, "width": 5.9, "height": 5.1},
    "right": {"center": RIGHT * 3.35 + UP * 0.25, "width": 5.9, "height": 5.1},
    "aside": {"center": RIGHT * 4.15 + UP * 1.6, "width": 4.4, "height": 2.6},
    "note": {"center": DOWN * 3.25, "width": 12.6, "height": 1.0},
}


class Stage:
    """Screen regions with a single occupant each.

    `show` returns the animations that swap a slot's contents, so it composes with
    `Beat.step`. Because a slot is emptied before it is refilled, two pieces of text
    can never end up on the same pixels.
    """

    def __init__(self, scene):
        self.scene = scene
        self._held = {}

    @staticmethod
    def fit(mob, slot):
        box = SLOTS[slot]
        if mob.width > box["width"]:
            mob.scale_to_fit_width(box["width"])
        if mob.height > box["height"]:
            mob.scale_to_fit_height(box["height"])
        return mob.move_to(box["center"])

    def show(self, slot, mob, fit=True):
        """Animations that replace whatever is in `slot` with `mob`."""
        if fit:
            self.fit(mob, slot)
        out = []
        if slot in self._held:
            out.append(FadeOut(self._held[slot]))
        self._held[slot] = mob
        out.append(FadeIn(mob))
        return out

    def add_to(self, slot, mob):
        """Add to a slot without clearing it. Only for things that cannot collide."""
        prev = self._held.get(slot)
        self._held[slot] = VGroup(prev, mob) if prev else mob
        return [FadeIn(mob)]

    def clear(self, *slots):
        out = []
        for s in slots or list(self._held):
            if s in self._held:
                out.append(FadeOut(self._held.pop(s)))
        return out

    def occupied(self, slot):
        return slot in self._held


# -------------------------------------------------------------------- palette

def palette():
    """Colour roles, fixed for a whole video. One meaning per colour."""
    return {
        "demand": BLUE,      # money demand and anything derived from it
        "focus": YELLOW,     # the object of attention right now
        "broken": RED,       # the thing that breaks; the wrong guess
        "survives": GREEN,   # the result that survives
        "muted": GREY,       # background; closed channels; dropped observations
    }


# ----------------------------------------------------------------- components

def title(text, colour=GREY, size=30):
    return Text(text, font_size=size, color=colour)


def note(text, colour=GREY, size=24):
    return Text(text, font_size=size, color=colour, line_spacing=0.85)


def eq(tex, size=44, colour=WHITE):
    return MathTex(tex, font_size=size, color=colour)


def bullets(items, size=23, colour=WHITE, buff=0.22):
    return VGroup(*[Text(i, font_size=size, color=colour) for i in items]) \
        .arrange(DOWN, aligned_edge=LEFT, buff=buff)


def table(columns, rows, col_widths=None, row_height=0.62, font_size=21,
          header_colour=WHITE, rule_colour=GREY, cell_colours=None):
    """A real table: one cell per value, ruled rows and columns.

    columns: list of header strings.
    rows:    list of row tuples, one entry per column. Use "" for an empty cell.
    cell_colours: optional dict {(row_index, col_index): COLOR}.
    """
    ncol = len(columns)
    widths = col_widths or [3.2] * ncol
    cell_colours = cell_colours or {}
    total_w = sum(widths)
    total_h = row_height * (len(rows) + 1)

    grid = VGroup()
    frame = Rectangle(width=total_w, height=total_h, color=rule_colour, stroke_width=2)
    grid.add(frame)

    # column rules: vertical, full height, at each internal boundary
    x = -total_w / 2
    for w in widths[:-1]:
        x += w
        grid.add(Line([x, total_h / 2, 0], [x, -total_h / 2, 0],
                      color=rule_colour, stroke_width=1.5))

    # row rules
    y = total_h / 2
    for r in range(len(rows) + 1):
        y -= row_height
        if r < len(rows):
            grid.add(Line(LEFT * total_w / 2, RIGHT * total_w / 2,
                          color=rule_colour,
                          stroke_width=2 if r == 0 else 1)
                     .move_to([0, y, 0]))

    def cell_centre(r, c):
        x0 = -total_w / 2 + sum(widths[:c]) + widths[c] / 2
        y0 = total_h / 2 - row_height * (r + 0.5)
        return np.array([x0, y0, 0])

    for c, head in enumerate(columns):
        grid.add(Text(head, font_size=font_size + 2, color=header_colour)
                 .move_to(cell_centre(0, c)))
    for r, row in enumerate(rows, start=1):
        for c, val in enumerate(row):
            if val == "":
                continue
            grid.add(Text(str(val), font_size=font_size,
                          color=cell_colours.get((r - 1, c), WHITE))
                     .move_to(cell_centre(r, c)))
    return grid


def balance_sheet(assets, liabilities, width=9.0, row_height=0.66, font_size=21):
    """A T-account with one cell per line item, not three labels in one box.

    assets, liabilities: lists of (label, colour_or_None).
    """
    n = max(len(assets), len(liabilities))
    rows = []
    colours = {}
    for i in range(n):
        a = assets[i] if i < len(assets) else ("", None)
        l = liabilities[i] if i < len(liabilities) else ("", None)
        rows.append((a[0], l[0]))
        if a[1]:
            colours[(i, 0)] = a[1]
        if l[1]:
            colours[(i, 1)] = l[1]
    return table(["assets", "liabilities"], rows,
                 col_widths=[width / 2, width / 2],
                 row_height=row_height, font_size=font_size, cell_colours=colours)


def axes_panel(x_range, y_range, x_label=None, y_label=None,
               width=8.6, height=4.3, colour=GREY, coords=False):
    ax = Axes(x_range=x_range, y_range=y_range, x_length=width, y_length=height,
              axis_config={"include_tip": False, "color": colour, "font_size": 18})
    if coords:
        ax.add_coordinates()
    group = VGroup(ax)
    if x_label:
        group.add(Text(x_label, font_size=20, color=colour)
                  .next_to(ax.x_axis, DOWN, buff=0.28))
    if y_label:
        group.add(Text(y_label, font_size=20, color=colour).rotate(PI / 2)
                  .next_to(ax.y_axis, LEFT, buff=0.22))
    return ax, group


def sawtooth(ax, n, colour=BLUE, peak=1.0):
    pts = []
    for k in range(n):
        pts += [ax.c2p(k / n, peak / n), ax.c2p((k + 1) / n, 0.0)]
    return VMobject(color=colour, stroke_width=5).set_points_as_corners(pts)


def series(ax, points, colour=BLUE, width=4, clip=None):
    pts = [(x, min(y, clip) if clip is not None else y) for x, y in points]
    return VMobject(color=colour, stroke_width=width).set_points_as_corners(
        [ax.c2p(x, y) for x, y in pts])


def scatter(ax, points, colour=BLUE, radius=0.045):
    return VGroup(*[Dot(ax.c2p(p[0], p[1]), radius=radius, color=colour) for p in points])


def ols(points):
    """Slope, intercept, correlation. For fitting a line you intend to show."""
    n = len(points)
    mx = sum(p[0] for p in points) / n
    my = sum(p[1] for p in points) / n
    sxy = sum((p[0] - mx) * (p[1] - my) for p in points)
    sxx = sum((p[0] - mx) ** 2 for p in points)
    syy = sum((p[1] - my) ** 2 for p in points)
    slope = sxy / sxx
    return slope, my - slope * mx, sxy / (sxx ** 0.5 * syy ** 0.5)


def read_csv(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


# ------------------------------------------------- visuals that are not Manim

def mpl_figure(draw, name, width=9.0, dpi=240, figsize=(8.0, 4.5),
               cache_dir="figures", ink="#e8ebef", regenerate=False):
    """Draw with matplotlib, composite into the scene as an image.

    Manim is excellent at construction — a curve being built, a term moving — and poor at
    dense data. Twelve thousand scatter points, a long time series, a heatmap: matplotlib
    draws those better and faster. Use this for those, and keep Manim for the argument.

    draw: callable(fig, ax) that does the drawing. Axes are pre-styled for a dark canvas.
    name: cache key; the PNG is written to cache_dir/<name>.png and reused unless
          regenerate=True, so re-rendering a beat does not redraw the figure.

    Returns an ImageMobject scaled to `width` scene units.
    """
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    out = Path(cache_dir)
    out.mkdir(parents=True, exist_ok=True)
    png = out / f"{name}.png"

    if regenerate or not png.exists():
        fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
        fig.patch.set_alpha(0.0)
        ax.set_facecolor("none")
        for spine in ("bottom", "left"):
            ax.spines[spine].set_color(ink)
        for spine in ("top", "right"):
            ax.spines[spine].set_visible(False)
        ax.tick_params(colors=ink, labelsize=9)
        ax.xaxis.label.set_color(ink)
        ax.yaxis.label.set_color(ink)
        ax.title.set_color(ink)
        draw(fig, ax)
        fig.savefig(png, transparent=True, bbox_inches="tight", pad_inches=0.08)
        plt.close(fig)

    return ImageMobject(str(png)).scale_to_fit_width(width)


def image_asset(path, width=8.0, credit=None):
    """An image from disk: a licensed still, a diagram, a generated texture.

    `credit` is not decoration. Anything that did not originate in this project needs its
    source and licence recorded in provenance.md before it ships. Public domain, CC0 and
    CC-BY are fine, CC-BY with the attribution actually written down; a frame grabbed from
    someone's video is not.
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"asset not found: {p}")
    if credit is None:
        raise ValueError(
            f"{p.name}: pass credit='source, licence' and record it in provenance.md")
    return ImageMobject(str(p)).scale_to_fit_width(width)


def svg_asset(path, width=6.0, credit="original"):
    """An SVG drawn for this project, or an openly licensed one. Manim parses SVG natively."""
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"asset not found: {p}")
    return SVGMobject(str(p)).scale_to_fit_width(width)
