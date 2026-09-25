"""Scenes for aula-03-technology-and-tfp. One Scene per beat.

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
        w, e = [6.4, 4.0], ("", "")
        r1 = ("Brazilian income per head, vs US", "25.7%")
        r2 = ("implied rental rate, Brazil vs US", "12.5x")
        r3 = ("implied Brazilian interest rate", "138% a year")
        b.step(st.show("title", title("Last session ended with a failure")), t=0.8, hold=2)
        b.step(st.show("note", note("the model predicted 92%. Brazil is at 26%")),
               t=0.7, hold=3)
        b.step(st.show("title", title("So take the model's side. What would have to be true?")),
               t=0.8, hold=3)
        b.step(st.show("main", table(["", ""], [r1, e, e], col_widths=w)), t=1.0, hold=3)
        b.step(st.show("note", note("if the only difference is capital, capital must be "
                                    "SCARCE in Brazil -- and scarce things earn more")),
               t=0.8, hold=4)
        b.step(st.show("main", table(["", ""], [r1, r2, e], col_widths=w,
                                     cell_colours={(1, 1): FOCUS})), t=1.0, hold=4)
        b.step(st.show("main", table(["", ""], [r1, r2, r3], col_widths=w,
                                     cell_colours={(1, 1): FOCUS, (2, 1): BROKEN})),
               t=1.0, hold=5)
        b.step(st.show("note", note("not thirteen point eight. A hundred and thirty-eight")),
               t=0.8, hold=4)
        b.step(st.show("note", note("if that were true, every dollar of capital on earth "
                                    "would already be in Brazil")), t=0.8, hold=4)
        b.step(st.show("title", title("This session: repair the model, then convict it")),
               t=0.8, hold=3)
        b.step(st.show("note", note("the second failure has no fix inside the model at all")),
               t=0.8, hold=3)
        b.step(st.show("note", note("and that conviction is the most useful result in "
                                    "growth theory")), t=0.8, hold=3)
        b.run()


# ------------------------------------------------------------------ Act I

class BeatGoldenSetup(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatGoldenSetup")
        s = Stack(st, size=36, rows=3)
        b.step(st.show("title", title("Unfinished business from last session")), t=0.8, hold=2)
        b.step(st.show("note", note("consumption rises with saving iff f'(k) > delta + n -- "
                                    "and then we stopped")), t=0.8, hold=4)
        b.step(st.show("note", note("a model with no optimising agent produced something "
                                    "that looked like a welfare criterion")), t=0.8, hold=4)
        b.step(st.show("title", title("Let us finish it")), t=0.8, hold=2)
        b.step(s.add(r"c_{ss} = f(k) - (\delta+n)k", colour=OBJ), t=1.1, hold=4)
        b.step(st.show("note", note("no s in it at all -- the steady-state condition was "
                                    "used to substitute s away")), t=0.8, hold=4)
        b.step(s.add(r"k_{ss}(s) \ \text{is strictly increasing}", size=30), t=1.1, hold=3)
        b.step(st.show("note", note("so choose k directly: every k is exactly one s, and "
                                    "the other way round")), t=0.8, hold=4)
        b.step(s.collapse(r"\max_{k}\;\; f(k) - (\delta+n)k", size=52), t=1.2, hold=5)
        b.step(st.show("note", note("over all possible steady states, which gives the most "
                                    "consumption per worker?")), t=0.8, hold=4)
        b.step(st.show("note", note("and the answer will turn out to be a statement about the production function alone")), t=0.7, hold=3)
        b.step(st.show("note", note("which is why it is quotable")), t=0.7, hold=3)
        b.run()


class BeatGoldenFOC(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatGoldenFOC")
        s = Stack(st, size=34, rows=3)
        b.step(st.show("title", title("Differentiate, and set to zero")), t=0.8, hold=1)
        b.step(s.add(r"c'(k) = f'(k) - (\delta+n) = 0"), t=1.2, hold=4)
        b.step(s.collapse(r"f'(k_{gold}) = \delta + n", size=58), t=1.3, hold=5)
        b.step(st.show("title", title("Check it is a maximum")), t=0.8, hold=1)
        b.step(st.show("main", eq(r"c''(k) = f''(k) < 0", size=50, colour=KEEP)),
               t=1.1, hold=4)
        b.step(st.show("note", note("diminishing returns again -- a peak, not a trough, "
                                    "and the only one")), t=0.8, hold=4)
        b.step(st.show("note", note("and Inada makes it interior: slope infinite at zero, "
                                    "negative far out")), t=0.8, hold=4)
        b.step(st.show("title", title("Now read the condition")), t=0.8, hold=2)
        b.step(st.show("main", note("One more machine PRODUCES f'(k), forever.\n\n"
                                    "It COSTS (delta + n) every period to keep:\n"
                                    "   delta  to replace what wore out\n"
                                    "   n      to equip the workers who arrived\n\n"
                                    "At the optimum, the last machine exactly earns\n"
                                    "its own upkeep.")), t=1.3, hold=6)
        b.step(st.show("note", note("push past it and each machine costs more to maintain "
                                    "than it produces")), t=0.8, hold=4)
        b.step(st.show("note", note("that is not a matter of taste. That is waste")),
               t=0.8, hold=4)
        b.step(st.show("note", note("f'(k) is what the machine yields; delta + n is what it costs to keep")), t=0.7, hold=3)
        b.run()


class BeatSGold(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatSGold")
        s = Stack(st, size=32, rows=4)
        s2 = Stack(st, size=34, rows=3)
        b.step(st.show("title", title("Which saving rate gets us there?")), t=0.8, hold=1)
        b.step(s.add(r"\alpha k_{gold}^{\alpha-1} = \delta+n \;\Rightarrow\; "
                     r"k_{gold} = \left(\frac{\alpha}{\delta+n}\right)^{\frac{1}{1-\alpha}}"),
               t=1.5, hold=4)
        b.step(s.add(r"k_{ss}(s) = \left(\frac{s}{\delta+n}\right)^{\frac{1}{1-\alpha}}"),
               t=1.3, hold=4)
        b.step(st.show("note", note("set them equal: exponents match, denominators match")),
               t=0.8, hold=3)
        b.step(s.collapse(r"s_{gold} = \alpha", size=64), t=1.3, hold=5)
        b.step(st.show("note", note("a strange result -- alpha is a property of the "
                                    "production function. Where did delta and n go?")),
               t=0.8, hold=4)
        b.step(st.show("title", title("A second derivation, which explains it")), t=0.8, hold=2)
        b.step(s2.add(r"\frac{(\delta+n)k_{ss}}{f(k_{ss})} = s"), t=1.2, hold=4)
        b.step(st.show("note", note("in any steady state, the investment share of output "
                                    "IS s")), t=0.8, hold=3)
        b.step(s2.add(r"\delta+n = f'(k_{gold}) \;\Rightarrow\; "
                      r"s_{gold} = \frac{f'(k_{gold})k_{gold}}{f(k_{gold})} = \alpha",
                      colour=KEEP), t=1.5, hold=5)
        b.step(st.show("title", title("Save exactly capital's share of income")), t=0.8, hold=4)
        b.step(st.show("note", note("delta and n set how much capital that buys -- "
                                    "not the rate itself")), t=0.8, hold=4)
        b.step(st.show("main", eq(r"\alpha = 0.35 \quad\text{vs}\quad s_{US} \simeq 0.20",
                                  size=50, colour=FOCUS)), t=1.2, hold=4)
        b.step(st.show("note", note("so the US is BELOW the Golden Rule -- which sounds "
                                    "like a criticism, and is not")), t=0.8, hold=4)
        b.run()


class BeatAsymmetry(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatAsymmetry")
        ax, panel = axes_panel([0, 6, 1], [0, 3, 1], x_label="capital per worker, k")
        hump = ax.plot(lambda x: 2.6 * x ** (1 / 3) - 0.72 * x, x_range=[0.05, 5.8],
                       color=OBJ)
        peak = Dot(ax.c2p(2.62, 2.6 * 2.62 ** (1 / 3) - 0.72 * 2.62), color=KEEP, radius=0.09)
        b.step(st.show("title", title("The two sides of the peak are not symmetric")),
               t=0.8, hold=2)
        b.step(st.show("main", panel), t=0.9, hold=2)
        b.step([Create(hump)], t=1.3, hold=3)
        b.step([Create(peak)], t=0.9, hold=3)
        b.step(st.show("note", note("steady-state consumption, against k")), t=0.7, hold=2)
        b.step(st.show("title", title("ABOVE the peak: f'(k) < delta + n")), t=0.8, hold=2)
        b.step(st.show("main", note("Cut s.\n\n"
                                    "On impact:      consumption jumps UP\n"
                                    "In transition:  required investment falls FASTER\n"
                                    "                than output does\n"
                                    "New steady state: consumption HIGHER")),
               t=1.3, hold=6)
        b.step(st.show("note", note("higher immediately, and at every date after. "
                                    "Nobody waits. No generation pays")), t=0.8, hold=5)
        b.step(st.show("note", note("a Pareto improvement -- with no utility function, no "
                                    "discount rate, no comparison between generations")),
               t=0.8, hold=5)
        b.step(st.show("main", eq(r"\text{DYNAMICALLY INEFFICIENT}", size=48, colour=BROKEN)),
               t=1.1, hold=4)
        b.step(st.show("title", title("BELOW the peak: f'(k) > delta + n")), t=0.8, hold=2)
        b.step(st.show("main", note("Raise s.\n\n"
                                    "On impact:      consumption FALLS, discretely\n"
                                    "In transition:  it recovers, then overtakes\n"
                                    "New steady state: consumption higher\n\n"
                                    "Some generations lose. Later ones gain.")),
               t=1.3, hold=6)
        b.step(st.show("note", note("that is a TRADE-OFF, not an inefficiency")),
               t=0.8, hold=4)
        b.step(st.show("note", note("and this model has no utility function, no discount "
                                    "factor, nobody choosing -- so it cannot rank it")),
               t=0.8, hold=5)
        b.step(st.show("title", title("Over-accumulation is a mistake. "
                                      "Under-accumulation is a preference")), t=0.8, hold=5)
        b.step(st.show("note", note("which is exactly why session 4 exists")), t=0.8, hold=3)
        b.run()


class BeatDynamicTest(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatDynamicTest")
        s = Stack(st, size=34, rows=3)
        b.step(st.show("title", title("Is any real economy above the Golden Rule?")),
               t=0.8, hold=2)
        b.step(st.show("note", note("sounds like it needs a capital stock estimate. "
                                    "It does not")), t=0.8, hold=3)
        b.step(s.add(r"f'(k) < \delta+n"), t=1.0, hold=3)
        b.step(st.show("note", note("multiply both sides by k -- free, since k is positive")),
               t=0.8, hold=3)
        b.step(s.add(r"\underbrace{f'(k)k}_{\text{capital income}} < "
                     r"\underbrace{(\delta+n)k}_{\text{investment}}", colour=KEEP),
               t=1.4, hold=5)
        b.step(st.show("note", note("both are line items in the national accounts. "
                                    "No production function, nothing to argue about")),
               t=0.8, hold=5)
        b.step(st.show("main", table(["United States", "% of GDP"],
                                     [("capital income", "~35"), ("investment", "~20")],
                                     col_widths=[4.6, 3.4],
                                     cell_colours={(0, 1): KEEP})), t=1.2, hold=5)
        b.step(st.show("note", note("capital income comfortably exceeds investment")),
               t=0.8, hold=4)
        b.step(st.show("title", title("Below the Golden Rule -- and so is every developed "
                                      "economy checked")), t=0.8, hold=4)
        b.step(st.show("note", note("reassuring, and slightly deflating: the one welfare "
                                    "verdict this model can deliver never binds")),
               t=0.8, hold=4)
        b.step(st.show("note", note("dynamic inefficiency is a theoretical possibility the data decline to produce")), t=0.7, hold=3)
        b.step(st.show("note", note("so the rest of this course is about economies below the peak")), t=0.7, hold=3)
        b.run()


# ------------------------------------------------------------------ Act II

class BeatFirmProblem(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatFirmProblem")
        s = Stack(st, size=32, rows=5)
        b.step(st.show("title", title("Decentralise: put in a competitive firm")),
               t=0.8, hold=2)
        b.step(st.show("note", note("so far: an aggregate constraint with a mechanical "
                                    "saving rule. No firms, no prices, nobody deciding")),
               t=0.8, hold=4)
        b.step(s.add(r"\max_{K,L}\;\; \Pi = F(K,L) - r^K K - wL", colour=OBJ), t=1.3, hold=4)
        b.step(s.add(r"r^K = F_K, \qquad w = F_L", colour=KEEP), t=1.2, hold=4)
        b.step(st.show("note", note("each factor paid its marginal product -- the entire "
                                    "content of competitive factor markets")), t=0.8, hold=4)
        b.step(st.show("note", note("and under CRS the firm's SCALE is undetermined; only "
                                    "K/L is pinned down")), t=0.8, hold=4)
        b.step(st.show("note", note("which is why a representative firm is legitimate here "
                                    "-- and would not be under increasing returns")),
               t=0.8, hold=4)
        b.step(st.show("title", title("In per-worker terms")), t=0.8, hold=1)
        b.step(s.add(r"F_K = \frac{\partial}{\partial K}\left[L f(K/L)\right] "
                     r"= L f'(k)\cdot\frac{1}{L} = f'(k)", size=30), t=1.5, hold=4)
        b.step(s.add(r"F_L = f(k) + L f'(k)\left(-\frac{K}{L^2}\right) = f(k) - k f'(k)",
                     size=30), t=1.5, hold=4)
        b.step(st.show("note", note("the product rule, then tidy up")), t=0.7, hold=3)
        b.step(s.collapse(r"r^K = f'(k), \qquad w = f(k) - k f'(k)", size=48), t=1.3, hold=5)
        b.step(st.show("note", note("both depend on k ALONE -- constant returns again")),
               t=0.8, hold=4)
        b.step(st.show("note", note("so a country's wage is a statement about its capital "
                                    "per worker and nothing else")), t=0.8, hold=4)
        b.run()


class BeatZeroProfit(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatZeroProfit")
        s = Stack(st, size=34, rows=3)
        b.step(st.show("title", title("Substitute the factor prices back in")), t=0.8, hold=1)
        b.step(s.add(r"\Pi = F(K,L) - F_K K - F_L L = 0", colour=KEEP), t=1.3, hold=5)
        b.step(st.show("note", note("by Euler's theorem, which we proved last session")),
               t=0.8, hold=3)
        b.step(st.show("note", note("not approximately. Not in the long run after entry. "
                                    "IDENTICALLY, at every k")), t=0.8, hold=5)
        b.step(st.show("title", title("CRS + competitive pricing FORCES zero profit")),
               t=0.8, hold=3)
        b.step(st.show("note", note("not an assumption we added -- a consequence of two "
                                    "we already had")), t=0.8, hold=4)
        b.step(s.add(r"r^K k + w = f'(k)k + f(k) - kf'(k)", size=32), t=1.4, hold=4)
        b.step(st.show("note", note("the k f'(k) terms cancel")), t=0.7, hold=3)
        b.step(s.collapse(r"r^K k + w = f(k) = y", size=54), t=1.3, hold=5)
        b.step(st.show("note", note("capital income plus labour income exhausts output "
                                    "per worker, exactly")), t=0.8, hold=4)
        b.step(st.show("note", note("that identity is the backbone of session 6")),
               t=0.8, hold=3)
        b.step(st.show("note", note("no profit means nothing is left over for the owner as OWNER")), t=0.7, hold=3)
        b.run()


class BeatAlphaEquilibrium(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatAlphaEquilibrium")
        s = Stack(st, size=32, rows=3)
        b.step(st.show("title", title("Now we can say what alpha IS")), t=0.8, hold=1)
        b.step(s.add(r"\text{capital share} = \frac{r^K k}{y} = \frac{f'(k)k}{f(k)}"),
               t=1.3, hold=4)
        b.step(st.show("note", note("for a general f, that MOVES as k moves -- a country "
                                    "in transition would see its shares drift")),
               t=0.8, hold=4)
        b.step(s.add(r"\frac{\alpha k^{\alpha-1}\cdot k}{k^{\alpha}} = \alpha", colour=KEEP),
               t=1.3, hold=5)
        b.step(st.show("note", note("for Cobb-Douglas: alpha, at EVERY k, in and out of "
                                    "steady state")), t=0.8, hold=4)
        b.step(st.show("title", title("Which is the real argument for the functional form")),
               t=0.8, hold=2)
        b.step(st.show("main", note("Kaldor fact 3: shares are constant in the data.\n"
                                    "Economies are not always in steady state.\n\n"
                                    "So we need a form that delivers constant shares\n"
                                    "WITHOUT requiring the economy to be at rest.\n\n"
                                    "Observe 65% labour share -> adopt Cobb-Douglas\n"
                                    "-> set alpha = 0.35.")), t=1.3, hold=6)
        b.step(st.show("note", note("read off a national accounts identity -- NOT estimated "
                                    "from a regression")), t=0.8, hold=4)
        b.step(st.show("note", note("and that matters: we use this same alpha to TEST the "
                                    "model. Estimating it from the same data would be "
                                    "circular")), t=0.8, hold=5)
        b.step(st.show("title", title("One honest caveat: CES")), t=0.8, hold=2)
        b.step(st.show("main", note("With a general CES function the capital share is\n"
                                    "constant only in the Cobb-Douglas case.\n\n"
                                    "If capital and labour substitute more easily, the\n"
                                    "capital share RISES with K/Y -- a leading explanation\n"
                                    "for the falling labour share after 2000.\n\n"
                                    "So the breakdown of Kaldor fact 3 is evidence against\n"
                                    "the form we just adopted.")), t=1.3, hold=6)
        b.step(st.show("note", note("the model's convenience is bought at a price, and the "
                                    "data is starting to charge it")), t=0.8, hold=4)
        b.step(st.show("note", note("alpha is calibrated, never estimated -- that is what keeps the coming test honest")), t=0.7, hold=3)
        b.run()


class BeatInterestRate(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatInterestRate")
        s = Stack(st, size=34, rows=3)
        b.step(st.show("title", title("One more price -- the one the course runs on")),
               t=0.8, hold=1)
        b.step(st.show("main", note("A unit of output, two ways to carry it forward:\n\n"
                                    "  lend it        -> get back 1 + r\n\n"
                                    "  buy capital    -> rent it out for r^K, then sell\n"
                                    "                    what is left: r^K + (1 - delta)")),
               t=1.3, hold=6)
        b.step(st.show("note", note("if both are used, they must pay the same")),
               t=0.8, hold=3)
        b.step(s.add(r"1 + r = r^K + (1-\delta)"), t=1.2, hold=4)
        b.step(s.collapse(r"r = r^K - \delta = f'(k) - \delta", size=54), t=1.3, hold=5)
        b.step(st.show("title", title("Three consequences")), t=0.8, hold=1)
        b.step(st.show("main", eq(r"f'(k_{gold}) = \delta+n \;\Longleftrightarrow\; r = n",
                                  size=48, colour=KEEP)), t=1.3, hold=5)
        b.step(st.show("note", note("dynamic inefficiency is r < n: an economy whose "
                                    "interest rate is below its growth rate")), t=0.8, hold=5)
        b.step(st.show("note", note("2. poor countries should have HIGH interest rates -- "
                                    "low k, high f'(k)")), t=0.8, hold=4)
        b.step(st.show("note", note("hold on to that one. In twenty minutes it is the "
                                    "hypothesis we kill")), t=0.8, hold=4)
        b.step(st.show("note", note("3. r falls monotonically as an economy develops, "
                                    "because f is concave")), t=0.8, hold=4)
        b.step(st.show("note", note("one price, three results we will use for the rest of the course")), t=0.7, hold=3)
        b.run()

# ------------------------------------------------------------------ Act III

class BeatEfficiencyUnits(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatEfficiencyUnits")
        s = Stack(st, size=34, rows=4)
        b.step(st.show("title", title("Now the repair")), t=0.8, hold=1)
        b.step(st.show("main", note("\"If we want to understand the growth of GDP per\n"
                                    "capita in the US over the last 250 years, the model\n"
                                    "we have studied so far doesn't have a lot of promise:\n"
                                    "it predicts that in the long run there will be no\n"
                                    "growth.\"\n\n                            - Kurlat, p. 69")),
               t=1.3, hold=6)
        b.step(s.add(r"Y = F(K, AL)", colour=OBJ), t=1.1, hold=4)
        b.step(st.show("note", note("A multiplies LABOUR. Better technology is equivalent "
                                    "to having more workers")), t=0.8, hold=4)
        b.step(st.show("note", note("and that placement is forced, not chosen -- we prove "
                                    "it in two beats")), t=0.8, hold=3)
        b.step(s.add(r"A_{t+1} = (1+g)A_t \qquad \text{(Assumption 4.9)}", size=30),
               t=1.2, hold=4)
        b.step(s.add(r"\tilde L \equiv AL, \qquad \tilde y \equiv \frac{Y}{AL}, "
                     r"\qquad \tilde k \equiv \frac{K}{AL}", colour=FOCUS), t=1.4, hold=5)
        b.step(st.show("note", note("\"These are not variables we are actually interested "
                                    "in, but it's a convenient way to rescale the model\"")),
               t=0.8, hold=5)
        b.step(st.show("note", note("nobody cares about output per efficiency unit. "
                                    "It is scaffolding -- we translate back at the end")),
               t=0.8, hold=4)
        b.step(s.collapse(r"\tilde y = F\!\left(\frac{K}{AL},1\right) = f(\tilde k)", size=48),
               t=1.3, hold=5)
        b.step(st.show("note", note("the same three steps as before, with AL in place of L")),
               t=0.8, hold=3)
        b.step(st.show("note", note("do all the algebra in tildes, then translate once at the end")), t=0.7, hold=3)
        b.run()


class BeatTildeLaw(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatTildeLaw")
        s = Stack(st, size=30, rows=5)
        b.step(st.show("title", title("The law of motion, in the new units")), t=0.8, hold=1)
        b.step(s.add(r"\Delta\tilde k_{t+1} = \frac{K_{t+1}}{A_{t+1}L_{t+1}} - \tilde k_t"),
               t=1.3, hold=4)
        b.step(s.add(r"= \frac{(1-\delta)K_t + sY_t}{(1+g)(1+n)A_tL_t} - \tilde k_t"),
               t=1.4, hold=4)
        b.step(st.show("note", note("A grows at g and L grows at n, so efficiency units "
                                    "grow at (1+g)(1+n)")), t=0.8, hold=4)
        b.step(s.add(r"= \frac{(1-\delta)\tilde k_t + s f(\tilde k_t)}{(1+g)(1+n)} "
                     r"- \tilde k_t"), t=1.4, hold=4)
        b.step(st.show("note", note("now over the common denominator, and collect")),
               t=0.7, hold=3)
        b.step(s.add(r"(1+g)(1+n) - (1-\delta) = \delta + n + g + ng", colour=FOCUS),
               t=1.4, hold=4)
        b.step(st.show("main", table(["the cross term ng", "value"],
                                     [("n x g at n=0.01, g=0.015", "0.00015"),
                                      ("break-even rate", "0.065"),
                                      ("ng as a share of it", "0.2%")],
                                     col_widths=[5.2, 3.4],
                                     cell_colours={(2, 1): FOCUS})), t=1.3, hold=5)
        b.step(st.show("note", note("second order. Drop it")), t=0.7, hold=3)
        b.step(st.show("main", eq(r"\dot{\tilde k} = s f(\tilde k) - "
                                  r"(\delta + n + g)\,\tilde k", size=54, colour=KEEP)),
               t=1.4, hold=6)
        b.step(st.show("note", note("the same equation as before, with g added to the "
                                    "break-even rate")), t=0.8, hold=4)
        b.step(st.show("note", note("capital must keep up with the EFFECTIVE labour force, "
                                    "which grows at n + g -- machines for the new workers")),
               t=0.8, hold=5)
        b.step(st.show("note", note("and every proof from last session goes through "
                                    "verbatim: they only used that the constant is positive")),
               t=0.8, hold=4)
        b.step(st.show("note", note("the destination changed; the machinery did not")), t=0.7, hold=3)
        b.run()


class BeatBGP(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatBGP")
        head = ["variable", "grows at"]
        w = [6.4, 4.0]
        rows = [("k~, y~, c~  (per efficiency unit)", "0"),
                ("k, y, c  (per worker)", "g"),
                ("K, Y, C  (aggregates)", "n + g"),
                ("K/Y, factor shares, r", "0"),
                ("the wage w", "g")]
        e = ("", "")
        b.step(st.show("title", title("Translate back -- nobody cares about tildes")),
               t=0.8, hold=2)
        b.step(st.show("main", eq(r"y = A\tilde y_{ss} \;\Longrightarrow\; "
                                  r"\frac{\dot y}{y} = \frac{\dot A}{A} = g", size=48,
                                  colour=KEEP)), t=1.3, hold=5)
        b.step(st.show("main", table(head, [rows[0], e, e, e, e], col_widths=w)),
               t=1.1, hold=3)
        b.step(st.show("main", table(head, [rows[0], rows[1], e, e, e], col_widths=w,
                                     cell_colours={(1, 1): FOCUS})), t=1.0, hold=4)
        b.step(st.show("main", table(head, [rows[0], rows[1], rows[2], e, e], col_widths=w)),
               t=1.0, hold=3)
        b.step(st.show("main", table(head, rows[:4] + [e], col_widths=w)), t=1.0, hold=3)
        b.step(st.show("main", table(head, rows, col_widths=w)), t=1.0, hold=4)
        b.step(st.show("title", title("Proposition 4.3, and the headline of the session")),
               t=0.8, hold=2)
        b.step(st.show("main", note("Output per capita grows at the rate of technological\n"
                                    "progress, g -- and at nothing else.\n\n"
                                    "Not the saving rate. Not population growth. Not\n"
                                    "depreciation.\n\n"
                                    "Those still set the LEVEL of the path. The slope is\n"
                                    "g alone.")), t=1.3, hold=6)
        b.step(st.show("note", note("check the wage row: w is A times a constant, so real "
                                    "wages grow at g and the labour share is flat")),
               t=0.8, hold=5)
        b.step(st.show("note", note("both are Kaldor facts -- the model now delivers them")),
               t=0.8, hold=4)
        b.step(st.show("title", title("And the statement that catches everybody")),
               t=0.8, hold=2)
        b.step(st.show("note", note("there is NO steady state in per-worker terms once "
                                    "g > 0. What converges is k-tilde")), t=0.8, hold=5)
        b.run()


class BeatUzawa(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatUzawa")
        s = Stack(st, size=30, rows=4)
        b.step(st.show("title", title("Why does A multiply labour?")), t=0.8, hold=2)
        b.step(st.show("main", note("Three conceivable places:\n\n"
                                    "  Y = F(K, AL)     labour-augmenting (Harrod)\n"
                                    "  Y = F(AK, L)     capital-augmenting (Solow)\n"
                                    "  Y = A F(K, L)    Hicks-neutral")), t=1.3, hold=6)
        b.step(st.show("note", note("Uzawa, 1961: only the first admits a balanced "
                                    "growth path")), t=0.8, hold=4)
        b.step(s.add(r"Y_0e^{\gamma t} = F\!\left(K_0e^{\gamma t},\, L_0e^{nt},\, t\right)",
                     size=32), t=1.4, hold=4)
        b.step(st.show("note", note("on a balanced path K and Y grow at the same rate "
                                    "gamma, and L at n")), t=0.8, hold=4)
        b.step(st.show("note", note("now use CRS to pull e^(gamma t) out of the first "
                                    "argument, and off the front")), t=0.8, hold=4)
        b.step(s.add(r"Y_0 = F\!\left(K_0,\, L_0e^{(n-\gamma)t},\, t\right)", size=32,
                     colour=FOCUS), t=1.4, hold=5)
        b.step(st.show("note", note("a fixed number on the left, at EVERY date t")),
               t=0.8, hold=4)
        b.step(s.collapse(r"\Rightarrow\; F(K,L,t) = F\!\left(K, A(t)L\right), \quad "
                          r"A \ \text{growing at}\ \gamma - n", size=36), t=1.4, hold=6)
        b.step(st.show("title", title("And the exception everybody meets first")),
               t=0.8, hold=2)
        b.step(st.show("main", eq(r"A K^{\alpha}L^{1-\alpha} = "
                                  r"K^{\alpha}\!\left(A^{\frac{1}{1-\alpha}}L\right)^{1-\alpha}"
                                  r" = \left(A^{\frac{1}{\alpha}}K\right)^{\alpha}L^{1-\alpha}",
                                  size=34)), t=1.5, hold=6)
        b.step(st.show("note", note("under Cobb-Douglas the three forms are the SAME "
                                    "function -- putting A somewhere is a choice of units")),
               t=0.8, hold=5)
        b.step(st.show("note", note("with any other CRS function it is a real restriction, "
                                    "and only labour-augmenting admits a balanced path")),
               t=0.8, hold=5)
        b.step(st.show("note", note("so the general model puts A next to L -- and Cobb-Douglas lets growth accounting ignore the distinction")), t=0.7, hold=3)
        b.run()


class BeatDisappointing(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatDisappointing")
        b.step(st.show("title", title("One moment of honesty before we test it")),
               t=0.8, hold=2)
        b.step(st.show("main", note("Why does output per person grow?\n\n"
                                    "Because A grows.\n\n"
                                    "And why does A grow?\n\n"
                                    "Because we assumed it does.")), t=1.3, hold=6)
        b.step(st.show("main", note("\"it is rather disappointing to have to make this\n"
                                    "assumption. Ideally, one would like to have a deeper\n"
                                    "understanding of why there is technological progress\n"
                                    "and what determines how fast it takes place.\"\n\n"
                                    "                              - Kurlat, p. 70")),
               t=1.3, hold=6)
        b.step(st.show("title", title("The fair summary")), t=0.8, hold=2)
        b.step(st.show("note", note("it explains capital accumulation completely -- "
                                    "transition, steady state, convergence, all proved")),
               t=0.8, hold=5)
        b.step(st.show("note", note("and it explains growth not at all. It assumes the one "
                                    "thing it was built to explain")), t=0.8, hold=5)
        b.step(st.show("note", note("making g an outcome is endogenous growth theory -- "
                                    "later chapters, outside this course")), t=0.8, hold=4)
        b.step(st.show("title", title("And there is a second thing it assumes")),
               t=0.8, hold=3)
        b.step(st.show("note", note("that one turns out to matter even more")), t=0.8, hold=4)
        b.step(st.show("note", note("so: a complete theory of accumulation, and no theory of growth")), t=0.7, hold=3)
        b.step(st.show("note", note("which is the honest thing to say in an exam")), t=0.7, hold=3)
        b.step(st.show("note", note("and the second assumption arrives in five minutes")), t=0.7, hold=3)
        b.run()


# ------------------------------------------------------------------ Act IV

class BeatCalibration(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatCalibration")
        head = ["parameter", "value", "read off"]
        w = [2.6, 2.2, 6.0]
        rows = [("alpha", "0.35", "the 65% labour share"),
                ("g", "0.015", "US growth per capita since 1800"),
                ("n", "0.01", "US population growth since 1950"),
                ("delta", "0.04", "BEA: 0.02 buildings, 0.15 equipment, 0.30 computers"),
                ("s", "0.20", "the recent US investment rate")]
        e = ("", "", "")
        b.step(st.show("title", title("Five parameters, each from one separate fact")),
               t=0.8, hold=1)
        b.step(st.show("main", table(head, [rows[0], e, e, e, e], col_widths=w)),
               t=1.1, hold=3)
        b.step(st.show("main", table(head, rows[:2] + [e, e, e], col_widths=w)), t=1.0, hold=3)
        b.step(st.show("note", note("legitimate to read g straight off growth, because "
                                    "Proposition 4.3 says they are the same thing")),
               t=0.8, hold=4)
        b.step(st.show("main", table(head, rows[:4] + [e], col_widths=w)), t=1.0, hold=3)
        b.step(st.show("main", table(head, rows, col_widths=w)), t=1.0, hold=4)
        b.step(st.show("note", note("and Kurlat is careful: the model assumes S = I, the US "
                                    "is not closed. Match investment and you get 0.20")),
               t=0.8, hold=5)
        b.step(st.show("title", title("Now the moment worth stopping on")), t=0.8, hold=2)
        b.step(st.show("note", note("five numbers from five separate facts. Nothing forces "
                                    "them to agree with a sixth")), t=0.8, hold=4)
        b.step(st.show("main", eq(r"\frac{K}{Y} = \frac{s}{\delta+n+g} "
                                  r"= \frac{0.20}{0.065} = 3.08", size=50, colour=KEEP)),
               t=1.4, hold=6)
        b.step(st.show("main", eq(r"\text{measured } K/Y = 3.2", size=54, colour=FOCUS)),
               t=1.2, hold=5)
        b.step(st.show("title", title("Five calibrated parameters reproduce a sixth fact "
                                      "to within 4%")), t=0.8, hold=4)
        b.step(st.show("note", note("the Solow model's best moment -- said plainly before "
                                    "the rest of this session takes it apart")),
               t=0.8, hold=4)
        b.run()


class BeatConjecture(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatConjecture")
        b.step(st.show("title", title("The hypothesis on trial")), t=0.8, hold=1)
        b.step(st.show("main", note("CONJECTURE 5.1\n\n"
                                    "Technology levels are the same across countries,\n"
                                    "and the differences in GDP per capita are the\n"
                                    "result of differences in capital per worker.")),
               t=1.3, hold=6)
        b.step(st.show("note", note("not a straw man. It is coherent, and consistent with "
                                    "everything we have built")), t=0.8, hold=4)
        b.step(st.show("title", title("And if true, it would be extraordinarily good news")),
               t=0.8, hold=3)
        b.step(st.show("main", note("Capital is a thing you can ACCUMULATE.\n\n"
                                    "A poor country would not be missing knowledge, or\n"
                                    "institutions, or anything hard to transfer.\n\n"
                                    "It would simply be short of machines.\n\n"
                                    "Poverty becomes an engineering problem.")),
               t=1.3, hold=6)
        b.step(st.show("note", note("Kurlat's verdict, stated before the evidence: "
                                    "'decisively rejected'")), t=0.8, hold=4)
        b.step(st.show("main", note("Three tests follow.\n\n"
                                    "They use different data and fail in different ways.\n\n"
                                    "Any one alone could be explained away.\n"
                                    "Together they cannot.")), t=1.3, hold=6)
        b.step(st.show("note", note("test one: does growth fall with income across countries?")), t=0.7, hold=3)
        b.step(st.show("note", note("test two: does measured capital predict measured output?")), t=0.7, hold=3)
        b.step(st.show("note", note("test three: are the implied interest rates believable?")), t=0.7, hold=3)
        b.step(st.show("note", note("different data, different failure modes")), t=0.7, hold=3)
        b.step(st.show("note", note("that is what makes the rejection hard to argue with")), t=0.7, hold=3)
        b.run()


class BeatTest1(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatTest1")
        s = Stack(st, size=30, rows=5)
        b.step(st.show("title", title("Test one: convergence")), t=0.8, hold=1)
        b.step(st.show("note", note("a poor country is just a rich country earlier on the "
                                    "same path -- so it should grow faster")), t=0.8, hold=4)
        b.step(s.add(r"g_y = \frac{f(k_{t+1}) - f(k_t)}{f(k_t)}"), t=1.3, hold=4)
        b.step(s.add(r"\simeq \frac{f'(k_t)\left[k_{t+1}-k_t\right]}{f(k_t)}", colour=FOCUS),
               t=1.3, hold=4)
        b.step(st.show("note", note("a first-order Taylor step -- the only approximation "
                                    "in the derivation")), t=0.8, hold=4)
        b.step(s.add(r"= \frac{f'(k_t)\left[sf(k_t)-\delta k_t\right]}{f(k_t)}"),
               t=1.4, hold=4)
        b.step(s.add(r"= s f'(k_t) - \delta\,\frac{f'(k_t)k_t}{f(k_t)} "
                     r"= s f'(k_t) - \delta\alpha", colour=KEEP), t=1.5, hold=5)
        b.step(st.show("note", note("growth depends on k ONLY through f'(k) -- which is "
                                    "decreasing")), t=0.8, hold=5)
        b.step(st.show("note", note("so the richer country must grow more slowly. "
                                    "At every point, not just near the steady state")),
               t=0.8, hold=5)
        b.step(st.show("main", eq(r"\text{the scatter says no. FAILED}", size=50,
                                  colour=BROKEN)), t=1.2, hold=5)
        b.step(st.show("title", title("Two honest qualifications")), t=0.8, hold=2)
        b.step(st.show("main", note("1. POPULATION WEIGHTING. Weight by population and the\n"
                                    "   data DO converge, since 1980. China and India\n"
                                    "   started poor, grew fast, and are a third of\n"
                                    "   humanity.\n\n"
                                    "   Is weighting right? A small country is as\n"
                                    "   informative an experiment as a large one -- but\n"
                                    "   perhaps India's states should count separately.")),
               t=1.4, hold=6)
        b.step(st.show("main", note("2. WITHIN GROUPS. Among US states since 1929, and\n"
                                    "   among Western European countries, poorer units\n"
                                    "   genuinely did grow faster. Strongly.\n\n"
                                    "   So the conjecture may hold WITHIN a set sharing\n"
                                    "   technology and institutions, while failing ACROSS\n"
                                    "   such sets.")), t=1.4, hold=6)
        b.step(st.show("note", note("capital may explain why one US state is richer than "
                                    "another, without explaining the US against Paraguay")),
               t=0.8, hold=5)
        b.step(st.show("note", note("so the conjecture survives inside a group and dies across groups")), t=0.7, hold=3)
        b.run()


class BeatSpeed(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatSpeed")
        s = Stack(st, size=30, rows=5)
        b.step(st.show("title", title("And a quantitative version: how FAST?")), t=0.8, hold=2)
        b.step(s.add(r"\frac{\dot{\tilde k}}{\tilde k} = s\,\tilde k^{\alpha-1} "
                     r"- (\delta+n+g)"), t=1.3, hold=4)
        b.step(s.add(r"x \equiv \ln\tilde k - \ln\tilde k_{ss}", colour=FOCUS), t=1.2, hold=4)
        b.step(s.add(r"\dot x = (\delta+n+g)\left[e^{(\alpha-1)x} - 1\right]"),
               t=1.4, hold=4)
        b.step(st.show("note", note("using the steady-state condition to replace "
                                    "s k-tilde^(alpha-1)")), t=0.8, hold=4)
        b.step(st.show("note", note("now expand the exponential to first order about "
                                    "x = 0")), t=0.8, hold=3)
        b.step(s.add(r"\dot x \simeq -(1-\alpha)(\delta+n+g)\,x \;\Rightarrow\; "
                     r"x_t = x_0 e^{-\lambda t}", size=28), t=1.5, hold=5)
        b.step(s.collapse(r"\lambda = (1-\alpha)(\delta+n+g) = 0.65 \times 0.065 = 4.2\%",
                          size=40), t=1.4, hold=6)
        b.step(st.show("note", note("a half-life of about sixteen years")), t=0.8, hold=4)
        b.step(st.show("main", table(["convergence speed", "half-life"],
                                     [("model: 4.2% a year", "16 years"),
                                      ("data: ~2% a year", "35 years")],
                                     col_widths=[5.0, 3.4],
                                     cell_colours={(1, 0): BROKEN, (1, 1): BROKEN})),
               t=1.3, hold=6)
        b.step(st.show("title", title("So what alpha would the data need?")), t=0.8, hold=2)
        b.step(st.show("main", eq(r"1-\alpha = \frac{0.02}{0.065} \;\Rightarrow\; "
                                  r"\alpha \simeq 0.69", size=50, colour=FOCUS)),
               t=1.3, hold=6)
        b.step(st.show("note", note("twice the capital share in the accounts. Hold that "
                                    "number -- it comes back from another direction")),
               t=0.8, hold=5)
        b.run()


class BeatTest2(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatTest2")
        b.step(st.show("title", title("Test two: predicted levels")), t=0.8, hold=1)
        b.step(st.show("note", note("forget growth rates. Take measured capital stocks and "
                                    "ask what output the model predicts")), t=0.8, hold=4)
        b.step(st.show("main", table(["poorest countries", "per person"],
                                     [("model predicts", "$10,000"),
                                      ("actual", "$1,000")],
                                     col_widths=[4.6, 3.4],
                                     cell_colours={(0, 1): BROKEN, (1, 1): FOCUS})),
               t=1.3, hold=6)
        b.step(st.show("note", note("a factor of ten, in the wrong direction")),
               t=0.8, hold=4)
        b.step(st.show("note", note("and the gap gets LARGER the poorer the country -- "
                                    "exactly where the conjecture most needs to succeed")),
               t=0.8, hold=5)
        b.step(st.show("note", note("not a calibration quibble you can fix with a "
                                    "different delta")), t=0.8, hold=4)
        b.step(st.show("main", eq(r"\text{FAILED}", size=60, colour=BROKEN)), t=1.1, hold=4)
        b.step(st.show("note", note("but this test needed capital-stock data -- the "
                                    "weakest data in the exercise")), t=0.8, hold=4)
        b.step(st.show("title", title("Which is why the third test is the one that matters")),
               t=0.8, hold=4)
        b.step(st.show("note", note("and the sceptic still has a move: distrust the capital data")), t=0.7, hold=3)
        b.step(st.show("note", note("so the third test uses none")), t=0.7, hold=3)
        b.step(st.show("note", note("only relative incomes, and the capital share")), t=0.7, hold=3)
        b.run()


class BeatLucas(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatLucas")
        s = Stack(st, size=30, rows=4)
        b.step(st.show("title", title("Test three: no capital data at all")), t=0.8, hold=2)
        b.step(st.show("note", note("only relative incomes and the capital share")),
               t=0.8, hold=3)
        b.step(s.add(r"x = \frac{y_A}{y_B} = \left(\frac{k_A}{k_B}\right)^{\alpha}"),
               t=1.3, hold=4)
        b.step(s.add(r"\frac{r^K_A}{r^K_B} = \left(\frac{k_A}{k_B}\right)^{\alpha-1}"),
               t=1.3, hold=4)
        b.step(st.show("note", note("eliminate the capital ratio, which we do not know "
                                    "and do not want")), t=0.8, hold=3)
        b.step(s.collapse(r"\frac{r^K_A}{r^K_B} = x^{\frac{\alpha-1}{\alpha}}, "
                          r"\qquad \frac{\alpha-1}{\alpha} = -1.857", size=44),
               t=1.4, hold=6)
        b.step(st.show("main", table(["country", "y / y_US", "rental vs US", "implied r"],
                                     [("Mexico (Kurlat)", "0.30", "9.4x", "-"),
                                      ("Brazil", "0.257", "12.5x", "138% a year"),
                                      ("India", "0.119", "51.9x", "586% a year")],
                                     col_widths=[3.6, 2.4, 2.8, 3.0],
                                     cell_colours={(1, 3): BROKEN, (2, 3): BROKEN})),
               t=1.4, hold=6)
        b.step(st.show("note", note("nothing remotely like that exists anywhere")),
               t=0.8, hold=4)
        b.step(st.show("note", note("and the corollary is worse: capital would pour into "
                                    "Brazil until the rates equalised. It does not")),
               t=0.8, hold=5)
        b.step(st.show("main", eq(r"\text{the LUCAS PARADOX. FAILED}", size=48,
                                  colour=BROKEN)), t=1.2, hold=5)
        b.step(st.show("title", title("Why is the exponent so violent?")), t=0.8, hold=2)
        b.step(st.show("note", note("alpha is small. Explaining a big output gap through "
                                    "capital alone needs an ENORMOUS capital gap")),
               t=0.8, hold=5)
        b.step(st.show("note", note("and diminishing returns then prices that scarce "
                                    "capital extravagantly")), t=0.8, hold=4)
        b.step(st.show("main", eq(r"\alpha = 0.7 \;\Rightarrow\; \text{exponent} = -0.43 "
                                  r"\;\Rightarrow\; 1.6\times", size=44, colour=FOCUS)),
               t=1.3, hold=5)
        b.step(st.show("note", note("there is that number again. Two failures, both asking "
                                    "for a capital share near 0.7")), t=0.8, hold=5)
        b.step(st.show("note", note("no capital stock estimate appears anywhere in that derivation")), t=0.7, hold=3)
        b.run()

# ------------------------------------------------------------------ Act V

class BeatResidual(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatResidual")
        s = Stack(st, size=28, rows=5)
        b.step(st.show("title", title("Three tests, three failures")), t=0.8, hold=2)
        b.step(st.show("note", note("what is left? Whatever makes given capital and labour "
                                    "produce more or less output")), t=0.8, hold=4)
        b.step(s.add(r"Y_t = F(K_t, L_t, A_t)", colour=OBJ), t=1.1, hold=4)
        b.step(st.show("note", note("technology as a SEPARATE argument -- not committing "
                                    "to where it sits")), t=0.8, hold=3)
        b.step(s.add(r"\dot Y = F_K\dot K + F_L\dot L + F_A\dot A"), t=1.3, hold=4)
        b.step(st.show("note", note("total differentiation with respect to time")),
               t=0.7, hold=3)
        b.step(s.add(r"\frac{\dot Y}{Y} = \frac{F_KK}{Y}\frac{\dot K}{K} "
                     r"+ \frac{F_LL}{Y}\frac{\dot L}{L} + \frac{F_AA}{Y}\frac{\dot A}{A}",
                     size=26), t=1.5, hold=5)
        b.step(st.show("note", note("divide by Y, then multiply and divide each term so "
                                    "every piece is a growth rate")), t=0.8, hold=4)
        b.step(st.show("title", title("Now look at what those coefficients became")),
               t=0.8, hold=2)
        b.step(st.show("main", note("They are ELASTICITIES of the production function --\n"
                                    "objects nobody can observe.\n\n"
                                    "But by Act II, competitive factor markets make them\n"
                                    "equal to factor SHARES -- which are line items in\n"
                                    "the national accounts.\n\n"
                                    "That is the only reason growth accounting can be\n"
                                    "done at all.")), t=1.4, hold=6)
        b.step(st.show("main", eq(r"g_Y = g_A + \alpha g_K + (1-\alpha)g_L", size=52,
                                  colour=KEEP)), t=1.3, hold=5)
        b.step(st.show("main", eq(r"g_y = g_A + \alpha g_k", size=56, colour=KEEP)),
               t=1.2, hold=5)
        b.step(st.show("main", eq(r"g_A = g_Y - \alpha g_K - (1-\alpha)g_L", size=48,
                                  colour=FOCUS)), t=1.3, hold=5)
        b.step(st.show("note", note("the SOLOW RESIDUAL. Nothing about A was observed -- "
                                    "it is defined as whatever makes the identity balance")),
               t=0.8, hold=5)
        b.run()


class BeatIgnorance(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatIgnorance")
        b.step(st.show("title", title("The most important caveat in this session")),
               t=0.8, hold=2)
        b.step(st.show("note", note("the residual gets called 'technology'. It is not "
                                    "technology")), t=0.8, hold=4)
        b.step(st.show("main", note("What is actually inside it:\n\n"
                                    "  genuine technical progress -- some of it\n"
                                    "  MISMEASURED INPUTS: idle capital, effort, quality\n"
                                    "  COMPOSITION: workers moving between sectors\n"
                                    "  ALLOCATION: the same inputs, distributed better\n"
                                    "  institutions, distortions, misallocation\n"
                                    "  and every error in alpha, in K, in L")),
               t=1.4, hold=6)
        b.step(st.show("main", eq(r"\text{``a measure of our ignorance''}", size=48,
                                  colour=BROKEN)), t=1.2, hold=5)
        b.step(st.show("note", note("Abramovitz. That is not modesty -- it is a definition")),
               t=0.8, hold=4)
        b.step(st.show("title", title("Two consequences")), t=0.8, hold=1)
        b.step(st.show("note", note("measured TFP is strongly PROCYCLICAL -- it falls in "
                                    "recessions")), t=0.8, hold=4)
        b.step(st.show("note", note("as a claim about technology that is absurd. Technology "
                                    "does not regress in a recession")), t=0.8, hold=5)
        b.step(st.show("note", note("most of it is unmeasured capital utilisation")),
               t=0.8, hold=4)
        b.step(st.show("title", title("And the one that matters here")), t=0.8, hold=2)
        b.step(st.show("note", note("writing down that a poor country has low TFP explains "
                                    "nothing. You have named a residual")), t=0.8, hold=5)
        b.step(st.show("note", note("calling it 'technology' is a decision about "
                                    "vocabulary, not a finding about the world")),
               t=0.8, hold=5)
        b.run()


class BeatDevAccounting(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatDevAccounting")
        s = Stack(st, size=30, rows=4)
        b.step(st.show("title", title("Two exercises, nearly identical algebra")),
               t=0.8, hold=2)
        b.step(st.show("main", table(["", "growth accounting", "development accounting"],
                                     [("asks", "why did THIS country grow?",
                                       "why is THIS country poorer?"),
                                      ("data", "one country, many dates",
                                       "many countries, one date"),
                                      ("object", "growth rates", "levels")],
                                     col_widths=[2.2, 4.6, 4.8])), t=1.4, hold=6)
        b.step(st.show("note", note("nothing in the mathematics stops you confusing them")),
               t=0.8, hold=3)
        b.step(s.add(r"y = A k^{\alpha}", colour=OBJ), t=1.0, hold=3)
        b.step(s.add(r"\ln\frac{y_i}{y_{US}} = \alpha\ln\frac{k_i}{k_{US}} "
                     r"+ \ln\frac{A_i}{A_{US}}", colour=KEEP), t=1.4, hold=5)
        b.step(st.show("note", note("the first term we can measure. The second is the "
                                    "residual again")), t=0.8, hold=4)
        b.step(st.show("title", title("Work an example")), t=0.8, hold=1)
        b.step(st.show("main", note("A country at 1/10 of US income per worker,\n"
                                    "with 15% of US capital per worker.\n\n"
                                    "capital contributes  0.15^0.35 = 0.515\n"
                                    "so TFP must supply   0.10 / 0.515 = 0.194")),
               t=1.3, hold=6)
        b.step(st.show("main", table(["share of the log gap", ""],
                                     [("capital", "28.8%"), ("TFP", "71.2%")],
                                     col_widths=[4.6, 3.0],
                                     cell_colours={(1, 1): FOCUS})), t=1.3, hold=6)
        b.step(st.show("note", note("capital explains a factor of 2 out of a factor of 10. "
                                    "TFP explains the other factor of 5")), t=0.8, hold=5)
        b.step(st.show("note", note("that is the standard headline -- and it is about to "
                                    "move by twenty points")), t=0.8, hold=4)
        b.step(st.show("note", note("capital explains a factor of two; TFP explains the other five")), t=0.7, hold=3)
        b.run()


class BeatKYform(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatKYform")
        s = Stack(st, size=30, rows=4)
        b.step(st.show("title", title("There is a real problem with that decomposition")),
               t=0.8, hold=2)
        b.step(st.show("main", note("CAPITAL IS ENDOGENOUS.\n\n"
                                    "A productive country is a profitable place to invest,\n"
                                    "so it accumulates more capital.\n\n"
                                    "Crediting 'capital' with that is crediting it with\n"
                                    "something productivity caused.")), t=1.3, hold=6)
        b.step(st.show("note", note("the two terms are not independent, so splitting them "
                                    "is misleading")), t=0.8, hold=4)
        b.step(st.show("title", title("Decompose with K/Y instead")), t=0.8, hold=1)
        b.step(s.add(r"y = A k^{\alpha} = A\left(\frac{K}{Y}\right)^{\alpha}"
                     r"\left(\frac{Y}{L}\right)^{\alpha}", size=28), t=1.4, hold=4)
        b.step(s.add(r"y^{1-\alpha} = A\left(\frac{K}{Y}\right)^{\alpha}"), t=1.3, hold=4)
        b.step(s.collapse(r"y = A^{\frac{1}{1-\alpha}}"
                          r"\left(\frac{K}{Y}\right)^{\frac{\alpha}{1-\alpha}}", size=50),
               t=1.4, hold=6)
        b.step(st.show("note", note("why better? K/Y is constant on a balanced path and "
                                    "does not respond to technology in the long run")),
               t=0.8, hold=5)
        b.step(st.show("note", note("so the two terms are much closer to independent")),
               t=0.8, hold=4)
        b.step(st.show("note", note("the exponent is bigger -- 0.54 -- but applied to a "
                                    "ratio that varies far LESS across countries")),
               t=0.8, hold=5)
        b.step(st.show("main", table(["share of the log gap", "K/L form", "K/Y form"],
                                     [("capital", "28.8%", "5.2%"),
                                      ("TFP", "71.2%", "94.8%")],
                                     col_widths=[3.8, 3.0, 3.0],
                                     cell_colours={(0, 2): FOCUS, (1, 2): BROKEN})),
               t=1.4, hold=6)
        b.step(st.show("note", note("not 29 per cent. Five")), t=0.8, hold=4)
        b.step(st.show("title", title("Always say which decomposition you used")),
               t=0.8, hold=4)
        b.run()


class BeatHumanCapital(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatHumanCapital")
        s = Stack(st, size=30, rows=4)
        b.step(st.show("title", title("One obvious objection left")), t=0.8, hold=1)
        b.step(st.show("note", note("labour is not homogeneous. 12 years of schooling "
                                    "against 4 is not 'one unit of labour' twice")),
               t=0.8, hold=4)
        b.step(s.add(r"Y = A K^{\alpha}(hL)^{1-\alpha}", colour=OBJ), t=1.2, hold=4)
        b.step(st.show("title", title("But how do you measure h?")), t=0.8, hold=2)
        b.step(st.show("main", note("MINCER WAGE REGRESSIONS.\n\n"
                                    "In essentially every country, log wages rise\n"
                                    "roughly linearly in years of schooling, with a\n"
                                    "return of about 6 to 10% per year.")), t=1.3, hold=6)
        b.step(s.add(r"\ln w = \text{const} + \phi S"), t=1.2, hold=4)
        b.step(st.show("note", note("and in competitive labour markets workers are paid "
                                    "their marginal product")), t=0.8, hold=4)
        b.step(st.show("note", note("so if a year of school raises your wage by 10%, it "
                                    "raised your productivity by 10%")), t=0.8, hold=4)
        b.step(s.collapse(r"h = e^{\phi S}", size=60), t=1.2, hold=5)
        b.step(st.show("main", note("4 years against 12, at phi = 0.10:\n\n"
                                    "   h_i / h_US = e^(-0.8) = 0.45\n\n"
                                    "contribution to income: 0.45^0.65 = 0.59\n\n"
                                    "So human capital explains a factor of 1.7,\n"
                                    "out of a tenfold gap.")), t=1.4, hold=6)
        b.step(st.show("note", note("real, and nowhere near sufficient")), t=0.8, hold=4)
        b.step(st.show("title", title("And one exponent trap")), t=0.8, hold=2)
        b.step(st.show("main", eq(r"\text{K/L form: } h^{1-\alpha} \qquad "
                                  r"\text{K/Y form: } h^{1}", size=44, colour=FOCUS)),
               t=1.3, hold=5)
        b.step(st.show("note", note("carry the wrong one across and you understate human "
                                    "capital by a third")), t=0.8, hold=5)
        b.run()


class BeatClose(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatClose")
        def bar(cap, hum, tfp, label):
            widths = [9.0 * cap, 9.0 * hum, 9.0 * tfp]
            cols = [KEEP, FOCUS, BROKEN]
            parts = VGroup(*[Rectangle(width=max(w, 0.12), height=0.7,
                                       color=c, fill_opacity=0.55, stroke_width=2)
                             for w, c in zip(widths, cols)]).arrange(RIGHT, buff=0)
            return VGroup(Text(label, font_size=20, color=MUTED), parts).arrange(DOWN, buff=0.2)
        bars = VGroup(bar(0.288, 0.10, 0.612, "K/L form:  capital 29%"),
                      bar(0.052, 0.10, 0.848, "K/Y form:  capital 5%")
                      ).arrange(DOWN, buff=0.9)
        b.step(st.show("title", title("So where does that leave us?")), t=0.8, hold=1)
        b.step(st.show("main", note("We repaired the model: output per worker now grows\n"
                                    "forever, at g -- which the model assumes.\n\n"
                                    "Then it failed three independent tests.\n\n"
                                    "What survives is a residual. And the residual is\n"
                                    "most of the answer.")), t=1.4, hold=6)
        b.step(st.show("title", title("So where do productivity differences come from?")),
               t=0.8, hold=2)
        b.step(st.show("main", note("MISALLOCATION -- the same technology, used badly.\n"
                                    "   US allocative efficiency would raise China and\n"
                                    "   India's productivity by 30 to 60 per cent.\n\n"
                                    "INSTITUTIONS -- property rights, enforcement.\n\n"
                                    "BARRIERS TO ADOPTION -- knowledge is non-rival and\n"
                                    "   ought to spread. Something stops it.\n\n"
                                    "SCHOOLING QUALITY, not quantity.\n\n"
                                    "MEASUREMENT -- some of it is not real.")),
               t=1.4, hold=6)
        b.step(st.show("title", title("Hold this frame")), t=0.8, hold=2)
        b.step(st.show("main", bars), t=1.3, hold=5)
        b.step(st.show("note", note("the same income gap, split twice")), t=0.8, hold=4)
        b.step(st.show("note", note("capital shrinks from 29 per cent of the gap to five")),
               t=0.8, hold=4)
        b.step(st.show("note", note("and the productivity block swells to fill almost "
                                    "all of it")), t=0.8, hold=4)
        b.step(st.show("title", title("The residual is what we cannot explain")),
               t=0.8, hold=3)
        b.step(st.show("note", note("and its size depends on a choice you have to declare")),
               t=0.8, hold=4)
        b.step(st.show("main", note("The honest verdict:\n\n"
                                    "Solow localises the problem with real precision.\n\n"
                                    "It PROVES the answer is not capital -- a genuine,\n"
                                    "non-obvious, hard-won result.\n\n"
                                    "Then it names what is left, and hands it over.")),
               t=1.4, hold=6)
        b.step(st.show("title", title("Next: where does the saving rate come from?")),
               t=0.8, hold=4)
        b.run()
