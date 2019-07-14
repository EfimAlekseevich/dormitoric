import psycopg2
from datetime import datetime

from bot_logging import get_log_line
from constantes import sql_queries


def get_connection(database_url, settings):
    try:
        connection = psycopg2.connect(database_url)
        print(get_log_line('The database connection is established', settings))
        return connection
    except:
        print(get_log_line('Database connection error', settings))


def get_user(connection, user_id):
    sql = sql_queries['get_user']
    data = {'user_id': user_id}
    cursor = execute_query(connection, sql, data)
    user = cursor.fetchone()
    cursor.close()
    return user


def get_users(connection):
    sql = sql_queries['get_users']
    data = None
    cursor = execute_query(connection, sql, data)
    users = cursor.fetchall()
    cursor.close()
    return users


def add_user(connection, message):
    sql = sql_queries['add_user']
    d_t = datetime.now()
    last_message = message.text
    user = message.from_user
    data = {'username': user.username, 'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name,
            'created': d_t, 'updated': d_t, 'last_message': last_message}
    cursor = execute_query(connection, sql, data)
    connection.commit()
    cursor.close()


def update_parameter(connection, user_id, parameter, value):
    sql = sql_queries['update_parameter'].replace('parameter', parameter)
    data = {'user_id': user_id, 'value': value}
    cursor = execute_query(connection, sql, data)
    connection.commit()
    cursor.close()


def update_user(connection, user_id, last_message, num_messages):
    sql = sql_queries['update_user']
    data = {'user_id': user_id, 'updated': datetime.now(), 'last_message': last_message, 'num_messages': num_messages}
    cursor = execute_query(connection, sql, data)
    connection.commit()
    cursor.close()


def execute_query(connection, sql, data):
    cursor = connection.cursor()
    cursor.execute(sql, data)
    return cursor
