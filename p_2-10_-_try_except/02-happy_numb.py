import random
file_name = 'out_file.txt'
rand_numb = random.randrange(1, 13)
print(rand_numb)
error = 0

with open(file_name, 'a', encoding='utf-8') as file:
    numb_summ = 0
    while True:
        error += 1
        numb = int(input('Введите число: '))
        try:
            if error == rand_numb:
                raise BaseException
        except BaseException:
            print('Вас постигла неудача')
            break

        file.write(str(numb) + '\n')

        numb_summ += numb
        if numb_summ >= 777:
            print('Вы успешно выполнили условие для выхода из порочного цикла!')
            break

print(f'Содержание файла: {file_name}')
with open(file_name, 'r', encoding='utf-8') as file:
    for item in file:
        print(item, end='')