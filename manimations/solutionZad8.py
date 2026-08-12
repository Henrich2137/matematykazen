from manim import *


# Zadanie 8 (otwarte, 3 pkt) — rozwiąż (x+3)/(x-1) = x/(2x-2). Wynik x = -6.
#
# Scenariusz kroków jest w manimations/zad8-kroki.md — zatwierdzony przed
# napisaniem tego pliku; jest tam też tabelka „kryterium z klucza CKE → krok".
#
# Render: manim --save_sections solutionZad8.py Zad8
class Zad8(Scene):

    def construct(self):
        GREEN = "#0AB32F"
        GRAY = "#A6A6A6"

        kroki = [None] * 6
        kroki[0] = MathTex(r"\frac{x+3}{x-1}", r"=", r"\frac{x}{2x-2}")
        kroki[1] = MathTex(r"\frac{x+3}{x-1}", r"=", r"\frac{x}{2(x-1)}")
        kroki[2] = MathTex(r"2(x+3)",          r"=", r"x")
        kroki[3] = MathTex(r"2x+6",            r"=", r"x")
        kroki[4] = MathTex(r"2x-x",            r"=", r"-6")
        kroki[5] = MathTex(r"x",               r"=", r"-6")

        for krok in kroki:
            krok.fill_color = BLACK
            krok.font_size = 110

        MARGINES = 0.85
        najszerszy = max(krok.width for krok in kroki)
        if najszerszy > config.frame_width * MARGINES:
            wspolczynnik = config.frame_width * MARGINES / najszerszy
            for krok in kroki:
                krok.scale(wspolczynnik)

        # Równanie stoi lekko nad środkiem, bo od kroku 3 pod nim siedzi założenie.
        # Miejsce rezerwujemy OD RAZU — inaczej cały zapis podskoczyłby w chwili,
        # gdy założenie się pojawia.
        for krok in kroki:
            krok.move_to(UP * 0.55)

        # Założenie (dziedzina) — za jego zapisanie klucz CKE daje osobny punkt,
        # dlatego dostaje własny krok i zostaje na ekranie do końca.
        zalozenie = MathTex(r"x \ne 1")
        zalozenie.fill_color = GRAY
        zalozenie.font_size = 70
        zalozenie.move_to(DOWN * 2.2)

        # Przytrzymanie 0,25 s na końcu KAŻDEJ sekcji i zawsze przed sprzątaniem sceny.

        self.next_section("krok1")
        # KROK 1 — równanie z zadania.
        self.play(Create(kroki[0]))
        self.wait(0.25)

        self.next_section("krok2")
        # KROK 2 — 2x-2 = 2(x-1). Dopiero teraz widać, że w obu mianownikach
        # siedzi ten sam nawias.
        kroki[0][2].set_color(GREEN)
        kroki[1][2].set_color(GREEN)
        self.play(TransformMatchingShapes(kroki[0], kroki[1]), run_time=1.4)
        self.wait(0.25)
        kroki[1][2].set_color(BLACK)

        self.next_section("krok3")
        # KROK 3 — założenie wjeżdża pod równanie i już tam zostaje.
        self.play(FadeIn(zalozenie, shift=UP * 0.4), run_time=1.0)
        self.wait(0.25)

        self.next_section("krok4")
        # KROK 4 — mnożymy obie strony przez 2(x-1); mianowniki się skracają.
        self.play(TransformMatchingShapes(kroki[1], kroki[2]), run_time=1.4)
        self.wait(0.25)

        self.next_section("krok5")
        # KROK 5 — opuszczamy nawias.
        self.play(TransformMatchingShapes(kroki[2], kroki[3]), run_time=1.4)
        self.wait(0.25)

        self.next_section("krok6")
        # KROK 6 — iksy na lewo, liczby na prawo.
        self.play(TransformMatchingShapes(kroki[3], kroki[4]), run_time=1.4)
        self.wait(0.25)

        self.next_section("krok7")
        # KROK 7 — wynik. Założenie wciąż stoi pod spodem, więc widać od razu,
        # że -6 nie jest jedynką i mieści się w dziedzinie.
        kroki[5][2].set_color(GREEN)
        self.play(TransformMatchingShapes(kroki[4], kroki[5]), run_time=1.4)
        self.wait(0.25)
