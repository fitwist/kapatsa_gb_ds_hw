# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
# окончании ввода данных будет свидетельствовать пустая строка.

strings = []

while True:
    line = input("Введите текст: ")
    if line == '':
        print(strings)
        exit()
    else:
        newline = line + '\n'
        strings.append(newline)

    with open("01_strings.txt", "w") as file_obj:
        file_obj.writelines(strings)
