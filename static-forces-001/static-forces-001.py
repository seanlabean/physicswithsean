from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

class ProblemSolve(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService(silence_threshold=-40.0))
        # Cover image, self introduction
        cover_img = ImageMobject("..\moon-lady-pws.jpg").scale(0.5)
        with self.voiceover(text="Welcome Physics with Sean, let's do another practice problem.") as tracker:
            self.play(FadeIn(cover_img))
            self.wait(duration=tracker.duration)
        self.play(FadeOut(cover_img))

        # Problem Statement and Explanation
        ptext = MarkupText(f"Find the tension in each chord \nif the weight of the suspended object is 7 N.")
        with self.voiceover(text="In this problem, we want to find the tension in each chord if the weight of the suspended object is 7 N.") as tracker:
            self.play(Write(ptext), run_time=tracker.duration)

        ptitle = MarkupText(f"Find the <span fgcolor='{YELLOW}'>tension in each chord</span> \nif the weight of the suspended object is <span fgcolor='{RED}'>7 N</span>.")

        ptitle.to_corner(UP + LEFT)
        self.play(
            Transform(ptext, ptitle),
        )
        self.wait()

        # Draw Problem
        xfbd = -6
        yfbd = 1
        ceiling = Line(start=(xfbd, yfbd, 0), end=(xfbd+4, yfbd, 0))
        wall = Line(start=(xfbd, yfbd-3, 0), end=(ceiling.start))
        chord1 = Line(start=(xfbd, yfbd-2.5, 0), end=(xfbd+2.5, yfbd-1.5, 0))
        chord2 = Line(start=(xfbd+3.5, yfbd, 0), end=(xfbd+2.5, yfbd-1.5, 0))
        chord3 = Line(start=(xfbd+2.5, yfbd-1.5, 0), end=(xfbd+2.5, yfbd-2.5, 0))
        weight = Polygon([xfbd+2.25, yfbd-2.5, 0], [xfbd+2.25, yfbd-3, 0], [xfbd+2.75, yfbd-3, 0], [xfbd+2.75, yfbd-2.5, 0]).set_color(RED)

        a1 = Angle(chord1, wall, radius=0.5, other_angle=False)
        a2 = Angle(chord2, ceiling, radius=0.5, other_angle=True, quadrant=(1,-1))
        a1_text = MathTex(r"60^\circ").scale(0.6).move_to(
            Angle(
                wall, chord1, radius=0.5 + 3 * SMALL_BUFF, other_angle=True
            ).point_from_proportion(0.5)
        )
        a2_text = MathTex(r"45^\circ").scale(0.6).move_to(
            Angle(
                ceiling, chord2, radius=0.5 + 3 * SMALL_BUFF, other_angle=True, quadrant=(1,-1)
            ).point_from_proportion(0.5)
        )

        diagram = VGroup(ceiling, wall, chord1, chord2, chord3, weight, a1, a1_text, a2, a2_text)
        self.play(Create(diagram))
        self.wait(2.5)

        # Draw Free Body Diagram
        xfbd = -6
        yfbd = 2
        offset = np.array([0.5,-1.5,0])
        fbd_origin = chord1.end - offset
        dot = Dot(fbd_origin)
        arrow1 = Arrow(fbd_origin, chord1.start - offset, buff=0)
        arrow2 = Arrow(fbd_origin, chord2.start - offset, buff=0)
        arrow3 = Arrow(fbd_origin, chord3.end - offset - np.array([0,1,0]), buff=0)

        a1_text = MathTex('T_{1}').next_to(arrow1.get_end(), RIGHT, buff=0.7)
        a2_text = MathTex('T_{2}').next_to(arrow2.get_end(), RIGHT, buff=0.3)
        a3_text = MathTex('7 N').next_to(arrow3.get_end(), RIGHT, buff=0.3)
        fbd = VGroup(dot, arrow1, arrow2, arrow3, a1_text, a2_text, a3_text)

        with self.voiceover(text="Whenever working with problems like this, it is incredibly important that we simplify things visually as much as possible, so I'll draw out a free-body diagram which will allow me to more easily label and think about things.") as tracker:
            self.play(Uncreate(diagram))
            self.remove((ptext))
            self.play(Unwrite(ptitle))
            self.play(Create(fbd))
        self.wait()

        # Write Parent Eqn And Move It To Corner
        eqn_text = MathTex(r"\Sigma F = ", "ma")
        eqn_text2 = MathTex(r"\Sigma F = ", "0")
        comp_text = MathTex(r"\Sigma F_{x} = 0", r", ", r"~ \Sigma F_{y} = 0")

        with self.voiceover(text="Remember that for these types of Force balance problems, we want to consider the equation F equals mass times acceleration."):
            self.play(Write(eqn_text))

        with self.voiceover(text="And for a system that is static (not moving) we can consider the acceleration to be zero!"):
            self.play(ReplacementTransform(eqn_text, eqn_text2))

        with self.voiceover(text="And on top of that, we can think about how the accerlation of this system must be zero in all directions, in this case, in the x and y directions."):
            self.play(ReplacementTransform(eqn_text2, comp_text))

        comp_text.generate_target()
        comp_text.target.to_corner(UP + RIGHT)
        self.play(MoveToTarget(comp_text))
        framebox1 = SurroundingRectangle(comp_text[0], buff = .1)
        framebox2 = SurroundingRectangle(comp_text[2], buff = .1)

        # Identify And Write Out X-Components
        xcomp_text = MathTex(r"-T_{1}cos(30^\circ)", r"+ T_{2}cos(45^\circ)", r" = 0").shift(RIGHT * 2)
        line_reference = Line().shift(fbd_origin).set_color(YELLOW)
        ang1 = Angle(line_reference, arrow1, radius=0.5, other_angle=False, quadrant=(-1,1))
        ang2 = Angle(line_reference, arrow2, radius=0.5, other_angle=False)
        ang1_text = MathTex(r"30^\circ").next_to(ang1.get_end(), LEFT, buff=0.5)
        ang2_text = MathTex(r"45^\circ").next_to(ang2.get_end(), RIGHT, buff=0.5)
        refs1 = VGroup(line_reference, ang1, ang1_text)

        with self.voiceover(text="Let's start by considering the x components of force in this system. I'm shifting the angle labels around a little bit here, it might be a good idea to check for yourself that these make sense."):
            self.play(Create(framebox1))
            self.wait(1)
            self.play(Create(refs1))

        t1_xcomp = Arrow(fbd_origin, (xfbd-0.5, 1, 0), buff=0).set_color(PINK)

        with self.voiceover(text="So we'll consider the x component of the first Tension force. Since it's going in the negative x direction I have to make sure to include the minus sign, and I'll do a little trigonometry to get the value"):
            self.play(Create(t1_xcomp))
            self.play(Write(xcomp_text[0]))
        self.wait(1)

        t2_xcomp = Arrow(fbd_origin, (xfbd+3, 1, 0), buff=0).set_color(PINK)
        refs2 = VGroup(ang2, ang2_text, t2_xcomp)
        
        with self.voiceover(text="Then I can do the same for the second tension force. We dont have to do anything with the weight of the block since it's force vector has no x components."):
            self.play(Uncreate(t1_xcomp))
            self.play(Create(refs2))
            self.play(Write(xcomp_text[1]))
            self.play(Write(xcomp_text[2]))

        self.wait(1)

        xcomp_text.generate_target()
        xcomp_text.target.to_corner(UP + RIGHT).shift(DOWN)
        self.play(MoveToTarget(xcomp_text))
        self.play(Uncreate(t2_xcomp))

        self.wait(1)
        self.play(Transform(framebox1, framebox2))

        # Identify And Write Out Y-Components
        ycomp_text = MathTex(r"-T_{1}sin(30^\circ)", r"+ T_{2}sin(45^\circ)", r" - 7 N", r"= 0").shift(RIGHT * 2)
        t1_ycomp = Arrow(np.array([xfbd-0.5, 1, 0]), arrow1.get_end(), buff=0).set_color(PINK)
        t2_ycomp = Arrow(np.array([arrow2.get_end()[0], 1, 0]), arrow2.get_end(), buff=0).set_color(PINK)
        w_ycomp = Arrow(fbd_origin, arrow3.get_end(), buff=0).set_color(PINK)

        with self.voiceover(text="Then we can do the same thing but for the y-components of the force vectors. First, T1. Notice here that the component is pointed down, so we have to consider it as negative."):
            self.play(Create(t1_ycomp))
            self.play(Write(ycomp_text[0]))
        self.play(Uncreate(t1_ycomp))

        with self.voiceover(text="Then T2, positive this time."):
            self.play(Create(t2_ycomp))
            self.play(Write(ycomp_text[1]))
        self.play(Uncreate(t2_ycomp))

        with self.voiceover(text="And this time we have to consider the fact that the weighted block is exerting a downward force on the system, so we'll include it here."):
            self.play(Create(w_ycomp))
            self.play(Write(ycomp_text[2:]))

        self.remove(w_ycomp)
        self.wait(1)

        ycomp_text.generate_target()
        ycomp_text.target.to_corner(UP + RIGHT).shift(DOWN * 2)
        self.play(MoveToTarget(ycomp_text))
        self.remove(framebox1, framebox2)
        self.wait(1)

        # Finish The Problem With Some Algebra
        eqn_text = VGroup(xcomp_text, ycomp_text)
        framebox3 = SurroundingRectangle(eqn_text, buff = .1).set_color(ORANGE)
        soln_text = MathTex(r"T_{1} = 19.1 N; T_{2} = 23.5 N").shift(RIGHT)

        with self.voiceover(text="Finally, notice that we have two equations and two unknowns, T1 and T2, which means we just need to do a little algebra to solve!"):
            self.play(Transform(framebox2, framebox3))
        self.wait(1)

        self.play(Write(soln_text))

        self.wait(2)