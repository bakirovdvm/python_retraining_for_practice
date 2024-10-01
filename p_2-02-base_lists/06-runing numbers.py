def runing_numbs():
    # shift = 1
    # original_list = [1, 2, 3, 4, 5]
    shift = 3
    original_list = [1, 4, -3, 0, 10]
    print('начальный список:', original_list)

    result_list = original_list[-shift:] + original_list[:-shift]

    print('результат сдвига:', result_list)


runing_numbs()
