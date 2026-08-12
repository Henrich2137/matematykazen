from manim import *


# Zadanie 9 (otwarte, 2 pkt) — rozwiąż x(x-6) <= 7. Wynik: x nalezy do <-1, 7>.
#
# Scenariusz kroków jest w manimations/zad9-kroki.md; jest tam tabelka
# „kryterium z klucza CKE → krok" i uzasadnienie, dlaczego film NIE rysuje paraboli
# (zadanie ma już widżet widgetNierownoscKwadratowa, który robi to interaktywnie).
#
# Render: manim --save_sections solutionZad9.py Zad9
class Zad9(Scene):

    def construct(self):
        GREEN = "#0AB32F"

        kroki = [None] * 8
        kroki[0] = MathTex(r"x(x-6) \le 7")
        kroki[1] = MathTex(r"x^{2}-6x \le 7")
        kroki[2] = MathTex(r"x^{2}-6x-7 \le 0")
        kroki[3] = MathTex(r"\Delta = (-6)^{2} - 4 \cdot 1 \cdot (-7)")
        kroki[4] = MathTex(r"\Delta = 64", r"\qquad", r"\sqrt{\Delta} = 8")
        kroki[5] = MathTex(r"x_{1} = \frac{6-8}{2}", r"\qquad", r"x_{2} = \frac{6+8}{2}")
        kroki[6] = MathTex(r"x_{1} = -1", r"\qquad", r"x_{2} = 7")
        kroki[7] = MathTex(r"x \in \langle -1,\ 7 \rangle")

        for krok in kroki:
            krok.fill_color = BLACK
            krok.font_size = 100

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
            # Przytrzymanie PRZED sprzątaniem sceny.
            self.wait(0.25)
            self.clear()
            if zielony_cel:
                kroki[dokad].set_color(BLACK)
            self.add(kroki[dokad])

        self.next_section("krok1")
        # KROK 1 — nierówność z zadania.
        self.play(Create(kroki[0]))
        self.wait(0.25)

        self.next_section("krok2")
        # KROK 2 — wymnażamy nawias.
        przejdz(0, 1)

        self.next_section("krok3")
        # KROK 3 — wszystko na lewo, po prawej zero. Bez tego nie ma jak korzystać
        # z miejsc zerowych (w kluczu CKE etap konieczny, choć sam za 0 pkt).
        przejdz(1, 2)

        self.next_section("krok4")
        # KROK 4 — wyróżnik. Tu siedzi najczęstszy błąd: c = -7, więc -4ac daje PLUS 28.
        przejdz(2, 3)

        self.next_section("krok5")
        # KROK 5 — wynik wyróżnika i jego pierwiastek.
        przejdz(3, 4)

        self.next_section("krok6")
        # KROK 6 — wzory na miejsca zerowe.
        przejdz(4, 5)

        self.next_section("krok7")
        # KROK 7 — miejsca zerowe. Za to jest punkt, stąd zielony.
        przejdz(5, 6, zielony_cel=True)

        self.next_section("krok8")
        # KROK 8 — zbiór rozwiązań. Drugi punkt z klucza.
        kroki[7].set_color(GREEN)
        self.play(TransformMatchingShapes(kroki[6], kroki[7]), run_time=1.4)
        self.wait(0.25)
