from manim import *


class ScenaZadania2(Scene):
    """Zadanie 2, grudzień 2024: (⁵√5 · 1/5)^(-5).

    OSIEM KROKÓW, jeden do jednego z ośmioma linijkami rachunku w rozwiązaniu
    opisowym (pole solutionText w matura/2024-grudzien/exercises.json).
    Zmieniając jedno, popraw drugie.

    KAŻDY KROK MA TEN SAM PRZEBIEG (zasada Henricha, 2026-08-21):

        1. wszystko czarne,
        2. kluczowy element zapala się na zielono,
        3. animacja przekształcenia, zielone zostaje zielone,
        4. wszystko znów czarne.

    ZIELONE JEST TO, CO SIĘ ZMIENIA: znika, pojawia się, zmienia wartość albo
    zmienia rolę. Czarne zostaje to, co jedzie w nowe miejsce zapisu, ale dalej
    znaczy to samo.

    Krok 3, 1/5 staje się 5^(-1): piątka dalej jest tą samą piątką i tylko jedzie
    na podstawę, więc jest CZARNA. Krok idzie DWIEMA animacjami, bo brakującego
    ogniwa (5 = 5^1) nie widać w zapisie z zadania, a bez niego jedynka leciałaby
    z licznika ułamka wprost do wykładnika, czyli przez pół kadru, między miejsca,
    które nic ze sobą nie mają (polecenie Henricha, 2026-08-23; README, punkt 17):

        A. przy piątce w mianowniku POJAWIA SIĘ zielona jedynka: 1/5 = 1/5^1,
        B. ta sama jedynka jedzie na miejsce wykładnika, a w tym samym ruchu
           „1/" znika i przed jedynką pojawia się minus.

    Zielona jest tylko jedynka (bohater kroku) i minus (pojawia się z niczego).
    Znikający licznik i kreska zostają czarne: gdyby i one były zielone, kolor
    przestałby wskazywać, na co patrzeć.

    Krok 2, ⁵√5 staje się 5^(1/5): liczba spod pierwiastka była podstawą i nią
    zostaje, więc CZARNA. Zielony jest znak pierwiastka (znika), licznik 1
    (pojawia się) i stopień pierwiastka, bo przestaje być stopniem, a zaczyna
    być mianownikiem wykładnika.

    Krok jest przez to SAMODZIELNY: zaczyna się i kończy tym samym, czystym
    obrazem. Dzięki temu ostatnia klatka kroku N zgadza się z pierwszą klatką
    kroku N+1 (zasada 1 z README) bez żadnych sztuczek z przenoszeniem
    podświetlenia między plikami, a uczeń widzi kolor dokładnie wtedy, kiedy
    coś się rusza.

    RUCH ZAMIAST MORFOWANIA. Stany są MathTexem pociętym na CZĘŚCI, a pary
    wskazane ręcznie co do glifu. Bez tego Manim paruje kształty po podobieństwie
    i podstawa potęgi „przelewa się" w inną podstawę zamiast po prostu do niej
    dojechać (README, „Ruch ma odpowiadać rachunkowi").
    """

    # Ten sam zielony, którym rozwiązanie opisowe obok filmu zaznacza fragment,
    # do którego odnosi się wzór: token --accent-green z COLORS.md, rola
    # „oznaczenie miejsca", a NIE zieleń poprawności. Wpisany hexem, bo Manim
    # nie widzi CSS-a; w ciemnym motywie film przechodzi przez filtr strony.
    ZIELONY = "#2e7d32"

    # MAPA GLIFÓW. Numery policzone z wyrenderowanego podglądu, nie zgadnięte.
    #
    #   \sqrt[5]{5}                0 stopień 5   1 znak pierwiastka   2 kreska   3 liczba 5
    #   \frac{1}{5}                0 licznik 1   1 kreska   2 mianownik 5
    #   \frac{1}{5^{1}}            0 licznik 1   1 kreska   2 mianownik 5   3 wykładnik 1
    #   ^{\frac{1}{5}}             0 licznik 1   1 kreska   2 mianownik 5
    #   ^{-5}  oraz  ^{-1}         0 minus       1 cyfra
    #   ^{\frac{1}{5}\cdot(-5)}    0 1  1 kreska  2 5  3 kropka  4 (  5 minus  6 5  7 )
    #   ^{(-1)\cdot(-5)}           0 (  1 minus  2 1  3 )  4 kropka  5 (  6 minus  7 5  8 )

    ZAPALANIE = 0.4   # sekundy; tyle trwa samo zapalenie i samo zgaszenie koloru

    def construct(self):

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
        # przylecieć ze swojej strony.
        k[6] = MathTex(r"5", r"^{-1", r"+5}")
        k[7] = MathTex(r"5", r"^{4}")

        # STAN POŚREDNI kroku 3, między k[1] a k[2]. Nie jest osobnym krokiem
        # filmu: kropek zostaje osiem, a ten zapis żyje tylko wewnątrz kroku 3
        # jako brakujące ogniwo 5 = 5^1.
        kp = MathTex(r"\left(", r"5", r"^{\frac{1}{5}}", r"\cdot", r"\frac{1}{5^{1}}",
                     r"\right)", r"^{-5}")
        k.append(kp)

        for stan in k:
            stan.fill_color = BLACK
            stan.font_size = 120

        # Skala WSPÓLNA dla wszystkich kroków, liczona z najszerszego: gdyby każdy
        # krok dopasowywał się osobno, litery zmieniałyby rozmiar w trakcie
        # przekształcenia i Transform robiłby z tego zoom.
        MARGINES = 0.85
        najszerszy = max(stan.width for stan in k)
        if najszerszy > config.frame_width * MARGINES:
            wspolczynnik = config.frame_width * MARGINES / najszerszy
            for stan in k:
                stan.scale(wspolczynnik)
        for stan in k:
            stan.move_to(ORIGIN)

        def zapal(*co):
            """Krok 2 przebiegu: kluczowy element zapala się na zielono."""
            self.play(*[m.animate.set_color(self.ZIELONY) for m in co],
                      run_time=self.ZAPALANIE)

        def zgas(zrodla, cele, nastepny):
            """Kroki 4 i domknięcie: wszystko wraca do czerni, scena na czysto.

            `zrodla` to obiekty LEŻĄCE NA EKRANIE po przekształceniu (po Transform
            zostają obiekty źródłowe, tyle że wyglądające jak cel), więc to je
            trzeba wygasić animacją. `cele` leżą poza sceną i wystarczy im zwykłe
            set_color, ale zrobić to trzeba, bo za chwilę to one wjeżdżają na
            ekran jako czysty stan następnego kroku.

            Podmiana stanu idzie PRZED przytrzymaniem, żeby te 0,25 s pokazywało
            czysty obiekt następnego stanu, a nie obiekty po Transform, które
            potrafią różnić się od niego drobiazgami. README ostrzega przed
            self.clear() przed self.wait(), ale ostrzeżenie dotyczy czyszczenia
            BEZ dodania czegokolwiek w zamian: wtedy przez 0,25 s stoi pusta
            plansza i to ona zostaje uczniowi na ekranie.
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
        # Zapisujemy działanie z zadania. Nic się jeszcze nie zmienia, więc nie ma
        # czego zaznaczać.
        self.play(Create(k[0]))
        zgas([], [], k[0])

        self.next_section("krok2")
        # Pierwiastek na potęgę o wykładniku ułamkowym. Pierwiastek się nie
        # „przelewa" w potęgę, tylko rozpada na kawałki, z których każdy ma swoje
        # miejsce w rachunku:
        #
        #   liczba spod pierwiastka  ->  podstawa potęgi
        #   stopień pierwiastka      ->  mianownik wykładnika   (na zielono)
        #   kreska pierwiastka       ->  kreska ułamka
        #   znak pierwiastka znika, licznik 1 się pojawia      (na zielono)
        #
        # Zielony bierze to, co przestaje znaczyć to, co znaczyło. Znak pierwiastka
        # znika, licznik 1 pojawia się z niczego, a stopień pierwiastka przestaje
        # być stopniem i zaczyna być mianownikiem wykładnika: mimo że dalej jest
        # piątką, jego rola się zmienia, więc też jest zielony.
        # Czarna zostaje liczba spod pierwiastka: była podstawą potęgowania i nią
        # zostaje, tylko przesuwa się w inne miejsce zapisu.
        zapal(k[0][1][1], k[0][1][0])
        k[1][2][0].set_color(self.ZIELONY)
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
        zgas([k[0][1][0], k[1][2][0]], [k[1][2][0], k[1][2][2]], k[1])

        self.next_section("krok3")
        # Ułamek 1/5 na potęgę o ujemnym wykładniku. DWIE ANIMACJE w jednym kroku,
        # bo jedynka z licznika i jedynka w wykładniku to NIE JEST ta sama jedynka:
        # gdyby licznik poleciał wprost do wykładnika, uczeń zobaczyłby lot przez
        # pół kadru i nie wiedziałby, co się właściwie stało.
        #
        #   A. przy piątce w mianowniku pojawia się jedynka:  1/5 = 1/5^1
        #   B. ta jedynka wychodzi ponad kreskę i staje się wykładnikiem, „1/"
        #      znika, a przed jedynką pojawia się minus:      1/5^1 = 5^{-1}

        # ANIMACJA A. Zapis się rozsuwa, żeby zrobić miejsce na wykładnik; nic
        # jeszcze nie zmienia miejsca w rachunku, więc rozsuwa się na czarno.
        # Zielona jest sama jedynka, bo tylko ona się pojawia.
        kp[4][3].set_color(self.ZIELONY)
        self.play(
            Transform(k[1][0], kp[0]),
            Transform(k[1][1], kp[1]),
            Transform(k[1][2], kp[2]),
            Transform(k[1][3], kp[3]),
            Transform(k[1][4][0], kp[4][0]),     # licznik 1
            Transform(k[1][4][1], kp[4][1]),     # kreska ułamka
            Transform(k[1][4][2], kp[4][2]),     # mianownik 5
            Transform(k[1][5], kp[5]),
            Transform(k[1][6], kp[6]),
            FadeIn(kp[4][3]),                    # jedynka: wykładnik piątki
        )
        self.wait(0.35)

        # ANIMACJA B. Zielona jedynka jedzie na miejsce wykładnika przy podstawie,
        # a to, co przestaje być potrzebne, znika w tym samym ruchu. Minus pojawia
        # się z niczego, więc też jest zielony. Piątka zostaje piątką i tylko jedzie
        # na podstawę, więc jest czarna.
        k[2][5][0].set_color(self.ZIELONY)
        self.play(
            Transform(k[1][0], k[2][0]),
            Transform(k[1][1], k[2][1]),         # podstawa pierwszego czynnika
            Transform(k[1][2], k[2][2]),
            Transform(k[1][3], k[2][3]),
            Transform(k[1][4][2], k[2][4]),      # mianownik 5 -> podstawa
            Transform(kp[4][3], k[2][5][1]),     # zielona jedynka -> cyfra wykładnika
            FadeOut(k[1][4][0]), FadeOut(k[1][4][1]),   # „1/" znika
            FadeIn(k[2][5][0]),                  # minus, którego wcześniej nie było
            Transform(k[1][5], k[2][6]),
            Transform(k[1][6], k[2][7]),
        )
        # W kadrze zostają zielone: jedynka (obiekt kp, źródło ostatniego Transform)
        # i minus (dodany FadeIn-em). Licznika i kreski nie gasimy, bo wyszły
        # z kadru FadeOut-em, a animacja na obiekcie spoza sceny wstawiłaby go z powrotem.
        zgas([kp[4][3], k[2][5][0]], [k[2][5]], k[2])

        self.next_section("krok4")
        # Opuszczenie nawiasu: (a·b)^r = a^r · b^r. Sedno kroku to ROZDWOJENIE
        # wykładnika -5, więc on się zapala, a jego kopia leci na drugi czynnik.
        # Kopie robimy PRZED zapaleniem, żeby zapaliły się razem z oryginałem
        # (leżą dokładnie na nim, więc widać jedno).
        kopia_wykladnika = k[2][7].copy()
        kopia_nawiasu_l = k[2][0].copy()
        kopia_nawiasu_p = k[2][6].copy()
        zapal(k[2][7], kopia_wykladnika)
        k[3][4].set_color(self.ZIELONY)
        k[3][10].set_color(self.ZIELONY)
        self.play(
            Transform(k[2][0], k[3][0]),
            Transform(k[2][1], k[3][1]),            # pierwsza podstawa 5
            Transform(k[2][2], k[3][2]),
            Transform(k[2][6], k[3][3]),
            Transform(k[2][7], k[3][4]),
            Transform(k[2][3], k[3][5]),            # kropka mnożenia
            Transform(kopia_nawiasu_l, k[3][6]),
            Transform(k[2][4], k[3][7]),            # druga podstawa 5
            Transform(k[2][5], k[3][8]),
            Transform(kopia_nawiasu_p, k[3][9]),
            Transform(kopia_wykladnika, k[3][10]),  # rozdwojony wykładnik
        )
        zgas([k[2][7], kopia_wykladnika], [k[3][4], k[3][10]], k[3])

        self.next_section("krok5")
        # Mnożenie wykładników: (a^r)^s = a^{r·s}. Nawiasy znikają, a oba
        # wykładniki zjeżdżają obok siebie do jednego wykładnika.
        #
        # Wykładnik -5 PRZESUWA SIĘ, cyfra po cyfrze, na swoje miejsce. Nawiasy
        # wokół (-5) i kropka mnożenia to jedyne rzeczy, których wcześniej nie
        # było, więc tylko one się pojawiają.
        zapal(k[3][4], k[3][10])
        k[4][1][5:7].set_color(self.ZIELONY)
        k[4][4][6:8].set_color(self.ZIELONY)
        self.play(
            FadeOut(k[3][0]), FadeOut(k[3][3]), FadeOut(k[3][6]), FadeOut(k[3][9]),
            Transform(k[3][1], k[4][0]),          # podstawa 5
            Transform(k[3][5], k[4][2]),          # kropka między czynnikami
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
        zgas([k[3][4], k[3][10]], [k[4][1], k[4][4]], k[4])

        self.next_section("krok6")
        # Same rachunki w wykładnikach, więc zapalają się wykładniki.
        # Podstawy stoją nieruchomo.
        zapal(k[4][1], k[4][4])
        k[5][1].set_color(self.ZIELONY)
        k[5][4].set_color(self.ZIELONY)
        self.play(
            Transform(k[4][0], k[5][0]),
            Transform(k[4][1], k[5][1]),
            Transform(k[4][2], k[5][2]),
            Transform(k[4][3], k[5][3]),
            Transform(k[4][4], k[5][4]),
        )
        zgas([k[4][1], k[4][4]], [k[5][1], k[5][4]], k[5])

        self.next_section("krok7")
        # Mnożenie potęg o tej samej podstawie: a^r · a^s = a^{r+s}. Dodają się
        # wykładniki, więc to one są zielone. Obie piątki dojeżdżają w to samo
        # miejsce, bo w rachunku zostaje jedna.
        zapal(k[5][1], k[5][4])
        k[6][1].set_color(self.ZIELONY)
        k[6][2].set_color(self.ZIELONY)
        self.play(
            Transform(k[5][0], k[6][0]),
            Transform(k[5][3], k[6][0].copy()),
            Transform(k[5][1], k[6][1]),
            Transform(k[5][4], k[6][2]),
            FadeOut(k[5][2]),
        )
        zgas([k[5][1], k[5][4]], [k[6][1], k[6][2]], k[6])

        self.next_section("krok8")
        # Dodanie w wykładniku. Podstawa stoi, zmienia się sam wykładnik.
        zapal(k[6][1], k[6][2])
        k[7][1].set_color(self.ZIELONY)
        self.play(
            Transform(k[6][0], k[7][0]),
            ReplacementTransform(VGroup(k[6][1], k[6][2]), k[7][1]),
        )
        zgas([k[7][1]], [k[7][1]], k[7])
