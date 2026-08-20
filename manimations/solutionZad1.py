from manim import * 


class Zad1(Scene):
        
    def construct(self):
        GREEN = "#0AB32F"
        GRAY = "#A6A6A6"

        def TransformSplitPAIRS(step, indexs1, indexs2):
            if len(indexs1) % 2 != 0 or len(indexs2) != len(indexs1):
                raise ValueError("ZŁA DŁUGOŚĆ LISTY INDEXS, MUSZĄ BYĆ PARZYSTE I TAKIE SAME")
            
            transforms = []
            for i in range(len(indexs1)):
                if( i != len(indexs1) - 1  and  i%2 == 0):
                    transforms.append(
                        Transform(
                            kroki[step][0][indexs1[i]:indexs1[i+1]], 
                            kroki[step+1][0][indexs2[i]:indexs2[i+1]], 
                            run_time=1.4
                        )
                    )
                    
            return transforms


        kroki = [None] * 20
        
        kroki[0] = MathTex(r"|x + 4| = 7")
        kroki[1] = MathTex(r"x + 4 = 7 \quad \lor \quad x + 4 = -7")

        kroki[2] = MathTex(r"x + 4 = 7")
        kroki[3] = MathTex(r"x = 7 - 4")
        kroki[4] = MathTex(r"x_1 = 3")
        kroki[5] = MathTex(r"")
        kroki[6] = MathTex(r"")
        kroki[7] = MathTex(r"")

        kroki[8] = MathTex(r"x + 4 = 7 \quad \lor \quad x + 4 = -7")
        kroki[9] = MathTex(r"x + 4 = -7")
        kroki[10] = MathTex(r"x = -7 - 4 ")
        kroki[11] = MathTex(r"x_2 = -11")

        kroki[12] = MathTex(r"x_1 + x_2 = 3 - 11")
        kroki[13] = MathTex(r"x_1 + x_2 = -8")







        for krok in kroki:
            if krok:
                krok.fill_color=BLACK
                krok.font_size=110
                #krok.shift(LEFT*4)

        # Kadr od 2026-08-11 jest 16:9 (1280x720), a nie 21:9 (840x360) — patrz
        # manim.cfg. Węższy kadr znaczy, że najdłuższy zapis („x + 4 = 7 v x + 4 = -7")
        # przy font_size 110 wychodzi bokiem, dlatego skalujemy tak samo jak
        # w zadaniu 2: JEDEN wspólny współczynnik liczony z najszerszego kroku.
        # Osobne dopasowanie każdego kroku zmieniałoby wielkość liter w trakcie
        # przekształcenia, a Transform robiłby z tego zoom.
        MARGINES = 0.85
        najszerszy = max(krok.width for krok in kroki if krok and krok.width > 0)
        if najszerszy > config.frame_width * MARGINES:
            wspolczynnik = config.frame_width * MARGINES / najszerszy
            for krok in kroki:
                if krok:
                    krok.scale(wspolczynnik)
        for krok in kroki:
            if krok:
                krok.move_to(ORIGIN)

        #NA RAZIE NIE BĘDĘ UŻYWAŁ WZORÓW
        """
        wzory = [MathTex()] * 6
        wzory[0] = MathTex(r"|x|=\left\{\begin{array}{cccc}x & \mathrm{dla} & x\geq0 \\-x & \mathrm{dla} & x<0\end{array}\right.")
        for wzor in wzory:
            wzor.fill_color=BLACK
            wzor.font_size=100
            wzor.shift(RIGHT*4.5)
        """

        # KROKI JAKO SEKCJE (przebudowa 2026-08-12). Wcześniej kroki przełączało się
        # komentarzem `"""` i renderowało po jednym; teraz scena jedzie w całości,
        # a granice kroków wyznacza `self.next_section`. Render:
        #     manim --save_sections solutionZad1.py Zad1
        # kładzie każdy krok osobnym plikiem w media/videos/solutionZad1/720p120/sections/.
        #
        # Treść animacji jest Henricha, przepisana 1:1 — sumy czasów zgadzają się
        # z wgranymi wcześniej plikami (1,0 / 4,0 / 1,4 / 4,4 / 5,4 / 2,4 / 2,4 / 4,4 / 4,4 s).
        # Dołożone są dwie rzeczy: wspólne skalowanie pod kadr 16:9 (wyżej) i
        # `self.wait(0.25)` na końcu KAŻDEJ sekcji — bez tego przeglądarka zatrzymuje
        # obraz kilka klatek przed końcem pliku i ostatni element animacji nie zostaje
        # na ekranie (README, punkt 0 workflow). Przytrzymanie idzie ZAWSZE przed
        # `self.clear()`, bo po wyczyszczeniu sceny trzymałoby białą planszę.

        self.next_section("krok1")
        #STEP 1
        self.play(Create(kroki[0]))
        self.wait(0.25)


        self.next_section("krok2")
        #STEP 2
        temp_krok = kroki[0].copy().shift(UP)
        temp_krok.font_size=90
        temp_krok[0][0].set_color(GREEN)
        temp_krok[0][4].set_color(GREEN)
        self.play(Transform(kroki[0], temp_krok))

        temp_krok = kroki[1].copy()

        temp_krok.shift(DOWN)
        temp_krok.font_size=70
        self.play(Create(temp_krok))
        self.wait(1)
        self.play(FadeOut(kroki[0], shift=UP*3), Transform(temp_krok, kroki[1].copy()))
        self.wait(0.25)
        self.clear()


        self.next_section("krok3")
        #STEP 3
        self.add(kroki[1])
        self.play(TransformSplitPAIRS(1, [0, 5, 5, 99], [0, 99, 99, 99]))
        self.wait(0.25)
        self.clear()


        self.next_section("krok4")
        #STEP 4
        temp_krok = MathTex()
        temp_krok = kroki[2].copy()
        self.add(temp_krok)
        kroki[2][0][1:3].set_color(GREEN)
        kroki[3][0][3:5].set_color(GREEN)
        self.play(ReplacementTransform(temp_krok, kroki[2]))
        self.wait(1)

        self.play(TransformSplitPAIRS(2, [0, 1, 1, 3, 3, 5], [0, 1, 3, 5, 1, 3]))
        self.clear()

        self.add(kroki[3])
        self.play(FadeToColor(kroki[3], color=BLACK))
        kroki[3][0][:].set_color(BLACK)
        self.wait(0.25)
        self.clear()


        self.next_section("krok5")
        #STEP 5
        temp_krok = kroki[3].copy()
        self.add(temp_krok)
        kroki[3][0][2:].set_color(GREEN)
        kroki[4][0][2:].set_color(GREEN)
        self.play(ReplacementTransform(temp_krok, kroki[3]))
        self.wait(1)

        self.play(TransformSplitPAIRS(3, [0, 2, 2, 99], [0, 2, 2, 99]))

        self.play(FadeToColor(kroki[4], color=BLACK))
        kroki[4][0][:].set_color(BLACK)
        self.clear()
        temp_krok = kroki[4].copy()
        # x1 = 3 odjeżdża w lewy dolny róg i zostaje tam na szaro — to wynik
        # pierwszego przypadku, potrzebny dopiero w ostatnim kroku przy sumie.
        self.play(ReplacementTransform(temp_krok, kroki[4].move_to(DOWN*2.3+LEFT*4).set_color(GRAY)))
        self.wait(0.25)


        self.next_section("krok6")
        #STEP 6
        # Odłożone x1 = 3 zostaje w kadrze — w wersji ciętej ręcznie trzeba je było
        # dodawać na nowo w każdym kroku (`self.add(kroki[4].move_to(...))`).
        # Przy renderze ciągłym stan przynosi poprzednia sekcja, więc te powtórzenia
        # znikają; to była główna pułapka starej procedury (README).
        self.play(Create(kroki[8]))
        self.play(TransformSplitPAIRS(8, [0, 6, 6, 99], [0, 0, 0, 99]))
        self.wait(0.25)
        self.clear()


        self.next_section("krok7")
        #STEP 7
        kroki[4].fill_color=GRAY
        self.add(kroki[4].move_to(DOWN*2.3+LEFT*4))

        temp_krok = kroki[9].copy()
        self.add(temp_krok)
        kroki[9][0][1:3].set_color(GREEN)
        kroki[10][0][4:6].set_color(GREEN)
        self.play(ReplacementTransform(temp_krok, kroki[9]))

        self.play(TransformSplitPAIRS(9, [0, 1, 1, 3, 3, 6], [0, 1, 4, 6, 1, 4]))
        self.wait(0.25)
        self.clear()


        self.next_section("krok8")
        #STEP 8
        kroki[4].fill_color=GRAY
        self.add(kroki[4].move_to(DOWN*2.3+LEFT*4))

        temp_krok = kroki[10].copy()
        self.add(temp_krok)
        kroki[10][0][2:99].set_color(GREEN)
        kroki[11][0][2:99].set_color(GREEN)

        self.play(FadeTransform(temp_krok, kroki[10]))

        self.add(kroki[10])
        self.play(TransformSplitPAIRS(10, [0, 2, 2, 99], [0, 2, 2, 99]))

        temp_krok = kroki[11].copy()
        temp_krok.set_color(BLACK)

        self.play(FadeTransform(kroki[11], temp_krok))
        self.clear()

        kroki[11].set_color(BLACK)
        # Oba wyniki rozjeżdżają się na boki: x1 w lewo, x2 w prawo — w następnym
        # kroku zderzą się w sumę.
        self.play(Transform(kroki[11].copy(), kroki[11].shift(RIGHT*4)), Transform(kroki[4].copy(), kroki[4].shift(UP*2.3).set_color(BLACK)))
        self.wait(0.25)
        self.clear()


        self.next_section("krok9")
        #STEP 9
        self.add(kroki[4].move_to(LEFT*4))
        self.add(kroki[11].move_to(RIGHT*4))
        # Bez postoju na wejściu (2026-08-20): oba wyniki są tu przyniesione
        # z poprzedniego kroku, więc uczeń ma je już obejrzane. Sekunda bezruchu
        # na starcie filmu czytała się jak zacięcie odtwarzacza.
        self.play(Transform(kroki[4][0][0:2], kroki[12][0][0:3]), Transform(kroki[4][0][2:99],  kroki[12][0][5:7]), Transform(kroki[11][0][0:2],  kroki[12][0][3:5]), Transform(kroki[11][0][2:99],  kroki[12][0][7:99]))
        self.wait(1)
        self.clear()

        self.add(kroki[12])
        self.play(TransformSplitPAIRS(12, [0, 6, 6, 99], [0, 6, 6, 99]))
        self.wait(0.25)
