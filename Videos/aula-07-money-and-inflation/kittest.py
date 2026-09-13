from manim import *
from manim_kit import Beat, Stage, balance_sheet, note, title, load_beats

class KitTest(Scene):
    def construct(self):
        st = Stage(self)
        b = Beat(self, "BeatOne")
        sheet = balance_sheet(
            [("reserves", YELLOW), ("bonds", None), ("loans", None)],
            [("deposits", None), ("other borrowing", None), ("net worth", GREY)])
        b.step(st.show("title", title("Where money comes from")), t=0.6, hold=1)
        b.step(st.show("main", sheet), t=1.0, hold=3)
        b.step(st.show("note", note("the reserves did not leave")), t=0.8, hold=3)
        b.step(st.show("note", note("and nobody's net worth changed")), t=0.8, hold=3)
        b.run()
