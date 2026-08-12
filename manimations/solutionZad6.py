from manim import *


# Zadanie 6 — (x/(x^2-1)) : (3x^2/(x+1)) = 1/(3x^2-3x), odpowiedź B.
#
# Scenariusz kroków jest w manimations/zad6-kroki.md — zatwierdzony przed
# napisaniem tego pliku. Zmieniasz przebieg tutaj → popraw i tam.
#
# Render: manim --save_sections solutionZad6.py Zad6
class Zad6(Scene):

    def construct(self):
        GREEN = "#0AB32F"

        # Każdy krok jest złożony z CZĘŚCI (osobne stringi w MathTex), a nie z jednego
        # napisu — dzięki temu kolorujemy „to, co się zmienia" całymi kawałkami
        # (np. sam mianownik), bez liczenia pojedynczych glifów. Ten sam chwyt
        # co w zad. 2.
        kroki = [None] * 6
        kroki[0] = MathTex(r"\frac{x}{x^{2}-1}",        r":",      r"\frac{3x^{2}}{x+1}")
        kroki[1] = MathTex(r"\frac{x}{(x-1)(x+1)}",     r":",      r"\frac{3x^{2}}{x+1}")
        kroki[2] = MathTex(r"\frac{x}{(x-1)(x+1)}",     r"\cdot",  r"\frac{x+1}{3x^{2}}")
        kroki[3] = MathTex(r"\frac{1}{x-1}",            r"\cdot",  r"\frac{1}{3x}")
        kroki[4] = MathTex(r"\frac{1}{3x(x-1)}")
        kroki[5] = MathTex(r"\frac{1}{3x^{2}-3x}")

        for krok in kroki:
            krok.fill_color = BLACK
            krok.font_size = 110

        # Skala WSPÓLNA, liczona z najszerszego kroku — inaczej litery zmieniałyby
        # rozmiar w trakcie przekształcenia (patrz zad. 1–4).
        MARGINES = 0.85
        najszerszy = max(krok.width for krok in kroki)
        if najszerszy > config.frame_width * MARGINES:
            wspolczynnik = config.frame_width * MARGINES / najszerszy
            for krok in kroki:
                krok.scale(wspolczynnik)
        for krok in kroki:
            krok.move_to(ORIGIN)

        # Przejścia robi TransformMatchingShapes: sam dobiera sobie pary glifów po
        # kształcie. Przy ułamkach, które zmieniają budowę (kreski ułamkowe rosną,
        # nawiasy się pojawiają), ręczne mapowanie indeksów jest bardzo kruche,
        # a tu chodzi o to, żeby te same symbole przejechały na nowe miejsce.
        def przejdz(skad, dokad, zielone_skad=(), zielone_dokad=()):
            for i in zielone_skad:
                kroki[skad][i].set_color(GREEN)
            for i in zielone_dokad:
                kroki[dokad][i].set_color(GREEN)
            self.play(TransformMatchingShapes(kroki[skad], kroki[dokad]), run_time=1.4)
            # Przytrzymanie PRZED sprzątaniem sceny — po `self.clear()` trzymałoby
            # białą planszę, a to ta klatka zostaje uczniowi na ekranie.
            self.wait(0.25)
            self.clear()
            # Zieleń zdejmujemy dopiero teraz: w trakcie przytrzymania ma być widać,
            # co się przed chwilą zmieniło.
            for i in zielone_dokad:
                kroki[dokad][i].set_color(BLACK)
            self.add(kroki[dokad])

        self.next_section("krok1")
        # KROK 1 — wyrażenie z zadania.
        self.play(Create(kroki[0]))
        self.wait(0.25)

        self.next_section("krok2")
        # KROK 2 — x^2-1 rozkłada się na (x-1)(x+1). Bez tego nie widać, co skrócić.
        przejdz(0, 1, zielone_skad=(0,), zielone_dokad=(0,))

        self.next_section("krok3")
        # KROK 3 — dzielenie na mnożenie przez odwrotność: drugi ułamek staje na głowie.
        przejdz(1, 2, zielone_skad=(1, 2), zielone_dokad=(1, 2))

        self.next_section("krok4")
        # KROK 4 — skracamy (x+1) i jedno x z x^2.
        przejdz(2, 3, zielone_dokad=(0, 2))

        self.next_section("krok5")
        # KROK 5 — dwa ułamki zlewają się w jeden.
        przejdz(3, 4)

        self.next_section("krok6")
        # KROK 6 — wymnożony mianownik, czyli zapis dokładnie taki jak w odpowiedzi B.
        self.play(TransformMatchingShapes(kroki[4], kroki[5]), run_time=1.4)
        self.wait(0.25)
