from telebot.types import ReplyKeyboardMarkup
from os import environ

bot_token = environ['BOT_TOKEN']
database_url = environ['DATABASE_URL']

sql_queries = {
    "get_user": "SELECT * FROM users WHERE id = %(user_id)s",
    "get_users": "SELECT * FROM users",
    "add_user": "INSERT INTO users "
                "(username, id, first_name, last_name, created, updated, last_message) "
                "VALUES (%(username)s, %(id)s, %(first_name)s, %(last_name)s,"
                " %(created)s, %(updated)s, %(last_message)s)",
    "update_parameter": "UPDATE users "
                        "SET parameter = %(value)s "
                        "WHERE id = %(user_id)s",
    "update_user": "UPDATE users "
                   "SET updated = %(updated)s, num_messages = %(num_messages)s, last_message = %(last_message)s "
                   "WHERE id = %(user_id)s"
}

user_parameters = {
    'username': '',
    'id': '',
    'first_name': 'Имя',
    'last_name': 'Фамилия',
    'gender': 'Пол',
    'floor': 'Этаж',
    'room': 'Комната',
    'course': 'Курс',
    'faculty': 'Факультет',
    'year_birth': 'Год рождения',
    'created': '',
    'updated': '',
    'num_messages': '',
    'role': '',
    'crimes': '',
    'sub': 'Подписка',
    'last_message': ''

}
skeleton_markups = {
    "Назад":
        [
            "Основная информация",
            "Расписания",
            "Обязательства",
            "Администрация",
            ["Заселение", "Выселение"],
            "Статистика",
            "Полезные ссылки"
        ],
    "Расписания":
        [
            ["Душ", "Обмен постельного белья", "Прачечная"],
            ["Кухня", "Столовая", "Лифт"],
            ["Время для гостей", "Время открытия-закрытия общежития"],
            "Камера хранения"
        ],
    "Обязательства":
        [
            ["Дежурства", "ОПТ"]
        ],
    "Полезные ссылки":
        [
            ["Печать", "Интернет"],
            ["Группа ВК", "Минск студенту"],
            "Пункты питания БГУИР",
        ],
    "Статистика":
        [
            ["Обо мне", "Обо всех"]
        ],
    "Факультет":
        [
            ["ФИТУ", "ФКП", "ФРЭ"],
            ["ФКСИС", "ФИК", "ИЭФ"],
            ["ФИНО", "ФДПиПО", "ВФ"]
        ],
    "Пол":
        [
            ["male", "female"]
        ],
    "Подписка":
        [
            ["True", "False"]
        ]
}

commands = {
    "start": "start",
    "help": "help",
    "info": "info",
    "menu": "menu"
}

usually_answers = {
    "Основная информация": "Общежитие №1 БГУИР\nМинск Якуба Коласа 28\n(метро Академия Наук)\nПочтовый индекс 220013",
    "Душ": "showers.txt",
    "Обмен постельного белья": "Обмен белья осуществляется\nкаждый вторник с 8:30 - 17:00.\nОбеденный  перерыв с 13:00 - 13:45.",
    "Время открытия-закрытия общежития": "C 6:00 до 24:00",
    "Время для гостей": "guests.txt",
    "Администрация": "administration.txt",
    "Прачечная": "laundry.txt",
    "Камера хранения": "Камера хранения",
    "Help": "Все вопросы сюда",
    "Столовая": "canteen.txt",
    "Лифт": "Лифт включают в 7:00, а выключают в 22:55.",
    "Кухня": "Плиты и микроволновки(если есть)\n<b>работают с 6:00 до 24:00</b>",
    "Дежурства": "duty.txt",
    "ОПТ": "OPT.txt",
    "Обо мне": "Извините, база данных не отвечает",
    "Обо всех": "Извините, база данных не отвечает",
    "Заселение": "заселение",
    "Выселение": "выселение",
    "Печать": "printing.txt",
    "Интернет": "<a href='https://unet.by'>Здесь только один провайдер.</a>",
    "Группа ВК": "Тут можно найти много полезного.",
    "Привет": "Не привет, а Здравствуйте.",
    "Пока": "Я тебя запомнил.",
    "Бот": "На себя посмотри.",
    "Пункты питания БГУИР": "<a href='http://library.bsuir.by/index.jsp?PageID=82390&resID=100229&lang=ru&menuItemID=114395'>Посмотреть.</a>"
}

bad_words = [
    "сук",
    "бля",
    "пизд",
    "нахуй",
    "хуй",
    "нахуя",
    "ебать",
    "ахуе",
    "трах",
    "ёба"
]

bad_answer = 'Offnis'

other_answers = ["Если у вас имеются какие-либо идеи или замечания просим вас написать в поддержку /help",
                 "Идёт развитие бота, будем благодарны за любую помощь",
                 "Все ваши сообщения адресованные не для бота пишите в службу поддержки /help",
                 "Бот не умеет испралять баги самостоятельно для этого есть служба поддержки /help",
                 "Ходят слухи, что Dormitoric не любит, когда его называют ботом)",
                 "Если вам скучно, можете меня протестить и отправить отзыв в поддержку /help",
                 "Хех)",
                 "Лол)",
                 "Иногда тебя понять довольно сложно)",
                 "Я тебя не понимать"
                 ]


def get_markups():
    markups = {}
    for name, rows in skeleton_markups.items():
        markups[name] = get_markup(rows)
        if name != 'Назад':
            if name in list(skeleton_markups.keys())[-3:]:
                markups[name].row('Обо мне')
            else:
                markups[name].row('Назад')

    return markups


def get_markup(rows):
    markup = ReplyKeyboardMarkup(True)
    for row in rows:
        if type(row) == list:
            if len(row) == 3:
                markup.row(row[0], row[1], row[2])
            else:
                markup.row(row[0], row[1])
        else:
            markup.row(row)

    return markup
