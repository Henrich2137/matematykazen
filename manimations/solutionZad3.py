from manim import *


class ScenaZadania3(Scene):
    """Zadanie 3, grudzien 2024: 2^100 + 4^49 + 16^24 dzieli sie przez 21.

    OSIEM KROKOW, jeden do jednego z osmioma linijkami rachunku w rozwiazaniu
    opisowym (pole solutionText w matura/2024-grudzien/exercises.json).
    Zmieniajac jedno, popraw drugie.

    Scena jest napisana tak samo jak solutionZad2.py, wedlug zasad z
    manimations/README.md, sekcja „Zasady krok po kroku, wersja krotka".

    KAZDY KROK MA TEN SAM PRZEBIEG:

        1. wszystko czarne,
        2. kluczowy element zapala sie na zielono,
        3. animacja przeksztalcenia, zielone zostaje zielone,
        4. wszystko znow czarne.

    ZIELONE JEST TO, CO SIE ZMIENIA: znika, pojawia sie, zmienia wartosc albo
    zmienia role. Czarne zostaje to, co jedzie w nowe miejsce zapisu, ale dalej
    znaczy to samo.

    Krok 2, 4 staje sie 2^2: czworka przestaje byc podstawa i zmienia sie
    w potege dwojki, wiec jest ZIELONA. Wykladniki 49 i 24 stoja bez zmian,
    tylko przesuwaja sie w prawo, wiec sa CZARNE.

    Krok 6, wylaczenie 2^96 przed nawias: jedno 2^96 zostaje w zapisie i tylko
    jedzie na przod, wiec jest CZARNE. Dwa pozostale znikaja, wiec sa ZIELONE,
    tak samo jak nawiasy, ktorych wczesniej nie bylo.

    RUCH ZAMIAST MORFOWANIA. Stany sa MathTexem pocietym na CZESCI, a pary
    wskazane recznie. Bez tego Manim paruje ksztalty po podobienstwie i cyfry
    lecza nie tam, gdzie ida w rachunku.
    """

    # Ten sam zielony, ktorym rozwiazanie opisowe obok filmu zaznacza fragment,
    # do ktorego odnosi sie wzor: token --accent-green z COLORS.md.
    ZIELONY = "#2e7d32"

    # MAPA CZESCI. Stany sa pociete na czesci tak, zeby wszystko, co przetrwa
    # przeksztalcenie (podstawa 2, wykladniki, plusy, kropki), mialo wlasny
    # uchwyt i dalo sie przesunac w calosci. Glify numerujemy tylko tam, gdzie
    # czesc trzeba rozciac na pol:
    #
    #   k3[2] = "+4}"   0 plus   1 cyfra 4
    #   k3[6] = "+2}"   0 plus   1 cyfra 2

    ZAPALANIE = 0.4   # sekundy; tyle trwa samo zapalenie i samo zgaszenie koloru

    def construct(self):

        k = [None] * 8
        k[0] = MathTex(r"2", r"^{100}", r"+", r"4", r"^{49}", r"+", r"16", r"^{24}")
        k[1] = MathTex(r"2", r"^{100}", r"+",
                       r"(", r"2", r"^{2}", r")", r"^{49}", r"+",
                       r"(", r"2", r"^{4}", r")", r"^{24}")
        k[2] = MathTex(r"2", r"^{100}", r"+", r"2", r"^{98}", r"+", r"2", r"^{96}")
        # Wykladniki pociete na dwie czesci, zeby 96 stalo w miejscu, a dokladana
        # reszta sumy przyleciala osobno.
        k[3] = MathTex(r"2", r"^{96", r"+4}", r"+", r"2", r"^{96", r"+2}", r"+", r"2", r"^{96}")
        k[4] = MathTex(r"2", r"^{96}", r"\cdot", r"2", r"^{4}", r"+",
                       r"2", r"^{96}", r"\cdot", r"2", r"^{2}", r"+",
                       r"2", r"^{96}", r"\cdot", r"1")
        k[5] = MathTex(r"2", r"^{96}", r"\cdot", r"(", r"2", r"^{4}", r"+",
                       r"2", r"^{2}", r"+", r"1", r")")
        k[6] = MathTex(r"2", r"^{96}", r"\cdot", r"(", r"16", r"+", r"4", r"+", r"1", r")")
        k[7] = MathTex(r"2", r"^{96}", r"\cdot", r"21")

        for stan in k:
            stan.fill_color = BLACK
            stan.font_size = 100

        # Skala WSPOLNA dla wszystkich krokow, liczona z najszerszego: gdyby kazdy
        # krok dopasowywal sie osobno, litery zmienialyby rozmiar w trakcie
        # przeksztalcenia i Transform robilby z tego zoom.
        MARGINES = 0.85
        najszerszy = max(stan.width for stan in k)
        if najszerszy > config.frame_width * MARGINES:
            wspolczynnik = config.frame_width * MARGINES / najszerszy
            for stan in k:
                stan.scale(wspolczynnik)
        for stan in k:
            stan.move_to(ORIGIN)

        def zapal(*co):
            """Krok 2 przebiegu: kluczowy element zapala sie na zielono."""
            self.play(*[m.animate.set_color(self.ZIELONY) for m in co],
                      run_time=self.ZAPALANIE)

        def zgas(zrodla, cele, nastepny):
            """Kroki 4 i domkniecie: wszystko wraca do czerni, scena na czysto.

            `zrodla` leza na ekranie po przeksztalceniu i trzeba je wygasic
            animacja. `cele` leza poza scena, wiec wystarczy im set_color, ale
            zrobic to trzeba, bo za chwile to one wjezdzaja jako czysty stan
            nastepnego kroku. Podmiana idzie PRZED przytrzymaniem, zeby te
            0,25 s pokazywalo czysty obiekt, a nie obiekty po Transform.
            """
            if zrodla:
                self.play(*[m.animate.set_color(BLACK) for m in zrodla],
                          run_time=self.ZAPALANIE)
            for m in cele:
                m.set_color(BLACK)
            self.clear()
            self.add(nastepny)
            self.wait(0.25)

        self.next_section("krok1")
        # Zapisujemy liczbe z zadania. Nic sie jeszcze nie zmienia, wiec nie ma
        # czego zaznaczac.
        self.play(Create(k[0]))
        zgas([], [], k[0])

        self.next_section("krok2")
        # Wspolna podstawa: 4 = 2^2 oraz 16 = 2^4. Zielone sa czworka i szesnastka,
        # bo przestaja byc podstawami i zmieniaja sie w potegi dwojki, oraz nawiasy,
        # ktorych wczesniej nie bylo. Wykladniki 49 i 24 tylko sie przesuwaja.
        zapal(k[0][3], k[0][6])
        for cel in (k[1][3], k[1][4], k[1][5], k[1][6], k[1][9], k[1][10], k[1][11], k[1][12]):
            cel.set_color(self.ZIELONY)
        self.play(
            Transform(k[0][0], k[1][0]),
            Transform(k[0][1], k[1][1]),
            Transform(k[0][2], k[1][2]),
            Transform(k[0][3], VGroup(k[1][4], k[1][5])),   # 4 -> 2^2
            FadeIn(k[1][3]), FadeIn(k[1][6]),               # nawiasy
            Transform(k[0][4], k[1][7]),                    # wykladnik 49
            Transform(k[0][5], k[1][8]),
            Transform(k[0][6], VGroup(k[1][10], k[1][11])),  # 16 -> 2^4
            FadeIn(k[1][9]), FadeIn(k[1][12]),              # nawiasy
            Transform(k[0][7], k[1][13]),                   # wykladnik 24
        )
        zgas([k[0][3], k[0][6], k[1][3], k[1][6], k[1][9], k[1][12]],
             [k[1][3], k[1][4], k[1][5], k[1][6], k[1][9], k[1][10], k[1][11], k[1][12]], k[1])

        self.next_section("krok3")
        # Potega potegi: (a^r)^s = a^{r*s}. Znikaja nawiasy, a dwa wykladniki
        # zlewaja sie w jeden o innej wartosci, wiec i nawiasy, i wykladniki
        # sa zielone. Podstawa 2 zostaje podstawa, wiec jest czarna.
        zapal(k[1][3], k[1][5], k[1][6], k[1][7], k[1][9], k[1][11], k[1][12], k[1][13])
        k[2][4].set_color(self.ZIELONY)
        k[2][7].set_color(self.ZIELONY)
        self.play(
            Transform(k[1][0], k[2][0]),
            Transform(k[1][1], k[2][1]),
            Transform(k[1][2], k[2][2]),
            Transform(k[1][4], k[2][3]),                       # podstawa 2
            Transform(VGroup(k[1][5], k[1][7]), k[2][4]),      # 2 i 49 -> 98
            FadeOut(k[1][3]), FadeOut(k[1][6]),
            Transform(k[1][8], k[2][5]),
            Transform(k[1][10], k[2][6]),                      # podstawa 2
            Transform(VGroup(k[1][11], k[1][13]), k[2][7]),    # 4 i 24 -> 96
            FadeOut(k[1][9]), FadeOut(k[1][12]),
        )
        zgas([k[1][5], k[1][11]], [k[2][4], k[2][7]], k[2])

        self.next_section("krok4")
        # Szukamy czegos wspolnego. Najmniejszy wykladnik to 96, wiec dwa
        # pozostale rozpisujemy tak, zeby 96 sie w nich pojawilo. Zmieniaja sie
        # wykladniki, wiec to one sa zielone.
        zapal(k[2][1], k[2][4])
        VGroup(k[3][1], k[3][2]).set_color(self.ZIELONY)
        VGroup(k[3][5], k[3][6]).set_color(self.ZIELONY)
        self.play(
            Transform(k[2][0], k[3][0]),
            Transform(k[2][1], VGroup(k[3][1], k[3][2])),      # 100 -> 96+4
            Transform(k[2][2], k[3][3]),
            Transform(k[2][3], k[3][4]),
            Transform(k[2][4], VGroup(k[3][5], k[3][6])),      # 98 -> 96+2
            Transform(k[2][5], k[3][7]),
            Transform(k[2][6], k[3][8]),
            Transform(k[2][7], k[3][9]),
        )
        zgas([k[2][1], k[2][4]],
             [k[3][1], k[3][2], k[3][5], k[3][6]], k[3])

        self.next_section("krok5")
        # Suma w wykladniku rozdziela sie na iloczyn poteg: a^{r+s} = a^r * a^s.
        # Zielony jest doklejony kawalek sumy, bo przestaje byc czescia wykladnika,
        # oraz to, czego wczesniej nie bylo: druga dwojka, kropka mnozenia i * 1
        # przy trzecim skladniku. Samo 96 zostaje na swoim miejscu, wiec czarne.
        zapal(k[3][2], k[3][6])
        for cel in (k[4][2], k[4][3], k[4][4], k[4][8], k[4][9], k[4][10], k[4][14], k[4][15]):
            cel.set_color(self.ZIELONY)
        self.play(
            Transform(k[3][0], k[4][0]),
            Transform(k[3][1], k[4][1]),                 # 2^96 zostaje
            Transform(k[3][2][1], k[4][4]),              # 4 z sumy -> wykladnik
            FadeOut(k[3][2][0]),                         # plus z wykladnika
            FadeIn(k[4][2]), FadeIn(k[4][3]),            # kropka i druga dwojka
            Transform(k[3][3], k[4][5]),
            Transform(k[3][4], k[4][6]),
            Transform(k[3][5], k[4][7]),
            Transform(k[3][6][1], k[4][10]),             # 2 z sumy -> wykladnik
            FadeOut(k[3][6][0]),
            FadeIn(k[4][8]), FadeIn(k[4][9]),
            Transform(k[3][7], k[4][11]),
            Transform(k[3][8], k[4][12]),
            Transform(k[3][9], k[4][13]),
            FadeIn(k[4][14]), FadeIn(k[4][15]),          # kropka i jedynka
        )
        zgas([k[3][2][1], k[4][2], k[4][3], k[4][8], k[4][9], k[4][14], k[4][15]],
             [k[4][2], k[4][3], k[4][4], k[4][8], k[4][9], k[4][10], k[4][14], k[4][15]], k[4])

        self.next_section("krok6")
        # Wylaczenie 2^96 przed nawias. Pierwsze 2^96 zostaje w zapisie i tylko
        # jedzie na przod, wiec jest czarne. Dwa pozostale znikaja, wiec sa
        # zielone, a razem z nimi nawiasy, ktorych wczesniej nie bylo.
        zapal(k[4][6], k[4][7], k[4][8], k[4][12], k[4][13], k[4][14])
        k[5][3].set_color(self.ZIELONY)
        k[5][11].set_color(self.ZIELONY)
        self.play(
            Transform(k[4][0], k[5][0]),                 # 2^96, ktore zostaje
            Transform(k[4][1], k[5][1]),
            Transform(k[4][2], k[5][2]),                 # kropka przed nawiasem
            FadeIn(k[5][3]),                             # nawias otwierajacy
            Transform(k[4][3], k[5][4]),
            Transform(k[4][4], k[5][5]),
            Transform(k[4][5], k[5][6]),
            FadeOut(VGroup(k[4][6], k[4][7], k[4][8])),  # drugie 2^96 z kropka
            Transform(k[4][9], k[5][7]),
            Transform(k[4][10], k[5][8]),
            Transform(k[4][11], k[5][9]),
            FadeOut(VGroup(k[4][12], k[4][13], k[4][14])),  # trzecie 2^96 z kropka
            Transform(k[4][15], k[5][10]),               # jedynka po trzecim skladniku
            FadeIn(k[5][11]),                            # nawias zamykajacy
        )
        zgas([k[5][3], k[5][11]], [k[5][3], k[5][11]], k[5])

        self.next_section("krok7")
        # Liczymy potegi w nawiasie. Zmieniaja sie wartosci, wiec sa zielone.
        zapal(k[5][4], k[5][5], k[5][7], k[5][8])
        k[6][4].set_color(self.ZIELONY)
        k[6][6].set_color(self.ZIELONY)
        self.play(
            Transform(k[5][0], k[6][0]),
            Transform(k[5][1], k[6][1]),
            Transform(k[5][2], k[6][2]),
            Transform(k[5][3], k[6][3]),
            Transform(VGroup(k[5][4], k[5][5]), k[6][4]),   # 2^4 -> 16
            Transform(k[5][6], k[6][5]),
            Transform(VGroup(k[5][7], k[5][8]), k[6][6]),   # 2^2 -> 4
            Transform(k[5][9], k[6][7]),
            Transform(k[5][10], k[6][8]),
            Transform(k[5][11], k[6][9]),
        )
        zgas([k[5][4], k[5][7]], [k[6][4], k[6][6]], k[6])

        self.next_section("krok8")
        # Dodajemy w nawiasie. Trzy skladniki zlewaja sie w jedna liczbe,
        # a nawiasy przestaja byc potrzebne, wiec wszystko to jest zielone.
        zapal(k[6][3], k[6][4], k[6][5], k[6][6], k[6][7], k[6][8], k[6][9])
        k[7][3].set_color(self.ZIELONY)
        self.play(
            Transform(k[6][0], k[7][0]),
            Transform(k[6][1], k[7][1]),
            Transform(k[6][2], k[7][2]),
            Transform(VGroup(k[6][4], k[6][5], k[6][6], k[6][7], k[6][8]), k[7][3]),
            FadeOut(k[6][3]), FadeOut(k[6][9]),
        )
        zgas([k[6][4], k[7][3]], [k[7][3]], k[7])


# ---------------------------------------------------------------------------
# DAWNA WERSJA SCENY (kod Henricha, sprzed przepisania na zasady z 2026-08-21).
# Zostawiona zakomentowana na czas sprawdzenia nowej wersji; do usuniecia,
# gdy Henrich potwierdzi, ze nowe kroki sa w porzadku.
# ---------------------------------------------------------------------------

# from manim import *
#
# class ScenaZadania3(Scene):
#
#     def construct(self):
#         GREEN = "#0AB32F"
#         GRAY = "#A6A6A6"
#
#         #for now WORKS ONLY WITH KROKI!!!
#         def TransformSplit(step, indexs1, indexs2):
#             transforms = []
#             for i in range(len(indexs1)):
#
#                 if( i != len(indexs1) -  1):
#                     transforms.append(
#                         Transform(
#                             kroki[step][0][indexs1[i]:indexs1[i+1]],
#                             kroki[step+1][0][indexs2[i]:indexs2[i+1]],
#                             run_time=1.4
#                         )
#                     )
#                 else:
#                     transforms.append(
#                         Transform(
#                             kroki[step][0][indexs1[i]:],
#                             kroki[step+1][0][indexs2[i]:],
#                             run_time=1.4
#                         )
#                     )
#
#             return transforms
#         #UWAGA PARY!!
#         def TransformSplitPAIRS(step, indexs1, indexs2):
#             if len(indexs1) % 2 != 0 or len(indexs2) != len(indexs1):
#                 raise ValueError("ZŁA DŁUGOŚĆ LISTY INDEXS, MUSZĄ BYĆ PARZYSTE I TAKIE SAME")
#
#             transforms = []
#             for i in range(len(indexs1)):
#                 if( i != len(indexs1) - 1  and  i%2 == 0):
#                     transforms.append(
#                         Transform(
#                             kroki[step][0][indexs1[i]:indexs1[i+1]],
#                             kroki[step+1][0][indexs2[i]:indexs2[i+1]],
#                             run_time=1.4
#                         )
#                     )
#
#             return transforms
#
#
#
#         # Wzory pomocnicze NIE są już rysowane w filmie (ujednolicone z zad. 2
#         # 2026-08-12; zmiana zasady jest z 2026-08-11). Pokazuje je strona, jako
#         # KaTeX pod filmem — patrz pole "text" przy kroku w exercises.json.
#         # Definicje zostają tutaj jako źródło wiedzy, który wzór należy do którego
#         # kroku; scena ich nie dodaje.
#         #   krok 3 → (a^r)^s = a^{r·s}
#         #   krok 5 → a^r · a^s = a^{r+s}
#         wzory = [MathTex()] * 6
#         wzory[1] = MathTex(r"(a^r)^s=a^{r \cdot s}")
#         wzory[2] = MathTex(r"a^r\cdot a^s=a^{r+s}")
#
#         for wzor in wzory:
#             wzor.fill_color=BLACK
#             wzor.font_size=100
#
#
#
#         kroki = [MathTex()] * 8
#         kroki[0] = MathTex(r"2^{100} + 4^{49} + 16^{24}")
#         kroki[1] = MathTex(r"2^{100} + (2^2)^{49} + (2^4) ^{24}")
#         kroki[2] = MathTex(r"2^{100} + 2^{98} + 2^{96}")
#         kroki[3] = MathTex(r"2^{96+4} + 2^{96+2} + 2^{96}")
#         kroki[4] = MathTex(r"2^{96} \cdot 2^4 + 2^{96} \cdot 2^2 + 2^{96} \cdot 1")
#         kroki[5] = MathTex(r"2^{96} \cdot (2^4 + 2^2 + 1)")
#         kroki[6] = MathTex(r"2^{96} \cdot (16 + 4 + 1)")
#         kroki[7] = MathTex(r"2^{96} \cdot 21")
#         #kroki[8] = MathTex(r"2^{96} jest liczbą całkowitą. To co nam wyszło jest wielokrotnością 21, więc jest podzielne przez 21.")
#         #Latex nie lubi polski znaków :(
#
#         for krok in kroki:
#             krok.fill_color=BLACK
#             krok.font_size=90
#
#         # Ten krok jest najdłuższy (trzy iloczyny), więc od początku był pisany
#         # mniejszą czcionką.
#         kroki[4].font_size=75
#
#         # Kadr od 2026-08-11 jest 16:9 (1280x720), a nie 21:9 (840x360) — patrz
#         # manim.cfg. Treść stoi teraz na ŚRODKU: przesunięcie w lewo (LEFT*4.5)
#         # trzymało z prawej miejsce na wzór pomocniczy, a ten wyszedł z filmu.
#         # Skala jest WSPÓLNA dla wszystkich kroków i liczona z najszerszego — gdyby
#         # każdy krok dopasowywał się osobno, litery zmieniałyby rozmiar w trakcie
#         # przekształcenia, a Transform robiłby z tego zoom. Względne różnice
#         # wielkości (krok 5 mniejszy) zostają, bo mnożymy wszystko tak samo.
#         MARGINES = 0.85
#         najszerszy = max(krok.width for krok in kroki)
#         if najszerszy > config.frame_width * MARGINES:
#             wspolczynnik = config.frame_width * MARGINES / najszerszy
#             for krok in kroki:
#                 krok.scale(wspolczynnik)
#         for krok in kroki:
#             krok.move_to(ORIGIN)
#
#
#
#         # KROKI JAKO SEKCJE (przebudowa 2026-08-12) — render:
#         #     manim --save_sections solutionZad3.py ScenaZadania3
#         # kładzie każdy krok osobnym plikiem w sections/. Każda sekcja kończy się
#         # `self.wait(0.25)` PRZED sprzątaniem sceny: bez przytrzymania przeglądarka
#         # gubi ostatnie klatki, a po `self.clear()` trzymałoby się białą planszę.
#
#         self.next_section("krok1")
#         #STEP 1
#         #self.add(Text("STEP 1", font_size=70, color=BLACK).shift(UP*2))
#         self.play(Create(kroki[0]))
#         self.wait(0.25)
#         self.clear()
#
#
#
#         self.next_section("krok2")
#         #STEP 2
#         #self.add(Text("STEP 2", font_size=70, color=BLACK).shift(UP*2))
#         temp_krok = kroki[0].copy()
#         kroki[0][0][:].set_color(GRAY)
#         kroki[1][0][:].set_color(GRAY)
#
#
#         kroki[0][0][5].set_color(BLACK)
#         kroki[0][0][9:11].set_color(BLACK)
#
#         kroki[1][0][5:9].set_color(BLACK)
#         kroki[1][0][12:16].set_color(BLACK)
#         self.play(ReplacementTransform(temp_krok, kroki[0]))
#         self.wait(1)
#         #self.play(Transform(kroki[0][0][0:5], kroki[1][0][0:5]), Transform(kroki[0][0][5], kroki[1][0][5:9]), Transform(kroki[0][0][6:9], kroki[1][0][9:12]), Transform(kroki[0][0][9:11], kroki[1][0][12:15]), Transform(kroki[0][0][11:], kroki[1][0][15:]))
#         self.play(TransformSplit(0, [0, 5, 6, 9, 11], [0, 5, 9, 12, 15]))
#
#         # ROZJAŚNIENIE na koniec kroku (Henrich, 2026-08-12). Na ekranie siedzą
#         # kawałki kroki[0][0] przekształcone w kroki[1] — i to one trzymają szary
#         # kolor, bo Transform interpoluje barwę do celu. Samo pomalowanie kroki[1]
#         # na czarno niczego nie zmieniało: to nie ten obiekt jest w kadrze.
#         # Bez tego krok kończył się na wpół przyciemnionym zapisie, a następny
#         # startował czysty — w odtwarzaczu to jest ta sama klatka, więc było widać
#         # przeskok. Pilnuje tego tools/styk-klatek.sh.
#         self.wait(0.35)
#         self.play(kroki[0][0].animate.set_color(BLACK), run_time=0.4)
#         kroki[1][0][:].set_color(BLACK)
#
#         self.wait(0.25)
#         self.clear()
#
#
#         self.next_section("krok3")
#         #STEP 3
#         #self.add(Text("STEP 3", font_size=70, color=BLACK).shift(UP*2))
#
#         self.add(kroki[1])
#
#         self.play(TransformSplit(1, [0, 7, 11, 14],
#                                     [0, 6, 8, 10]))
#         self.wait(0.25)
#         self.clear()
#
#
#
#         self.next_section("krok4")
#         #STEP 4
#         #self.add(Text("STEP 4", font_size=70, color=BLACK).shift(UP*2))
#
#
#         temp_krok = kroki[2].copy()
#         kroki[2][0][:].set_color(GRAY)
#         kroki[3][0][:].set_color(GRAY)
#
#         kroki[2][0][1:4].set_color(BLACK)
#         kroki[2][0][6:8].set_color(BLACK)
#
#         kroki[3][0][1:5].set_color(BLACK)
#         kroki[3][0][7:11].set_color(BLACK)
#
#
#         self.play(ReplacementTransform(temp_krok, kroki[2]))
#         self.wait(1)
#         self.play(TransformSplit(2, [0, 1, 4, 6, 8, 10], [0, 1, 5, 7, 11, 13]))
#
#
#         # Rozjaśnienie na koniec kroku — patrz komentarz przy kroku 2.
#         self.wait(0.35)
#         self.play(kroki[2][0].animate.set_color(BLACK), run_time=0.4)
#         kroki[3][0][:].set_color(BLACK)
#         self.wait(0.25)
#         self.clear()
#
#
#
#
#         self.next_section("krok5")
#         #STEP 5
#         #self.add(Text("STEP 5", font_size=70, color=BLACK).shift(UP*2))
#         self.add(kroki[3])
#
#         #self.add(index_labels(kroki[3][0]))
#         # Bez postoju na wejściu (2026-08-20): ten zapis stoi już na ostatniej
#         # klatce kroku 4, więc sekunda bezruchu tylko wydłużała film.
#         self.play(TransformSplit(3, [0, 3, 5, 9, 11, 13], [0, 3, 6, 10, 13, 17]))
#
#         self.wait(0.25)
#         self.clear()
#
#
#
#
#
#         self.next_section("krok6")
#         #STEP 6
#
#         temp_krok = kroki[4].copy()
#         kroki[4][0][:].set_color(GRAY)
#         kroki[5][0][:].set_color(GRAY)
#
#         kroki[4][0][0:3].set_color(BLACK)
#         kroki[4][0][7:10].set_color(BLACK)
#         kroki[4][0][14:17].set_color(BLACK)
#
#         kroki[5][0][0:3].set_color(BLACK)
#
#         #self.add(Text("STEP 6", font_size=70, color=BLACK).shift(UP*2))
#         #self.add(index_labels(kroki[4][0]).shift(UP*.5))
#
#         self.play(ReplacementTransform(temp_krok, kroki[4]))
#         self.wait(1)
#         self.play(TransformSplitPAIRS(4, [0, 4,  4, 7,  7, 11,  11, 14,  14, 18,  18, 99],
#                                          [0, 5,  5, 8,  0,  3,   8, 11,   0,  3,  11, 99]))
#
#         # Trzy kopie 2^96 zjeżdżają na to samo miejsce (o to chodzi w wyłączaniu
#         # przed nawias), ale Transform zostawia wszystkie trzy w scenie. Na klatce
#         # spoczynku zapis robił się przez to grubszy niż pierwsza klatka kroku 7 —
#         # wychodziło to na SSIM 0,9990. Dwie nadmiarowe kopie usuwamy.
#         self.remove(*kroki[4][0][7:11], *kroki[4][0][14:18])
#
#         # Rozjaśnienie na koniec kroku — patrz komentarz przy kroku 2.
#         self.wait(0.35)
#         self.play(kroki[4][0].animate.set_color(BLACK), run_time=0.4)
#         kroki[5][0][:].set_color(BLACK)
#
#         self.wait(0.25)
#         self.clear()
#
#         self.next_section("krok7")
#         #STEP 7
#         #self.add(Text("STEP 7", font_size=70, color=BLACK).shift(UP*2))
#         #self.add(index_labels(kroki[5][0]).shift(UP*.5))
#
#         self.add(kroki[5])
#         self.play(TransformSplit(5, [0, 5], [0, 5]))
#         self.wait(0.25)
#         self.clear()
#
#
#
#         self.next_section("krok8")
#         #STEP 8
#         #self.add(Text("STEP 8", font_size=70, color=BLACK).shift(UP*2))
#         self.add(kroki[6])
#         self.play(TransformSplit(6, [0, 4], [0, 4]))
#         self.wait(0.25)
#         self.clear()
#
#
#
#
