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
        
        

        wzory = [MathTex()] * 6
        #wzory[0] jest pusty albo mozna wstawić tu prosty wzór na potęgę
        wzory[1] = MathTex(r"(a^r)^s=a^{r \cdot s}")
        wzory[2] = MathTex(r"a^r\cdot a^s=a^{r+s}")

        
        for wzor in wzory:
            wzor.fill_color=BLACK
            wzor.font_size=100
            wzor.shift(RIGHT*4.5)


        
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
            krok.shift(LEFT*4.5)

        kroki[4].font_size=75

        
        
        #STEP 1
        #self.add(Text("STEP 1", font_size=70, color=BLACK).shift(UP*2))
        self.play(Create(kroki[0]))
        self.clear()
        
        
        
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

        kroki[1][0][:].set_color(BLACK)
        
        self.clear()


        #STEP 3
        #self.add(Text("STEP 3", font_size=70, color=BLACK).shift(UP*2))
        
        self.add(kroki[1])
        
        self.play(Create(wzory[1]))
        self.play(TransformSplit(1, [0, 7, 11, 14], 
                                    [0, 6, 8, 10]))
        self.clear()



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

        
        kroki[3][0][:].set_color(BLACK)
        self.clear()
        



        #STEP 5
        #self.add(Text("STEP 5", font_size=70, color=BLACK).shift(UP*2))
        self.add(kroki[3])
        self.play(Create(wzory[2]))
        
        #self.add(index_labels(kroki[3][0]))
        self.wait(1)
        self.play(TransformSplit(3, [0, 3, 5, 9, 11, 13], [0, 3, 6, 10, 13, 17]))

        self.clear()


    
    
        
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
        
        kroki[5][0][:].set_color(BLACK)

        self.clear()

        #STEP 7
        #self.add(Text("STEP 7", font_size=70, color=BLACK).shift(UP*2))
        #self.add(index_labels(kroki[5][0]).shift(UP*.5))

        self.add(kroki[5])
        self.play(TransformSplit(5, [0, 5], [0, 5]))
        self.clear()



        #STEP 8
        #self.add(Text("STEP 8", font_size=70, color=BLACK).shift(UP*2))
        self.add(kroki[6])
        self.play(TransformSplit(6, [0, 4], [0, 4]))
        self.clear()

        #STEP 9

        self.add(kroki[6])
        self.clear()

        

