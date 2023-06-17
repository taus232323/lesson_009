# -*- coding: utf-8 -*-
import os, time, shutil
import zipfile
from pprint import pprint


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class FileOrganizer:

    def __init__(self, zip_file_name, target_dir):
        self.target_dir = target_dir
        self.zip_file_name = zip_file_name
        self.source_dir = 'icons'
        self.dir_name = None
        self.source_file_path = None


    def unzip(self):
        if self.zip_file_name.endswith('.zip'):
            with zipfile.ZipFile(self.zip_file_name, 'r') as zip_ref:
                zip_ref.extractall(self.source_dir)
            self.dir_name = os.path.splitext(self.zip_file_name)[0]
        else:
            with zipfile.ZipFile(self.zip_file_name, 'r') as zip_ref:
                for dirname in zip_ref.namelist():
                    zip_ref.extract(dirname)
                self.dir_name = dirname

    def organize_files(self):
        self.unzip()
        for root, dirs, files in os.walk(self.dir_name):
            for file in files:
                self.source_file_path = os.path.join(root, file)
                year, month = self.extract_year_and_month(self.source_file_path)
                target_dir_path = os.path.join(self.target_dir, str(year), str(month).zfill(2))
                if not os.path.exists(target_dir_path):
                    os.makedirs(target_dir_path)
                target_file_path = os.path.join(target_dir_path, file)
                shutil.copy2(self.source_file_path, target_file_path)
        self.remove_residuals()

    def remove_residuals(self):
        shutil.rmtree(self.dir_name)

    def extract_year_and_month(self, file_path):
        create_time = os.path.getmtime(file_path)
        struct_time = time.localtime(create_time)
        year = struct_time.tm_year
        month = struct_time.tm_mon
        return year, month


organizer = FileOrganizer(zip_file_name='icons.zip', target_dir='icons_by_year')
organizer.organize_files()



# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
