order_quantity = int(input('Введите количество заказов: '))


print('Введите свой заказ в таком формате: Фамилия - пицца - количество ')

full_order_dict = {}

for i in range(order_quantity):
    # new_order = input(f'{order + 1} заказ: ').lower().strip().split()
    new_order = input('Введите {} заказ через пробел: '.format(i + 1)).split()


    if new_order[0] in full_order_dict.keys():

        full_order_dict[new_order[0]].update(
            {new_order[1]: int(new_order[2]) + full_order_dict[new_order[0]].get(new_order[1], 0)
             }
        )

    else:
        full_order_dict[new_order[0]] = {new_order[1]: int(new_order[2])}


for i_key in full_order_dict.keys():
    print(i_key, full_order_dict[i_key])

