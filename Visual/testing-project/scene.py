from manim import *

class Scheduler(Scene):
    def stride(self):
        p1 = []
        p2 = []
        p3 = []
        h1 = 0
        h2 = 0
        h3 = 0
        order = []
        for i in range(16):
            if i == 0:
                order.append(0)
            else:
                if h1 <= h2 and h1 <= h3:
                    h1 += 1.5
                    print(h1)
                    order.append(1)
                elif h2 <= h1 and h2 <= h3:
                    h2 += 1
                    order.append(2)
                else:
                    h3 += 0.5
                    order.append(3)
        label = []
        h1 = 0
        h2 = 0
        h3 = 0
        for i in range(16):
            if order[i] == 1:
                h1 += 1.5
                p1.append(Square(color=BLUE, stroke_opacity=0, fill_opacity=0.7))
                p1[i].stretch_to_fit_width(0.5)
                p1[i].stretch_to_fit_height(h1)
                p1[i].align_to([0, -2.5, 0], DOWN)
                p1[i].align_to([-1, -2.5, 0], LEFT)
            elif i == 0:
                p1.append(Square(color=BLUE, stroke_opacity=0, fill_opacity=0.7))
                p1[i].stretch_to_fit_width(0.5)
                p1[i].stretch_to_fit_height(0)
                p1[i].align_to([0, -2.5, 0], DOWN)
                p1[i].align_to([-1, -2.5, 0], LEFT)
            else:
                p1.append(p1[i-1])

            if order[i] == 2:
                h2 += 1
                p2.append(Square(color=ORANGE, stroke_opacity=0, fill_opacity=0.7))
                p2[i].stretch_to_fit_width(0.5)
                p2[i].stretch_to_fit_height(h2)
                p2[i].next_to(p1[i], RIGHT, buff=0)
                p2[i].align_to(p1[i], DOWN)
            elif i == 0:
                p2.append(Square(color=ORANGE, stroke_opacity=0, fill_opacity=0.7))
                p2[i].stretch_to_fit_width(0.5)
                p2[i].stretch_to_fit_height(0)
                p2[i].next_to(p1[i], RIGHT, buff=0)
                p2[i].align_to([0, -2.5, 0], DOWN)
            else:
                p2.append(p2[i-1])


            if order[i] == 3:
                h3 += 0.5
                p3.append(Square(color=GREEN, stroke_opacity=0, fill_opacity=0.7))
                p3[i].stretch_to_fit_width(0.5)
                p3[i].stretch_to_fit_height(h3)
                p3[i].next_to(p2[i], RIGHT, buff=0)
                p3[i].align_to(p1[i], DOWN)
            elif i == 0:
                p3.append(Square(color=GREEN, stroke_opacity=0, fill_opacity=0.7))
                p3[i].stretch_to_fit_width(0.5)
                p3[i].stretch_to_fit_height(0)
                p3[i].next_to(p2[i], RIGHT, buff=0)
                p3[i].align_to([0, -2.5, 0], DOWN)
            else:
                p3.append(p3[i-1])

            label.append(Text("t = " + str(i), color=BLACK))
            label[i].next_to(p2[i], DOWN, buff=0.5)
        for i in range(16):
            if i == 0:
                border = Square(color=BLACK, fill_opacity=0)
                border.stretch_to_fit_height(5)
                border.stretch_to_fit_width(1.5)
                border.align_to(p1[0], DOWN)
                border.align_to(p1[0], LEFT)
                txt_pass_value = Text("Pass Value", font_size=24, color=BLACK)
                txt_pass_value.rotate(PI/2)
                txt_pass_value.next_to(border, LEFT, buff=0.25)
                #dashed_1 = DashedLine(border.get_top(), border.get_bottom(), dashed_ratio=0.5)
                #dashed_1.rotate(PI/2).align_to(border, DOWN)
                #dashed_2 = DashedLine(border.get_top(), border.get_bottom(), dashed_ratio=0.5)
                #dashed_2.rotate(PI/2).shift(LEFT*0.5).align_to(border, DOWN)
                self.add_foreground_mobjects(border, txt_pass_value) #, dashed_1, dashed_2)
                self.play(Create(border), Write(txt_pass_value))
                self.play(Create(p3[0]) , Create(p1[0]) , Create(p2[0]) , Write(label[0]))
            else:
                self.play(ReplacementTransform(p1[i-1], p1[i]), ReplacementTransform(p2[i-1], p2[i]), ReplacementTransform(p3[i-1], p3[i]), ReplacementTransform(label[i-1], label[i]))
            self.wait(0.5)

    def construct(self):
        self.camera.background_color=WHITE
        self.stride()
