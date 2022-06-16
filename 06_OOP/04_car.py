# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn
# (direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите
# методы и покажите результат.

import random

class Car:
    __speed = 0
    __direction = None

    def __init__(self, speed, color, name, is_police=False):
        self.__speed = speed
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        self.speed = self.__speed

    def stop(self):
        self.speed = 0
        print('-' * 100)

    def turn(self):
        sample_set = {'назад', 'налево', 'направо'}
        item = random.choice(tuple(sample_set))
        self.direction = item
        print(f'{self.name} повернул {self.direction}.')

    def show_speed(self):
        print(f'Скорость {self.name}: {self.speed}км/ч')


class TownCar(Car):
    max_speed = 60

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > self.max_speed:
            print(f'{self.name} превышает скорость.')
        print(f'Скорость {self.name}: {self.speed} км/ч')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    max_speed = 40

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > self.max_speed:
            print(f'{self.name} превышает скорость.')
        print(f'Скорость {self.name}: {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


if __name__ == '__main__':
    towney = PoliceCar(90, 'Черный', 'Barney')
    workey = WorkCar(105, 'Белый', 'Coat')
    sportey = SportCar(70, 'Синий', 'Eagle')

    print(f'\nКодовое имя: {towney.name}')
    print(f'Цвет: {towney.color}')
    towney.show_speed()
    towney.go()
    towney.show_speed()
    towney.turn()
    towney.go()
    towney.stop()

    print(f'Кодовое имя: {workey.name}')
    print(f'Цвет: {workey.color}')
    workey.show_speed()
    workey.go()
    workey.show_speed()
    workey.go()
    workey.stop()

    print(f'Кодовое имя: {sportey.name}')
    print(f'Цвет: {sportey.color}')
    sportey.show_speed()
    sportey.go()
    sportey.show_speed()
    sportey.turn()
    sportey.go()
    sportey.stop()
