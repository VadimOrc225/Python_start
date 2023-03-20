import math

seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {0: 'winter', 1: 'spring', 2: 'summer', 3: 'autumn'}
month = int(input("Введите номер месяца: "))
month = month + 1 if month < 12 else 1
season_number = math.ceil(month / 3) - 1
print(seasons_list[season_number])
print(seasons_dict[season_number])
