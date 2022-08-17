import telebot
import os

bot = telebot.TeleBot("5705328355:AAFedN19S5plliZ90Nv4G-KD33cnPuXAAEI")


@bot.message_handler(commands=["start"])
def start(message):
    mess = f"Привет {message.from_user.first_name}"
    bot.send_message(message.chat.id, mess, parse_mode="html")


#@bot.message_handler()
#def get_message(text):
#    if text == "wiki":
#        search_text = input("What do you search?")
#        return wiki()

@bot.message_handler()
def wiki(search_text):
    result = url = "https://ru.wikipedia.org/wiki/" + str(search_text.text)
    bot.send_message(search_text.chat.id, result, parse_mode="html")


bot.polling(non_stop=True)
