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
        message_text = 'Доброе утро,\n' \
                       'по причине аварии (неизвестной) души временно не работают,\n' \
                       'если вам станет что-то известно - пишите\n' \
                       '*Хотите распостранить новость* - смело пишите [сюда](t.me/efi_fi).'

        db_users = db_queries.get_users(connection)
        num_users = len(db_users)
        delivered = 0
        for db_user in db_users:
            user = get_user_dict(db_user)
            if send_mail(bot, user, message_text, settings):
                delivered += 1

        print(f'ALL USERS {num_users}\n'
              f'DELIVERED {delivered}\n'
              f'ERROR, NOT DELIVERED {num_users - delivered}\n')
    except:
        print(get_log_line('ERROR', settings))


def send_mail(bot, user, message_text, settings):
    user_info = f'ID:{user["id"]} username:{user["username"]}'
    appeal = f'Message for *{user["first_name"]} {user["last_name"]}*\n'
    for _ in range(10):
        try:
            bot.send_message(user['id'], appeal+message_text, parse_mode=settings.parse_mode)
            print(get_log_line('DELIVERED\n' + user_info, settings))
            return True
        except Exception:
            continue
    print(get_log_line('ERROR, NOT DELIVERED\n' + user_info, settings))


if __name__ == '__main__':
    main()
