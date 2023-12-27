import random
import datetime
import requests

from flask import Flask, render_template

app = Flask(__name__)
Gender_url = "https://api.genderize.io"
Age_url = "https://api.agify.io"


@app.route('/')
def hello():
    random_number = random.randint(0, 19)
    today = datetime.date.today()
    current_year = today.year
    return render_template('index.html', num=random_number, year=current_year)


@app.route('/guess/<string:name>')
def guess(name):
    gen_params = {
        "name": name
    }
    random_number = random.randint(0, 19)
    today = datetime.date.today()
    current_year = today.year

    response_gen = requests.get(url=Gender_url, params=gen_params)
    res_data = response_gen.json()["gender"]

    response_age = requests.get(url=Age_url, params=gen_params)
    res_data_age = response_age.json()["age"]

    return render_template('guess.html', greet=name, user_gen=res_data, user_age=res_data_age, year=current_year)


@app.route('/blog')
def blog():
    random_number = random.randint(0, 19)
    today = datetime.date.today()
    current_year = today.year
    response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    data = response.json()
    return render_template('blog.html', blog_data=data, year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
