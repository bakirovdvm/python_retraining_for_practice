# Напишите программу, которая инициализирует список из 10 случайных целых чисел,
# а затем делит эти числа на пары кортежей внутри списка. Выведите результат на экран.
# Дополнительно: решите задачу несколькими способами.
# Пример:
#
# Оригинальный список: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Новый список: [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]


import random


randomList = [random.randint(0, 50) for i in range(10)]
print('randomList =', randomList)


print('Вариант 1:', [(randomList[i], randomList[i+1]) for i in range(0, len(randomList), 2)])
print('Вариант 1:', [(randomList[i_key], randomList[i_key + 1])
                     for i_key, i_value in enumerate(randomList) if i_key % 2 == 0])




