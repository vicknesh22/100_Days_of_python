import turtle
from turtle import Turtle, Screen

timmy = Turtle()
# print(timmy)
# changing turtle attributes
timmy.shape("turtle")
timmy.color("DarkSeaGreen2")
timmy.shapesize(5, 5, 12)
timmy.shapesize(outline=8)

# Moving the turtle

timmy.fd(0)
print(timmy.position())
timmy.speed(4)
timmy.lt(180)
timmy.pendown()
timmy.pencolor("coral")
timmy.pensize(5)
timmy.fd(600)

# Screen attributes
my_screen = Screen()
my_screen.title("Welcome To Turtle Show!!!")
# print(my_screen.canvheight)
my_screen.exitonclick()
