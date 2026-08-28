from manim import *

# Zadanie 10 (zamkniete z lukami, 4 pkt). Odczyt z wykresu funkcji danej trzema
# wzorami. Odpowiedzi: (-4, 4>, <-1, 3>, (1, 3), (-4, -2>.
#
# Projekt: issues/projekt-zad9-zad10-2024-grudzien.md. Dziewiec krokow, jeden
# do jednego z dziewiecioma linijkami w solutionText.
#
# WERSJA DRUGA, 2026-08-28, po uwagach Henricha do pierwszej (TODO.md):
#   - szesnascie krokow zeszlo do dziewieciu. W filmie, ktory nie liczy, tylko
#     czyta rysunek, jednostka kroku jest JEDNA MYSL, a nie jeden symbol
#     (README, punkt 42): oba konce przedzialu odczytuje sie razem;
#   - krok z warunkiem y < 0 i strzalka w dol wypadl: nastepny krok i tak
#     zapala fragment wykresu pod osia, wiec strzalka nic nie dokladala
#     (README, punkt 43);
#   - pierwsza czesc idzie wolniej (trzy kroki), bo tam pierwszy raz tlumaczy
#     sie kolko i kropke; kazda kolejna ma dwa kroki;
#   - w ostatnim kroku etykieta czesci znika, zeby na koniec w kadrze zostal
#     sam wykres i cztery odpowiedzi.
#
# Uklad sceny:
#   - LEWA polowa kadru: uklad wspolrzednych z wykresem, odwzorowany z arkusza
#     (matura/2024-grudzien/media/zad10/zad10rys.png): ten sam fiolet, ten sam
#     podpis y = f(x), kolko otwarte w (-4, 3) i kropka pelna w (4, 1).
#     Zakres osi y jest wezszy niz w arkuszu (-2 do 4 zamiast -5 do 5), bo kadr
#     16:9 jest niski. Jednostki na obu osiach sa rowne, wiec ksztalt sie zgadza.
#   - PRAWA polowa: etykieta biezacej czesci, zapis budowany z dwoch koncow
#     i lista zamknietych odpowiedzi, ktora rosnie do czterech pozycji.
#
# Wykres, os, siatka i lista wynikow to SCENOGRAFIA: stoja przez caly film.
# Kazdy krok dokłada tylko to, co w nim zielone.
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

        wykres = VMobject(color=FIOLET, stroke_width=6)
        wykres.set_points_as_corners([p(-4, 3), p(-2, 3), p(2, -1), p(4, 1)])

        koniec_otwarty = Circle(
            radius=0.09, color=FIOLET, stroke_width=5,
            fill_color=WHITE, fill_opacity=1,
        ).move_to(p(-4, 3))
        koniec_pelny = Dot(p(4, 1), radius=0.09, color=FIOLET)

        podpis_f = MathTex("y = f(x)", color=FIOLET, font_size=40)
        podpis_f.move_to(p(2.5, 2.6))

        def zapis(*czesci):
            g = VGroup(*[MathTex(c, color=BLACK, font_size=60) for c in czesci])
            g.arrange(RIGHT, buff=0.06)
            g.move_to([KOLUMNA_X, ZAPIS_Y, 0])
            return g

        def pozycja_listy(nr, wzor):
            g = VGroup(
                MathTex(f"{nr}.", color=BLACK, font_size=40),
                MathTex(wzor, color=BLACK, font_size=40),
            ).arrange(RIGHT, buff=0.22)
            g.move_to([KOLUMNA_X, LISTA_Y - (nr - 1) * LISTA_KROK, 0])
            g.shift(RIGHT * (LISTA_LEWO - g.get_left()[0]))
            return g

        def duch(wzorzec, gdzie, kolo=False):
            """Kopia znacznika, ktora startuje NIEWIDOCZNA. Dolozona wprost
            na oryginal robilaby podwojna krawedz juz w pierwszej klatce
            kroku, czyli rozjazd na styku (tools/styk-klatek.sh)."""
            k = wzorzec.copy().set_opacity(0).move_to(gdzie)
            self.add(k)
            return k

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
        # KROK 2. OBA konce naraz: kolko otwarte zjezdza na os jako pusta
        # kropka, kropka pelna jako zamalowana. Po prawej powstaja dwa
        # kawalki zapisu. Zielone: konce i to, co z nich powstaje.
        # ================================================================
        self.next_section("krok2")
        zapis1 = zapis("(-4", ",\\ ", "4\\rangle")

        kopia_o = duch(koniec_otwarty, koniec_otwarty.get_center())
        kopia_k = duch(koniec_pelny, koniec_pelny.get_center())
        self.play(
            kopia_o.animate.set_opacity(1).set_color(ZIELONY).set_fill(WHITE, 1),
            kopia_k.animate.set_opacity(1).set_color(ZIELONY),
            run_time=0.4,
        )
        self.play(
            kopia_o.animate.move_to(p(-4, 0)),
            kopia_k.animate.move_to(p(4, 0)),
            run_time=1.0,
        )
        zapis1[0].set_color(ZIELONY)
        zapis1[2].set_color(ZIELONY)
        self.play(FadeIn(zapis1[0]), FadeIn(zapis1[2]), run_time=0.7)
        self.zgas(kopia_o, kopia_k, zapis1[0], zapis1[2])
        self.wait(0.6)

        # ================================================================
        # KROK 3. Oba konce skladaja sie w jeden przedzial i odjezdzaja
        # na liste odpowiedzi.
        # ================================================================
        self.next_section("krok3")
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
        # KROK 4. Druga czesc: ten sam wykres, ale rzut na os y.
        # ================================================================
        self.next_section("krok4")
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
        # KROK 5. Najnizszy punkt i poziomy odcinek jada na os y, a z nich
        # od razu powstaje caly przedzial i idzie na liste.
        # ================================================================
        self.next_section("krok5")
        zapis2 = zapis("\\langle -1", ",\\ ", "3\\rangle")

        dol = Dot(p(2, -1), radius=0.09, color=ZIELONY).set_opacity(0)
        gora = Line(p(-4, 3), p(-2, 3), color=ZIELONY, stroke_width=8)
        kropka_g = Dot(p(-2, 3), radius=0.09, color=ZIELONY).set_opacity(0)
        self.add(dol, kropka_g)
        self.play(
            dol.animate.set_opacity(1),
            Create(gora),
            kropka_g.animate.set_opacity(1),
            run_time=0.8,
        )
        self.play(
            dol.animate.move_to(p(0, -1)),
            kropka_g.animate.move_to(p(0, 3)),
            run_time=1.0,
        )
        zapis2[0].set_color(ZIELONY)
        zapis2[2].set_color(ZIELONY)
        self.play(FadeIn(zapis2[0]), FadeIn(zapis2[2]), run_time=0.7)
        self.zgas(gora, dol, kropka_g, zapis2[0], zapis2[2])
        self.play(FadeIn(zapis2[1]), run_time=0.4)
        poz2 = pozycja_listy(2, "\\langle -1,\\ 3\\rangle")
        self.play(
            Transform(zapis2, poz2[1].copy()),
            FadeIn(poz2[0]),
            FadeOut(pas_wartosci), FadeOut(gora), FadeOut(dol),
            FadeOut(kropka_g),
            run_time=1.2,
        )
        self.remove(zapis2)
        self.add(poz2)
        self.wait(0.6)

        # ================================================================
        # KROK 6. Trzecia czesc: fragment wykresu pod osia zapala sie
        # jednym ciagiem i rzutuje na os x.
        # ================================================================
        self.next_section("krok6")
        et3 = self.etykieta("3. Wartości ujemne")
        self.play(FadeOut(et2), FadeIn(et3), run_time=0.5)
        fragment = VMobject(color=ZIELONY, stroke_width=8)
        fragment.set_points_as_corners([p(1, 0), p(2, -1), p(3, 0)])
        self.play(Create(fragment), run_time=1.1)
        pas_ujemne = Line(p(1, 0), p(3, 0), color=ZIELONY, stroke_width=8)
        self.play(Create(pas_ujemne), run_time=0.7)
        self.zgas(pas_ujemne)
        self.zamknij(fragment)
        self.wait(0.6)

        # ================================================================
        # KROK 7. Oba konce sa wylaczone, bo w tych punktach wartosc jest
        # zerem, a zero nie jest ujemne. Przedzial powstaje od razu.
        # ================================================================
        self.next_section("krok7")
        zapis3 = zapis("(1", ",\\ ", "3)")
        pusta_l = Circle(
            radius=0.09, color=ZIELONY, stroke_width=5,
            fill_color=WHITE, fill_opacity=1,
        ).move_to(p(1, 0))
        pusta_p = Circle(
            radius=0.09, color=ZIELONY, stroke_width=5,
            fill_color=WHITE, fill_opacity=1,
        ).move_to(p(3, 0))
        self.play(FadeIn(pusta_l), FadeIn(pusta_p), run_time=0.6)
        zapis3[0].set_color(ZIELONY)
        zapis3[2].set_color(ZIELONY)
        self.play(FadeIn(zapis3[0]), FadeIn(zapis3[2]), run_time=0.7)
        self.zgas(pusta_l, pusta_p, zapis3[0], zapis3[2])
        self.play(FadeIn(zapis3[1]), run_time=0.4)
        poz3 = pozycja_listy(3, "(1,\\ 3)")
        self.play(
            Transform(zapis3, poz3[1].copy()),
            FadeIn(poz3[0]),
            FadeOut(pas_ujemne), FadeOut(pusta_l), FadeOut(pusta_p),
            run_time=1.2,
        )
        self.remove(zapis3)
        self.add(poz3)
        self.wait(0.6)

        # ================================================================
        # KROK 8. Czwarta czesc: najwieksza wartosc to 3. Rysujemy ten
        # poziom przez caly wykres.
        # ================================================================
        self.next_section("krok8")
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
        # KROK 9. Na tej wysokosci lezy poziomy odcinek. Rzut na os x,
        # z pusta kropka w -4 i pelna w -2, i od razu przedzial na liste.
        # Etykieta czesci znika: na koniec w kadrze zostaje sam wykres
        # i cztery odpowiedzi (Henrich, 2026-08-28).
        # ================================================================
        self.next_section("krok9")
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
        self.zgas(pas_max, koniec_a, koniec_b, odcinek_max)
        self.play(FadeOut(rzut_a), FadeOut(rzut_b), FadeOut(odcinek_max),
                  run_time=0.35)

        zapis4 = MathTex("(-4,\\ -2\\rangle", color=BLACK, font_size=60)
        zapis4.move_to([KOLUMNA_X, ZAPIS_Y, 0])
        self.play(
            ReplacementTransform(VGroup(pas_max, koniec_a, koniec_b), zapis4),
            run_time=1.0,
        )
        poz4 = pozycja_listy(4, "(-4,\\ -2\\rangle")
        self.play(
            Transform(zapis4, poz4[1].copy()),
            FadeIn(poz4[0]),
            FadeOut(poziom), FadeOut(podpis_poziom), FadeOut(et4),
            run_time=1.2,
        )
        self.remove(zapis4)
        self.add(poz4)
        self.wait(0.5)
