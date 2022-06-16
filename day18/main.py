import turtle
from turtle import Turtle, Screen
import random

my_turtle = Turtle()

# turtle attributes
my_turtle.shape("turtle")
my_turtle.resizemode("auto")
my_turtle.color("green")

# # square - challenge-1
# for i in range(4):
#     my_turtle.forward(100)
#     my_turtle.right(90)

# # Dash line - challenge-2
#
# for _ in range(15):
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)
#     my_turtle.pendown()
#     my_turtle.forward(10)

# drawing different shapes - challenge-3
# num_of_sides = 3
# color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
#
# def shapes(num_of_sides):
#     angle = 360 / num_of_sides
#     for i in range(num_of_sides):
#         my_turtle.forward(100)
#         my_turtle.right(angle)
#
#
# for shapes_side in range(3, 10):
#     my_turtle.color(random.choice(color))
#     shapes(shapes_side)

# # Random walk - challenge - 4
#
# color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# my_turtle.hideturtle()
# my_turtle.pensize(15)
# my_turtle.speed("fastest")
# sides = ["right", "left", "right", "left", "right", "left"]
#
#
# def random_move(direction, colour):
#     my_turtle.color(colour)
#     my_turtle.forward(20)
#     if direction == "right":
#         my_turtle.rt(90)
#     elif direction == "left":
#         my_turtle.lt(90)
#     my_turtle.forward(20)
#
#
# for i in range(0, 200):
#     new_color = random.choice(color)
#     new_dir = random.choice(sides)
#     random_move(new_dir, new_color)

# circle
turtle.colormode(255)
my_turtle.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_colour = (r, g, b)
    return rand_colour




for i in range(200):
    new_pos = my_turtle.heading() + 10
    my_turtle.color(random_color())
    my_turtle.circle(100)
    my_turtle.setheading(new_pos)

# GuI popup
screen = Screen()
screen.exitonclick()
