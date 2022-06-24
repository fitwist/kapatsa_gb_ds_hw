# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса
# (комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.

class ComplexNumber:
    def __init__(self, real, imag=0):
        self.__complex = complex(real, imag)

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            other = other.__complex

        complex_ = self.__complex + other
        return ComplexNumber(complex_.real, int(complex_.imag))

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            other = other.__complex

        complex_ = self.__complex * other
        return ComplexNumber(complex_.real, int(complex_.imag))

    def __str__(self):
        return self.__complex.__str__()


if __name__ == '__main__':
    c1 = ComplexNumber(1, 6)
    c2 = ComplexNumber(5)

    print(c1 + c2, complex(-1, 4) + complex(7))
    print(c1 * c2, complex(3, -5) * complex(8))
