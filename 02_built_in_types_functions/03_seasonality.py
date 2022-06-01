# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и dict.
month = int(input('Укажите порядковый номер месяца: '))

# СПИСОК
# seasons = ['зима', 'весна', 'лето', 'осень']

#
# if (month >= 0 and month <= 1) or (month == 11):
#     print('Сезон: ', seasons[0])
# elif month >= 2 and month <= 4:
#     print('Сезон: ', seasons[1])
# elif month >= 5 and month <= 7:
#     print('Сезон: ', seasons[2])
# elif month >= 8 and month <= 10:
#     print('Сезон: ', seasons[3])
# else:
#     print('Такого месяца не существует.')

# СЛОВАРЬ
seasons = {
    'зима': [0, 1, 11],
    'весна': [2, 3, 4],
    'лето': [5, 6, 7],
    'осень': [8, 9, 10]
}

for el in seasons:
    if month in seasons[el]:
        print('Сезон:', el)
        break
