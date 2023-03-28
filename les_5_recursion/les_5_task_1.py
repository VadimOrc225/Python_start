'''
Задание 1. Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
Решите через рекурсию. В задании нельзя применять циклы.
'''


def calculator():
    operation = input("Введите операцию (+, -, *, / или 0 для выхода): ")
    if operation == '0':
        return "Завершение работы"
    else:
        if operation in "+-*/":
            try:
                a = int(input("Введите ПЕРВОЕ число: "))
                b = int(input("Введите ВТОРОЕ число: "))
                if operation == '+':
                    print(f"Ваш результат {a + b}")
                    return calculator()
                elif operation == '-':
                    print(f"Ваш результат {a - b}")
                    return calculator()
                elif operation == '*':
                    print(f"Ваш результат {a * b}")
                    return calculator()
                else:
                    try:
                        result = a / b
                    except ZeroDivisionError:
                        print("Делить на ноль нельзя")
                    else:
                        print(f"Ваш результат {a / b}")
                    finally:
                        return calculator()
            except ValueError:
                print("Вы ввели не число")
                return calculator()
        else:
            print("Вы ввели неверный символ. Повторите ввод.")
            return calculator()

calculator()