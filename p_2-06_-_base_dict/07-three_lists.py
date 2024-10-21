array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]


print(set(array_1).union(array_2).union(array_3))
print(set(array_1).intersection(array_2).intersection(array_3))
print(set(array_1).difference(array_2).difference(array_3))