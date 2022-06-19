# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10
# строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить
# подсчёт средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

low_salary_workers = []
salary_lst = []

with open('03_salaries.txt', 'r') as workers:
    lines = 0
    i = 0
    for line in workers:
        lines += line.count("\n")
        lst = line.split(' ', 1)
        if float(lst[1]) < 20000.00:
            low_salary_workers.append(lst[0])

        salary_lst.append(float(lst[1]))
        i += 1

avg_salary = sum(map(float, salary_lst)) / len(salary_lst)
print(f'Оклад меньше 20.000 у следующих сотрудников: {low_salary_workers}. \nСредний оклад: {avg_salary}')
