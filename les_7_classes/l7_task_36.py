'''
Задача 36: Напишите функцию print_operation_table(operation, num_rows=6,
num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую
элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают
число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация
строк и столбцов идет с единицы (подумайте, почему не с нуля).
Примечание: бинарной операцией называется любая операция, у которой ровно
два аргумента, как, например, у операции умножения.

*Пример:*

**Ввод:** `print_operation_table(lambda x, y: x * y) `
**Вывод:**
1 2 3 4 5 6

2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
'''


class MyPrinter:
    num_rows = 6
    num_columns = 6

    def __init__(self, operation):
        self.print_operation_table(operation)

    def math_1(self, operation, x, y):
        print(operation(x, y), end=' ')

    def print_operation_table(self, operation):
        for x in range(1, self.num_rows + 1):
            for y in range(1, self.num_columns + 1):
                self.math_1(operation, x, y)
            print('\n')



p_1 = MyPrinter(lambda x, y: x * y)
