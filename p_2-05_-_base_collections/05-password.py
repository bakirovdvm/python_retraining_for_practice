# new_pass = str(input('Придумайте пароль: '))
while True:

    new_pass = input('Придумайте пароль: ')

    sym_digit = 0
    sym_upper = 0

    for i in new_pass:
        if i.isupper():
            sym_upper += 1
        elif i.isdigit():
            sym_digit += 1

    if sym_digit >= 3 and sym_upper >= 2:
        print('Это надежный пароль!')
        break
    else:
        print('Пароль не надежен!')