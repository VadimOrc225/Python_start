"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": []
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""
import json


def write_order_to_json(order, orders_f, res_file):
    order_list = []
    with open(orders_f, encoding="utf-8") as f_n:
        data = json.load(f_n)
        for x in data['orders']:
            order_list.append(x)
        order_list.append(order)
    with open(res_file, "w", encoding="utf-8") as f_n:
        json.dump({'orders': order_list}, f_n, indent=4, ensure_ascii=False)


write_order_to_json({'item': 'table1',
                     'quantity': '1',
                     'price': '3500',
                     'buyer': 'Igor P.',
                     'date': '07.04.2023'}, 'orders.json', "my_orders.json")
