"""Scenes for aula-07-money-and-inflation (group g2).

Durations come from beats.json via the kit. Do not hard-code seconds.
Render: python -m manim render -ql --media_dir media scenes_g2.py BeatX
"""
import numpy as np
from manim import *

from video_explainer import (axes_panel, balance_sheet, Beat, bullets, cell, eq, note, ols,
                             palette, read_csv, sawtooth, scatter, series, Stage, table,
                             title, FAST, NORMAL, SLOW)


class BeatSix(Scene):
    """Where money comes from: one real ledger, changed a line at a time.

    The ledger is a four-column table, so every number is its own cell and the open
    market operation, the loan and the cash withdrawal are each a Transform of the
    same sheet. Net worth stays at 20 throughout, on screen, which is the point.
    """

    @staticmethod
    def ledger(loans, bonds, reserves, deposits, colours=None):
        sheet = table(["assets", "", "liabilities", ""],
                      [("loans", loans, "deposits", deposits),
                       ("bonds", bonds, "net worth", "20"),
                       ("reserves", reserves, "", "")],
                      col_widths=[1.95, 1.0, 1.95, 1.0],
                      row_height=0.6, font_size=20, cell_colours=colours or {})
        return VGroup(Text("commercial bank", font_size=21, color=GREY), sheet) \
            .arrange(DOWN, buff=0.26)

    def construct(self):
        st, b = Stage(self), Beat(self, "BeatSix")

        b.step(st.show("title", title("Where money comes from")), t=0.6, hold=1)
        b.step(st.show("note", note("deposits are a bank's liability, and deposits are most of the money")),
               t=0.8, hold=2)

        sheet = self.ledger("90", "20", "10", "100")
        b.step(st.show("left", sheet), t=1.0, hold=2)
        b.step([Indicate(cell(sheet, "loans"), color=BLUE)], t=0.7, hold=1)
        b.step([Indicate(cell(sheet, "bonds"), color=BLUE)], t=0.7, hold=1)
        b.step([Indicate(cell(sheet, "reserves"), color=YELLOW)], t=0.8, hold=2)

        cb = VGroup(Text("central bank", font_size=21, color=GREY),
                    balance_sheet([("government bonds", None)],
                                  [("reserves", YELLOW), ("currency", None)],
                                  width=4.8, font_size=19)).arrange(DOWN, buff=0.26)
        b.step(st.show("right", cb), t=1.0, hold=3)
        b.step(st.show("note", note("the bank's asset is the central bank's liability, and it pays almost nothing",
                                    size=22)), t=0.8, hold=2)

        b.step([Indicate(cell(sheet, "deposits"), color=BLUE)], t=0.7, hold=2)
        b.step(st.show("note", note("net worth is just assets minus liabilities", size=22))
               + [Indicate(cell(sheet, "net worth"), color=GREY)], t=0.8, hold=2)

        why = VGroup(note("1.  to meet unexpected withdrawals\n     (which mattered more before\n     deposit insurance)", size=19),
                     note("2.  because regulation requires it", size=19, colour=YELLOW)) \
            .arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        b.step(st.show("right", why), t=0.9, hold=3)

        rule = VGroup(eq(r"\text{reserves} \;\ge\; \theta \times \text{deposits}", size=30, colour=YELLOW),
                      note("the reason that binds today", size=19)).arrange(DOWN, buff=0.35)
        b.step(st.show("right", rule), t=0.9, hold=3)
        b.step(st.show("note", note("so a bank holds as few reserves as the rule allows", colour=YELLOW)),
               t=0.8, hold=3)

        b.step(st.show("note", note("an open market operation: the central bank buys the bonds\nand pays with reserves it creates",
                                    size=22)), t=0.8, hold=2)
        after_omo = Stage.fit(self.ledger("90", "10", "20", "100",
                                          {(2, 0): YELLOW, (2, 1): YELLOW}), "left")
        b.step([Transform(sheet, after_omo)], t=1.3, hold=3)

        check = table(["reserves", ""],
                      [("required", "10"), ("actual", "20"), ("excess", "10")],
                      col_widths=[2.6, 1.2], row_height=0.6, font_size=20,
                      cell_colours={(2, 0): RED, (2, 1): RED})
        b.step(st.show("right", check), t=1.0, hold=3)
        b.step(st.show("note", note("excess reserves earn nothing, so the bank lends them out", colour=RED)),
               t=0.8, hold=2)

        after_loan = Stage.fit(self.ledger("100", "10", "20", "110",
                                           {(0, 1): BLUE, (0, 3): BLUE,
                                            (2, 0): YELLOW, (2, 1): YELLOW}), "left")
        b.step([Transform(sheet, after_loan)], t=1.3, hold=3)
        b.step(st.show("note", note("it writes a loan, the borrower deposits the proceeds: deposits have risen",
                                    size=22)), t=0.8, hold=2)

        fix = VGroup(note("the reserves did not leave", colour=YELLOW, size=25),
                     note("they are still on a balance sheet;\nwhat vanished is the slack\nagainst the requirement", size=19)) \
            .arrange(DOWN, buff=0.35)
        b.step(st.show("right", fix), t=1.0, hold=3)
        b.step(st.show("note", note("and nobody's net worth changed: 20 before, 20 after", size=22))
               + [Indicate(cell(sheet, "net worth"), color=GREEN)], t=1.0, hold=3)

        after_cash = Stage.fit(self.ledger("100", "10", "15", "105",
                                            {(2, 1): YELLOW, (0, 3): BLUE}), "left")
        b.step(st.show("note", note("some of the new deposits walk out as cash,\nand the central bank debits the reserves",
                                    size=22)) + [Transform(sheet, after_cash)], t=1.3, hold=3)

        geo = VGroup(note("and now it repeats, smaller", size=21),
                     eq(r"1,\ \rho,\ \rho^{2},\ \rho^{3},\ \dots", size=34, colour=BLUE),
                     eq(r"\rho = (1-\theta)(1-\gamma)", size=24, colour=GREY)) \
            .arrange(DOWN, buff=0.3)
        b.step(st.show("right", geo), t=1.0, hold=3)
        b.run()


class BeatSeven(Scene):
    """The rounds stack, the running total converges, and the limit is the multiplier."""

    THETA, GAMMA = 0.10, 0.20

    @staticmethod
    def bar(ax, k, h, colour, ghost=False):
        p0, p1 = ax.c2p(k + 0.18, 0), ax.c2p(k + 0.82, h)
        rect = Rectangle(width=abs(p1[0] - p0[0]),
                         height=max(abs(p1[1] - p0[1]), 0.04),
                         color=colour, stroke_width=2,
                         fill_opacity=0.0 if ghost else 0.55)
        rect.move_to((np.array(p0) + np.array(p1)) / 2)
        return DashedVMobject(rect, num_dashes=14, color=colour) if ghost else rect

    def construct(self):
        st, b = Stage(self), Beat(self, "BeatSeven")
        rho = (1 - self.THETA) * (1 - self.GAMMA)
        limit = 1.0 / (self.THETA + self.GAMMA - self.THETA * self.GAMMA)

        b.step(st.show("title", title("Summing the rounds")), t=0.6, hold=1)
        b.step(st.show("note", note("each round is the one before it, scaled down")), t=0.7, hold=1)

        ax, chart = axes_panel([0, 9, 1], [0, 4, 1], x_label="round",
                               y_label="multiples of the injection",
                               width=4.9, height=3.2, coords=True)
        b.step(st.show("left", chart), t=1.0, hold=1)
        b.step(st.add_to("left", self.bar(ax, 0, 1.0, YELLOW)), t=0.8, hold=2)

        leak_r = VGroup(eq(r"\theta", size=40, colour=YELLOW),
                        note("of each new deposit is held as reserves,\nso that much cannot be lent again", size=20)) \
            .arrange(DOWN, buff=0.3)
        b.step(st.show("right", leak_r), t=0.9, hold=3)
        leak_c = VGroup(eq(r"\gamma", size=40, colour=YELLOW),
                        note("of the new money walks out as cash,\nwhich leaves the deposit system", size=20)) \
            .arrange(DOWN, buff=0.3)
        b.step(st.show("right", leak_c), t=0.9, hold=3)

        chain = eq(r"\rho = (1-\theta)(1-\gamma) = 0.72", size=32, colour=BLUE)
        b.step(st.show("right", chain), t=0.9, hold=3)

        for k, t in [(1, 0.7), (2, 0.7), (3, 0.6), (4, 0.6), (5, 0.6)]:
            b.step(st.add_to("left", self.bar(ax, k, rho ** k, BLUE)), t=t, hold=1)

        ghosts = VGroup(*[self.bar(ax, k, rho ** k, GREY, ghost=True) for k in (6, 7, 8)])
        b.step(st.add_to("left", ghosts), t=0.8, hold=2)

        cap = DashedLine(ax.c2p(0, limit), ax.c2p(9, limit), color=GREY, stroke_width=3)
        cap_lab = Text(f"{limit:.2f}", font_size=19, color=GREY).next_to(ax.c2p(0, limit), UL, buff=0.06)
        b.step(st.add_to("left", VGroup(cap, cap_lab)), t=0.9, hold=2)

        cum, total = [], 0.0
        for k in range(9):
            total += rho ** k
            cum.append((k + 0.5, total))
        running = series(ax, cum, colour=GREEN, width=5)
        b.step(st.add_to("left", running), t=1.2, hold=3)

        summed = Stage.fit(VGroup(
            eq(r"\Delta M1 = \Delta\text{base}\,(1+\rho+\rho^{2}+\cdots)", size=26),
            eq(r"= \dfrac{\Delta\text{base}}{1-\rho}", size=26)).arrange(DOWN, buff=0.3), "right")
        b.step([Transform(chain, summed)], t=1.5, hold=3)

        mult = Stage.fit(eq(r"\dfrac{\Delta M1}{\Delta\text{base}} = \dfrac{1}{\theta+\gamma-\theta\gamma}",
                            size=34, colour=YELLOW), "right")
        b.step([Transform(chain, mult)], t=1.5, hold=3)
        b.step(st.show("note", note("say the denominator carefully: theta plus gamma minus theta gamma",
                                    colour=YELLOW)), t=0.8, hold=2)

        lever = Stage.fit(VGroup(eq(r"\Delta M1 = \dfrac{1}{\theta+\gamma-\theta\gamma}\;\Delta\text{base}",
                                    size=28, colour=YELLOW),
                                 note("the bank moves the base;\nthe money stock moves by this much", size=19)) \
                          .arrange(DOWN, buff=0.35), "right")
        b.step([Transform(chain, lever)], t=1.5, hold=3)

        roles = table(["", "what it is", "who sets it"],
                      [("theta", "the reserve ratio", "the central bank"),
                       ("gamma", "the cash share of money", "the public")],
                      col_widths=[1.7, 4.2, 3.6], row_height=0.7, font_size=23,
                      cell_colours={(0, 0): GREEN, (0, 2): GREEN, (1, 0): RED, (1, 2): RED})
        b.step([*st.clear("left", "right"), *st.show("main", roles)], t=1.2, hold=4)
        b.step(st.show("note", note("one argument is an instrument, the other is behaviour")), t=0.8, hold=3)
        b.step(st.show("note", note("the base it controls directly; the broader measure only through\na multiplier it does not fully own",
                                    size=22)), t=0.9, hold=3)

        notation = VGroup(
            VGroup(Text("your rules file", font_size=21, color=GREY),
                   eq(r"\frac{1+cd}{rr+cd}", size=36)).arrange(DOWN, buff=0.28),
            VGroup(Text("the book", font_size=21, color=GREY),
                   eq(r"\frac{1}{\theta+\gamma-\theta\gamma}", size=36)).arrange(DOWN, buff=0.28),
        ).arrange(RIGHT, buff=2.4)
        notation = VGroup(notation, Text("different definitions, different numbers, the same economy",
                                         font_size=21, color=GREY)).arrange(DOWN, buff=0.6)
        b.step(st.show("main", notation), t=1.2, hold=3)
        b.step(st.show("note", note("pick one, say which, and stay with it", colour=YELLOW)), t=0.8, hold=3)
        b.run()


class BeatEight(Scene):
    """The assumption the multiplier rests on, and the decade in which it failed."""

    BASE = [(2008, 1.0), (2009, 2.3), (2010, 2.5), (2011, 3.3),
            (2012, 3.6), (2013, 4.2), (2014, 4.8), (2015, 4.8)]
    M1 = [(2008, 1.0), (2009, 1.15), (2010, 1.25), (2011, 1.45),
          (2012, 1.6), (2013, 1.7), (2014, 1.8), (2015, 1.85)]

    @staticmethod
    def earns(reserve_return, colour):
        sheet = table(["asset", "what it earns"],
                      [("loans", "i"), ("reserves", reserve_return)],
                      col_widths=[2.3, 2.5], row_height=0.66, font_size=22,
                      cell_colours={(1, 1): colour})
        return VGroup(Text("what a bank earns at the margin", font_size=20, color=GREY),
                      sheet).arrange(DOWN, buff=0.28)

    @staticmethod
    def bar(ax, k, h, colour, ghost=False):
        p0, p1 = ax.c2p(k + 0.18, 0), ax.c2p(k + 0.82, h)
        rect = Rectangle(width=abs(p1[0] - p0[0]),
                         height=max(abs(p1[1] - p0[1]), 0.04),
                         color=colour, stroke_width=2,
                         fill_opacity=0.0 if ghost else 0.55)
        rect.move_to((np.array(p0) + np.array(p1)) / 2)
        return DashedVMobject(rect, num_dashes=12, color=colour) if ghost else rect

    def construct(self):
        st, b = Stage(self), Beat(self, "BeatEight")

        b.step(st.show("title", title("Where the multiplier breaks")), t=0.6, hold=1)

        sheet = self.earns("0", GREY)
        b.step(st.show("left", sheet), t=1.0, hold=2)
        box = SurroundingRectangle(sheet, color=YELLOW, buff=0.22)
        b.step(st.add_to("left", box)
               + [FadeIn(Text("", font_size=1))], t=0.9, hold=2)
        b.step(st.show("note", note("every step of the derivation rested on this one assumption",
                                    colour=YELLOW)), t=0.8, hold=2)
        b.step(st.show("note", note("so ask what happens when it stops being true")), t=0.8, hold=2)

        zero = VGroup(eq(r"i \to 0", size=40, colour=RED),
                      note("the nominal rate falls to almost nothing", size=20)).arrange(DOWN, buff=0.3)
        b.step(st.show("right", zero), t=0.9, hold=3)
        ior = VGroup(eq(r"i_{\text{reserves}} \approx i", size=38, colour=RED),
                     note("or the central bank starts paying\ninterest on reserves", size=20)).arrange(DOWN, buff=0.3)
        b.step(st.show("right", ior), t=0.9, hold=3)

        b.step([Transform(sheet, Stage.fit(self.earns("about i", RED), "left"))], t=1.2, hold=3)
        b.step(st.show("note", note("reserves are no longer the worst asset a bank can hold", colour=RED)),
               t=0.8, hold=3)
        b.step(st.show("note", note("a bank handed new reserves has no particular reason to lend them out",
                                    size=22)), t=0.8, hold=3)

        ax, chain = axes_panel([0, 6, 1], [0, 1.2, 0.5], x_label="round",
                               y_label="new deposits", width=7.4, height=2.9, coords=True)
        b.step([*st.clear("left", "right"), *st.show("main", chain)], t=1.2, hold=1)
        b.step(st.add_to("main", self.bar(ax, 0, 1.0, YELLOW)), t=0.8, hold=2)
        ghosts = VGroup(*[self.bar(ax, k, 0.72 ** k, GREY, ghost=True) for k in (1, 2, 3, 4)])
        b.step(st.add_to("main", ghosts), t=1.0, hold=2)
        b.step(st.add_to("main", Cross(ghosts, color=RED, stroke_width=6))
               + st.show("note", note("round two never happens", colour=RED)), t=1.0, hold=3)
        b.step(st.show("note", note("changes in the monetary base stop reaching the money people transact with",
                                    size=22)), t=0.8, hold=3)

        top_ax, top = axes_panel([2008, 2016, 2], [0, 5.5, 1], y_label="index, 2008 = 1",
                                 width=8.2, height=2.1, coords=True)
        bot_ax, bot = axes_panel([2008, 2016, 2], [0, 2.5, 1], y_label="multiplier",
                                 width=8.2, height=1.7, coords=True)
        combo = VGroup(top, bot).arrange(DOWN, buff=0.45)
        combo = VGroup(combo, Text("illustrative: magnitudes as stated in the chapter",
                                   font_size=18, color=GREY)).arrange(DOWN, buff=0.3)
        Stage.fit(combo, "main")

        b.step([*st.clear("main"), FadeIn(combo[0][0]), FadeIn(combo[1])], t=1.2, hold=1)
        st.add_to("main", VGroup(combo[0][0], combo[1]))

        base_line = series(top_ax, self.BASE, colour=RED, width=5)
        base_lab = Text("monetary base", font_size=19, color=RED) \
            .next_to(top_ax.c2p(2015, 4.8), UP, buff=0.1)
        b.step(st.add_to("main", VGroup(base_line, base_lab)), t=1.2, hold=3)

        m1_line = series(top_ax, self.M1, colour=BLUE, width=5)
        m1_lab = Text("money people transact with", font_size=19, color=BLUE) \
            .next_to(top_ax.c2p(2012.2, 1.6), DOWN, buff=0.12)
        b.step(st.add_to("main", VGroup(m1_line, m1_lab)), t=1.2, hold=3)

        brace = BraceBetweenPoints(top_ax.c2p(2015.4, 1.85), top_ax.c2p(2015.4, 4.8),
                                   direction=RIGHT, color=YELLOW)
        brace_lab = Text("reserves\nsitting idle", font_size=17, color=YELLOW,
                         line_spacing=0.8).next_to(brace, RIGHT, buff=0.08)
        b.step(st.add_to("main", VGroup(brace, brace_lab)), t=1.0, hold=3)
        b.step(st.show("note", note("the base rose almost fivefold; the transactions measure rose far less",
                                    size=22)), t=0.8, hold=3)

        one = DashedLine(bot_ax.c2p(2008, 1), bot_ax.c2p(2016, 1), color=GREY, stroke_width=3)
        b.step(st.add_to("main", VGroup(combo[0][1], one)), t=1.0, hold=2)

        mult_pts = [(y, 2.0 * m / bs) for (y, bs), (_, m) in zip(self.BASE, self.M1)]
        mult_line = series(bot_ax, mult_pts, colour=YELLOW, width=5)
        b.step(st.add_to("main", mult_line), t=1.2, hold=3)

        below = Text("below one", font_size=21, color=RED) \
            .next_to(bot_ax.c2p(2015, mult_pts[-1][1]), RIGHT, buff=0.12)
        b.step(st.add_to("main", below) + [Indicate(below, color=RED)], t=1.0, hold=3)
        b.step(st.show("note", note("less transactional money than the base that supposedly supports it",
                                    size=22)), t=0.8, hold=3)

        verdict = VGroup(Text("the accounting is untouched", font_size=27, color=GREEN),
                         Text("the behavioural assumption is refuted", font_size=27, color=RED),
                         Text("and with it, reliable control of the money stock through the base",
                              font_size=22, color=RED),
                         Text("which is one reason central banks now talk about an interest rate",
                              font_size=22, color=GREY)).arrange(DOWN, buff=0.4)
        b.step([*st.clear("main"), *st.show("main", verdict)], t=1.2, hold=4)
        b.step(st.show("note", note("when a model says the bank chooses the money supply: a modelling convenience",
                                    size=22)), t=0.8, hold=3)
        b.run()


class BeatNine(Scene):
    """Three doors out of the equilibrium condition, and the two the chapter shuts."""

    def construct(self):
        st, b = Stage(self), Beat(self, "BeatNine")

        b.step(st.show("title", title("What adjusts")), t=0.6, hold=1)
        b.step(st.show("note", note("the money created is exactly the money people are willing to hold, voluntarily",
                                    size=22)), t=0.8, hold=2)

        board = VGroup()
        eqn = MathTex(r"M^{S}", "=", r"m^{D}(Y, i)", r"\cdot", "p", font_size=50).move_to(UP * 2.0)
        eqn[2].set_color(BLUE)
        board.add(eqn)
        doors = []
        for x, head_text, why in [(-4.5, "p rises", "the same real transactions\nneed more money"),
                                  (0.0, "i falls", "money is cheaper to hold,\nso people hold more of it"),
                                  (4.5, "Y rises", "there are more\ntransactions to carry out")]:
            head = Text(head_text, font_size=30, color=YELLOW).move_to([x, 0.2, 0])
            why_t = note(why, size=19).move_to([x, -1.15, 0])
            arrow = Arrow(eqn.get_bottom() + DOWN * 0.08, head.get_top() + UP * 0.12,
                          color=YELLOW, buff=0.1, stroke_width=4)
            door = VGroup(arrow, head, why_t)
            doors.append(door)
            board.add(door)
        Stage.fit(board, "main")

        b.step(st.add_to("main", eqn), t=1.0, hold=2)
        b.step(st.show("note", note("real money demand: the purchasing power people want to hold", size=22))
               + [Indicate(eqn[2], color=BLUE)], t=0.9, hold=2)
        b.step(st.show("note", note("times the price level, which puts it back into money", size=22))
               + [Indicate(eqn[4], color=YELLOW)], t=0.9, hold=2)

        bump = MathTex(r"\uparrow", font_size=46, color=YELLOW).next_to(eqn[0], UP, buff=0.1)
        b.step(st.add_to("main", bump)
               + [eqn[0].animate.set_color(YELLOW)], t=0.9, hold=2)
        b.step(st.show("note", note("the left side goes up: what on the right moves to restore the equality?",
                                    size=22)), t=0.8, hold=2)

        for door in doors:
            b.step(st.add_to("main", door), t=1.0, hold=3)

        b.step(st.show("note", note("exactly three candidates, and only three")), t=0.8, hold=2)
        b.step(st.show("note", note("which one moves is answered here by assumption, not by argument")),
               t=0.8, hold=3)
        b.step(st.show("note", note("the classical view: real quantities are settled by real forces\nby technology, preferences and endowments",
                                    size=21, colour=GREY)), t=0.9, hold=3)

        b.step([doors[2].animate.set_color(GREY).set_opacity(0.3)], t=0.9, hold=3)
        b.step([doors[1].animate.set_color(GREY).set_opacity(0.3)], t=0.9, hold=3)

        keep = SurroundingRectangle(doors[0], color=YELLOW, buff=0.2)
        b.step(st.add_to("main", keep) + [Indicate(doors[0][1], color=YELLOW)], t=1.0, hold=3)
        b.step(st.show("note", note("not an extra assumption: it is what remains when the other two doors shut",
                                    size=22, colour=YELLOW)), t=0.9, hold=3)
        b.step(st.show("note", note("money is neutral: it moves nominal things, and the only nominal thing left is p",
                                    size=22, colour=YELLOW)), t=0.9, hold=3)

        honest = VGroup(Text("we did not prove that money is neutral", font_size=30, color=RED),
                        Text("we assumed real variables are set by real forces", font_size=25, color=GREY),
                        Text("and neutrality followed", font_size=25, color=GREY)).arrange(DOWN, buff=0.45)
        b.step([*st.clear("main"), *st.show("main", honest)], t=1.2, hold=3)
        b.step(st.show("note", note("in the last beat we take the assumption away and watch what breaks",
                                    colour=RED, size=22)), t=0.8, hold=3)
        b.run()


class BeatTen(Scene):
    """Differentiate, divide through, kill the middle term, and read the law."""

    def construct(self):
        st, b = Stage(self), Beat(self, "BeatTen")

        b.step(st.show("title", title("The law")), t=0.6, hold=1)
        b.step(st.show("note", eq(r"\dot Y / Y = g,\qquad \dot M^{S}/M^{S} = \mu,\qquad r\ \text{constant}",
                                  size=30, colour=GREY)), t=0.9, hold=2)

        board = VGroup()
        l1 = MathTex(r"M^{S} = m^{D}(Y,i)\,p", font_size=40).move_to(UP * 2.1)
        l2 = MathTex(r"\dot M^{S}", "=", r"m^{D}_{Y}\dot Y\,p", "+",
                     r"m^{D}_{i}\,\dot{\imath}\,p", "+", r"m^{D}\dot p", font_size=38).move_to(UP * 1.0)
        l3 = MathTex(r"\mu", "=", r"\frac{m^{D}_{Y}Y}{m^{D}}", "g", "+",
                     r"\frac{m^{D}_{i}}{m^{D}}\dot{\imath}", "+", r"\pi",
                     font_size=38).move_to(DOWN * 0.15)
        law = MathTex(r"\pi = \mu - \eta g", font_size=60, color=GREEN).move_to(DOWN * 1.75)
        board.add(l1, l2, l3, law)
        Stage.fit(board, "main")

        b.step(st.add_to("main", l1), t=1.0, hold=2)
        b.step(st.show("note", note("differentiate both sides with respect to time")), t=0.8, hold=2)
        st.add_to("main", l2)                     # registered here; the transform below reveals it
        b.step([ReplacementTransform(l1.copy(), l2)], t=1.6, hold=2)
        b.step([Indicate(l2[2], color=YELLOW)], t=0.7, hold=2)
        b.step([Indicate(l2[4], color=YELLOW)], t=0.7, hold=2)
        b.step([Indicate(l2[6], color=YELLOW)], t=0.7, hold=2)

        b.step(st.show("note", note("now divide every term by the condition itself:\nlevels disappear and growth rates appear",
                                    size=22, colour=YELLOW)), t=0.9, hold=3)
        st.add_to("main", l3)
        b.step([ReplacementTransform(l2.copy(), l3)], t=1.8, hold=3)

        b.step(st.show("note", note("on the left, the growth rate of the money supply", size=22))
               + [Indicate(l3[0], color=YELLOW)], t=0.8, hold=2)
        b.step(st.show("note", eq(r"\eta \equiv \frac{m^{D}_{Y}Y}{m^{D}}: \ \text{the income elasticity of money demand}",
                                  size=28, colour=YELLOW))
               + [Indicate(l3[2], color=YELLOW)], t=0.9, hold=3)
        b.step(st.show("note", note("the second term carries the change in the nominal interest rate", size=22))
               + [Indicate(l3[5], color=YELLOW)], t=0.8, hold=2)
        b.step(st.show("note", note("the third is the growth rate of the price level: inflation", size=22))
               + [Indicate(l3[7], color=YELLOW)], t=0.8, hold=2)

        b.step(st.show("note", eq(r"\pi\ \text{constant}\;\Rightarrow\; i = r + \pi\ \text{constant}\;\Rightarrow\;\dot{\imath} = 0",
                                  size=28, colour=GREY)), t=0.9, hold=3)
        b.step([l3[4].animate.set_opacity(0.2), l3[5].animate.set_color(GREY).set_opacity(0.2)],
               t=0.9, hold=2)

        clean = MathTex(r"\mu", "=", r"\eta", "g", "+", r"\pi", font_size=40).move_to(l3)
        b.step([Transform(l3, clean)], t=1.5, hold=3)
        b.step(st.show("note", note("what remains is clean", size=22)), t=0.7, hold=2)
        st.add_to("main", law)
        b.step([ReplacementTransform(l3.copy(), law)], t=1.6, hold=3)
        frame = SurroundingRectangle(law, color=GREEN, buff=0.22)
        b.step(st.add_to("main", frame), t=0.9, hold=3)
        b.step(st.show("note", note("inflation is money growth, minus the income elasticity times output growth",
                                    size=22, colour=GREEN)), t=0.9, hold=3)
        b.step(st.show("note", note("we assumed inflation constant to drop a term, and the formula returns a constant",
                                    size=22)), t=0.9, hold=3)

        big = VGroup(MathTex(r"\pi = \mu - \eta g", font_size=60, color=GREEN))
        big.add(SurroundingRectangle(big[0], color=GREEN, buff=0.25))
        b.step([*st.clear("main"), *st.show("left", big)], t=1.2, hold=2)

        first = VGroup(Text("why growth lowers inflation", font_size=23, color=YELLOW),
                       note("more transactions, so more real money\nwanted, so new money is absorbed\ninstead of bidding prices up", size=19)) \
            .arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        second = VGroup(Text("why eta is in there at all", font_size=23, color=YELLOW),
                        note("eta is the exchange rate between growth\nand absorbable money: the larger it is,\nthe more money growth the economy\ncan soak up for free", size=19)) \
            .arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        pair = VGroup(first, second).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        Stage.fit(pair, "right")
        b.step(st.add_to("right", first), t=1.0, hold=4)
        b.step(st.add_to("right", second), t=1.0, hold=4)
        b.run()
