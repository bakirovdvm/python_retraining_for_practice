# # words_quantity = int(input('Введите количество пар слов: '))
# #
# # synonym_dict = dict()
# #
# # for i in range(words_quantity):
# #     word = str(input('Введите пару синонимов через "-": ')).split('-')
# #     synonym_dict[word[0].strip()] = word[1].strip()
# #
# # print(synonym_dict)
# #
# synonym_dict = {
#     'Привет': 'Здравствуйте',
#     'Печально': 'Грустно',
#     'Весело': 'Радостно'
# }
#
# print(synonym_dict)
#
# word = str(input('Введите слово: '))
# success_flag = 0
# for i_key in synonym_dict.keys():
#     if word == i_key:
#         print('Синоним =', synonym_dict[i_key])
#         break
#     elif word == synonym_dict[i_key]:
#         print('Синоним =', i_key)
#         break
#     else:
#         success_flag += 1
#
# if success_flag >= len(synonym_dict):
#     print('Такого слова в словаре нет.')


def get_key(dictionary, searchWord):
    for keyD, valueD in dictionary.items():
        if valueD == searchWord:
            return keyD


n = int(input('Введите количество пар слов: '))
dictionary = dict()


for i in range(n):
    word = input('Введите {} пару слов через пробел: '.format(i + 1)).lower().split()
    # print(word)
    dictionary[word[0]] = word[1]

# print(dictionary)


searchWord = input('Введите слово: ').lower()


if dictionary.get(searchWord):
    print('Синоним:', dictionary.get(searchWord))
elif searchWord in dictionary.values():
    print('Синоним:',get_key(dictionary, searchWord))
else:
    print('Такого слова нет в нашем словаре')
