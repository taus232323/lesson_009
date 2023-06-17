# -*- coding: utf-8 -*-
import re
from pprint import pprint

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
file_name = 'events.txt'


class Parser:
    events_counter = {}
    list_of_lines = []

    def __init__(self, file_name):
        self.file_name = file_name
        self.user = 0
        self.sorted_keys = []

    def extract(self):
        with open(file_name, 'r', encoding='utf8') as file:
            for line in file:
                if 'NOK' in line:
                    new_lines = line[1:17]
                    self.list_of_lines.append(new_lines)

    def institute(self):
        for elements in self.list_of_lines:
            if elements in self.events_counter:
                self.events_counter[elements] += 1
            else:
                self.events_counter[elements] = 1

    def user_input(self):
        self.user = int(input('Введите:\n"1" для сортировки по году\n'
                         '"2" для сортировки по месяцу\n'
                         '"3" для сортировки по часам\n'
                         'Ваш выбор: '))

    def sorting(self):
        if self.user == 1:
            self.sorted_keys = sorted(self.events_counter.keys(), key=lambda x: x[3:])
        elif self.user == 2:
            self.sorted_keys = sorted(self.events_counter.keys(), key=lambda x: x[8:])
        elif self.user == 3:
            self.sorted_keys = sorted(self.events_counter.keys(), key=lambda x: x[-5:])
        else:
            print('Не корректный ввод')
            return

    def output(self, output_file):
        with open(output_file, 'w', encoding='utf8') as file:
            for key in self.sorted_keys:
                file.write(f"[{key}] {self.events_counter[key]}\n")

    def act(self):
        self.extract()
        self.institute()
        self.user_input()
        self.sorting()
        self.output(output_file='events_output.txt')


parser = Parser(file_name='events.txt')
parser.act()
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
