# Напишите программу, которая получает на вход путь до каталога
# (в том числе это может быть просто корень диска)
# и выводит общее количество файлов и подкаталогов в нём.
# Также выведите на экран размер каталога в килобайтах (1 килобайт = 1024 байт).

# Важный момент: чтобы посчитать, сколько весит каталог,
# нужно найти сумму размеров всех вложенных в него файлов.

# Результат работы программы на примере python_basic\Module14:
# E:\PycharmProjects\python_basic\Module14
# Размер каталога (в Кбайтах): 8.373046875
# Количество подкаталогов: 7
# Количество файлов: 15


import os

folder_name = 'p_2-09_-_files'
# folder_path = os.path.abspath(folder_name)
folder_path = os.path.join('..', folder_name)
# folder_abspath = os.path.abspath(folder_name)
#

file_size = 0
file_count = 0

# print(os.listdir(folder_path))
for folder in os.listdir(folder_path):
    # print(folder, os.path.getsize(os.path.join(folder)))
    file_size += os.path.getsize(folder)
    file_count += 1

print(f'Ваша путь до папки: {os.path.abspath(folder_path)}')
print(f'Размер каталога: {file_size} байта')
print(f'Количество файлов: {file_count}')



