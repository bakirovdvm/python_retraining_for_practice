def list_merger(list_1, list_2):
    list_1.extend(list_2)
    result_list = sorted(list_1)

    count = 0
    for i in range(len(result_list), 1, -1):
        if result_list[i - 1] == result_list[i - 2]:
            result_list.remove(count)
        count += 1

    # print(result_list)
    return result_list


list_1 = [1, 3, 5, 7, 9]
list_2 = [2, 4, 5, 6, 8, 10]

print('Результат работы:', list_merger(list_1, list_2))
