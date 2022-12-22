from manim import *

class PlotGraph(Scene): #Đồ thị hàm số 
    def construct(self):
        ax=Axes(x_range=(-2.5,2.5),y_range=(-5,5),)
        curve=ax.plot(lambda x: x*(x-2)*(x+2)/2,color=RED)
        area=ax.get_area(curve,x_range=(-1,1))
        self.play(Create(ax,runtime=2),Create(curve,runtime=2))
        self.play(FadeIn(area))
        self.wait(3)
        