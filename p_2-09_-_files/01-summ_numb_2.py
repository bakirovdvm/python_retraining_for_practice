import os


file_name = 'numbers.txt'
file_path = os.path.join(file_name)

print(os.path.exists(file_path))

result = 0
# with open(file_path, 'r') as file:
#     for i in file:
#         result += int(i)
#
#     print(result)

file = open(file_path, 'r')
for i in file:
    result += int(i)
file.close()

answer_file = open('answer.txt', 'w')
answer_file.write(str(result))
answer_file.close()



