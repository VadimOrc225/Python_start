# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random

n = int(input("Введите количество монет: "))
list_1 = []
sum_0 = 0
sum_1 = 0
for x in range(n):
    list_1.append(random.randint(0, 1))
print(list_1)
for x in range(n):
    if list_1[x] == 0:
        sum_0 += 1
    else:
        sum_1 += 1
if sum_0 < sum_1:
    print(f" Минимальное количество монет, которые нужно перевернуть: {sum_0}")
else:
    print(f" Минимальное количество монет, которые нужно перевернуть: {sum_1}")
