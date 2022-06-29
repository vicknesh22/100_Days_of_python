from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-300, 340)
        self.scorep = 0
        self.update_score()


    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("courier", 40, "normal"))


    def update_score(self):
        self.clear()
        self.scorep += 1
        self.write(f"ScoreBoard: {self.scorep}", align="center", font=("courier", 20, "normal"))
