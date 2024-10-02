def scary_code():
    a = [1, 5, 3]
    b = [1, 5, 1, 5]
    c = [1, 3, 1, 5, 3, 3]
    # print(a)
    a.extend(b)
    # print(a)
    count = 0
    for i in a:
        if i == 5:
            a.remove(i)
            count += 1
    print(f'Количество цифр 5 при первом объединении: {count}')

    a.extend(c)
    count = 0
    for i in a:
        if i == 3:
            count += 1
    print(f'Количество цифр 3 при первом объединении: {count}')
    print('Итоговый список:', a)


scary_code()

