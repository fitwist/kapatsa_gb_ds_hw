# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о
# фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: business_entity_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“business_entity_1”: 5000, “business_entity_2”: 3000, “business_entity_3”: 1000}, {“average_profit”:
# 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"business_entity_1": 5000, "business_entity_2": 3000, "business_entity_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json
profits = {}
total_profit = 0
average_profit_dict = {}
lst = []

# Счетчик положительных прибылей для расчета среднего значения
i = 0

with open('07_company_profit.txt', 'r') as file:
    for line in file:
        name, *info = line.split(' ')
        business_entity = info[0]
        revenue = info[1]
        costs = info[2]
        
        # Пополним словарь с названием компании и прибылью
        profit = float(revenue) - float(costs)
        profits.update({name: profit})

        # Добавим положительное значение прибыли ко временной сумме
        if profit >= 0:
            total_profit = total_profit + profit
            i += 1
        else:
            pass

lst.append(profits)

# Вычислим среднюю прибыль
average_profit = total_profit / i
average_profit_dict.update({"average_profit": average_profit})
lst.append(average_profit_dict)

with open('07_company_profit_to_write.json', 'w') as f:
    json.dump(lst, f, indent=4)
