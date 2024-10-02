def cinemas():
    films_list = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов',
              'Мементо', 'Отступники', 'Деревня']
    result_list = list()

    films_quantity = int(input('Сколько фильмов хотите добавить?'))

    for i in range(films_quantity):
        film = str(input('Введите название фильма: '))
        if film in films_list:
            result_list.append(film)
        else:
            print(f'Ошибка! Фильма {film} у нас нет ...')

    print(f'Ваш список любимых фильмов: {result_list}')


cinemas()

