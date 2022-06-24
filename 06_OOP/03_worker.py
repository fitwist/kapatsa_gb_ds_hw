# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_
# total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self,  name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'Ф.И.: {self.surname} {self.name}'

    def get_total_income(self):
        return sum(self._income.values())


if __name__ == '__main__':
    person = Position('Алена', 'Иванченко', 'Fullstack-разработчик', 100000, 15000)
    second_person = Position('Иван', 'Смирнов', 'Экспедитор', 70000, 15000)

    print(f'{person.get_full_name()}, {person.position}')
    print(f'Совокупный доход: {person.get_total_income()}\n')

    print(f'{second_person.get_full_name()}, {second_person.position}')
    print(f'Совокупный доход: {second_person.get_total_income()}')
