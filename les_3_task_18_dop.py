'''
Требуется найти в массиве A[1..N] самый близкий по величине элемент к
заданному числу X. Пользователь в первой строке вводит натуральное число N –
количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит X
'''

import random

n = int(input("Введите число элементов массива: "))
list_A = []
for i in range(n):
    list_A.append(random.randint(1, 50))
print(*list_A)
x = int(input("Введите число X: "))
i = 1
while True:
    try:
        res = list_A.index(x - i)  # ближайшее число
        break
    except ValueError:        # в массиве нет такого значения
        try:
            res = list_A.index(x + i)  # ближайшее число в др.сторону
            break
        except ValueError:    # в массиве нет такого значения
            i += 1
print(list_A[res])
