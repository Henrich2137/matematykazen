from manim import *

# Zadanie 23 (zamkniete, 1 pkt). Cztery okregi o1..o4, szukamy tego bez
# zadnego punktu wspolnego z osiami ukladu. Wynik: o3, odpowiedz C.
#
# Projekt: issues/projekt-zad22-zad23-2024-grudzien.md. To zadanie SPRAWDZA,
# a nie liczy jedna sciezka: jeden okrag = jeden krok (README, zasada 42,
# "jednostka kroku jest jedna mysl"), a nie jeden krok na kazde porownanie.
#
# Dane (S = srodek, r = promien):
#   o1: S=(1,2),   r=1  -> |a|=1=r (styczny do Oy)
#   o2: S=(-1,-2), r=3  -> |a|=1<3, |b|=2<3 (przecina obie osie)
#   o3: S=(3,4),   r=2  -> |a|=3>2, |b|=4>2 (brak punktu wspolnego) - ODPOWIEDZ
#   o4: S=(-3,-4), r=4  -> |a|=3<4 (przecina Oy), |b|=4=4 (styczny do Ox)
#
# Regula "|a|>r i |b|>r" NIE stoi w tablicy jako gotowy wzor (to wniosek
# z [11.11], rownania okregu), wiec idzie zdaniem, nie w ramce (README, zasada 3).
#
# Uklad kadru: LEWA polowa - jeden wspolny uklad z czterema okregami (czarne,
# podpisane), kazdy z mala szara etykieta S i r obok. PRAWA polowa: regula na
# gorze (zostaje przez caly film), pas sprawdzania biezacego okregu na srodku,
# odpowiedz na dole.
#
# Render: manim --save_sections solutionZad23.py Zad23  (albo tools/wgraj-kroki.sh 23)

ZIELONY = "#2e7d32"
SZARY_OSIE = "#666666"
SZARY_DANE = "#666666"

SRODEK_WYKRESU = LEFT * 4.05 + DOWN * 0.10
KOLUMNA_X = 3.30
REGULA_Y = 3.05
SPRAWDZ_Y = 0.15
ODPOWIEDZ_Y = -2.55

# Skala ukladu: x_range i y_range maja rozpietosc 16, x_length=y_length=5.4,
# wiec 1 jednostka danych = 5.4/16 jednostki sceny. Kwadratowy uklad jest
# tu wazny - to jedyna scena z okregami, a niesymetryczna skala zrobilaby
# z nich elipsy.
JEDNOSTKA = 5.4 / 16


class Zad23(Scene):

    # ---- klocki -------------------------------------------------------

    def stan(self, *args, rozmiar=44, kolor=BLACK):
        m = MathTex(*args)
        m.set_color(kolor)
        m.font_size = rozmiar
        return m

    def zgas(self, *mobiekty, czas=0.4):
        if mobiekty:
            self.play(*[m.animate.set_color(BLACK) for m in mobiekty], run_time=czas)

    def przywolaj(self, zrodla, cele, czas=0.9, luk=-PI / 4):
        """Kopie przylatuja z etykiety okregu na rysunku, nie z niczego
        (README, punkty 37-38)."""
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

    def construct(self):
        # ================================================================
        # SCENOGRAFIA: uklad wspolrzednych i cztery okregi
        # ================================================================
        plansza = NumberPlane(
            x_range=[-8, 8, 2],
            y_range=[-8, 8, 2],
            x_length=5.4,
            y_length=5.4,
            background_line_style={
                "stroke_color": "#e0e0e0",
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

        os_x = MathTex("x", color=SZARY_OSIE, font_size=32)
        os_x.next_to(p(8, 0), DOWN + RIGHT, buff=0.04)
        os_y = MathTex("y", color=SZARY_OSIE, font_size=32)
        os_y.next_to(p(0, 8), UP + LEFT, buff=0.04)

        DANE = [
            {"nr": 1, "a": 1, "b": 2, "r": 1, "znak_a": "=", "znak_b": None,
             "wynik": "styczny do osi Oy"},
            {"nr": 2, "a": -1, "b": -2, "r": 3, "znak_a": "<", "znak_b": "<",
             "wynik": "przecina obie osie"},
            {"nr": 3, "a": 3, "b": 4, "r": 2, "znak_a": ">", "znak_b": ">",
             "wynik": "brak punktu wspólnego"},
            {"nr": 4, "a": -3, "b": -4, "r": 4, "znak_a": "<", "znak_b": "=",
             "wynik": "przecina Oy, styka Ox"},
        ]

        okregi = {}
        etykiety_srodka = {}
        for d in DANE:
            srodek = p(d["a"], d["b"])
            okrag = Circle(radius=d["r"] * JEDNOSTKA, color=BLACK, stroke_width=4)
            okrag.move_to(srodek)
            nazwa = MathTex(f"o_{{{d['nr']}}}", color=BLACK, font_size=32)
            # Etykieta nazwy siedzi ZAWSZE nad okregiem (kierunek staly, nie
            # zalezny od cwiartki), zeby przy skrajnych okregach (o2, o4) nie
            # wyjezdzac poza kadr - zlapane pierwszym renderem.
            nazwa.next_to(okrag, UP, buff=0.08)
            okregi[d["nr"]] = okrag
            etykiety_srodka[d["nr"]] = nazwa

        # ================================================================
        # PRAWA POLOWA: regula (zostaje przez caly film) i odpowiedz
        # ================================================================
        regula_tekst = Text(
            "Okrąg nie ma punktu wspólnego\nz żadną osią, gdy:",
            font_size=26, color=BLACK, line_spacing=1.15,
        )
        regula_wzor = self.stan(r"|a|>r", r"\ \text{i}\ ", r"|b|>r", rozmiar=38)
        regula = VGroup(regula_tekst, regula_wzor).arrange(DOWN, buff=0.24)
        regula.move_to([KOLUMNA_X, REGULA_Y, 0])

        odpowiedz = VGroup(
            Text("Odpowiedź", font_size=34, color=BLACK),
            Text("C", font_size=38, weight=BOLD, color=BLACK),
        ).arrange(RIGHT, buff=0.26)
        odpowiedz.move_to([KOLUMNA_X, ODPOWIEDZ_Y, 0])

        # ================================================================
        # KROK 1. Rysunek: uklad, cztery okregi czarne, podpisane, z mala
        # etykieta danych obok kazdego. Regula. Cale czarne/szare.
        # ================================================================
        self.next_section("krok1")
        self.play(FadeIn(plansza), FadeIn(os_x), FadeIn(os_y), run_time=0.8)
        for d in DANE:
            nr = d["nr"]
            self.play(Create(okregi[nr]), run_time=0.6)
            self.play(FadeIn(etykiety_srodka[nr]), run_time=0.3)
        self.play(FadeIn(regula), run_time=0.8)
        self.wait(0.45)

        # ================================================================
        # KROKI 2-5. Jeden okrag na krok: podswietlenie (TYLKO kolor, nie
        # grubosc - README punkt 46), dane wjezdzaja przy okregu i lecą stamtad
        # do pasa sprawdzania, porownanie, werdykt. Kandydat (o3) zostaje
        # zielony, reszta gasnie na czarno.
        # ================================================================
        for d in DANE:
            nr = d["nr"]
            self.next_section(f"krok{nr + 1}")

            self.play(okregi[nr].animate.set_color(ZIELONY),
                      etykiety_srodka[nr].animate.set_color(ZIELONY), run_time=0.5)

            dane_okrag = self.stan(
                f"S=({d['a']},\\ {d['b']})", ",\\ ", f"r={d['r']}",
                rozmiar=24, kolor=SZARY_DANE,
            )
            dane_okrag.next_to(etykiety_srodka[nr], UP, buff=0.06)
            self.play(FadeIn(dane_okrag), run_time=0.4)
            self.wait(0.2)

            dane_pas = self.stan(f"S=({d['a']},\\ {d['b']})", ",\\ ",
                                 f"r={d['r']}", rozmiar=34)
            dane_pas.move_to([KOLUMNA_X, SPRAWDZ_Y + 0.85, 0])
            kopie = self.przywolaj(
                [dane_okrag], [dane_pas.get_center()], luk=PI / 4,
            )
            self.play(FadeOut(kopie[0]), FadeOut(dane_okrag), FadeIn(dane_pas),
                      run_time=0.3)
            self.wait(0.2)

            por_a = self.stan(f"|{d['a']}|", d["znak_a"], f"{d['r']}", rozmiar=36)
            linie = [por_a]
            if d["znak_b"] is not None:
                por_b = self.stan(f"|{d['b']}|", d["znak_b"], f"{d['r']}", rozmiar=36)
                linie.append(por_b)
            porownania = VGroup(*linie).arrange(DOWN, buff=0.22)
            porownania.move_to([KOLUMNA_X, SPRAWDZ_Y - 0.15, 0])
            for linia in linie:
                linia.set_color(ZIELONY)
            self.play(FadeIn(porownania), run_time=0.6)
            self.wait(0.3)
            self.zgas(*linie)

            werdykt = Text(d["wynik"], color=BLACK, font_size=26)
            werdykt.move_to([KOLUMNA_X, SPRAWDZ_Y - 1.15, 0])
            self.play(FadeIn(werdykt), run_time=0.5)
            self.wait(0.35)

            znika = [dane_pas, porownania, werdykt]
            if nr == 3:
                # o3 zostaje zielony - to kandydat na odpowiedz.
                self.play(*[FadeOut(m) for m in znika], run_time=0.4)
            else:
                self.play(
                    okregi[nr].animate.set_color(BLACK),
                    etykiety_srodka[nr].animate.set_color(BLACK),
                    *[FadeOut(m) for m in znika],
                    run_time=0.4,
                )
            self.wait(0.45)

        # ================================================================
        # KROK 6. o3 zostaje jedynym zielonym okregiem, pada odpowiedz.
        # ================================================================
        self.next_section("krok6")
        self.play(FadeIn(odpowiedz), run_time=0.6)
        self.wait(0.45)
