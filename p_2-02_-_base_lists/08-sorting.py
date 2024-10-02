def sorting():
    # start_list = [1, 4, -3, 0, 10]
    start_list = [61, 70, 42, 64, 11, 34, 82, 60, 49, 61]
    print(start_list)
    for i in range(len(start_list)):
        for j in range(len(start_list) - i - 1):
            if start_list[j] > start_list[j + 1]:
                start_list[j], start_list[j + 1] = start_list[j + 1], start_list[j]
    print(start_list)

sorting()

