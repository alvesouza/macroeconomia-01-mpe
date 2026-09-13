"""Scenes for aula-07-money-and-inflation (group g4).

Durations come from beats.json via the kit. Do not hard-code seconds.
Render: python -m manim render -ql --media_dir media scenes_g4.py BeatX
"""
from datetime import datetime

import numpy as np
from manim import *

from video_explainer import (Beat, Stage, axes_panel, balance_sheet, bullets, eq, mpl_figure,
                       note, ols, palette, read_csv, sawtooth, scatter, series, table,
                       title, FAST, NORMAL, SLOW)


class BeatSixteen(Scene):
    """The cross-country test: apparently refuted, rescued by one bad observation."""

    @staticmethod
    def _stack(items, slot, buff=0.34):
        g = VGroup(*items).arrange(DOWN, aligned_edge=LEFT, buff=buff)
        Stage.fit(g, slot)
        return items

    def construct(self):
        st = Stage(self)
        b = Beat(self, "BeatSixteen")

        rows = read_csv("data/wdi_money_vs_inflation_country_averages.csv")
        pts = [(float(r["money_growth_avg"]), float(r["inflation_avg"]), r["country"])
               for r in rows]
        raw = [(m, i) for m, i, _ in pts]
        slope_raw, _, corr_raw = ols(raw)
        assert abs(slope_raw - 0.061) < 0.01 and abs(corr_raw - 0.171) < 0.01, \
            (slope_raw, corr_raw)

        clean = [(m, i) for m, i, _ in pts if m < 100 and i < 100]
        slope_clean, _, corr_clean = ols(clean)
        assert abs(slope_clean - 1.064) < 0.01 and abs(corr_clean - 0.746) < 0.01, \
            (slope_clean, corr_clean)

        sle_rows = read_csv("data/wdi_fm_lbl_bmny_zg.csv")
        sle = sorted((int(r["year"]), float(r["value"]))
                     for r in sle_rows if r["iso3"] == "SLE")
        sle_normal = [v for y, v in sle if y not in (2001, 2015)]
        median_normal = sorted(sle_normal)[len(sle_normal) // 2]
        assert 22.0 < median_normal < 24.0, median_normal

        def draw_raw(fig, ax):
            ax.scatter([p[0] for p in raw], [p[1] for p in raw], s=14,
                      c="#58C4DD", alpha=.75, edgecolors="none")
            xs = np.array([0, 4000])
            ax.plot(xs, slope_raw * xs, color="#FC6255", lw=2, ls="--")
            ax.set_xlabel("average broad money growth, per cent")
            ax.set_ylabel("average inflation, per cent")
            ax.set_xlim(0, 4000); ax.set_ylim(0, 1400)
            ax.grid(alpha=.15, color="#e8ebef")

        fig_raw = mpl_figure(draw_raw, "scatter_raw159", width=9.4)

        def draw_zoom(fig, ax):
            ax.scatter([p[0] for p in raw], [p[1] for p in raw], s=16,
                      c="#58C4DD", alpha=.85, edgecolors="none")
            ax.set_xlabel("average broad money growth, per cent")
            ax.set_ylabel("average inflation, per cent")
            ax.set_xlim(0, 100); ax.set_ylim(0, 100)
            ax.grid(alpha=.15, color="#e8ebef")

        fig_zoom = mpl_figure(draw_zoom, "scatter_raw159_zoom", width=9.0)

        def draw_sle(fig, ax):
            years = [y for y, _ in sle]
            levels = [1 + v / 100 for _, v in sle]
            colours = ["#FC6255" if y in (2001, 2015) else "#58C4DD" for y in years]
            ax.scatter(years, levels, s=26, c=colours, edgecolors="none")
            ax.set_yscale("log")
            ax.set_xlabel("year")
            ax.set_ylabel("money stock, 1 + growth rate (log)")
            ax.grid(alpha=.15, color="#e8ebef")

        fig_sle = mpl_figure(draw_sle, "sierraleone_series", width=5.6)

        def draw_clean(fig, ax):
            ax.scatter([p[0] for p in clean], [p[1] for p in clean], s=16,
                      c="#58C4DD", alpha=.85, edgecolors="none")
            ax.plot([0, 100], [0, 100], color="#83C167", lw=2, ls="--")
            ax.set_xlabel("average broad money growth, per cent")
            ax.set_ylabel("average inflation, per cent")
            ax.set_xlim(0, 100); ax.set_ylim(0, 100)
            ax.grid(alpha=.15, color="#e8ebef")

        fig_clean = mpl_figure(draw_clean, "scatter_clean", width=9.0)

        sle_table = table(["Sierra Leone, 1990-2023", "value"],
                          [("32 ordinary years", "7% to 76%"),
                           ("median year", "23.0%"),
                           ("2001", "131 119%"),
                           ("2015", "-99.9%")],
                          col_widths=[4.6, 3.0], font_size=21,
                          cell_colours={(2, 1): RED, (3, 1): RED})

        lessons = bullets([
            "the theory survives",
            "one unexamined observation can hide a slope of one",
        ], size=22)

        b.step(st.show("title", title("Does the world agree?")), t=0.6, hold=1.5)
        b.step(st.show("note", note("every country with data: average money growth "
                                    "across, average inflation up")), t=0.7, hold=2.5)
        b.step(st.show("note", note("if the theory holds, the dots sit near a line "
                                    "of slope one")), t=0.7, hold=2)
        b.step(st.show("main", fig_raw, fit=False), t=1.0, hold=2.5)
        b.step(st.show("note", eq(r"\text{slope } 0.06,\;\; r = 0.17", 30, RED)),
               t=0.9, hold=2.5)
        b.step(st.show("note", note("the theory appears refuted", RED)), t=0.7, hold=2)
        b.step(st.show("main", fig_zoom, fit=False), t=1.0, hold=2)
        b.step(st.show("note", note("almost every country crushed bottom-left; the "
                                    "raw axis runs out to nearly four thousand per cent")),
               t=0.8, hold=3)
        b.step(st.show("note", note("one dot is stretching this picture", YELLOW)),
               t=0.7, hold=2)
        b.step(st.show("title", title("Sierra Leone: 3 879% average", YELLOW)),
               t=0.7, hold=2)
        b.step(st.clear("main", "note") + st.show("left", fig_sle, fit=False),
               t=1.0, hold=2)
        b.step(st.show("right", sle_table), t=1.1, hold=3)
        b.step(st.show("note", note("a jump, followed by a fall of almost exactly "
                                    "one hundred per cent, is not an economy")),
               t=0.8, hold=3)
        b.step(st.show("note", note("the signature of a redenomination, or a break "
                                    "in the units of the series", RED)), t=0.8, hold=3)
        b.step(st.show("note", note("one bad year dragged a thirty-year average up "
                                    "by a factor of more than 160")), t=0.8, hold=3)
        b.step(st.clear("left", "right", "note")
               + st.show("title", title("148 countries, the outlier removed", GREEN)),
               t=0.8, hold=1.5)
        b.step(st.show("main", fig_clean, fit=False), t=1.0, hold=2.5)
        b.step(st.show("note", eq(r"\text{slope } 1.06,\;\; r = 0.75", 30, GREEN)),
               t=0.9, hold=3)
        b.step(st.show("note", note("slope one: inflation almost exactly proportional "
                                    "to money growth", GREEN)), t=0.8, hold=3)
        b.step(st.clear("main", "note") + st.show("main", lessons), t=1.0, hold=3)
        b.step(st.show("note", note("the fit is tightest among high-inflation "
                                    "countries, loosest among low-inflation ones")),
               t=0.8, hold=3)
        b.step(st.show("note", note("velocity does move, but its movement is small "
                                    "next to the movement in money at violent rates",
                                    GREY)), t=0.8, hold=3)
        b.run()


class BeatSeventeen(Scene):
    """Brazil's IPCA and Selic, the Fisher relation made visible."""

    def construct(self):
        st = Stage(self)
        b = Beat(self, "BeatSeventeen")

        def parse(rows):
            return [(datetime.strptime(r["date"], "%d/%m/%Y"), float(r["value"]))
                    for r in rows]

        ipca = parse(read_csv("data/bcb_sgs_13522.csv"))
        selic = parse(read_csv("data/bcb_sgs_432.csv"))

        def draw(fig, ax):
            ax.plot([d for d, _ in ipca], [v for _, v in ipca],
                    color="#58C4DD", lw=1.8, label="IPCA, 12-month")
            ax.plot([d for d, _ in selic], [v for _, v in selic],
                    color="#FFFF00", lw=1.2, label="Selic target")
            ax.set_ylabel("per cent")
            ax.legend(facecolor="none", edgecolor="#e8ebef", labelcolor="#e8ebef",
                      fontsize=9, loc="upper left")
            ax.grid(alpha=.15, color="#e8ebef")

        fig = mpl_figure(draw, "brazil_ipca_selic", width=9.6)

        b.step(st.show("title", title("Brazil: two series, one story")), t=0.6, hold=1.5)
        b.step(st.show("note", note("blue: IPCA, inflation over twelve months, since "
                                    "2000")), t=0.7, hold=1.8)
        b.step(st.show("note", note("yellow: the Selic target, the policy rate")),
               t=0.7, hold=1.8)
        b.step(st.show("main", fig, fit=False), t=1.0, hold=2.5)
        b.step(st.show("note", note("watch them move together: the rate climbs "
                                    "above inflation, and follows it down")),
               t=0.8, hold=2.5)
        b.step(st.show("note", eq(r"i \approx r + \pi \quad \text{(Fisher)}", 32)),
               t=0.9, hold=2.5)
        b.step(st.show("note", note("a nominal rate is never a number you read on "
                                    "its own: it always contains an inflation "
                                    "forecast", YELLOW)), t=0.8, hold=3)
        b.step(st.show("note", note("the Selic has ranged from 2% to 26.5% in this "
                                    "period: not a small dial")), t=0.8, hold=2.5)
        b.step(st.show("note", note("at 14%, the Selic is the opportunity cost of "
                                    "holding money, not merely a return on bonds")),
               t=0.8, hold=3)
        b.step(st.show("note", eq(r"\text{high } i \Rightarrow \text{more trips, "
                                  r"smaller real balances}", 26, BLUE)), t=0.9, hold=2.5)
        b.step(st.show("note", note("the square root we derived earlier is the "
                                    "reason a high Selic is costly, with nothing to "
                                    "do with borrowing")), t=0.9, hold=3)
        b.step(st.show("title", title("One thing I am not showing, and why", GREY)),
               t=0.7, hold=1.5)
        b.step(st.show("note", note("no Brazilian monetary aggregate is on this "
                                    "chart")), t=0.7, hold=2)
        b.step(st.show("note", note("the data endpoint returns numbers with no "
                                    "series name")), t=0.7, hold=2.2)
        b.step(st.show("note", note("and the metadata service that would identify "
                                    "them is dead", RED)), t=0.7, hold=2.2)
        b.step(st.show("note", note("picking one and calling it the money stock "
                                    "would be a guess presented as a fact", RED)),
               t=0.8, hold=2.5)
        b.step(st.show("note", note("the cross-country evidence used a source that "
                                    "names its own series; this chart shows only "
                                    "what could be verified", GREY)), t=0.9, hold=3)
        b.run()


class BeatEighteen(Scene):
    """Seigniorage: the base as debt paying no interest, and its Laffer curve."""

    @staticmethod
    def _stack(items, slot, buff=0.34):
        g = VGroup(*items).arrange(DOWN, aligned_edge=LEFT, buff=buff)
        Stage.fit(g, slot)
        return items

    def construct(self):
        st = Stage(self)
        b = Beat(self, "BeatEighteen")

        bs = balance_sheet([("bonds, pay interest", GREEN)],
                           [("currency + reserves, no interest", RED)])

        gbc = self._stack([
            eq(r"G_t + (1+i)B_{t-1}", 28),
            eq(r"=\; T_t + (B_t - B_{t-1}) + (H_t - H_{t-1})", 26),
            eq(r"H_t - H_{t-1} \;\text{sits where debt sits}", 26, YELLOW),
            eq(r"\text{except it pays no interest}", 24, GREEN),
        ], "right", buff=0.45)

        tax = table(["the inflation tax", "equals"],
                   [("rate", "the rate money loses value"),
                    ("base", "real money balances, m^D")],
                   col_widths=[2.6, 5.2], font_size=21,
                   cell_colours={(0, 1): RED, (1, 1): BLUE})

        ax, panel = axes_panel([0, 150, 50], [0, 40, 10], x_label="inflation, per cent",
                              y_label="seigniorage revenue", width=7.6, height=4.0)
        xs = np.linspace(0, 150, 80)
        ys = xs * np.exp(-xs / 35)
        curve = series(ax, list(zip(xs, ys)), colour=YELLOW, width=5)
        peak_x = 35.0
        peak = Dot(ax.c2p(peak_x, peak_x * np.exp(-1)), color=RED, radius=0.07)
        peak_lab = Text("the hump", font_size=18, color=RED) \
            .next_to(peak, UP, buff=0.15)

        b.step(st.show("title", title("Seigniorage")), t=0.6, hold=1.5)
        b.step(st.show("note", note("why would a government want inflation? "
                                    "historically, for revenue")), t=0.7, hold=2.5)
        b.step(st.show("left", bs), t=1.2, hold=3)
        b.step(st.show("note", note("expanding the base: equal assets and "
                                    "liabilities, but only one side pays interest")),
               t=0.8, hold=3)
        b.step(st.show("note", note("a loan the government never repays, and pays "
                                    "no interest on")), t=0.8, hold=2.5)
        b.step(st.add_to("right", gbc[0]), t=0.8, hold=2)
        b.step(st.add_to("right", gbc[1]), t=0.9, hold=2.5)
        b.step(st.add_to("right", gbc[2]), t=0.9, hold=2.5)
        b.step(st.add_to("right", gbc[3]), t=0.8, hold=2.5)
        b.step(st.show("note", note("who is actually paying? nobody writes a "
                                    "cheque")), t=0.7, hold=2.5)
        b.step(st.clear("left", "right")
               + st.show("note", note("anyone holding money while it loses value "
                                      "hands purchasing power to the government",
                                      RED)), t=0.9, hold=3)
        b.step(st.show("note", note("that is why seigniorage is also called the "
                                    "inflation tax", YELLOW)), t=0.8, hold=2.5)
        b.step(st.show("main", tax), t=1.2, hold=3)
        b.step(st.show("note", note("to raise a lot, expand the base fast")),
               t=0.7, hold=2)
        b.step(st.show("note", note("fast expansion means high inflation, which "
                                    "means a high nominal rate, by Fisher")),
               t=0.8, hold=2.5)
        b.step(st.show("note", note("a high nominal rate means smaller real "
                                    "balances, by the very model we derived", RED)),
               t=0.9, hold=3)
        b.step(st.show("note", note("the tax base shrinks precisely because the "
                                    "rate went up", YELLOW)), t=0.8, hold=2.5)
        b.step(st.clear("main", "note") + st.show("main", panel, fit=False),
               t=1.0, hold=2)
        b.step(st.add_to("main", curve), t=1.3, hold=2.5)
        b.step(st.add_to("main", VGroup(peak, peak_lab)), t=0.9, hold=2.5)
        b.step(st.show("note", note("a Laffer curve, in inflation: past some rate, "
                                    "raising it further collects less", GREEN)),
               t=0.9, hold=3)
        b.step(st.show("note", note("hyperinflations are what the far side of that "
                                    "hump looks like", RED)), t=0.8, hold=2.5)
        b.step(st.show("note", note("a growing economy wants growing real balances: "
                                    "some seigniorage can be collected even at zero "
                                    "inflation", GREY)), t=0.9, hold=3)
        b.run()


class BeatNineteen(Scene):
    """Four costs: shoe leather, the Friedman rule, menu costs, uncertainty, banks."""

    @staticmethod
    def _stack(items, slot, buff=0.34):
        g = VGroup(*items).arrange(DOWN, aligned_edge=LEFT, buff=buff)
        Stage.fit(g, slot)
        return items

    def construct(self):
        st = Stage(self)
        b = Beat(self, "BeatNineteen")

        shoe = self._stack([
            eq(r"C = \sqrt{\dfrac{i\,Y\,F}{2}}", 32, YELLOW),
            eq(r"i = r+\pi \;\Rightarrow\; C = \sqrt{\dfrac{(r+\pi)\,Y\,F}{2}}", 26, GREEN),
        ], "left", buff=0.5)

        friedman = self._stack([
            eq(r"\text{set } i = 0", 30, YELLOW),
            eq(r"0 = r+\pi \;\Rightarrow\; \pi = -r", 30, RED),
        ], "right", buff=0.5)

        costs = table(["cost", "what it implies for inflation"],
                     [("1: shoe leather", "minimised by deflation, pi = -r"),
                      ("2: menu costs", "minimised at zero inflation"),
                      ("3: relative-price uncertainty", "rises with inflation"),
                      ("4: bank seigniorage", "rises with inflation")],
                     col_widths=[4.2, 5.4], font_size=20,
                     cell_colours={(0, 1): RED, (1, 1): YELLOW})

        line = NumberLine(x_range=[-4, 4, 1], length=8.0, color=GREY)
        a_fried = Arrow(line.n2p(-2) + UP * 0.8, line.n2p(-2), color=RED,
                        buff=0.05, stroke_width=5)
        l_fried = Text("Friedman: pi = -r", font_size=18, color=RED) \
            .next_to(a_fried, UP, buff=0.12)
        a_menu = Arrow(line.n2p(0) + UP * 0.8, line.n2p(0), color=YELLOW,
                      buff=0.05, stroke_width=5)
        l_menu = Text("menu costs: pi = 0", font_size=18, color=YELLOW) \
            .next_to(a_menu, UP, buff=0.12)
        arrows = VGroup(line, a_fried, l_fried, a_menu, l_menu)

        b.step(st.show("title", title("What inflation costs")), t=0.6, hold=1.5)
        b.step(st.show("note", note("four costs; the first we already derived "
                                    "without realising it")), t=0.7, hold=2.5)
        b.step(st.show("left", shoe[0], fit=False), t=1.0, hold=2.5)
        b.step(st.add_to("left", shoe[1]), t=0.9, hold=2.5)
        b.step(st.show("note", note("the total cost of trips to the bank rises "
                                    "with inflation directly")), t=0.8, hold=2.5)
        b.step(st.show("note", note("the shoe-leather cost: real, even though it "
                                    "looks trivial at low inflation", RED)),
               t=0.8, hold=3)
        b.step(st.show("right", friedman[0], fit=False), t=1.0, hold=2)
        b.step(st.add_to("right", friedman[1]), t=0.9, hold=2.5)
        b.step(st.show("note", note("the Friedman rule: a zero nominal rate "
                                    "requires deflation", YELLOW)), t=0.8, hold=3)
        b.step(st.show("note", note("a theoretical extreme, valuable for its "
                                    "logic, not a policy proposal", GREY)),
               t=0.8, hold=2.5)
        b.step(st.clear("left", "right")
               + st.show("note", note("cost two: menu costs consume real "
                                      "resources when prices are reprinted")),
               t=0.8, hold=2.5)
        b.step(st.show("main", arrows, fit=False), t=1.1, hold=3)
        b.step(st.show("note", note("two costs, two different optimal inflation "
                                    "rates: the chapter does not resolve it")),
               t=0.9, hold=3)
        b.step(st.clear("main")
               + st.show("note", note("cost three: a rough sense of what a unit "
                                      "of currency buys, eroded by inflation")),
               t=0.8, hold=2.5)
        b.step(st.show("note", note("like measuring with a ruler that keeps "
                                    "changing size", YELLOW)), t=0.8, hold=3)
        b.step(st.show("note", note("producers face the same problem setting "
                                    "their own prices")), t=0.7, hold=2.2)
        b.step(st.show("note", note("cost four: banks earn seigniorage too, "
                                    "paying deposits less as inflation rises")),
               t=0.8, hold=2.5)
        b.step(st.show("note", note("excessive entry into banking: real resources "
                                    "drawn in by a wedge inflation created")),
               t=0.8, hold=2.5)
        b.step(st.show("main", costs, fit=False), t=1.2, hold=3.5)
        b.run()


class BeatTwenty(Scene):
    """Neutral, not superneutral; then the seam to the sticky-price model."""

    @staticmethod
    def _stack(items, slot, buff=0.34):
        g = VGroup(*items).arrange(DOWN, aligned_edge=LEFT, buff=buff)
        Stage.fit(g, slot)
        return items

    def construct(self):
        st = Stage(self)
        b = Beat(self, "BeatTwenty")

        claims = table(["claim", "about", "this lecture"],
                      [("neutrality", "the level of M", "true, proved"),
                       ("superneutrality", "the growth rate of M", "false, refuted")],
                      col_widths=[3.0, 3.0, 3.2], font_size=21,
                      cell_colours={(0, 2): GREEN, (1, 2): RED})

        chain = self._stack([
            eq(r"\mu \uparrow \;\Rightarrow\; \pi \uparrow", 28),
            eq(r"\pi \uparrow \;\Rightarrow\; i = r+\pi \uparrow \;\;\text{(Fisher)}", 26),
            eq(r"i \uparrow \;\Rightarrow\; m^{D}(Y,i) \downarrow", 26, BLUE),
            eq(r"m^{D}\downarrow \;\Rightarrow\; \text{more trips to the bank}", 24),
            eq(r"\text{trips} \;\Rightarrow\; \text{real resources burned}", 26, RED),
        ], "left", buff=0.4)

        law = eq(r"\pi = \mu - \eta g", 44, GREEN)
        vals = table(["pi", "mu", "g", "eta"], [("2", "3.5", "3", "0.5")],
                    col_widths=[1.6, 1.6, 1.6, 1.6], font_size=22)
        law.move_to(UP * 1.2)
        vals.next_to(law, DOWN, buff=0.5)
        eta_note = note("eta = 1/2: economies of scale in managing cash", GREY, 18)

        b.step(st.show("title", title("Neutral, but not superneutral")), t=0.6, hold=1.5)
        b.step(st.show("note", note("the most common error made with this "
                                    "material")), t=0.7, hold=2)
        b.step(st.show("main", claims), t=1.2, hold=3)
        b.step(st.show("note", note("change the level once: nothing real happens, "
                                    "prices move in proportion", GREEN)),
               t=0.8, hold=2.5)
        b.step(st.show("note", note("keep it growing faster forever: this lecture "
                                    "says that is false", RED)), t=0.8, hold=2.5)
        b.step(st.clear("main", "note") + st.show("left", chain[0], fit=False),
               t=1.0, hold=2)
        b.step(st.add_to("left", chain[1]), t=0.9, hold=2.2)
        b.step(st.add_to("left", chain[2]), t=0.9, hold=2.2)
        b.step(st.add_to("left", chain[3]), t=0.9, hold=2.2)
        b.step(st.add_to("left", chain[4]), t=1.0, hold=2.5)
        b.step(st.show("note", note("the very same model where money is neutral "
                                    "has sustained inflation with real costs")),
               t=0.8, hold=3)
        b.step(st.show("note", note("not a contradiction: a level against a rate")),
               t=0.7, hold=2.5)
        b.step(st.clear("left", "note")
               + st.show("title", title("The honest limit", YELLOW)), t=0.7, hold=1.5)
        b.step(st.show("note", note("everything rested on one assumption: prices "
                                    "are free to move")), t=0.8, hold=2.5)
        b.step(st.show("note", note("that assumption made the price level the "
                                    "variable that adjusts")), t=0.8, hold=2.5)
        b.step(st.show("note", note("take it away: suppose p cannot move in the "
                                    "short run", RED)), t=0.8, hold=2.5)
        b.step(st.show("note", note("money supply must still equal money demand; "
                                    "something must give")), t=0.8, hold=2.5)
        b.step(st.show("note", note("the only candidates left: the interest rate "
                                    "and output")), t=0.8, hold=2.5)
        b.step(st.show("note", note("output: money stops being neutral and starts "
                                    "having real effects", RED)), t=0.9, hold=3)
        b.step(st.show("note", note("this chapter has no mechanism for that, and "
                                    "genuinely does not", GREY)), t=0.8, hold=2.5)
        b.step(st.show("note", note("name it: the sticky-price model, the next two "
                                    "lectures", YELLOW)), t=0.8, hold=2.5)
        b.step(st.clear("note") + st.show("main", law, fit=False), t=1.0, hold=2.5)
        b.step(st.add_to("main", vals), t=1.1, hold=3)
        b.step(st.show("aside", eta_note), t=0.8, hold=2.5)
        b.run()
