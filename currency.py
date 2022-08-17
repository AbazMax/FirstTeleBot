import requests
import datetime

site = requests.get("https://minfin.com.ua/currency/usd/")


def get_usd_black():
    bmindex = (site.text.find('<a href="/currency/auction/usd/buy/all/">ЧЕРНЫЙ РЫНОК</a>'))
    bm_buy = site.text[bmindex:bmindex + 150]
    bm_sell = site.text[bmindex + 250:bmindex + 300]
    bm_buy_value = ""
    bm_sell_value = ""
    dt = datetime.datetime.now()
    for i in bm_buy:
        if i.isdigit() or i == ".":
            bm_buy_value += i

    for i in bm_sell:
        if i.isdigit() or i == ".":
            bm_sell_value += i
    return f"{dt.strftime('Date: %d/%m/%Y  time: %H:%M:%S')} \nПокупка - {bm_buy_value}\nПродажа - {bm_sell_value}"



print(get_usd_black())

# print(site.text)
