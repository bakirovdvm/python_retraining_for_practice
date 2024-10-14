def count_uppercase_lowercase(stroka):
    upper_b = 0
    lower_b = 0

    for i in stroka:
        if i.isupper():
            upper_b += 1
        elif i.islower():
            lower_b += 1

    print('Количество заглавных букв:', upper_b)
    print('Количество строчных букв:', lower_b)


text = input("Введите строку для анализа: ")

count_uppercase_lowercase(text)

