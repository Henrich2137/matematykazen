from manim import *

from _wspolne import MARGINES, PRZYTRZYMANIE


# Zadanie 8 (otwarte, 3 pkt). Rozwiąż (x+3)/(x-1) = x/(2x-2). Wynik: x = -6.
#
# Spec i podział na kroki: issues/spec-zad8-2024-grudzien.md, scenariusz ruchu:
# manimations/zad8-kroki.md. Dziesięć kroków, jeden do jednego z dziesięcioma
# linijkami rachunku w rozwiązaniu opisowym. Sprawdzenia przez podstawienie film
# nie pokazuje (decyzja Henricha, 2026-08-27).
#
# ---------------------------------------------------------------------------
# Napisane od nowa 2026-08-27 po uwagach Henricha do pierwszej wersji:
#
#   1. „Morf wrzucony na całą stronę równania zasłania to, co dzieje się naprawdę."
#      Pierwsza wersja robiła każdy krok jednym `TransformMatchingTex(...,
#      transform_mismatches=True)`, czyli oddawała ruch automatowi: pół równania
#      rozmazywało się w kleks, w połowie animacji nie dało się odczytać ani starego,
#      ani nowego zapisu. Tutaj nie ma ani jednego automatycznego dopasowania. Każdy
#      glif ma wskazaną parę (mapa niżej), a to, co się pojawia albo znika, jest
#      wypisane z nazwy.
#   2. „Krok mógłby zawierać wyjaśnienie, a dopiero się kończyć prostym."
#      Kroki 2, 3, 6, 7 i 10 mają w środku rachunek pomocniczy (skąd x ≠ 1, dlaczego
#      2x-2 = 2(x-1), co się skraca przy mnożeniu przez 2, skąd 6, skąd jeden iks),
#      a kończą się czystą linijką wyniku. Rachunek pomocniczy po użyciu znika.
#   3. „Założenie mniej kontrastowe." x ≠ 1 stoi w kadrze od kroku 2 do końca filmu
#      (osobny punkt w kluczu CKE), ale szarością SZARY_ZALOZENIE, żeby nie
#      konkurowało wzrokowo z rachunkiem.
# ---------------------------------------------------------------------------
#
# MAPA GLIFÓW, policzona z renderu `index_labels`, nie zgadnięta (README, punkt 20).
# Zmierzone: MathTex numeruje glify w kolejności czytania, a w ułamku idzie najpierw
# licznik, potem kreska, potem mianownik. `\ne` to DWA glify (kreski, ukośnik), `=` jeden.
#
#   s0  \frac{x+3}{x-1} = \frac{x}{2x-2}                 14
#       0 x  1 +  2 3  3 kreska  4 x  5 -  6 1  7 =  8 x  9 kreska  10 2  11 x  12 -  13 2
#   s2  \frac{x+3}{x-1} = \frac{x}{2(x-1)}               16
#       0 x  1 +  2 3  3 kreska  4 x  5 -  6 1  7 =  8 x  9 kreska  10 2  11 (  12 x  13 -  14 1  15 )
#   s3  \frac{(x+3)(x-1)}{x-1} = \frac{x(x-1)}{2(x-1)}   28
#       0 (  1 x  2 +  3 3  4 )  5 (  6 x  7 -  8 1  9 )  10 kreska  11 x  12 -  13 1
#       14 =  15 x  16 (  17 x  18 -  19 1  20 )  21 kreska  22 2  23 (  24 x  25 -  26 1  27 )
#   s3b x+3 = \frac{x(x-1)}{2(x-1)}                      17   (po skróceniu lewej strony)
#       0 x  1 +  2 3  3 =  4 x  5 (  6 x  7 -  8 1  9 )  10 kreska  11 2  12 (  13 x  14 -  15 1  16 )
#   s4  x+3 = \frac{x}{2}                                 7   0 x 1 + 2 3 3 = 4 x 5 kreska 6 2
#   s4b 2(x+3) = 2\cdot\frac{x}{2}                       12   0 2 1 ( 2 x 3 + 4 3 5 ) 6 = 7 2 8 · 9 x 10 kreska 11 2
#   s5  2(x+3) = x                                        8   0 2 1 ( 2 x 3 + 4 3 5 ) 6 = 7 x
#   s5b 2\cdot x+2\cdot 3 = x                             9   0 2 1 · 2 x 3 + 4 2 5 · 6 3 7 = 8 x
#   s6  2x+6 = x                                          6   0 2 1 x 2 + 3 6 4 = 5 x
#   s7  2x = x-6                                          6   0 2 1 x 2 = 3 x 4 - 5 6
#   s8  2x-x = -6                                         7   0 2 1 x 2 - 3 x 4 = 5 - 6 6
#   s8b 2x-1x = -6                                        8   0 2 1 x 2 - 3 1 4 x 5 = 6 - 7 6
#   s8c 1x = -6                                           5   0 1 1 x 2 = 3 - 4 6
#   s9  x = -6                                            4   0 x 1 = 2 - 3 6
#
#   rachunek pomocniczy kroku 2 (dziedzina):
#   w1  x-1 \ne 0     6   0 x  1 -  2 1  3 ≠kreski  4 ≠ukośnik  5 0
#   w2  x \ne 1       4   0 x  1 ≠kreski  2 ≠ukośnik  3 1
#   w3  2x-2 \ne 0    7   0 2  1 x  2 -  3 2  4 ≠kreski  5 ≠ukośnik  6 0
#   w4  2x \ne 2      5   0 2  1 x  2 ≠kreski  3 ≠ukośnik  4 2
#   w5  x \ne 1       4   jak w2
#
#   rachunek pomocniczy kroku 3 (wyłączanie dwójki przed nawias):
#   f1  2x-2              4   0 2  1 x  2 -  3 2
#   f2  2\cdot x-2\cdot 1 7   0 2  1 ·  2 x  3 -  4 2  5 ·  6 1
#   f3  2(x-1)            6   0 2  1 (  2 x  3 -  4 1  5 )
#
#   dopiski działań: „\big/ \cdot (x-1)" ma 7 glifów (2..6 to nawias „(x-1)"),
#   „\big/ \cdot 2" ma 3 (glif 2 to dwójka), „\big/ - 6" i „\big/ - x" po 3.
#
# Render: tools/wgraj-kroki.sh 8

# Zieleń „popatrz tutaj", czyli ten sam hex co --accent-green w jasnym motywie
# (COLORS.md, README punkt 10). To NIE jest zieleń „poprawne".
ZIELONY = "#2e7d32"
# Dwie szarości. Założenie ma być czytelne, ale słabsze od rachunku. Dopisek
# działania jest jeszcze słabszy, bo nie jest częścią rachunku, tylko zapowiedzią
# tego, co robimy z obiema stronami (tak samo jak .rozw-dzialanie w rozwiązaniu
# opisowym).
SZARY_ZALOZENIE = "#666666"
SZARY_DOPISEK = "#888888"

ROWNANIE_Y = UP * 1.05       # rachunek główny
POMOCNICZY_Y = DOWN * 0.95   # pas rachunku pomocniczego, sprzątany przed końcem kroku
ZALOZENIE_Y = DOWN * 2.25    # założenie, od kroku 2 do końca filmu
# Ile nad równaniem zatrzymuje się czynnik, który wyleciał z dopisku działania.
POSTOJ = 0.55


class Zad8(Scene):

    # ---- klocki ------------------------------------------------------------

    def stan(self, tex, rozmiar=100):
        m = MathTex(tex)
        m.set_color(BLACK)
        m.font_size = rozmiar
        return m

    def zapal(self, *mobiekty, czas=0.4):
        """Zieleń zapala się ANIMACJĄ, nigdy przed pierwszym `play`.

        Inaczej pierwsza klatka kroku jest już podświetlona, a ostatnia klatka
        kroku poprzedniego czysta, czyli dokładnie ten przeskok, którego pilnuje
        `tools/styk-klatek.sh`.
        """
        self.play(*[m.animate.set_color(ZIELONY) for m in mobiekty], run_time=czas)

    def gas(self, *mobiekty, czas=0.3):
        """Zgaszenie pojedynczych elementów w środku kroku (między taktami)."""
        self.play(*[m.animate.set_color(BLACK) for m in mobiekty], run_time=czas)

    def zakoncz(self, *czysty, pomin=(), czas=0.4):
        """Koniec kroku: zgaszenie koloru → podmiana na czysty stan → przytrzymanie.

        Gasi to, co FAKTYCZNIE leży w kadrze (`self.mobjects`), bo po serii
        przekształceń w scenie zostają obiekty źródłowe, a nie docelowe. Poza
        gaszeniem zostaje założenie i dopisek działania: one mają własną szarość.
        """
        self.wait(0.3)
        gasnie = [m for m in self.mobjects if not any(m is p for p in pomin)]
        if gasnie:
            self.play(*[m.animate.set_color(BLACK) for m in gasnie], run_time=czas)
        self.clear()
        self.add(*czysty)
        self.wait(PRZYTRZYMANIE)

    def construct(self):
        # ---- stany rachunku ------------------------------------------------
        s0 = self.stan(r"\frac{x+3}{x-1} = \frac{x}{2x-2}")
        s2 = self.stan(r"\frac{x+3}{x-1} = \frac{x}{2(x-1)}")
        s3 = self.stan(r"\frac{(x+3)(x-1)}{x-1} = \frac{x(x-1)}{2(x-1)}")
        s3b = self.stan(r"x+3 = \frac{x(x-1)}{2(x-1)}")
        s4 = self.stan(r"x+3 = \frac{x}{2}")
        s4b = self.stan(r"2(x+3) = 2\cdot\frac{x}{2}")
        s5 = self.stan(r"2(x+3) = x")
        s5b = self.stan(r"2\cdot x+2\cdot 3 = x")
        s6 = self.stan(r"2x+6 = x")
        s7 = self.stan(r"2x = x-6")
        s8 = self.stan(r"2x-x = -6")
        s8b = self.stan(r"2x-1x = -6")
        s8c = self.stan(r"1x = -6")
        s9 = self.stan(r"x = -6")
        glowne = [s0, s2, s3, s3b, s4, s4b, s5, s5b, s6, s7, s8, s8b, s8c, s9]

        # Rachunek pomocniczy jest mniejszy, bo to praca na boku, a nie linijka
        # rozwiązania. Uczeń ma po wielkości poznać, co jest czym.
        w1 = self.stan(r"x-1 \ne 0", 72)
        w2 = self.stan(r"x \ne 1", 72)
        w3 = self.stan(r"2x-2 \ne 0", 72)
        w4 = self.stan(r"2x \ne 2", 72)
        w5 = self.stan(r"x \ne 1", 72)
        f1 = self.stan(r"2x-2", 72)
        f2 = self.stan(r"2\cdot x-2\cdot 1", 72)
        f3 = self.stan(r"2(x-1)", 72)
        pomocnicze = [w1, w2, w3, w4, w5, f1, f2, f3]

        zalozenie = self.stan(r"x \ne 1", 80)
        zalozenie.set_color(SZARY_ZALOZENIE)

        def dopisek(tekst):
            d = self.stan(tekst, 72)
            d.set_color(SZARY_DOPISEK)
            return d

        d_x1 = dopisek(r"\big/ \cdot (x-1)")
        d_2 = dopisek(r"\big/ \cdot 2")
        d_m6 = dopisek(r"\big/ - 6")
        d_mx = dopisek(r"\big/ - x")
        dopiski = [d_x1, d_2, d_m6, d_mx]

        # ---- wspólna skala --------------------------------------------------
        # Jeden współczynnik dla WSZYSTKICH stanów, liczony z najszerszego układu:
        # inaczej litery zmieniałyby wielkość w trakcie przekształcenia i Transform
        # robiłby z tego zoom. Równanie stoi na środku, a dopisek wystaje w prawo,
        # więc szerokość efektywna kroku z dopiskiem liczy się podwójnie od środka.
        ODSTEP = 0.9
        pary = [(s2, d_x1), (s4, d_2), (s6, d_m6), (s7, d_mx)]
        szerokosci = [m.width for m in glowne]
        szerokosci += [2 * (r.width / 2 + ODSTEP + d.width) for r, d in pary]
        najszerszy = max(szerokosci)
        if najszerszy > config.frame_width * MARGINES:
            wsp = config.frame_width * MARGINES / najszerszy
            for m in glowne + pomocnicze + dopiski + [zalozenie]:
                m.scale(wsp)

        for m in glowne:
            m.move_to(ROWNANIE_Y)
        zalozenie.move_to(ZALOZENIE_Y)

        # Rachunek pomocniczy kroku 2 stoi w dwóch kolumnach, każda pod tym
        # mianownikiem, z którego wyszła. Kolejne linijki wyrównane do LEWEJ, żeby
        # iks nie jeździł w bok tylko dlatego, że linijka się skróciła.
        w1.move_to(LEFT * 3.7 + POMOCNICZY_Y)
        w3.move_to(RIGHT * 3.3 + POMOCNICZY_Y)
        for nowy, wzor in ((w2, w1), (w4, w3), (w5, w3)):
            nowy.move_to(wzor).align_to(wzor, LEFT)
        # Rachunek pomocniczy kroku 3 stoi pod prawym ułamkiem, tam gdzie mianownik.
        f1.move_to(RIGHT * 2.4 + POMOCNICZY_Y)
        for nowy in (f2, f3):
            nowy.move_to(f1).align_to(f1, LEFT)

        def przy(rownanie, d):
            d.next_to(rownanie, RIGHT, buff=ODSTEP)
            return d

        def postoj(cel, rownanie):
            """Miejsce postoju NAD celem: czynnik z dopisku najpierw tam leci."""
            return cel.copy().move_to(
                [cel.get_x(), rownanie.get_top()[1] + POSTOJ, 0])

        # ======================================================================
        # KROK 1. Równanie z treści zadania. Bez koloru: nic się jeszcze nie dzieje.
        # ======================================================================
        self.next_section("krok1")
        self.play(Write(s0), run_time=1.4)
        self.wait(PRZYTRZYMANIE)

        # ======================================================================
        # KROK 2. Dziedzina. Krok pokazuje, SKĄD bierze się x ≠ 1: każdy mianownik
        # zjeżdża w dół, dostaje warunek „≠ 0" i zostaje rozwiązany, a oba wyniki
        # schodzą się w jedno założenie. Liczymy po kolei, nie równolegle (README,
        # punkt 4). Rachunek pomocniczy znika, w kadrze zostaje szare x ≠ 1.
        # ======================================================================
        self.next_section("krok2")

        # -- lewy mianownik: x - 1 ≠ 0
        self.zapal(*s0[0][4:7])
        kopia_l = s0[0][4:7].copy()
        self.add(kopia_l)
        w1[0][0:3].set_color(ZIELONY)
        self.play(
            ReplacementTransform(kopia_l, w1[0][0:3]),
            *[g.animate.set_color(BLACK) for g in s0[0][4:7]],
            FadeIn(w1[0][3:6]),
            run_time=1.1,
        )
        self.gas(*w1[0][0:3])
        # przeniesienie: jedynka przelatuje przez ≠ i zmienia znak, minus i zero znikają
        self.zapal(w1[0][1], w1[0][2], czas=0.35)
        w2[0][3].set_color(ZIELONY)
        self.play(
            ReplacementTransform(w1[0][2], w2[0][3]),
            FadeOut(w1[0][1], scale=0.4),
            FadeOut(w1[0][5], scale=0.4),
            ReplacementTransform(w1[0][0], w2[0][0]),
            ReplacementTransform(w1[0][3:5], w2[0][1:3]),
            run_time=1.1,
        )
        self.gas(w2[0][3])

        # -- prawy mianownik: 2x - 2 ≠ 0
        self.zapal(*s0[0][10:14])
        kopia_p = s0[0][10:14].copy()
        self.add(kopia_p)
        w3[0][0:4].set_color(ZIELONY)
        self.play(
            ReplacementTransform(kopia_p, w3[0][0:4]),
            *[g.animate.set_color(BLACK) for g in s0[0][10:14]],
            FadeIn(w3[0][4:7]),
            run_time=1.1,
        )
        self.gas(*w3[0][0:4])
        # dwójka przelatuje przez ≠ i zmienia znak
        self.zapal(w3[0][2], w3[0][3], czas=0.35)
        w4[0][4].set_color(ZIELONY)
        self.play(
            ReplacementTransform(w3[0][3], w4[0][4]),
            FadeOut(w3[0][2], scale=0.4),
            FadeOut(w3[0][6], scale=0.4),
            ReplacementTransform(w3[0][0:2], w4[0][0:2]),
            ReplacementTransform(w3[0][4:6], w4[0][2:4]),
            run_time=1.1,
        )
        self.gas(w4[0][4])
        # obie strony dzielimy przez dwa: dwójka sprzed iksa znika, dwójka po prawej
        # staje się jedynką
        self.zapal(w4[0][0], w4[0][4], czas=0.35)
        w5[0][3].set_color(ZIELONY)
        self.play(
            FadeOut(w4[0][0], scale=0.4),
            ReplacementTransform(w4[0][4], w5[0][3]),
            ReplacementTransform(w4[0][1], w5[0][0]),
            ReplacementTransform(w4[0][2:4], w5[0][1:3]),
            run_time=1.1,
        )
        self.gas(w5[0][3])

        # -- oba warunki dały to samo, więc schodzą się w jedną linijkę i bledną
        self.play(
            Transform(w2, zalozenie.copy()),
            Transform(w5, zalozenie.copy()),
            run_time=1.2,
        )
        self.remove(w2, w5)
        self.add(zalozenie)
        self.zakoncz(s0, zalozenie, pomin=[zalozenie])

        # ======================================================================
        # KROK 3. Prawy mianownik zapisany jako 2(x-1). Wyłączanie dwójki liczy się
        # na boku, z ogniwem pośrednim 2·x - 2·1 (README, punkt 17), a gotowy nawias
        # wjeżdża na miejsce starego mianownika.
        # ======================================================================
        self.next_section("krok3")
        self.zapal(*s0[0][10:14])
        kopia_m = s0[0][10:14].copy()
        self.add(kopia_m)
        self.play(
            ReplacementTransform(kopia_m, f1[0][0:4]),
            *[g.animate.set_color(BLACK) for g in s0[0][10:14]],
            run_time=1.0,
        )
        # 2x to 2·x, a 2 to 2·1, więc dopisujemy to, czego w zapisie nie widać
        f2[0][6].set_color(ZIELONY)
        self.play(
            ReplacementTransform(f1[0][0], f2[0][0]),
            ReplacementTransform(f1[0][1], f2[0][2]),
            ReplacementTransform(f1[0][2], f2[0][3]),
            ReplacementTransform(f1[0][3], f2[0][4]),
            FadeIn(f2[0][1]),
            FadeIn(f2[0][5]),
            FadeIn(f2[0][6]),
            run_time=1.1,
        )
        self.gas(f2[0][6])
        # obie dwójki to ta sama dwójka: druga dojeżdża do pierwszej i się z nią zlewa
        self.zapal(f2[0][0], f2[0][4], czas=0.35)
        f3[0][0].set_color(ZIELONY)
        self.play(
            ReplacementTransform(f2[0][0], f3[0][0]),
            Transform(f2[0][4], f3[0][0].copy()),
            FadeOut(f2[0][1], scale=0.4),
            FadeOut(f2[0][5], scale=0.4),
            ReplacementTransform(f2[0][2], f3[0][2]),
            ReplacementTransform(f2[0][3], f3[0][3]),
            ReplacementTransform(f2[0][6], f3[0][4]),
            FadeIn(f3[0][1]),
            FadeIn(f3[0][5]),
            run_time=1.3,
        )
        self.remove(f2[0][4])
        # gotowy nawias wjeżdża na miejsce starego mianownika, a reszta równania
        # PRZESUWA się na nowe pozycje, glif po glifie
        self.play(
            ReplacementTransform(f3[0][0:6], s2[0][10:16]),
            *[FadeOut(g, scale=0.6) for g in s0[0][10:14]],
            *[ReplacementTransform(s0[0][i], s2[0][i]) for i in range(0, 10)],
            run_time=1.4,
        )
        self.zakoncz(s2, zalozenie, pomin=[zalozenie])
        przy(s2, d_x1)
        self.play(FadeIn(d_x1, shift=LEFT * 0.3), run_time=0.6)
        self.wait(PRZYTRZYMANIE)

        # ======================================================================
        # KROK 4. Mnożymy obie strony przez (x-1). Nawias z dopisku leci w OBA
        # liczniki naraz: to jest dokładnie ta czynność, którą dopisek zapowiada.
        # ======================================================================
        self.next_section("krok4")
        self.zapal(*d_x1[0][2:7])
        kopia_a = d_x1[0][2:7].copy()
        kopia_b = d_x1[0][2:7].copy()
        self.add(kopia_a, kopia_b)
        cel_a = s3[0][5:10]
        cel_b = s3[0][16:21]
        cel_a.set_color(ZIELONY)
        cel_b.set_color(ZIELONY)
        # Takt 1: nawias odrywa się od dopisku i staje NAD licznikiem, w który wejdzie.
        # Górą, a nie przez środek równania: lot przez środek przechodzi po literach
        # i w połowie animacji nie da się odczytać ani starego zapisu, ani nowego.
        self.play(
            Transform(kopia_a, postoj(cel_a, s3)),
            Transform(kopia_b, postoj(cel_b, s3)),
            FadeOut(d_x1, shift=RIGHT * 0.3),
            run_time=1.0,
        )
        # Takt 2: nawiasy zjeżdżają w liczniki, a równanie robi im miejsce
        przenosiny = {0: 1, 1: 2, 2: 3, 3: 10, 4: 11, 5: 12, 6: 13, 7: 14,
                      8: 15, 9: 21, 10: 22, 11: 23, 12: 24, 13: 25, 14: 26, 15: 27}
        self.play(
            ReplacementTransform(kopia_a, cel_a),
            ReplacementTransform(kopia_b, cel_b),
            *[ReplacementTransform(s2[0][i], s3[0][j]) for i, j in przenosiny.items()],
            FadeIn(s3[0][0]),   # nawiasy wokół x+3 dopisujemy, bo teraz jest tam iloczyn
            FadeIn(s3[0][4]),
            run_time=1.3,
        )
        self.zakoncz(s3, zalozenie, pomin=[zalozenie])

        # ======================================================================
        # KROK 5. Skracamy (x-1), najpierw po lewej, potem po prawej. Nawias odjeżdża
        # z licznika i z mianownika JEDNOCZEŚNIE, do kreski ułamka, a nie znika sam
        # z siebie. Wolno tak zrobić dzięki założeniu: x - 1 nie jest zerem.
        # ======================================================================
        self.next_section("krok5")
        self.zapal(*s3[0][5:10], *s3[0][11:14])
        po_lewej = {1: 0, 2: 1, 3: 2, 14: 3, 15: 4, 16: 5, 17: 6, 18: 7, 19: 8,
                    20: 9, 21: 10, 22: 11, 23: 12, 24: 13, 25: 14, 26: 15, 27: 16}
        self.play(
            *[FadeOut(g, shift=DOWN * 0.35, scale=0.5) for g in s3[0][5:10]],
            *[FadeOut(g, shift=UP * 0.35, scale=0.5) for g in s3[0][11:14]],
            FadeOut(s3[0][10], scale=0.5),   # kreska ułamka, bo ułamka już nie ma
            FadeOut(s3[0][0]),               # nawiasy wokół x+3 przestają być potrzebne
            FadeOut(s3[0][4]),
            *[ReplacementTransform(s3[0][i], s3b[0][j]) for i, j in po_lewej.items()],
            run_time=1.4,
        )
        self.zapal(*s3b[0][5:10], *s3b[0][12:17])
        po_prawej = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 10: 5, 11: 6}
        self.play(
            *[FadeOut(g, shift=DOWN * 0.35, scale=0.5) for g in s3b[0][5:10]],
            *[FadeOut(g, shift=UP * 0.35, scale=0.5) for g in s3b[0][12:17]],
            *[ReplacementTransform(s3b[0][i], s4[0][j]) for i, j in po_prawej.items()],
            run_time=1.4,
        )
        self.zakoncz(s4, zalozenie, pomin=[zalozenie])
        przy(s4, d_2)
        self.play(FadeIn(d_2, shift=LEFT * 0.3), run_time=0.6)
        self.wait(PRZYTRZYMANIE)

        # ======================================================================
        # KROK 6. Mnożymy obie strony przez 2. Dwójka z dopisku leci w obie strony:
        # po lewej staje przed nawiasem, po prawej wchodzi przed ułamek i dopiero
        # potem skraca się z dwójką z mianownika. Bez tego ogniwa wyglądałoby to tak,
        # jakby mianownik zniknął sam z siebie.
        # ======================================================================
        self.next_section("krok6")
        self.zapal(d_2[0][2])
        kopia_l6 = d_2[0][2].copy()
        kopia_p6 = d_2[0][2].copy()
        self.add(kopia_l6, kopia_p6)
        cel_l = s4b[0][0]
        cel_p = s4b[0][7]
        cel_l.set_color(ZIELONY)
        cel_p.set_color(ZIELONY)
        # takt 1: obie dwójki odrywają się od dopisku i stają nad swoimi miejscami
        self.play(
            Transform(kopia_l6, postoj(cel_l, s4b)),
            Transform(kopia_p6, postoj(cel_p, s4b)),
            FadeOut(d_2, shift=RIGHT * 0.3),
            run_time=1.0,
        )
        # takt 2: zjeżdżają na miejsce, po lewej przed nawias, po prawej przed ułamek
        self.play(
            ReplacementTransform(kopia_l6, cel_l),
            ReplacementTransform(kopia_p6, cel_p),
            FadeIn(s4b[0][1]),   # nawias wokół x+3, bo dwójka mnoży całą sumę
            FadeIn(s4b[0][5]),
            FadeIn(s4b[0][8]),   # kropka mnożenia przed ułamkiem
            *[ReplacementTransform(s4[0][i], s4b[0][j])
              for i, j in {0: 2, 1: 3, 2: 4, 3: 6, 4: 9, 5: 10, 6: 11}.items()],
            run_time=1.3,
        )
        self.gas(s4b[0][0], s4b[0][7])
        # skracanie: dwójka sprzed ułamka i dwójka z mianownika odjeżdżają do kreski
        self.zapal(s4b[0][7], s4b[0][11], czas=0.35)
        self.play(
            FadeOut(s4b[0][7], shift=DOWN * 0.3, scale=0.5),
            FadeOut(s4b[0][11], shift=UP * 0.3, scale=0.5),
            FadeOut(s4b[0][8], scale=0.5),    # kropka mnożenia
            FadeOut(s4b[0][10], scale=0.5),   # kreska ułamka
            *[ReplacementTransform(s4b[0][i], s5[0][j])
              for i, j in {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 9: 7}.items()],
            run_time=1.4,
        )
        self.zakoncz(s5, zalozenie, pomin=[zalozenie])

        # ======================================================================
        # KROK 7. Opuszczamy nawias. Dwójka mnoży każdy składnik OSOBNO, więc
        # najpierw się rozdwaja (2·x oraz 2·3), a dopiero potem liczymy 2·3 = 6.
        # ======================================================================
        self.next_section("krok7")
        self.zapal(s5[0][0])
        kopia_2 = s5[0][0].copy()
        self.add(kopia_2)
        s5b[0][0].set_color(ZIELONY)
        s5b[0][4].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s5[0][0], s5b[0][0]),
            ReplacementTransform(kopia_2, s5b[0][4]),
            FadeOut(s5[0][1]),   # nawiasy już niepotrzebne, mnożenie jest rozpisane
            FadeOut(s5[0][5]),
            FadeIn(s5b[0][1]),   # kropki mnożenia
            FadeIn(s5b[0][5]),
            *[ReplacementTransform(s5[0][i], s5b[0][j])
              for i, j in {2: 2, 3: 3, 4: 6, 6: 7, 7: 8}.items()],
            run_time=1.4,
        )
        self.gas(s5b[0][0], s5b[0][4])
        # 2·3 to jedna liczba: dwójka, kropka i trójka zjeżdżają się w szóstkę
        self.zapal(s5b[0][4], s5b[0][6], czas=0.35)
        s6[0][3].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s5b[0][6], s6[0][3]),
            Transform(s5b[0][4], s6[0][3].copy()),
            Transform(s5b[0][5], s6[0][3].copy()),
            FadeOut(s5b[0][1], scale=0.5),   # kropka przy 2·x, bo 2·x zapisujemy 2x
            *[ReplacementTransform(s5b[0][i], s6[0][j])
              for i, j in {0: 0, 2: 1, 3: 2, 7: 4, 8: 5}.items()],
            run_time=1.4,
        )
        self.remove(s5b[0][4], s5b[0][5])
        self.zakoncz(s6, zalozenie, pomin=[zalozenie])
        przy(s6, d_m6)
        self.play(FadeIn(d_m6, shift=LEFT * 0.3), run_time=0.6)
        self.wait(PRZYTRZYMANIE)

        # ======================================================================
        # KROK 8. Szóstka przechodzi na prawo. Plus nie znika i nie pojawia się obok:
        # to ten sam znak leci razem z szóstką i po drodze ZAMIENIA się w minus
        # (README, punkt 15). Tu najczęściej ucieka znak.
        # ======================================================================
        self.next_section("krok8")
        self.zapal(s6[0][2], s6[0][3])
        s7[0][4].set_color(ZIELONY)
        s7[0][5].set_color(ZIELONY)
        # Łuk, a nie linia prosta: po prostej szóstka przechodzi PO znaku równości
        # i przez pół sekundy nie widać ani jej, ani jego. Nad znakiem widać oba.
        self.play(
            ReplacementTransform(s6[0][2], s7[0][4], path_arc=-2 * PI / 3),
            ReplacementTransform(s6[0][3], s7[0][5], path_arc=-2 * PI / 3),
            *[ReplacementTransform(s6[0][i], s7[0][j])
              for i, j in {0: 0, 1: 1, 4: 2, 5: 3}.items()],
            FadeOut(d_m6, shift=RIGHT * 0.3),
            run_time=1.4,
        )
        self.zakoncz(s7, zalozenie, pomin=[zalozenie])
        przy(s7, d_mx)
        self.play(FadeIn(d_mx, shift=LEFT * 0.3), run_time=0.6)
        self.wait(PRZYTRZYMANIE)

        # ======================================================================
        # KROK 9. To samo z iksem. Przed iksem po prawej nie stoi żaden znak, więc
        # minus, który przy przejściu powstaje, musi się POJAWIĆ (README, punkt 21).
        # ======================================================================
        self.next_section("krok9")
        self.zapal(s7[0][3])
        s8[0][2].set_color(ZIELONY)
        s8[0][3].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s7[0][3], s8[0][3], path_arc=2 * PI / 3),
            FadeIn(s8[0][2], shift=RIGHT * 0.3),
            *[ReplacementTransform(s7[0][i], s8[0][j])
              for i, j in {0: 0, 1: 1, 2: 4, 4: 5, 5: 6}.items()],
            FadeOut(d_mx, shift=RIGHT * 0.3),
            run_time=1.4,
        )
        self.zakoncz(s8, zalozenie, pomin=[zalozenie])

        # ======================================================================
        # KROK 10. Dwa iksy bez jednego iksa. Żeby to było odejmowanie, a nie magia,
        # przy drugim iksie pojawia się jedynka (x to 1x), potem 2 - 1 = 1, a na końcu
        # jedynka sprzed iksa znika, bo 1x zapisujemy po prostu x.
        # ======================================================================
        self.next_section("krok10")
        s8b[0][3].set_color(ZIELONY)
        self.play(
            FadeIn(s8b[0][3], shift=UP * 0.25),
            *[ReplacementTransform(s8[0][i], s8b[0][j])
              for i, j in {0: 0, 1: 1, 2: 2, 3: 4, 4: 5, 5: 6, 6: 7}.items()],
            run_time=1.0,
        )
        self.gas(s8b[0][3])
        # 2 - 1 = 1: minus i jedynka dojeżdżają do dwójki, a dwójka staje się jedynką.
        # Iks zostaje ten sam, więc jest czarny i stoi w miejscu; drugi iks wtapia
        # się w niego, bo to ten sam iks, tylko policzony.
        self.zapal(s8b[0][0], s8b[0][2], s8b[0][3], czas=0.35)
        s8c[0][0].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s8b[0][0], s8c[0][0]),
            Transform(s8b[0][2], s8c[0][0].copy()),
            Transform(s8b[0][3], s8c[0][0].copy()),
            Transform(s8b[0][4], s8c[0][1].copy()),
            *[ReplacementTransform(s8b[0][i], s8c[0][j])
              for i, j in {1: 1, 5: 2, 6: 3, 7: 4}.items()],
            run_time=1.3,
        )
        self.remove(s8b[0][2], s8b[0][3], s8b[0][4])
        # jeden iks to po prostu iks
        self.play(
            FadeOut(s8c[0][0], scale=0.4),
            *[ReplacementTransform(s8c[0][i], s9[0][j])
              for i, j in {1: 0, 2: 1, 3: 2, 4: 3}.items()],
            run_time=1.0,
        )
        self.zakoncz(s9, zalozenie, pomin=[zalozenie])
