import random
import time
from turtle import Screen
from myturtle import Myturtle
from blocks import Blocks
from score import Score

# creating screen canvas
screen = Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)

tim = Myturtle()
bar = Blocks()
score_board = Score()
screen.listen()
screen.onkey(tim.move_fd, "Up")
screen.onkey(tim.move_bk, "Down")

#    bar.move_blocks()

game_is_on = True

while game_is_on:

    time.sleep(0.1)
    screen.update()

    bar.line_block()
    bar.move_blocks()

    # Detect collision of box with turtle
    for box in bar.segments:
        if box.distance(tim) < 20:
            game_is_on = False
            score_board.game_over()

    if tim.is_at_finish_line():
        tim.goto_start()
        bar.level_up()
        score_board.update_score()

screen.exitonclick()
