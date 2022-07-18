import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. states Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#answer_state = screen.textinput(title="Guess the State", prompt="What is the state name?").title()

# print(answer_state)
# data = pandas.read_csv("50_states.csv")
# state_data = data[data.state == "Ohio"]
# xcord = int(state_data.x)
# print(xcord)
guessed_list = []
data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
while len(guessed_list) < 50:
    answer_state = screen.textinput(title=f"{guessed_list}/50. Guess the State",
                                    prompt="What is the state name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_list:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in state_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        x_cord = int(state_data.x)
        y_cord = int(state_data.y)
        t.goto(x_cord, y_cord)
        t.write(answer_state)
