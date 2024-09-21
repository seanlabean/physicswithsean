from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

# Example call to process video
# python -m manim -pqh .\static-forces-000.py ProblemExplanation

class BallOnStringOnWall(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService(silence_threshold=-40.0))
        # Cover image, self introduction
        cover_img = ImageMobject("..\moon-lady-pws.jpg").scale(0.5)
        with self.voiceover(text="Welcome Physics with Sean, let's do another practice problem.") as tracker:
            self.play(FadeIn(cover_img))
            self.wait(duration=tracker.duration)
        self.play(FadeOut(cover_img))

        ptext = MarkupText(f"A sphere with diameter 32cm and mass 45kg \nis supported against a frictionless wall by a 30cm wire. \nFind the tension of the wire.", font_size=32)
        with self.voiceover(text="In this problem, we have a sphere with a diameter of 32cm and mass of 45kg. The sphere is supported against a wall by a 30cm wire. And we want to find the tension of the wire.") as tracker:
            self.play(Write(ptext), run_time=tracker.duration)

        ptitle = MarkupText(f"A sphere with <span fgcolor='{YELLOW}'>diameter 32cm and mass 45kg</span> \nis supported against a frictionless wall by a <span fgcolor='{YELLOW}'>30cm wire</span>. \nFind the <span fgcolor='{RED}'>tension of the wire</span>.", font_size=32)

        ptitle.to_corner(UP + LEFT)
        self.play(
            Transform(ptext, ptitle),
        )
        self.wait()

        # Draw Problem Diagram
        x = -4
        y = 1
        wall = Line(start=(x, y, 0), end=(x, y-3, 0))
        string = Line(start=wall.start, end=(x-0.75, y-2,0))
        ball = Circle(radius=0.75, color=RED).shift(LEFT*4.75, DOWN)
        radius = Line(start=string.end, end=string.end+np.array([ball.radius, 0, 0]), color=RED)
        #rbrace = Brace(string)
        #rbrace_text = rbrace.get_tex("32cm")
        #sbrace = Brace(string, direction=string.copy().rotate(3*PI/2).get_unit_vector())
        #sbrace_text = sbrace.get_tex("30cm")
        stext = Text("30cm", font_size=20).next_to(string.start, LEFT*1.5 + DOWN*2.5)
        rtext = Text("16cm", font_size=20).next_to(radius, DOWN)
        angle = Angle(string, wall, radius=0.5, other_angle=False)
        angle_text =  MathTex(r"\theta").scale(0.6).move_to(
            Angle(
                wall, string, radius=0.5 + 3 * SMALL_BUFF, other_angle=True
            ).point_from_proportion(0.5)
        )

        diagram = VGroup(wall,string,ball,angle,angle_text)
        with self.voiceover(text="As always, before we start getting freaked out by all this text, let's draw a quick picture to better visualize the problem.") as tracker:
            self.play(Create(diagram), run_time=tracker.duration)
        labels = VGroup(stext, rtext, radius)
        with self.voiceover(text="So we've got that ball against the wall there, I'll just label a few things.") as tracker:
            self.play(Create(labels), run_time=tracker.duration)
        self.wait()

        # Get Angle Before Anything Else
        theta_eqn_text0 = MathTex(r"\text{sin}(\theta) = ", r"\frac{\text{opposite}}{\text{hypotenuse}}")
        theta_eqn_text1 = MathTex(r"\theta = ", r"\text{sin}^{-1}\Big(\frac{\text{opposite}}{\text{hypotenuse}}\Big)")
        theta_eqn_text2 = MathTex(r"\theta = ", r"\text{sin}^{-1}\Big(\frac{\text{16 \text{cm}}}{30 \text{cm}}\Big)")
        theta_eqn_text3 = MathTex(r"\theta = ", r"20.4^\circ")
        with self.voiceover(text="Before we get going with anything else, I want to find the angle the wire makes with the wall. We can do this easily by using our trigonometry knowledge: sine of an angle is equal to the ratio of the opposite and hypotenuse sides. And we can plug in 16cm for the opposite side (ball radius) and 30cm for the hypotenuse (wire length) ") as tracker:
            self.play(Write(theta_eqn_text0), run_time=tracker.duration/4)
            self.play(ReplacementTransform(theta_eqn_text0, theta_eqn_text1), run_time=tracker.duration/4); self.remove(theta_eqn_text0)
            self.play(ReplacementTransform(theta_eqn_text1, theta_eqn_text2), run_time=tracker.duration/4); self.remove(theta_eqn_text1)
            self.play(ReplacementTransform(theta_eqn_text2, theta_eqn_text3), run_time=tracker.duration/4); self.remove(theta_eqn_text2)

        theta_eqn_text3.generate_target()
        theta_eqn_text3.target.to_corner(UP+RIGHT)
        self.play(MoveToTarget(theta_eqn_text3))
        # Draw Free Body Diagram
        self.remove(ptext)
        self.play(Unwrite(ptitle))
        task_reminder = MarkupText(f"Find the <span fgcolor='{RED}'>tension of the wire</span>.", font_size=32).to_corner(UP + LEFT)
        self.play(Create(task_reminder))

        diagram = VGroup(diagram, labels)

        diagram.shift(UP*1.5)

        fbdT = Arrow(ball.get_center(), wall.start + np.array([0.0,1.0,0.0]), buff=0)
        fbdT_label = MathTex('T').next_to(fbdT.get_end(), RIGHT, buff=0.2)
        fbdN = Arrow(ball.get_center(), ball.get_center() - np.array([1.0,0,0]), buff=0)
        fbdN_label = MathTex('N').next_to(fbdN.get_end(), UP, buff=0.2)
        fbdG = Arrow(ball.get_center(), ball.get_center() - np.array([0,1.0,0]), buff=0)
        fbdG_label = MathTex('mg').next_to(fbdG.get_end(), RIGHT, buff=0.2)

        fbd = VGroup(fbdT, fbdN, fbdG, fbdT_label, fbdN_label, fbdG_label)
        with self.voiceover(text="We can simplify our picture into a free-body-diagram, showing the tension of the wire, the weight of the ball, and the Normal force acting on the ball as it presses on the wall.") as tracker:
            self.play(Uncreate(diagram), Create(fbd), run_time=tracker.duration)
            #self.play(Create(fbd), run_time=tracker.duration/2)
            
        # Solve For T
        forcesy0 = MathTex(r"\Sigma F_{y} = 0")
        forcesy1 = MathTex(r"T\text{cos}(\theta) - mg = 0")

        with self.voiceover(text="To find the tension of the wire, we can consider the y-components of forces acting on the system.") as tracker:
            self.play(Write(forcesy0), run_time=tracker.duration)

        fdbTy = Arrow(fbdT.get_start(), np.array([fbdT.get_start()[0],wall.start[1]+1.05,0]), buff=0).set_color('PINK')
        fbdTy_ang = Angle(fdbTy, fbdT, other_angle=True)

        with self.voiceover(text="For y-components, we have the y component of the tension which we can isolate with a little help from cosine, and the force of gravity acting downwards on the ball.") as tracker:
            self.play(Unwrite(forcesy0))
            self.play(Write(forcesy1), Create(fdbTy), Create(fbdTy_ang), fbdG.animate.set_color('PINK'), run_time=tracker.duration)
        
        forcesy2 = MathTex(r"T\text{cos}(20.4^\circ) - (45kg)*(9.8\frac{m}{s^2}) = 0")

        forcesy3 = MathTex(r"T = 470 N")

        with self.voiceover(text="Plugging in some numbers, we find that the tension T is 470 Newtons.") as tracker:
            self.play(Unwrite(forcesy1))
            self.play(Write(forcesy2), run_time=tracker.duration/2)
            self.play(Transform(forcesy2, forcesy3), run_time=tracker.duration/2)
            self.remove(forcesy2)
        
        self.play(forcesy3.animate.to_corner(UP + RIGHT).shift(DOWN))

        # How Hard Does Ball Push On Wall?
        self.play(Uncreate(fdbTy), Uncreate(fbdTy_ang), fbdG.animate.set_color('WHITE'))
        self.play(Unwrite(task_reminder))

        task_reminder = MarkupText(f"How hard does the ball push on the wall?", font_size=32).to_corner(UP + LEFT)

        with self.voiceover(text="There's a second part of this problem that asks, 'how hard does the ball push on the wall'?") as tracker:
            self.play(Write(task_reminder))

        fbdTx = Arrow(fbdT.get_start(), np.array([fbdT.get_end()[0],0.5,0]), buff=0).set_color('PINK')
        forcesx0 = MathTex(r"T\text{sin}(\theta) - N = 0")
        forcesx1 = MathTex(r"N = T\text{sin}(\theta)")
        forcesx2 = MathTex(r"N = 163 N")

        with self.voiceover(text="There's a trick to this one: we have to remember that the Normal force represents the reaction to the ball pushing on the wall, so the value of the normal force is our answer!") as tracker:
            self.play(Create(fbdTx), fbdN.animate.set_color('PINK'), Write(forcesx0))
        with self.voiceover(text="And we can solve that quickly by plugging in for theta and T which we have from before") as tracker:
            self.play(Transform(forcesx0, forcesx1), run_time=tracker.duration/3)
            self.remove(forcesx0, forcesx1)
            self.play(Transform(forcesx1, forcesx2), run_time=tracker.duration/3)

        with self.voiceover(text="Thanks for watching! Let me know fi you have any questions or thoughts.") as tracker:
            self.wait(duration=tracker.duration)
