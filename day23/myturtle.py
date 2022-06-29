from turtle import Turtle


class Myturtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(1)
        self.color("white")
        self.penup()
        self.setheading(90)
        self.goto_start()

    def move_fd(self):
        self.forward(10)

    def goto_start(self):
        self.goto(0, -360)

    def move_bk(self):
        self.backward(10)

    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False

