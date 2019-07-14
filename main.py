from time import sleep
from telebot import TeleBot

from settings import Settings
from bot_logging import get_log_line
from db_queries import get_connection
from main_functions import process_message
from constantes import bot_token, database_url, get_markups


def main():
    bot = TeleBot(bot_token)
    settings = Settings()
    markups = get_markups()

    while True:
        try:
            connection = get_connection(database_url, settings)
            print(get_log_line('START', settings))

            @bot.message_handler(func=lambda message: True)
            def echo_all(message):
                process_message(bot, connection, message, markups, settings)

            bot.polling()

        except:
            print(get_log_line('ERROR', settings))
            sleep(settings.pause)


if __name__ == '__main__':
    main()
