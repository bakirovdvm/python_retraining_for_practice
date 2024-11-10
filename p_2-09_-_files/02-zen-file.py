import os
# import this

file_name = 'zen.txt'
file_path = os.path.join(file_name)

file = open(file_path, 'r', encoding='utf-8')

file_list = list(file)


for i in range(len(file_list) - 1, -1, -1):
    print(file_list[i].replace('\n', ''))


# Напишите программу, которая выводит на экран все строки этого файла в обратном порядке.
# Кстати, попробуйте открыть консоль Python и ввести команду import this.
# Результат работы программы:
# Namespaces are one honking great idea -- let's do more of those!
# If the implementation is easy to explain, it may be a good idea.
# If the implementation is hard to explain, it's a bad idea.
# Although never is often better than *right* now.