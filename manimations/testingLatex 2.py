from manim import * 

class Scena1(Scene):
        
    def construct(self):
        eq2 = MathTex("\sqrt[{{5}}]{2}")
        eq3 = MathTex("\sqrt[{{2}}]{5}")

        eq2.fill_color=BLACK
        eq2.font_size=110
        
        eq3.fill_color=BLACK
        eq3.font_size=110


        self.add(eq2)
        self.play(TransformMatchingTex(eq2, eq3))

        #https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingTex.html
