from manim import *


class TestSekcje(Scene):
    def construct(self):
        a = MathTex(r"1+1").set_color(BLACK)
        b = MathTex(r"2").set_color(BLACK)

        self.next_section("krok1")
        self.play(Create(a))
        self.wait(0.25)

        self.next_section("krok2")
        self.play(Transform(a, b))
        self.wait(0.25)
