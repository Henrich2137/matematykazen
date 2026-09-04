from manim import *

# Zadanie 21 (zamkniete, 1 pkt). A = (-2, -1) i C = (3, 4) to przeciwlegle
# wierzcholki kwadratu ABCD; szukamy dlugosci boku. Wynik: a = 5, odpowiedz A.
#
# Projekt: issues/projekt-zad20-zad21-2024-grudzien.md. Pietnascie krokow;
# dziesiec z nich to linijki rachunku z solutionText, piec (1, 2, 3, 9, 15)
# to kroki rysunkowe, ktorych tekst nie potrzebuje jako osobnych linijek.
#
# Decyzje Henricha (2026-09-04):
#   - obie dlugosci liczymy Pitagorasem i obie pokazujemy graficznie,
#   - kwadrat widoczny od pierwszego kroku, na siatce kratek,
#   - trojkat pod przekatna pokazany jawnie (5 w gore, 5 w prawo),
#   - rysunek zostaje w kadrze do konca, rachunek idzie obok niego.
#
# Z danych wychodzi B = (3, -1) i D = (-2, 4), czyli kwadrat lezy rownolegle do
# osi, a przekatna dzieli go na dwa przystajace trojkaty. Zeby czesc druga nie
# liczyla tego, co widac juz w czesci pierwszej, KAZDA POLOWA ROBI INNA ROBOTE:
#   - gorny trojkat ACD: przyprostokatne to roznice wspolrzednych (przekatna),
#   - dolny trojkat ABC: przyprostokatne to boki kwadratu, obie rowne a.
#
# Uklad kadru (README, punkt 35: trzy pasy, zawsze te same):
#   - LEWA polowa: uklad wspolrzednych z kwadratem i przekatna,
#   - PRAWA gora: pas odczytu (dane z tresci), pod nim pas roboczy (ogniwa,
#     mniejszym pismem, znikaja przed koncem kroku, README punkt 29),
#   - PRAWA srodek: glowny rachunek, ten sam pas przez caly film,
#   - PRAWA dol: odpowiedz.
#
# Niewiadoma zostaje po tej stronie, po ktorej postawilo ja podstawienie: w
# czesci pierwszej po prawej (5^2 + 5^2 = |AC|^2), w czesci drugiej po lewej.
# Dzieki temu zaden krok nie robi dwoch rzeczy naraz (przestawienie stron
# rownania byloby drugim przeksztalceniem w tej samej linijce).
#
# Render: manim --save_sections solutionZad21.py Zad21  (albo tools/wgraj-kroki.sh 21)

ZIELONY = "#2e7d32"
SZARY_OSIE = "#666666"
SZARY_SIATKA = "#e0e0e0"
SZARY_DZIALANIE = "#888888"

SRODEK_WYKRESU = LEFT * 4.05 + DOWN * 0.10
KOLUMNA_X = 3.30
PAS_Y = 3.10
ROBOCZY_Y = 2.15
RACHUNEK_Y = 0.10
ODPOWIEDZ_Y = -2.55


class Zad21(Scene):

    # ---- klocki -------------------------------------------------------

    def stan(self, *args, rozmiar=54):
        m = MathTex(*args)
        m.set_color(BLACK)
        m.font_size = rozmiar
        return m

    def wiersz(self, *czesci, buff=0.17):
        return VGroup(*czesci).arrange(RIGHT, buff=buff)

    def zgas(self, *mobiekty, czas=0.4):
        """Gasi zielone na czarno PRZED koncowym postojem, zeby ostatnia klatka
        kroku byla czysta (README, punkt 1 zasad)."""
        if mobiekty:
            self.play(*[m.animate.set_color(BLACK) for m in mobiekty], run_time=czas)

    def zamknij(self, *znika, czas=0.35):
        if znika:
            self.play(*[FadeOut(m) for m in znika], run_time=czas)
        self.wait(0.45)

    def construct(self):
        # ================================================================
        # SCENOGRAFIA: uklad wspolrzednych, kwadrat ABCD, przekatna AC
        # ================================================================
        plansza = NumberPlane(
            x_range=[-3, 4, 1],
            y_range=[-2, 5, 1],
            x_length=5.4,
            y_length=5.4,
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

        # Liczby na osiach odsuniete OD BOKOW kwadratu: kazdy z tych czterech
        # bokow przechodzi dokladnie przez swoja liczbe na osi, wiec podpis
        # postawiony wprost przy osi leglby na odcinku i bylby nieczytelny.
        liczby = VGroup()
        for x, przesun in ((-2, LEFT * 0.20), (3, RIGHT * 0.20)):
            n = MathTex(str(x), color=SZARY_OSIE, font_size=32)
            n.next_to(p(x, 0), DOWN, buff=0.16)
            n.shift(przesun)
            liczby.add(n)
        for y, przesun in ((-1, UP * 0.28), (4, DOWN * 0.28)):
            n = MathTex(str(y), color=SZARY_OSIE, font_size=32)
            n.next_to(p(0, y), LEFT, buff=0.16)
            n.shift(przesun)
            liczby.add(n)
        os_x = MathTex("x", color=SZARY_OSIE, font_size=36)
        os_x.next_to(p(4, 0), DOWN + RIGHT, buff=0.04)
        os_y = MathTex("y", color=SZARY_OSIE, font_size=36)
        os_y.next_to(p(0, 5), UP + LEFT, buff=0.04)
        liczby.add(os_x, os_y)

        # Boki jako osobne odcinki, bo kazdy zapala sie z osobna. Podswietlenie
        # zmienia TYLKO kolor, nigdy grubosc (README, punkt 46).
        bok_ab = Line(p(-2, -1), p(3, -1), color=BLACK, stroke_width=5)
        bok_bc = Line(p(3, -1), p(3, 4), color=BLACK, stroke_width=5)
        bok_cd = Line(p(3, 4), p(-2, 4), color=BLACK, stroke_width=5)
        bok_da = Line(p(-2, 4), p(-2, -1), color=BLACK, stroke_width=5)
        przekatna = Line(p(-2, -1), p(3, 4), color=BLACK, stroke_width=5)

        def kat_prosty(wierzcholek, kier1, kier2, bok=0.30):
            """Kwadracik kata prostego, zlozony recznie z trzech punktow."""
            a = wierzcholek + kier1 * bok
            b = wierzcholek + kier1 * bok + kier2 * bok
            c = wierzcholek + kier2 * bok
            return VMobject(color=BLACK, stroke_width=3).set_points_as_corners([a, b, c])

        kat_d = kat_prosty(p(-2, 4), DOWN, RIGHT)
        kat_b = kat_prosty(p(3, -1), LEFT, UP)

        def podpis(litera, punkt, kierunek):
            m = MathTex(litera, color=BLACK, font_size=38)
            m.next_to(punkt, kierunek, buff=0.16)
            return m

        pkt_a, pkt_b = p(-2, -1), p(3, -1)
        pkt_c, pkt_d = p(3, 4), p(-2, 4)
        litery = VGroup(
            podpis("A", pkt_a, DOWN + LEFT),
            podpis("B", pkt_b, DOWN + RIGHT),
            podpis("C", pkt_c, UP + RIGHT),
            podpis("D", pkt_d, UP + LEFT),
        )
        kropki = VGroup(*[Dot(q, radius=0.06, color=BLACK)
                          for q in (pkt_a, pkt_b, pkt_c, pkt_d)])

        # ================================================================
        # PRAWA POLOWA: pas odczytu, pas roboczy, rachunek, odpowiedz
        # ================================================================
        dane_a = self.stan("A", "=", "(", "-2", ",\\ ", "-1", ")", rozmiar=40)
        dane_c = self.stan("C", "=", "(", "3", ",\\ ", "4", ")", rozmiar=40)
        dane = VGroup(dane_a, dane_c).arrange(RIGHT, buff=0.60)
        dane.move_to([KOLUMNA_X, PAS_Y, 0])

        # Ogniwa liczone na boku: mniejsze pismo, bo to praca robocza, a nie
        # linijka rozwiazania (README, punkty 29 i 30).
        roz_pion = self.stan("4", "-", "(-1)", "=", "4+1", "=", "5", rozmiar=36)
        roz_poz = self.stan("3", "-", "(-2)", "=", "3+2", "=", "5", rozmiar=36)
        roznice = VGroup(roz_pion, roz_poz).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        roznice.move_to([KOLUMNA_X, ROBOCZY_Y, 0])

        ogniwo_pierwiastek = self.stan(
            r"\sqrt{50}", "=", r"\sqrt{25 \cdot 2}", "=", r"\sqrt{25} \cdot \sqrt{2}",
            rozmiar=36)
        ogniwo_kwadrat = self.stan(
            r"(5\sqrt{2})^{2}", "=", r"5^{2} \cdot (\sqrt{2})^{2}", "=", r"25 \cdot 2",
            rozmiar=36)
        for m in (ogniwo_pierwiastek, ogniwo_kwadrat):
            m.move_to([KOLUMNA_X, ROBOCZY_Y, 0])

        # Stany rachunku, czesc 1 (przekatna).
        w1 = self.wiersz(self.stan("a^{2}"), self.stan("+"), self.stan("b^{2}"),
                         self.stan("="), self.stan("c^{2}"))
        s4 = self.wiersz(self.stan("5^{2}"), self.stan("+"), self.stan("5^{2}"),
                         self.stan("="), self.stan("|AC|^{2}"))
        s5 = self.wiersz(self.stan("25"), self.stan("+"), self.stan("25"),
                         self.stan("="), self.stan("|AC|^{2}"))
        s6 = self.wiersz(self.stan("50"), self.stan("="), self.stan("|AC|^{2}"))
        s7 = self.wiersz(self.stan(r"\sqrt{50}"), self.stan("="), self.stan("|AC|"))
        s8 = self.wiersz(self.stan(r"5\sqrt{2}"), self.stan("="), self.stan("|AC|"))

        # Stany rachunku, czesc 2 (bok kwadratu).
        w2 = self.wiersz(self.stan("a^{2}"), self.stan("+"), self.stan("b^{2}"),
                         self.stan("="), self.stan("c^{2}"))
        s10 = self.wiersz(self.stan("a^{2}"), self.stan("+"), self.stan("a^{2}"),
                          self.stan("="), self.stan(r"(5\sqrt{2})^{2}"))
        s11 = self.wiersz(self.stan("2a^{2}"), self.stan("="),
                          self.stan(r"(5\sqrt{2})^{2}"))
        s12 = self.wiersz(self.stan("2a^{2}"), self.stan("="), self.stan("50"))
        s13 = self.wiersz(self.stan("a^{2}"), self.stan("="), self.stan("25"))
        s14 = self.wiersz(self.stan("a"), self.stan("="), self.stan("5"))

        for m in (w1, s4, s5, s6, s7, s8, w2, s10, s11, s12, s13, s14):
            m.move_to([KOLUMNA_X, RACHUNEK_Y, 0])

        dzielenie = MathTex(r"\big/ : 2", color=SZARY_DZIALANIE, font_size=44)

        odpowiedz = VGroup(
            Text("Odpowiedź", font_size=34, color=BLACK),
            Text("A", font_size=38, weight=BOLD, color=BLACK),
        ).arrange(RIGHT, buff=0.26)
        odpowiedz.move_to([KOLUMNA_X, ODPOWIEDZ_Y, 0])

        def przywolaj(zrodla, cele, czas=1.0, luk=-PI / 4):
            """Kopie wartosci leca z rysunku na miejsca liter we wzorze
            (README, punkty 37 i 38): liczba nigdy nie pojawia sie z niczego."""
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
        # KROK 1. Kwadrat z tresci zadania i dane. Caly czarny: nic sie tu
        # jeszcze nie przelicza (README, punkt 12).
        # ================================================================
        self.next_section("krok1")
        self.play(FadeIn(plansza), FadeIn(liczby), run_time=0.8)
        self.play(Create(bok_ab), Create(bok_bc), Create(bok_cd), Create(bok_da),
                  run_time=1.2)
        self.play(FadeIn(kropki), FadeIn(litery), run_time=0.6)
        self.play(Create(przekatna), run_time=0.9)
        self.play(FadeIn(dane), run_time=0.7)
        self.wait(0.45)

        # ================================================================
        # KROK 2. Przekatna dzieli kwadrat na dwa trojkaty prostokatne.
        # Bierzemy gorny: jego przyprostokatne to AD i DC. Zielone: te dwie
        # przyprostokatne, bo to na nie uczen ma teraz patrzec.
        # ================================================================
        self.next_section("krok2")
        self.play(bok_da.animate.set_color(ZIELONY),
                  bok_cd.animate.set_color(ZIELONY), run_time=0.6)
        self.play(Create(kat_d), run_time=0.5)
        self.wait(0.35)
        self.zgas(bok_da, bok_cd)
        self.wait(0.45)

        # ================================================================
        # KROK 3. Przyprostokatne to roznice wspolrzednych. Ogniwo odejmowania
        # liczby ujemnej wypisane jawnie w pasie roboczym, potem piatki lecą na
        # rysunek. Na koncu kroku wjezdza wzor (README, punkt 53).
        # ================================================================
        self.next_section("krok3")
        self.play(FadeIn(roz_pion), run_time=0.7)
        self.play(FadeIn(roz_poz), run_time=0.7)
        self.wait(0.35)

        piatka_pion = MathTex("5", color=ZIELONY, font_size=40)
        piatka_pion.next_to(bok_da, LEFT, buff=0.18)
        piatka_poz = MathTex("5", color=ZIELONY, font_size=40)
        piatka_poz.next_to(bok_cd, UP, buff=0.18)
        kopie = przywolaj([roz_pion[6], roz_poz[6]],
                          [piatka_pion.get_center(), piatka_poz.get_center()],
                          luk=PI / 3)
        self.play(ReplacementTransform(kopie[0], piatka_pion),
                  ReplacementTransform(kopie[1], piatka_poz), run_time=0.5)
        self.wait(0.35)
        self.zgas(piatka_pion, piatka_poz)
        self.play(FadeOut(roznice), run_time=0.4)
        self.play(FadeIn(w1), run_time=0.7)
        self.wait(0.45)

        # ================================================================
        # KROK 4. Podstawienie: piatki przylatuja Z RYSUNKU pod a i b, pod c
        # wchodzi szukana przekatna. Zielone: to, co wchodzi w miejsce liter.
        # ================================================================
        self.next_section("krok4")
        kopie = przywolaj([piatka_pion, piatka_poz],
                          [w1[0].get_center(), w1[2].get_center()])
        for i in (0, 2, 4):
            s4[i].set_color(ZIELONY)
        self.play(
            ReplacementTransform(kopie[0], s4[0]),
            ReplacementTransform(kopie[1], s4[2]),
            FadeOut(w1[0], scale=0.4), FadeOut(w1[2], scale=0.4),
            ReplacementTransform(w1[1], s4[1]),
            ReplacementTransform(w1[3], s4[3]),
            ReplacementTransform(w1[4], s4[4]),
            run_time=1.1,
        )
        self.zgas(s4[0], s4[2], s4[4])
        self.wait(0.45)

        # ================================================================
        # KROK 5. Podnosimy obie piatki do kwadratu.
        # ================================================================
        self.next_section("krok5")
        s5[0].set_color(ZIELONY)
        s5[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s4[0], s5[0]),
            ReplacementTransform(s4[2], s5[2]),
            ReplacementTransform(s4[1], s5[1]),
            ReplacementTransform(s4[3], s5[3]),
            ReplacementTransform(s4[4], s5[4]),
            run_time=1.0,
        )
        self.zgas(s5[0], s5[2])
        self.wait(0.45)

        # ================================================================
        # KROK 6. Dodawanie: dwie liczby scalaja sie w jedna (README, punkt 56:
        # jeden skladnik jedzie Transformem, drugi znika lecac w to samo miejsce).
        # ================================================================
        self.next_section("krok6")
        s6[0].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s5[0], s6[0]),
            FadeOut(s5[1], target_position=s6[0].get_center(), scale=0.4),
            FadeOut(s5[2], target_position=s6[0].get_center(), scale=0.4),
            ReplacementTransform(s5[3], s6[1]),
            ReplacementTransform(s5[4], s6[2]),
            run_time=1.0,
        )
        self.zgas(s6[0])
        self.wait(0.45)

        # ================================================================
        # KROK 7. Pierwiastkujemy obie strony. Zielone: pierwiastek, ktory sie
        # pojawia, i kwadrat, ktory znika.
        # ================================================================
        self.next_section("krok7")
        s7[0].set_color(ZIELONY)
        s7[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s6[0], s7[0]),
            ReplacementTransform(s6[1], s7[1]),
            ReplacementTransform(s6[2], s7[2]),
            run_time=1.0,
        )
        self.zgas(s7[0], s7[2])
        self.wait(0.45)

        # ================================================================
        # KROK 8. Wyciagamy 25 spod pierwiastka. Ogniwo w pasie roboczym znika
        # przed koncem kroku, wiec ostatnia klatka zostaje czysta.
        # ================================================================
        self.next_section("krok8")
        self.play(FadeIn(ogniwo_pierwiastek), run_time=0.7)
        self.wait(0.35)
        s8[0].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s7[0], s8[0]),
            ReplacementTransform(s7[1], s8[1]),
            ReplacementTransform(s7[2], s8[2]),
            run_time=1.0,
        )
        self.wait(0.35)
        self.zgas(s8[0])
        self.play(FadeOut(ogniwo_pierwiastek), run_time=0.4)
        self.wait(0.45)

        # ================================================================
        # KROK 9. Przekatna policzona, wiec jej dlugosc siada przy odcinku na
        # rysunku, a pas odczytu sie czysci (README, punkt 52). Teraz dolny
        # trojkat: jego przyprostokatne to boki kwadratu, obie rowne a.
        # ================================================================
        self.next_section("krok9")
        podpis_przek = MathTex(r"5\sqrt{2}", color=BLACK, font_size=40)
        podpis_przek.move_to(przekatna.get_center() + UP * 0.30 + LEFT * 0.34)
        kopia_wyniku = s8[0].copy()
        self.play(
            kopia_wyniku.animate.move_to(podpis_przek.get_center()).scale(40 / 54),
            FadeOut(dane),
            FadeOut(piatka_pion), FadeOut(piatka_poz),
            FadeOut(kat_d),
            run_time=1.1,
        )
        self.remove(kopia_wyniku)
        self.add(podpis_przek)
        self.play(FadeOut(s8[0]), FadeOut(s8[1]), FadeOut(s8[2]), run_time=0.5)

        podpis_ab = MathTex("a", color=ZIELONY, font_size=40)
        podpis_ab.next_to(bok_ab, DOWN, buff=0.18)
        podpis_bc = MathTex("a", color=ZIELONY, font_size=40)
        podpis_bc.next_to(bok_bc, RIGHT, buff=0.18)
        self.play(bok_ab.animate.set_color(ZIELONY),
                  bok_bc.animate.set_color(ZIELONY), run_time=0.6)
        self.play(Create(kat_b), FadeIn(podpis_ab), FadeIn(podpis_bc), run_time=0.7)
        self.wait(0.35)
        self.zgas(bok_ab, bok_bc, podpis_ab, podpis_bc)
        self.play(FadeIn(w2), run_time=0.7)
        self.wait(0.45)

        # ================================================================
        # KROK 10. Podstawienie do tego samego wzoru: pod a i b wchodza boki
        # kwadratu, pod c policzona przekatna. Wszystko przylatuje z rysunku.
        # ================================================================
        self.next_section("krok10")
        kopie = przywolaj(
            [podpis_ab, podpis_bc, podpis_przek],
            [w2[0].get_center(), w2[2].get_center(), w2[4].get_center()],
        )
        for i in (0, 2, 4):
            s10[i].set_color(ZIELONY)
        self.play(
            ReplacementTransform(kopie[0], s10[0]),
            ReplacementTransform(kopie[1], s10[2]),
            ReplacementTransform(kopie[2], s10[4]),
            FadeOut(w2[0], scale=0.4), FadeOut(w2[2], scale=0.4),
            FadeOut(w2[4], scale=0.4),
            ReplacementTransform(w2[1], s10[1]),
            ReplacementTransform(w2[3], s10[3]),
            run_time=1.2,
        )
        self.zgas(s10[0], s10[2], s10[4])
        self.wait(0.45)

        # ================================================================
        # KROK 11. Po lewej dwa takie same skladniki scalaja sie w jeden.
        # ================================================================
        self.next_section("krok11")
        s11[0].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s10[0], s11[0]),
            FadeOut(s10[1], target_position=s11[0].get_center(), scale=0.4),
            FadeOut(s10[2], target_position=s11[0].get_center(), scale=0.4),
            ReplacementTransform(s10[3], s11[1]),
            ReplacementTransform(s10[4], s11[2]),
            run_time=1.0,
        )
        self.zgas(s11[0])
        self.wait(0.45)

        # ================================================================
        # KROK 12. Podnosimy przekatna do kwadratu. Ogniwo (pierwiastek do
        # kwadratu znosi sie z potega) idzie w pasie roboczym.
        # ================================================================
        self.next_section("krok12")
        self.play(FadeIn(ogniwo_kwadrat), run_time=0.7)
        self.wait(0.35)
        s12[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s11[0], s12[0]),
            ReplacementTransform(s11[1], s12[1]),
            ReplacementTransform(s11[2], s12[2]),
            run_time=1.0,
        )
        self.wait(0.35)
        self.zgas(s12[2])
        self.play(FadeOut(ogniwo_kwadrat), run_time=0.4)
        self.wait(0.45)

        # ================================================================
        # KROK 13. Dzielimy obie strony przez 2. Dopisek dzialania jest szary,
        # bo to zapowiedz, a nie zapis rachunku (COLORS.md).
        # ================================================================
        self.next_section("krok13")
        dzielenie.next_to(s12, RIGHT, buff=0.55)
        self.play(FadeIn(dzielenie), run_time=0.5)
        self.wait(0.35)
        s13[0].set_color(ZIELONY)
        s13[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s12[0], s13[0]),
            ReplacementTransform(s12[1], s13[1]),
            ReplacementTransform(s12[2], s13[2]),
            FadeOut(dzielenie),
            run_time=1.0,
        )
        self.zgas(s13[0], s13[2])
        self.wait(0.45)

        # ================================================================
        # KROK 14. Pierwiastkujemy. Ujemny wynik odpada, bo bok nie ma ujemnej
        # dlugosci.
        # ================================================================
        self.next_section("krok14")
        s14[0].set_color(ZIELONY)
        s14[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s13[0], s14[0]),
            ReplacementTransform(s13[1], s14[1]),
            ReplacementTransform(s13[2], s14[2]),
            run_time=1.0,
        )
        self.zgas(s14[0], s14[2])
        self.wait(0.45)

        # ================================================================
        # KROK 15. Wynik siada przy boku kwadratu i pada odpowiedz.
        # ================================================================
        self.next_section("krok15")
        # Wynik rozdwaja sie i siada przy OBU bokach naraz (README, punkt 28):
        # to jedna czynnosc, wiec dzieje sie w jednym ruchu.
        wynik_ab = MathTex("5", color=ZIELONY, font_size=40)
        wynik_ab.move_to(podpis_ab.get_center())
        wynik_bc = MathTex("5", color=ZIELONY, font_size=40)
        wynik_bc.move_to(podpis_bc.get_center())
        kopie = [s14[2].copy(), s14[2].copy()]
        for k in kopie:
            self.add(k)
        self.play(
            kopie[0].animate.set_color(ZIELONY)
            .move_to(wynik_ab.get_center()).scale(40 / 54),
            kopie[1].animate.set_color(ZIELONY)
            .move_to(wynik_bc.get_center()).scale(40 / 54),
            FadeOut(podpis_ab), FadeOut(podpis_bc),
            run_time=1.0, path_arc=-PI / 4,
        )
        self.remove(*kopie)
        self.add(wynik_ab, wynik_bc)
        self.play(FadeIn(odpowiedz), run_time=0.6)
        self.wait(0.35)
        self.zgas(wynik_ab, wynik_bc)
        self.wait(0.45)
