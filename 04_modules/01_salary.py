# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника. Используйте в
# нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для конкретных значений необходимо
# запускать скрипт с параметрами.

from sys import argv

filename, output, hourly_rate, bonus = argv  # output – выработка в часах

res = (int(output) * int(hourly_rate)) + int(bonus)

print(f"Ваша выплата составит: {res}.")
