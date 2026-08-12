from manim import *


# Zadanie 4 — log_7 x + 6 log_7 y = log_7(x y^6), odpowiedź D.
#
# Scenariusz kroków był ustalony i zatwierdzony PRZED napisaniem tego pliku —
# leży w manimations/zad4-kroki.md (treść, cztery kroki, opisy pod film,
# wyjaśnienie błędnych odpowiedzi). Jeśli zmieniasz tu przebieg, popraw i tam.
#
# Render (bez flagi jakości — kadr i fps biorą się z manim.cfg):
#     manim --save_sections solutionZad4.py Zad4
# Każdy krok ląduje osobnym plikiem w media/videos/solutionZad4/720p120/sections/.
class Zad4(Scene):

    def construct(self):
        GREEN = "#0AB32F"

        # Kolejne stany zapisu. Kropka na pasku pod filmem = jeden z nich,
        # film = przejście między dwoma sąsiednimi.
        kroki = [None] * 4
        kroki[0] = MathTex(r"\log_{7}x + 6\log_{7}y")        # 12 glifów: log_7 x + 6 log_7 y
        kroki[1] = MathTex(r"\log_{7}x + \log_{7}(y^6)")     # 14 glifów: doszły nawiasy
        kroki[2] = MathTex(r"\log_{7}(x \cdot y^6)")         # 10 glifów
        kroki[3] = MathTex(r"\log_{7}(xy^6)")                #  9 glifów: bez kropki mnożenia

        for krok in kroki:
            krok.fill_color = BLACK
            krok.font_size = 110

        # Skala WSPÓLNA dla wszystkich kroków, liczona z najszerszego — osobne
        # dopasowanie każdego kroku zmieniałoby wielkość liter w trakcie
        # przekształcenia, a Transform robiłby z tego zoom. Tak samo w zad. 1–3.
        MARGINES = 0.85
        najszerszy = max(krok.width for krok in kroki)
        if najszerszy > config.frame_width * MARGINES:
            wspolczynnik = config.frame_width * MARGINES / najszerszy
            for krok in kroki:
                krok.scale(wspolczynnik)
        for krok in kroki:
            krok.move_to(ORIGIN)

        # Wzory pomocnicze nie są rysowane w filmie (zasada z 2026-08-11) —
        # pokazuje je strona pod filmem, z pola "text" przy kroku w exercises.json.
        # Oba potrzebne tu wzory to [3.2] z tablic (s. 5):
        #   krok 2 → log_a x^r = r · log_a x   (czytane od prawej)
        #   krok 3 → log_a x + log_a y = log_a(x · y)

        # Każda sekcja kończy się `self.wait(0.25)` — bez tego przeglądarka
        # zatrzymuje obraz kilka klatek przed końcem pliku i ostatni element
        # animacji nie zostaje na ekranie (README, punkt 0 workflow).

        self.next_section("krok1")
        # KROK 1 — wyrażenie z zadania wjeżdża w kadr.
        self.play(Create(kroki[0]))
        self.wait(0.25)

        self.next_section("krok2")
        # KROK 2 — szóstka sprzed logarytmu przelatuje na miejsce wykładnika
        # przy y. Na zielono to, co się rusza: szóstka tu i tam.
        kroki[0][0][6].set_color(GREEN)
        kroki[1][0][12].set_color(GREEN)
        self.play(
            Transform(kroki[0][0][0:6], kroki[1][0][0:6]),      # log_7 x +  — bez zmian
            Transform(kroki[0][0][6], kroki[1][0][12]),         # 6 → wykładnik
            Transform(kroki[0][0][7:11], kroki[1][0][6:10]),    # drugie log_7
            Transform(kroki[0][0][11], kroki[1][0][11]),        # y
            FadeIn(kroki[1][0][10], kroki[1][0][13]),           # nawiasy wokół y^6
            run_time=1.4,
        )
        self.wait(0.25)
        # Zieleń zdejmujemy dopiero po przytrzymaniu: to ona pokazuje, co się
        # przed chwilą stało, i ma zostać na klatce, którą widzi uczeń.
        self.clear()
        kroki[1][0][12].set_color(BLACK)

        self.next_section("krok3")
        # KROK 3 — dwa logarytmy o tej samej podstawie zbiegają się w jeden,
        # a plus zamienia się w kropkę mnożenia.
        self.add(kroki[1])
        kroki[1][0][5].set_color(GREEN)
        kroki[2][0][6].set_color(GREEN)
        self.play(
            Transform(kroki[1][0][0:4], kroki[2][0][0:4]),      # log_7 zostaje
            Transform(kroki[1][0][4], kroki[2][0][5]),          # x wchodzi do nawiasu
            Transform(kroki[1][0][5], kroki[2][0][6]),          # + → ·
            FadeOut(kroki[1][0][6:10]),                         # drugie log_7 znika
            Transform(kroki[1][0][10], kroki[2][0][4]),         # nawias otwierający
            Transform(kroki[1][0][11:14], kroki[2][0][7:10]),   # y^6 z nawiasem zamykającym
            run_time=1.4,
        )
        self.wait(0.25)
        self.clear()
        kroki[2][0][6].set_color(BLACK)

        self.next_section("krok4")
        # KROK 4 — kropkę mnożenia zwyczajowo pomijamy; dopiero taki zapis
        # wygląda dokładnie jak odpowiedź D w arkuszu.
        self.add(kroki[2])
        self.play(
            Transform(kroki[2][0][0:6], kroki[3][0][0:6]),
            FadeOut(kroki[2][0][6], scale=0.3),                 # kropka znika
            Transform(kroki[2][0][7:10], kroki[3][0][6:9]),     # y^6 dosuwa się do x
            run_time=1.4,
        )
        self.wait(0.25)
