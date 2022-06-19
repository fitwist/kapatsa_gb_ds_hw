# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год
# рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Осуществить
# вывод данных о пользователе одной строкой.

def profiling(first_name, last_name, birth_year, city, email, phone):
    res = 'Имя: ' + first_name + ' ' + last_name + ', год рождения: ' +  str(birth_year) + ', город: ' + city + \
          ', email: ' + email + ', телефон: ' + phone
    print(res)


profiling(first_name='Евгений', last_name='Понасенков', birth_year=1982, city='Москва',
          email='info@ponasenkov.net', phone='+7 (912) 345-67-89')
