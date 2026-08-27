from manim import *

# Zadanie 9 (otwarte, 2 pkt). Rozwiąż x(x-6) <= 7. Wynik: x nalezy do <-1, 7>.
#
# Projekt: issues/projekt-zad9-zad10-2024-grudzien.md. Scenariusz kroków opisowo:
# manimations/zad9-kroki.md. Dwadzieścia jeden kroków, jeden do jednego
# z dwudziestoma jeden linijkami rachunku w solutionText.
#
# NAPISANE OD NOWA 2026-08-28 (poprzednia wersja miała osiem kroków i szła do
# kosza, patrz projekt). Co jest nowe:
#   - ogniwa policzone dotąd w głowie (x*x-x*6, podstawienie do delty,
#     -(-6), dzielenia) dostają własny krok, na wzór zad. 7 i 8,
#   - miejsca zerowe liczone SĄ DWOMA TORAMI PO KOLEI (x1 do końca, potem x2),
#     jak w zad. 7 (README, „dwie niezależne rzeczy licz po kolei"),
#   - ostatnie trzy kroki rysują szkic paraboli, żeby wniosek o przedziale
#     ⟨-1, 7⟩ był widoczny w filmie, a nie tylko w opisie pod nim.
#
# Kolor: zielone = to, co się w danym kroku ZMIENIA (README, „Jak ma wyglądać
# animacja"). Trzymam się dosłownie kolumny „Zielone" z projektu; reszta nowych
# elementów (etykiety, struktura wzoru) wjeżdża czarno/szaro bez podświetlenia.
#
# DWIE ŚWIADOME UPROSZCZENIA WOBEC PROJEKTU (opisane w raporcie końcowym):
#   - krok 5 „trzy minusy": interpretuję jako dwa faktyczne znaki minus
#     (przy -6 i przy -7) plus nowa jedynka (współczynnik a), bo w treści
#     nie ma trzeciego minusa do wskazania,
#   - krok 10 „wstawiane liczby": -6, 2 i 1 wjeżdżają jako nowe (FadeIn),
#     nie z KONKRETNEGO miejsca na ekranie, bo współczynniki z kroku 5 są już
#     w tym momencie usunięte ze sceny (zużyte w kroku 6 do budowy wzoru na deltę).
#
# Wykres w krokach 19 do 21 używa fioletu `--accent-purple` (#7a3fa8, COLORS.md,
# rola „wykres funkcji jak w arkuszach CKE"), bo to dosłownie wykres funkcji,
# tylko szkicowy. Oś jest szara (#666666, rola „osie").
#
# Render: manim --save_sections solutionZad9.py Zad9  (albo tools/wgraj-kroki.sh 9)

ZIELONY = "#2e7d32"
FIOLET = "#7a3fa8"
SZARY_OSIE = "#666666"
SZARY_DOPISEK = "#888888"

ROWNANIE_Y = UP * 0.4
GORA_Y = UP * 2.4
KOEF_Y = DOWN * 1.4
POSTOJ = 0.45


class Zad9(Scene):

    # ---- klocki, jak w solutionZad8.py --------------------------------

    def stan(self, *args, rozmiar=100):
        m = MathTex(*args)
        m.set_color(BLACK)
        m.font_size = rozmiar
        return m

    def zapal(self, *mobiekty, czas=0.4):
        self.play(*[m.animate.set_color(ZIELONY) for m in mobiekty], run_time=czas)

    def zakoncz(self, *czysty, pomin=(), czas=0.4):
        self.wait(0.3)
        gasnie = [m for m in self.mobjects if not any(m is p for p in pomin)]
        if gasnie:
            self.play(*[m.animate.set_color(BLACK) for m in gasnie], run_time=czas)
        self.clear()
        self.add(*czysty)
        self.wait(0.25)

    def construct(self):
        # ================================================================
        # Stany rachunku, po jednym MathTex na krok. Każdy argument jest
        # sam w sobie zbalansowaną klamrą LaTeX (README, pułapka ułamków),
        # więc wolno je ciąć na dowolne kawałki, którymi trzeba sterować
        # osobno (litery, znaki, liczby).
        # ================================================================
        s1 = self.stan("x", "(", "x", "-", "6", ")", r"\le", "7")
        s2 = self.stan("x", r"\cdot", "x", "-", "x", r"\cdot", "6", r"\le", "7")
        s3 = self.stan("x", "^{2}", "-", "6", "x", r"\le", "7")
        dop3 = self.stan(r"\big/", "-", "7", rozmiar=72)
        dop3.set_color(SZARY_DOPISEK)
        s4 = self.stan("x", "^{2}", "-", "6", "x", "-", "7", r"\le", "0")

        a_cz = self.stan("a", "=", "1")
        b_cz = self.stan("b", "=", "-", "6")
        c_cz = self.stan("c", "=", "-", "7")

        s6 = self.stan(r"\Delta", "=", "(", "-", "6", ")", "^{2}", "-", "4",
                        r"\cdot", "1", r"\cdot", "(", "-", "7", ")")
        s7 = self.stan(r"\Delta", "=", "36", "+", "28")
        s8 = self.stan(r"\Delta", "=", "64")
        s9 = self.stan(r"\sqrt{\Delta}", "=", "8")
        s10 = self.stan(r"x_{1,2}", "=", r"\dfrac{-(-6) \pm 8}{2 \cdot 1}")
        s11 = self.stan(r"x_{1,2}", "=", r"\dfrac{6 \pm 8}{2}")

        x1a = self.stan(r"x_{1}", "=", r"\dfrac{6 - 8}{2}")
        x1b = self.stan(r"x_{1}", "=", r"\dfrac{-2}{2}")
        x1c = self.stan(r"x_{1}", "=", "-1")
        x1_gora = self.stan(r"x_{1}", "=", "-1")

        x2a = self.stan(r"x_{2}", "=", r"\dfrac{6 + 8}{2}")
        x2b = self.stan(r"x_{2}", "=", r"\dfrac{14}{2}")
        x2c = self.stan(r"x_{2}", "=", "7")

        s18 = self.stan(r"x_{1} = -1, \quad x_{2} = 7")
        s18_gora = self.stan(r"x_{1} = -1, \quad x_{2} = 7")

        # Wspólna skala. Liczymy z najszerszego pojedynczego stanu; dopisek
        # liczy się osobno (stoi obok równania, nie na jego miejscu).
        MARGINES = 0.85
        glowne = [s1, s2, s3, s4, a_cz, b_cz, c_cz, s6, s7, s8, s9, s10, s11,
                  x1a, x1b, x1c, x1_gora, x2a, x2b, x2c, s18, s18_gora]
        najszerszy = max(m.width for m in glowne)
        POLE = config.frame_width * MARGINES
        wsp = min(1.0, POLE / najszerszy)
        for m in glowne + [dop3]:
            m.scale(wsp)

        for m in glowne:
            m.move_to(ROWNANIE_Y)
        x1_gora.move_to(GORA_Y)
        s18_gora.move_to(GORA_Y)
        for m in (a_cz, b_cz, c_cz):
            m.move_to(KOEF_Y)
        VGroup(a_cz, b_cz, c_cz).arrange(RIGHT, buff=0.6).move_to(KOEF_Y)

        def postoj(cel, wzgledem):
            return cel.copy().move_to([cel.get_x(), wzgledem.get_top()[1] + POSTOJ, 0])

        # ================================================================
        # KROK 1. Nierówność z treści zadania. Bez koloru.
        # ================================================================
        self.next_section("krok1")
        self.play(Write(s1), run_time=1.4)
        self.wait(0.25)

        # ================================================================
        # KROK 2. Opuszczamy nawias: x sprzed nawiasu rozdwaja się przed
        # każdy składnik. Zielone: dwa nowe x i obie kropki mnożenia.
        # ================================================================
        self.next_section("krok2")
        self.zapal(s1[0])
        kopia_a = s1[0].copy()
        kopia_b = s1[0].copy()
        self.add(kopia_a, kopia_b)
        s2[0].set_color(ZIELONY)
        s2[1].set_color(ZIELONY)
        s2[4].set_color(ZIELONY)
        s2[5].set_color(ZIELONY)
        self.play(
            ReplacementTransform(kopia_a, s2[0]),
            FadeIn(s2[1]),
            ReplacementTransform(s1[2], s2[2]),
            ReplacementTransform(s1[3], s2[3]),
            ReplacementTransform(kopia_b, s2[4]),
            FadeIn(s2[5]),
            ReplacementTransform(s1[4], s2[6]),
            FadeOut(s1[1]), FadeOut(s1[5]),
            ReplacementTransform(s1[6], s2[7]),
            ReplacementTransform(s1[7], s2[8]),
            FadeOut(s1[0], scale=0.5),
            run_time=1.4,
        )
        self.zakoncz(s2)

        # ================================================================
        # KROK 3. x*x -> x^2 (wykładnik się pojawia, zielony), x*6 -> 6x
        # (sama zamiana kolejności, bez koloru).
        # ================================================================
        self.next_section("krok3")
        self.zapal(s2[2])
        s3[1].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s2[0], s3[0]),
            FadeOut(s2[1], scale=0.4),
            FadeOut(s2[2], scale=0.4),
            FadeIn(s3[1]),
            ReplacementTransform(s2[3], s3[2]),
            ReplacementTransform(s2[6], s3[3]),
            FadeOut(s2[5], scale=0.4),
            ReplacementTransform(s2[4], s3[4]),
            ReplacementTransform(s2[7], s3[5]),
            ReplacementTransform(s2[8], s3[6]),
            run_time=1.4,
        )
        self.zakoncz(s3)
        dop3.next_to(s3, RIGHT, buff=0.9)
        self.play(FadeIn(dop3, shift=LEFT * 0.3), run_time=0.6)
        self.wait(0.25)

        # ================================================================
        # KROK 4. Siódemka z dopisku leci łukiem nad znakiem <=, staje się
        # -7; po prawej zostaje 0. Zielone: minus przy siódemce i zero.
        # ================================================================
        self.next_section("krok4")
        self.zapal(dop3[1], dop3[2])
        s4[5].set_color(ZIELONY)
        s4[8].set_color(ZIELONY)
        self.play(
            ReplacementTransform(dop3[2], s4[6], path_arc=-2 * PI / 3),
            ReplacementTransform(dop3[1], s4[5], path_arc=-2 * PI / 3),
            FadeOut(dop3[0], scale=0.4),
            ReplacementTransform(s3[6], s4[8]),
            ReplacementTransform(s3[0], s4[0]),
            ReplacementTransform(s3[1], s4[1]),
            ReplacementTransform(s3[2], s4[2]),
            ReplacementTransform(s3[3], s4[3]),
            ReplacementTransform(s3[4], s4[4]),
            ReplacementTransform(s3[5], s4[7]),
            run_time=1.4,
        )
        self.zakoncz(s4)

        # ================================================================
        # KROK 5. Współczynniki zjeżdżają pod nierówność: kopie -6 i -7
        # z rachunku, nowa jedynka dla a (przy x^2 nic nie stoi). Zielone:
        # oba minusy i nowa jedynka.
        # ================================================================
        self.next_section("krok5")
        self.zapal(s4[2], s4[3], s4[5], s4[6])
        kopia_b = s4[2:4].copy()
        kopia_c = s4[5:7].copy()
        self.add(kopia_b, kopia_c)
        a_cz[2].set_color(ZIELONY)
        b_cz[2].set_color(ZIELONY)
        c_cz[2].set_color(ZIELONY)
        self.play(
            FadeIn(a_cz[0], a_cz[1]),
            FadeIn(a_cz[2]),
            FadeIn(b_cz[0], b_cz[1]),
            ReplacementTransform(kopia_b, b_cz[2:4]),
            FadeIn(c_cz[0], c_cz[1]),
            ReplacementTransform(kopia_c, c_cz[2:4]),
            *[g.animate.set_color(BLACK) for g in (s4[2], s4[3], s4[5], s4[6])],
            run_time=1.4,
        )
        self.zakoncz(s4, a_cz, b_cz, c_cz, pomin=[s4])

        # ================================================================
        # KROK 6. Wartości wsuwają się we wzór na deltę: -6 w nawiasie
        # do kwadratu, 1 i -7 w iloczynie -4*a*c. Zielone: wstawiane liczby.
        # ================================================================
        self.next_section("krok6")
        self.zapal(a_cz[2], b_cz[2], b_cz[3], c_cz[2], c_cz[3])
        for i in (3, 4, 10, 13, 14):
            s6[i].set_color(ZIELONY)
        self.play(
            FadeOut(a_cz[0], a_cz[1]),
            FadeOut(b_cz[0], b_cz[1]),
            FadeOut(c_cz[0], c_cz[1]),
            ReplacementTransform(b_cz[2], s6[3]),
            ReplacementTransform(b_cz[3], s6[4]),
            ReplacementTransform(a_cz[2], s6[10]),
            ReplacementTransform(c_cz[2], s6[13]),
            ReplacementTransform(c_cz[3], s6[14]),
            FadeIn(s6[0], s6[1], s6[2], s6[5], s6[6], s6[7], s6[8], s6[9],
                   s6[11], s6[12], s6[15]),
            FadeOut(s4),
            run_time=1.6,
        )
        self.zakoncz(s6)

        # ================================================================
        # KROK 7. (-6)^2 -> 36, -4*1*(-7) -> +28. Zielone: tylko plus,
        # bo iloczyn dwóch liczb ujemnych daje plus.
        # ================================================================
        self.next_section("krok7")
        self.zapal(*s6[2:7])
        self.zapal(*s6[7:16])
        s7[3].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s6[0], s7[0]),
            ReplacementTransform(s6[1], s7[1]),
            Transform(VGroup(*s6[2:7]), s7[2]),
            FadeIn(s7[3]),
            Transform(VGroup(*s6[7:16]), s7[4]),
            run_time=1.5,
        )
        self.zakoncz(s7)

        # ================================================================
        # KROK 8. 36+28 -> 64. Bez koloru.
        # ================================================================
        self.next_section("krok8")
        self.play(
            ReplacementTransform(s7[0], s8[0]),
            ReplacementTransform(s7[1], s8[1]),
            Transform(VGroup(s7[2], s7[3], s7[4]), s8[2]),
            run_time=1.3,
        )
        self.zakoncz(s8)

        # ================================================================
        # KROK 9. Nad deltą pojawia się pierwiastek, 64 zamienia się w 8.
        # Zielone: sama ósemka.
        # ================================================================
        self.next_section("krok9")
        self.zapal(s8[2])
        s9[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s8[0], s9[0]),
            ReplacementTransform(s8[1], s9[1]),
            ReplacementTransform(s8[2], s9[2]),
            run_time=1.3,
        )
        self.zakoncz(s9)

        # ================================================================
        # KROK 10. Liczby wsuwają się we wzór na pierwiastki: -6 w nawiasie,
        # 2 i 1 w mianowniku. Ósemka to ta sama wartość co przed chwilą
        # (z kroku 9), więc leci na miejsce i zostaje czarna. Zielone:
        # tylko naprawdę NOWE liczby (-6, 2, 1).
        #
        # Glify wewnątrz s10[2] (jeden string, jak w solutionZad8.py):
        # 0 -  1 (  2 -  3 6  4 )  5 ±  6 8  7 kreska  8 2  9 ·  10 1
        # ================================================================
        self.next_section("krok10")
        nowe_zielone = (2, 3, 8, 10)
        for i in range(len(s10[2])):
            if i != 6:
                s10[2][i].set_color(ZIELONY if i in nowe_zielone else BLACK)
        self.play(
            FadeOut(s9[0]), FadeOut(s9[1]),
            FadeIn(s10[0]), FadeIn(s10[1]),
            ReplacementTransform(s9[2], s10[2][6]),
            FadeIn(*[s10[2][i] for i in range(len(s10[2])) if i != 6]),
            run_time=1.4,
        )
        self.remove(s9)
        self.zakoncz(s10)

        # ================================================================
        # KROK 11. -(-6) -> 6 (dwa minusy dają szóstkę, zielona), 2*1 -> 2
        # (bez koloru, to sama porządkowa uproszczenie zapisu).
        #
        # Glify s11[2]: 0 6  1 ±  2 8  3 kreska  4 2
        # ================================================================
        self.next_section("krok11")
        self.zapal(*s10[2][0:5])
        s11[2][0].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s10[0], s11[0]),
            ReplacementTransform(s10[1], s11[1]),
            Transform(VGroup(*s10[2][0:5]), s11[2][0]),
            ReplacementTransform(s10[2][5], s11[2][1]),
            ReplacementTransform(s10[2][6], s11[2][2]),
            ReplacementTransform(s10[2][7], s11[2][3]),
            Transform(VGroup(s10[2][8], s10[2][9], s10[2][10]), s11[2][4]),
            run_time=1.4,
        )
        # s11[2][0] sam nigdy nie trafia na scenę (Transform bez zamiany
        # tożsamości animuje STARE glify s10 w jego stronę), więc zielony
        # kolor ustawiony wyżej trzeba zdjąć ręcznie, zanim s11 posłuży
        # jako czysty stan kolejnego kroku - inaczej zostałby w nim na stałe.
        s11[2][0].set_color(BLACK)
        self.zakoncz(s11)

        # ================================================================
        # KROK 12. Rozdzielamy: zostaje sam x1, znak ± zamienia się w -.
        # Zielone: powstający minus.
        #
        # Glify x1a[2]: 0 6  1 -  2 8  3 kreska  4 2
        # ================================================================
        self.next_section("krok12")
        self.zapal(s11[2][1])
        x1a[2][1].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s11[0], x1a[0]),
            ReplacementTransform(s11[1], x1a[1]),
            ReplacementTransform(s11[2][0], x1a[2][0]),
            ReplacementTransform(s11[2][1], x1a[2][1]),
            ReplacementTransform(s11[2][2], x1a[2][2]),
            ReplacementTransform(s11[2][3], x1a[2][3]),
            ReplacementTransform(s11[2][4], x1a[2][4]),
            run_time=1.4,
        )
        self.zakoncz(x1a)

        # ================================================================
        # KROK 13. 6-8 -> -2. Zielone: wynik -2.
        #
        # Glify x1b[2]: 0 -  1 2  2 kreska  3 2
        # ================================================================
        self.next_section("krok13")
        self.zapal(*x1a[2][0:3])
        VGroup(x1b[2][0], x1b[2][1]).set_color(ZIELONY)
        self.play(
            ReplacementTransform(x1a[0], x1b[0]),
            ReplacementTransform(x1a[1], x1b[1]),
            Transform(VGroup(*x1a[2][0:3]), VGroup(x1b[2][0], x1b[2][1])),
            ReplacementTransform(x1a[2][3], x1b[2][2]),
            ReplacementTransform(x1a[2][4], x1b[2][3]),
            run_time=1.3,
        )
        # Jak w kroku 11: merge-target nigdy sam nie ląduje na scenie, więc
        # zielony kolor zdejmujemy ręcznie przed użyciem x1b jako stanu.
        x1b[2][0].set_color(BLACK)
        x1b[2][1].set_color(BLACK)
        self.zakoncz(x1b)

        # ================================================================
        # KROK 14. -2/2 -> -1. Bez koloru (wynik zostaje na koniec kroku 15).
        # ================================================================
        self.next_section("krok14")
        self.play(
            ReplacementTransform(x1b[0], x1c[0]),
            ReplacementTransform(x1b[1], x1c[1]),
            Transform(x1b[2], x1c[2]),
            run_time=1.3,
        )
        self.zakoncz(x1c)

        # ================================================================
        # KROK 15. x1 = -1 odjeżdża na górę i tam zostaje; wjeżdża drugi
        # tor: x2 = (6+8)/2. Krok przenoszący, bez koloru.
        # ================================================================
        self.next_section("krok15")
        self.play(
            Transform(x1c, x1_gora.copy()),
            FadeIn(x2a, shift=DOWN * 0.3),
            run_time=1.2,
        )
        self.remove(x1c)
        self.zakoncz(x2a, x1_gora, pomin=[x1_gora])

        # ================================================================
        # KROK 16. 6+8 -> 14. Zielone: wynik 14 (nie cały ułamek: kreska
        # i mianownik 2 zostają czarne, bo się nie zmieniają).
        #
        # Glify x2a[2]: 0 6  1 +  2 8  3 kreska  4 2
        # Glify x2b[2]: 0 1  1 4  2 kreska  3 2
        # ================================================================
        self.next_section("krok16")
        self.zapal(*x2a[2][0:3])
        VGroup(x2b[2][0], x2b[2][1]).set_color(ZIELONY)
        self.play(
            ReplacementTransform(x2a[0], x2b[0]),
            ReplacementTransform(x2a[1], x2b[1]),
            Transform(VGroup(*x2a[2][0:3]), VGroup(x2b[2][0], x2b[2][1])),
            ReplacementTransform(x2a[2][3], x2b[2][2]),
            ReplacementTransform(x2a[2][4], x2b[2][3]),
            run_time=1.3,
        )
        # Merge-target nigdy sam nie ląduje na scenie (jak w kroku 11 i 13),
        # więc zielony kolor zdejmujemy ręcznie przed użyciem x2b jako stanu.
        x2b[2][0].set_color(BLACK)
        x2b[2][1].set_color(BLACK)
        self.zakoncz(x2b, x1_gora, pomin=[x1_gora])

        # ================================================================
        # KROK 17. 14/2 -> 7. Bez koloru.
        # ================================================================
        self.next_section("krok17")
        self.play(
            ReplacementTransform(x2b[0], x2c[0]),
            ReplacementTransform(x2b[1], x2c[1]),
            Transform(x2b[2], x2c[2]),
            run_time=1.3,
        )
        self.zakoncz(x2c, x1_gora, pomin=[x1_gora])

        # ================================================================
        # KROK 18. Oba wyniki zjeżdżają w jedną linijkę „miejsca zerowe".
        # Bez koloru: nic się nie przelicza, tylko się spotyka.
        # ================================================================
        self.next_section("krok18")
        self.play(
            Transform(VGroup(x1_gora, x2c), s18.copy()),
            run_time=1.2,
        )
        self.remove(x1_gora, x2c)
        self.zakoncz(s18)

        # ================================================================
        # KROK 19. Linijka wyników odjeżdża w górę i zostaje tam do końca.
        # Pod nią rysuje się oś x, a przez -1 i 7 przechodzi parabola
        # ramionami w górę. Bez koloru: sam rysunek niczego nie przelicza.
        # ================================================================
        self.next_section("krok19")
        os_x = NumberLine(
            x_range=[-3, 9, 1], length=9, include_ticks=False,
            color=SZARY_OSIE, stroke_width=3,
        ).move_to(DOWN * 1.7)
        etykieta_m1 = MathTex("-1", color=SZARY_OSIE, font_size=64)
        etykieta_m1.next_to(os_x.n2p(-1), DOWN, buff=0.2)
        etykieta_7 = MathTex("7", color=SZARY_OSIE, font_size=64)
        etykieta_7.next_to(os_x.n2p(7), DOWN, buff=0.2)
        znacznik_m1 = Dot(os_x.n2p(-1), radius=0.05, color=SZARY_OSIE)
        znacznik_7 = Dot(os_x.n2p(7), radius=0.05, color=SZARY_OSIE)

        Y_SKALA = 0.06

        def f(t):
            return (t + 1) * (t - 7)

        def punkt(t):
            return os_x.n2p(t) + UP * f(t) * Y_SKALA

        parabola = ParametricFunction(
            punkt, t_range=[-3, 9], color=FIOLET, stroke_width=5,
        )
        rysunek = VGroup(os_x, znacznik_m1, znacznik_7, etykieta_m1, etykieta_7)

        self.play(
            Transform(s18, s18_gora.copy()),
            run_time=1.0,
        )
        self.remove(s18)
        self.add(s18_gora)
        self.play(Create(os_x), run_time=0.8)
        self.play(
            FadeIn(znacznik_m1, etykieta_m1),
            FadeIn(znacznik_7, etykieta_7),
            run_time=0.6,
        )
        self.play(Create(parabola), run_time=1.4)
        self.zakoncz(s18_gora, rysunek, parabola,
                     pomin=[s18_gora, parabola, *rysunek])

        # ================================================================
        # KROK 20. Fragment paraboli pod osią i odcinek na osi zapalają
        # się na zielono, z pełnymi kropkami na końcach (przedział domknięty).
        # ================================================================
        self.next_section("krok20")
        fragment = ParametricFunction(
            punkt, t_range=[-1, 7], color=ZIELONY, stroke_width=7,
        )
        odcinek = Line(os_x.n2p(-1), os_x.n2p(7), color=ZIELONY, stroke_width=7)
        kropka_l = Dot(os_x.n2p(-1), radius=0.09, color=ZIELONY)
        kropka_p = Dot(os_x.n2p(7), radius=0.09, color=ZIELONY)
        self.play(Create(fragment), run_time=1.0)
        self.play(
            Create(odcinek), FadeIn(kropka_l), FadeIn(kropka_p),
            run_time=0.8,
        )
        self.wait(0.35)
        self.play(fragment.animate.set_color(BLACK), run_time=0.4)
        self.remove(fragment)
        # Fragment paraboli zgasł (posłużył jako wskazówka „tu jest pod
        # osią"). Odcinek na osi gaśnie razem z resztą sceny w zakoncz, bo
        # ostatnia klatka kroku ma być czarna, tak jak we wszystkich innych
        # krokach: krok 21 zaczyna od czarnego odcinka i dopiero go zamienia
        # w zapis przedziału.
        self.zakoncz(s18_gora, rysunek, parabola, odcinek, kropka_l, kropka_p,
                     pomin=[s18_gora, parabola, *rysunek])

        # ================================================================
        # KROK 21. Odcinek zamienia się w zapis x nalezy do <-1, 7>.
        # Nawiasy kątowe i liczby wynikowe zostają czarne (wynik bez koloru).
        # ================================================================
        self.next_section("krok21")
        wynik = MathTex(r"x \in \langle -1,\ 7\rangle", color=BLACK, font_size=90)
        wynik.move_to(DOWN * 2.7)
        self.play(
            ReplacementTransform(VGroup(odcinek, kropka_l, kropka_p), wynik),
            run_time=1.2,
        )
        self.remove(odcinek, kropka_l, kropka_p)
        self.zakoncz(s18_gora, rysunek, parabola, wynik,
                     pomin=[s18_gora, parabola, wynik, *rysunek])
