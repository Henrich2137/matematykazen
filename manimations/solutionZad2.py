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



        # Wzory pomocnicze NIE są już rysowane w filmie (zmiana 2026-08-11).
        # Pokazuje je strona, jako KaTeX pod filmem — patrz pole "text" przy
        # kroku w exercises.json. Definicje zostają tutaj jako źródło wiedzy,
        # który wzór należy do którego kroku; scena ich nie dodaje.
        for wzor in wzory:
            wzor.fill_color=BLACK
            wzor.font_size=120

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

        # Kadr jest teraz 16:9 i film pokazuje samo działanie, więc treść stoi
        # na środku, a nie zepchnięta w lewo (prawa strona trzymała miejsce na
        # wzór pomocniczy, który wyszedł z filmu).
        #
        # Skala jest WSPÓLNA dla wszystkich kroków i liczona z najszerszego —
        # gdyby każdy krok dopasowywał się osobno, litery zmieniałyby rozmiar
        # w trakcie przekształcenia, a Transform robiłby z tego zoom.
        MARGINES = 0.85
        najszerszy = max(krok.width for krok in kroki)
        if najszerszy > config.frame_width * MARGINES:
            wspolczynnik = config.frame_width * MARGINES / najszerszy
            for krok in kroki:
                krok.scale(wspolczynnik)
        for krok in kroki:
            krok.move_to(ORIGIN)
        
        

        """
        #STEP 1
        self.play(Create(kroki[0]))

        
        #STEP 2
        

        
        kroki[0][1][0].set_color(GREEN)
        kroki[1][1][3].set_color(GREEN)

        self.play( Transform(kroki[0][0], kroki[1][0]), TransformMatchingShapes(kroki[0][1], kroki[1][1]), Transform(kroki[0][2:3], kroki[1][2:3]))
        
        kroki[0][1][0].set_color(BLACK)
        kroki[1][1][3].set_color(BLACK)
        
        self.remove(kroki[0][0], kroki[1][1], kroki[0][2], kroki[0][3]) #mozna zamiast tego self.clear()
        


        #STEP 3

        
        self.add(kroki[1])
        kroki[1][2][3].set_color(GREEN)
        kroki[2][2][1].set_color(GREEN)
        

        self.play( Transform(kroki[1][0], kroki[2][0]), Transform(kroki[1][1], kroki[2][1]), Transform(kroki[1][2][0], kroki[2][2][0]), Transform(kroki[1][2][1:3], kroki[2][2][1:4]), Transform(kroki[1][2][3], kroki[2][2][1]), Transform(kroki[1][3], kroki[2][3]) )
        
        kroki[1][2][1].set_color(BLACK)
        kroki[2][2][1].set_color(BLACK)

        self.clear()
        

        #STEP 4

        
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

        self.add(kroki[4])
        self.wait(1)
        self.play(ReplacementTransform(kroki[4], kroki[5]))


"""
if __name__=="__main__":
    with tempconfig({"preview": True, "output_file": "mojanazwa.mp4"}):
        Zad2().render()

"""
