# r_list = list()
# p_list = list()
r_list = ['41', '40', '39', '42', '42']
p_list = ['42', '41', '42', '42']

result = 0

# r_count = int(input('Введите количество роликов: '))
# for i in range(r_count):
#     para_rolikov = input(f'Введите размер пары {i + 1}: ')
#     r_list.append(para_rolikov)
#
# p_count = int(input('\nВведите количество людей: '))
# for i in range(p_count):
#     razmer_nogi = input(f'Введите размер ноги {i + 1}: ')
#     p_list.append(razmer_nogi)

print(r_list)
print(p_list)

for i in r_list:
    for j in p_list:
        if i == j:
            result += 1
            break

print(result)


