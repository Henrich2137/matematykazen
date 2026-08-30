from manim import *

# Zadanie 16 (zamkniete, 1 pkt). Ciag geometryczny, a_2 = 1/6, a_3 = 1/9,
# szukamy a_5. Wynik 4/81, czyli odpowiedz C.
#
# Projekt: issues/projekt-zad15-zad16-2024-grudzien.md. Szesnascie krokow, jeden
# do jednego z szesnastoma linijkami w solutionText.
#
# Piaty wyraz liczymy PO KOLEI: najpierw q, potem a_4, potem a_5. Krotsza droga
# a_5 = a_3 * q^2 wymaga wiedzy, skad bierze sie wykladnik 2, a to jest dokladnie
# ta wiedza, ktorej tu brakuje. Mnozenie przez q dwa razy pokazuje sama definicje
# ciagu geometrycznego w dzialaniu.
#
# Dystraktor B to 2/27, czyli CZWARTY wyraz: kto pomnozy przez q tylko raz,
# trafia w podana odpowiedz. Dlatego kazdy wynik posredni jest podpisany swoja
# nazwa i odkladany do pasa na gorze, a na dole przez caly film stoi cel
# "a_5 = ?". W ostatniej klatce widac obok siebie a_4 i a_5.
#
# Wzoru [8.4] z tablicy tu nie ma i to jest swiadome: a_n = a_1 * q^(n-1) wymaga
# a_1, ktorego zadanie nie podaje. Definicji ilorazu tablica nie podaje wcale.
#
# Uklad kadru: pas danych i wynikow na gorze (rosnie w miare liczenia), rachunek
# na srodku, cel i werdykt na dole. Werdykt czarny (COLORS.md).
#
# Render: manim --save_sections solutionZad16.py Zad16  (albo tools/wgraj-kroki.sh 16)

ZIELONY = "#2e7d32"
SZARY = "#888888"

PAS_Y = 2.70
RACHUNEK_Y = 0.10
CEL_Y = -2.35
WERDYKT_Y = -2.35
# Kolejnosc pasa (Henrich, 2026-08-30): najpierw wyrazy ciagu po numerach
# (a_2, a_3, a_4), a dopiero na koncu iloraz q, odsuniety wieksza przerwa,
# bo nie jest wyrazem ciagu. Przedtem q stalo miedzy a_3 i a_4.
SLOTY = [-5.30, -2.35, 0.60, 4.75]
POSTOJ = 0.25


class Zad16(Scene):

    # ------------------------------------------------------------------
    # Klocki
    # ------------------------------------------------------------------
    def stan(self, *args, rozmiar=82):
        m = MathTex(*args)
        m.set_color(BLACK)
        m.font_size = rozmiar
        return m

    def kreska(self, szer):
        return Line(LEFT * szer / 2, RIGHT * szer / 2, color=BLACK, stroke_width=4)

    def ulamek_m(self, g, d, szer=None, buff=0.14):
        """Ulamek z gotowych mobiektow: (licznik, kreska, mianownik).

        Skladany recznie, a nie przez \\dfrac, bo tylko wtedy jest uchwyt do
        pojedynczej liczby w liczniku i liczba moze przyleciec z pasa na swoje
        miejsce (README, p. 37). Ten sam klocek sklada tez ulamek pietrowy:
        licznikiem bywa caly mniejszy ulamek.
        """
        s = szer if szer is not None else max(g.width, d.width) + 0.26
        k = self.kreska(s)
        g.next_to(k, UP, buff=buff)
        d.next_to(k, DOWN, buff=buff)
        return VGroup(g, k, d)

    def ulamek(self, gora, dol, rozmiar=64, szer=None, buff=0.14):
        return self.ulamek_m(self.stan(*gora, rozmiar=rozmiar),
                             self.stan(*dol, rozmiar=rozmiar), szer, buff)

    def linia(self, *czesci, buff=0.26):
        for i in range(1, len(czesci)):
            czesci[i].next_to(czesci[i - 1], RIGHT, buff=buff)
        return VGroup(*czesci)

    def wpis_pasa(self, etykieta, gora, dol, slot):
        """Jedna pozycja pasa: podpis w rodzaju "a_2 =" i ulamek obok niego."""
        e = self.stan(etykieta, "=", rozmiar=54)
        u = self.ulamek(gora, dol, rozmiar=48)
        g = self.linia(e, u, buff=0.20)
        g.move_to([SLOTY[slot], PAS_Y, 0])
        return g

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
        # DANE: najpierw duze na srodku, potem maly wpis w pasie
        # ================================================================
        d2_e = self.stan("a_{2}", "=", rozmiar=82)
        d2_u = self.ulamek(("1",), ("6",), rozmiar=64)
        d2 = self.linia(d2_e, d2_u)
        d3_e = self.stan("a_{3}", "=", rozmiar=82)
        d3_u = self.ulamek(("1",), ("9",), rozmiar=64)
        d3 = self.linia(d3_e, d3_u)
        d2.move_to([-2.3, 0.55, 0])
        d3.move_to([2.3, 0.55, 0])

        pas2 = self.wpis_pasa("a_{2}", ("1",), ("6",), 0)
        pas3 = self.wpis_pasa("a_{3}", ("1",), ("9",), 1)
        pas4 = self.wpis_pasa("a_{4}", ("2",), ("27",), 2)
        pasq = self.wpis_pasa("q", ("2",), ("3",), 3)

        # Cel stoi na dole przez caly film: pytanie jest o a_5, nie o a_4.
        cel_e = self.stan("a_{5}", "=", rozmiar=54)
        cel_q = self.stan("?", rozmiar=54)
        cel = self.linia(cel_e, cel_q, buff=0.22)
        cel.move_to([0, CEL_Y, 0])

        werdykt = Text("Odpowiedź C", font_size=40, color=BLACK)
        werdykt.move_to([0, WERDYKT_Y, 0])

        # ================================================================
        # KROK 2: strzalka "razy q" miedzy dwoma danymi wyrazami
        # ================================================================
        strzalka = CurvedArrow(
            pas2.get_bottom() + DOWN * 0.32 + RIGHT * 0.25,
            pas3.get_bottom() + DOWN * 0.32 + LEFT * 0.25,
            angle=-PI / 2.6, color=BLACK, stroke_width=3, tip_length=0.18)
        podpis = self.stan(r"\cdot", "q", rozmiar=56)
        podpis.next_to(strzalka, DOWN, buff=0.10)

        # ================================================================
        # STANY RACHUNKU
        # ================================================================
        L2 = self.stan("q", "=")
        F2 = self.ulamek(("a_{3}",), ("a_{2}",), rozmiar=64, szer=1.35)
        s2 = self.linia(L2, F2)

        L3 = self.stan("q", "=")
        F3 = self.ulamek_m(self.ulamek(("1",), ("9",), rozmiar=52),
                           self.ulamek(("1",), ("6",), rozmiar=52),
                           szer=1.45, buff=0.18)
        s3 = self.linia(L3, F3)

        L4 = self.stan("q", "=")
        A4 = self.ulamek(("1",), ("9",), rozmiar=64)
        D4 = self.stan(":")
        B4 = self.ulamek(("1",), ("6",), rozmiar=64)
        s4 = self.linia(L4, A4, D4, B4)

        L5 = self.stan("q", "=")
        A5 = self.ulamek(("1",), ("9",), rozmiar=64)
        D5 = self.stan(r"\cdot")
        B5 = self.ulamek(("6",), ("1",), rozmiar=64)
        s5 = self.linia(L5, A5, D5, B5)

        L6 = self.stan("q", "=")
        F6 = self.ulamek(("1", r"\cdot", "6"), ("9", r"\cdot", "1"),
                         rozmiar=64, szer=2.05)
        s6 = self.linia(L6, F6)

        L7 = self.stan("q", "=")
        F7 = self.ulamek(("6",), ("9",), rozmiar=64)
        s7 = self.linia(L7, F7)

        L8 = self.stan("q", "=")
        F8 = self.ulamek(("2",), ("3",), rozmiar=64)
        s8 = self.linia(L8, F8)

        L9 = self.stan("a_{4}", "=")
        P9a = self.stan("a_{3}")
        P9b = self.stan(r"\cdot")
        P9c = self.stan("q")
        s9 = self.linia(L9, P9a, P9b, P9c, buff=0.24)

        L10 = self.stan("a_{4}", "=")
        A10 = self.ulamek(("1",), ("9",), rozmiar=64)
        D10 = self.stan(r"\cdot")
        B10 = self.ulamek(("2",), ("3",), rozmiar=64)
        s10 = self.linia(L10, A10, D10, B10)

        L11 = self.stan("a_{4}", "=")
        F11 = self.ulamek(("1", r"\cdot", "2"), ("9", r"\cdot", "3"),
                          rozmiar=64, szer=2.05)
        s11 = self.linia(L11, F11)

        L12 = self.stan("a_{4}", "=")
        F12 = self.ulamek(("2",), ("27",), rozmiar=64)
        s12 = self.linia(L12, F12)

        L13 = self.stan("a_{5}", "=")
        P13a = self.stan("a_{4}")
        P13b = self.stan(r"\cdot")
        P13c = self.stan("q")
        s13 = self.linia(L13, P13a, P13b, P13c, buff=0.24)

        L14 = self.stan("a_{5}", "=")
        A14 = self.ulamek(("2",), ("27",), rozmiar=64)
        D14 = self.stan(r"\cdot")
        B14 = self.ulamek(("2",), ("3",), rozmiar=64)
        s14 = self.linia(L14, A14, D14, B14)

        L15 = self.stan("a_{5}", "=")
        F15 = self.ulamek(("2", r"\cdot", "2"), ("27", r"\cdot", "3"),
                          rozmiar=64, szer=2.45)
        s15 = self.linia(L15, F15)

        L16 = self.stan("a_{5}", "=")
        F16 = self.ulamek(("4",), ("81",), rozmiar=64)
        s16 = self.linia(L16, F16)

        stany = [s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16]
        wsp = min(1.0, POLE / max(m.width for m in stany))
        for m in stany:
            m.scale(wsp)
            m.move_to([0, RACHUNEK_Y, 0])

        # Rachunek pomocniczy do kroku 8: skracanie przez 3. Mniejszym pismem,
        # bo to praca na boku, i znika przed koncem kroku (README, p. 29 i 30).
        pom1 = self.stan("6", ":", "3", "=", "2", rozmiar=46)
        pom2 = self.stan("9", ":", "3", "=", "3", rozmiar=46)
        pom = VGroup(pom1, pom2).arrange(DOWN, buff=0.34, aligned_edge=LEFT)
        pom.set_color(SZARY)
        pom.move_to([3.4, RACHUNEK_Y, 0])

        # ================================================================
        # KROK 1. Dane z tresci zadania i cel na dole. Bez koloru.
        # ================================================================
        self.next_section("krok1")
        self.play(Write(d2), Write(d3), run_time=1.7)
        self.play(FadeIn(cel, shift=UP * 0.2), run_time=0.8)
        self.zakoncz(d2, d3, cel)

        # ================================================================
        # KROK 2. Kazdy nastepny wyraz to poprzedni razy q, wiec q to a_3
        # podzielone przez a_2. Litera q z podpisu strzalki jedzie na miejsce
        # lewej strony, a nie pojawia sie znikad.
        # ================================================================
        self.next_section("krok2")
        self.play(ReplacementTransform(d2, pas2),
                  ReplacementTransform(d3, pas3), run_time=1.1)
        self.play(Create(strzalka), FadeIn(podpis), run_time=0.9)
        self.wait(0.45)
        L2[0].set_color(ZIELONY)
        # Sama litera q z podpisu strzalki jedzie w dol i staje sie lewa strona
        # rownania. Do 2026-08-30 lecila tu KOPIA, a oryginal gasl w tym samym
        # czasie: przez pol sekundy w kadrze stalo q na q i wygladalo to jak
        # blad renderu (uwaga Henricha o „strzalce q").
        self.play(
            FadeOut(strzalka),
            FadeOut(podpis[0], scale=0.4),
            ReplacementTransform(podpis[1], L2[0]),
            FadeIn(L2[1]), FadeIn(F2[1]),
            TransformFromCopy(pas3[0][0], F2[0]),
            TransformFromCopy(pas2[0][0], F2[2]),
            run_time=1.4, path_arc=-PI / 3,
        )
        self.zakoncz(s2, pas2, pas3, cel)

        # ================================================================
        # KROK 3. Podstawienie: litery zamieniaja sie w ulamki, ktore
        # PRZYLATUJA z pasa.
        # ================================================================
        self.next_section("krok3")
        u3 = pas3[1].copy()
        u2 = pas2[1].copy()
        self.add(u3, u2)
        F3[0].set_color(ZIELONY)
        F3[2].set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(L2[i], L3[i]) for i in range(2)],
            ReplacementTransform(F2[1], F3[1]),
            FadeOut(F2[0], scale=0.4), FadeOut(F2[2], scale=0.4),
            Transform(u3, F3[0]), Transform(u2, F3[2]),
            run_time=1.5, path_arc=-PI / 6,
        )
        self.zakoncz(s3, pas2, pas3, cel)

        # ================================================================
        # KROK 4. Kreska ulamka znaczy dzielenie: duza kreska zamienia sie
        # w dwukropek, a oba ulamki zjezdzaja obok siebie.
        # ================================================================
        self.next_section("krok4")
        # Zielona jest i duza kreska, i dwukropek, w ktory sie zamienia: to
        # jedyny ruch tego kroku, a sam dwukropek jest za maly, zeby go zauwazyc.
        self.zapal(F3[1])
        D4.set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(L3[i], L4[i]) for i in range(2)],
            ReplacementTransform(F3[0], A4),
            ReplacementTransform(F3[2], B4),
            ReplacementTransform(F3[1], D4),
            run_time=1.5,
        )
        self.zakoncz(s4, pas2, pas3, cel)

        # ================================================================
        # KROK 5. Dzielenie przez ulamek to mnozenie przez odwrotnosc:
        # dwukropek zamienia sie w kropke, a szostka z jedynka zamieniaja
        # sie miejscami, kazda swoim lukiem.
        # ================================================================
        self.next_section("krok5")
        D5.set_color(ZIELONY)
        B5[0].set_color(ZIELONY)
        B5[2].set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(L4[i], L5[i]) for i in range(2)],
            *[ReplacementTransform(A4[i], A5[i]) for i in range(3)],
            ReplacementTransform(D4, D5),
            ReplacementTransform(B4[1], B5[1]),
            run_time=1.0,
        )
        self.play(
            ReplacementTransform(B4[0], B5[2]),
            ReplacementTransform(B4[2], B5[0]),
            run_time=1.2, path_arc=PI,
        )
        self.zakoncz(s5, pas2, pas3, cel)

        # ================================================================
        # KROK 6. Licznik mnozymy przez licznik, mianownik przez mianownik.
        # Zielona jest tylko kropka w mianowniku, bo jej wczesniej nie bylo
        # (README, p. 21). Ta z licznika przyleciala ze srodka.
        # ================================================================
        self.next_section("krok6")
        F6[2][1].set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(L5[i], L6[i]) for i in range(2)],
            ReplacementTransform(A5[0], F6[0][0]),
            ReplacementTransform(D5, F6[0][1]),
            ReplacementTransform(B5[0], F6[0][2]),
            ReplacementTransform(A5[2], F6[2][0]),
            ReplacementTransform(B5[2], F6[2][2]),
            FadeIn(F6[2][1]),
            ReplacementTransform(A5[1], F6[1]),
            FadeOut(B5[1], target_position=F6[1].get_center(), scale=0.4),
            run_time=1.6,
        )
        self.zakoncz(s6, pas2, pas3, cel)

        # ================================================================
        # KROK 7. 1 * 6 = 6 oraz 9 * 1 = 9.
        # ================================================================
        self.next_section("krok7")
        F7[0][0].set_color(ZIELONY)
        F7[2][0].set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(L6[i], L7[i]) for i in range(2)],
            ReplacementTransform(F6[1], F7[1]),
            *[FadeOut(F6[0][i], target_position=F7[0][0].get_center(),
                      scale=0.4) for i in (0, 1)],
            ReplacementTransform(F6[0][2], F7[0][0]),
            ReplacementTransform(F6[2][0], F7[2][0]),
            *[FadeOut(F6[2][i], target_position=F7[2][0].get_center(),
                      scale=0.4) for i in (1, 2)],
            run_time=1.4,
        )
        self.zakoncz(s7, pas2, pas3, cel)

        # ================================================================
        # KROK 8. Skracamy przez 3. Sam rachunek stoi z boku, mniejszym
        # pismem, i znika przed koncem kroku.
        # ================================================================
        self.next_section("krok8")
        self.play(FadeIn(pom, shift=LEFT * 0.2), run_time=0.8)
        self.wait(0.4)
        F8[0][0].set_color(ZIELONY)
        F8[2][0].set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(L7[i], L8[i]) for i in range(2)],
            ReplacementTransform(F7[1], F8[1]),
            ReplacementTransform(F7[0][0], F8[0][0]),
            ReplacementTransform(F7[2][0], F8[2][0]),
            run_time=1.3,
        )
        self.play(FadeOut(pom, shift=RIGHT * 0.2), run_time=0.6)
        self.zakoncz(s8, pas2, pas3, cel)

        # ================================================================
        # KROK 9. Iloraz odkladamy do pasa i piszemy plan na czwarty wyraz.
        # Bez koloru: nic sie nie przelicza.
        # ================================================================
        self.next_section("krok9")
        self.play(ReplacementTransform(s8, pasq), run_time=1.1)
        self.play(FadeIn(s9, shift=UP * 0.2), run_time=0.9)
        self.zakoncz(s9, pas2, pas3, pasq, cel)

        # ================================================================
        # KROK 10. Podstawienie: a_3 i q zamieniaja sie w ulamki z pasa.
        # ================================================================
        self.next_section("krok10")
        u3b = pas3[1].copy()
        uq = pasq[1].copy()
        self.add(u3b, uq)
        A10.set_color(ZIELONY)
        B10.set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(L9[i], L10[i]) for i in range(2)],
            ReplacementTransform(P9b, D10),
            FadeOut(P9a, scale=0.4), FadeOut(P9c, scale=0.4),
            Transform(u3b, A10), Transform(uq, B10),
            run_time=1.5, path_arc=-PI / 6,
        )
        self.zakoncz(s10, pas2, pas3, pasq, cel)

        # ================================================================
        # KROK 11. Mnozenie ulamkow, ten sam ruch co w kroku 6.
        # ================================================================
        self.next_section("krok11")
        F11[2][1].set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(L10[i], L11[i]) for i in range(2)],
            ReplacementTransform(A10[0], F11[0][0]),
            ReplacementTransform(D10, F11[0][1]),
            ReplacementTransform(B10[0], F11[0][2]),
            ReplacementTransform(A10[2], F11[2][0]),
            ReplacementTransform(B10[2], F11[2][2]),
            FadeIn(F11[2][1]),
            ReplacementTransform(A10[1], F11[1]),
            FadeOut(B10[1], target_position=F11[1].get_center(), scale=0.4),
            run_time=1.6,
        )
        self.zakoncz(s11, pas2, pas3, pasq, cel)

        # ================================================================
        # KROK 12. 1 * 2 = 2 oraz 9 * 3 = 27.
        # ================================================================
        self.next_section("krok12")
        F12[0][0].set_color(ZIELONY)
        F12[2][0].set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(L11[i], L12[i]) for i in range(2)],
            ReplacementTransform(F11[1], F12[1]),
            *[FadeOut(F11[0][i], target_position=F12[0][0].get_center(),
                      scale=0.4) for i in (0, 1)],
            ReplacementTransform(F11[0][2], F12[0][0]),
            ReplacementTransform(F11[2][0], F12[2][0]),
            *[FadeOut(F11[2][i], target_position=F12[2][0].get_center(),
                      scale=0.4) for i in (1, 2)],
            run_time=1.4,
        )
        self.zakoncz(s12, pas2, pas3, pasq, cel)

        # ================================================================
        # KROK 13. Czwarty wyraz odkladamy do pasa. To dopiero a_4, a pytanie
        # na dole caly czas mowi o a_5.
        # ================================================================
        self.next_section("krok13")
        self.play(ReplacementTransform(s12, pas4), run_time=1.1)
        self.play(FadeIn(s13, shift=UP * 0.2), run_time=0.9)
        self.zakoncz(s13, pas2, pas3, pasq, pas4, cel)

        # ================================================================
        # KROK 14. Podstawienie: a_4 i q zamieniaja sie w ulamki z pasa.
        # ================================================================
        self.next_section("krok14")
        u4 = pas4[1].copy()
        uq2 = pasq[1].copy()
        self.add(u4, uq2)
        A14.set_color(ZIELONY)
        B14.set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(L13[i], L14[i]) for i in range(2)],
            ReplacementTransform(P13b, D14),
            FadeOut(P13a, scale=0.4), FadeOut(P13c, scale=0.4),
            Transform(u4, A14), Transform(uq2, B14),
            run_time=1.5, path_arc=-PI / 6,
        )
        self.zakoncz(s14, pas2, pas3, pasq, pas4, cel)

        # ================================================================
        # KROK 15. Mnozenie ulamkow, trzeci raz ten sam ruch.
        # ================================================================
        self.next_section("krok15")
        F15[2][1].set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(L14[i], L15[i]) for i in range(2)],
            ReplacementTransform(A14[0], F15[0][0]),
            ReplacementTransform(D14, F15[0][1]),
            ReplacementTransform(B14[0], F15[0][2]),
            ReplacementTransform(A14[2], F15[2][0]),
            ReplacementTransform(B14[2], F15[2][2]),
            FadeIn(F15[2][1]),
            ReplacementTransform(A14[1], F15[1]),
            FadeOut(B14[1], target_position=F15[1].get_center(), scale=0.4),
            run_time=1.6,
        )
        self.zakoncz(s15, pas2, pas3, pasq, pas4, cel)

        # ================================================================
        # KROK 16. 2 * 2 = 4 oraz 27 * 3 = 81. Pytanie z dolu znika, bo mamy
        # odpowiedz, a w jego miejsce wchodzi werdykt.
        # ================================================================
        self.next_section("krok16")
        F16[0][0].set_color(ZIELONY)
        F16[2][0].set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(L15[i], L16[i]) for i in range(2)],
            ReplacementTransform(F15[1], F16[1]),
            *[FadeOut(F15[0][i], target_position=F16[0][0].get_center(),
                      scale=0.4) for i in (0, 1)],
            ReplacementTransform(F15[0][2], F16[0][0]),
            ReplacementTransform(F15[2][0], F16[2][0]),
            *[FadeOut(F15[2][i], target_position=F16[2][0].get_center(),
                      scale=0.4) for i in (1, 2)],
            run_time=1.4,
        )
        self.play(FadeOut(cel, shift=DOWN * 0.2), run_time=0.6)
        self.play(FadeIn(werdykt, shift=UP * 0.2), run_time=0.7)
        # Gaszenie idzie przez zakoncz, a nie recznie po dwoch glifach: w kadrze
        # leza jeszcze KOPIE celu (ReplacementTransform na kilka zrodel), wiec
        # recznie zgaszone zostawialo zielona osiemdziesiatke jedynke na
        # ostatniej klatce (README, "Transform zostawia w kadrze obiekt zrodlowy").
        self.zakoncz(s16, pas2, pas3, pasq, pas4, werdykt)
