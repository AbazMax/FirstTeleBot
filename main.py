import telebot
from telebot import types
import requests
import datetime


bot = telebot.TeleBot("5705328355:AAFedN19S5plliZ90Nv4G-KD33cnPuXAAEI")


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Поиск в Википедии")
    item2 = types.KeyboardButton("Курс валют")
    markup.add(item1)
    markup.add(item2)
    mess = f"Привет {message.from_user.first_name}, что хочешь узнать?\nЖми на кнопку"
    bot.send_message(message.chat.id, mess, reply_markup=markup, parse_mode="html")



@bot.message_handler()
def main(massage):
    if massage.text == "Поиск в Википедии":
        search_text = bot.send_message(massage.chat.id, "Что хочешь найти?")
        bot.register_next_step_handler(search_text, wiki)
    elif massage.text == "Курс валют":
        bot.send_message(massage.chat.id, get_usd_black())
    else:
        bot.send_message(massage.chat.id, "Жми на кнопки")

def wiki(search_text):
    result = url = "https://ru.wikipedia.org/wiki/" + str(search_text.text)
    bot.send_message(search_text.chat.id, result, parse_mode="html")

def get_usd_black():
    site = requests.get("https://minfin.com.ua/currency/usd/")
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
    return f"USD на наличном рынке:\n{dt.strftime('Дата: %d/%m/%Y  Время: %H:%M:%S')} \nПокупка - {bm_buy_value}\nПродажа - {bm_sell_value}"

bot.polling(non_stop=True)

