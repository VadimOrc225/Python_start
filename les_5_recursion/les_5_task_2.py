'''
Задание 2. Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
'''


def my_func(n, counter_1, counter_2):
    if n == 0:
        print(f"Четных цифр: {counter_1}, нечетных цифр: {counter_2}")
    else:
        if n % 2 == 0:
            counter_1 += 1
        else:
            counter_2 += 1
        return my_func(n // 10, counter_1, counter_2)


n = int(input("Введите число "))
counter_1 = 0
counter_2 = 0
my_func(n, counter_1, counter_2)
