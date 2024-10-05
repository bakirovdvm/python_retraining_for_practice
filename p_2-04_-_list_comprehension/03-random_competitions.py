import random

result1 = [round(random.uniform(5, 10), 2) for i in range(20)]
result2 = [round(random.uniform(5, 10), 2) for i in range(20)]
print('Первая команда:', result1)
print('Вторая команда:', result2)
result = [max(result1[i], result2[i]) for i in range(20)]
print('Победители тура:', result)
