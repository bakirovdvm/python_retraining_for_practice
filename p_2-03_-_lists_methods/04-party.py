guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
max_guests = 6

while True:
    print(f'\nСейчас на вечеринке {len(guests)} человек: {guests}')
    new_guest = input('Гость пришел или ушел? ')

    if new_guest == 'пришел':
        guests_name = input('напишите имя гостя: ')
        if len(guests) == 6:
            print(f'Прости {guests_name}, но мест нет')
        else:
            guests.append(guests_name)
            print(f'Привет, {guests_name}')

    elif new_guest == 'ушел':
        guests_name = input('напишите имя гостя: ')
        guests.remove(guests_name)
        print(f'Пока, {guests_name}')

    elif new_guest == 'пора спать':
        print('Вечеринка закончилась, всем спать!')
        break

    else:
        print('Ошибка ввода')
