# Содержимое файла second_tour.txt:
# 2
# 1) V. Petrov 98
# 2) P. Sergeev 92

import os

file = open('first_tour.txt', 'r', encoding='utf-8')

data = list()
for item in file:
    # print(item, end='')
    data.append(item.replace('\n', '').split())

file.close()

print('data:', data)

result_list = list()
count = 0
for item in range(1, len(data)):
    info = str()

    if int(data[0][0]) < int(data[item][2]):
        info = f'{data[item][1][:1]}. {data[item][0]} {data[item][2]}'
        result_list.append(info)

print('\nresult_list'.upper(), result_list)

list_for_sort = list()
for i in range(len(result_list)):
    # print(result_list[i].split())
    list_for_sort.append(result_list[i].split())

list_sorted = sorted(list_for_sort, key=lambda winner:int(winner[2]), reverse=True)
# print(list_sorted)

result = list()
result.append(0)

for item in list_sorted:
    result.append(item)

result[0] = len(list_sorted)
# print(result)

result_file = open('second_tour.txt', 'w', encoding='utf-8')
for i in result:
    data = f'{str(i)}\n'
    result_file.write(data)
result_file.close()

result_data = open('second_tour.txt', 'r', encoding='utf-8')
print('\nСодержимое файла second_tour.txt:')
for item in result_data:
    print(item, end='')
result_data.close()