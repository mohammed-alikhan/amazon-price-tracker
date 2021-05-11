import requests

from bs4 import BeautifulSoup

import smtplib

import time

URL = 'https://www.amazon.in/Dualshock-Wireless-Controller-Playstation-Black/dp/B06WWR2GZF/ref=sr_1_1?dchild=1&keywords=ps4+controller&qid=1617646300&sr=8-1'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68'}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()

    converted_price = float(price[1:7].replace(',', ''))

    print(title.strip())
    print(converted_price)

    if(converted_price < 4000):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('mohammed.alikhan.9237@gmail.com', 'rifubtouikktnazt')

    subject = 'Price fell down!'
    body = 'Check the link https://www.amazon.in/Dualshock-Wireless-Controller-Playstation-Black/dp/B06WWR2GZF/ref=sr_1_1?dchild=1&keywords=ps4+controller&qid=1617646300&sr=8-1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'mohammed.alikhan.9237@gmail.com',
        'cntc.mak@gmail.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT')

    server.quit()


while(True):
    check_price()
    time.sleep(86400)
