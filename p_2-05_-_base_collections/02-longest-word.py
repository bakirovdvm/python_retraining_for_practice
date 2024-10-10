stroka = 'я есть самаясамая большая строка в этом тексте'
stroka_list = stroka.split()
print('stroka_list', stroka_list)

count = 0
result = ''
for word in stroka_list:

    if len(word) > count:
        count = len(word)
        result = word

print('Самое длинное слово:', result)
print('Длина слова:', len(result))