from turtle import Screen
import time

from food import Food
from snake import SnakeBluePrint
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = SnakeBluePrint()
food = Food()
score_board = ScoreBoard(score=0)

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
    # Detecting Food coalition
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        # Extend snake
        snake.extend()
        # Creating a scoreboard
        score_board.increase_score()
    # Detect collision with the wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or \
            snake.snake_head.ycor() < -280:
        game_is_on = False
        score_board.game_over()

    # Detect collision with the Tail
    for segment in snake.snake_box[1:]:
        # if segment == snake.snake_head:
        #     pass
        if snake.snake_head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()
