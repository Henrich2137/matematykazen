from manim import *

from _wspolne import (CZERWONY, ZIELONY, PRZYTRZYMANIE,
                      ustaw_kroki, rozbij_ulamek, zapal, zakoncz_krok)


# Zadanie 6 — (x/(x^2-1)) : (3x^2/(x+1)) = 1/(3x^2-3x), odpowiedź B.
#
# Scenariusz kroków jest w manimations/zad6-kroki.md.
#
# PRZEPISANE 2026-08-12 po zgłoszeniu Henricha (to samo co w zad. 5: automatyczne
# parowanie kształtów przez TransformMatchingShapes rozsypywało zapis).
# Dwie zmiany względem pierwszej wersji:
#   • każda para „skąd → dokąd" wypisana wprost, a ułamki trzymane jako osobne
#     mobiekty, żeby dało się przenieść licznik pod kreskę i odwrotnie,
#   • skracanie rozbite na DWA kroki (najpierw (x+1), potem x z x^2). W jednym
#     kroku działy się cztery rzeczy naraz i nie dało się tego pokazać uczciwie.
#     Przez to kroków jest siedem, a nie sześć.
#
# Render: manim --save_sections solutionZad6.py Zad6
class Zad6(Scene):

    def construct(self):
        R = 96  # wspólny rozmiar pisma

        def wiersz(*czesci):
            return VGroup(*czesci).arrange(RIGHT, buff=0.28)

        # --- kolejne stany zapisu, każdy z osobnymi uchwytami do ułamków -----
        lewy0 = MathTex(r"\frac{x}{x^{2}-1}", font_size=R)
        znak0 = MathTex(r":", font_size=R)
        prawy0 = MathTex(r"\frac{3x^{2}}{x+1}", font_size=R)
        k0 = wiersz(lewy0, znak0, prawy0)

        lewy1 = MathTex(r"\frac{x}{(x-1)(x+1)}", font_size=R,
                        substrings_to_isolate=["(x-1)", "(x+1)"])
        znak1 = MathTex(r":", font_size=R)
        prawy1 = MathTex(r"\frac{3x^{2}}{x+1}", font_size=R)
        k1 = wiersz(lewy1, znak1, prawy1)

        lewy2 = MathTex(r"\frac{x}{(x-1)(x+1)}", font_size=R,
                        substrings_to_isolate=["(x-1)", "(x+1)"])
        znak2 = MathTex(r"\cdot", font_size=R)
        prawy2 = MathTex(r"\frac{x+1}{3x^{2}}", font_size=R)
        k2 = wiersz(lewy2, znak2, prawy2)

        lewy3 = MathTex(r"\frac{x}{x-1}", font_size=R)
        znak3 = MathTex(r"\cdot", font_size=R)
        prawy3 = MathTex(r"\frac{1}{3x^{2}}", font_size=R)
        k3 = wiersz(lewy3, znak3, prawy3)

        lewy4 = MathTex(r"\frac{1}{x-1}", font_size=R)
        znak4 = MathTex(r"\cdot", font_size=R)
        prawy4 = MathTex(r"\frac{1}{3x}", font_size=R)
        k4 = wiersz(lewy4, znak4, prawy4)

        k5 = MathTex(r"\frac{1}{3x(x-1)}", font_size=R,
                     substrings_to_isolate=["3x", "(x-1)"])
        k6 = MathTex(r"\frac{1}{3x^{2}-3x}", font_size=R)

        ustaw_kroki([k0, k1, k2, k3, k4, k5, k6], rozmiar=None)

        # Rozbicia ułamków na licznik / kreskę / mianownik — po nich chodzą
        # wszystkie przejścia.
        licz_l0, kres_l0, mian_l0 = rozbij_ulamek(lewy0[0])
        licz_p1, kres_p1, mian_p1 = rozbij_ulamek(prawy1[0])
        licz_p2, kres_p2, mian_p2 = rozbij_ulamek(prawy2[0])
        licz_l3, kres_l3, mian_l3 = rozbij_ulamek(lewy3[0])
        licz_p3, kres_p3, mian_p3 = rozbij_ulamek(prawy3[0])
        licz_l4, kres_l4, mian_l4 = rozbij_ulamek(lewy4[0])
        licz_p4, kres_p4, mian_p4 = rozbij_ulamek(prawy4[0])
        licz_5, kres_5, _ = rozbij_ulamek(VGroup(*[g for cz in k5 for g in cz]))
        licz_6, kres_6, mian_6 = rozbij_ulamek(k6[0])

        # W zapisie z isolate: [0] = licznik z kreską, [1] = (x-1), [2] = (x+1).
        gora_l1, xm1_l1, xp1_l1 = lewy1[0], lewy1[1], lewy1[2]
        gora_l2, xm1_l2, xp1_l2 = lewy2[0], lewy2[1], lewy2[2]
        trzy_x_5, xm1_5 = k5.get_part_by_tex("3x"), k5.get_part_by_tex("(x-1)")

        self.next_section("krok1")
        # KROK 1 — wyrażenie z zadania.
        self.play(Write(k0), run_time=1.6)
        zakoncz_krok(self)

        self.next_section("krok2")
        # KROK 2 — x^2-1 rozkłada się na (x-1)(x+1). Na zielono sam mianownik,
        # bo tylko on się zmienia.
        zapal(self, na_ekranie=[mian_l0], poza_ekranem=[xm1_l1, xp1_l1])
        self.play(
            Transform(VGroup(licz_l0, kres_l0), gora_l1),   # x nad kreską zostaje
            FadeTransform(mian_l0, VGroup(xm1_l1, xp1_l1)),  # x^2-1 → (x-1)(x+1)
            Transform(znak0, znak1),
            Transform(prawy0, prawy1),
            run_time=1.6,
        )
        zakoncz_krok(self, xm1_l1, xp1_l1)
        self.clear()
        self.add(k1)

        self.next_section("krok3")
        # KROK 3 — dzielenie zamieniamy na mnożenie przez odwrotność. Prawy ułamek
        # staje na głowie: 3x^2 schodzi POD kreskę, a (x+1) wchodzi NAD nią.
        zapal(self, na_ekranie=[licz_p1, mian_p1], poza_ekranem=[licz_p2, mian_p2])
        self.play(
            Transform(lewy1, lewy2),
            Transform(znak1, znak2),                 # dwukropek → kropka
            Transform(licz_p1, mian_p2),             # 3x^2 w dół
            Transform(mian_p1, licz_p2),             # x+1 w górę
            Transform(kres_p1, kres_p2),
            run_time=1.7,
        )
        zakoncz_krok(self, licz_p2, mian_p2)
        self.clear()
        self.add(k2)

        self.next_section("krok4")
        # KROK 4 — skracamy (x+1). Najpierw je przekreślamy, tak jak na kartce,
        # dopiero potem znikają. Czerwień, bo to znikanie, nie zmiana.
        kreska_a = Line(xp1_l2.get_corner(DL), xp1_l2.get_corner(UR), color=CZERWONY, stroke_width=6)
        kreska_b = Line(licz_p2.get_corner(DL), licz_p2.get_corner(UR), color=CZERWONY, stroke_width=6)
        self.play(Create(kreska_a), Create(kreska_b), run_time=0.7)
        self.wait(0.3)
        self.play(
            FadeOut(VGroup(xp1_l2, kreska_a), scale=0.4),
            FadeOut(VGroup(licz_p2, kreska_b), scale=0.4),
            # Zostaje x/(x-1). Nawiasy wokół (x-1) przestają być potrzebne, więc
            # przenosimy tylko środek; przeniesienie całej piątki glifów na
            # trzyglifowy cel nakładało znaki na siebie.
            Transform(gora_l2, VGroup(licz_l3, kres_l3)),
            Transform(xm1_l2[1:4], mian_l3),
            FadeOut(xm1_l2[0], xm1_l2[4], scale=0.3),
            Transform(znak2, znak3),
            Transform(mian_p2, mian_p3),                 # 3x^2 zostaje
            Transform(kres_p2, kres_p3),
            FadeIn(licz_p3),                             # w liczniku zostaje 1
            run_time=1.6,
        )
        zakoncz_krok(self)
        self.clear()
        self.add(k3)

        self.next_section("krok5")
        # KROK 5 — skracamy x z x^2. Z licznika po lewej znika x, a po prawej
        # z x^2 zostaje samo x. Na zielono oba miejsca, bo to jedno skrócenie.
        zapal(self, na_ekranie=[licz_l3, mian_p3], poza_ekranem=[licz_l4, mian_p4])
        self.play(
            Transform(licz_l3, licz_l4),      # x → 1
            Transform(kres_l3, kres_l4),
            Transform(mian_l3, mian_l4),
            Transform(znak3, znak4),
            Transform(licz_p3, licz_p4),
            Transform(kres_p3, kres_p4),
            Transform(mian_p3, mian_p4),      # 3x^2 → 3x
            run_time=1.6,
        )
        zakoncz_krok(self, licz_l4, mian_p4)
        self.clear()
        self.add(k4)

        self.next_section("krok6")
        # KROK 6 — mnożenie ułamków: licznik przez licznik, mianownik przez
        # mianownik. Dwa ułamki zlewają się w jeden.
        self.play(
            Transform(VGroup(licz_l4, licz_p4), licz_5),
            Transform(VGroup(kres_l4, kres_p4), kres_5),
            Transform(mian_l4, xm1_5),        # (x-1) idzie na PRAWO od 3x
            Transform(mian_p4, trzy_x_5),
            FadeOut(znak4, scale=0.3),
            run_time=1.7,
        )
        zakoncz_krok(self)
        self.clear()
        self.add(k5)

        self.next_section("krok7")
        # KROK 7 — wymnażamy mianownik. Zapis dokładnie taki jak w odpowiedzi B.
        zapal(self, na_ekranie=[trzy_x_5, xm1_5], poza_ekranem=[mian_6])
        self.play(
            Transform(licz_5, licz_6),
            Transform(kres_5, kres_6),
            FadeTransform(VGroup(trzy_x_5, xm1_5), mian_6),
            run_time=1.6,
        )
        zakoncz_krok(self, mian_6)
