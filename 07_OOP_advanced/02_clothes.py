# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H
# + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Clothes:
    def __init__(self, width, height):
        self.V = width
        self.H = height

    def get_coat_area(self):
        print(f'Ткани требуется на пальто: {self.V / 6.5 + 0.5}')

    def get_costume_area(self):
        print(f'Ткани требуется на костюм: {2 * self.H + 0.3}')

    @property
    def get_total_area(self):
        print(f'Всего ткани требуется: {(self.V / 6.5 + 0.5) + (self.H * 2 + 0.3)}')


class Coat(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.cloth_qty = self.V / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.cloth_qty = self.H * 2 + 0.3


jacket = Coat(11, 8)
jacket.get_coat_area()

suit = Costume(13, 10)
suit.get_costume_area()
suit.get_total_area
