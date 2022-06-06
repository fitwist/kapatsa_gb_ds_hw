# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
# должен создаваться объект-генератор. Функция вызывается следующим образом: for el in fact(n). Она отвечает за
# получение факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!. Подсказка: факториал
# числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from sys import argv

filename, stop_number = argv  # python 07_yield.py 5


def factorials_up_to(x):
    a = 1
    for i in range(1, int(x) + 1):
        a *= i
        yield a


for x in factorials_up_to(stop_number):
    print(x)