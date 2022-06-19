# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух
# матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, first_list, second_list):
        self.l1 = first_list
        self.l2 = second_list

    def __add__(self):
        zero_matrix = [[0, 0, 0],
                       [0, 0, 0]]

        for i in range(len(self.l1)):

            for j in range(len(self.l2[i])):
                zero_matrix[i][j] = self.l1[i][j] + self.l2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in zero_matrix]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in zero_matrix]))


matrices = Matrix([[53, 96, 17],
                   [82, 25, 27]],
                  [[51, 19, 94],
                   [47, 28, 63]])


print(matrices.__add__())