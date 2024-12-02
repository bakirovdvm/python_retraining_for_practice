class Student:
    def __init__(self):
        self.full_name = ''
        self.group_number = 0
        self.academic_performance = []

    def add_data(self):
        self.full_name = input('\nВведите ФИО: ')
        self.group_number = int(input('Введите номер группы: '))
        print('Введите данные своей успевамеости:')
        self.academic_performance = [
            input('Через пробел - предмет и оценка: ').split() for i in range(5)
        ]
        return self.full_name, self.group_number, self.academic_performance

    def print_info(self):
        print('ФИО:', self.full_name)
        print('Номер вашей группы: ', self.group_number)
        print('Ваша успеваемость: ', self.academic_performance)

    # def print_average(self):
    #     print('Средний бал вашей успеваемости: ', self.give_average())

    def give_average(self):
        summ_average = 0
        for i in self.academic_performance:
            summ_average += int(i[1])
        average = summ_average / len(self.academic_performance)
        return average

# data = [
#     ['Вася Попов', 33, ['Алгебра 5', 'Информатика 5', 'История 4', 'английский язык 5', 'Философия 4']],
#     ['Мади Турлов', 34, ['Алгебра 4', 'Информатика 4', 'История 4', 'английский язык 3', 'Философия 3']],
#     ['Камила Омарова', 33, ['Алгебра 5', 'Информатика 5', 'История 5', 'английский язык 4', 'Философия 3']],
#     ['Алина Сумкина', 37, ['Алгебра 3', 'Информатика 3', 'История 5', 'английский язык 5', 'Философия 5']],
#     ['Арман Каримов', 34, ['Алгебра 5', 'Информатика 4', 'История 3', 'английский язык 3', 'Философия 3']],
#     ['Тимур Амиров', 33, ['Алгебра 5', 'Информатика 5', 'История 2', 'английский язык 3', 'Философия 3']],
#     ['Андрей Бочка', 34, ['Алгебра 3', 'Информатика 3', 'История 3', 'английский язык 4', 'Философия 3']],
#     ['Галина Сурикова', 33, ['Алгебра 4', 'Информатика 3', 'История 3', 'английский язык 3', 'Философия 3']],
#     ['Мадина Торехан', 34, ['Алгебра 5', 'Информатика 5', 'История 3', 'английский язык 5', 'Философия 3']],
#     ['Сабина Ахметова', 33, ['Алгебра 4', 'Информатика 4', 'История 3', 'английский язык 5', 'Философия 5']]
# ]


student = Student()

students_list = []
students_dict = dict()
for i in range(10):
    i = Student()
    i.add_data()
    dataList = [i.give_average(), i]
    students_list.append(dataList)


for i in sorted(students_list):
    print('Свредний балл вашей успеваемости:', i[1].give_average())
    i[1].print_info()
    print('\n')



