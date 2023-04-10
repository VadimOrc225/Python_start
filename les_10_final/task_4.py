"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
list_1 = ['разработка', 'администрирование', 'protocol', 'standard']
list_2 = [x.encode('utf-8') for x in list_1]
list_3 = []
for x in range(len(list_2)):
    print(list_2[x])
    list_3.append(list_2[x].decode('utf-8'))
print(list_3)

