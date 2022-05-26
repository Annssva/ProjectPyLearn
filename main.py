import random

import telebot  # Импорт библиотеки для работы с телеграм ботом
from telebot import types  # Импортирование из библиотеки объекта для создания кнопок

import main
from config import token
import sql_requests  # Файл с нужными sql запросами к бд
import theory

bot = telebot.TeleBot(token)  # Присваивание токена переменной bot, с которой будем взаимодействовать

answer = 0  # Переменная - счетчик попыток ответов на тесты


# Вывод стартового сообщения
@bot.message_handler(commands=['start'])
def start(message):
    if not sql_requests.check_db(message.from_user.id):  # Если пользователя нет в бд, добавляет его туда
        sql_requests.create_user_db(message.from_user.id)
    sti = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)  # присылает приветсвенный стикер
    mess = f'Привет, <ins><b>{message.from_user.first_name}</b></ins>!\n' \
           f'Я Бот, созданный, чтобы помочь тебе изучить основы Python! 🐍'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    menu(message)  # метод, который показывает меню


# Метод для улавливания инлайновых кнопок
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'next_btn':  # Улавливает нажатие кнопки "Дальше"
            send_lesson(call)
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        elif call.data == 'test_btn':  # Улавливает нажатие кнопки "Перейти к тесту"
            # prog_stat - кол-во пройденных уроков, далее с поиощью запроса мы получаем его и отсылаем нужный тест
            prog_stat = sql_requests.get_progress(call.from_user.id)["progress"]
            if prog_stat == 0:
                send_test(call, theory.test_1_v1, theory.test_1_v2, theory.test_1_v3, theory.test_1)
            elif prog_stat == 1:
                send_test(call, theory.test_2_v1, theory.test_2_v2, theory.test_2_v3, theory.test_2)
            elif prog_stat == 1.5:
                send_test(call, theory.test_2_2_v1, theory.test_2_2_v2, theory.test_2_2_v3, theory.test_2_2)
            elif prog_stat == 2:
                send_test(call, theory.test_3_v1, theory.test_3_v2, theory.test_3_v3, theory.test_3)
            elif prog_stat == 3:
                send_test(call, theory.test_4_v1, theory.test_4_v2, theory.test_4_v3, theory.test_4)
            elif prog_stat == 4:
                send_test(call, theory.test_5_v1, theory.test_5_v2, theory.test_5_v3, theory.test_5)
            elif prog_stat == 5:
                send_test(call, theory.test_6_v1, theory.test_6_v2, theory.test_6_v3, theory.test_6)
            elif prog_stat == 5.5:
                send_test(call, theory.test_6_2_v1, theory.test_6_2_v2, theory.test_6_2_v3, theory.test_6_2)
            elif prog_stat == 6:
                send_test(call, theory.test_7_v1, theory.test_7_v2, theory.test_7_v3, theory.test_7)
            elif prog_stat == 7:
                send_test(call, theory.test_8_v1, theory.test_8_v2, theory.test_8_v3, theory.test_8)

        elif call.data == 'var_false':  # улавливает нажатие неверного ответа в тесте и вызывает метод для его обработки
            send_false(call)

        elif call.data == 'var_right':  # улавливает нажатие верного ответа в тесте и вызывает метод для его обработки
            send_right(call)
        # Далее улавливаются нажатие кнопок для просмотра соот-ей теории, но теория показывается только для уроков,
        # которые пользователь уже прошел, поэтому делается проверка прогресса
        elif call.data == 'teor_1':
            prog_stat = sql_requests.get_progress(call.from_user.id)["progress"]
            if prog_stat >= 1:
                send_theory(call, theory.lesson_1, theory.theory_1_mess)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Модуль 1:", reply_markup=None, parse_mode='html')
            else:
                bot.answer_callback_query(callback_query_id=call.id,
                                          text='Пока урок не пройден, теория к нему закрыта❌')
        elif call.data == 'teor_2':
            prog_stat = sql_requests.get_progress(call.from_user.id)["progress"]
            if prog_stat >= 2:
                send_theory(call, theory.lesson_2, theory.theory_2_mess)
                send_theory(call, theory.lesson_2, theory.theory_2_2_mess)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Модуль 1:", reply_markup=None, parse_mode='html')
            else:
                bot.answer_callback_query(callback_query_id=call.id,
                                          text='Пока урок не пройден, теория к нему закрыта❌')

        elif call.data == 'teor_3':
            prog_stat = sql_requests.get_progress(call.from_user.id)["progress"]
            if prog_stat >= 3:
                send_theory(call, theory.lesson_3, theory.theory_3_mess)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Модуль 1:", reply_markup=None, parse_mode='html')
            else:
                bot.answer_callback_query(callback_query_id=call.id,
                                          text='Пока урок не пройден, теория к нему закрыта❌')
        elif call.data == 'teor_4':
            prog_stat = sql_requests.get_progress(call.from_user.id)["progress"]
            if prog_stat >= 4:
                send_theory(call, theory.lesson_4, theory.theory_4_mess)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Модуль 1:", reply_markup=None, parse_mode='html')
            else:
                bot.answer_callback_query(callback_query_id=call.id,
                                          text='Пока урок не пройден, теория к нему закрыта❌')
        elif call.data == 'teor_5':
            prog_stat = sql_requests.get_progress(call.from_user.id)["progress"]
            if prog_stat >= 5:
                send_theory(call, theory.lesson_5, theory.theory_5_mess)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Модуль 1:", reply_markup=None, parse_mode='html')
            else:
                bot.answer_callback_query(callback_query_id=call.id,
                                          text='Пока урок не пройден, теория к нему закрыта❌')
        elif call.data == 'teor_6':
            prog_stat = sql_requests.get_progress(call.from_user.id)["progress"]
            if prog_stat >= 6:
                send_theory(call, theory.lesson_6, theory.theory_6_mess)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Модуль 1:", reply_markup=None, parse_mode='html')
            else:
                bot.answer_callback_query(callback_query_id=call.id,
                                          text='Пока урок не пройден, теория к нему закрыта❌')
        elif call.data == 'teor_7':
            prog_stat = sql_requests.get_progress(call.from_user.id)["progress"]
            if prog_stat >= 7:
                send_theory(call, theory.lesson_7, theory.theory_7_mess)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Модуль 1:", reply_markup=None, parse_mode='html')
            else:
                bot.answer_callback_query(callback_query_id=call.id,
                                          text='Пока урок не пройден, теория к нему закрыта❌')
        elif call.data == 'teor_8':
            prog_stat = sql_requests.get_progress(call.from_user.id)["progress"]
            if prog_stat >= 8:
                send_theory(call, theory.lesson_8, theory.theory_8_mess)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Модуль 1:", reply_markup=None, parse_mode='html')
            else:
                bot.answer_callback_query(callback_query_id=call.id,
                                          text='Пока урок не пройден, теория к нему закрыта❌')

        elif call.data == 'to_theory':  # Улавливает кнопку, чтобы вернутся от теории к меню выбора теорий
            theorys(call, call.message)


# Вывод урока
def send_lesson(call):
    # Для вывода следующего урока делается проверка прогресса
    prog_stat = sql_requests.get_progress(call.from_user.id)["progress"]
    markup_to_test = types.InlineKeyboardMarkup(row_width=1)
    btn_to_test = types.InlineKeyboardButton("Приступить к тесту ⬇", callback_data='test_btn')
    markup_to_test.add(btn_to_test)
    if prog_stat == 0:
        bot.send_message(call.message.chat.id, theory.module_1, parse_mode='html')
        bot.send_message(call.message.chat.id, theory.lesson_1, parse_mode='html')
        bot.send_message(call.message.chat.id, theory.theory_1_mess, parse_mode='html', reply_markup=markup_to_test)
    elif prog_stat == 1:
        bot.send_message(call.message.chat.id, theory.lesson_2, parse_mode='html')
        bot.send_message(call.message.chat.id, theory.theory_2_mess, parse_mode='html', reply_markup=markup_to_test)
    elif prog_stat == 2:
        bot.send_message(call.message.chat.id, theory.lesson_2, parse_mode='html')
        bot.send_message(call.message.chat.id, theory.theory_2_2_mess, parse_mode='html', reply_markup=markup_to_test)
    elif prog_stat == 3:
        bot.send_message(call.message.chat.id, theory.lesson_3, parse_mode='html')
        bot.send_message(call.message.chat.id, theory.theory_3_mess, parse_mode='html', reply_markup=markup_to_test)
    elif prog_stat == 4:
        bot.send_message(call.message.chat.id, theory.lesson_4, parse_mode='html')
        bot.send_message(call.message.chat.id, theory.theory_4_mess, parse_mode='html', reply_markup=markup_to_test)
    elif prog_stat == 5:
        bot.send_message(call.message.chat.id, theory.lesson_5, parse_mode='html')
        bot.send_message(call.message.chat.id, theory.theory_5_mess, parse_mode='html', reply_markup=markup_to_test)
    elif prog_stat == 6:
        bot.send_message(call.message.chat.id, theory.lesson_6, parse_mode='html')
        bot.send_message(call.message.chat.id, theory.theory_6_mess, parse_mode='html', reply_markup=markup_to_test)
    elif prog_stat == 7:
        bot.send_message(call.message.chat.id, theory.lesson_6, parse_mode='html')
        bot.send_message(call.message.chat.id, theory.theory_6_2_mess, parse_mode='html', reply_markup=markup_to_test)
    elif prog_stat == 8:
        bot.send_message(call.message.chat.id, theory.lesson_7, parse_mode='html')
        bot.send_message(call.message.chat.id, theory.theory_7_mess, parse_mode='html', reply_markup=markup_to_test)
    elif prog_stat == 9:
        bot.send_message(call.message.chat.id, theory.lesson_8, parse_mode='html')
        bot.send_message(call.message.chat.id, theory.theory_8_mess, parse_mode='html', reply_markup=markup_to_test)


# Вывод теста
def send_test(call, var_1, var_2, var_3r, test):
    bot.send_message(call.message.chat.id,
                     text='Выполни тест правильно за 2 попытки, чтобы перейти к следуещему уроку',
                     reply_markup=None)

    markup_test = types.InlineKeyboardMarkup(row_width=3)
    # 2 кнопки с неверным ответом и 1 с верным
    btn_var_1 = types.InlineKeyboardButton(var_1, callback_data='var_false')
    btn_var_2 = types.InlineKeyboardButton(var_2, callback_data='var_false')
    btn_var_3r = types.InlineKeyboardButton(var_3r, callback_data='var_right')
    # Генерируется рандомное расположение кнопки с верным ответом
    num = random.randint(1, 3)
    if num == 1:
        markup_test.add(btn_var_1, btn_var_2, btn_var_3r)
    elif num == 2:
        markup_test.add(btn_var_1, btn_var_3r, btn_var_2)
    elif num == 3:
        markup_test.add(btn_var_3r, btn_var_1, btn_var_2)
    bot.send_message(call.message.chat.id, text=test, parse_mode='html', reply_markup=markup_test)
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


# Обрабатывет верный ответ на тест
def send_right(call):
    bot.send_message(call.message.chat.id, text='✅Верно!✅', reply_markup=None)
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    # Добавление 2х баллов за верный ответ
    sql_requests.add_points(call.from_user.id, 2)
    # Тк 2й и 6й урок поделены на 2 части, мы сверяем прогресс и в случае, если пользователь прошел 1й тест 2го или 6го
    # урока, то ему начисляется 0.5 "прогресса", в др случаях по 1
    prog_stat = sql_requests.get_progress(call.from_user.id)["progress"]
    if prog_stat == 1 or prog_stat == 5:
        sql_requests.add_progress(call.from_user.id, 0.5)
    else:
        sql_requests.add_progress(call.from_user.id, 1)

    markup_next = types.InlineKeyboardMarkup(row_width=1)
    btn_next = types.InlineKeyboardButton("Приступить к уроку ⬇", callback_data='next_btn')
    markup_next.add(btn_next)
    bot.send_message(call.message.chat.id, "Приступить к следующему уроку?", reply_markup=markup_next,
                     parse_mode='html')


# Обрабатывет неверный ответ на тест
def send_false(call):
    # Число попыток сохраняется в answer, если пользоваетль потратил свот попытки, то бот высылает урок повторно, чтобы
    # пользователь смог повторить теорию и пройти тест еще раз
    if main.answer <= 0:
        main.answer = main.answer + 1
        bot.answer_callback_query(callback_query_id=call.id, text='❌Неверно!❌')
    elif main.answer >= 1:
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, text='❌Тест провален: слишком много неверных попыток, прочитай теорию '
                                                    'еще раз и попробную снова.',
                         reply_markup=None)
        main.answer = 0
        send_lesson(call)


# Вывод начального сообщения обучения
def learning(message):
    to_menu(message, theory.start_mess1)

    markup_next = types.InlineKeyboardMarkup(row_width=1)
    btn_next = types.InlineKeyboardButton("Приступить к уроку ⬇", callback_data='next_btn')
    markup_next.add(btn_next)
    bot.send_message(message.chat.id, theory.lesson_0, reply_markup=markup_next, parse_mode='html')


# Вывод теории
def send_theory(call, name, theory_text):
    bot.send_message(call.message.chat.id, text=name, parse_mode='html')
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn_back = types.InlineKeyboardButton("Назад", callback_data='to_theory')
    markup.add(btn_back)
    bot.send_message(call.message.chat.id, text=theory_text, parse_mode='html', reply_markup=markup)


# Вывод меню теории
def theorys(message, message1):
    # Опять же проверяется значение "прогресса", чтобы открыть пользователю только ту теорию, которую он прошел
    prog = sql_requests.get_progress(message.from_user.id)["progress"]
    close1 = '🔒'
    close2 = '🔒'
    close3 = '🔒'
    close4 = '🔒'
    close5 = '🔒'
    close6 = '🔒'
    close7 = '🔒'
    close8 = '🔒'

    if prog >= 1:
        close1 = '✅'
    if prog >= 2:
        close2 = '✅'
    if prog >= 3:
        close3 = '✅'
    if prog >= 4:
        close4 = '✅'
    if prog >= 5:
        close5 = '✅'
    if prog >= 6:
        close6 = '✅'
    if prog >= 7:
        close7 = '✅'
    if prog >= 8:
        close8 = '✅'

    theor_mess = "📖Теория\n" \
                 "(Чтобы открыть всю теорию, пройди все уроки)."
    to_menu(message1, theor_mess)
    markup = types.InlineKeyboardMarkup(row_width=1)

    btn_teor_1 = types.InlineKeyboardButton("Урок 1: Введение. О Python." + close1, callback_data='teor_1')
    btn_teor_2 = types.InlineKeyboardButton("Урок 2: Hello world." + close2, callback_data='teor_2')
    btn_teor_3 = types.InlineKeyboardButton("Урок 3: Простые операции." + close3, callback_data='teor_3')
    btn_teor_4 = types.InlineKeyboardButton("Урок 4: Типы данных." + close4, callback_data='teor_4')
    btn_teor_5 = types.InlineKeyboardButton("Урок 5: Вещественные числа." + close5, callback_data='teor_5')
    btn_teor_6 = types.InlineKeyboardButton("Урок 6: Возведение в степень." + close6, callback_data='teor_6')
    btn_teor_7 = types.InlineKeyboardButton("Урок 7: Частное от деления." + close7, callback_data='teor_7')
    btn_teor_8 = types.InlineKeyboardButton("Урок 8: Остаток" + close8, callback_data='teor_8')
    markup.add(btn_teor_1, btn_teor_2, btn_teor_3, btn_teor_4, btn_teor_5, btn_teor_6, btn_teor_7, btn_teor_8)
    bot.send_message(message1.chat.id, text="Модуль 1:", parse_mode='html', reply_markup=markup)


# Вывод информации из профиля
def profile(message):
    # Выводится информация о пользователе с помощью запросов к бд
    points = sql_requests.get_point(message.from_user.id)
    progress = sql_requests.get_progress(message.from_user.id)
    bot.send_message(message.chat.id, f'👤Профиль <ins><b>{message.from_user.first_name}</b></ins>:\n'
                                      f'⚡ Баллы: {points["point"]}\n'
                                      f'🌟Уроков пройдено: {progress["progress"]} из 8 уроков',
                     parse_mode='html')


# Вывод меню
def menu(message):
    menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                            row_width=1)  # Создание кнопок в меню (размер кнопок, и кол-во в ряду):
    btn_learn = types.KeyboardButton('📚Обучение📚')
    btn_profile = types.KeyboardButton('👤Профиль👤')
    btn_theory = types.KeyboardButton('📖Теория📖')
    menu_markup.add(btn_learn, btn_profile, btn_theory)
    bot.send_message(message.chat.id, "⚪️<ins><b>Меню:</b></ins>⚪️", reply_markup=menu_markup, parse_mode='html')


# Кнопка "Вернутся в меню"
def to_menu(message, mess):
    to_menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_to_menu = types.KeyboardButton('Вернуться в меню')
    to_menu_markup.add(btn_to_menu)
    bot.send_message(message.chat.id, mess, reply_markup=to_menu_markup, parse_mode='html')


# Ловит кнопки меню и вызывает соот-ий метод
@bot.message_handler()
def call_menu(message):
    if message.text == '📚Обучение📚':
        learning(message)
    elif message.text == '👤Профиль👤':
        profile(message)
    elif message.text == 'Вернуться в меню':
        menu(message)
    elif message.text == '📖Теория📖':
        theorys(message, message)


bot.polling(none_stop=True)
