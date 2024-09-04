from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

class ProblemSample(Scene):
    def construct(self):
        # Cover image, self introduction
        cover_img = ImageMobject("moon-lady-pws.jpg").scale(0.5)
        self.play(FadeIn(cover_img))
        #self.wait(3)
        self.play(FadeOut(cover_img))

        # Problem Statement and Explanation
        ptext = MarkupText(f"Find the tension in each chord \nif the weight of the suspended object is 7 N.")
        self.play(Write(ptext))#, run_time=tracker.duration)

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
        self.add(diagram)
        self.wait()

        self.remove(diagram)
        self.remove(ptext)
        self.remove(ptitle)

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

        self.add(fbd)
        self.wait()

class ProblemExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService(silence_threshold=-40.0))
        text = MarkupText(f"PhysicsWithSean")
        with self.voiceover(text="Welcome, this is physicswithsean where I teach you how to solve physics practice problems.") as tracker:
            self.play(Write(text))
        self.play(FadeOut(text))    
        # Problem Statement

        text = MarkupText(f"Find the tension in each chord \nif the weight of the suspended object is 4 N.")
        with self.voiceover(text="In this problem, we want to find the tension in each chord if the weight of the suspended object is 4 N.") as tracker:
            self.play(Write(text), run_time=tracker.duration)

        title = MarkupText(f"Find the <span fgcolor='{YELLOW}'>tension in each chord</span> \nif the weight of the suspended object is <span fgcolor='{RED}'>4 N</span>.")
        title.to_corner(UP + LEFT)
        self.play(
            Transform(text, title),
        )
        self.wait()
        
        # Setup Problem
        xfbd = -6
        yfbd = 1
        ceiling = Line(start=(xfbd, yfbd, 0), end=(xfbd+4, yfbd, 0))

        chord1 = Line(start=(xfbd+0.5, yfbd, 0), end=(xfbd+2, yfbd-2, 0))
        chord2 = Line(start=(xfbd+3.5, yfbd, 0), end=(xfbd+2, yfbd-2, 0))
        chord3 = Line(start=(xfbd+2, yfbd-2, 0), end=(xfbd+2, yfbd-3, 0))
        weight = Polygon([xfbd+1.75, yfbd-3, 0], [xfbd+2.25, yfbd-3, 0], [xfbd+2.25, yfbd-3.5, 0], [xfbd+1.75, yfbd-3.5, 0]).set_color(RED)
        a1 = Angle(chord1, ceiling, radius=0.5, other_angle=False)
        a2 = Angle(chord2, ceiling, radius=0.5, other_angle=True, quadrant=(1,-1))
        a1_text = MathTex(r"30^\circ").scale(0.6).move_to(
            Angle(
                ceiling, chord1, radius=0.5 + 3 * SMALL_BUFF, other_angle=True
            ).point_from_proportion(0.5)
        )
        a2_text = MathTex(r"45^\circ").scale(0.6).move_to(
            Angle(
                ceiling, chord2, radius=0.5 + 3 * SMALL_BUFF, other_angle=True, quadrant=(1,-1)
            ).point_from_proportion(0.5)
        )
        fbd = VGroup(ceiling, chord1, chord2, chord3, a1, a2, a1_text, a2_text, weight)

        with self.voiceover(text="And the diagram provided looks something like this.") as tracker:
            self.play(Create(fbd), run_time=tracker.duration)

        self.wait(1)
        self.play(FadeOut(fbd))

        # Draw Free Body Diagram
        xfbd = -6
        yfbd = 2
        fbd_origin = np.array((xfbd+2, yfbd-2, 0))
        dot = Dot(fbd_origin)
        arrow1 = Arrow(fbd_origin, (xfbd+0.5, yfbd, 0), buff=0)
        arrow2 = Arrow(fbd_origin, (xfbd+3.5, yfbd, 0), buff=0)
        arrow3 = Arrow(fbd_origin, (xfbd+2, yfbd-4, 0), buff=0)

        a1_text = MathTex('T_{1}').next_to(arrow1.get_end(), RIGHT, buff=0.5)
        a2_text = MathTex('T_{2}').next_to(arrow2.get_end(), RIGHT, buff=0.3)
        a3_text = MathTex('4 N').next_to(arrow3.get_end(), RIGHT, buff=0.3)
        fbd = VGroup(dot, arrow1, arrow2, arrow3, a1_text, a2_text, a3_text)
        with self.voiceover(text="Whenever I am solving problems, I like to draw a Free Body Diagram \
            to make things easier to visualize. I'll label the forces on the chords and keep in mind the angles they make with the ceiling.") as tracker:
            self.play(FadeOut(title))
            self.play(FadeOut(text))
            self.play(Create(fbd, run_time=tracker.duration))
        
        # Write Parent Eqn And Move It To Corner
        eqn_text = MathTex(r"\Sigma F = ", "ma")
        eqn_text2 = MathTex(r"\Sigma F = ", "0")
        comp_text = MathTex(r"\Sigma F_{x} = 0", r", ", r"~ \Sigma F_{y} = 0")
        with self.voiceover(text="With these types of problems, we want to consider the equation: 'adding up all the applied forces equals mass times acceleration.") as tracker:
            self.add(eqn_text)
        with self.voiceover(text="The important insight here is that in a static system, the acceleration must be zero. So the sum of the forces must be zero.") as tracker:
            self.play(ReplacementTransform(eqn_text, eqn_text2))
        with self.voiceover(text="More specifically, we want to consider the x and y force components of the system, both of which must equal zero.") as tracker:
            self.play(ReplacementTransform(eqn_text2, comp_text))
            comp_text.generate_target()
            comp_text.target.to_corner(UP + RIGHT)
        self.play(MoveToTarget(comp_text))
        framebox1 = SurroundingRectangle(comp_text[0], buff = .1)
        framebox2 = SurroundingRectangle(comp_text[2], buff = .1)
        self.play(Create(framebox1))
        self.wait(1)
        
        # Identify And Write Out X-Components
        xcomp_text = MathTex(r"-T_{1}cos(30^\circ)", r"+ T_{2}cos(45^\circ)", r" = 0").shift(RIGHT * 2)
        line_reference = Line().shift(fbd_origin).set_color(YELLOW)
        ang1 = Angle(line_reference, arrow1, radius=0.5, other_angle=True, quadrant=(-1,1))
        ang2 = Angle(line_reference, arrow2, radius=0.5, other_angle=False)
        ang1_text = MathTex(r"30^\circ").next_to(ang1.get_end(), LEFT, buff=0.5)
        ang2_text = MathTex(r"45^\circ").next_to(ang2.get_end(), RIGHT, buff=0.5)
        refs1 = VGroup(line_reference, ang1, ang1_text)
        with self.voiceover(text="Let's consider the x components first, I'll draw a reference on our free body diagram and from that we can extract the x components of each tension.") as tracker:
            self.play(Create(refs1))

        t1_xcomp = Arrow(fbd_origin, (xfbd+0.5, 0, 0), buff=0).set_color(PINK)

        with self.voiceover(text="For the first tension, we can get the x-component of the force by multiplying the overall force T1 with the cosine of the angle it makes with the ceiling, 30 degrees. Make sure to include the minus sign here too since the force component is in the negative direction.") as tracker:
            self.play(Create(t1_xcomp))
            self.play(Write(xcomp_text[0]))
            self.wait(1)

        t2_xcomp = Arrow(fbd_origin, (xfbd+3.5, 0, 0), buff=0).set_color(PINK)
        refs2 = VGroup(ang2, ang2_text, t2_xcomp)
        self.remove(t1_xcomp)

        with self.voiceover(text="Similarly for T2, the x component of the force is T2 cosine of 45 degress. Then, the sum of these two force components must still equal zero.") as tracker:
            self.play(Create(refs2))
            self.play(Write(xcomp_text[1]))
            self.play(Write(xcomp_text[2]))
        xcomp_text.generate_target()
        xcomp_text.target.to_corner(UP + RIGHT).shift(DOWN)
        self.play(MoveToTarget(xcomp_text))
        self.remove(t2_xcomp)

        self.wait(1)
        self.play(Transform(framebox1, framebox2))
        
        # Identify And Write Out Y-Components
        ycomp_text = MathTex(r"T_{1}sin(30^\circ)", r"+ T_{2}sin(45^\circ)", r" - 4 N", r"= 0").shift(RIGHT * 2)
        t1_ycomp = Arrow(np.array([arrow1.get_end()[0], 0, 0]), arrow1.get_end(), buff=0).set_color(PINK)
        t2_ycomp = Arrow(np.array([arrow2.get_end()[0], 0, 0]), arrow2.get_end(), buff=0).set_color(PINK)
        w_ycomp = Arrow(fbd_origin, arrow3.get_end(), buff=0).set_color(PINK)
        with self.voiceover(text="With similar steps we can get the y-component for the first tension force.") as tracker:
            self.play(Create(t1_ycomp))
            self.play(Write(ycomp_text[0]))
        self.remove(t1_ycomp)

        with self.voiceover(text="And the second tension force.") as tracker:
            self.play(Create(t2_ycomp))
            self.play(Write(ycomp_text[1]))
        self.remove(t2_ycomp)

        with self.voiceover(text="And this time we need to consider the force applied by the block, 4 Newtons. We'll make sure to include that too and as a negative value since it's vector is pointed in the negative direction.") as tracker:
            self.play(Create(w_ycomp))
            self.play(Write(ycomp_text[2:]))

        self.remove(w_ycomp)
        ycomp_text.generate_target()
        ycomp_text.target.to_corner(UP + RIGHT).shift(DOWN * 2)
        self.play(MoveToTarget(ycomp_text))
        self.remove(framebox1, framebox2)
        self.wait(1)

        # Finish The Problem With Some Algebra
        eqn_text = VGroup(xcomp_text, ycomp_text)
        framebox3 = SurroundingRectangle(eqn_text, buff = .1).set_color(ORANGE)
        soln_text = MathTex(r"T_{1} = 3.59 N; T_{2} = 2.93 N").shift(RIGHT)

        with self.voiceover(text="Lastly, and perhaps unceremoniously, we can solve for T1 and T2 using our two equations we've made. The solution to this problem is T1 equals 3.59 Newtons and T2 equals 2.93 Newtons.") as tracker:
            self.play(Transform(framebox2, framebox3))
            self.play(Write(soln_text))
        self.wait(2)