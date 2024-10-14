# Пример 1
# Первая строка: abcd.
# Вторая строка: cdab.
# Первая строка получается из второй со сдвигом 2.
#
# Пример 2
# Первая строка: abcd.
# Вторая строка: cdba.
# Первую строку нельзя получить из второй с помощью циклического сдвига.


first_str = str(input('Первая строка: '))
second_str = str(input('Вторая строка: '))
success_flag = 0

if len(first_str) == len(second_str):

    for shift in range(len(first_str)):
        new_str = list()
        for i in range(len(first_str)):
            new_str.append(first_str[(i + shift) % len(first_str)])
        if ''.join(new_str) == second_str:
            print('Первая строчка получается из второй при сдвиге:', i)
            success_flag += 1

    if success_flag == 0:
        print('Первая строка не может получится из второй')

else:
    print('Количество символов в первой и второй строке не совпадают')