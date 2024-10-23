txtStr = list('abcd')
numbs = (10, 20, 30, 40)

print('ZIP:')
print(zip(txtStr, numbs))
for i in zip(txtStr, numbs):
    print(i)


print('\nРезультат:')
print((txtStr[index], value) for index, value in enumerate(numbs))
result = ((txtStr[index], value) for index, value in enumerate(numbs))
for i in result:
    print(i)

