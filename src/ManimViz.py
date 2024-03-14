from manim import *
from IPython.display import display, HTML

class ListExplanation(Scene):
    def construct(self):
        # Define list and its elements
        list_name = Text("my_list", color=BLUE)
        square1 = Square(side_length=1, fill_color=YELLOW, fill_opacity=1)
        square2 = Square(side_length=1, fill_color=GREEN, fill_opacity=1)
        square3 = Square(side_length=1, fill_color=RED, fill_opacity=1)

        # Position elements
        list_name.move_to(UP * 2)
        square1.move_to(LEFT * 2)
        square2.move_to(ORIGIN)
        square3.move_to(RIGHT * 2)

        # Define list brackets
        left_bracket = Text("[", color=WHITE)
        right_bracket = Text("]", color=WHITE)
        left_bracket.next_to(square1, LEFT)
        right_bracket.next_to(square3, RIGHT)

        # Animations
        self.play(Write(list_name))
        self.play(
            FadeIn(left_bracket, shift=LEFT),
            FadeIn(square1, shift=LEFT),
            FadeIn(square2, shift=LEFT),
            FadeIn(square3, shift=LEFT),
            FadeIn(right_bracket, shift=RIGHT),
        )
        self.wait(2)

        # Explanation
        explanation = Tex(
            r"A list in Python is an ordered collection of elements. \\"
            r"Each element has an index starting from 0. \\"
            r"Lists are mutable, meaning elements can be added or removed."
        )
        explanation.move_to(DOWN * 2)
        self.play(Write(explanation))
        self.wait(5)

# Run the animation
if __name__ == "__main__":
    scene = ListExplanation()
    scene.render()