from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

class BallOnStringOnWall(Scene):
    def construct(self):
        #self.set_speech_service(RecorderService(silence_threshold=-40.0))
        # Cover image, self introduction
        cover_img = ImageMobject("..\moon-lady-pws.jpg").scale(0.5)
        #with self.voiceover(text="Welcome Physics with Sean, let's do another practice problem.") as tracker:
        self.play(FadeIn(cover_img))
        self.wait()#duration=tracker.duration)
        self.play(FadeOut(cover_img))

        ptext = MarkupText(f"A sphere with diameter 32cm and mass 45kg is supported against a frictionless wall by a 30cm wire. Find the tension of the wire.")
        #with self.voiceover(text="In this problem, we want to find the tension in each chord if the weight of the suspended object is 7 N.") as tracker:
        self.play(Write(ptext))#, run_time=tracker.duration)

        ptitle = MarkupText(f"A sphere with <span fgcolor='{YELLOW}'>diameter 32cm and mass 45kg</span> is supported against a frictionless wall by a <span fgcolor='{YELLOW}'>30cm wire</span>. Find the <span fgcolor='{RED}'>tension of the wire</span>.")

        ptitle.to_corner(UP + LEFT)
        self.play(
            Transform(ptext, ptitle),
        )
        self.wait()