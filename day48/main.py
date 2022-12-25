import requests
import smtplib
from bs4 import BeautifulSoup

URL = "https://www.amazon.in/dp/B098D615FK/ref=sspa_dk_detail_3?psc=1&pd_rd_i=B098D615FK&pd_rd_w=jlYDL&content-id=amzn1.sym.6c74ac28-0eba-4461-ba39-7b1bc57f1b6e&pf_rd_p=6c74ac28-0eba-4461-ba39-7b1bc57f1b6e&pf_rd_r=C6KQDVHBF7Q0B44G9GK6&pd_rd_wg=DXnYy&pd_rd_r=711da094-6bb6-45e4-bf7c-c9d2fc0878ab&s=electronics&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWwy"

response = requests.get(url=URL, headers={
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
})

###################################### parse the page using soup ###############################

amazon_page = response.text
soup = BeautifulSoup(amazon_page, parser="lxml", features="lxml")
page_parsed = soup.find(class_="a-price-whole").getText()

############ get current price from the parsed page ################

current_price = float(page_parsed.split(".")[0].replace(",", ""))
my_threshold_price = 2000

title = "Price drop on your tracked item "


def notify_email():
    message = f"{title} is now {current_price}"
    with smtplib.SMTP(example.com, port=587) as connection:
        connection.starttls()
        result = connection.login("example@gmail.com", "testpasswd")
        connection.sendmail(
            from_addr="example@gmail.com",
            to_addrs="example@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )


if current_price <= float(my_threshold_price):
    notify_email()
