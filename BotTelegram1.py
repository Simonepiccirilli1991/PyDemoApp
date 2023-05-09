import os

import telebot

BOT_TOKEN = '5971884557:AAHEML5YzXTfMrB4Z0AOJZaPEaA-LEylOPw'

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hello Sir, how are you doing?")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()