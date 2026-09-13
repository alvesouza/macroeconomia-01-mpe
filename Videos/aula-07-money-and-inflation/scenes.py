"""Scenes for aula-07-money-and-inflation. One Scene per beat.

Durations come from beats.json, which holds the MEASURED length of each narration clip.
Never hard-code seconds here.

Render one beat:
    cd "Videos/aula-07-money-and-inflation"
    python -m manim render -ql --media_dir "media" scenes.py BeatOne

Colour roles, fixed for the whole video:
    BLUE   money demand and anything derived from it
    YELLOW the object of attention now; the elasticity; the Selic
    RED    the thing that breaks; the wrong guess
    GREEN  the result that survives; the 45-degree line
    GREY   background; closed channels; dropped observations
"""
import csv
import json
from pathlib import Path

import numpy as np
from manim import *

HERE = Path(__file__).parent
BEATS = {b["id"]: b["seconds"] for b in
         json.loads((HERE / "beats.json").read_text(encoding="utf-8"))["beats"]}
DATA = HERE / "data"


def steps(beat, *weights):
    """Split a beat's measured duration into weights that must sum to 100."""
    total = sum(weights)
    assert total == 100, f"{beat}: weights sum to {total}, not 100"
    T = BEATS[beat]
    return [T * w / 100.0 for w in weights]


def heading(text, colour=WHITE):
    return Text(text, font_size=30, color=colour).to_edge(UP, buff=0.4)


def load_csv(name):
    with open(DATA / name, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def scatter_data():
    """Country averages: money growth against inflation."""
    rows = load_csv("wdi_money_vs_inflation_country_averages.csv")
    return [(float(r["money_growth_avg"]), float(r["inflation_avg"]), r["country"]) for r in rows]


def ols(pts):
    n = len(pts)
    mx = sum(p[0] for p in pts) / n
    my = sum(p[1] for p in pts) / n
    sxy = sum((p[0] - mx) * (p[1] - my) for p in pts)
    sxx = sum((p[0] - mx) ** 2 for p in pts)
    syy = sum((p[1] - my) ** 2 for p in pts)
    slope = sxy / sxx
    corr = sxy / (sxx ** 0.5 * syy ** 0.5)
    return slope, my - slope * mx, corr



# ---------------------------------------------------------------- Act I

class BeatOne(Scene):
    """The miss. A target line, a realised line, and the gap between them."""

    def construct(self):
        a, b, c, d, e, f, g, h = steps("BeatOne", 10, 10, 12, 12, 10, 10, 20, 16)
        ax = Axes(x_range=[0, 10, 2], y_range=[0, 3, 1], x_length=9, y_length=4.2,
                  axis_config={"include_tip": False, "color": GREY})
        labs = VGroup(Text("year", font_size=22, color=GREY).next_to(ax.x_axis, DOWN, buff=0.2),
                      Text("inflation, per cent", font_size=22, color=GREY)
                      .rotate(PI / 2).next_to(ax.y_axis, LEFT, buff=0.2))
        self.play(Create(ax), FadeIn(labs), run_time=a)

        target = DashedLine(ax.c2p(0, 2), ax.c2p(10, 2), color=GREY)
        tlab = Text("target  2", font_size=24, color=GREY).next_to(target, RIGHT, buff=0.15)
        self.play(Create(target), FadeIn(tlab), run_time=b)

        real = Line(ax.c2p(0, 0.5), ax.c2p(10, 0.5), color=RED, stroke_width=6)
        rlab = Text("realised  0.5", font_size=24, color=RED).next_to(real, RIGHT, buff=0.15)
        self.play(Create(real), FadeIn(rlab), run_time=c)

        br = BraceBetweenPoints(ax.c2p(5, 0.5), ax.c2p(5, 2), direction=LEFT, color=YELLOW)
        brl = Text("1.5 points", font_size=26, color=YELLOW).next_to(br, LEFT, buff=0.15)
        self.play(GrowFromCenter(br), FadeIn(brl), run_time=d)

        facts = VGroup(
            Text("the economy grows at 3 per cent", font_size=24),
            Text("it chose money growth of 3.5 per cent", font_size=24),
            Text("it controlled the money stock exactly", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22).to_corner(UL, buff=0.5)
        self.play(FadeIn(facts[0], shift=RIGHT * 0.3), run_time=e)
        self.play(FadeIn(facts[1], shift=RIGHT * 0.3), run_time=f)

        q = Text("It did everything right and still missed.\nWhat did it get wrong?",
                 font_size=34, color=YELLOW, line_spacing=0.8)
        q.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(facts[2], shift=RIGHT * 0.3), Write(q), run_time=g)
        self.wait(h)


class BeatTwo(Scene):
    """The sawtooth of money holdings, for two trips and then four."""

    @staticmethod
    def teeth(ax, n):
        pts = []
        for k in range(n):
            x0, x1 = k / n, (k + 1) / n
            pts += [ax.c2p(x0, 1.0 / n), ax.c2p(x1, 0.0)]
        return VMobject(color=BLUE, stroke_width=5).set_points_as_corners(pts)

    def construct(self):
        a, b, c, d, e, f, g, h = steps("BeatTwo", 10, 8, 18, 12, 18, 12, 12, 10)
        ax = Axes(x_range=[0, 1, 0.25], y_range=[0, 0.6, 0.25], x_length=9, y_length=4,
                  axis_config={"include_tip": False, "color": GREY})
        xl = Text("one year", font_size=22, color=GREY).next_to(ax.x_axis, DOWN, buff=0.2)
        yl = Text("money held", font_size=22, color=GREY).rotate(PI / 2) \
            .next_to(ax.y_axis, LEFT, buff=0.2)
        self.play(Create(ax), FadeIn(xl), FadeIn(yl), run_time=a)

        peak = MathTex(r"\frac{pY}{N}", color=BLUE, font_size=40).to_corner(UR, buff=0.7)
        self.play(Write(peak), run_time=b)

        saw2 = self.teeth(ax, 2)
        n2 = Text("two trips", font_size=26, color=BLUE).to_corner(UL, buff=0.6)
        self.play(Create(saw2), FadeIn(n2), run_time=c)

        avg2 = DashedLine(ax.c2p(0, 0.25), ax.c2p(1, 0.25), color=YELLOW)
        al = Text("average", font_size=22, color=YELLOW).next_to(avg2, RIGHT, buff=0.1)
        self.play(Create(avg2), FadeIn(al), run_time=d)

        saw4 = self.teeth(ax, 4)
        n4 = Text("four trips", font_size=26, color=BLUE).to_corner(UL, buff=0.6)
        self.play(Transform(saw2, saw4), Transform(n2, n4), run_time=e)

        avg4 = DashedLine(ax.c2p(0, 0.125), ax.c2p(1, 0.125), color=YELLOW)
        self.play(Transform(avg2, avg4), al.animate.next_to(avg4, RIGHT, buff=0.1), run_time=f)

        res = MathTex(r"\bar{M} = \frac{pY}{2N}", color=YELLOW, font_size=46) \
            .to_edge(DOWN, buff=0.5)
        self.play(Write(res), run_time=g)
        self.wait(h)


class BeatThree(Scene):
    """Two costs, their U-shaped sum, and the algebra of the minimum."""

    def construct(self):
        a, b, c, d, e, f, g, h, i = steps("BeatThree", 8, 10, 10, 12, 8, 12, 12, 14, 14)
        ax = Axes(x_range=[0, 10, 2], y_range=[0, 10, 2], x_length=7.2, y_length=4.4,
                  axis_config={"include_tip": False, "color": GREY}).to_edge(LEFT, buff=0.7)
        xl = Text("trips per year, N", font_size=22, color=GREY).next_to(ax.x_axis, DOWN, buff=0.2)
        self.play(Create(ax), FadeIn(xl), run_time=a)

        trip = ax.plot(lambda x: 0.8 * x, x_range=[0.4, 9.6], color=RED)
        tl = Text("cost of trips", font_size=22, color=RED).next_to(trip.get_end(), UR, buff=0.05)
        self.play(Create(trip), FadeIn(tl), run_time=b)

        forg = ax.plot(lambda x: 8.0 / x, x_range=[0.9, 9.6], color=BLUE)
        fl = Text("forgone interest", font_size=22, color=BLUE) \
            .next_to(forg.get_start(), RIGHT, buff=0.1)
        self.play(Create(forg), FadeIn(fl), run_time=c)

        tot = ax.plot(lambda x: 0.8 * x + 8.0 / x, x_range=[0.9, 9.0], color=GREEN)
        self.play(Create(tot), run_time=d)

        nstar = (8.0 / 0.8) ** 0.5
        dot = Dot(ax.c2p(nstar, 0.8 * nstar + 8.0 / nstar), color=YELLOW, radius=0.09)
        drop = DashedLine(dot.get_center(), ax.c2p(nstar, 0), color=YELLOW)
        self.play(FadeIn(dot, scale=2), Create(drop), run_time=e)

        foc = MathTex(r"pF - \frac{ipY}{2N^2} = 0", font_size=40).to_corner(UR, buff=0.8)
        self.play(Write(foc), run_time=f)

        nsol = MathTex(r"N^{*} = \sqrt{\frac{iY}{2F}}", color=YELLOW, font_size=46) \
            .next_to(foc, DOWN, buff=0.5, aligned_edge=RIGHT)
        self.play(Write(nsol), run_time=g)

        md = MathTex(r"\frac{M}{p} = \sqrt{\frac{YF}{2i}}", color=BLUE, font_size=54) \
            .next_to(nsol, DOWN, buff=0.6, aligned_edge=RIGHT)
        self.play(TransformFromCopy(nsol, md), run_time=h)
        self.play(Indicate(md, color=BLUE, scale_factor=1.15), run_time=i)


class BeatFour(Scene):
    """Log axes: the slope is the elasticity, and it is one half."""

    def construct(self):
        a, b, c, d, e, f, g, h = steps("BeatFour", 10, 12, 12, 10, 16, 14, 10, 16)
        ax = Axes(x_range=[0, 4, 1], y_range=[0, 3, 1], x_length=7.4, y_length=4.4,
                  axis_config={"include_tip": False, "color": GREY}).shift(LEFT * 1.4)
        xl = Text("log income", font_size=22, color=GREY).next_to(ax.x_axis, DOWN, buff=0.2)
        yl = Text("log real balances", font_size=22, color=GREY).rotate(PI / 2) \
            .next_to(ax.y_axis, LEFT, buff=0.2)
        self.play(Create(ax), FadeIn(xl), FadeIn(yl), run_time=a)

        bt = ax.plot(lambda x: 0.5 * x + 0.4, x_range=[0.2, 3.8], color=BLUE)
        btl = MathTex(r"\tfrac{1}{2}", color=BLUE, font_size=34) \
            .next_to(bt.get_end(), UR, buff=0.05)
        self.play(Create(bt), FadeIn(btl), run_time=b)

        p0, p1 = ax.c2p(1.6, 1.2), ax.c2p(2.6, 1.2)
        p2 = ax.c2p(2.6, 1.7)
        tri = VGroup(Line(p0, p1, color=YELLOW), Line(p1, p2, color=YELLOW))
        run = Text("1", font_size=22, color=YELLOW).next_to(Line(p0, p1), DOWN, buff=0.1)
        rise = Text("0.5", font_size=22, color=YELLOW).next_to(Line(p1, p2), RIGHT, buff=0.1)
        self.play(Create(tri), FadeIn(run), FadeIn(rise), run_time=c)

        eta = MathTex(r"\eta = \tfrac{1}{2}", color=YELLOW, font_size=52).to_corner(UR, buff=0.8)
        self.play(Write(eta), run_time=d)

        dbl = VGroup(
            Text("income doubles", font_size=24),
            Text("cash rises 41 per cent", font_size=24, color=BLUE),
            Text("you go to the bank more often instead", font_size=22, color=GREY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).next_to(eta, DOWN, buff=0.5, aligned_edge=RIGHT)
        self.play(FadeIn(dbl, shift=DOWN * 0.2), run_time=e)

        camb = ax.plot(lambda x: 1.0 * x - 0.2, x_range=[0.4, 3.2], color=RED)
        cl = Text("Cambridge: elasticity 1", font_size=22, color=RED) \
            .next_to(camb.get_end(), UL, buff=0.05)
        self.play(Create(camb), FadeIn(cl), run_time=f)

        note = Text("two different claims about behaviour, not two settings of a dial",
                    font_size=24, color=GREY).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(note), run_time=g)
        self.wait(h)


class BeatFive(Scene):
    """The ladder of monetary aggregates, and the base off to one side."""

    def construct(self):
        a, b, c, d, e, f, g = steps("BeatFive", 8, 10, 12, 14, 26, 16, 14)
        title = heading("There is no single measure of money", GREY)
        self.play(FadeIn(title), run_time=a)

        def box(label, w, colour):
            r = Rectangle(width=w, height=0.62, color=colour, fill_opacity=0.18)
            return VGroup(r, Text(label, font_size=20).move_to(r))

        cur = box("currency", 2.6, BLUE)
        dep = box("demand deposits", 3.4, BLUE)
        sav = box("savings, time, money funds", 5.0, BLUE)
        m0 = VGroup(cur).arrange(RIGHT, buff=0).shift(LEFT * 2.2 + UP * 1.1)
        m1 = VGroup(cur.copy(), dep).arrange(RIGHT, buff=0.05).next_to(m0, DOWN, buff=0.35,
                                                                      aligned_edge=LEFT)
        m2 = VGroup(cur.copy(), dep.copy(), sav).arrange(RIGHT, buff=0.05) \
            .next_to(m1, DOWN, buff=0.35, aligned_edge=LEFT)
        for grp, name in ((m0, "M0"), (m1, "M1"), (m2, "M2")):
            grp.add(Text(name, font_size=24, color=YELLOW).next_to(grp, LEFT, buff=0.25))

        self.play(FadeIn(m0, shift=RIGHT * 0.2), run_time=b)
        self.play(FadeIn(m1, shift=RIGHT * 0.2), run_time=c)
        self.play(FadeIn(m2, shift=RIGHT * 0.2), run_time=d)

        props = VGroup(*[Text("- " + s, font_size=21, color=GREY) for s in (
            "hard to counterfeit", "easy to carry", "durable",
            "divisible", "commonly accepted")]) \
            .arrange(DOWN, aligned_edge=LEFT, buff=0.14).to_corner(DR, buff=0.6)
        for p in props:
            self.play(FadeIn(p, shift=LEFT * 0.2), run_time=e / 5)

        base = box("currency + bank reserves", 4.6, GREEN).to_edge(DOWN, buff=0.6) \
            .shift(LEFT * 2.0)
        bl = Text("monetary base: a different object", font_size=22, color=GREEN) \
            .next_to(base, UP, buff=0.12)
        self.play(FadeIn(base), FadeIn(bl), run_time=f)

        q = Text("so how does a central bank control anything but the base?",
                 font_size=26, color=YELLOW).to_edge(DOWN, buff=0.15)
        self.play(FadeOut(props), FadeIn(q), run_time=g)


# ---------------------------------------------------------------- Act II

class BeatSix(Scene):
    """A bank balance sheet, and the open market operation step by step."""

    def construct(self):
        a, b, c, d, e, f, g, h = steps("BeatSix", 10, 12, 10, 14, 14, 14, 14, 12)
        title = heading("Where money comes from", GREY)
        frame = Rectangle(width=9.0, height=4.0, color=GREY)
        mid = Line(frame.get_top(), frame.get_bottom(), color=GREY)
        top = Line(frame.get_left() + UP * 1.3, frame.get_right() + UP * 1.3, color=GREY)
        heads = VGroup(Text("assets", font_size=24).move_to(frame.get_left() * 0.5 + UP * 1.65),
                       Text("liabilities", font_size=24).move_to(frame.get_right() * 0.5 + UP * 1.65))
        self.play(FadeIn(title), Create(frame), Create(mid), Create(top), FadeIn(heads), run_time=a)

        assets = VGroup(Text("reserves", font_size=22, color=YELLOW),
                        Text("bonds", font_size=22), Text("loans", font_size=22)) \
            .arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(frame.get_left() * 0.5 + DOWN * 0.3)
        self.play(FadeIn(assets), run_time=b)
        liabs = VGroup(Text("deposits", font_size=22), Text("net worth", font_size=22, color=GREY)) \
            .arrange(DOWN, aligned_edge=LEFT, buff=0.6).move_to(frame.get_right() * 0.5 + DOWN * 0.3)
        self.play(FadeIn(liabs), run_time=c)

        why = VGroup(Text("held for withdrawals, and because regulation requires it",
                          font_size=21, color=GREY),
                     Text("so banks hold as few as the rule allows", font_size=21, color=YELLOW)) \
            .arrange(DOWN, buff=0.12).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(why), run_time=d)

        plus = MathTex(r"+\,\Delta", color=GREEN, font_size=40).next_to(assets[0], RIGHT, buff=0.4)
        omo = Text("open market operation: the central bank buys bonds with new reserves",
                   font_size=21, color=GREEN).to_edge(DOWN, buff=0.5)
        self.play(FadeOut(why), FadeIn(plus), FadeIn(omo), run_time=e)

        excess = Text("excess reserves, earning nothing", font_size=21, color=RED) \
            .next_to(plus, RIGHT, buff=0.3)
        self.play(FadeIn(excess), run_time=f)

        arrow = Arrow(assets[2].get_right(), liabs[0].get_left(), color=BLUE, buff=0.3)
        lend = Text("lend, and deposits rise", font_size=21, color=BLUE) \
            .next_to(arrow, UP, buff=0.08)
        self.play(GrowArrow(arrow), FadeIn(lend), run_time=g)

        fix = VGroup(Text("the reserves did not leave", font_size=24, color=YELLOW),
                     Text("and nobody's net worth changed", font_size=21, color=GREY)) \
            .arrange(DOWN, buff=0.12).to_edge(DOWN, buff=0.4)
        self.play(FadeOut(omo), FadeIn(fix), run_time=h)


class BeatSeven(Scene):
    """Rounds of the expansion stacking into the multiplier."""

    def construct(self):
        a, b, c, d, e, f, g = steps("BeatSeven", 10, 28, 12, 18, 16, 10, 6)
        title = heading("Summing the rounds", GREY)
        ax = Axes(x_range=[0, 7, 1], y_range=[0, 1.1, 0.5], x_length=8.0, y_length=3.4,
                  axis_config={"include_tip": False, "color": GREY}).shift(DOWN * 0.4)
        self.play(FadeIn(title), Create(ax), run_time=a)

        ratio, bars = 0.55, VGroup()
        each = b / 5
        for k in range(5):
            h = ratio ** k
            bar = Rectangle(width=0.7, height=max(h * 3.4 / 1.1, 0.04),
                            color=BLUE, fill_opacity=0.65)
            bar.move_to(ax.c2p(k + 0.5, 0), aligned_edge=DOWN)
            bars.add(bar)
            self.play(GrowFromEdge(bar, DOWN), run_time=each)

        br = Brace(bars, direction=RIGHT, color=YELLOW)
        bl = Text("the sum converges", font_size=24, color=YELLOW).next_to(br, RIGHT, buff=0.1)
        self.play(GrowFromCenter(br), FadeIn(bl), run_time=c)

        mult = MathTex(r"\frac{\Delta M1}{\Delta \text{base}} = "
                       r"\frac{1}{\theta + \gamma - \theta\gamma}",
                       color=YELLOW, font_size=46).to_edge(UP, buff=1.1)
        self.play(Write(mult), run_time=d)

        roles = VGroup(
            Text("theta: the reserve ratio, a policy choice", font_size=22, color=GREEN),
            Text("gamma: the cash share, public behaviour", font_size=22, color=RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.16).to_edge(DOWN, buff=0.45)
        self.play(FadeIn(roles, shift=UP * 0.2), run_time=e)

        note = Text("one is an instrument, the other is not", font_size=22, color=GREY) \
            .to_edge(DOWN, buff=0.12)
        self.play(FadeIn(note), run_time=f)
        self.wait(g)


class BeatEight(Scene):
    """Late 2008: the base up fivefold, M1 far less, the multiplier below one."""

    def construct(self):
        a, b, c, d, e, f, g = steps("BeatEight", 10, 16, 16, 12, 24, 14, 8)
        top = Axes(x_range=[0, 6, 1], y_range=[0, 5.5, 1], x_length=8.4, y_length=2.7,
                   axis_config={"include_tip": False, "color": GREY}).shift(UP * 1.5)
        tl = Text("index, 2008 = 1", font_size=20, color=GREY).next_to(top, LEFT, buff=0.1)
        self.play(Create(top), FadeIn(tl), run_time=a)

        base = top.plot(lambda x: 1 + 0.78 * x, x_range=[0, 5.2], color=RED)
        bl = Text("monetary base", font_size=22, color=RED).next_to(base.get_end(), UR, buff=0.05)
        self.play(Create(base), FadeIn(bl), run_time=b)

        m1 = top.plot(lambda x: 1 + 0.16 * x, x_range=[0, 5.2], color=BLUE)
        ml = Text("M1", font_size=22, color=BLUE).next_to(m1.get_end(), DR, buff=0.05)
        self.play(Create(m1), FadeIn(ml), run_time=c)

        br = BraceBetweenPoints(top.c2p(5.2, 1.83), top.c2p(5.2, 5.06),
                                direction=RIGHT, color=YELLOW)
        self.play(GrowFromCenter(br), run_time=d)

        bot = Axes(x_range=[0, 6, 1], y_range=[0, 2.4, 1], x_length=8.4, y_length=2.2,
                   axis_config={"include_tip": False, "color": GREY}).shift(DOWN * 1.9)
        mult = bot.plot(lambda x: 2.05 - 0.24 * x, x_range=[0, 5.2], color=YELLOW)
        one = DashedLine(bot.c2p(0, 1), bot.c2p(5.6, 1), color=GREY)
        lab = Text("the M1 multiplier", font_size=22, color=YELLOW) \
            .next_to(bot, UP, buff=0.05).shift(LEFT * 2.4)
        self.play(Create(bot), Create(one), Create(mult), FadeIn(lab), run_time=e)

        below = Text("below one", font_size=26, color=RED).next_to(mult.get_end(), RIGHT, buff=0.15)
        self.play(FadeIn(below), Indicate(below, color=RED), run_time=f)

        why = Text("reserves stopped being the worst asset to hold",
                   font_size=24, color=GREY).to_edge(DOWN, buff=0.1)
        self.play(FadeIn(why), run_time=g)


# ---------------------------------------------------------------- Act III

class BeatNine(Scene):
    """The equilibrium condition and its three channels; two of them close."""

    def construct(self):
        a, b, c, d, e, f, g = steps("BeatNine", 12, 24, 12, 20, 12, 12, 8)
        eq = MathTex(r"M^{S}", r"=", r"m^{D}(Y, i)", r"\cdot", r"p", font_size=56).to_edge(UP, buff=1.0)
        eq[2].set_color(BLUE)
        self.play(Write(eq), run_time=a)

        labels = ["p rises", "i falls", "Y rises"]
        colours = [YELLOW, YELLOW, YELLOW]
        arrows, texts = VGroup(), VGroup()
        each = b / 3
        xs = [-4.0, 0.0, 4.0]
        for x, lab, col in zip(xs, labels, colours):
            ar = Arrow(eq.get_bottom() + DOWN * 0.1, np.array([x, -0.6, 0]), color=col, buff=0.1)
            tx = Text(lab, font_size=30, color=col).next_to(ar.get_end(), DOWN, buff=0.2)
            arrows.add(ar)
            texts.add(tx)
            self.play(GrowArrow(ar), FadeIn(tx), run_time=each)

        cl = Text("the classical view: real things are set by real forces",
                  font_size=26, color=GREY).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(cl), run_time=c)

        self.play(arrows[2].animate.set_color(GREY).set_opacity(0.3),
                  texts[2].animate.set_color(GREY).set_opacity(0.3), run_time=d / 2)
        self.play(arrows[1].animate.set_color(GREY).set_opacity(0.3),
                  texts[1].animate.set_color(GREY).set_opacity(0.3), run_time=d / 2)

        self.play(texts[0].animate.scale(1.3).set_color(YELLOW),
                  Indicate(eq[4], color=YELLOW, scale_factor=1.4), run_time=e)

        honest = Text("we did not prove neutrality; we assumed what makes it follow",
                      font_size=24, color=RED).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(honest), run_time=f)
        self.wait(g)


class BeatTen(Scene):
    """Differentiate the equilibrium condition and divide through."""

    def construct(self):
        a, b, c, d, e, f, g, h = steps("BeatTen", 8, 16, 14, 14, 12, 12, 16, 8)
        eq = MathTex(r"M^{S} = m^{D}(Y,i)\, p", font_size=46).to_edge(UP, buff=0.7)
        self.play(Write(eq), run_time=a)

        der = MathTex(r"\dot{M}^{S} =",
                      r"\left[ m^{D}_{Y}\dot{Y} + m^{D}_{i}\,\dot{i} \right] p",
                      r"+\, m^{D}\dot{p}", font_size=40).next_to(eq, DOWN, buff=0.5)
        self.play(Write(der), run_time=b)

        note = Text("now divide every term by the condition itself", font_size=24, color=YELLOW) \
            .next_to(der, DOWN, buff=0.4)
        self.play(FadeIn(note), run_time=c)

        gro = MathTex(r"\mu =", r"\underbrace{\frac{m^{D}_{Y} Y}{m^{D}}}_{\eta}\, g",
                      r"+\, \frac{m^{D}_{i}}{m^{D}}\dot{i}", r"+\, \pi",
                      font_size=42).next_to(note, DOWN, buff=0.45)
        gro[1].set_color(YELLOW)
        self.play(ReplacementTransform(der.copy(), gro), run_time=d)

        why = Text("inflation constant, so the nominal rate is constant, so its change is zero",
                   font_size=22, color=GREY).next_to(gro, DOWN, buff=0.35)
        self.play(FadeIn(why), run_time=e)

        cross = Cross(gro[2], color=RED, stroke_width=6)
        self.play(Create(cross), run_time=f)

        law = MathTex(r"\pi = \mu - \eta g", color=GREEN, font_size=64).to_edge(DOWN, buff=0.6)
        boxed = SurroundingRectangle(law, color=GREEN, buff=0.25)
        self.play(FadeOut(why), Write(law), Create(boxed), run_time=g)
        self.wait(h)



class BeatEleven(Scene):
    """The cold open resolved: the miss is one number wide."""

    def construct(self):
        a, b, c, d, e, f, g, h = steps("BeatEleven", 10, 12, 10, 16, 12, 16, 14, 10)
        law = MathTex(r"\pi = \mu - \eta g", color=GREEN, font_size=56).to_edge(UP, buff=0.7)
        self.play(Write(law), run_time=a)

        given = VGroup(MathTex(r"\pi^{*} = 2", font_size=40),
                       MathTex(r"g = 3", font_size=40)) \
            .arrange(RIGHT, buff=1.1).next_to(law, DOWN, buff=0.55)
        self.play(FadeIn(given, shift=DOWN * 0.2), run_time=b)

        belief = MathTex(r"\eta = \tfrac{1}{2}", color=YELLOW, font_size=44) \
            .next_to(given, DOWN, buff=0.45)
        self.play(Write(belief), run_time=c)

        chose = MathTex(r"\mu = 2 + \tfrac{1}{2}(3) = 3.5", color=YELLOW, font_size=46) \
            .next_to(belief, DOWN, buff=0.4)
        self.play(Write(chose), run_time=d)

        truth = MathTex(r"\text{but truly } \eta = 1", color=RED, font_size=40) \
            .next_to(chose, DOWN, buff=0.45)
        self.play(Write(truth), run_time=e)

        out = MathTex(r"\pi = 3.5 - 1(3) = 0.5", color=RED, font_size=48) \
            .next_to(truth, DOWN, buff=0.35)
        self.play(Write(out), run_time=f)

        rule = MathTex(r"\text{miss} = \Delta\eta \times g = \tfrac{1}{2}(3) = 1.5",
                       color=YELLOW, font_size=44).to_edge(DOWN, buff=0.45)
        self.play(Write(rule), run_time=g)
        self.play(Indicate(rule, color=YELLOW, scale_factor=1.12), run_time=h)


class BeatTwelve(Scene):
    """A level jump, then the subtle one: a growth-rate change makes prices jump too."""

    def construct(self):
        a, b, c, d, e, f, g, h = steps("BeatTwelve", 10, 16, 12, 8, 14, 16, 16, 8)
        ax = Axes(x_range=[0, 10, 2], y_range=[0, 6, 2], x_length=9, y_length=4.2,
                  axis_config={"include_tip": False, "color": GREY})
        yl = Text("price level", font_size=22, color=GREY).rotate(PI / 2) \
            .next_to(ax.y_axis, LEFT, buff=0.2)
        self.play(Create(ax), FadeIn(yl), run_time=a)

        flat1 = Line(ax.c2p(0, 1.5), ax.c2p(5, 1.5), color=BLUE, stroke_width=5)
        jump = DashedLine(ax.c2p(5, 1.5), ax.c2p(5, 3.0), color=YELLOW, stroke_width=5)
        flat2 = Line(ax.c2p(5, 3.0), ax.c2p(10, 3.0), color=BLUE, stroke_width=5)
        self.play(Create(flat1), run_time=b / 2)
        self.play(Create(jump), Create(flat2), run_time=b / 2)

        lab1 = Text("a one-off rise in the level of money:\nprices jump in proportion",
                    font_size=24, color=GREY, line_spacing=0.8).to_corner(UL, buff=0.6)
        self.play(FadeIn(lab1), run_time=c)
        self.play(FadeOut(VGroup(flat1, jump, flat2, lab1)), run_time=d)

        slow = ax.plot(lambda x: 1.2 * np.exp(0.09 * x), x_range=[0, 5], color=BLUE)
        self.play(Create(slow), run_time=e)

        naive = ax.plot(lambda x: 1.88 * np.exp(0.22 * (x - 5)), x_range=[5, 9.6],
                        color=RED).set_stroke(width=4, opacity=0.9)
        nl = Text("the naive answer: only the slope changes", font_size=22, color=RED) \
            .to_corner(UL, buff=0.6)
        self.play(Create(DashedVMobject(naive, num_dashes=40)), FadeIn(nl), run_time=f)

        step = DashedLine(ax.c2p(5, 1.88), ax.c2p(5, 2.55), color=GREEN, stroke_width=6)
        right = ax.plot(lambda x: 2.55 * np.exp(0.22 * (x - 5)), x_range=[5, 9.2], color=GREEN)
        gl = Text("the rate rises, so the nominal rate rises,\n"
                  "so real balances fall, so the price level must jump",
                  font_size=23, color=GREEN, line_spacing=0.8).to_edge(DOWN, buff=0.4)
        self.play(Create(step), Create(right), FadeIn(gl), run_time=g)
        self.wait(h)


class BeatThirteen(Scene):
    """The quantity equation is a definition; velocity is an implication."""

    def construct(self):
        a, b, c, d, e, f, g = steps("BeatThirteen", 12, 12, 16, 16, 18, 16, 10)
        qe = MathTex(r"M \cdot V = p \cdot Y", font_size=64).to_edge(UP, buff=0.9)
        self.play(Write(qe), run_time=a)

        stamp = Text("DEFINITION", font_size=34, color=GREY).next_to(qe, DOWN, buff=0.3)
        box = SurroundingRectangle(stamp, color=GREY, buff=0.14)
        self.play(FadeIn(stamp, scale=1.4), Create(box), run_time=b)

        why = VGroup(
            Text("velocity is defined as nominal output over the money stock", font_size=24),
            Text("so it holds for any data, anywhere, always", font_size=24, color=GREY),
            Text("an equation that cannot fail is not evidence", font_size=26, color=RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).next_to(box, DOWN, buff=0.45)
        self.play(FadeIn(why[0]), run_time=c / 3)
        self.play(FadeIn(why[1]), run_time=c / 3)
        self.play(FadeIn(why[2]), run_time=c / 3)

        self.play(FadeOut(VGroup(why, stamp, box)), run_time=d / 4)
        vdef = MathTex(r"V = \frac{Y}{m^{D}(Y,i)}", color=BLUE, font_size=52) \
            .next_to(qe, DOWN, buff=0.6)
        self.play(Write(vdef), run_time=d * 3 / 4)

        sub = MathTex(r"V = \sqrt{\frac{2iY}{F}}", color=BLUE, font_size=56) \
            .next_to(vdef, DOWN, buff=0.5)
        self.play(TransformFromCopy(vdef, sub), run_time=e)

        signs = VGroup(
            Text("rises with the interest rate", font_size=23, color=YELLOW),
            Text("rises with output", font_size=23, color=YELLOW),
            Text("falls with the cost of a trip", font_size=23, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14).to_corner(DR, buff=0.6)
        self.play(FadeIn(signs, shift=LEFT * 0.2), run_time=f)

        pivot = Text("so the assumption that makes it a theory is false here",
                     font_size=25, color=RED).to_edge(DOWN, buff=0.2)
        self.play(FadeIn(pivot), run_time=g)


# ---------------------------------------------------------------- Act IV

class BeatFourteen(Scene):
    """Two indices, computed, and one price falling while the index rises."""

    def construct(self):
        a, b, c, d, e, f, g = steps("BeatFourteen", 8, 22, 14, 10, 26, 12, 8)
        title = heading("Two ways to weight a basket", GREY)
        self.play(FadeIn(title), run_time=a)

        defl = VGroup(
            MathTex(r"\text{deflator} = \frac{\text{nominal}}{\text{real}} \times 100",
                    font_size=40),
            MathTex(r"= \frac{1860}{2550} \times 100 \approx 73", font_size=40),
            MathTex(r"\pi \approx -27\%", color=RED, font_size=40),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.6)
        self.play(Write(defl[0]), run_time=b / 2)
        self.play(Write(defl[1]), run_time=b / 2)
        self.play(Write(defl[2]), run_time=c)
        w = Text("weights goods by how much is produced", font_size=22, color=GREY) \
            .next_to(defl, DOWN, buff=0.35)
        self.play(FadeIn(w), run_time=d)
        self.play(FadeOut(VGroup(defl, w)), run_time=e / 6)

        rows = VGroup(
            VGroup(Text("cars", font_size=24), Text("100", font_size=24),
                   Text("115", font_size=24, color=GREEN)),
            VGroup(Text("caviar", font_size=24), Text("4", font_size=24),
                   Text("3", font_size=24, color=RED)),
            VGroup(Text("champagne", font_size=24), Text("2", font_size=24),
                   Text("4", font_size=24, color=GREEN)),
        )
        for r in rows:
            r.arrange(RIGHT, buff=1.3)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(UP * 0.4)
        self.play(FadeIn(rows), run_time=e * 5 / 6)

        tot = VGroup(MathTex(r"300 \;\longrightarrow\; 330", font_size=44),
                     MathTex(r"\text{index } 100 \longrightarrow 110", font_size=38),
                     MathTex(r"\pi = 10\%", color=YELLOW, font_size=44)) \
            .arrange(DOWN, buff=0.25).next_to(rows, DOWN, buff=0.5)
        self.play(Write(tot), run_time=f)

        note = Text("caviar fell, and the index still rose by ten per cent",
                    font_size=25, color=RED).to_edge(DOWN, buff=0.2)
        self.play(FadeIn(note), Indicate(rows[1][2], color=RED), run_time=g)


class BeatFifteen(Scene):
    """The real rate, counted in goods."""

    def construct(self):
        a, b, c, d, e, f, g = steps("BeatFifteen", 10, 20, 14, 18, 14, 16, 8)
        line = Line(LEFT * 5, RIGHT * 5, color=GREY).shift(UP * 1.6)
        t0 = VGroup(Dot(LEFT * 4 + UP * 1.6, color=GREY),
                    Text("today", font_size=22, color=GREY).next_to(LEFT * 4 + UP * 1.6, UP, buff=0.15))
        t1 = VGroup(Dot(RIGHT * 4 + UP * 1.6, color=GREY),
                    Text("one year", font_size=22, color=GREY)
                    .next_to(RIGHT * 4 + UP * 1.6, UP, buff=0.15))
        self.play(Create(line), FadeIn(t0), FadeIn(t1), run_time=a)

        money = VGroup(Text("100 dollars", font_size=28).next_to(t0, DOWN, buff=0.6),
                       Text("111 dollars", font_size=28).next_to(t1, DOWN, buff=0.6))
        self.play(FadeIn(money[0]), run_time=b / 2)
        self.play(FadeIn(money[1]), run_time=b / 2)

        idx = VGroup(Text("index 100", font_size=22, color=GREY).next_to(money[0], DOWN, buff=0.3),
                     Text("index 102", font_size=22, color=GREY).next_to(money[1], DOWN, buff=0.3))
        self.play(FadeIn(idx), run_time=c)

        goods = VGroup(Text("1 basket", font_size=28, color=BLUE).next_to(idx[0], DOWN, buff=0.5),
                       Text("1.088 baskets", font_size=28, color=BLUE)
                       .next_to(idx[1], DOWN, buff=0.5))
        self.play(FadeIn(goods[0]), run_time=d / 2)
        self.play(FadeIn(goods[1]), run_time=d / 2)

        rr = MathTex(r"r \approx 8.8\%", color=YELLOW, font_size=48).to_edge(DOWN, buff=1.2)
        self.play(Write(rr), run_time=e)

        fml = VGroup(MathTex(r"1 + r = \frac{1+i}{1+\pi}", font_size=40),
                     MathTex(r"r \approx i - \pi", color=GREY, font_size=36)) \
            .arrange(RIGHT, buff=1.0).to_edge(DOWN, buff=0.4)
        self.play(Write(fml), run_time=f)
        warn = Text("the subtraction is an approximation; it fails at high inflation",
                    font_size=21, color=RED).to_edge(DOWN, buff=0.1)
        self.play(FadeIn(warn), run_time=g)


class BeatSixteen(Scene):
    """The evidence, the outlier that hides it, and the law recovered."""

    def construct(self):
        a, b, c, d, e, f, g, h, i = steps("BeatSixteen", 8, 14, 12, 10, 12, 18, 8, 12, 6)
        pts = scatter_data()
        ax = Axes(x_range=[0, 4000, 1000], y_range=[0, 1400, 400], x_length=8.4, y_length=4.2,
                  axis_config={"include_tip": False, "color": GREY,
                               "font_size": 18}).add_coordinates()
        xl = Text("average money growth, per cent", font_size=20, color=GREY) \
            .next_to(ax.x_axis, DOWN, buff=0.3)
        yl = Text("average inflation", font_size=20, color=GREY).rotate(PI / 2) \
            .next_to(ax.y_axis, LEFT, buff=0.2)
        self.play(Create(ax), FadeIn(xl), FadeIn(yl), run_time=a)

        dots = VGroup(*[Dot(ax.c2p(x, y), radius=0.045, color=BLUE) for x, y, _ in pts])
        self.play(LaggedStartMap(FadeIn, dots, lag_ratio=0.01), run_time=b)

        s, c0, r = ols([(p[0], p[1]) for p in pts])
        fit = ax.plot(lambda x: c0 + s * x, x_range=[0, 3900], color=RED)
        stats = VGroup(Text(f"slope {s:.2f}", font_size=26, color=RED),
                       Text(f"correlation {r:.2f}", font_size=26, color=RED)) \
            .arrange(DOWN, aligned_edge=LEFT, buff=0.12).to_corner(UR, buff=0.7)
        self.play(Create(fit), FadeIn(stats), run_time=c)

        verdict = Text("the theory looks refuted", font_size=28, color=RED) \
            .next_to(stats, DOWN, buff=0.3, aligned_edge=RIGHT)
        self.play(FadeIn(verdict), run_time=d)

        sl = max(pts, key=lambda p: p[0])
        ring = Circle(radius=0.3, color=YELLOW).move_to(ax.c2p(sl[0], sl[1]))
        slab = Text(f"{sl[2]}: {sl[0]:.0f} per cent", font_size=24, color=YELLOW) \
            .next_to(ring, UP, buff=0.2)
        self.play(Create(ring), FadeIn(slab), run_time=e)

        series = [74, 76, 33, 22, 9, 20, 30, 47, 11, 38, 12, 131119, 29, 22, 20, 31, 22, 17,
                  27, 35, 24, 30, 22, 11, 24, -99.89, 18, 7, 14, 14, 38, 22, 42, 33]
        inset = Axes(x_range=[0, 34, 10], y_range=[-100, 200, 100], x_length=5.0, y_length=2.2,
                     axis_config={"include_tip": False, "color": GREY, "font_size": 16})
        inset.to_corner(DL, buff=0.5)
        bg = BackgroundRectangle(inset, color=BLACK, fill_opacity=0.85, buff=0.25)
        normal = VGroup(*[Dot(inset.c2p(k, min(v, 195)), radius=0.035,
                             color=RED if abs(v) > 200 or v < -90 else BLUE)
                          for k, v in enumerate(series)])
        itxt = Text("its annual series: 7 to 76 per cent, except two years",
                    font_size=19, color=GREY).next_to(bg, UP, buff=0.1)
        self.play(FadeIn(bg), Create(inset), FadeIn(normal), FadeIn(itxt), run_time=f)

        bad = VGroup(Text("131,119", font_size=20, color=RED),
                     Text("-99.89", font_size=20, color=RED)) \
            .arrange(RIGHT, buff=0.6).next_to(inset, UP, buff=0.02)
        self.play(FadeIn(bad), run_time=g)

        keep = [p for p in pts if p[0] < 100 and p[1] < 100]
        s2, c2, r2 = ols([(p[0], p[1]) for p in keep])
        ax2 = Axes(x_range=[0, 100, 25], y_range=[0, 100, 25], x_length=8.4, y_length=4.2,
                   axis_config={"include_tip": False, "color": GREY,
                                "font_size": 18}).add_coordinates()
        dots2 = VGroup(*[Dot(ax2.c2p(x, y), radius=0.045, color=BLUE) for x, y, _ in keep])
        fit2 = ax2.plot(lambda x: c2 + s2 * x, x_range=[0, 98], color=GREEN)
        stats2 = VGroup(Text(f"slope {s2:.2f}", font_size=28, color=GREEN),
                        Text(f"correlation {r2:.2f}", font_size=28, color=GREEN)) \
            .arrange(DOWN, aligned_edge=LEFT, buff=0.12).to_corner(UR, buff=0.7)
        self.play(FadeOut(VGroup(bg, inset, normal, itxt, bad, ring, slab, verdict)),
                  ReplacementTransform(VGroup(ax, dots, fit), VGroup(ax2, dots2, fit2)),
                  ReplacementTransform(stats, stats2), run_time=h)
        self.wait(i)


class BeatSeventeen(Scene):
    """Brazil: IPCA and the Selic target on one time axis."""

    def construct(self):
        a, b, c, d, e, f = steps("BeatSeventeen", 12, 20, 20, 14, 20, 14)
        ipca = [(i, float(r["value"])) for i, r in enumerate(load_csv("bcb_sgs_13522.csv"))]
        selic = load_csv("bcb_sgs_432.csv")
        sel = [(i * len(ipca) / len(selic), float(r["value"])) for i, r in enumerate(selic)]

        ax = Axes(x_range=[0, len(ipca), 60], y_range=[0, 30, 10], x_length=9.2, y_length=4.4,
                  axis_config={"include_tip": False, "color": GREY, "font_size": 18})
        yl = Text("per cent per year", font_size=20, color=GREY).rotate(PI / 2) \
            .next_to(ax.y_axis, LEFT, buff=0.15)
        xl = Text("2000 to 2026", font_size=20, color=GREY).next_to(ax.x_axis, DOWN, buff=0.25)
        self.play(Create(ax), FadeIn(yl), FadeIn(xl), run_time=a)

        ip = VMobject(color=BLUE, stroke_width=4).set_points_as_corners(
            [ax.c2p(x, min(y, 29)) for x, y in ipca])
        ipl = Text("IPCA, twelve months", font_size=22, color=BLUE).to_corner(UL, buff=0.7)
        self.play(Create(ip), FadeIn(ipl), run_time=b)

        se = VMobject(color=YELLOW, stroke_width=4).set_points_as_corners(
            [ax.c2p(x, min(y, 29)) for x, y in sel])
        sel_l = Text("Selic target", font_size=22, color=YELLOW) \
            .next_to(ipl, DOWN, buff=0.15, aligned_edge=LEFT)
        self.play(Create(se), FadeIn(sel_l), run_time=c)

        rng = Text("from 2 to 26.5 per cent", font_size=22, color=GREY).to_corner(UR, buff=0.7)
        self.play(FadeIn(rng), run_time=d)

        call = VGroup(
            Text("the nominal rate is the opportunity cost of holding money",
                 font_size=24, color=YELLOW),
            Text("so a high Selic means more trips to the bank, and real resources burned",
                 font_size=22, color=GREY),
        ).arrange(DOWN, buff=0.14).to_edge(DOWN, buff=0.45)
        self.play(FadeIn(call), run_time=e)

        omit = Text("no Brazilian monetary aggregate here: I could not verify which series is which",
                    font_size=19, color=RED).to_edge(DOWN, buff=0.12)
        self.play(FadeIn(omit), run_time=f)


# ---------------------------------------------------------------- Act V

class BeatEighteen(Scene):
    """Seigniorage, the inflation tax, and the hump."""

    def construct(self):
        a, b, c, d, e, f, g = steps("BeatEighteen", 16, 12, 14, 14, 22, 14, 8)
        gbc = MathTex(r"B_{t+1} + p_t \tau_t + \left(M^{B}_{t+1} - M^{B}_{t}\right)",
                      r"=", r"p_t G_t + (1+i_t) B_t", font_size=38).to_edge(UP, buff=0.7)
        gbc[0].set_color(BLUE)
        self.play(Write(gbc), run_time=a)

        note = Text("the base sits where debt sits, except it pays no interest",
                    font_size=25, color=YELLOW).next_to(gbc, DOWN, buff=0.4)
        self.play(FadeIn(note), run_time=b)

        who = VGroup(Text("so who pays?", font_size=26),
                     Text("everyone holding money, as it loses value", font_size=26, color=RED)) \
            .arrange(DOWN, buff=0.14).next_to(note, DOWN, buff=0.4)
        self.play(FadeIn(who[0]), run_time=c / 2)
        self.play(FadeIn(who[1]), run_time=c / 2)

        tax = VGroup(Text("rate: how fast money loses value", font_size=22, color=GREY),
                     Text("base: real money balances", font_size=22, color=BLUE)) \
            .arrange(DOWN, aligned_edge=LEFT, buff=0.12).next_to(who, DOWN, buff=0.35)
        self.play(FadeIn(tax), run_time=d)

        self.play(FadeOut(VGroup(gbc, note, who, tax)), run_time=e / 8)
        ax = Axes(x_range=[0, 10, 2], y_range=[0, 3, 1], x_length=8.4, y_length=4.0,
                  axis_config={"include_tip": False, "color": GREY})
        xl = Text("inflation", font_size=22, color=GREY).next_to(ax.x_axis, DOWN, buff=0.2)
        yl = Text("seigniorage revenue", font_size=22, color=GREY).rotate(PI / 2) \
            .next_to(ax.y_axis, LEFT, buff=0.2)
        hump = ax.plot(lambda x: 2.7 * x * np.exp(-0.32 * x), x_range=[0.05, 9.8], color=GREEN)
        self.play(Create(ax), FadeIn(xl), FadeIn(yl), Create(hump), run_time=e * 7 / 8)

        peak = Dot(ax.c2p(1 / 0.32, 2.7 * (1 / 0.32) * np.exp(-1)), color=YELLOW, radius=0.09)
        pl = Text("past here, more inflation collects less", font_size=23, color=YELLOW) \
            .next_to(peak, UR, buff=0.15)
        self.play(FadeIn(peak, scale=2), FadeIn(pl), run_time=f)

        why = Text("the rate went up, and the base shrank faster",
                   font_size=24, color=RED).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(why), run_time=g)


class BeatNineteen(Scene):
    """Four costs, and two of them disagree about the optimum."""

    def construct(self):
        a, b, c, d, e, f, g = steps("BeatNineteen", 14, 12, 14, 16, 18, 16, 10)
        cost = MathTex(r"\text{cost} = N^{*}F = \sqrt{\frac{(r+\pi)\,YF}{2}}",
                       color=BLUE, font_size=48).to_edge(UP, buff=0.8)
        self.play(Write(cost), run_time=a)
        sl = Text("shoe leather: it rises with inflation, through the nominal rate",
                  font_size=23, color=GREY).next_to(cost, DOWN, buff=0.3)
        self.play(FadeIn(sl), run_time=b)

        arg = Text("the author's father, Argentina, late 1980s:\n"
                   "to the bank twice a day, to hold exactly one day of cash",
                   font_size=22, color=YELLOW, line_spacing=0.8).next_to(sl, DOWN, buff=0.35)
        self.play(FadeIn(arg), run_time=c)

        self.play(FadeOut(VGroup(sl, arg)), run_time=d / 6)
        ax = NumberLine(x_range=[-4, 4, 2], length=9, color=GREY, include_numbers=True,
                        font_size=22).shift(DOWN * 0.6)
        axl = Text("inflation rate", font_size=22, color=GREY).next_to(ax, DOWN, buff=0.25)
        self.play(Create(ax), FadeIn(axl), run_time=d * 5 / 6)

        fr_pt = ax.number_to_point(-2)
        mc_pt = ax.number_to_point(0)
        fr = VGroup(Arrow(fr_pt + UP * 1.3, fr_pt + UP * 0.15, color=BLUE, buff=0),
                    Text("Friedman rule\ni = 0, so inflation = minus r", font_size=21,
                         color=BLUE, line_spacing=0.8).move_to(fr_pt + UP * 2.0))
        mc = VGroup(Arrow(mc_pt + DOWN * 1.3, mc_pt + DOWN * 0.15, color=RED, buff=0),
                    Text("menu costs\nzero inflation", font_size=21, color=RED,
                         line_spacing=0.8).move_to(mc_pt + DOWN * 2.0))
        self.play(FadeIn(fr), run_time=e / 2)
        self.play(FadeIn(mc), run_time=e / 2)

        conflict = Text("two costs, two different optima, and the chapter does not resolve it",
                        font_size=24, color=YELLOW).to_edge(UP, buff=2.2)
        self.play(FadeIn(conflict), run_time=f)

        more = VGroup(Text("and two more: relative prices become a ruler that changes size,",
                           font_size=21, color=GREY),
                      Text("and banks earn seigniorage too, drawing resources into banking",
                           font_size=21, color=GREY)) \
            .arrange(DOWN, buff=0.1).to_edge(DOWN, buff=0.1)
        self.play(FadeIn(more), run_time=g)


class BeatTwenty(Scene):
    """Neutral but not superneutral, the seam, and the closing frame."""

    def construct(self):
        a, b, c, d, e, f, g = steps("BeatTwenty", 12, 26, 10, 14, 14, 12, 12)
        two = VGroup(
            Text("change the LEVEL of money: nothing real happens", font_size=28, color=GREEN),
            Text("change the GROWTH RATE: something real happens", font_size=28, color=RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).to_edge(UP, buff=0.8)
        self.play(FadeIn(two[0]), FadeIn(two[1]), run_time=a)

        chain = VGroup(*[Text(s, font_size=23) for s in (
            "faster money growth",
            "higher inflation",
            "higher nominal rate",
            "smaller real balances",
            "more trips, real resources burned")])
        chain.arrange(DOWN, buff=0.22).next_to(two, DOWN, buff=0.45)
        each = b / 5
        for item in chain:
            self.play(FadeIn(item, shift=RIGHT * 0.25), run_time=each)

        rec = Text("neutral, and not superneutral", font_size=28, color=YELLOW) \
            .next_to(chain, DOWN, buff=0.3)
        self.play(FadeIn(rec), run_time=c)

        self.play(FadeOut(VGroup(two, chain, rec)), run_time=d / 6)
        removed = Text("now take away the one assumption: prices can move",
                       font_size=28, color=RED).to_edge(UP, buff=0.9)
        eq = MathTex(r"M^{S} = m^{D}(Y, i)\,\cdot\, \bar{p}", font_size=48) \
            .next_to(removed, DOWN, buff=0.5)
        self.play(FadeIn(removed), Write(eq), run_time=d * 5 / 6)

        left = VGroup(Text("the price level is frozen", font_size=24, color=GREY),
                      Text("so the interest rate, or output, must clear it", font_size=26,
                           color=YELLOW),
                      Text("output. money would stop being neutral.", font_size=26, color=RED)) \
            .arrange(DOWN, buff=0.18).next_to(eq, DOWN, buff=0.45)
        self.play(FadeIn(left), run_time=e)

        seam = Text("this chapter has no mechanism for that. the next two lectures do.",
                    font_size=23, color=GREY).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(seam), run_time=f)

        self.play(FadeOut(VGroup(removed, eq, left, seam)), run_time=g / 8)
        law = MathTex(r"\pi = \mu - \eta g", color=GREEN, font_size=84)
        nums = VGroup(Text("target 2", font_size=26, color=GREY),
                      Text("growth 3", font_size=26, color=GREY),
                      Text("money growth 3.5", font_size=26, color=GREY),
                      Text("realised 0.5", font_size=26, color=RED)) \
            .arrange(RIGHT, buff=0.7).next_to(law, DOWN, buff=0.6)
        eta = VGroup(MathTex(r"\eta = \tfrac{1}{2}", color=YELLOW, font_size=44),
                     Text("Baumol-Tobin", font_size=22, color=YELLOW)) \
            .arrange(DOWN, buff=0.12).to_corner(DR, buff=0.7)
        self.play(Write(law), FadeIn(nums), FadeIn(eta), run_time=g * 7 / 8)
