order_quantity = int(input('Введите количество заказов: '))


print('Введите свой заказ в таком формате: Фамилия - пицца - количество ')
orders_list = list()
full_order_dict = dict()
for order in range(order_quantity):
    new_order = input(f'{order + 1} заказ: ').lower().strip().split()
    orders_list.append(new_order)

    if new_order[0] in full_order_dict.keys():

        full_order_dict[new_order[0]].append(
            {new_order[1]:
                 int(new_order[2]) + full_order_dict[new_order[0]].get([new_order[1]])
             }
        )

    else:
        full_order_dict[new_order[0]] = list()


for i_key in full_order_dict.keys():
    print(i_key, full_order_dict[i_key])

