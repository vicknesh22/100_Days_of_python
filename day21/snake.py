from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class SnakeBluePrint:
    def __init__(self):
        self.snake_box = []
        self.position = [(0, 0), (-20, 0), (-40, 0)]
        self.create_snake()
        self.snake_head = self.snake_box[0]

    def create_snake(self):
        for i in self.position:
            self.add_segment(i)

    def add_segment(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.speed("slow")
        snake.penup()
        self.snake_box.append(snake)

    def extend(self):
        self.add_segment(self.snake_box[-1].position())

    def move(self, ):
        for snake_num in range(len(self.snake_box) - 1, 0, -1):
            new_x = self.snake_box[snake_num - 1].xcor()
            new_y = self.snake_box[snake_num - 1].ycor()
            self.snake_box[snake_num].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
