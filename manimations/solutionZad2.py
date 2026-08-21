from manim import *


class ScenaZadania2(Scene):
    """Zadanie 2, grudzień 2024: (⁵√5 · 1/5)^(-5).

    PRZEBUDOWA 2026-08-21. Scena miała sześć kroków, teraz ma osiem. Dwa kroki
    robiły po dwa przekształcenia naraz i przez to nie zgadzały się z rozwiązaniem
    opisowym w matura/2024-grudzien/exercises.json, które idzie linijka po linijce,
    jeden wzór na jedną linijkę. Rozbite zostały:

        krok 4: opuszczenie nawiasu ORAZ mnożenie wykładników  ->  kroki 4 i 5
        krok 6: dodanie wykładników ORAZ zsumowanie ich          ->  kroki 7 i 8

    Osiem kroków filmu odpowiada teraz jeden do jednego ośmiu linijkom rachunku
    w rozwiązaniu opisowym. Zmieniając jedno, popraw drugie.

    Druga zmiana z tego samego dnia: KAŻDA para glifów jest wskazana ręcznie.
    Wcześniej część przejść szła przez TransformMatchingShapes albo przez Transform
    na całych krokach, więc piątka będąca podstawą potęgi „przelewała się" w inną
    piątkę zamiast po prostu do niej dojechać. Zasada Henricha: co nie zmienia
    formy, ma się PRZESUWAĆ, nie morfować (manimations/README.md, „Ruch ma
    odpowiadać rachunkowi"). Stąd stany zapisane są jako MathTex pocięty na CZĘŚCI,
    a nie jako jeden napis: dzięki temu pary wskazuje się czytelnym indeksem części
    (k2[1] to podstawa, k2[2] to wykładnik), a nie zgadywanym numerem glifu.
    """

    # Ten sam zielony, którym rozwiązanie opisowe obok filmu zaznacza fragment,
    # do którego odnosi się wzór: token --accent-green z COLORS.md, rola
    # „oznaczenie miejsca", a NIE zieleń poprawności. Wpisany hexem, bo Manim
    # nie widzi CSS-a; w ciemnym motywie film przechodzi przez filtr strony.
    ZIELONY = "#2e7d32"

    # MAPA GLIFÓW. Numery policzone z wyrenderowanego podglądu, nie zgadnięte.
    # Bez niej pary trzeba by wskazywać na wyczucie, a wtedy Manim paruje kształty
    # po podobieństwie i piątka potrafi polecieć nie tam, gdzie idzie w rachunku.
    #
    #   \sqrt[5]{5}                0 stopień 5   1 znak pierwiastka   2 kreska   3 liczba 5
    #   \frac{1}{5}                0 licznik 1   1 kreska   2 mianownik 5
    #   ^{\frac{1}{5}}             0 licznik 1   1 kreska   2 mianownik 5
    #   ^{-5}  oraz  ^{-1}         0 minus       1 cyfra
    #   ^{\frac{1}{5}\cdot(-5)}    0 1  1 kreska  2 5  3 kropka  4 (  5 minus  6 5  7 )
    #   ^{(-1)\cdot(-5)}           0 (  1 minus  2 1  3 )  4 kropka  5 (  6 minus  7 5  8 )

    def construct(self):

        # Wzory pomocnicze NIE są rysowane w filmie (zmiana 2026-08-11).
        # Pokazuje je strona, jako KaTeX pod filmem, w polu "text" przy kroku
        # w exercises.json. Który wzór należy do którego kroku:
        #
        #   krok 2  ->  \sqrt[n]{a^m} = a^{m/n}
        #   krok 3  ->  a^{-n} = 1/a^n
        #   krok 4  ->  (a·b)^r = a^r · b^r
        #   krok 5  ->  (a^r)^s = a^{r·s}
        #   krok 6  ->  bez wzoru, samo mnożenie liczb
        #   krok 7  ->  a^r · a^s = a^{r+s}
        #   krok 8  ->  bez wzoru, samo dodawanie w wykładniku

        # STANY. Podział na części jest tak dobrany, żeby to, co przetrwa
        # przekształcenie (podstawa 5, kropka mnożenia, nawiasy), było OSOBNĄ
        # częścią i dało się je przesunąć w całości.
        k = [None] * 8
        k[0] = MathTex(r"\left(", r"\sqrt[5]{5}", r"\cdot", r"\frac{1}{5}", r"\right)", r"^{-5}")
        k[1] = MathTex(r"\left(", r"5", r"^{\frac{1}{5}}", r"\cdot", r"\frac{1}{5}", r"\right)", r"^{-5}")
        k[2] = MathTex(r"\left(", r"5", r"^{\frac{1}{5}}", r"\cdot", r"5", r"^{-1}", r"\right)", r"^{-5}")
        k[3] = MathTex(r"\left(", r"5", r"^{\frac{1}{5}}", r"\right)", r"^{-5}",
                       r"\cdot", r"\left(", r"5", r"^{-1}", r"\right)", r"^{-5}")
        k[4] = MathTex(r"5", r"^{\frac{1}{5}\cdot(-5)}", r"\cdot", r"5", r"^{(-1)\cdot(-5)}")
        k[5] = MathTex(r"5", r"^{-1}", r"\cdot", r"5", r"^{5}")
        # Wykładnik pocięty na dwie części, żeby każdy ze składników sumy mógł
        # przylecieć ze swojej strony. MathTex skleja części przed kompilacją,
        # więc "^{-1" i "+5}" osobno są poprawne po sklejeniu.
        k[6] = MathTex(r"5", r"^{-1", r"+5}")
        k[7] = MathTex(r"5", r"^{4}")

        for stan in k:
            stan.fill_color = BLACK
            stan.font_size = 120

        # Kadr jest 16:9 i film pokazuje samo działanie, więc treść stoi na środku.
        # Skala jest WSPÓLNA dla wszystkich kroków i liczona z najszerszego: gdyby
        # każdy krok dopasowywał się osobno, litery zmieniałyby rozmiar w trakcie
        # przekształcenia i Transform robiłby z tego zoom.
        MARGINES = 0.85
        najszerszy = max(stan.width for stan in k)
        if najszerszy > config.frame_width * MARGINES:
            wspolczynnik = config.frame_width * MARGINES / najszerszy
            for stan in k:
                stan.scale(wspolczynnik)
        for stan in k:
            stan.move_to(ORIGIN)

        # KROKI JAKO SEKCJE. Granice wyznacza self.next_section("krokN"),
        # a `manim --save_sections` zapisuje każdy krok osobnym plikiem.
        # Scena jedzie w całości, więc każdy krok zaczyna się dokładnie tam,
        # gdzie skończył poprzedni.
        #
        # KAŻDA sekcja kończy się self.wait(0.25) PRZED sprzątaniem: bez tego
        # przeglądarka zatrzymuje obraz kilka klatek przed końcem pliku i ostatni
        # element animacji nie zostaje na ekranie. Przytrzymanie PO wyczyszczeniu
        # trzymałoby pustą planszę i to ona zostawałaby uczniowi przed oczami.
        def domknij(nastepny):
            """Kończy sekcję i ustawia scenę na czysty obiekt następnego stanu.

            Po Transform na ekranie zostają obiekty POPRZEDNIEGO stanu, tyle że
            wyglądające jak następny. Podmiana na prawdziwy obiekt nie zmienia
            obrazu (te same kształty w tych samych miejscach), a kolejna sekcja
            może adresować części po indeksach.

            KOLEJNOŚĆ JEST WAŻNA: najpierw podmiana, DOPIERO POTEM przytrzymanie.
            README ostrzega przed self.clear() przed self.wait(), ale ostrzeżenie
            dotyczy czyszczenia BEZ dodania czegokolwiek w zamian: wtedy przez
            0,25 s stoi pusta plansza i to ona zostaje uczniowi na ekranie. Tutaj
            zamiana jest natychmiastowa i obraz się nie zmienia, a zysk jest taki,
            że przytrzymanie pokazuje CZYSTY następny stan. Gdyby było odwrotnie,
            0,25 s trzymałoby obiekty po Transform, które potrafią różnić się od
            czystego stanu (choćby kolorem podświetlenia), i ostatnia klatka kroku
            N nie zgadzałaby się z pierwszą klatką kroku N+1. Sprawdzone
            porównaniem klatek: różnica spada z ~2000 pikseli do szumu kompresji.
            """
            self.clear()
            self.add(nastepny)
            self.wait(0.25)

        self.next_section("krok1")
        # Zapisujemy działanie z zadania.
        self.play(Create(k[0]))
        domknij(k[0])

        self.next_section("krok2")
        # Pierwiastek na potęgę o wykładniku ułamkowym. Pierwiastek się nie
        # „przelewa" w potęgę: rozpada się na kawałki, z których każdy ma swoje
        # miejsce w rachunku.
        #
        #   liczba spod pierwiastka  ->  podstawa potęgi
        #   stopień pierwiastka      ->  mianownik wykładnika   (na zielono)
        #   kreska pierwiastka       ->  kreska ułamka
        #   znak pierwiastka znika, licznik 1 się pojawia
        #
        # Zielony zapala się W TRAKCIE animacji (źródło czarne, cel zielony), więc
        # pierwsza klatka tego kroku jest identyczna z ostatnią klatką kroku 1.
        # Gaśnie dopiero w kroku 3, też animacją. Dzięki temu podświetlenie stoi
        # dokładnie na klatce, na której uczeń zatrzymuje film, a żaden styk
        # dwóch plików nie przeskakuje.
        k[1][2][2].set_color(self.ZIELONY)
        self.play(
            Transform(k[0][0], k[1][0]),
            Transform(k[0][1][3], k[1][1]),      # liczba spod pierwiastka -> podstawa
            Transform(k[0][1][0], k[1][2][2]),   # stopień -> mianownik wykładnika
            Transform(k[0][1][2], k[1][2][1]),   # kreska pierwiastka -> kreska ułamka
            FadeOut(k[0][1][1]),                 # sam znak pierwiastka
            FadeIn(k[1][2][0]),                  # licznik 1, którego wcześniej nie było
            Transform(k[0][2], k[1][3]),
            Transform(k[0][3], k[1][4]),
            Transform(k[0][4], k[1][5]),
            Transform(k[0][5], k[1][6]),
        )
        domknij(k[1])

        self.next_section("krok3")
        # Ułamek 1/5 na potęgę o ujemnym wykładniku. Znowu nic nie morfuje:
        #
        #   piątka spod kreski  ->  podstawa potęgi   (na zielono)
        #   jedynka znad kreski ->  cyfra w wykładniku
        #   kreska ułamka       ->  minus w wykładniku
        #
        # Zielone podświetlenie z kroku 2 gaśnie tutaj samo: jego cel w tym kroku
        # jest czarny, więc kolor wraca do czerni w trakcie ruchu.
        k[2][4].set_color(self.ZIELONY)
        self.play(
            Transform(k[1][0], k[2][0]),
            Transform(k[1][1], k[2][1]),         # podstawa 5: przesunięcie
            Transform(k[1][2], k[2][2]),         # tu gaśnie zielony z kroku 2
            Transform(k[1][3], k[2][3]),
            Transform(k[1][4][2], k[2][4]),      # mianownik 5 -> podstawa
            Transform(k[1][4][0], k[2][5][1]),   # licznik 1 -> cyfra wykładnika
            Transform(k[1][4][1], k[2][5][0]),   # kreska ułamka -> minus
            Transform(k[1][5], k[2][6]),
            Transform(k[1][6], k[2][7]),
        )
        domknij(k[2])

        self.next_section("krok4")
        # Opuszczenie nawiasu: (a·b)^r = a^r · b^r.
        # Sedno kroku to ROZDWOJENIE wykładnika -5: kopia leci na drugi czynnik,
        # a obie podstawy tylko się rozjeżdżają.
        #
        # Na zielono OBA wykładniki -5, bo to one się rozdwajają. Zielony z kroku 3
        # gaśnie tu sam, bo jego cel (druga podstawa) jest w tym kroku czarny.
        k[3][4].set_color(self.ZIELONY)
        k[3][10].set_color(self.ZIELONY)
        self.play(
            Transform(k[2][0], k[3][0]),
            Transform(k[2][1], k[3][1]),          # pierwsza podstawa 5
            Transform(k[2][2], k[3][2]),
            Transform(k[2][6], k[3][3]),
            Transform(k[2][7], k[3][4]),
            Transform(k[2][3], k[3][5]),          # kropka mnożenia
            Transform(k[2][0].copy(), k[3][6]),   # drugi nawias: kopia pierwszego
            Transform(k[2][4], k[3][7]),          # druga podstawa 5
            Transform(k[2][5], k[3][8]),
            Transform(k[2][6].copy(), k[3][9]),
            Transform(k[2][7].copy(), k[3][10]),  # rozdwojony wykładnik
        )
        domknij(k[3])

        self.next_section("krok5")
        # Mnożenie wykładników: (a^r)^s = a^{r·s}. Nawiasy znikają, a oba
        # wykładniki zjeżdżają obok siebie do jednego wykładnika.
        #
        # Wykładnik -5 PRZESUWA SIĘ, cyfra po cyfrze, na swoje miejsce w nowym
        # wykładniku. Wcześniej cały stary wykładnik szedł jednym morfem na cały
        # nowy i minus z piątką rozpływały się w drodze. Nawiasy wokół (-5) i
        # kropka mnożenia to jedyne rzeczy, których wcześniej nie było, więc
        # tylko one się pojawiają.
        #
        # Zielony z kroku 4 gaśnie tu sam: cele w tym kroku są czarne.
        self.play(
            FadeOut(k[3][0]), FadeOut(k[3][3]), FadeOut(k[3][6]), FadeOut(k[3][9]),
            Transform(k[3][1], k[4][0]),          # podstawa 5
            Transform(k[3][5], k[4][2]),          # kropka mnożenia między czynnikami
            Transform(k[3][7], k[4][3]),          # podstawa 5
            # pierwszy czynnik: 1/5 zostaje, -5 dojeżdża za kropkę
            Transform(k[3][2][0], k[4][1][0]),    # licznik 1
            Transform(k[3][2][1], k[4][1][1]),    # kreska
            Transform(k[3][2][2], k[4][1][2]),    # mianownik 5
            Transform(k[3][4][0], k[4][1][5]),    # minus z -5
            Transform(k[3][4][1], k[4][1][6]),    # piątka z -5
            FadeIn(k[4][1][3]), FadeIn(k[4][1][4]), FadeIn(k[4][1][7]),
            # drugi czynnik: to samo z -1 i -5
            Transform(k[3][8][0], k[4][4][1]),    # minus z -1
            Transform(k[3][8][1], k[4][4][2]),    # jedynka
            Transform(k[3][10][0], k[4][4][6]),   # minus z -5
            Transform(k[3][10][1], k[4][4][7]),   # piątka z -5
            FadeIn(k[4][4][0]), FadeIn(k[4][4][3]), FadeIn(k[4][4][4]),
            FadeIn(k[4][4][5]), FadeIn(k[4][4][8]),
        )
        domknij(k[4])

        self.next_section("krok6")
        # Same rachunki w wykładnikach. Podstawy stoją nieruchomo.
        self.play(
            Transform(k[4][0], k[5][0]),
            Transform(k[4][1], k[5][1]),
            Transform(k[4][2], k[5][2]),
            Transform(k[4][3], k[5][3]),
            Transform(k[4][4], k[5][4]),
        )
        domknij(k[5])

        self.next_section("krok7")
        # Mnożenie potęg o tej samej podstawie: a^r · a^s = a^{r+s}.
        # Obie piątki dojeżdżają w to samo miejsce, bo w rachunku zostaje jedna.
        self.play(
            Transform(k[5][0], k[6][0]),
            Transform(k[5][3], k[6][0].copy()),
            Transform(k[5][1], k[6][1]),
            Transform(k[5][4], k[6][2]),
            FadeOut(k[5][2]),
        )
        domknij(k[6])

        self.next_section("krok8")
        # Dodanie w wykładniku. Podstawa stoi, zmienia się sam wykładnik.
        self.play(
            Transform(k[6][0], k[7][0]),
            ReplacementTransform(VGroup(k[6][1], k[6][2]), k[7][1]),
        )
        self.wait(0.25)
