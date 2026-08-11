from manim import * 


class Zad4(Scene):
        
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
        
        kroki[0] = MathTex(r"\log_{7}x + 6\log_{7}y")
        kroki[1] = MathTex(r"\log_{7}x + \log_{7}(y^6)")
        kroki[2] = MathTex(r"\log_{7}(x \cdot y^6)")
        kroki[2] = MathTex(r"\log_{7}(xy^6)")

        for krok in kroki:
            if krok:
                krok.fill_color=BLACK
                krok.font_size=100
                

        wzory = [None] * 20

        wzory[0] = MathTex(r"a\log_x r = \log_x(r^a)")
        wzory[1] = MathTex(r"\log_a(x\cdot y)=\log_ax+\log_ay")
        
        for wzor in wzory:
            if wzor:
                wzor.fill_color=BLACK
                wzor.font_size=100
        

        #STEP 1
        #self.play(Create(kroki[0]))
        #self.wait(1)
        self.clear
        
        
        #STEP 2
        self.add(kroki[0])

        temp_krok = kroki[0].copy().move_to(UP*1.5+LEFT*2.15)
        temp_krok[0][6].set_color(GREEN)       
        wzory[0].move_to(DOWN*1.5+RIGHT*2.15)
        wzory[0][0][0].set_color(GREEN)
        wzory[0][0][13].set_color(GREEN)

        #self.play(Transform(kroki[0], temp_krok), Create(wzory[0]))
        #self.wait(0.2)


        #STEP 3
        kroki[1].move_to(UP*1.5+LEFT*2.15)
        kroki[1][0][12].set_color(GREEN)

        #self.play(TransformSplitPAIRS(0, [0, 6, 6, 7, 7, 11, 11, 99], [0, 6, 12, 13, 6, 10, 11, 12]), FadeIn(kroki[1][0][10:14:3]))
        #self.wait(0.2)
        
        self.clear()
        self.add(kroki[1], wzory[0])
        temp_krok = kroki[1].copy()
        temp_krok.move_to(ORIGIN).set_color(BLACK)
        
        #self.play(Transform(kroki[1], temp_krok), FadeOut(wzory[0], shift=DOWN*5))
        
        self.clear()


        #STEP 4
        self.add(kroki[1].move_to(ORIGIN).set_color(BLACK))
        self.play(Transform(kroki[1], kroki[1].copy().move_to(UP*1.5)), Create(wzory[1].move_to(DOWN*1.5)))
        self.play(Transform(kroki[1], kroki[1].copy().shift(RIGHT*1.7)), Transform(wzory[1], wzory[1].copy().shift(LEFT*1.7)))
        
        self.wait(1)
        
        """
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