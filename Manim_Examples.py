from manim import *

class Example1(Scene): #add #play #become  
    def construct(self):
        circle=Circle(radius=3,color=BLUE,fill_opacity=1)
        square=Square(side_length=3,color=RED,fill_opacity=1)
        self.add(circle)
        self.wait()
        self.play(DrawBorderThenFill(square))
        self.wait()
        circle.become(square)
        self.wait()     

class Example2(Scene): #Transfomer
    def construct(self):
        circle=Circle(radius=1,color=BLUE,fill_opacity=1)
        square=Square(side_length=3,color=RED,fill_opacity=1)
        self.add(circle)
        self.wait()
        self.play(Transform(circle,square))
        self.wait()

class Example3(Scene): #RIGHT #LEFT #UP #DOWN #scale #change color
    def construct(self):
        circle=Circle(radius=1,color=BLUE,fill_opacity=1)
        square=Square(side_length=3,color=RED,fill_opacity=1)
        self.play(circle.animate.shift(RIGHT*2))
        self.wait()
        self.play(square.animate.shift(UP*2))
        self.wait()
        self.play(circle.animate.shift(DOWN*2))
        self.wait()
        self.play(square.animate.shift(LEFT*2))
        self.wait()
        self.play(square.animate.shift(DOWN*2).scale(0.5).set_color(GREEN))
        self.wait()

class Example4(Scene): #Updaters
    def construct(self):
        circle=Circle(radius=1,color=BLUE,fill_opacity=1)
        square=Square(side_length=3,color=RED,fill_opacity=1)
        self.add(circle)
        circle.add_updater(lambda x,dt: x.shift(2*RIGHT*dt))
        self.wait(3)
        self.add(square)
        square.add_updater(lambda x,dt: x.shift(2*LEFT*dt))
        self.wait(3)



