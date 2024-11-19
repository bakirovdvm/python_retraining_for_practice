import os

file_name = 'chat.txt'
path_for_file_name = os.path.join(file_name)

name = input('Введите свое имя: ')

while True:
    action = int(input('Что делаем?\n'
                       '1 - посмотреть текущий текст чата\n'
                       '2 - отправить сообщение\n'
                       'Выбирите действие: '))

    if action == 1:
        try:
            with open(path_for_file_name, 'r', encoding='utf-8') as file:
                for i in file:
                    print(i, end='')
        except FileNotFoundError:
            print('Ошибка: история чата не найдена!')

    elif action == 2:
        message = input('Введите сообщение: ')

        with open(path_for_file_name, 'a', encoding='utf-8') as file:
            file.write('{name}: {message} \n'. format(name=name,
                                                   message=message))

    else:
        print('Команды не существует!')
