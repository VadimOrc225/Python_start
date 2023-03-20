import random

n = int(input("Введите число кустов на грядке: "))
list_1 = []
for i in range(n):
    list_1.append(random.randint(0, 10))
print(*list_1, "- кусты на грядке с опр. количеством ягод")
max_berries = sum(list_1[0: 3])
list_1.append(list_1[0])
list_1.append(list_1[1])
for i in range(1, n + 1):
    sum_berries = sum(list_1[i - 1: i + 2])
    if max_berries < sum_berries:
        max_berries = sum_berries
print(max_berries, "- максимальное собранное количество")
