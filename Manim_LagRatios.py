from manim import *
import numpy as np

class LagRatios(Scene):
    def construct(self):
        ratios = np.arange(0,3,0.5)  # demonstrated lag_ratios

        # Create dot groups
        group = VGroup(*[Dot() for _ in range(5)]).arrange_submobjects()
        groups = VGroup(*[group.copy() for _ in ratios]).arrange_submobjects(buff=0.5)
        self.add(groups)
        #self.wait()

        # Label groups
        self.add(Text("Lag_Ratios = ", font_size=25).next_to(groups, UP, buff=1))
        for group, ratio in zip(groups, ratios):
            self.add(Text(str(ratio), font_size=25).next_to(group, UP))
        #self.wait()

        #Animate groups with different lag_ratios
        self.play(AnimationGroup(*[
            group.animate(lag_ratio=ratio, run_time=1.5).shift(DOWN * 2)
            for group, ratio in zip(groups, ratios)
        ]))
        #self.wait()

        # lag_ratio also works recursively on nested submobjects:
        self.play(groups.animate(run_time=1, lag_ratio=0.1).shift(UP * 2))
        self.wait()

        
