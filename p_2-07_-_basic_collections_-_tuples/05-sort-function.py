# Напишите функцию, которая сортирует по возрастанию кортеж,
# состоящий из целых чисел, и возвращает его отсортированным.
# Если хотя бы один элемент не является целым числом, то функция возвращает исходный кортеж.
# Основной код оставьте пустым или закомментированным (используйте его только для тестирования).
# Пример вызова функции:
# tpl = (6, 3, -1, 8, 4, 10, -5)
# print(tpl_sort(tpl))
#
# Ответ в консоли: (-5, -1, 3, 4, 6, 8, 10)

def sortTuple(anyTuple):
    for index, value in enumerate(anyTuple):
        if value % 1 > 0:
            return anyTuple
    return tuple(sorted(list(anyTuple)))

tupleForSort = (6, 3, -1, 8, 4, 10, -5)

print(sortTuple(tupleForSort))
