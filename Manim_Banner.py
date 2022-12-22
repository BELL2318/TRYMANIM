from manim import *

class Example(ZoomedScene):
    def construct(self):
        self.camera.background_color =  "#ece6e2"  #HEREFROM "#07f107"
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        circle = Circle(radius=1,color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(side_length=2,color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(radius=1,color=logo_red, fill_opacity=1).shift(RIGHT)
        logo = VGroup(triangle, square, circle).scale(1.3)  # .scale(2.0) #HERETO
        logo.move_to(ORIGIN)
        self.play(DrawBorderThenFill(logo))
        self.camera.frame.scale(1 / 1.5)
        self.wait()