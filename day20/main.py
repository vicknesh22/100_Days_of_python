from turtle import Turtle, Screen
import time

from snake import SnakeBluePrint

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = SnakeBluePrint()
screen.listen()
screen.onkey(snake.up, key="Up")
screen.onkey(snake.down, key="Down")
screen.onkey(snake.left, key="Left")
screen.onkey(snake.right, key="Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
