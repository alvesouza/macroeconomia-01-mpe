"""Scenes for aula-07-money-and-inflation (group g1).

Durations come from beats.json via the kit. Do not hard-code seconds.
Render: python -m manim render -ql --media_dir media scenes_g1.py BeatX
"""
import numpy as np
from manim import *

from video_explainer import (Beat, Stage, axes_panel, balance_sheet, bullets, eq, note,
                       ols, palette, read_csv, sawtooth, scatter, series, table,
                       title, FAST, NORMAL, SLOW)


class BeatOne(Scene):
    """The miss: a target, a realisation, and the one number in between."""

    def construct(self):
        P = palette()
        st = Stage(self)
        b = Beat(self, "BeatOne")

        # --- the bank's problem, as a chart on the left and its numbers on the right
        b.step(st.show("title", title("A central bank with a simple job")),
               t=0.8, hold=1.0)

        ax, panel = axes_panel([0, 10, 2], [0, 3, 1], x_label="years",
                              y_label="inflation, per cent", width=5.0, height=3.4)
        b.step(st.show("left", panel), t=1.2, hold=1.0)

        target = DashedLine(ax.c2p(0, 2), ax.c2p(10, 2), color=P["muted"])
        tlab = note("target  2", P["muted"], 20).move_to(ax.c2p(7.4, 2.38))
        b.step(st.add_to("left", VGroup(target, tlab)), t=0.9, hold=1.2)

        setting = [("inflation target", "2"),
                   ("output growth", "3"),
                   ("money growth chosen", "3.5")]
        t_plain = table(["what the bank set", "per cent"], setting,
                        col_widths=[3.3, 1.8], font_size=20)
        b.step(st.show("right", t_plain), t=1.0, hold=3.0)

        realised = Line(ax.c2p(0, 0.5), ax.c2p(10, 0.5), color=P["broken"],
                        stroke_width=6)
        rlab = note("realised  0.5", P["broken"], 20).move_to(ax.c2p(7.4, 0.88))
        b.step(st.add_to("left", VGroup(realised, rlab)), t=1.0, hold=1.5)

        brace = BraceBetweenPoints(ax.c2p(3.2, 0.5), ax.c2p(3.2, 2),
                                   direction=RIGHT, color=P["focus"])
        blab = note("1.5 points", P["focus"], 21).move_to(ax.c2p(5.1, 1.25))
        gap = VGroup(brace, blab)
        b.step(st.add_to("left", gap), t=1.0, hold=1.5)

        # --- and nothing went wrong
        b.step(st.show("note", note("no financial crisis")), t=0.6, hold=0.8)
        b.step(st.show("note", note("no oil shock, no war")), t=0.6, hold=0.8)
        b.step(st.show("note", note("nobody lost control of the printing press")),
               t=0.6, hold=0.9)

        t_hit = table(["what the bank set", "per cent"], setting,
                      col_widths=[3.3, 1.8], font_size=20,
                      cell_colours={(2, 0): P["focus"], (2, 1): P["focus"]})
        b.step(st.show("right", t_hit), t=0.9, hold=1.4)
        b.step(st.show("note", note("it hit that to the decimal", P["focus"])),
               t=0.7, hold=1.2)

        b.step(st.show("title", title("It did everything right, and still missed",
                                      P["focus"])), t=0.8, hold=1.0)

        unknown = VGroup(note("one number"), eq(r"\eta \;=\; ?", 56, P["focus"])) \
            .arrange(DOWN, buff=0.35)
        b.step(st.show("right", unknown), t=1.0, hold=1.6)
        b.step(st.show("note", note("not a model, not a regime, not a judgement call")),
               t=0.7, hold=1.4)
        b.step(st.show("note", note("it cannot be observed, so it has to be assumed")),
               t=0.7, hold=1.8)

        guesses = VGroup(
            eq(r"\eta = \tfrac{1}{2}", 52, P["survives"]),
            note("or", P["muted"], 22),
            eq(r"\eta = 1", 52, P["broken"])).arrange(DOWN, buff=0.3)
        b.step(st.show("right", guesses), t=1.0, hold=2.8)
        b.step([Indicate(gap, color=P["focus"], scale_factor=1.12)], t=1.0, hold=1.6)

        # --- so: why hold money at all?
        b.step(st.clear("left", "right")
               + st.show("title", title("Why would anyone hold money at all?",
                                        P["focus"])), t=1.0, hold=1.6)

        pays = table(["where value can sit", "what it pays"],
                     [("a bond", "the nominal rate i"),
                      ("a savings account", "interest"),
                      ("cash in your pocket", "nothing")],
                     col_widths=[4.2, 4.2], font_size=23,
                     cell_colours={(2, 0): P["broken"], (2, 1): P["broken"]})
        b.step(st.show("main", pays), t=1.0, hold=2.2)
        b.step(st.show("note", note("holding cash is, on its face, a choice to be poorer")),
               t=0.8, hold=2.0)
        b.step(st.show("note", note("answer that properly and the number appears, with a reason",
                                    P["focus"])), t=0.8, hold=1.6)
        b.run()


class BeatTwo(Scene):
    """The sawtooth: what a household's money balance does across one year."""

    def construct(self):
        P = palette()
        st = Stage(self)
        b = Beat(self, "BeatTwo")

        b.step(st.show("title", title("A household's money across one year")),
               t=0.8, hold=1.0)

        spend = VGroup(eq(r"p\,Y", 72, P["focus"]),
                       note("quantity Y of goods, at price p, over the year")) \
            .arrange(DOWN, buff=0.45)
        b.step(st.show("main", spend), t=1.0, hold=1.5)
        b.step(st.show("note", note("it does not spend it all at once: it spends evenly")),
               t=0.7, hold=1.0)

        where = table(["where wealth can sit", "what it pays"],
                      [("bonds, savings", "interest i"),
                       ("money", "nothing")],
                      col_widths=[4.2, 4.2], font_size=23,
                      cell_colours={(1, 0): P["demand"], (1, 1): P["demand"]})
        b.step(st.show("main", where), t=1.0, hold=1.4)
        b.step(st.show("note", note("every payment has to be made with money")),
               t=0.6, hold=1.0)
        b.step(st.show("note", note("but not the whole year's cash on the first of January")),
               t=0.6, hold=1.2)

        trip = table(["a trip to the bank", "costs"],
                     [("a cash machine", "F"),
                      ("selling a bond", "F"),
                      ("the hassle of it", "F")],
                     col_widths=[4.2, 2.4], font_size=23,
                     cell_colours={(0, 1): P["focus"], (1, 1): P["focus"],
                                   (2, 1): P["focus"]})
        b.step(st.show("main", trip), t=1.0, hold=2.4)
        b.step(st.show("note", note("one choice to make: N, the number of trips a year",
                                    P["focus"])), t=0.7, hold=1.3)

        # --- the picture
        ax, panel = axes_panel([0, 1, 0.25], [0, 1.15, 0.25], x_label="one year",
                              y_label="money held", width=8.4, height=3.9)
        b.step(st.show("main", panel), t=1.2, hold=0.8)

        full = DashedLine(ax.c2p(0, 1), ax.c2p(1, 1), color=P["muted"])
        flab = note("pY, held all year", P["muted"], 19) \
            .next_to(ax.c2p(1, 1), RIGHT, buff=0.15)
        b.step(st.add_to("main", VGroup(full, flab)), t=0.8, hold=0.9)

        peak = VGroup(Dot(ax.c2p(0, 0.5), color=P["demand"], radius=0.07),
                      eq(r"\frac{pY}{N}", 34, P["demand"])
                      .next_to(ax.c2p(0.03, 0.5), UR, buff=0.12))
        b.step(st.add_to("main", peak), t=0.9, hold=1.2)

        tooth = VMobject(color=P["demand"], stroke_width=5) \
            .set_points_as_corners([ax.c2p(0, 0.5), ax.c2p(0.5, 0)])
        b.step([Create(tooth)], t=1.0, hold=1.2)
        st.add_to("main", tooth)

        saw2 = sawtooth(ax, 2, colour=P["demand"])
        b.step([Transform(tooth, saw2)]
               + st.show("note", note("two trips a year")), t=1.0, hold=1.5)
        b.step(st.show("note", note("each tooth is half the year's spending, sliding to nothing")),
               t=0.6, hold=1.2)

        saw4 = sawtooth(ax, 4, colour=P["demand"])
        b.step([Transform(tooth, saw4)]
               + st.show("note", note("now four trips: half as tall, twice as many")),
               t=1.2, hold=1.5)

        avg = DashedLine(ax.c2p(0, 0.125), ax.c2p(1, 0.125), color=P["focus"])
        alab = note("average", P["focus"], 19).next_to(ax.c2p(1, 0.125), RIGHT, buff=0.15)
        average = VGroup(avg, alab)
        b.step(st.add_to("main", average), t=0.9, hold=1.5)
        b.step(st.show("note", note("it falls linearly from peak to zero, "
                                    "so the average is exactly half the peak")),
               t=0.7, hold=1.8)

        b.step(st.show("title", eq(r"\bar{M} = \frac{pY}{2N}", 44, P["focus"])),
               t=1.0, hold=1.5)
        b.step([Indicate(average, color=P["focus"], scale_factor=1.05)]
               + st.show("note", note("more trips, smaller balances: "
                                      "the first half of a trade-off")),
               t=0.8, hold=1.6)
        b.run()


class BeatThree(Scene):
    """The trade-off: a line, a hyperbola, a U, and the algebra of its bottom."""

    @staticmethod
    def _dom(f, lo, hi, ymax):
        xs = np.linspace(lo, hi, 500)
        ok = [x for x in xs if f(x) <= ymax]
        return [ok[0], ok[-1]]

    def _curves(self, ax, a, c, P, ymax=13.4):
        """Trip cost a*N, forgone interest c/N, and their sum, for one (F, i) pair."""
        f1, f2 = (lambda x: a * x), (lambda x: c / x)
        f3 = lambda x: a * x + c / x
        line = ax.plot(f1, x_range=self._dom(f1, 0.3, 9.3, ymax),
                       color=GREY_B, stroke_width=4)
        hyp = ax.plot(f2, x_range=self._dom(f2, 1.2, 9.6, ymax),
                      color=P["demand"], stroke_width=4)
        tot = ax.plot(f3, x_range=self._dom(f3, 1.2, 9.3, ymax),
                      color=P["survives"], stroke_width=5)
        n = (c / a) ** 0.5
        dot = Dot(ax.c2p(n, f3(n)), color=P["focus"], radius=0.085)
        drop = DashedLine(ax.c2p(n, f3(n)), ax.c2p(n, 0), color=P["focus"],
                          stroke_width=2)
        lab = note("N*", P["focus"], 20).move_to(ax.c2p(n + 0.7, 1.1))
        return line, hyp, tot, VGroup(dot, drop, lab)

    def construct(self):
        P = palette()
        st = Stage(self)
        b = Beat(self, "BeatThree")

        b.step(st.show("title", title("Why not go to the bank every day?")),
               t=0.8, hold=0.9)

        ax, panel = axes_panel([0, 10, 2], [0, 14, 2], x_label="trips per year, N",
                              y_label="cost", width=5.0, height=3.5)
        b.step(st.show("left", panel), t=1.2, hold=0.8)

        line, hyp, tot, mark = self._curves(ax, 0.8, 8.0, P)

        c_trips = VGroup(note("the trips cost F each", GREY_B, 22),
                         eq(r"p\,F\,N", 50, GREY_B)).arrange(DOWN, buff=0.3)
        b.step(st.show("right", c_trips), t=1.0, hold=1.8)
        b.step([Create(line)], t=1.0, hold=1.4)
        st.add_to("left", line)
        b.step(st.show("note", note("more trips, more cost, with no limit")),
               t=0.6, hold=1.0)

        b.step(st.show("note", note("the money in your pocket could have been "
                                    "a bond earning i")), t=0.7, hold=1.4)
        c_int = VGroup(note("so you give up interest", P["demand"], 22),
                       eq(r"i\,\frac{pY}{2N}", 50, P["demand"])).arrange(DOWN, buff=0.3)
        b.step(st.show("right", c_int), t=1.0, hold=1.6)
        b.step([Create(hyp)], t=1.0, hold=1.4)
        st.add_to("left", hyp)
        b.step(st.show("note", note("steeply at first, then flattening: "
                                    "it approaches zero without reaching it")),
               t=0.7, hold=1.4)

        c_tot = VGroup(note("total cost", P["survives"], 22),
                       eq(r"p\,F\,N + i\,\frac{pY}{2N}", 46, P["survives"])) \
            .arrange(DOWN, buff=0.3)
        b.step(st.show("right", c_tot), t=1.0, hold=1.2)
        b.step([Create(tot)], t=1.2, hold=1.4)
        st.add_to("left", tot)
        b.step([FadeIn(mark[0], scale=2), Create(mark[1]), FadeIn(mark[2])],
               t=1.0, hold=1.3)
        st.add_to("left", mark)
        b.step(st.show("note", note("a line rising and a hyperbola falling: "
                                    "the household sits at the bottom of the U")),
               t=0.7, hold=1.4)

        foc = Stage.fit(eq(r"pF - \frac{i\,pY}{2N^{2}} = 0", 44), "right")
        b.step(st.show("right", foc), t=1.0, hold=2.0)
        nstar = Stage.fit(eq(r"N^{*} = \sqrt{\frac{iY}{2F}}", 52, P["focus"]), "right")
        b.step([Transform(foc, nstar)], t=1.2, hold=1.6)

        # --- comparative statics, read off the same picture
        b.step(st.show("note", note("trips rise with the interest rate: "
                                    "when money is expensive to hold, you go more often")),
               t=0.7, hold=1.2)
        l2, h2, t2, m2 = self._curves(ax, 0.8, 16.0, P)
        b.step([Transform(hyp, h2), Transform(tot, t2), Transform(mark, m2)],
               t=1.4, hold=1.6)

        b.step(st.show("note", note("and they fall with F: "
                                    "when trips are expensive, you go less often")),
               t=0.7, hold=1.2)
        l3, h3, t3, m3 = self._curves(ax, 1.4, 16.0, P)
        b.step([Transform(line, l3), Transform(tot, t3), Transform(mark, m3)],
               t=1.4, hold=1.6)
        b.step(st.show("note", note("both are what you would expect, "
                                    "which is a good sign")), t=0.7, hold=1.3)

        sub = Stage.fit(VGroup(eq(r"\bar{M} = \frac{pY}{2N^{*}}", 44),
                              eq(r"\Rightarrow\;\; \frac{\bar{M}}{p} "
                                 r"= \frac{Y}{2N^{*}}", 40)).arrange(DOWN, buff=0.4),
                        "right")
        b.step(st.show("right", sub), t=1.0, hold=2.0)
        md = Stage.fit(eq(r"\frac{\bar{M}}{p} = \sqrt{\frac{YF}{2i}}", 58, P["demand"]),
                       "right")
        b.step([Transform(sub, md)], t=1.4, hold=2.0)
        b.step(st.show("note", note("that is money demand: derived from a household "
                                    "minimising a cost, not assumed", P["survives"])),
               t=0.8, hold=2.0)
        b.step(st.show("title", title("Money demand, derived")), t=0.8, hold=1.2)
        b.run()


class BeatFour(Scene):
    """On log axes the slope is the elasticity, and the slope is one half."""

    def construct(self):
        P = palette()
        st = Stage(self)
        b = Beat(self, "BeatFour")

        b.step(st.show("title", title("The number inside the square root")),
               t=0.8, hold=0.8)

        md = Stage.fit(eq(r"\frac{\bar{M}}{p} = \sqrt{\frac{YF}{2i}}", 54, P["demand"]),
                       "right")
        b.step(st.show("right", md), t=1.0, hold=1.2)
        prop = Stage.fit(eq(r"\frac{\bar{M}}{p} \;\propto\; Y^{1/2}", 54, P["focus"]),
                         "right")
        b.step([Transform(md, prop)], t=1.2, hold=1.6)
        b.step(st.show("note", note("not proportional to income: "
                                    "proportional to its square root")), t=0.6, hold=1.0)

        ax, panel = axes_panel([0, 4, 1], [0, 2.6, 1], x_label="log income",
                              y_label="log real balances", width=5.0, height=3.5)
        b.step(st.show("left", panel), t=1.2, hold=0.8)

        logs = Stage.fit(eq(r"\log \frac{\bar{M}}{p} = \tfrac{1}{2}\log Y + c", 40,
                            P["focus"]), "right")
        b.step([Transform(md, logs)], t=1.2, hold=1.0)

        bt = ax.plot(lambda x: 0.5 * x + 0.4, x_range=[0.15, 3.9],
                     color=P["demand"], stroke_width=5)
        btl = note("slope 1/2", P["demand"], 20).move_to(ax.c2p(2.55, 2.3))
        b.step(st.add_to("left", VGroup(bt, btl)), t=1.0, hold=1.0)

        p0, p1, p2 = ax.c2p(1.6, 1.2), ax.c2p(2.6, 1.2), ax.c2p(2.6, 1.7)
        tri = VGroup(Line(p0, p1, color=P["focus"]), Line(p1, p2, color=P["focus"]))
        b.step(st.add_to("left", tri), t=0.9, hold=0.8)
        tl = VGroup(note("1", P["focus"], 19).next_to(Line(p0, p1), DOWN, buff=0.1),
                    note("0.5", P["focus"], 19).next_to(Line(p1, p2), RIGHT, buff=0.1))
        b.step(st.add_to("left", tl), t=0.7, hold=1.0)

        eta = Stage.fit(eq(r"\eta \equiv \frac{d\log(\bar{M}/p)}{d\log Y} "
                           r"= \tfrac{1}{2}", 42, P["focus"]), "right")
        b.step([Transform(md, eta)], t=1.0, hold=2.0)
        b.step(st.show("note", note("income up one per cent, "
                                    "money demand up half a per cent")), t=0.7, hold=1.4)

        scale = table(["income rises by", "cash rises by"],
                      [("100 per cent", "41 per cent"),
                       ("900 per cent", "216 per cent")],
                      col_widths=[2.9, 2.6], font_size=21,
                      cell_colours={(0, 1): P["demand"], (1, 1): P["demand"]})
        b.step(st.show("right", scale), t=1.0, hold=2.2)
        b.step(st.show("note", note("you do not double your cash: "
                                    "you can go to the bank more often instead")),
               t=0.7, hold=1.4)

        trips = Stage.fit(eq(r"N^{*} = \sqrt{\frac{iY}{2F}} \;\propto\; Y^{1/2}", 40,
                             P["focus"]), "right")
        b.step(st.show("right", trips), t=1.0, hold=1.8)
        b.step(st.show("note", note("economies of scale in managing cash, "
                                    "and one half is their measure", P["survives"])),
               t=0.7, hold=1.4)

        camb = ax.plot(lambda x: 1.0 * x - 0.4, x_range=[0.55, 2.95],
                       color=P["broken"], stroke_width=5)
        cl = note("slope 1", P["broken"], 20).move_to(ax.c2p(1.15, 2.3))
        b.step(st.add_to("left", VGroup(camb, cl)), t=1.0, hold=2.0)
        camb_eq = Stage.fit(eq(r"\frac{\bar{M}}{p} = k\,Y \;\Rightarrow\; \eta = 1", 40,
                               P["broken"]), "right")
        b.step(st.show("right", camb_eq), t=1.0, hold=1.4)
        b.step(st.show("note", note("not two settings of a dial: "
                                    "two different claims about behaviour")),
               t=0.7, hold=1.6)

        claims = table(["the claim", "elasticity"],
                       [("Baumol-Tobin: derived", "1/2"),
                        ("Cambridge: assumed", "1")],
                       col_widths=[3.6, 2.0], font_size=21,
                       cell_colours={(0, 0): P["demand"], (0, 1): P["demand"],
                                     (1, 0): P["broken"], (1, 1): P["broken"]})
        b.step(st.show("right", claims), t=1.1, hold=2.0)
        b.step(st.show("note", note("one half against one: the number our central bank "
                                    "had to guess at", P["focus"])), t=0.8, hold=1.6)
        b.run()


class BeatFive(Scene):
    """What counts as money: three functions, five properties, and a ladder."""

    @staticmethod
    def _box(label, width, colour, font_size=20):
        r = Rectangle(width=width, height=0.64, color=colour, stroke_width=3,
                      fill_opacity=0.14, fill_color=colour)
        return VGroup(r, Text(label, font_size=font_size).move_to(r))

    def construct(self):
        P = palette()
        st = Stage(self)
        b = Beat(self, "BeatFive")

        b.step(st.show("title", title("What counts as money")), t=0.8, hold=1.0)
        b.step(st.show("note", note("we have used the word for five minutes "
                                    "without defining it, deliberately")),
               t=0.7, hold=1.7)
        b.step(st.show("note", note("the model has a quantity of money in it, "
                                    "and somebody has to measure that quantity")),
               t=0.7, hold=1.7)

        fn_rows = [("store of value", "plenty of things do"),
                   ("unit of account", "plenty of things could"),
                   ("medium of exchange", "this is the one that works")]
        fns = table(["the three functions", "who else can do it"], fn_rows,
                    col_widths=[4.2, 4.8], font_size=23)
        b.step(st.show("main", fns), t=1.2, hold=1.8)
        b.step(st.show("note", note("plenty of things store value")), t=0.6, hold=1.0)
        b.step(st.show("note", note("plenty of things could serve as a unit of account")),
               t=0.6, hold=1.0)

        fns2 = Stage.fit(
            table(["the three functions", "who else can do it"], fn_rows,
                  col_widths=[4.2, 4.8], font_size=23,
                  cell_colours={(0, 0): P["muted"], (0, 1): P["muted"],
                                (1, 0): P["muted"], (1, 1): P["muted"],
                                (2, 0): P["survives"], (2, 1): P["survives"]}),
            "main")
        b.step([Transform(fns, fns2)]
               + st.show("note", note("what makes money money is that it is "
                                      "handed over in payment")), t=1.0, hold=1.5)
        b.step(st.show("note", note("and the reason that matters is "
                                    "the double coincidence of wants", P["focus"])),
               t=0.7, hold=1.4)

        barter = table(["", "has", "wants"],
                       [("me", "apples", "shoes"), ("you", "shoes", "bread")],
                       col_widths=[1.8, 3.0, 3.0], font_size=23)
        b.step(st.show("main", barter), t=1.2, hold=2.2)
        fail = note("no trade", P["broken"], 26).next_to(barter, DOWN, buff=0.35)
        b.step(st.add_to("main", fail), t=0.8, hold=1.2)

        withmoney = table(["with money", "what happens"],
                          [("I sell apples", "and take money"),
                           ("I buy shoes", "and hand the money over")],
                          col_widths=[3.4, 5.2], font_size=23,
                          cell_colours={(0, 0): P["survives"], (0, 1): P["survives"],
                                        (1, 0): P["survives"], (1, 1): P["survives"]})
        b.step(st.show("main", withmoney), t=1.2, hold=2.3)

        props = table(["it has to be", "or else"],
                      [("hard to counterfeit", "the seller wonders every time"),
                       ("easy to carry", "transactions happen everywhere"),
                       ("durable", "coffee beans, not strawberries"),
                       ("divisible", "you cannot make change"),
                       ("commonly accepted", "convention, or written into law")],
                      col_widths=[3.8, 5.6], font_size=21)
        b.step(st.show("main", props), t=1.4, hold=1.4)
        b.step(st.show("note", note("hard to counterfeit, or the seller spends "
                                    "every transaction wondering")), t=0.6, hold=1.2)
        b.step(st.show("note", note("durable: coffee beans make better money "
                                    "than strawberries")), t=0.6, hold=1.4)
        b.step(st.show("note", note("divisible, so you can pay the exact price "
                                    "and make change")), t=0.6, hold=1.2)
        b.step(st.show("note", note("commonly accepted: sometimes a convention, "
                                    "sometimes the law")), t=0.6, hold=1.2)

        # --- no sharp line: a continuum, not a yes or no
        spots = [("a house", 0.04), ("a government bond", 0.30),
                 ("savings deposits", 0.56), ("demand deposits", 0.79),
                 ("currency", 0.98)]
        arrow = Arrow(LEFT * 4.6, RIGHT * 4.6, color=P["muted"], stroke_width=3,
                      buff=0, max_tip_length_to_length_ratio=0.035)
        marks = VGroup()
        for k, (lab, pos) in enumerate(spots):
            x = -4.6 + 9.2 * pos
            d = Dot([x, 0, 0], color=P["focus"] if pos > 0.5 else P["muted"],
                    radius=0.06)
            t = note(lab, WHITE if pos > 0.5 else P["muted"], 19)
            t.next_to(d, UP if k % 2 == 0 else DOWN, buff=0.22)
            marks.add(VGroup(d, t))
        cont = VGroup(note("the properties are satisfied by degrees, not yes or no",
                           P["muted"], 22),
                      VGroup(arrow, marks)).arrange(DOWN, buff=0.7)
        b.step(st.show("main", cont), t=1.4, hold=2.0)
        b.step(st.show("note", note("there is no sharp line between money and not money",
                                    P["broken"])), t=0.7, hold=1.4)
        b.step(st.show("note", note("so there is no single correct measure of how much "
                                    "money an economy has", P["broken"])),
               t=0.7, hold=1.4)

        # --- the ladder, one rung at a time, and the base off to one side
        r1 = self._box("currency", 3.2, P["demand"])
        r2 = self._box("currency + demand deposits", 5.8, P["demand"])
        r3 = self._box("+ savings, small time deposits, money funds", 8.4,
                       P["demand"], font_size=19)
        rungs = VGroup(r1, r2, r3).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        tags = []
        for rung, name in ((r1, "currency"), (r2, "M1"), (r3, "M2")):
            tags.append(note(name, P["focus"], 22).next_to(rung, LEFT, buff=0.25))
        rung1 = VGroup(r1, tags[0])
        rung2 = VGroup(r2, tags[1])
        rung3 = VGroup(r3, tags[2])
        base = self._box("currency + bank reserves", 5.4, P["focus"])
        btag = note("monetary base", P["focus"], 22).next_to(base, LEFT, buff=0.25)
        rule = DashedLine(LEFT * 4.8, RIGHT * 4.8, color=P["muted"], stroke_width=2)
        whole = VGroup(VGroup(rung1, rung2, rung3), rule, VGroup(base, btag)) \
            .arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        Stage.fit(whole, "main")

        b.step(st.show("main", rung1, fit=False)
               + st.show("note", note("what exists instead is a ladder")),
               t=1.0, hold=1.2)
        b.step(st.add_to("main", rung2), t=1.0, hold=1.8)
        b.step(st.add_to("main", rung3), t=1.0, hold=1.9)
        b.step(st.show("note", note("each rung is slightly less usable in a transaction "
                                    "than the one below it")), t=0.7, hold=1.4)
        b.step(st.add_to("main", VGroup(rule, base, btag)), t=1.2, hold=2.2)
        b.step(st.show("note", note("not a smaller M1: the part of money the central "
                                    "bank issues directly")), t=0.7, hold=1.8)
        b.step(st.show("note", note("if the central bank only issues the base,\n"
                                    "how does it control anything else?", P["focus"])),
               t=0.9, hold=1.8)
        b.run()
