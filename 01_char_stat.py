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

class Counter:
    stat = {}

    def __init__(self, file_name):
        self.file_name = file_name
        self.total = 0
        self.user = 0

    def count(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha() == True:
                        if char in self.stat:
                            self.stat[char] += 1
                        else:
                            self.stat[char] = 1
            values_sum = sum(self.stat.values())
            self.total += values_sum

    def sorting(self):
        print(' Введи "1" чтобы отсортировать по алфавиту по убыванию, "2" по возрастанию\n '
              'Введи "3" чтобы отсортировать по количеству по убыванию, "4" по возрастанию')
        user = int(input('\n Я выбираю: '))
        if user == 1:
            sorted_dict = sorted(self.stat.items(), key=lambda x: x[0], reverse=True)
        elif user == 2:
            sorted_dict = sorted(self.stat.items(), key=lambda x: x[0], reverse=False)
        elif user == 3:
            sorted_dict = sorted(self.stat.items(), key=lambda x: x[1], reverse=True)
        elif user == 4:
            sorted_dict = sorted(self.stat.items(), key=lambda x: x[1], reverse=False)
        else:
            print('Такой цифры нет!!')
            return
        for chars, values in sorted_dict:
            print(f'|{chars:10}|{values:10}|')

    def head(self):
        print('+{txt:-^21}+'.format(txt='+'))
        print('|{txt1:^10}|{txt2:^10}|'.format(txt1='буква', txt2='частота'))
        print('+{txt:-^21}+'.format(txt='+'))

    def totals(self):
        print('+{txt:-^21}+'.format(txt='+'))
        print('|{txt1:^10}|{txt2:^10}|'.format(txt1='Итого', txt2=self.total))
        print('+{txt:-^21}+'.format(txt='+'))

    def implementation(self):
        self.count()
        self.sorting()
        self.head()
        self.totals()


counter = Counter(file_name='voyna-i-mir.txt')
counter.implementation()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
