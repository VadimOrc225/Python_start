'''
Задание 3. Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.
'''


def num_reverse(n, str_res):
    if n == 0:
        return str_res
    else:
        str_res = str_res + str(n % 10)
        return num_reverse((n // 10), str_res)


n = int(input("Введите число "))
str_res = ""
print(num_reverse(n, str_res))
