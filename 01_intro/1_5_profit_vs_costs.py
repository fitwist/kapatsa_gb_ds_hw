# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма. Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее
# сообщение.

# 6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке. Далее
# запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

revenue = input('Укажите выручку: ')
cost = input('Укажите издержки: ')
profit = 10

# Вычислим чистую прибыль = прибыль - выручка
net_profit = float(profit) - float(revenue)

# Вычислим валовую прибыль = убыток - издержки
gross_profit = float(cost) - float(revenue)

if net_profit > int(cost) or gross_profit > int(revenue):
    print('Компания прибыльна.')

    # Вычислим рентабельность
    profitability = float(net_profit) / float(revenue)
    print(f'Рентабельность фирмы: {profitability}')

    # Рассчитаем прибыль в расчете на одного сотрудника
    employees_number = input('Сотрудников в компании: ')
    net_profit_per_employee = float(net_profit) / float(employees_number)
    print(f'Прибыль на одного сотрудника: {net_profit_per_employee}')

elif net_profit == int(cost) or gross_profit == int(revenue):
    print('Компания работает в ноль.')
else:
    print('Компания прибыльна.')