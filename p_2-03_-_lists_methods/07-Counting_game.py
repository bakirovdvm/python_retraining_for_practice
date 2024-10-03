people_quantity = 5
# count = int(input('Какое число вылетает? '))
count = 7
people_list = list(range(1, people_quantity + 1))


start = 0
newStart = 0

for i in range(people_quantity - 1):
   start = newStart % len(people_list)
   newStart = (start + count - 1) % len(people_list)
   print('\nТекущий круг:', people_list)
   print('Начало счета с номера', people_list[start])
   print('Выбывает человек с номером', people_list[newStart])
   people_list.remove(people_list[newStart])

print('Остался один человек победитель:', people_list[0])