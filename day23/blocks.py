from turtle import Turtle
import random

colours = ["white", "red", "blue", "yellow", "pink"]


class Blocks(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.car_speed = 30

    def line_block(self):
        random_chance = random.randint(1, 4)
        if random_chance == 1:
            box = Turtle("square")
            box.shapesize(stretch_wid=1, stretch_len=3)
            box.color(random.choice(colours))
            #box.speed(r_speed)
            box.penup()
            random_y = random.randint(-250, 280)
            # random_x = random.randint(350, -350)
            box.goto(500, random_y)
            self.segments.append(box)

    def move_blocks(self):
        for box_num in self.segments:
            box_num.backward(self.car_speed)

    def level_up(self):
        self.car_speed += 30


