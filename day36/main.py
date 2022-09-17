import requests
import datetime as dt
import emoji

import os
from twilio.rest import Client

# https://unicode.org/emoji/charts/emoji-list.html
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
day_before = date_now - dt.timedelta(days=2)

# print(yesterday_date)

####### getting yesterday data from stock endpoint

stock_daily_dic = stock_url_json['Time Series (Daily)']
yesterday_stock = stock_daily_dic.get(str(yesterday_date))
day_before_stock = stock_daily_dic.get(str(day_before))

stock_day_before = float(day_before_stock.get('4. close'))
stock_yesterday_close = float(yesterday_stock.get('4. close'))
change = stock_yesterday_close - stock_day_before
stock_changes = abs(stock_yesterday_close - stock_day_before)
# abs - absolute value function - to get positive difference between the numbers
diff_price = stock_changes
diff_percent = (diff_price * 100) / stock_yesterday_close

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


def get_news():
    global STOCK_API_ENDPOINT, news_parameters
    news_url = requests.get(STOCK_API_ENDPOINT, news_parameters)
    news_update = news_url.json()
    # print(news_update)
    sentiment_score = news_update["sentiment_score_definition"]
    title_list = []
    for key in news_update["feed"]:
        title_list.append(key["title"])

    return title_list[:4]


news_sms = ""

up_down = None
if change > 0:
    up_down = "up"
elif change == 0:
    up_down = "no-change"
elif change > 0:
    up_down = "down"

if diff_percent > 5:
    news_sms = get_news()

# sending SMS

account_sid = os.environ.get("TW_ACC")
auth_token = os.environ.get("AUTH_TOKEN")

client = Client(account_sid, auth_token)
message = client.messages \
    .create(
    body=f"{STOCK_NAME}: Change in price from yesterday: {diff_percent}  {up_down}\n Recent-News: {news_sms}",
    from_='+17075173593',
    to='+918012895962'
)

print(message.status)
