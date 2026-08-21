from manim import *


class Zad7(Scene):
    """Zadanie 7, grudzien 2024: para x = -1, y = 6 spelnia uklad; szukamy a*b.

    DWANASCIE KROKOW, jeden do jednego z dwunastoma linijkami rachunku
    w rozwiazaniu opisowym (pole solutionText w exercises.json). Scenariusz
    slowny: manimations/zad7-kroki.md.

    DWA ETAPY, KAZDE ROWNANIE OSOBNO (zasada Henricha, 2026-08-21). Dawna wersja
    prowadzila oba rownania rownolegle w jednej klamrze; teraz film bierze
    najpierw pierwsze rownanie i doprowadza je do a = -2, potem odklada ten wynik
    na gore kadru i tak samo przerabia drugie rownanie do b = 1. Dopiero na koncu
    obie wartosci schodza sie w iloczyn.

    Reszta jak w solutionZad2.py i solutionZad3.py: kazdy krok idzie
    „wszystko czarne, zapalenie zielonego, animacja, znowu czarne", stany sa
    MathTexem pocietym na CZESCI, a pary wskazane recznie.

    ZIELONE JEST TO, CO SIE ZMIENIA. Podstawiane wartosci (x na -1, y na 6),
    liczby, ktore zlewaja sie w jedna, znak, ktory przechodzi na druga strone.
    Litery a i b oraz same rownania, ktore tylko jada w inne miejsce kadru,
    zostaja czarne. Nawiasow nie kolorujemy.
    """

    ZIELONY = "#2e7d32"
    ZAPALANIE = 0.4

    def construct(self):

        # ETAP 1: pierwsze rownanie. Stany sa pociete tak, zeby kazda litera,
        # liczba i znak mialy wlasny uchwyt.
        r1 = MathTex(r"a", r"x", r"+", r"3", r"y", r"=", r"20")       # w klamrze
        r2 = MathTex(r"x", r"+", r"b", r"y", r"=", r"5")              # w klamrze
        k2 = MathTex(r"a", r"x", r"+", r"3", r"y", r"=", r"20")       # samo, na srodku
        k3 = MathTex(r"a", r"\cdot", r"(-1)", r"+", r"3", r"\cdot", r"6", r"=", r"20")
        k4 = MathTex(r"-", r"a", r"+", r"18", r"=", r"20")
        k5 = MathTex(r"-", r"a", r"=", r"2")
        k6 = MathTex(r"a", r"=", r"-", r"2")

        # ETAP 2: wynik pierwszego etapu jedzie na gore kadru i tam zostaje,
        # a pod nim idzie drugie rownanie.
        gora = MathTex(r"a", r"=", r"-", r"2")
        e2 = MathTex(r"x", r"+", r"b", r"y", r"=", r"5")
        d8 = MathTex(r"(-1)", r"+", r"6", r"b", r"=", r"5")
        d9 = MathTex(r"6", r"b", r"=", r"6")
        d10 = MathTex(r"b", r"=", r"1")

        # ETAP 3: obie wartosci schodza sie w iloczyn.
        k11 = MathTex(r"a", r"\cdot", r"b", r"=", r"(-2)", r"\cdot", r"1")
        k12 = MathTex(r"a", r"\cdot", r"b", r"=", r"-2")

        wszystkie = [r1, r2, k2, k3, k4, k5, k6, gora, e2, d8, d9, d10, k11, k12]
        for stan in wszystkie:
            stan.set_color(BLACK)
            stan.font_size = 90

        # Skala WSPOLNA dla wszystkich krokow, liczona z najszerszego: inaczej
        # litery zmieniaja rozmiar w trakcie przeksztalcenia i Transform robi
        # z tego zoom.
        MARGINES = 0.85
        najszerszy = max(stan.width for stan in wszystkie)
        if najszerszy > config.frame_width * MARGINES:
            wspolczynnik = config.frame_width * MARGINES / najszerszy
            for stan in wszystkie:
                stan.scale(wspolczynnik)

        # Uklad z zadania: dwa rownania wyrownane do lewej plus klamra.
        VGroup(r1, r2).arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        klamra = MathTex(r"\{", color=BLACK)
        # scale_to_fit_height, a nie stretch_to_fit_height: rozciaganie tylko w pionie
        # robi z klamry cienka kreske z haczykiem.
        klamra.scale_to_fit_height(VGroup(r1, r2).height * 1.35)
        klamra.next_to(VGroup(r1, r2), LEFT, buff=0.35)
        uklad = VGroup(klamra, r1, r2)
        uklad.move_to(ORIGIN)

        for stan in (k2, k3, k4, k5, k6, k11, k12):
            stan.move_to(ORIGIN)
        gora.move_to(UP * 1.25)
        for stan in (e2, d8, d9, d10):
            stan.move_to(DOWN * 0.95)

        def zapal(*co):
            self.play(*[m.animate.set_color(self.ZIELONY) for m in co],
                      run_time=self.ZAPALANIE)

        def zgas(zrodla, cele, nastepny):
            """Gasimy to, co PO PRZEKSZTALCENIU lezy w kadrze (czyli zrodla,
            bo Transform zostawia obiekt zrodlowy), potem podmieniamy scene na
            czysty nastepny stan i dopiero przytrzymujemy.

            Do `zrodla` nie wolno wpisac niczego, co wyszlo z kadru przez
            FadeOut: animacja na obiekcie spoza sceny wstawilaby go z powrotem.
            """
            if zrodla:
                self.play(*[m.animate.set_color(BLACK) for m in zrodla],
                          run_time=self.ZAPALANIE)
            for m in cele:
                m.set_color(BLACK)
            self.clear()
            self.add(nastepny)
            self.wait(0.25)

        self.next_section("krok1")
        # Uklad z zadania. Nic sie jeszcze nie zmienia, wiec nie ma czego zaznaczac.
        self.play(Create(uklad))
        zgas([], [], uklad)

        self.next_section("krok2")
        # Bierzemy PIERWSZE rownanie i tylko nim sie teraz zajmujemy. Nic sie
        # w nim nie zmienia, samo przejezdza na srodek kadru, wiec bez koloru.
        self.play(
            *[Transform(r1[i], k2[i]) for i in range(len(k2))],
            FadeOut(r2), FadeOut(klamra),
        )
        zgas([], [], k2)

        self.next_section("krok3")
        # Podstawienie x = -1 oraz y = 6. Zielone jest to, co zmienia wartosc
        # (litery x i y na liczby) i kropki mnozenia, ktorych wczesniej nie bylo.
        # Litera a zostaje czarna, bo to jej wlasnie szukamy.
        zapal(k2[1], k2[4])
        for cel in (k3[1], k3[2], k3[5], k3[6]):
            cel.set_color(self.ZIELONY)
        self.play(
            Transform(k2[0], k3[0]),
            Transform(k2[1], k3[2]),      # x -> (-1)
            Transform(k2[2], k3[3]),
            Transform(k2[3], k3[4]),
            Transform(k2[4], k3[6]),      # y -> 6
            Transform(k2[5], k3[7]),
            Transform(k2[6], k3[8]),
            FadeIn(k3[1]), FadeIn(k3[5]),  # kropki mnozenia
        )
        zgas([k2[1], k2[4], k3[1], k3[5]],
             [k3[1], k3[2], k3[5], k3[6]], k3)

        self.next_section("krok4")
        # Liczymy iloczyny: a razy (-1) to -a, a 3 razy 6 to 18. Zielone jest to,
        # co sie zlewa w nowy zapis; sama litera a zostaje.
        zapal(k3[1], k3[2], k3[4], k3[5], k3[6])
        k4[0].set_color(self.ZIELONY)
        k4[3].set_color(self.ZIELONY)
        self.play(
            Transform(k3[0], k4[1]),                          # a zostaje a
            Transform(VGroup(k3[1], k3[2]), k4[0]),           # kropka i (-1) -> minus
            Transform(k3[3], k4[2]),
            Transform(VGroup(k3[4], k3[5], k3[6]), k4[3]),    # 3 razy 6 -> 18
            Transform(k3[7], k4[4]),
            Transform(k3[8], k4[5]),
        )
        zgas([k3[1], k3[2], k3[4], k3[5], k3[6]], [k4[0], k4[3]], k4)

        self.next_section("krok5")
        # 18 przechodzi na prawa strone i tam odejmuje sie od 20. Trzy elementy
        # zlewaja sie w jedna liczbe, wiec wszystkie trzy sa zielone.
        zapal(k4[2], k4[3], k4[5])
        k5[3].set_color(self.ZIELONY)
        self.play(
            Transform(k4[0], k5[0]),
            Transform(k4[1], k5[1]),
            Transform(k4[4], k5[2]),
            Transform(VGroup(k4[2], k4[3], k4[5]), k5[3]),    # +18 i 20 -> 2
        )
        zgas([k4[2], k4[3], k4[5]], [k5[3]], k5)

        self.next_section("krok6")
        # Obie strony mnozymy przez -1, czyli minus przechodzi od a do wyniku.
        # Zielony jest tylko ten minus, bo tylko on zmienia miejsce w rachunku.
        zapal(k5[0])
        k6[2].set_color(self.ZIELONY)
        self.play(
            Transform(k5[1], k6[0]),
            Transform(k5[2], k6[1]),
            Transform(k5[0], k6[2]),      # minus przechodzi na druga strone
            Transform(k5[3], k6[3]),
        )
        zgas([k5[0]], [k6[2]], k6)

        self.next_section("krok7")
        # ETAP DRUGI. Wyliczone a odjezdza na gore kadru i tam zostaje do konca,
        # a pod nim wjezdza drugie rownanie z zadania. Nic sie nie przelicza,
        # wiec nie ma koloru.
        self.play(
            *[Transform(k6[i], gora[i]) for i in range(len(gora))],
            FadeIn(e2),
        )
        zgas([], [], VGroup(gora, e2))

        self.next_section("krok8")
        # To samo podstawienie co poprzednio, tylko w drugim rownaniu.
        # Litera b jedzie przed szostke i zostaje czarna, bo dalej jest ta sama
        # niewiadoma; zielone sa x i y, ktore zmieniaja sie w liczby.
        zapal(e2[0], e2[3])
        d8[0].set_color(self.ZIELONY)
        d8[2].set_color(self.ZIELONY)
        self.play(
            Transform(e2[0], d8[0]),      # x -> (-1)
            Transform(e2[1], d8[1]),
            Transform(e2[2], d8[3]),      # b przesuwa sie za szostke
            Transform(e2[3], d8[2]),      # y -> 6
            Transform(e2[4], d8[4]),
            Transform(e2[5], d8[5]),
        )
        zgas([e2[0], e2[3]], [d8[0], d8[2]], VGroup(gora, d8))

        self.next_section("krok9")
        # -1 przechodzi na prawa strone i dodaje sie do 5.
        zapal(d8[0], d8[1], d8[5])
        d9[3].set_color(self.ZIELONY)
        self.play(
            Transform(d8[2], d9[0]),
            Transform(d8[3], d9[1]),
            Transform(d8[4], d9[2]),
            Transform(VGroup(d8[0], d8[1], d8[5]), d9[3]),    # (-1) i 5 -> 6
        )
        zgas([d8[0], d8[1], d8[5]], [d9[3]], VGroup(gora, d9))

        self.next_section("krok10")
        # Obie strony dzielimy przez 6, wiec obie szostki znikaja i zostaje 1.
        zapal(d9[0], d9[3])
        d10[2].set_color(self.ZIELONY)
        self.play(
            Transform(d9[1], d10[0]),
            Transform(d9[2], d10[1]),
            Transform(VGroup(d9[0], d9[3]), d10[2]),          # 6 i 6 -> 1
        )
        zgas([d9[0], d9[3]], [d10[2]], VGroup(gora, d10))

        self.next_section("krok11")
        # ETAP TRZECI. Zadanie pyta o iloczyn, wiec obie wyliczone wartosci
        # zjezdzaja do jednej linijki. Same wartosci tylko sie przesuwaja, wiec
        # sa czarne; zielone sa kropki mnozenia, ktorych wczesniej nie bylo.
        for cel in (k11[1], k11[5]):
            cel.set_color(self.ZIELONY)
        self.play(
            Transform(gora[0], k11[0]),                       # a
            Transform(gora[1], k11[3]),                       # znak =
            Transform(VGroup(gora[2], gora[3]), k11[4]),      # -2
            Transform(d10[0], k11[2]),                        # b
            Transform(d10[2], k11[6]),                        # 1
            FadeOut(d10[1]),                                  # drugi znak =
            FadeIn(k11[1]), FadeIn(k11[5]),                   # kropki mnozenia
        )
        zgas([k11[1], k11[5]], [k11[1], k11[5]], k11)

        self.next_section("krok12")
        # Mnozenie przez 1 nic nie zmienia, wiec kropka z jedynka znikaja,
        # a wynik zostaje. Zielone jest to, co znika.
        zapal(k11[5], k11[6])
        self.play(
            Transform(k11[0], k12[0]),
            Transform(k11[1], k12[1]),
            Transform(k11[2], k12[2]),
            Transform(k11[3], k12[3]),
            Transform(k11[4], k12[4]),        # (-2) traci nawiasy
            FadeOut(VGroup(k11[5], k11[6])),  # kropka i jedynka
        )
        # Zielone kawalki wyszly z kadru FadeOut-em, wiec nie ma juz czego gasic.
        zgas([], [], k12)


# ---------------------------------------------------------------------------
# DAWNA WERSJA SCENY (oba rownania rownolegle w jednej klamrze, sprzed podzialu
# na dwa etapy z 2026-08-21). Zostawiona zakomentowana na czas sprawdzenia nowej
# wersji; do usuniecia, gdy Henrich potwierdzi, ze nowe kroki sa w porzadku.
# ---------------------------------------------------------------------------

# from manim import *
#
#
# # Zadanie 7 — para x = -1, y = 6 spełnia układ; szukamy a·b. Wynik -2, odpowiedź A.
# #
# # Scenariusz kroków jest w manimations/zad7-kroki.md.
# #
# # Render: manim --save_sections solutionZad7.py Zad7
# class Zad7(Scene):
#
#     def construct(self):
#         GREEN = "#0AB32F"
#
#         # Oba równania jadą RÓWNOLEGLE, jedno pod drugim — w tym zadaniu nie ma
#         # układu do rozwiązywania, są dwa niezależne równania z jedną niewiadomą
#         # każde, i to ma być widać.
#         kroki = [None] * 7
#         kroki[0] = MathTex(r"\begin{cases} ax + 3y = 20 \\ x + by = 5 \end{cases}")
#         kroki[1] = MathTex(r"\begin{cases} a \cdot (-1) + 3 \cdot 6 = 20 \\ (-1) + b \cdot 6 = 5 \end{cases}")
#         kroki[2] = MathTex(r"\begin{cases} -a + 18 = 20 \\ -1 + 6b = 5 \end{cases}")
#         kroki[3] = MathTex(r"\begin{cases} -a = 2 \\ 6b = 6 \end{cases}")
#         kroki[4] = MathTex(r"\begin{cases} a = -2 \\ b = 1 \end{cases}")
#         kroki[5] = MathTex(r"a \cdot b = (-2) \cdot 1")
#         kroki[6] = MathTex(r"a \cdot b = -2")
#
#         for krok in kroki:
#             krok.fill_color = BLACK
#             krok.font_size = 90
#
#         MARGINES = 0.85
#         najszerszy = max(k.width for k in kroki)
#         if najszerszy > config.frame_width * MARGINES:
#             wspolczynnik = config.frame_width * MARGINES / najszerszy
#             for k in kroki:
#                 k.scale(wspolczynnik)
#         for k in kroki:
#             k.move_to(ORIGIN)
#
#         def przejdz(skad, dokad, zielony_cel=False):
#             if zielony_cel:
#                 kroki[dokad].set_color(GREEN)
#             self.play(TransformMatchingShapes(kroki[skad], kroki[dokad]), run_time=1.4)
#             self.wait(0.25)
#             self.clear()
#             if zielony_cel:
#                 kroki[dokad].set_color(BLACK)
#             self.add(kroki[dokad])
#
#         self.next_section("krok1")
#         # KROK 1 — układ z zadania.
#         self.play(Create(kroki[0]))
#         self.wait(0.25)
#
#         self.next_section("krok2")
#         # KROK 2 — podstawiamy x = -1 i y = 6.
#         przejdz(0, 1)
#
#         self.next_section("krok3")
#         # KROK 3 — liczymy iloczyny liczbowe.
#         przejdz(1, 2)
#
#         self.next_section("krok4")
#         # KROK 4 — liczby na prawą stronę.
#         przejdz(2, 3)
#
#         self.next_section("krok5")
#         # KROK 5 — wyliczone a i b. Na zielono, bo to pierwszy realny wynik.
#         przejdz(3, 4, zielony_cel=True)
#
#         self.next_section("krok6")
#         # KROK 6 — wstawiamy do tego, o co pyta zadanie: iloczynu a·b.
#         przejdz(4, 5)
#
#         self.next_section("krok7")
#         # KROK 7 — wynik.
#         kroki[6].set_color(GREEN)
#         self.play(TransformMatchingShapes(kroki[5], kroki[6]), run_time=1.4)
#         self.wait(0.25)
