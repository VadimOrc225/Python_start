'''
Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
'''
n = input("Введите целое положительное число n: ")
sum_numbers = int(n + n + n) + int(n + n) + int(n)
print(f"n + nn + nnn = {sum_numbers}")

