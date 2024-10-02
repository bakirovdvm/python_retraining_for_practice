def sorting(any_list):
    for i in range(len(any_list)):
        for j in range(len(any_list) - i - 1):
            if any_list[j] < any_list[j + 1]:
                any_list[j], any_list[j + 1] = any_list[j + 1], any_list[j]

    return any_list


def reverse_numbers():
    any_list = [1, 2, 3, 4, 5]

    for i in range(len(any_list)-1, -1, -1):
        # print(i, any_list[i])
        if any_list[i] % 2 != 0:
            any_list.remove(any_list[i])

    # print('any_list', any_list)
    # print('sorting(any_list)', sorting(any_list))
    return sorting(any_list)


print(reverse_numbers())
