# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Выполните возведение
# числа x в степень y. Задание реализуйте в виде функции my_func(x, y). При решении задания нужно обойтись без
# встроенной функции возведения числа в степень. Подсказка: попробуйте решить задачу двумя способами. Первый —
# возведение в степень с помощью оператора **. Второй — более сложная реализация без оператора **, предусматривающая
# использование цикла.

# ОПЕРАТОР **
# def my_func(x, y):
#     if x < 0:
#         x_new = float(input(f'Внимание! {phrase_x}'))
#         return x_new ** y
#     elif y > 0:
#         y_new = float(input(f'Внимание! {phrase_y}'))
#         return x ** y_new
#     else:
#         return x ** y


# С ИСПОЛЬЗОВАНИЕМ ЦИКЛА
def my_func(x, y):
    res = 1
    i = -1
    while i <= y:
        res *= x
        i -= 1
    return 1 / res


# Тексты запросов в виде строк, чтобы IDE не ругался на длинную строку
phrase_x = 'Введите действительное положительное число – основание степени: '
phrase_y = 'Введите целое отрицательное число – показатель степени: '

print(f'Результат: {my_func(float(input(f"{phrase_x}")), int(input(f"{phrase_y}")))}')

