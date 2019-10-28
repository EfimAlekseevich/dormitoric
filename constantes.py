from telebot.types import ReplyKeyboardMarkup
from os import environ as env


bot_token = env['BOT_TOKEN']
database_url = env['DATABASE_URL']

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
                   "SET updated = %(updated)s,"
                   " num_messages = %(num_messages)s,"
                   " last_message = %(last_message)s,"
                   " crimes = %(crimes)s "
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
            ["Группа ВК", "Пункты питания БГУИР"],
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
    "start": "Привет, надеюсь я смогу тебе помочь.",
    "help": "По всем вопросам связанным с ботом обращайтесь [сюда](t.me/efi_fi)",
    "info": "Бот был создан для помощи жителям 1 общежития БГУИР,\n"
            "с помощью меню вы можете быстро найти нужную информацию.\n"
            "Ради интереса и для лучшего понимания пользователей мы собираем статистику,\n"
            "В разделе *статистика* вы можете заполнить информацию *о себе*.\n"
            "Замечания и предложения -> /help",
    "menu": "Если меню не открылось пишите [сюда](t.me/efi_fi)"
}

usually_answers = {
    "Основная информация": "maininfo.txt",
    "Душ": "showers.txt",
    "Обмен постельного белья": "Обмен белья осуществляется\n"
                               "каждый вторник с *8:30* - *17:00*.\n"
                               "Обеденный  перерыв с *13:00* - *13:45*.",
    "Время открытия-закрытия общежития": "C *6:00* до *24:00*",
    "Время для гостей": "guests.txt",
    "Администрация": "administration.txt",
    "Прачечная": "laundry.txt",
    "Камера хранения": "Чтобы поместить вещи в камеру хранения\n"
                       "можно обратиться к [коменданту: Высоцкая Марина Михайловна](https://vk.com/id70368328)",
    "Столовая": "canteen.txt",
    "Лифт": "Лифт включают в *7:00*, а выключают в *22:55*.",
    "Кухня": "Плиты и микроволновки(если есть)\nработают с *6:00* до *24:00*",
    "Дежурства": "duty.txt",
    "ОПТ": "OPT.txt",
    "Обо мне": "Извините, база данных не отвечает",
    "Обо всех": "Извините, база данных не отвечает",
    "Заселение": "checkin.txt",
    "Выселение": "eviction.txt",
    "Печать": "printing.txt",
    "Интернет": "Здесь только один [провайдер](https://unet.by).",
    "Группа ВК": "[Тут](https://vk.com/hostel_1) можно найти много полезного.",
    "Привет": "Не привет, а Здравствуйте.",
    "Пока": "Я тебя запомнил.",
    "Бот": "На себя посмотри.",
    "Пункты питания БГУИР": "[Посмотреть]"
                            "(http://library.bsuir.by/index.jsp?PageID=82390&resID=100229&lang=ru&menuItemID=114395)."
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

bad_answer = 'В случае не прекращения использования ненормативной лексики\n' \
             '*на вас* будет составлен _бото-административный протокол_.'

other_answers = ["Если у вас имеются какие-либо идеи или замечания просим вас написать в поддержку /help",
                 "Идёт развитие бота, будем благодарны за любую помощь",
                 "Будем рады, если вы заполните информацию о себе в разделе статистика /help",
                 "Бот не умеет испралять баги самостоятельно для этого есть служба поддержки /help",
                 "Ходят слухи, что Dormitoric не любит, когда его называют ботом)",
                 "Если вам скучно, можете меня протестить и отправить отзыв в поддержку /help",
                 "Если вы заполните всю информацию о себе вам станет доступна часть статистики обо всех)",
                 "Мне кажется тебе нужно выспаться.",
                 "Иногда тебя понять довольно сложно)",
                 "Я тебя не понимать",
                 "Помоги мне стать лучше, напиши [сюда](t.me/efi_fi) идею.",
                 "А ты сегодня неплох.",
                 "Может помытся уже сгоняешь.",
                 "А не пора ли тебе отдохнуть.",
                 "Как насчёт поменять бельё во вторник?",
                 "Не забывай делать зарядку для глаз.",
                 "Может встанешь и разамнёшься.",
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
