from manim import *

# Zadanie 14 (prawda/falsz, 1 pkt). a_n = 3 * (-1)^n + 10. Zdanie 1: ciag jest
# geometryczny (FALSZ). Zdanie 2: suma osmiu poczatkowych wyrazow wynosi 80
# (PRAWDA).
#
# Projekt: issues/projekt-zad13-zad14-2024-grudzien.md. Osiemnascie krokow,
# jeden do jednego z osiemnastoma linijkami w solutionText.
#
# Cale zadanie stoi na tym, ze (-1)^n przyjmuje tylko dwie wartosci, na przemian
# -1 i 1. Dlatego dwa pierwsze wyrazy licza sie PELNYM rachunkiem, z osobnym
# krokiem na 3 * (-1) = -3 (znak) i osobnym na (-1) * (-1) = 1 (dwa minusy).
# Trzeciego wyrazu juz nie liczymy: krok 10 pokazuje, dlaczego wyrazy musza sie
# powtarzac, i to wystarczy.
#
# Wzoru z tablicy tu nie ma i to jest swiadome: definicji ilorazu tablica nie
# podaje, a wzor na sume ciagu geometrycznego nie dziala, bo ciag geometryczny
# nie jest.
#
# Uklad kadru: rachunek na srodku, nad nim pas policzonych wartosci (a_1, a_2).
# Od kroku 11 pas zastepuje lista osmiu wyrazow, ktora zostaje do konca filmu,
# bo z niej biora sie i ilorazy, i suma. Werdykty na dole, litery czarne
# (COLORS.md: to odpowiedz ucznia, nie ocena poprawnosci).
#
# Render: manim --save_sections solutionZad14.py Zad14  (albo tools/wgraj-kroki.sh 14)

ZIELONY = "#2e7d32"

RACHUNEK_Y = UP * 0.35
PAS_Y = 2.75
LISTA_Y = 2.55
WERDYKT_Y = -2.95
POSTOJ = 0.25


class Zad14(Scene):

    def stan(self, *args, rozmiar=82):
        m = MathTex(*args)
        m.set_color(BLACK)
        m.font_size = rozmiar
        return m

    def ulamek(self, gora, dol, rozmiar=64):
        """Ulamek zlozony recznie (licznik, kreska, mianownik).

        Wzorzec z solutionZad9.py: \\dfrac w jednym MathTeksie nie daje uchwytu
        do pojedynczej liczby w liczniku, a bez tego liczba nie moze przyleciec
        z listy wyrazow na swoje miejsce.
        """
        g = self.stan(*gora, rozmiar=rozmiar)
        d = self.stan(*dol, rozmiar=rozmiar)
        szer = max(g.width, d.width) + 0.24
        kreska = Line(LEFT * szer / 2, RIGHT * szer / 2, color=BLACK, stroke_width=4)
        g.next_to(kreska, UP, buff=0.14)
        d.next_to(kreska, DOWN, buff=0.14)
        return VGroup(g, kreska, d)

    def werdykt(self, nr, litera, x):
        g = VGroup(
            Text(f"Zdanie {nr}:", font_size=32, color=BLACK),
            Text(litera, font_size=38, weight=BOLD, color=BLACK),
        ).arrange(RIGHT, buff=0.30)
        g.move_to([x, WERDYKT_Y, 0])
        return g

    def zapal(self, *mobiekty, czas=0.4):
        if mobiekty:
            self.play(*[m.animate.set_color(ZIELONY) for m in mobiekty], run_time=czas)

    def zakoncz(self, *czysty, pomin=(), czas=0.4, postoj=POSTOJ):
        """Gaszenie kolorow, podmiana na czysty stan, dopiero potem przytrzymanie."""
        self.wait(0.3)
        gasnie = [m for m in self.mobjects if not any(m is p for p in pomin)]
        if gasnie:
            self.play(*[m.animate.set_color(BLACK) for m in gasnie], run_time=czas)
        self.clear()
        for m in czysty:
            if not any(m is p for p in pomin):
                m.set_color(BLACK)
        self.add(*czysty)
        self.wait(postoj)

    def construct(self):
        # ================================================================
        # STANY RACHUNKU
        # ================================================================
        w0 = self.stan("a", "_{n}", "=", "3", r"\cdot", "(", "-", "1", ")",
                       "^{n}", "+", "10")
        s1 = self.stan("a", "_{1}", "=", "3", r"\cdot", "(", "-", "1", ")",
                       "^{1}", "+", "10")
        s2 = self.stan("a", "_{1}", "=", "3", r"\cdot", "(", "-", "1", ")",
                       "+", "10")
        s3 = self.stan("a", "_{1}", "=", "-", "3", "+", "10")
        s4 = self.stan("a", "_{1}", "=", "7")
        s5 = self.stan("a", "_{2}", "=", "3", r"\cdot", "(", "-", "1", ")",
                       "^{2}", "+", "10")
        s6 = self.stan("a", "_{2}", "=", "3", r"\cdot", "(", "-", "1", ")",
                       r"\cdot", "(", "-", "1", ")", "+", "10")
        s7 = self.stan("a", "_{2}", "=", "3", r"\cdot", "1", "+", "10")
        s8 = self.stan("a", "_{2}", "=", "3", "+", "10")
        s9 = self.stan("a", "_{2}", "=", "13")

        grupa_a = [w0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
        POLE = config.frame_width * 0.85
        wsp_a = min(1.0, POLE / max(m.width for m in grupa_a))
        for m in grupa_a:
            m.scale(wsp_a)
            m.move_to(RACHUNEK_Y)

        # Pas policzonych wartosci: mniejszym pismem niz rachunek, bo to notatka
        # z boku, a nie kolejna linijka (README, punkt 41).
        pas1 = self.stan("a", "_{1}", "=", "7", rozmiar=52)
        pas2 = self.stan("a", "_{2}", "=", "13", rozmiar=52)
        pas1.move_to([-1.5, PAS_Y, 0])
        pas2.move_to([1.5, PAS_Y, 0])

        # ================================================================
        # KROK 10: cztery potegi minus jedynki, w dwoch kolumnach
        # ================================================================
        pot = [self.stan("(", "-", "1", ")", "^{1}", "=", "-", "1", rozmiar=62),
               self.stan("(", "-", "1", ")", "^{2}", "=", "1", rozmiar=62),
               self.stan("(", "-", "1", ")", "^{3}", "=", "-", "1", rozmiar=62),
               self.stan("(", "-", "1", ")", "^{4}", "=", "1", rozmiar=62)]
        for i, m in enumerate(pot):
            m.move_to([-2.3 + 4.6 * (i % 2), 0.95 - 1.25 * (i // 2), 0])

        # ================================================================
        # KROK 11: lista osmiu wyrazow, ktora zostaje do konca filmu
        # ================================================================
        WYRAZY = [7, 13, 7, 13, 7, 13, 7, 13]
        liczby = VGroup(*[self.stan(str(w), rozmiar=52) for w in WYRAZY])
        liczby.arrange(RIGHT, buff=0.62)
        liczby.move_to([0, LISTA_Y, 0])
        numery = VGroup()
        for i, l in enumerate(liczby):
            n = MathTex("a_{%d}" % (i + 1), color=BLACK, font_size=34)
            n.next_to(l, UP, buff=0.20)
            numery.add(n)
        lista = VGroup(liczby, numery)

        # ================================================================
        # KROKI 12 do 14: ilorazy sasiednich wyrazow
        # ================================================================
        il1_lewa = self.stan(r"\dfrac{a_{2}}{a_{1}}", "=", rozmiar=64)
        il1_prawa = self.ulamek(("13",), ("7",))
        il1 = VGroup(il1_lewa, il1_prawa).arrange(RIGHT, buff=0.26)
        il1.move_to([0, 0.55, 0])

        il2_lewa = self.stan(r"\dfrac{a_{3}}{a_{2}}", "=", rozmiar=64)
        il2_prawa = self.ulamek(("7",), ("13",))
        il2 = VGroup(il2_lewa, il2_prawa).arrange(RIGHT, buff=0.26)
        il2.move_to([0, -1.15, 0])

        znak_ne = self.stan(r"\ne", rozmiar=72)
        znak_ne.move_to([0, -0.3, 0])
        CEL_IL1 = [-1.35, -0.3, 0]
        CEL_IL2 = [1.35, -0.3, 0]

        # ================================================================
        # KROKI 15 do 18: suma osmiu wyrazow
        # ================================================================
        def suma(*args):
            return self.stan(*args, rozmiar=72)

        skladniki = []
        for w in WYRAZY:
            skladniki += [str(w), "+"]
        skladniki = skladniki[:-1]
        t15 = suma("S", "_{8}", "=", *skladniki)

        naw = []
        for i in range(4):
            naw += ["(", str(WYRAZY[2 * i]), "+", str(WYRAZY[2 * i + 1]), ")", "+"]
        naw = naw[:-1]
        t16 = suma("S", "_{8}", "=", *naw)

        t17 = suma("S", "_{8}", "=", "20", "+", "20", "+", "20", "+", "20")
        t18 = suma("S", "_{8}", "=", "80")

        grupa_b = [t15, t16, t17, t18]
        wsp_b = min(1.0, POLE / max(m.width for m in grupa_b))
        for m in grupa_b:
            m.scale(wsp_b)
            m.move_to([0, -0.15, 0])

        werdykt1 = self.werdykt(1, "F", -3.35)
        werdykt2 = self.werdykt(2, "P", 2.15)

        # ================================================================
        # KROK 1. Podstawienie n = 1, w obu miejscach naraz.
        # ================================================================
        self.next_section("krok1")
        self.play(Write(w0), run_time=1.5)
        self.wait(0.35)
        self.zapal(w0[1], w0[9])
        s1[1].set_color(ZIELONY)
        s1[9].set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(w0[i], s1[i]) for i in range(12)],
            run_time=1.3,
        )
        self.zakoncz(s1)

        # ================================================================
        # KROK 2. Pierwsza potega niczego nie zmienia: wykladnik znika.
        # ================================================================
        self.next_section("krok2")
        self.zapal(s1[9])
        self.play(
            *[ReplacementTransform(s1[i], s2[i]) for i in range(9)],
            FadeOut(s1[9], scale=0.3),
            ReplacementTransform(s1[10], s2[9]),
            ReplacementTransform(s1[11], s2[10]),
            run_time=1.2,
        )
        self.zakoncz(s2)

        # ================================================================
        # KROK 3. 3 * (-1) = -3. Zielony jest minus: to on decyduje o znaku,
        # a trojka tylko wychodzi z nawiasu i dalej jest ta sama trojka.
        # ================================================================
        self.next_section("krok3")
        self.zapal(s2[6])
        s3[3].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s2[0], s3[0]),
            ReplacementTransform(s2[1], s3[1]),
            ReplacementTransform(s2[2], s3[2]),
            ReplacementTransform(s2[6], s3[3]),
            ReplacementTransform(s2[3], s3[4]),
            ReplacementTransform(s2[9], s3[5]),
            ReplacementTransform(s2[10], s3[6]),
            FadeOut(s2[4], scale=0.3), FadeOut(s2[5], scale=0.3),
            FadeOut(s2[7], scale=0.3), FadeOut(s2[8], scale=0.3),
            run_time=1.4, path_arc=PI / 4,
        )
        self.zakoncz(s3)

        # ================================================================
        # KROK 4. -3 + 10 = 7.
        # ================================================================
        self.next_section("krok4")
        s4[3].set_color(ZIELONY)
        self.play(
            ReplacementTransform(s3[0], s4[0]),
            ReplacementTransform(s3[1], s4[1]),
            ReplacementTransform(s3[2], s4[2]),
            *[ReplacementTransform(s3[i], s4[3].copy()) for i in (3, 4, 5)],
            ReplacementTransform(s3[6], s4[3]),
            run_time=1.3,
        )
        self.zakoncz(s4)

        # ================================================================
        # KROK 5. Pierwszy wyraz odjezdza do pasu, wjezdza drugi. Bez koloru:
        # nic sie tu nie przelicza (README, punkt 5).
        # ================================================================
        self.next_section("krok5")
        self.play(ReplacementTransform(s4, pas1), run_time=1.0)
        self.play(FadeIn(s5, shift=UP * 0.3), run_time=0.9)
        self.zakoncz(s5, pas1)

        # ================================================================
        # KROK 6. Druga potega to iloczyn dwoch takich samych czynnikow.
        # Ogniwo dostaje wlasny krok, a nie rachunek na boku (README,
        # "Wyjasnienie w srodku kroku": lepiej dolozyc krok).
        # ================================================================
        self.next_section("krok6")
        self.zapal(s5[9])
        kopia_naw = s5[5:9].copy()
        self.add(kopia_naw)
        # Zielone sa tylko minus i jedynka nowego czynnika. Nawiasow ani kropki
        # mnozenia sie nie koloruje (README, punkt 13).
        s6[11].set_color(ZIELONY)
        s6[12].set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(s5[i], s6[i]) for i in range(9)],
            FadeOut(s5[9], scale=0.3),
            FadeIn(s6[9]),
            ReplacementTransform(kopia_naw, s6[10:14]),
            ReplacementTransform(s5[10], s6[14]),
            ReplacementTransform(s5[11], s6[15]),
            run_time=1.6,
        )
        self.zakoncz(s6, pas1)

        # ================================================================
        # KROK 7. Dwa minusy daja plus: (-1) * (-1) = 1.
        # ================================================================
        self.next_section("krok7")
        self.zapal(s6[6], s6[11])
        s7[5].set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(s6[i], s7[i]) for i in range(5)],
            *[ReplacementTransform(s6[i], s7[5].copy())
              for i in (5, 6, 7, 8, 9, 10, 11, 12, 13)],
            FadeIn(s7[5]),
            ReplacementTransform(s6[14], s7[6]),
            ReplacementTransform(s6[15], s7[7]),
            run_time=1.5,
        )
        self.zakoncz(s7, pas1)

        # ================================================================
        # KROK 8. Mnozenie przez jedynke niczego nie zmienia.
        # ================================================================
        self.next_section("krok8")
        self.zapal(s7[5])
        self.play(
            *[ReplacementTransform(s7[i], s8[i]) for i in range(4)],
            FadeOut(s7[4], scale=0.3), FadeOut(s7[5], scale=0.3),
            ReplacementTransform(s7[6], s8[4]),
            ReplacementTransform(s7[7], s8[5]),
            run_time=1.2,
        )
        self.zakoncz(s8, pas1)

        # ================================================================
        # KROK 9. 3 + 10 = 13.
        # ================================================================
        self.next_section("krok9")
        s9[3].set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(s8[i], s9[i]) for i in range(3)],
            *[ReplacementTransform(s8[i], s9[3].copy()) for i in (3, 4)],
            ReplacementTransform(s8[5], s9[3]),
            run_time=1.3,
        )
        self.zakoncz(s9, pas1)

        # ================================================================
        # KROK 10. Skad naprzemiennosc: wykladnik idzie 1, 2, 3, 4, wiec raz
        # jest nieparzysty, raz parzysty. Zielone sa same wyniki, zeby bylo
        # widac, ze skacza.
        # ================================================================
        self.next_section("krok10")
        self.play(ReplacementTransform(s9, pas2), run_time=1.0)
        for m, od in zip(pot, (6, 6, 6, 6)):
            for g in m[od:]:
                g.set_color(ZIELONY)
        self.play(FadeIn(pot[0], shift=UP * 0.2), FadeIn(pot[1], shift=UP * 0.2),
                  run_time=0.9)
        self.play(FadeIn(pot[2], shift=UP * 0.2), FadeIn(pot[3], shift=UP * 0.2),
                  run_time=0.9)
        self.zakoncz(*pot, pas1, pas2)

        # ================================================================
        # KROK 11. Osiem poczatkowych wyrazow. Siodemka i trzynastka nie
        # pojawiaja sie znikad: przylatuja z pasa, w ktorym je policzylismy
        # (README, punkt 38).
        # ================================================================
        self.next_section("krok11")
        self.play(*[FadeOut(m, scale=0.6) for m in pot], run_time=0.6)
        for i in range(2, 8):
            liczby[i].set_color(ZIELONY)
        self.play(
            ReplacementTransform(pas1, liczby[0]),
            ReplacementTransform(pas2, liczby[1]),
            run_time=1.1,
        )
        self.play(
            *[FadeIn(liczby[i], shift=DOWN * 0.15) for i in range(2, 8)],
            FadeIn(numery),
            run_time=1.0,
        )
        self.zakoncz(lista)

        # ================================================================
        # KROK 12. Pierwszy iloraz sasiadow. Liczby przylatuja z listy.
        # ================================================================
        self.next_section("krok12")
        self.play(FadeIn(il1_lewa), run_time=0.7)
        k13 = liczby[1].copy()
        k7 = liczby[0].copy()
        self.add(k13, k7)
        il1_prawa[1].set_color(BLACK)
        self.play(FadeIn(il1_prawa[1]), run_time=0.4)
        self.play(
            k13.animate.set_color(ZIELONY).move_to(il1_prawa[0]).scale(
                il1_prawa[0].height / max(k13.height, 1e-6)),
            k7.animate.set_color(ZIELONY).move_to(il1_prawa[2]).scale(
                il1_prawa[2].height / max(k7.height, 1e-6)),
            run_time=1.2, path_arc=-PI / 5,
        )
        self.zakoncz(lista, il1)

        # ================================================================
        # KROK 13. Drugi iloraz sasiadow, ten sam rachunek.
        # ================================================================
        self.next_section("krok13")
        self.play(FadeIn(il2_lewa), run_time=0.7)
        k7b = liczby[2].copy()
        k13b = liczby[1].copy()
        self.add(k7b, k13b)
        il2_prawa[1].set_color(BLACK)
        self.play(FadeIn(il2_prawa[1]), run_time=0.4)
        self.play(
            k7b.animate.set_color(ZIELONY).move_to(il2_prawa[0]).scale(
                il2_prawa[0].height / max(k7b.height, 1e-6)),
            k13b.animate.set_color(ZIELONY).move_to(il2_prawa[2]).scale(
                il2_prawa[2].height / max(k13b.height, 1e-6)),
            run_time=1.2, path_arc=-PI / 5,
        )
        self.zakoncz(lista, il1, il2)

        # ================================================================
        # KROK 14. Oba wyniki zjezdzaja w jedna linijke, a miedzy nimi
        # pojawia sie przekreslony znak rownosci. Zdanie 1: F.
        # ================================================================
        self.next_section("krok14")
        znak_ne.set_color(ZIELONY)
        self.play(
            FadeOut(il1_lewa, scale=0.5), FadeOut(il2_lewa, scale=0.5),
            il1_prawa.animate.move_to(CEL_IL1),
            il2_prawa.animate.move_to(CEL_IL2),
            run_time=1.2,
        )
        self.play(FadeIn(znak_ne), run_time=0.6)
        self.play(FadeIn(werdykt1, shift=UP * 0.2), run_time=0.7)
        self.zakoncz(lista, il1_prawa, il2_prawa, znak_ne, werdykt1)

        # ================================================================
        # KROK 15. Suma osmiu wyrazow. Skladniki zjezdzaja z listy, wiec
        # widac, ze to dokladnie te osiem liczb, a nie nowe.
        # ================================================================
        self.next_section("krok15")
        self.play(
            FadeOut(il1_prawa), FadeOut(il2_prawa), FadeOut(znak_ne),
            run_time=0.6,
        )
        kopie = [liczby[i].copy() for i in range(8)]
        self.add(*kopie)
        cele = [t15[3 + 2 * i] for i in range(8)]
        self.play(
            FadeIn(t15[0]), FadeIn(t15[1]), FadeIn(t15[2]),
            *[k.animate.move_to(c).scale(c.height / max(k.height, 1e-6))
              for k, c in zip(kopie, cele)],
            run_time=1.5,
        )
        self.play(*[FadeIn(t15[4 + 2 * i]) for i in range(7)], run_time=0.6)
        self.zakoncz(lista, t15, werdykt1)

        # ================================================================
        # KROK 16. Skladniki lacza sie w pary. Bez koloru: nawiasow sie nie
        # koloruje (SOLUTION_TEXT_RULES.md, punkt 14).
        # ================================================================
        self.next_section("krok16")
        pary = []
        for i in range(4):
            b = 3 + 6 * i
            pary += [(t15[3 + 4 * i], t16[b + 1]),
                     (t15[4 + 4 * i], t16[b + 2]),
                     (t15[5 + 4 * i], t16[b + 3])]
        for i in range(3):
            pary.append((t15[6 + 4 * i], t16[8 + 6 * i]))
        self.play(
            *[ReplacementTransform(t15[i], t16[i]) for i in range(3)],
            *[ReplacementTransform(a, b) for a, b in pary],
            *[FadeIn(t16[3 + 6 * i]) for i in range(4)],
            *[FadeIn(t16[7 + 6 * i]) for i in range(4)],
            run_time=1.5,
        )
        self.zakoncz(lista, t16, werdykt1)

        # ================================================================
        # KROK 17. Kazda para daje 20.
        # ================================================================
        self.next_section("krok17")
        for i in range(4):
            t17[3 + 2 * i].set_color(ZIELONY)
        ruchy = []
        for i in range(4):
            b = 3 + 6 * i
            for j in (0, 1, 2, 3, 4):
                ruchy.append(ReplacementTransform(t16[b + j],
                                                  t17[3 + 2 * i].copy()))
        self.play(
            *[ReplacementTransform(t16[i], t17[i]) for i in range(3)],
            *ruchy,
            *[FadeIn(t17[3 + 2 * i]) for i in range(4)],
            *[ReplacementTransform(t16[8 + 6 * i], t17[4 + 2 * i])
              for i in range(3)],
            run_time=1.5,
        )
        self.zakoncz(lista, t17, werdykt1)

        # ================================================================
        # KROK 18. Cztery dwudziestki daja 80. Zdanie 2: P.
        # ================================================================
        self.next_section("krok18")
        t18[3].set_color(ZIELONY)
        self.play(
            *[ReplacementTransform(t17[i], t18[i]) for i in range(3)],
            *[ReplacementTransform(t17[i], t18[3].copy()) for i in range(3, 10)],
            FadeIn(t18[3]),
            run_time=1.4,
        )
        self.play(FadeIn(werdykt2, shift=UP * 0.2), run_time=0.7)
        self.wait(0.35)
        self.play(t18[3].animate.set_color(BLACK), run_time=0.4)
        self.wait(POSTOJ)
