'''Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000),
а Катя должна их отгадать. Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.'''
import math

x = int(input("Задайте натуральное число x: "))
y = int(input("Задайте натуральное число y: "))
sum_num = x + y
product = x * y
print(f"Сумма: {sum_num}")
print(f"Произведение: {product}")
print(f"Загаданные числа были равны {x} и {y}")
deskrimin = sum_num * sum_num - 4 * product
if deskrimin < 0:
    print("решений нет")
elif deskrimin == 0:
    print(f"Катины числа: {int(sum_num / 2)} и {int(sum_num / 2)}")
else:
    print(f"Катины числа: {int((sum_num - math.sqrt(deskrimin)) / 2)} и"
          f" {int((sum_num + math.sqrt(deskrimin)) / 2)}")
