def symbs(message):
    txtdict = dict()
    for i in message:
        if i in txtdict:
            txtdict[i] += 1
        else:
            txtdict[i] = 1
    return txtdict


textInput = input('Введите строку: ')

symbsDict = symbs(textInput)

count = 0
result = str()
for i in symbsDict.values():
    # print('i', i)
    if i % 2 != 0:
        count += 1

    if count > 1:
        result = 'ОШИБКА: Неьлзя сделать палиндром!'
        break
    else:
        result = 'Можно сделать палиндром'

print(result)
