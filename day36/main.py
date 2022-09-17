import requests
import datetime as dt
import time
import os
from twilio.rest import Client

######## getting stock from endpoint
STOCK_API_KEY = "6WAMRLI3CEN6D4OV"
STOCK_API_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_NAME = "INFY.BSE"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "datatype": "json",
    "apikey": STOCK_API_KEY,
    "symbol": STOCK_NAME,
    "outputsize": "compact"
}

stock_url = requests.get(STOCK_API_ENDPOINT, params=parameters)
stock_url_json = stock_url.json()

# print(stock_url_json)

######### getting yesterday data alone

date_now = dt.date.today()

yesterday_date = date_now - dt.timedelta(days=1)

# print(yesterday_date)
####### getting yesterday data from stock endpoint

stock_daily_dic = stock_url_json['Time Series (Daily)']
yesterday_stock = stock_daily_dic.get(str(yesterday_date))

stock_open = float(yesterday_stock.get('1. open'))
stock_close = float(yesterday_stock.get('4. close'))
stock_changes = stock_open - stock_close
diff_price = stock_changes
### relevant news about the stock

STOCK_CODE = "INFY"

news_parameters = {
    "function": "NEWS_SENTIMENT",
    "datatype": "json",
    "apikey": STOCK_API_KEY,
    "tickers": STOCK_CODE,
    "sort": "LATEST",
    "limit": "5",
    "outputsize": "compact"
}

news_url = requests.get(STOCK_API_ENDPOINT, news_parameters)
news_update = news_url.json()
# print(news_update)
sentiment_score = news_update["sentiment_score_definition"]
title_list = []
for key in news_update["feed"]:
    title_list.append(key["title"])

news_sms = title_list[:4]

# sending SMS

account_sid = os.environ.get("TW_ACC")
auth_token = os.environ.get("AUTH_TOKEN")

client = Client(account_sid, auth_token)
message = client.messages \
    .create(
    body=f"{STOCK_NAME}: Changing price from yesterday: {diff_price} \n Recent-News: {news_sms}",
    from_='+17075173593',
    to='+918012895962'
)

print(message.status)