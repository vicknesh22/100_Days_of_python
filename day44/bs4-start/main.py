import os
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article = soup.find_all(class_="titleline")

article_text = []
article_links = []

for article_tag in article:
    text = article_tag.getText()
    article_text.append(text)
    link = article_tag.find(name="a").get("href")
    article_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_text)
# print(article_links)
# print(article_upvote)
largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)

popular_article = article_links[largest_index]
print(popular_article)



























# with open("website.html", mode="r") as file:
#     contents = file.read()
#     #print(contents)
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.prettify())
# print(soup.title)
