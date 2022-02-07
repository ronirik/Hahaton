# import telebot
# from telebot import types

# # from MyTok3 import token

# name = ''
# surname = ''
# age = 0

# bot = telebot.TeleBot('5057373309:AAFJQuJwMYW6tRoJlWc6AA4cKUOcJOQuJBE')

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
# 	bot.reply_to(message, "привет ")

# @bot.message_handler(commands=['info'])
# def send_welcome(message):
# 	bot.reply_to(message, "  /info - получить инфо по камандам \n /start - привествие \n /help - информация о тебе \n /reg - регистрация ")

# @bot.message_handler(commands=['help'])
# def send_welcome(message):
# 	bot.reply_to(message, f"ой не ной,\n{message.from_user.first_name} {message.from_user.username}")

# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
#     if message.text == 'Привет':
#         bot.reply_to(message, 'Привет создатель бота!')
#     elif message.text == 'hi':
#         bot.reply_to(message, 'Hi again! The bot creator!')
#     elif message.text == '/reg':
#         bot.send_message(message.from_user.id, "Привет! Давай познакомимся! Как тебя зовут?")
#         bot.register_next_step_handler(message, reg_name)

# 	#bot.reply_to(message, message.text)

# def reg_name(message):
#     global name
#     name = message.text
#     bot.send_message(message.from_user.id, "Какая у вас фамилия?")
#     bot.register_next_step_handler(message, reg_surname)

# def reg_surname(message):
#     global surname
#     surname = message.text
#     bot.send_message(message.from_user.id, "Сколько вам лет?")
#     bot.register_next_step_handler(message, reg_age)

# def reg_age(message):
#     global age
#     #age = message.text
#     while age == 0:
#         try:
#             age = int(message.text)
#         except Exception:
#             bot.send_message(message.from_user.id, "Вводите цифрами!")
    
#     keyboard = types.InlineKeyboardMarkup()
#     key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
#     keyboard.add(key_yes)
#     key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
#     keyboard.add(key_no)
#     question = 'Тебе ' + str(age) + ' лет? И тебя зовут: ' + name + ' ' + surname + '?'
#     bot.send_message(message.from_user.id, text = question, reply_markup=keyboard)

# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
#     if call.data == "yes":
#         bot.send_message(call.message.chat.id, "Приятно познакомиться! Теперь запишу в БД!")
#     elif call.data == "no":
#         bot.send_message(call.message.chat.id, "Попробуем еще раз!")
#         bot.send_message(call.message.chat.id, "Привет! Давай познакомимся! Как тебя зовут?")
#         bot.register_next_step_handler(call.message, reg_name)

    


# bot.polling()


#------------------------------------------------------------------------------------------------------------------------


# import telebot
# import requests
# from bs4 import BeautifulSoup as BS

# bot = telebot.TeleBot('5057373309:AAFJQuJwMYW6tRoJlWc6AA4cKUOcJOQuJBE')
# db = {}
# kaktus_info = dict()
# url = 'https://kaktus.media/?lable=8&date=2022-01-24&order=time'

# def get_html(url):
#     return requests.get(url).text

# def get_data(html):
#     page_html = BS(html, "lxml")
#     news_info = page_html.find_all('div', class_="Tag--article")
#     for news in news_info:
#         link = news.find('a', class_="ArticleItem--image").get('href')
#         title = news.find('a', class_="ArticleItem--name").text
#         image = news.find('img').get('src')
#         db.update({link:[title, image]})

# def main():
#     html = get_html(url)
#     get_data(html)
#     return db
# main()


# @bot.message_handler(commands=['start'])
# def start(message):
#     global kaktus_info
#     kaktus_info = main()
#     chat_id = message.chat.id
#     i = 1
#     for news in list(kaktus_info.values())[0:20]:
#         bot.send_message(chat_id, f"{i} {news[0]}")
#         i += 1
#     msg = bot.send_message(chat_id, "Номер желаемой новости:")
#     bot.register_next_step_handler(msg, get_description)

# def get_description(message):
#     chat_id = message.chat.id
#     ind = int(message.text) - 1
#     bot.send_message(chat_id, list(kaktus_info.values())[ind])
#     msg = bot.send_message(chat_id, "Номер желаемой иллюстрации:")
#     bot.register_next_step_handler(msg, get_image)

# def get_image(message):
#     chat_id = message.chat.id
#     ind = int(message.text) - 1
#     bot.send_message(chat_id, list(kaktus_info.values())[ind][1])
#     print(kaktus_info.values())

# @bot.message_handler(commands=['quit'])
# def start(message):
#     bot.send_message(message.chat.id, "До свидания!")

# bot.polling()

#--------------------------------------------------------------------------------------------------------------------------------

import requests
from bs4 import BeautifulSoup as BS
import telebot
from telebot import types

bot = telebot.TeleBot('5057373309:AAFJQuJwMYW6tRoJlWc6AA4cKUOcJOQuJBE')
db = {}
kaktus_info = dict()
url = 'https://kaktus.media/?lable=8&date=2022-01-24&order=time'

def get_html(url):
    return requests.get(url).text

def get_data(html):
    page_html = BS(html, "lxml")
    news_info = page_html.find_all('div', class_="Tag--article")
    for news in news_info:
        link = news.find('a', class_="ArticleItem--image").get('href')
        title = news.find('a', class_="ArticleItem--name").text
        image = news.find('img').get('src')
        db.update({link:[title, image]})

def main():
    html = get_html(url)
    get_data(html)
    return db
main()

inline_keyboard = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton('Доход', callback_data='income')
inline_keyboard.add(btn1)

    
@bot.message_handler(commands=['start'])
def start(message):
    global kaktus_info
    kaktus_info = main()
    chat_id = message.chat.id
    i = 1
    for news in list(kaktus_info.values())[0:20]:
        bot.send_message(chat_id, f"{i} {news[0]}")
        i += 1
    msg = bot.send_message(chat_id, "Номер желаемой новости:", reply_markup=inline_keyboard)
    bot.register_next_step_handler(msg, get_description)
    

def get_description(message):
    chat_id = message.chat.id
    ind = int(message.text) - 1
    bot.send_message(chat_id, list(kaktus_info.values())[ind])
    msg = bot.send_message(chat_id, "Номер желаемой иллюстрации:")
    bot.register_next_step_handler(msg, get_image)

def get_image(message):
    chat_id = message.chat.id
    ind = int(message.text) - 1
    bot.send_message(chat_id, list(kaktus_info.values())[ind][1])
    print(kaktus_info.values())

@bot.message_handler(commands=['quit'])
def start(message):
    bot.send_message(message.chat.id, "До свидания!")

bot.polling()