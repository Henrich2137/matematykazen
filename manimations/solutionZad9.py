from manim import *

# Zadanie 9 (otwarte, 2 pkt). Rozwiąż x(x-6) <= 7. Wynik: x nalezy do <-1, 7>.
#
# Projekt: issues/projekt-zad9-zad10-2024-grudzien.md. Scenariusz krokow opisowo:
# manimations/zad9-kroki.md. Dwadziescia dwa kroki, jeden do jednego
# z dwudziestoma dwoma linijkami rachunku w solutionText.
#
# WERSJA DRUGA, 2026-08-28, po uwagach Henricha do pierwszej (TODO.md):
#   - krok 5: najpierw przed x^2 pojawia sie jedynka, i dopiero z niej rodzi sie
#     a = 1 (README, punkt 39). Wspolczynniki sa mniejsze i rozsuniete (punkt 41);
#   - krok 6: nierownosc znika, wjezdza wzor na delte w postaci LITEROWEJ, a
#     wartosci przylatuja z pasa notatek na miejsca liter (punkt 37);
#   - kroki 10 do 18: wjezdzaja OBA wzory na pierwiastki, tak jak stoja w tablicy
#     (s. 8). Najpierw pierwszy dostaje liczby i jest liczony do konca, potem
#     drugi. Liczby sa za kazdym razem PRZYWOLYWANE z pasa notatek (punkt 38).
#
# Pas notatek stoi pod rachunkiem od kroku 5 do kroku 18: a = 1, b = -6, c = -7
# i dolaczajacy w kroku 10 pierwiastek z delty. Znika dopiero w kroku 19, kiedy
# kadr przemeblowuje sie pod rysunek.
#
# Kolor: zielone = to, co sie w danym kroku ZMIENIA (README, "Jak ma wygladac
# animacja"). Ulamki w torach sa skladane RECZNIE (licznik, kreska, mianownik),
# bo MathTex z \dfrac nie daje uchwytu do pojedynczej liczby w liczniku, a bez
# tego nie da sie zapalic samej szostki powstalej z podwojnego minusa.
#
# Wykres w krokach 20 do 22 uzywa fioletu `--accent-purple` (#7a3fa8, COLORS.md,
# rola "wykres funkcji jak w arkuszach CKE"). Os jest szara (#666666).
#
# Render: manim --save_sections solutionZad9.py Zad9  (albo tools/wgraj-kroki.sh 9)

ZIELONY = "#2e7d32"
FIOLET = "#7a3fa8"
SZARY_OSIE = "#666666"
SZARY_DOPISEK = "#888888"

ROWNANIE_Y = UP * 0.75
GORA_Y = UP * 2.4
KOEF_Y = DOWN * 2.35
POSTOJ = 0.45


class Zad9(Scene):

    # ---- klocki, jak w solutionZad8.py --------------------------------

    def stan(self, *args, rozmiar=100):
        m = MathTex(*args)
        m.set_color(BLACK)
        m.font_size = rozmiar
        return m

    def ulamek(self, gora, dol, rozmiar=76):
        """Ulamek zlozony recznie: licznik, kreska, mianownik. Daje uchwyt do
        kazdego glifu licznika, czego \\dfrac w jednym MathTeksie nie daje."""
        g = self.stan(*gora, rozmiar=rozmiar)
        d = self.stan(*dol, rozmiar=rozmiar)
        szer = max(g.width, d.width) + 0.22
        kreska = Line(LEFT * szer / 2, RIGHT * szer / 2, color=BLACK, stroke_width=4)
        g.next_to(kreska, UP, buff=0.14)
        d.next_to(kreska, DOWN, buff=0.14)
        return VGroup(g, kreska, d)

    def tor(self, nazwa, ulamek, rozmiar=76):
        """x_1 = <ulamek>, jako jedna grupa z uchwytami do czesci."""
        etykieta = self.stan(nazwa, rozmiar=rozmiar)
        rowna = self.stan("=", rozmiar=rozmiar)
        return VGroup(etykieta, rowna, ulamek).arrange(RIGHT, buff=0.22)

    def zapal(self, *mobiekty, czas=0.4):
        self.play(*[m.animate.set_color(ZIELONY) for m in mobiekty], run_time=czas)

    def zakoncz(self, *czysty, pomin=(), czas=0.4):
        self.wait(0.3)
        gasnie = [m for m in self.mobjects if not any(m is p for p in pomin)]
        if gasnie:
            self.play(*[m.animate.set_color(BLACK) for m in gasnie], run_time=czas)
        self.clear()
        # Stan wstawiany na czysto tez musi byc czarny. Cel animacji `Transform`
        # nigdy nie trafia na scene, wiec jego zielony glif nie bierze udzialu
        # w gaszeniu powyzej, a po `add` ladowalby zielony na ostatniej klatce
        # (lapie to tools/zielen-krokow.py).
        for m in czysty:
            if not any(m is p for p in pomin):
                m.set_color(BLACK)
        self.add(*czysty)
        self.wait(0.25)

    def construct(self):
        # ================================================================
        # Stany rachunku, po jednym MathTex na krok.
        # ================================================================
        s1 = self.stan("x", "(", "x", "-", "6", ")", r"\le", "7")
        s2 = self.stan("x", r"\cdot", "x", "-", "x", r"\cdot", "6", r"\le", "7")
        s3 = self.stan("x", "^{2}", "-", "6", "x", r"\le", "7")
        dop3 = self.stan(r"\big/", "-", "7", rozmiar=72)
        dop3.set_color(SZARY_DOPISEK)
        s4 = self.stan("x", "^{2}", "-", "6", "x", "-", "7", r"\le", "0")
        # Ta sama nierownosc z dopisana jedynka przy x^2.
        s5 = self.stan("1", "x", "^{2}", "-", "6", "x", "-", "7", r"\le", "0")

        s6lit = self.stan(r"\Delta", "=", "b", "^{2}", "-", "4", "a", "c")
        s6 = self.stan(r"\Delta", "=", "(", "-", "6", ")", "^{2}", "-", "4",
                       r"\cdot", "1", r"\cdot", "(", "-", "7", ")")
        s7 = self.stan(r"\Delta", "=", "36", "+", "28")
        s8 = self.stan(r"\Delta", "=", "64")
        s9 = self.stan(r"\sqrt{\Delta}", "=", "8")

        s19 = self.stan(r"x_{1} = -1, \quad x_{2} = 7")
        s19_gora = self.stan(r"x_{1} = -1, \quad x_{2} = 7")

        # Pas notatek: wartosci odczytane raz i przywolywane pozniej.
        # Mniejszym pismem niz rachunek, zeby bylo widac, ze to notatka
        # z boku, a nie kolejna linijka (README, punkt 41).
        a_cz = self.stan("a", "=", "1", rozmiar=62)
        b_cz = self.stan("b", "=", "-", "6", rozmiar=62)
        c_cz = self.stan("c", "=", "-", "7", rozmiar=62)
        d_cz = self.stan(r"\sqrt{\Delta}", "=", "8", rozmiar=62)

        # Wspolna skala rachunku. Dopisek i pas licza sie osobno.
        MARGINES = 0.85
        glowne = [s1, s2, s3, s4, s5, s6lit, s6, s7, s8, s9, s19, s19_gora]
        najszerszy = max(m.width for m in glowne)
        POLE = config.frame_width * MARGINES
        wsp = min(1.0, POLE / najszerszy)
        for m in glowne + [dop3]:
            m.scale(wsp)
        for m in glowne:
            m.move_to(ROWNANIE_Y)
        s19_gora.move_to(GORA_Y)

        pas = VGroup(a_cz, b_cz, c_cz, d_cz).arrange(RIGHT, buff=1.15)
        pas.move_to(KOEF_Y)

        # ---- dwa tory: wzory na pierwiastki i ich kolejne stany --------
        w1 = self.tor(r"x_{1}", self.ulamek(("-b", "-", r"\sqrt{\Delta}"), ("2a",)))
        w2 = self.tor(r"x_{2}", self.ulamek(("-b", "+", r"\sqrt{\Delta}"), ("2a",)))
        x1a = self.tor(r"x_{1}", self.ulamek(("-", "(", "-6", ")", "-", "8"),
                                             ("2", r"\cdot", "1")))
        x1b = self.tor(r"x_{1}", self.ulamek(("6", "-", "8"), ("2",)))
        x1c = self.tor(r"x_{1}", self.ulamek(("-2",), ("2",)))
        x1d = VGroup(self.stan(r"x_{1}", rozmiar=76), self.stan("=", rozmiar=76),
                     self.stan("-1", rozmiar=76)).arrange(RIGHT, buff=0.22)
        x2a = self.tor(r"x_{2}", self.ulamek(("-", "(", "-6", ")", "+", "8"),
                                             ("2", r"\cdot", "1")))
        x2b = self.tor(r"x_{2}", self.ulamek(("6", "+", "8"), ("2",)))
        x2c = self.tor(r"x_{2}", self.ulamek(("14",), ("2",)))
        x2d = VGroup(self.stan(r"x_{2}", rozmiar=76), self.stan("=", rozmiar=76),
                     self.stan("7", rozmiar=76)).arrange(RIGHT, buff=0.22)

        torowe_l = [w1, x1a, x1b, x1c, x1d]
        torowe_p = [w2, x2a, x2b, x2c, x2d]
        najszersza_para = max(l.width + p.width
                              for l, p in zip(torowe_l, torowe_p))
        wsp_tor = min(1.0, (POLE - 1.4) / najszersza_para)
        for m in torowe_l + torowe_p:
            m.scale(wsp_tor)
        TOR_L = LEFT * (POLE / 4 + 0.15) + ROWNANIE_Y
        TOR_P = RIGHT * (POLE / 4 + 0.15) + ROWNANIE_Y
        for m in torowe_l:
            m.move_to(TOR_L)
        for m in torowe_p:
            m.move_to(TOR_P)

        def przywolaj(zrodla, cele, czas=1.0):
            """Kopie wartosci z pasa notatek leca w okolice miejsc, w ktore
            wchodza we wzorze. Zielone, bo to one sa tym, co sie zmienia."""
            kopie = []
            for zrodlo in zrodla:
                k = zrodlo.copy().set_opacity(0)
                self.add(k)
                kopie.append(k)
            self.play(
                *[k.animate.set_opacity(1).set_color(ZIELONY).move_to(c)
                  for k, c in zip(kopie, cele)],
                run_time=czas, path_arc=-PI / 4,
            )
            return kopie

        # ================================================================
        # KROK 1. Nierówność z treści zadania. Bez koloru.
        # ================================================================
        self.next_section("krok1")
        self.play(Write(s1), run_time=1.4)
        self.wait(0.25)

        # ================================================================
        # KROK 2. Opuszczamy nawias: x sprzed nawiasu rozdwaja się przed
        # każdy składnik. Zielone: dwa nowe x i obie kropki mnożenia.
        # ================================================================
        self.next_section("krok2")
        self.zapal(s1[0])
        kopia_a = s1[0].copy()
        kopia_b = s1[0].copy()
        self.add(kopia_a, kopia_b)
        s2[0].set_color(ZIELONY)
        s2[1].set_color(ZIELONY)
        s2[4].set_color(ZIELONY)
        s2[5].set_color(ZIELONY)
        self.play(
            ReplacementTransform(kopia_a, s2[0]),
            FadeIn(s2[1]),
            ReplacementTransform(s1[2], s2[2]),
            ReplacementTransform(s1[3], s2[3]),
            ReplacementTransform(kopia_b, s2[4]),
            FadeIn(s2[5]),
            ReplacementTransform(s1[4], s2[6]),
            FadeOut(s1[1]), FadeOut(s1[5]),
            ReplacementTransform(s1[6], s2[7]),
            ReplacementTransform(s1[7], s2[8]),
            FadeOut(s1[0], scale=0.5),
            run_time=1.4,
        )
        self.zakoncz(s2)

        # ================================================================
        # KROK 3. x*x -> x^2 (wykładnik się pojawia, zielony), x*6 -> 6x
        # (sama zamiana kolejności, bez koloru).
        # ================================================================
        self.next_section("krok3")
        self.zapal(s2[2])
        s3[1].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s2[0], s3[0]),
            FadeOut(s2[1], scale=0.4),
            FadeOut(s2[2], scale=0.4),
            FadeIn(s3[1]),
            ReplacementTransform(s2[3], s3[2]),
            ReplacementTransform(s2[6], s3[3]),
            FadeOut(s2[5], scale=0.4),
            ReplacementTransform(s2[4], s3[4]),
            ReplacementTransform(s2[7], s3[5]),
            ReplacementTransform(s2[8], s3[6]),
            run_time=1.4,
        )
        self.zakoncz(s3)
        dop3.next_to(s3, RIGHT, buff=0.9)
        self.play(FadeIn(dop3, shift=LEFT * 0.3), run_time=0.6)
        self.wait(0.25)

        # ================================================================
        # KROK 4. Siódemka z dopisku leci łukiem nad znakiem <=, staje się
        # -7; po prawej zostaje 0. Zielone: minus przy siódemce i zero.
        # ================================================================
        self.next_section("krok4")
        self.zapal(dop3[1], dop3[2])
        s4[5].set_color(ZIELONY)
        s4[8].set_color(ZIELONY)
        self.play(
            ReplacementTransform(dop3[2], s4[6], path_arc=-2 * PI / 3),
            ReplacementTransform(dop3[1], s4[5], path_arc=-2 * PI / 3),
            FadeOut(dop3[0], scale=0.4),
            ReplacementTransform(s3[6], s4[8]),
            ReplacementTransform(s3[0], s4[0]),
            ReplacementTransform(s3[1], s4[1]),
            ReplacementTransform(s3[2], s4[2]),
            ReplacementTransform(s3[3], s4[3]),
            ReplacementTransform(s3[4], s4[4]),
            ReplacementTransform(s3[5], s4[7]),
            run_time=1.4,
        )
        self.zakoncz(s4)

        # ================================================================
        # KROK 5. Najpierw przed x^2 staje jedynka, ktorej dotad nie bylo
        # widac, i dopiero z niej rodzi sie a = 1. Potem oba minusy razem
        # ze swoimi liczbami zjezdzaja do pasa notatek.
        # Zielone: jedynka, a potem to, co zjezdza.
        # ================================================================
        self.next_section("krok5")
        s5[0].set_color(ZIELONY)
        self.play(
            FadeIn(s5[0], shift=RIGHT * 0.2),
            ReplacementTransform(s4[0], s5[1]),
            ReplacementTransform(s4[1], s5[2]),
            ReplacementTransform(s4[2], s5[3]),
            ReplacementTransform(s4[3], s5[4]),
            ReplacementTransform(s4[4], s5[5]),
            ReplacementTransform(s4[5], s5[6]),
            ReplacementTransform(s4[6], s5[7]),
            ReplacementTransform(s4[7], s5[8]),
            ReplacementTransform(s4[8], s5[9]),
            run_time=1.2,
        )
        self.wait(0.4)

        kop_a = s5[0].copy()
        kop_b = s5[3:5].copy()
        kop_c = s5[6:8].copy()
        self.add(kop_a, kop_b, kop_c)
        self.zapal(s5[3], s5[4], s5[6], s5[7], czas=0.3)
        for m in (a_cz[2], b_cz[2], b_cz[3], c_cz[2], c_cz[3]):
            m.set_color(ZIELONY)
        self.play(
            FadeIn(a_cz[0], a_cz[1]),
            ReplacementTransform(kop_a, a_cz[2]),
            FadeIn(b_cz[0], b_cz[1]),
            ReplacementTransform(kop_b, b_cz[2:4]),
            FadeIn(c_cz[0], c_cz[1]),
            ReplacementTransform(kop_c, c_cz[2:4]),
            *[g.animate.set_color(BLACK)
              for g in (s5[0], s5[3], s5[4], s5[6], s5[7])],
            run_time=1.4,
        )
        self.zakoncz(s5, a_cz, b_cz, c_cz, pomin=[s5])

        # ================================================================
        # KROK 6. Nierownosc znika, wjezdza wzor na delte w postaci
        # literowej, a wartosci przylatuja z pasa na miejsca liter.
        # Zielone: przylatujace liczby.
        # ================================================================
        self.next_section("krok6")
        self.play(FadeOut(s5, shift=UP * 0.3), FadeIn(s6lit), run_time=0.9)
        self.wait(0.3)

        kop_b2, kop_a2, kop_c2 = przywolaj(
            [b_cz[2:4], a_cz[2], c_cz[2:4]],
            [s6lit[2].get_center(), s6lit[6].get_center(), s6lit[7].get_center()],
        )
        for i in (3, 4, 10, 13, 14):
            s6[i].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s6lit[0], s6[0]),
            ReplacementTransform(s6lit[1], s6[1]),
            FadeIn(s6[2]), FadeIn(s6[5]),
            ReplacementTransform(kop_b2, s6[3:5]),
            FadeOut(s6lit[2], scale=0.4),
            ReplacementTransform(s6lit[3], s6[6]),
            ReplacementTransform(s6lit[4], s6[7]),
            ReplacementTransform(s6lit[5], s6[8]),
            FadeIn(s6[9]),
            ReplacementTransform(kop_a2, s6[10]),
            FadeOut(s6lit[6], scale=0.4),
            FadeIn(s6[11], s6[12], s6[15]),
            ReplacementTransform(kop_c2, s6[13:15]),
            FadeOut(s6lit[7], scale=0.4),
            run_time=1.6,
        )
        self.zakoncz(s6, a_cz, b_cz, c_cz)

        # ================================================================
        # KROK 7. (-6)^2 -> 36, -4*1*(-7) -> +28. Zielone: tylko plus,
        # bo iloczyn dwoch liczb ujemnych daje plus.
        # ================================================================
        self.next_section("krok7")
        self.zapal(*s6[2:16])
        s7[3].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s6[0], s7[0]),
            ReplacementTransform(s6[1], s7[1]),
            Transform(VGroup(*s6[2:7]), s7[2]),
            FadeIn(s7[3]),
            Transform(VGroup(*s6[7:16]), s7[4]),
            run_time=1.5,
        )
        self.zakoncz(s7, a_cz, b_cz, c_cz)

        # ================================================================
        # KROK 8. 36+28 -> 64. Bez koloru.
        # ================================================================
        self.next_section("krok8")
        self.play(
            ReplacementTransform(s7[0], s8[0]),
            ReplacementTransform(s7[1], s8[1]),
            Transform(VGroup(s7[2], s7[3], s7[4]), s8[2]),
            run_time=1.3,
        )
        self.zakoncz(s8, a_cz, b_cz, c_cz)

        # ================================================================
        # KROK 9. Nad delta pojawia sie pierwiastek, 64 zamienia sie w 8.
        # Zielone: sama osemka.
        # ================================================================
        self.next_section("krok9")
        self.zapal(s8[2])
        s9[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s8[0], s9[0]),
            ReplacementTransform(s8[1], s9[1]),
            ReplacementTransform(s8[2], s9[2]),
            run_time=1.3,
        )
        self.zakoncz(s9, a_cz, b_cz, c_cz)

        # ================================================================
        # KROK 10. Pierwiastek z delty dolacza do pasa notatek, a w kadr
        # wjezdzaja OBA wzory na miejsca zerowe, tak jak stoja w tablicy.
        # Bez koloru: nic sie tu nie przelicza.
        # ================================================================
        self.next_section("krok10")
        self.play(Transform(s9, d_cz.copy()), run_time=1.0)
        self.remove(s9)
        self.add(d_cz)
        self.play(FadeIn(w1, shift=UP * 0.2), FadeIn(w2, shift=UP * 0.2),
                  run_time=0.9)
        self.zakoncz(w1, w2, pas)

        # ================================================================
        # KROK 11. Do PIERWSZEGO wzoru wracaja liczby z pasa notatek.
        # Zielone: przywolane wartosci.
        # ================================================================
        self.next_section("krok11")
        licznik1 = w1[2][0]
        kopie = przywolaj(
            [b_cz[2:4], d_cz[2], a_cz[2]],
            [licznik1[0].get_center(), licznik1[2].get_center(),
             w1[2][2].get_center()],
        )
        self.play(
            *[FadeOut(k, scale=0.5) for k in kopie],
            ReplacementTransform(w1, x1a),
            run_time=1.1,
        )
        self.zakoncz(x1a, w2, pas)

        # ================================================================
        # KROK 12. -(-6) -> 6 (dwa minusy daja szostke, zielona),
        # 2*1 -> 2 bez koloru.
        # ================================================================
        self.next_section("krok12")
        self.zapal(x1a[2][0][0], x1a[2][0][1], x1a[2][0][2], x1a[2][0][3])
        x1b[2][0][0].set_color(ZIELONY)
        self.play(
            ReplacementTransform(x1a[0], x1b[0]),
            ReplacementTransform(x1a[1], x1b[1]),
            Transform(VGroup(*x1a[2][0][0:4]), x1b[2][0][0]),
            ReplacementTransform(x1a[2][0][4], x1b[2][0][1]),
            ReplacementTransform(x1a[2][0][5], x1b[2][0][2]),
            ReplacementTransform(x1a[2][1], x1b[2][1]),
            Transform(VGroup(*x1a[2][2]), x1b[2][2]),
            run_time=1.3,
        )
        self.zakoncz(x1b, w2, pas)

        # ================================================================
        # KROK 13. 6-8 -> -2. Zielone: wynik odejmowania.
        # ================================================================
        self.next_section("krok13")
        self.zapal(*x1b[2][0])
        x1c[2][0][0].set_color(ZIELONY)
        self.play(
            ReplacementTransform(x1b[0], x1c[0]),
            ReplacementTransform(x1b[1], x1c[1]),
            Transform(VGroup(*x1b[2][0]), x1c[2][0][0]),
            ReplacementTransform(x1b[2][1], x1c[2][1]),
            ReplacementTransform(x1b[2][2], x1c[2][2]),
            run_time=1.3,
        )
        self.zakoncz(x1c, w2, pas)

        # ================================================================
        # KROK 14. -2/2 -> -1. Bez koloru.
        # ================================================================
        self.next_section("krok14")
        self.play(
            ReplacementTransform(x1c[0], x1d[0]),
            ReplacementTransform(x1c[1], x1d[1]),
            Transform(x1c[2], x1d[2]),
            run_time=1.3,
        )
        self.zakoncz(x1d, w2, pas)

        # ================================================================
        # KROK 15. Teraz DRUGI wzor. Pierwszy wynik czeka po lewej.
        # Zielone: przywolane wartosci.
        # ================================================================
        self.next_section("krok15")
        licznik2 = w2[2][0]
        kopie = przywolaj(
            [b_cz[2:4], d_cz[2], a_cz[2]],
            [licznik2[0].get_center(), licznik2[2].get_center(),
             w2[2][2].get_center()],
        )
        self.play(
            *[FadeOut(k, scale=0.5) for k in kopie],
            ReplacementTransform(w2, x2a),
            run_time=1.1,
        )
        self.zakoncz(x1d, x2a, pas)

        # ================================================================
        # KROK 16. -(-6) -> 6, 2*1 -> 2.
        # ================================================================
        self.next_section("krok16")
        self.zapal(x2a[2][0][0], x2a[2][0][1], x2a[2][0][2], x2a[2][0][3])
        x2b[2][0][0].set_color(ZIELONY)
        self.play(
            ReplacementTransform(x2a[0], x2b[0]),
            ReplacementTransform(x2a[1], x2b[1]),
            Transform(VGroup(*x2a[2][0][0:4]), x2b[2][0][0]),
            ReplacementTransform(x2a[2][0][4], x2b[2][0][1]),
            ReplacementTransform(x2a[2][0][5], x2b[2][0][2]),
            ReplacementTransform(x2a[2][1], x2b[2][1]),
            Transform(VGroup(*x2a[2][2]), x2b[2][2]),
            run_time=1.3,
        )
        self.zakoncz(x1d, x2b, pas)

        # ================================================================
        # KROK 17. 6+8 -> 14. Zielone: wynik dodawania.
        # ================================================================
        self.next_section("krok17")
        self.zapal(*x2b[2][0])
        x2c[2][0][0].set_color(ZIELONY)
        self.play(
            ReplacementTransform(x2b[0], x2c[0]),
            ReplacementTransform(x2b[1], x2c[1]),
            Transform(VGroup(*x2b[2][0]), x2c[2][0][0]),
            ReplacementTransform(x2b[2][1], x2c[2][1]),
            ReplacementTransform(x2b[2][2], x2c[2][2]),
            run_time=1.3,
        )
        self.zakoncz(x1d, x2c, pas)

        # ================================================================
        # KROK 18. 14/2 -> 7. Bez koloru.
        # ================================================================
        self.next_section("krok18")
        self.play(
            ReplacementTransform(x2c[0], x2d[0]),
            ReplacementTransform(x2c[1], x2d[1]),
            Transform(x2c[2], x2d[2]),
            run_time=1.3,
        )
        self.zakoncz(x1d, x2d, pas)

        # ================================================================
        # KROK 19. Oba wyniki zjezdzaja w jedna linijke, a pas notatek
        # znika: dalej juz nie jest potrzebny. Bez koloru.
        # ================================================================
        self.next_section("krok19")
        self.play(
            Transform(VGroup(x1d, x2d), s19.copy()),
            FadeOut(pas, shift=DOWN * 0.3),
            run_time=1.3,
        )
        self.remove(x1d, x2d)
        self.zakoncz(s19)

        # ================================================================
        # KROK 20. Linijka wynikow odjezdza w gore i zostaje tam do konca.
        # Pod nia rysuje sie os x, a przez -1 i 7 przechodzi parabola
        # ramionami w gore. Bez koloru: sam rysunek niczego nie przelicza.
        # ================================================================
        self.next_section("krok20")
        os_x = NumberLine(
            x_range=[-3, 9, 1], length=9, include_ticks=False,
            color=SZARY_OSIE, stroke_width=3,
        ).move_to(DOWN * 0.9)
        etykieta_m1 = MathTex("-1", color=SZARY_OSIE, font_size=64)
        etykieta_m1.next_to(os_x.n2p(-1), DOWN, buff=0.2)
        etykieta_7 = MathTex("7", color=SZARY_OSIE, font_size=64)
        etykieta_7.next_to(os_x.n2p(7), DOWN, buff=0.2)
        znacznik_m1 = Dot(os_x.n2p(-1), radius=0.05, color=SZARY_OSIE)
        znacznik_7 = Dot(os_x.n2p(7), radius=0.05, color=SZARY_OSIE)

        Y_SKALA = 0.06

        def f(t):
            return (t + 1) * (t - 7)

        def punkt(t):
            return os_x.n2p(t) + UP * f(t) * Y_SKALA

        parabola = ParametricFunction(
            punkt, t_range=[-3, 9], color=FIOLET, stroke_width=5,
        )
        rysunek = VGroup(os_x, znacznik_m1, znacznik_7, etykieta_m1, etykieta_7)

        self.play(Transform(s19, s19_gora.copy()), run_time=1.0)
        self.remove(s19)
        self.add(s19_gora)
        self.play(Create(os_x), run_time=0.8)
        self.play(
            FadeIn(znacznik_m1, etykieta_m1),
            FadeIn(znacznik_7, etykieta_7),
            run_time=0.6,
        )
        self.play(Create(parabola), run_time=1.4)
        self.zakoncz(s19_gora, rysunek, parabola,
                     pomin=[s19_gora, parabola, rysunek, *rysunek])
        # Dluzszy postoj na koncu kroku: rysunek zajmuje pol kadru gladkimi
        # krzywymi, wiec koder H.264 potrzebuje kilku klatek bez ruchu, zeby
        # ostatnia klatka zgadzala sie z pierwsza klatka nastepnego kroku
        # (bez tego styk-klatek.sh schodzi ponizej progu 0,999).
        self.wait(0.35)

        # ================================================================
        # KROK 21. Fragment paraboli pod osia i odcinek na osi zapalaja
        # sie na zielono, z pelnymi kropkami na koncach.
        # ================================================================
        self.next_section("krok21")
        fragment = ParametricFunction(
            punkt, t_range=[-1, 7], color=ZIELONY, stroke_width=7,
        )
        odcinek = Line(os_x.n2p(-1), os_x.n2p(7), color=ZIELONY, stroke_width=7)
        kropka_l = Dot(os_x.n2p(-1), radius=0.09, color=ZIELONY)
        kropka_p = Dot(os_x.n2p(7), radius=0.09, color=ZIELONY)
        self.play(Create(fragment), run_time=1.0)
        self.play(
            Create(odcinek), FadeIn(kropka_l), FadeIn(kropka_p),
            run_time=0.8,
        )
        self.wait(0.35)
        self.play(fragment.animate.set_color(BLACK), run_time=0.4)
        self.remove(fragment)
        self.zakoncz(s19_gora, rysunek, parabola, odcinek, kropka_l, kropka_p,
                     pomin=[s19_gora, parabola, rysunek, *rysunek])
        self.wait(0.35)

        # ================================================================
        # KROK 22. Odcinek zamienia sie w zapis x nalezy do <-1, 7>.
        # ================================================================
        self.next_section("krok22")
        # Krotki postoj na starcie: pierwsza klatka kroku ma byc czystym stanem
        # koncowym poprzedniego, a nie klatka t=0 animacji.
        self.wait(0.2)
        wynik = MathTex(r"x \in \langle -1,\ 7\rangle", color=BLACK, font_size=90)
        wynik.move_to(DOWN * 3.05)
        self.play(
            ReplacementTransform(VGroup(odcinek, kropka_l, kropka_p), wynik),
            run_time=1.2,
        )
        self.remove(odcinek, kropka_l, kropka_p)
        self.zakoncz(s19_gora, rysunek, parabola, wynik,
                     pomin=[s19_gora, parabola, wynik, rysunek, *rysunek])
