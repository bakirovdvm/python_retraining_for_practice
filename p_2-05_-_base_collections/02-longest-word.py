stroka = 'я есть строка'
stroka_list = stroka.split()
result = []
for word in stroka.split():
    count = 0
    for bukva in word:
        count += 1
    result.append(count)
# print(f'Самое длинное слово: {}')

print(result)
print(max(result))