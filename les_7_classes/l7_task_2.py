'''
Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.
Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
'''


class Road:
    _road_length = 20000
    _road_width = 10
    mass_for_1 = 1
    height = 10

    def __init__(self):
        self.count_weight(Road._road_length, Road._road_width)

    def count_weight(self, _road_length, _road_width):
        self.mass_for_1 = int(input("Ввведите количество килограмм на 1 см "))
        self.height = int(input("Введите толщину полотна "))
        self.weight = Road._road_length * Road._road_width * \
                      self.mass_for_1 * self.height

        return self.weight


r_1 = Road()
print(f"Требуется {r_1.weight} кг, {r_1.weight / 1000} т")
