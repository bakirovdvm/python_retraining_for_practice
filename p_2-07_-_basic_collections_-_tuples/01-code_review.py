students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}



print('Список пар "ID студента - возраст":',
      [(i_key, i_value['age']) for i_key, i_value in students.items()])

#
# def functi(dict):
#     print([i_value['interests'] for i_key, i_value in students.items()])

def getInfo(stuInfo):
    interests = []
    lenghtSurname = 0
    for id, data in stuInfo.items():
        lenghtSurname += (len(data['surname']))
        interests += data['interests']

    return set(interests), lenghtSurname


getInfo(students)

interestsList, lenghtSurname = getInfo(students)
print('Полный список интересов всех студентов:', interestsList)
print('Общая длина всех фамилий студентов:', lenghtSurname)

# def f(dict):
#     lst = []
#     string = ''
#     for i in dict:
#         lst += (dict[i]['interests'])
#         string += dict[i]['surname']
#     cnt = 0
#     for s in string:
#         cnt += 1
#     return lst, cnt
#
# pairs = []
# for i in students:
#     pairs += (i, students[i]['age'])
# print(pairs)
#
# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)