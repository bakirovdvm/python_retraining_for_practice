# Содержимое файла second_tour.txt:
# 2
# 1) V. Petrov 98
# 2) P. Sergeev 92

import os

file = open('first_tour.txt', 'r', encoding='utf-8')

data = list()
for item in file:
    print(item, end='')
    data.append(item.replace('\n', '').split())

file.close()
print()
print(data)

result_file = open('second_tour.txt', 'w')
count = 0
for item in range(1, len(data)):
    info = str()
    if int(data[0][0]) < int(data[item][2]):
        info = f'{data[item][1][:1]}. {data[item][0]} {data[item][2]}\n'
        result_file.write(info)
        count += 1

result_file.write(count)
result_file.close()

result = open('second_tour.txt', 'r', encoding='utf-8')
for i in result:
    print(i, end='')