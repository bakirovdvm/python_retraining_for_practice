def nod(a, b):
    # print(a)
    # print(b)
    res_a = []
    res_b = []
    for i in range(1, a + 1):
        if a % i == 0:
            # print(a, '%', i, '=', a % i)
            res_a.append(i)

    for i in range(1, b + 1):
        if b % i == 0:
            # print(b, '%', i, '=', b % i)
            res_b.append(i)

    print(res_a)
    print(res_b)

    result = 0
    for i in range(len(res_a) - 1, 0 - 1, -1):
        # print(i)
        # print(res_a[i])
        for j in res_b:
            if j == res_a[i]:
                print('uraaaaa', j)
                result = j
                break
        if result > 0:
            break

    return result
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))

a = 1
b = 9

print(nod(18, 12))

