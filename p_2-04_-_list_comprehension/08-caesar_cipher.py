alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
message = input('Введите текст: ')
shift = int(input('Введите сдвиг: '))

result = [' ' if i == ' ' else alphabet[(alphabet.index(i) + shift) % 33] for i in message]

print('\nРезультат: ', end='')
for i in result:
    print(i, end='')
