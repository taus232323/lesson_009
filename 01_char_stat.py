# -*- coding: utf-8 -*-
from operator import itemgetter
from pprint import pprint

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

stat = {}
file_name = 'voyna-i-mir.txt'
with open(file_name, 'r', encoding='cp1251') as file:
    for line in file:
        for char in line:
            if char.isalpha() == True:
                if char in stat:
                    stat[char] += 1
                else:
                    stat[char] = 1
sorted_dict = sorted(stat.items(), key=lambda x: x[1], reverse=True)
# pprint(sorted_dict)

print('|{txt:-^31}|'.format(txt='+'))
print('|{txt1:^15}|{txt2:^15}|'.format(txt1='буква', txt2='частота'))
print('|{txt:-^31}|'.format(txt='+'))

for chars, values in sorted_dict:
    print(f'|{chars:15}|{values:15}|')




# for char, count in stat.items()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
