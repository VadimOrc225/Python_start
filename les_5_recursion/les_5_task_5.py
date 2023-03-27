'''
Задание 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
'''


def func_ascii(n, m, counter):
    if n == m + 1:
        return 0
    else:
        print(f"{n} - {chr(n)} ") if counter % 10 == 0 else print(
            f"{n} - {chr(n)} ", end='')
        counter += 1
        return func_ascii(n + 1, m, counter)


func_ascii(32, 127, 1)
