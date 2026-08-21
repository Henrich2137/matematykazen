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
        
        

        # KROKI JAKO SEKCJE (przebudowa 2026-08-12). Wcześniej kroki przełączało
        # się komentarzem `"""` i renderowało po jednym — stąd w repo leżała wersja
        # z zakomentowaną większością treści, która NIE odtwarzała wgranych plików
        # (nie miała m.in. przytrzymań `self.wait(0.25)`). Teraz scena jedzie w całości,
        # a `self.next_section` wyznacza granice kroków: `manim --save_sections`
        # zapisuje każdy krok osobnym plikiem. Efekt uboczny, który jest tu ZALETĄ:
        # kroki nie muszą być samowystarczalne, bo stan wejściowy przynosi
        # poprzednia sekcja — to był problem opisany w README (krok 2 renderowany
        # w izolacji gubił domykający nawias).
        #
        # KAŻDA sekcja kończy się `self.wait(0.25)` — bez tego przeglądarka
        # zatrzymuje obraz kilka klatek przed końcem pliku i ostatni element
        # animacji nie zostaje na ekranie (patrz README, punkt 0 workflow).

        self.next_section("krok1")
        #STEP 1
        self.play(Create(kroki[0]))
        self.wait(0.25)


        self.next_section("krok2")
        #STEP 2



        kroki[0][1][0].set_color(GREEN)
        kroki[1][1][3].set_color(GREEN)

        self.play( Transform(kroki[0][0], kroki[1][0]), TransformMatchingShapes(kroki[0][1], kroki[1][1]), Transform(kroki[0][2:3], kroki[1][2:3]))
        
        kroki[0][1][0].set_color(BLACK)
        kroki[1][1][3].set_color(BLACK)
        
        # Przytrzymanie MUSI iść przed sprzątaniem sceny — po `self.remove` kadr
        # jest pusty, więc 0,25 s trzymałoby białą planszę i to ona zostawałaby
        # uczniowi na ekranie (złapane porównaniem SSIM z wgranym plikiem).
        self.wait(0.25)
        self.remove(kroki[0][0], kroki[1][1], kroki[0][2], kroki[0][3]) #mozna zamiast tego self.clear()


        self.next_section("krok3")
        #STEP 3


        self.add(kroki[1])
        kroki[1][2][3].set_color(GREEN)
        kroki[2][2][1].set_color(GREEN)
        

        self.play( Transform(kroki[1][0], kroki[2][0]), Transform(kroki[1][1], kroki[2][1]), Transform(kroki[1][2][0], kroki[2][2][0]), Transform(kroki[1][2][1:3], kroki[2][2][1:4]), Transform(kroki[1][2][3], kroki[2][2][1]), Transform(kroki[1][3], kroki[2][3]) )
        
        kroki[1][2][1].set_color(BLACK)
        kroki[2][2][1].set_color(BLACK)

        self.wait(0.25)
        self.clear()


        self.next_section("krok4")
        #STEP 4
        #
        # DO PRZEROBIENIA: TEN KROK TRZEBA ROZBIC NA DWA I PRZERENDEROWAC.
        #
        # Powod: rozwiazanie opisowe tego samego zadania (pole "solutionText"
        # w matura/2024-grudzien/exercises.json) od 2026-08-21 idzie linijka po
        # linijce, JEDEN wzor na JEDNA linijke, i ta linijka jest tam rozbita
        # na dwie:
        #
        #     (5^{1/5} * 5^{-1})^{-5}            <-  (a*b)^r = a^r * b^r
        #     (5^{1/5})^{-5} * (5^{-1})^{-5}     <-  (a^r)^s = a^{r*s}
        #
        # Film robi oba te przeksztalcenia naraz, w jednym kroku, wiec opis pod
        # filmem i rozwiazanie opisowe pokazuja teraz rozna liczbe krokow.
        # Zeby sie zgadzalo:
        #
        #   1. rozbij ta sekcje na "krok4a" (samo opuszczenie nawiasu, wynik
        #      (5^{1/5})^{-5} * (5^{-1})^{-5}) i "krok4b" (wymnozenie wykladnikow
        #      z nawiasami, wynik taki jak dzis kroki[3]),
        #   2. dolóż miedzy kroki[2] a kroki[3] nowy MathTex ze stanem posrednim,
        #   3. przerenderuj scene i PODMIEN pliki krokow w
        #      matura/2024-grudzien/media/zad2/solution-step-by-step/ (kroki od
        #      czwartego w gore przesuwaja sie o jeden numer),
        #   4. dopisz nowy krok w tablicy "solutionStepByStep" w exercises.json
        #      i rozdziel jego opis: krok4a dostaje (a*b)^r = a^r * b^r,
        #      krok4b dostaje (a^r)^s = a^{r*s}.
        #
        # Pamietaj o zasadzie z README: ostatnia klatka kroku 4a musi byc
        # pierwsza klatka kroku 4b.


        self.add(kroki[2])
        kroki[2][3][1:3].set_color(GREEN)
        kroki[3][0][5:7].set_color(GREEN)
        kroki[3][0][12:14].set_color(GREEN)

        self.play(FadeOut(kroki[2][0][0], kroki[2][3][0]), Transform(kroki[2][1], kroki[3][0][0:5]), Transform(kroki[2][3][1:3], kroki[3][0][5:7]), Transform(kroki[2][2][0:4], kroki[3][0][7:12]), Transform(kroki[2][3][1:3].copy(), kroki[3][0][12:14]))

        kroki[3][0][5:7].set_color(BLACK)
        kroki[3][0][12:14].set_color(BLACK)

        self.wait(0.25)
        self.clear()
        self.add(kroki[3])


        self.next_section("krok5")
        #STEP 5
        self.play(ReplacementTransform(kroki[3], kroki[4]))
        self.add(kroki[4])
        self.wait(0.25)


        self.next_section("krok6")
        #STEP 6
        #
        # DO PRZEROBIENIA: TEN KROK TEZ TRZEBA ROZBIC NA DWA I PRZERENDEROWAC.
        #
        # Ta sama sprawa co przy kroku 4. Rozwiazanie opisowe (solutionText
        # w matura/2024-grudzien/exercises.json) rozbija to od 2026-08-21 na:
        #
        #     5^{-1} * 5^{5}     <-  a^r * a^s = a^{r+s}
        #     5^{-1+5}           <-  bez wzoru, samo dodawanie w wykladniku
        #     5^{4}
        #
        # Film robi dodanie wykladnikow i ich zsumowanie w jednym ruchu, wiec
        # pokazuje o krok mniej. Rozbij sekcje na "krok6a" (do stanu 5^{-1+5})
        # i "krok6b" (do 5^{4}), dolóż MathTex ze stanem posrednim, przerenderuj,
        # podmien pliki krokow i dopisz nowy krok w "solutionStepByStep".
        #
        # Ostatnia klatka kroku 6a musi byc pierwsza klatka kroku 6b (README).
        # Sekunda bezruchu na wejściu była tu do 2026-08-20 (step6.mp4 miał 2,25 s
        # = 1 s postoju + 1 s animacji + 0,25 s przytrzymania). Wycięta na prośbę
        # Henricha: punkt wyjścia uczeń widzi już na ostatniej klatce kroku 5,
        # a postój na starcie filmu wygląda jak zacięcie odtwarzacza.
        self.clear()
        self.add(kroki[4])
        self.play(ReplacementTransform(kroki[4], kroki[5]))
        self.wait(0.25)


"""
if __name__=="__main__":
    with tempconfig({"preview": True, "output_file": "mojanazwa.mp4"}):
        Zad2().render()

"""
