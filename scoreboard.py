from turtle import Turtle
ALIGN = "center"
FONT = ("Century Gothic", 13, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(10, 280)
        self.current_score = 0
        self.write(f"Score: {self.current_score}", False, align=ALIGN, font=FONT)
        self.clear()

    def update_score(self):
        self.clear()
        self.current_score += 1
        self.write(f"Score: {self.current_score}", False, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align=ALIGN, font=FONT)
