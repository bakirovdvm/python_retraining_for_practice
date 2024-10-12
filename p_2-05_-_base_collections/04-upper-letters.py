any_text = 'Кажется, я забыл выключить утюг'

result_list = any_text.split()

print(result_list)
result = list()

for word in result_list:
    for i in word:
        word = word.replace(i, i.upper())
        break
    print(word)
    result.append(word)

print(' '.join(result))

