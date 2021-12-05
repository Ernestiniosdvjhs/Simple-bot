import telebot
from telebot import types

import random

token = "2112003461:AAEMjMougJLgphJX_D2thgHBtOqs7X2Ukws"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Вот список моих команд:\n/help - список команд\n/sticker - отправлю тебе стикер\n/start - если хочешь узнать информацию о нашем вузе')


@bot.message_handler(commands=['sticker'])
def start_message(message):
    j = random.randint(1, 3)
    if j == 1:
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEDYfVhpPt8tKQl1ilRSzdJrri9qNiuOAACFAADwDZPE61lmeS5MPY-IgQ")
    elif j == 2:
        bot.send_sticker(message.chat.id, "CAACAgQAAxkBAAEDY7FhpgGmtQu4JMvgM_z0TZsVIc3hogACiAADcKvVBHQNr5yr6ckOIgQ")
    elif j == 3:
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEDY7NhpgHG4WvokyblSSC39Zu4m4xZ3wACkQIAAm2bihcJSCUSLgIMYyIE")


@bot.message_handler(commands=['photo'])
def start_message(message):
    bot.send_message(message.chat.id, 'Держи: https://www.instagram.com/mtuci.official/')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    elif message.text.lower() == "привет" or message.text.lower() == "здравствуй" or message.text.lower() == "hi":
        bot.send_message(message.chat.id, 'Здравствуй! Не хочешь посетить наш сайт? Если да, то напиши "Хочу".')
    elif message.text.lower() == "пока":
        bot.send_message(message.chat.id, 'До встречи')
    else:
        i = random.randint(0, 2)
        if i == 0:
            bot.send_message(message.chat.id, 'Чего ты несешь?')
        if i == 1:
            bot.send_message(message.chat.id, 'Что?')
        if i == 2:
            bot.send_message(message.chat.id, 'Ай донт ноу')


bot.polling(non_stop=True)
