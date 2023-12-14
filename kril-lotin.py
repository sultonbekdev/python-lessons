#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 11:53:49 2023

@author: aepeul
"""

# from transliterate import to_cyrillic, to_latin
import telebot

TOKEN='6708295216:AAFoztdtlfg4hA8nvBneuJOXlmp1UyCnCoY'

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob="Assalomu allaykum xush kelibsiz!"
    javob += "\nMatn kiriting!"
    bot.reply_to(message,javob)
        
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg=message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))
bot.polling()

# matn=input("Matn kiriting! ")
# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))    