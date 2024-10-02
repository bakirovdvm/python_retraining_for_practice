shop_list = [['каретка', 1200],
        ['шатун', 1000],
        ['седло', 300],
        ['педаль', 100],
        ['седло', 1500],
        ['рама', 12000],
        ['обод', 2000],
        ['шатун', 200],
        ['седло', 2700]]


def shop(my_list):
    detail = str(input('Введите название детали: '))

    quantity = 0
    price = 0
    for i in my_list:
        if detail == i[0]:
            # print('Общая стоимость:', i[1] * quantity)
            price += i[1]
            quantity += 1

        # print(my_list[i][0], my_list[i][1])

    print(f'Количество деталей {quantity}'
          f'\nОбщая стоимость {price}')


shop(shop_list)
