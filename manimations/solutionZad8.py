from manim import *

from _wspolne import (ZIELONY, MARGINES, PRZYTRZYMANIE, rozbij_ulamek, rozjasnij_scene,
                      zapal, zakoncz_krok)


# Zadanie 8 (otwarte, 3 pkt) — rozwiąż (x+3)/(x-1) = x/(2x-2). Wynik: x = -6.
#
# Spec i podział na kroki: issues/spec-zad8-2024-grudzien.md. Dziesięć kroków,
# jeden do jednego z dziesięcioma linijkami rachunku w rozwiązaniu opisowym.
# Sprawdzenie przez podstawienie jest TYLKO w rozwiązaniu opisowym (decyzja
# Henricha, 2026-08-27), więc filmu nie kończy.
#
# Droga: prawy mianownik to 2(x-1), mnożymy obie strony przez (x-1), skracamy
# nawias, mnożymy przez 2, zostaje równanie pierwszego stopnia. Bez delty.
#
# Stany pisane MathTeXem POCIĘTYM NA CZĘŚCI (README, punkt 19), żeby parować je
# po argumentach, a nie po zgadywanych numerach glifów: TransformMatchingTex
# łączy części o tym samym zapisie LaTeX, a reszcie robi przejście.
#
# Render: manim --save_sections solutionZad8.py Zad8
class Zad8(Scene):

    def construct(self):
        # ---- stany rachunku ----------------------------------------------
        s = [None] * 10
        s[0] = MathTex(r"\frac{x+3}{x-1}", r"=", r"\frac{x}{2x-2}")
        s[1] = MathTex(r"\frac{x+3}{x-1}", r"=", r"\frac{x}{2x-2}")
        s[2] = MathTex(r"\frac{x+3}{x-1}", r"=", r"\frac{x}{2(x-1)}")
        # Ułamków NIE tnie się na argumenty: Manim renderuje każdy argument
        # osobno i domyka klamry, więc "\frac{(x+3)" staje się "\frac{(x+3)}",
        # czyli \frac z jednym argumentem, i render pada. Uchwyty do wnętrza
        # ułamka bierzemy z glifów przez rozbij_ulamek (mapa policzona, nie
        # zgadnięta: licznik "(x+3)(x-1)" ma 10 glifów, ostatnie pięć to "(x-1)").
        s[3] = MathTex(r"\frac{(x+3)(x-1)}{x-1}", r"=", r"\frac{x(x-1)}{2(x-1)}")
        s[4] = MathTex(r"x+3", r"=", r"\frac{x}{2}")
        s[5] = MathTex(r"2", r"(x+3)", r"=", r"x")
        s[6] = MathTex(r"2x", r"+6", r"=", r"x")
        s[7] = MathTex(r"2x", r"=", r"x", r"-6")
        s[8] = MathTex(r"2x", r"-x", r"=", r"-6")
        s[9] = MathTex(r"x", r"=", r"-6")

        zalozenie = MathTex(r"x \ne 1")

        for m in s + [zalozenie]:
            m.set_color(BLACK)
            m.font_size = 100

        # ---- dopiski działań obustronnych --------------------------------
        # Nie są częścią rachunku, tylko zapowiedzią, co robimy z obiema
        # stronami, więc stoją obok i są szare (tak samo jak w rozwiązaniu
        # opisowym, klasa .rozw-dzialanie).
        def dopisek(tekst):
            d = MathTex(tekst)
            d.set_color(GREY)
            d.font_size = 72
            return d

        d_x1 = dopisek(r"\big/ \cdot (x-1)")
        d_2 = dopisek(r"\big/ \cdot 2")
        d_m6 = dopisek(r"\big/ - 6")
        d_mx = dopisek(r"\big/ - x")

        # ---- wspólna skala -----------------------------------------------
        # Jeden współczynnik dla WSZYSTKICH kroków, liczony z najszerszego
        # układu (README): inaczej litery zmieniałyby wielkość w trakcie
        # przekształcenia. Równanie stoi zawsze na środku, a dopisek wystaje
        # w prawo, więc szerokość efektywna kroku z dopiskiem liczy się
        # podwójnie od środka.
        ODSTEP = 0.9
        pary = [(s[2], d_x1), (s[4], d_2), (s[6], d_m6), (s[7], d_mx)]
        szerokosci = [m.width for m in s]
        szerokosci += [2 * (r.width / 2 + ODSTEP + d.width) for r, d in pary]
        najszerszy = max(szerokosci)
        if najszerszy > config.frame_width * MARGINES:
            wsp = config.frame_width * MARGINES / najszerszy
            for m in s + [zalozenie, d_x1, d_2, d_m6, d_mx]:
                m.scale(wsp)

        # Równanie w górnej połowie, założenie pod nim: od kroku 2 stoi w kadrze
        # do końca filmu, bo za nie jest osobny punkt w kluczu CKE.
        for m in s:
            m.move_to(UP * 0.7)
        zalozenie.move_to(DOWN * 1.9)

        # Uchwyty do nawiasów (x-1), które w kroku 4 się pojawiają, a w kroku 5
        # skracają. Liczone z glifów, po jednym wycinku na ułamek.
        lewy_licznik, _, lewy_mianownik = rozbij_ulamek(s[3][0])
        prawy_licznik, _, prawy_mianownik = rozbij_ulamek(s[3][2])
        nawias_lewy_gora = VGroup(*lewy_licznik[-5:])      # "(x-1)" w liczniku po lewej
        nawias_lewy_dol = VGroup(*lewy_mianownik)          # cały mianownik "x-1"
        nawias_prawy_gora = VGroup(*prawy_licznik[-5:])    # "(x-1)" w liczniku po prawej
        nawias_prawy_dol = VGroup(*prawy_mianownik[-5:])   # "(x-1)" w mianowniku po prawej

        def przy(rownanie, d):
            d.next_to(rownanie, RIGHT, buff=ODSTEP)
            return d

        # ---- kroki --------------------------------------------------------
        self.next_section("krok1")
        # KROK 1 — równanie z treści zadania. Bez koloru: nic się jeszcze nie dzieje.
        self.play(Write(s[0]), run_time=1.2)
        self.wait(PRZYTRZYMANIE)

        self.next_section("krok2")
        # KROK 2 — założenie. Zielone, bo pojawia się coś, czego nie było.
        zalozenie.set_color(ZIELONY)
        self.play(FadeIn(zalozenie, shift=UP * 0.3), run_time=0.9)
        zakoncz_krok(self, zalozenie)

        self.next_section("krok3")
        # KROK 3 — prawy mianownik zapisany jako 2(x-1). Zielony tylko ten ułamek,
        # bo tylko on zmienia formę; lewa strona stoi bez zmian.
        self.remove(s[0])
        self.add(s[1])
        zapal(self, na_ekranie=[s[1][2]], poza_ekranem=[s[2][2]])
        self.play(TransformMatchingTex(s[1], s[2], transform_mismatches=True), run_time=1.3)
        rozjasnij_scene(self)
        przy(s[2], d_x1)
        self.play(FadeIn(d_x1, shift=LEFT * 0.3), run_time=0.6)
        self.wait(PRZYTRZYMANIE)

        self.next_section("krok4")
        # KROK 4 — mnożymy obie strony przez (x-1). Zielone są DOPISANE nawiasy,
        # czyli dokładnie to, co się w kadrze pojawia.
        zapal(self, poza_ekranem=[nawias_lewy_gora, nawias_prawy_gora])
        self.play(
            TransformMatchingTex(s[2], s[3], transform_mismatches=True),
            FadeOut(d_x1, shift=RIGHT * 0.3),
            run_time=1.4,
        )
        rozjasnij_scene(self)

        self.next_section("krok5")
        # KROK 5 — skracamy (x-1). Zieleń idzie na to, co ZNIKA, więc zapala się
        # w stanie sprzed skrócenia, a po animacji nie ma czego gasić.
        zapal(self, na_ekranie=[nawias_lewy_gora, nawias_lewy_dol,
                                nawias_prawy_gora, nawias_prawy_dol])
        self.play(TransformMatchingTex(s[3], s[4], transform_mismatches=True), run_time=1.4)
        rozjasnij_scene(self)
        przy(s[4], d_2)
        self.play(FadeIn(d_2, shift=LEFT * 0.3), run_time=0.6)
        self.wait(PRZYTRZYMANIE)

        self.next_section("krok6")
        # KROK 6 — mnożymy przez 2: po lewej dwójka staje przed nawiasem, po
        # prawej znika z mianownika. Zielona jest ta dwójka.
        zapal(self, poza_ekranem=[s[5][0]])
        self.play(
            TransformMatchingTex(s[4], s[5], transform_mismatches=True),
            FadeOut(d_2, shift=RIGHT * 0.3),
            run_time=1.3,
        )
        rozjasnij_scene(self)

        self.next_section("krok7")
        # KROK 7 — opuszczamy nawias. Zielone jest 6, bo to nowa liczba: trójka
        # pomnożona przez dwójkę.
        zapal(self, poza_ekranem=[s[6][1]])
        self.play(TransformMatchingTex(s[5], s[6], transform_mismatches=True), run_time=1.3)
        rozjasnij_scene(self)
        przy(s[6], d_m6)
        self.play(FadeIn(d_m6, shift=LEFT * 0.3), run_time=0.6)
        self.wait(PRZYTRZYMANIE)

        self.next_section("krok8")
        # KROK 8 — szóstka przechodzi na prawo i zmienia znak. Zielona jest ona
        # po obu stronach przejścia, bo to ona się zmienia.
        zapal(self, na_ekranie=[s[6][1]], poza_ekranem=[s[7][3]])
        self.play(
            TransformMatchingTex(s[6], s[7], transform_mismatches=True),
            FadeOut(d_m6, shift=RIGHT * 0.3),
            run_time=1.3,
        )
        rozjasnij_scene(self)
        przy(s[7], d_mx)
        self.play(FadeIn(d_mx, shift=LEFT * 0.3), run_time=0.6)
        self.wait(PRZYTRZYMANIE)

        self.next_section("krok9")
        # KROK 9 — to samo z iksem: przechodzi na lewo i zmienia znak.
        zapal(self, na_ekranie=[s[7][2]], poza_ekranem=[s[8][1]])
        self.play(
            TransformMatchingTex(s[7], s[8], transform_mismatches=True),
            FadeOut(d_mx, shift=RIGHT * 0.3),
            run_time=1.3,
        )
        rozjasnij_scene(self)

        self.next_section("krok10")
        # KROK 10 — dwa iksy bez jednego iksa to jeden iks. Wynik.
        zapal(self, na_ekranie=[s[8][0], s[8][1]], poza_ekranem=[s[9][0]])
        self.play(TransformMatchingTex(s[8], s[9], transform_mismatches=True), run_time=1.3)
        rozjasnij_scene(self)
