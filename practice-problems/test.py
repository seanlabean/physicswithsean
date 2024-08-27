from manim import *

# Simply inherit from VoiceoverScene instead of Scene to get all the
# voiceover functionality.
class ProblemIntroduction(Scene):
    def construct(self):
        ceiling = Line(start=(-5, 2, 0), end=(-1, 2, 0))

        chord1 = Line(start=(-4.5, 2, 0), end=(-3, 0, 0))
        chord2 = Line(start=(-1.5, 2, 0), end=(-3, 0, 0))
        chord3 = Line(start=(-3, 0, 0), end=(-3, -1, 0))
        a1 = Angle(chord1, ceiling, radius=0.5, other_angle=False)
        a2 = Angle(chord2, ceiling, radius=0.5, other_angle=False)
        tetx = Text(f"30").scale(0.5).move_to(
            Angle(
                ceiling, chord1, radius=0.5 + 3 * SMALL_BUFF, other_angle=True
            ).point_from_proportion(0.5)
        )
        self.add(ceiling, chord1, chord2, chord3, a1, a2, tetx)
        text=MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))