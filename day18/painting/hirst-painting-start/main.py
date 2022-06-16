###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import random
import turtle

import colorgram
from turtle import Turtle, Screen

turtle.colormode(255)
colors = colorgram.extract('image.jpg', 30)
rgb_colors = []


def rgb():
    for color in colors:
        rgb_colors.append(color.rgb)

    return rgb_colors


tim = Turtle()
tim.hideturtle()

#
def pattern():
    for j in range(10):
        tim.dot(20, random.choice(rgb()))
        tim.penup()
        tim.forward(50)


new_f = 0
for i in range(10):
    pattern()
    tim.home()
    tim.left(90)
    new_f += 50
    tim.forward(new_f)
    tim.right(90)

screen = Screen()
screen.exitonclick()
