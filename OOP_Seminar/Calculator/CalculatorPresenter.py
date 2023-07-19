# Презентер (Presenter) - связывает модель и представление, обрабатывает бизнес-логику
class CalculatorPresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def calculate(self):
        num1, operator, num2 = self.view.get_input()

        if operator == "+":
            result = self.model.add(num1, num2)
        elif operator == "-":
            result = self.model.subtract(num1, num2)
        elif operator == "*":
            result = self.model.multiply(num1, num2)
        elif operator == "/":
            result = self.model.divide(num1, num2)
        else:
            result = "Ошибка: некорректный оператор"

        self.view.display_result(result)
