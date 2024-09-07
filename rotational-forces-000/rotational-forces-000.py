from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

class AroundALoop0(Scene):
    def construct(self):
        #self.set_speech_service(RecorderService(silence_threshold=-40.0))
        # Cover image, self introduction
        cover_img = ImageMobject("..\moon-lady-pws.jpg").scale(0.5)
        #with self.voiceover(text="Welcome Physics with Sean, let's do another practice problem.") as tracker:
        self.play(FadeIn(cover_img))
        self.wait()#duration=tracker.duration)
        self.play(FadeOut(cover_img))
