"""Scenes for aula-02-solow. One Scene per beat.

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
        w = [6.0, 4.2]
        e = ("", "")
        r1 = ("Brazil invests, of what it produces", "18.3%")
        r2 = ("The United States invests", "21.3%")
        r3 = ("Brazilian income per head, vs American", "25.7%")
        r4 = ("What this model will predict", "92%")
        b.step(st.show("title", title("Two investment rates")), t=0.8, hold=1)
        b.step(st.show("main", table(["", ""], [r1, e, e, e], col_widths=w)), t=1.0, hold=3)
        b.step(st.show("main", table(["", ""], [r1, r2, e, e], col_widths=w)), t=1.0, hold=3)
        b.step(st.show("note", note("three percentage points apart")), t=0.7, hold=3)
        b.step(st.show("main", table(["", ""], [r1, r2, r3, e], col_widths=w,
                                     cell_colours={(2, 1): FOCUS})), t=1.0, hold=4)
        b.step(st.show("note", note("and an American is four times richer")), t=0.7, hold=4)
        b.step(st.show("title", title("Put those two rates into the model")), t=0.8, hold=2)
        b.step(st.show("main", table(["", ""], [r1, r2, r3, r4], col_widths=w,
                                     cell_colours={(2, 1): FOCUS, (3, 1): BROKEN})),
               t=1.0, hold=5)
        b.step(st.show("note", note("not twenty-six per cent. Ninety-two")), t=0.7, hold=4)
        b.step(st.show("note", note("out by a factor of three and a half")), t=0.7, hold=3)
        b.step(st.show("title", title("Where it fails is the interesting part")), t=0.8, hold=3)
        b.step(st.show("note", note("because what makes it fail is what makes it work")),
               t=0.8, hold=4)
        b.run()


# ------------------------------------------------------------------ Act I

class BeatVeryLongRun(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatVeryLongRun")
        ax, panel = axes_panel([0, 6, 1], [0, 4, 1], x_label="1300        1800        2000")
        flat = ax.plot(lambda x: 0.55 + 0.055 * x, x_range=[0.2, 3.4], color=OBJ)
        bend = ax.plot(lambda x: 0.55 + 0.055 * 3.4 + 1.05 * (x - 3.4),
                       x_range=[3.4, 5.6], color=OBJ)
        sub = DashedLine(ax.c2p(0.2, 0.42), ax.c2p(5.8, 0.42), color=MUTED)
        b.step(st.show("title", title("Output per person, United Kingdom, log scale")),
               t=0.8, hold=1)
        b.step(st.show("main", panel), t=0.9, hold=2)
        b.step(st.show("note", note("log scale: a straight line is a constant growth RATE, "
                                    "and the slope is that rate")), t=0.8, hold=3)
        b.step([Create(sub)], t=0.9, hold=2)
        b.step(st.show("note", note("subsistence: about $400 a year at today's prices")),
               t=0.7, hold=3)
        b.step(st.show("note", note("skeletal heights, livestock counts, crop yields, "
                                    "iron output")), t=0.8, hold=3)
        b.step([Create(flat)], t=1.4, hold=3)
        b.step(st.show("note", note("above subsistence, and growing -- slowly. "
                                    "And this reading is contested")), t=0.8, hold=3)
        b.step([Create(bend)], t=1.4, hold=4)
        b.step(st.show("note", note("the growth RATE itself changes. "
                                    "No settled answer as to why, or why Britain first")),
               t=0.8, hold=4)
        b.step(st.show("title", title("What orders countries today is the DATE of take-off")),
               t=0.8, hold=4)
        b.step(st.show("note", note("not the growth rate afterwards")), t=0.7, hold=3)
        b.run()


class BeatKaldor(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatKaldor")
        head = ["Kaldor, 1957", "United States"]
        w = [6.4, 4.6]
        e = ("", "")
        r1 = ("1. growth of output per person is constant", "~1.5% a year")
        r2 = ("   compounded over 216 years", "27x")
        r3 = ("2. the capital-output ratio is constant", "K/Y = 3.2")
        r4 = ("3. factor shares are constant", "labour 65%")
        b.step(st.show("title", title("Kaldor, 1957")), t=0.8, hold=1)
        b.step(st.show("note", note("a model is judged by the regularities it reproduces")),
               t=0.7, hold=2)
        b.step(st.show("title", title("Remarkable historical constancies")), t=0.8, hold=2)
        b.step(st.show("main", table(head, [r1, e, e, e], col_widths=w)), t=1.0, hold=3)
        b.step(st.show("main", table(head, [r1, r2, e, e], col_widths=w,
                                     cell_colours={(1, 1): FOCUS})), t=1.0, hold=3)
        b.step(st.show("note", note("check it: 1.015 to the 216 is about 25. "
                                    "The book's 27 implies 1.53%. Agrees to the rounding")),
               t=0.8, hold=4)
        b.step(st.show("main", table(head, [r1, r2, r3, e], col_widths=w)), t=1.0, hold=3)
        b.step(st.show("note", note("read it as: the capital America has accumulated is "
                                    "what it produces in three years")), t=0.8, hold=4)
        b.step(st.show("note", note("nobody OBSERVES the capital stock -- it is built by "
                                    "cumulating investment net of depreciation")),
               t=0.8, hold=4)
        b.step(st.show("note", note("which is this model's own accumulation identity, "
                                    "run forwards from a guess")), t=0.8, hold=4)
        b.step(st.show("main", table(head, [r1, r2, r3, r4], col_widths=w)), t=1.0, hold=3)
        b.step(st.show("note", note("stable until ~2000, then down about 3 points")),
               t=0.7, hold=3)
        b.step(st.show("title", title("And one genuine measurement problem")), t=0.8, hold=1)
        b.step(st.show("main", note("Proprietors' income: someone who owns AND works in\n"
                                    "their own small business.\n\n"
                                    "A return to their labour, or to their capital?\n\n"
                                    "The usual fix is to discard the whole category -- which\n"
                                    "assumes the split there matches the rest of the economy.")),
               t=1.2, hold=6)
        b.step(st.show("note", note("Kurlat: 'not entirely satisfactory'")), t=0.7, hold=3)
        b.run()


class BeatFactFour(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatFactFour")
        s = Stack(st, size=34, rows=4)
        b.step(st.show("title", title("Fact 4: the return on capital is constant")),
               t=0.8, hold=2)
        b.step(st.show("note", note("and it is not an independent fact at all")),
               t=0.7, hold=2)
        b.step(s.add(r"r \equiv \frac{\text{capital income}}{\text{capital stock}}"),
               t=1.1, hold=3)
        b.step(st.show("note", note("now divide top and bottom by GDP -- which looks like "
                                    "it achieves nothing")), t=0.8, hold=3)
        b.step(s.add(r"r = \frac{\text{capital income}/Y}{\text{capital stock}/Y}"),
               t=1.2, hold=3)
        b.step(st.show("note", note("numerator: the capital SHARE. Constant by fact 3")),
               t=0.7, hold=3)
        b.step(st.show("note", note("denominator: K/Y. Constant by fact 2")), t=0.7, hold=3)
        b.step(s.add(r"\text{a ratio of two constants is constant}", size=30, colour=KEEP),
               t=1.0, hold=3)
        b.step(s.collapse(r"r = \frac{1-\text{labour share}}{K/Y} "
                          r"= \frac{0.35}{3.2} \simeq 11\%", size=44), t=1.3, hold=4)
        b.step(st.show("note", note("but that is GROSS of depreciation -- the capital "
                                    "income measure includes it")), t=0.8, hold=4)
        b.step(st.show("main", eq(r"r_{\text{net}} = 11\% - \delta \simeq 6\%", size=52,
                                  colour=KEEP)), t=1.1, hold=4)
        b.step(st.show("note", note("six is the number for a calibration -- and it returns "
                                    "as the real interest rate in session 6")), t=0.8, hold=4)
        b.step(st.show("title", title("So why state it separately?")), t=0.8, hold=2)
        b.step(st.show("main", note("Because the PATH of the return on capital is what much\n"
                                    "of growth theory is about.\n\n"
                                    "Diminishing returns says it should FALL as capital\n"
                                    "accumulates. Across two centuries, it has not.\n\n"
                                    "A constraint, hiding as a redundancy.")), t=1.2, hold=6)
        b.run()


class BeatScatter(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatScatter")

        def draw(fig, ax):
            rows = read_csv("data/wdi_ny_gdp_pcap_pp_kd.csv")
            by = {}
            for r in rows:
                if r["value"] and len(r["iso3"]) == 3:
                    by.setdefault(r["iso3"], {})[int(r["year"])] = float(r["value"])
            xs, ys, marks = [], [], {}
            for iso, d in by.items():
                if 1990 in d and 2023 in d and d[1990] > 0:
                    g = ((d[2023] / d[1990]) ** (1 / 33) - 1) * 100
                    xs.append(d[1990]); ys.append(g)
                    if iso in ("BRA", "USA"):
                        marks[iso] = (d[1990], g)
            ax.scatter(xs, ys, s=14, alpha=0.55)
            for iso, (x, y) in marks.items():
                ax.scatter([x], [y], s=70)
                ax.annotate(iso, (x, y), textcoords="offset points", xytext=(7, 5))
            ax.set_xscale("log")
            ax.set_xlabel("income per head in 1990 (log scale)")
            ax.set_ylabel("growth since 1990, % a year")
            ax.axhline(0, lw=0.8, alpha=0.4)

        chart = mpl_figure(draw, "convergence_scatter", width=9.2)
        b.step(st.show("title", title("One last fact -- the one the model will fail")),
               t=0.8, hold=2)
        b.step(st.show("note", note("every country: growth since 1990, against income "
                                    "in 1990")), t=0.7, hold=2)
        b.step(st.show("title", title("Growth against initial income, every country")),
               t=0.8, hold=1)
        b.step(st.show("note", note("what shape SHOULD this be?")), t=0.7, hold=2)
        b.step(st.show("main", chart), t=1.2, hold=6)
        b.step(st.show("note", note("countries that started rich: bunched together, "
                                    "low variance")), t=0.8, hold=4)
        b.step(st.show("note", note("countries that started poor: sprayed everywhere")),
               t=0.8, hold=4)
        b.step(st.show("note", note("same starting income, utterly different outcomes")),
               t=0.8, hold=3)
        b.step(st.show("title", title("So what does this refute?")), t=0.8, hold=2)
        b.step(st.show("main", note("ABSOLUTE convergence -- poor countries grow faster,\n"
                                    "full stop -- would be a downward-sloping line.\n"
                                    "It is a cloud. Refuted.\n\n"
                                    "CONDITIONAL convergence -- each country approaches\n"
                                    "ITS OWN destination, faster the further below it --\n"
                                    "survives, because destinations differ.")),
               t=1.3, hold=6)
        b.step(st.show("note", note("we will DERIVE that distinction, not assert it")),
               t=0.8, hold=3)
        b.step(st.show("title", title("A second picture, a different question")),
               t=0.8, hold=2)
        b.step(st.show("main", note("Plot the DISTRIBUTION of incomes relative to the US,\n"
                                    "and watch it over time.\n\n"
                                    "Catching up would make it collapse to a point.\n"
                                    "It has not collapsed. Arguably it has spread, and\n"
                                    "become bimodal.\n\n"
                                    "The scatter asks: do poor countries grow faster?\n"
                                    "The distribution asks: is the world more equal?")),
               t=1.3, hold=6)
        b.step(st.show("note", note("they can disagree -- you want both in an exam answer")),
               t=0.8, hold=3)
        b.run()


# ------------------------------------------------------------------ Act II

class BeatCRS(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatCRS")
        head = ["assumption", "what it buys"]
        w = [5.0, 6.2]
        e = ("", "")
        r1 = ("4.1  constant returns to scale", "the per-worker form")
        r2 = ("4.2  positive marginal products", "f rises")
        r3 = ("4.3  diminishing marginal products", "THE engine of the model")
        r4 = ("4.4  Inada conditions", "a crossing exists at all")
        b.step(st.show("title", title("Eight assumptions; here are the first four")),
               t=0.8, hold=2)
        b.step(st.show("main", eq(r"Y_t = F(K_t, L_t)", size=52, colour=OBJ)), t=1.0, hold=3)
        b.step(st.show("main", table(head, [r1, e, e, e], col_widths=w)), t=1.0, hold=3)
        b.step(st.show("main", eq(r"F(\lambda K, \lambda L) = \lambda F(K,L)", size=46)),
               t=1.1, hold=3)
        b.step(st.show("note", note("exactly ONE step in the derivation uses it -- and "
                                    "without that step the model does not close")),
               t=0.8, hold=4)
        b.step(st.show("note", note("economically: REPLICATION. A second identical factory, "
                                    "a second identical workforce, twice the output")),
               t=0.8, hold=4)
        b.step(st.show("note", note("plausible for an economy; much less so for one firm "
                                    "with one irreplaceable manager")), t=0.8, hold=3)
        b.step(st.show("main", table(head, [r1, r2, r3, e], col_widths=w,
                                     cell_colours={(2, 1): FOCUS})), t=1.0, hold=4)
        b.step(st.show("note", note("the second machine adds less than the first")),
               t=0.7, hold=3)
        b.step(st.show("note", note("it is why accumulation cannot sustain growth, and why "
                                    "a country far below its destination grows fast")),
               t=0.8, hold=4)
        b.step(st.show("main", table(head, [r1, r2, r3, r4], col_widths=w)), t=1.0, hold=3)
        b.step(st.show("main", eq(r"\lim_{K\to0}F_K = \infty, \qquad "
                                  r"\lim_{K\to\infty}F_K = 0", size=42)), t=1.2, hold=4)
        b.step(st.show("note", note("with almost no capital, a little is priceless; with "
                                    "an enormous amount, nobody is left to operate it")),
               t=0.8, hold=4)
        b.step(st.show("title", title("Inada does NOT follow from diminishing returns")),
               t=0.8, hold=3)
        b.step(st.show("note", note("nor the reverse. They buy two different halves of "
                                    "one theorem -- Act IV")), t=0.8, hold=3)
        b.run()


class BeatCobbDouglas(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatCobbDouglas")
        s = Stack(st, size=32, rows=5)
        b.step(st.show("title", title("Cobb and Douglas, 1928")), t=0.8, hold=1)
        b.step(s.add(r"Y = K^{\alpha}L^{1-\alpha}", colour=OBJ), t=1.0, hold=3)
        b.step(st.show("note", note("Kurlat says 'easy to verify' and does not verify it")),
               t=0.8, hold=3)
        b.step(s.add(r"(\lambda K)^{\alpha}(\lambda L)^{1-\alpha} "
                     r"= \lambda^{\alpha + 1 - \alpha}K^{\alpha}L^{1-\alpha} = \lambda Y"),
               t=1.4, hold=4)
        b.step(st.show("note", note("constant returns to scale")), t=0.6, hold=2)
        b.step(s.add(r"F_K = \alpha K^{\alpha-1}L^{1-\alpha} = \alpha\frac{Y}{K} > 0"),
               t=1.3, hold=4)
        b.step(st.show("note", note("and the marginal product of labour is one minus alpha, "
                                    "times output over labour")), t=0.8, hold=3)
        b.step(s.add(r"F_{KK} = \alpha(\alpha-1)K^{\alpha-2}L^{1-\alpha} < 0"),
               t=1.3, hold=4)
        b.step(st.show("note", note("negative BECAUSE alpha is less than one")),
               t=0.7, hold=3)
        b.step(s.add(r"F_K = \alpha k^{\alpha-1}, \qquad \alpha - 1 < 0", colour=FOCUS),
               t=1.2, hold=4)
        b.step(st.show("note", note("a vanishing number to a negative power explodes; "
                                    "a huge one collapses")), t=0.8, hold=4)
        b.step(s.collapse(r"\text{all four} \iff 0 < \alpha < 1", size=48), t=1.2, hold=4)
        b.step(st.show("title", title("So what IS alpha?")), t=0.8, hold=3)
        b.run()


class BeatEuler(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatEuler")
        s = Stack(st, size=34, rows=3)
        s2 = Stack(st, size=34, rows=3)
        b.step(st.show("title", title("Pay each factor its marginal product")), t=0.8, hold=1)
        b.step(st.show("note", note("competitive factor markets -- proved properly in "
                                    "session 3")), t=0.7, hold=2)
        b.step(s.add(r"F_K \cdot K = \alpha\frac{Y}{K}\cdot K"), t=1.1, hold=3)
        b.step(s.add(r"= \alpha Y", colour=KEEP), t=1.0, hold=3)
        b.step(s.add(r"\frac{\text{capital income}}{Y} = \alpha, \qquad "
                     r"\frac{\text{labour income}}{Y} = 1-\alpha", size=30, colour=KEEP),
               t=1.3, hold=4)
        b.step(st.show("note", note("the two shares add to exactly one. Nothing left over, "
                                    "nothing missing")), t=0.8, hold=4)
        b.step(st.show("title", title("Not a coincidence: Euler's theorem")), t=0.8, hold=2)
        b.step(s2.add(r"F(\lambda K, \lambda L) = \lambda F(K,L)"), t=1.1, hold=3)
        b.step(st.show("note", note("differentiate both sides with respect to lambda")),
               t=0.7, hold=3)
        b.step(s2.add(r"F_K\cdot K + F_L\cdot L = F(K,L)", colour=KEEP), t=1.2, hold=4)
        b.step(st.show("note", note("set lambda to one. Factor payments exhaust output "
                                    "EXACTLY -- so competitive profit is exactly zero")),
               t=0.8, hold=4)
        b.step(st.show("main", eq(r"\text{labour share} \simeq 0.65 "
                                  r"\;\Longrightarrow\; \alpha \simeq 0.35", size=48,
                                  colour=FOCUS)), t=1.2, hold=4)
        b.step(st.show("note", note("a parameter in an abstract function turned out to be a "
                                    "number in a national accounts table")), t=0.8, hold=4)
        b.run()


class BeatSavingRate(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatSavingRate")
        s = Stack(st, size=34, rows=4)
        b.step(st.show("title", title("Assumption 4.5: population")), t=0.8, hold=1)
        b.step(st.show("main", eq(r"L_{t+1} = (1+n)L_t", size=52, colour=OBJ)), t=1.0, hold=3)
        b.step(st.show("note", note("Kurlat: 'actually a very big deal'")), t=0.7, hold=3)
        b.step(st.show("main", note("For most of history population growth was NOT\n"
                                    "exogenous -- it responded to living standards.\n\n"
                                    "With endogenous fertility (Exercise 4.5, p. 73) the\n"
                                    "model inverts: a productivity gain raises the NUMBER\n"
                                    "of people, not the income of each one.\n\n"
                                    "That is the model of the other 99% of human history.")),
               t=1.3, hold=6)
        b.step(st.show("note", note("and hidden inside 4.5: everybody works, so per worker "
                                    "= per capita. Session 5 separates them")), t=0.8, hold=4)
        b.step(st.show("title", title("4.6 closed economy, 4.7 exogenous saving")),
               t=0.8, hold=2)
        b.step(st.show("main", eq(r"Y = C + I", size=54, colour=OBJ)), t=1.0, hold=3)
        b.step(s.add(r"S \equiv Y - C = I \qquad \text{(an identity)}", size=30), t=1.2, hold=3)
        b.step(st.show("note", note("nothing can make that false in a closed economy")),
               t=0.7, hold=3)
        b.step(s.add(r"S = sY \qquad \text{(the behavioural assumption)}", size=30,
                     colour=FOCUS), t=1.2, hold=3)
        b.step(st.show("note", note("and it is the one the rest of the course dismantles: "
                                    "from session 4, s becomes a decision")), t=0.8, hold=4)
        b.step(st.show("title", title("S = I does NOT require G = 0")), t=0.8, hold=2)
        b.step(st.show("main", eq(r"S = \underbrace{(Y-\tau-C)}_{\text{private}} + "
                                  r"\underbrace{(\tau-G)}_{\text{public}} = Y-C-G = I",
                                  size=38, colour=KEEP)), t=1.4, hold=5)
        b.step(st.show("note", note("the taxes cancel. Government changes the LEVEL of "
                                    "saving, not the identity")), t=0.8, hold=4)
        b.step(st.show("main", eq(r"K_{t+1} = (1-\delta)K_t + I_t", size=50, colour=OBJ)),
               t=1.1, hold=4)
        b.step(st.show("note", note("assumption 4.8 -- and the same equation the "
                                    "statisticians use to BUILD the capital stock")),
               t=0.8, hold=3)
        b.run()

# ------------------------------------------------------------------ Act III

class BeatPerWorker(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatPerWorker")
        s = Stack(st, size=36, rows=4)
        b.step(st.show("title", title("The model has one moving part")), t=0.8, hold=1)
        b.step(st.show("main", eq(r"y \equiv \frac{Y}{L}, \qquad k \equiv \frac{K}{L}",
                                  size=50, colour=OBJ)), t=1.1, hold=3)
        b.step(s.add(r"y = \frac{F(K,L)}{L}"), t=1.0, hold=3)
        b.step(st.show("note", note("step 1: replace output with the production function")),
               t=0.7, hold=2)
        b.step(s.add(r"= F\!\left(\frac{K}{L}, 1\right)", colour=FOCUS), t=1.2, hold=4)
        b.step(st.show("note", note("step 2 -- the only substantive one: CRS with "
                                    "lambda = 1/L")), t=0.8, hold=4)
        b.step(s.add(r"\equiv f(k)", colour=KEEP), t=1.0, hold=3)
        b.step(st.show("note", note("step 3 is a definition")), t=0.6, hold=2)
        b.step(st.show("title", title("Output per worker depends on k alone")), t=0.8, hold=3)
        b.step(st.show("note", note("that is the entire payoff of constant returns")),
               t=0.7, hold=3)
        b.step(st.show("main", eq(r"f(k) = k^{\alpha}: \quad f' > 0,\; f'' < 0,\; "
                                  r"f'(0)=\infty,\; f'(\infty)=0", size=36, colour=OBJ)),
               t=1.3, hold=5)
        b.step(st.show("note", note("every property we verified, now in one variable")),
               t=0.7, hold=3)
        b.run()


class BeatLawOfMotion(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatLawOfMotion")
        s = Stack(st, size=30, rows=7)
        b.step(st.show("title", title("How does capital per worker move?")), t=0.8, hold=1)
        b.step(s.add(r"\Delta k_{t+1} \equiv k_{t+1} - k_t"), t=1.0, hold=3)
        b.step(s.add(r"= \frac{K_{t+1}}{L_{t+1}} - k_t"), t=1.1, hold=3)
        b.step(st.show("note", note("keep your eye on that subscript -- labour NEXT period. "
                                    "It is where everything goes wrong")), t=0.8, hold=4)
        b.step(s.add(r"= \frac{(1-\delta)K_t + I_t}{L_{t+1}} - k_t"), t=1.2, hold=3)
        b.step(st.show("note", note("the accumulation identity: what survived, plus what "
                                    "was built")), t=0.8, hold=3)
        b.step(s.add(r"= \frac{(1-\delta)K_t + sY_t}{L_{t+1}} - k_t"), t=1.2, hold=3)
        b.step(st.show("note", note("and the saving assumption")), t=0.6, hold=2)
        b.step(st.show("note", note("now the step that has to be done carefully")),
               t=0.7, hold=3)
        b.step(s.add(r"= \frac{(1-\delta)K_t + sY_t}{L_t}\cdot\frac{L_t}{L_{t+1}} - k_t",
                     colour=FOCUS), t=1.4, hold=4)
        b.step(st.show("note", note("multiply and divide by THIS period's labour")),
               t=0.7, hold=3)
        b.step(s.add(r"\frac{L_t}{L_{t+1}} = \frac{1}{1+n}", colour=FOCUS), t=1.1, hold=3)
        b.step(s.collapse(r"\Delta k_{t+1} = \frac{(1-\delta)k_t + s f(k_t)}{1+n} - k_t",
                          size=42), t=1.4, hold=5)
        b.step(st.show("note", note("the EXACT law of motion -- not an approximation")),
               t=0.7, hold=4)
        b.step(st.show("title", title("What is that 1+n doing down there?")), t=0.8, hold=2)
        b.step(st.show("main", note("Dilution.\n\n"
                                    "Next period there are more workers sharing the same\n"
                                    "pile of machines. Even if the pile grew, the pile\n"
                                    "PER WORKER may not have.\n\n"
                                    "Population growth dilutes capital exactly as water\n"
                                    "dilutes a solution -- and that division is how it\n"
                                    "enters.")), t=1.3, hold=6)
        b.run()


class BeatApproximation(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatApproximation")
        s = Stack(st, size=32, rows=4)
        b.step(st.show("title", title("Nobody writes it that way. Why?")), t=0.8, hold=1)
        b.step(s.add(r"\Delta k_{t+1} = \frac{(1-\delta)k_t + sf(k_t) - (1+n)k_t}{1+n}"),
               t=1.3, hold=4)
        b.step(st.show("note", note("everything over the common denominator")), t=0.7, hold=2)
        b.step(s.add(r"= \frac{sf(k_t) - (\delta+n)k_t}{1+n}", colour=KEEP), t=1.2, hold=4)
        b.step(s.add(r"\simeq \underbrace{sf(k_t)}_{\text{actual}} - "
                     r"\underbrace{(\delta+n)k_t}_{\text{break-even}}", colour=KEEP),
               t=1.4, hold=5)
        b.step(st.show("note", note("the famous equation, hiding under a division")),
               t=0.7, hold=3)
        b.step(st.show("title", title("The approximation is EXACT at the steady state")),
               t=0.8, hold=3)
        b.step(st.show("note", note("dividing by a positive number cannot move a zero")),
               t=0.8, hold=4)
        b.step(st.show("note", note("so 1+n affects the SPEED of travel, never the "
                                    "destination")), t=0.8, hold=4)
        b.step(st.show("note", note("forget it and you get the right steady state and the "
                                    "wrong path")), t=0.8, hold=3)
        b.step(st.show("main", eq(r"\Delta k^{\text{approx}} - \Delta k^{\text{exact}} = "
                                  r"\frac{n}{1+n}\left(sf - (\delta+n)k\right)", size=38,
                                  colour=FOCUS)), t=1.4, hold=5)
        b.step(st.show("note", note("at n = 1%, the simple form overstates each period's "
                                    "move by about 1% of that move")), t=0.8, hold=4)
        b.step(st.show("note", note("negligible in a year; visible over a fifty-year "
                                    "transition")), t=0.8, hold=3)
        b.run()


class BeatContinuous(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatContinuous")
        s = Stack(st, size=32, rows=5)
        b.step(st.show("title", title("A second route: continuous time")), t=0.8, hold=1)
        b.step(st.show("main", eq(r"k = \frac{K}{L}, \quad \text{both functions of time}",
                                  size=44, colour=OBJ)), t=1.1, hold=3)
        b.step(st.show("note", note("differentiate it")), t=0.6, hold=2)
        b.step(st.show("note", note("you need it because exam questions mix the two "
                                    "conventions freely")), t=0.8, hold=3)
        b.step(s.add(r"\dot k = \frac{d}{dt}\left(\frac{K}{L}\right) "
                     r"= \frac{\dot K L - K \dot L}{L^2}"), t=1.4, hold=4)
        b.step(st.show("note", note("the quotient rule")), t=0.6, hold=2)
        b.step(s.add(r"= \frac{\dot K}{L} - \frac{K}{L}\frac{\dot L}{L} "
                     r"= \frac{\dot K}{L} - nk"), t=1.4, hold=4)
        b.step(s.add(r"\dot K = sY - \delta K \;\Rightarrow\; "
                     r"\frac{\dot K}{L} = sf(k) - \delta k", size=30), t=1.4, hold=4)
        b.step(s.collapse(r"\dot k = s f(k) - (\delta + n)k", size=54), t=1.3, hold=5)
        b.step(st.show("note", note("now look back at what we called the approximation. "
                                    "They are the SAME equation")), t=0.8, hold=4)
        b.step(st.show("note", note("the 1/(1+n) is the entire difference between the two "
                                    "conventions")), t=0.8, hold=4)
        b.step(st.show("title", title("Which to use")), t=0.8, hold=1)
        b.step(st.show("main", note("Continuous time for anything analytic -- every proof\n"
                                    "in the next act is cleaner in it.\n\n"
                                    "Discrete time for anything you simulate or match to\n"
                                    "annual data.\n\n"
                                    "And always say which one you are in.")), t=1.2, hold=5)
        b.step(st.show("title", title("And notice the general technique")), t=0.8, hold=2)
        b.step(st.show("main", note("We differentiated a RATIO.\n\n"
                                    "Growth of a ratio = growth of the numerator minus\n"
                                    "growth of the denominator. Last session's rule.\n\n"
                                    "The -nk term is not special to capital: it is the\n"
                                    "denominator growing. Next session, per EFFICIENCY\n"
                                    "unit, the same term reappears with g added.")),
               t=1.3, hold=6)
        b.run()


class BeatGrowthRate(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatGrowthRate")
        ax, panel = axes_panel([0, 6, 1], [0, 3, 1], x_label="capital per worker, k")
        curve = ax.plot(lambda x: 2.4 * x ** (-0.55) if x > 0.15 else 5.0,
                        x_range=[0.35, 5.8], color=OBJ)
        line = DashedLine(ax.c2p(0, 1.0), ax.c2p(5.8, 1.0), color=KEEP)
        s = Stack(st, size=40, rows=2)
        b.step(st.show("title", title("Divide the whole equation by k")), t=0.8, hold=1)
        b.step(s.add(r"\frac{\dot k}{k} = \frac{s f(k)}{k} - (\delta+n)", colour=KEEP),
               t=1.3, hold=4)
        b.step(st.show("note", note("the left is now the GROWTH RATE of capital per worker")),
               t=0.8, hold=3)
        b.step(st.show("note", note("for Cobb-Douglas the first term is s k to the "
                                    "(alpha - 1) -- a negative exponent")), t=0.8, hold=3)
        b.step(st.show("main", panel), t=0.9, hold=2)
        b.step([Create(curve)], t=1.3, hold=3)
        b.step(st.show("note", note("strictly decreasing in k")), t=0.6, hold=2)
        b.step([Create(line)], t=1.0, hold=3)
        b.step(st.show("note", note("against a flat line")), t=0.6, hold=2)
        b.step(st.show("title", title("This picture IS conditional convergence")), t=0.8, hold=3)
        b.step(st.show("note", note("poorer economy, smaller k, higher curve, faster growth")),
               t=0.8, hold=4)
        b.step(st.show("main", eq(r"y = k^{\alpha} \;\Longrightarrow\; "
                                  r"\frac{\dot y}{y} = \alpha\frac{\dot k}{k}", size=48,
                                  colour=FOCUS)), t=1.2, hold=4)
        b.step(st.show("note", note("output always grows slower than capital, by exactly "
                                    "the capital share")), t=0.8, hold=4)
        b.step(st.show("note", note("and this is the object a growth regression is trying "
                                    "to recover -- session 3")), t=0.8, hold=3)
        b.run()


# ------------------------------------------------------------------ Act IV

class BeatDiagram(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatDiagram")
        ax, panel = axes_panel([0, 6, 1], [0, 3, 1], x_label="capital per worker, k")
        prod = ax.plot(lambda x: 1.65 * x ** (1 / 3), x_range=[0, 5.8], color=OBJ)
        inv = ax.plot(lambda x: 0.55 * 1.65 * x ** (1 / 3), x_range=[0, 5.8], color=FOCUS)
        brk = ax.plot(lambda x: 0.36 * x, x_range=[0, 5.8], color=KEEP)
        kss = (0.55 * 1.65 / 0.36) ** 1.5
        dot = Dot(ax.c2p(kss, 0.36 * kss), color=KEEP, radius=0.09)
        drop = DashedLine(ax.c2p(kss, 0), ax.c2p(kss, 0.36 * kss), color=MUTED)
        b.step(st.show("title", title("The picture the whole session lives in")),
               t=0.8, hold=1)
        b.step(st.show("main", panel), t=0.9, hold=2)
        b.step([Create(prod)], t=1.3, hold=3)
        b.step(st.show("note", note("f(k): rising, concave. That flattening IS diminishing "
                                    "returns, drawn")), t=0.8, hold=4)
        b.step([Create(inv)], t=1.2, hold=3)
        b.step(st.show("note", note("actual investment: the same curve, scaled by s")),
               t=0.7, hold=3)
        b.step([Create(brk)], t=1.2, hold=3)
        b.step(st.show("note", note("break-even investment: what you must invest to hold "
                                    "k STILL")), t=0.8, hold=4)
        b.step(st.show("main", side_by_side(panel.copy(), note(
            "Two reasons k falls on its own:\n\n"
            "  delta k  replaces machines that wore out\n\n"
            "  n k      equips the workers who arrived\n\n"
            "Both drain the same pool, so they add.")), fit=True), t=1.3, hold=6)
        b.step(st.show("title", title("So delta and n enter IDENTICALLY")), t=0.8, hold=3)
        b.step(st.show("note", note("a rise in depreciation and an equal rise in population "
                                    "growth are the same experiment")), t=0.8, hold=4)
        b.step(st.show("main", panel), t=0.9, hold=2)
        b.step([Create(dot), Create(drop)], t=1.1, hold=4)
        b.step(st.show("note", note("near zero the curve is above the line; far out the "
                                    "line wins. Somewhere between, they cross")),
               t=0.8, hold=4)
        b.run()


class BeatClosedForm(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatClosedForm")
        s = Stack(st, size=32, rows=5)
        b.step(st.show("title", title("Find the crossing exactly")), t=0.8, hold=1)
        b.step(s.add(r"s f(k_{ss}) = (\delta+n)k_{ss}"), t=1.1, hold=3)
        b.step(s.add(r"s k_{ss}^{\alpha} = (\delta+n)k_{ss}"), t=1.1, hold=3)
        b.step(st.show("note", note("divide both sides by k")), t=0.6, hold=2)
        b.step(s.add(r"k_{ss}^{\alpha-1} = \frac{\delta+n}{s}"), t=1.1, hold=3)
        b.step(s.add(r"k_{ss}^{1-\alpha} = \frac{s}{\delta+n}", colour=FOCUS), t=1.1, hold=3)
        b.step(s.collapse(r"k_{ss} = \left(\frac{s}{\delta+n}\right)^{\frac{1}{1-\alpha}},"
                          r"\quad y_{ss} = \left(\frac{s}{\delta+n}\right)"
                          r"^{\frac{\alpha}{1-\alpha}},\quad c_{ss} = (1-s)y_{ss}", size=34),
               t=1.5, hold=5)
        b.step(st.show("title", title("Do not memorise the exponents. Read them")),
               t=0.8, hold=2)
        b.step(st.show("main", table(["at alpha = 1/3", "exponent", "double s gives"],
                                     [("capital", "1/(1-a) = 1.5", "x 2.83"),
                                      ("output", "a/(1-a) = 0.5", "x 1.41")],
                                     col_widths=[3.4, 3.8, 3.2],
                                     cell_colours={(1, 1): FOCUS, (1, 2): FOCUS})),
               t=1.3, hold=6)
        b.step(st.show("note", note("capital nearly triples; output rises 40 per cent")),
               t=0.8, hold=4)
        b.step(st.show("note", note("why the difference? Diminishing returns -- each machine "
                                    "did less than the last")), t=0.8, hold=4)
        b.step(st.show("main", eq(r"\frac{d\ln y_{ss}}{d\ln s} = "
                                  r"\frac{\alpha}{1-\alpha} = \tfrac{1}{2}", size=56,
                                  colour=FOCUS)), t=1.2, hold=5)
        b.step(st.show("note", note("the most important elasticity in this session. "
                                    "In the last act we point it at Brazil")), t=0.8, hold=4)
        b.run()


class BeatExistence(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatExistence")
        s = Stack(st, size=32, rows=5)
        b.step(st.show("title", title("Kurlat argues from the picture. That is not a proof")),
               t=0.8, hold=2)
        b.step(st.show("main", note("A picture does not rule out three crossings.\n\n"
                                    "A picture does not rule out the economy leaping over\n"
                                    "the crossing and diverging.\n\n"
                                    "Here is what the picture assumes.")), t=1.2, hold=5)
        b.step(st.show("title", title("Define excess investment")), t=0.8, hold=1)
        b.step(s.add(r"\phi(k) \equiv s f(k) - (\delta+n)k", colour=OBJ), t=1.1, hold=3)
        b.step(st.show("note", note("a steady state is a positive root of phi")),
               t=0.7, hold=3)
        b.step(s.add(r"\frac{\phi(k)}{k} = \frac{s f(k)}{k} - (\delta+n)"), t=1.2, hold=3)
        b.step(st.show("note", note("as k goes to zero: f(k)/k is zero over zero")),
               t=0.7, hold=3)
        b.step(s.add(r"\lim_{k\to0}\frac{f(k)}{k} = \lim_{k\to0}f'(k) = \infty",
                     colour=FOCUS), t=1.3, hold=4)
        b.step(st.show("note", note("L'Hopital, then the FIRST Inada condition. "
                                    "So phi is positive near zero")), t=0.8, hold=4)
        b.step(s.add(r"\lim_{k\to\infty}\frac{f(k)}{k} = \lim_{k\to\infty}f'(k) = 0",
                     colour=FOCUS), t=1.3, hold=4)
        b.step(st.show("note", note("the SECOND Inada condition. So phi tends to "
                                    "minus (delta + n). Negative")), t=0.8, hold=4)
        b.step(s.collapse(r"\phi \text{ continuous},\; >0 \text{ somewhere},\; "
                          r"<0 \text{ somewhere} \;\Rightarrow\; \exists\, k_{ss}", size=34),
               t=1.4, hold=5)
        b.step(st.show("title", title("Existence is EXACTLY the two Inada conditions")),
               t=0.8, hold=4)
        b.step(st.show("main", note("We did not assume a steady state exists.\n"
                                    "We did not assume the diagram looks as it looks.\n\n"
                                    "We assumed something about the SLOPE at two extremes,\n"
                                    "and existence followed from continuity alone.\n\n"
                                    "Handed an unfamiliar production function: do not\n"
                                    "squint at the diagram. Check the two limits.")),
               t=1.3, hold=6)
        b.run()


class BeatUniqueness(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatUniqueness")
        s = Stack(st, size=32, rows=4)
        b.step(st.show("title", title("Existence is not enough: is it unique?")),
               t=0.8, hold=2)
        b.step(st.show("note", note("otherwise 'the steady state' is not a well-defined "
                                    "object")), t=0.8, hold=3)
        b.step(st.show("main", eq(r"\text{claim: } \frac{f(k)}{k}"
                                  r"\ \text{is strictly decreasing}", size=44, colour=OBJ)),
               t=1.1, hold=3)
        b.step(s.add(r"\frac{d}{dk}\left(\frac{f(k)}{k}\right) "
                     r"= \frac{f'(k)k - f(k)}{k^2}"), t=1.3, hold=4)
        b.step(st.show("note", note("quotient rule")), t=0.6, hold=2)
        b.step(st.show("note", note("the denominator is positive, so the sign is the "
                                    "numerator's")), t=0.8, hold=3)
        b.step(s.add(r"f(k) - f(0) = \int_0^k f'(x)\,dx \;>\; k\,f'(k)", colour=FOCUS),
               t=1.4, hold=4)
        b.step(st.show("note", note("every f' inside the integral is LARGER than f' at the "
                                    "endpoint, because f' is decreasing")), t=0.8, hold=4)
        b.step(st.show("note", note("geometrically: the chord from the origin lies above "
                                    "the tangent")), t=0.8, hold=4)
        b.step(s.collapse(r"\frac{f(k)}{k}\;\text{strictly decreasing}", size=48),
               t=1.2, hold=4)
        b.step(st.show("note", note("a strictly decreasing function crosses a constant "
                                    "AT MOST once")), t=0.8, hold=4)
        b.step(st.show("title", title("Uniqueness is EXACTLY diminishing returns")),
               t=0.8, hold=4)
        b.step(st.show("main", note("Inada:               at LEAST one crossing\n"
                                    "Diminishing returns: at MOST one crossing\n\n"
                                    "Together: exactly one.\n\n"
                                    "Two assumptions, two halves of one theorem -- which is\n"
                                    "why Kurlat was careful that neither implies the other.")),
               t=1.3, hold=6)
        b.step(st.show("note", note("and the general form: average product exceeds marginal "
                                    "product, so the average falls")), t=0.8, hold=3)
        b.run()


class BeatAK(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatAK")
        ax, panel = axes_panel([0, 6, 1], [0, 3, 1], x_label="capital per worker, k")
        sak = ax.plot(lambda x: 0.42 * x, x_range=[0, 5.8], color=BROKEN)
        brk = ax.plot(lambda x: 0.26 * x, x_range=[0, 5.8], color=KEEP)
        s = Stack(st, size=34, rows=3)
        b.step(st.show("title", title("Take diminishing returns away")), t=0.8, hold=2)
        b.step(s.add(r"f(k) = a\,k", colour=BROKEN), t=1.0, hold=3)
        b.step(st.show("note", note("positive marginal product -- but the second derivative "
                                    "is ZERO. No diminishing returns, no Inada")),
               t=0.8, hold=4)
        b.step(s.add(r"\phi(k) = s a k - (\delta+n)k"), t=1.1, hold=3)
        b.step(s.add(r"= \left[sa - (\delta+n)\right]k", colour=BROKEN), t=1.2, hold=4)
        b.step(st.show("note", note("proportional to k. A straight line through the origin")),
               t=0.8, hold=3)
        b.step(st.show("main", panel), t=0.9, hold=2)
        b.step([Create(sak)], t=1.1, hold=3)
        b.step([Create(brk)], t=1.1, hold=4)
        b.step(st.show("note", note("two straight lines through the origin. They never "
                                    "cross")), t=0.8, hold=4)
        b.step(st.show("main", note("If sa > delta + n: capital per worker grows at a\n"
                                    "constant rate, forever. No steady state.\n\n"
                                    "If sa < delta + n: the economy shrinks to nothing.\n\n"
                                    "This is the AK model, and in it raising s raises the\n"
                                    "growth rate PERMANENTLY.")), t=1.3, hold=6)
        b.step(st.show("title", title("So 'level not rate' is not a law of the universe")),
               t=0.8, hold=3)
        b.step(st.show("note", note("it is a consequence of assumption 4.3, and nothing "
                                    "else. Drop it and the conclusion reverses")),
               t=0.8, hold=4)
        b.run()


class BeatStability(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatStability")
        s = Stack(st, size=32, rows=4)
        s2 = Stack(st, size=32, rows=3)
        b.step(st.show("title", title("Does the economy actually get there?")), t=0.8, hold=1)
        b.step(s.add(r"k < k_{ss} \;\Rightarrow\; \frac{sf(k)}{k} > \delta+n "
                     r"\;\Rightarrow\; \dot k > 0"), t=1.4, hold=4)
        b.step(s.add(r"k > k_{ss} \;\Rightarrow\; \frac{sf(k)}{k} < \delta+n "
                     r"\;\Rightarrow\; \dot k < 0"), t=1.4, hold=4)
        b.step(st.show("note", note("because sf(k)/k is strictly decreasing, and equals "
                                    "delta+n exactly at the steady state")), t=0.8, hold=4)
        b.step(s.add(r"\text{monotone and bounded} \Rightarrow \text{converges}", size=30,
                     colour=KEEP), t=1.2, hold=4)
        b.step(st.show("note", note("and its limit must be a rest point, of which there is "
                                    "exactly one. That is a complete proof")), t=0.8, hold=4)
        b.step(st.show("note", note("note what the picture was quietly supplying: capital "
                                    "NEVER overshoots")), t=0.8, hold=4)
        b.step(st.show("title", title("Discrete time is not automatic")), t=0.8, hold=2)
        b.step(s2.add(r"G'(k) = \frac{(1-\delta) + s f'(k)}{1+n} > 0"), t=1.3, hold=4)
        b.step(st.show("note", note("every term positive, so G is increasing -- the path "
                                    "cannot oscillate at all")), t=0.8, hold=4)
        b.step(s2.add(r"G'(k_{ss}) < 1 \iff \alpha(\delta+n) < \delta+n", colour=KEEP),
               t=1.3, hold=4)
        b.step(st.show("note", note("which holds for any alpha below one. "
                                    "Assumption 4.3 again, doing the work again")),
               t=0.8, hold=4)
        b.step(st.show("main", eq(r"\lambda = (1-\alpha)(\delta+n) = \tfrac{2}{3}(0.06) "
                                  r"= 4\%\ \text{a year}", size=44, colour=FOCUS)),
               t=1.3, hold=5)
        b.step(st.show("note", note("a half-life of about SEVENTEEN YEARS to close half "
                                    "the remaining gap")), t=0.8, hold=5)
        b.run()

# ------------------------------------------------------------------ Act V

class BeatCompStatics(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatCompStatics")
        s = Stack(st, size=32, rows=3)
        head = ["shock", "k_ss", "y_ss", "long-run growth of y"]
        w = [3.0, 2.2, 2.2, 4.2]
        e = ("", "", "", "")
        r1 = ("s up", "up", "up", "0")
        r2 = ("n up", "down", "down", "0")
        r3 = ("delta up", "down", "down", "0")
        b.step(st.show("title", title("What happens if a country saves more?")),
               t=0.8, hold=1)
        b.step(st.show("note", note("differentiate the steady-state condition implicitly")),
               t=0.7, hold=2)
        b.step(s.add(r"\frac{\partial k_{ss}}{\partial s} = "
                     r"-\frac{\phi_s}{\phi_k} = \frac{f(k_{ss})}"
                     r"{(1-\alpha)(\delta+n)} > 0", colour=KEEP), t=1.5, hold=5)
        b.step(st.show("note", note("implicit differentiation -- and it works for ANY "
                                    "production function, not just Cobb-Douglas")),
               t=0.8, hold=4)
        b.step(s.add(r"\frac{\partial k_{ss}}{\partial n} = "
                     r"\frac{\partial k_{ss}}{\partial \delta} = "
                     r"-\frac{k_{ss}}{(1-\alpha)(\delta+n)} < 0", colour=FOCUS),
               t=1.5, hold=5)
        b.step(st.show("note", note("identical to each other -- n and delta are the same "
                                    "parameter wearing two names")), t=0.8, hold=4)
        b.step(st.show("main", eq(r"\frac{d\ln k_{ss}}{d\ln s} = \frac{1}{1-\alpha},"
                                  r"\qquad \frac{d\ln y_{ss}}{d\ln s} = "
                                  r"\frac{\alpha}{1-\alpha}", size=42)), t=1.3, hold=5)
        b.step(st.show("main", table(head, [r1, e, e], col_widths=w)), t=1.1, hold=3)
        b.step(st.show("main", table(head, [r1, r2, e], col_widths=w)), t=1.0, hold=3)
        b.step(st.show("main", table(head, [r1, r2, r3], col_widths=w,
                                     cell_colours={(0, 3): FOCUS, (1, 3): FOCUS,
                                                   (2, 3): FOCUS})), t=1.0, hold=5)
        b.step(st.show("title", title("Zero in every row")), t=0.8, hold=3)
        b.step(st.show("note", note("you can change where the economy ends up. You cannot "
                                    "change that it ends up somewhere and stops")),
               t=0.8, hold=5)
        b.run()


class BeatTransition(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatTransition")
        s = Stack(st, size=32, rows=3)
        b.step(st.show("title", title("So nothing happens? Let us compute what does")),
               t=0.8, hold=2)
        b.step(st.show("note", note("the saving rate rises permanently, from s-nought to "
                                    "s-one")), t=0.8, hold=3)
        b.step(st.show("title", title("On impact")), t=0.8, hold=1)
        b.step(st.show("main", note("k is a STOCK -- the accumulated result of the entire\n"
                                    "past. It cannot jump.\n\n"
                                    "y is a function of k, so output does not jump either.")),
               t=1.2, hold=5)
        b.step(s.add(r"\dot k_T = s_1 f(k_T) - (\delta+n)k_T = (s_1 - s_0)f(k_T) > 0",
                     size=30, colour=KEEP), t=1.5, hold=5)
        b.step(st.show("note", note("investment jumps at once -- same output, a bigger "
                                    "slice saved")), t=0.8, hold=4)
        b.step(st.show("main", eq(r"c = (1-s)f(k): \quad \text{falls DISCRETELY by }"
                                  r"(s_1-s_0)f(k_T)", size=38, colour=BROKEN)),
               t=1.3, hold=5)
        b.step(st.show("note", note("the price of the transition, paid on day one")),
               t=0.8, hold=4)
        b.step(st.show("title", title("During the transition")), t=0.8, hold=1)
        b.step(st.show("main", eq(r"\frac{\dot y}{y} = \alpha\left[\frac{s_1 f(k)}{k} "
                                  r"- (\delta+n)\right] \;\propto\; e^{-\lambda(t-T)}",
                                  size=40)), t=1.4, hold=5)
        b.step(st.show("note", note("growth SPIKES, then decays -- at 4% a year, with a "
                                    "17-year half-life")), t=0.8, hold=4)
        b.step(st.show("title", title("And the identity that makes it precise")),
               t=0.8, hold=2)
        b.step(st.show("main", eq(r"\int_T^{\infty}\frac{\dot y_t}{y_t}\,dt "
                                  r"= \ln y_{ss}(s_1) - \ln y_{ss}(s_0) "
                                  r"= \frac{\alpha}{1-\alpha}\ln\frac{s_1}{s_0}", size=38,
                                  colour=KEEP)), t=1.5, hold=6)
        b.step(st.show("note", note("the area under the growth spike IS the level gain")),
               t=0.8, hold=4)
        b.step(st.show("note", note("a rate effect would make that integral diverge. "
                                    "One converges, the other does not")), t=0.8, hold=4)
        b.run()


class BeatNumbers(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatNumbers")
        head = ["a permanent rise in s, 0.20 to 0.25", ""]
        w = [7.0, 3.4]
        e = ("", "")
        r1 = ("level gain in output per worker", "+11.5%, forever")
        r2 = ("half-life of the transition", "17 years")
        r3 = ("peak growth rate, on day one", "~0.5% a year")
        r4 = ("consumption, on day one", "falls at once")
        b.step(st.show("note", note("'a level effect' sounds small until you price it")),
               t=0.7, hold=2)
        b.step(st.show("title", title("Price it: alpha = 1/3, delta = 0.05, n = 0.01")),
               t=0.8, hold=2)
        b.step(st.show("main", eq(r"\tfrac{1}{2}\ln 1.25 = 0.112", size=52, colour=FOCUS)),
               t=1.1, hold=4)
        b.step(st.show("main", table(head, [r1, e, e, e], col_widths=w,
                                     cell_colours={(0, 1): KEEP})), t=1.1, hold=4)
        b.step(st.show("main", table(head, [r1, r2, e, e], col_widths=w)), t=1.0, hold=3)
        b.step(st.show("note", note("about 35 years to get three quarters of the way")),
               t=0.8, hold=3)
        b.step(st.show("main", table(head, [r1, r2, r3, e], col_widths=w,
                                     cell_colours={(2, 1): FOCUS})), t=1.0, hold=4)
        b.step(st.show("main", table(head, [r1, r2, r3, r4], col_widths=w,
                                     cell_colours={(3, 1): BROKEN})), t=1.0, hold=4)
        b.step(st.show("title", title("Should a country save more?")), t=0.8, hold=2)
        b.step(st.show("main", note("Yes. It ends up permanently richer, by about a tenth.\n\n"
                                    "It pays with an immediate fall in consumption.\n\n"
                                    "It waits a generation to collect.\n\n"
                                    "And its growth rate never rises by a full point.")),
               t=1.3, hold=6)
        b.step(st.show("note", note("11 per cent is what accumulation buys. "
                                    "Korea went up by a factor of ten")), t=0.8, hold=5)
        b.step(st.show("note", note("and whether the trade is worth making, the model has "
                                    "not yet said")), t=0.8, hold=3)
        b.run()


class BeatConsumption(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatConsumption")
        s = Stack(st, size=32, rows=3)
        b.step(st.show("title", title("The one entry I left unsigned")), t=0.8, hold=2)
        b.step(s.add(r"c_{ss}(s) = (1-s)\,f\!\left(k_{ss}(s)\right)", colour=OBJ),
               t=1.2, hold=4)
        b.step(st.show("note", note("s appears twice, pulling in opposite directions")),
               t=0.8, hold=3)
        b.step(st.show("note", note("higher s raises capital, so raises output -- but takes "
                                    "a bigger slice of it")), t=0.8, hold=4)
        b.step(s.add(r"\frac{dc_{ss}}{ds} = -f(k_{ss}) + (1-s)f'(k_{ss})"
                     r"\frac{dk_{ss}}{ds}", size=30), t=1.5, hold=5)
        b.step(st.show("note", note("substitute, use the steady-state condition to "
                                    "eliminate s, and simplify")), t=0.8, hold=3)
        b.step(s.collapse(r"\frac{dc_{ss}}{ds} > 0 \iff f'(k_{ss}) > \delta+n", size=50),
               t=1.4, hold=6)
        b.step(st.show("note", note("invest more only while the extra machine produces more "
                                    "than it costs to keep the stock intact")),
               t=0.8, hold=5)
        b.step(st.show("title", title("And notice where that came from")), t=0.8, hold=2)
        b.step(st.show("main", note("This model contains NO optimising agent.\n\n"
                                    "Nobody in it maximises anything. The saving rate is a\n"
                                    "parameter handed down from outside.\n\n"
                                    "And we have just derived a welfare criterion -- because\n"
                                    "steady-state consumption is a well-defined function of\n"
                                    "that parameter, and we can ask where it peaks.")),
               t=1.3, hold=6)
        b.step(st.show("title", title("That inequality is the GOLDEN RULE")), t=0.8, hold=3)
        b.step(st.show("note", note("and chasing it down is where session 3 begins")),
               t=0.8, hold=3)
        b.run()


class BeatBrazil(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatBrazil")
        s = Stack(st, size=32, rows=4)
        head = ["", "Brazil", "United States"]
        w = [4.6, 3.2, 3.2]
        b.step(st.show("title", title("Point it at the question it was built for")),
               t=0.8, hold=2)
        b.step(st.show("note", note("why is Brazil poorer than the United States?")),
               t=0.8, hold=3)
        b.step(st.show("main", table(head, [("gross capital formation", "18.3%", "21.3%"),
                                            ("population growth", "0.86%", "0.78%")],
                                     col_widths=w)), t=1.2, hold=5)
        b.step(s.add(r"\frac{y_{ss}^{BR}}{y_{ss}^{US}} = "
                     r"\left(\frac{s_{BR}}{s_{US}}\right)^{\frac{\alpha}{1-\alpha}}"),
               t=1.4, hold=4)
        b.step(st.show("note", note("everything else cancels")), t=0.6, hold=2)
        b.step(s.add(r"= \left(0.86\right)^{1/2} = 0.93", colour=FOCUS), t=1.2, hold=4)
        b.step(st.show("note", note("the square root -- that is what an elasticity of a "
                                    "half means")), t=0.8, hold=4)
        b.step(s.add(r"\text{with } (n+\delta) \text{ too}: \quad 0.92", size=30,
                     colour=FOCUS), t=1.2, hold=4)
        b.step(st.show("main", table(["", "predicted", "measured"],
                                     [("Brazilian income, vs US", "92%", "25.7%")],
                                     col_widths=[4.6, 3.2, 3.2],
                                     cell_colours={(0, 1): BROKEN, (0, 2): FOCUS})),
               t=1.3, hold=6)
        b.step(st.show("note", note("out by a factor of three and a half. Not fifteen "
                                    "per cent. Three and a half TIMES")), t=0.8, hold=5)
        b.step(st.show("title", title("Run it backwards")), t=0.8, hold=2)
        b.step(st.show("main", eq(r"s_{BR}\ \text{would have to be}\ 1.4\%\ \text{of GDP}",
                                  size=44, colour=BROKEN)), t=1.3, hold=5)
        b.step(st.show("note", note("Brazil would have to invest essentially nothing, for "
                                    "decades, to be as poor as Brazil actually is")),
               t=0.8, hold=5)
        b.step(st.show("title", title("And this is not a failure of data or calibration")),
               t=0.8, hold=3)
        b.step(st.show("note", note("it is the elasticity. One half is small BECAUSE of "
                                    "diminishing returns")), t=0.8, hold=4)
        b.step(st.show("note", note("the assumption that makes the model work is the "
                                    "assumption that makes it fail")), t=0.8, hold=5)
        b.run()


class BeatClose(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatClose")
        ax, panel = axes_panel([0, 6, 1], [0, 3, 1], x_label="capital per worker, k")
        inv = ax.plot(lambda x: 0.55 * 1.65 * x ** (1 / 3), x_range=[0, 5.8], color=FOCUS)
        brk = ax.plot(lambda x: 0.36 * x, x_range=[0, 5.8], color=KEEP)
        kss = (0.55 * 1.65 / 0.36) ** 1.5
        cross = Dot(ax.c2p(kss, 0.36 * kss), color=KEEP, radius=0.09)
        model = VGroup(Dot(ORIGIN, color=BROKEN, radius=0.10),
                       Text("model: 92%", font_size=20, color=BROKEN)
                       ).arrange(RIGHT, buff=0.25)
        real = VGroup(Dot(ORIGIN, color=OBJ, radius=0.10),
                      Text("Brazil: 26%", font_size=20, color=OBJ)
                      ).arrange(RIGHT, buff=0.25)
        dots = VGroup(model, real).arrange(DOWN, buff=1.2, aligned_edge=LEFT)
        b.step(st.show("title", title("Where we stand")), t=0.8, hold=1)
        b.step(st.show("main", note("Eight assumptions.\n"
                                    "A law of motion, derived line by line.\n"
                                    "Existence -- that was Inada.\n"
                                    "Uniqueness -- that was diminishing returns.\n"
                                    "Convergence, monotone, at 4% a year.")), t=1.3, hold=6)
        b.step(st.show("note", note("and saving more is a level effect, never a rate "
                                    "effect")), t=0.8, hold=4)
        b.step(st.show("note", note("then we pointed it at two countries and it missed by "
                                    "three and a half times")), t=0.8, hold=4)
        b.step(st.show("title", title("Hold this frame")), t=0.8, hold=2)
        b.step(st.show("main", side_by_side(panel, dots)), t=1.3, hold=4)
        b.step([Create(inv)], t=1.1, hold=3)
        b.step([Create(brk)], t=1.1, hold=3)
        b.step([Create(cross)], t=0.9, hold=4)
        b.step(st.show("note", note("the diagram you can already draw -- and beside it, "
                                    "the distance session 3 has to explain")), t=0.8, hold=5)
        b.step(st.show("title", title("There are only two ways out")), t=0.8, hold=2)
        b.step(st.show("main", note("Either the saving differences are far larger than they\n"
                                    "look -- and we have just checked that they are not.\n\n"
                                    "Or something ELSE differs across countries, something\n"
                                    "that is not capital at all, and does most of the\n"
                                    "explaining.")), t=1.3, hold=6)
        b.step(st.show("note", note("and a second failure: Kaldor's fact 1 says growth is "
                                    "constant and positive. This model says zero")),
               t=0.8, hold=5)
        b.step(st.show("title", title("Both problems have the same answer: technology")),
               t=0.8, hold=4)
        b.run()
