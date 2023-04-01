list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd', 'e']
# list_1 = list(zip(list1, list2))
# for x in list_1:
#     print(x, end= ' ')
# print()
# x = list(enumerate(list2))
# for i in x:
#     print(i, end= ' ')
# print()
# print(*list_1)
# print(*x)
list1 = list(map(lambda x: x**2, list1))
print(*list1)
# res = list(filter(lambda x: x%3 == 0, list1))
# print(res)
data = open('file1.txt', 'a')
data.writelines(str(list1))
data.close()
