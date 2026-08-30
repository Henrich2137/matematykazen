import math

import numpy as np
from manim import *

# Zadanie 17.2 (zamkniete, 1 pkt). Ten sam trojkat co w 17.1: kat prosty przy A,
# |AC| = sqrt(15), |BC| = 8, punkt D na AB z |DB| = 6. Szukamy tangensa kata ADC.
# Wynik sqrt(15), czyli odpowiedz A.
#
# WERSJA DRUGA, 2026-08-30. Pierwsza (pietnascie krokow) zostala przez Henricha
# odrzucona w calosci. Trzy uwagi i co z nich wyszlo:
#
#   1. „czesc tresci jest za mala, nie wszystko musi byc zawsze na ekranie"
#      -> zniknal pas odczytu w prawym gornym rogu (|AC| = sqrt(15), |DB| = 6:
#      obie liczby stoja przeciez na rysunku), rysunek jest szerszy, a pismo
#      wieksze. Prawa polowa ma dzis DWA pasy zamiast czterech: gorny niesie
#      tangens i stoi do konca filmu, dolny to miejsce robocze na Pitagorasa,
#      ktore po policzeniu podstawy CZYSCI SIE (krok 11).
#   2. „w kroku 4 niepotrzebnie klamra zostaje podswietlona" -> klamry i ich
#      podpisy sa szare przez caly film. Zielone bywaja tylko boki i liczby,
#      czyli to, co wchodzi do rachunku. Klamra jest oznaczeniem, nie skladnikiem.
#   3. „nazwy bokow w stylu |AC| sa niepotrzebne" (uwaga z 17.1, ta sama zasada)
#      -> w kadrze nie ma ani jednego zapisu w rodzaju |AB|. Nieznana podstawa
#      dostaje po prostu litere x pod klamra i ta litera jedzie do Pitagorasa.
#
# Trzynascie krokow. Droga: tangens potrzebuje odcinka AD, AD to cala podstawa
# bez znanego kawalka 6, a cala podstawa wychodzi z Pitagorasa w trojkacie ABC.
#
# Wzory z tablicy: [9.1] tg alfa = a/b (strona 11) i [10.5] twierdzenie
# Pitagorasa a^2 + b^2 = c^2 (strona 13).
#
# Dystraktor D (sqrt(15)/8) to tangens policzony z bokiem 8 zamiast z AD,
# czyli mylenie przeciwprostokatnej z przyprostokatna przylegla.
#
# Render: manim --save_sections solutionZad17_2.py Zad17_2
#         (albo tools/wgraj-kroki.sh 17_2)

ZIELONY = "#2e7d32"
SZARY = "#666666"

# Te same wspolrzedne co w solutionZad17_1.py: oba filmy pokazuja ten sam rysunek.
BOK_AB = 7.0
BOK_AC = math.sqrt(15.0)
ODC_DB = 6.0

JEDNOSTKA = 0.65
SZEROKOSC_RYSUNKU = 6.2
SRODEK_RYSUNKU = np.array([-3.85, 0.55, 0.0])

KOLUMNA_X = 3.75
PAS_A_Y = 2.55          # tangens, stoi do konca filmu
PAS_B_Y = -0.85         # miejsce robocze: Pitagoras, potem odejmowanie
WERDYKT_Y = -3.05


class Zad17_2(Scene):

    # ---- klocki -------------------------------------------------------

    def stan(self, *args, rozmiar=60):
        m = MathTex(*args)
        m.set_color(BLACK)
        m.font_size = rozmiar
        return m

    def ulamek(self, gora, dol, rozmiar=60):
        g = self.stan(*gora, rozmiar=rozmiar)
        d = self.stan(*dol, rozmiar=rozmiar)
        szer = max(g.width, d.width) + 0.24
        kreska = Line(LEFT * szer / 2, RIGHT * szer / 2, color=BLACK, stroke_width=4)
        g.next_to(kreska, UP, buff=0.15)
        d.next_to(kreska, DOWN, buff=0.15)
        return VGroup(g, kreska, d)

    def wiersz(self, *czesci, buff=0.22):
        return VGroup(*czesci).arrange(RIGHT, buff=buff)

    def postoj(self):
        # 0,45 s: w kadrze stoi rysunek, czyli duzo drobnego szczegolu
        # (README, punkt 47).
        self.wait(0.45)

    def zgas(self, *mobiekty, czas=0.4):
        if mobiekty:
            self.play(*[m.animate.set_color(BLACK) for m in mobiekty], run_time=czas)

    # ---- rysunek ------------------------------------------------------

    def zbuduj_rysunek(self):
        """Trojkat z arkusza razem z obiema klamrami i wszystkimi podpisami,
        ktore kiedykolwiek pod nimi staja. Wszystko powstaje tutaj, zeby jedno
        wspolne skalowanie zlapalo to razem i nic nie roznilo sie wielkoscia."""

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

        # Kwadracik kata prostego jest tu MNIEJSZY niz w 17.1: trojkat ACD to
        # waski klin (podstawa 1, wysokosc prawie 4) i przy wiekszym kwadraciku
        # luk kata alfa wchodzil na niego.
        bok = 0.16
        r["kat_prosty"] = VMobject(color=BLACK, stroke_width=4).set_points_as_corners(
            [A + RIGHT * bok, A + RIGHT * bok + UP * bok, A + UP * bok]
        )

        # Luk kata ADC: przy wierzcholku D, miedzy ramionami DA i DC.
        kier_da = math.atan2(A[1] - D[1], A[0] - D[0])
        kier_dc = math.atan2(C[1] - D[1], C[0] - D[0])
        r["luk_d"] = Arc(
            radius=0.30, start_angle=kier_dc, angle=kier_da - kier_dc,
            arc_center=D, color=SZARY, stroke_width=5,
        )
        # Alfa siedzi na dwusiecznej kata, tuz za lukiem: w tym klinie jest
        # tylko pol jednostki miejsca miedzy bokiem AC a odcinkiem CD.
        dwusieczna = (kier_da + kier_dc) / 2.0
        r["alfa"] = MathTex(r"\alpha", color=SZARY, font_size=38)
        r["alfa"].move_to(D + 0.56 * np.array(
            [math.cos(dwusieczna), math.sin(dwusieczna), 0.0]))

        r["etyk_a"] = MathTex("A", color=BLACK, font_size=46).next_to(A, DOWN + LEFT, buff=0.10)
        r["etyk_b"] = MathTex("B", color=BLACK, font_size=46).next_to(B, DOWN + RIGHT, buff=0.10)
        r["etyk_c"] = MathTex("C", color=BLACK, font_size=46).next_to(C, UP + LEFT, buff=0.10)
        r["etyk_d"] = MathTex("D", color=BLACK, font_size=46).next_to(D, DOWN, buff=0.24)

        r["dl_ac"] = MathTex(r"\sqrt{15}", color=BLACK, font_size=54)
        r["dl_ac"].next_to(Line(A, C).get_center(), LEFT, buff=0.24)
        r["dl_cb"] = MathTex("8", color=BLACK, font_size=54)
        r["dl_cb"].next_to(Line(C, B).get_center(), UP + RIGHT, buff=0.12)
        r["dl_db"] = MathTex("6", color=BLACK, font_size=54)
        r["dl_db"].next_to(Line(D, B).get_center(), DOWN, buff=0.24)

        # KLAMRY. Szare i szare zostaja: to oznaczenie odcinka, a nie liczba,
        # ktora wchodzi do rachunku (uwaga Henricha o kroku 4).
        r["klamra_ad"] = BraceBetweenPoints(A, D, direction=DOWN, color=SZARY)
        r["klamra_ad"].shift(DOWN * 0.55)
        r["klamra_ab"] = BraceBetweenPoints(A, B, direction=DOWN, color=SZARY)
        r["klamra_ab"].shift(DOWN * 1.55)

        r["pyt_ad"] = MathTex("?", color=SZARY, font_size=52)
        r["pyt_ad"].next_to(r["klamra_ad"], DOWN, buff=0.10)
        r["dl_ad"] = MathTex("1", color=SZARY, font_size=52)
        r["dl_ad"].move_to(r["pyt_ad"])
        r["x_ab"] = MathTex("x", color=BLACK, font_size=52)
        r["x_ab"].next_to(r["klamra_ab"], DOWN, buff=0.10)
        r["dl_ab"] = MathTex("7", color=BLACK, font_size=52)
        r["dl_ab"].move_to(r["x_ab"])

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
        # PAS A: tangens. Stoi w kadrze od kroku 2 do konca filmu.
        # ================================================================
        t2 = self.wiersz(self.stan(r"\operatorname{tg}", r"\alpha"), self.stan("="),
                         self.ulamek(("a",), ("b",)))
        t3 = self.wiersz(self.stan(r"\operatorname{tg}", r"\alpha"), self.stan("="),
                         self.ulamek((r"\sqrt{15}",), ("b",)))
        t12 = self.wiersz(self.stan(r"\operatorname{tg}", r"\alpha"), self.stan("="),
                          self.ulamek((r"\sqrt{15}",), ("1",)))
        t13 = self.wiersz(self.stan(r"\operatorname{tg}", r"\alpha"), self.stan("="),
                          self.stan(r"\sqrt{15}"))
        for w in (t2, t3, t12, t13):
            w.move_to([KOLUMNA_X, PAS_A_Y, 0])
            w.shift(RIGHT * (KOLUMNA_X - w[1].get_center()[0]))

        # ================================================================
        # PAS B: miejsce robocze. Pitagoras, a po nim odejmowanie.
        # ================================================================
        p6 = self.stan("a^{2}", "+", "b^{2}", "=", "c^{2}", rozmiar=56)
        p7 = self.stan("x^{2}", "+", r"\left(\sqrt{15}\right)^{2}", "=", "8^{2}", rozmiar=56)
        p8 = self.stan("x^{2}", "+", "15", "=", "64", rozmiar=56)
        p9 = self.stan("x^{2}", "=", "49", rozmiar=56)
        p10 = self.stan("x", "=", "7", rozmiar=56)
        p11 = self.stan("7", "-", "6", "=", "1", rozmiar=56)
        for m in (p6, p7, p8, p9, p10, p11):
            m.move_to([KOLUMNA_X, PAS_B_Y, 0])

        werdykt = Text("Odpowiedź A", font_size=40, weight=BOLD, color=BLACK)
        werdykt.move_to([KOLUMNA_X, WERDYKT_Y, 0])

        def przylec(zrodlo, cel, czas=1.0, luk=-PI / 4):
            """Kopia liczby z rysunku leci na miejsce litery we wzorze
            (README, punkt 37)."""
            k = zrodlo.copy()
            self.add(k)
            self.play(k.animate.move_to(cel.get_center()).scale(
                cel.height / max(zrodlo.height, 0.01)),
                run_time=czas, path_arc=luk)
            return k

        # ================================================================
        # KROK 1. Rysunek i kat, o ktory pyta zadanie. Uwaga: to kat przy D,
        # w trojkacie ACD, a nie ten sam co w 17.1. Luk i alfa szare.
        # ================================================================
        self.next_section("krok1")
        self.play(FadeIn(rysunek), run_time=1.1)
        self.wait(0.4)
        self.play(Create(r["luk_d"]), FadeIn(r["alfa"]), run_time=0.8)
        self.postoj()

        # ================================================================
        # KROK 2. Wzor z tablicy, strona 11. Bez koloru.
        # ================================================================
        self.next_section("krok2")
        self.play(FadeIn(t2, shift=LEFT * 0.25), run_time=0.9)
        self.postoj()

        # ================================================================
        # KROK 3. Litera a: przyprostokatna NAPRZECIW kata alfa, czyli AC.
        # Bok i licznik zapalaja sie razem i zostaja zielone do konca filmu.
        # ================================================================
        self.next_section("krok3")
        licz2, kreska2, mian2 = t2[2]
        licz3, kreska3, mian3 = t3[2]
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
            *[ReplacementTransform(t2[i], t3[i]) for i in (0, 1)],
            run_time=1.0,
        )
        self.postoj()

        # ================================================================
        # KROK 4. Litera b: przyprostokatna PRZY kacie, czyli odcinek AD.
        # Zielony jest sam odcinek i mianownik. Klamra ze znakiem zapytania
        # jest SZARA i szara zostaje: to oznaczenie, nie skladnik rachunku
        # (poprawka po uwadze Henricha).
        # ================================================================
        self.next_section("krok4")
        self.play(
            r["bok_ad"].animate.set_color(ZIELONY),
            mian3.animate.set_color(ZIELONY),
            run_time=0.7,
        )
        self.play(FadeIn(r["klamra_ad"]), FadeIn(r["pyt_ad"]), run_time=0.7)
        self.postoj()

        # ================================================================
        # KROK 5. Zadanie podaje tylko kawalek od D do B. Zeby dojsc do AD,
        # trzeba najpierw poznac CALA podstawe: dostaje ona druga klamre
        # i nazwe x. Klamra szara, litera czarna, bo x wchodzi do rachunku.
        # ================================================================
        self.next_section("krok5")
        self.play(FadeIn(r["klamra_ab"]), FadeIn(r["x_ab"]), run_time=0.8)
        self.postoj()

        # ================================================================
        # KROK 6. Wzor Pitagorasa z tablicy, strona 13, wjezdza w pas roboczy.
        # Bez koloru: to dopiero przepis.
        # ================================================================
        self.next_section("krok6")
        self.play(FadeIn(p6, shift=UP * 0.25), run_time=0.9)
        self.postoj()

        # ================================================================
        # KROK 7. Kazda litera zamienia sie w liczbe, ktora przylatuje ze
        # swojego boku (README, punkt 37). Przeciwprostokatna to bok naprzeciw
        # kata prostego, czyli 8, i ona idzie pod c.
        # ================================================================
        self.next_section("krok7")
        # Odcinek AD jest juz zielony od kroku 4, a x to CALA podstawa, wiec
        # dokladamy do niego druga polowe (DB) i mamy zielona podstawe.
        self.play(
            r["bok_db"].animate.set_color(ZIELONY),
            r["bok_cb"].animate.set_color(ZIELONY),
            r["dl_cb"].animate.set_color(ZIELONY),
            r["x_ab"].animate.set_color(ZIELONY),
            run_time=0.8,
        )
        self.wait(0.3)
        kx = przylec(r["x_ab"], p7[0], czas=1.1, luk=-PI / 5)
        kc = przylec(r["dl_cb"], p7[4], czas=1.1, luk=PI / 5)
        for i in (0, 2, 4):
            p7[i].set_color(ZIELONY)
        self.play(
            ReplacementTransform(kx, p7[0]),
            ReplacementTransform(kc, p7[4]),
            FadeOut(p6[0], scale=0.4), FadeOut(p6[4], scale=0.4),
            ReplacementTransform(p6[1], p7[1]),
            ReplacementTransform(p6[3], p7[3]),
            ReplacementTransform(p6[2], p7[2]),
            run_time=1.2,
        )
        # Gasi sie wszystko poza odcinkiem AD: on zostaje zielony, bo dalej
        # jest tym, czego szukamy do mianownika tangensa.
        self.zgas(p7[0], p7[2], p7[4], r["bok_db"], r["bok_cb"],
                  r["dl_cb"], r["x_ab"])
        self.postoj()

        # ================================================================
        # KROK 8. Kwadraty liczb. Pierwiastek i kwadrat sie znosza.
        # ================================================================
        self.next_section("krok8")
        p8[2].set_color(ZIELONY)
        p8[4].set_color(ZIELONY)
        self.play(
            ReplacementTransform(p7[0], p8[0]),
            ReplacementTransform(p7[1], p8[1]),
            ReplacementTransform(p7[2], p8[2]),
            ReplacementTransform(p7[3], p8[3]),
            ReplacementTransform(p7[4], p8[4]),
            run_time=1.2,
        )
        self.zgas(p8[2], p8[4])
        self.postoj()

        # ================================================================
        # KROK 9. Pietnastka przechodzi na druga strone ze zmiana znaku,
        # lukiem NAD znakiem rownosci (README, punkt 27).
        # ================================================================
        self.next_section("krok9")
        self.play(p8[2].animate.set_color(ZIELONY), run_time=0.35)
        p9[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(p8[0], p9[0]),
            ReplacementTransform(p8[3], p9[1]),
            ReplacementTransform(p8[4], p9[2]),
            FadeOut(p8[1], scale=0.4),
            FadeOut(p8[2], target_position=p9[2].get_center(), scale=0.4),
            run_time=1.3, path_arc=-2 * PI / 3,
        )
        self.zgas(p9[2])
        self.postoj()

        # ================================================================
        # KROK 10. Pierwiastkujemy. Dlugosc boku nie bywa ujemna, wiec bierzemy
        # sam wynik dodatni. Siodemka od razu jedzie pod klamre, na miejsce x.
        # ================================================================
        self.next_section("krok10")
        p10[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(p9[0], p10[0]),
            ReplacementTransform(p9[1], p10[1]),
            ReplacementTransform(p9[2], p10[2]),
            run_time=1.1,
        )
        self.wait(0.35)
        kop7 = p10[2].copy()
        self.add(kop7)
        r["dl_ab"].set_color(ZIELONY)
        self.play(
            kop7.animate.move_to(r["x_ab"]).scale(
                r["dl_ab"].height / max(p10[2].height, 0.01)),
            run_time=1.0, path_arc=PI / 4,
        )
        self.play(
            ReplacementTransform(kop7, r["dl_ab"]),
            FadeOut(r["x_ab"], scale=0.4),
            run_time=0.6,
        )
        self.zgas(p10[2], r["dl_ab"])
        self.postoj()

        # ================================================================
        # KROK 11. Pas roboczy sie czysci: Pitagoras zrobil swoje. Zostaje
        # jedno odejmowanie, cala podstawa bez znanego kawalka, a wynik ladzie
        # pod mala klamra zamiast znaku zapytania.
        # ================================================================
        self.next_section("krok11")
        self.play(
            r["dl_ab"].animate.set_color(ZIELONY),
            r["dl_db"].animate.set_color(ZIELONY),
            run_time=0.6,
        )
        k7b = przylec(r["dl_ab"], p11[0], czas=0.9, luk=-PI / 5)
        k6b = przylec(r["dl_db"], p11[2], czas=0.9, luk=-PI / 5)
        self.play(
            ReplacementTransform(k7b, p11[0]),
            ReplacementTransform(k6b, p11[2]),
            FadeOut(p10, scale=0.4),
            FadeIn(p11[1]), FadeIn(p11[3]),
            run_time=1.0,
        )
        p11[4].set_color(ZIELONY)
        self.play(FadeIn(p11[4]), run_time=0.6)
        self.wait(0.3)
        kop1 = p11[4].copy()
        self.add(kop1)
        self.play(
            kop1.animate.move_to(r["pyt_ad"]).scale(
                r["dl_ad"].height / max(p11[4].height, 0.01)),
            run_time=0.9, path_arc=PI / 4,
        )
        r["dl_ad"].set_color(ZIELONY)
        self.play(
            ReplacementTransform(kop1, r["dl_ad"]),
            FadeOut(r["pyt_ad"], scale=0.4),
            run_time=0.6,
        )
        self.zgas(p11[4], r["dl_ab"], r["dl_db"])
        self.play(r["dl_ad"].animate.set_color(SZARY), run_time=0.3)
        self.postoj()

        # ================================================================
        # KROK 12. Jedynka wraca do wzoru na miejsce litery b. Pas roboczy
        # znika: zrobil swoje i tylko zabieralby miejsce.
        # ================================================================
        self.next_section("krok12")
        licz12, kreska12, mian12 = t12[2]
        self.play(FadeOut(p11, shift=DOWN * 0.3), run_time=0.7)
        kop1b = przylec(r["dl_ad"], mian12, czas=1.0, luk=-PI / 4)
        mian12.set_color(ZIELONY)
        licz12.set_color(ZIELONY)
        self.play(
            ReplacementTransform(kop1b, mian12),
            FadeOut(mian3, scale=0.4),
            ReplacementTransform(kreska3, kreska12),
            ReplacementTransform(licz3, licz12),
            *[ReplacementTransform(t3[i], t12[i]) for i in (0, 1)],
            run_time=1.1,
        )
        self.postoj()

        # ================================================================
        # KROK 13. Dzielenie przez jeden niczego nie zmienia, wiec kreska
        # i jedynka znikaja. Zielen na boku AC i na pierwiastku zostaje:
        # ostatnia klatka ma mowic, skad wzial sie wynik.
        # ================================================================
        self.next_section("krok13")
        self.play(mian12.animate.set_color(ZIELONY), run_time=0.3)
        t13[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(licz12, t13[2]),
            FadeOut(mian12, scale=0.3),
            FadeOut(kreska12, scale=0.3),
            *[ReplacementTransform(t12[i], t13[i]) for i in (0, 1)],
            run_time=1.1,
        )
        self.play(FadeIn(werdykt, shift=UP * 0.25), run_time=0.7)
        self.postoj()
