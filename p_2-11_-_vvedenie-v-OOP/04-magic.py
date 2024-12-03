class Water:
    name = 'Вода'
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt
        else:
            return None


class Air:
    name = 'Воздух'
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning
        elif isinstance(other, Earth):
            return Dust
        else:
            return None


class Fire:
    name = 'Огонь'
    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Stone):
            return Metal
        elif isinstance(other, Air):
            return Lightning
        else:
            return None

class Storm:
    name = 'Шторм'
    def __add__(self, other):
        if isinstance(other, Air):
            return Lava()

class Earth:
    name = 'Земля'


class Metal:
    name = 'Металл'

class Stone:
    name = 'Камень'

class Lava:
    name = 'Лава'

class Dust:
    name = 'Пыль'

class Lightning:
    name = 'Молния'

class Dirt:
    name = 'Грязь'

class Steam:
    name = 'Пар'





aWater = Water()
aAir = Air()
result = aWater + aAir
print('{} + {} = {}'.format(aWater.name, aAir.name, result.name))

bStone = Stone()
bFire = Fire()
result = bFire + bStone
print('{} + {} = {}'.format(bFire.name, bStone.name, result.name))


cAir = Air()
cFire = Fire()
result = cAir + cFire
print('{} + {} = {}'.format(cFire.name, cAir.name, result.name))


cAir = Air()
cFire = Fire()
result = cFire + cAir
print('{} + {} = {}'.format(cFire.name, cAir.name, result.name))


dAir = Air()
dStorm = Storm()
result = dAir + dStorm
if result == None:
    print(result)
else:
    print('{} + {}'.format(dAir.name, dStorm.name, result.name))
