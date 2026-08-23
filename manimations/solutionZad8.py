from manim import *


class Zad8(Scene):
    """Zadanie 8, grudzien 2024: rozwiaz (x+3)/(x-1) = x/(2x-2). Wynik x = -6.

    DZIEWIEC KROKOW, jeden do jednego z rozwiazaniem opisowym (pole solutionText
    w matura/2024-grudzien/exercises.json): siedem linijek rachunku, zalozenie
    nad nimi i zdanie ze sprawdzeniem pod nimi. Zmieniasz jedno, popraw drugie.

    SCENA NAPISANA OD NOWA 2026-08-23 (polecenie Henricha). Poprzednia wersja
    powstala przed zasadami z 21 sierpnia i lamala je wszystkie naraz: caly ruch
    szedl przez TransformMatchingShapes (paruje glify po podobienstwie, wiec
    cyfry lecialy nie tam, gdzie ida w rachunku), kolor byl ustawiany PRZED
    animacja (czyli pierwsza klatka kroku byla juz podswietlona), zalozenie bylo
    szare, a mnozenie obu stron i skracanie mianownikow dzialo sie w jednym kroku.

    UKLAD KADRU. Rownanie stoi nad srodkiem, bo od kroku 2 pod nim siedzi
    zalozenie, a od kroku 9 jeszcze sprawdzenie. Miejsce rezerwujemy OD RAZU,
    inaczej caly zapis podskakiwalby w chwili, gdy cos sie pod nim pojawia.

    ZALOZENIE ZOSTAJE NA EKRANIE DO KONCA. CKE daje za nie osobny punkt, wiec ma
    byc widoczne przez caly film, a nie mignac w jednym kroku. Dlatego kazdy krok
    konczy sie podmiana sceny na VGroup(rownanie, zalozenie), a nie na samo
    rownanie.

    KAZDY KROK MA TEN SAM PRZEBIEG: wszystko czarne, kluczowy element zapala sie
    na zielono, animacja przeksztalcenia, wszystko znowu czarne. Dzieki temu
    ostatnia klatka kroku N zgadza sie z pierwsza klatka kroku N+1.

    ZIELONE JEST TO, CO SIE ZMIENIA: znika, pojawia sie, zmienia wartosc albo
    zmienia role. Czarne zostaje to, co jedzie w nowe miejsce zapisu, ale dalej
    znaczy to samo. Nawiasow nie kolorujemy.

    Render: tools/wgraj-kroki.sh 8
    """

    ZIELONY = "#2e7d32"
    ZAPALANIE = 0.4

    # MAPA GLIFOW. Policzona z wyrenderowanego podgladu, nie zgadnieta.
    #
    #   \frac{x+3}{x-1}          0 x  1 +  2 3  3 kreska ulamka  4 x  5 minus  6 1
    #   \frac{x}{2x-2}           0 x  1 kreska ulamka  2 dwojka  3 x  4 minus  5 dwojka
    #   \frac{x}{2(x-1)}         0 x  1 kreska  2 dwojka  3 (  4 x  5 minus  6 1  7 )
    #   \;\big/ \cdot\, 2(x-1)   0 ukosnik  1 kropka  2 dwojka  3 (  4 x  5 minus  6 1  7 )
    #   (x+3)                    0 (  1 x  2 +  3 3  4 )

    def construct(self):

        # STANY. Podzial na czesci jest tak dobrany, zeby kazdy skladnik, ktory
        # w rachunku wedruje osobno, mial wlasny uchwyt.
        s1 = MathTex(r"\frac{x+3}{x-1}", r"=", r"\frac{x}{2x-2}")
        s3 = MathTex(r"\frac{x+3}{x-1}", r"=", r"\frac{x}{2(x-1)}")
        s4 = MathTex(r"\frac{x+3}{x-1}", r"=", r"\frac{x}{2(x-1)}",
                     r"\;\big/ \cdot\, 2(x-1)")
        s5 = MathTex(r"2", r"(x+3)", r"=", r"x")
        s6 = MathTex(r"2", r"x", r"+", r"6", r"=", r"x")
        s7 = MathTex(r"2", r"x", r"-", r"x", r"=", r"-", r"6")
        s8 = MathTex(r"x", r"=", r"-", r"6")

        rownania = [s1, s3, s4, s5, s6, s7, s8]
        for stan in rownania:
            stan.set_color(BLACK)
            stan.font_size = 90

        # Skala WSPOLNA dla wszystkich krokow, liczona z najszerszego (to krok 4,
        # rownanie z dopiskiem o mnozeniu). Gdyby kazdy krok dopasowywal sie
        # osobno, litery zmienialyby rozmiar w trakcie przeksztalcenia
        # i Transform robilby z tego zoom.
        MARGINES = 0.85
        najszerszy = max(stan.width for stan in rownania)
        if najszerszy > config.frame_width * MARGINES:
            wspolczynnik = config.frame_width * MARGINES / najszerszy
            for stan in rownania:
                stan.scale(wspolczynnik)
        for stan in rownania:
            stan.move_to(UP * 0.9)

        # Zalozenie (dziedzina) i sprawdzenie wyniku. Mniejsze od rachunku, bo to
        # komentarz do niego, a nie kolejna linijka przeksztalcen.
        zalozenie = MathTex(r"x", r"\ne", r"1")
        sprawdzenie = MathTex(r"-", r"6", r"\ne", r"1")
        for stan in (zalozenie, sprawdzenie):
            stan.set_color(BLACK)
            stan.font_size = 70
        zalozenie.move_to(DOWN * 1.7)
        sprawdzenie.move_to(DOWN * 2.9)

        def zapal(*co):
            self.play(*[m.animate.set_color(self.ZIELONY) for m in co],
                      run_time=self.ZAPALANIE)

        def zgas(zrodla, cele, nastepny):
            """Koniec kroku: zgaszenie koloru, podmiana na czysty stan, przytrzymanie.

            `zrodla` to obiekty LEZACE NA EKRANIE po przeksztalceniu (Transform
            zostawia obiekt zrodlowy, a po Transform(VGroup(a, b), cel) oba
            skladniki grupy), wiec to je gasi sie animacja. `cele` leza poza
            scena i wystarczy im set_color, ale zrobic to trzeba, bo za chwile
            to one wjezdzaja jako czysty stan nastepnego kroku.

            Do `zrodla` nie wolno wpisac niczego, co wyszlo z kadru przez FadeOut:
            animacja na obiekcie spoza sceny wstawilaby go z powrotem.
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
        # Rownanie z zadania. Nic sie jeszcze nie zmienia, wiec nie ma czego
        # zaznaczac. Rownanie stoi nad srodkiem, bo za chwile pod nim stanie
        # zalozenie.
        self.play(Create(s1))
        zgas([], [], s1)

        self.next_section("krok2")
        # ZALOZENIE. Mianownik nie moze byc zerem, a oba mianowniki zeruja sie
        # dla x = 1. Za sam ten zapis jest punkt w kluczu CKE, wiec dostaje
        # wlasny krok i zostaje na ekranie do konca filmu. Zielone, bo pojawia
        # sie z niczego; kolor mozna nadac przed animacja, skoro obiektu jeszcze
        # nie ma w kadrze.
        zalozenie.set_color(self.ZIELONY)
        self.play(FadeIn(zalozenie, shift=UP * 0.4), run_time=1.0)
        zgas([zalozenie], [], VGroup(s1, zalozenie))

        self.next_section("krok3")
        # 2x - 2 = 2(x - 1). Sedno zadania: po wylaczeniu dwojki widac, ze w obu
        # mianownikach siedzi ten sam nawias.
        #
        # Zielona jest tylko druga dwojka, bo to ona zmienia wartosc na jedynke.
        # Pierwsza dwojka i litera x tylko przesuwaja sie w inne miejsce zapisu,
        # wiec zostaja czarne, a nawiasow nie kolorujemy.
        zapal(s1[2][5])
        s3[2][6].set_color(self.ZIELONY)
        self.play(
            Transform(s1[0], s3[0]),           # lewa strona: samo przesuniecie
            Transform(s1[1], s3[1]),
            Transform(s1[2][0], s3[2][0]),     # licznik x
            Transform(s1[2][1], s3[2][1]),     # kreska ulamka
            Transform(s1[2][2], s3[2][2]),     # dwojka przed nawiasem
            Transform(s1[2][3], s3[2][4]),     # x
            Transform(s1[2][4], s3[2][5]),     # minus
            Transform(s1[2][5], s3[2][6]),     # dwojka -> jedynka
            FadeIn(s3[2][3]), FadeIn(s3[2][7]),   # nawiasy
        )
        zgas([s1[2][5]], [s3[2][6]], VGroup(s3, zalozenie))

        self.next_section("krok4")
        # Zapowiedz dzialania: obie strony mnozymy przez 2(x-1). Sam dopisek nic
        # jeszcze nie przelicza, ale to osobne przeksztalcenie, wiec ma osobny
        # krok. Rownanie odjezdza w lewo, zeby zrobic mu miejsce.
        s4[3].set_color(self.ZIELONY)
        self.play(
            Transform(s3[0], s4[0]),
            Transform(s3[1], s4[1]),
            Transform(s3[2], s4[2]),
            FadeIn(s4[3]),
        )
        zgas([s4[3]], [s4[3]], VGroup(s4, zalozenie))

        self.next_section("krok5")
        # SKRACANIE. Po lewej (x-1) skraca sie z mianownikiem i zostaje 2(x+3);
        # po prawej caly mianownik 2(x-1) znika i zostaje samo x.
        #
        # Zielone jest to, co sie skraca, czyli oba mianowniki razem z kreskami
        # ulamkow i mnoznik z dopisku. Czarne zostaja: liczniki (jada dalej bez
        # zmian) i dwojka z dopisku, ktora dojezdza przed nawias po lewej.
        # Nawiasow nie kolorujemy.
        zapal(
            s4[0][3], s4[0][4], s4[0][5], s4[0][6],            # kreska i mianownik x-1
            s4[2][1], s4[2][2], s4[2][4], s4[2][5], s4[2][6],  # kreska i mianownik 2(x-1)
            s4[3][0], s4[3][1], s4[3][4], s4[3][5], s4[3][6],  # ukosnik, kropka, (x-1)
        )
        self.play(
            Transform(s4[0][0], s5[1][1]),     # licznik x
            Transform(s4[0][1], s5[1][2]),     # +
            Transform(s4[0][2], s5[1][3]),     # 3
            FadeOut(VGroup(s4[0][3], s4[0][4], s4[0][5], s4[0][6])),
            Transform(s4[1], s5[2]),           # znak =
            Transform(s4[2][0], s5[3]),        # prawy licznik x
            FadeOut(VGroup(s4[2][1], s4[2][2], s4[2][3], s4[2][4],
                           s4[2][5], s4[2][6], s4[2][7])),
            Transform(s4[3][2], s5[0]),        # dwojka z dopisku -> mnoznik przed nawiasem
            FadeOut(VGroup(s4[3][0], s4[3][1], s4[3][3], s4[3][4],
                           s4[3][5], s4[3][6], s4[3][7])),
            FadeIn(s5[1][0]), FadeIn(s5[1][4]),   # nawiasy wokol x+3
        )
        # Wszystko, co bylo zielone, wyszlo z kadru FadeOut-em i zgaslo razem
        # z soba, wiec nie ma czego gasic. Animacja na obiekcie spoza sceny
        # wstawilaby go z powrotem na ostatnia klatke.
        zgas([], [], VGroup(s5, zalozenie))

        self.next_section("krok6")
        # Opuszczenie nawiasu: dwojka mnozy oba skladniki, wiec sie ROZDWAJA.
        # Kopie robimy przed zapaleniem, zeby zapalila sie razem z oryginalem
        # (lezy dokladnie na nim, wiec widac jedno). Zielone jest to, co zlewa
        # sie w nowa liczbe: dwojka i trojka daja szostke. Litera x zostaje
        # czarna, bo 2 razy x to dalej 2x.
        kopia_dwojki = s5[0].copy()
        zapal(s5[0], kopia_dwojki, s5[1][3])
        s6[3].set_color(self.ZIELONY)
        self.play(
            Transform(s5[0], s6[0]),                              # dwojka zostaje przy x
            Transform(s5[1][1], s6[1]),                           # x
            Transform(s5[1][2], s6[2]),                           # +
            Transform(VGroup(kopia_dwojki, s5[1][3]), s6[3]),     # 2 razy 3 -> 6
            FadeOut(VGroup(s5[1][0], s5[1][4])),                  # nawiasy
            Transform(s5[2], s6[4]),                              # znak =
            Transform(s5[3], s6[5]),                              # x po prawej
        )
        zgas([s5[0], kopia_dwojki, s5[1][3]], [s6[3]], VGroup(s6, zalozenie))

        self.next_section("krok7")
        # Iksy na lewo, liczby na prawo. Kazdy przeniesiony skladnik zmienia znak,
        # wiec zielone jest to, co zmienia strone: szostka i x z prawej strony.
        # Plus nie znika: ZAMIENIA SIE w minus, ktory staje przed szostka.
        # Minus przed x po lewej pojawia sie z niczego, wiec tez jest zielony.
        zapal(s6[2], s6[3], s6[5])
        s7[2].set_color(self.ZIELONY)
        s7[5].set_color(self.ZIELONY)
        self.play(
            Transform(s6[0], s7[0]),           # dwojka
            Transform(s6[1], s7[1]),           # x
            Transform(s6[2], s7[5]),           # plus -> minus przy szostce
            Transform(s6[3], s7[6]),           # szostka na prawa strone
            Transform(s6[4], s7[4]),           # znak =
            Transform(s6[5], s7[3]),           # x na lewa strone
            FadeIn(s7[2]),                     # minus przed przeniesionym x
        )
        zgas([s6[2], s6[3], s6[5], s7[2]], [s7[2], s7[5]], VGroup(s7, zalozenie))

        self.next_section("krok8")
        # 2x - x = x. Cztery znaki po lewej zlewaja sie w jedna litere, wiec
        # wszystkie sa zielone razem z wynikiem. Prawa strona sie nie zmienia.
        zapal(s7[0], s7[1], s7[2], s7[3])
        s8[0].set_color(self.ZIELONY)
        self.play(
            Transform(VGroup(s7[0], s7[1], s7[2], s7[3]), s8[0]),   # 2x - x -> x
            Transform(s7[4], s8[1]),
            Transform(s7[5], s8[2]),
            Transform(s7[6], s8[3]),
        )
        zgas([s7[0], s7[1], s7[2], s7[3]], [s8[0]], VGroup(s8, zalozenie))

        self.next_section("krok9")
        # SPRAWDZENIE ZALOZENIA. Wynik zjezdza kopia pod zalozenie i staje na
        # miejscu x: widac wtedy, ze -6 to nie jest 1, czyli wynik miesci sie
        # w dziedzinie. Znak "rozne od" i jedynka tez przylatuja kopiami
        # z zalozenia, bo byly juz w kadrze; pojawia sie tylko to, czego wczesniej
        # nie bylo. Zielony jest sam wynik, bo to on wchodzi w miejsce x.
        kopia_minusa = s8[2].copy()
        kopia_szostki = s8[3].copy()
        kopia_znaku = zalozenie[1].copy()
        kopia_jedynki = zalozenie[2].copy()
        zapal(kopia_minusa, kopia_szostki)
        sprawdzenie[0].set_color(self.ZIELONY)
        sprawdzenie[1].set_color(self.ZIELONY)
        self.play(
            Transform(kopia_minusa, sprawdzenie[0]),
            Transform(kopia_szostki, sprawdzenie[1]),
            Transform(kopia_znaku, sprawdzenie[2]),
            Transform(kopia_jedynki, sprawdzenie[3]),
        )
        zgas([kopia_minusa, kopia_szostki], [sprawdzenie],
             VGroup(s8, zalozenie, sprawdzenie))
