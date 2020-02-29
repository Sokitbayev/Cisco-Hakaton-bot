from random import randint

import telebot

bot = telebot.TeleBot('1095476545:AAHn5EOEn6Xyen3gZ28w5sDmJnvs_WNe4k0')


@bot.message_handler(commands=['start'])
def start(message):
    while(True):
        bot.send_message(message.from_user.id, 'Shamsh Pidr!!!')


bot.polling()
