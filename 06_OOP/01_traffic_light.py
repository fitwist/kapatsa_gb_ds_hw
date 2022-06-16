# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) —
# на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и
# завершать скрипт.

import time


class TrafficLight:
    colors = {'Зеленый': 4,  'Желтый': 2, 'Красный': 7}
    __color = None
    __c_index = 0
    count = int(3)

    def __init__(self, count=3, init_color='Красный'):
        self.__color = init_color if self.colors.get(init_color) else list(self.colors.keys())[self.__c_index]
        self.__c_index = list(self.colors.keys()).index(self.__color)
        self.count = int(count)

    def running(self):
        print(self.__color)
        while self.count:
            time.sleep(self.colors.get(self.__color))
            self.__c_index = (self.__c_index + 1) % 3
            self.__color = list(self.colors.keys())[self.__c_index]
            print(self.__color)
            self.count -= 1


if __name__ == '__main__':
    while True:
        count = input('Сколько раз поменять цвета: ')
        try:
            count = int(count)
            break
        except ValueError as e:
            print('Введите целое число: ')
    lights = TrafficLight(count, 'Желтый')
    lights.running()



