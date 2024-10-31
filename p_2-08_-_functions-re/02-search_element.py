site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def depth(struct, level=1):
    if not isinstance(struct, dict) or not struct:
        return level
    return max(depth(struct[k], level + 1) for k in struct)


def searchItem(struct, userKey, d):
    while d > 0:
 
        if userKey in struct:
            # print('struct[userKey]', struct[userKey])
            return struct[userKey]

        for subStuct in struct.values():
            if isinstance(subStuct, dict):
                result = searchItem(subStuct, userKey, d - 1)
                if result:
                    break
        else:
            result = None

        return result


userKey = input('Введите название ключа: ')
question = input('Хотите ввести максимальную глубину? Y/N: ').lower()
# deep = int(input('Введите максимальную глубину: '))
# value = searchItem(site, userKey, deep)

if question == 'n':
    deep = depth(site)
    # print(deep)
    value = searchItem(site, userKey, deep)
elif question == 'y':
    deep = int(input('Введите максимальную глубину: '))
    value = searchItem(site, userKey, deep)


print()
print('результат:'.upper())

if value:
    print('Значение ключа:', value)
elif value == None:
    print('Значение ключа:', value)

