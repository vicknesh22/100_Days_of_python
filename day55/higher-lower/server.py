from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)
app = Flask(__name__)


@app.route('/')
def guess_number():
    return '<h1 style="text-align: center">Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:user_number>')
def number_match(user_number):
    if int(random_number) > int(user_number):
        return '<h1 style="color: purple"> Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif int(random_number) < int(user_number):
        return '<h1 style="color: red">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif int(random_number) == int(user_number):
        return '<h1 style="color: green">You have found it. Yaay!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
