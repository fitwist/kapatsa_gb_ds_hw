# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти чётные
# числа от 100 до 1000 (включая границы). Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

lst = [el for el in range(99, 999) if el % 2 == 0]


def select_even(prev_el, el):
    return prev_el * el


new_lst = [reduce(select_even, lst)]
print(new_lst)
