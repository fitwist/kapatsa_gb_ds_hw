# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух
# аргументов.


def my_func(first_number, second_number, third_number):
    sequence = [first_number, second_number, third_number]
    sequence.sort(reverse=True)
    return sequence[0] + sequence[1]

print(f'Результат: {my_func(int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(input("Введите третье число: ")))}')
