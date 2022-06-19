# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие
# лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий. Необязательно,
# чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import json
import re

discipline_names = []
discipline_total_scores = []

with open('06_disciplines.txt', 'r', encoding='utf8') as disciplines:

    lines = 0
    for line in disciplines:
        lines += line.count("\n")

        # Выделим количества занятий по каждому предмету
        discipline_score = re.findall('\d+', line)
        discipline_sum = sum(map(float, discipline_score))
        discipline_total_scores.append(int(discipline_sum))

        # Выделим названия предметов
        discipline_name = line.split(':', 1)
        discipline_names.append(discipline_name[0])

        # Превратим полученные объекты в словарь
        zip_iterator = zip(discipline_names, discipline_total_scores)


dict = dict(zip_iterator)
print(json.dumps(dict, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': ')))
