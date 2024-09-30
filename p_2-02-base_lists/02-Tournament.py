def tournament():
    name_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
    result_list = list()
    for i in range(len(name_list)):
        if i % 2 == 0:
            result_list.append(name_list[i])

    print(f'Первый день: {result_list}')


tournament()
