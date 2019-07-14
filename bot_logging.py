def get_log_line(text, settings):
    text = trim_string(text, settings.length_log_string // 2)
    length_symbols = (settings.length_log_string - len(text)) // 2
    symbols = settings.log_symbol * length_symbols
    line = symbols + text + symbols
    if len(line) < settings.length_log_string:
        line += settings.log_symbol

    return line


def trim_string(string, length):
    len_string = len(string)
    if len_string > length:
        string = string[:length-3] + '...'

    return string


def get_log_text(message, datetime, answer, crimes, settings):
    roof = get_log_line(str(datetime), settings)
    user_text = trim_string(message.text, settings.length_log_string // 2)
    answer = trim_string(answer, settings.length_log_string // 2)
    log_text = '\n' + roof + f'\n' \
        f'Username: {message.from_user.username}, Id: {message.from_user.id}\n' \
        f'First name: {message.from_user.first_name}, Last name: {message.from_user.last_name}\n' \
        f'Request: {user_text}\n' \
        f'Answer: {answer}\n' \
        f'Crimes: {str(crimes)}'

    return log_text
