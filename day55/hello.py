from flask import Flask

app = Flask(__name__)


# styling decorators
def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"

    return wrapper


def make_italic(function):
    def wrapper():
        return "<em>" + function() + "</em>"

    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"


#

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello World!</h1>' \
           '<p>My weather man says..</p>' \
           '<img src="https://media.giphy.com/media/l0HlPwMAzh13pcZ20/giphy.gif" width=300>'


@app.route('/username/<name>/<int:age>')
def greet_user(name, age):
    return f'Hi {name}! - you are {age} years old.'


@app.route('/bye')
@make_bold
@make_italic
def bye():
    return 'Bye!'


if __name__ == "__main__":
    # Run as debugger mode - to auto reload the page
    app.run(debug=True)
