def videocards():
    old_card_list = [3070, 2060, 3090, 3070, 3090]
    old_card_list = list(old_card_list)
    new_list = list()

    print(f'Старый список видеокарт: {old_card_list}')
    for i in old_card_list:
        if i != max(old_card_list):
            new_list.append(i)

    print(f'Новый список видеокарт: {new_list}')

videocards()
