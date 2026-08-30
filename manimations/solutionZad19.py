import math

import numpy as np
from manim import *

# Zadanie 19 (otwarte, 4 pkt). Trapez prostokatny ABCD, |AB| = 7,5, przekatna
# |AC| = 6 dzieli go na dwa trojkaty prostokatne. Szukane pole trapezu.
# Wynik: P = 22,14.
#
# WERSJA DRUGA, 2026-08-30. Pierwsza (Sonnet) liczyla przez cosinus i sinus
# kata BAC i zostala odrzucona przez Henricha w calosci: „nie baw sie
# w pokazywanie sinusa, znajdz inna jak najprostsza do zrozumienia droge,
# sugeruje podobienstwo trojkatow, bo mozna to fajnie pokazac przez animacje
# przeniesienia i przekrecania jednego trojkata w miejsce drugiego".
#
# Projekt: issues/projekt-zad19-2024-grudzien.md. Siedemnascie krokow.
#
# Droga rachunku (wybor Henricha, inna niz Sposob I w kluczu CKE):
#   1. |BC| = 4,5 z twierdzenia Pitagorasa w trojkacie ABC,
#   2. trojkaty ACD i ABC sa podobne, skala k = 6 : 7,5 = 0,8,
#   3. |DC| = 6 * 0,8 = 4,8 oraz |AD| = 4,5 * 0,8 = 3,6,
#   4. P = (7,5 + 4,8)/2 * 3,6 = 22,14.
# Uczen nie rozwiazuje zadnej proporcji: obie brakujace dlugosci wychodza
# zwyklym mnozeniem przez skale, a skala jest liczba, ktora widac w animacji.
#
# ODPOWIEDNIOSC WIERZCHOLKOW: C -> A, D -> C, A -> B. Zmierzone (a nie
# zgadniete): przy tej odpowiedniosci trojka (D, C, A) ma orientacje przeciwna
# do swojego obrazu (C, A, B), wiec podobienstwo jest ODWROTNE. Sam obrot
# w plaszczyznie nie nalozy malego trojkata na duzy, trzeba go najpierw
# PRZEKRECIC na druga strone jak kartke. Dlatego krok 9 zaczyna sie od
# Rotate(..., axis=UP), czyli od przekrecenia, a nie od obrotu.
#
# Uklad kadru (README, punkt 35: trzy pasy, zawsze te same):
#   - lewa polowa: rysunek trapezu w PRAWDZIWYCH proporcjach (bez tego
#     nakladanie trojkatow by sie nie zgadzalo). Podpisy 7,5 i 6 stoja od
#     poczatku, a 4,5, 4,8 i 3,6 dopisuja sie w chwili policzenia,
#   - prawa polowa: jedna linijka rachunku, nad nia wzor z tablicy,
#   - prawa polowa jest wolna od kroku 9, wiec tam laduje przekrecana kopia
#     malego trojkata (warsztat).
#
# Wzory z tablicy: [10.1] Pitagoras (s. 15), [10.8] cechy podobienstwa (s. 17),
# [10.17] pole trapezu (s. 20).
#
# Render: manim --save_sections solutionZad19.py Zad19
#         (albo tools/wgraj-kroki.sh 19)

ZIELONY = "#2e7d32"
SZARY = "#666666"

# Geometria w jednostkach zadania. Wszystko wynika z danych: |AB| = 7,5,
# |AC| = 6, kat prosty przy C, wiec |BC| = 4,5, |AD| = 3,6 i |DC| = 4,8.
PKT_A = np.array([0.0, 0.0, 0.0])
PKT_B = np.array([7.5, 0.0, 0.0])
PKT_C = np.array([4.8, 3.6, 0.0])
PKT_D = np.array([0.0, 3.6, 0.0])

SZEROKOSC_RYSUNKU = 6.5
SRODEK_RYSUNKU = np.array([-3.65, -0.35, 0.0])

KOLUMNA_X = 3.60
WZOR_Y = 1.85
RACHUNEK_Y = 0.10
WARSZTAT = np.array([KOLUMNA_X, -0.10, 0.0])

# Rysunek to duzo drobnego szczegolu, wiec przytrzymanie 0,45 s zamiast 0,25 s
# (README, punkt 47).
POSTOJ = 0.45


class Zad19(Scene):

    # ---- klocki -------------------------------------------------------

    def stan(self, *args, rozmiar=62):
        m = MathTex(*args)
        m.set_color(BLACK)
        m.font_size = rozmiar
        return m

    def ulamek(self, gora, dol, rozmiar=62):
        """Ulamek zlozony recznie: licznik, kreska, mianownik. Daje osobny
        uchwyt do licznika, czego \\dfrac w jednym MathTeksie nie daje
        (wzorzec z solutionZad17_1.py)."""
        g = self.stan(*gora, rozmiar=rozmiar)
        d = self.stan(*dol, rozmiar=rozmiar)
        szer = max(g.width, d.width) + 0.24
        kreska = Line(LEFT * szer / 2, RIGHT * szer / 2, color=BLACK, stroke_width=4)
        g.next_to(kreska, UP, buff=0.14)
        d.next_to(kreska, DOWN, buff=0.14)
        return VGroup(g, kreska, d)

    def postoj(self):
        self.wait(POSTOJ)

    def zapal(self, *mobiekty, czas=0.4):
        if mobiekty:
            self.play(*[m.animate.set_color(ZIELONY) for m in mobiekty], run_time=czas)

    def zgas(self, *mobiekty, czas=0.4):
        if mobiekty:
            self.play(*[m.animate.set_color(BLACK) for m in mobiekty], run_time=czas)

    # ---- rysunek ------------------------------------------------------

    def zbuduj_rysunek(self):
        """Trapez z arkusza. WSZYSTKIE elementy powstaja tutaj, takze te
        odslaniane pozniej, zeby wspolne skalowanie grupy zlapalo je razem
        z reszta i nie roznily sie wielkoscia."""
        A, B, C, D = PKT_A, PKT_B, PKT_C, PKT_D
        r = self.rys = {}

        r["bok_ab"] = Line(A, B, color=BLACK, stroke_width=5)
        r["bok_bc"] = Line(B, C, color=BLACK, stroke_width=5)
        r["bok_cd"] = Line(C, D, color=BLACK, stroke_width=5)
        r["bok_da"] = Line(D, A, color=BLACK, stroke_width=5)
        r["przekatna"] = Line(A, C, color=BLACK, stroke_width=5)

        # Kwadraciki katow prostych rysowane jak na kartce, z dwoch odcinkow.
        bok = 0.34

        def kwadracik(wierzcholek, p1, p2):
            u = normalize(p1 - wierzcholek)
            v = normalize(p2 - wierzcholek)
            return VMobject(color=BLACK, stroke_width=4).set_points_as_corners([
                wierzcholek + u * bok,
                wierzcholek + (u + v) * bok,
                wierzcholek + v * bok,
            ])

        r["kat_prosty_d"] = kwadracik(D, A, C)
        r["kat_prosty_c"] = kwadracik(C, A, B)

        # Luki obu rownych katow. Katy licze recznie, bo Angle() wymaga
        # podania cwiartki i przy ramionach skierowanych w lewo latwo trafic
        # w ten drugi kat.
        kier = math.atan2(PKT_C[1], PKT_C[0])          # 36,87 stopnia
        r["luk_a"] = Arc(radius=1.30, start_angle=0.0, angle=kier,
                         arc_center=A, color=SZARY, stroke_width=5)
        r["luk_c"] = Arc(radius=1.30, start_angle=PI, angle=kier,
                         arc_center=C, color=SZARY, stroke_width=5)

        r["etyk_a"] = MathTex("A", color=BLACK, font_size=44).next_to(A, DOWN + LEFT, buff=0.12)
        r["etyk_b"] = MathTex("B", color=BLACK, font_size=44).next_to(B, DOWN + RIGHT, buff=0.12)
        r["etyk_c"] = MathTex("C", color=BLACK, font_size=44).next_to(C, UP + RIGHT, buff=0.12)
        r["etyk_d"] = MathTex("D", color=BLACK, font_size=44).next_to(D, UP + LEFT, buff=0.12)

        # Podpisy dlugosci sa WIEKSZE od nazw wierzcholkow: to one wchodza do
        # rachunku, a litery tylko mowia, gdzie co lezy.
        r["dl_ab"] = MathTex("7{,}5", color=BLACK, font_size=54)
        r["dl_ab"].next_to((A + B) / 2, DOWN, buff=0.30)
        r["dl_ac"] = MathTex("6", color=BLACK, font_size=54)
        r["dl_ac"].next_to((A + C) / 2, UP + LEFT, buff=0.10)
        r["dl_bc"] = MathTex("4{,}5", color=BLACK, font_size=54)
        r["dl_bc"].next_to((B + C) / 2, RIGHT, buff=0.18)
        r["dl_dc"] = MathTex("4{,}8", color=BLACK, font_size=54)
        r["dl_dc"].next_to((D + C) / 2, UP, buff=0.20)
        r["dl_ad"] = MathTex("3{,}6", color=BLACK, font_size=54)
        r["dl_ad"].next_to((D + A) / 2, LEFT, buff=0.22)

        # Dwa niewidzialne wielokaty: uchwyty do trojkatow, z ktorych robi sie
        # kopie w krokach 9 i 10. Sa w grupie, wiec skaluja sie razem z reszta
        # rysunku i ich wierzcholki mozna czytac juz w jednostkach ekranu.
        r["troj_maly"] = Polygon(A, C, D, stroke_opacity=0, fill_opacity=0)
        r["troj_duzy"] = Polygon(A, B, C, stroke_opacity=0, fill_opacity=0)

        grupa = VGroup(*r.values())
        grupa.scale_to_fit_width(SZEROKOSC_RYSUNKU)
        grupa.move_to(SRODEK_RYSUNKU)
        return grupa

    # ---- scena --------------------------------------------------------

    def construct(self):
        self.zbuduj_rysunek()
        r = self.rys

        rysunek = VGroup(
            r["bok_ab"], r["bok_bc"], r["bok_cd"], r["bok_da"], r["przekatna"],
            r["kat_prosty_d"], r["kat_prosty_c"],
            r["etyk_a"], r["etyk_b"], r["etyk_c"], r["etyk_d"],
            r["dl_ab"], r["dl_ac"],
        )

        # ================================================================
        # PRAWA POLOWA: wzory z tablicy i kolejne stany rachunku
        # ================================================================
        wzor_pit = self.stan("a", "^{2}", "+", "b", "^{2}", "=", "c", "^{2}", rozmiar=54)
        wzor_pole = VGroup(
            self.stan("P", "=", rozmiar=54),
            self.ulamek(("a", "+", "b"), ("2",), rozmiar=54),
            self.stan(r"\cdot", "h", rozmiar=54),
        ).arrange(RIGHT, buff=0.18)
        for w in (wzor_pit, wzor_pole):
            w.move_to([KOLUMNA_X, WZOR_Y, 0])

        s3 = self.stan("6", "^{2}", "+", "|BC|", "^{2}", "=", "7{,}5", "^{2}")
        s4 = self.stan("|BC|", "^{2}", "=", "7{,}5", "^{2}", "-", "6", "^{2}")
        s5 = self.stan("|BC|", "^{2}", "=", "56{,}25", "-", "36")
        s6 = self.stan("|BC|", "^{2}", "=", "20{,}25")
        s7 = self.stan("|BC|", "=", "4{,}5")

        s11 = VGroup(
            self.stan("k", "="),
            self.ulamek(("6",), ("7{,}5",)),
            self.stan("=", "0{,}8"),
        ).arrange(RIGHT, buff=0.20)
        s12 = self.stan("|DC|", "=", "6", r"\cdot", "0{,}8", "=", "4{,}8")
        s13 = self.stan("|AD|", "=", "4{,}5", r"\cdot", "0{,}8", "=", "3{,}6")

        s14 = VGroup(
            self.stan("P", "="),
            self.ulamek(("7{,}5", "+", "4{,}8"), ("2",)),
            self.stan(r"\cdot", "3{,}6"),
        ).arrange(RIGHT, buff=0.18)
        s15 = VGroup(
            self.stan("P", "="),
            self.ulamek(("12{,}3",), ("2",)),
            self.stan(r"\cdot", "3{,}6"),
        ).arrange(RIGHT, buff=0.18)
        s16 = self.stan("P", "=", "6{,}15", r"\cdot", "3{,}6")
        s17 = self.stan("P", "=", "22{,}14")

        # Wspolna skala liczona z najszerszego zapisu, zeby litery nie zmienialy
        # wielkosci w trakcie przeksztalcenia (README, workflow).
        rachunki = [s3, s4, s5, s6, s7, s11, s12, s13, s14, s15, s16, s17]
        POLE_PRAWE = config.frame_width / 2 * 0.92
        najszerszy = max(m.width for m in rachunki + [wzor_pit, wzor_pole])
        if najszerszy > POLE_PRAWE:
            wsp = POLE_PRAWE / najszerszy
            for m in rachunki + [wzor_pit, wzor_pole]:
                m.scale(wsp)
        for m in rachunki:
            m.move_to([KOLUMNA_X, RACHUNEK_Y, 0])

        def przylec(zrodlo, cel, czas=1.0, luk=-PI / 4):
            """Kopia liczby z rysunku leci na miejsce we wzorze (README,
            punkt 37): liczba nie pojawia sie znikad, tylko przylatuje stamtad,
            gdzie ja odczytalismy."""
            k = zrodlo.copy()
            self.add(k)
            self.play(
                k.animate.move_to(cel.get_center()).scale(
                    cel.height / max(zrodlo.height, 0.01)),
                run_time=czas, path_arc=luk,
            )
            return k

        # ================================================================
        # KROK 1. Rysunek z arkusza. Nic sie nie liczy, wiec nic nie jest
        # zielone (README, punkt 12).
        # ================================================================
        self.next_section("krok1")
        self.play(FadeIn(rysunek), run_time=1.2)
        self.postoj()

        # ================================================================
        # KROK 2. Przekatna dzieli trapez na dwa trojkaty prostokatne.
        # Bierzemy ten wiekszy: ABC, z przeciwprostokatna AB. Wzor z tablicy
        # wjezdza tu, na koncu kroku, zeby nastepny zaczynal sie od rachunku
        # (README, punkt 53).
        # ================================================================
        self.next_section("krok2")
        obrys = Polygon(*r["troj_duzy"].get_vertices(), color=ZIELONY,
                        stroke_width=7, fill_opacity=0)
        self.play(Create(obrys), run_time=1.1)
        self.wait(0.3)
        self.play(FadeOut(obrys), run_time=0.5)
        self.play(FadeIn(wzor_pit, shift=LEFT * 0.25), run_time=0.8)
        self.postoj()

        # ================================================================
        # KROK 3. Litery zamieniaja sie w liczby, ktore przylatuja z rysunku:
        # 6 to przyprostokatna AC, 7,5 to przeciwprostokatna AB. Druga
        # przyprostokatna jest szukana, wiec zostaje zapisem |BC|.
        # ================================================================
        self.next_section("krok3")
        self.play(
            r["przekatna"].animate.set_color(ZIELONY),
            r["dl_ac"].animate.set_color(ZIELONY),
            r["bok_ab"].animate.set_color(ZIELONY),
            r["dl_ab"].animate.set_color(ZIELONY),
            run_time=0.7,
        )
        kop6 = przylec(r["dl_ac"], s3[0])
        kop75 = przylec(r["dl_ab"], s3[6])
        s3[0].set_color(ZIELONY)
        s3[6].set_color(ZIELONY)
        self.play(
            ReplacementTransform(kop6, s3[0]),
            ReplacementTransform(kop75, s3[6]),
            ReplacementTransform(wzor_pit[1].copy(), s3[1]),
            ReplacementTransform(wzor_pit[2].copy(), s3[2]),
            ReplacementTransform(wzor_pit[3].copy(), s3[3]),
            ReplacementTransform(wzor_pit[4].copy(), s3[4]),
            ReplacementTransform(wzor_pit[5].copy(), s3[5]),
            ReplacementTransform(wzor_pit[7].copy(), s3[7]),
            run_time=1.3,
        )
        self.zgas(s3[0], s3[6], r["przekatna"], r["dl_ac"],
                  r["bok_ab"], r["dl_ab"])
        self.postoj()

        # ================================================================
        # KROK 4. 6^2 przechodzi na druga strone ze zmiana znaku. Leci lukiem
        # NAD znakiem rownosci, a nie przez niego (README, punkt 27).
        # ================================================================
        self.next_section("krok4")
        minus = s4[5]
        minus.set_color(ZIELONY)
        self.play(
            ReplacementTransform(s3[3], s4[0]),
            ReplacementTransform(s3[4], s4[1]),
            ReplacementTransform(s3[5], s4[2]),
            ReplacementTransform(s3[6], s4[3]),
            ReplacementTransform(s3[7], s4[4]),
            ReplacementTransform(s3[0], s4[6], path_arc=-2 * PI / 3),
            ReplacementTransform(s3[1], s4[7], path_arc=-2 * PI / 3),
            FadeOut(s3[2], scale=0.4),
            FadeIn(minus),
            run_time=1.4,
        )
        self.zgas(minus)
        self.postoj()

        # ================================================================
        # KROK 5. Podnosimy obie liczby do kwadratu.
        # ================================================================
        self.next_section("krok5")
        s5[3].set_color(ZIELONY)
        s5[5].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s4[0], s5[0]),
            ReplacementTransform(s4[1], s5[1]),
            ReplacementTransform(s4[2], s5[2]),
            ReplacementTransform(VGroup(s4[3], s4[4]), s5[3]),
            ReplacementTransform(s4[5], s5[4]),
            ReplacementTransform(VGroup(s4[6], s4[7]), s5[5]),
            run_time=1.3,
        )
        self.zgas(s5[3], s5[5])
        self.postoj()

        # ================================================================
        # KROK 6. Odejmowanie.
        # ================================================================
        self.next_section("krok6")
        s6[3].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s5[0], s6[0]),
            ReplacementTransform(s5[1], s6[1]),
            ReplacementTransform(s5[2], s6[2]),
            ReplacementTransform(VGroup(s5[3], s5[4], s5[5]), s6[3]),
            run_time=1.3,
        )
        self.zgas(s6[3])
        self.postoj()

        # ================================================================
        # KROK 7. Pierwiastkujemy obie strony. Kwadrat znika z lewej, a wynik
        # od razu jedzie na rysunek, na bok BC.
        # ================================================================
        self.next_section("krok7")
        s7[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s6[0], s7[0]),
            FadeOut(s6[1], scale=0.4),
            ReplacementTransform(s6[2], s7[1]),
            ReplacementTransform(s6[3], s7[2]),
            run_time=1.3,
        )
        kop45 = s7[2].copy()
        self.add(kop45)
        r["dl_bc"].set_color(ZIELONY)
        self.play(
            kop45.animate.move_to(r["dl_bc"].get_center()).scale(
                r["dl_bc"].height / max(s7[2].height, 0.01)),
            r["bok_bc"].animate.set_color(ZIELONY),
            run_time=1.1, path_arc=PI / 4,
        )
        self.remove(kop45)
        self.add(r["dl_bc"])
        self.zgas(s7[2], r["dl_bc"], r["bok_bc"])
        self.postoj()

        # ================================================================
        # KROK 8. Druga czesc zadania. Rachunek z pierwszej zrobil swoje
        # (4,5 stoi juz na rysunku), wiec schodzi z kadru, a na rysunku
        # pojawiaja sie luki dwoch katow. Sa rowne, bo DC jest rownolegle
        # do AB. Luki sa SZARE: to oznaczenie, nie rachunek (README 36).
        # ================================================================
        self.next_section("krok8")
        self.play(
            FadeOut(s7, shift=RIGHT * 0.3),
            FadeOut(wzor_pit, shift=UP * 0.3),
            run_time=0.9,
        )
        self.play(Create(r["luk_a"]), Create(r["luk_c"]), run_time=1.2)
        self.postoj()

        # ================================================================
        # KROK 9. Kopia malego trojkata odkleja sie od trapezu i staje w prawej
        # polowie w tej samej pozie co duzy. Po drodze PRZEKRECA SIE na druga
        # strone: bez tego nie da sie jej nalozyc, bo podobienstwo tych dwoch
        # trojkatow jest odwrotne (patrz naglowek pliku).
        # ================================================================
        self.next_section("krok9")
        maly = Polygon(*r["troj_maly"].get_vertices(), color=ZIELONY,
                       stroke_width=7, fill_opacity=0)
        maly.set_stroke(opacity=0)
        self.add(maly)
        # Kopia zapala sie ANIMACJA, nie przed pierwszym play: inaczej pierwsza
        # klatka kroku jest juz zielona, a ostatnia klatka kroku 8 czysta.
        self.play(maly.animate.set_stroke(opacity=1), run_time=0.5)
        # Lot GORA, a nie przez rysunek (README, punkt 27): po prostej kopia
        # przechodzilaby po boku BC i po podpisie 4,5.
        self.play(maly.animate.move_to(WARSZTAT), run_time=1.1,
                  path_arc=-PI / 2)
        self.play(Rotate(maly, PI, axis=UP), run_time=1.1)

        # Kat dobierany rachunkiem, a nie na oko: po przekreceniu bok, ktory
        # byl bokiem DC malego trojkata, ma stanac rownolegle do boku AC
        # duzego (to sa boki odpowiadajace sobie).
        W = r["troj_duzy"].get_vertices()      # A, B, C duzego
        wek_cel = W[2] - W[0]                  # A -> C
        V = maly.get_vertices()                # obrazy A, C, D malego
        wek_ter = V[2] - V[1]                  # obraz C -> obraz D, czyli bok DC
        theta = math.atan2(wek_cel[1], wek_cel[0]) - math.atan2(wek_ter[1], wek_ter[0])
        self.play(maly.animate.rotate(theta).move_to(WARSZTAT), run_time=1.2)
        self.postoj()

        # ================================================================
        # KROK 10. Powiekszenie 1,25 raza i nalozenie na duzy trojkat. Kopia
        # pokrywa go dokladnie, wiec widac, ze to ten sam ksztalt. Zielen
        # ZOSTAJE do konca kroku 11, bo z tej kopii odczytujemy skale.
        # ================================================================
        self.next_section("krok10")
        srodek_duzego = Polygon(*W).get_center()
        self.play(
            maly.animate.scale(1.25).move_to(srodek_duzego),
            run_time=1.6,
        )
        # Bok, ktory w malym trojkacie byl przeciwprostokatna, lezy teraz na
        # przeciwprostokatnej duzego. Zeby to bylo widac LICZBAMI, a nie tylko
        # ksztaltem, kopia podpisu 6 jedzie pod bok AB i staje obok 7,5.
        szostka = r["dl_ac"].copy().set_color(ZIELONY)
        self.add(szostka)
        cel_szostki = r["dl_ab"].get_center() + DOWN * r["dl_ab"].height * 1.35
        self.play(szostka.animate.move_to(cel_szostki), run_time=1.1,
                  path_arc=PI / 3)
        self.postoj()

        # ================================================================
        # KROK 11. Skala. Bok, ktory w malym trojkacie byl przeciwprostokatna
        # (6), lezy teraz na przeciwprostokatnej duzego (7,5). Kopia zrobila
        # swoje i schodzi z kadru.
        # ================================================================
        self.next_section("krok11")
        self.play(r["dl_ab"].animate.set_color(ZIELONY), run_time=0.5)
        licznik, _, mianownik = s11[1]
        kop_b = przylec(r["dl_ab"], mianownik, czas=1.0)
        licznik.set_color(ZIELONY)
        mianownik.set_color(ZIELONY)
        self.play(
            ReplacementTransform(szostka, licznik),
            ReplacementTransform(kop_b, mianownik),
            FadeIn(s11[0]), FadeIn(s11[1][1]), FadeIn(s11[2]),
            FadeOut(maly),
            run_time=1.3,
        )
        self.zgas(licznik, mianownik, r["dl_ab"])
        self.postoj()

        # ================================================================
        # KROK 12. Bok DC odpowiada bokowi AC duzego trojkata, wiec jest od
        # niego 0,8 raza krotszy. Wynik jedzie na rysunek.
        # ================================================================
        self.next_section("krok12")
        self.play(FadeOut(s11, shift=UP * 0.3), run_time=0.6)
        self.play(
            r["przekatna"].animate.set_color(ZIELONY),
            r["dl_ac"].animate.set_color(ZIELONY),
            r["bok_cd"].animate.set_color(ZIELONY),
            run_time=0.6,
        )
        self.play(FadeIn(s12), run_time=0.9)
        kop48 = s12[6].copy()
        self.add(kop48)
        r["dl_dc"].set_color(ZIELONY)
        self.play(
            kop48.animate.move_to(r["dl_dc"].get_center()).scale(
                r["dl_dc"].height / max(s12[6].height, 0.01)),
            run_time=1.1, path_arc=PI / 4,
        )
        self.remove(kop48)
        self.add(r["dl_dc"])
        self.zgas(r["przekatna"], r["dl_ac"], r["bok_cd"], r["dl_dc"])
        self.postoj()

        # ================================================================
        # KROK 13. Bok AD odpowiada bokowi CB, wiec liczymy tak samo.
        # ================================================================
        self.next_section("krok13")
        self.play(FadeOut(s12, shift=UP * 0.3), run_time=0.6)
        self.play(
            r["bok_bc"].animate.set_color(ZIELONY),
            r["dl_bc"].animate.set_color(ZIELONY),
            r["bok_da"].animate.set_color(ZIELONY),
            run_time=0.6,
        )
        self.play(FadeIn(s13), run_time=0.9)
        kop36 = s13[6].copy()
        self.add(kop36)
        r["dl_ad"].set_color(ZIELONY)
        self.play(
            kop36.animate.move_to(r["dl_ad"].get_center()).scale(
                r["dl_ad"].height / max(s13[6].height, 0.01)),
            run_time=1.1, path_arc=PI / 4,
        )
        self.remove(kop36)
        self.add(r["dl_ad"])
        self.zgas(r["bok_bc"], r["dl_bc"], r["bok_da"], r["dl_ad"])
        self.postoj()

        # ================================================================
        # KROK 14. Wzor na pole trapezu z tablicy. Obie podstawy i wysokosc
        # przylatuja z rysunku na miejsca liter.
        # ================================================================
        self.next_section("krok14")
        self.play(FadeOut(s13, shift=UP * 0.3), run_time=0.6)
        self.play(FadeIn(wzor_pole, shift=LEFT * 0.25), run_time=0.9)
        licznik14 = s14[1][0]
        self.play(
            r["dl_ab"].animate.set_color(ZIELONY),
            r["dl_dc"].animate.set_color(ZIELONY),
            r["dl_ad"].animate.set_color(ZIELONY),
            run_time=0.6,
        )
        k_a = przylec(r["dl_ab"], licznik14[0], czas=1.0)
        k_b = przylec(r["dl_dc"], licznik14[2], czas=1.0)
        k_h = przylec(r["dl_ad"], s14[2][1], czas=1.0)
        licznik14[0].set_color(ZIELONY)
        licznik14[2].set_color(ZIELONY)
        s14[2][1].set_color(ZIELONY)
        self.play(
            ReplacementTransform(k_a, licznik14[0]),
            ReplacementTransform(k_b, licznik14[2]),
            ReplacementTransform(k_h, s14[2][1]),
            FadeIn(s14[0]), FadeIn(licznik14[1]),
            FadeIn(s14[1][1]), FadeIn(s14[1][2]), FadeIn(s14[2][0]),
            run_time=1.3,
        )
        self.zgas(licznik14[0], licznik14[2], s14[2][1],
                  r["dl_ab"], r["dl_dc"], r["dl_ad"])
        self.postoj()

        # ================================================================
        # KROK 15. Dodawanie w liczniku.
        # ================================================================
        self.next_section("krok15")
        s15[1][0].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s14[0], s15[0]),
            ReplacementTransform(s14[1][0], s15[1][0]),
            ReplacementTransform(s14[1][1], s15[1][1]),
            ReplacementTransform(s14[1][2], s15[1][2]),
            ReplacementTransform(s14[2], s15[2]),
            run_time=1.3,
        )
        self.zgas(s15[1][0])
        self.postoj()

        # ================================================================
        # KROK 16. Dzielenie przez 2.
        # ================================================================
        self.next_section("krok16")
        s16[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s15[0][0], s16[0]),
            ReplacementTransform(s15[0][1], s16[1]),
            ReplacementTransform(s15[1], s16[2]),
            ReplacementTransform(s15[2][0], s16[3]),
            ReplacementTransform(s15[2][1], s16[4]),
            run_time=1.3,
        )
        self.zgas(s16[2])
        self.postoj()

        # ================================================================
        # KROK 17. Mnozenie i wynik.
        # ================================================================
        self.next_section("krok17")
        s17[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s16[0], s17[0]),
            ReplacementTransform(s16[1], s17[1]),
            ReplacementTransform(VGroup(s16[2], s16[3], s16[4]), s17[2]),
            FadeOut(wzor_pole, shift=UP * 0.3),
            run_time=1.4,
        )
        self.zgas(s17[2])
        self.postoj()
