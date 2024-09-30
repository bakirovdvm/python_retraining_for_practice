def f_summ(number):
    result = 0
    for i in str(number):
        result += int(i)

    print('result:', result)
    return result


def f_max(number):
    result = 0
    for i in str(number):
        if int(i) >= result:
            result = int(i)
    print(result)


def f_min(number):
    result = int(str(number)[0])
    for i in str(number):
        if int(i) <= result:
            result = int(i)
    print(result)


def upg_calc():
    numb = int(input('Введите число: '))

    print('доступные действия:\n'
          '1. сумма цифр\n'
          '2. найти максимальное число\n'
          '3. найти минимальное чеисло\n')

    action = int(input('Введите действие: '))

    if action == 1:
        print('1111')
        f_summ(numb)
    elif action == 2:
        f_max(numb)
    elif action == 3:
        f_min(numb)

    print('')
    upg_calc()


upg_calc()
