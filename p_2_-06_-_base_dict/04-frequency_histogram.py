my_text = 'здесь что-то написано'

result_dict = dict()
origin_dict = dict()

for i in my_text:
    if i in result_dict:
        result_dict[i] += 1
    else:
        result_dict[i] = 1

print('Оригинальный словарь частот:')
for i in sorted(result_dict.keys()):
    print(i, ':', result_dict[i])


for i in sorted(result_dict.keys()):
    new_list = list()
    if result_dict[i] in origin_dict:
        origin_dict[result_dict[i]].append(i)
    else:
        origin_dict[result_dict[i]] = list()
        origin_dict[result_dict[i]].append(i)

print('\nИнвертированный словарь частот:')
for i in origin_dict.keys():
    print(i, origin_dict[i])
