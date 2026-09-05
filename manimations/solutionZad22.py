from manim import *

# Zadanie 22 (zamkniete, 1 pkt). Prosta k: y = -7x+3, prosta l rownolegla do k
# przecina Oy w (0, 6), punkt (1, p) lezy na l. Szukamy p. Wynik: p = -1,
# odpowiedz B.
#
# Projekt: issues/projekt-zad22-zad23-2024-grudzien.md. Siedem krokow: dwa
# rysunkowe (1, 2) bez wlasnej linijki w solutionText, piec pokrywajacych
# jego dwie linijki rachunku (l: y=-7x+6, potem p=-7*1+6=-1).
#
# Uklad kadru (README, punkt 35): LEWA polowa uklad wspolrzednych z prosta k
# (szara, bo to tylko DANA, nie cos co liczymy) i budowana prosta l (czarna);
# PRAWA polowa: pas reguly/odczytu u gory, rachunek na srodku, odpowiedz na dole.
#
# Kolor: zielone = to, co sie w danym kroku zmienia albo przylatuje skads
# innad (README punkty 37-38). Prosta k zostaje szara przez caly film, bo
# jest dana z tresci, a nie wynikiem.
#
# Render: manim --save_sections solutionZad22.py Zad22  (albo tools/wgraj-kroki.sh 22)

ZIELONY = "#2e7d32"
SZARY_OSIE = "#666666"
SZARY_DANE = "#666666"

SRODEK_WYKRESU = LEFT * 4.05 + DOWN * 0.10
KOLUMNA_X = 3.30
PAS_Y = 3.05
RACHUNEK_Y = 0.10
ODPOWIEDZ_Y = -2.55


class Zad22(Scene):

    # ---- klocki -------------------------------------------------------

    def stan(self, *args, rozmiar=54, kolor=BLACK):
        m = MathTex(*args)
        m.set_color(kolor)
        m.font_size = rozmiar
        return m

    def wiersz(self, *czesci, buff=0.17):
        return VGroup(*czesci).arrange(RIGHT, buff=buff)

    def zgas(self, *mobiekty, czas=0.4):
        """Gasi zielone na czarno PRZED koncowym postojem (README, punkt 1)."""
        if mobiekty:
            self.play(*[m.animate.set_color(BLACK) for m in mobiekty], run_time=czas)

    def przywolaj(self, zrodla, cele, czas=1.0, luk=-PI / 4):
        """Kopie przylatuja z miejsca, w ktorym zostaly odczytane, na miejsce
        docelowe (README, punkty 37-38): liczba nigdy nie pojawia sie z niczego."""
        kopie = []
        for zrodlo in zrodla:
            k = zrodlo.copy().set_opacity(0)
            self.add(k)
            kopie.append(k)
        self.play(
            *[k.animate.set_opacity(1).set_color(ZIELONY).move_to(c)
              for k, c in zip(kopie, cele)],
            run_time=czas, path_arc=luk,
        )
        return kopie

    def construct(self):
        # ================================================================
        # SCENOGRAFIA: uklad wspolrzednych, prosta k (dana) i prosta l (budowana)
        # ================================================================
        plansza = NumberPlane(
            x_range=[-1, 1.5, 0.5],
            y_range=[-6, 10, 4],
            x_length=3.6,
            y_length=5.6,
            background_line_style={
                "stroke_color": "#e0e0e0",
                "stroke_width": 1.5,
                "stroke_opacity": 1,
            },
            axis_config={
                "color": SZARY_OSIE,
                "stroke_width": 2.5,
                "include_ticks": False,
                "include_tip": True,
                "tip_width": 0.16,
                "tip_height": 0.16,
            },
        )
        plansza.move_to(SRODEK_WYKRESU)

        def p(x, y):
            return plansza.c2p(x, y)

        os_x = MathTex("x", color=SZARY_OSIE, font_size=34)
        os_x.next_to(p(1.5, 0), DOWN + RIGHT, buff=0.04)
        os_y = MathTex("y", color=SZARY_OSIE, font_size=34)
        os_y.next_to(p(0, 10), UP + LEFT, buff=0.04)

        # k: y = -7x+3, przyciete do ramki (-1, 10) do (9/7, -6).
        prosta_k = Line(p(-1, 10), p(9 / 7, -6), color=SZARY_DANE, stroke_width=5)
        etykieta_k = self.stan("k:\\ y=", "-7", "x+3", rozmiar=34, kolor=SZARY_DANE)
        etykieta_k.move_to(p(0.85, 7.3))

        # l: y = -7x+6, przyciete do ramki (-4/7, 10) do (1.5, -4.5).
        prosta_l = Line(p(-4 / 7, 10), p(1.5, -4.5), color=BLACK, stroke_width=5)

        punkt_06 = Dot(p(0, 6), radius=0.07, color=BLACK)
        opis_06 = self.stan("(", "0", ",\\ ", "6", ")", rozmiar=34)
        opis_06.next_to(punkt_06, LEFT, buff=0.14)

        # ================================================================
        # PRAWA POLOWA: regula, rachunek, odpowiedz
        # ================================================================
        regula = Text(
            "Proste równoległe mają ten sam\nwspółczynnik kierunkowy:",
            font_size=28, color=BLACK, line_spacing=1.1,
        )
        wzor_rownolegle = self.stan("a_1", "=", "a_2", rozmiar=44)
        ramka_pas = VGroup(regula, wzor_rownolegle).arrange(DOWN, buff=0.28)
        ramka_pas.move_to([KOLUMNA_X, PAS_Y, 0])

        etykieta_l_lit = self.wiersz(
            self.stan("l:\\ y="), self.stan("-7", rozmiar=54), self.stan("x+"),
            self.stan("6", rozmiar=54),
        )
        etykieta_l_lit.move_to([KOLUMNA_X, RACHUNEK_Y, 0])

        w4 = self.wiersz(self.stan("y"), self.stan("="), self.stan("-7"),
                         self.stan("x+"), self.stan("6"))
        s4 = self.wiersz(self.stan("p"), self.stan("="), self.stan("-7"),
                         self.stan(r"\cdot"), self.stan("1"), self.stan("+"),
                         self.stan("6"))
        s5 = self.wiersz(self.stan("p"), self.stan("="), self.stan("-7"),
                         self.stan("+"), self.stan("6"))
        s6 = self.wiersz(self.stan("p"), self.stan("="), self.stan("-1"))

        for m in (w4, s4, s5, s6):
            m.move_to([KOLUMNA_X, RACHUNEK_Y, 0])

        odpowiedz = VGroup(
            Text("Odpowiedź", font_size=34, color=BLACK),
            Text("B", font_size=38, weight=BOLD, color=BLACK),
        ).arrange(RIGHT, buff=0.26)
        odpowiedz.move_to([KOLUMNA_X, ODPOWIEDZ_Y, 0])

        # ================================================================
        # KROK 1. Rysunek: uklad, prosta k (dana), punkt (0, 6). Cale szare/
        # czarne, nic sie tu jeszcze nie liczy (README, punkt 12).
        # ================================================================
        self.next_section("krok1")
        self.play(FadeIn(plansza), FadeIn(os_x), FadeIn(os_y), run_time=0.8)
        self.play(Create(prosta_k), run_time=1.0)
        self.play(FadeIn(etykieta_k), run_time=0.5)
        self.play(FadeIn(punkt_06), FadeIn(opis_06), run_time=0.5)
        self.wait(0.45)

        # ================================================================
        # KROK 2. Regula (proste rownolegle maja ten sam wspolczynnik
        # kierunkowy) i rysunek prostej l przechodzacej przez (0, 6),
        # rownoleglej do k. Bez koloru: to fakt, jeszcze nic nie liczymy.
        # ================================================================
        self.next_section("krok2")
        self.play(FadeIn(ramka_pas), run_time=0.8)
        self.wait(0.3)
        self.play(Create(prosta_l), run_time=1.1)
        self.wait(0.45)

        # ================================================================
        # KROK 3. Rownanie l: -7 przylatuje z etykiety k (ten sam wspolczynnik
        # kierunkowy), 6 przylatuje z punktu (0, 6) na rysunku.
        # ================================================================
        self.next_section("krok3")
        self.play(FadeIn(etykieta_l_lit[0], etykieta_l_lit[2]), run_time=0.5)
        kopie = self.przywolaj(
            [etykieta_k[1], opis_06[3]],
            [etykieta_l_lit[1].get_center(), etykieta_l_lit[3].get_center()],
            luk=PI / 4,
        )
        self.play(
            ReplacementTransform(kopie[0], etykieta_l_lit[1]),
            ReplacementTransform(kopie[1], etykieta_l_lit[3]),
            run_time=0.6,
        )
        self.zgas(etykieta_l_lit[1], etykieta_l_lit[3])
        self.wait(0.45)

        # ================================================================
        # KROK 4. Na prostej l pojawia sie punkt (1, p). Podstawiamy x = 1
        # do rownania l: y zamienia sie na p, x na 1 (przylatuje z rysunku).
        # ================================================================
        self.next_section("krok4")
        punkt_1p = Dot(p(1, -1), radius=0.07, color=BLACK)
        opis_1p = self.stan("(", "1", ",\\ ", "p", ")", rozmiar=34)
        opis_1p.next_to(punkt_1p, DOWN + RIGHT, buff=0.12)
        self.play(FadeIn(punkt_1p), FadeIn(opis_1p), run_time=0.6)
        self.wait(0.3)

        self.play(ReplacementTransform(etykieta_l_lit, w4), run_time=0.5)
        self.wait(0.3)

        kopia_x = self.przywolaj([opis_1p[1]], [s4[4].get_center()], luk=PI / 3)[0]
        s4[0].set_color(ZIELONY)
        s4[4].set_color(ZIELONY)
        self.play(
            ReplacementTransform(w4[0], s4[0]),
            ReplacementTransform(w4[1], s4[1]),
            ReplacementTransform(w4[2], s4[2]),
            FadeOut(w4[3], scale=0.4),
            FadeIn(s4[3]),
            ReplacementTransform(kopia_x, s4[4]),
            FadeIn(s4[5]),
            ReplacementTransform(w4[4], s4[6]),
            run_time=1.1,
        )
        self.zgas(s4[0], s4[4])
        self.wait(0.45)

        # ================================================================
        # KROK 5. Mnozymy -7 razy 1 (bez zmiany wartosci).
        # ================================================================
        self.next_section("krok5")
        s5[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s4[0], s5[0]),
            ReplacementTransform(s4[1], s5[1]),
            ReplacementTransform(s4[2], s5[2]),
            FadeOut(s4[3], target_position=s5[2].get_center(), scale=0.4),
            FadeOut(s4[4], target_position=s5[2].get_center(), scale=0.4),
            ReplacementTransform(s4[5], s5[3]),
            ReplacementTransform(s4[6], s5[4]),
            run_time=1.0,
        )
        self.zgas(s5[2])
        self.wait(0.45)

        # ================================================================
        # KROK 6. Dodajemy. Wynik siada tez na rysunku, przy punkcie (1, p).
        # ================================================================
        self.next_section("krok6")
        s6[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s5[0], s6[0]),
            ReplacementTransform(s5[1], s6[1]),
            FadeOut(s5[2], target_position=s6[2].get_center(), scale=0.4),
            FadeOut(s5[3], target_position=s6[2].get_center(), scale=0.4),
            FadeOut(s5[4], target_position=s6[2].get_center(), scale=0.4),
            FadeIn(s6[2]),
            run_time=1.0,
        )
        self.zgas(s6[2])
        self.wait(0.45)

        # ================================================================
        # KROK 7. Odpowiedz. Wynik przylatuje na rysunek jako podpis punktu.
        # ================================================================
        self.next_section("krok7")
        nowy_opis = self.stan("(", "1", ",\\ ", "-1", ")", rozmiar=34)
        nowy_opis.next_to(punkt_1p, DOWN + RIGHT, buff=0.12)
        kopia_wyniku = s6[2].copy()
        self.play(
            kopia_wyniku.animate.set_color(BLACK)
            .move_to(nowy_opis[3].get_center()).scale(34 / 54),
            FadeOut(opis_1p),
            run_time=1.0,
        )
        self.remove(kopia_wyniku)
        self.add(nowy_opis)
        self.play(FadeIn(odpowiedz), run_time=0.6)
        self.wait(0.45)
