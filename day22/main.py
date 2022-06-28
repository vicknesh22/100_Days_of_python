import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

# Screen object
screen = Screen()
screen.setup(width=1000, height=800)
screen.title("Ping - Pong")
screen.bgcolor("black")
screen.tracer(0)  # creating screen changes without any delay
# screen.delay(0) # no animation delay

r_paddle = Paddle((450, 0))
l_paddle = Paddle((-450, 0))
ball = Ball()
scoreboard = Score()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision to wall
    if ball.ycor() > 380 or ball.ycor() < -280:
        ball.bounce_y()
    # Detection with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 380 or ball.distance(l_paddle) < 50 and ball.xcor() < -380:
        ball.bounce_x()

    # Detect out of bound
    if ball.xcor() > 450:
        ball.reset_ball()
        scoreboard.left_score()
    if ball.xcor() < -450:
        ball.reset_ball()
        scoreboard.right_score()
    # score

screen.exitonclick()
