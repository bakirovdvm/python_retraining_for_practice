# Вы работаете в компании, занимающейся финансовыми вычислениями.
# Вам необходимо разработать функцию для вычисления квадратного корня числа,
# которая будет использоваться в анализе финансовых данных и расчёте инвестиционных показателей.
# Вы понимаете, что передача отрицательного числа или возникновение других ошибок вычисления могут привести
# к непредсказуемым результатам.
#
# Задача
# Напишите функцию, которая будет:
#
# Вычислять и возвращать квадратный корень полученного числа.
#
# Обрабатывать исключения для отрицательных чисел и других возможных ошибок.
#
# Советы
# При помощи оператора as вы можете сохранить пойманную ошибку в переменную,
# чтобы затем использовать её для получения дополнительной информации:
#
# except Exception as exc:
#     print(exc)
# Старайтесь не смешивать конкретные исключения, которые вы ожидаете, со всеми другими
# (except Exception будет ловить все исключения, которые не были пойманы предыдущими except).


import math


def sq_numb(number):
    """
    Вычисляет и возвращает квадратный корень числа.
    Обрабатывает исключения для отрицательных чисел и других ошибок.
    """
    try:
        number = float(number)
        if number < 0:
            raise ValueError("Квадратный корень из отрицательного числа не определён.")

        return math.sqrt(number)

    except ValueError as ve:
        print(f"Ошибка: {ve}")
    except TypeError as te:
        print(f"Ошибка: Ожидалось число, но получен другой тип. {te}")
    except Exception as exc:
        print(f"Неизвестная ошибка: {exc}")


# Пример использования
num = input("Введите число для вычисления квадратного корня: ")
result = sq_numb(num)
if result is not None:
    print(f"Квадратный корень числа {num} равен {result}")


sq_numb(16)
sq_numb(-16)
sq_numb('abc')
