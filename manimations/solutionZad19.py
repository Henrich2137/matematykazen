import math

import numpy as np
from manim import *

# Zadanie 19 (otwarte, 4 pkt). Trapez prostokatny ABCD, dluzsza podstawa
# |AB| = 7,5, krotsza przekatna |AC| = 6 dzieli go na dwa trojkaty prostokatne:
# ABC (kat prosty przy C) i ACD (kat prosty przy D). Trzeba obliczyc pole trapezu.
#
# Wspolrzedne dobrane tak, by dawaly DOKLADNIE finalne wyniki (tak jak rysunek
# w arkuszu jest narysowany do prawdziwej skali): A(0,0), B(7,5, 0), C(4,8, 3,6),
# D(0, 3,6). Sprawdzone: |AC| = sqrt(4,8^2+3,6^2) = 6, kat ACB i kat ADC oba 90 st.
#
# Droga: |BC| z Pitagorasa w ABC -> kat alfa = kat CAB = kat DCA (naprzemianlegle,
# DC || AB) -> sin alfa w trojkacie ABC -> |AD| = |AC|*sin alfa w trojkacie ACD
# -> |DC| z Pitagorasa w ACD -> pole trapezu P = (a+b)/2 * h.
#
# 24 kroki, jeden do jednego z liniami solutionText w exercises.json (2024-grudzien,
# zad. 19). Wzory z tablicy: [10.1] Pitagoras a^2+b^2=c^2 (s. 15), [9.1] sin alfa = a/c
# (s. 11), [10.5] a = c*sin alfa (s. 16), [10.17] pole trapezu P=(a+b)/2*h (s. 20).
#
# Render: manim --save_sections solutionZad19.py Zad19
#         (albo tools/wgraj-kroki.sh 19 2024-grudzien)

ZIELONY = "#2e7d32"
CZERWONY = "#c62828"
SZARY = "#666666"

BOK_AB = 7.5
BOK_AC = 6.0
BOK_BC = 4.5
BOK_AD = 3.6
BOK_DC = 4.8

JEDNOSTKA = 0.62
SZEROKOSC_RYSUNKU = 5.6
SRODEK_RYSUNKU = np.array([-3.9, 0.15, 0.0])

KOLUMNA_X = 3.55
PAS_WZOR_Y = 2.35
PAS_GLOWNY_Y = 0.75
PAS_MALY_Y = -1.55
WERDYKT_Y = -3.05


class Zad19(Scene):

    # ---- klocki ---------------------------------------------------------

    def stan(self, *args, rozmiar=58, kolor=BLACK):
        m = MathTex(*args)
        m.set_color(kolor)
        m.font_size = rozmiar
        return m

    def ulamek(self, gora, dol, rozmiar=58, kolor=BLACK):
        g = self.stan(*gora, rozmiar=rozmiar, kolor=kolor)
        d = self.stan(*dol, rozmiar=rozmiar, kolor=kolor)
        szer = max(g.width, d.width) + 0.22
        kreska = Line(LEFT * szer / 2, RIGHT * szer / 2, color=kolor, stroke_width=4)
        g.next_to(kreska, UP, buff=0.14)
        d.next_to(kreska, DOWN, buff=0.14)
        return VGroup(g, kreska, d)

    def wiersz(self, *czesci, buff=0.22):
        return VGroup(*czesci).arrange(RIGHT, buff=buff)

    def postoj(self, dlugosc=0.45):
        # 0,45 s: w kadrze caly czas stoi rysunek (README, punkt 47).
        self.wait(dlugosc)

    def zgas(self, *mobiekty, czas=0.4):
        if mobiekty:
            self.wait(0.3)
            self.play(*[m.animate.set_color(BLACK) for m in mobiekty], run_time=czas)
        # Przytrzymanie PO ściemnieniu (README, workflow pkt 0): bez niego ostatnia
        # klatka sekcji to klatka w trakcie/na koncu Play, nie ustabilizowany stan.
        self.wait(0.25)

    def przylec(self, zrodlo, cel, czas=1.0, luk=-PI / 4):
        """Kopia liczby z rysunku leci na miejsce litery we wzorze (README, pkt 37)."""
        k = zrodlo.copy()
        self.add(k)
        self.play(
            k.animate.move_to(cel.get_center()).scale(
                cel.height / max(zrodlo.height, 0.01)
            ),
            run_time=czas, path_arc=luk,
        )
        return k

    # ---- rysunek ----------------------------------------------------------

    def zbuduj_rysunek(self):
        def pkt(x, y):
            return np.array([x * JEDNOSTKA, y * JEDNOSTKA, 0.0])

        A, B, C, D = pkt(0, 0), pkt(BOK_AB, 0), pkt(4.8, 3.6), pkt(0, 3.6)

        r = self.rys = {}
        r["ab"] = Line(A, B, color=BLACK, stroke_width=5)
        r["bc"] = Line(B, C, color=BLACK, stroke_width=5)
        r["cd"] = Line(C, D, color=BLACK, stroke_width=5)
        r["da"] = Line(D, A, color=BLACK, stroke_width=5)
        r["ac"] = Line(A, C, color=BLACK, stroke_width=5)

        bok = 0.15
        r["kp_d"] = VMobject(color=BLACK, stroke_width=4).set_points_as_corners(
            [D + RIGHT * bok, D + RIGHT * bok + DOWN * bok, D + DOWN * bok]
        )
        r["kp_c"] = VMobject(color=BLACK, stroke_width=4).set_points_as_corners(
            [C + LEFT * bok + DOWN * bok * 0.0, C + LEFT * bok, C + LEFT * bok + DOWN * bok]
        )
        # Kwadracik przy C lezy na dwusiecznej kata ACB (miedzy CB i CA), nie
        # osiowo, bo trojkat ABC jest przy C mocno rozwarty w strone B.
        kier_cb = math.atan2(B[1] - C[1], B[0] - C[0])
        kier_ca = math.atan2(A[1] - C[1], A[0] - C[0])
        r["kp_c"] = VMobject(color=BLACK, stroke_width=4).set_points_as_corners([
            C + bok * np.array([math.cos(kier_cb), math.sin(kier_cb), 0.0]),
            C + bok * np.array([math.cos(kier_cb) + math.cos(kier_ca),
                                 math.sin(kier_cb) + math.sin(kier_ca), 0.0]),
            C + bok * np.array([math.cos(kier_ca), math.sin(kier_ca), 0.0]),
        ])

        # Luki katow alfa: przy A (miedzy AC i AB) i przy C (miedzy CD i CA).
        # Roznica katow znormalizowana do (-pi, pi], inaczej Arc potrafi obiec
        # dlugą stroną (zlapane na luk_c: 323 st. zamiast 37 st.).
        def znorm(a):
            while a <= -math.pi:
                a += 2 * math.pi
            while a > math.pi:
                a -= 2 * math.pi
            return a

        kier_ac = math.atan2(C[1] - A[1], C[0] - A[0])
        kier_ab = math.atan2(B[1] - A[1], B[0] - A[0])
        rozp_a = znorm(kier_ac - kier_ab)
        r["luk_a"] = Arc(radius=0.42, start_angle=kier_ab, angle=rozp_a,
                          arc_center=A, color=SZARY, stroke_width=5)
        dwu_a = kier_ab + rozp_a / 2.0
        r["alfa_a"] = MathTex(r"\alpha", color=SZARY, font_size=36)
        r["alfa_a"].move_to(A + 0.68 * np.array([math.cos(dwu_a), math.sin(dwu_a), 0.0]))

        kier_cd = math.atan2(D[1] - C[1], D[0] - C[0])
        rozp_c = znorm(kier_cd - kier_ca)
        r["luk_c"] = Arc(radius=0.40, start_angle=kier_ca, angle=rozp_c,
                          arc_center=C, color=SZARY, stroke_width=5)
        dwu_c = kier_ca + rozp_c / 2.0
        r["alfa_c"] = MathTex(r"\alpha", color=SZARY, font_size=36)
        r["alfa_c"].move_to(C + 0.62 * np.array([math.cos(dwu_c), math.sin(dwu_c), 0.0]))

        # Grociki rownoleglosci na AB i DC (dwie krotkie kreski w poprzek).
        def grocik(p, kier):
            środek = p
            prost = np.array([-math.sin(kier), math.cos(kier), 0.0]) * 0.075
            wzdluz = np.array([math.cos(kier), math.sin(kier), 0.0]) * 0.06
            return VGroup(
                Line(środek - wzdluz * 1.3 + prost, środek - wzdluz * 1.3 - prost,
                     color=BLACK, stroke_width=3),
                Line(środek - wzdluz * 0.5 + prost, środek - wzdluz * 0.5 - prost,
                     color=BLACK, stroke_width=3),
            )
        r["rown_ab"] = grocik((A + B) / 2, kier_ab)
        r["rown_dc"] = grocik((D + C) / 2, kier_cd + PI)

        r["etyk_a"] = MathTex("A", color=BLACK, font_size=44).next_to(A, DOWN + LEFT, buff=0.08)
        r["etyk_b"] = MathTex("B", color=BLACK, font_size=44).next_to(B, DOWN + RIGHT, buff=0.08)
        r["etyk_c"] = MathTex("C", color=BLACK, font_size=44).next_to(C, UP + RIGHT, buff=0.16)
        r["etyk_d"] = MathTex("D", color=BLACK, font_size=44).next_to(D, UP + LEFT, buff=0.08)

        r["dl_ab"] = MathTex("7{,}5", color=BLACK, font_size=50)
        r["dl_ab"].next_to(Line(A, B).get_center(), DOWN, buff=0.22)
        r["dl_ac"] = MathTex("6", color=BLACK, font_size=50)
        r["dl_ac"].next_to(Line(A, C).get_center(), UP + LEFT, buff=0.16)

        # Wyniki, ktore doklejaja sie w trakcie filmu (na starcie niewidoczne,
        # tworzone tu, zeby wspolne skalowanie zlapalo je razem z reszta).
        r["dl_bc"] = MathTex("4{,}5", color=BLACK, font_size=50)
        r["dl_bc"].next_to(Line(B, C).get_center(), RIGHT, buff=0.18)
        r["dl_ad"] = MathTex("3{,}6", color=BLACK, font_size=50)
        r["dl_ad"].next_to(Line(D, A).get_center(), LEFT, buff=0.18)
        r["dl_dc"] = MathTex("4{,}8", color=BLACK, font_size=50)
        r["dl_dc"].next_to(Line(C, D).get_center(), UP, buff=0.20)

        grupa = VGroup(*r.values())
        grupa.scale_to_fit_width(SZEROKOSC_RYSUNKU)
        grupa.move_to(SRODEK_RYSUNKU)
        return grupa

    # ---- scena --------------------------------------------------------

    def construct(self):
        self.zbuduj_rysunek()
        r = self.rys

        szkielet = VGroup(
            r["ab"], r["bc"], r["cd"], r["da"], r["ac"],
            r["kp_d"], r["kp_c"],
            r["etyk_a"], r["etyk_b"], r["etyk_c"], r["etyk_d"],
            r["dl_ab"], r["dl_ac"],
        )

        # ================================================================
        # KROK 1. Caly rysunek: trapez, przekatna, oba kąty proste.
        # ================================================================
        self.next_section("krok1")
        self.play(FadeIn(szkielet), run_time=1.3)
        self.postoj()

        # ================================================================
        # ETAP 1: |BC| z Pitagorasa w trojkacie ABC.
        # ================================================================

        # KROK 2. Wzor + podstawienie: |BC|^2+6^2=7,5^2.
        self.next_section("krok2")
        wzor1 = self.stan("a^{2}", "+", "b^{2}", "=", "c^{2}", rozmiar=40, kolor=SZARY)
        wzor1.move_to([KOLUMNA_X, PAS_WZOR_Y, 0])
        self.play(FadeIn(wzor1, shift=LEFT * 0.2), run_time=0.7)

        e2 = self.stan(r"|BC|^{2}", "+", "6^{2}", "=", r"7{,}5^{2}")
        e2.move_to([KOLUMNA_X, PAS_GLOWNY_Y, 0])
        self.play(
            r["ac"].animate.set_color(ZIELONY), r["dl_ac"].animate.set_color(ZIELONY),
            r["ab"].animate.set_color(ZIELONY), r["dl_ab"].animate.set_color(ZIELONY),
            FadeIn(e2[0], e2[1], e2[3]),
            run_time=0.8,
        )
        self.wait(0.25)
        k1 = self.przylec(r["dl_ac"], e2[2], czas=0.9, luk=-PI / 5)
        k2 = self.przylec(r["dl_ab"], e2[4], czas=0.9, luk=PI / 5)
        for cz in (e2[2], e2[4]):
            cz.set_color(ZIELONY)
        self.play(ReplacementTransform(k1, e2[2]), ReplacementTransform(k2, e2[4]), run_time=0.6)
        self.zgas(e2, r["ac"], r["dl_ac"], r["ab"], r["dl_ab"])

        # KROK 3. Kwadraty policzone: |BC|^2+36=56,25.
        self.next_section("krok3")
        e3 = self.stan(r"|BC|^{2}", "+", "36", "=", "56{,}25")
        e3.move_to([KOLUMNA_X, PAS_GLOWNY_Y, 0])
        for cz in (e3[2], e3[4]):
            cz.set_color(ZIELONY)
        self.play(
            ReplacementTransform(e2[0], e3[0]), ReplacementTransform(e2[1], e3[1]),
            ReplacementTransform(e2[2], e3[2]), ReplacementTransform(e2[3], e3[3]),
            ReplacementTransform(e2[4], e3[4]),
            run_time=1.0,
        )
        self.zgas(e3[2], e3[4])

        # KROK 4. Trzydziestka szesc przechodzi na druga strone: |BC|^2=56,25-36.
        self.next_section("krok4")
        e4 = self.stan(r"|BC|^{2}", "=", "56{,}25", "-", "36")
        e4.move_to([KOLUMNA_X, PAS_GLOWNY_Y, 0])
        self.play(e3[1].animate.set_color(CZERWONY), e3[2].animate.set_color(ZIELONY), run_time=0.3)
        e4[3].set_color(CZERWONY)
        e4[4].set_color(ZIELONY)
        self.play(
            ReplacementTransform(e3[0], e4[0]),
            ReplacementTransform(e3[3], e4[1]),
            ReplacementTransform(e3[4], e4[2]),
            FadeOut(e3[1], scale=0.4),
            ReplacementTransform(e3[2], e4[4]),
            FadeIn(e4[3]),
            run_time=1.2, path_arc=-2 * PI / 3,
        )
        self.zgas(e4[2], e4[3], e4[4])

        # KROK 5. |BC|^2=20,25.
        self.next_section("krok5")
        e5 = self.stan(r"|BC|^{2}", "=", "20{,}25")
        e5.move_to([KOLUMNA_X, PAS_GLOWNY_Y, 0])
        e5[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(e4[0], e5[0]), ReplacementTransform(e4[1], e5[1]),
            FadeOut(e4[2], scale=0.4), FadeOut(e4[3], scale=0.4),
            ReplacementTransform(e4[4], e5[2]),
            run_time=1.1,
        )
        self.zgas(e5[2])

        # KROK 6. |BC|=4,5, wynik wraca na rysunek.
        self.next_section("krok6")
        e6 = self.stan(r"|BC|", "=", "4{,}5")
        e6.move_to([KOLUMNA_X, PAS_GLOWNY_Y, 0])
        e6[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(e5[0], e6[0]), ReplacementTransform(e5[1], e6[1]),
            ReplacementTransform(e5[2], e6[2]),
            run_time=1.0,
        )
        self.wait(0.3)
        r["dl_bc"].set_color(ZIELONY)
        kop = self.przylec(e6[2], r["dl_bc"], czas=0.9, luk=PI / 4)
        self.play(ReplacementTransform(kop, r["dl_bc"]), run_time=0.5)
        self.wait(0.3)
        self.play(FadeOut(e6, scale=0.4), r["dl_bc"].animate.set_color(BLACK), run_time=0.4)
        self.postoj(0.5)

        # ================================================================
        # KROK 7. Kat alfa: DC rownolegle do AB, kat DCA = kat CAB.
        # ================================================================
        self.next_section("krok7")
        self.play(FadeOut(wzor1, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(r["rown_ab"]), FadeIn(r["rown_dc"]), run_time=0.6)
        self.play(
            Create(r["luk_a"]), FadeIn(r["alfa_a"]),
            Create(r["luk_c"]), FadeIn(r["alfa_c"]),
            run_time=0.9,
        )
        self.postoj()

        # ================================================================
        # ETAP 2: sin alfa w trojkacie ABC.
        # ================================================================

        # KROK 8. Wzor + nazwanie bokow: sin alfa = |BC|/|AB|.
        self.next_section("krok8")
        wzor2b = self.wiersz(
            self.stan(r"\sin\alpha", rozmiar=40, kolor=SZARY),
            self.stan("=", rozmiar=40, kolor=SZARY),
            self.ulamek(("a",), ("c",), rozmiar=40, kolor=SZARY),
        )
        wzor2b.move_to([KOLUMNA_X, PAS_WZOR_Y, 0])
        self.play(FadeIn(wzor2b, shift=LEFT * 0.2), run_time=0.7)

        e8 = self.wiersz(
            self.stan(r"\sin\alpha"), self.stan("="),
            self.ulamek((r"|BC|",), (r"|AB|",)),
        )
        e8.move_to([KOLUMNA_X, PAS_GLOWNY_Y, 0])
        self.play(
            r["bc"].animate.set_color(ZIELONY), r["dl_bc"].animate.set_color(ZIELONY),
            r["ab"].animate.set_color(ZIELONY), r["dl_ab"].animate.set_color(ZIELONY),
            r["luk_a"].animate.set_color(ZIELONY), r["alfa_a"].animate.set_color(ZIELONY),
            FadeIn(e8, shift=UP * 0.2),
            run_time=0.9,
        )
        self.zgas(e8, r["bc"], r["ab"], r["luk_a"], r["alfa_a"], r["dl_bc"], r["dl_ab"])

        # KROK 9. Liczby: sin alfa = 4,5/7,5.
        self.next_section("krok9")
        e9 = self.wiersz(
            self.stan(r"\sin\alpha"), self.stan("="),
            self.ulamek(("4{,}5",), ("7{,}5",)),
        )
        e9.move_to([KOLUMNA_X, PAS_GLOWNY_Y, 0])
        self.play(r["dl_bc"].animate.set_color(ZIELONY), r["dl_ab"].animate.set_color(ZIELONY), run_time=0.4)
        licz9, kreska9, mian9 = e9[2]
        licz8, kreska8, mian8 = e8[2]
        licz9.set_color(ZIELONY)
        mian9.set_color(ZIELONY)
        kk1 = self.przylec(r["dl_bc"], licz9, czas=0.9, luk=-PI / 5)
        kk2 = self.przylec(r["dl_ab"], mian9, czas=0.9, luk=PI / 5)
        self.play(
            ReplacementTransform(kk1, licz9), ReplacementTransform(kk2, mian9),
            FadeOut(licz8, scale=0.4), FadeOut(mian8, scale=0.4),
            ReplacementTransform(kreska8, kreska9),
            ReplacementTransform(e8[0], e9[0]), ReplacementTransform(e8[1], e9[1]),
            run_time=1.1,
        )
        self.zgas(e9, r["dl_bc"], r["dl_ab"])

        # KROK 10. sin alfa = 0,6.
        self.next_section("krok10")
        e10 = self.wiersz(self.stan(r"\sin\alpha"), self.stan("="), self.stan("0{,}6"))
        e10.move_to([KOLUMNA_X, PAS_GLOWNY_Y, 0])
        e10[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(e9[0], e10[0]), ReplacementTransform(e9[1], e10[1]),
            FadeOut(e9[2], scale=0.4), FadeIn(e10[2], scale=1.2),
            run_time=1.0,
        )
        self.zgas(e10[2])
        self.postoj()

        # ================================================================
        # KROK 11. Trojkat ACD: kat alfa przy C, przeciwprostokatna AC=6,
        # naprzeciw alfa lezy AD. sin alfa=0,6 kurczy sie do malej "przypominajki".
        # ================================================================
        self.next_section("krok11")
        self.play(
            r["cd"].animate.set_color(ZIELONY), r["da"].animate.set_color(ZIELONY),
            r["ac"].animate.set_color(ZIELONY),
            run_time=0.7,
        )
        self.zgas(r["cd"], r["da"], r["ac"])
        przypominajka = self.wiersz(
            self.stan(r"\sin\alpha", rozmiar=34), self.stan("=", rozmiar=34), self.stan("0{,}6", rozmiar=34)
        )
        przypominajka.move_to([KOLUMNA_X - 1.6, PAS_WZOR_Y, 0])
        self.play(
            FadeOut(wzor2b, shift=UP * 0.2),
            ReplacementTransform(e10, przypominajka),
            run_time=0.8,
        )
        self.postoj()

        # ================================================================
        # ETAP 3: |AD| = |AC| * sin alfa.
        # ================================================================

        # KROK 12. Wzor + podstawienie: |AD|=6*sin alfa.
        self.next_section("krok12")
        wzor3 = self.wiersz(
            self.stan("a", rozmiar=40, kolor=SZARY), self.stan("=", rozmiar=40, kolor=SZARY),
            self.stan("c", rozmiar=40, kolor=SZARY), self.stan(r"\cdot", rozmiar=40, kolor=SZARY),
            self.stan(r"\sin\alpha", rozmiar=40, kolor=SZARY),
        )
        wzor3.move_to([KOLUMNA_X + 0.9, PAS_WZOR_Y, 0])
        self.play(FadeIn(wzor3, shift=LEFT * 0.2), run_time=0.7)

        e12 = self.wiersz(
            self.stan(r"|AD|"), self.stan("="), self.stan("6"), self.stan(r"\cdot"), self.stan(r"\sin\alpha")
        )
        e12.move_to([KOLUMNA_X, PAS_GLOWNY_Y, 0])
        self.play(
            r["ac"].animate.set_color(ZIELONY), r["dl_ac"].animate.set_color(ZIELONY),
            FadeIn(e12[0], e12[1], e12[3]),
            run_time=0.7,
        )
        kk3 = self.przylec(r["dl_ac"], e12[2], czas=0.9, luk=-PI / 5)
        e12[2].set_color(ZIELONY)
        e12[4].set_color(ZIELONY)
        kk4 = self.przylec(przypominajka[0], e12[4], czas=0.9, luk=PI / 5)
        self.play(ReplacementTransform(kk3, e12[2]), ReplacementTransform(kk4, e12[4]), run_time=0.6)
        self.zgas(e12, r["ac"], r["dl_ac"])

        # KROK 13. |AD|=6*0,6.
        self.next_section("krok13")
        e13 = self.wiersz(
            self.stan(r"|AD|"), self.stan("="), self.stan("6"), self.stan(r"\cdot"), self.stan("0{,}6")
        )
        e13.move_to([KOLUMNA_X, PAS_GLOWNY_Y, 0])
        e13[4].set_color(ZIELONY)
        self.play(
            ReplacementTransform(e12[0], e13[0]), ReplacementTransform(e12[1], e13[1]),
            ReplacementTransform(e12[2], e13[2]), ReplacementTransform(e12[3], e13[3]),
            ReplacementTransform(przypominajka[2].copy(), e13[4]),
            FadeOut(e12[4], scale=0.4), FadeOut(przypominajka, scale=0.4),
            run_time=1.0,
        )
        self.zgas(e13[4])

        # KROK 14. |AD|=3,6, wynik wraca na rysunek.
        self.next_section("krok14")
        e14 = self.wiersz(self.stan(r"|AD|"), self.stan("="), self.stan("3{,}6"))
        e14.move_to([KOLUMNA_X, PAS_GLOWNY_Y, 0])
        e14[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(e13[0], e14[0]), ReplacementTransform(e13[1], e14[1]),
            FadeOut(e13[2], scale=0.4), FadeOut(e13[3], scale=0.4),
            ReplacementTransform(e13[4], e14[2]),
            run_time=1.0,
        )
        self.wait(0.3)
        r["dl_ad"].set_color(ZIELONY)
        kop2 = self.przylec(e14[2], r["dl_ad"], czas=0.9, luk=-PI / 4)
        self.play(ReplacementTransform(kop2, r["dl_ad"]), run_time=0.5)
        self.wait(0.3)
        self.play(
            FadeOut(e14, scale=0.4), r["dl_ad"].animate.set_color(BLACK),
            FadeOut(wzor3), run_time=0.4,
        )
        self.postoj(0.5)

        # ================================================================
        # ETAP 4: |DC| z Pitagorasa w trojkacie ACD.
        # ================================================================

        # KROK 15. Wzor + podstawienie: |DC|^2+3,6^2=6^2.
        self.next_section("krok15")
        wzor4 = self.stan("a^{2}", "+", "b^{2}", "=", "c^{2}", rozmiar=40, kolor=SZARY)
        wzor4.move_to([KOLUMNA_X, PAS_WZOR_Y, 0])
        self.play(FadeIn(wzor4, shift=LEFT * 0.2), run_time=0.7)

        e15 = self.stan(r"|DC|^{2}", "+", r"3{,}6^{2}", "=", "6^{2}")
        e15.move_to([KOLUMNA_X, PAS_GLOWNY_Y, 0])
        self.play(
            r["da"].animate.set_color(ZIELONY), r["dl_ad"].animate.set_color(ZIELONY),
            r["ac"].animate.set_color(ZIELONY), r["dl_ac"].animate.set_color(ZIELONY),
            FadeIn(e15[0], e15[1], e15[3]),
            run_time=0.8,
        )
        self.wait(0.25)
        kk5 = self.przylec(r["dl_ad"], e15[2], czas=0.9, luk=-PI / 5)
        kk6 = self.przylec(r["dl_ac"], e15[4], czas=0.9, luk=PI / 5)
        for cz in (e15[2], e15[4]):
            cz.set_color(ZIELONY)
        self.play(ReplacementTransform(kk5, e15[2]), ReplacementTransform(kk6, e15[4]), run_time=0.6)
        self.zgas(e15, r["da"], r["dl_ad"], r["ac"], r["dl_ac"])

        # KROK 16. Kwadraty policzone: |DC|^2+12,96=36.
        self.next_section("krok16")
        e16 = self.stan(r"|DC|^{2}", "+", "12{,}96", "=", "36")
        e16.move_to([KOLUMNA_X, PAS_GLOWNY_Y, 0])
        for cz in (e16[2], e16[4]):
            cz.set_color(ZIELONY)
        self.play(
            ReplacementTransform(e15[0], e16[0]), ReplacementTransform(e15[1], e16[1]),
            ReplacementTransform(e15[2], e16[2]), ReplacementTransform(e15[3], e16[3]),
            ReplacementTransform(e15[4], e16[4]),
            run_time=1.0,
        )
        self.zgas(e16[2], e16[4])

        # KROK 17. |DC|^2=36-12,96.
        self.next_section("krok17")
        e17 = self.stan(r"|DC|^{2}", "=", "36", "-", "12{,}96")
        e17.move_to([KOLUMNA_X, PAS_GLOWNY_Y, 0])
        self.play(e16[1].animate.set_color(CZERWONY), e16[2].animate.set_color(ZIELONY), run_time=0.3)
        e17[3].set_color(CZERWONY)
        e17[4].set_color(ZIELONY)
        self.play(
            ReplacementTransform(e16[0], e17[0]),
            ReplacementTransform(e16[3], e17[1]),
            ReplacementTransform(e16[4], e17[2]),
            FadeOut(e16[1], scale=0.4),
            ReplacementTransform(e16[2], e17[4]),
            FadeIn(e17[3]),
            run_time=1.2, path_arc=-2 * PI / 3,
        )
        self.zgas(e17[2], e17[3], e17[4])

        # KROK 18. |DC|^2=23,04.
        self.next_section("krok18")
        e18 = self.stan(r"|DC|^{2}", "=", "23{,}04")
        e18.move_to([KOLUMNA_X, PAS_GLOWNY_Y, 0])
        e18[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(e17[0], e18[0]), ReplacementTransform(e17[1], e18[1]),
            FadeOut(e17[2], scale=0.4), FadeOut(e17[3], scale=0.4),
            ReplacementTransform(e17[4], e18[2]),
            run_time=1.1,
        )
        self.zgas(e18[2])

        # KROK 19. |DC|=4,8, wynik wraca na rysunek.
        self.next_section("krok19")
        e19 = self.stan(r"|DC|", "=", "4{,}8")
        e19.move_to([KOLUMNA_X, PAS_GLOWNY_Y, 0])
        e19[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(e18[0], e19[0]), ReplacementTransform(e18[1], e19[1]),
            ReplacementTransform(e18[2], e19[2]),
            run_time=1.0,
        )
        self.wait(0.3)
        r["dl_dc"].set_color(ZIELONY)
        kop3 = self.przylec(e19[2], r["dl_dc"], czas=0.9, luk=PI / 4)
        self.play(ReplacementTransform(kop3, r["dl_dc"]), run_time=0.5)
        self.wait(0.3)
        self.play(
            FadeOut(e19, scale=0.4), r["dl_dc"].animate.set_color(BLACK),
            FadeOut(wzor4), run_time=0.4,
        )
        self.postoj(0.5)

        # ================================================================
        # ETAP 5: Pole trapezu.
        # ================================================================

        # KROK 20. Wzor + podstawienie: P=(7,5+4,8)/2 * 3,6.
        self.next_section("krok20")
        wzor5 = self.wiersz(
            self.stan("P", "=", rozmiar=40, kolor=SZARY),
            self.ulamek(("a", "+", "b"), ("2",), rozmiar=40, kolor=SZARY),
            self.stan(r"\cdot", "h", rozmiar=40, kolor=SZARY),
        )
        wzor5.move_to([KOLUMNA_X, PAS_WZOR_Y, 0])
        self.play(FadeIn(wzor5, shift=LEFT * 0.2), run_time=0.7)

        e20 = self.wiersz(
            self.stan("P"), self.stan("="),
            self.ulamek(("7{,}5", "+", "4{,}8"), ("2",)),
            self.stan(r"\cdot", r"3{,}6"),
        )
        e20.move_to([KOLUMNA_X, PAS_GLOWNY_Y, 0])
        self.play(
            r["ab"].animate.set_color(ZIELONY), r["dl_ab"].animate.set_color(ZIELONY),
            r["cd"].animate.set_color(ZIELONY), r["dl_dc"].animate.set_color(ZIELONY),
            r["da"].animate.set_color(ZIELONY), r["dl_ad"].animate.set_color(ZIELONY),
            FadeIn(e20[0], e20[1], e20[2][1], e20[2][2], e20[3][0]),
            run_time=0.9,
        )
        licz20, kreska20, mian20 = e20[2]
        self.wait(0.25)
        kk7 = self.przylec(r["dl_ab"], licz20[0], czas=0.9, luk=-PI / 6)
        kk8 = self.przylec(r["dl_dc"], licz20[2], czas=0.9, luk=PI / 6)
        kk9 = self.przylec(r["dl_ad"], e20[3][1], czas=0.9, luk=PI / 5)
        for cz in (licz20[0], licz20[2], e20[3][1]):
            cz.set_color(ZIELONY)
        self.play(
            ReplacementTransform(kk7, licz20[0]), ReplacementTransform(kk8, licz20[2]),
            ReplacementTransform(kk9, e20[3][1]),
            FadeIn(mian20, scale=0.9),
            run_time=0.8,
        )
        self.zgas(e20, r["ab"], r["dl_ab"], r["cd"], r["dl_dc"], r["da"], r["dl_ad"])

        # KROK 21. Suma podstaw: P=12,3/2 * 3,6.
        self.next_section("krok21")
        e21 = self.wiersz(
            self.stan("P"), self.stan("="),
            self.ulamek(("12{,}3",), ("2",)),
            self.stan(r"\cdot", r"3{,}6"),
        )
        e21.move_to([KOLUMNA_X, PAS_GLOWNY_Y, 0])
        licz21, kreska21, mian21 = e21[2]
        licz21.set_color(ZIELONY)
        self.play(
            ReplacementTransform(e20[0], e21[0]), ReplacementTransform(e20[1], e21[1]),
            ReplacementTransform(licz20, licz21), ReplacementTransform(kreska20, kreska21),
            ReplacementTransform(mian20, mian21),
            ReplacementTransform(e20[3], e21[3]),
            run_time=1.1,
        )
        self.zgas(licz21)

        # KROK 22. Dzielenie: P=6,15 * 3,6.
        self.next_section("krok22")
        e22 = self.wiersz(self.stan("P"), self.stan("="), self.stan("6{,}15"), self.stan(r"\cdot", r"3{,}6"))
        e22.move_to([KOLUMNA_X, PAS_GLOWNY_Y, 0])
        e22[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(e21[0], e22[0]), ReplacementTransform(e21[1], e22[1]),
            FadeOut(e21[2], scale=0.4), FadeIn(e22[2], scale=1.1),
            ReplacementTransform(e21[3], e22[3]),
            run_time=1.1,
        )
        self.zgas(e22[2])

        # KROK 23. P=22,14.
        self.next_section("krok23")
        e23 = self.wiersz(self.stan("P"), self.stan("="), self.stan(r"\boldsymbol{22{,}14}"))
        e23.move_to([KOLUMNA_X, PAS_GLOWNY_Y, 0])
        e23[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(e22[0], e23[0]), ReplacementTransform(e22[1], e23[1]),
            FadeOut(e22[2], scale=0.4), FadeOut(e22[3], scale=0.4),
            FadeIn(e23[2], scale=1.15),
            run_time=1.1,
        )
        self.wait(0.3)
        self.play(e23[2].animate.set_color(BLACK), FadeOut(wzor5), run_time=0.4)
        self.wait(0.25)

        # KROK 24. Odpowiedz koncowa.
        self.next_section("krok24")
        werdykt = Text("Pole trapezu ABCD = 22,14", font_size=30, weight=BOLD, color=BLACK)
        if werdykt.width > 6.6:
            werdykt.scale_to_fit_width(6.6)
        werdykt.move_to([KOLUMNA_X - 0.3, WERDYKT_Y, 0])
        self.play(FadeOut(e23, shift=UP * 0.3), run_time=0.5)
        self.play(FadeIn(werdykt, shift=UP * 0.25), run_time=0.7)
        self.postoj()
