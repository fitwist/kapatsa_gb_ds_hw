# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-
# год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, dd_mm_yyyy):
        self.dd_mm_yyyy = str(dd_mm_yyyy)

    @classmethod
    def parse_data(cls, dd_mm_yyyy):
        date_lst = []

        for i in dd_mm_yyyy.split():
            if i != '-': 
                date_lst.append(i)

        return int(date_lst[0]), int(date_lst[1]), int(date_lst[2])

    @staticmethod
    def check_validity(day, month, year):

        if 31 >= day >= 1:
            if 1 >= month >= 12:
                if 2022 >= year >= 0:
                    return 'Верная дата.'
                else:
                    return 'Неверно введен год.'
            else:
                return 'Неверно введен месяц.'
        else:
            return 'Неверно введен день.'

    def __str__(self):
        return f'Введенная дата: {Data.parse_data(self.dd_mm_yyyy)}'


today = Data('11 - 1 - 2004')
print(today)

print(Data.check_validity(12, 4, 2007))
print(today.check_validity(11, 17, 2022))
print(Data.parse_data('4 - 12 - 2001'))
