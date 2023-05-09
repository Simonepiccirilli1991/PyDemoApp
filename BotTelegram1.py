import os

import telebot
from ScrappingUtils import web_scrapping

BOT_TOKEN = '5971884557:AAHEML5YzXTfMrB4Z0AOJZaPEaA-LEylOPw'

bot = telebot.TeleBot(BOT_TOKEN)


#@bot.message_handler(func=lambda msg: True)
#def echo_all(message):
#    bot.reply_to(message, message.text)


@bot.message_handler(commands=['start', 'hello'])
def saluta(message):
    bot.reply_to(message, 'Salve Signore, come posso aiutarla oggi?')


@bot.message_handler(commands=['scrapping'])
def scrapper(message):
    text = "What's site u wanna scrap?\nChoose one: *Lego*, *Amazon*, *Ebay*, *Cazzoneso* ."
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, scrap_handler)


def scrap_handler(message):
    sito = message.text
    print('ecco il sito', sito)
    text = "What word are u looking for?\nChoose one: *Harry Potter*, *Star Wars*, *Marvel*, or a whatewer u want."
    sent_msg = bot.send_message(
        message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(
        sent_msg, fetch_scrapping, sito)


def fetch_scrapping(message, sito):
    parola = message.text
    resp = web_scrapping(sito, parola)
    scrap_message = f'Risultati: Sito:{sito}\\ Parola:{parola}\\ Risultato: {resp}'
    bot.send_message(message.chat.id, "Here's your response!")
    bot.send_message(message.chat.id, scrap_message)


bot.infinity_polling()