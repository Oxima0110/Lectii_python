# Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

from string import ascii_letters, punctuation


def clean_text(text: str) -> str:
    """
    Функция которая удаляет из текста все символы
    кроме букв латинского алфавита и пробелов.
    Возвращается строка в нижнем регистре.
    >>> clean_text(text="Some text, тест")
    'some text, '

    >>> clean_text(text="Hel222lo wo456rld!")
    'hello world!'

    >>> clean_text(text='У меня есть подруга Anna')
    '    anna'
    """
    return "".join(i for i in text
        if i in ascii_letters + punctuation + " ").lower()


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
