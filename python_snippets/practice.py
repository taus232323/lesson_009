# -*- coding: utf-8 -*-

# Сделать генератор текста на основе статистики
# Идея проста: подсчитаем какие буквы наиболее часто стоят рядом
# Точнее, подсчитаем как часто за буковой Х идет буква У, на основе некоего текста.
# После этого начнем с произвольной буквы и каждую следующую будем выбирать в зависимости от
# частоты её появления в статистике.
import zipfile
from pprint import pprint
from random import randint

class Chatterer:
    analize_count = 4

    def __int__(self, zip_file_name):
        self.zip_file_name = zip_file_name
        self.stat = {}

    def unzip(self):
        zfile = zipfile.ZipFile(self.zip_file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        return filename

    def collect(self, file_name):
        stat = {}
        sequence = ' ' * self.analize_count
        with open(file_name, 'r', encoding='cp1251') as file:
            for line in file:
                line = line[:-1]
                for char in line:
                    if sequence in stat:
                        if char in stat[sequence]:
                            stat[sequence][char] += 1
                        else:
                            stat[sequence][char] = 1
                    else:
                        stat[sequence] = {char: 1}
                    sequence = sequence[1:] + char


file_name = 'voyna-i-mir.txt'
analize_count = 4



# pprint(stat)
# pprint(len(stat))
#
# totals = {}
# stat_for_generate = {}
# for sequence, char_stat in stat.items( ):
#     totals[sequence] = 0
#     stat_for_generate[sequence] = []
#     for char, count in char_stat.items():
#         totals[sequence] += count
#         stat_for_generate[sequence].append([count, char])
#     stat_for_generate[sequence].sort(reverse=True)
#
# N = 1000
#
# printed = 0
# sequence = ' ' * analize_count
# spaces_printed = 0
# while printed < N:
#     char_stat = stat_for_generate[sequence]
#     total = totals[sequence]
#     dice = randint(1, total)
#     pos = 0
#     for count, char in char_stat:
#         pos += count
#         if dice <= pos:
#             break
#     print(char, end='')
#     if char == ' ':
#         spaces_printed += 1
#         if spaces_printed >= 10:
#             print()
#             spaces_printed = 0
#     printed += 1
#     sequence = sequence[1:] + char
#
