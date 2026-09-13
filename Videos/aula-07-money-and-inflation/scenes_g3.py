"""Scenes for aula-07-money-and-inflation (group g3).

Durations come from beats.json via the kit. Do not hard-code seconds.
Render: python -m manim render -ql --media_dir media scenes_g3.py BeatX
"""
import numpy as np
from manim import *

from video_explainer import (Beat, Stage, axes_panel, balance_sheet, bullets, eq, note,
                       ols, palette, read_csv, sawtooth, scatter, series, table,
                       title, FAST, NORMAL, SLOW)


class BeatEleven(Scene):
    """The cold open resolved: the miss is the elasticity error times growth."""

    @staticmethod
    def _stack(items, slot, buff=0.34):
        """Pre-arrange rows inside a slot so they can be revealed one at a time."""
        g = VGroup(*items).arrange(DOWN, aligned_edge=LEFT, buff=buff)
        Stage.fit(g, slot)
        return items

    def construct(self):
        st = Stage(self)
        b = Beat(self, "BeatEleven")

        law = eq(r"\pi = \mu - \eta g", size=42, colour=GREEN)

        bank = self._stack([
            eq(r"\text{target}\;\; \pi^{*} = 2\%", 30),
            eq(r"\text{growth}\;\; g = 3\%", 30),
            eq(r"\text{believed}\;\; \hat{\eta} = \tfrac{1}{2}", 30, YELLOW),
            eq(r"\mu = \pi^{*} + \hat{\eta}\, g", 30),
            eq(r"\mu = 2 + \tfrac{1}{2}(3)", 30),
            eq(r"\mu = 3.5\%", 34, YELLOW),
            eq(r"\text{had the belief held: } 3.5 - \tfrac{1}{2}(3) = 2", 22, GREEN),
        ], "left")

        truth = self._stack([
            eq(r"\text{but truly}\;\; \eta = 1", 30, RED),
            eq(r"\pi = 3.5 - 1(3)", 30),
            eq(r"\pi = 0.5\%", 36, RED),
        ], "right", buff=0.5)

        # the payoff chart: the same gap the video opened with
        ax, panel = axes_panel([0, 8, 2], [0, 4, 1], x_label="years",
                               y_label="inflation, per cent", width=5.0, height=3.1)
        Stage.fit(panel, "left")
        target = DashedLine(ax.c2p(0, 2), ax.c2p(8, 2), color=GREY, stroke_width=4)
        tlab = Text("target 2%", font_size=16, color=GREY) \
            .next_to(ax.c2p(1.2, 2), UP, buff=0.10)
        got = Line(ax.c2p(0, 0.5), ax.c2p(8, 0.5), color=RED, stroke_width=5)
        glab = Text("realised 0.5%", font_size=16, color=RED) \
            .next_to(ax.c2p(1.4, 0.5), UP, buff=0.10)
        gap = DoubleArrow(ax.c2p(4.3, 0.5), ax.c2p(4.3, 2.0), color=YELLOW,
                          buff=0, stroke_width=3, tip_length=0.13)
        gaplab = Text("1.5 points short", font_size=16, color=YELLOW) \
            .next_to(gap, RIGHT, buff=0.12)

        decomp = self._stack([
            eq(r"\text{assumed } \tfrac{1}{2}, \text{ truth } 1", 26),
            eq(r"\Delta\eta = 1 - \tfrac{1}{2} = \tfrac{1}{2}", 30, YELLOW),
            eq(r"\Delta\pi = -\,\Delta\eta \times g", 32, YELLOW),
            eq(r"= -\tfrac{1}{2}(3) = -1.5 \text{ points}", 28, RED),
        ], "right", buff=0.45)

        # ---- the bank's own calculation
        b.step(st.show("title", title("Back to the miss")), t=0.6, hold=1)
        b.step(st.show("title", law), t=0.9, hold=2)
        b.step(st.add_to("left", bank[0]), t=0.7, hold=1.5)
        b.step(st.add_to("left", bank[1]), t=0.7, hold=1.5)
        b.step(st.add_to("left", bank[2]), t=0.8, hold=2)
        b.step(st.add_to("left", bank[3]), t=0.9, hold=2)
        b.step(st.add_to("left", bank[4]), t=0.8, hold=1.5)
        b.step(st.add_to("left", bank[5]), t=0.8, hold=2)
        b.step(st.add_to("left", bank[6]), t=0.9, hold=2.5)
        # ---- the same formula, run with the truth
        b.step(st.add_to("right", truth[0]), t=0.9, hold=2.5)
        b.step(st.add_to("right", truth[1]), t=0.8, hold=2)
        b.step(st.add_to("right", truth[2]), t=0.8, hold=2)
        b.step(st.show("note", note("two per cent was the target; half of one per cent arrived")),
               t=0.8, hold=2.5)
        # ---- the gap, drawn, then decomposed
        b.step(st.clear("left", "right", "note") + st.show("left", panel, fit=False),
               t=1.0, hold=1)
        b.step(st.add_to("left", VGroup(target, tlab)), t=0.8, hold=1.5)
        b.step(st.add_to("left", VGroup(got, glab)), t=0.8, hold=2)
        b.step(st.add_to("left", VGroup(gap, gaplab)), t=0.8, hold=2)
        b.step(st.add_to("right", decomp[0]), t=0.8, hold=2)
        b.step(st.add_to("right", decomp[1]), t=0.8, hold=2)
        b.step(st.add_to("right", decomp[2]), t=0.9, hold=2.5)
        b.step(st.add_to("right", decomp[3]), t=0.9, hold=2)
        b.step(st.show("note", note("under-estimate eta and the economy absorbs more money, "
                                    "so inflation comes in too low, not too high")),
               t=0.9, hold=3.5)
        b.step(st.show("note", note("perfect control of the money stock does not buy control "
                                    "of inflation: eta is unobserved and keeps moving", RED)),
               t=0.9, hold=3)
        b.step(st.show("note", note("put 2008 next to this and you have the case for "
                                    "targeting an interest rate instead")),
               t=0.9, hold=3)
        b.run()


class BeatTwelve(Scene):
    """A one-off level change, then the subtle one: a growth-rate change jumps p too."""

    @staticmethod
    def _stack(items, slot, buff=0.34):
        g = VGroup(*items).arrange(DOWN, aligned_edge=LEFT, buff=buff)
        Stage.fit(g, slot)
        return items

    def construct(self):
        st = Stage(self)
        b = Beat(self, "BeatTwelve")

        # ---------- experiment one: the level of M
        axm, panm = axes_panel([0, 10, 5], [0, 4, 1], x_label="time",
                               y_label="money supply M", width=4.9, height=2.9)
        Stage.fit(panm, "left")
        m_flat = Line(axm.c2p(0, 1.5), axm.c2p(5, 1.5), color=YELLOW, stroke_width=5)
        m_step = DashedLine(axm.c2p(5, 1.5), axm.c2p(5, 3.0), color=YELLOW, stroke_width=4)
        m_new = Line(axm.c2p(5, 3.0), axm.c2p(10, 3.0), color=YELLOW, stroke_width=5)
        m_lab = Text("once, and for good", font_size=15, color=YELLOW) \
            .next_to(axm.c2p(5.3, 3.55), RIGHT, buff=0.02)

        axp, panp = axes_panel([0, 10, 5], [0, 4, 1], x_label="time",
                               y_label="price level p", width=4.9, height=2.9)
        Stage.fit(panp, "right")
        p_flat = Line(axp.c2p(0, 1.5), axp.c2p(5, 1.5), color=BLUE, stroke_width=5)
        p_step = DashedLine(axp.c2p(5, 1.5), axp.c2p(5, 3.0), color=GREEN, stroke_width=5)
        p_new = Line(axp.c2p(5, 3.0), axp.c2p(10, 3.0), color=GREEN, stroke_width=5)
        p_lab = Text("same proportion", font_size=15, color=GREEN) \
            .next_to(axp.c2p(5.3, 3.55), RIGHT, buff=0.02)

        # ---------- experiment two: the growth rate of M
        axl, panl = axes_panel([0, 10, 5], [0, 6, 2], x_label="time",
                               y_label="price level, log scale", width=5.0, height=3.1)
        Stage.fit(panl, "left")
        base = Line(axl.c2p(0, 1.0), axl.c2p(5, 2.5), color=BLUE, stroke_width=5)
        mark = DashedLine(axl.c2p(5, 0), axl.c2p(5, 2.3), color=GREY, stroke_width=2)
        mark_lab = Text("mu rises here", font_size=15, color=YELLOW) \
            .next_to(axl.c2p(5.15, 0.75), RIGHT, buff=0.02)
        naive = DashedVMobject(Line(axl.c2p(5, 2.5), axl.c2p(9.5, 5.2),
                                    color=RED, stroke_width=4), num_dashes=24)
        naive_lab = Text("naive: a kink only", font_size=15, color=RED) \
            .move_to(axl.c2p(7.6, 3.1))
        jump = DashedLine(axl.c2p(5, 2.5), axl.c2p(5, 3.3), color=GREEN, stroke_width=6)
        right_path = Line(axl.c2p(5, 3.3), axl.c2p(8.6, 5.46), color=GREEN, stroke_width=5)
        right_lab = Text("a step, then the kink", font_size=15, color=GREEN) \
            .move_to(axl.c2p(5.0, 5.6), aligned_edge=LEFT)

        chain = self._stack([
            eq(r"\text{not wrong, but incomplete}", 26, RED),
            eq(r"\pi \uparrow \;\Rightarrow\; i = r + \pi \;\uparrow", 28),
            eq(r"i \uparrow \;\Rightarrow\; m^{D}(Y,i) \;\downarrow", 28, BLUE),
            eq(r"\text{yet the level of } M \text{ has not moved}", 24, YELLOW),
            eq(r"p = M \big/ m^{D} \;\text{ must jump}", 28, GREEN),
        ], "right", buff=0.45)

        b.step(st.show("title", title("Two experiments")), t=0.6, hold=1)
        b.step(st.show("note", note("the second one is the subtlest thing in the chapter")),
               t=0.7, hold=1.5)
        b.step(st.show("title", title("Experiment one: the level of M rises once", YELLOW)),
               t=0.7, hold=1.2)
        b.step(st.show("left", panm, fit=False), t=0.9, hold=1)
        b.step(st.add_to("left", m_flat), t=0.8, hold=1.5)
        b.step(st.add_to("left", VGroup(m_step, m_new, m_lab)), t=1.0, hold=2)
        b.step(st.show("note", eq(r"p = M \big/ m^{D}(Y,i)", 34)), t=0.9, hold=2)
        b.step(st.show("note", note("a bigger numerator, the same denominator")), t=0.7, hold=2)
        b.step(st.show("note", eq(r"p' / p = M' / M", 36, GREEN)), t=0.9, hold=2.5)
        b.step(st.show("right", panp, fit=False), t=0.9, hold=1)
        b.step(st.add_to("right", p_flat), t=0.8, hold=1.5)
        b.step(st.add_to("right", VGroup(p_step, p_new, p_lab)), t=1.0, hold=2)
        b.step(st.show("note", note("prices jump once, in exact proportion: "
                                    "nothing real happens", GREEN)), t=0.8, hold=2.5)
        b.step(st.show("note", note("everyone holds more money than they want, "
                                    "so everyone tries to spend it down")), t=0.8, hold=2.5)
        b.step(st.show("note", note("but somebody has to hold it: they cannot all succeed",
                                    RED)), t=0.8, hold=2.5)
        b.step(st.show("note", note("so money loses value, and that is what a higher p is")),
               t=0.8, hold=2.5)
        # ---------- experiment two
        b.step(st.clear("left", "right", "note")
               + st.show("title", title("Experiment two: the growth rate of M rises", YELLOW)),
               t=0.8, hold=1)
        b.step(st.show("left", panl, fit=False), t=0.9, hold=1)
        b.step(st.add_to("left", base), t=0.9, hold=1.5)
        b.step(st.add_to("left", VGroup(mark, mark_lab)), t=0.8, hold=1.5)
        b.step(st.add_to("left", VGroup(naive, naive_lab)), t=1.0, hold=2)
        b.step(st.add_to("right", chain[0]), t=0.8, hold=2)
        b.step(st.add_to("right", chain[1]), t=0.8, hold=2)
        b.step(st.add_to("right", chain[2]), t=0.8, hold=2)
        b.step(st.add_to("right", chain[3]), t=0.8, hold=2)
        b.step(st.add_to("right", chain[4]), t=0.9, hold=2)
        b.step(st.add_to("left", VGroup(jump, right_path, right_lab)), t=1.1, hold=2.5)
        b.step(st.show("note", note("a kink and a step: the naive answer is incomplete, "
                                    "not wrong", GREEN)), t=0.9, hold=3)
        b.run()


class BeatThirteen(Scene):
    """The quantity equation is a definition; velocity is whatever money demand says."""

    @staticmethod
    def _stack(items, slot, buff=0.34):
        g = VGroup(*items).arrange(DOWN, aligned_edge=LEFT, buff=buff)
        Stage.fit(g, slot)
        return items

    def construct(self):
        st = Stage(self)
        b = Beat(self, "BeatThirteen")

        example = table(["the two-dollar economy", "value"],
                        [("money stock M", "2"),
                         ("nominal output p Y", "6"),
                         ("times each dollar was used", "3")],
                        col_widths=[5.2, 2.0], font_size=22,
                        cell_colours={(2, 1): YELLOW})

        ident = self._stack([
            eq(r"V \;\equiv\; \frac{p\,Y}{M} \qquad \text{(a definition)}", 32),
            eq(r"M \cdot \frac{p\,Y}{M} = p\,Y \quad \text{for any data, always}", 26, GREY),
        ], "left", buff=0.65)

        theory = self._stack([
            eq(r"\text{identity:}\;\; M V = p Y", 26),
            eq(r"+\;\; \text{assumption:}\;\; V \text{ constant}", 26, YELLOW),
            eq(r"\Rightarrow\;\; p = \frac{\bar{V}}{Y}\, M", 30, GREEN),
            eq(r"\text{the quantity theory of money}", 22, GREY),
        ], "right", buff=0.42)

        deriv = self._stack([
            eq(r"\frac{M}{p} = m^{D}(Y,i)", 30),
            eq(r"V = \frac{Y}{m^{D}(Y,i)}", 32, BLUE),
            eq(r"V = Y \Big/ \sqrt{\frac{Y F}{2 i}}", 30, BLUE),
            eq(r"V = \sqrt{\frac{2 i Y}{F}}", 34, GREEN),
        ], "left", buff=0.40)

        signs = table(["a rise in", "velocity"],
                      [("the nominal rate i", "rises"),
                       ("output Y", "rises"),
                       ("the cost of a trip F", "falls")],
                      col_widths=[3.4, 2.2], font_size=20,
                      cell_colours={(0, 1): YELLOW, (1, 1): YELLOW, (2, 1): YELLOW})

        b.step(st.show("title", title("the most famous equation here")), t=0.6, hold=1)
        b.step(st.show("title", eq(r"M \cdot V = p \cdot Y", 44)), t=0.9, hold=1.5)
        b.step(st.show("note", note("money times velocity equals nominal output")),
               t=0.7, hold=1.5)
        b.step(st.show("note", note("velocity: how many times a unit of money is used "
                                    "in a period")), t=0.7, hold=2)
        b.step(st.show("main", example), t=1.2, hold=3)
        b.step(st.show("note", eq(r"V = p Y / M = 6/2 = 3", 34, YELLOW)), t=0.9, hold=2.5)
        b.step(st.clear("main") + st.show("left", ident[0], fit=False), t=1.0, hold=2)
        b.step(st.add_to("left", ident[1]), t=1.0, hold=2.5)
        b.step(st.show("note", note("any country, any century, whatever the economics is")),
               t=0.8, hold=2)
        b.step(st.show("note", note("an equation that cannot fail cannot be evidence", RED)),
               t=0.8, hold=2.5)
        b.step(st.show("note", note("you cannot test it; you cannot violate it", RED)),
               t=0.8, hold=2)
        b.step(st.add_to("right", theory[0]), t=0.8, hold=1.5)
        b.step(st.add_to("right", theory[1]), t=0.8, hold=2)
        b.step(st.add_to("right", theory[2]), t=0.9, hold=2.5)
        b.step(st.add_to("right", theory[3]), t=0.7, hold=1.5)
        b.step(st.show("note", note("the assumption is where all the content lives", YELLOW)),
               t=0.8, hold=2.5)
        b.step(st.show("left", deriv[0], fit=False), t=0.9, hold=2)
        b.step(st.add_to("left", deriv[1]), t=0.9, hold=2.5)
        b.step(st.show("note", note("so any theory of money demand is already a theory "
                                    "of velocity")), t=0.8, hold=2.5)
        b.step(st.add_to("left", deriv[2]), t=0.9, hold=2)
        b.step(st.add_to("left", deriv[3]), t=1.0, hold=2.5)
        b.step(st.show("right", signs), t=1.2, hold=3)
        b.step(st.show("note", note("not a constant, and it moves exactly when policy "
                                    "moves the interest rate", RED)), t=0.9, hold=2.5)
        b.step(st.show("note", note("the assumption that makes it a theory is contradicted "
                                    "in precisely the dimension that matters", RED)),
               t=0.9, hold=3)
        b.run()


class BeatFourteen(Scene):
    """Two indices, each computed, and one price falling while the index rises."""

    @staticmethod
    def _stack(items, slot, buff=0.34):
        g = VGroup(*items).arrange(DOWN, aligned_edge=LEFT, buff=buff)
        Stage.fit(g, slot)
        return items

    def construct(self):
        st = Stage(self)
        b = Beat(self, "BeatFourteen")

        ax, pan = axes_panel([0, 8, 4], [0, 6, 2], x_label="time",
                            y_label="prices of three goods", width=5.0, height=3.1)
        Stage.fit(pan, "left")
        same = VGroup(*[Line(ax.c2p(0, y), ax.c2p(8, y + 1.8), color=GREY, stroke_width=4)
                        for y in (0.6, 1.9, 3.2)])
        apart = VGroup(Line(ax.c2p(0, 0.6), ax.c2p(8, 1.3), color=GREY, stroke_width=4),
                       Line(ax.c2p(0, 1.9), ax.c2p(8, 5.6), color=GREY, stroke_width=4),
                       Line(ax.c2p(0, 3.2), ax.c2p(8, 1.9), color=RED, stroke_width=4))

        basket = self._stack([
            note("choose a basket:", GREY, 23),
            note("fixed quantities of specific goods", WHITE, 23),
            note("its total cost over time is a price index", WHITE, 23),
            note("different baskets, different indices", YELLOW, 23),
            note("there is no neutral choice", YELLOW, 23),
        ], "right", buff=0.40)

        defl = self._stack([
            eq(r"\text{deflator} = \frac{\text{nominal}}{\text{real}} \times 100", 32),
            note("weights each good by its share of production", GREY, 21),
        ], "left", buff=0.6)

        amounts = table(["valued at", "total"],
                        [("base-year prices", "2550"), ("current prices", "1860")],
                        col_widths=[3.0, 1.9], font_size=21)

        goods = table(["basket", "old", "new"],
                      [("2 cars", "100", "115"),
                       ("20 kg caviar", "4", "3"),
                       ("10 L champagne", "2", "4")],
                      col_widths=[3.0, 1.3, 1.3], font_size=20,
                      cell_colours={(1, 2): RED})

        cost = self._stack([
            eq(r"\text{old: } 2(100) + 20(4) + 10(2) = 300", 26),
            eq(r"\text{new: } 2(115) + 20(3) + 10(4) = 330", 26),
            eq(r"\text{index } 100 \to 110", 28),
            eq(r"\pi = 10\%", 34, YELLOW),
        ], "right", buff=0.45)

        oil = table(["an oil exporter", "an oil price rise shows up"],
                    [("production-weighted index", "strongly"),
                     ("consumption-weighted index", "much less")],
                    col_widths=[5.4, 4.8], font_size=22,
                    cell_colours={(0, 1): YELLOW, (1, 1): GREY})

        b.step(st.show("title", title("Measuring inflation")), t=0.6, hold=1)
        b.step(st.show("note", note("the same problem as lecture one, in different clothes")),
               t=0.7, hold=1.5)
        b.step(st.show("left", pan, fit=False), t=0.9, hold=1)
        b.step(st.add_to("left", same), t=0.8, hold=1.5)
        b.step(st.show("note", note("if every price rose by the same per cent there would "
                                    "be nothing to discuss")), t=0.7, hold=2)
        b.step([Transform(same, apart)], t=1.2, hold=2)
        b.step(st.show("note", note("they move by different amounts, and some move the "
                                    "other way")), t=0.8, hold=2)
        b.step(st.show("note", note("so what is the overall change?", YELLOW)), t=0.7, hold=2)
        b.step(st.add_to("right", VGroup(basket[0], basket[1])), t=0.8, hold=2)
        b.step(st.add_to("right", basket[2]), t=0.8, hold=2)
        b.step(st.add_to("right", VGroup(basket[3], basket[4])), t=0.8, hold=2.5)
        # ---------- index one
        b.step(st.clear("left", "right", "note")
               + st.show("title", title("Index one: the GDP deflator", YELLOW)),
               t=0.8, hold=1)
        b.step(st.show("left", defl[0], fit=False), t=0.9, hold=2)
        b.step(st.add_to("left", defl[1]), t=0.8, hold=2)
        b.step(st.show("right", amounts), t=1.2, hold=2.5)
        b.step(st.show("note", eq(r"1860 / 2550 \times 100 \approx 73", 34, YELLOW)),
               t=0.9, hold=2.5)
        b.step(st.show("note", note("it started at 100, so prices fell by about 27 per cent",
                                    RED)), t=0.8, hold=2.5)
        # ---------- index two
        b.step(st.clear("left", "right", "note")
               + st.show("title", title("Index two: a consumption basket", YELLOW)),
               t=0.8, hold=1)
        b.step(st.show("note", note("weights by what is consumed; a survey fixes the basket")),
               t=0.7, hold=1.5)
        b.step(st.show("left", goods), t=1.2, hold=3)
        b.step(st.add_to("right", cost[0]), t=1.0, hold=2.5)
        b.step(st.add_to("right", cost[1]), t=1.0, hold=2.5)
        b.step(st.add_to("right", cost[2]), t=0.8, hold=2)
        b.step(st.add_to("right", cost[3]), t=0.8, hold=2)
        b.step(st.show("note", note("caviar fell from 4 to 3, and the index still rose "
                                    "ten per cent", RED)), t=0.9, hold=2.5)
        b.step(st.show("note", note("inflation is a statement about an index, never about "
                                    "every price")), t=0.9, hold=2.5)
        b.step(st.clear("left", "right") + st.show("main", oil), t=1.2, hold=3)
        b.step(st.show("note", note("the same shock, two different numbers")), t=0.9, hold=2.5)
        b.run()


class BeatFifteen(Scene):
    """The real rate, counted in goods, and where the approximation fails."""

    @staticmethod
    def _stack(items, slot, buff=0.34):
        g = VGroup(*items).arrange(DOWN, aligned_edge=LEFT, buff=buff)
        Stage.fit(g, slot)
        return items

    def construct(self):
        st = Stage(self)
        b = Beat(self, "BeatFifteen")

        walk = self._stack([
            eq(r"1 \text{ dollar today} \;\to\; (1+i) \text{ dollars in a year}", 24),
            eq(r"100 \text{ dollars} = 1 \text{ basket today}", 26, BLUE),
            eq(r"\text{a year later: } 111 \text{ dollars}", 26),
            eq(r"111/100 = 1.11 \text{ baskets?}", 26, RED),
            eq(r"111/102 \approx 1.088 \text{ baskets}", 28, GREEN),
            eq(r"r \approx 8.8\% \text{ , counted in goods}", 26, YELLOW),
        ], "left", buff=0.32)

        given = table(["the loan", "value"],
                      [("nominal rate i", "11%"),
                       ("expected inflation", "2%"),
                       ("price index", "100 to 102"),
                       ("amount lent", "100 dollars")],
                      col_widths=[3.2, 2.2], font_size=21,
                      cell_colours={(0, 1): YELLOW})

        fisher = self._stack([
            eq(r"1 + r = \frac{1+i}{1+\pi}", 38, GREEN),
            eq(r"r \approx i - \pi \qquad \text{(Fisher)}", 30),
        ], "left", buff=0.8)

        approx = table(["the loan", "i minus inf.", "exact"],
                       [("i 11%, inf. 2%", "9.0%", "8.8%"),
                        ("i 100%, inf. 90%", "10.0%", "5.3%")],
                       col_widths=[3.2, 1.9, 1.5], font_size=20,
                       cell_colours={(1, 1): RED, (1, 2): GREEN})

        timing = table(["which real rate", "uses"],
                       [("ex ante, when you lend", "expected inflation"),
                        ("ex post, after the fact", "realised inflation")],
                       col_widths=[3.4, 2.8], font_size=20)

        cross = table(["the decision", "the rate"],
                      [("trading goods across time", "real r"),
                       ("holding cash, not bonds", "nominal i")],
                      col_widths=[3.8, 2.0], font_size=20,
                      cell_colours={(0, 1): GREEN, (1, 1): BLUE})

        b.step(st.show("title", title("Nominal and real")), t=0.6, hold=1)
        b.step(st.show("note", note("the piece students get wrong under time pressure")),
               t=0.7, hold=1.5)
        b.step(st.add_to("left", walk[0]), t=0.9, hold=2)
        b.step(st.show("note", note("but we care about goods, not dollars", YELLOW)),
               t=0.7, hold=2)
        b.step(st.show("right", given), t=1.1, hold=2.5)
        b.step(st.show("note", note("a price index of 100 becomes 102 over the year")),
               t=0.7, hold=1.5)
        b.step(st.add_to("left", walk[1]), t=0.9, hold=2)
        b.step(st.add_to("left", walk[2]), t=0.8, hold=2)
        b.step(st.add_to("left", walk[3]), t=0.9, hold=2.5)
        b.step(st.add_to("left", walk[4]), t=1.0, hold=2.5)
        b.step(st.show("note", note("for every good given up, about 1.088 goods come back")),
               t=0.8, hold=2.5)
        b.step(st.add_to("left", walk[5]), t=0.9, hold=2.5)
        b.step(st.show("left", fisher[0], fit=False), t=1.0, hold=2.5)
        b.step(st.add_to("left", fisher[1]), t=0.9, hold=2.5)
        b.step(st.show("right", approx), t=1.2, hold=3)
        b.step(st.show("note", note("fine at two per cent, badly wrong in a hyperinflation: "
                                    "use the ratio", RED)), t=0.9, hold=2.5)
        b.step(st.show("right", timing), t=1.1, hold=3)
        b.step(st.show("note", note("you do not know the real rate at the time you lend")),
               t=0.8, hold=2.5)
        b.step(st.show("left", cross), t=1.2, hold=3)
        b.step(st.show("note", note("real rates for decisions across time; the nominal rate "
                                    "for the cost of holding money")), t=0.9, hold=3)
        b.run()
