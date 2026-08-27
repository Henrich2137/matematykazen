from manim import *

from _wspolne import MARGINES, PRZYTRZYMANIE


# Zadanie 8 (otwarte, 3 pkt). Rozwiąż (x+3)/(x-1) = x/(2x-2). Wynik: x = -6.
#
# Scenariusz ruchu: manimations/zad8-kroki.md. Dziewiętnaście kroków, jeden do
# jednego z dziewiętnastoma linijkami rachunku w rozwiązaniu opisowym.
#
# ---------------------------------------------------------------------------
# Napisane od nowa 2026-08-28, na wzór zadania 7 (polecenie Henricha). Co się
# zmieniło wobec wersji z 2026-08-27:
#
#   1. DZIEDZINA IDZIE DWOMA TORAMI, jak a i b w zadaniu 7. Lewy mianownik dostaje
#      swój tor, prawy swój, oba kończą się tym samym warunkiem i dopiero wtedy
#      schodzą się w jedno założenie. Wcześniej cała dziedzina była JEDNYM krokiem
#      z rachunkiem pomocniczym w środku; teraz to sześć osobnych kroków, bo każdy
#      z nich jest osobną linijką rozwiązania opisowego.
#   2. NIE MA PASA RACHUNKU POMOCNICZEGO. Ogniwo, którego uczeń nie widzi
#      (2x-2 = 2·x-2·1, 2(x+3) = 2·x+2·3, x = 1x), jest teraz PEŁNĄ linijką
#      rachunku i pełnym krokiem filmu, a nie pracą na boku mniejszym pismem.
#      Dzięki temu rozwiązanie opisowe może być samymi wzorami, bez zdań między
#      linijkami, dokładnie jak w zadaniu 7.
#   3. Zostaje to, co się sprawdziło: warunek x ≠ 1 stoi szary NAD rachunkiem od
#      kroku 7 do końca, dopiski działań są jeszcze bledsze, żaden ruch nie idzie
#      po literach, a każda para glifów jest wskazana ręcznie.
# ---------------------------------------------------------------------------
#
# MAPA GLIFÓW, policzona z pozycji glifów, nie zgadnięta (README, punkt 20).
# MathTex numeruje glify w kolejności czytania, a w ułamku idzie najpierw licznik,
# potem kreska, potem mianownik. `\ne` to DWA glify (kreski, ukośnik), `=` jeden.
#
#   S1   \frac{x+3}{x-1} = \frac{x}{2x-2}                14
#        0 x  1 +  2 3  3 kreska  4 x  5 -  6 1  7 =  8 x  9 kreska  10 2  11 x  12 -  13 2
#   S8   \frac{x+3}{x-1} = \frac{x}{2\cdot x-2\cdot 1}   17
#        0..9 jak wyżej  10 2  11 ·  12 x  13 -  14 2  15 ·  16 1
#   S9   \frac{x+3}{x-1} = \frac{x}{2(x-1)}              16
#        0..9 jak wyżej  10 2  11 (  12 x  13 -  14 1  15 )
#   S10  \frac{(x+3)(x-1)}{x-1} = \frac{x(x-1)}{2(x-1)}  28
#        0 (  1 x  2 +  3 3  4 )  5 (  6 x  7 -  8 1  9 )  10 kreska  11 x  12 -  13 1
#        14 =  15 x  16 (  17 x  18 -  19 1  20 )  21 kreska  22 2  23 (  24 x  25 -  26 1  27 )
#   S10b x+3 = \frac{x(x-1)}{2(x-1)}                     17  (stan pośredni kroku 11)
#        0 x  1 +  2 3  3 =  4 x  5 (  6 x  7 -  8 1  9 )  10 kreska  11 2  12 (  13 x  14 -  15 1  16 )
#   S11  x+3 = \frac{x}{2}                                7  0 x 1 + 2 3 3 = 4 x 5 kreska 6 2
#   S12  2(x+3) = 2\cdot\frac{x}{2}                      12  0 2 1 ( 2 x 3 + 4 3 5 ) 6 = 7 2 8 · 9 x 10 kreska 11 2
#   S13  2(x+3) = x                                       8  0 2 1 ( 2 x 3 + 4 3 5 ) 6 = 7 x
#   S14  2\cdot x+2\cdot 3 = x                            9  0 2 1 · 2 x 3 + 4 2 5 · 6 3 7 = 8 x
#   S15  2x+6 = x                                         6  0 2 1 x 2 + 3 6 4 = 5 x
#   S16  2x = x-6                                         6  0 2 1 x 2 = 3 x 4 - 5 6
#   S17  2x-x = -6                                        7  0 2 1 x 2 - 3 x 4 = 5 - 6 6
#   S18  2x-1x = -6                                       8  0 2 1 x 2 - 3 1 4 x 5 = 6 - 7 6
#   S18c 1x = -6                                          5  0 1 1 x 2 = 3 - 4 6  (stan pośredni kroku 19)
#   S19  x = -6                                           4  0 x 1 = 2 - 3 6
#
#   tory dziedziny:
#   D2  x-1 \ne 0     6  0 x  1 -  2 1  3 ≠kreski  4 ≠ukośnik  5 0
#   D3  x \ne 1       4  0 x  1 ≠kreski  2 ≠ukośnik  3 1
#   D4  2x-2 \ne 0    7  0 2  1 x  2 -  3 2  4 ≠kreski  5 ≠ukośnik  6 0
#   D5  2x \ne 2      5  0 2  1 x  2 ≠kreski  3 ≠ukośnik  4 2
#   D6  x \ne 1       4  jak D3
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

ROWNANIE_Y = UP * 0.5           # rachunek główny, nie rusza się przez cały film
TORY_Y = DOWN * 2.0             # dwa tory dziedziny, tylko w krokach 2 do 7
ZALOZENIE_Y = UP * 2.9          # gotowe założenie, nad rachunkiem, do końca filmu
# Ile nad równaniem zatrzymuje się czynnik, który wyleciał z dopisku działania.
POSTOJ = 0.45


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
        s1 = self.stan(r"\frac{x+3}{x-1} = \frac{x}{2x-2}")
        s8 = self.stan(r"\frac{x+3}{x-1} = \frac{x}{2\cdot x-2\cdot 1}")
        s9 = self.stan(r"\frac{x+3}{x-1} = \frac{x}{2(x-1)}")
        s10 = self.stan(r"\frac{(x+3)(x-1)}{x-1} = \frac{x(x-1)}{2(x-1)}")
        s10b = self.stan(r"x+3 = \frac{x(x-1)}{2(x-1)}")
        s11 = self.stan(r"x+3 = \frac{x}{2}")
        s12 = self.stan(r"2(x+3) = 2\cdot\frac{x}{2}")
        s13 = self.stan(r"2(x+3) = x")
        s14 = self.stan(r"2\cdot x+2\cdot 3 = x")
        s15 = self.stan(r"2x+6 = x")
        s16 = self.stan(r"2x = x-6")
        s17 = self.stan(r"2x-x = -6")
        s18 = self.stan(r"2x-1x = -6")
        s18c = self.stan(r"1x = -6")
        s19 = self.stan(r"x = -6")
        glowne = [s1, s8, s9, s10, s10b, s11, s12, s13, s14,
                  s15, s16, s17, s18, s18c, s19]

        # Tory dziedziny są tej samej wielkości co rachunek: to też są linijki
        # rozwiązania, a nie praca na boku.
        d2 = self.stan(r"x-1 \ne 0")
        d3 = self.stan(r"x \ne 1")
        d4 = self.stan(r"2x-2 \ne 0")
        d5 = self.stan(r"2x \ne 2")
        d6 = self.stan(r"x \ne 1")
        tory = [d2, d3, d4, d5, d6]

        zalozenie = self.stan(r"x \ne 1")
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
        pary = [(s9, d_x1), (s11, d_2), (s15, d_m6), (s16, d_mx)]
        szerokosci = [m.width for m in glowne]
        szerokosci += [2 * (r.width / 2 + ODSTEP + d.width) for r, d in pary]
        # Oba tory dziedziny stoją obok siebie, więc muszą się zmieścić razem.
        PRZERWA_TOROW = 1.2
        szerokosci.append(d4.width + PRZERWA_TOROW + d4.width)
        najszerszy = max(szerokosci)
        POLE = config.frame_width * MARGINES
        if najszerszy > POLE:
            wsp = POLE / najszerszy
            for m in glowne + tory + dopiski + [zalozenie]:
                m.scale(wsp)

        for m in glowne:
            m.move_to(ROWNANIE_Y)

        # Dwa tory dziedziny: lewy pod lewym mianownikiem, prawy pod prawym, każdy
        # wyrównany do LEWEJ krawędzi swojej kolumny, żeby iks nie jeździł w bok
        # tylko dlatego, że linijka się skróciła.
        LEWY_X = -POLE / 2
        PRAWY_X = 0.6
        def przy_lewej(mobiekt, x):
            """Lewa krawędź zapisu ląduje dokładnie na x."""
            mobiekt.shift(RIGHT * (x - mobiekt.get_left()[0]))
            return mobiekt

        przy_lewej(d2.move_to(TORY_Y), LEWY_X)
        przy_lewej(d4.move_to(TORY_Y), PRAWY_X)
        for nowy, wzor in ((d3, d2), (d5, d4), (d6, d4)):
            nowy.move_to(wzor).align_to(wzor, LEFT)
        # Gotowe założenie stoi NAD rachunkiem i przy lewej krawędzi, tak jak
        # zapisuje się je na kartce: najpierw warunek, pod nim liczenie.
        przy_lewej(zalozenie.move_to(ZALOZENIE_Y), LEWY_X)

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
        self.play(Write(s1), run_time=1.4)
        self.wait(PRZYTRZYMANIE)

        # ======================================================================
        # KROK 2. Pierwszy tor: lewy mianownik nie może być zerem. Kopia mianownika
        # zjeżdża w lewą kolumnę i dostaje warunek „≠ 0".
        # ======================================================================
        self.next_section("krok2")
        self.zapal(*s1[0][4:7])
        kopia_l = s1[0][4:7].copy()
        self.add(kopia_l)
        d2[0][0:3].set_color(ZIELONY)
        self.play(
            ReplacementTransform(kopia_l, d2[0][0:3]),
            *[g.animate.set_color(BLACK) for g in s1[0][4:7]],
            FadeIn(d2[0][3:6]),
            run_time=1.2,
        )
        self.zakoncz(s1, d2)

        # ======================================================================
        # KROK 3. Jedynka przechodzi na drugą stronę i zmienia znak. Leci ŁUKIEM nad
        # znakiem ≠: po prostej przez ułamek sekundy leżałaby dokładnie na nim.
        # ======================================================================
        self.next_section("krok3")
        self.zapal(d2[0][1], d2[0][2])
        d3[0][3].set_color(ZIELONY)
        self.play(
            ReplacementTransform(d2[0][2], d3[0][3], path_arc=-2 * PI / 3),
            FadeOut(d2[0][1], scale=0.4),
            FadeOut(d2[0][5], scale=0.4),
            ReplacementTransform(d2[0][0], d3[0][0]),
            ReplacementTransform(d2[0][3:5], d3[0][1:3]),
            run_time=1.3,
        )
        self.zakoncz(s1, d3)

        # ======================================================================
        # KROK 4. Drugi tor: to samo pytanie o prawy mianownik. Pierwszy tor zostaje
        # w kadrze, bo na końcu oba wyniki mają się spotkać (tak jak a i b w zad. 7).
        # ======================================================================
        self.next_section("krok4")
        self.zapal(*s1[0][10:14])
        kopia_p = s1[0][10:14].copy()
        self.add(kopia_p)
        d4[0][0:4].set_color(ZIELONY)
        self.play(
            ReplacementTransform(kopia_p, d4[0][0:4]),
            *[g.animate.set_color(BLACK) for g in s1[0][10:14]],
            FadeIn(d4[0][4:7]),
            run_time=1.2,
        )
        self.zakoncz(s1, d3, d4)

        # ======================================================================
        # KROK 5. Dwójka przechodzi na drugą stronę i zmienia znak.
        # ======================================================================
        self.next_section("krok5")
        self.zapal(d4[0][2], d4[0][3])
        d5[0][4].set_color(ZIELONY)
        self.play(
            ReplacementTransform(d4[0][3], d5[0][4], path_arc=-2 * PI / 3),
            FadeOut(d4[0][2], scale=0.4),
            FadeOut(d4[0][6], scale=0.4),
            ReplacementTransform(d4[0][0:2], d5[0][0:2]),
            ReplacementTransform(d4[0][4:6], d5[0][2:4]),
            run_time=1.3,
        )
        self.zakoncz(s1, d3, d5)

        # ======================================================================
        # KROK 6. Obie strony dzielimy przez dwa: dwójka sprzed iksa znika, a dwójka
        # po prawej staje się jedynką.
        # ======================================================================
        self.next_section("krok6")
        self.zapal(d5[0][0], d5[0][4])
        d6[0][3].set_color(ZIELONY)
        self.play(
            FadeOut(d5[0][0], scale=0.4),
            ReplacementTransform(d5[0][4], d6[0][3]),
            ReplacementTransform(d5[0][1], d6[0][0]),
            ReplacementTransform(d5[0][2:4], d6[0][1:3]),
            run_time=1.3,
        )
        self.zakoncz(s1, d3, d6)

        # ======================================================================
        # KROK 7. Oba tory dały ten sam warunek, więc prawy dojeżdża do lewego i już
        # jedno założenie jedzie NAD rachunek, gdzie zostaje do końca filmu. Krok nie
        # ma koloru: nic się w nim nie przelicza, zapis tylko zmienia miejsce.
        # Lot idzie pionowo, wzdłuż lewej krawędzi kadru, a nie po skosie przez
        # środek: po skosie przelatywałby po literach równania.
        # ======================================================================
        self.next_section("krok7")
        self.play(Transform(d6, d3.copy()), run_time=1.1)
        self.remove(d6)
        self.wait(0.2)
        self.play(Transform(d3, zalozenie.copy()), run_time=1.2)
        self.remove(d3)
        self.add(zalozenie)
        self.zakoncz(s1, zalozenie, pomin=[zalozenie])

        # ======================================================================
        # KROK 8. Prawy mianownik rozpisany na iloczyny: 2x to 2·x, a 2 to 2·1.
        # To jest ogniwo, które ekspert liczy w głowie, więc wypisujemy je jawnie
        # (README, punkt 17) i dopiero w następnym kroku zwijamy do nawiasu.
        # ======================================================================
        self.next_section("krok8")
        s8[0][16].set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(s1[0][i], s8[0][i]) for i in range(0, 11)],
            ReplacementTransform(s1[0][11], s8[0][12]),
            ReplacementTransform(s1[0][12], s8[0][13]),
            ReplacementTransform(s1[0][13], s8[0][14]),
            FadeIn(s8[0][11]),   # kropki mnożenia, których w zapisie nie widać
            FadeIn(s8[0][15]),
            FadeIn(s8[0][16]),   # jedynka: 2 to 2·1
            run_time=1.4,
        )
        self.zakoncz(s8, zalozenie, pomin=[zalozenie])

        # ======================================================================
        # KROK 9. Obie dwójki to ta sama dwójka, więc druga dojeżdża do pierwszej
        # i zlewa się z nią, a dokoła reszty wjeżdża nawias. Teraz w obu mianownikach
        # stoi ten sam czynnik x - 1, i o to w tej metodzie chodziło.
        # ======================================================================
        self.next_section("krok9")
        self.zapal(s8[0][10], s8[0][14])
        s9[0][10].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s8[0][10], s9[0][10]),
            Transform(s8[0][14], s9[0][10].copy()),
            FadeOut(s8[0][11], scale=0.4),   # kropki znikają, bo wracamy do zapisu skróconego
            FadeOut(s8[0][15], scale=0.4),
            ReplacementTransform(s8[0][12], s9[0][12]),
            ReplacementTransform(s8[0][13], s9[0][13]),
            ReplacementTransform(s8[0][16], s9[0][14]),
            FadeIn(s9[0][11]),   # nawias, bo dwójka mnoży teraz całą różnicę
            FadeIn(s9[0][15]),
            *[ReplacementTransform(s8[0][i], s9[0][i]) for i in range(0, 10)],
            run_time=1.5,
        )
        self.remove(s8[0][14])
        self.zakoncz(s9, zalozenie, pomin=[zalozenie])
        przy(s9, d_x1)
        self.play(FadeIn(d_x1, shift=LEFT * 0.3), run_time=0.6)
        self.wait(PRZYTRZYMANIE)

        # ======================================================================
        # KROK 10. Mnożymy obie strony przez (x-1). Nawias z dopisku leci w OBA
        # liczniki naraz: to jest dokładnie ta czynność, którą dopisek zapowiada.
        # ======================================================================
        self.next_section("krok10")
        self.zapal(*d_x1[0][3:6])
        kopia_a = d_x1[0][2:7].copy()
        kopia_b = d_x1[0][2:7].copy()
        self.add(kopia_a, kopia_b)
        cel_a = s10[0][5:10]
        cel_b = s10[0][16:21]
        # Kolor noszą liczby i litery, nie nawiasy (README, punkt 13), więc zielone
        # jest samo x-1 w środku, a nawias dokoła zostaje czarny.
        cel_a[1:4].set_color(ZIELONY)
        cel_b[1:4].set_color(ZIELONY)
        # Takt 1: nawias odrywa się od dopisku i staje NAD licznikiem, w który wejdzie.
        # Górą, a nie przez środek równania: lot przez środek przechodzi po literach
        # i w połowie animacji nie da się odczytać ani starego zapisu, ani nowego.
        self.play(
            Transform(kopia_a, postoj(cel_a, s10)),
            Transform(kopia_b, postoj(cel_b, s10)),
            FadeOut(d_x1, shift=RIGHT * 0.3),
            run_time=1.0,
        )
        # Takt 2: nawiasy zjeżdżają w liczniki, a równanie robi im miejsce
        przenosiny = {0: 1, 1: 2, 2: 3, 3: 10, 4: 11, 5: 12, 6: 13, 7: 14,
                      8: 15, 9: 21, 10: 22, 11: 23, 12: 24, 13: 25, 14: 26, 15: 27}
        self.play(
            ReplacementTransform(kopia_a, cel_a),
            ReplacementTransform(kopia_b, cel_b),
            *[ReplacementTransform(s9[0][i], s10[0][j]) for i, j in przenosiny.items()],
            FadeIn(s10[0][0]),   # nawiasy wokół x+3 dopisujemy, bo teraz jest tam iloczyn
            FadeIn(s10[0][4]),
            run_time=1.4,
        )
        self.zakoncz(s10, zalozenie, pomin=[zalozenie])

        # ======================================================================
        # KROK 11. Skracamy (x-1), najpierw po lewej, potem po prawej. Nawias odjeżdża
        # z licznika i z mianownika JEDNOCZEŚNIE, do kreski ułamka, a nie znika sam
        # z siebie. Wolno tak zrobić dzięki założeniu: x - 1 nie jest zerem.
        # ======================================================================
        self.next_section("krok11")
        self.zapal(*s10[0][6:9], *s10[0][11:14])
        po_lewej = {1: 0, 2: 1, 3: 2, 14: 3, 15: 4, 16: 5, 17: 6, 18: 7, 19: 8,
                    20: 9, 21: 10, 22: 11, 23: 12, 24: 13, 25: 14, 26: 15, 27: 16}
        self.play(
            *[FadeOut(g, shift=DOWN * 0.35, scale=0.5) for g in s10[0][5:10]],
            *[FadeOut(g, shift=UP * 0.35, scale=0.5) for g in s10[0][11:14]],
            FadeOut(s10[0][10], scale=0.5),   # kreska ułamka, bo ułamka już nie ma
            FadeOut(s10[0][0]),               # nawiasy wokół x+3 przestają być potrzebne
            FadeOut(s10[0][4]),
            *[ReplacementTransform(s10[0][i], s10b[0][j]) for i, j in po_lewej.items()],
            run_time=1.4,
        )
        self.zapal(*s10b[0][6:9], *s10b[0][13:16])
        po_prawej = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 10: 5, 11: 6}
        self.play(
            *[FadeOut(g, shift=DOWN * 0.35, scale=0.5) for g in s10b[0][5:10]],
            *[FadeOut(g, shift=UP * 0.35, scale=0.5) for g in s10b[0][12:17]],
            *[ReplacementTransform(s10b[0][i], s11[0][j]) for i, j in po_prawej.items()],
            run_time=1.4,
        )
        self.zakoncz(s11, zalozenie, pomin=[zalozenie])
        przy(s11, d_2)
        self.play(FadeIn(d_2, shift=LEFT * 0.3), run_time=0.6)
        self.wait(PRZYTRZYMANIE)

        # ======================================================================
        # KROK 12. Mnożymy obie strony przez 2. Dwójka z dopisku rozdwaja się i leci
        # w obie strony naraz: po lewej staje przed nawiasem, bo mnoży całą sumę,
        # po prawej wchodzi przed ułamek.
        # ======================================================================
        self.next_section("krok12")
        self.zapal(d_2[0][2])
        kopia_l6 = d_2[0][2].copy()
        kopia_p6 = d_2[0][2].copy()
        self.add(kopia_l6, kopia_p6)
        cel_l = s12[0][0]
        cel_p = s12[0][7]
        cel_l.set_color(ZIELONY)
        cel_p.set_color(ZIELONY)
        self.play(
            Transform(kopia_l6, postoj(cel_l, s12)),
            Transform(kopia_p6, postoj(cel_p, s12)),
            FadeOut(d_2, shift=RIGHT * 0.3),
            run_time=1.0,
        )
        self.play(
            ReplacementTransform(kopia_l6, cel_l),
            ReplacementTransform(kopia_p6, cel_p),
            FadeIn(s12[0][1]),   # nawias wokół x+3, bo dwójka mnoży całą sumę
            FadeIn(s12[0][5]),
            FadeIn(s12[0][8]),   # kropka mnożenia przed ułamkiem
            *[ReplacementTransform(s11[0][i], s12[0][j])
              for i, j in {0: 2, 1: 3, 2: 4, 3: 6, 4: 9, 5: 10, 6: 11}.items()],
            run_time=1.4,
        )
        self.zakoncz(s12, zalozenie, pomin=[zalozenie])

        # ======================================================================
        # KROK 13. Dwójka sprzed ułamka i dwójka z mianownika skracają się.
        # ======================================================================
        self.next_section("krok13")
        self.zapal(s12[0][7], s12[0][11])
        self.play(
            FadeOut(s12[0][7], shift=DOWN * 0.3, scale=0.5),
            FadeOut(s12[0][11], shift=UP * 0.3, scale=0.5),
            FadeOut(s12[0][8], scale=0.5),    # kropka mnożenia
            FadeOut(s12[0][10], scale=0.5),   # kreska ułamka
            *[ReplacementTransform(s12[0][i], s13[0][j])
              for i, j in {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 9: 7}.items()],
            run_time=1.4,
        )
        self.zakoncz(s13, zalozenie, pomin=[zalozenie])

        # ======================================================================
        # KROK 14. Opuszczamy nawias: dwójka mnoży każdy składnik OSOBNO, więc się
        # rozdwaja. To znowu ogniwo wypisane jawnie, a nie policzone w głowie.
        # ======================================================================
        self.next_section("krok14")
        self.zapal(s13[0][0])
        kopia_2 = s13[0][0].copy()
        self.add(kopia_2)
        s14[0][0].set_color(ZIELONY)
        s14[0][4].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s13[0][0], s14[0][0]),
            ReplacementTransform(kopia_2, s14[0][4]),
            FadeOut(s13[0][1]),   # nawiasy już niepotrzebne, mnożenie jest rozpisane
            FadeOut(s13[0][5]),
            FadeIn(s14[0][1]),    # kropki mnożenia
            FadeIn(s14[0][5]),
            *[ReplacementTransform(s13[0][i], s14[0][j])
              for i, j in {2: 2, 3: 3, 4: 6, 6: 7, 7: 8}.items()],
            run_time=1.5,
        )
        self.zakoncz(s14, zalozenie, pomin=[zalozenie])

        # ======================================================================
        # KROK 15. Wykonujemy oba mnożenia: 2·x zapisujemy 2x, a 2·3 zjeżdża się
        # w szóstkę.
        # ======================================================================
        self.next_section("krok15")
        self.zapal(s14[0][4], s14[0][6])
        s15[0][3].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s14[0][6], s15[0][3]),
            Transform(s14[0][4], s15[0][3].copy()),
            Transform(s14[0][5], s15[0][3].copy()),
            FadeOut(s14[0][1], scale=0.5),   # kropka przy 2·x, bo 2·x zapisujemy 2x
            *[ReplacementTransform(s14[0][i], s15[0][j])
              for i, j in {0: 0, 2: 1, 3: 2, 7: 4, 8: 5}.items()],
            run_time=1.4,
        )
        self.remove(s14[0][4], s14[0][5])
        self.zakoncz(s15, zalozenie, pomin=[zalozenie])
        przy(s15, d_m6)
        self.play(FadeIn(d_m6, shift=LEFT * 0.3), run_time=0.6)
        self.wait(PRZYTRZYMANIE)

        # ======================================================================
        # KROK 16. Szóstka przechodzi na prawo. Plus nie znika i nie pojawia się obok:
        # to ten sam znak leci razem z szóstką i po drodze ZAMIENIA się w minus
        # (README, punkt 15). Tu najczęściej ucieka znak.
        # ======================================================================
        self.next_section("krok16")
        self.zapal(s15[0][2], s15[0][3])
        s16[0][4].set_color(ZIELONY)
        s16[0][5].set_color(ZIELONY)
        # Łuk, a nie linia prosta: po prostej szóstka przechodzi PO znaku równości
        # i przez pół sekundy nie widać ani jej, ani jego. Nad znakiem widać oba.
        self.play(
            ReplacementTransform(s15[0][2], s16[0][4], path_arc=-2 * PI / 3),
            ReplacementTransform(s15[0][3], s16[0][5], path_arc=-2 * PI / 3),
            *[ReplacementTransform(s15[0][i], s16[0][j])
              for i, j in {0: 0, 1: 1, 4: 2, 5: 3}.items()],
            FadeOut(d_m6, shift=RIGHT * 0.3),
            run_time=1.4,
        )
        self.zakoncz(s16, zalozenie, pomin=[zalozenie])
        przy(s16, d_mx)
        self.play(FadeIn(d_mx, shift=LEFT * 0.3), run_time=0.6)
        self.wait(PRZYTRZYMANIE)

        # ======================================================================
        # KROK 17. To samo z iksem. Przed iksem po prawej nie stoi żaden znak, więc
        # minus, który przy przejściu powstaje, musi się POJAWIĆ (README, punkt 21).
        # ======================================================================
        self.next_section("krok17")
        self.zapal(s16[0][3])
        s17[0][2].set_color(ZIELONY)
        s17[0][3].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s16[0][3], s17[0][3], path_arc=2 * PI / 3),
            FadeIn(s17[0][2], shift=RIGHT * 0.3),
            *[ReplacementTransform(s16[0][i], s17[0][j])
              for i, j in {0: 0, 1: 1, 2: 4, 4: 5, 5: 6}.items()],
            FadeOut(d_mx, shift=RIGHT * 0.3),
            run_time=1.4,
        )
        self.zakoncz(s17, zalozenie, pomin=[zalozenie])

        # ======================================================================
        # KROK 18. Przy drugim iksie pojawia się jedynka: x znaczy tyle samo co 1x.
        # Bez tej jedynki następny krok wygląda jak magia, bo nie widać, co od czego
        # odejmujemy.
        # ======================================================================
        self.next_section("krok18")
        s18[0][3].set_color(ZIELONY)
        self.play(
            FadeIn(s18[0][3], shift=UP * 0.25),
            *[ReplacementTransform(s17[0][i], s18[0][j])
              for i, j in {0: 0, 1: 1, 2: 2, 3: 4, 4: 5, 5: 6, 6: 7}.items()],
            run_time=1.1,
        )
        self.zakoncz(s18, zalozenie, pomin=[zalozenie])

        # ======================================================================
        # KROK 19. Dwa iksy bez jednego iksa to jeden iks: minus i jedynka dojeżdżają
        # do dwójki, dwójka staje się jedynką, a na końcu ta jedynka znika, bo 1x
        # zapisujemy po prostu x. Iks stoi w miejscu i jest czarny, bo to dalej ten
        # sam iks, tylko policzony.
        # ======================================================================
        self.next_section("krok19")
        self.zapal(s18[0][0], s18[0][2], s18[0][3])
        s18c[0][0].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s18[0][0], s18c[0][0]),
            Transform(s18[0][2], s18c[0][0].copy()),
            Transform(s18[0][3], s18c[0][0].copy()),
            Transform(s18[0][4], s18c[0][1].copy()),
            *[ReplacementTransform(s18[0][i], s18c[0][j])
              for i, j in {1: 1, 5: 2, 6: 3, 7: 4}.items()],
            run_time=1.4,
        )
        self.remove(s18[0][2], s18[0][3], s18[0][4])
        self.play(
            FadeOut(s18c[0][0], scale=0.4),
            *[ReplacementTransform(s18c[0][i], s19[0][j])
              for i, j in {1: 0, 2: 1, 3: 2, 4: 3}.items()],
            run_time=1.0,
        )
        self.zakoncz(s19, zalozenie, pomin=[zalozenie])
