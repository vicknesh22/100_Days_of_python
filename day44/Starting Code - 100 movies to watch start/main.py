import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
web_data = response.text
soup = BeautifulSoup(web_data, "html.parser")
article_data = soup.find_all("h3", class_="title")
# article_title = article_data.getText()

movie_list = []

for article in article_data:
    movie_name = article.getText()
    movie_list.append(movie_name)

movie_list.reverse()
# for i in movie_list:
#     movie_list_data = f"{i}\n"

with open("Top_100_movie_list.txt", mode="w") as file:
    for i in movie_list:
        movie_list_data = f"{i}\n"
        file.write(movie_list_data)

