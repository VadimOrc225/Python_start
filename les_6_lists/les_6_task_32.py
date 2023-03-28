'''Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)'''
import random

primary_list = [random.randint(1, 50) for x in range(15)]
min_el = int(input("Введите минимум "))
max_el = int(input("Введите максимум "))
print(f"Исходный массив {primary_list}")
index_list = [x for x in range(len(primary_list)) if
              primary_list[x] >= min_el and primary_list[x] <= max_el]
print(f"Индексы элементов, удовлетворяющих условию {index_list}")
