'''
Задание 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
'''


def func1(n, limit):
    if limit == 0:
        return 0
    else:
        return n + func1(n / -2, limit - 1)


limit = int(input("Введите количество элементов: "))
n = 1
print(f"Количество элементов - {limit}, их сумма - {func1(n, limit)}")
