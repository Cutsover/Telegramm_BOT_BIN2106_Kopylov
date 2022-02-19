import telebot
import datetime
import random
import requests


from telebot import types
from knowledgebase import token
from knowledgebase import answer1
from knowledgebase import answer2
from knowledgebase import mesyac
from knowledgebase import den_ned
from knowledgebase import answer_help
from knowledgebase import answer_else
from knowledgebase import cit_marks
from knowledgebase import ans_marginal
from knowledgebase import anekdots
from knowledgebase import weather_token
from knowledgebase import ans_autor


bot = telebot.TeleBot(token)


#клавиатура 1
keyboard1 = types.ReplyKeyboardMarkup()
keyboard1.row("Хочу")
keyboard1.add("Кто нас учит", "Ссылки")
keyboard1.add("Пинг", "Анекдот")
keyboard1.add("/help", "/time")
keyboard1.add("/randomiser", "/links")

#клавиатура 2
keyboard2 = types.ReplyKeyboardMarkup()
keyboard2.add("Да, я хочу цитату Карла Маркса")
keyboard2.row("Хочу")
keyboard2.add("Кто нас учит", "Ссылки")
keyboard2.add("Пинг", "Анекдот")
keyboard2.add("/help", "/time")
keyboard2.add("/randomiser", "/links")



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать новую информацию о МТУСИ?', reply_markup=keyboard1)

@bot.message_handler(commands = ['help'])
def help(message):
    bot.send_message(message.chat.id, answer_help)

@bot.message_handler(commands = ['randomiser'])
def randomiser(message):
    bot.send_message(message.chat.id, random.randrange(-10000, 10000), reply_markup=keyboard1)


@bot.message_handler(commands = ['links'])
def links(message):
    bot.send_message(message.chat.id, ans_autor, reply_markup=keyboard1)


@bot.message_handler(commands = ['time'])
def time(message):
    nums = int(datetime.datetime.utcnow().isocalendar()[1])
    now = datetime.datetime.now()#опеределение даты и времени

    if (nums % 2) == 0:
        ned = 1

    if (nums % 2) != 0:
        ned = 0

    if ned == 1:
        da = " неделя ЧЁТНАЯ (нижняя)"

    elif ned == 0:
        da = " неделя НЕЧЁТНАЯ (верхняя)"

    answer3 = "Сегодня " + str(now.day)  + mesyac + ", " + str(den_ned) + ", " + da + "\n" + str(now.hour) + ":" + str(now.minute)

    bot.send_message(message.chat.id, answer3, reply_markup = keyboard1)


@bot.message_handler(content_types = ['text'])
def ans1(message):
    if message.text.lower () == "хочу":
        bot. send_message(message.chat.id, 'Тогда тебе сюда - https://mtuci.ru/', reply_markup=keyboard1)

    elif message.text.lower() == "кто нас учит" or message.text.lower() == "имена преподов":
        bot.send_message(message.chat.id, answer1, reply_markup=keyboard1)

    elif message.text.lower() == "ссылки":
        bot.send_message(message.chat.id, answer2, reply_markup=keyboard1)


    elif message.text.lower() == "слава украине" or message.text.lower() == "slava ukraine":
        bot.send_message(message.chat.id, "Героям слава")
    
    elif message.text.lower() == "слава нації" or message.text.lower() == "слава нации":
        bot.send_message(message.chat.id, "Смерть ворогам")


    elif message.text.lower() == "да, я хочу цитату карла маркса":
        bot.send_message(message.chat.id, random.sample(cit_marks, 1), reply_markup = keyboard2)


    elif message.text.lower() == "стакан" or message.text.lower() == "философия" :
        bot.send_message(message.chat.id, ans_marginal, reply_markup = keyboard1)


    elif message.text.lower() == "анекдот":
        bot.send_message(message.chat.id, random.sample(anekdots, 1), reply_markup = keyboard1)


    elif message.text.lower() == "пинг":
        bot.send_message(message.chat.id, "Понг", reply_markup = keyboard1)


    elif message.text.lower() == "а что это на кубе?" or message.text.lower() == "а что это на кубе" or message.text.lower() == "а что на кубе":
        bot.send_message(message.chat.id, "Это база. Based", reply_markup = keyboard1)


    elif message.text.lower() == "союз нерушимый":
        bot.send_message(message.chat.id, "Республик свободных, сплотила навеки Великая Русь", reply_markup = keyboard1)


    elif message.text.lower() == "учиться":
        bot.send_message(message.chat.id, "Как завещал Дедушка Ленин, учиться, учиться, и, ещё раз, учиться", reply_markup = keyboard1)


    elif message.text.lower() == "позови человека":
        bot.send_message(message.chat.id, "Мы работаем над этим", reply_markup = keyboard1)


    else:
        bot.send_message(message.chat.id, answer_else, reply_markup = keyboard2)


bot.polling()