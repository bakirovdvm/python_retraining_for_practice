glasnye_b_list = ['а', 'е', 'и', 'о', 'у', 'ы', 'ю', 'я']

text = str(input('Введите текст: '))

result = [i for i in text if i in glasnye_b_list]


print('Список гласных букв:', result)
print('Длина списка: ', len(result))
