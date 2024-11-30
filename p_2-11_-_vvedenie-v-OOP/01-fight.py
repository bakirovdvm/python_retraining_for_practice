# Вы работаете в команде разработчиков мобильной игры, и вам досталась часть от ТЗ заказчика.

# Есть два юнита, каждый называется «Воин». Каждому устанавливается здоровье в 100 очков.
# Они бьют друг друга в случайном порядке. Тот, кто бьёт, здоровье не теряет.
# У того, кого бьют, оно уменьшается на 20 очков от одного удара.
# После каждого удара надо выводить сообщение, какой юнит атаковал и сколько у противника осталось здоровья.
# Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.
#
# Реализуйте такую программу.
import random


class Unit:
    damage = 20

    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp

    def print_info(self):
        print('Боец {} \nОсталось {} очков здоровья \n'.format(
            self.name, self.hp
        ))


warrior_1 = Unit('Robocop')
warrior_2 = Unit('Terminator')


while True:
    attack = random.randrange(0, 2)
    if attack == 1:
        warrior_2.hp -= 20
        print('Воин {} атакует '.format(warrior_1.name))
        warrior_2.print_info()
    else:
        warrior_1.hp -= 20
        print('Воин {} атакует '.format(warrior_2.name))
        warrior_1.print_info()

    if warrior_1.hp == 0:
        print('{} победил!'.format(warrior_2.name))
        break
    elif warrior_2.hp == 0:
        print('{} победил!'.format(warrior_1.name))
        break

