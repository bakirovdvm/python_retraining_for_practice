import os

file_name = 'people.txt'
path_for_file_name = os.path.join(file_name)

symb_count = 0
with open(path_for_file_name, 'r', encoding='utf-8') as data_from_file:
    for item in data_from_file:
        symb_count += len(item.strip())
        try:
            if len(item) - 1 < 3:
                raise BaseException

        except BaseException:
            print('Ошибка: менее трёх символов в строке 5.')


print('Общее количество символов:', symb_count)
