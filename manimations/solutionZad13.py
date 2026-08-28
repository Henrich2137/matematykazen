from manim import *

# Zadanie 13 (prawda/falsz, 1 pkt). f(x) = log_6 x. Zdanie 1: f(36) = 6 (FALSZ,
# bo f(36) = 2). Zdanie 2: f jest rosnaca (PRAWDA, bo podstawa 6 > 1).
#
# Projekt: issues/projekt-zad13-zad14-2024-grudzien.md. Siedem krokow, jeden do
# jednego z siedmioma linijkami w solutionText.
#
# Zadanie jest napisane pod jedna pomylke: w zdaniu 1 stoi liczba 6, czyli
# PODSTAWA logarytmu, a wynikiem jest WYKLADNIK. Dlatego krok 2 rozklada zapis
# na 6^c = 36, gdzie podstawa i wykladnik stoja w dwoch roznych miejscach,
# a zielone jest wylacznie szukane c.
#
# Uklad kadru: kroki 1 do 4 to sam rachunek na srodku. Krok 5 zwija go w liste
# trzech wartosci, krok 6 przesuwa liste w lewo i dokłada wykres po prawej.
# Werdykty obu zdan stoja na dole; litery P i F sa czarne, bo to odpowiedz
# ucznia, a nie ocena poprawnosci (COLORS.md).
#
# Wykres uzywa fioletu --accent-purple (#7a3fa8, rola "wykres funkcji jak
# w arkuszach CKE"). Os pozioma ma nierowne podzialki 1, 6, 36: to sa dokladnie
# te trzy argumenty, ktore policzylismy, a nie regularna siatka.
#
# Render: manim --save_sections solutionZad13.py Zad13  (albo tools/wgraj-kroki.sh 13)

ZIELONY = "#2e7d32"
FIOLET = "#7a3fa8"
SZARY_OSIE = "#666666"

RACHUNEK_Y = UP * 0.7
LISTA_X = -4.45
WYKRES_SRODEK = RIGHT * 2.75 + UP * 0.55
WERDYKT_Y = -2.95
POSTOJ = 0.45


class Zad13(Scene):

    def stan(self, *args, rozmiar=88):
        m = MathTex(*args)
        m.set_color(BLACK)
        m.font_size = rozmiar
        return m

    def werdykt(self, nr, litera, x):
        g = VGroup(
            Text(f"Zdanie {nr}:", font_size=32, color=BLACK),
            Text(litera, font_size=38, weight=BOLD, color=BLACK),
        ).arrange(RIGHT, buff=0.30)
        g.move_to([x, WERDYKT_Y, 0])
        return g

    def zapal(self, *mobiekty, czas=0.4):
        if mobiekty:
            self.play(*[m.animate.set_color(ZIELONY) for m in mobiekty], run_time=czas)

    def zakoncz(self, *czysty, pomin=(), czas=0.4, postoj=0.25):
        """Gaszenie kolorow, podmiana na czysty stan, dopiero potem przytrzymanie.

        Wzorzec z solutionZad9.py: `Transform` zostawia w kadrze obiekt zrodlowy,
        wiec zamiast zgadywac, co jeszcze trzyma kolor, gasimy wszystko i wstawiamy
        czysty nastepny stan.
        """
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

    def construct(self):
        # ================================================================
        # STANY RACHUNKU
        # ================================================================
        # `\log` daje trzy glify (l, o, g), `_{6}` jeden, wiec szostka spod
        # logarytmu ma wlasny uchwyt i moze dojechac na podstawe potegi.
        s0 = self.stan("f", "(", "x", ")", "=", r"\log", "_{6}", "x")
        s1 = self.stan("f", "(", "36", ")", "=", r"\log", "_{6}", "36")
        s2 = self.stan("6", "^{c}", "=", "36")
        s3 = self.stan("6", "^{2}", "=", "36")
        s4 = self.stan("f", "(", "36", ")", "=", "2")

        glowne = [s0, s1, s2, s3, s4]
        najszerszy = max(m.width for m in glowne)
        POLE = config.frame_width * 0.85
        wsp = min(1.0, POLE / najszerszy)
        for m in glowne:
            m.scale(wsp)
            m.move_to(RACHUNEK_Y)

        # ================================================================
        # LISTA TRZECH WARTOSCI (od kroku 5)
        # ================================================================
        # Lewa kolumna to potegi szostki, prawa to odczytane z nich wartosci
        # funkcji. Wiersz z 36 powstaje z rachunku, dwa gorne dochodza w kroku 5.
        pot = [self.stan("6", "^{0}", "=", "1", rozmiar=54),
               self.stan("6", "^{1}", "=", "6", rozmiar=54),
               self.stan("6", "^{2}", "=", "36", rozmiar=54)]
        war = [self.stan("f", "(", "1", ")", "=", "0", rozmiar=54),
               self.stan("f", "(", "6", ")", "=", "1", rozmiar=54),
               self.stan("f", "(", "36", ")", "=", "2", rozmiar=54)]

        WIERSZ_H = 1.02
        LISTA_GORA = 1.75
        KOL_POT = -2.15          # srodek kolumny poteg w kroku 5
        KOL_WAR = 0.95           # srodek kolumny wartosci w kroku 5
        for i in range(3):
            pot[i].move_to([KOL_POT, LISTA_GORA - i * WIERSZ_H, 0])
            war[i].move_to([KOL_WAR, LISTA_GORA - i * WIERSZ_H, 0])

        # Pozycje docelowe kolumny wartosci po przesunieciu w lewo (krok 6).
        war_cel = [w.copy().move_to([LISTA_X, LISTA_GORA - i * WIERSZ_H, 0])
                   for i, w in enumerate(war)]

        # ================================================================
        # WYKRES (od kroku 6)
        # ================================================================
        osie = Axes(
            # Os pionowa odsunieta od lewej krawedzi (x_range zaczyna sie
            # ponizej zera), zeby podpis "1" mial sie gdzie zmiescic: punkt
            # x = 1 lezy przy takiej skali tuz obok osi y.
            x_range=[-3, 41, 44],
            y_range=[-1, 2.6, 1],
            x_length=7.3,
            y_length=3.9,
            axis_config={
                "color": SZARY_OSIE,
                "stroke_width": 2.5,
                "include_ticks": False,
                "include_tip": True,
                "tip_width": 0.15,
                "tip_height": 0.15,
            },
        )
        osie.move_to(WYKRES_SRODEK)

        def p(x, y):
            return osie.c2p(x, y)

        # Podzialki tylko w trzech policzonych argumentach: to nie jest siatka,
        # tylko trzy miejsca, ktore uczen ma odnalezc na osi.
        znaczniki = VGroup()
        for x in (1, 6, 36):
            kreska = Line(p(x, 0) + DOWN * 0.09, p(x, 0) + UP * 0.09,
                          color=SZARY_OSIE, stroke_width=2.5)
            opis = MathTex(str(x), color=SZARY_OSIE, font_size=42)
            opis.next_to(p(x, 0), DOWN, buff=0.16)
            if x == 1:
                opis.shift(RIGHT * 0.10)
            znaczniki.add(kreska, opis)
        for y in (1, 2):
            kreska = Line(p(0, y) + LEFT * 0.09, p(0, y) + RIGHT * 0.09,
                          color=SZARY_OSIE, stroke_width=2.5)
            opis = MathTex(str(y), color=SZARY_OSIE, font_size=42)
            opis.next_to(p(0, y), LEFT, buff=0.16)
            znaczniki.add(kreska, opis)
        os_x_podpis = MathTex("x", color=SZARY_OSIE, font_size=38)
        os_x_podpis.next_to(p(41, 0), UP + RIGHT, buff=0.05)
        os_y_podpis = MathTex("y", color=SZARY_OSIE, font_size=38)
        os_y_podpis.next_to(p(0, 2.6), UP + LEFT, buff=0.05)
        znaczniki.add(os_x_podpis, os_y_podpis)

        import math

        krzywa = osie.plot(
            lambda x: math.log(x, 6),
            x_range=[0.25, 40.5, 0.12],
            color=FIOLET, stroke_width=6,
        )
        podpis_f = MathTex("y = f(x)", color=FIOLET, font_size=40)
        podpis_f.move_to(p(28, 0.75))

        punkty = [Dot(p(1, 0), radius=0.085, color=BLACK),
                  Dot(p(6, 1), radius=0.085, color=BLACK),
                  Dot(p(36, 2), radius=0.085, color=BLACK)]

        regula = self.stan("6", ">", "1", rozmiar=60)
        regula.move_to([WYKRES_SRODEK[0], -2.0, 0])

        werdykt1 = self.werdykt(1, "F", -4.05)
        werdykt2 = self.werdykt(2, "P", 1.85)

        # ================================================================
        # KROK 1. Podstawienie: w miejsce x wchodzi 36. Zielone sa obie
        # trzydziestki szostki, bo to one sa nowe.
        # ================================================================
        self.next_section("krok1")
        self.play(Write(s0), run_time=1.3)
        self.wait(0.35)
        self.zapal(s0[2], s0[7])
        s1[2].set_color(ZIELONY)
        s1[7].set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(s0[i], s1[i]) for i in range(8)],
            run_time=1.3,
        )
        self.zakoncz(s1)

        # ================================================================
        # KROK 2. Definicja logarytmu. Szostka spod log JEDZIE na podstawe
        # potegi (czarna, dalej ta sama szostka), 36 przejezdza na prawa
        # strone, a zielone c POJAWIA sie jako wykladnik.
        # ================================================================
        self.next_section("krok2")
        s2[1].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s1[6], s2[0]),
            ReplacementTransform(s1[4], s2[2]),
            ReplacementTransform(s1[7], s2[3]),
            FadeOut(s1[0], scale=0.4), FadeOut(s1[1], scale=0.4),
            FadeOut(s1[2], scale=0.4), FadeOut(s1[3], scale=0.4),
            FadeOut(s1[5], scale=0.4),
            run_time=1.5,
        )
        self.play(FadeIn(s2[1], shift=DOWN * 0.25), run_time=0.6)
        self.zakoncz(s2)

        # ================================================================
        # KROK 3. c zamienia sie w 2: szukamy potegi szostki rownej 36.
        # ================================================================
        self.next_section("krok3")
        self.zapal(s2[1])
        s3[1].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s2[0], s3[0]),
            ReplacementTransform(s2[1], s3[1]),
            ReplacementTransform(s2[2], s3[2]),
            ReplacementTransform(s2[3], s3[3]),
            run_time=1.2,
        )
        self.zakoncz(s3)

        # ================================================================
        # KROK 4. Wracamy do pytania: dwojka zjezdza z wykladnika na miejsce
        # wyniku, 36 wraca do nawiasu przy f. Bez koloru, to jest odczyt.
        # ================================================================
        self.next_section("krok4")
        self.play(
            ReplacementTransform(s3[1], s4[5]),
            ReplacementTransform(s3[2], s4[4]),
            ReplacementTransform(s3[3], s4[2]),
            FadeOut(s3[0], scale=0.4),
            FadeIn(s4[0]), FadeIn(s4[1]), FadeIn(s4[3]),
            run_time=1.4, path_arc=-PI / 6,
        )
        self.play(FadeIn(werdykt1, shift=UP * 0.2), run_time=0.7)
        self.zakoncz(s4, werdykt1)

        # ================================================================
        # KROK 5. Dwie latwiejsze wartosci, liczone tym samym sposobem.
        # Policzony wiersz zjezdza na swoje miejsce w liscie, nad nim
        # dochodza dwa nowe. Zielone: same wyniki 0 i 1.
        # ================================================================
        self.next_section("krok5")
        self.play(
            ReplacementTransform(s4[0], war[2][0]),
            ReplacementTransform(s4[1], war[2][1]),
            ReplacementTransform(s4[2], war[2][2]),
            ReplacementTransform(s4[3], war[2][3]),
            ReplacementTransform(s4[4], war[2][4]),
            ReplacementTransform(s4[5], war[2][5]),
            run_time=1.2,
        )
        self.play(FadeIn(pot[2]), run_time=0.5)
        war[0][5].set_color(ZIELONY)
        war[1][5].set_color(ZIELONY)
        self.play(
            FadeIn(pot[0], shift=DOWN * 0.2), FadeIn(war[0], shift=DOWN * 0.2),
            run_time=0.8,
        )
        self.play(
            FadeIn(pot[1], shift=DOWN * 0.2), FadeIn(war[1], shift=DOWN * 0.2),
            run_time=0.8,
        )
        self.zakoncz(*pot, *war, werdykt1, postoj=POSTOJ)

        # ================================================================
        # KROK 6. Wykres. Najpierw drobny ruch (lista jedzie w lewo, potegi
        # znikaja), dopiero potem wjezdza uklad: krok nie zaczyna sie od
        # najwiekszego przejazdu w scenie (README, punkt 48).
        # ================================================================
        self.next_section("krok6")
        self.play(
            *[FadeOut(m, scale=0.5) for m in pot],
            *[ReplacementTransform(war[i], war_cel[i]) for i in range(3)],
            run_time=1.0,
        )
        self.play(FadeIn(osie), FadeIn(znaczniki), run_time=0.9)

        kopie = []
        for i, cel in enumerate(punkty):
            k = Dot(war_cel[i].get_right() + RIGHT * 0.2, radius=0.085,
                    color=ZIELONY)
            kopie.append(k)
        self.play(*[FadeIn(k) for k in kopie], run_time=0.5)
        self.play(
            *[k.animate.move_to(c.get_center()) for k, c in zip(kopie, punkty)],
            run_time=1.2, path_arc=-PI / 6,
        )
        self.play(Create(krzywa), run_time=1.6)
        self.play(FadeIn(podpis_f), run_time=0.5)
        self.zakoncz(*war_cel, osie, znaczniki, krzywa, podpis_f, *punkty,
                     werdykt1, pomin=(krzywa, podpis_f, osie, znaczniki),
                     postoj=POSTOJ)

        # ================================================================
        # KROK 7. Trzy punkty to za malo na pewnosc, wiec na koniec regula:
        # podstawa wieksza od jedynki. Zielona jest sama podstawa.
        # ================================================================
        self.next_section("krok7")
        regula[0].set_color(ZIELONY)
        self.play(FadeIn(regula, shift=UP * 0.2), run_time=0.8)
        self.play(FadeIn(werdykt2, shift=UP * 0.2), run_time=0.7)
        self.wait(0.4)
        self.play(regula[0].animate.set_color(BLACK), run_time=0.4)
        self.wait(POSTOJ)
