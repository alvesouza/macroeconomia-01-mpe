"""Scenes for aula-01-measuring-the-economy. One Scene per beat.

Durations come from beats.json, extended by PAUSE_S for every [pause] the script marks:
Speechify ignores intra-clip silence (verified - a clip with ellipses measures identically),
so the pauses are held frames at the end of the beat and explainer-compile pads the audio.

Colour roles, fixed for the whole video and declared in plan.md:
    BLUE   the object being measured          GREY   muted: derivation lines already past
    YELLOW the live line / object of attention RED    what breaks
    GREEN  the repaired object
"""
from manim import *
from video_explainer import (SLOTS, Beat, Stage, axes_panel, bullets, eq, load_beats,
                             mpl_figure, note, read_csv, series, side_by_side, table, title)

PAUSE_S = 2.5          # held silence per [pause] marker in script.md
FOCUS, MUTED, BROKEN, KEEP, OBJ = YELLOW, GREY, RED, GREEN, BLUE
_SECONDS, _PAUSES = None, None


def beat(scene, bid):
    """A Beat whose length is the measured narration plus its scripted silences."""
    global _SECONDS, _PAUSES
    if _SECONDS is None:
        import json
        data = json.loads(open("beats.json", encoding="utf-8").read())
        _SECONDS = {b["id"]: b["seconds"] for b in data["beats"]}
        _PAUSES = {b["id"]: b.get("pauses", 0) for b in data["beats"]}
    return Beat(scene, bid, beats={bid: _SECONDS[bid] + _PAUSES[bid] * PAUSE_S})


class Stack:
    """A column of equation lines on a FIXED grid: live line FOCUS, lines above MUTED.

    The grid is sized to the number of lines the scene will write (`rows`), so a line is
    never repositioned or rescaled after it is placed. An earlier version re-fitted the
    whole group on every line; each new line was then sized against an already-shrunken
    predecessor, the spacing collapsed, and the last two lines rendered on top of each
    other. Positions here are computed once, from the slot's own geometry.
    """

    def __init__(self, stage, size=36, rows=6, slot="main"):
        self.st, self.size, self.rows, self.slot = stage, size, rows, slot
        self.group = VGroup()
        box = SLOTS[slot]
        self.pitch = box["height"] / rows
        self.top = box["center"][1] + box["height"] / 2
        self.x = box["center"][0]

    def _place(self, line, row):
        box = SLOTS[self.slot]
        if line.width > box["width"]:
            line.scale_to_fit_width(box["width"])
        if line.height > self.pitch * 0.86:
            line.scale_to_fit_height(self.pitch * 0.86)
        return line.move_to([self.x, self.top - self.pitch * (row + 0.5), 0])

    def add(self, tex, colour=FOCUS, size=None):
        """Animations that mute the current live line and write `tex` on the next row."""
        line = eq(tex, size=size or self.size, colour=colour)
        row = len(self.group)
        if row == 0:
            self.group.add(line)
            anims = self.st.show(self.slot, self.group, fit=False)
            self._place(line, 0)      # show() recentres the slot's occupant; undo that
            return anims
        anims = [self.group[-1].animate.set_color(MUTED)]
        self._place(line, row)
        self.group.add(line)
        anims.append(FadeIn(line))
        return anims

    def collapse(self, tex, size=46):
        """Clear the column and re-show the result alone -- never carry muted lines on."""
        return self.st.show(self.slot, eq(tex, size=size, colour=KEEP))


# ------------------------------------------------------------------ Act 0

class BeatOpen(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatOpen")
        q = title("How much richer is the United States than Brazil?", size=34)
        rows = [("at the market exchange rate", "82,587", "10,378", "8.0x"),
                ("at purchasing power parity", "82,587", "21,193", "3.9x"),
                ("in welfare-equivalent consumption", "computed in Act V", "", "~8x")]
        t1 = table(["", "US", "Brazil", "ratio"], [rows[0], ("", "", "", ""), ("", "", "", "")],
                   col_widths=[5.0, 2.4, 2.4, 1.8])
        t2 = table(["", "US", "Brazil", "ratio"], [rows[0], rows[1], ("", "", "", "")],
                   col_widths=[5.0, 2.4, 2.4, 1.8])
        t3 = table(["", "US", "Brazil", "ratio"], rows, col_widths=[5.0, 2.4, 2.4, 1.8],
                   cell_colours={(0, 3): BROKEN, (1, 3): KEEP, (2, 3): FOCUS})
        b.step(st.show("title", title("How much richer is the United States", size=34)),
               t=0.8, hold=1)
        b.step(st.show("title", q), t=0.8, hold=2)
        b.step(st.show("main", table(["", "US", "Brazil", "ratio"],
                                     [("at the market exchange rate", "", "", "")],
                                     col_widths=[5.0, 2.4, 2.4, 1.8])), t=0.9, hold=2)
        b.step(st.show("main", t1), t=1.0, hold=3)
        b.step(st.show("note", note("World Bank, 2023 -- US$ per person")), t=0.6, hold=2)
        b.step(st.show("main", t2), t=1.0, hold=3)
        b.step(st.show("note", note("same year, same source, same two countries")), t=0.6, hold=3)
        b.step(st.show("main", t3), t=1.0, hold=3)
        b.step(st.show("note", note("eight, then four, then eight again")), t=0.6, hold=3)
        b.step(st.show("note", note("the third one we compute ourselves, in Act V")),
               t=0.6, hold=3)
        b.step(st.show("title", title("Three numbers. Not one of them is a mistake.", size=34)),
               t=0.8, hold=3)
        b.step(st.show("note", note("every number is a construction, and every construction "
                                    "is a choice")), t=0.8, hold=4)
        b.run()


# ------------------------------------------------------------------ Act I

class BeatFirmIdentity(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatFirmIdentity")
        s = Stack(st, size=34, rows=7)
        b.step(st.show("title", title("One firm, one year: where does the money go?")), t=0.8, hold=1)
        b.step(s.add(r"R_j", colour=OBJ), t=0.8, hold=1)
        b.step(st.show("note", note("R: sales revenue")), t=0.6, hold=2)
        b.step(s.add(r"R_j = M_j"), t=0.9, hold=2)
        b.step(st.show("note", note("M: bought from other firms -- steel, power, fertiliser")),
               t=0.6, hold=2)
        b.step(s.add(r"R_j = M_j + W_jL_j"), t=0.9, hold=2)
        b.step(s.add(r"R_j = M_j + W_jL_j + I^{nt}_j"), t=0.9, hold=2)
        b.step(s.add(r"R_j = M_j + W_jL_j + I^{nt}_j + D_j"), t=0.9, hold=2)
        b.step(s.add(r"R_j = M_j + W_jL_j + I^{nt}_j + D_j + T_j"), t=0.9, hold=2)
        b.step(s.add(r"R_j = M_j + W_jL_j + I^{nt}_j + D_j + T_j + \Pi_j"), t=1.0, hold=3)
        b.step(st.show("note", note("profit is DEFINED as the residual -- so this is an "
                                    "identity, not an assumption")), t=0.8, hold=3)
        b.step(s.collapse(r"\underbrace{R_j - M_j}_{\text{value added}} = "
                          r"W_jL_j + I^{nt}_j + D_j + T_j + \Pi_j", size=40), t=1.4, hold=4)
        b.step(st.show("note", note("left: production.   right: payments to people.   "
                                    "the same sum, regrouped")), t=0.8, hold=4)
        b.step(st.show("note", note("and that is why depreciation sits on the income side: "
                                    "GDP is GROSS")), t=0.8, hold=3)
        b.run()


class BeatTelescope(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatTelescope")
        wrong = VGroup(eq(r"0.80 + 1.00 = 1.80", size=52, colour=BROKEN),
                       Text("add up what everybody sold", font_size=24, color=MUTED)
                       ).arrange(DOWN, buff=0.45)
        right = VGroup(eq(r"\underbrace{0.80}_{\text{plant}} + "
                          r"\underbrace{0.20}_{\text{farmer}} = 1.00", size=48, colour=KEEP),
                       Text("value added: revenue minus what was bought in",
                            font_size=24, color=MUTED)).arrange(DOWN, buff=0.45)
        s = Stack(st, size=38, rows=5)
        b.step(st.show("title", title("Fertiliser 0.80, lettuce 1.00. What was produced?")),
               t=0.8, hold=1)
        b.step(st.show("main", wrong), t=0.9, hold=3)
        b.step(st.show("note", note("but only one head of lettuce left the system, "
                                    "and it is worth one dollar")), t=0.8, hold=3)
        b.step(st.show("note", note("the fertiliser was counted twice -- once as itself, "
                                    "once inside the lettuce")), t=0.8, hold=3)
        b.step(st.show("main", right), t=1.0, hold=4)
        b.step(st.show("title", title("And it is not a lucky example")), t=0.8, hold=1)
        b.step(s.add(r"\sum_{j=1}^{n}\left(R_j - M_j\right)"), t=0.9, hold=2)
        b.step(s.add(r"M_j = R_{j-1}\quad\text{(each firm buys the last one's output)}",
                     size=30), t=0.9, hold=2)
        b.step(s.add(r"\sum_{j=1}^{n}\left(R_j - R_{j-1}\right)"), t=0.9, hold=2)
        b.step(s.add(r"= (R_1 - R_0) + (R_2 - R_1) + \cdots + (R_n - R_{n-1})", size=32),
               t=1.0, hold=3)
        b.step(s.add(r"= R_n \qquad (R_0 = 0)", colour=KEEP), t=1.0, hold=3)
        b.step(st.show("note", note("total value added = the value of final output. "
                                    "The telescoping IS the theorem")), t=0.8, hold=4)
        b.run()


class BeatExpenditure(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatExpenditure")
        s = Stack(st, size=40, rows=5)
        ledger = table(["", "production", "expenditure"],
                       [("car", "20 - 5 = 15", "C = 20"),
                        ("components kept", "", "I = 5"),
                        ("lettuce", "2", "X = 2"),
                        ("imported components", "", "M = -10"),
                        ("total", "17", "17")],
                       col_widths=[4.2, 3.6, 3.6],
                       cell_colours={(1, 2): FOCUS, (4, 1): KEEP, (4, 2): KEEP})
        b.step(st.show("title", title("Who buys the output?")), t=0.8, hold=1)
        b.step(st.show("note", note("only four buyers exist: households, firms, "
                                    "government, foreigners")), t=0.7, hold=2)
        b.step(s.add(r"Y = C"), t=0.8, hold=2)
        b.step(s.add(r"Y = C + I"), t=0.8, hold=2)
        b.step(s.add(r"Y = C + I + G"), t=0.8, hold=2)
        b.step(s.add(r"Y = C + I + G + X"), t=0.8, hold=2)
        b.step(s.add(r"Y = C + I + G + X - M", colour=KEEP), t=1.0, hold=3)
        b.step(st.show("note", note("the minus sign does NOT mean imports reduce output")),
               t=0.7, hold=3)
        b.step(st.show("note", note("C, I, G and X are measured at what buyers paid -- "
                                    "and some of that was made abroad")), t=0.8, hold=4)
        b.step(st.show("title", title("Kurlat, Example 1.6, p. 19")), t=0.8, hold=1)
        b.step(st.show("main", note("A manufacturer imports 10 of components.\n"
                                    "It puts half into a car and sells it for 20.\n"
                                    "The other 5 sit in the warehouse.\n"
                                    "A gardener exports 2 of lettuce.")), t=1.1, hold=4)
        b.step(st.show("main", ledger), t=1.2, hold=5)
        b.step(st.show("note", note("the 5 in the warehouse is an INVENTORY INVESTMENT -- "
                                    "without it the two sides read 17 and 12")), t=0.8, hold=4)
        b.step(st.show("note", note("sign trap: a drawdown is negative investment. "
                                    "GDP records the year of PRODUCTION")), t=0.8, hold=4)
        b.run()


class BeatConventions(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatConventions")
        head = ["", "the convention", "Kurlat"]
        r1 = ("transfers", "a pension changes no entry at all", "Ex. 1.8, p. 20")
        r2 = ("government", "valued at what it cost to provide", "Ex. 1.7, p. 20")
        r3 = ("durables", "consumed at purchase; housing imputed", "Ex. 1.5, p. 18")
        r4 = ("non-market", "excluded entirely", "Ex. 1.11, p. 22")
        blank = ("", "", "")
        w = [3.0, 6.2, 2.8]
        t1 = table(head, [r1, blank, blank, blank], col_widths=w)
        t2 = table(head, [r1, r2, blank, blank], col_widths=w)
        t3 = table(head, [r1, r2, r3, blank], col_widths=w)
        t4 = table(head, [r1, r2, r3, r4], col_widths=w)
        b.step(st.show("title", title("Four conventions -- decisions, not theorems")),
               t=0.8, hold=2)
        b.step(st.show("main", t1), t=1.0, hold=3)
        b.step(st.show("note", note("a pension of twenty thousand: how much output?")),
               t=0.7, hold=2)
        b.step(st.show("note", note("purchasing power moved; nothing was produced")),
               t=0.7, hold=3)
        b.step(st.show("note", note("session 9's lump-sum transfer does exactly this")),
               t=0.7, hold=2)
        b.step(st.show("main", t2), t=0.9, hold=3)
        b.step(st.show("note", note("a teacher paid 85,000 and a concert costing 85,000 "
                                    "count the same")), t=0.8, hold=3)
        b.step(st.show("note", note("consequence: measured government productivity growth "
                                    "is zero BY CONSTRUCTION")), t=0.8, hold=4)
        b.step(st.show("main", t3), t=0.9, hold=3)
        b.step(st.show("note", note("a television: consumed once. A house: investment, "
                                    "then a rent imputed every year after")), t=0.8, hold=3)
        b.step(st.show("note", note("imputed owner-occupier rent is nearly 8% of US GDP")),
               t=0.7, hold=3)
        b.step(st.show("note", note("without it, output would FALL when a renter buys "
                                    "their own home")), t=0.8, hold=3)
        b.step(st.show("main", t4), t=0.9, hold=3)
        b.step(st.show("note", note("two neighbours paid: 50 dollars of output. "
                                    "The same two mowing their own lawns: nothing")),
               t=0.8, hold=4)
        b.step(st.show("note", note("the largest gap between this number and welfare -- "
                                    "and Act V puts a price on it")), t=0.8, hold=3)
        b.run()


class BeatGNP(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatGNP")
        s = Stack(st, size=38, rows=3)
        flows = table(["stock (a level)", "flow (a rate)"],
                      [("capital K", "investment I"), ("wealth", "saving"),
                       ("debt B", "deficit B - B(-1)"), ("money M", "money growth")],
                      col_widths=[4.6, 4.6])
        b.step(st.show("title", title("Territory, or ownership?")), t=0.8, hold=1)
        b.step(st.show("note", note("the distinction the international comparisons "
                                    "will need")), t=0.7, hold=2)
        b.step(s.add(r"\text{GDP: produced inside the borders}", size=30, colour=OBJ),
               t=0.8, hold=2)
        b.step(s.add(r"\text{GNP: earned by residents, wherever}", size=30, colour=OBJ),
               t=0.8, hold=2)
        b.step(s.add(r"\mathrm{GNP} = \mathrm{GDP} + F^{out} - F^{in}", colour=KEEP),
               t=1.0, hold=3)
        b.step(st.show("note", note("Ireland: profit produced there, accruing abroad -- "
                                    "GNP runs 15-20% below GDP")), t=0.8, hold=4)
        b.step(st.show("note", note("which is why the HDI, in Act V, uses national income")),
               t=0.7, hold=3)
        b.step(st.show("title", title("Keep stocks and flows apart")), t=0.8, hold=1)
        b.step(st.show("main", flows), t=1.2, hold=4)
        b.step(st.show("main", eq(r"K_{t+1} = (1-\delta)K_t + I_t", size=52, colour=OBJ)),
               t=1.2, hold=4)
        b.step(st.show("note", note("this one line is the entire engine of session 2")),
               t=0.7, hold=3)
        b.step(st.show("note", note("and its depreciation is the same D that sat on the "
                                    "income side three beats ago")), t=0.8, hold=3)
        b.run()


# ------------------------------------------------------------------ Act II

class BeatExpandia(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatExpandia")
        data = table(["Expandia", "2017 price", "2017 qty", "2018 price", "2018 qty"],
                     [("wheat", "50", "10", "60", "11"),
                      ("computers", "1,000", "1", "600", "2")],
                     col_widths=[2.8, 2.4, 2.2, 2.4, 2.2])
        s = Stack(st, size=34, rows=4)
        b.step(st.show("title", title("Kurlat, Example 1.13, p. 23")), t=0.8, hold=1)
        b.step(st.show("main", data), t=1.2, hold=4)
        b.step(st.show("note", note("agriculture grew 10%, manufacturing 100%. "
                                    "So what grew in aggregate?")), t=0.8, hold=3)
        b.step(st.show("title", title("Hold prices fixed -- but WHICH prices?")), t=0.8, hold=2)
        b.step(st.show("note", note("the standard repair: let only quantities move")),
               t=0.7, hold=2)
        b.step(s.add(r"\text{at 2017 prices:}\;\; 11(50) + 2(1000) = 2550", size=32),
               t=1.0, hold=3)
        b.step(s.add(r"g^{I} = \frac{2550}{1500} - 1 = 0.70", colour=FOCUS), t=1.0, hold=3)
        b.step(s.add(r"\text{at 2018 prices:}\;\; 10(60) + 1(600) = 1200", size=32),
               t=1.0, hold=3)
        b.step(s.add(r"g^{F} = \frac{1860}{1200} - 1 = 0.55", colour=FOCUS), t=1.0, hold=3)
        b.step(st.show("note", note("70 per cent, or 55 per cent")), t=0.7, hold=3)
        b.step(st.show("note", note("same country, same data, same arithmetic -- "
                                    "fifteen points decided by the choice of base")),
               t=0.8, hold=4)
        b.step(st.show("note", note("so: can we say which is larger BEFORE computing?")),
               t=0.8, hold=3)
        b.run()


class BeatCovariance(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatCovariance")
        s = Stack(st, size=32, rows=7)
        b.step(st.show("title", title("The gap between the two bases is a covariance")),
               t=0.8, hold=1)
        b.step(s.add(r"1+g^{I} = Q^{L} = \frac{\sum_i p_{i0}q_{i1}}{\sum_i p_{i0}q_{i0}}"),
               t=1.0, hold=2)
        b.step(s.add(r"1+g^{F} = Q^{P} = \frac{\sum_i p_{i1}q_{i1}}{\sum_i p_{i1}q_{i0}}"),
               t=1.0, hold=2)
        b.step(st.show("note", note("Laspeyres and Paasche quantity indices")), t=0.6, hold=2)
        b.step(s.add(r"s_{i0} = \frac{p_{i0}q_{i0}}{\sum_j p_{j0}q_{j0}},\quad "
                     r"\hat q_i = \frac{q_{i1}}{q_{i0}},\quad \hat p_i = \frac{p_{i1}}{p_{i0}}",
                     size=30), t=1.2, hold=3)
        b.step(st.show("note", note("shares, and gross growth factors")), t=0.6, hold=2)
        b.step(s.add(r"Q^{L} = \sum_i s_{i0}\hat q_i"), t=1.0, hold=3)
        b.step(st.show("note", note("a plain share-weighted average of quantity growth")),
               t=0.7, hold=2)
        b.step(s.add(r"Q^{P} = \frac{\sum_i s_{i0}\hat p_i \hat q_i}{\sum_i s_{i0}\hat p_i}"),
               t=1.0, hold=3)
        b.step(st.show("note", note("the SAME average -- reweighted by price growth")),
               t=0.7, hold=3)
        b.step(s.add(r"Q^{P} - Q^{L} = \frac{\mathbb{E}_s[\hat p\hat q] - "
                     r"\mathbb{E}_s[\hat p]\,\mathbb{E}_s[\hat q]}{\mathbb{E}_s[\hat p]}",
                     size=30), t=1.4, hold=3)
        b.step(s.add(r"= \frac{\operatorname{Cov}_s(\hat p, \hat q)}{\mathbb{E}_s[\hat p]}",
                     colour=KEEP), t=1.2, hold=4)
        b.step(st.show("note", note("the denominator is positive, so the sign is the "
                                    "covariance's sign")), t=0.7, hold=3)
        b.step(s.collapse(r"\operatorname{Cov}_s(\hat p,\hat q) < 0 \iff Q^{P} < Q^{L} "
                          r"\iff g^{F} < g^{I}", size=40), t=1.2, hold=4)
        b.step(st.show("note", note("negative covariance = cheaper goods are the ones "
                                    "bought more. That is the demand curve")), t=0.8, hold=4)
        b.step(st.show("main", eq(r"\operatorname{Cov}_s = 1.24 - (0.80)(1.70) = -0.12,"
                                  r"\qquad \frac{-0.12}{0.80} = -0.15", size=36, colour=FOCUS)),
               t=1.2, hold=4)
        b.step(st.show("note", note("fifteen points, with the right sign, predicted before "
                                    "either index was computed")), t=0.8, hold=3)
        b.run()


class BeatFisher(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatFisher")
        s = Stack(st, size=34, rows=2)
        props = bullets(["bracketed: the geometric mean cannot escape the two answers",
                         "time reversal: run it backwards and it inverts exactly",
                         "factor reversal: price index x quantity index = value ratio"])
        b.step(st.show("title", title("Neither base is defensible")), t=0.8, hold=2)
        b.step(st.show("note", note("one overstates, the other understates, and we have "
                                    "proved which is which")), t=0.8, hold=3)
        b.step(st.show("title", title("Stop choosing a base: the Fisher ideal index")),
               t=0.8, hold=1)
        b.step(s.add(r"1+g_t = \left[(1+g^{I}_t)(1+g^{F}_t)\right]^{1/2}", colour=KEEP),
               t=1.1, hold=3)
        b.step(s.add(r"= \sqrt{1.70 \times 1.55} - 1 = 0.6233", size=32, colour=FOCUS),
               t=1.0, hold=3)
        b.step(st.show("note", note("between 0.55 and 0.70, as it must be")), t=0.7, hold=2)
        b.step(st.show("title", title("Why the GEOMETRIC mean?")), t=0.8, hold=1)
        b.step(st.show("main", props), t=1.2, hold=5)
        b.step(st.show("title", title("Why 'ideal' is earned: the factor-reversal test")),
               t=0.8, hold=1)
        s2 = Stack(st, size=30, rows=4)
        b.step(s2.add(r"P^{L}Q^{P} = \frac{\sum p_{i1}q_{i0}}{\sum p_{i0}q_{i0}}\cdot"
                      r"\frac{\sum p_{i1}q_{i1}}{\sum p_{i1}q_{i0}}"), t=1.3, hold=3)
        b.step(st.show("note", note("the mismatched sum -- new prices, old quantities -- "
                                    "cancels")), t=0.8, hold=3)
        b.step(s2.add(r"= \frac{\sum p_{i1}q_{i1}}{\sum p_{i0}q_{i0}} \equiv V", colour=FOCUS),
               t=1.1, hold=3)
        b.step(st.show("note", note("now the other way round -- and the OTHER mismatched "
                                    "sum cancels")), t=0.8, hold=3)
        b.step(s2.add(r"P^{P}Q^{L} = \frac{\sum p_{i1}q_{i1}}{\sum p_{i0}q_{i1}}\cdot"
                      r"\frac{\sum p_{i0}q_{i1}}{\sum p_{i0}q_{i0}} = V"), t=1.3, hold=3)
        b.step(s2.add(r"P^{F}Q^{F} = \sqrt{P^{L}Q^{P}\cdot P^{P}Q^{L}} = \sqrt{V^2} = V",
                      colour=KEEP), t=1.3, hold=4)
        b.step(st.show("note", note("the price paid: chained real components no longer add "
                                    "up -- hence the 'residual' line in the accounts")),
               t=0.8, hold=4)
        b.run()


class BeatBias(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatBias")
        s = Stack(st, size=34, rows=2)
        b.step(st.show("title", title("Now run the same argument on prices")), t=0.8, hold=1)
        b.step(st.show("note", note("swap the roles of price growth and quantity growth")),
               t=0.7, hold=2)
        b.step(s.add(r"P^{L} = \sum_i s_{i0}\hat p_i \quad\text{(a fixed basket: the CPI)}",
                     size=30), t=1.0, hold=3)
        b.step(s.add(r"P^{P} - P^{L} = \frac{\operatorname{Cov}_s(\hat q, \hat p)}"
                     r"{\mathbb{E}_s[\hat q]} < 0", size=32), t=1.2, hold=3)
        b.step(st.show("note", note("same covariance, same sign")), t=0.6, hold=2)
        b.step(s.collapse(r"P^{L} \;>\; P^{F} \;>\; P^{P}", size=54), t=1.2, hold=4)
        b.step(st.show("note", note("SUBSTITUTION BIAS -- a theorem, not a regularity")),
               t=0.7, hold=3)
        b.step(st.show("note", note("a fixed basket never lets the consumer walk away from "
                                    "what became expensive")), t=0.8, hold=4)
        s2 = Stack(st, size=34, rows=2)
        b.step(st.show("title", title("How big? Size it with CES demand")), t=0.8, hold=1)
        b.step(s2.add(r"\hat q_i \propto \hat p_i^{-\varepsilon}", size=36), t=0.9, hold=3)
        b.step(s2.add(r"\ln P^{L} - \ln P^{F} \simeq \tfrac{1}{2}\,\varepsilon\,"
                      r"\operatorname{Var}_s(\pi)", colour=KEEP), t=1.2, hold=4)
        b.step(st.show("note", note("it grows with price DISPERSION, not with average "
                                    "inflation")), t=0.8, hold=4)
        b.step(st.show("note", note("and at epsilon = 0 -- no substitution -- the bias is "
                                    "exactly zero")), t=0.8, hold=3)
        b.step(st.show("main", table(["Boskin Commission, 1996", "points per year"],
                                     [("total US CPI bias", "~1.1"),
                                      ("of which substitution", "~0.4"),
                                      ("quality and new goods", "the rest")],
                                     col_widths=[5.4, 3.6],
                                     cell_colours={(1, 1): KEEP})), t=1.2, hold=4)
        b.step(st.show("note", note("the theorem covers the middle row only: the others are "
                                    "failures of the basket, not of the weights")),
               t=0.8, hold=3)
        b.run()


class BeatDeflatorCPI(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatDeflatorCPI")
        comp = table(["", "GDP deflator", "CPI"],
                     [("basket", "what is produced", "a fixed basket bought"),
                      ("weights", "current -> Paasche", "base -> Laspeyres"),
                      ("imports", "excluded", "included"),
                      ("capital goods", "included", "excluded"),
                      ("revised?", "yes", "essentially never")],
                     col_widths=[2.8, 4.2, 4.2])

        def draw(fig, ax):
            rows = read_csv("data/wdi_fp_cpi_totl_zg.csv")
            dfl = read_csv("data/wdi_ny_gdp_defl_kd_zg.csv")
            def bra(rs):
                return {int(r["year"]): float(r["value"]) for r in rs
                        if r["iso3"] == "BRA" and r["value"] and 1996 <= int(r["year"]) <= 2023}
            c, d = bra(rows), bra(dfl)
            yrs = sorted(set(c) & set(d))
            ax.plot(yrs, [c[y] for y in yrs], lw=2.2, label="consumer prices")
            ax.plot(yrs, [d[y] for y in yrs], lw=2.2, label="GDP deflator")
            ax.fill_between(yrs, [c[y] for y in yrs], [d[y] for y in yrs], alpha=0.18)
            ax.set_ylabel("per cent a year"); ax.legend(frameon=False)
            ax.set_title("Brazil: what you buy against what we sell")

        chart = mpl_figure(draw, "brazil_cpi_vs_deflator", width=9.0)
        b.step(st.show("title", title("Two price indices, two questions")), t=0.8, hold=1)
        b.step(st.show("main", comp), t=1.2, hold=5)
        b.step(st.show("title", title("An oil IMPORTER sees a crude price spike")),
               t=0.8, hold=2)
        b.step(st.show("note", note("what happens to each index?")), t=0.6, hold=2)
        b.step(st.show("note", note("CPI rises: households buy petrol")), t=0.7, hold=3)
        b.step(st.show("note", note("deflator FALLS: imports enter output with a minus sign")),
               t=0.8, hold=4)
        b.step(st.show("note", note("opposite directions, same quarter, neither is broken")),
               t=0.8, hold=3)
        b.step(st.show("title", title("Brazil is the mirror: a commodity EXPORTER")),
               t=0.8, hold=2)
        b.step(st.show("main", chart), t=1.2, hold=5)
        b.step(st.show("note", note("2021: consumer prices 8.3, deflator 13.0")), t=0.7, hold=3)
        b.step(st.show("note", note("2010: 5.0 against 8.4 -- the wedge opens in every "
                                    "commodity boom")), t=0.8, hold=4)
        b.step(st.show("note", note("'Brazilian inflation was X' -- of what you bought, "
                                    "or of what we sold?")), t=0.8, hold=4)
        b.run()

# ------------------------------------------------------------------ Act III

class BeatLogs(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatLogs")
        s = Stack(st, size=34, rows=4)
        err = table(["g", "log rate", "error", "relative"],
                    [("0.01", "0.00995", "0.00005", "0.5%"),
                     ("0.05", "0.04879", "0.00121", "2.4%"),
                     ("0.10", "0.09531", "0.00469", "4.7%"),
                     ("0.50", "0.40546", "0.09454", "18.9%"),
                     ("2.00", "1.09861", "0.90139", "45.1%")],
                    col_widths=[2.2, 2.8, 2.6, 2.4],
                    cell_colours={(4, 3): BROKEN, (0, 3): KEEP})
        b.step(st.show("title", title("Three ways to say the same thing")), t=0.8, hold=1)
        b.step(s.add(r"Y_t = Y_{t-1}(1+g_t)"), t=0.9, hold=2)
        b.step(s.add(r"\frac{Y_t}{Y_{t-1}} = 1+g_t"), t=0.9, hold=2)
        b.step(s.add(r"\ln Y_t - \ln Y_{t-1} = \ln(1+g_t) \equiv \tilde g_t", colour=OBJ),
               t=1.1, hold=3)
        b.step(st.show("note", note("the log growth rate. The relation is EXACT")),
               t=0.7, hold=2)
        b.step(s.add(r"\tilde g = g - \frac{g^2}{2} + \frac{g^3}{3} - \cdots", size=36),
               t=1.1, hold=3)
        b.step(s.collapse(r"g - \tilde g \;\simeq\; \frac{g^2}{2}", size=54), t=1.2, hold=4)
        b.step(st.show("note", note("one term tells you when you may be careless")),
               t=0.7, hold=2)
        b.step(st.show("main", err), t=1.2, hold=5)
        b.step(st.show("note", note("fine for an annual rate; hopeless for a hyperinflation")),
               t=0.8, hold=3)
        b.step(st.show("note", note("which is why session 7 keeps the EXACT Fisher equation")),
               t=0.8, hold=3)
        b.step(st.show("note", note("and why Kurlat's Cagan demand, exercise 11.6, "
                                    "is in logs from line one")), t=0.8, hold=3)
        b.run()


class BeatProducts(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatProducts")
        s = Stack(st, size=36, rows=4)
        b.step(st.show("title", title("Products, ratios, powers")), t=0.8, hold=1)
        b.step(s.add(r"\ln(XZ) = \ln X + \ln Z"), t=0.9, hold=2)
        b.step(s.add(r"\frac{\dot{(XZ)}}{XZ} = \frac{\dot X}{X} + \frac{\dot Z}{Z}"),
               t=1.1, hold=3)
        b.step(s.add(r"g_{XZ} = g_X + g_Z", colour=KEEP), t=1.0, hold=3)
        b.step(st.show("note", note("exactly, in continuous time")), t=0.6, hold=2)
        b.step(s.add(r"g_{X/Z} = g_X - g_Z, \qquad g_{X^a} = a\,g_X", colour=KEEP),
               t=1.1, hold=3)
        b.step(st.show("title", title("What discrete time costs you")), t=0.8, hold=1)
        s2 = Stack(st, size=36, rows=3)
        b.step(s2.add(r"(1+g_X)(1+g_Z) = 1 + g_X + g_Z + g_Xg_Z"), t=1.2, hold=3)
        b.step(s2.add(r"\underbrace{g_Xg_Z}_{\text{cross term}}", colour=BROKEN, size=42),
               t=1.0, hold=3)
        b.step(s2.add(r"g_Y = 3\%,\; g_L = 1\% \;\Rightarrow\; g_{Y/L} = 1.98\%", size=34,
                      colour=FOCUS), t=1.2, hold=4)
        b.step(st.show("note", note("round it away -- but round it away knowingly")),
               t=0.7, hold=3)
        b.step(s2.collapse(r"Y = AK^{\alpha}L^{1-\alpha} \;\Rightarrow\; "
                           r"g_Y = g_A + \alpha g_K + (1-\alpha)g_L", size=40), t=1.3, hold=4)
        b.step(st.show("note", note("an identity, assuming nothing about behaviour -- "
                                    "session 3 solves it for g_A and calls the rest the "
                                    "Solow residual")), t=0.8, hold=4)
        b.run()


class BeatCAGR(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatCAGR")
        s = Stack(st, size=36, rows=3)
        b.step(st.show("title", title("Up fifty per cent, then down fifty. "
                                      "Average growth?")), t=0.8, hold=2)
        b.step(st.show("main", eq(r"\frac{+50\% + (-50\%)}{2} = 0", size=56, colour=BROKEN)),
               t=1.0, hold=4)
        b.step(st.show("note", note("100 -> 150 -> 75. You lost a quarter of your money")),
               t=0.8, hold=4)
        b.step(st.show("title", title("Growth multiplies; it does not add")), t=0.8, hold=1)
        b.step(s.add(r"\mathrm{CAGR} = \left(\frac{Y_T}{Y_0}\right)^{1/T} - 1"), t=1.0, hold=3)
        b.step(s.add(r"= \sqrt{1.5 \times 0.5} - 1 = -13.4\%", colour=KEEP), t=1.1, hold=4)
        b.step(s.add(r"\left(\prod_{t=1}^{T}(1+g_t)\right)^{1/T} \le "
                     r"\frac{1}{T}\sum_{t=1}^{T}(1+g_t)", size=32), t=1.3, hold=3)
        b.step(st.show("note", note("AM-GM: the arithmetic mean ALWAYS overstates realised "
                                    "growth, and the gap widens with volatility")),
               t=0.8, hold=4)
        b.step(st.show("note", note("hold on to that convexity -- it returns in Act V as "
                                    "the price of inequality")), t=0.8, hold=3)
        s2 = Stack(st, size=36, rows=2)
        b.step(st.show("title", title("The rule of seventy")), t=0.8, hold=1)
        b.step(s2.add(r"(1+g)^T = 2"), t=0.9, hold=2)
        b.step(s2.add(r"T = \frac{\ln 2}{\ln(1+g)} \simeq \frac{0.693}{g} "
                      r"= \frac{69.3}{100g}", colour=KEEP), t=1.3, hold=4)
        b.step(st.show("main", table(["growth", "rule of 70", "exact"],
                                     [("2%", "35.0", "35.0"), ("5%", "14.0", "14.2"),
                                      ("7%", "10.0", "10.2")], col_widths=[2.6, 3.0, 2.6])),
               t=1.2, hold=4)
        b.step(st.show("note", note("2% doubles income in a working life. 7% doubles it in "
                                    "a decade -- a factor of eleven in the same life")),
               t=0.8, hold=4)
        b.run()


class BeatLogScale(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatLogScale")

        def draw(fig, ax):
            rows = read_csv("data/wdi_ny_gdp_pcap_pp_kd.csv")
            def get(iso):
                return {int(r["year"]): float(r["value"]) for r in rows
                        if r["iso3"] == iso and r["value"] and 1990 <= int(r["year"]) <= 2023}
            br, us = get("BRA"), get("USA")
            yrs = sorted(set(br) & set(us))
            ax.semilogy(yrs, [us[y] for y in yrs], lw=2.4, label="United States")
            ax.semilogy(yrs, [br[y] for y in yrs], lw=2.4, label="Brazil")
            ax.set_ylabel("GDP per capita, PPP (log scale)")
            ax.legend(frameon=False)
            ax.set_title("Parallel lines are a constant ratio, not convergence")

        chart = mpl_figure(draw, "brazil_us_logscale", width=9.2)
        s = Stack(st, size=38, rows=1)
        b.step(st.show("title", title("Plot the log of output against time")), t=0.8, hold=1)
        b.step(s.add(r"\frac{d\ln Y}{dt} = \frac{\dot Y}{Y} = \tilde g", colour=KEEP),
               t=1.1, hold=3)
        b.step(st.show("note", note("the SLOPE is the growth rate -- not the change in output")),
               t=0.8, hold=3)
        b.step(st.show("note", note("1. a straight line is exponential growth")), t=0.7, hold=3)
        b.step(st.show("note", note("2. parallel lines: same rate, constant RATIO, "
                                    "no convergence")), t=0.8, hold=3)
        b.step(st.show("note", note("3. a line bending flat: growth slowing, level still "
                                    "rising")), t=0.8, hold=3)
        b.step(st.show("title", title("Brazil and the United States since 1990")),
               t=0.8, hold=1)
        b.step(st.show("main", chart), t=1.2, hold=6)
        b.step(st.show("note", note("Brazil compounded at 1.26% a year; the US at 1.58%")),
               t=0.8, hold=4)
        b.step(st.show("note", note("Brazil was 28.5% of US income in 1990. "
                                    "In 2023: 25.7%")), t=0.8, hold=4)
        b.step(st.show("note", note("thirty-three years, and the ratio went the wrong way")),
               t=0.8, hold=3)
        b.step(st.show("note", note("read the wrong axis and a permanent ratio looks like "
                                    "catching up")), t=0.8, hold=3)
        b.run()


# ------------------------------------------------------------------ Act IV

class BeatPPPproblem(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatPPPproblem")
        s = Stack(st, size=34, rows=4)
        b.step(st.show("title", title("Kurlat, Example 1.14, p. 25")), t=0.8, hold=1)
        b.step(s.add(r"\text{US: } \$20.5\text{tn},\; 327\text{m people} "
                     r"\Rightarrow \$62{,}700", size=30), t=1.1, hold=3)
        b.step(s.add(r"\text{Mexico: } 23.5\text{tn pesos},\; 127\text{m} "
                     r"\Rightarrow 185{,}000 \text{ pesos}", size=30), t=1.1, hold=3)
        b.step(st.show("note", note("not comparable: the units differ")), t=0.7, hold=2)
        b.step(s.add(r"\frac{185{,}000}{19} \simeq \$9{,}700", size=36), t=1.0, hold=3)
        b.step(s.add(r"\text{so Americans are } 6.5\times \text{ richer}", colour=BROKEN,
                     size=34), t=1.0, hold=4)
        b.step(st.show("note", note("and that conclusion is where the trouble starts")),
               t=0.7, hold=2)
        b.step(st.show("title", title("And here is the objection")), t=0.8, hold=2)
        b.step(st.show("main", note("A dollar converted into pesos buys MORE in Mexico.\n\n"
                                    "Low measured output, or low prices?\n\n"
                                    "The market rate cannot tell them apart.")),
               t=1.2, hold=5)
        b.step(st.show("note", note("the exchange rate is set by goods that CAN cross "
                                    "borders, and by financial flows")), t=0.8, hold=4)
        b.step(st.show("note", note("nobody arbitrages the price of a Mexican haircut -- "
                                    "you cannot ship a haircut")), t=0.8, hold=4)
        b.step(st.show("note", note("it answers 'how many pesos does a dollar buy'. "
                                    "We asked 'how much does a Mexican get'")), t=0.8, hold=3)
        b.run()


class BeatPPPconstruct(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatPPPconstruct")
        s = Stack(st, size=34, rows=3)
        b.step(st.show("title", title("The same repair as Act II")), t=0.8, hold=1)
        b.step(st.show("main", note("two YEARS not comparable: hold prices fixed.\n\n"
                                    "two COUNTRIES not comparable: hold prices fixed.")),
               t=1.1, hold=4)
        b.step(s.add(r"\mathrm{GDP}^{\mathrm{PPP}}_{\text{foreign}} = "
                     r"\sum_{i=1}^{N} p^{\mathrm{US}}_i\, q^{\,i}_{\text{foreign}}",
                     colour=KEEP), t=1.3, hold=4)
        b.step(st.show("note", note("the base-YEAR index with 'base year' replaced by "
                                    "'base country' -- Laspeyres in space")), t=0.8, hold=4)
        b.step(st.show("note", note("so it inherits the same ambiguity, which is why the "
                                    "Penn World Table is multilateral")), t=0.8, hold=4)
        b.step(s.add(r"\$9{,}700 \;\longrightarrow\; \$18{,}000", size=42, colour=FOCUS),
               t=1.1, hold=3)
        b.step(s.add(r"6.5\times \;\longrightarrow\; 3.5\times", size=42, colour=KEEP),
               t=1.1, hold=4)
        b.step(st.show("note", note("almost half the measured gap was never an output gap")),
               t=0.8, hold=4)
        s2 = Stack(st, size=34, rows=2)
        b.step(st.show("title", title("Two definitions fall out")), t=0.8, hold=1)
        b.step(s2.add(r"e^{\mathrm{PPP}} \equiv \frac{\mathrm{GDP}^{\mathrm{PPP}}}"
                      r"{\mathrm{GDP}\ \text{(local currency)}}", size=32), t=1.2, hold=3)
        b.step(s2.add(r"\mathcal{P} \equiv \frac{e^{\mathrm{PPP}}}{e^{\text{market}}} "
                      r"= 0.54 \quad\text{(Mexico)}", colour=KEEP), t=1.2, hold=4)
        b.step(st.show("note", note("the Big Mac index is this with a basket of one good")),
               t=0.7, hold=3)
        b.step(st.show("note", note("its 'defect' -- the price is mostly rent, wages and "
                                    "local services -- is the whole mechanism")), t=0.8, hold=3)
        b.run()


class BeatBalassaSetup(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatBalassaSetup")
        s = Stack(st, size=34, rows=3)
        b.step(st.show("title", title("Why are poor countries SYSTEMATICALLY cheap?")),
               t=0.8, hold=2)
        b.step(s.add(r"Y_T = A_T L_T \qquad\text{(tradables: shippable)}", size=30),
               t=1.0, hold=3)
        b.step(s.add(r"Y_N = A_N L_N \qquad\text{(non-tradables: haircuts, buses, rent)}",
                     size=30), t=1.0, hold=3)
        b.step(st.show("note", note("assumption 1: law of one price in tradables. "
                                    "Normalise that price to one")), t=0.8, hold=3)
        b.step(st.show("note", note("assumption 2: labour moves between sectors until wages "
                                    "are equal")), t=0.8, hold=3)
        b.step(st.show("note", note("competitive firms pay the value of the marginal "
                                    "product")), t=0.7, hold=2)
        b.step(s.add(r"W = P_T A_T = P_N A_N", colour=OBJ), t=1.1, hold=4)
        b.step(st.show("note", note("now divide one by the other, and watch what survives")),
               t=0.8, hold=3)
        b.step(s.collapse(r"\frac{P_N}{P_T} = \frac{A_T}{A_N}", size=60), t=1.4, hold=5)
        b.step(st.show("note", note("no preferences. no demand. no capital. no income")),
               t=0.8, hold=4)
        b.step(st.show("note", note("the relative price of a haircut is a pure TECHNOLOGY "
                                    "ratio")), t=0.8, hold=4)
        b.step(st.show("main", note("A country good at making tradables must pay high\n"
                                    "wages in tradables.\n\n"
                                    "Barbers do not get more productive - a haircut takes\n"
                                    "what it takes - but they must be paid near the\n"
                                    "factory wage, or they go to the factory.\n\n"
                                    "So haircuts are dear in rich countries BECAUSE the\n"
                                    "factories are good.")), t=1.3, hold=6)
        b.run()


class BeatBalassaPrediction(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatBalassaPrediction")
        s = Stack(st, size=34, rows=3)
        b.step(st.show("title", title("From a relative price to a price level")), t=0.8, hold=1)
        b.step(s.add(r"P = P_T^{1-\gamma}P_N^{\gamma}", size=38), t=1.0, hold=3)
        b.step(s.add(r"= \left(\frac{P_N}{P_T}\right)^{\gamma} "
                     r"= \left(\frac{A_T}{A_N}\right)^{\gamma}", colour=KEEP), t=1.3, hold=4)
        b.step(s.add(r"\ln \mathcal{P}_j = \gamma\left[\Delta\ln A_{T,j} - "
                     r"\Delta\ln A_{N,j}\right]", size=32), t=1.3, hold=4)
        b.step(st.show("note", note("poor countries: far behind in manufacturing, "
                                    "only a little behind in haircuts")), t=0.8, hold=4)
        b.step(s.collapse(r"\text{poorer} \Rightarrow \text{lower price level} "
                          r"\Rightarrow \text{market rate understates real output}", size=34),
               t=1.3, hold=5)
        b.step(st.show("note", note("and it understates MORE the poorer the country is")),
               t=0.8, hold=3)
        b.step(st.show("note", note("and it understates MORE the poorer the country is")),
               t=0.8, hold=3)
        b.step(st.show("title", title("Two things the slogan never says")), t=0.8, hold=1)
        b.step(st.show("main", note("1. It is the RATIO of productivities, not poverty.\n"
                                    "   Uniformly unproductive: same ratio, no effect.\n\n"
                                    "2. Gamma scales it. A small open economy that consumes\n"
                                    "   mostly tradables shows a weak effect; a large\n"
                                    "   continental one shows a strong one.")),
               t=1.3, hold=6)
        b.step(st.show("note", note("corollary: catching up in tradables means the price "
                                    "level RISES toward the US")), t=0.8, hold=4)
        b.step(st.show("note", note("so market-rate growth overstates real growth -- "
                                    "China in the 2000s")), t=0.8, hold=3)
        b.run()


class BeatDenominator(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatDenominator")
        s = Stack(st, size=34, rows=1)
        b.step(st.show("title", title("The trap hiding in the denominator")), t=0.8, hold=1)
        b.step(s.add(r"\frac{Y}{\text{Pop}} \;\ne\; \frac{Y}{\text{Employment}} "
                     r"\;\ne\; \frac{Y}{\text{Hours}}", size=36), t=1.2, hold=4)
        b.step(s.collapse(r"\frac{Y}{\text{Pop}} = \underbrace{\frac{Y}{H}}_{\text{per hour}}"
                          r"\times \underbrace{\frac{H}{E}}_{\text{hours per worker}}"
                          r"\times \underbrace{\frac{E}{\text{Pop}}}_{\text{employment rate}}",
                          size=42), t=1.4, hold=5)
        b.step(st.show("note", note("productivity, times how long each works, times "
                                    "how many work at all")), t=0.8, hold=3)
        b.step(st.show("title", title("France against the United States")), t=0.8, hold=1)
        b.step(st.show("note", note("output per HOUR: within a few per cent of the US")),
               t=0.8, hold=4)
        b.step(st.show("note", note("output per PERSON: roughly 25-30% lower")), t=0.8, hold=4)
        b.step(st.show("note", note("the whole gap is in the other two factors")),
               t=0.8, hold=3)
        b.step(st.show("main", note("French productivity is poor?      the first term says no\n\n"
                                    "France is poorer?                 in consumption, a little\n\n"
                                    "The French are worse off?         only if those hours are\n"
                                    "                                  unemployment, not holiday")),
               t=1.3, hold=6)
        b.step(st.show("note", note("is a short working year a loss, or a purchase?")),
               t=0.8, hold=3)
        b.step(st.show("note", note("session 5 models that choice; Act V puts a price on it")),
               t=0.8, hold=3)
        b.step(st.show("note", note("get the denominator wrong and a statement about leisure "
                                    "becomes a false statement about productivity")),
               t=0.8, hold=3)
        b.run()


# ------------------------------------------------------------------ Act V

class BeatHDI(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatHDI")
        s = Stack(st, size=32, rows=4)
        b.step(st.show("title", title("Answer one: pick what matters, and average it")),
               t=0.8, hold=1)
        b.step(s.add(r"I_{\text{life}} = \frac{\text{LE} - 20}{85 - 20}"), t=1.0, hold=3)
        b.step(s.add(r"I_{\text{educ}} = \frac{1}{2}\left[\frac{\text{mean years}}{15} + "
                     r"\frac{\text{expected years}}{18}\right]", size=30), t=1.2, hold=3)
        b.step(s.add(r"I_{\text{inc}} = \frac{\ln(\text{GNI}) - \ln 100}"
                     r"{\ln 75{,}000 - \ln 100}"), t=1.1, hold=3)
        b.step(s.add(r"\mathrm{HDI} = \left(I_{\text{life}}I_{\text{educ}}"
                     r"I_{\text{inc}}\right)^{1/3}", colour=KEEP), t=1.2, hold=4)
        b.step(st.show("note", note("the log on income -- and only income -- imposes "
                                    "diminishing returns")), t=0.8, hold=4)
        b.step(st.show("note", note("the other two are linear: a year of life worth the same "
                                    "at 45 as at 80")), t=0.8, hold=3)
        s2 = Stack(st, size=36, rows=1)
        b.step(st.show("note", note("each component rescaled onto zero-to-one by its "
                                    "own min and max")), t=0.8, hold=3)
        b.step(st.show("title", title("Why geometric, and not arithmetic?")), t=0.8, hold=1)
        b.step(s2.add(r"\ln \mathrm{HDI} = \tfrac{1}{3}\left(\ln I_{\text{life}} + "
                      r"\ln I_{\text{educ}} + \ln I_{\text{inc}}\right)", size=32),
               t=1.3, hold=4)
        b.step(st.show("note", note("the three become COMPLEMENTS: any one at zero sends the "
                                    "index to zero")), t=0.8, hold=4)
        b.step(st.show("note", note("an arithmetic mean would let a rich country buy its way "
                                    "past dying young. The UN switched in 2010")),
               t=0.8, hold=4)
        b.step(st.show("main", eq(r"\operatorname{corr}\left(\mathrm{HDI},\;"
                                  r"\text{GDP per capita}\right) = 0.94", size=48,
                                  colour=BROKEN)), t=1.2, hold=5)
        b.step(st.show("note", note("the index built to correct output mostly reproduces it")),
               t=0.8, hold=4)
        b.step(st.show("note", note("so: could we build a welfare measure out of THEORY "
                                    "instead of a list?")), t=0.8, hold=3)
        b.run()


class BeatRawls(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatRawls")
        s = Stack(st, size=32, rows=2)
        b.step(st.show("title", title("Answer two: ask what compensation makes you "
                                      "indifferent")), t=0.8, hold=2)
        b.step(st.show("main", note("Rawls will live one year in a country.\n\n"
                                    "He does not get to know WHO he will be.\n\n"
                                    "Option 1: the country we want to measure.\n"
                                    "Option 2: the United States, every consumption\n"
                                    "          multiplied by lambda.")), t=1.3, hold=6)
        b.step(st.show("note", note("rich or poor, employed or not, long-lived or not")),
               t=0.7, hold=3)
        b.step(s.add(r"u\!\left(\lambda c^{US}, l^{US}, a^{US}\right) = "
                     r"u\!\left(c^{j}, l^{j}, a^{j}\right)", colour=KEEP, size=34),
               t=1.3, hold=4)
        b.step(st.show("note", note("lambda is an EQUIVALENT VARIATION, not an index")),
               t=0.8, hold=3)
        b.step(st.show("note", note("so we need his preferences -- Kurlat's eq. 2.2.1")),
               t=0.7, hold=2)
        b.step(s.add(r"u(c,l,a) = \mathbb{E}\left[\left(\bar u + "
                     r"\frac{c^{1-\sigma}}{1-\sigma} - \theta(1-l)^2\right)a\right]",
                     size=32), t=1.4, hold=5)
        b.step(st.show("title", title("Four commitments, each doing work")), t=0.8, hold=1)
        b.step(st.show("note", note("1. consumption, not output -- he cannot eat a "
                                    "machine tool")), t=0.8, hold=4)
        b.step(st.show("note", note("investment and exports do not enter his year")),
               t=0.7, hold=3)
        b.step(st.show("note", note("2. the alive-indicator multiplies EVERYTHING, "
                                    "so u-bar decides how much mortality matters")),
               t=0.8, hold=4)
        b.step(st.show("note", note("3. work enters as a convex disutility -- so "
                                    "non-market time is finally valued")), t=0.8, hold=4)
        b.step(st.show("note", note("the formal answer to two neighbours mowing lawns")),
               t=0.7, hold=3)
        b.step(st.show("note", note("4. sigma is risk aversion AND, mechanically, "
                                    "aversion to inequality")), t=0.8, hold=4)
        b.step(st.show("main", note("Behind the veil, a spread-out consumption\n"
                                    "distribution simply IS risk.\n\n"
                                    "That equivalence is the cleverest move in the paper.")),
               t=1.2, hold=5)
        b.run()


class BeatJensen(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatJensen")
        ax, panel = axes_panel([0, 6, 1], [0, 2.2, 1], x_label="consumption")
        curve = ax.plot(lambda x: 0.9 * np.log(x + 0.6) + 0.55, x_range=[0.3, 5.7], color=OBJ)
        p1, p2 = ax.c2p(1.0, 0.9 * np.log(1.6) + 0.55), ax.c2p(5.0, 0.9 * np.log(5.6) + 0.55)
        chord = Line(p1, p2, color=FOCUS, stroke_width=4)
        mid = ax.c2p(3.0, 0.9 * np.log(3.6) + 0.55)
        midchord = Line(p1, p2).get_center()
        gap = DashedLine(midchord, mid, color=KEEP, stroke_width=4)
        b.step(st.show("title", title("The machinery underneath")), t=0.8, hold=1)
        b.step(st.show("main", panel), t=0.9, hold=2)
        b.step([Create(curve)], t=1.2, hold=3)
        b.step(st.show("note", note("a concave utility function")), t=0.6, hold=2)
        b.step(st.show("title", title("Jensen's inequality")), t=0.8, hold=1)
        b.step([FadeIn(Dot(p1, color=FOCUS, radius=0.07)),
                FadeIn(Dot(p2, color=FOCUS, radius=0.07))], t=0.7, hold=2)
        b.step([Create(chord)], t=1.0, hold=3)
        b.step(st.show("note", note("mark two consumption levels and join them")),
               t=0.6, hold=2)
        b.step([Create(gap)], t=0.9, hold=3)
        b.step(st.show("note", note("utility of the mean, above the mean of the utility")),
               t=0.8, hold=4)
        b.step(st.show("note", note("a certain average is preferred to the gamble -- "
                                    "which is what risk aversion means")), t=0.8, hold=4)
        b.step(st.show("main", note("\"It's wrong to say people dislike risk because their\n"
                                    "utility function is concave. Instead: we describe\n"
                                    "preferences with concave utility functions to capture\n"
                                    "the fact that people dislike risk.\n\n"
                                    "Do not put the mathematical cart before the\n"
                                    "conceptual horse.\"      - Kurlat, p. 35")),
               t=1.3, hold=6)
        b.run()


class BeatLambdaDerive(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatLambdaDerive")
        s = Stack(st, size=30, rows=3)
        b.step(st.show("title", title("Solve it, with sigma equal to one")), t=0.8, hold=1)
        b.step(st.show("note", note("Jones and Klenow's own choice -- the CONSERVATIVE one, "
                                    "so the smallest honest inequality penalty")),
               t=0.8, hold=3)
        b.step(s.add(r"u^{j} = e^{j}\left[\bar u + \mathbb{E}\ln c^{j} - "
                     r"\theta(1-l^{j})^2\right]"), t=1.3, hold=3)
        b.step(st.show("note", note("e is life expectancy over a hundred: the share of a "
                                    "full life actually lived")), t=0.8, hold=3)
        b.step(s.add(r"e^{US}\left[\bar u + \ln\lambda + \mathbb{E}\ln c^{US} - "
                     r"\theta(1-l^{US})^2\right] = u^{j}"), t=1.4, hold=4)
        b.step(st.show("note", note("scaling consumption by lambda just ADDS log lambda")),
               t=0.8, hold=3)
        b.step(s.add(r"\ln c \sim \mathcal{N}(\mu, s^2) \;\Rightarrow\; "
                     r"\mathbb{E}[\ln c] = \ln \mathbb{E}[c] - \tfrac{1}{2}s^2", colour=FOCUS),
               t=1.4, hold=4)
        b.step(st.show("note", note("Jensen's inequality, made quantitative")), t=0.7, hold=3)
        b.step(st.show("note", note("the same convexity that made the arithmetic mean lie "
                                    "in Act III -- in a second costume")), t=0.8, hold=4)
        b.step(s.collapse(r"\ln\lambda = \underbrace{\ln\frac{\bar c^{j}}{\bar c^{US}}}"
                          r"_{\text{consumption}} - "
                          r"\underbrace{\tfrac{1}{2}(s_j^2 - s_{US}^2)}_{\text{inequality}} - "
                          r"\underbrace{\theta\left[(1-l^{j})^2 - (1-l^{US})^2\right]}"
                          r"_{\text{leisure}} + \underbrace{\frac{e^{j}-e^{US}}{e^{US}}"
                          r"\left[\cdot\right]}_{\text{life}}", size=30), t=1.6, hold=6)
        b.step(st.show("note", note("four additive terms in logs")), t=0.7, hold=3)
        b.step(st.show("note", note("inequality priced at EXACTLY half the log variance -- "
                                    "and at sigma over two in general")), t=0.8, hold=4)
        b.run()


class BeatLambdaBrazil(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatLambdaBrazil")
        head = ["term", "Brazil vs US", "value"]
        w = [4.2, 4.6, 2.6]
        r1 = ("consumption", "11,496 against 50,571", "-1.481")
        r2 = ("inequality", "Gini 51.5 against 41.8", "-0.185")
        r3 = ("leisure", "no verified hours series", "omitted")
        r4 = ("life", "75.8 against 78.4 years", "-0.465")
        e = ("", "", "")
        b.step(st.show("title", title("Put Brazilian numbers in it")), t=0.8, hold=1)
        b.step(st.show("main", table(head, [r1, e, e, e], col_widths=w)), t=1.1, hold=4)
        b.step(st.show("note", note("household consumption per head, constant PPP -- "
                                    "a ratio of 0.23")), t=0.8, hold=3)
        b.step(st.show("main", table(head, [r1, r2, e, e], col_widths=w,
                                     cell_colours={(1, 2): FOCUS})), t=1.0, hold=4)
        b.step(st.show("note", note("under lognormality those Ginis are log standard "
                                    "deviations of 0.99 and 0.78")), t=0.8, hold=4)
        b.step(st.show("note", note("inequality alone costs Brazil about 17 per cent "
                                    "of measured consumption")), t=0.8, hold=4)
        b.step(st.show("main", table(head, [r1, r2, r3, e], col_widths=w)), t=1.0, hold=3)
        b.step(st.show("main", table(head, [r1, r2, r3, r4], col_widths=w,
                                     cell_colours={(3, 2): FOCUS})), t=1.0, hold=4)
        b.step(st.show("note", note("this term depends on u-bar, which has no market price. "
                                    "Reported at u-bar = 5")), t=0.8, hold=4)
        b.step(st.show("main", eq(r"\lambda \simeq 0.12", size=64, colour=KEEP)),
               t=1.2, hold=5)
        b.step(st.show("note", note("market rate: 8 times.  PPP: 3.9 times.  "
                                    "welfare: back to 8")), t=0.8, hold=5)
        b.step(st.show("note", note("Western Europe gains 20-35%; poor countries lose. "
                                    "Correlation with GDP per head: 0.95")), t=0.8, hold=4)
        b.step(st.show("note", note("the HDI's lesson again -- from a utility function "
                                    "instead of a committee's list")), t=0.8, hold=3)
        b.run()


class BeatClose(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatClose")
        rungs = [("market exchange rate", "10,378", "convert"),
                 ("purchasing power parity", "21,193", "reweight"),
                 ("output per hour", "a different question", "re-denominate"),
                 ("consumption per head", "11,496", "re-base"),
                 ("welfare-equivalent, lambda", "~0.12 of the US", "price the risk")]
        head = ["Brazil, one year", "the number", "the construction"]
        w = [4.4, 4.2, 3.6]
        def upto(n, colours=None):
            rows = rungs[:n] + [("", "", "")] * (5 - n)
            return table(head, rows, col_widths=w, cell_colours=colours or {})
        b.step(st.show("title", title("One country. One year. Five numbers.")), t=0.8, hold=2)
        b.step(st.show("main", upto(1, {(0, 2): BROKEN})), t=1.0, hold=3)
        b.step(st.show("main", upto(2, {(1, 2): KEEP})), t=1.0, hold=3)
        b.step(st.show("main", upto(3)), t=1.0, hold=3)
        b.step(st.show("main", upto(4)), t=1.0, hold=3)
        b.step(st.show("main", upto(5, {(4, 2): FOCUS})), t=1.0, hold=5)
        b.step(st.show("note", note("not one of them is wrong. Each answers a different "
                                    "question")), t=0.8, hold=4)
        b.step(st.show("note", note("and each step between them is a construction "
                                    "somebody chose")), t=0.8, hold=3)
        b.step(st.show("title", title("Five signed statements, every one proved on screen")),
               t=0.8, hold=2)
        b.step(st.show("main", note("the early base gives the LARGER growth rate\n"
                                    "a fixed basket OVERSTATES inflation\n"
                                    "the market rate UNDERSTATES poor countries\n"
                                    "the arithmetic mean OVERSTATES growth\n"
                                    "the average CONCEALS inequality, at half the log "
                                    "variance")), t=1.3, hold=6)
        b.step(st.show("note", note("next session: we stop measuring and start explaining")),
               t=0.8, hold=3)
        b.step(st.show("title", title("Why is that Brazilian line below that American one?")),
               t=0.8, hold=3)
        b.run()
