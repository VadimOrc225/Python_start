# Представление (View) - отображает пользовательский интерфейс и обрабатывает ввод пользователя
class CalculatorView:
    def get_input(self):
        num1 = float(input("Введите первое число: "))
        operator = input("Введите оператор (+, -, *, /): ")
        num2 = float(input("Введите второе число: "))
        return num1, operator, num2

    def display_result(self, result):
        print("Результат:", result)