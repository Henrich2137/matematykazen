from manim import * 


class ScenaZadania2(Scene):
        
    def construct(self):
        
        GREEN = "#008628"
        #WARTOBY TU ZROBIĆ ARRAY Z NICH
        wzory = [MathTex()] * 6
        #wzory[0] = Text("Przydadzą się wzory na\npotęgi i pierwiastki")
        wzory[0] = MathTex("")
        wzory[1] = MathTex(r"a^{\frac{m}{n}}=\sqrt[n]{a^m}")
        wzory[2] = MathTex(r"\frac{a^r}{a^s}=a^{r-s}")
        
        #STEP 4
        wzory[3] = MathTex(r"(a\cdot b)^r=a^r\cdot b^r")
        wzory[4] = MathTex(r"(a^r)^s=a^{r \cdot s}")

        #STEP 5 jest bez wzoru bo każdy umie mnożyć

        #STEP 6
        wzory[5] = MathTex(r"a^r\cdot a^s=a^{r+s}")



        for wzor in wzory:
            wzor.fill_color=BLACK
            wzor.font_size=120
            wzor.shift(RIGHT*4.5)
        wzory[0].font_size=50

        kroki = [None] * 6

        # ", r"
        kroki[0] = MathTex(r"\left(", r"\sqrt[5]{5}", r"\cdot\frac{1}{5}", r"\right)^{-5}")
        #kroki[0] = VGroup(MathTex(r"\left("), MathTex(r"\sqrt[5]{5}"), MathTex(r"\cdot\frac{1}{5}\right)^{-5}"))


        kroki[1] = MathTex(r"\left(", r"5^{\frac{1}{5}}", r"\cdot \frac{1}{5}", r"\right)^{-5}")

        kroki[2] = MathTex(r"\left(", r"5^\frac{1}{5} ", r"\cdot 5^{-1}", r"\right)^{-5}")
        kroki[3] = MathTex(r" 5^{\frac{1}{5} \cdot -5}\cdot 5^{-1 \cdot -5}")
        kroki[4] = MathTex(r" 5^{-1} \cdot 5^5 ")
        kroki[5] = MathTex(r" 5^{4}")

        for krok in kroki:
            krok.fill_color=BLACK
            krok.font_size=120
            krok.shift(LEFT*4.5)
        
        

        """
        #STEP 1
        self.play(Create(kroki[0]), Create(wzory[0]))
        self.remove(wzory[0])

        
        #STEP 2
        
        wzory[1][0][3].set_color(GREEN)
        wzory[1][0][5].set_color(GREEN)

        self.add(wzory[1])
        
        kroki[0][1][0].set_color(GREEN)
        kroki[1][1][3].set_color(GREEN)

        self.play( Transform(kroki[0][0], kroki[1][0]), TransformMatchingShapes(kroki[0][1], kroki[1][1]), Transform(kroki[0][2:3], kroki[1][2:3]))
        
        kroki[0][1][0].set_color(BLACK)
        kroki[1][1][3].set_color(BLACK)
        
        self.remove(kroki[0][0], kroki[1][1], kroki[0][2], kroki[0][3]) #mozna zamiast tego self.clear()
        self.remove(wzory[1])
        


        #STEP 3

        self.add(wzory[2])
        wzory[2][0][3].set_color(GREEN)
        wzory[2][0][6].set_color(GREEN)
        
        self.add(kroki[1])
        kroki[1][2][3].set_color(GREEN)
        kroki[2][2][1].set_color(GREEN)
        

        self.play( Transform(kroki[1][0], kroki[2][0]), Transform(kroki[1][1], kroki[2][1]), Transform(kroki[1][2][0], kroki[2][2][0]), Transform(kroki[1][2][1:3], kroki[2][2][1:4]), Transform(kroki[1][2][3], kroki[2][2][1]), Transform(kroki[1][3], kroki[2][3]) )
        
        kroki[1][2][1].set_color(BLACK)
        kroki[2][2][1].set_color(BLACK)

        self.clear()
        

        #STEP 4
        self.add(wzory[3].shift(UP))
        self.add(wzory[4].shift(DOWN))
        wzory[3][0][5].set_color(GREEN)
        wzory[3][0][8].set_color(GREEN)
        wzory[3][0][11].set_color(GREEN)

        
        self.add(kroki[2])
        kroki[2][3][1:3].set_color(GREEN)
        kroki[3][0][5:7].set_color(GREEN)
        kroki[3][0][12:14].set_color(GREEN)

        self.play(FadeOut(kroki[2][0][0], kroki[2][3][0]), Transform(kroki[2][1], kroki[3][0][0:5]), Transform(kroki[2][3][1:3], kroki[3][0][5:7]), Transform(kroki[2][2][0:4], kroki[3][0][7:12]), Transform(kroki[2][3][1:3].copy(), kroki[3][0][12:14]))

        kroki[3][0][5:7].set_color(BLACK)
        kroki[3][0][12:14].set_color(BLACK)

        self.clear()
        self.add(kroki[3])
        self.wait(1)


        #STEP 5
        self.play(ReplacementTransform(kroki[3], kroki[4]))        
        self.add(kroki[4])

        """
        self.clear()
        #STEP 6

        self.add(wzory[5])
        self.add(kroki[4])
        self.wait(1)
        self.play(ReplacementTransform(kroki[4], kroki[5]))
        #self.play(Transform(kroki[5], kroki[5].copy().move_to(ORIGIN)), FadeOut(wzory[5]))


"""
if __name__=="__main__":
    with tempconfig({"preview": True, "output_file": "mojanazwa.mp4"}):
        Zad2().render()

"""