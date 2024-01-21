import telebot
from telebot.types import Message

token = "6214808173:AAHmqWl1LL-9ytJ7T5MY9mTnfkvRADIOpv0"

bot = telebot.TeleBot(token)

def name(message:Message):
    bot.send_message(message.from_user.id, 'Нияз Хакимов')

def age(message:Message):
    bot.send_message(message.from_user.id, '14 лет')

def geo(message:Message):
    bot.send_message(message.from_user.id, 'Казань')

def interests(message:Message):
    bot.send_message(message.from_user.id, 'Программирование, биология, обществознание, история')

def school(message:Message):
    bot.send_message(message.from_user.id, 'Лицей №2')

def hobby(message:Message):
    bot.send_message(message.from_user.id, 'Настольный теннис')

def photo(message:Message):
    img = open(r'penguin.jpg', 'rb')
    bot.send_photo(message.from_user.id, img)
    bot.send_message(message.from_user.id, 'Да, именно так он выглядит')
