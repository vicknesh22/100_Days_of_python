from turtle import Turtle

FONT = ('Courier', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self, score):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.score = 0
        self.score_update()

    def score_update(self):
        self.write(f"Score: {self.score} ", False, align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.score_update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, align="center", font=FONT)
