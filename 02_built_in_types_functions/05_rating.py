# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает. У
# пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать сразу в коде, например, my_rating = [7, 5, 3, 3, 2].

my_rating = [7, 5, 3, 3, 2]
print(my_rating)

digit = int(input("Введите число (200, чтобы выйти): "))
while digit != 200:
    for el in range(len(my_rating)):
        if my_rating[el] == digit:
            my_rating.insert(el + 1, digit)
            break
        elif my_rating[0] < digit:
            my_rating.insert(0, digit)
            break
        elif my_rating[-1] > digit:
            my_rating.append(digit)
            break
        elif my_rating[el] > digit and my_rating[el + 1] < digit:
            my_rating.insert(el + 1, digit)
            break
    print(f"текущий список - {my_rating}")
    digit = int(input("Введите число (200, чтобы выйти): "))
