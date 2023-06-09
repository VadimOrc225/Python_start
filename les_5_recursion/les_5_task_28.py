'''
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух
 целых неотрицательных чисел. Из всех арифметических операций допускаются
только +1 и -1. Также нельзя использовать циклы.
'''


def summator(a, b):
    if a == 0 and b == 0:
        return 0
    if a == 0:
        return 1 + summator(0, b - 1)
    elif b == 0:
        return 1 + summator(a - 1, 0)
    else:
        # уменьшаем сразу оба числа, увеличивая сумму на 2
        # пока одно из них не станет равно 0
        return 1 + 1 + summator(a - 1, b - 1)


a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
print(summator(a, b))