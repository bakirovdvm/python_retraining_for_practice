def count_letters():
    word = str(input('Введите текст: '))
    k = int(input('Какую цифру ищем?'))
    n = str(input('Какую букву ищем?'))
    k_result = 0
    n_result = 0

    for i in word.lower():
        if i == str(k):
            k_result += 1
        elif i == n:
            n_result += 1

    print(f'количество букв K = {k_result}\n'
          f'количество букв N = {n_result}')



count_letters()