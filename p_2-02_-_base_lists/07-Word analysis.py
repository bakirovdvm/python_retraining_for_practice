def palindrome():
    # word = 'мадам'
    word = 'abccba'
    result = 0

    for i in range(len(word) // 2):
        if word[i] == word[len(word) - i - 1]:
            result = 1
            continue
        else:
            print(f'Слово "{word}" = НЕ ПАЛИНДРОМ!')
            break

    if result == 1:
        print(f'Слово "{word}" является ПАЛИНДРОМ')


palindrome()
