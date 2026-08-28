from manim import *

# Zadanie 11 (prawda/falsz, 1 pkt). Funkcja liniowa: miejsce zerowe 2, punkt
# przeciecia z osia Oy rowny (0, 4). Wynik: a = -2 (P), pole trojkata 4, a nie 8 (F).
#
# Projekt: issues/projekt-zad11-zad12-2024-grudzien.md. Osiem krokow, jeden do
# jednego z osmioma linijkami rachunku w solutionText.
#
# Uklad kadru (README, punkt 35: trzy pasy, zawsze te same):
#   - LEWA polowa: uklad wspolrzednych z prosta, odwzorowany z arkusza
#     (matura/2024-grudzien/media/zad11/zad11.png): ten sam fiolet, ten sam
#     podpis y = f(x). Zakres osi wezszy niz w arkuszu (-2 do 5 zamiast -5 do 5),
#     bo kadr 16:9 jest niski, a caly rachunek dzieje sie w pierwszej cwiartce.
#   - PRAWA polowa, cztery pasy: pas odczytu u gory (mniejszym pismem, README
#     punkt 41), pod nim miejsce na wynik pierwszej czesci, ktory tam parkuje
#     do konca filmu (wzorzec zad. 7), pod nim glowny rachunek, na dole werdykty
#     obu zdan.
#
# Dwie niezalezne czesci licza sie PO KOLEI (README, punkt 4): najpierw caly
# wspolczynnik kierunkowy, potem cale pole.
#
# Kolor: zielone = to, na co uczen ma w danym kroku patrzec i co sie zmienia.
# Wykres zostaje fioletowy (#7a3fa8, COLORS.md, rola "wykres funkcji jak
# w arkuszach CKE"), osie i siatka szare. Litery P i F sa CZARNE: to odpowiedz
# ucznia, a nie ocena poprawnosci (COLORS.md, "domyslnie NIE koloruj").
#
# Render: manim --save_sections solutionZad11.py Zad11  (albo tools/wgraj-kroki.sh 11)

ZIELONY = "#2e7d32"
FIOLET = "#7a3fa8"
SZARY_OSIE = "#666666"
SZARY_SIATKA = "#e0e0e0"

SRODEK_WYKRESU = LEFT * 4.0 + DOWN * 0.15
KOLUMNA_X = 3.15
PAS_Y = 3.05
GORA_Y = 1.45
RACHUNEK_Y = -0.55
WERDYKT_Y = -2.55
WERDYKT_KROK = 0.85


class Zad11(Scene):

    # ---- klocki -------------------------------------------------------

    def stan(self, *args, rozmiar=54):
        m = MathTex(*args)
        m.set_color(BLACK)
        m.font_size = rozmiar
        return m

    def ulamek(self, gora, dol, rozmiar=54):
        """Ulamek zlozony recznie: licznik, kreska, mianownik. Daje uchwyt do
        kazdego glifu licznika, czego \\dfrac w jednym MathTeksie nie daje."""
        g = self.stan(*gora, rozmiar=rozmiar)
        d = self.stan(*dol, rozmiar=rozmiar)
        szer = max(g.width, d.width) + 0.20
        kreska = Line(LEFT * szer / 2, RIGHT * szer / 2, color=BLACK, stroke_width=4)
        g.next_to(kreska, UP, buff=0.13)
        d.next_to(kreska, DOWN, buff=0.13)
        return VGroup(g, kreska, d)

    def zgas(self, *mobiekty, czas=0.4):
        """Gasi zielone na czarno. Wolane PRZED koncowym postojem, zeby
        ostatnia klatka kroku byla czysta (README, punkt 1 zasad)."""
        if mobiekty:
            self.play(*[m.animate.set_color(BLACK) for m in mobiekty], run_time=czas)

    def zamknij(self, *znika, czas=0.35):
        if znika:
            self.play(*[FadeOut(m) for m in znika], run_time=czas)
        self.wait(0.45)

    def construct(self):
        # ================================================================
        # SCENOGRAFIA: uklad wspolrzednych i prosta y = -2x + 4
        # ================================================================
        plansza = NumberPlane(
            x_range=[-2, 5, 1],
            y_range=[-2, 5, 1],
            x_length=5.6,
            y_length=5.6,
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
                "tip_width": 0.16,
                "tip_height": 0.16,
            },
        )
        plansza.move_to(SRODEK_WYKRESU)

        def p(x, y):
            return plansza.c2p(x, y)

        liczby = VGroup()
        for x in (1, 2, 3, 4):
            n = MathTex(str(x), color=SZARY_OSIE, font_size=34)
            n.next_to(p(x, 0), DOWN, buff=0.22)
            liczby.add(n)
        for y in (1, 2, 3, 4):
            n = MathTex(str(y), color=SZARY_OSIE, font_size=34)
            n.next_to(p(0, y), LEFT, buff=0.20)
            liczby.add(n)
        os_x_podpis = MathTex("x", color=SZARY_OSIE, font_size=38)
        os_x_podpis.next_to(p(5, 0), DOWN + RIGHT, buff=0.04)
        os_y_podpis = MathTex("y", color=SZARY_OSIE, font_size=38)
        os_y_podpis.next_to(p(0, 5), UP + LEFT, buff=0.04)
        liczby.add(os_x_podpis, os_y_podpis)

        # y = -2x + 4 przycięte do kadru wykresu: od (-0.5, 5) do (3, -2).
        prosta = Line(p(-0.5, 5), p(3, -2), color=FIOLET, stroke_width=6)
        podpis_f = MathTex("y = f(x)", color=FIOLET, font_size=42)
        podpis_f.move_to(p(3.4, 2.6))

        # ================================================================
        # PRAWA POLOWA: pas odczytu, rachunek, werdykty
        # ================================================================
        a_pkt = self.stan("A", "=", "(", "0", ",\\ ", "4", ")", rozmiar=40)
        b_pkt = self.stan("B", "=", "(", "2", ",\\ ", "0", ")", rozmiar=40)
        pas = VGroup(a_pkt, b_pkt).arrange(RIGHT, buff=0.75)
        pas.move_to([KOLUMNA_X, PAS_Y, 0])

        def wiersz(*czesci, buff=0.16):
            g = VGroup(*czesci)
            g.arrange(RIGHT, buff=buff)
            return g

        # Stany rachunku pierwszej czesci.
        w2lit = wiersz(
            self.stan("a"), self.stan("="),
            self.ulamek(("y_{B}", "-", "y_{A}"), ("x_{B}", "-", "x_{A}")),
        )
        s2 = wiersz(
            self.stan("a"), self.stan("="),
            self.ulamek(("0", "-", "4"), ("2", "-", "0")),
        )
        s3 = wiersz(
            self.stan("a"), self.stan("="),
            self.ulamek(("-4",), ("2",)),
        )
        s4 = self.stan("a", "=", "-2")

        # Stany rachunku drugiej czesci.
        w7lit = wiersz(
            self.stan("P"), self.stan("="),
            self.ulamek(("1",), ("2",)),
            self.stan("a"), self.stan(r"\cdot"), self.stan("h_{a}"),
        )
        s7 = wiersz(
            self.stan("P"), self.stan("="),
            self.ulamek(("1",), ("2",)),
            self.stan(r"\cdot"), self.stan("2"),
            self.stan(r"\cdot"), self.stan("4"),
        )
        s8 = self.stan("P", "=", "4")
        roznica = self.stan("4", r"\ne", "8", rozmiar=42)

        for m in (w2lit, s2, s3, s4, w7lit, s7, s8):
            m.move_to([KOLUMNA_X, RACHUNEK_Y, 0])
        roznica.move_to([KOLUMNA_X, RACHUNEK_Y - 1.15, 0])

        s4_gora = self.stan("a", "=", "-2")
        s4_gora.move_to([KOLUMNA_X, GORA_Y, 0])

        def werdykt(nr, litera):
            g = VGroup(
                Text(f"Zdanie {nr}:", font_size=30, color=BLACK),
                Text(litera, font_size=34, weight=BOLD, color=BLACK),
            ).arrange(RIGHT, buff=0.28)
            g.move_to([KOLUMNA_X, WERDYKT_Y - (nr - 1) * WERDYKT_KROK, 0])
            return g

        werdykt1 = werdykt(1, "P")
        werdykt2 = werdykt(2, "F")

        def przywolaj(zrodla, cele, czas=1.0, luk=-PI / 4):
            """Kopie wartosci z pasa odczytu leca na miejsca liter we wzorze.
            Zielone, bo to one sa tym, co sie w tym kroku zmienia
            (README, punkty 37 i 38)."""
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
        # KROK 1. Odczyt dwoch punktow z wykresu. Zielone: punkty i ich
        # wspolrzedne, bo to na nie uczen ma patrzec.
        # ================================================================
        self.next_section("krok1")
        self.play(FadeIn(plansza), FadeIn(liczby), run_time=0.8)
        self.play(Create(prosta), run_time=1.2)
        self.play(FadeIn(podpis_f), run_time=0.4)

        punkt_a = Dot(p(0, 4), radius=0.09, color=ZIELONY)
        punkt_b = Dot(p(2, 0), radius=0.09, color=ZIELONY)
        opis_a = MathTex("(0,\\ 4)", color=ZIELONY, font_size=38)
        opis_a.next_to(punkt_a, LEFT, buff=0.16)
        opis_b = MathTex("(2,\\ 0)", color=ZIELONY, font_size=38)
        opis_b.next_to(punkt_b, DOWN + RIGHT, buff=0.10)
        self.play(FadeIn(punkt_a), FadeIn(punkt_b), run_time=0.5)
        self.play(FadeIn(opis_a), FadeIn(opis_b), run_time=0.6)

        for cz in (a_pkt[2:7], b_pkt[2:7]):
            cz.set_color(ZIELONY)
        self.play(
            FadeIn(a_pkt[0], a_pkt[1]), FadeIn(b_pkt[0], b_pkt[1]),
            ReplacementTransform(opis_a, a_pkt[2:7]),
            ReplacementTransform(opis_b, b_pkt[2:7]),
            run_time=1.2,
        )
        self.zgas(punkt_a, punkt_b, a_pkt[2:7], b_pkt[2:7])
        self.play(FadeOut(punkt_a), FadeOut(punkt_b), run_time=0.3)
        self.wait(0.45)

        # ================================================================
        # KROK 2. Wzor na wspolczynnik kierunkowy staje literami, a potem
        # kazda litera zamienia sie w liczbe przylatujaca z pasa odczytu
        # (README, punkt 37). Zielone: przylatujace liczby.
        # ================================================================
        self.next_section("krok2")
        self.play(FadeIn(w2lit), run_time=0.9)
        self.wait(0.45)

        licz_lit, _, mian_lit = w2lit[2]
        licz_now, _, mian_now = s2[2]
        kopie = przywolaj(
            [b_pkt[5], a_pkt[5], b_pkt[3], a_pkt[3]],
            [licz_lit[0].get_center(), licz_lit[2].get_center(),
             mian_lit[0].get_center(), mian_lit[2].get_center()],
        )
        for i in (0, 2):
            licz_now[i].set_color(ZIELONY)
            mian_now[i].set_color(ZIELONY)
        self.play(
            ReplacementTransform(w2lit[0], s2[0]),
            ReplacementTransform(w2lit[1], s2[1]),
            ReplacementTransform(w2lit[2][1], s2[2][1]),
            ReplacementTransform(licz_lit[1], licz_now[1]),
            ReplacementTransform(mian_lit[1], mian_now[1]),
            ReplacementTransform(kopie[0], licz_now[0]),
            ReplacementTransform(kopie[1], licz_now[2]),
            ReplacementTransform(kopie[2], mian_now[0]),
            ReplacementTransform(kopie[3], mian_now[2]),
            FadeOut(licz_lit[0], scale=0.4), FadeOut(licz_lit[2], scale=0.4),
            FadeOut(mian_lit[0], scale=0.4), FadeOut(mian_lit[2], scale=0.4),
            run_time=1.5,
        )
        self.zgas(licz_now[0], licz_now[2], mian_now[0], mian_now[2])
        self.wait(0.45)

        # ================================================================
        # KROK 3. Odejmowanie w liczniku i w mianowniku. Zielone: to, co
        # z niego powstaje, bo tu uczen najczesciej odwraca kolejnosc.
        # ================================================================
        self.next_section("krok3")
        licz_3, _, mian_3 = s3[2]
        self.play(
            *[m.animate.set_color(ZIELONY) for m in (licz_now, mian_now)],
            run_time=0.35,
        )
        licz_3.set_color(ZIELONY)
        mian_3.set_color(ZIELONY)
        self.play(
            ReplacementTransform(s2[0], s3[0]),
            ReplacementTransform(s2[1], s3[1]),
            ReplacementTransform(s2[2][1], s3[2][1]),
            ReplacementTransform(licz_now, licz_3),
            ReplacementTransform(mian_now, mian_3),
            run_time=1.3,
        )
        self.zgas(licz_3, mian_3)
        self.wait(0.45)

        # ================================================================
        # KROK 4. Dzielenie i werdykt pierwszego zdania. Zielony jest sam
        # wynik; litera P zostaje czarna.
        # ================================================================
        self.next_section("krok4")
        s4[2].set_color(ZIELONY)
        # ReplacementTransform, a nie Transform: Transform zostawia w kadrze
        # obiekt ZRODLOWY pomalowany na kolor celu, wiec zielone "-2" zostawalo
        # na miejscu rachunku i przez kolejne kroki lezalo pod wzorem na pole
        # (README, punkt 14).
        self.play(
            ReplacementTransform(s3[0], s4[0]),
            ReplacementTransform(s3[1], s4[1]),
            ReplacementTransform(s3[2], s4[2]),
            run_time=1.2,
        )
        self.play(FadeIn(werdykt1, shift=UP * 0.2), run_time=0.6)
        self.zgas(s4[2])
        self.wait(0.45)

        # ================================================================
        # KROK 5. Druga czesc. Wynik pierwszej odjezdza na gore kadru
        # i tam zostaje (wzorzec zad. 7). Na wykresie zapala sie trojkat
        # ograniczony osiami i prosta.
        # ================================================================
        self.next_section("krok5")
        self.play(ReplacementTransform(s4, s4_gora), run_time=0.9)

        trojkat = Polygon(
            p(0, 0), p(2, 0), p(0, 4),
            color=ZIELONY, stroke_width=5,
            fill_color=ZIELONY, fill_opacity=0.13,
        )
        wierzcholki = VGroup(
            Dot(p(0, 0), radius=0.08, color=ZIELONY),
            Dot(p(2, 0), radius=0.08, color=ZIELONY),
            Dot(p(0, 4), radius=0.08, color=ZIELONY),
        )
        self.play(FadeIn(wierzcholki), run_time=0.5)
        self.play(Create(trojkat), run_time=1.2)
        self.play(
            trojkat.animate.set_stroke(BLACK).set_fill(BLACK, 0.08),
            wierzcholki.animate.set_color(BLACK),
            run_time=0.4,
        )
        self.wait(0.45)

        # ================================================================
        # KROK 6. Podstawa i wysokosc. Oba odcinki leza na osiach, wiec
        # ich dlugosci odczytuje sie wprost z liczb przy osiach.
        # ================================================================
        self.next_section("krok6")
        podstawa = Line(p(0, 0), p(2, 0), color=ZIELONY, stroke_width=8)
        wysokosc = Line(p(0, 0), p(0, 4), color=ZIELONY, stroke_width=8)
        dl_podstawy = MathTex("2", color=ZIELONY, font_size=44)
        # Dlugosci stoja WEWNATRZ trojkata, jak w podreczniku. Postawione obok
        # osi siadaly dokladnie na szarych liczbach przy osiach (2 pod jedynka,
        # 4 obok dwojki) i czytaly sie jak druga podzialka.
        dl_podstawy.move_to(p(1, 0.42))
        dl_wysokosci = MathTex("4", color=ZIELONY, font_size=44)
        dl_wysokosci.move_to(p(0.42, 2))
        self.play(Create(podstawa), run_time=0.6)
        self.play(FadeIn(dl_podstawy), run_time=0.4)
        self.play(Create(wysokosc), run_time=0.6)
        self.play(FadeIn(dl_wysokosci), run_time=0.4)
        self.zgas(podstawa, wysokosc, dl_podstawy, dl_wysokosci)
        self.wait(0.45)

        # ================================================================
        # KROK 7. Wzor na pole staje literami, potem a i h_a zamieniaja sie
        # w liczby przylatujace z odcinkow na wykresie.
        # ================================================================
        self.next_section("krok7")
        self.play(FadeIn(w7lit), run_time=0.9)
        self.wait(0.45)

        kopie2 = przywolaj(
            [dl_podstawy, dl_wysokosci],
            [w7lit[3].get_center(), w7lit[5].get_center()],
            czas=1.1, luk=-PI / 3,
        )
        s7[4].set_color(ZIELONY)
        s7[6].set_color(ZIELONY)
        self.play(
            ReplacementTransform(w7lit[0], s7[0]),
            ReplacementTransform(w7lit[1], s7[1]),
            ReplacementTransform(w7lit[2], s7[2]),
            FadeIn(s7[3]),
            ReplacementTransform(kopie2[0], s7[4]),
            ReplacementTransform(w7lit[4], s7[5]),
            ReplacementTransform(kopie2[1], s7[6]),
            FadeOut(w7lit[3], scale=0.4), FadeOut(w7lit[5], scale=0.4),
            run_time=1.5,
        )
        self.zgas(s7[4], s7[6])
        self.wait(0.45)

        # ================================================================
        # KROK 8. Wynik, porownanie z liczba ze zdania 2 i werdykt.
        # ================================================================
        self.next_section("krok8")
        s8[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s7[0], s8[0]),
            ReplacementTransform(s7[1], s8[1]),
            ReplacementTransform(VGroup(*s7[2:]), s8[2]),
            run_time=1.3,
        )
        self.play(FadeIn(roznica), run_time=0.6)
        self.play(FadeIn(werdykt2, shift=UP * 0.2), run_time=0.6)
        self.zgas(s8[2])
        self.wait(0.45)
