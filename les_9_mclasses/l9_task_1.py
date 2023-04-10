# первый блок
class Validator:
    def __set__(self, instance, value):
        if type(value) != int:
            raise TypeError("Зарплату и премию необходимо указать"
                            " целым положительным числом)")

        elif value < 0:
            raise ValueError("Зарплату и премию необходимо указать"
                             " целым положительным числом)")

        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    wage = Validator()
    bonus = Validator()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.bonus = bonus
        self.wage = wage


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        sum_v = self.wage + self.bonus
        return sum_v

    def __str__(self):
        return f"{self.get_full_name()} {str(self.get_total_income())}"


men = Position('Vally', 'Black', 'worker', 10, 50)
print(men)


# Второй блок
class Validator2:
    def __set__(self, instance, value):
        if not isinstance(value, list):
            raise TypeError("Необходимо ввести список (список списков)")

        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Matrix:
    my_list = Validator2()

    def __init__(self, my_list):
        self.my_list = my_list
        self.rows = len(my_list)
        self.columns = len(my_list[0])

    def __str__(self):
        res = ''
        for i in range(self.rows):
            for x in self.my_list[i]:
                res += str(x)
                res += " "
            res += "\n"
        return res

    def __add__(self, other):
        res_list_1 = []
        res_list_2 = []
        res_matrix = []
        for i in range(self.rows):
            for x in self.my_list[i]:
                res_list_1.append(x)
        for i in range(other.rows):
            for x in other.my_list[i]:
                res_list_2.append(x)
        for i in range(self.rows):
            try:
                res_matrix.append([res_list_1[count_1] + res_list_2[count_1]
                                   for count_1 in
                                   range(i * self.columns,
                                         (i + 1) * self.columns)])
            except IndexError:
                return "Нельзя складывать матрицы разного размера"

        return Matrix(res_matrix)


obj_1 = Matrix([[1, 1, 1], [1, 1, 1], [4, 4, 4], [3, 5, 0]])
obj_2 = Matrix([[1, 1, 1], [1, 1, 1], [4, 4, 4], [5, 5, 5]])
print(obj_1)
print(obj_2)
print(obj_1 + obj_2)
print(type(obj_1.my_list))
