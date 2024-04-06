import telebot
from telebot import types
import sqlite3

TOKEN = '6884858444:AAEZIjKYqN7WVp-5_TUki5Yu7pWmn0cBhrY'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):

#кнопка рестарта
    markupStart = types.ReplyKeyboardMarkup()
    btnStart = types.KeyboardButton('/start')
    markupStart.add(btnStart)
    bot.send_message(message.chat.id, 'Добро пожаловать в StudentSearcher!', reply_markup=markupStart)


#подключение БД
    conn = sqlite3.connect('StudentSearcher.sql')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, univ varchar(1), username varchar(50))')
    conn.commit()
    cur.close()
    conn.close()


#кнопки выбора ВУЗа
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("МГУ", callback_data='mgu')
    btn2 = types.InlineKeyboardButton("ИТМО", callback_data='itmo')
    markup.row(btn1, btn2)
    btn3 = types.InlineKeyboardButton("МФТИ", callback_data='mfti')
    btn4 = types.InlineKeyboardButton("МИФИ", callback_data='mifi')
    markup.row(btn3, btn4)

    bot.send_message(message.chat.id, "Выбери интересующий тебе вуз:", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_univ(callback):

    global numberUniv

#кнопки кем является пользователь
    markupWho = types.InlineKeyboardMarkup()
    btnSt = types.InlineKeyboardButton("Студент", callback_data='st')
    btnSc = types.InlineKeyboardButton("Школьник", callback_data='sc')
    markupWho.row(btnSt, btnSc)


#кнопки специальностей МГУ
    markupMgu = types.InlineKeyboardMarkup()
    btnMguInfo = types.InlineKeyboardButton("Информация", url='https://msu.ru')
    markupMgu.row(btnMguInfo)
    btnMgu_1 = types.InlineKeyboardButton("Прикладная математика и информатика", callback_data='mgu1')
    btnMgu_2 = types.InlineKeyboardButton("Фундаментальная информатика и информационные технологии", callback_data='mgu2')
    markupMgu.row(btnMgu_1, btnMgu_2)


#кнопки специальностей ИТМО
    markupItmo = types.InlineKeyboardMarkup()
    btnItmoInfo = types.InlineKeyboardButton("Информация", url='https://itmo.ru')
    markupItmo.row(btnItmoInfo)
    btnItmo_1 = types.InlineKeyboardButton("Программирование и искусственный интелект", callback_data='itmo1')
    btnItmo_2 = types.InlineKeyboardButton("Нейротехнологии и программирование", callback_data='itmo2')
    markupItmo.row(btnItmo_1, btnItmo_2)
    btnItmo_3 = types.InlineKeyboardButton("Технологии разработки компьютерных игр", callback_data='itmo3')
    btnItmo_4 = types.InlineKeyboardButton("Мобильные и сетевые технологии", callback_data='itmo4')
    markupItmo.row(btnItmo_3, btnItmo_4)


#кнопки специальностей МФТИ
    markupMfti = types.InlineKeyboardMarkup()
    btnMftiInfo = types.InlineKeyboardButton("Информация", url='https://mipt.ru')
    markupMfti.row(btnMftiInfo)
    btnMfti_1 = types.InlineKeyboardButton("Биотехнология", callback_data='mfti1')
    btnMfti_2 = types.InlineKeyboardButton("Прикладная математика и информатика", callback_data='mfti2')
    markupMfti.row(btnMfti_1, btnMfti_2)


#кнопки специальностей МИФИ
    markupMifi = types.InlineKeyboardMarkup()
    btnMifiInfo = types.InlineKeyboardButton("Информация", url='https://mephi.ru')
    markupMifi.row(btnMifiInfo)
    btnMifi_1 = types.InlineKeyboardButton("Прикладная математика и информатика", callback_data='mifi1')
    btnMifi_2 = types.InlineKeyboardButton("Математическое и программное обеспечение киберфизических систем", callback_data='mifi2')
    markupMifi.row(btnMifi_1, btnMifi_2)


 #проверка ВУЗа
    if callback.data == 'mgu':
        numberUniv = 'mgu'
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text='Теперь выбери направление или узнай информацию:', reply_markup=markupMgu)
    elif callback.data == 'itmo':
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text='Теперь выбери направление или узнай информацию:', reply_markup=markupItmo)
        numberUniv = 'itmo'
    elif callback.data == 'mfti':
        numberUniv = 'mfti'
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text='Теперь выбери направление или узнай информацию:', reply_markup=markupMfti)
    elif callback.data == 'mifi':
        numberUniv = 'mifi'
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text='Теперь выбери направление или узнай информацию:', reply_markup=markupMifi)

#проверка направления
    if callback.data == 'mgu1':
        numberUniv += '.1'
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text='Кем вы являетесь?', reply_markup=markupWho)
    elif callback.data == 'mgu2':
        numberUniv += '.2'
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text='Кем вы являетесь?', reply_markup=markupWho)
    elif callback.data == 'itmo1':
        numberUniv += '.1'
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text='Кем вы являетесь?', reply_markup=markupWho)
    elif callback.data == 'itmo2':
        numberUniv += '.2'
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text='Кем вы являетесь?', reply_markup=markupWho)
    elif callback.data == 'itmo3':
        numberUniv += '.3'
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text='Кем вы являетесь?', reply_markup=markupWho)
    elif callback.data == 'itmo4':
        numberUniv += '.4'
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text='Кем вы являетесь?', reply_markup=markupWho)
    elif callback.data == 'mfti1':
        numberUniv += '.1'
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text='Кем вы являетесь?', reply_markup=markupWho)
    elif callback.data == 'mfti2':
        numberUniv += '.2'
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text='Кем вы являетесь?', reply_markup=markupWho)
    elif callback.data == 'mifi1':
        numberUniv += '.1'
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text='Кем вы являетесь?', reply_markup=markupWho)
    elif callback.data == 'mifi2':
        numberUniv += '.2'
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text='Кем вы являетесь?', reply_markup=markupWho)


#проверка кем является пользователь
    if callback.data == 'st':
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text='введите свой ник в тг в формате @username')
        bot.register_next_step_handler(callback.message, register)
    elif callback.data == 'sc':
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text='контакты студентов:\n')


#вывод данных из БД
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


#внос данных в БД
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
