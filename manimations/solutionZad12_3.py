from manim import *

# Zadanie 12.3 (prawda/falsz, 1 pkt). g(x) = f(x) - 1, gdzie f to parabola
# z 12.1 i 12.2. Wynik: brak miejsc zerowych (F), os symetrii x = 3 (P).
#
# Projekt: issues/projekt-zad11-zad12-2024-grudzien.md. Piec krokow, jeden do
# jednego z pieciona linijkami w solutionText.
#
# Zadanie stoi na jednej rzeczy: odjecie liczby od wzoru funkcji zsuwa CALY
# wykres w dol. Reszta to odczyt z tak przesunietego wykresu, wiec kadr pokazuje
# te sama parabole co 12.1 i zsuwa ja o jedna kratke.
#
# Uklad kadru: wykres po lewej (fiolet #7a3fa8, COLORS.md), po prawej wzor f
# przywolany z 12.2, pod nim budowany wzor g, na dole werdykty obu zdan.
# Litery P i F sa czarne: to odpowiedz ucznia, nie ocena poprawnosci.
#
# Uwaga techniczna, wyciagnieta z 12.1: galaz ani krzywa NIE zmienia grubosci
# przy podswietleniu, tylko kolor. Zmiana grubosci przerysowuje krzywa i koder
# H.264 inaczej ustala jej brzeg, przez co styk klatek spada ponizej progu.
#
# Render: manim --save_sections solutionZad12_3.py Zad12_3

ZIELONY = "#2e7d32"
FIOLET = "#7a3fa8"
SZARY_OSIE = "#666666"
SZARY_SIATKA = "#e0e0e0"

JEDNOSTKA = 0.65
SRODEK_WYKRESU = LEFT * 4.0 + DOWN * 0.1
KOLUMNA_X = 2.95
DANE_Y = 2.95
RACHUNEK_Y = 1.35
WERDYKT_Y = -1.85
WERDYKT_KROK = 0.9


class Zad12_3(Scene):

    def stan(self, *args, rozmiar=64):
        m = MathTex(*args)
        m.set_color(BLACK)
        m.font_size = rozmiar
        return m

    def zgas(self, *mobiekty, czas=0.4):
        if mobiekty:
            self.play(*[m.animate.set_color(BLACK) for m in mobiekty], run_time=czas)

    def construct(self):
        # ================================================================
        # SCENOGRAFIA
        # ================================================================
        plansza = NumberPlane(
            x_range=[-1, 7, 1],
            y_range=[-10.4, 1.4, 1],
            x_length=8 * JEDNOSTKA,
            y_length=11.8 * JEDNOSTKA,
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
                "tip_width": 0.15,
                "tip_height": 0.15,
            },
        )
        plansza.move_to(SRODEK_WYKRESU)

        def p(x, y):
            return plansza.c2p(x, y)

        KRATKA = p(0, 0) - p(0, 1)      # wektor "jedna kratka w dol"

        liczby = VGroup()
        for x in (1, 2, 3, 4, 5, 6):
            n = MathTex(str(x), color=SZARY_OSIE, font_size=34)
            n.next_to(p(x, 0), UP, buff=0.14)
            liczby.add(n)
        for y in (-3, -6, -9):
            n = MathTex(str(y), color=SZARY_OSIE, font_size=34)
            n.next_to(p(0, y), LEFT, buff=0.16)
            liczby.add(n)
        os_x_podpis = MathTex("x", color=SZARY_OSIE, font_size=32)
        os_x_podpis.next_to(p(7, 0), UP + RIGHT, buff=0.04)
        os_y_podpis = MathTex("y", color=SZARY_OSIE, font_size=32)
        os_y_podpis.next_to(p(0, 1.4), UP + LEFT, buff=0.04)
        liczby.add(os_x_podpis, os_y_podpis)

        # Parabola f narysowana od (0, -9) do (6, -9): oba konce to punkt
        # z tresci i jego odbicie, wiec po zsunieciu o kratke krzywa dalej
        # miesci sie w kadrze.
        wykres = plansza.plot(
            lambda x: -((x - 3) ** 2),
            x_range=[0, 6, 0.02],
            color=FIOLET, stroke_width=6,
        )
        podpis_f = MathTex("y = f(x)", color=FIOLET, font_size=34)
        podpis_f.move_to(p(5.5, -1.1))

        # ================================================================
        # PRAWA POLOWA
        # ================================================================
        wzor_f = self.stan("f", "(", "x", ")", "=", "-", "(", "x", "-", "3",
                           ")", "^{2}", rozmiar=52)
        wzor_f.move_to([KOLUMNA_X, DANE_Y, 0])

        g_lit = self.stan("g", "(", "x", ")", "=", "f", "(", "x", ")", "-", "1")
        g_pel = self.stan("g", "(", "x", ")", "=",
                          "-", "(", "x", "-", "3", ")", "^{2}", "-", "1")
        for m in (g_lit, g_pel):
            m.move_to([KOLUMNA_X, RACHUNEK_Y, 0])

        def werdykt(nr, litera):
            g = VGroup(
                Text(f"Zdanie {nr}:", font_size=30, color=BLACK),
                Text(litera, font_size=34, weight=BOLD, color=BLACK),
            ).arrange(RIGHT, buff=0.28)
            g.move_to([KOLUMNA_X, WERDYKT_Y - (nr - 1) * WERDYKT_KROK, 0])
            return g

        werdykt1 = werdykt(1, "F")
        werdykt2 = werdykt(2, "P")

        # ================================================================
        # KROK 1. Wzor g powstaje ze wzoru f: w miejsce f(x) wchodzi to,
        # co zostalo policzone w poprzedniej czesci. Zielona jest odjeta
        # jedynka, bo to ona jest tu nowa.
        # ================================================================
        self.next_section("krok1")
        self.play(FadeIn(plansza), FadeIn(liczby), run_time=0.7)
        self.play(Create(wykres), run_time=1.2)
        self.play(FadeIn(podpis_f), run_time=0.4)
        self.play(FadeIn(wzor_f), run_time=0.6)
        self.play(FadeIn(g_lit), run_time=0.7)
        self.wait(0.3)

        kopia = wzor_f[5:12].copy()
        self.add(kopia)
        g_pel[12].set_color(ZIELONY)
        g_pel[13].set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(g_lit[i], g_pel[i]) for i in range(5)],
            ReplacementTransform(kopia, g_pel[5:12]),
            FadeOut(g_lit[5], scale=0.4), FadeOut(g_lit[6], scale=0.4),
            FadeOut(g_lit[7], scale=0.4), FadeOut(g_lit[8], scale=0.4),
            ReplacementTransform(g_lit[9], g_pel[12]),
            ReplacementTransform(g_lit[10], g_pel[13]),
            run_time=1.6,
        )
        self.zgas(g_pel[12], g_pel[13])
        self.wait(0.65)

        # ================================================================
        # KROK 2. Odejmowanie jedynki zsuwa CALY wykres o jedna kratke
        # w dol. Stara pozycja zostaje na chwile jako przerywana, zeby
        # bylo widac, o ile to jest.
        #
        # ZIELONE JEST TU DWOJE NARAZ i to jest caly sens kroku: strzalka
        # w kadrze oraz „- 1" we wzorze g (Henrich, 2026-08-30). To ta sama
        # jedynka, raz zapisana, raz narysowana; zapalona osobno strzalka mowila
        # „o tyle w dol", ale nie mowila, SKAD ta liczba sie wziela.
        # ================================================================
        self.next_section("krok2")
        # Slad startuje NIEWIDOCZNY i zapala sie dopiero w trakcie zsuwania.
        # Dolozony wprost na krzywa lezalby na niej szarymi kreskami juz
        # w pierwszej klatce kroku, czyli rozjazd na styku (tools/styk-klatek.sh).
        slad = DashedVMobject(
            wykres.copy().set_color(SZARY_OSIE).set_stroke(width=3),
            num_dashes=60,
        )
        slad.set_opacity(0)
        self.add(slad)

        strzalka = Arrow(
            p(3, 0), p(3, -1),
            color=ZIELONY, buff=0, stroke_width=6,
            max_tip_length_to_length_ratio=0.35,
        )
        etykieta_1 = MathTex("1", color=ZIELONY, font_size=32)
        etykieta_1.next_to(strzalka, RIGHT, buff=0.12)

        # Najpierw strzalka "o ile", dopiero potem zsuniecie. Kolejnosc jest
        # dydaktyczna (widac miare przesuniecia, zanim cokolwiek pojedzie),
        # a przy okazji krok zaczyna sie drobnym ruchem zamiast przejazdu calego
        # wykresu: pierwsza klatka pliku jest wtedy kodowana tak samo dokladnie
        # jak spoczynkowa klatka poprzedniego kroku (styk 0,99854 -> 0,99901).
        self.play(
            GrowArrow(strzalka), FadeIn(etykieta_1),
            g_pel[12].animate.set_color(ZIELONY),
            g_pel[13].animate.set_color(ZIELONY),
            run_time=0.8,
        )
        self.play(
            wykres.animate.shift(KRATKA),
            podpis_f.animate.shift(KRATKA),
            slad.animate.set_opacity(1),
            run_time=1.4,
        )

        nowy_w = Dot(p(3, -1), radius=0.08, color=ZIELONY)
        opis_w = MathTex("(3,\\ -1)", color=ZIELONY, font_size=34)
        # Odsuniety w prawo i w gore: postawiony tuz obok wierzcholka
        # siadal od kroku 3 na przerywanej prostej y = -1.
        opis_w.move_to(p(4.5, -0.5))
        self.play(FadeIn(nowy_w), FadeIn(opis_w), run_time=0.7)
        self.wait(0.4)
        self.zgas(nowy_w, opis_w, g_pel[12], g_pel[13])
        self.play(FadeOut(slad), FadeOut(strzalka), FadeOut(etykieta_1),
                  run_time=0.5)
        # Podpis wykresu nazywa juz inna funkcje.
        nowy_podpis = MathTex("y = g(x)", color=FIOLET, font_size=34)
        nowy_podpis.move_to(podpis_f.get_center())
        self.play(ReplacementTransform(podpis_f, nowy_podpis), run_time=0.6)
        self.wait(0.65)

        # ================================================================
        # KROK 3. Ramiona ida w dol, wiec wierzcholek jest najwyzej: caly
        # wykres lezy pod poziomem y = -1.
        # ================================================================
        self.next_section("krok3")
        poziom = DashedLine(p(-0.8, -1), p(6.9, -1), color=ZIELONY,
                            stroke_width=3, dash_length=0.30)
        podpis_poziom = MathTex("y = -1", color=ZIELONY, font_size=34)
        podpis_poziom.next_to(p(0.1, -1), DOWN + RIGHT, buff=0.10)
        self.play(Create(poziom), FadeIn(podpis_poziom), run_time=1.0)
        self.play(wykres.animate.set_color(ZIELONY), run_time=0.6)
        self.wait(0.5)
        self.play(wykres.animate.set_color(FIOLET),
                  poziom.animate.set_color(SZARY_OSIE),
                  podpis_poziom.animate.set_color(SZARY_OSIE),
                  run_time=0.5)
        self.wait(0.65)

        # ================================================================
        # KROK 4. Najwyzszy punkt lezy o kratke PONIZEJ osi x, wiec wykres
        # nigdzie jej nie dotyka: miejsc zerowych nie ma. Zdanie 1: F.
        # ================================================================
        self.next_section("krok4")
        os_zapalona = Line(p(-0.8, 0), p(6.9, 0), color=ZIELONY, stroke_width=6)
        self.play(Create(os_zapalona), run_time=0.8)
        odstep = Arrow(
            p(3, 0), p(3, -1),
            color=ZIELONY, buff=0, stroke_width=6,
            max_tip_length_to_length_ratio=0.35,
        )
        self.play(GrowArrow(odstep), run_time=0.7)
        self.play(FadeIn(werdykt1, shift=UP * 0.2), run_time=0.6)
        self.wait(0.4)
        self.zgas(os_zapalona, odstep)
        self.play(FadeOut(os_zapalona), FadeOut(odstep), run_time=0.4)
        self.wait(0.65)

        # ================================================================
        # KROK 5. Zsuniecie w dol nie przesuwa wykresu w bok, wiec os
        # symetrii zostaje ta sama. Zdanie 2: P.
        # ================================================================
        self.next_section("krok5")
        os_sym = DashedLine(p(3, 1.2), p(3, -10.2), color=ZIELONY,
                            stroke_width=3, dash_length=0.30)
        podpis_sym = MathTex("x = 3", color=ZIELONY, font_size=34)
        podpis_sym.next_to(p(3, 1.2), UP, buff=0.06)
        # Prawa galaz i os symetrii wjezdzaja razem, lewa dopiero potem: widac
        # wtedy, ze lewa jest odbiciem prawej wzgledem tej prostej.
        lewa = plansza.plot(lambda x: -((x - 3) ** 2) - 1, x_range=[0, 3, 0.02],
                            color=ZIELONY, stroke_width=6)
        prawa = plansza.plot(lambda x: -((x - 3) ** 2) - 1, x_range=[3, 6, 0.02],
                             color=ZIELONY, stroke_width=6)
        # Prosta wjezdza przez FadeIn, a nie Create: Create rysuje pierwsza kreske
        # juz w klatce zerowej, wiec pierwsza klatka pliku miala kilkadziesiat
        # zielonych pikseli (tools/zielen-krokow.py).
        self.play(FadeIn(os_sym, shift=UP * 0.4), FadeIn(podpis_sym, shift=UP * 0.4),
                  Create(prawa), run_time=1.0)
        self.play(Create(lewa), run_time=0.9)
        self.play(FadeIn(werdykt2, shift=UP * 0.2), run_time=0.6)
        self.wait(0.4)
        self.play(FadeOut(lewa), FadeOut(prawa), run_time=0.4)
        self.zgas(os_sym, podpis_sym)
        self.wait(0.65)
