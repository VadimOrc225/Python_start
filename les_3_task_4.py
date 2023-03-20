'''
4.Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
'''

from timeit import timeit  # для замера быстродействия двух функций


def my_func(a, b, c):
    list_1 = [a, b, c]
    list_1.sort()
    return list_1[1] + list_1[2]


def my_func2(a, b, c):
    list_1 = [a, b, c]
    for i in range(len(list_1) - 1):
        pos = i
        for j in range(i + 1, len(list_1)):
            if list_1[j] < list_1[pos]:
                pos = j
        temp = list_1[i]
        list_1[i] = list_1[pos]
        list_1[pos] = temp
    return list_1[1] + list_1[2]


print(my_func(7, 20, 5))
print(my_func2(7, 20, 5))

# замер времени выполнения первым способом
print(timeit("my_func(7, 20, 5)", "from __main__ import my_func"))
print(timeit("my_func2(7, 20, 5)", "from __main__ import my_func2"))

# замер времени выполнения вторым способом
print(timeit("my_func(7, 20, 5)", globals=globals()))
print(timeit("my_func2(7, 20, 5)", globals=globals()))
