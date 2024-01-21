import telebot
from  telebot.types import Message
from info import name, age, geo, interests, school, hobby, photo

token = "6214808173:AAHmqWl1LL-9ytJ7T5MY9mTnfkvRADIOpv0"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def get_start(message:Message):
    bot.send_message(message.from_user.id, 'Приветствую!')
    bot.send_message(message.from_user.id, 'Напиши /help, чтобы посмотреть список команд')

@bot.message_handler(commands=['help'])
def help(message:Message):
    bot.send_message(message.from_user.id, 'Этот бот - визитная карточка своего создателя. Вы можете узнать немного информации о нём с помощью следующих команд:')
    bot.send_message(message.from_user.id, 'Имя - /name')
    bot.send_message(message.from_user.id, 'возраст - /age')
    bot.send_message(message.from_user.id, 'город - /geo')
    bot.send_message(message.from_user.id, 'интересы - /interests')
    bot.send_message(message.from_user.id, 'школа - /school')
    bot.send_message(message.from_user.id, 'хобби - /hobby')
    bot.send_message(message.from_user.id, 'внешность - /photo')
    bot.send_message(message.from_user.id, 'Бот также может отвечать на приветствия')

@bot.message_handler(content_types=['text'])
def reply(message:Message):
    if message.text == '/name':
        name(message)
    elif message.text == '/age':
        age(message)
    elif message.text == '/geo':
        geo(message)
    elif message.text == '/interests':
        interests(message)
    elif message.text == '/school':
        school(message)
    elif message.text == '/hobby':
        hobby(message)
    elif message.text == '/photo':
        photo(message)
    elif 'привет' in message.text.lower():
        bot.send_message(message.from_user.id, 'И вам привет')
    else:
        bot.send_message(message.from_user.id, 'Извините, не понял')

bot.polling()