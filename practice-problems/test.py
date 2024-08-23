from manim import *

# Simply inherit from VoiceoverScene instead of Scene to get all the
# voiceover functionality.
class ProblemIntroduction(Scene):
    def construct(self):
        text = MarkupText(f"Find the tension in each chord if the weight of the suspended object is w.")
        self.play(Write(text))
        text = MarkupText(f"Find the <span fgcolor='{YELLOW}'>tension in each chord</span> if the weight of the suspended object is <span fgcolor='{RED}'>w</span>.")
        self.play(Write(text))