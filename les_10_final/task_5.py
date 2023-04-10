"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

yandex = ['ping', 'yandex.ru']
yand_ping = subprocess.Popen(yandex, stdout=subprocess.PIPE)
print('yandex.ru')
for line in yand_ping.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

youtube = ['ping', 'youtube.com']
yout_ping = subprocess.Popen(youtube, stdout=subprocess.PIPE)
print('youtube.com')
for line in yout_ping.stdout:
    result = chardet.detect(line)
    print(line.decode(result['encoding']))  # без перекодировки
