import flask, aiogram, requests, telebot, pywhatkit, pyautogui, requests, bs4
import function
from telebot import types

'''1) Генерация пароля по указанным правилам. Минимальное количество чисел 1, 
минимальное количество специальных символов 1 из !@#$%^&*, 
минимальный размер пароля 8 символов. Можешь сам усложнять правила

2) Напоминание через указанное время. 
Пример, напомни мне сделать гимнастику на глаза через 10 минут или 
напомни мне выйти на встречу в 18:00

3) Генерация рандомного UUID хэша

4) Валидация введенного ИИН 
(в интернете найдешь формулу как правильно расшифровывать и проверять)

5) Выдача рандомного мақал-мәтел из справочника 
(справочник сам подготовишь, можно хранить их в Базе данных)
'''

Client_ID = "cfJB3CXDTpKYpboQA0m2Sg"
Client_Secret = "i0bDl3zdodBO3OcIhRCbipqPbOchiMzH" 
token = '7786204973:AAHNgj2-i3EynjdcPFeIMhH7OJ4RE0I1qqc'
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Привет! Нажми на кнопку ниже:",
        reply_markup=keyboard
    )

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton("Запустить Zoom")
button2 = types.KeyboardButton("Напоминание")
button3 = types.KeyboardButton("Погода")
button4 = types.KeyboardButton("Генерация пароля")
keyboard.add(button1, button2, button3, button4)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Привет! Нажми на кнопку ниже:",
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Запустить Zoom":
        bot.send_message(message.chat.id, "Привет-привет!")
        
    elif message.text == "Напоминание":
        bot.send_message(message.chat.id, 'Введите время планируемой стречи')
        #Пользователь пишет время
        #Бот обрабатывает 
        #Время передается в функицю alarm
        #Телеграм выдает уведомление о введенном пользователем времени
        
    elif message.text == "Погода": 
        bot.send_message(message.chat.id, function.get_weather())
        
    elif message.text == "Генерация пароля":
        bot.send_message(message.chat.id, function.password_generate())
        
    else:
        bot.send_message(message.chat.id, "Не понимаю, попробуй нажать кнопку.")

bot.polling()