import telebot
from telebot import types
import sqlite3

TOKEN = '6884858444:AAEZIjKYqN7WVp-5_TUki5Yu7pWmn0cBhrY'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('StudentSearcher.sql')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, univ varchar(1), username varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("МГУ", callback_data='mgu')
    btn2 = types.InlineKeyboardButton("ИТМО", callback_data='itmo')
    markup.row(btn1, btn2)
    btn3 = types.InlineKeyboardButton("МФТИ", callback_data='mfti')
    btn4 = types.InlineKeyboardButton("МИФИ", callback_data='mifi')
    markup.row(btn3, btn4)
    bot.send_message(message.chat.id, "Добро пожаловать в StudentSearcher! \nВыбери интересующий тебе вуз", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_univ(callback):
    global numberUniv

    markup2 = types.InlineKeyboardMarkup()
    btnSt = types.InlineKeyboardButton("Студент", callback_data='st')
    btnSc = types.InlineKeyboardButton("Школьник", callback_data='sc')
    markup2.row(btnSt, btnSc)

    if callback.data == 'mgu':
        numberUniv = 'mgu'
        bot.send_message(callback.message.chat.id, 'Кем вы являетесь?', reply_markup=markup2)
    elif callback.data == 'itmo':
        numberUniv = 'itmo'
        bot.send_message(callback.message.chat.id, 'Кем вы являетесь?', reply_markup=markup2)
    elif callback.data == 'mfti':
        numberUniv = 'mfti'
        bot.send_message(callback.message.chat.id, 'Кем вы являетесь?', reply_markup=markup2)
    elif callback.data == 'mifi':
        numberUniv = 'mifi'
        bot.send_message(callback.message.chat.id, 'Кем вы являетесь?', reply_markup=markup2)

    if callback.data == 'st':
        bot.send_message(callback.message.chat.id, 'введите свой ник в тг в формате @username')
        bot.register_next_step_handler(callback.message, register)
    elif callback.data == 'sc':
        bot.send_message(callback.message.chat.id, 'контакты студентов:\n')

        conn = sqlite3.connect('StudentSearcher.sql')
        cur = conn.cursor()
        cur.execute('SELECT * FROM users')
        users = cur.fetchall()

        info = ''

        for el in users:
            if el[1] == str(numberUniv):
                info += f'Контакт: {el[2]}\n'

        cur.close()
        conn.close()

        if info == '':
            info += 'пока нет контактов'
            
        bot.send_message(callback.message.chat.id, info)

def register(message):
    username = message.text.strip()

    conn = sqlite3.connect('StudentSearcher.sql')
    cur = conn.cursor()
    cur.execute("INSERT INTO users (univ, username) VALUES ('%s', '%s')" % (numberUniv, username))
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, "Спасибо, что оставили данные")

bot.polling(none_stop=True, interval=0)

