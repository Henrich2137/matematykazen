from manim import *


# Zadanie 7 — para x = -1, y = 6 spełnia układ; szukamy a·b. Wynik -2, odpowiedź A.
#
# Scenariusz kroków jest w manimations/zad7-kroki.md.
#
# Render: manim --save_sections solutionZad7.py Zad7
class Zad7(Scene):

    def construct(self):
        GREEN = "#0AB32F"

        # Oba równania jadą RÓWNOLEGLE, jedno pod drugim — w tym zadaniu nie ma
        # układu do rozwiązywania, są dwa niezależne równania z jedną niewiadomą
        # każde, i to ma być widać.
        kroki = [None] * 7
        kroki[0] = MathTex(r"\begin{cases} ax + 3y = 20 \\ x + by = 5 \end{cases}")
        kroki[1] = MathTex(r"\begin{cases} a \cdot (-1) + 3 \cdot 6 = 20 \\ (-1) + b \cdot 6 = 5 \end{cases}")
        kroki[2] = MathTex(r"\begin{cases} -a + 18 = 20 \\ -1 + 6b = 5 \end{cases}")
        kroki[3] = MathTex(r"\begin{cases} -a = 2 \\ 6b = 6 \end{cases}")
        kroki[4] = MathTex(r"\begin{cases} a = -2 \\ b = 1 \end{cases}")
        kroki[5] = MathTex(r"a \cdot b = (-2) \cdot 1")
        kroki[6] = MathTex(r"a \cdot b = -2")

        for krok in kroki:
            krok.fill_color = BLACK
            krok.font_size = 90

        MARGINES = 0.85
        najszerszy = max(k.width for k in kroki)
        if najszerszy > config.frame_width * MARGINES:
            wspolczynnik = config.frame_width * MARGINES / najszerszy
            for k in kroki:
                k.scale(wspolczynnik)
        for k in kroki:
            k.move_to(ORIGIN)

        def przejdz(skad, dokad, zielony_cel=False):
            if zielony_cel:
                kroki[dokad].set_color(GREEN)
            self.play(TransformMatchingShapes(kroki[skad], kroki[dokad]), run_time=1.4)
            self.wait(0.25)
            self.clear()
            if zielony_cel:
                kroki[dokad].set_color(BLACK)
            self.add(kroki[dokad])

        self.next_section("krok1")
        # KROK 1 — układ z zadania.
        self.play(Create(kroki[0]))
        self.wait(0.25)

        self.next_section("krok2")
        # KROK 2 — podstawiamy x = -1 i y = 6.
        przejdz(0, 1)

        self.next_section("krok3")
        # KROK 3 — liczymy iloczyny liczbowe.
        przejdz(1, 2)

        self.next_section("krok4")
        # KROK 4 — liczby na prawą stronę.
        przejdz(2, 3)

        self.next_section("krok5")
        # KROK 5 — wyliczone a i b. Na zielono, bo to pierwszy realny wynik.
        przejdz(3, 4, zielony_cel=True)

        self.next_section("krok6")
        # KROK 6 — wstawiamy do tego, o co pyta zadanie: iloczynu a·b.
        przejdz(4, 5)

        self.next_section("krok7")
        # KROK 7 — wynik.
        kroki[6].set_color(GREEN)
        self.play(TransformMatchingShapes(kroki[5], kroki[6]), run_time=1.4)
        self.wait(0.25)
