from manim import * 

class ScenaZadania3(Scene):
        
    def construct(self):
        GREEN = "#0AB32F"
        GRAY = "#A6A6A6"

        #for now WORKS ONLY WITH KROKI!!!
        def TransformSplit(step, indexs1, indexs2):
            transforms = []
            for i in range(len(indexs1)):
                
                if( i != len(indexs1) -  1):
                    transforms.append(
                        Transform(
                            kroki[step][0][indexs1[i]:indexs1[i+1]], 
                            kroki[step+1][0][indexs2[i]:indexs2[i+1]], 
                            run_time=1.4
                        )
                    )
                else:
                    transforms.append(
                        Transform(
                            kroki[step][0][indexs1[i]:], 
                            kroki[step+1][0][indexs2[i]:], 
                            run_time=1.4
                        )
                    )
                    
            return transforms
        #UWAGA PARY!!
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
        
        

        # Wzory pomocnicze NIE są już rysowane w filmie (ujednolicone z zad. 2
        # 2026-08-12; zmiana zasady jest z 2026-08-11). Pokazuje je strona, jako
        # KaTeX pod filmem — patrz pole "text" przy kroku w exercises.json.
        # Definicje zostają tutaj jako źródło wiedzy, który wzór należy do którego
        # kroku; scena ich nie dodaje.
        #   krok 3 → (a^r)^s = a^{r·s}
        #   krok 5 → a^r · a^s = a^{r+s}
        wzory = [MathTex()] * 6
        wzory[1] = MathTex(r"(a^r)^s=a^{r \cdot s}")
        wzory[2] = MathTex(r"a^r\cdot a^s=a^{r+s}")

        for wzor in wzory:
            wzor.fill_color=BLACK
            wzor.font_size=100


        
        kroki = [MathTex()] * 8
        kroki[0] = MathTex(r"2^{100} + 4^{49} + 16^{24}")
        kroki[1] = MathTex(r"2^{100} + (2^2)^{49} + (2^4) ^{24}")
        kroki[2] = MathTex(r"2^{100} + 2^{98} + 2^{96}")
        kroki[3] = MathTex(r"2^{96+4} + 2^{96+2} + 2^{96}")
        kroki[4] = MathTex(r"2^{96} \cdot 2^4 + 2^{96} \cdot 2^2 + 2^{96} \cdot 1")
        kroki[5] = MathTex(r"2^{96} \cdot (2^4 + 2^2 + 1)")
        kroki[6] = MathTex(r"2^{96} \cdot (16 + 4 + 1)")
        kroki[7] = MathTex(r"2^{96} \cdot 21")
        #kroki[8] = MathTex(r"2^{96} jest liczbą całkowitą. To co nam wyszło jest wielokrotnością 21, więc jest podzielne przez 21.")
        #Latex nie lubi polski znaków :(

        for krok in kroki:
            krok.fill_color=BLACK
            krok.font_size=90

        # Ten krok jest najdłuższy (trzy iloczyny), więc od początku był pisany
        # mniejszą czcionką.
        kroki[4].font_size=75

        # Kadr od 2026-08-11 jest 16:9 (1280x720), a nie 21:9 (840x360) — patrz
        # manim.cfg. Treść stoi teraz na ŚRODKU: przesunięcie w lewo (LEFT*4.5)
        # trzymało z prawej miejsce na wzór pomocniczy, a ten wyszedł z filmu.
        # Skala jest WSPÓLNA dla wszystkich kroków i liczona z najszerszego — gdyby
        # każdy krok dopasowywał się osobno, litery zmieniałyby rozmiar w trakcie
        # przekształcenia, a Transform robiłby z tego zoom. Względne różnice
        # wielkości (krok 5 mniejszy) zostają, bo mnożymy wszystko tak samo.
        MARGINES = 0.85
        najszerszy = max(krok.width for krok in kroki)
        if najszerszy > config.frame_width * MARGINES:
            wspolczynnik = config.frame_width * MARGINES / najszerszy
            for krok in kroki:
                krok.scale(wspolczynnik)
        for krok in kroki:
            krok.move_to(ORIGIN)

        
        
        # KROKI JAKO SEKCJE (przebudowa 2026-08-12) — render:
        #     manim --save_sections solutionZad3.py ScenaZadania3
        # kładzie każdy krok osobnym plikiem w sections/. Każda sekcja kończy się
        # `self.wait(0.25)` PRZED sprzątaniem sceny: bez przytrzymania przeglądarka
        # gubi ostatnie klatki, a po `self.clear()` trzymałoby się białą planszę.

        self.next_section("krok1")
        #STEP 1
        #self.add(Text("STEP 1", font_size=70, color=BLACK).shift(UP*2))
        self.play(Create(kroki[0]))
        self.wait(0.25)
        self.clear()
        
        
        
        self.next_section("krok2")
        #STEP 2
        #self.add(Text("STEP 2", font_size=70, color=BLACK).shift(UP*2))
        temp_krok = kroki[0].copy()
        kroki[0][0][:].set_color(GRAY)
        kroki[1][0][:].set_color(GRAY)


        kroki[0][0][5].set_color(BLACK)
        kroki[0][0][9:11].set_color(BLACK)

        kroki[1][0][5:9].set_color(BLACK)
        kroki[1][0][12:16].set_color(BLACK)
        self.play(ReplacementTransform(temp_krok, kroki[0]))
        self.wait(1)
        #self.play(Transform(kroki[0][0][0:5], kroki[1][0][0:5]), Transform(kroki[0][0][5], kroki[1][0][5:9]), Transform(kroki[0][0][6:9], kroki[1][0][9:12]), Transform(kroki[0][0][9:11], kroki[1][0][12:15]), Transform(kroki[0][0][11:], kroki[1][0][15:]))
        self.play(TransformSplit(0, [0, 5, 6, 9, 11], [0, 5, 9, 12, 15]))

        # ROZJAŚNIENIE na koniec kroku (Henrich, 2026-08-12). Na ekranie siedzą
        # kawałki kroki[0][0] przekształcone w kroki[1] — i to one trzymają szary
        # kolor, bo Transform interpoluje barwę do celu. Samo pomalowanie kroki[1]
        # na czarno niczego nie zmieniało: to nie ten obiekt jest w kadrze.
        # Bez tego krok kończył się na wpół przyciemnionym zapisie, a następny
        # startował czysty — w odtwarzaczu to jest ta sama klatka, więc było widać
        # przeskok. Pilnuje tego tools/styk-klatek.sh.
        self.wait(0.35)
        self.play(kroki[0][0].animate.set_color(BLACK), run_time=0.4)
        kroki[1][0][:].set_color(BLACK)

        self.wait(0.25)
        self.clear()


        self.next_section("krok3")
        #STEP 3
        #self.add(Text("STEP 3", font_size=70, color=BLACK).shift(UP*2))
        
        self.add(kroki[1])
        
        self.play(TransformSplit(1, [0, 7, 11, 14], 
                                    [0, 6, 8, 10]))
        self.wait(0.25)
        self.clear()



        self.next_section("krok4")
        #STEP 4
        #self.add(Text("STEP 4", font_size=70, color=BLACK).shift(UP*2))
        
        
        temp_krok = kroki[2].copy()
        kroki[2][0][:].set_color(GRAY)
        kroki[3][0][:].set_color(GRAY)

        kroki[2][0][1:4].set_color(BLACK)
        kroki[2][0][6:8].set_color(BLACK)

        kroki[3][0][1:5].set_color(BLACK)
        kroki[3][0][7:11].set_color(BLACK)

        
        self.play(ReplacementTransform(temp_krok, kroki[2]))
        self.wait(1)
        self.play(TransformSplit(2, [0, 1, 4, 6, 8, 10], [0, 1, 5, 7, 11, 13]))

        
        # Rozjaśnienie na koniec kroku — patrz komentarz przy kroku 2.
        self.wait(0.35)
        self.play(kroki[2][0].animate.set_color(BLACK), run_time=0.4)
        kroki[3][0][:].set_color(BLACK)
        self.wait(0.25)
        self.clear()
        



        self.next_section("krok5")
        #STEP 5
        #self.add(Text("STEP 5", font_size=70, color=BLACK).shift(UP*2))
        self.add(kroki[3])
        
        #self.add(index_labels(kroki[3][0]))
        # Bez postoju na wejściu (2026-08-20): ten zapis stoi już na ostatniej
        # klatce kroku 4, więc sekunda bezruchu tylko wydłużała film.
        self.play(TransformSplit(3, [0, 3, 5, 9, 11, 13], [0, 3, 6, 10, 13, 17]))

        self.wait(0.25)
        self.clear()


    
    
        
        self.next_section("krok6")
        #STEP 6

        temp_krok = kroki[4].copy()
        kroki[4][0][:].set_color(GRAY)
        kroki[5][0][:].set_color(GRAY)

        kroki[4][0][0:3].set_color(BLACK)
        kroki[4][0][7:10].set_color(BLACK)
        kroki[4][0][14:17].set_color(BLACK)

        kroki[5][0][0:3].set_color(BLACK)

        #self.add(Text("STEP 6", font_size=70, color=BLACK).shift(UP*2))
        #self.add(index_labels(kroki[4][0]).shift(UP*.5))

        self.play(ReplacementTransform(temp_krok, kroki[4]))
        self.wait(1)
        self.play(TransformSplitPAIRS(4, [0, 4,  4, 7,  7, 11,  11, 14,  14, 18,  18, 99],
                                         [0, 5,  5, 8,  0,  3,   8, 11,   0,  3,  11, 99]))

        # Trzy kopie 2^96 zjeżdżają na to samo miejsce (o to chodzi w wyłączaniu
        # przed nawias), ale Transform zostawia wszystkie trzy w scenie. Na klatce
        # spoczynku zapis robił się przez to grubszy niż pierwsza klatka kroku 7 —
        # wychodziło to na SSIM 0,9990. Dwie nadmiarowe kopie usuwamy.
        self.remove(*kroki[4][0][7:11], *kroki[4][0][14:18])

        # Rozjaśnienie na koniec kroku — patrz komentarz przy kroku 2.
        self.wait(0.35)
        self.play(kroki[4][0].animate.set_color(BLACK), run_time=0.4)
        kroki[5][0][:].set_color(BLACK)

        self.wait(0.25)
        self.clear()

        self.next_section("krok7")
        #STEP 7
        #self.add(Text("STEP 7", font_size=70, color=BLACK).shift(UP*2))
        #self.add(index_labels(kroki[5][0]).shift(UP*.5))

        self.add(kroki[5])
        self.play(TransformSplit(5, [0, 5], [0, 5]))
        self.wait(0.25)
        self.clear()



        self.next_section("krok8")
        #STEP 8
        #self.add(Text("STEP 8", font_size=70, color=BLACK).shift(UP*2))
        self.add(kroki[6])
        self.play(TransformSplit(6, [0, 4], [0, 4]))
        self.wait(0.25)
        self.clear()


        

