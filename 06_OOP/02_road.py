# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1
# см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    mass = 25

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculate_area(self, thickness):
        return self.mass * self.__width * self.__length * thickness


if __name__ == '__main__':
    autobahn = Road(3940, 50)
    mass = autobahn.calculate_area(12)
    numbers = "{:,}".format(mass)
    print(f"Масса, кг: {numbers}")
