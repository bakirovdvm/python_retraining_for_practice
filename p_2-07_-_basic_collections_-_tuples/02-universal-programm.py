def is_prime(numb):
    count = 0
    for i in range(1, numb + 1):
        if numb % i == 0:
            count += 1
    if count < 3 and numb != 1:
        return numb


def crypto(text):
    return [symb for index, symb in enumerate(text) if is_prime(index)]


print(crypto('О Дивный Новый мир!'))
