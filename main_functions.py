from datetime import datetime
from random import choice
from telebot.types import ReplyKeyboardMarkup

import db_queries
import constantes as const
from bot_logging import get_log_text
from statistics import get_role_stat, get_user_dict


def process_message(bot, connection, message, markups, settings):

    answer_text = choice(const.other_answers)
    answer_markup = None

    user_id = str(message.from_user.id)
    user_text = message.text

    crimes = get_crimes(user_text)

    if user_text[1:] in const.commands:
        answer_text = const.commands[user_text[1:]]
        answer_markup = markups['Назад']
    elif user_text in const.usually_answers.keys():
        answer_text = get_answer(user_text)

    if user_text in markups.keys():
        answer_markup = markups[user_text]

    if crimes:
        answer_text = const.bad_answer

    if connection:
        db_user = verify_user(connection, user_id, message)

        if user_text == 'Обо мне':
            answer_markup = get_user_markup(db_user)
            answer_text = 'Для редакирования данных нажмите на соответствующий параметр'
        elif user_text == 'Обо всех':
            answer_text = get_role_stat(connection, db_user['role'])
        elif ': ' in user_text:
            rus_parameter = user_text.split(':')[0]
            answer_text = f'Пожалуйста введите {rus_parameter.lower()}'
            if rus_parameter in markups.keys():
                answer_markup = markups[rus_parameter]
        elif ': ' in db_user['last_message']:
            parameter = get_parameter(db_user['last_message'])
            if parameter and verify_user_parameter(parameter, user_text):
                db_queries.update_parameter(connection, user_id, parameter, user_text)
                answer_text = f'Ваш {db_user["last_message"].split(":")[0].lower()} был успешно сохранён.'
                answer_markup = get_user_markup(get_user_dict(db_queries.get_user(connection, user_id)))

            else:
                answer_text = 'Параметр введён некорректно'

        db_queries.update_user(connection, user_id, user_text, db_user['num_messages']+1)

    bot.send_message(user_id, answer_text, reply_markup=answer_markup, parse_mode=settings.parse_mode)
    print(get_log_text(message, datetime.now(), answer_text, crimes, settings))


def get_answer(user_text):
    answer = const.usually_answers[user_text]
    try:
        with open('answers/' + answer) as f:
            answer = f.read()
    except:
        pass
    return answer


def get_crimes(text):
    text = text.lower()
    crimes = 0
    for word in const.bad_words:
        if word in text:
            crimes += 1

    return crimes


def verify_user(connection, user_id, message):
    user = db_queries.get_user(connection, user_id)
    if not user:
        db_queries.add_user(connection, message)
        user = db_queries.get_user(connection, user_id)

    return get_user_dict(user)


def update_user_role(connection, user_id):
    db_user = get_user_dict(db_queries.get_user(connection, user_id))
    points = count_points(db_user)
    if points > 12:
        db_queries.update_parameter(connection, user_id, 'role', 'user2')
    elif points > 15:
        db_queries.update_parameter(connection, user_id, 'role', 'user2')


def count_points(db_user):
    points = 0
    for parameter, value in db_user.items():
        if value:
            points += 1
        if parameter == 'crimes':
            if value:
                points -= 1
            points -= value // 4

    return points


def get_user_markup(db_user):
    markup = ReplyKeyboardMarkup(True)
    for parameter, name in const.user_parameters.items():
        if name:
            markup.row(f'{name}: {db_user[parameter]}')
    markup.row('Статистика')
    return markup


def get_parameter(text):
    rus_parameter = text.split(':')[0]
    for parameter, r_parameter in const.user_parameters.items():
        if rus_parameter == r_parameter:
            return parameter


def verify_user_parameter(parameter, value):
    if value:
        if parameter == 'first_name' or parameter == 'last_name':
            return True
        elif parameter == 'gender' and (value == 'male' or value == 'female'):
            return True
        elif parameter == 'floor':
            floor = try_to_int(value)
            if 1 < floor < 13:
                return True
        elif parameter == 'room':
            if len(value) < 6:
                return True
        elif parameter == 'course':
            course = try_to_int(value)
            if 0 < course < 5:
                return True
        elif parameter == 'faculty' and value in list_merge(const.skeleton_markups['Факультет']):
            return True
        elif parameter == 'year_birth':
            year = try_to_int(value)
            if 1900 < year < 2010:
                return True
        elif parameter == 'sub' and (value == 'True' or value == 'False'):
            return True


def try_to_int(string):
    try:
        return int(string)
    except:
        return 0


def list_merge(lst_lst):
    full_list = list()
    for lst in lst_lst:
      full_list.extend(lst)
    return full_list
