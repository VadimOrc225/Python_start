'''Задача 30:  Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.'''

a1 = float(input("Введите первый элемент арифметической прогрессии"))
d = float(input("Введите разность прогрессии"))
n = int(input("Введите количество элементов прогрессии"))
list_res = [a1 + (k - 1) * d for k in range(1, n + 1)]
print(list_res)