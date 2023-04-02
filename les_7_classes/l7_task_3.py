'''
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать публичные методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
str(self) - вызывается функциями str, print и format. Возвращает строковое
представление объекта.
'''


class Worker:
    name = "Name"
    surname = "Surname"
    position = "Position"
    _income = {"wage": 100, "bonus": 5}


class Position(Worker):
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

    def get_full_name(self):
        return self.name + self.surname

    def get_total_income(self):
        sum_v = 0
        for v in self._income.values():
            sum_v += v
        return sum_v

    def __str__(self):
        return f"{self.get_full_name()} {str(self.get_total_income())}"


men = Position('Vally', 'Black', 'worker')
print(men)
