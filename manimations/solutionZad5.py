from manim import *


# Zadanie 5 — procent składany. 60 000 · (1+p)^2 = 67 925,76 → p = 6,4%, odpowiedź B.
#
# Scenariusz kroków jest w manimations/zad5-kroki.md — zatwierdź go, zanim ruszysz
# ten plik; zmieniasz przebieg tutaj → popraw i tam.
#
# Render: manim --save_sections solutionZad5.py Zad5
class Zad5(Scene):

    def construct(self):
        GREEN = "#0AB32F"

        kroki = [None] * 7
        kroki[0] = MathTex(r"60\,000 \cdot (1+p)^{2}", r"=", r"67\,925{,}76")
        kroki[1] = MathTex(r"(1+p)^{2}",                r"=", r"\frac{67\,925{,}76}{60\,000}")
        kroki[2] = MathTex(r"(1+p)^{2}",                r"=", r"1{,}132096")
        kroki[3] = MathTex(r"1+p",                      r"=", r"1{,}064")
        kroki[4] = MathTex(r"p",                        r"=", r"0{,}064")
        kroki[5] = MathTex(r"p",                        r"=", r"6{,}4\%")

        for krok in kroki:
            if krok:
                krok.fill_color = BLACK
                krok.font_size = 100

        # Skala WSPÓLNA, liczona z najszerszego kroku — inaczej litery zmieniałyby
        # rozmiar w trakcie przekształcenia (wzorzec z zad. 1–4, 6 i 8).
        MARGINES = 0.85
        istniejace = [k for k in kroki if k]
        najszerszy = max(k.width for k in istniejace)
        if najszerszy > config.frame_width * MARGINES:
            wspolczynnik = config.frame_width * MARGINES / najszerszy
            for k in istniejace:
                k.scale(wspolczynnik)
        for k in istniejace:
            k.move_to(ORIGIN)

        # Wspólna obsługa przejścia: kolorowanie „co się zmienia", przejście,
        # przytrzymanie 0,25 s (PRZED sprzątaniem sceny — po `clear` trzymałoby
        # białą planszę) i zdjęcie koloru dopiero po przytrzymaniu.
        def przejdz(skad, dokad, zielone_skad=(), zielone_dokad=()):
            for i in zielone_skad:
                kroki[skad][i].set_color(GREEN)
            for i in zielone_dokad:
                kroki[dokad][i].set_color(GREEN)
            self.play(TransformMatchingShapes(kroki[skad], kroki[dokad]), run_time=1.4)
            self.wait(0.25)
            self.clear()
            for i in zielone_dokad:
                kroki[dokad][i].set_color(BLACK)
            self.add(kroki[dokad])

        self.next_section("krok1")
        # KROK 1 — dane wstawione we wzór na procent składany.
        self.play(Create(kroki[0]))
        self.wait(0.25)

        self.next_section("krok2")
        # KROK 2 — dzielimy obie strony przez 60 000.
        przejdz(0, 1, zielone_skad=(0,), zielone_dokad=(2,))

        self.next_section("krok3")
        # KROK 3 — liczymy ułamek.
        przejdz(1, 2, zielone_dokad=(2,))

        self.next_section("krok4")
        # KROK 4 — pierwiastkujemy; bierzemy wartość dodatnią, bo 1+p > 0.
        przejdz(2, 3, zielone_dokad=(0, 2))

        self.next_section("krok5")
        # KROK 5 — odejmujemy 1 od obu stron.
        przejdz(3, 4, zielone_dokad=(0, 2))

        self.next_section("krok6")
        # KROK 6 — ułamek dziesiętny na procent.
        kroki[5][2].set_color(GREEN)
        self.play(TransformMatchingShapes(kroki[4], kroki[5]), run_time=1.4)
        self.wait(0.25)
