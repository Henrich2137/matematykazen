from manim import *

# Zadanie 15 (zamkniete, 1 pkt). Ciag (5m, 4+2m, m) jest arytmetyczny dla m = 4,
# czyli odpowiedz D.
#
# Projekt: issues/projekt-zad15-zad16-2024-grudzien.md. Dziesiec krokow, jeden
# do jednego z dziesiecioma linijkami w solutionText.
#
# Warunek bierzemy z tablicy, wzor [8.3] ze strony 9: srodkowy wyraz jest
# srednia sasiadow. Wchodzi jednak dopiero PO przykladzie na liczbach (2, 5, 8),
# bo uczen celujacy w 30% blokuje sie na literze, nie na rachunku.
#
# Dwa ostatnie kroki to sprawdzenie i one niosa cala dydaktyke tego zadania:
# po podstawieniu m = 4 ciag wychodzi 20, 12, 4, czyli MALEJACY, a mimo to
# arytmetyczny, bo obie roznice sa rowne -8. Tak rozbrajamy mylenie ciagu
# arytmetycznego z geometrycznym, bez zdania "uczniowie czesto myla".
#
# Uklad kadru: pas z ciagiem na gorze (zostaje do konca filmu, bo z niego
# przylatuja wyrazenia i do niego wracaja liczby), rachunek na srodku, roznice
# pod rachunkiem, werdykt na dole. Werdykt czarny (COLORS.md: to odpowiedz
# ucznia, nie ocena poprawnosci).
#
# Render: manim --save_sections solutionZad15.py Zad15  (albo tools/wgraj-kroki.sh 15)

ZIELONY = "#2e7d32"
SZARY = "#888888"

PAS_Y = 2.60
RACHUNEK_Y = 0.35
ROZNICE_Y = -1.45
WERDYKT_Y = -2.95
POSTOJ = 0.25


class Zad15(Scene):

    # ------------------------------------------------------------------
    # Klocki
    # ------------------------------------------------------------------
    def stan(self, *args, rozmiar=82):
        m = MathTex(*args)
        m.set_color(BLACK)
        m.font_size = rozmiar
        return m

    def ulamek(self, gora, dol, rozmiar=64, szer=None):
        """Ulamek zlozony recznie (licznik, kreska, mianownik).

        Wzorzec z solutionZad9.py i solutionZad14.py: \\dfrac w jednym MathTeksie
        nie daje uchwytu do pojedynczej liczby w liczniku, a bez tego liczba nie
        moze przyleciec z pasa na swoje miejsce.
        """
        g = self.stan(*gora, rozmiar=rozmiar)
        d = self.stan(*dol, rozmiar=rozmiar)
        s = szer if szer is not None else max(g.width, d.width) + 0.24
        kreska = Line(LEFT * s / 2, RIGHT * s / 2, color=BLACK, stroke_width=4)
        g.next_to(kreska, UP, buff=0.14)
        d.next_to(kreska, DOWN, buff=0.14)
        return VGroup(g, kreska, d)

    def rownanie(self, lewa, prawa, buff=0.26):
        g = VGroup(lewa, prawa)
        prawa.next_to(lewa, RIGHT, buff=buff)
        return g

    def ciag_grupa(self, w1, w2, w3, rozmiar=82, podpisy=True):
        """(5m, 4+2m, m) z podpisami a_1, a_2, a_3 nad wyrazami.

        Zwraca (grupa, [trzy wyrazy], [trzy podpisy], [nawiasy i przecinki]),
        zeby kazda czesc dala sie ruszyc osobno: przecinki i nawiasy tylko
        przesuwaja sie, a wyrazy zamieniaja sie w cos innego.
        """
        naw_l = self.stan("(", rozmiar=rozmiar)
        a = self.stan(*w1, rozmiar=rozmiar)
        p1 = self.stan(",", rozmiar=rozmiar)
        b = self.stan(*w2, rozmiar=rozmiar)
        p2 = self.stan(",", rozmiar=rozmiar)
        c = self.stan(*w3, rozmiar=rozmiar)
        naw_p = self.stan(")", rozmiar=rozmiar)
        kolejnosc = [naw_l, a, p1, b, p2, c, naw_p]
        odstepy = [0.08, 0.04, 0.26, 0.04, 0.26, 0.08]
        for i in range(1, len(kolejnosc)):
            kolejnosc[i].next_to(kolejnosc[i - 1], RIGHT, buff=odstepy[i - 1])
            kolejnosc[i].align_to(kolejnosc[0], DOWN)
        wyrazy = [a, b, c]
        znaki = [naw_l, p1, p2, naw_p]
        etykiety = []
        if podpisy:
            for i, w in enumerate(wyrazy):
                e = MathTex("a_{%d}" % (i + 1), color=BLACK,
                            font_size=int(rozmiar * 0.78))
                e.next_to(w, UP, buff=0.26)
                etykiety.append(e)
        grupa = VGroup(*kolejnosc, *etykiety)
        return grupa, wyrazy, etykiety, znaki

    def zapal(self, *mobiekty, czas=0.4):
        if mobiekty:
            self.play(*[m.animate.set_color(ZIELONY) for m in mobiekty],
                      run_time=czas)

    def zakoncz(self, *czysty, pomin=(), czas=0.4, postoj=POSTOJ):
        """Gaszenie kolorow, podmiana na czysty stan, dopiero potem przytrzymanie."""
        self.wait(0.3)
        gasnie = [m for m in self.mobjects if not any(m is p for p in pomin)]
        if gasnie:
            self.play(*[m.animate.set_color(BLACK) for m in gasnie], run_time=czas)
        self.clear()
        for m in czysty:
            if not any(m is p for p in pomin):
                m.set_color(BLACK)
        self.add(*czysty)
        self.wait(postoj)

    # ------------------------------------------------------------------
    def construct(self):
        POLE = config.frame_width * 0.85

        # ================================================================
        # PAS: ciag z treci zadania, najpierw duzy na srodku, potem maly na gorze
        # ================================================================
        duzy, duzy_w, duzy_e, duzy_z = self.ciag_grupa(
            ("5", "m"), ("4", "+", "2", "m"), ("m",), rozmiar=86)
        duzy.move_to([0, 0.15, 0])

        pas, pas_w, pas_e, pas_z = self.ciag_grupa(
            ("5", "m"), ("4", "+", "2", "m"), ("m",), rozmiar=60)
        pas.move_to([0, PAS_Y, 0])

        # Pas po sprawdzeniu: te same miejsca, ale policzone liczby.
        pasl, pasl_w, pasl_e, pasl_z = self.ciag_grupa(
            ("20",), ("12",), ("4",), rozmiar=60)
        pasl.move_to([0, PAS_Y, 0])

        # ================================================================
        # KROK 2: przyklad na liczbach, a pod nim wzor z tablicy
        # ================================================================
        prz_ciag = self.stan("2", ",", "5", ",", "8", rozmiar=76)
        prz_lewa = self.ulamek(("2", "+", "8"), ("2",), rozmiar=56)
        prz_rown = self.stan("=", rozmiar=56)
        prz_wynik = self.stan("5", rozmiar=56)
        prz_rown.next_to(prz_lewa, RIGHT, buff=0.24)
        prz_wynik.next_to(prz_rown, RIGHT, buff=0.24)
        prz_rachunek = VGroup(prz_lewa, prz_rown, prz_wynik)
        prz_ciag.move_to([0, 1.25, 0])
        prz_rachunek.move_to([0, -0.35, 0])

        # ================================================================
        # STANY RACHUNKU
        # ================================================================
        # s2: wzor z tablicy w postaci literowej.
        s2_lewa = self.stan("a_{2}", "=", rozmiar=82)
        s2_ul = self.ulamek(("a_{1}", "+", "a_{3}"), ("2",), rozmiar=68)
        s2 = self.rownanie(s2_lewa, s2_ul)

        # s3: po podstawieniu.
        s3_lewa = self.stan("4", "+", "2", "m", "=", rozmiar=82)
        s3_ul = self.ulamek(("5", "m", "+", "m"), ("2",), rozmiar=68, szer=2.1)
        s3 = self.rownanie(s3_lewa, s3_ul)

        # s3b: z dopisana jedynka przy samotnym m (ogniwo: m to inaczej 1m).
        s3b_lewa = self.stan("4", "+", "2", "m", "=", rozmiar=82)
        s3b_ul = self.ulamek(("5", "m", "+", "1", "m"), ("2",), rozmiar=68, szer=2.1)
        s3b = self.rownanie(s3b_lewa, s3b_ul)

        # s4: licznik policzony.
        s4_lewa = self.stan("4", "+", "2", "m", "=", rozmiar=82)
        s4_ul = self.ulamek(("6", "m"), ("2",), rozmiar=68, szer=1.25)
        s4 = self.rownanie(s4_lewa, s4_ul)

        s5 = self.stan("4", "+", "2", "m", "=", "3", "m", rozmiar=82)
        s6 = self.stan("4", "=", "3", "m", "-", "2", "m", rozmiar=82)
        s6b = self.stan("4", "=", "1", "m", rozmiar=82)
        s7 = self.stan("4", "=", "m", rozmiar=82)
        s8 = self.stan("m", "=", "4", rozmiar=82)

        stany = [s2, s3, s3b, s4, s5, s6, s6b, s7, s8]
        wsp = min(1.0, POLE / max(m.width for m in stany))
        for m in stany:
            m.scale(wsp)
            m.move_to([0, RACHUNEK_Y, 0])

        # Dopisek dzialania: szary, bo to zapowiedz, a nie zapis (README, p. 36).
        dopisek = MathTex(r"\big/ - 2m", color=SZARY, font_size=58)
        dopisek.next_to(s5, RIGHT, buff=0.85)

        # ================================================================
        # KROKI 9 i 10: sprawdzenie
        # ================================================================
        r1 = self.stan("12", "-", "20", "=", "-", "8", rozmiar=62)
        r2 = self.stan("4", "-", "12", "=", "-", "8", rozmiar=62)
        r1.move_to([-2.6, ROZNICE_Y, 0])
        r2.move_to([2.6, ROZNICE_Y, 0])

        werdykt = Text("Odpowiedź D", font_size=40, color=BLACK)
        werdykt.move_to([0, WERDYKT_Y, 0])

        # ================================================================
        # KROK 1. Nazywamy wyrazy. Bez koloru: nic sie nie liczy.
        # ================================================================
        self.next_section("krok1")
        self.play(Write(VGroup(*duzy_z, *duzy_w)), run_time=1.5)
        self.play(*[FadeIn(e, shift=DOWN * 0.15) for e in duzy_e], run_time=0.9)
        self.zakoncz(duzy)

        # ================================================================
        # KROK 2. Skad wzor: najpierw przyklad na liczbach, potem postac
        # literowa z tablicy. Zielone sa obie piatki, zeby bylo widac, ze
        # srodkowy wyraz i srednia skrajnych to ta sama liczba.
        # ================================================================
        self.next_section("krok2")
        self.play(ReplacementTransform(duzy, pas), run_time=1.1)
        self.play(FadeIn(prz_ciag, shift=DOWN * 0.2), run_time=0.8)
        self.play(FadeIn(prz_lewa), FadeIn(prz_rown), run_time=0.7)
        prz_wynik.set_color(ZIELONY)
        self.play(FadeIn(prz_wynik), prz_ciag[2].animate.set_color(ZIELONY),
                  run_time=0.7)
        self.wait(0.5)
        self.play(prz_wynik.animate.set_color(BLACK),
                  prz_ciag[2].animate.set_color(BLACK), run_time=0.35)
        self.play(FadeOut(prz_ciag, shift=UP * 0.2),
                  FadeOut(prz_rachunek, shift=UP * 0.2), run_time=0.7)
        self.play(FadeIn(s2, shift=DOWN * 0.2), run_time=0.9)
        self.zakoncz(s2, pas)

        # ================================================================
        # KROK 3. Podstawienie: kazda litera zamienia sie w wyrazenie, ktore
        # PRZYLATUJE z pasa (README, p. 37).
        # ================================================================
        self.next_section("krok3")
        kop_a2 = VGroup(*[m.copy() for m in pas_w[1]])
        kop_a1 = VGroup(*[m.copy() for m in pas_w[0]])
        kop_a3 = VGroup(*[m.copy() for m in pas_w[2]])
        self.add(kop_a2, kop_a1, kop_a3)
        cel_a2 = VGroup(*[s3_lewa[i] for i in range(4)])
        cel_a1 = VGroup(s3_ul[0][0], s3_ul[0][1])
        cel_a3 = VGroup(s3_ul[0][3])
        for c in (cel_a2, cel_a1, cel_a3):
            c.set_color(ZIELONY)
        self.play(
            FadeOut(s2_lewa[0], scale=0.4),
            ReplacementTransform(s2_lewa[1], s3_lewa[4]),
            ReplacementTransform(s2_ul[1], s3_ul[1]),
            ReplacementTransform(s2_ul[0][1], s3_ul[0][2]),
            ReplacementTransform(s2_ul[2], s3_ul[2]),
            FadeOut(s2_ul[0][0], scale=0.4),
            FadeOut(s2_ul[0][2], scale=0.4),
            Transform(kop_a2, cel_a2),
            Transform(kop_a1, cel_a1),
            Transform(kop_a3, cel_a3),
            run_time=1.6, path_arc=-PI / 6,
        )
        self.zakoncz(s3, pas)

        # ================================================================
        # KROK 4. Licznik. Najpierw przy samotnym m pojawia sie zielona
        # jedynka (m to inaczej 1m), dopiero potem 5m + 1m zwija sie w 6m.
        # ================================================================
        self.next_section("krok4")
        s3b_ul[0][3].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s3_lewa, s3b_lewa),
            ReplacementTransform(s3_ul[1], s3b_ul[1]),
            ReplacementTransform(s3_ul[2], s3b_ul[2]),
            *[ReplacementTransform(s3_ul[0][i], s3b_ul[0][i]) for i in (0, 1, 2)],
            ReplacementTransform(s3_ul[0][3], s3b_ul[0][4]),
            FadeIn(s3b_ul[0][3], shift=RIGHT * 0.2),
            run_time=1.2,
        )
        self.wait(0.4)
        s4_ul[0][0].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s3b_lewa, s4_lewa),
            ReplacementTransform(s3b_ul[1], s4_ul[1]),
            ReplacementTransform(s3b_ul[2], s4_ul[2]),
            ReplacementTransform(s3b_ul[0][0], s4_ul[0][0]),
            ReplacementTransform(s3b_ul[0][3], s4_ul[0][0].copy()),
            ReplacementTransform(s3b_ul[0][2], s4_ul[0][0].copy()),
            ReplacementTransform(s3b_ul[0][1], s4_ul[0][1]),
            ReplacementTransform(s3b_ul[0][4], s4_ul[0][1].copy()),
            run_time=1.3,
        )
        self.zakoncz(s4, pas)

        # ================================================================
        # KROK 5. Dzieli sie sama szostka: 6 : 2 = 3, litera zostaje.
        # ================================================================
        self.next_section("krok5")
        self.zapal(s4_ul[0][0], s4_ul[2][0])
        s5[5].set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(s4_lewa[i], s5[i]) for i in range(5)],
            ReplacementTransform(s4_ul[0][0], s5[5]),
            ReplacementTransform(s4_ul[2][0], s5[5].copy()),
            FadeOut(s4_ul[1], scale=0.4),
            ReplacementTransform(s4_ul[0][1], s5[6]),
            run_time=1.4,
        )
        self.zakoncz(s5, pas)

        # ================================================================
        # KROK 6. Przenosimy 2m na druga strone. Plus z lewej ZAMIENIA SIE
        # w minus po prawej (README, p. 15), a skladnik leci lukiem NAD
        # znakiem rownosci, nie przez niego (README, p. 27).
        # ================================================================
        self.next_section("krok6")
        self.play(FadeIn(dopisek, shift=LEFT * 0.2), run_time=0.6)
        self.zapal(s5[1], s5[2], s5[3])
        for i in (2, 3, 4):
            s6[i + 2 if i > 3 else i].set_color(ZIELONY)
        s6[4].set_color(ZIELONY)
        s6[5].set_color(ZIELONY)
        s6[6].set_color(ZIELONY)
        s6[2].set_color(BLACK)
        s6[3].set_color(BLACK)
        self.play(
            ReplacementTransform(s5[0], s6[0]),
            ReplacementTransform(s5[4], s6[1]),
            ReplacementTransform(s5[5], s6[2]),
            ReplacementTransform(s5[6], s6[3]),
            ReplacementTransform(s5[1], s6[4]),
            ReplacementTransform(s5[2], s6[5]),
            ReplacementTransform(s5[3], s6[6]),
            run_time=1.5, path_arc=-2 * PI / 3,
        )
        self.play(FadeOut(dopisek, shift=RIGHT * 0.2), run_time=0.5)
        self.zakoncz(s6, pas)

        # ================================================================
        # KROK 7. 3m - 2m = 1m, a 1m to po prostu m.
        # ================================================================
        self.next_section("krok7")
        self.zapal(s6[2], s6[5])
        s6b[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s6[0], s6b[0]),
            ReplacementTransform(s6[1], s6b[1]),
            ReplacementTransform(s6[2], s6b[2]),
            ReplacementTransform(s6[5], s6b[2].copy()),
            ReplacementTransform(s6[4], s6b[2].copy()),
            ReplacementTransform(s6[3], s6b[3]),
            ReplacementTransform(s6[6], s6b[3].copy()),
            run_time=1.4,
        )
        self.wait(0.4)
        self.play(
            ReplacementTransform(s6b[0], s7[0]),
            ReplacementTransform(s6b[1], s7[1]),
            FadeOut(s6b[2], scale=0.3),
            ReplacementTransform(s6b[3], s7[2]),
            run_time=1.0,
        )
        self.zakoncz(s7, pas)

        # ================================================================
        # KROK 8. Wynik zapisujemy z niewiadoma po lewej: strony zamieniaja
        # sie miejscami. Bez koloru, nic sie nie przelicza (README, p. 5).
        # ================================================================
        self.next_section("krok8")
        self.play(
            ReplacementTransform(s7[0], s8[2]),
            ReplacementTransform(s7[1], s8[1]),
            ReplacementTransform(s7[2], s8[0]),
            run_time=1.3, path_arc=PI / 2,
        )
        self.play(FadeIn(werdykt, shift=UP * 0.2), run_time=0.7)
        self.zakoncz(s8, pas, werdykt)

        # ================================================================
        # KROK 9. Sprawdzenie. Czworka z wyniku wchodzi do kazdego wyrazu,
        # a wyrazenia zamieniaja sie w liczby.
        # ================================================================
        self.next_section("krok9")
        kopie4 = [s8[2].copy() for _ in range(3)]
        self.add(*kopie4)
        for w in pasl_w:
            w.set_color(ZIELONY)
        # Czworki staja POD wyrazami i dopiero stamtad wchodza w miejsce
        # wyrazen: ladowanie wprost na wyrazie robi w polowie kroku klaks
        # z dwoch nalozonych zapisow.
        self.play(
            *[k.animate.move_to(c).shift(DOWN * 0.62).scale(0.6)
              for k, c in zip(kopie4, pasl_w)],
            run_time=1.0, path_arc=-PI / 4,
        )
        self.wait(0.35)
        self.play(
            *[FadeOut(k, scale=0.3) for k in kopie4],
            *[ReplacementTransform(a, b) for a, b in zip(pas_w, pasl_w)],
            *[ReplacementTransform(a, b) for a, b in zip(pas_z, pasl_z)],
            *[ReplacementTransform(a, b) for a, b in zip(pas_e, pasl_e)],
            run_time=1.3,
        )
        self.zakoncz(pasl, s8, werdykt)

        # ================================================================
        # KROK 10. Od kazdego wyrazu odejmujemy poprzedni. Liczby przylatuja
        # z pasa, wiec widac, ze to dokladnie te trzy wyrazy.
        # ================================================================
        self.next_section("krok10")
        k12 = pasl_w[1].copy()
        k20 = pasl_w[0].copy()
        k4 = pasl_w[2].copy()
        k12b = pasl_w[1].copy()
        self.add(k12, k20, k4, k12b)
        self.play(
            FadeIn(r1[1]), FadeIn(r1[3]), FadeIn(r2[1]), FadeIn(r2[3]),
            Transform(k12, r1[0].copy()),
            Transform(k20, r1[2].copy()),
            Transform(k4, r2[0].copy()),
            Transform(k12b, r2[2].copy()),
            run_time=1.4, path_arc=-PI / 5,
        )
        wynik1 = VGroup(r1[4], r1[5]).set_color(ZIELONY)
        wynik2 = VGroup(r2[4], r2[5]).set_color(ZIELONY)
        self.play(FadeIn(wynik1), FadeIn(wynik2), run_time=0.9)
        self.wait(0.4)
        self.play(wynik1.animate.set_color(BLACK),
                  wynik2.animate.set_color(BLACK), run_time=0.4)
        self.wait(POSTOJ)
