from manim import *

# Zadanie 10 (zamkniete z lukami, 4 pkt). Odczyt z wykresu funkcji danej trzema
# wzorami. Odpowiedzi: (-4, 4>, <-1, 3>, (1, 3), (-4, -2>.
#
# Projekt: issues/projekt-zad9-zad10-2024-grudzien.md.
#
# WERSJA TRZECIA, 2026-08-29, po uwagach Henricha do drugiej (TODO.md).
# Piec krokow zamiast dziewieciu, po jednym na kazde zdanie do uzupelnienia
# plus jeden na sam rysunek:
#
#   krok 1  rysuje sie uklad wspolrzednych i wykres, nic wiecej;
#   krok 2  zdanie 1 (dziedzina), calosc od podswietlenia do gotowej odpowiedzi;
#   krok 3  zdanie 2 (zbior wartosci), tak samo;
#   krok 4  zdanie 3 (wartosci ujemne), tak samo;
#   krok 5  zdanie 4 (najwieksza wartosc), tak samo.
#
# CO SIE ZMIENILO I DLACZEGO. W wersji drugiej przedzial powstawal DWUETAPOWO:
# najprzod skladal sie ze skrawkow ("(-4", ",\\ ", "4\\rangle") na wysokosci
# ZAPIS_Y pod naglowkiem czesci, i dopiero stamtad odjezdzal na liste odpowiedzi.
# Henrich: „zapisy przedzialow, ktore pojawiaja sie pod naglowkami, zle sie
# renderuja". I renderowaly sie zle z powodu, ktory byl w samym pomysle: trzy
# osobne MathTeksy ustawione obok siebie przez arrange() nie stoja na wspolnej
# linii bazowej i maja przypadkowy odstep, wiec nawias, przecinek i liczba
# rozjezdzaja sie tak, jak nie rozjechalyby sie w jednym wzorze. Dlatego etap
# posredni znika w calosci: zielony pas na osi zamienia sie od razu w GOTOWY
# przedzial, zlozony jednym MathTeksem, i laduje wprost na liscie odpowiedzi.
#
# Wzorcem ruchu jest dawny krok 9 („animacje w ostatnim kroku wygladaja
# swietnie, mozesz stosowac podobne do reszty krokow"): podswietlenie na wykresie
# -> rzut kreskowany na os -> zielony pas z wlasciwymi koncami -> pas zamienia
# sie w zapis przedzialu. Ten sam schemat idzie teraz przez wszystkie cztery
# czesci, z roznica w tym, co jest podswietlane.
#
# Uklad sceny:
#   - LEWA polowa kadru: uklad wspolrzednych z wykresem, odwzorowany z arkusza
#     (matura/2024-grudzien/media/zad10/zad10rys.png): ten sam fiolet, ten sam
#     podpis y = f(x), kolko otwarte w (-4, 3) i kropka pelna w (4, 1).
#     Zakres osi y jest wezszy niz w arkuszu (-2 do 4 zamiast -5 do 5), bo kadr
#     16:9 jest niski. Jednostki na obu osiach sa rowne, wiec ksztalt sie zgadza.
#   - PRAWA polowa: naglowek biezacej czesci u gory, a pod nim lista odpowiedzi,
#     ktora rosnie do czterech pozycji.
#
# Wykres, os, siatka i lista wynikow to SCENOGRAFIA: stoja przez caly film.
# Kazdy krok dokłada tylko to, co w nim zielone.
#
# Kolor: zielone = to, na co uczen ma w tym kroku patrzec (COLORS.md, rola
# "oznaczenie miejsca"). Wykres zostaje fioletowy (#7a3fa8, rola "wykres
# funkcji jak w arkuszach CKE"), osie i siatka szare.
#
# Render: manim --save_sections solutionZad10.py Zad10  (albo tools/wgraj-kroki.sh 10)

ZIELONY = "#2e7d32"
FIOLET = "#7a3fa8"
SZARY_OSIE = "#666666"
SZARY_SIATKA = "#e0e0e0"

SRODEK_WYKRESU = LEFT * 3.35 + DOWN * 0.35
KOLUMNA_X = 3.9
ETYKIETA_Y = 3.15
LISTA_Y = 1.3
LISTA_KROK = 0.95
LISTA_LEWO = 2.35

# Postoj na koncu kroku. Przy wykresie 0,25 s nie wystarcza: cienka krzywa
# i siatka to duzo drobnego szczegolu, wiec koder potrzebuje kilku klatek
# bezruchu, zeby ostatnia klatka kroku zgadzala sie z pierwsza klatka
# nastepnego (manimations/README.md, punkt 47).
POSTOJ = 0.45


class Zad10(Scene):

    # ---- klocki -------------------------------------------------------

    def etykieta(self, tekst):
        t = Text(tekst, font_size=34, color=BLACK)
        t.move_to([KOLUMNA_X, ETYKIETA_Y, 0])
        return t

    def zgas(self, *mobiekty, czas=0.4):
        """Gasi zielone na czarno. Wolane PRZED koncowym postojem, zeby
        ostatnia klatka kroku byla czysta (README, punkt 1 zasad)."""
        if mobiekty:
            self.play(*[m.animate.set_color(BLACK) for m in mobiekty], run_time=czas)

    def construct(self):
        # ================================================================
        # SCENOGRAFIA
        # ================================================================
        plansza = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-2, 4, 1],
            x_length=7.4,
            y_length=4.44,
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
        for x in (-4, -2, 1, 2, 3, 4):
            n = MathTex(str(x), color=SZARY_OSIE, font_size=30)
            n.next_to(p(x, 0), DOWN, buff=0.30)
            liczby.add(n)
        for y in (-1, 1, 3):
            n = MathTex(str(y), color=SZARY_OSIE, font_size=30)
            n.next_to(p(0, y), LEFT, buff=0.28)
            liczby.add(n)
        os_x_podpis = MathTex("x", color=SZARY_OSIE, font_size=34)
        os_x_podpis.next_to(p(5, 0), DOWN + RIGHT, buff=0.06)
        os_y_podpis = MathTex("y", color=SZARY_OSIE, font_size=34)
        os_y_podpis.next_to(p(0, 4), UP + LEFT, buff=0.06)
        liczby.add(os_x_podpis, os_y_podpis)

        wykres = VMobject(color=FIOLET, stroke_width=6)
        wykres.set_points_as_corners([p(-4, 3), p(-2, 3), p(2, -1), p(4, 1)])

        koniec_otwarty = Circle(
            radius=0.09, color=FIOLET, stroke_width=5,
            fill_color=WHITE, fill_opacity=1,
        ).move_to(p(-4, 3))
        koniec_pelny = Dot(p(4, 1), radius=0.09, color=FIOLET)

        podpis_f = MathTex("y = f(x)", color=FIOLET, font_size=40)
        podpis_f.move_to(p(2.5, 2.6))

        def pozycja_listy(nr, wzor):
            g = VGroup(
                MathTex(f"{nr}.", color=BLACK, font_size=40),
                MathTex(wzor, color=BLACK, font_size=40),
            ).arrange(RIGHT, buff=0.22)
            g.move_to([KOLUMNA_X, LISTA_Y - (nr - 1) * LISTA_KROK, 0])
            g.shift(RIGHT * (LISTA_LEWO - g.get_left()[0]))
            return g

        def kropka_otwarta(gdzie, kolor=ZIELONY):
            return Circle(
                radius=0.09, color=kolor, stroke_width=5,
                fill_color=WHITE, fill_opacity=1,
            ).move_to(gdzie)

        def duch(wzorzec, gdzie):
            """Kopia znacznika, ktora startuje NIEWIDOCZNA. Dolozona wprost
            na oryginal robilaby podwojna krawedz juz w pierwszej klatce
            kroku, czyli rozjazd na styku (tools/styk-klatek.sh)."""
            k = wzorzec.copy().set_opacity(0).move_to(gdzie)
            self.add(k)
            return k

        def kreska(od, do):
            return DashedLine(od, do, color=ZIELONY, stroke_width=3,
                              dash_length=0.1)

        # ================================================================
        # KROK 1. Sam rysunek: uklad wspolrzednych, wykres i jego dwa konce.
        # Nic sie tu jeszcze nie odczytuje, wiec nic nie jest zielone.
        # ================================================================
        self.next_section("krok1")
        self.play(FadeIn(plansza), FadeIn(liczby), run_time=0.8)
        self.play(Create(wykres), run_time=1.6)
        self.play(
            FadeIn(koniec_otwarty), FadeIn(koniec_pelny), FadeIn(podpis_f),
            run_time=0.6,
        )
        self.wait(POSTOJ)

        # ================================================================
        # KROK 2. ZDANIE 1: dziedzina. Oba konce wykresu zjezdzaja na os x
        # i zabieraja ze soba swoj rodzaj kropki, miedzy nimi zapala sie pas,
        # a pas zamienia sie w gotowy przedzial na liscie.
        # ================================================================
        self.next_section("krok2")
        et1 = self.etykieta("1. Dziedzina")
        self.play(FadeIn(et1), run_time=0.4)

        rzut_l = kreska(p(-4, 3), p(-4, 0))
        rzut_p = kreska(p(4, 1), p(4, 0))
        self.play(Create(rzut_l), Create(rzut_p), run_time=0.8)

        kopia_o = duch(koniec_otwarty, koniec_otwarty.get_center())
        kopia_k = duch(koniec_pelny, koniec_pelny.get_center())
        self.play(
            kopia_o.animate.set_opacity(1).set_color(ZIELONY).set_fill(WHITE, 1),
            kopia_k.animate.set_opacity(1).set_color(ZIELONY),
            run_time=0.4,
        )
        self.play(
            kopia_o.animate.move_to(p(-4, 0)),
            kopia_k.animate.move_to(p(4, 0)),
            run_time=1.0,
        )
        pas1 = Line(p(-4, 0), p(4, 0), color=ZIELONY, stroke_width=8)
        self.play(Create(pas1), run_time=0.8)
        self.wait(0.3)

        poz1 = pozycja_listy(1, r"(-4,\ 4\rangle")
        self.play(
            ReplacementTransform(VGroup(pas1, kopia_o, kopia_k), poz1[1]),
            FadeIn(poz1[0]),
            FadeOut(rzut_l), FadeOut(rzut_p),
            run_time=1.2,
        )
        self.wait(POSTOJ)

        # ================================================================
        # KROK 3. ZDANIE 2: zbior wartosci. To samo, tylko rzut idzie na os y:
        # najnizszy punkt wykresu i poziomy odcinek na wysokosci 3.
        # ================================================================
        self.next_section("krok3")
        et2 = self.etykieta("2. Zbiór wartości")
        self.play(FadeOut(et1), FadeIn(et2), run_time=0.5)

        dolny = Dot(p(2, -1), radius=0.09, color=ZIELONY)
        gorny = Line(p(-4, 3), p(-2, 3), color=ZIELONY, stroke_width=8)
        self.play(FadeIn(dolny), Create(gorny), run_time=0.8)

        rzut_d = kreska(p(2, -1), p(0, -1))
        rzut_g = kreska(p(-2, 3), p(0, 3))
        self.play(Create(rzut_d), Create(rzut_g), run_time=0.8)

        kopia_d = duch(dolny, dolny.get_center())
        kopia_g = duch(Dot(p(-2, 3), radius=0.09, color=ZIELONY), p(-2, 3))
        self.play(
            kopia_d.animate.set_opacity(1).move_to(p(0, -1)),
            kopia_g.animate.set_opacity(1).move_to(p(0, 3)),
            run_time=1.0,
        )
        pas2 = Line(p(0, -1), p(0, 3), color=ZIELONY, stroke_width=8)
        self.play(Create(pas2), run_time=0.8)
        self.wait(0.3)

        poz2 = pozycja_listy(2, r"\langle -1,\ 3\rangle")
        self.play(
            ReplacementTransform(VGroup(pas2, kopia_d, kopia_g), poz2[1]),
            FadeIn(poz2[0]),
            FadeOut(rzut_d), FadeOut(rzut_g),
            FadeOut(dolny), FadeOut(gorny),
            run_time=1.2,
        )
        self.wait(POSTOJ)

        # ================================================================
        # KROK 4. ZDANIE 3: wartosci ujemne. Zapala sie fragment wykresu pod
        # osia, a jego oba konce sa PUSTE, bo w nich wartosc jest zerem.
        # ================================================================
        self.next_section("krok4")
        et3 = self.etykieta("3. Wartości ujemne")
        self.play(FadeOut(et2), FadeIn(et3), run_time=0.5)

        fragment = VMobject(color=ZIELONY, stroke_width=8)
        fragment.set_points_as_corners([p(1, 0), p(2, -1), p(3, 0)])
        self.play(Create(fragment), run_time=1.1)

        rzut_1 = kreska(p(1, 0), p(1, -0.75))
        rzut_3 = kreska(p(3, 0), p(3, -0.75))
        self.play(Create(rzut_1), Create(rzut_3), run_time=0.6)

        pas3 = Line(p(1, 0), p(3, 0), color=ZIELONY, stroke_width=8)
        pusta_l = kropka_otwarta(p(1, 0))
        pusta_p = kropka_otwarta(p(3, 0))
        self.play(Create(pas3), FadeIn(pusta_l), FadeIn(pusta_p), run_time=0.8)
        self.wait(0.3)

        poz3 = pozycja_listy(3, r"(1,\ 3)")
        self.play(
            ReplacementTransform(VGroup(pas3, pusta_l, pusta_p), poz3[1]),
            FadeIn(poz3[0]),
            FadeOut(rzut_1), FadeOut(rzut_3), FadeOut(fragment),
            run_time=1.2,
        )
        self.wait(POSTOJ)

        # ================================================================
        # KROK 5. ZDANIE 4: najwieksza wartosc. Poziom y = 3 przecina wykres
        # wzdluz calego poziomego odcinka, wiec na os x schodzi caly ten
        # odcinek: kolko otwarte w -4, kropka pelna w -2.
        # Naglowek czesci na koniec znika, zeby zostal sam wykres i cztery
        # odpowiedzi (Henrich, 2026-08-28).
        # ================================================================
        self.next_section("krok5")
        et4 = self.etykieta("4. Największa wartość")
        self.play(FadeOut(et3), FadeIn(et4), run_time=0.5)

        poziom = kreska(p(-5, 3), p(5, 3))
        podpis_poziom = MathTex("y = 3", color=ZIELONY, font_size=36)
        podpis_poziom.next_to(p(4.2, 3), UP, buff=0.1)
        self.play(Create(poziom), FadeIn(podpis_poziom), run_time=0.9)

        odcinek_max = Line(p(-4, 3), p(-2, 3), color=ZIELONY, stroke_width=8)
        self.play(Create(odcinek_max), run_time=0.7)

        rzut_a = kreska(p(-4, 3), p(-4, 0))
        rzut_b = kreska(p(-2, 3), p(-2, 0))
        self.play(Create(rzut_a), Create(rzut_b), run_time=0.8)

        pas4 = Line(p(-4, 0), p(-2, 0), color=ZIELONY, stroke_width=8)
        koniec_a = kropka_otwarta(p(-4, 0))
        koniec_b = Dot(p(-2, 0), radius=0.09, color=ZIELONY)
        self.play(Create(pas4), FadeIn(koniec_a), FadeIn(koniec_b), run_time=0.8)
        self.wait(0.3)

        poz4 = pozycja_listy(4, r"(-4,\ -2\rangle")
        self.play(
            ReplacementTransform(VGroup(pas4, koniec_a, koniec_b), poz4[1]),
            FadeIn(poz4[0]),
            FadeOut(rzut_a), FadeOut(rzut_b), FadeOut(odcinek_max),
            FadeOut(poziom), FadeOut(podpis_poziom), FadeOut(et4),
            run_time=1.2,
        )
        self.wait(POSTOJ)
