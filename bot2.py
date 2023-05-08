import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Создание экземпляра бота с токеном
bot = telebot.TeleBot("6271726253:AAFJrshSjjseDqpLGnq9KrIXSv_oE3_KTgc")

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # Создание клавиатуры для выбора критерия
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_area = KeyboardButton(text="Regions")
    button_price = KeyboardButton(text="Price")
    keyboard.add(button_area, button_price)
    
    # Отправка приветственного сообщения с выбором критерия
    bot.send_message(message.chat.id, "Hello! By what criteria do you want to choose a tour?", reply_markup=keyboard)

# Обработчик выбора критерия "Цены"
@bot.message_handler(func=lambda message: message.text == "Price")
def choose_price(message):
    # Создание клавиатуры для выбора цены
    keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True)
    button_25 = KeyboardButton(text="25-50$")
    button_50 = KeyboardButton(text="50-100$")
    button_100 = KeyboardButton(text="100-200$")
    keyboard1.add( button_25,button_50,button_100 )
# Отправка сообщения с выбором цены
    bot.send_message(message.chat.id, "Choose price:", reply_markup=keyboard1)
#25-50$
@bot.message_handler(func=lambda message: message.text == "25-50$")
def choose_chui(message):
    bot.send_message(message.chat.id, "Ala-Archa(from 8a.m to 6p.m) price: 25$ ; Rux-Ordo (1 day) price: 35$  ; Jalal-Abad(2 days) price: 45$" )
# 50-100$
@bot.message_handler(func=lambda message: message.text == "50-100$")
def choose_chui(message):
    bot.send_message(message.chat.id, "Talas(3 days) price: 55$ ;  Sulaiman-Too(2 days) price: 65$" )
# 100-200$
@bot.message_handler(func=lambda message: message.text == "100-200$")
def choose_chui(message):
    bot.send_message(message.chat.id, "Son-Kol(2 days) price: 105$" )
# Обработчик выбора критерия "Области"
@bot.message_handler(func=lambda message: message.text == "Regions")
def choose_area(message):
    # Создание клавиатуры для выбора области
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_chui = KeyboardButton(text="Chui")
    button_naryn = KeyboardButton(text="Naryn")
    button_talas = KeyboardButton(text="Talas")
    button_issyk_kul = KeyboardButton(text="Isyk-Kul")
    button_osh = KeyboardButton(text="Osh")
    button_jalal_abad = KeyboardButton(text="Jalal-Abad")
    button_batken = KeyboardButton(text="Batken")
    keyboard.add(button_chui, button_naryn, button_talas, button_issyk_kul, button_osh, button_jalal_abad, button_batken)
    
    # Отправка сообщения с выбором области
    bot.send_message(message.chat.id, "Choose region:", reply_markup=keyboard)

# Обработчик выбора области "Чуй"
@bot.message_handler(func=lambda message: message.text == "Chui")
def choose_chui(message):
    # Отправка сообщения с информацией о туре
    bot.send_message(message.chat.id, "Ala-Archa(from 8a.m to 6p.m) price: 25$")

# Обработчик выбора области "Нарын"
@bot.message_handler(func=lambda message: message.text == "Naryn")
def choose_naryn(message):
    # Отправка сообщения с информацией о туре
    bot.send_message(message.chat.id, "Son-Kol(2 days) price: 105$")

# Обработчик выбора области "Талас"
@bot.message_handler(func=lambda message: message.text == "Talas")
def choose_talas(message):
    # Отправка сообщения с информацией о туре
    bot.send_message(message.chat.id, "Talas(3 days) price: 55$")

# Обработчик выбора области "Исык-Кул"
@bot.message_handler(func=lambda message: message.text == "Isyk-Kul")
def choose_talas(message):
    # Отправка сообщения с информацией о туре
    bot.send_message(message.chat.id, "Rux-Ordo (1 day) price: 35$")

# Обработчик выбора области "Ош"
@bot.message_handler(func=lambda message: message.text == "Osh")
def choose_talas(message):
    # Отправка сообщения с информацией о туре
    bot.send_message(message.chat.id, "Sulaiman-Too(2 days) price: 65$")

# Обработчик выбора области "Джалал-Абад"
@bot.message_handler(func=lambda message: message.text == "Jalal-Abad")
def choose_talas(message):
    # Отправка сообщения с информацией о туре
    bot.send_message(message.chat.id, "Jalal-Abad(2 days) price: 45$")

# Обработчик выбора области "Баткен"
@bot.message_handler(func=lambda message: message.text == "Batken")
def choose_talas(message):
    # Отправка сообщения с информацией о туре
    bot.send_message(message.chat.id, "Batken(2 days) Price: 77$")

bot.polling(non_stop=True, interval=0)
