# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны
# заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

rus = {'One': 'Один',
       'Two': 'Два',
       'Three': 'Три',
       'Four': 'Четыре'}

new_file = []
with open('04_numeral.txt', 'r') as eng:
    for i in eng:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + ' ' + i[1])
    print(new_file)

with open('04_numeral_to_write.txt', 'w') as rus:
    rus.writelines(new_file)
