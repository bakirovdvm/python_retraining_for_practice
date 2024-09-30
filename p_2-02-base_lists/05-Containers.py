def containers():
    container_quantity = int(input('Введите количество контейнеров: '))
    containers_list = list()

    for i in range(container_quantity):
        cont = int(input('Введите вес контейнера: '))
        containers_list.append(cont)

    print(f'Список контейнеров: {containers_list}')

    new_count = int(input('Введите вес нового контейнера: '))
    count = 0
    for i in containers_list:
        print(i)
        if i >= new_count:
            count += 1

    print('Номер, который получит новый контейнер:', count + 1)


containers()
