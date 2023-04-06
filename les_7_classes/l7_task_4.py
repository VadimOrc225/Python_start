'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод init()), который должен принимать данные (список списков)
для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных
в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы
в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух
 объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
'''


class Matrix:

    def __init__(self, list_1):
        self.my_list = list_1
        self.rows = len(list_1)
        self.columns = len(list_1[0])

    def __str__(self):
        res = ''
        for i in range(self.rows):
            for x in self.my_list[i]:
                res += str(x)
                res += " "
            res += "\n"
        return res

    def __add__(self, other):
        res_list_1 = []
        res_list_2 = []
        res_matrix = []
        for i in range(self.rows):
            for x in self.my_list[i]:
                res_list_1.append(x)
        for i in range(other.rows):
            for x in other.my_list[i]:
                res_list_2.append(x)
        for i in range(self.rows):
            try:
                res_matrix.append([res_list_1[count_1] + res_list_2[count_1]
                                   for count_1 in
                                   range(i * self.columns,
                                         (i + 1) * self.columns)])
            except IndexError:
                return "Нельзя складывать матрицы разного размера"

        return Matrix(res_matrix)


obj_1 = Matrix([[1, 2, 3], [1, 1, 1], [2, 2, 2], [3, 3, 3]])
obj_2 = Matrix([[1, 1, 1], [1, 1, 1], [4, 4, 4], [5, 5, 5]])
print(obj_1)
print(obj_2)
print(obj_1 + obj_2)
