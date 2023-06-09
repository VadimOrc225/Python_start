"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""

import re


def get_data(source_files, search_list):
    res = [search_list]
    count_1 = 1
    for x in source_files:
        with open(x) as f_stream:
            file_data = f_stream.read()
            data_line = []
            for el in range(len(res[0])):
                os_prod_reg = re.compile(rf'{search_list[el]}:\s*\S*')
                data_line.append(
                    (os_prod_reg.findall(file_data)[0].split()[2]))
            if True:
                data_line.insert(0, str(count_1))
            res.append(data_line)
        count_1 += 1
    return res


def write_to_csv(finded_data, result_file):
    with open(result_file, "w", encoding="utf8") as file_w:
        for data_string in finded_data:
            file_w.write(', '.join(data_string) + "\n")


write_to_csv(get_data(["info_1.txt", "info_2.txt", "info_3.txt"],
                      ["Изготовитель системы", "Название ОС", "Код продукта",
                       "Тип системы"]), "my_data_report.csv")
