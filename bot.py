import telebot
from  telebot.types import Message
from telebot import types
import json

token = "6214808173:AAHmqWl1LL-9ytJ7T5MY9mTnfkvRADIOpv0"
bot = telebot.TeleBot(token)

def load_user_data(data_path):
    try:
        with open(data_path, 'r', encoding='utf8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_user_data(user_data, data_path):
    with open(data_path, 'w+', encoding='utf8') as file:
        json.dump(user_data, file, ensure_ascii=False)

data_path_name = 'users.json'

questions = {
    1 : {"text" : "1) Считаешь ли ты себя грибом?", "true_answer" : 'Да'},
    2 : {"text" : "2) Умеешь двигаться?", "true_answer" : 'Нет'},
    3 : {"text" : "3) У тебя есть шляпа?", "true_answer" : 'Да'},
    4 : {"text" : "4) Любишь сырость?", "true_answer" : 'Да'},
    5 : {"text" : "5) Дружишь с деревьями?", "true_answer" : 'Да'}
}

results = {
    0 : 'Ты не гриб',
    1 : 'Ты не гриб',
    2 : 'Ты полугриб',
    3 : 'Ты полугриб',
    4 : 'Ты гриб',
    5 : 'Ты гриб'
}

markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton("Да")
btn2 = types.KeyboardButton("Нет")
markup1.add(btn1, btn2)

markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton("Да")
btn2 = types.KeyboardButton("Нет")
markup2.add(btn1, btn2)

markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton("Да")
btn2 = types.KeyboardButton("Нет")
markup3.add(btn1, btn2)

markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton("Нет")
btn2 = types.KeyboardButton("Да")
markup4.add(btn1, btn2)

markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton("Да")
btn2 = types.KeyboardButton("Нет")
markup5.add(btn1, btn2)

markups = [markup1, markup2, markup3, markup4, markup5]

@bot.message_handler(commands=['start'])
def start(message: Message):
    user_data = load_user_data(data_path_name)
    bot.send_message(message.from_user.id, 'Привет! Это - бот-анкета "Насколько ты гриб?". Давай начнём!')

    if str(message.from_user.id) in user_data:
        bot.send_message(message.from_user.id, 'Вы уже начали прохождение анкеты. Давайте продолжим:')

        if user_data[str(message.from_user.id)]['result'] == []:
            bot.send_message(message.from_user.id, questions[1]['text'], reply_markup=markup1)
        else:
            question_number = len(user_data[str(message.from_user.id)]['result'])
            bot.send_message(message.from_user.id, questions[question_number + 1]['text'], reply_markup=markups[question_number])

    else:
        user_data[message.from_user.id] = {"name": message.from_user.first_name,
                                           "result": []}
        save_user_data(user_data, data_path_name)
        bot.send_message(message.from_user.id, 'Чтобы начать тестирование, снова напишите /start. Используйте кнопки для ответов')

@bot.message_handler(content_types=['text'])
def handle_media_files(message: Message):
    user_data = load_user_data(data_path_name)
    question_number = len(user_data[str(message.from_user.id)]['result']) + 1

    right_answer = questions[question_number]["true_answer"]
    if message.text == right_answer:
        user_data[str(message.from_user.id)]["result"].append(1)
    else:
        user_data[str(message.from_user.id)]["result"].append(0)

    if question_number < len(questions):
        bot.send_message(str(message.from_user.id), questions[question_number+1]['text'], reply_markup=markups[question_number])
    elif question_number == len(questions):
        result_balls = sum(user_data[str(message.from_user.id)]["result"])
        bot.send_message(message.from_user.id, f"Тест пройден! Ваш результат: {results[result_balls]}")
        user_data[str(message.from_user.id)]["result"].clear()
        if result_balls == 0 or result_balls == 1:
            img = open(r'p1.jpg', 'rb')
            bot.send_photo(message.from_user.id, img)
        elif result_balls == 2 or result_balls == 3:
            img = open(r'p2.jpg', 'rb')
            bot.send_photo(message.from_user.id, img)
        elif result_balls == 4 or result_balls == 5:
            img = open(r'p3.jpg', 'rb')
            bot.send_photo(message.from_user.id, img)

    save_user_data(user_data, data_path_name)

bot.polling()