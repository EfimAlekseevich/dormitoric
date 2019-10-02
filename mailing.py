from telebot import TeleBot

import db_queries
from constantes import bot_token, database_url
from bot_logging import get_log_line
from statistics import get_user_dict
from settings import Settings


def main():
    bot = TeleBot(bot_token)
    settings = Settings()

    try:
        connection = db_queries.get_connection(database_url, settings)
        print(get_log_line('START', settings))
        message_text = 'Проверяю рассылку сообщений\n, нужны люди ждя поддержания актуальности информации в боте.\n' \
                       '*Хотите поучаствовать* - смело пишите [сюда](t.me/efi_fi).'

        db_users = db_queries.get_users(connection)
        for db_user in db_users:
            user = get_user_dict(db_user)
            print(send_mail(bot, user, message_text, settings))

    except:
        print(get_log_line('ERROR', settings))


def send_mail(bot, user, message_text, settings):
    user_info = f'ID:{user["id"]} username:{user["username"]}'
    appeal = f'Message for *{user["first_name"]} {user["last_name"]}*\n'
    for _ in range(10):
        try:
            bot.send_message(user['id'], appeal+message_text, parse_mode=settings.parse_mode)
            return get_log_line('DELIVERED\n' + user_info, settings)
        except Exception:
            continue
    return get_log_line('ERROR\n' + user_info, settings)


main()
