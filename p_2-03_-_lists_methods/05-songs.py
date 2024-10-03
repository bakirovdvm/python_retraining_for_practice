violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

songs_quantity = int(input('Сколько песен выбрать? '))

total_duration = 0

for i in range(songs_quantity):
    songs_name = input(f'Название {i + 1} песни: ')
    for j in violator_songs:
        # print(j)
        if songs_name == j[0]:
            total_duration += j[1]
            # print(total_duration, j[1])
# print(violator_songs[i][0], violator_songs[i][1])

print('Общее время звучания песен:', round(total_duration, 2))