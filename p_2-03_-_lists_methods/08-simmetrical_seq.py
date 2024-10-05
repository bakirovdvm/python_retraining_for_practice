numbers_quantity = int(input('Введите количество чисел: '))
numbers_list = list()

for i in range(numbers_quantity):
    numbers_list.append(int(input('Введите число: ')))

i = 0

# numbers_list = [1, 2, 1, 2, 2]
result_list = list()

while numbers_list != numbers_list[::-1]:
    numbers_list.insert(numbers_quantity, numbers_list[i])
    i += 1

print('Нужно приписать чисел', i)
print('Числа:', numbers_list[:i][::-1])


