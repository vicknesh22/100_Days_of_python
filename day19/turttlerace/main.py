from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle colour will win: ")
print(user_bet)

is_race_on = False

colors = ["red", "green", "orange", "blue", "purple", "yellow"]
all_turtles = []
new_y = -100

for turtle_index in range(0, 6):
    new_turtles = Turtle(shape="turtle")
    new_turtles.penup()
    new_turtles.shapesize(1)
    new_turtles.color(colors[turtle_index])
    new_turtles.goto(x=-230, y=new_y)
    new_y += 50
    all_turtles.append(new_turtles)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)
        current_pos = turtle.position()
        if turtle.xcor() > 230:
            win_color = turtle.pencolor()
            is_race_on = False
            if user_bet == win_color:
                print(f"User has won {win_color} has finished first.")
            else:
                print(f"User has lost the race, {win_color} turtle has won the race.")


screen.exitonclick()
