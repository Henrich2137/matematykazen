from manim import *

from _wspolne import ZIELONY, ustaw_kroki, rozbij_ulamek, zapal, zakoncz_krok


# Zadanie 5 — procent składany. 60 000 · (1+p)^2 = 67 925,76 → p = 6,4%, odpowiedź B.
#
# Scenariusz kroków jest w manimations/zad5-kroki.md.
#
# PRZEPISANE 2026-08-12 po zgłoszeniu Henricha („animacje nie mają sensu, cyfry
# i znaki tańczą bez ładu i składu"). Pierwsza wersja jechała na
# TransformMatchingShapes, czyli automatycznym parowaniu glifów po kształcie —
# szóstka z 60 000 lądowała w LICZNIKU ułamka zamiast w mianowniku, a (1+p)^2
# zamiast przesunąć się w lewo, znikało i pojawiało się na nowo. Teraz każda para
# „skąd → dokąd" jest wypisana wprost.
#
# Render: manim --save_sections solutionZad5.py Zad5
class Zad5(Scene):

    def construct(self):
        # Każdy krok pocięty na kawałki, którymi da się osobno ruszać.
        k0 = MathTex(r"60\,000", r"\cdot", r"(1+p)^{2}", r"=", r"67\,925{,}76")
        k1 = MathTex(r"(1+p)^{2}", r"=", r"\frac{67\,925{,}76}{60\,000}")
        k2 = MathTex(r"(1+p)^{2}", r"=", r"1{,}132096")
        k3 = MathTex(r"1+p", r"=", r"1{,}064")
        k4 = MathTex(r"p", r"=", r"0{,}064")
        k5 = MathTex(r"p", r"=", r"6{,}4\%")

        ustaw_kroki([k0, k1, k2, k3, k4, k5])
        licznik, kreska, mianownik = rozbij_ulamek(k1[2])

        self.next_section("krok1")
        # KROK 1 — dane wstawione we wzór na procent składany.
        self.play(Write(k0), run_time=1.4)
        zakoncz_krok(self)

        self.next_section("krok2")
        # KROK 2 — dzielimy obie strony przez 60 000. Sedno kroku: 60 000 schodzi
        # POD KRESKĘ ułamka, więc tylko ono jest na zielono.
        zapal(self, na_ekranie=[k0[0]], poza_ekranem=[mianownik])
        self.play(
            Transform(k0[2], k1[0]),          # (1+p)^2 przesuwa się w lewo
            Transform(k0[3], k1[1]),          # znak równości
            Transform(k0[4], licznik),        # 67 925,76 idzie do licznika
            Transform(k0[0], mianownik),      # 60 000 idzie do MIANOWNIKA
            FadeOut(k0[1], scale=0.3),        # kropka mnożenia znika
            Create(kreska),
            run_time=1.6,
        )
        zakoncz_krok(self, k0[0], mianownik)
        self.clear()
        self.add(k1)

        self.next_section("krok3")
        # KROK 3 — liczymy ułamek. Zwykły rachunek, nic tu nie wymaga wskazywania
        # palcem, więc bez koloru.
        self.play(
            Transform(k1[0], k2[0]),
            Transform(k1[1], k2[1]),
            FadeTransform(k1[2], k2[2]),
            run_time=1.4,
        )
        zakoncz_krok(self)
        self.clear()
        self.add(k2)

        self.next_section("krok4")
        # KROK 4 — pierwiastkujemy obie strony. Na zielono dwójka wykładnika:
        # to ona znika i to jest cała treść kroku. Nawiasy przestają być potrzebne.
        zapal(self, na_ekranie=[k2[0][5]])
        self.play(
            Transform(k2[0][1:4], k3[0]),                  # 1+p zostaje
            FadeOut(k2[0][0], k2[0][4], scale=0.3),        # nawiasy
            FadeOut(k2[0][5], scale=0.3),                  # wykładnik 2
            Transform(k2[1], k3[1]),
            FadeTransform(k2[2], k3[2]),
            run_time=1.5,
        )
        zakoncz_krok(self)
        self.clear()
        self.add(k3)

        self.next_section("krok5")
        # KROK 5 — odejmujemy 1 od obu stron. Na zielono jedynka z plusem po lewej
        # i zmiana po prawej: to jedno i to samo odjęcie, widziane z dwóch stron.
        zapal(self, na_ekranie=[k3[0][0:2]], poza_ekranem=[k4[2][0]])
        self.play(
            Transform(k3[0][2], k4[0]),                    # samo p zostaje
            FadeOut(k3[0][0:2], shift=RIGHT * 0.5),        # „1+" znika
            Transform(k3[1], k4[1]),
            FadeTransform(k3[2], k4[2]),
            run_time=1.5,
        )
        zakoncz_krok(self, k4[2][0])
        self.clear()
        self.add(k4)

        self.next_section("krok6")
        # KROK 6 — ułamek dziesiętny na procent. Na zielono wynik, ale gaszony
        # przed przytrzymaniem, żeby ostatnia klatka była taka jak wszystkie inne.
        zapal(self, poza_ekranem=[k5[2]])
        self.play(
            Transform(k4[0], k5[0]),
            Transform(k4[1], k5[1]),
            FadeTransform(k4[2], k5[2]),
            run_time=1.4,
        )
        zakoncz_krok(self, k5[2])
