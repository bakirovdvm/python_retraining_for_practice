violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
    }

songs_quality = int(input('Сколько песен выбрать? '))
result = 0

for i_song in range(songs_quality):
    song = str(input(f'Название {i_song + 1} песни: '))
    result += violator_songs[song]

print(round(result, 2))