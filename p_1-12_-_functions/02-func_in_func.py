def positive():
    print('Число положительное!\n')


def negative():
    print('Число отрицательное!\n')


def test():
    numb = int(input('Введите целое число: '))

    if numb > 0:
        positive()
        test()
    elif numb < 0:
        negative()
        test()


test()
