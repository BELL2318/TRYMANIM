from manim import *

dORIGIN= Dot(color= BLUE,radius=0.5)
class Example(Scene):
    def construct(self):
        d= Dot(color= YELLOW, radius=0.5)
        d.shift(2*RIGHT)
        self.play(DrawBorderThenFill(dORIGIN))
        self.wait()
        self.play(Transform(dORIGIN,d))
        self.wait()