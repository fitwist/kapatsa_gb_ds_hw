# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В
# базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а
# также других данных, можно использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

import datetime


class Warehouse:
    def __init__(self, address, high, area):
        self.address = address
        self.max_high = high
        self.area = area


class Equipment:
    __instances = {}

    def __init__(self, model, power, paper_formats):
        self.model = model
        self.power = power
        self.paper_formats = paper_formats
        invent_code = len(Equipment.__instances) + 1
        self.__inventory_id = invent_code
        Equipment.__instances[invent_code] = self

    def __str__(self):
        return f'Модель: {self.model}. ID: {self.get_id()}. Мощность: {self.power}. Поддерживает форматы: {self.paper_formats}'

    def get_id(self):
        return self.__inventory_id

    @classmethod
    def get_by_inv(cls, inv):
        return cls.__instances[inv]


class BalanceException(Exception):

    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt


class Balance:
    __instance = None
    __balance = {}

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, Balance):
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, warehouse = None):
        self.__warehouse = None
        if warehouse is not None:
            self.use(warehouse)

    def use(self, warehouse):
        self.__warehouse = warehouse
        if not (warehouse in self.__balance.keys()):
            self.__balance[warehouse] = []

    def income(self, equipment):
        self.__balance[self.__warehouse].append(equipment)

    def outcome(self, equipment):
        if not (equipment in self.__balance[self.__warehouse]):
            raise BalanceException(f'Оборудование не числится на балансе текущего склада ({self.__warehouse.address})')
        self.__balance[self.__warehouse].remove(equipment)

    def exchange_to(self, warehouse_to, equipment):
        self.outcome(equipment)
        _warehouse = self.__warehouse
        self.use(warehouse_to)
        self.income(equipment)
        self.use(_warehouse)

    def report(self):
        return f'Отчет за ({datetime.datetime.now()})\n' + f'\n'.join(
            f'{key.address} ({len(value)}):' + f'\n\t' + f'\n\t'.join(map(str, value))
            for key, value in self.__balance.items()
        )

    def __str__(self):
        return self.report()


class Printer(Equipment):

    def __init__(self, model, power, paper_formats, colors, velocity):
        super().__init__(model, power, paper_formats)
        self.colors = colors
        self.velocity = velocity


class Scanner(Equipment):

    def __init__(self, model, power, paper_formats, quality):
        super().__init__(model, power, paper_formats)
        self.quality = quality


class Copier(Equipment):

    def __init__(self, model, power, paper_formats, colors):
        super().__init__(model, power, paper_formats)
        self.colors = colors


if __name__ == '__main__':
    p_model = input('Укажите модель принтера: ')

    try:
        p_power = float(input('Мощность: '))
    except ValueError:
        p_power = input('Мощность выражается числом. Пожалуйста, повторите ввод: ')

    p_paper_formats = input('Поддерживаемые форматы: ')
    p_colors = input('Цветовая модель: ')

    try:
        p_velocity = float(input('Скорость печати: '))
    except ValueError:
        p_velocity = input('Скорость печати выражается числом. Пожалуйста, повторите ввод: ')

    p = Printer(p_model, p_power, p_paper_formats, p_colors, p_velocity)

    c_model = input('Укажите модель ксерокса: ')
    try:
        c_power = float(input('Мощность: '))
    except ValueError:
        c_power = input('Мощность выражается числом. Пожалуйста, повторите ввод: ')

    c_paper_formats = input('Поддерживаемые форматы: ')
    c_colors = input('Цветовая модель: ')

    c = Copier('Samsung', 100, ['A1', 'A2'], 'RGB')

    print(f'p ID = {p.get_id()}')
    print(f'c ID = {c.get_id()}')

    d1 = Warehouse('Восток', 3, 500)
    d2 = Warehouse('Север', 10, 1000)

    b = Balance(d1)
    b2 = Balance(d2)

    b.income(p)
    b.income(c)
    print(b.report())
    b.use(d1)
    for _ in range(5):
        b.income(Printer('Canon', 1500, ['a4', 'a5'], 'rgb', 20))
    print(b.report())
    b.use(d2)
    b.outcome(c)
    print(b.report())
    b.exchange_to(d1, p)
    print(b)

    b.use(d1)
    for inv in range(1, 6):
        try:
            b.exchange_to(d2, Equipment.get_by_inv(inv))
        except BalanceException:
            print(f'Товара с ID #{str(Equipment.get_by_inv(inv))} нет на складе!')

    print(b)

    print(b is b2)
