from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

# Example call to process video
# python -m manim -pqh .\static-forces-000.py ProblemExplanation

class BallOnStringOnWall(Scene):
    def construct(self):
        #self.set_speech_service(RecorderService(silence_threshold=-40.0))
        # Cover image, self introduction
        cover_img = ImageMobject("..\moon-lady-pws.jpg").scale(0.5)
        #with self.voiceover(text="Welcome Physics with Sean, let's do another practice problem.") as tracker:
        self.play(FadeIn(cover_img))
        self.wait()#duration=tracker.duration)
        self.play(FadeOut(cover_img))

        ptext = MarkupText(f"A sphere with diameter 32cm and mass 45kg \nis supported against a frictionless wall by a 30cm wire. \nFind the tension of the wire.", font_size=32)
        #with self.voiceover(text="In this problem, we want to find the tension in each chord if the weight of the suspended object is 7 N.") as tracker:
        self.play(Write(ptext))#, run_time=tracker.duration)

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
        self.play(Create(diagram))
        labels = VGroup(stext, rtext, radius)
        self.play(Create(labels))
        self.wait()

        # Get Angle Before Anything Else
        theta_eqn_text0 = MathTex(r"\text{sin}(\theta) = ", r"\frac{\text{opposite}}{\text{hypotenuse}}")
        theta_eqn_text1 = MathTex(r"\theta = ", r"\text{sin}^{-1}\Big(\frac{\text{opposite}}{\text{hypotenuse}}\Big)")
        theta_eqn_text2 = MathTex(r"\theta = ", r"\text{sin}^{-1}\Big(\frac{\text{16 \text{cm}}}{30 \text{cm}}\Big)")
        theta_eqn_text3 = MathTex(r"\theta = ", r"20.4^\circ")
        self.play(Write(theta_eqn_text0))
        self.play(ReplacementTransform(theta_eqn_text0, theta_eqn_text1)); self.remove(theta_eqn_text0)
        self.play(ReplacementTransform(theta_eqn_text1, theta_eqn_text2)); self.remove(theta_eqn_text1)
        self.play(ReplacementTransform(theta_eqn_text2, theta_eqn_text3)); self.remove(theta_eqn_text2)

        self.wait(2)

        theta_eqn_text3.generate_target()
        theta_eqn_text3.target.to_corner(UP+RIGHT)
        self.play(MoveToTarget(theta_eqn_text3))
        # Draw Free Body Diagram
        self.play(Unwrite(ptitle))
        task_reminder = MarkupText("Find the <span fgcolor={RED}>tension of the wire<span>.", font_size=32).to_corner(UP + LEFT)
        self.play(Create(task_reminder))

        # Solve For T

        # How Hard Does Ball Push On Wall?