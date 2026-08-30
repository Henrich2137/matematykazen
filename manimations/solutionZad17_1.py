import math

import numpy as np
from manim import *

# Zadanie 17.1 (zamkniete, 1 pkt). Trojkat prostokatny ABC, kat prosty przy A,
# |AC| = sqrt(15), |BC| = 8. Szukamy sinusa kata ABC. Wynik sqrt(15)/8, odpowiedz D.
#
# WERSJA DRUGA, 2026-08-30. Pierwsza (szesc krokow, pas odczytu z |BC| = 8
# i |AC| = sqrt(15) w prawym gornym rogu) zostala przez Henricha odrzucona
# w calosci. Cztery jego uwagi i co z nich wyszlo:
#
#   1. „niektore napisy sa za male" -> rysunek jest szerszy (6.6 zamiast 5.4),
#      a podpisy bokow i wierzcholkow ida wieksza czcionka. Prawa polowa niesie
#      dzis tylko JEDNA linijke rachunku, wiec jest na to miejsce.
#   2. „spraw aby na rysunku boki 8 i pierwiastek 15 zostawaly podswietlone
#      razem z tymi wartosciami we wzorze sinusa" -> zielen NIE gasnie na koncu
#      kroku. Bok AC i licznik zapalaja sie razem w kroku 3 i zostaja zielone
#      do konca filmu; bok BC i mianownik tak samo od kroku 4. Uczen w kazdej
#      chwili widzi, ktora liczba we wzorze to ktory bok.
#   3. „nazwy bokow w stylu |AC|, |BC| sa tutaj niepotrzebne, bo nie ma ich we
#      wzorach" -> zniknal caly posredni stan sin(kat ABC) = |AC|/|BC| i pas
#      odczytu w prawym gornym rogu. Wzor z tablicy jest literowy (a i c),
#      a litery zamieniaja sie WPROST w liczby przylatujace z rysunku.
#   4. „skasuj ostatni krok" -> sprawdzenie sqrt(15)/8 < 1 wypadlo i z filmu,
#      i z rozwiazania zwykłego.
#
# Piec krokow, jeden do jednego z pieciu linijkami w solutionText.
#
# Uklad kadru: rysunek z arkusza na calej lewej polowie (stoi przez caly film,
# bo cale zadanie polega na czytaniu z niego rol bokow), jedna linijka rachunku
# po prawej, werdykt pod nia.
#
# Wzor [9.1] z tablicy, strona 11: sin(alfa) = a/c, gdzie a to przyprostokatna
# lezaca naprzeciw kata alfa, a c przeciwprostokatna. Dystraktor B (7/8) to
# cosinus, czyli bok PRZYLEGLY, dlatego kroki 3 i 4 nazywaja role bokow osobno.
#
# Render: manim --save_sections solutionZad17_1.py Zad17_1
#         (albo tools/wgraj-kroki.sh 17_1)

ZIELONY = "#2e7d32"
SZARY = "#666666"

# Geometria w jednostkach zadania: A w poczatku, B na prawo, C nad A, D na AB.
# Te same wspolrzedne ma scena solutionZad17_2.py i musza sie zgadzac, bo oba
# filmy pokazuja ten sam rysunek.
BOK_AB = 7.0
BOK_AC = math.sqrt(15.0)
ODC_DB = 6.0

JEDNOSTKA = 0.65
SZEROKOSC_RYSUNKU = 6.6
SRODEK_RYSUNKU = np.array([-3.75, -0.25, 0.0])

KOLUMNA_X = 3.70
RACHUNEK_Y = 0.60
WERDYKT_Y = -2.10


class Zad17_1(Scene):

    # ---- klocki -------------------------------------------------------

    def stan(self, *args, rozmiar=64):
        m = MathTex(*args)
        m.set_color(BLACK)
        m.font_size = rozmiar
        return m

    def ulamek(self, gora, dol, rozmiar=64):
        """Ulamek zlozony recznie: licznik, kreska, mianownik. Daje osobny
        uchwyt do licznika i mianownika, czego \\dfrac w jednym MathTeksie
        nie daje (wzorzec z solutionZad11.py)."""
        g = self.stan(*gora, rozmiar=rozmiar)
        d = self.stan(*dol, rozmiar=rozmiar)
        szer = max(g.width, d.width) + 0.24
        kreska = Line(LEFT * szer / 2, RIGHT * szer / 2, color=BLACK, stroke_width=4)
        g.next_to(kreska, UP, buff=0.15)
        d.next_to(kreska, DOWN, buff=0.15)
        return VGroup(g, kreska, d)

    def postoj(self):
        # 0,45 s zamiast 0,25 s: w kadrze stoi rysunek, czyli duzo drobnego
        # szczegolu, a przy krotszym przytrzymaniu styk klatek siada
        # (README, punkt 47).
        self.wait(0.45)

    # ---- rysunek ------------------------------------------------------

    def zbuduj_rysunek(self):
        """Trojkat z arkusza. WSZYSTKIE elementy powstaja tutaj, takze te
        odslaniane pozniej, zeby wspolne skalowanie grupy zlapalo je razem
        z reszta i nie roznily sie wielkoscia."""

        def pkt(x, y):
            return np.array([x * JEDNOSTKA, y * JEDNOSTKA, 0.0])

        A, B, C = pkt(0, 0), pkt(BOK_AB, 0), pkt(0, BOK_AC)
        D = pkt(BOK_AB - ODC_DB, 0)

        r = self.rys = {}
        r["bok_ac"] = Line(A, C, color=BLACK, stroke_width=5)
        r["bok_cb"] = Line(C, B, color=BLACK, stroke_width=5)
        r["bok_ad"] = Line(A, D, color=BLACK, stroke_width=5)
        r["bok_db"] = Line(D, B, color=BLACK, stroke_width=5)
        r["odc_cd"] = Line(C, D, color=BLACK, stroke_width=5)

        # Kwadracik kata prostego przy A, rysowany jak na kartce: dwa odcinki.
        bok = 0.24
        r["kat_prosty"] = VMobject(color=BLACK, stroke_width=4).set_points_as_corners(
            [A + RIGHT * bok, A + RIGHT * bok + UP * bok, A + UP * bok]
        )

        # Luk kata ABC. Katy licze recznie, bo Angle() wymaga podania cwiartki
        # i przy kacie rozwartym w ramionach latwo trafic w ten drugi.
        kier_ba = math.atan2(A[1] - B[1], A[0] - B[0])
        kier_bc = math.atan2(C[1] - B[1], C[0] - B[0])
        r["luk_b"] = Arc(
            radius=0.85, start_angle=kier_bc, angle=kier_ba - kier_bc,
            arc_center=B, color=SZARY, stroke_width=5,
        )
        r["alfa"] = MathTex(r"\alpha", color=SZARY, font_size=46)
        r["alfa"].move_to(B + np.array([-1.35, 0.30, 0.0]))

        r["etyk_a"] = MathTex("A", color=BLACK, font_size=46).next_to(A, DOWN + LEFT, buff=0.10)
        r["etyk_b"] = MathTex("B", color=BLACK, font_size=46).next_to(B, DOWN + RIGHT, buff=0.10)
        r["etyk_c"] = MathTex("C", color=BLACK, font_size=46).next_to(C, UP + LEFT, buff=0.10)
        r["etyk_d"] = MathTex("D", color=BLACK, font_size=46).next_to(D, DOWN, buff=0.24)

        # Podpisy dlugosci sa WIEKSZE od nazw wierzcholkow: to one wchodza do
        # rachunku, a litery A, B, C, D tylko mowia, gdzie co lezy.
        r["dl_ac"] = MathTex(r"\sqrt{15}", color=BLACK, font_size=56)
        r["dl_ac"].next_to(Line(A, C).get_center(), LEFT, buff=0.24)
        r["dl_cb"] = MathTex("8", color=BLACK, font_size=56)
        r["dl_cb"].next_to(Line(C, B).get_center(), UP + RIGHT, buff=0.12)
        r["dl_db"] = MathTex("6", color=BLACK, font_size=56)
        r["dl_db"].next_to(Line(D, B).get_center(), DOWN, buff=0.24)

        grupa = VGroup(*r.values())
        grupa.scale_to_fit_width(SZEROKOSC_RYSUNKU)
        grupa.move_to(SRODEK_RYSUNKU)
        return grupa

    # ---- scena --------------------------------------------------------

    def construct(self):
        self.zbuduj_rysunek()
        r = self.rys
        rysunek = VGroup(
            r["bok_ac"], r["bok_cb"], r["bok_ad"], r["bok_db"], r["odc_cd"],
            r["kat_prosty"], r["etyk_a"], r["etyk_b"], r["etyk_c"], r["etyk_d"],
            r["dl_ac"], r["dl_cb"], r["dl_db"],
        )

        # ================================================================
        # PRAWA POLOWA: jedna linijka rachunku w trzech postaciach.
        # ================================================================
        def wiersz(*czesci, buff=0.22):
            return VGroup(*czesci).arrange(RIGHT, buff=buff)

        w2 = wiersz(self.stan(r"\sin", r"\alpha"), self.stan("="),
                    self.ulamek(("a",), ("c",)))
        w3 = wiersz(self.stan(r"\sin", r"\alpha"), self.stan("="),
                    self.ulamek((r"\sqrt{15}",), ("c",)))
        w4 = wiersz(self.stan(r"\sin", r"\alpha"), self.stan("="),
                    self.ulamek((r"\sqrt{15}",), ("8",)))

        # Rzedy wyrownane po znaku rownosci, a nie po srodku: inaczej lewa strona
        # dryfuje w bok przy kazdym przeksztalceniu, mimo ze sie nie zmienia.
        for w in (w2, w3, w4):
            w.move_to([KOLUMNA_X, RACHUNEK_Y, 0])
            w.shift(RIGHT * (KOLUMNA_X - w[1].get_center()[0]))

        werdykt = Text("Odpowiedź D", font_size=40, weight=BOLD, color=BLACK)
        werdykt.move_to([KOLUMNA_X, WERDYKT_Y, 0])

        def przylec(zrodlo, cel, czas=1.1, luk=-PI / 4):
            """Kopia liczby z rysunku leci na miejsce litery we wzorze
            (README, punkt 37): liczba nie pojawia sie znikad, tylko przylatuje
            stamtad, gdzie ja odczytalismy."""
            k = zrodlo.copy()
            self.add(k)
            self.play(k.animate.move_to(cel.get_center()).scale(
                cel.height / max(zrodlo.height, 0.01)),
                run_time=czas, path_arc=luk)
            return k

        # ================================================================
        # KROK 1. Rysunek z arkusza i nazwanie kata, o ktory pyta zadanie.
        # Luk i litera alfa sa szare: to oznaczenie, nie rachunek (README,
        # punkt 36). Bez zieleni, bo nic sie tu nie przelicza (punkt 12).
        # ================================================================
        self.next_section("krok1")
        self.play(FadeIn(rysunek), run_time=1.1)
        self.wait(0.4)
        self.play(Create(r["luk_b"]), FadeIn(r["alfa"]), run_time=0.8)
        self.postoj()

        # ================================================================
        # KROK 2. Wzor z tablicy, strona 11. Wjezdza bez koloru: to dopiero
        # przepis, jeszcze nie nasze liczby.
        # ================================================================
        self.next_section("krok2")
        self.play(FadeIn(w2, shift=LEFT * 0.25), run_time=0.9)
        self.postoj()

        # ================================================================
        # KROK 3. Litera a to przyprostokatna lezaca NAPRZECIW kata alfa,
        # czyli bok AC. Zapala sie razem z licznikiem, a potem przylatuje
        # z rysunku jego dlugosc. Zielen zostaje do konca filmu: dzieki niej
        # widac, ktora liczba we wzorze jest ktorym bokiem (prosba Henricha).
        # ================================================================
        self.next_section("krok3")
        licz2, kreska2, mian2 = w2[2]
        licz3, kreska3, mian3 = w3[2]
        self.play(
            r["bok_ac"].animate.set_color(ZIELONY),
            r["dl_ac"].animate.set_color(ZIELONY),
            licz2.animate.set_color(ZIELONY),
            run_time=0.8,
        )
        self.wait(0.3)
        kopia = przylec(r["dl_ac"], licz3)
        licz3.set_color(ZIELONY)
        self.play(
            ReplacementTransform(kopia, licz3),
            FadeOut(licz2, scale=0.4),
            ReplacementTransform(kreska2, kreska3),
            ReplacementTransform(mian2, mian3),
            *[ReplacementTransform(w2[i], w3[i]) for i in (0, 1)],
            run_time=1.0,
        )
        self.postoj()

        # ================================================================
        # KROK 4. Litera c to przeciwprostokatna, czyli bok lezacy naprzeciw
        # kata prostego: BC. Ten sam ruch co w kroku 3, druga liczba.
        # ================================================================
        self.next_section("krok4")
        licz4, kreska4, mian4 = w4[2]
        self.play(
            r["kat_prosty"].animate.set_color(ZIELONY),
            run_time=0.5,
        )
        self.play(
            r["bok_cb"].animate.set_color(ZIELONY),
            r["dl_cb"].animate.set_color(ZIELONY),
            mian3.animate.set_color(ZIELONY),
            r["kat_prosty"].animate.set_color(BLACK),
            run_time=0.8,
        )
        self.wait(0.3)
        kopia = przylec(r["dl_cb"], mian4, luk=PI / 4)
        mian4.set_color(ZIELONY)
        licz4.set_color(ZIELONY)
        self.play(
            ReplacementTransform(kopia, mian4),
            FadeOut(mian3, scale=0.4),
            ReplacementTransform(kreska3, kreska4),
            ReplacementTransform(licz3, licz4),
            *[ReplacementTransform(w3[i], w4[i]) for i in (0, 1)],
            run_time=1.0,
        )
        self.postoj()

        # ================================================================
        # KROK 5. Werdykt. Zielone boki i zielone liczby zostaja w kadrze,
        # bo o to prosil Henrich: ostatnia klatka ma pokazywac, skad wzial
        # sie licznik i skad mianownik.
        # ================================================================
        self.next_section("krok5")
        self.play(FadeIn(werdykt, shift=UP * 0.25), run_time=0.8)
        self.postoj()
