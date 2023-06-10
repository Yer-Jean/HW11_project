def str_to_upper(phrase: str):
    """Переводим строку в заглавные буквы"""
    return phrase.upper()


def words_to_capital(phrase: str):
    """Функция переводит все слова во фразе с заглавной буквы"""
    result = []
    words_in_list = phrase.split()
    for word in words_in_list:
        result.append(word.capitalize())
    return ' '.join(result)
