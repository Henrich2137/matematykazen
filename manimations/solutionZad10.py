from manim import *

# Zadanie 10 (zamkniete z lukami, 4 pkt). Odczyt z wykresu funkcji danej trzema
# wzorami. Odpowiedzi: (-4, 4>, <-1, 3>, (1, 3), (-4, -2>.
#
# Projekt: issues/projekt-zad9-zad10-2024-grudzien.md. Szesnascie krokow, jeden
# do jednego z szesnastoma linijkami w solutionText.
#
# Uklad sceny (inny niz w pozostalych scenach, bo tu nie ma rachunku do
# rozpisania, tylko rysunek):
#   - LEWA polowa kadru: uklad wspolrzednych z wykresem, odwzorowany z arkusza
#     (matura/2024-grudzien/media/zad10/zad10rys.png): ten sam fiolet, ten sam
#     podpis y = f(x), kolko otwarte w (-4, 3) i kropka pelna w (4, 1).
#     Zakres osi y jest wezszy niz w arkuszu (-2 do 4 zamiast -5 do 5), bo
#     wykres i tak zyje miedzy -1 a 3, a kadr 16:9 jest niski. Jednostki na obu
#     osiach sa rowne, wiec ksztalt wykresu jest ten sam co w arkuszu.
#   - PRAWA polowa: etykieta biezacej czesci (zmienia sie cztery razy), zapis
#     budowany z dwoch koncow przedzialu i lista zamknietych odpowiedzi, ktora
#     rosnie do czterech pozycji i zostaje w kadrze do konca.
#
# Wykres, os, siatka i lista wynikow to SCENOGRAFIA: stoja przez caly film
# i nigdy nie gasna. Kazdy krok dokłada tylko to, co w nim zielone.
#
# Kolor: zielone = to, na co uczen ma w tym kroku patrzec (COLORS.md, rola
# "oznaczenie miejsca"). Wykres zostaje fioletowy (#7a3fa8, rola "wykres
# funkcji jak w arkuszach CKE"), osie i siatka szare.
#
# Render: manim --save_sections solutionZad10.py Zad10  (albo tools/wgraj-kroki.sh 10)

ZIELONY = "#2e7d32"
FIOLET = "#7a3fa8"
SZARY_OSIE = "#666666"
SZARY_SIATKA = "#e0e0e0"

SRODEK_WYKRESU = LEFT * 3.35 + DOWN * 0.35
KOLUMNA_X = 3.9
ETYKIETA_Y = 3.15
ZAPIS_Y = 1.75
LISTA_Y = 0.75
LISTA_KROK = 0.8
LISTA_LEWO = 2.35


class Zad10(Scene):

    # ---- klocki -------------------------------------------------------

    def etykieta(self, tekst):
        t = Text(tekst, font_size=34, color=BLACK)
        t.move_to([KOLUMNA_X, ETYKIETA_Y, 0])
        return t

    def zgas(self, *mobiekty, czas=0.4):
        """Gasi zielone na czarno. Wolane PRZED koncowym postojem, zeby
        ostatnia klatka kroku byla czysta (README, punkt 1 zasad)."""
        if mobiekty:
            self.play(*[m.animate.set_color(BLACK) for m in mobiekty], run_time=czas)

    def zamknij(self, *znika, czas=0.35):
        """Usuwa pomocnicze podswietlenia i przytrzymuje czysty obraz."""
        if znika:
            self.play(*[FadeOut(m) for m in znika], run_time=czas)
        self.wait(0.3)

    def construct(self):
        # ================================================================
        # SCENOGRAFIA
        # ================================================================
        plansza = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-2, 4, 1],
            x_length=7.4,
            y_length=4.44,
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
                "tip_width": 0.16,
                "tip_height": 0.16,
            },
        )
        plansza.move_to(SRODEK_WYKRESU)

        def p(x, y):
            return plansza.c2p(x, y)

        # Liczby przy osiach. Wpisywane recznie, bo include_numbers stawia je
        # po obu stronach zera i przy tej skali wchodza na siatke.
        liczby = VGroup()
        for x in (-4, -2, 1, 2, 3, 4):
            n = MathTex(str(x), color=SZARY_OSIE, font_size=30)
            n.next_to(p(x, 0), DOWN, buff=0.30)
            liczby.add(n)
        for y in (-1, 1, 3):
            n = MathTex(str(y), color=SZARY_OSIE, font_size=30)
            n.next_to(p(0, y), LEFT, buff=0.28)
            liczby.add(n)
        os_x_podpis = MathTex("x", color=SZARY_OSIE, font_size=34)
        os_x_podpis.next_to(p(5, 0), DOWN + RIGHT, buff=0.06)
        os_y_podpis = MathTex("y", color=SZARY_OSIE, font_size=34)
        os_y_podpis.next_to(p(0, 4), UP + LEFT, buff=0.06)
        liczby.add(os_x_podpis, os_y_podpis)

        # Wykres: lamana przez cztery punkty, ciagla od (-4, 3) do (4, 1).
        wykres = VMobject(color=FIOLET, stroke_width=6)
        wykres.set_points_as_corners([p(-4, 3), p(-2, 3), p(2, -1), p(4, 1)])

        koniec_otwarty = Circle(
            radius=0.09, color=FIOLET, stroke_width=5,
            fill_color=WHITE, fill_opacity=1,
        ).move_to(p(-4, 3))
        koniec_pelny = Dot(p(4, 1), radius=0.09, color=FIOLET)

        podpis_f = MathTex("y = f(x)", color=FIOLET, font_size=40)
        podpis_f.move_to(p(2.5, 2.6))

        scenografia = VGroup(plansza, liczby, wykres, koniec_otwarty,
                             koniec_pelny, podpis_f)

        # Lista zamknietych odpowiedzi, po prawej. Powstaje po jednej pozycji.
        def pozycja_listy(nr, wzor):
            g = VGroup(
                MathTex(f"{nr}.", color=BLACK, font_size=40),
                MathTex(wzor, color=BLACK, font_size=40),
            ).arrange(RIGHT, buff=0.22)
            g.move_to([KOLUMNA_X, LISTA_Y - (nr - 1) * LISTA_KROK, 0])
            g.shift(RIGHT * (LISTA_LEWO - g.get_left()[0]))
            return g

        # ================================================================
        # KROK 1. Wykres pojawia sie od zera. Pod nim, na osi x, zapala sie
        # cien calego wykresu: to jest dziedzina.
        # ================================================================
        self.next_section("krok1")
        et1 = self.etykieta("1. Dziedzina")
        self.play(FadeIn(plansza), FadeIn(liczby), run_time=0.8)
        self.play(Create(wykres), run_time=1.4)
        self.play(
            FadeIn(koniec_otwarty), FadeIn(koniec_pelny), FadeIn(podpis_f),
            run_time=0.5,
        )
        self.play(FadeIn(et1), run_time=0.4)

        pas_dziedziny = Line(p(-4, 0), p(4, 0), color=ZIELONY, stroke_width=8)
        rzut_l = DashedLine(p(-4, 3), p(-4, 0), color=ZIELONY, stroke_width=3,
                            dash_length=0.1)
        rzut_p = DashedLine(p(4, 1), p(4, 0), color=ZIELONY, stroke_width=3,
                            dash_length=0.1)
        self.play(Create(rzut_l), Create(rzut_p), run_time=0.7)
        self.play(Create(pas_dziedziny), run_time=0.8)
        self.zgas(pas_dziedziny)
        self.zamknij(rzut_l, rzut_p)
        self.wait(0.6)

        # ================================================================
        # KROK 2. Lewy koniec: kolko otwarte zjezdza na os i zostaje tam
        # jako pusta kropka. Po prawej pojawia sie zapis "(-4".
        # ================================================================
        self.next_section("krok2")
        zapis1 = VGroup(
            MathTex("(-4", color=BLACK, font_size=60),
            MathTex(",\\ ", color=BLACK, font_size=60),
            MathTex("4\\rangle", color=BLACK, font_size=60),
        ).arrange(RIGHT, buff=0.06)
        zapis1.move_to([KOLUMNA_X, ZAPIS_Y, 0])

        # Kopia startuje NIEWIDOCZNA. Dolozona wprost na oryginal robilaby
        # podwojna krawedz juz w pierwszej klatce kroku, czyli rozjazd ze
        # styku z krokiem poprzednim (zlapane przez tools/styk-klatek.sh).
        kopia_o = koniec_otwarty.copy().set_opacity(0)
        self.add(kopia_o)
        self.play(
            kopia_o.animate.set_opacity(1).set_color(ZIELONY).set_fill(WHITE, 1),
            run_time=0.3,
        )
        cel_o = Circle(
            radius=0.09, color=ZIELONY, stroke_width=5,
            fill_color=WHITE, fill_opacity=1,
        ).move_to(p(-4, 0))
        self.play(Transform(kopia_o, cel_o), run_time=1.0)
        zapis1[0].set_color(ZIELONY)
        self.play(FadeIn(zapis1[0]), run_time=0.6)
        self.zgas(kopia_o, zapis1[0])
        self.wait(0.6)

        # ================================================================
        # KROK 3. Prawy koniec: kropka pelna zjezdza na os. Zapis "4>".
        # ================================================================
        self.next_section("krok3")
        kopia_k = koniec_pelny.copy().set_opacity(0)
        self.add(kopia_k)
        self.play(kopia_k.animate.set_opacity(1).set_color(ZIELONY), run_time=0.3)
        self.play(kopia_k.animate.move_to(p(4, 0)), run_time=1.0)
        zapis1[2].set_color(ZIELONY)
        self.play(FadeIn(zapis1[2]), run_time=0.6)
        self.zgas(kopia_k, zapis1[2])
        self.wait(0.6)

        # ================================================================
        # KROK 4. Oba konce skladaja sie w jeden przedzial i odjezdzaja
        # na liste odpowiedzi.
        # ================================================================
        self.next_section("krok4")
        self.play(FadeIn(zapis1[1]), run_time=0.4)
        poz1 = pozycja_listy(1, "(-4,\\ 4\\rangle")
        self.play(
            Transform(zapis1, poz1[1].copy()),
            FadeIn(poz1[0]),
            FadeOut(pas_dziedziny), FadeOut(kopia_o), FadeOut(kopia_k),
            run_time=1.2,
        )
        self.remove(zapis1)
        self.add(poz1)
        self.wait(0.6)

        # ================================================================
        # KROK 5. Druga czesc: ten sam wykres, ale rzut na os y.
        # ================================================================
        self.next_section("krok5")
        et2 = self.etykieta("2. Zbiór wartości")
        self.play(FadeOut(et1), FadeIn(et2), run_time=0.5)
        pas_wartosci = Line(p(0, -1), p(0, 3), color=ZIELONY, stroke_width=8)
        rzut_d = DashedLine(p(2, -1), p(0, -1), color=ZIELONY, stroke_width=3,
                            dash_length=0.1)
        rzut_g = DashedLine(p(-3, 3), p(0, 3), color=ZIELONY, stroke_width=3,
                            dash_length=0.1)
        self.play(Create(rzut_d), Create(rzut_g), run_time=0.7)
        self.play(Create(pas_wartosci), run_time=0.8)
        self.zgas(pas_wartosci)
        self.zamknij(rzut_d, rzut_g)
        self.wait(0.6)

        # ================================================================
        # KROK 6. Najnizszy punkt wykresu jedzie na os y.
        # ================================================================
        self.next_section("krok6")
        zapis2 = VGroup(
            MathTex("\\langle -1", color=BLACK, font_size=60),
            MathTex(",\\ ", color=BLACK, font_size=60),
            MathTex("3\\rangle", color=BLACK, font_size=60),
        ).arrange(RIGHT, buff=0.06)
        zapis2.move_to([KOLUMNA_X, ZAPIS_Y, 0])

        dol = Dot(p(2, -1), radius=0.09, color=ZIELONY)
        self.play(FadeIn(dol), run_time=0.4)
        self.play(dol.animate.move_to(p(0, -1)), run_time=1.0)
        zapis2[0].set_color(ZIELONY)
        self.play(FadeIn(zapis2[0]), run_time=0.6)
        self.zgas(dol, zapis2[0])
        self.wait(0.6)

        # ================================================================
        # KROK 7. Poziomy odcinek lezy na wysokosci 3, wiec ta wartosc
        # jest osiagana. Jedzie na os y.
        # ================================================================
        self.next_section("krok7")
        gora = Line(p(-4, 3), p(-2, 3), color=ZIELONY, stroke_width=8)
        self.play(Create(gora), run_time=0.7)
        kropka_g = Dot(p(-2, 3), radius=0.09, color=ZIELONY)
        self.play(FadeIn(kropka_g), run_time=0.3)
        self.play(kropka_g.animate.move_to(p(0, 3)), run_time=0.9)
        zapis2[2].set_color(ZIELONY)
        self.play(FadeIn(zapis2[2]), run_time=0.6)
        self.zgas(gora, kropka_g, zapis2[2])
        self.zamknij(gora)
        self.wait(0.6)

        # ================================================================
        # KROK 8. Skladamy przedzial i odkladamy na liste.
        # ================================================================
        self.next_section("krok8")
        self.play(FadeIn(zapis2[1]), run_time=0.4)
        poz2 = pozycja_listy(2, "\\langle -1,\\ 3\\rangle")
        self.play(
            Transform(zapis2, poz2[1].copy()),
            FadeIn(poz2[0]),
            FadeOut(pas_wartosci), FadeOut(kropka_g), FadeOut(dol),
            run_time=1.2,
        )
        self.remove(zapis2)
        self.add(poz2)
        self.wait(0.6)

        # ================================================================
        # KROK 9. Trzecia czesc: wartosc ujemna to y < 0, czyli wykres
        # pod osia x.
        # ================================================================
        self.next_section("krok9")
        et3 = self.etykieta("3. Wartości ujemne")
        self.play(FadeOut(et2), FadeIn(et3), run_time=0.5)
        warunek = MathTex("y < 0", color=ZIELONY, font_size=40)
        warunek.next_to(p(-3.6, -1), LEFT, buff=0.0).shift(RIGHT * 0.35)
        strzalka = Arrow(
            start=p(-4.6, -0.2), end=p(-4.6, -1.6),
            color=ZIELONY, stroke_width=4, buff=0,
            max_tip_length_to_length_ratio=0.25,
        )
        self.play(FadeIn(warunek), GrowArrow(strzalka), run_time=0.8)
        self.zgas(warunek, strzalka)
        self.wait(0.6)

        # ================================================================
        # KROK 10. Fragment wykresu pod osia zapala sie jednym ciagiem
        # i rzutuje sie na os x.
        # ================================================================
        self.next_section("krok10")
        fragment = VMobject(color=ZIELONY, stroke_width=8)
        fragment.set_points_as_corners([p(1, 0), p(2, -1), p(3, 0)])
        self.play(Create(fragment), run_time=1.1)
        pas_ujemne = Line(p(1, 0), p(3, 0), color=ZIELONY, stroke_width=8)
        self.play(Create(pas_ujemne), run_time=0.7)
        self.zgas(pas_ujemne)
        self.zamknij(fragment)
        self.wait(0.6)

        # ================================================================
        # KROK 11. W x = 1 wykres dotyka osi, wiec wartosc jest tam zerem.
        # Zero nie jest ujemne: koniec wylaczony.
        # ================================================================
        self.next_section("krok11")
        zapis3 = VGroup(
            MathTex("(1", color=BLACK, font_size=60),
            MathTex(",\\ ", color=BLACK, font_size=60),
            MathTex("3)", color=BLACK, font_size=60),
        ).arrange(RIGHT, buff=0.06)
        zapis3.move_to([KOLUMNA_X, ZAPIS_Y, 0])

        pusta_l = Circle(
            radius=0.09, color=ZIELONY, stroke_width=5,
            fill_color=WHITE, fill_opacity=1,
        ).move_to(p(1, 0))
        self.play(FadeIn(pusta_l), run_time=0.5)
        zapis3[0].set_color(ZIELONY)
        self.play(FadeIn(zapis3[0]), run_time=0.6)
        self.zgas(pusta_l, zapis3[0])
        self.wait(0.6)

        # ================================================================
        # KROK 12. To samo w x = 3.
        # ================================================================
        self.next_section("krok12")
        pusta_p = Circle(
            radius=0.09, color=ZIELONY, stroke_width=5,
            fill_color=WHITE, fill_opacity=1,
        ).move_to(p(3, 0))
        self.play(FadeIn(pusta_p), run_time=0.5)
        zapis3[2].set_color(ZIELONY)
        self.play(FadeIn(zapis3[2]), run_time=0.6)
        self.zgas(pusta_p, zapis3[2])
        self.wait(0.6)

        # ================================================================
        # KROK 13. Skladamy przedzial i odkladamy na liste.
        # ================================================================
        self.next_section("krok13")
        self.play(FadeIn(zapis3[1]), run_time=0.4)
        poz3 = pozycja_listy(3, "(1,\\ 3)")
        self.play(
            Transform(zapis3, poz3[1].copy()),
            FadeIn(poz3[0]),
            FadeOut(pas_ujemne), FadeOut(pusta_l), FadeOut(pusta_p),
            FadeOut(warunek), FadeOut(strzalka),
            run_time=1.2,
        )
        self.remove(zapis3)
        self.add(poz3)
        self.wait(0.6)

        # ================================================================
        # KROK 14. Czwarta czesc: najwieksza wartosc to 3. Rysujemy ten
        # poziom przez caly wykres.
        # ================================================================
        self.next_section("krok14")
        et4 = self.etykieta("4. Największa wartość")
        self.play(FadeOut(et3), FadeIn(et4), run_time=0.5)
        poziom = DashedLine(p(-5, 3), p(5, 3), color=ZIELONY, stroke_width=3,
                            dash_length=0.12)
        podpis_poziom = MathTex("y = 3", color=ZIELONY, font_size=36)
        podpis_poziom.next_to(p(4.2, 3), UP, buff=0.1)
        self.play(Create(poziom), FadeIn(podpis_poziom), run_time=0.9)
        self.zgas(poziom, podpis_poziom)
        self.wait(0.6)

        # ================================================================
        # KROK 15. Na tej wysokosci lezy poziomy odcinek wykresu. Rzut na
        # os x, z pusta kropka w -4 i pelna w -2.
        # ================================================================
        self.next_section("krok15")
        odcinek_max = Line(p(-4, 3), p(-2, 3), color=ZIELONY, stroke_width=8)
        self.play(Create(odcinek_max), run_time=0.7)
        rzut_a = DashedLine(p(-4, 3), p(-4, 0), color=ZIELONY, stroke_width=3,
                            dash_length=0.1)
        rzut_b = DashedLine(p(-2, 3), p(-2, 0), color=ZIELONY, stroke_width=3,
                            dash_length=0.1)
        self.play(Create(rzut_a), Create(rzut_b), run_time=0.7)
        pas_max = Line(p(-4, 0), p(-2, 0), color=ZIELONY, stroke_width=8)
        koniec_a = Circle(
            radius=0.09, color=ZIELONY, stroke_width=5,
            fill_color=WHITE, fill_opacity=1,
        ).move_to(p(-4, 0))
        koniec_b = Dot(p(-2, 0), radius=0.09, color=ZIELONY)
        self.play(Create(pas_max), FadeIn(koniec_a), FadeIn(koniec_b),
                  run_time=0.8)
        self.zgas(pas_max, koniec_a, koniec_b)
        self.zamknij(odcinek_max, rzut_a, rzut_b)
        self.wait(0.6)

        # ================================================================
        # KROK 16. Ostatni przedzial idzie na liste. W kadrze zostaja
        # cztery odpowiedzi naraz.
        # ================================================================
        self.next_section("krok16")
        zapis4 = MathTex("(-4,\\ -2\\rangle", color=BLACK, font_size=60)
        zapis4.move_to([KOLUMNA_X, ZAPIS_Y, 0])
        self.play(
            ReplacementTransform(
                VGroup(pas_max, koniec_a, koniec_b), zapis4
            ),
            run_time=1.0,
        )
        poz4 = pozycja_listy(4, "(-4,\\ -2\\rangle")
        self.play(
            Transform(zapis4, poz4[1].copy()),
            FadeIn(poz4[0]),
            FadeOut(poziom), FadeOut(podpis_poziom),
            run_time=1.2,
        )
        self.remove(zapis4)
        self.add(poz4)
        self.wait(0.4)
