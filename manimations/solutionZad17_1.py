import math

import numpy as np
from manim import *

# Zadanie 17.1 (zamkniete, 1 pkt). Trojkat prostokatny ABC, kat prosty przy A,
# |AC| = sqrt(15), |BC| = 8. Szukamy sin(kata ABC). Wynik: sqrt(15)/8, odpowiedz D.
#
# Projekt: issues/projekt-zad17-2024-grudzien.md. Szesc krokow, jeden do jednego
# z szescioma linijkami rachunku w solutionText.
#
# Uklad kadru (README, punkt 35: trzy pasy, zawsze te same):
#   - LEWA polowa: rysunek z arkusza (matura/2024-grudzien/media/zad17/zad17.png),
#     te same oznaczenia i te same podpisy bokow. Stoi w kadrze przez caly film,
#     bo cale zadanie polega na czytaniu z niego rol bokow.
#   - PRAWA polowa, cztery pasy: pas odczytu u gory (mniejszym pismem, README
#     punkt 41), pod nim glowny rachunek, pod nim pas sprawdzenia, na dole werdykt.
#
# Cala trudnosc zadania to dopasowanie dwoch bokow do dwoch miejsc we wzorze,
# dlatego kroki 1 i 2 nazywaja te boki OSOBNO, z osobnym uzasadnieniem: krok 1
# zapala przeciwprostokatna (bok naprzeciw kata prostego), krok 2 bok lezacy
# naprzeciw pytanego kata. Dystraktor B (7/8) to cosinus, czyli bok przylegly.
#
# Kolor: zielone = to, na co uczen ma w danym kroku patrzec i co sie zmienia.
# Rysunek jest czarny (jak w arkuszu), kat i podpisy szare.
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
SZEROKOSC_RYSUNKU = 5.4
SRODEK_RYSUNKU = np.array([-4.15, -0.15, 0.0])

KOLUMNA_X = 3.15
PAS_Y = 2.95
RACHUNEK_Y = 0.35
SPRAWDZENIE_Y = -1.60
WERDYKT_Y = -2.95


class Zad17_1(Scene):

    # ---- klocki -------------------------------------------------------

    def stan(self, *args, rozmiar=54):
        m = MathTex(*args)
        m.set_color(BLACK)
        m.font_size = rozmiar
        return m

    def ulamek(self, gora, dol, rozmiar=54):
        """Ulamek zlozony recznie: licznik, kreska, mianownik. Daje osobny
        uchwyt do licznika i mianownika, czego \\dfrac w jednym MathTeksie
        nie daje (wzorzec z solutionZad11.py)."""
        g = self.stan(*gora, rozmiar=rozmiar)
        d = self.stan(*dol, rozmiar=rozmiar)
        szer = max(g.width, d.width) + 0.20
        kreska = Line(LEFT * szer / 2, RIGHT * szer / 2, color=BLACK, stroke_width=4)
        g.next_to(kreska, UP, buff=0.13)
        d.next_to(kreska, DOWN, buff=0.13)
        return VGroup(g, kreska, d)

    def zgas(self, *mobiekty, czas=0.4):
        """Gasi zielone na czarno. Wolane PRZED koncowym postojem, zeby ostatnia
        klatka kroku byla czysta (README, zasada 1)."""
        if mobiekty:
            self.play(*[m.animate.set_color(BLACK) for m in mobiekty], run_time=czas)

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

        r["etyk_a"] = MathTex("A", color=BLACK, font_size=40).next_to(A, DOWN + LEFT, buff=0.10)
        r["etyk_b"] = MathTex("B", color=BLACK, font_size=40).next_to(B, DOWN + RIGHT, buff=0.10)
        r["etyk_c"] = MathTex("C", color=BLACK, font_size=40).next_to(C, UP + LEFT, buff=0.10)
        r["etyk_d"] = MathTex("D", color=BLACK, font_size=40).next_to(D, DOWN, buff=0.22)

        r["dl_ac"] = MathTex(r"\sqrt{15}", color=BLACK, font_size=40)
        r["dl_ac"].next_to(Line(A, C).get_center(), LEFT, buff=0.22)
        r["dl_cb"] = MathTex("8", color=BLACK, font_size=40)
        r["dl_cb"].next_to(Line(C, B).get_center(), UP + RIGHT, buff=0.10)
        r["dl_db"] = MathTex("6", color=BLACK, font_size=40)
        r["dl_db"].next_to(Line(D, B).get_center(), DOWN, buff=0.22)

        grupa = VGroup(*r.values())
        grupa.scale_to_fit_width(SZEROKOSC_RYSUNKU)
        grupa.move_to(SRODEK_RYSUNKU)
        return grupa

    # ---- scena --------------------------------------------------------

    def construct(self):
        rysunek = self.zbuduj_rysunek()
        r = self.rys
        widoczne_od_startu = VGroup(
            r["bok_ac"], r["bok_cb"], r["bok_ad"], r["bok_db"], r["odc_cd"],
            r["kat_prosty"], r["etyk_a"], r["etyk_b"], r["etyk_c"], r["etyk_d"],
            r["dl_ac"], r["dl_cb"], r["dl_db"],
        )

        # ================================================================
        # PRAWA POLOWA
        # ================================================================
        pas_bc = self.stan("|BC|", "=", "8", rozmiar=38)
        pas_ac = self.stan("|AC|", "=", r"\sqrt{15}", rozmiar=38)
        pas = VGroup(pas_bc, pas_ac).arrange(RIGHT, buff=0.85)
        pas.move_to([KOLUMNA_X, PAS_Y, 0])

        def wiersz(*czesci, buff=0.20):
            return VGroup(*czesci).arrange(RIGHT, buff=buff)

        w3 = wiersz(self.stan(r"\sin", r"\alpha"), self.stan("="),
                    self.ulamek(("a",), ("c",)))
        w4 = wiersz(self.stan(r"\sin", r"(\angle ABC)"), self.stan("="),
                    self.ulamek(("|AC|",), ("|BC|",)))
        w5 = wiersz(self.stan(r"\sin", r"(\angle ABC)"), self.stan("="),
                    self.ulamek((r"\sqrt{15}",), ("8",)))

        # Rzedy wyrownane po znaku rownosci, a nie po srodku: inaczej lewa strona
        # dryfuje w bok przy kazdym przeksztalceniu, mimo ze sie nie zmienia.
        for w in (w3, w4, w5):
            w.move_to([KOLUMNA_X, RACHUNEK_Y, 0])
            w.shift(RIGHT * (KOLUMNA_X - w[1].get_center()[0]))

        # Pas sprawdzenia: rachunek pomocniczy (mniejszym pismem, README punkt 29)
        # i linijka, ktora po nim zostaje.
        ogniwo = self.stan(r"\sqrt{15}", "<", r"\sqrt{16}", "=", "4", rozmiar=40)
        ogniwo.move_to([KOLUMNA_X, SPRAWDZENIE_Y, 0])
        w6 = wiersz(self.ulamek((r"\sqrt{15}",), ("8",), rozmiar=44),
                    self.stan("<", rozmiar=44), self.stan("1", rozmiar=44))
        w6.move_to([KOLUMNA_X, SPRAWDZENIE_Y, 0])

        werdykt = Text("Odpowiedź D", font_size=34, weight=BOLD, color=BLACK)
        werdykt.move_to([KOLUMNA_X, WERDYKT_Y, 0])

        def przywolaj(zrodla, cele, czas=1.0, luk=-PI / 4):
            """Kopie wartosci z pasa odczytu leca na miejsca liter we wzorze
            (README, punkty 37 i 38). Zielone, bo to one sie w tym kroku zmieniaja."""
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

        # ================================================================
        # KROK 1. Kat prosty przy A wskazuje przeciwprostokatna: bok lezacy
        # naprzeciw niego, czyli BC. Zielony jest kwadracik (od niego zaczyna
        # sie mysl) i sam bok BC z podpisem.
        # ================================================================
        self.next_section("krok1")
        self.play(FadeIn(widoczne_od_startu), run_time=1.0)
        self.wait(0.35)

        self.play(r["kat_prosty"].animate.set_color(ZIELONY), run_time=0.4)
        self.play(
            r["bok_cb"].animate.set_color(ZIELONY),
            r["dl_cb"].animate.set_color(ZIELONY),
            run_time=0.7,
        )
        kopia = przywolaj([r["dl_cb"]], [pas_bc[2].get_center()], czas=1.0)
        pas_bc[2].set_color(ZIELONY)
        self.play(
            FadeIn(pas_bc[0], pas_bc[1]),
            ReplacementTransform(kopia[0], pas_bc[2]),
            run_time=0.9,
        )
        self.zgas(r["kat_prosty"], r["bok_cb"], r["dl_cb"], pas_bc[2])
        self.postoj()

        # ================================================================
        # KROK 2. Pytany kat siedzi przy B. Naprzeciw niego lezy bok AC.
        # Zielony jest luk kata i bok AC z podpisem. Luk zostaje w kadrze
        # do konca filmu, bo to on mowi, o ktory kat chodzi.
        # ================================================================
        self.next_section("krok2")
        r["luk_b"].set_color(ZIELONY)
        self.play(Create(r["luk_b"]), run_time=0.7)
        self.play(
            r["bok_ac"].animate.set_color(ZIELONY),
            r["dl_ac"].animate.set_color(ZIELONY),
            run_time=0.7,
        )
        kopia = przywolaj([r["dl_ac"]], [pas_ac[2].get_center()], czas=1.0)
        pas_ac[2].set_color(ZIELONY)
        self.play(
            FadeIn(pas_ac[0], pas_ac[1]),
            ReplacementTransform(kopia[0], pas_ac[2]),
            run_time=0.9,
        )
        self.zgas(r["bok_ac"], r["dl_ac"], pas_ac[2])
        self.play(r["luk_b"].animate.set_color(SZARY), run_time=0.35)
        self.postoj()

        # ================================================================
        # KROK 3. Wzor z tablicy, strona 11. Bez koloru: nic sie tu jeszcze
        # nie przelicza (README, punkt 12).
        # ================================================================
        self.next_section("krok3")
        self.play(FadeIn(w3), run_time=0.9)
        self.postoj()

        # ================================================================
        # KROK 4. Litery wzoru zamieniaja sie w nazwy bokow. Zielone sa trzy
        # nowe zapisy, bo kazdy z nich zmienia znaczenie: alfa staje sie NASZYM
        # katem, a litery a i c naszymi bokami. Rownoczesnie na rysunku zapalaja
        # sie oba boki, po jednym na litere.
        # ================================================================
        self.next_section("krok4")
        licz3, kreska3, mian3 = w3[2]
        licz4, kreska4, mian4 = w4[2]
        for m in (w4[0][1], licz4, mian4):
            m.set_color(ZIELONY)
        self.play(
            w3[0][1].animate.set_color(ZIELONY),
            licz3.animate.set_color(ZIELONY),
            mian3.animate.set_color(ZIELONY),
            run_time=0.4,
        )
        self.play(
            ReplacementTransform(w3[0][0], w4[0][0]),
            ReplacementTransform(w3[0][1], w4[0][1]),
            ReplacementTransform(w3[1], w4[1]),
            ReplacementTransform(kreska3, kreska4),
            ReplacementTransform(licz3, licz4),
            ReplacementTransform(mian3, mian4),
            r["bok_ac"].animate.set_color(ZIELONY),
            r["bok_cb"].animate.set_color(ZIELONY),
            run_time=1.4,
        )
        self.zgas(w4[0][1], licz4, mian4, r["bok_ac"], r["bok_cb"])
        self.postoj()

        # ================================================================
        # KROK 5. Nazwy bokow zamieniaja sie w liczby, ktore przylatuja z pasa
        # odczytu, czyli stamtad, gdzie je odczytalismy (README, punkt 38).
        # ================================================================
        self.next_section("krok5")
        licz5, kreska5, mian5 = w5[2]
        kopie = przywolaj(
            [pas_ac[2], pas_bc[2]],
            [licz4.get_center(), mian4.get_center()],
            czas=1.1,
        )
        licz5.set_color(ZIELONY)
        mian5.set_color(ZIELONY)
        self.play(
            ReplacementTransform(w4[0][0], w5[0][0]),
            ReplacementTransform(w4[0][1], w5[0][1]),
            ReplacementTransform(w4[1], w5[1]),
            ReplacementTransform(kreska4, kreska5),
            ReplacementTransform(kopie[0], licz5),
            ReplacementTransform(kopie[1], mian5),
            FadeOut(licz4, scale=0.4),
            FadeOut(mian4, scale=0.4),
            run_time=1.4,
        )
        self.play(FadeIn(werdykt), run_time=0.5)
        self.zgas(licz5, mian5)
        self.postoj()

        # ================================================================
        # KROK 6. Sprawdzenie sensu. Przeciwprostokatna jest najdluzszym bokiem,
        # wiec sinus kata ostrego nie moze wyjsc wiekszy od 1. Ogniwo
        # sqrt(15) < sqrt(16) = 4 stoi mniejszym pismem i znika przed koncem
        # kroku (README, punkt 29); to samo ogniwo niesie komentarz w solutionText.
        # ================================================================
        self.next_section("krok6")
        self.play(r["bok_cb"].animate.set_color(ZIELONY), run_time=0.4)
        self.play(FadeIn(ogniwo), run_time=0.7)
        self.wait(0.6)

        licz6, kreska6, mian6 = w6[0]
        kopie = przywolaj(
            [licz5, mian5],
            [licz6.get_center(), mian6.get_center()],
            czas=1.0, luk=PI / 3,
        )
        w6[1].set_color(ZIELONY)
        w6[2].set_color(ZIELONY)
        self.play(
            FadeOut(ogniwo, shift=DOWN * 0.3),
            ReplacementTransform(kopie[0], licz6),
            ReplacementTransform(kopie[1], mian6),
            FadeIn(kreska6), FadeIn(w6[1]), FadeIn(w6[2]),
            run_time=1.2,
        )
        self.zgas(licz6, mian6, w6[1], w6[2], r["bok_cb"])
        self.postoj()
