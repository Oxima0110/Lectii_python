# Возьмите 1-3 задачи из тех, что были на прошлых семинарах
# или в домашних заданиях. Напишите к ним классы исключения
# с выводом подробной информации. Поднимайте исключения
# внутри основного кода. Например нельзя создавать
# прямоугольник со сторонами отрицательной длины.


class MyException(Exception):
    pass


class RadiusError(MyException):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'Значение радиуса должно быть положительное.'\
               f'Вы вводите: {self.value}'


class NameError(MyException):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'Значение должно быть строкой.'\
               f'Вы вводите: {self.value}'


class AgeError(MyException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Возраст человека должен быть целым int() или вещественным float() больше нуля.\n' \
               f'У вас тип {type(self.value)}, а значение {self.value}'


class RectangleError(MyException):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'Значение стороны должно быть целым int() или вещественным float() больше нуля.'\
               f'У вас тип {type(self.value)}, а значение {self.value}'
