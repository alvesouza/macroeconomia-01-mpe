from manim import *
from manim_kit import Beat, Stage, mpl_figure, read_csv, title

class MplTest(Scene):
    def construct(self):
        rows = read_csv("data/wdi_money_vs_inflation_country_averages.csv")
        pts = [(float(r["money_growth_avg"]), float(r["inflation_avg"])) for r in rows]
        keep = [p for p in pts if p[0] < 100 and p[1] < 100]

        def draw(fig, ax):
            ax.scatter([p[0] for p in keep], [p[1] for p in keep], s=16,
                       c="#58C4DD", alpha=.85, edgecolors="none")
            ax.plot([0, 100], [0, 100], color="#83C167", lw=2, ls="--")
            ax.set_xlabel("average broad money growth, per cent")
            ax.set_ylabel("average inflation, per cent")
            ax.set_xlim(0, 100); ax.set_ylim(0, 100)
            ax.grid(alpha=.15, color="#e8ebef")

        fig = mpl_figure(draw, "scatter_clean", width=9.0)
        st, b = Stage(self), Beat(self, "BeatOne")
        b.step(st.show("title", title("148 countries, three decades")), t=0.6, hold=1)
        b.step(st.show("main", fig, fit=False), t=1.0, hold=4)
        b.run()
