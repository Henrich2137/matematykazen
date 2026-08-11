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
        
        #NA RAZIE NIE BĘDĘ UŻYWAŁ WZORÓW
        """
        wzory = [MathTex()] * 6
        wzory[0] = MathTex(r"|x|=\left\{\begin{array}{cccc}x & \mathrm{dla} & x\geq0 \\-x & \mathrm{dla} & x<0\end{array}\right.")
        for wzor in wzory:
            wzor.fill_color=BLACK
            wzor.font_size=100
            wzor.shift(RIGHT*4.5)
        """

        """
        #STEP 1
        self.play(Create(kroki[0]))
        

        #STEP 2
        temp_krok = kroki[0].copy().shift(UP)
        temp_krok.font_size=90
        temp_krok[0][0].set_color(GREEN)
        temp_krok[0][4].set_color(GREEN)
        #wzory[0].font_size=50 #Create(wzory[0])
        self.play(Transform(kroki[0], temp_krok))
        
        temp_krok = kroki[1].copy()
        
        temp_krok.shift(DOWN)
        temp_krok.font_size=70
        self.play(Create(temp_krok))
        self.wait(1)
        self.play(FadeOut(kroki[0], shift=UP*3), Transform(temp_krok, kroki[1].copy()))
        self.clear()
        
        
        
        #STEP 3
        self.add(kroki[1])
        self.play(TransformSplitPAIRS(1, [0, 5, 5, 99], [0, 99, 99, 99]))
        self.clear()
        
        
        #STEP 4
        #self.add(index_labels(kroki[0][0]).shift(UP))
        temp_krok = MathTex()
        temp_krok = kroki[2].copy()
        self.add(temp_krok)
        #kroki[2][0][:].set_color(GRAY)
        #kroki[3][0][:].set_color(GRAY)
        kroki[2][0][1:3].set_color(GREEN)
        kroki[3][0][3:5].set_color(GREEN)
        self.play(ReplacementTransform(temp_krok, kroki[2]))
        self.wait(1)

        self.play(TransformSplitPAIRS(2, [0, 1, 1, 3, 3, 5], [0, 1, 3, 5, 1, 3]))
        self.clear()

        self.add(kroki[3])
        self.play(FadeToColor(kroki[3], color=BLACK))
        kroki[3][0][:].set_color(BLACK)
        self.clear()
        """

        #STEP 5
        #self.add(index_labels(kroki[3][0]).shift(UP))

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
        self.play(ReplacementTransform(temp_krok, kroki[4].move_to(DOWN*2.3+LEFT*4).set_color(GRAY)))
        self.clear()
        
        
        
        """
        #STEP 6 COŚ TU SIĘ GRUBO ZJEBAŁO Z KROKI 1
        kroki[4].fill_color=GRAY
        self.add(kroki[4].move_to(DOWN*2.3+LEFT*4))
        

        self.play(Create(kroki[8]))
        #z jakiegoś powodu zamiast kroki[1] pojawia się krok 2 i animuje go zupełnia jak krok 2 -> 3
        self.play(TransformSplitPAIRS(8, [0, 6, 6, 99], [0, 0, 0, 99]))
        self.clear()
        
        
        #STEP 7
        kroki[4].fill_color=GRAY
        self.add(kroki[4].move_to(DOWN*2.3+LEFT*4))
        
        temp_krok = kroki[9].copy()
        self.add(temp_krok)
        kroki[9][0][1:3].set_color(GREEN)
        kroki[10][0][4:6].set_color(GREEN)
        self.play(ReplacementTransform(temp_krok, kroki[9]))

        self.play(TransformSplitPAIRS(9, [0, 1, 1, 3, 3, 6], [0, 1, 4, 6, 1, 4]))
        
        self.clear()
        

        
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
        self.play(Transform(kroki[11].copy(), kroki[11].shift(RIGHT*4)), Transform(kroki[4].copy(), kroki[4].shift(UP*2.3).set_color(BLACK)))
        self.clear()
        

        
        #STEP 9
        self.add(kroki[4].move_to(LEFT*4))
        self.add(kroki[11].move_to(RIGHT*4))
        self.wait(1)
        self.play(Transform(kroki[4][0][0:2], kroki[12][0][0:3]), Transform(kroki[4][0][2:99],  kroki[12][0][5:7]), Transform(kroki[11][0][0:2],  kroki[12][0][3:5]), Transform(kroki[11][0][2:99],  kroki[12][0][7:99]))
        self.wait(1)
        self.clear()
        
        self.add(kroki[12])
        self.play(TransformSplitPAIRS(12, [0, 6, 6, 99], [0, 6, 6, 99]))
        self.clear()

        """