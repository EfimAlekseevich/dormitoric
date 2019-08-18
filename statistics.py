from datetime import date

import db_queries
from constantes import user_parameters


def get_role_stat(connection, role):
    if role == 'user3':
        answer = 'Чтобы получить доступ к статистике вам необходимо заполнить данные о себе.' \
                 ' Сделать это можно в разделе "Обо мне"'
    else:
        users = db_queries.get_users(connection)
        statistics = get_stat(users)
        if role == 'user2':
            answer = f'Количество пользователей: {statistics["users"]}\n' \
                f'Количество подписанных: {statistics["sub"]}\n' \
                f'Для получения полной статистики укажите все данные о себе.'
        elif role == 'user1':
            answer = f'Количество пользователей: {statistics["users"]}\n' \
                f'Количество подписанных: {statistics["sub"]}\n' \
                f'Парни: {statistics["male"]}\n' \
                f'Девушки: {statistics["female"]}\n' \
                f'Количество оскорблений: {statistics["crimes"]}\n' \
                f'Средний курс: {statistics["sum_course"]//statistics["num_course"]}\n' \
                f'Средний этаж: {statistics["sum_floor"]//statistics["num_floor"]}'
        else:
            mid_age = (date.today().year * statistics['num_year'] - statistics['sum_year']) // statistics['num_year']
            answer = f'Количество пользователей: {statistics["users"]}\n' \
                f'Количество подписанных: {statistics["sub"]}\n' \
                f'Парни: {statistics["male"]}\n' \
                f'Девушки: {statistics["female"]}\n' \
                f'Количество оскорблений: {statistics["crimes"]}\n' \
                f'Количество сообщений: {statistics["num_messages"]}\n' \
                f'Средний курс: {statistics["sum_course"]//statistics["num_course"]}\n' \
                f'Средний этаж: {statistics["sum_floor"]//statistics["num_floor"]}\n' \
                f'Средний возраст: {mid_age}'
    return answer


def get_stat(users):
    stat = {'users': len(users),
            'sub': 0,
            'male': 0,
            'female': 0,
            'crimes': 0,
            'num_course': 10**(-6),
            'sum_course': 0,
            'num_floor': 10**(-6),
            'sum_floor': 0,
            'num_year': 10**(-6),
            'sum_year': 0,
            'num_messages': 0
            }
    for user in users:
        user = get_user_dict(user)
        stat['crimes'] += user['crimes']
        stat['num_messages'] += user['num_messages']
        if user['sub']:
            stat['sub'] += 1
        if user['gender']:
            if user['gender'] == 'male':
                stat['male'] += 1
            elif user['gender'] == 'female':
                stat['female'] += 1
        if user['course']:
            stat['num_course'] += 1
            stat['sum_course'] += user['course']
        if user['floor']:
            stat['num_floor'] += 1
            stat['sum_floor'] += user['floor']
        if user['year_birth']:
            stat['num_year'] += 1
            stat['sum_year'] += user['year_birth']

    return stat


def get_user_dict(user):
    user_dict = {}
    for index, parameter in enumerate(user_parameters.keys()):
        print(parameter, ' ', str(user[index]))
        user_dict[parameter] = user[index]

    return user_dict
