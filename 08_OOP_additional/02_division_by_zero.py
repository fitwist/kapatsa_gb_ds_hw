# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.

executed = False


class DivisionByZero(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt


while not executed:
    try:
        a = float(input('Введите делимое: '))
        b = float(input('Делитель: '))
        z = a / b
        print(z)
        executed = True
    except ZeroDivisionError as zde:
        print('Делить на ноль нельзя.', ZeroDivisionError)
    except ValueError as ve:
        print('Вы ввели нечисловое значение.', ve)
