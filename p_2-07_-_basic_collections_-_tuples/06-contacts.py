phonebook = dict()

while True:
    choice = int(input('\nВведите выбор действия:'
                       '\n1 - добавить контакт'
                       '\n2 - найти человека'
                       '\nВаше действие: '))
    if choice == 1:
        name = input('Введите имя и фамилию нового контакта через пробел: ').lower().split()
        if tuple(name) in phonebook:
            print('Ошибка: Такой человек уже есть в контактах!')
        else:
            phone = int(input('Введите номер телефона: '))
            phonebook[(name[0], name[1])] = phone

    elif choice == 2:
        print('ПОИСК ...')
        searchContact = input('Введите фамилию для поиска: ').lower()
        for names, phones in phonebook.items():
            # print(names, phones)
            if searchContact in names[1]:
                print('По вашему запросу есть совпадение:', names, phones)


    # print(name)
    print('Ваши контакты:', phonebook)