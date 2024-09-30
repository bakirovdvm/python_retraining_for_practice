import random


def rock_paper_scissors():
    # Здесь будет игра «Камень, ножницы, бумага»
    komp_action = random.randrange(1, 4)
    print(komp_action)
    action = int(input('кто вы?'
                       '\n1 - камень'
                       '\n2 - ножницы'
                       '\n3 - бумага'))

    if action == 1 and komp_action == 1:
        print('Ничья!')

    elif action == 1 and komp_action == 2:
        print('Ура! ты победил!')

    elif action == 1 and komp_action == 3:
        print('ты проиграл (')

    if action == 2 and komp_action == 2:
        print('Ничья!')
        rock_paper_scissors()
    elif action == 2 and komp_action == 3:
        print('Ура! ты победил!')
    elif action == 2 and komp_action == 1:
        print('ты проиграл (')

    if action == 3 and komp_action == 3:
        print('Ничья!')
        rock_paper_scissors()
    elif action == 3 and komp_action == 1:
        print('Ура! ты победил!')
    elif action == 3 and komp_action == 2:
        print('ты проиграл (')

    rock_paper_scissors()


def guess_the_number():
    # Здесь будет игра «Угадай число»
    rand_numb = random.randrange(10)

    print('Угадайте загаданное мной число от 0 до 10')
    while True:
        numb = int(input('Введите число:'))
        if numb == rand_numb:
            print('\nУра! вы победили! '
                  '\nзагаданное число:', rand_numb)
            break


def mainMenu():
    # Здесь главное меню игры
    print('Выбирайте игру:\n'
          '1 - камень / ножиницы / бумага\n'
          '2 - угадай число\n')
    game = int(input('напишите номер игры: '))

    if game == 2:
        guess_the_number()
    elif game == 1:
        rock_paper_scissors()


mainMenu()
