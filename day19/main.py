import turtle
from turtle import Turtle, Screen

tim = Turtle()


def forwards():
    tim.forward(50)


def back():
    tim.back(50)


def clock():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def anti():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=forwards)
screen.onkey(key="s", fun=back)
screen.onkey(key="a", fun=clock)
screen.onkey(key="d", fun=anti)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
