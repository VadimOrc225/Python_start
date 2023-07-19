class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("The engine has started.")


my_car = Car("Toyota", "Camry", 2020)
print(my_car.make)  # Выводит: Toyota
print(my_car.model)  # Выводит: Camry
print(my_car.year)  # Выводит: 2020
my_car.start_engine()  # Выводит: The engine has started.

