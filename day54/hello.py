# import requests
# response = requests.get("https://www.google.com")
# print(response.text)

# # First flask
# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
#
#
# # execute the code
# if __name__ == "__main__":
#     app.run()

# python decorator function
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/bye')
def bye():
    return 'bye!'

if __name__ == '__main__':
    app.run()