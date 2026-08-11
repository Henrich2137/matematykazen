from manim import * 

class Scena1(Scene):
        
    def construct(self):
        #mozna tu zrobić template z MathTex i potem tylko zmieniać tekst
        w = MathTex(r" \sqrt[5]{5}", font_size=130)
        w.fill_color=BLACK
        
        w2 = MathTex(r" 5^\frac{1}{5}", font_size=130)
        w2.fill_color=BLACK
        w2[0][3].set_color(GREEN)

        
        self.play(Create(w))
        self.wait(1)
        
        w[0][0].set_color(GREEN)


        #text[0][1:3].set_color(YELLOW)
        self.wait(1)

        



        self.play(TransformMatchingShapes(w, w2))
        #https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingTex.html
