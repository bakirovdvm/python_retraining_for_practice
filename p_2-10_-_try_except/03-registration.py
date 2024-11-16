import os

file_name = 'registrations.txt'
file_good_log = 'registrations_good.log'
file_bad_log = 'registrations_bad.log'
data = list()
with open(file_name, 'r', encoding='utf-8') as file:
    for item in file:
        data.append(item.split())


for item in data:
    # print(item)
    try:
        if len(item) != 3:
            raise IndexError
        elif item[0].isalpha() != True:
            raise NameError
        elif '@' not in item[1] and ('.' not in item[1]):
            raise SyntaxError
        elif 10 < int(item[2]) > 99:
            raise ValueError
        else:
            with open(file_good_log, 'a', encoding='utf-8') as file_bad:
                file_bad.write(' '. join(item) + '\n')


    except IndexError:
        with open(file_bad_log, 'a', encoding='utf-8') as good_file:
            good_file.write(' '.join(item) + ' - НЕ присутствуют все три поля' + '\n')

    except NameError:
        with open(file_bad_log, 'a', encoding='utf-8') as good_file:
            good_file.write(' '.join(item) + ' - Поле «Имя» содержит НЕ только буквы' + '\n')

    except SyntaxError:
        with open(file_bad_log, 'a', encoding='utf-8') as good_file:
            good_file.write(' '.join(item) + ' - Поле «Имейл» НЕ содержит @ и . (точку)' + '\n')

    except ValueError:
        with open(file_bad_log, 'a', encoding='utf-8') as good_file:
            good_file.write(' '.join(item) + ' - Поле «Возраст» НЕ является числом от 10 до 99' + '\n')



print('\nСодержимое файла {}:'.format(file_bad_log))
with open(file_bad_log, 'r', encoding='utf-8') as bad_file:
    for i in bad_file:
        print(i, end='')

print('\nСодержимое файла {}:'.format(file_good_log))
with open(file_good_log, 'r', encoding='utf-8') as good_file:
    for i in good_file:
        print(i, end='')
