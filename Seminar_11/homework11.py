'''
Задача 3. Создайте класс Матрица.
Добавьте методы для:
- вывода на печать,
- сравнения,
- сложения,
- *умножения матриц
'''


class Matrix:
    '''Класс матрица с инициализацией списка списков,с переопределенными
     методами сложения и умножения и строчного вывода.'''

    def __init__(self, nested_list: list[list[int]]) -> None:
        '''Инициализация экземпляра с аргументом list[list[int]].'''
        self.nested_list = nested_list

    def __str__(self):
        'Вывод строкового представления экземпляра.'
        result = ''
        for row in self.nested_list:
            for elem in row:
                result += ''.join(f'{elem}\t')
            result += ''.join('\n')
        return result

    def __repr__(self):
        '''Переопределенный дандер метод строчного выведения
          создания экземпляра класса'''
        return f'Matrix({self.nested_list})'

    def __eq__(self, other):
        '''Переопределённый метод для сравнения матриц.
        Матрицы могут быть равны когда равны их длины и каждый элемент.'''
        return True if self.nested_list == other.nested_list else False

    def __add__(self, other):
        '''Переопределенный метод поэлементного сложения матриц.
        Можно складывать матрицы одинаковой длины:
        строки первой и столбца второй. '''
        result = []
        row = []
        for i in range(len(self.nested_list)):
            for j in range(len(self.nested_list[0])):
                row.append(self.nested_list[i][j] +
                           other.nested_list[i][j])
            result.append(row)
            row = []
        return Matrix(result)

    def __mul__(self, other):
        '''Переопределенный метод умножения матриц.
        Можно умножать матрицы одинаковой длины:
        строки первой и столбца второй.'''
        m = len(self.nested_list)
        n = len(other.nested_list)
        k = len(other.nested_list[0])
        result = [[0 for _ in range(k)] for _ in range(m)]
        for i in range(m):
            for j in range(k):
                result[i][j] = sum(self.nested_list[i][k] *
                                   other.nested_list[k][j] for k in range(n))
        return Matrix(result)


if __name__ == '__main__':
    matrix_1 = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    matrix_2 = Matrix([[2, 2, 2], [1, 1, 1], [1, 1, 1]])
    matrix_sum = matrix_1 + matrix_2
    print(matrix_sum)
    matrix_mul = matrix_1 * matrix_2
    print(matrix_mul)
    print(matrix_1 == matrix_2)
