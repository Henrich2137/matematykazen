from manim import *

# Zadanie 12.2 (wybor dwoch odpowiedzi, 2 pkt). Parabola o wierzcholku (3, 0)
# przechodzaca przez (0, -9). Wynik: f(x) = -(x-3)^2 = -x^2 + 6x - 9, czyli B i D.
#
# Projekt: issues/projekt-zad11-zad12-2024-grudzien.md. Czternascie krokow.
#
# WERSJA DRUGA, 2026-08-30, po uwagach Henricha:
#   - krok 1 pokazuje TROJKE danych naraz: wzor postaci kanonicznej, punkt W
#     i punkt A. Wczesniej wzor wjezdzal dopiero w kroku 2, wiec pierwszy krok
#     nie mial czego dotyczyc;
#   - punkt (0, -9) nazywa sie teraz A i tak stoi w kadrze; zapis f(0) = -9
#     dopisuje sie dopiero w kroku podstawienia, jako tlumaczenie „przechodzi
#     przez punkt A" na jezyk rownania;
#   - po policzeniu a = -1 GORA KADRU SIE CZYSCI (znikaja W, A, dopisek i pas
#     odczytu), a sam wynik jedzie na srodek na ich miejsce. Do tej pory caly
#     ten material wisial do konca filmu i przeszkadzal;
#   - wzor na kwadrat roznicy wjezdza JUZ NA KONCU poprzedniego kroku, wiec
#     krok z rozwijaniem nawiasu zaczyna sie od rachunku, a nie od wjazdu wzoru;
#   - lista odpowiedzi to „Odpowiedzi: B, D", z przecinkiem zamiast spojnika;
#   - ostatni krok zdejmuje a = -1 i zostawia w kadrze OBIE postaci wzoru,
#     jedna pod druga: to jest cala odpowiedz na pytanie zadania.
#
# Sedno zadania: B i D to TEN SAM wzor, raz zwiniety, raz rozwiniety. Dlatego
# rozwiazanie nie konczy sie na -(x-3)^2, tylko jedzie dalej i rozwija nawias.
# Litera B zapala sie w kroku 10, litera D w kroku 13, a krok 14 stawia obie
# postaci obok siebie.
#
# Uklad kadru (README, punkt 35: trzy pasy, zawsze te same):
#   - u gory dane z tresci: W = (3, 0) oraz A = (0, -9), najmniejszym pismem,
#   - pod nimi pas odczytu: p = 3, q = 0 (README, punkt 41: odczyt jest MNIEJSZY
#     od rachunku, bo to notatka z boku, a nie kolejna linijka),
#   - pas wzoru z tablicy, zajety w krokach 10 i 11 (kwadrat roznicy),
#   - w srodku glowny rachunek,
#   - na dole rosnaca lista wybranych odpowiedzi.
#
# Kazda liczba wchodzaca do wzoru PRZYLATUJE stamtad, gdzie zostala odczytana
# (README, punkty 37 i 38), a nie pojawia sie znikad.
#
# Kolor: zielone = to, co sie w danym kroku ZMIENIA. Litery B i D sa czarne:
# to odpowiedz ucznia, nie ocena poprawnosci (COLORS.md).
#
# Render: manim --save_sections solutionZad12_2.py Zad12_2

ZIELONY = "#2e7d32"
SZARY_DOPISEK = "#888888"

DANE_Y = 3.15
DOPISEK_Y = 2.45     # f(0) = -9, tuz pod punktem A i w jego kolumnie
PAS_Y = 1.9          # p i q; nizej niz dopisek, zeby nie czytaly sie jednym ciagiem
A_GORA_Y = 2.75      # gdzie staje a = -1 po sprzatnieciu gory kadru
WZOR_Y = 1.15
RACHUNEK_Y = -0.55
PODSUM_G_Y = 0.3     # postac kanoniczna w podsumowaniu
PODSUM_D_Y = -1.3    # postac ogolna w podsumowaniu
ODP_Y = -2.9
POSTOJ = 0.35


class Zad12_2(Scene):

    def stan(self, *args, rozmiar=86):
        m = MathTex(*args)
        m.set_color(BLACK)
        m.font_size = rozmiar
        return m

    def zapal(self, *mobiekty, czas=0.35):
        if mobiekty:
            self.play(*[m.animate.set_color(ZIELONY) for m in mobiekty],
                      run_time=czas)

    def zgas(self, *mobiekty, czas=0.4):
        if mobiekty:
            self.play(*[m.animate.set_color(BLACK) for m in mobiekty], run_time=czas)

    def construct(self):
        # ================================================================
        # DANE, PAS ODCZYTU, WZOR
        # ================================================================
        dane_w = self.stan("W", "=", "(", "3", ",\\ ", "0", ")", rozmiar=46)
        dane_a = self.stan("A", "=", "(", "0", ",\\ ", "-9", ")", rozmiar=46)
        dane_w.move_to([-3.3, DANE_Y, 0])
        dane_a.move_to([3.6, DANE_Y, 0])

        # Tlumaczenie „wykres przechodzi przez A" na jezyk rownania. Dopisuje
        # sie POD punktem A i dopiero w kroku, w ktorym jest potrzebne.
        dopisek_f0 = self.stan("f", "(", "0", ")", "=", "-9", rozmiar=46)
        dopisek_f0.set_color(SZARY_DOPISEK)
        # Wlasny wiersz POD punktem A, w tej samej kolumnie. Postawiony na
        # wysokosci pasa odczytu dotykal „q = 0" i cala gora czytala sie jako
        # jedna dluga linijka (zlapane na klatkach 2026-08-30).
        dopisek_f0.move_to([3.6, DOPISEK_Y, 0])

        # Pas odczytu trzyma TYLKO p i q. Wspolczynnik a nie dolacza do pasa:
        # po policzeniu zajmuje srodek sprzatnietej gory kadru (krok 8).
        p_cz = self.stan("p", "=", "3", rozmiar=58)
        q_cz = self.stan("q", "=", "0", rozmiar=58)
        pas = VGroup(p_cz, q_cz).arrange(RIGHT, buff=1.30)
        pas.move_to([0, PAS_Y, 0])

        wzor10 = self.stan("(", "a", "-", "b", ")", "^{2}", "=",
                           "a", "^{2}", "-", "2", "a", "b", "+", "b", "^{2}",
                           rozmiar=58)
        wzor10.move_to([0, WZOR_Y, 0])

        # ================================================================
        # STANY RACHUNKU, po jednym na krok
        # ================================================================
        s2lit = self.stan("f", "(", "x", ")", "=", "a",
                          "(", "x", "-", "p", ")", "^{2}", "+", "q")
        s2 = self.stan("f", "(", "x", ")", "=", "a",
                       "(", "x", "-", "3", ")", "^{2}", "+", "0")
        s3 = self.stan("f", "(", "x", ")", "=", "a",
                       "(", "x", "-", "3", ")", "^{2}")
        s4 = self.stan("-9", "=", "a", "(", "0", "-", "3", ")", "^{2}")
        s5 = self.stan("-9", "=", "a", "(", "-3", ")", "^{2}")
        s6 = self.stan("-9", "=", "a", r"\cdot", "9")
        dop6 = self.stan(r"\big/", ":", "9", rozmiar=62)
        dop6.set_color(SZARY_DOPISEK)
        s7 = self.stan("a", "=", "-1")
        s3b = self.stan("f", "(", "x", ")", "=", "a",
                        "(", "x", "-", "3", ")", "^{2}")
        s8 = self.stan("f", "(", "x", ")", "=", "-1", r"\cdot",
                       "(", "x", "-", "3", ")", "^{2}")
        s9 = self.stan("f", "(", "x", ")", "=", "-",
                       "(", "x", "-", "3", ")", "^{2}")
        s10 = self.stan("f", "(", "x", ")", "=", "-", "(",
                        "x", "^{2}", "-", "2", r"\cdot", "x", r"\cdot", "3",
                        "+", "3", "^{2}", ")")
        s11 = self.stan("f", "(", "x", ")", "=", "-", "(",
                        "x", "^{2}", "-", "6", "x", "+", "9", ")")
        s12 = self.stan("f", "(", "x", ")", "=",
                        "-", "x", "^{2}", "+", "6", "x", "-", "9")
        # Postac kanoniczna wraca w ostatnim kroku, obok postaci ogolnej.
        podsum_b = self.stan("f", "(", "x", ")", "=", "-",
                             "(", "x", "-", "3", ")", "^{2}")

        # Wspolna skala liczona z najszerszego kroku, zeby litery nie zmienialy
        # wielkosci w trakcie przeksztalcenia (README, workflow).
        MARGINES = 0.85
        glowne = [s2lit, s2, s3, s4, s5, s6, s7, s3b, s8, s9, s10, s11, s12,
                  podsum_b]
        POLE = config.frame_width * MARGINES
        wsp = min(1.0, POLE / max(m.width for m in glowne))
        for m in glowne + [dop6]:
            m.scale(wsp)
        for m in glowne:
            m.move_to([0, RACHUNEK_Y, 0])
        podsum_b.move_to([0, PODSUM_G_Y, 0])

        # ================================================================
        # LISTA WYBRANYCH ODPOWIEDZI
        # ================================================================
        # „Odpowiedzi: B, D" (Henrich, 2026-08-30 — bylo „Wybieramy: B i D").
        # Caly napis ustawiamy z gory i dopiero odslaniamy po kawalku, zeby
        # dopisanie „, D" w ostatnim kroku nie przesuwalo tego, co juz stoi.
        etykieta_odp = Text("Odpowiedzi:", font_size=34, color=BLACK)
        litera_b = Text("B", font_size=42, weight=BOLD, color=BLACK)
        przecinek = Text(",", font_size=34, color=BLACK)
        litera_d = Text("D", font_size=42, weight=BOLD, color=BLACK)
        odp = VGroup(etykieta_odp, litera_b, przecinek, litera_d)
        odp.arrange(RIGHT, buff=0.26)
        przecinek.next_to(litera_b, RIGHT, buff=0.05)
        przecinek.align_to(litera_b, DOWN)
        litera_d.next_to(przecinek, RIGHT, buff=0.28)
        litera_d.align_to(litera_b, DOWN)
        odp.move_to([0, ODP_Y, 0])

        def przywolaj(zrodla, cele, czas=1.0, luk=-PI / 4):
            """Kopie odczytanych wartosci leca na miejsca liter we wzorze."""
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
        # KROK 1. Trojka danych naraz: wzor postaci kanonicznej i dwa punkty
        # z tresci. Nic sie jeszcze nie liczy, wiec nic nie jest zielone.
        # ================================================================
        self.next_section("krok1")
        self.play(FadeIn(s2lit), run_time=0.9)
        self.play(FadeIn(dane_w), FadeIn(dane_a), run_time=0.8)
        self.wait(POSTOJ)

        # ================================================================
        # KROK 2. Wierzcholek ma wspolrzedne (p, q), wiec z W wyluskujemy
        # p = 3 i q = 0, i te same liczby od razu wchodza do wzoru.
        # Zielone: liczby, ktore z wierzcholka wychodza i gdzie ladują.
        # ================================================================
        self.next_section("krok2")
        kop_p = dane_w[3].copy()
        kop_q = dane_w[5].copy()
        self.add(kop_p, kop_q)
        self.zapal(dane_w[3], dane_w[5])
        p_cz[2].set_color(ZIELONY)
        q_cz[2].set_color(ZIELONY)
        self.play(
            FadeIn(p_cz[0], p_cz[1]), ReplacementTransform(kop_p, p_cz[2]),
            FadeIn(q_cz[0], q_cz[1]), ReplacementTransform(kop_q, q_cz[2]),
            dane_w[3].animate.set_color(BLACK),
            dane_w[5].animate.set_color(BLACK),
            run_time=1.4,
        )
        self.wait(0.25)

        kopie = przywolaj(
            [p_cz[2], q_cz[2]],
            [s2lit[9].get_center(), s2lit[13].get_center()],
        )
        s2[9].set_color(ZIELONY)
        s2[13].set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(s2lit[i], s2[i])
              for i in (0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12)],
            ReplacementTransform(kopie[0], s2[9]),
            ReplacementTransform(kopie[1], s2[13]),
            FadeOut(s2lit[9], scale=0.4), FadeOut(s2lit[13], scale=0.4),
            run_time=1.5,
        )
        self.zgas(s2[9], s2[13], p_cz[2], q_cz[2])
        self.wait(POSTOJ)

        # ================================================================
        # KROK 3. Dodanie zera niczego nie zmienia, wiec "+ 0" znika.
        # ================================================================
        self.next_section("krok3")
        self.zapal(s2[12], s2[13])
        self.play(
            *[ReplacementTransform(s2[i], s3[i]) for i in range(12)],
            FadeOut(s2[12], scale=0.4), FadeOut(s2[13], scale=0.4),
            run_time=1.2,
        )
        self.wait(POSTOJ)

        # ================================================================
        # KROK 4. "Wykres przechodzi przez A" znaczy, ze dla x = 0 wartosc
        # funkcji wynosi -9. Najpierw dopisujemy to zdanie rachunkiem
        # (f(0) = -9) pod samym punktem A, i dopiero potem obie wspolrzedne
        # wyjezdzaja z A na swoje miejsca w rownaniu.
        # ================================================================
        self.next_section("krok4")
        self.play(FadeIn(dopisek_f0, shift=DOWN * 0.2), run_time=0.7)
        self.wait(0.25)
        kopie4 = przywolaj(
            [dane_a[5], dane_a[3]],
            [s4[0].get_center(), s4[4].get_center()],
            czas=1.1,
        )
        s4[0].set_color(ZIELONY)
        s4[4].set_color(ZIELONY)
        self.play(
            ReplacementTransform(kopie4[0], s4[0]),
            FadeOut(s3[0], scale=0.4), FadeOut(s3[1], scale=0.4),
            FadeOut(s3[2], scale=0.4), FadeOut(s3[3], scale=0.4),
            ReplacementTransform(s3[4], s4[1]),
            ReplacementTransform(s3[5], s4[2]),
            ReplacementTransform(s3[6], s4[3]),
            ReplacementTransform(kopie4[1], s4[4]),
            FadeOut(s3[7], scale=0.4),
            ReplacementTransform(s3[8], s4[5]),
            ReplacementTransform(s3[9], s4[6]),
            ReplacementTransform(s3[10], s4[7]),
            ReplacementTransform(s3[11], s4[8]),
            run_time=1.6,
        )
        self.zgas(s4[0], s4[4])
        self.wait(POSTOJ)

        # ================================================================
        # KROK 5. 0 - 3 to -3. Wlasny krok, bo tu uczen gubi znak.
        # ================================================================
        self.next_section("krok5")
        self.zapal(s4[4], s4[5], s4[6])
        s5[4].set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(s4[i], s5[j])
              for i, j in ((0, 0), (1, 1), (2, 2), (3, 3), (7, 5), (8, 6))],
            ReplacementTransform(VGroup(s4[4], s4[5], s4[6]), s5[4]),
            run_time=1.3,
        )
        self.zgas(s5[4])
        self.wait(POSTOJ)

        # ================================================================
        # KROK 6. Kwadrat liczby ujemnej jest dodatni: (-3)^2 = 9.
        # Pojawia sie kropka mnozenia, bo "a9" nie da sie przeczytac.
        # ================================================================
        self.next_section("krok6")
        self.zapal(s5[3], s5[4], s5[5], s5[6])
        s6[3].set_color(ZIELONY)
        s6[4].set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(s5[i], s6[j])
              for i, j in ((0, 0), (1, 1), (2, 2))],
            FadeIn(s6[3]),
            ReplacementTransform(VGroup(s5[3], s5[4], s5[5], s5[6]), s6[4]),
            run_time=1.4,
        )
        self.zgas(s6[3], s6[4])
        dop6.next_to(s6, RIGHT, buff=0.9)
        self.play(FadeIn(dop6, shift=LEFT * 0.3), run_time=0.6)
        self.wait(POSTOJ)

        # ================================================================
        # KROK 7. Dzielimy obie strony przez 9.
        # ================================================================
        self.next_section("krok7")
        self.zapal(s6[0], s6[3], s6[4])
        s7[2].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s6[2], s7[0]),
            ReplacementTransform(s6[1], s7[1]),
            ReplacementTransform(VGroup(s6[0], s6[3], s6[4]), s7[2]),
            FadeOut(dop6, shift=RIGHT * 0.3),
            run_time=1.4,
        )
        self.zgas(s7[2])
        self.wait(POSTOJ)

        # ================================================================
        # KROK 8. Gora kadru sie czysci. W, A, dopisek i pas odczytu zrobily
        # swoje, a jedyne, co z nich zostaje potrzebne, to a = -1, wiec ten
        # wynik jedzie na ich miejsce, na srodek (Henrich, 2026-08-30: „ten
        # caly balagan na gorze ma zniknac i a = -1 wejsc na jego miejsce").
        # Bez koloru: nic sie tu nie przelicza, tylko sprzata.
        # ================================================================
        self.next_section("krok8")
        przesuw = UP * A_GORA_Y - s7.get_center()
        self.play(
            FadeOut(dane_w, shift=UP * 0.3),
            FadeOut(dane_a, shift=UP * 0.3),
            FadeOut(dopisek_f0, shift=UP * 0.3),
            FadeOut(p_cz, shift=UP * 0.3),
            FadeOut(q_cz, shift=UP * 0.3),
            *[m.animate.shift(przesuw) for m in (s7[0], s7[1], s7[2])],
            run_time=1.3,
        )
        self.wait(POSTOJ)

        # ================================================================
        # KROK 9. Wraca postac kanoniczna, a w miejsce litery a wlatuje
        # policzona liczba, prosto z gory kadru (README, punkt 38).
        # ================================================================
        self.next_section("krok9")
        self.play(FadeIn(s3b), run_time=0.8)
        self.wait(0.25)
        kopie8 = przywolaj([s7[2]], [s3b[5].get_center()], czas=1.0)
        s8[5].set_color(ZIELONY)
        s8[6].set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(s3b[i], s8[i]) for i in range(5)],
            ReplacementTransform(kopie8[0], s8[5]),
            FadeOut(s3b[5], scale=0.4),
            FadeIn(s8[6]),
            *[ReplacementTransform(s3b[i], s8[i + 1]) for i in range(6, 12)],
            run_time=1.5,
        )
        self.zgas(s8[5], s8[6])
        self.wait(POSTOJ)

        # ================================================================
        # KROK 10. Mnozenie przez -1 zapisujemy samym minusem. To jest
        # odpowiedz B. Na KONCU tego kroku wjezdza wzor na kwadrat roznicy
        # (Henrich, 2026-08-30: „moze on sie pojawic juz na koncu poprzedniego
        # filmiku"): nastepny krok zaczyna sie wtedy od samego rachunku, a nie
        # od wjazdu wzoru, wiec pierwsza klatka pliku jest spokojna.
        # ================================================================
        self.next_section("krok10")
        self.zapal(s8[5], s8[6])
        s9[5].set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(s8[i], s9[i]) for i in range(5)],
            ReplacementTransform(VGroup(s8[5], s8[6]), s9[5]),
            *[ReplacementTransform(s8[i + 1], s9[i]) for i in range(6, 12)],
            run_time=1.4,
        )
        self.zgas(s9[5])
        self.play(FadeIn(etykieta_odp), FadeIn(litera_b, shift=UP * 0.2),
                  run_time=0.7)
        self.wait(0.3)
        self.play(FadeIn(wzor10), run_time=0.8)
        self.wait(POSTOJ)

        # ================================================================
        # KROK 11. Kwadrat roznicy ze wzoru z tablicy, ktory stoi juz w kadrze
        # od konca poprzedniego kroku. W nawiasie x wchodzi na miejsce a,
        # a trojka na miejsce b. Wzor znika na koncu tego kroku.
        # ================================================================
        self.next_section("krok11")
        self.zapal(wzor10[1], wzor10[3], s9[7], s9[9])
        for i in (10,):
            s10[i].set_color(ZIELONY)
        s10[7].set_color(ZIELONY)
        s10[12].set_color(ZIELONY)
        s10[14].set_color(ZIELONY)
        s10[16].set_color(ZIELONY)
        kop_x = s9[7].copy()
        kop_3 = s9[9].copy()
        kop_kw = s9[11].copy()
        self.add(kop_x, kop_3, kop_kw)
        self.play(
            *[ReplacementTransform(s9[i], s10[i]) for i in range(7)],
            ReplacementTransform(s9[7], s10[7]),
            ReplacementTransform(s9[11], s10[8]),
            ReplacementTransform(s9[8], s10[9]),
            FadeIn(s10[10]), FadeIn(s10[11]), FadeIn(s10[13]), FadeIn(s10[15]),
            ReplacementTransform(kop_x, s10[12]),
            ReplacementTransform(s9[9], s10[14]),
            ReplacementTransform(kop_3, s10[16]),
            ReplacementTransform(kop_kw, s10[17]),
            ReplacementTransform(s9[10], s10[18]),
            run_time=1.8,
        )
        self.zgas(s10[7], s10[10], s10[12], s10[14], s10[16],
                  wzor10[1], wzor10[3])
        self.play(FadeOut(wzor10), run_time=0.5)
        self.wait(POSTOJ)

        # ================================================================
        # KROK 12. 2 razy 3 to 6, a 3 do kwadratu to 9.
        # ================================================================
        self.next_section("krok12")
        self.zapal(s10[10], s10[11], s10[13], s10[14], s10[16], s10[17])
        s11[10].set_color(ZIELONY)
        s11[13].set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(s10[i], s11[i]) for i in range(10)],
            ReplacementTransform(VGroup(s10[10], s10[11], s10[13], s10[14]),
                                 s11[10]),
            ReplacementTransform(s10[12], s11[11]),
            ReplacementTransform(s10[15], s11[12]),
            ReplacementTransform(VGroup(s10[16], s10[17]), s11[13]),
            ReplacementTransform(s10[18], s11[14]),
            run_time=1.6,
        )
        self.zgas(s11[10], s11[13])
        self.wait(POSTOJ)

        # ================================================================
        # KROK 13. Minus przed nawiasem zmienia znak KAZDEGO skladnika.
        # Zielone: oba znaki, ktore sie odwracaja. To jest odpowiedz D.
        # ================================================================
        self.next_section("krok13")
        self.zapal(s11[5], s11[9], s11[12])
        s12[8].set_color(ZIELONY)
        s12[11].set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(s11[i], s12[i]) for i in range(6)],
            ReplacementTransform(s11[7], s12[6]),
            ReplacementTransform(s11[8], s12[7]),
            ReplacementTransform(s11[9], s12[8]),
            ReplacementTransform(s11[10], s12[9]),
            ReplacementTransform(s11[11], s12[10]),
            ReplacementTransform(s11[12], s12[11]),
            ReplacementTransform(s11[13], s12[12]),
            FadeOut(s11[6], scale=0.4), FadeOut(s11[14], scale=0.4),
            run_time=1.7,
        )
        self.zgas(s12[8], s12[11])
        self.play(FadeIn(przecinek), FadeIn(litera_d, shift=UP * 0.2),
                  run_time=0.7)
        self.wait(POSTOJ)

        # ================================================================
        # KROK 14. Podsumowanie. a = -1 zrobilo swoje i znika, a w kadrze
        # zostaja OBIE postaci wzoru, jedna pod druga (Henrich, 2026-08-30).
        # To one sa odpowiedzia na pytanie zadania: ten sam wzor raz zwiniety,
        # raz rozwiniety. Bez koloru: nic sie tu nie przelicza.
        # ================================================================
        self.next_section("krok14")
        czesci12 = [s12[i] for i in range(13)]
        zjazd = UP * PODSUM_D_Y - s12.get_center()
        self.play(
            FadeOut(s7[0], shift=UP * 0.3),
            FadeOut(s7[1], shift=UP * 0.3),
            FadeOut(s7[2], shift=UP * 0.3),
            *[m.animate.shift(zjazd) for m in czesci12],
            run_time=1.1,
        )
        self.play(FadeIn(podsum_b, shift=DOWN * 0.2), run_time=0.9)
        self.wait(0.5)
