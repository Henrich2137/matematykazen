import math

import numpy as np
from manim import *

# Zadanie 17.2 (zamkniete, 1 pkt). Ten sam trojkat co w 17.1: kat prosty przy A,
# |AC| = sqrt(15), |BC| = 8, D na AB z |DB| = 6. Szukamy tg(kata ADC).
# |AB| = 7, wiec |AD| = 1 i tg = sqrt(15)/1 = sqrt(15), odpowiedz A.
#
# Projekt: issues/projekt-zad17-2024-grudzien.md. Pietnascie krokow, jeden do
# jednego z pietnastoma linijkami rachunku w solutionText.
#
# Uklad kadru (README, punkt 35), tym razem cztery pasy po prawej, bo trzy
# zapisy musza stac w kadrze jednoczesnie i wracac do nich po kolei:
#   - pas odczytu u gory (mniejszym pismem, README punkt 41),
#   - pas CELU: tangens, ktory ustawiamy w kroku 3 i do ktorego wracamy w 14,
#   - pas RELACJI: |AD| = |AB| - 6, ustawiony w kroku 4, dokonczony w 12 i 13,
#   - glowny rachunek: caly Pitagoras (kroki 5 do 11), na dole werdykt.
# Dzieki temu kazda linijka ma swoje miejsce i przeksztalca sie W MIEJSCU,
# bez osobnych krokow na parkowanie wynikow.
#
# Pulapka zadania: dystraktor D to sqrt(15)/8, czyli odpowiedz z podpunktu 17.1.
# Kto policzy funkcje kata przy B zamiast przy D, trafia w gotowa odpowiedz.
# Rozbraja to krok 1 (zapala sie MALY trojkat ACD, nie ABC) i krok 13, w ktorym
# na rysunku staja obok siebie 7 przy AB i 1 przy AD.
#
# Render: manim --save_sections solutionZad17_2.py Zad17_2
#         (albo tools/wgraj-kroki.sh 17_2)

ZIELONY = "#2e7d32"
SZARY = "#666666"
SZARY_DOPISEK = "#888888"

# Geometria musi sie zgadzac z solutionZad17_1.py: oba filmy pokazuja ten sam
# rysunek z arkusza.
BOK_AB = 7.0
BOK_AC = math.sqrt(15.0)
ODC_DB = 6.0

JEDNOSTKA = 0.65
SZEROKOSC_RYSUNKU = 5.2
SRODEK_RYSUNKU = np.array([-4.25, -0.30, 0.0])

KOLUMNA_X = 3.30
PAS_Y = 3.25
CEL_Y = 1.95
RELACJA_Y = 0.55
RACHUNEK_Y = -1.10
POMOCNICZY_Y = -2.10
WERDYKT_Y = -3.05


class Zad17_2(Scene):

    # ---- klocki -------------------------------------------------------

    def stan(self, *args, rozmiar=50):
        m = MathTex(*args)
        m.set_color(BLACK)
        m.font_size = rozmiar
        return m

    def ulamek(self, gora, dol, rozmiar=46):
        g = self.stan(*gora, rozmiar=rozmiar)
        d = self.stan(*dol, rozmiar=rozmiar)
        szer = max(g.width, d.width) + 0.20
        kreska = Line(LEFT * szer / 2, RIGHT * szer / 2, color=BLACK, stroke_width=4)
        g.next_to(kreska, UP, buff=0.13)
        d.next_to(kreska, DOWN, buff=0.13)
        return VGroup(g, kreska, d)

    def zgas(self, *mobiekty, czas=0.4):
        if mobiekty:
            self.play(*[m.animate.set_color(BLACK) for m in mobiekty], run_time=czas)

    def postoj(self):
        # README punkt 47: przy rysunku w kadrze 0,25 s to za malo na styk klatek.
        self.wait(0.45)

    def przywolaj(self, zrodla, cele, czas=1.0, luk=-PI / 4):
        """Kopia wartosci leci z miejsca, w ktorym ja odczytalismy, na miejsce
        litery we wzorze (README, punkty 37 i 38). W tej scenie zrodlem jest
        RYSUNEK: to na nim stoja wszystkie dane zadania."""
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

    # ---- rysunek ------------------------------------------------------

    def zbuduj_rysunek(self):
        """Trojkat z arkusza plus trzy podpisy odslaniane w trakcie filmu
        (znak zapytania przy AD, klamra z 7 pod AB, jedynka przy AD).
        Wszystko powstaje tutaj, zeby wspolne skalowanie objelo je razem
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

        bok = 0.24
        r["kat_prosty"] = VMobject(color=BLACK, stroke_width=4).set_points_as_corners(
            [A + RIGHT * bok, A + RIGHT * bok + UP * bok, A + UP * bok]
        )

        # Luk kata ADC. Promien maly, bo D lezy blisko A i wiekszy luk wchodzilby
        # na kwadracik kata prostego.
        kier_da = math.atan2(A[1] - D[1], A[0] - D[0])
        kier_dc = math.atan2(C[1] - D[1], C[0] - D[0])
        r["luk_d"] = Arc(
            radius=0.38, start_angle=kier_dc, angle=kier_da - kier_dc,
            arc_center=D, color=SZARY, stroke_width=5,
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

        # Dwie klamry pod podstawa, na roznych glebokosciach. Wiersz z literami
        # A, D, B i szostka jest juz zajety, a odcinek AD ma dlugosc jednej
        # siodmej podstawy, wiec podpis wpisany tam wprost zlewa sie z litera D.
        # Klamra mowi jednoznacznie, ktorego odcinka dotyczy liczba pod nia.
        r["klamra_ad"] = BraceBetweenPoints(A, D, direction=DOWN, color=BLACK)
        r["klamra_ad"].shift(DOWN * 0.45)
        r["znak_ad"] = MathTex("?", color=BLACK, font_size=40)
        r["znak_ad"].next_to(r["klamra_ad"], DOWN, buff=0.10)
        r["dl_ad"] = MathTex("1", color=BLACK, font_size=40)
        r["dl_ad"].move_to(r["znak_ad"].get_center())

        r["klamra_ab"] = BraceBetweenPoints(A, B, direction=DOWN, color=BLACK)
        r["klamra_ab"].shift(DOWN * 1.35)
        r["dl_ab"] = MathTex("7", color=BLACK, font_size=40)
        r["dl_ab"].next_to(r["klamra_ab"], DOWN, buff=0.10)

        grupa = VGroup(*r.values())
        grupa.scale_to_fit_width(SZEROKOSC_RYSUNKU)
        grupa.move_to(SRODEK_RYSUNKU)
        return grupa

    # ---- scena --------------------------------------------------------

    def construct(self):
        self.zbuduj_rysunek()
        r = self.rys
        widoczne_od_startu = VGroup(
            r["bok_ac"], r["bok_cb"], r["bok_ad"], r["bok_db"], r["odc_cd"],
            r["kat_prosty"], r["etyk_a"], r["etyk_b"], r["etyk_c"], r["etyk_d"],
            r["dl_ac"], r["dl_cb"], r["dl_db"],
        )

        # ================================================================
        # PRAWA POLOWA
        # ================================================================
        pas_ac = self.stan("|AC|", "=", r"\sqrt{15}", rozmiar=36)
        pas_db = self.stan("|DB|", "=", "6", rozmiar=36)
        pas = VGroup(pas_ac, pas_db).arrange(RIGHT, buff=0.85)
        pas.move_to([KOLUMNA_X, PAS_Y, 0])

        def wiersz(*czesci, buff=0.20):
            return VGroup(*czesci).arrange(RIGHT, buff=buff)

        def wyrownaj(rzedy, indeks_rownosci, y):
            for w in rzedy:
                w.move_to([KOLUMNA_X, y, 0])
                w.shift(RIGHT * (KOLUMNA_X - w[indeks_rownosci].get_center()[0]))

        # --- pas celu: tangens (linijki 2, 3, 14, 15) --------------------
        c2 = wiersz(self.stan(r"\operatorname{tg}", r"\alpha", rozmiar=46),
                    self.stan("=", rozmiar=46), self.ulamek(("a",), ("b",)))
        c3 = wiersz(self.stan(r"\operatorname{tg}", r"(\angle ADC)", rozmiar=46),
                    self.stan("=", rozmiar=46), self.ulamek(("|AC|",), ("|AD|",)))
        c14 = wiersz(self.stan(r"\operatorname{tg}", r"(\angle ADC)", rozmiar=46),
                     self.stan("=", rozmiar=46), self.ulamek((r"\sqrt{15}",), ("1",)))
        c15 = wiersz(self.stan(r"\operatorname{tg}", r"(\angle ADC)", rozmiar=46),
                     self.stan("=", rozmiar=46), self.stan(r"\sqrt{15}", rozmiar=46))
        wyrownaj((c2, c3, c14, c15), 1, CEL_Y)

        # --- pas relacji: |AD| (linijki 4, 12, 13) -----------------------
        e4 = self.stan("|AD|", "=", "|AB|", "-", "6", rozmiar=46)
        e12 = self.stan("|AD|", "=", "7", "-", "6", rozmiar=46)
        e13 = self.stan("|AD|", "=", "1", rozmiar=46)
        wyrownaj((e4, e12, e13), 1, RELACJA_Y)

        # --- glowny rachunek: Pitagoras (linijki 5 do 11) ----------------
        s5 = self.stan("a^{2}", "+", "b^{2}", "=", "c^{2}")
        s6 = self.stan("|AB|^{2}", "+", "|AC|^{2}", "=", "|BC|^{2}")
        s7 = self.stan("|AB|^{2}", "+", r"(\sqrt{15})^{2}", "=", "8^{2}")
        s8 = self.stan("|AB|^{2}", "+", "15", "=", "64")
        wyrownaj((s5, s6, s7, s8), 3, RACHUNEK_Y)
        s9 = self.stan("|AB|^{2}", "=", "64", "-", "15")
        s10 = self.stan("|AB|^{2}", "=", "49")
        s11 = self.stan("|AB|", "=", "7")
        wyrownaj((s9, s10, s11), 1, RACHUNEK_Y)

        # --- rachunki pomocnicze (README punkt 29: mniejsze pismo, znikaja) ---
        ogniwo8 = self.stan(r"\sqrt{15}", r"\cdot", r"\sqrt{15}", "=", "15", rozmiar=36)
        ogniwo8.move_to([KOLUMNA_X, POMOCNICZY_Y, 0])
        ogniwo11 = self.stan("7", r"\cdot", "7", "=", "49", rozmiar=36)
        ogniwo11.move_to([KOLUMNA_X, POMOCNICZY_Y, 0])

        dopisek = self.stan(r"\big/ - 15", rozmiar=40)
        dopisek.set_color(SZARY_DOPISEK)
        dopisek.next_to(s8, RIGHT, buff=0.55)

        werdykt = Text("Odpowiedź A", font_size=34, weight=BOLD, color=BLACK)
        werdykt.move_to([KOLUMNA_X, WERDYKT_Y, 0])

        # ================================================================
        # KROK 1. Kat ADC siedzi w trojkacie ACD, a nie w ABC. Zapala sie MALY
        # trojkat, zeby uczen zobaczyl inna figure, zanim padnie jakikolwiek
        # wzor. Do pasa odczytu ida dwie dane, ktore z tego rysunku bierzemy.
        # ================================================================
        self.next_section("krok1")
        self.play(FadeIn(widoczne_od_startu), run_time=1.0)
        self.wait(0.35)

        r["luk_d"].set_color(ZIELONY)
        self.play(Create(r["luk_d"]), run_time=0.7)
        self.play(
            r["bok_ac"].animate.set_color(ZIELONY),
            r["odc_cd"].animate.set_color(ZIELONY),
            r["bok_ad"].animate.set_color(ZIELONY),
            run_time=0.8,
        )
        self.wait(0.3)
        self.zgas(r["odc_cd"], r["bok_ad"])

        kopie = self.przywolaj(
            [r["dl_ac"], r["dl_db"]],
            [pas_ac[2].get_center(), pas_db[2].get_center()],
            czas=1.1,
        )
        pas_ac[2].set_color(ZIELONY)
        pas_db[2].set_color(ZIELONY)
        self.play(
            FadeIn(pas_ac[0], pas_ac[1]), FadeIn(pas_db[0], pas_db[1]),
            ReplacementTransform(kopie[0], pas_ac[2]),
            ReplacementTransform(kopie[1], pas_db[2]),
            run_time=1.0,
        )
        self.zgas(pas_ac[2], pas_db[2], r["bok_ac"])
        self.play(r["luk_d"].animate.set_color(SZARY), run_time=0.35)
        self.postoj()

        # ================================================================
        # KROK 2. Wzor z tablicy, strona 11. Bez koloru (README, punkt 12).
        # ================================================================
        self.next_section("krok2")
        self.play(FadeIn(c2), run_time=0.9)
        self.postoj()

        # ================================================================
        # KROK 3. Litery wzoru zamieniaja sie w nazwy bokow trojkata ACD.
        # Przy AD staje ZNAK ZAPYTANIA i zostaje na rysunku az do kroku 13:
        # to on trzyma w kadrze pytanie, na ktore odpowiada caly Pitagoras.
        # ================================================================
        self.next_section("krok3")
        licz2, kreska2, mian2 = c2[2]
        licz3, kreska3, mian3 = c3[2]
        for m in (c3[0][1], licz3, mian3):
            m.set_color(ZIELONY)
        self.play(
            c2[0][1].animate.set_color(ZIELONY),
            licz2.animate.set_color(ZIELONY),
            mian2.animate.set_color(ZIELONY),
            run_time=0.4,
        )
        self.play(
            ReplacementTransform(c2[0][0], c3[0][0]),
            ReplacementTransform(c2[0][1], c3[0][1]),
            ReplacementTransform(c2[1], c3[1]),
            ReplacementTransform(kreska2, kreska3),
            ReplacementTransform(licz2, licz3),
            ReplacementTransform(mian2, mian3),
            r["bok_ac"].animate.set_color(ZIELONY),
            r["bok_ad"].animate.set_color(ZIELONY),
            run_time=1.4,
        )
        r["znak_ad"].set_color(ZIELONY)
        r["klamra_ad"].set_color(ZIELONY)
        self.play(FadeIn(r["klamra_ad"]), FadeIn(r["znak_ad"]), run_time=0.5)
        self.zgas(c3[0][1], licz3, mian3, r["bok_ac"], r["bok_ad"],
                  r["znak_ad"], r["klamra_ad"])
        self.postoj()

        # ================================================================
        # KROK 4. Skad wziac AD. Klamra pokazuje CALE AB, a szostka mowi, ile
        # z niego odcina odcinek DB. Zielone: klamra i szostka, bo to one
        # niosa mysl tego kroku.
        # ================================================================
        self.next_section("krok4")
        r["klamra_ab"].set_color(ZIELONY)
        self.play(
            FadeIn(r["klamra_ab"]),
            r["bok_ad"].animate.set_color(ZIELONY),
            r["bok_db"].animate.set_color(ZIELONY),
            run_time=0.9,
        )
        self.play(
            r["bok_db"].animate.set_color(BLACK),
            r["dl_db"].animate.set_color(ZIELONY),
            run_time=0.6,
        )
        for m in (e4[2], e4[3], e4[4]):
            m.set_color(ZIELONY)
        self.play(FadeIn(e4), run_time=0.9)
        self.zgas(e4[2], e4[3], e4[4], r["klamra_ab"], r["bok_ad"], r["dl_db"])
        self.postoj()

        # ================================================================
        # KROK 5. Twierdzenie Pitagorasa z tablicy, strona 15. Bez koloru.
        # ================================================================
        self.next_section("krok5")
        self.play(FadeIn(s5), run_time=0.9)
        self.postoj()

        # ================================================================
        # KROK 6. Litery wzoru zamieniaja sie w boki trojkata ABC. Kwadracik
        # kata prostego zapala sie razem z |BC|: przeciwprostokatna to bok
        # lezacy naprzeciw kata prostego, i to jest jedyny powod, dla ktorego
        # osemka trafia po prawej stronie rownosci.
        # ================================================================
        self.next_section("krok6")
        self.play(
            *[s5[i].animate.set_color(ZIELONY) for i in (0, 2, 4)],
            run_time=0.4,
        )
        for i in (0, 2, 4):
            s6[i].set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(s5[i], s6[i]) for i in range(5)],
            r["bok_ad"].animate.set_color(ZIELONY),
            r["bok_db"].animate.set_color(ZIELONY),
            r["bok_ac"].animate.set_color(ZIELONY),
            run_time=1.3,
        )
        self.play(
            r["kat_prosty"].animate.set_color(ZIELONY),
            r["bok_cb"].animate.set_color(ZIELONY),
            run_time=0.6,
        )
        self.zgas(s6[0], s6[2], s6[4], r["bok_ad"], r["bok_db"],
                  r["bok_ac"], r["bok_cb"], r["kat_prosty"])
        self.postoj()

        # ================================================================
        # KROK 7. Znane boki zamieniaja sie w liczby przylatujace z rysunku.
        # |AB| zostaje nazwa, bo to jest niewiadoma.
        # ================================================================
        self.next_section("krok7")
        kopie = self.przywolaj(
            [r["dl_ac"], r["dl_cb"]],
            [s6[2].get_center(), s6[4].get_center()],
            czas=1.2,
        )
        s7[2].set_color(ZIELONY)
        s7[4].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s6[0], s7[0]),
            ReplacementTransform(s6[1], s7[1]),
            ReplacementTransform(s6[3], s7[3]),
            ReplacementTransform(kopie[0], s7[2]),
            ReplacementTransform(kopie[1], s7[4]),
            FadeOut(s6[2], scale=0.4), FadeOut(s6[4], scale=0.4),
            run_time=1.4,
        )
        self.zgas(s7[2], s7[4])
        self.postoj()

        # ================================================================
        # KROK 8. Podnoszenie do kwadratu. Pierwiastek i kwadrat znosza sie
        # nawzajem, wiec pod rachunkiem staje na chwile ogniwo
        # sqrt(15) * sqrt(15) = 15 (to samo, ktore niesie komentarz
        # w solutionText). Osemka podnosi sie do kwadratu w tym samym ruchu:
        # to jedno dzialanie zrobione w dwoch miejscach naraz.
        # ================================================================
        self.next_section("krok8")
        self.play(
            s7[2].animate.set_color(ZIELONY),
            s7[4].animate.set_color(ZIELONY),
            run_time=0.4,
        )
        self.play(FadeIn(ogniwo8), run_time=0.7)
        self.wait(0.5)
        s8[2].set_color(ZIELONY)
        s8[4].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s7[0], s8[0]),
            ReplacementTransform(s7[1], s8[1]),
            ReplacementTransform(s7[3], s8[3]),
            ReplacementTransform(s7[2], s8[2]),
            ReplacementTransform(s7[4], s8[4]),
            FadeOut(ogniwo8, shift=DOWN * 0.3),
            run_time=1.3,
        )
        self.zgas(s8[2], s8[4])
        self.postoj()

        # ================================================================
        # KROK 9. Przeniesienie pietnastki na druga strone. Dopisek dzialania
        # jest szary (README, punkt 36), a liczba leci LUKIEM nad znakiem
        # rownosci, nie przez niego (README, punkt 27).
        # ================================================================
        self.next_section("krok9")
        self.play(FadeIn(dopisek), run_time=0.5)
        self.play(s8[2].animate.set_color(ZIELONY), run_time=0.35)
        s9[3].set_color(ZIELONY)
        s9[4].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s8[0], s9[0]),
            ReplacementTransform(s8[3], s9[1]),
            ReplacementTransform(s8[4], s9[2]),
            ReplacementTransform(s8[2], s9[4]),
            FadeOut(s8[1], scale=0.4),
            FadeIn(s9[3]),
            FadeOut(dopisek),
            run_time=1.4, path_arc=-2 * PI / 3,
        )
        self.zgas(s9[3], s9[4])
        self.postoj()

        # ================================================================
        # KROK 10. Odejmowanie.
        # ================================================================
        self.next_section("krok10")
        self.play(
            *[s9[i].animate.set_color(ZIELONY) for i in (2, 3, 4)],
            run_time=0.4,
        )
        s10[2].set_color(ZIELONY)
        kopie_celu = [s10[2].copy() for _ in range(3)]
        self.play(
            ReplacementTransform(s9[0], s10[0]),
            ReplacementTransform(s9[1], s10[1]),
            *[ReplacementTransform(z, k)
              for z, k in zip((s9[2], s9[3], s9[4]), kopie_celu)],
            run_time=1.2,
        )
        self.remove(*kopie_celu)
        self.add(s10[2])
        self.zgas(s10[2])
        self.postoj()

        # ================================================================
        # KROK 11. Pierwiastkowanie. Ogniwo 7 * 7 = 49 staje na chwile pod
        # rachunkiem, a policzona siodemka odlatuje na rysunek i zostaje pod
        # klamra przy AB. Od tej chwili dlugosc AB jest widoczna na rysunku,
        # a nie tylko w rachunku.
        # ================================================================
        self.next_section("krok11")
        self.play(s10[2].animate.set_color(ZIELONY), run_time=0.35)
        self.play(FadeIn(ogniwo11), run_time=0.7)
        self.wait(0.5)
        s11[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s10[0], s11[0]),
            ReplacementTransform(s10[1], s11[1]),
            ReplacementTransform(s10[2], s11[2]),
            FadeOut(ogniwo11, shift=DOWN * 0.3),
            run_time=1.2,
        )
        kopia = s11[2].copy()
        self.add(kopia)
        r["dl_ab"].set_color(ZIELONY)
        self.play(
            kopia.animate.move_to(r["dl_ab"].get_center()).scale(0.75),
            run_time=1.1, path_arc=PI / 4,
        )
        self.play(FadeIn(r["dl_ab"]), FadeOut(kopia), run_time=0.35)
        self.zgas(s11[2], r["dl_ab"])
        self.postoj()

        # ================================================================
        # KROK 12. Wracamy do relacji z kroku 4: w miejsce |AB| wchodzi
        # siodemka, ktora przylatuje z rysunku.
        # ================================================================
        self.next_section("krok12")
        kopie = self.przywolaj([r["dl_ab"]], [e4[2].get_center()], czas=1.1, luk=PI / 3)
        e12[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(e4[0], e12[0]),
            ReplacementTransform(e4[1], e12[1]),
            ReplacementTransform(e4[3], e12[3]),
            ReplacementTransform(e4[4], e12[4]),
            ReplacementTransform(kopie[0], e12[2]),
            FadeOut(e4[2], scale=0.4),
            run_time=1.3,
        )
        self.zgas(e12[2])
        self.postoj()

        # ================================================================
        # KROK 13. Odejmowanie odcinkow. Jedynka odlatuje na rysunek i zastepuje
        # znak zapytania. Teraz na rysunku stoja obok siebie 7 przy AB i 1 przy
        # AD: dwa rozne odcinki, dwie rozne liczby.
        # ================================================================
        self.next_section("krok13")
        self.play(
            *[e12[i].animate.set_color(ZIELONY) for i in (2, 3, 4)],
            run_time=0.4,
        )
        e13[2].set_color(ZIELONY)
        kopie_celu = [e13[2].copy() for _ in range(3)]
        self.play(
            ReplacementTransform(e12[0], e13[0]),
            ReplacementTransform(e12[1], e13[1]),
            *[ReplacementTransform(z, k)
              for z, k in zip((e12[2], e12[3], e12[4]), kopie_celu)],
            run_time=1.2,
        )
        self.remove(*kopie_celu)
        self.add(e13[2])
        kopia = e13[2].copy()
        self.add(kopia)
        r["dl_ad"].set_color(ZIELONY)
        self.play(
            kopia.animate.move_to(r["znak_ad"].get_center()).scale(0.75),
            run_time=1.1, path_arc=PI / 4,
        )
        self.play(
            FadeIn(r["dl_ad"]), FadeOut(kopia), FadeOut(r["znak_ad"]),
            run_time=0.4,
        )
        self.zgas(e13[2], r["dl_ad"])
        self.postoj()

        # ================================================================
        # KROK 14. Powrot do tangensa. Obie przyprostokatne przylatuja
        # z rysunku, kazda ze swojego odcinka.
        # ================================================================
        self.next_section("krok14")
        licz14, kreska14, mian14 = c14[2]
        kopie = self.przywolaj(
            [r["dl_ac"], r["dl_ad"]],
            [licz3.get_center(), mian3.get_center()],
            czas=1.2,
        )
        licz14.set_color(ZIELONY)
        mian14.set_color(ZIELONY)
        self.play(
            ReplacementTransform(c3[0][0], c14[0][0]),
            ReplacementTransform(c3[0][1], c14[0][1]),
            ReplacementTransform(c3[1], c14[1]),
            ReplacementTransform(kreska3, kreska14),
            ReplacementTransform(kopie[0], licz14),
            ReplacementTransform(kopie[1], mian14),
            FadeOut(licz3, scale=0.4), FadeOut(mian3, scale=0.4),
            run_time=1.4,
        )
        self.zgas(licz14, mian14)
        self.postoj()

        # ================================================================
        # KROK 15. Dzielenie przez jeden niczego nie zmienia: jedynka gasnie
        # razem z kreska ulamka, a pierwiastek zjezdza na jej miejsce.
        # ================================================================
        self.next_section("krok15")
        self.play(
            mian14.animate.set_color(ZIELONY),
            kreska14.animate.set_color(ZIELONY),
            run_time=0.4,
        )
        c15[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(c14[0][0], c15[0][0]),
            ReplacementTransform(c14[0][1], c15[0][1]),
            ReplacementTransform(c14[1], c15[1]),
            ReplacementTransform(licz14, c15[2]),
            FadeOut(mian14, scale=0.4),
            FadeOut(kreska14, scale=0.4),
            run_time=1.3,
        )
        self.play(FadeIn(werdykt), run_time=0.5)
        self.zgas(c15[2])
        self.postoj()
