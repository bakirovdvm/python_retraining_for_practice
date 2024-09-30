def gen_list():
    result_list = []
    numb = int(input('Введите число: '))
    for i in range(numb):
        if i % 2 == 0:
            result_list.append(i + 1)

    print(f'Список из нечётных чисел от одного до {numb}: {result_list}')


gen_list()
