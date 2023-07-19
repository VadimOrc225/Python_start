import json
from datetime import datetime
import os


def add_new_to_json(res_file):  # функция добавления новой заметки
    header = input("Введите заголовок: ")
    body = input("Введите тело заметки: ")
    current_date = str(datetime.now().date())
    note_list = []
    if (os.path.exists(res_file)):
        with open(res_file, encoding="utf-8") as f_n:
            data = json.load(f_n)
            identificator = len(data)
            for x in data:
                note_list.append(x)
    else:
        identificator = 0
    note = {
        'Идентификатор': identificator,
        'Заголовок': header,
        'Тело заметки': body,
        'Дата': current_date}
    note_list.append(note)
    with open(res_file, "w", encoding="utf-8") as f_n:
        json.dump(note_list, f_n, indent=4, ensure_ascii=False)
    print("Заметка успешно сохранена")


def date_search(searcher, res_file):  # функция вывода заметок по дате
    if (os.path.exists(res_file)):
        with open(res_file, encoding="utf-8") as f_n:
            data = json.load(f_n)
            key = 'Дата'
            for x in data:
                if x[key] == searcher:
                    print(x)


def search_in_json(searcher,
                   res_file):  # функция поиска заметки и работы с найденной заметкой
    if (os.path.exists(res_file)):
        with open(res_file, encoding="utf-8") as f_n:
            data = json.load(f_n)
            key = 'Заголовок'
            d = next(
                (d for d in data if d.get(key).lower() == searcher.lower()),
                None)
            index = data.index(d)
            identificator = d.get('Идентификатор')
            print(d)

    choose2 = int(input(
        "Что вы хотите? Изменить эту заметку - 1; Удалить заметку - 2: "))
    if (choose2 == 1):
        note_list = data
        header = input("Введите новый заголовок: ")
        body = input("Введите новое тело заметки: ")
        current_date = str(datetime.now().date())
        note = {
            'Идентификатор': identificator,
            'Заголовок': header,
            'Тело заметки': body,
            'Дата': current_date}
        note_list[index] = note
        with open(res_file, "w", encoding="utf-8") as f_n:
            json.dump(note_list, f_n, indent=4, ensure_ascii=False)
        print("Заметка успешно изменена")

    elif (choose2 == 2):
        note_list = data
        note_list.pop(index)
        with open(res_file, "w", encoding="utf-8") as f_n:
            json.dump(note_list, f_n, indent=4, ensure_ascii=False)
        print("Заметка успешно удалена")


while (True):
    choose1 = int(input(
        "Что вы хотите? Добавить новую заметку - 1; Найти заметку по заголовку - 2;"
        " Вывести список всех заметок - 3; Вывести заметки по дате создания - 4; Выход - 0: "))
    if (choose1 == 1):
        add_new_to_json("my_notes.json")
    elif (choose1 == 2):
        searcher = input("Введите заголовок: ")
        search_in_json(searcher, "my_notes.json")
    elif (choose1 == 3):
        if (os.path.exists("my_notes.json")):
            with open("my_notes.json", encoding="utf-8") as f_n:
                data = json.load(f_n)
                print(data)
    elif (choose1 == 4):
        searcher = input(
            "Введите дату в формате год-месяц-число (ПРИМЕР: 2023-07-18): ")
        date_search(searcher, "my_notes.json")
    elif (choose1 == 0):
        print("Работа завершена. До свидания!")
        break
