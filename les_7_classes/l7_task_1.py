'''
Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный
метод running (запуск).
В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
'''


class TrafficLight:
    import time
    color = "color"

    def running(self):
        while True:
            self.color = "red"
            print(self.color)
            self.time.sleep(7)
            self.color = "yellow"
            print(self.color)
            self.time.sleep(2)
            self.color = "green"
            print(self.color)
            self.time.sleep(8)


a_1 = TrafficLight()
a_1.running()