class Parent:
    def __init__(self, name, age, child_quantity):
        self.name = name
        self.age = age
        self.child_quantity = child_quantity
        self.children_list = []

    def print_info(self):
        print('Меня зовут:', self.name)
        print('Мне {} лет'.format(self.age))
        print('У меня {} детей: {}'.format(len(self.children_list), self.children_list))

    def give_food(self, id_child, action):
        self.id_child = id_child
        self.action = action
        for child in range(1, len(self.children_list) + 1):
            if self.id_child == child:
                self.children_list[child-1].state_of_hungry = action
                # self.children_list[child].print_info()

    def give_relax(self, id_child, action):
        self.id_child = id_child
        self.action = action
        for child in range(1, len(self.children_list) + 1):
            if self.id_child == child:
                self.children_list[child-1].state_of_relax = action


class Child:
    state_of_relax_ = {1: 'спокоен ', 0: 'плачет '}
    state_of_hungry_ = {1: 'сыт ', 0: 'голоден '}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.state_of_relax = 0
        self.state_of_hungry = 0

    def print_info(self):
        print('Имя ребенка:', self.name)
        print('Возраст', self.age)
        print('Ребенок спокоен?', Child.state_of_relax_[self.state_of_relax])
        print('Ребенок голоден?', Child.state_of_hungry_[self.state_of_hungry])
        print()


papa = Parent('Папа', 36, 2)


for child in range(1, papa.child_quantity + 1):
    child = Child(input('\nВведите имя {} ребенка: '.format(child)),
                  int(input('Сколько {} ребенку лет? '.format(child))))
    papa.children_list.append(child)


errors = []
for child in range(len(papa.children_list)):
    if (papa.age - 16) <= papa.children_list[child].age:
        errors.append('error')


if 'error' in errors:
    print('\nИнформация о возрасте ребенка не верна! перепроверьте!')
else:
    print('\nПапа кормит и успокаивает своих детей:')
    papa.give_food(1, 1)
    papa.give_relax(1, 1)
    papa.give_food(2, 1)
    papa.give_relax(2, 1)

    for i in papa.children_list:
        i.print_info()


    print('\nПапа кормит и нервирует своих детей:')
    papa.give_food(1, 1)
    papa.give_relax(1, 0)
    papa.give_food(2, 1)
    papa.give_relax(2, 0)

    for child in papa.children_list:
        child.print_info()







