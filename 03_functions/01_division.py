# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.

def division(dividend, divider):
    try:
        return dividend / divider
    except ZeroDivisionError:
        print("Деление на ноль невозможно")
        new_divider = int(input('Введите делитель: '))
        return dividend / new_divider


print(division(int(input("Введите делимое: ")), int(input("Введите делитель: "))))
