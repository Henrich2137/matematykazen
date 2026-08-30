from manim import *

# Zadanie 12.1 (jednokrotny wybor, 1 pkt). Parabola o wierzcholku (3, 0)
# przechodzaca przez (0, -9). W jakim przedziale funkcja maleje?
# Wynik: <3, +oo), odpowiedz D.
#
# Projekt: issues/projekt-zad11-zad12-2024-grudzien.md. Piec krokow, jeden do
# jednego z pieciona linijkami w solutionText.
#
# Zadanie nic nie liczy, tylko czyta rysunek, wiec jednostka kroku jest JEDNA
# MYSL, a nie jeden symbol (README, punkt 42). Rysunek robimy sami: w tresci go
# nie ma, a bez niego zdanie "punkt lezy ponizej wierzcholka" jest pustym slowem.
#
# Uklad kadru: wykres po lewej (fiolet #7a3fa8, COLORS.md), po prawej pusto az
# do ostatniego kroku, w ktorym staje tam odczytany przedzial. Osie sa szare,
# jednostki na obu osiach rowne, zeby ksztalt paraboli byl prawdziwy.
#
# Render: manim --save_sections solutionZad12_1.py Zad12_1

ZIELONY = "#2e7d32"
FIOLET = "#7a3fa8"
SZARY_OSIE = "#666666"
SZARY_SIATKA = "#e0e0e0"

JEDNOSTKA = 0.65
SRODEK_WYKRESU = LEFT * 3.6
KOLUMNA_X = 3.7


class Zad12_1(Scene):

    def zgas(self, *mobiekty, czas=0.4):
        if mobiekty:
            self.play(*[m.animate.set_color(BLACK) for m in mobiekty], run_time=czas)

    def construct(self):
        # ================================================================
        # SCENOGRAFIA
        # ================================================================
        plansza = NumberPlane(
            x_range=[-1, 7, 1],
            y_range=[-10.2, 1.4, 1],
            x_length=8 * JEDNOSTKA,
            y_length=11.6 * JEDNOSTKA,
            background_line_style={
                "stroke_color": SZARY_SIATKA,
                "stroke_width": 1.5,
                "stroke_opacity": 1,
            },
            axis_config={
                "color": SZARY_OSIE,
                "stroke_width": 2.5,
                "include_ticks": False,
                "include_tip": True,
                "tip_width": 0.15,
                "tip_height": 0.15,
            },
        )
        plansza.move_to(SRODEK_WYKRESU)

        def p(x, y):
            return plansza.c2p(x, y)

        liczby = VGroup()
        for x in (1, 2, 3, 4, 5, 6):
            n = MathTex(str(x), color=SZARY_OSIE, font_size=32)
            n.next_to(p(x, 0), UP, buff=0.16)
            liczby.add(n)
        for y in (-3, -6, -9):
            n = MathTex(str(y), color=SZARY_OSIE, font_size=32)
            n.next_to(p(0, y), LEFT, buff=0.18)
            liczby.add(n)
        os_x_podpis = MathTex("x", color=SZARY_OSIE, font_size=30)
        os_x_podpis.next_to(p(7, 0), UP + RIGHT, buff=0.04)
        os_y_podpis = MathTex("y", color=SZARY_OSIE, font_size=30)
        os_y_podpis.next_to(p(0, 1.4), UP + LEFT, buff=0.04)
        liczby.add(os_x_podpis, os_y_podpis)

        def parabola(od, do, kolor=FIOLET, grubosc=6):
            return plansza.plot(
                lambda x: -((x - 3) ** 2),
                x_range=[od, do, 0.02],
                color=kolor, stroke_width=grubosc,
            )

        # Parabola jest rysowana KAWALEK PONIZEJ dolnej krawedzi kadru (y = -11.2,
        # a plansza konczy sie na -10.2), zeby wychodzila z kadru, a nie urywala
        # sie w powietrzu. Dzieki temu wedrujaca kropka wjezdza w kadr zza jego
        # krawedzi i wyjezdza za nia (Henrich, 2026-08-30: „wedrujaca kropka
        # powinna pojawiac sie zza kadru oraz zniknac za kadrem"). Przedtem
        # zaczynala i konczyla bieg na widocznym koncu krzywej, wiec wygladalo to
        # tak, jakby wyskakiwala znikad i znikala w niczym.
        POZA_KADREM = 11.2
        LEWY_KRANIEC = 3 - POZA_KADREM ** 0.5
        PRAWY_KRANIEC = 3 + POZA_KADREM ** 0.5

        # Parabola jest ZLOZONA Z DWOCH KAWALKOW, lewego i prawego, mimo ze
        # w kadrze wyglada jak jedna krzywa. Dzieki temu galaz zapala sie
        # zmiana koloru samej krzywej, a nie zielona nakladka polozona na
        # fioletowej. Nakladka wygladala tak samo, ale kazde jej wygaszenie
        # zostawialo na krzywej slad kodera i styk klatek spadal do 0,9985
        # (zmierzone 2026-08-28; po tej zmianie 0,9998).
        lewa_k = parabola(LEWY_KRANIEC, 3)
        prawa_k = parabola(3, PRAWY_KRANIEC)

        # Galaz zapala sie SAMYM KOLOREM, bez pogrubienia. Zmiana grubosci
        # przerysowuje krzywa i koder H.264 inaczej ustala jej brzeg, przez co
        # styk klatek spadal ponizej progu (zmierzone 2026-08-28).
        def zapal_galaz(galaz, czas=0.6):
            self.play(galaz.animate.set_color(ZIELONY), run_time=czas)

        def zgas_galaz(galaz, *razem, czas=0.5):
            self.play(galaz.animate.set_color(FIOLET), *razem, run_time=czas)

        # ================================================================
        # KROK 1. Oba dane punkty. Paraboli jeszcze nie ma.
        # ================================================================
        self.next_section("krok1")
        self.play(FadeIn(plansza), FadeIn(liczby), run_time=0.8)

        wierzcholek = Dot(p(3, 0), radius=0.09, color=ZIELONY)
        opis_w = MathTex("(3,\\ 0)", color=ZIELONY, font_size=34)
        # Nad rzedem liczb przy osi, nie obok wierzcholka: postawiony obok
        # siadal dokladnie na szarych "3" i "4" i czytal sie jak jedna liczba.
        opis_w.move_to(p(3, 1.0))
        punkt = Dot(p(0, -9), radius=0.09, color=ZIELONY)
        opis_p = MathTex("(0,\\ -9)", color=ZIELONY, font_size=34)
        opis_p.next_to(punkt, RIGHT, buff=0.16)

        self.play(FadeIn(wierzcholek), FadeIn(opis_w), run_time=0.7)
        self.play(FadeIn(punkt), FadeIn(opis_p), run_time=0.7)
        self.zgas(wierzcholek, opis_w, punkt, opis_p)
        self.wait(0.45)

        # ================================================================
        # KROK 2. Punkt lezy nizej niz wierzcholek, wiec wierzcholek jest
        # najwyzszym punktem wykresu: ramiona ida w dol. Zielona jest
        # strzalka, bo to ona niesie ten wniosek, a nie sama parabola.
        # ================================================================
        self.next_section("krok2")
        strzalka = Arrow(
            p(0, 0), p(0, -9),
            color=ZIELONY, buff=0, stroke_width=6,
            max_tip_length_to_length_ratio=0.08,
        )
        poziom = DashedLine(p(0, 0), p(3, 0), color=ZIELONY, stroke_width=3,
                            dash_length=0.12)
        self.play(Create(poziom), run_time=0.5)
        self.play(GrowArrow(strzalka), run_time=0.9)
        self.wait(0.4)
        self.play(Create(lewa_k), Create(prawa_k), run_time=1.6)
        self.zgas(strzalka, poziom)
        self.play(FadeOut(strzalka), FadeOut(poziom), run_time=0.35)
        self.wait(0.45)

        # ================================================================
        # KROK 3. Lewa galaz: idac od lewej do wierzcholka, wykres ROSNIE.
        # ================================================================
        self.next_section("krok3")
        # Start bierzemy z samej krzywej, zeby kropka nie odstawala od toru,
        # gdyby kiedys zmienil sie zakres. Punkt lezy pod krawedzia kadru.
        kropka = Dot(lewa_k.get_start(), radius=0.10, color=ZIELONY)
        napis_ro = Text("rośnie", font_size=32, color=ZIELONY)
        napis_ro.move_to(p(0.55, -2.1))

        zapal_galaz(lewa_k)
        self.add(kropka)
        self.play(MoveAlongPath(kropka, lewa_k), run_time=1.4, rate_func=linear)
        self.play(FadeIn(napis_ro), run_time=0.5)
        self.wait(0.4)
        zgas_galaz(lewa_k, FadeOut(kropka),
                   napis_ro.animate.set_color(BLACK))
        self.wait(0.45)

        # ================================================================
        # KROK 4. Prawa galaz: za wierzcholkiem wykres MALEJE.
        # ================================================================
        self.next_section("krok4")
        kropka2 = Dot(p(3, 0), radius=0.10, color=ZIELONY)
        napis_ma = Text("maleje", font_size=32, color=ZIELONY)
        napis_ma.move_to(p(5.6, -2.1))

        zapal_galaz(prawa_k)
        self.add(kropka2)
        self.play(MoveAlongPath(kropka2, prawa_k), run_time=1.4, rate_func=linear)
        self.play(FadeIn(napis_ma), run_time=0.5)
        self.wait(0.4)
        zgas_galaz(prawa_k, FadeOut(kropka2),
                   napis_ma.animate.set_color(BLACK))
        self.wait(0.45)

        # ================================================================
        # KROK 5. Rzut malejacego kawalka na os x. Kropka w trojce jest
        # ZAMALOWANA, bo sam wierzcholek nalezy do przedzialu.
        # ================================================================
        self.next_section("krok5")
        zapal_galaz(prawa_k)

        pas = Arrow(
            p(3, 0), p(6.9, 0),
            color=ZIELONY, buff=0, stroke_width=8,
            max_tip_length_to_length_ratio=0.12,
        )
        koniec = Dot(p(3, 0), radius=0.10, color=ZIELONY)
        self.play(FadeIn(koniec), run_time=0.4)
        self.play(GrowArrow(pas), run_time=1.0)

        podpis = Text("Funkcja maleje w przedziale", font_size=30, color=BLACK)
        podpis.move_to([KOLUMNA_X, 1.55, 0])
        przedzial = MathTex(r"\langle 3,\ +\infty)", color=ZIELONY, font_size=76)
        przedzial.move_to([KOLUMNA_X, 0.45, 0])
        self.play(FadeIn(podpis), run_time=0.5)
        self.play(FadeIn(przedzial, shift=UP * 0.2), run_time=0.8)
        self.wait(0.4)
        # Przedzial zostaje w kadrze, wiec musi skonczyc na czarno: zielen
        # w ostatniej klatce byla by przeskokiem wobec spoczynku odtwarzacza.
        zgas_galaz(prawa_k, FadeOut(pas), FadeOut(koniec),
                   przedzial.animate.set_color(BLACK))
        self.wait(0.45)
